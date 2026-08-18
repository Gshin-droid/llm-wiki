#!/usr/bin/env python3
"""Механическая часть операции Ingest: что уже разобрано и что забыто.

    python ingest.py pending              # сырые материалы без страницы в wiki/sources
    python ingest.py check <slug>         # проверить готовность разбора
    python ingest.py --self-test

Смысловое (что взять из источника, во что превратить, чему противоречит)
скрипт не умеет — это работа модели, см. SKILL.md.
"""
import argparse
import datetime as dt
import re
import sys
from pathlib import Path

# Имена файлов из веб-клиппера несут символы вне cp1251 (неразрывный дефис и т.п.),
# на которых печать в консоль Windows падает UnicodeEncodeError.
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[4]
RAW_DIRS = ("web-clipped", "inbox-assistant", "sources")
REQUIRED_SECTIONS = ("**Дата загрузки:**", "**Raw:**", "## Связи")


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


def check(root, slug, today):
    page = root / "wiki" / "sources" / f"{slug}.md"
    problems = []
    if not page.exists():
        return [f"нет страницы wiki/sources/{slug}.md"]

    body = page.read_text(encoding="utf-8")
    for section in REQUIRED_SECTIONS:
        if section not in body:
            problems.append(f"на странице нет обязательного поля: {section}")

    index = (root / "wiki" / "index.md").read_text(encoding="utf-8")
    if f"[[{slug}]]" not in index:
        problems.append("страница не добавлена в wiki/index.md")

    log = (root / "wiki" / "log.md").read_text(encoding="utf-8")
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
    print("self-test ok")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("command", nargs="?", choices=["pending", "check"])
    ap.add_argument("slug", nargs="?")
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        self_test()
        return 0
    root = Path(args.root)

    if args.command == "pending":
        items = pending(root)
        print(f"Неразобранного сырья: {len(items)}")
        for i in items:
            print(f"  {i}")
        if not items:
            print("Всё сырьё в raw/ имеет страницу в wiki/sources/.")
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

    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
