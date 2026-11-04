#!/usr/bin/env python3
"""Поиск по вики по смыслу (Giga-Embeddings 480M в Ollama) с подсказкой поиска по словам (BM25).

    python poisk.py "запрос"          # 5 ближайших страниц, у каждой — самый близкий раздел
    python poisk.py "запрос" -n 10
    python poisk.py --self-test

Зачем: grep находит слова, а не смысл. «Предел возвратов» и «два раунда доработки» — одно,
но общих слов нет. Перед «в вики этого нет» — сначала сюда.

Порядок задаёт смысл; у каждой страницы — её место по словам, ниже — первые по словам, кого
смысл не показал (редкие имена). Замер 03.11 на 32 эталонах, в пятёрке: слова 17, bge-m3 24,
Giga 25; слияние смысла и слов по местам (RRF) — 24 и сбрасывало верные ответы вниз, поэтому не сливаем.

Страница режется на разделы по заголовкам «## »; оценка страницы — лучший раздел. Векторы
лежат в private/poisk-kesh.json (вне git) и пересчитываются только у изменённых страниц.
"""
import argparse
import hashlib
import json
import math
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ingest import ollama_embedder  # noqa: E402  — один вызов Ollama на оба скрипта

ROOT = Path(__file__).resolve().parents[4]
KESH = ROOT / "private" / "poisk-kesh.json"
SKIP = {"log.md", "index.md", "gaps-backlog.md"}  # журналы и оглавления: совпадут со всем подряд
# Кусок — абзацы раздела до CHUNK знаков. Было 3500 (раздел целиком): 03.11 фраза в одну строку
# внутри длинного раздела тонула, и запрос «сколько раз отправлять на доработку» не нашёл «два возврата».
CHUNK = 1000
NAREZKA = "2"  # версия нарезки — в ключе кэша: сменилась нарезка, векторы пересчитываются
MODEL = "giga-emb-480m"  # GGUF Q8_0 с весов ai-sage/Giga-Embeddings-instruct; модель тоже в ключе кэша
# приставка запроса — по карточке модели; у документа приставки нет
ZAPROS = "Instruct: Given a question, retrieve wiki passages that answer it\nQuery: "


def razdely(text):
    """[(заголовок, текст)] — по «## », внутри раздела абзацы склеиваются в куски до CHUNK знаков."""
    out, title, buf = [], "", []
    for line in text.splitlines():
        if line.startswith("## "):
            if buf:
                out.append((title, "\n".join(buf)))
            title, buf = line[3:].strip(), [line]
        else:
            buf.append(line)
    if buf:
        out.append((title, "\n".join(buf)))
    res = []
    for t, body in out:
        kusok = ""
        for abz in re.split(r"\n\s*\n", body):
            # длинный абзац сам по себе режется по CHUNK, чтобы не превысить предел модели
            for i in range(0, max(len(abz), 1), CHUNK):
                part = abz[i:i + CHUNK].strip()
                if not part:
                    continue
                if kusok and len(kusok) + len(part) > CHUNK:
                    res.append((t, kusok))
                    kusok = ""
                kusok = f"{kusok}\n\n{part}" if kusok else part
        if kusok:
            res.append((t, kusok))
    return res


def stranicy(root):
    return sorted(p for p in (root / "wiki").rglob("*.md") if p.name not in SKIP)


def cos(a, b):
    return sum(x * y for x, y in zip(a, b)) / (math.hypot(*a) * math.hypot(*b) or 1)


def sohranit(kesh):
    KESH.parent.mkdir(exist_ok=True)
    tmp = KESH.with_suffix(".tmp")
    tmp.write_text(json.dumps(kesh, ensure_ascii=False), encoding="utf-8")
    tmp.replace(KESH)  # обрыв посреди записи не портит прежний кэш


def obnovit(root, embed, kesh, save=sohranit):
    """Пересчитать векторы изменённых страниц; удалённые — выкинуть. Возвращает число пересчитанных.
    Кэш пишется каждые 20 страниц: первое построение идёт десятки минут, обрыв не уносит всё."""
    zhivye, n = set(), 0
    for p in stranicy(root):
        key = p.relative_to(root).as_posix()
        zhivye.add(key)
        text = p.read_text(encoding="utf-8")
        h = f"{NAREZKA}:{MODEL}:" + hashlib.sha1(text.encode()).hexdigest()
        if kesh.get(key, {}).get("h") == h:
            continue
        parts = razdely(text)
        vecs = embed([f"{p.stem}. {t}\n{b}" for t, b in parts]) if parts else []
        kesh[key] = {"h": h, "parts": [[t, v] for (t, _), v in zip(parts, vecs)]}
        n += 1
        if n % 20 == 0:
            save(kesh)
            print(f"(пересчитано страниц: {n})", file=sys.stderr, flush=True)
    for k in set(kesh) - zhivye:
        del kesh[k]
    return n


def iskat(kesh, qvec, n=None):
    best = []
    for key, rec in kesh.items():
        if rec["parts"]:
            score, title = max((cos(qvec, v), t) for t, v in rec["parts"])
            best.append((score, key, title))
    return sorted(best, reverse=True)[:n]


def osnovy(text):
    """Основы слов — первые 5 букв слов от 5 букв: грубая замена лемматизации для русского."""
    return [w[:5] for w in re.findall(r"[а-яёa-z]{5,}", text.lower())]


def bm25(docs, zapros):
    """docs: {ключ: [основы]} → [(оценка, ключ)] по убыванию; страницы без общих основ отброшены."""
    N = len(docs)
    avg = sum(map(len, docs.values())) / (N or 1)
    df = {}
    for ws in docs.values():
        for w in set(ws):
            df[w] = df.get(w, 0) + 1
    q = set(osnovy(zapros))
    out = []
    for key, ws in docs.items():
        tf = {}
        for w in ws:
            if w in q:
                tf[w] = tf.get(w, 0) + 1
        s = sum(math.log(1 + (N - df[w] + .5) / (df[w] + .5)) * f * 2.2 / (f + 1.2 * (.25 + .75 * len(ws) / avg))
                for w, f in tf.items())
        if s:
            out.append((s, key))
    return sorted(out, reverse=True)


def self_test():
    # нарезка: два раздела, длинный режется
    parts = razdely("# Заг\nвступление\n## Первый\n" + "а" * (CHUNK + 10) + "\n## Второй\nтекст")
    assert [t for t, _ in parts] == ["", "Первый", "Первый", "Второй"], parts
    # короткие абзацы склеиваются, длинный ряд — делится по границе абзаца, не посреди
    abz = "## Р\n\n" + "\n\n".join(["б" * 400] * 3)
    kuski = [b for _, b in razdely(abz)]
    assert len(kuski) == 2 and all(len(b) <= CHUNK for b in kuski), [len(b) for b in kuski]
    assert kuski[1] == "б" * 400, "второй кусок должен начинаться с целого абзаца"
    # поиск: страница с ближайшим разделом выше, оценка — по лучшему разделу
    kesh = {"a.md": {"h": "", "parts": [["x", [1, 0]], ["y", [0, 1]]]}, "b.md": {"h": "", "parts": [["z", [0.7, 0.7]]]}}
    assert iskat(kesh, [0, 1], 2)[0][1:] == ("a.md", "y")
    assert [k for _, k, _ in iskat(kesh, [1, 1], 2)] == ["b.md", "a.md"]
    # слова: редкое слово весит больше частого, страница без общих основ не попадает
    docs = {"r.md": osnovy("редкий термин гибрид"), "c.md": osnovy("обычный текст"),
            "d.md": osnovy("обычный пример"), "n.md": osnovy("ничего")}
    r = [k for _, k in bm25(docs, "гибрид обычный")]
    assert r[0] == "r.md" and "n.md" not in r and len(r) == 3, r
    print("самопроверка: ок")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("zapros", nargs="?")
    ap.add_argument("-n", type=int, default=5)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not a.zapros:
        ap.error("нужен запрос")
    embed = ollama_embedder(model=MODEL)
    if embed is None:
        sys.exit(f"Ollama не отвечает или нет модели {MODEL} — поиск по смыслу недоступен, остаётся grep.")
    kesh = json.loads(KESH.read_text(encoding="utf-8")) if KESH.exists() else {}
    n = obnovit(ROOT, embed, kesh)
    if n:
        sohranit(kesh)
        print(f"(пересчитано страниц: {n})", file=sys.stderr)
    smysl = {key: title for _, key, title in iskat(kesh, embed([ZAPROS + a.zapros])[0])}
    docs = {p.relative_to(ROOT).as_posix(): osnovy(p.read_text(encoding="utf-8")) for p in stranicy(ROOT)}
    slova = [key for _, key in bm25(docs, a.zapros)]
    mesta_c = {k: i for i, k in enumerate(slova, 1)}
    pokazany = list(smysl)[:a.n]
    for key in pokazany:
        title = smysl[key]
        print(f"слова {mesta_c.get(key, '—'):>3}  {key}" + (f"  § {title}" if title else ""))
    eshche = [k for k in slova[:3] if k not in pokazany]
    if eshche:  # редкие имена и термины слова ловят лучше смысла
        print("по словам ещё: " + ", ".join(eshche))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
