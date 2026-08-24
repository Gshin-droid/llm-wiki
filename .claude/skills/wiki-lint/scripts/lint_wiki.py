#!/usr/bin/env python3
"""Механическая часть Lint этой вики: то, что проверяется без модели.

    python lint_wiki.py                 # отчёт по wiki/
    python lint_wiki.py --json
    python lint_wiki.py --stale-days 45
    python lint_wiki.py --self-test

Проверяет: битые [[wiki-links]], страницы-сироты, страницы вне index.md,
просроченные «Актуально на», повторяющиеся безрезультатные заходы в один
и тот же недоступный домен. Смысловое (противоречия, недостающие страницы,
устаревшие факты) скрипт не умеет — это работа модели.
"""
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

WIKI = Path(__file__).resolve().parents[4] / "wiki"

LINK = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
CODE_SPAN = re.compile(r"`[^`\n]*`")
CODE_BLOCK = re.compile(r"```.*?```", re.S)
ACTUAL = re.compile(r"\*\*Актуально на:?\*\*:?\s*(\d{4}-\d{2}-\d{2})")

# Служебные страницы: не считаются сиротами и не требуют записи в индексе.
SERVICE = {"index", "log", "gaps-backlog"}
# Ссылка-конвенция: файл правил вики, страницы у него нет и не должно быть.
LINK_ALLOWLIST = {"CLAUDE.md"}

# Абсолютные пути к файлам на диске в публичном .claude/settings.json.
# Повод — 2026-08-10: разрешение «всегда разрешать» село в этот файл правилом с
# путём к личному проекту, а `additionalDirectories` уже содержал домашнюю папку
# с именем пользователя. Основной предохранитель — локальный pre-commit, но он в
# репозиторий не уезжает и после нового клона отсутствует; эта проверка ловит то
# же самое постфактум. Правило намеренно про форму пути, а не про конкретные имена:
# имя пользователя в самом скрипте было бы той же утечкой, которую он ищет.
# Буква диска — одна, и перед ней нет других букв: без этого "https://" читается
# как диск "s:" и любая строка с адресом становится ложной находкой (13.08.2026).
DISK_PATH = re.compile(r"(?<![A-Za-z])[A-Za-z]:[\\/]|/home/|/Users/|/c/my_")
SETTINGS = ".claude/settings.json"

# Страницы стареют с разной скоростью, поэтому и порог у них разный (введено
# 2026-08-10 по данным прогона: из 28 просроченных 15 были людьми и каналами,
# где сверка формальна и годами даёт ноль находок — шум приучал не смотреть на
# число вовсе). Тип берём из самой страницы, а не из списка имён в скрипте:
# список имён пришлось бы вести руками, и он бы протухал быстрее страниц.
TYPE = re.compile(r"\*\*Тип:?\*\*:?\s*(.+)")
PERSON_MARKS = ("человек", "автор", "youtube-канал")

# Продукт, помеченный «не используется», из счётчика свежести выпадает совсем
# (решение пользователя 2026-08-24). Смысл счётчика — «версии и цены протухают за
# недели», но актуализировать нечего у того, чем не пользуются: страница описывает
# факт «оценили и не взяли», а он не устаревает. Пометка ставится руками строкой
# `**Статус:** ... не используется ...` — счётчик выключает человек, а не скрипт.
STATUS = re.compile(r"\*\*Статус:?\*\*:?\s*(.+)")
UNUSED_MARK = "не используется"

# Повторяющаяся бесполезная попытка: рутина который день ходит в один и тот же
# недоступный домен, честно записывает неудачу и назавтра заходит снова. Повод —
# 2026-08-18: `EGRESS_BLOCKED` встречался в логе 12 раз, пять прогонов подряд
# ушли в ноль на одном домене. Текстовое правило «не долбиться» уже записано в
# gaps-backlog, но текст — просьба, а не гарантия; ловит только проверка.
# Считаем по РАЗНЫМ датам записей, а не по числу упоминаний: три абзаца про одну
# и ту же неудачу в одном прогоне — это один заход, а не три.
ENTRY_HEAD = re.compile(r"^## \[(\d{4}-\d{2}-\d{2})\]", re.M)
BLOCK_MARK = re.compile(r"EGRESS_BLOCKED|заблокирован|недоступ|не открыл|403", re.I)
DOMAIN = re.compile(r"\b([a-z0-9][a-z0-9-]*(?:\.[a-z0-9-]+)+)\b", re.I)
# Имена файлов ловятся тем же выражением, что и домены: log.md, lint_wiki.py.
# Номера версий и arXiv-идентификаторы — тоже: 2.1.224, 2605.08442. Отсюда же
# отсев чисто числовой «зоны»: доменов с цифровым окончанием не бывает.
NOT_DOMAIN = {"md", "py", "json", "html", "yml", "yaml", "txt", "js", "ts", "jsonl", "ipynb"}
# Запись почти всегда строится через противопоставление: «прокси блокировал
# почти всё, но github.com остался доступен». По строке целиком в находки
# попадает именно тот домен, который открылся, — то есть проверка ругается на
# успех. Поэтому строка режется по противительным союзам, и домены берутся
# только из той части, где стоит признак блокировки.
CONTRAST = re.compile(r",?\s+(?:но|зато|однако|при этом|кроме)\s+|;\s+")
# Сколько знаков между доменом и словом о блокировке ещё считать «рядом».
# ponytail: расстояние в символах, а не разбор предложения; станет шумно — сузить.
NEAR = 90


def kind_of(text):
    """«человек» — авторы, каналы, издания; «продукт» — всё остальное.

    Без пометки «Тип» страница считается продуктом: неизвестное проверяем чаще,
    а не реже."""
    m = TYPE.search(text)
    if m and any(w in m.group(1).lower() for w in PERSON_MARKS):
        return "человек"
    return "продукт"


def strip_code(text):
    """Ссылки внутри кода — цитаты правил, а не связи. Съедаем их до разбора."""
    return CODE_SPAN.sub(" ", CODE_BLOCK.sub(" ", text))


def collect(wiki):
    pages = {}
    for path in sorted(wiki.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        pages[path.stem] = {
            "path": path.relative_to(wiki).as_posix(),
            "links": [m.group(1).strip() for m in LINK.finditer(strip_code(text))],
            "actual": (ACTUAL.search(text) or [None, None])[1],
            "kind": kind_of(text),
            "unused": UNUSED_MARK in (STATUS.search(text) or [None, ""])[1].lower(),
        }
    return pages


def lint(wiki, today, stale_days, people_days=180, stuck_days=3):
    pages = collect(wiki)
    index_text = (wiki / "index.md").read_text(encoding="utf-8") if (wiki / "index.md").exists() else ""
    index_links = {m.group(1).strip() for m in LINK.finditer(strip_code(index_text))}

    broken, incoming = [], {name: 0 for name in pages}
    for name, p in pages.items():
        for target in p["links"]:
            if target in pages:
                incoming[target] += 1
            elif target not in LINK_ALLOWLIST:
                broken.append({"page": p["path"], "target": target})

    orphans = [p["path"] for name, p in pages.items()
               if name not in SERVICE and incoming[name] == 0 and name not in index_links]
    unindexed = [p["path"] for name, p in pages.items()
                 if name not in SERVICE and name not in index_links]

    stale = []
    for name, p in pages.items():
        if not p["actual"] or p["unused"]:
            continue
        limit = people_days if p["kind"] == "человек" else stale_days
        age = (today - dt.date.fromisoformat(p["actual"])).days
        if age > limit:
            stale.append({"page": p["path"], "actual": p["actual"], "age_days": age,
                          "kind": p["kind"], "limit": limit})
    stale.sort(key=lambda s: -s["age_days"])

    paths = disk_paths(wiki.parent)
    stuck = stuck_attempts(wiki, stuck_days)
    return {
        "pages": len(pages),
        "people_days": people_days,
        "broken_links": broken,
        "orphans": orphans,
        "unindexed": unindexed,
        "stale": stale,
        "disk_paths": paths,
        "stuck": stuck,
        "total": (len(broken) + len(orphans) + len(unindexed)
                  + len(stale) + len(paths) + len(stuck)),
    }


def stuck_attempts(wiki, min_days=3):
    """Домены, в которые лог упирается из прогона в прогон без результата.

    Ищем построчно, а не по записи целиком: в одной записи рядом обычно стоят и
    заблокированный домен, и тот, который открылся, — по абзацу их не разделить."""
    log = wiki / "log.md"
    if not log.exists():
        return []

    text = log.read_text(encoding="utf-8")
    heads = list(ENTRY_HEAD.finditer(text))
    seen = {}
    for i, h in enumerate(heads):
        date = h.group(1)
        body = text[h.end(): heads[i + 1].start() if i + 1 < len(heads) else len(text)]
        for line in body.splitlines():
            if not BLOCK_MARK.search(line):
                continue
            for part in CONTRAST.split(line):
                marks = [m.start() for m in BLOCK_MARK.finditer(part)]
                if not marks:
                    continue
                for m in DOMAIN.finditer(part):
                    host = m.group(1).lower()
                    zone = host.rsplit(".", 1)[-1]
                    if zone in NOT_DOMAIN or zone.isdigit():
                        continue
                    # Записи длинные, и в одном предложении часто перечислены и
                    # закрытые домены, и тот, через который в итоге всё получилось.
                    # Засчитываем только домен рядом с самим признаком блокировки.
                    if min(abs(m.start() - k) for k in marks) > NEAR:
                        continue
                    seen.setdefault(host, set()).add(date)

    stuck = [{"host": h, "days": len(d), "dates": sorted(d)}
             for h, d in seen.items() if len(d) >= min_days]
    stuck.sort(key=lambda s: -s["days"])
    return stuck


def disk_paths(repo):
    """Строки публичного settings.json с абсолютным путём к файлу на диске."""
    f = repo / SETTINGS
    if not f.exists():
        return []
    return [{"line": i, "text": s.strip()}
            for i, s in enumerate(f.read_text(encoding="utf-8").splitlines(), 1)
            if DISK_PATH.search(s)]


def report(r, stale_days):
    print(f"Страниц: {r['pages']}, находок: {r['total']}\n")
    if r["broken_links"]:
        print(f"Битые [[ссылки]] ({len(r['broken_links'])}):")
        for b in r["broken_links"]:
            print(f"  {b['page']} → [[{b['target']}]]")
    if r["orphans"]:
        print(f"\nСтраницы-сироты, без входящих ссылок и без строки в индексе ({len(r['orphans'])}):")
        for o in r["orphans"]:
            print(f"  {o}")
    if r["unindexed"]:
        print(f"\nНе перечислены в index.md ({len(r['unindexed'])}):")
        for u in r["unindexed"]:
            print(f"  {u}")
    if r["stale"]:
        print(f"\nПросроченное «Актуально на» ({len(r['stale'])}) — порог {stale_days} дн. "
              f"для продуктов, {r['people_days']} дн. для людей и изданий:")
        for s in r["stale"]:
            print(f"  {s['page']} — {s['actual']} ({s['age_days']} дн., {s['kind']}, порог {s['limit']})")
    if r["disk_paths"]:
        print(f"\nПути с диска в публичном {SETTINGS} ({len(r['disk_paths'])}) — файл уезжает на GitHub:")
        for d in r["disk_paths"]:
            print(f"  строка {d['line']}: {d['text'][:100]}")
        print("  Перенести правило в .claude/settings.local.json (он в gitignore);")
        print("  путь к самому проекту в командах заменять на ${CLAUDE_PROJECT_DIR}.")
    if r["stuck"]:
        print(f"\nПовторяющиеся безрезультатные заходы ({len(r['stuck'])}) — "
              f"лог упирается в одно и то же:")
        for s in r["stuck"]:
            print(f"  {s['host']} — {s['days']} прогонов: {', '.join(s['dates'])}")
        print("  Рутине туда больше не ходить: домен блокирует сетевой фильтр её")
        print("  окружения, а не сам сайт. Такой пункт закрывается из локальной сессии.")
        print("  Список — подсказка, а не приговор: домен, который в тех же записях")
        print("  открывался, может попасть сюда за компанию. Проверить глазами.")
    if not r["total"]:
        print("Механических находок нет. Дальше — смысловая часть, её делает модель.")


def self_test():
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        # Игрушечный репозиторий целиком, не одна папка wiki: проверке настроек
        # нужен корень (wiki.parent), а он не должен указывать в системный temp.
        w = Path(tmp) / "wiki"
        w.mkdir()
        (w / "index.md").write_text("# Индекс\n- [[alpha]]\n", encoding="utf-8")
        (w / "log.md").write_text("# Лог\n", encoding="utf-8")
        (w / "alpha.md").write_text(
            "# Alpha\n**Актуально на:** 2026-01-01\n[[beta]] и [[CLAUDE.md]], "
            "а вот `[[wiki-links]]` — это цитата\n", encoding="utf-8")
        (w / "beta.md").write_text("# Beta\n", encoding="utf-8")
        (w / "ghost.md").write_text("# Ghost\nникто на меня не ссылается\n", encoding="utf-8")

        r = lint(w, dt.date(2026, 7, 29), 30)
        assert r["broken_links"] == [], r["broken_links"]          # allowlist + код
        assert r["orphans"] == ["ghost.md"], r["orphans"]          # beta связана, alpha в индексе
        assert sorted(r["unindexed"]) == ["beta.md", "ghost.md"], r["unindexed"]
        assert [s["page"] for s in r["stale"]] == ["alpha.md"], r["stale"]

        assert r["disk_paths"] == [], r["disk_paths"]               # settings.json нет вовсе

        # Пути с диска в публичных настройках. Проверяем оба исхода: чистый файл
        # молчит, файл с путём — находка. Проверка только «сработал на плохом»
        # оставила бы правило, ругающееся на что угодно.
        s = w.parent / ".claude"
        s.mkdir(exist_ok=True)
        (s / "settings.json").write_text('{"permissions":{"allow":["Bash(git status)"]}}\n', encoding="utf-8")
        assert lint(w, dt.date(2026, 7, 29), 30)["disk_paths"] == []

        # Файл настроек в жизни отформатирован по строкам, находки тоже построчные:
        # оба пути должны найтись по отдельности, а не слипнуться в один.
        (s / "settings.json").write_text(
            '{\n'
            '  "permissions": {\n'
            '    "allow": ["Bash(node --test \\"C:/my_projects/x/t.js\\")"],\n'
            '    "additionalDirectories": ["C:\\\\Users\\\\someone\\\\.claude"]\n'
            '  }\n'
            '}\n', encoding="utf-8")
        found = lint(w, dt.date(2026, 7, 29), 30)["disk_paths"]
        assert [d["line"] for d in found] == [3, 4], found

        # Разные пороги: у продукта и у человека одна и та же дата, но продукт
        # просрочен, а человек нет. Проверяем и границу срабатывания для человека —
        # иначе правило «людей не трогаем» молча превратилось бы в «не трогаем никогда».
        (w / "index.md").write_text("# Индекс\n- [[alpha]]\n- [[tool]]\n- [[person]]\n", encoding="utf-8")
        (w / "tool.md").write_text(
            "# Tool\n**Тип:** инструмент (IDE)\n**Актуально на:** 2026-06-01\n[[alpha]]\n", encoding="utf-8")
        (w / "person.md").write_text(
            "# Person\n**Тип:** человек / YouTube-канал\n**Актуально на:** 2026-06-01\n[[alpha]]\n", encoding="utf-8")

        by_page = {s["page"]: s for s in lint(w, dt.date(2026, 7, 29), 30, 180)["stale"]}
        assert "tool.md" in by_page, by_page          # 58 дней при пороге 30
        assert "person.md" not in by_page, by_page    # 58 дней при пороге 180 — рано
        assert by_page["tool.md"]["kind"] == "продукт"

        late = {s["page"] for s in lint(w, dt.date(2027, 1, 1), 30, 180)["stale"]}
        assert "person.md" in late, late              # 214 дней — уже пора

        # Пометка «не используется» снимает счётчик свежести совсем: та же дата,
        # что у просроченного tool.md, но в находки не попадает ни сейчас, ни через
        # полгода. Проверяем оба среза — иначе правило было бы просто отсрочкой.
        (w / "index.md").write_text(
            "# Индекс\n- [[alpha]]\n- [[tool]]\n- [[person]]\n- [[dropped]]\n", encoding="utf-8")
        (w / "dropped.md").write_text(
            "# Dropped\n**Тип:** инструмент (IDE)\n**Статус:** не используется в этой вике\n"
            "**Актуально на:** 2026-06-01\n[[alpha]]\n", encoding="utf-8")
        assert "dropped.md" not in {s["page"] for s in lint(w, dt.date(2026, 7, 29), 30, 180)["stale"]}
        assert "dropped.md" not in {s["page"] for s in lint(w, dt.date(2027, 1, 1), 30, 180)["stale"]}

        for f in ("tool.md", "person.md", "dropped.md"):
            (w / f).unlink()

        (w / "alpha.md").write_text("# Alpha\n[[nowhere]]\n", encoding="utf-8")
        r2 = lint(w, dt.date(2026, 7, 29), 30)
        assert r2["broken_links"][0]["target"] == "nowhere", r2["broken_links"]

        # Повторяющиеся безрезультатные заходы. Проверяем четыре вещи сразу:
        # (1) три разных дня по одному домену — находка; (2) два дня — ещё нет,
        # иначе правило ругалось бы на обычную вторую попытку; (3) домен, который
        # в тех же записях открылся, в находки не попадает — иначе сработало бы
        # на любой странице, где рядом стоят удачный и неудачный фетч;
        # (4) имена файлов (log.md) за домены не считаются.
        (w / "log.md").write_text(
            "# Лог\n\n"
            "## [2026-08-15] lint | раз\n"
            "`arxiv.org` заблокирован сетевым фильтром окружения, "
            "но `github.com` остался доступен — оттуда и взяли README.\n"
            "Запись легла в log.md как обычно.\n\n"
            "## [2026-08-16] lint | два\n"
            "Снова EGRESS_BLOCKED на `arxiv.org` (статья 2605.08442).\n"
            "И ещё раз `arxiv.org` в том же прогоне — это тот же заход, не новый.\n"
            "`cursor.com` недоступен.\n\n"
            "## [2026-08-17] lint | три\n"
            "`arxiv.org` опять не открылся, зато `github.com` отдал всё нужное.\n",
            encoding="utf-8")

        stuck = {s["host"]: s for s in lint(w, dt.date(2026, 8, 18), 30)["stuck"]}
        assert "arxiv.org" in stuck, stuck                 # три разных дня
        assert stuck["arxiv.org"]["days"] == 3, stuck      # повтор внутри дня не считается
        assert "cursor.com" not in stuck, stuck            # один день — рано
        assert "github.com" not in stuck, stuck            # открылся, а не заблокирован
        assert "log.md" not in stuck, stuck                # имя файла — не домен
        assert "2605.08442" not in stuck, stuck            # arXiv-номер — не домен

        # Порог настраиваемый, и на двух днях он тоже должен срабатывать.
        loose = {s["host"] for s in lint(w, dt.date(2026, 8, 18), 30, stuck_days=2)["stuck"]}
        assert "arxiv.org" in loose and "cursor.com" not in loose, loose
    print("self-test ok")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--wiki", default=str(WIKI), help="путь к папке wiki")
    ap.add_argument("--stale-days", type=int, default=30,
                    help="порог свежести «Актуально на» для продуктов (по умолчанию 30)")
    ap.add_argument("--people-days", type=int, default=180,
                    help="то же для людей и изданий — у них почти ничего не меняется "
                         "(по умолчанию 180)")
    ap.add_argument("--stuck-days", type=int, default=3,
                    help="со скольких разных прогонов заход в один и тот же "
                         "недоступный домен считать зацикливанием (по умолчанию 3)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        self_test()
        return 0

    wiki = Path(args.wiki)
    if not wiki.is_dir():
        print(f"нет такой папки: {wiki}", file=sys.stderr)
        return 2

    result = lint(wiki, dt.date.today(), args.stale_days, args.people_days,
                  args.stuck_days)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        report(result, args.stale_days)
    return 0


if __name__ == "__main__":
    sys.exit(main())
