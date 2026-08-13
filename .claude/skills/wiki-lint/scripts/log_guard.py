#!/usr/bin/env python3
"""Сторож журнала: запись из wiki/log.md не может исчезнуть или задвоиться.

    python log_guard.py <BASE_REF>   # сверить с состоянием файла в base-коммите
    python log_guard.py              # только проверка на дубли в текущем файле
    python log_guard.py --self-test

Повод — 2026-08-13. Автономная рутина сделала два коммита подряд, а второй
писала по тексту лога, прочитанному ДО первого: заголовок чужой записи она
переписала своим. Внешне это выглядело как один дубль, на деле пропала запись
целиком. Правило «новые записи сверху» такого не ловит — оно про порядок, а не
про сохранность, и человеком замечено только через сутки.

Сторож живёт в CI, а не в локальном pre-commit, намеренно: коммиты сюда шлёт и
облачная рутина, у которой локальных хуков нет вовсе (git не исполняет хуки из
клона по соображениям безопасности). Проверка на стороне GitHub — единственная,
через которую проходят оба.

Журнал append-only: старая запись меняться может (уточнение, исправление), но
её заголовок обязан остаться. Заголовок — это адрес записи, по нему на неё
ссылаются рутины и сверки.
"""
import argparse
import re
import subprocess
import sys
from collections import Counter

LOG = "wiki/log.md"
HEAD = re.compile(r"^## \[\d{4}-\d{2}-\d{2}\].*$", re.M)


def headings(text):
    return [m.group(0).strip() for m in HEAD.finditer(text)]


def check(base_text, cur_text):
    """Возвращает (пропавшие, задвоившиеся). Пустые списки — всё хорошо."""
    cur = headings(cur_text)
    missing = [h for h in dict.fromkeys(headings(base_text)) if h not in cur]
    dupes = [h for h, n in Counter(cur).items() if n > 1]
    return missing, dupes


def git_show(ref, path):
    """Текст файла в коммите; пустая строка, если файла там не было."""
    r = subprocess.run(["git", "show", f"{ref}:{path}"],
                       capture_output=True, text=True, encoding="utf-8")
    return r.stdout if r.returncode == 0 else ""


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("base", nargs="?", help="коммит, с которым сверять (обычно github.event.before)")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()

    if a.self_test:
        self_test()
        return 0

    cur = open(LOG, encoding="utf-8").read()
    # У первого push ветки base — сорок нулей: сравнивать не с чем, остаются дубли.
    no_base = not a.base or set(a.base) <= {"0"}
    base_text = "" if no_base else git_show(a.base, LOG)
    missing, dupes = check(base_text, cur)

    for h in missing:
        print(f"ПРОПАЛА ЗАПИСЬ: {h}", file=sys.stderr)
    for h in dupes:
        print(f"ДУБЛЬ ЗАГОЛОВКА: {h}", file=sys.stderr)
    if missing or dupes:
        print("\nЖурнал append-only: правка старой записи допустима, исчезновение — нет.\n"
              "Скорее всего запись писалась поверх устаревшего в памяти текста файла.\n"
              "Почини: верни заголовок из истории (git show <коммит>:wiki/log.md).",
              file=sys.stderr)
        return 1
    print(f"журнал цел: записей {len(headings(cur))}, пропаж и дублей нет")
    return 0


def self_test():
    base = "# Лог\n\n## [2026-08-12] practice | Замеры моделей\n\nтекст\n"
    ok = "# Лог\n\n## [2026-08-13] lint | Новое\n\n## [2026-08-12] practice | Замеры моделей\n"
    assert check(base, ok) == ([], []), check(base, ok)

    # Ровно наш случай: заголовок старой записи переписан новым.
    broken = "# Лог\n\n## [2026-08-13] lint | Новое\n\n## [2026-08-13] lint | Новое\n"
    missing, dupes = check(base, broken)
    assert missing == ["## [2026-08-12] practice | Замеры моделей"], missing
    assert dupes == ["## [2026-08-13] lint | Новое"], dupes

    # Правка тела старой записи — законна, заголовок на месте.
    edited = base.replace("текст", "текст, уточнённый позже")
    assert check(base, edited) == ([], [])

    # Первый push ветки: базы нет, но дубли ловим и без неё.
    assert check("", broken) == ([], ["## [2026-08-13] lint | Новое"])
    print("self-test ok")


if __name__ == "__main__":
    sys.exit(main())
