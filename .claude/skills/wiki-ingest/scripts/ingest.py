#!/usr/bin/env python3
"""Механическая часть операции Ingest: что уже разобрано и что забыто.

    python ingest.py pending              # сырые материалы без страницы в wiki/sources
    python ingest.py check <slug>         # проверить готовность разбора
    python ingest.py check-new <base>     # то же для страниц, добавленных после base (для CI)
    python ingest.py --self-test

Смысловое (что взять из источника, во что превратить, чему противоречит)
скрипт не умеет — это работа модели, см. SKILL.md.
"""
import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

# Имена файлов из веб-клиппера несут символы вне cp1251 (неразрывный дефис и т.п.),
# на которых печать в консоль Windows падает UnicodeEncodeError.
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[4]
RAW_DIRS = ("web-clipped", "inbox-assistant", "sources")
# Внутри элемента — равноправные варианты одного поля. Страницы июля-августа 2026
# писали `**Источник:**` и `## Связанные страницы`, нынешний шаблон — `**Raw:**` и
# `## Связи`. Смысл поля тот же, поэтому старые страницы не переписываем, а признаём
# оба написания (решение пользователя 2026-08-24). Новые пишутся по шаблону ниже.
REQUIRED_SECTIONS = (
    ("**Дата загрузки:**",),
    ("**Raw:**", "**Источник:**"),
    ("## Связи", "## Связанные страницы"),
)


def covered_text(root):
    """Где материал считается учтённым: страницы источников — разобран,
    log.md — разбор был или было задокументировано решение не разбирать
    (как с архивом закрытой базы знаний 2026-07-28)."""
    src = root / "wiki" / "sources"
    parts = [p.read_text(encoding="utf-8") for p in src.glob("*.md")] if src.is_dir() else []
    log = root / "wiki" / "log.md"
    if log.exists():
        parts.append(log.read_text(encoding="utf-8"))
    return "\n".join(parts)


def pending(root):
    """Сырьё, чьё имя не встречается ни на странице источника, ни в логе.

    ponytail: сверка по имени файла/папки, не по содержимому. Материал,
    упомянутый под другим именем, покажется неразобранным — ложная тревога,
    не пропуск."""
    text = covered_text(root)
    out = []
    for sub in RAW_DIRS:
        d = root / "raw" / sub
        if not d.is_dir():
            continue
        for item in sorted(d.iterdir()):
            if item.name.startswith("."):
                continue
            key = item.stem if item.is_file() else item.name
            if key and key not in text:
                out.append(f"raw/{sub}/{item.name}")
    return out


INBOX = Path("raw") / "inbox-assistant"
OLLAMA_URL = "http://localhost:11434"
EMBED_MODEL = "bge-m3"  # уже стоит в Ollama у ai-assistant, своей модели не заводим
# Замер 2026-10-12 на 55 постах: дословные дубли — 1.00, посты на одну тему — 0.82–0.87,
# соседи по каталогу — 0.78. Подсказка, а не запрет: материал из списка не убирается.
SIMILAR_AT = 0.80


def inbox_posts(root):
    """{путь: (номер поста, нормализованный текст)} по всем постам инбокса, разобранным тоже:
    дубль нового поста обычно лежит среди старых."""
    out = {}
    d = root / INBOX
    for f in sorted(d.glob("*.md")) if d.is_dir() else []:
        raw = f.read_text(encoding="utf-8")
        m = re.search(r"^source: ai-assistant (#\d+)", raw, re.M)
        body = re.sub(r"\A---.*?\n---", "", raw, flags=re.S)
        out[f"{INBOX.as_posix()}/{f.name}"] = (m.group(1) if m else f.name, " ".join(body.lower().split()))
    return out


def exact_duplicates(items, posts):
    """{неразобранный: [номера постов с тем же текстом]}."""
    by_text = {}
    for path, (_, text) in posts.items():
        by_text.setdefault(text, []).append(path)
    return {i: [posts[p][0] for p in by_text[posts[i][1]] if p != i]
            for i in items if i in posts and len(by_text[posts[i][1]]) > 1}


def ollama_embedder(url=OLLAMA_URL, model=EMBED_MODEL):
    """Функция «тексты → векторы», или None, если Ollama не отвечает или модели нет."""
    import json
    import urllib.request
    try:
        with urllib.request.urlopen(f"{url}/api/tags", timeout=2) as r:
            names = [m["name"].split(":")[0] for m in json.load(r)["models"]]
    except Exception:
        return None
    if model not in names:
        return None

    def embed(texts):
        req = urllib.request.Request(f"{url}/api/embed", headers={"Content-Type": "application/json"},
                                     data=json.dumps({"model": model, "input": [t[:4000] for t in texts]}).encode())
        with urllib.request.urlopen(req, timeout=300) as r:
            return json.load(r)["embeddings"]
    return embed


def similar(items, posts, embed, skip):
    """{неразобранный: (номер поста, оценка)} — самый похожий другой пост от SIMILAR_AT.
    skip — дословные дубли, уже показанные отдельно."""
    import math
    paths = list(posts)
    vecs = dict(zip(paths, embed([posts[p][1] for p in paths])))

    def cos(a, b):
        return sum(x * y for x, y in zip(a, b)) / (math.hypot(*a) * math.hypot(*b) or 1)
    out = {}
    for i in items:
        if i not in vecs:
            continue
        cands = [(cos(vecs[i], vecs[p]), p) for p in paths
                 if p != i and posts[p][0] not in skip.get(i, [])]
        if cands:
            score, p = max(cands)
            if score >= SIMILAR_AT:
                out[i] = (posts[p][0], score)
    return out


def check(root, slug, today):
    """today=None — не требовать записи именно за сегодня (в CI страница могла
    приехать коммитом позавчерашнего прогона), достаточно упоминания в логе."""
    page = root / "wiki" / "sources" / f"{slug}.md"
    problems = []
    if not page.exists():
        return [f"нет страницы wiki/sources/{slug}.md"]

    body = page.read_text(encoding="utf-8")
    for variants in REQUIRED_SECTIONS:
        if not any(v in body for v in variants):
            problems.append("на странице нет обязательного поля: " + " / ".join(variants))

    index = (root / "wiki" / "index.md").read_text(encoding="utf-8")
    if f"[[{slug}]]" not in index:
        problems.append("страница не добавлена в wiki/index.md")

    log = (root / "wiki" / "log.md").read_text(encoding="utf-8")
    if today is None:
        if slug not in log:
            problems.append("в wiki/log.md нет записи об этой странице")
    else:
        entry = re.search(rf"^## \[{today}\] ingest \|.*$", log, re.M)
        if not entry:
            problems.append(f"в wiki/log.md нет записи '## [{today}] ingest | ...'")
        elif slug not in log[entry.start():]:
            problems.append("запись в логе есть, но не ссылается на эту страницу")

    linked = [p.name for p in (root / "wiki").rglob("*.md")
              if p.parent.name in ("entities", "concepts") and f"[[{slug}]]" in p.read_text(encoding="utf-8")]
    if not linked:
        problems.append("ни одна страница entities/concepts не ссылается на источник "
                        "— шаги 5-6 Ingest, вероятно, пропущены")
    return problems


def added_sources(base, ref="HEAD", cwd=None):
    """Слаги страниц wiki/sources/, появившихся между base и ref.

    Пустой или нулевой base (первый push ветки) — сравнивать не с чем."""
    if not base or set(base) <= {"0"}:
        return []
    r = subprocess.run(["git", "diff", "--name-only", "--diff-filter=A", base, ref,
                        "--", "wiki/sources"],
                       capture_output=True, text=True, encoding="utf-8", cwd=cwd, check=True)
    return [Path(p).stem for p in r.stdout.split() if p.endswith(".md")]


def self_test():
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        r = Path(tmp)
        (r / "raw" / "web-clipped" / "Статья про X").mkdir(parents=True)
        (r / "raw" / "inbox-assistant").mkdir(parents=True)
        (r / "raw" / "inbox-assistant" / "2026-07-28-новьё.md").write_text("сырьё", encoding="utf-8")
        (r / "wiki" / "sources").mkdir(parents=True)
        (r / "wiki" / "entities").mkdir()
        (r / "wiki" / "sources" / "statya-x.md").write_text(
            "# X\n**Дата загрузки:** 2026-07-29\n**Raw:** `raw/web-clipped/Статья про X/`\n## Связи\n",
            encoding="utf-8")
        (r / "wiki" / "index.md").write_text("- [[statya-x]] — про X\n", encoding="utf-8")
        (r / "wiki" / "log.md").write_text("## [2026-07-29] ingest | X\nразобран [[statya-x]]\n",
                                           encoding="utf-8")
        (r / "wiki" / "entities" / "some-author.md").write_text("[[statya-x]]", encoding="utf-8")

        assert pending(r) == ["raw/inbox-assistant/2026-07-28-новьё.md"], pending(r)

        # Материал без страницы источника, но с решением в логе — не pending.
        (r / "raw" / "sources").mkdir()
        (r / "raw" / "sources" / "архив-чего-то").mkdir()
        (r / "wiki" / "log.md").write_text(
            "## [2026-07-29] ingest | X\nразобран [[statya-x]]\n"
            "## [2026-07-29] project | архив-чего-то ingest не требует\n", encoding="utf-8")
        assert pending(r) == ["raw/inbox-assistant/2026-07-28-новьё.md"], pending(r)
        assert check(r, "statya-x", "2026-07-29") == [], check(r, "statya-x", "2026-07-29")

        (r / "wiki" / "index.md").write_text("пусто\n", encoding="utf-8")
        (r / "wiki" / "entities" / "some-author.md").write_text("нет ссылок", encoding="utf-8")
        got = check(r, "statya-x", "2026-07-29")
        assert any("index.md" in p for p in got) and any("шаги 5-6" in p for p in got), got
        assert check(r, "нет-такого", "2026-07-29")[0].startswith("нет страницы")

        # Старый формат шапки (`**Источник:**` + `## Связанные страницы`) равноправен
        # новому: проверка не должна ронять страницы, написанные до смены шаблона.
        (r / "wiki" / "index.md").write_text("- [[statya-x]] — про X\n", encoding="utf-8")
        (r / "wiki" / "entities" / "some-author.md").write_text("[[statya-x]]", encoding="utf-8")
        (r / "wiki" / "sources" / "statya-x.md").write_text(
            "# X\n**Дата загрузки:** 2026-07-29\n"
            "**Источник:** raw/web-clipped/Статья про X/\n## Связанные страницы\n",
            encoding="utf-8")
        assert check(r, "statya-x", "2026-07-29") == [], check(r, "statya-x", "2026-07-29")
        # А поля нет вовсе — по-прежнему находка.
        (r / "wiki" / "sources" / "statya-x.md").write_text(
            "# X\n**Дата загрузки:** 2026-07-29\n## Связи\n", encoding="utf-8")
        got = check(r, "statya-x", "2026-07-29")
        assert any("**Raw:** / **Источник:**" in p for p in got), got
        (r / "wiki" / "sources" / "statya-x.md").write_text(
            "# X\n**Дата загрузки:** 2026-07-29\n**Raw:** `raw/web-clipped/Статья про X/`\n## Связи\n",
            encoding="utf-8")

        # Режим CI (today=None): дата записи не важна, наличие — важно.
        (r / "wiki" / "index.md").write_text("- [[statya-x]] — про X\n", encoding="utf-8")
        (r / "wiki" / "entities" / "some-author.md").write_text("[[statya-x]]", encoding="utf-8")
        assert check(r, "statya-x", None) == [], check(r, "statya-x", None)
        (r / "wiki" / "log.md").write_text("## [2026-07-29] lint | без нашей страницы\n",
                                           encoding="utf-8")
        assert check(r, "statya-x", None) == ["в wiki/log.md нет записи об этой странице"]

    self_test_added()
    self_test_duplicates()
    print("self-test ok")


def self_test_duplicates():
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        r = Path(tmp)
        d = r / INBOX
        d.mkdir(parents=True)
        post = "---\nsource: ai-assistant #{n}\ncaptured: {c}\n---\n\n# {t}\n\n{t}\n"
        (d / "a.md").write_text(post.format(n=32, c="2026-09-22", t="Мод экономит токены"), encoding="utf-8")
        # Тот же текст с другой шапкой и пробелами — дубль: шапка в сравнение не входит.
        (d / "b.md").write_text(post.format(n=61, c="2026-10-05", t="Мод  экономит токены"), encoding="utf-8")
        (d / "c.md").write_text(post.format(n=62, c="2026-10-07", t="Модель эмбеддингов"), encoding="utf-8")
        posts = inbox_posts(r)
        b, c = f"{INBOX.as_posix()}/b.md", f"{INBOX.as_posix()}/c.md"
        assert exact_duplicates([b, c], posts) == {b: ["#32"]}, exact_duplicates([b, c], posts)

        # Векторы подменены: c ближе к a, чем порог; дубль b для c не в счёт.
        fake = {"мод": [1.0, 0.0], "модель": [0.9, 0.3]}
        embed = lambda texts: [fake["модель"] if "модель" in t else fake["мод"] for t in texts]
        got = similar([c], posts, embed, {})
        assert got[c][0] in ("#32", "#61") and got[c][1] >= SIMILAR_AT, got
        far = lambda texts: [[0.0, 1.0] if "модель" in t else [1.0, 0.0] for t in texts]
        assert similar([c], posts, far, {}) == {}
        # Дубль, показанный отдельно, не повторяется как «похоже».
        got = similar([b], posts, embed, {b: ["#32"]})
        assert got[b][0] == "#62", got

    # Ollama недоступна — не ошибка, а None: разбор идёт дальше.
    assert ollama_embedder("http://127.0.0.1:9") is None


def self_test_added():
    """Сторож, который ничего не находит, выглядит как зелёная сборка."""
    import subprocess as sp
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        r = Path(tmp)
        env = {"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t",
               "GIT_COMMITTER_EMAIL": "t@t", "PATH": __import__("os").environ["PATH"]}
        def git(*a):
            sp.run(["git", *a], cwd=r, check=True, capture_output=True, env=env)
        git("init", "-q")
        (r / "wiki" / "sources").mkdir(parents=True)
        (r / "wiki" / "sources" / "staraya.md").write_text("старая", encoding="utf-8")
        git("add", "-A"); git("commit", "-qm", "первый")
        base = sp.run(["git", "rev-parse", "HEAD"], cwd=r, capture_output=True, text=True,
                      check=True).stdout.strip()

        (r / "wiki" / "sources" / "novaya.md").write_text("новая", encoding="utf-8")
        (r / "wiki" / "sources" / "staraya.md").write_text("старая, дополненная", encoding="utf-8")
        (r / "wiki" / "concepts").mkdir()
        (r / "wiki" / "concepts" / "ne-istochnik.md").write_text("не страница источника", encoding="utf-8")
        git("add", "-A"); git("commit", "-qm", "второй")

        # Только добавленная страница источника: правка старой и новый концепт — мимо.
        assert added_sources(base, cwd=r) == ["novaya"], added_sources(base, cwd=r)
        assert added_sources("0" * 40, cwd=r) == []
        assert added_sources("", cwd=r) == []


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("command", nargs="?", choices=["pending", "check", "check-new"])
    ap.add_argument("slug", nargs="?", help="для check — slug страницы, для check-new — base-коммит")
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        self_test()
        return 0
    root = Path(args.root)

    if args.command == "pending":
        items = pending(root)
        posts = inbox_posts(root)
        dups = exact_duplicates(items, posts)
        embed = ollama_embedder() if any(i in posts for i in items) else None
        try:
            near = similar(items, posts, embed, dups) if embed else {}
        except Exception as e:  # упавшая Ollama не должна задерживать разбор
            embed, near = None, {}
            print(f"(смысловая проверка оборвалась: {e})")
        print(f"Неразобранного сырья: {len(items)}")
        for i in items:
            print(f"  {i}")
            if i in dups:
                print(f"      ↳ дубль {', '.join(dups[i])} — текст совпадает")
            if i in near:
                print(f"      ↳ похоже по смыслу на {near[i][0]} ({near[i][1]:.2f})")
        if not items:
            print("Всё сырьё в raw/ имеет страницу в wiki/sources/.")
        elif any(i in posts for i in items):
            print(f"Смысловая проверка: {EMBED_MODEL}, порог {SIMILAR_AT}" if embed
                  else f"Смысловая проверка пропущена: Ollama не отвечает или нет {EMBED_MODEL}")
        return 0

    if args.command == "check":
        if not args.slug:
            ap.error("check требует slug страницы источника")
        problems = check(root, args.slug, dt.date.today().isoformat())
        if problems:
            print(f"Разбор не закончен ({len(problems)}):")
            for p in problems:
                print(f"  - {p}")
            return 1
        print(f"{args.slug}: страница, индекс, лог и связи на месте.")
        return 0

    if args.command == "check-new":
        slugs = added_sources(args.slug, cwd=str(root))
        if not slugs:
            print("Новых страниц источников в этом push нет.")
            return 0
        bad = 0
        for slug in slugs:
            problems = check(root, slug, None)
            if problems:
                bad += 1
                print(f"РАЗБОР НЕ ЗАКОНЧЕН: {slug}", file=sys.stderr)
                for p in problems:
                    print(f"  - {p}", file=sys.stderr)
            else:
                print(f"{slug}: индекс, лог и связи на месте.")
        if bad:
            print("\nСтраница источника без строки в индексе, записи в логе или обратной\n"
                  "ссылки из entities/concepts — это оборванный разбор: найти её потом\n"
                  "не сможет ни человек, ни следующий прогон.", file=sys.stderr)
            return 1
        return 0

    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
