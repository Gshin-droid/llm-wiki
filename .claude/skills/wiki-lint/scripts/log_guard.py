#!/usr/bin/env python3
"""Сторож журнала: запись из wiki/log.md не может исчезнуть или задвоиться.

    python log_guard.py              # сверить журнал со всей его историей в git
    python log_guard.py --self-test

2026-11-17: сверка с прошлым пушем заменена сверкой со всей историей. Пропажа
заголовка 10.11 (b152030) дала один красный прогон, его не заметили, а со
следующего пуша сравнивать стало не с чем — сторож неделю был зелёным при
сломанном журнале. Теперь пропажа краснеет на каждом пуше, пока её не вернут.
Первый же прогон нашёл вторую такую же потерю — 07.08, до появления сторожа.

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


# Заголовки, убранные осознанно (переименование). Переименовать заголовок —
# значит внести сюда старое имя тем же коммитом: так снятие видно в истории.
RETIRED = {
    # 2026-07-31, 6da2016: тег scout → ingest по конвенции вики.
    "## [2026-07-31] scout | Финальная спецификация MCP 2026-07-28 вышла точно в срок"
    " — закрыт открытый статус на странице протокола",
}


def ever_headings(patch_text):
    """Заголовки, когда-либо добавленные в журнал, по выводу `git log -p`."""
    added = (l[1:].strip() for l in patch_text.split("\n") if l.startswith("+## ["))
    return list(dict.fromkeys(h for h in added if HEAD.match(h)))


def check(base, cur_text):
    """base — текст журнала или список заголовков, которые обязаны остаться.
    Возвращает (пропавшие, задвоившиеся). Пустые списки — всё хорошо."""
    cur = headings(cur_text)
    base = headings(base) if isinstance(base, str) else base
    missing = [h for h in dict.fromkeys(base) if h not in cur and h not in RETIRED]
    dupes = [h for h, n in Counter(cur).items() if n > 1]
    return missing, dupes


def out_of_order(cur_text):
    """Первая запись обязана быть самой свежей. Возвращает (первая, самая свежая)
    при нарушении, иначе None.

    Добавлено 2026-08-24 замером решающего дерева (wiki/synthesis/
    karta-shvov-nashey-obvyazki.md). Правило «новые записи сверху» жило только
    текстом, хотя проверяется формой. Строгий порядок дат сторожем не годится:
    измерение показало 21 нарушение на историческом хвосте — журнал начинали
    вести снизу вверх и позже перевернули соглашение, и такой сторож краснел бы
    вечно. А вот «первая запись — самая свежая» выполняется на всей истории и
    ловит настоящую поломку: запись, приписанную в конец или вставленную в
    середину. Узкий инвариант вместо широкого, ровно по фильтру из
    wiki/concepts/verification-three-levels.md."""
    dates = [h[4:14] for h in headings(cur_text)]
    if not dates:
        return None
    newest = max(dates)
    return None if dates[0] == newest else (dates[0], newest)


def git_history(path):
    """Все изменения файла за историю. В неполном клоне истории меньше —
    сторож видит меньше, но ложно не краснеет."""
    r = subprocess.run(["git", "log", "-p", "--format=", "--no-color", "--no-ext-diff",
                        "--", path], capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        sys.exit(f"git log не сработал: {r.stderr.strip()}")
    return r.stdout


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()

    if a.self_test:
        self_test()
        return 0

    cur = open(LOG, encoding="utf-8").read()
    # Сверка со всей историей, а не с прошлым пушем: иначе пропажа краснеет
    # один раз, а со следующего пуша сторож снова зелёный (случай 2026-11-10).
    missing, dupes = check(ever_headings(git_history(LOG)), cur)

    disorder = out_of_order(cur)
    for h in missing:
        print(f"ПРОПАЛА ЗАПИСЬ: {h}", file=sys.stderr)
    for h in dupes:
        print(f"ДУБЛЬ ЗАГОЛОВКА: {h}", file=sys.stderr)
    if disorder:
        first, newest = disorder
        print(f"ПОРЯДОК: первая запись за {first}, а самая свежая — за {newest}.\n"
              "Новые записи идут сверху и вставкой: файл читается с начала, и запись,\n"
              "приписанная в конец, для следующего прогона не существует.",
              file=sys.stderr)
        return 1
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

    # Храповик: заголовок пропал два пуша назад — сравнение с прошлым пушем
    # его уже не видит, сравнение со всей историей видит. Случай 2026-11-10.
    patch = ("@@ -1,0 +1,1 @@\n+## [2026-08-12] practice | Замеры моделей\n+текст\n"
             "@@ -1,1 +1,1 @@\n-## [2026-08-12] practice | Замеры моделей\n"
             "+## [2026-08-13] lint | Новое\n"
             " ## [2026-08-14] lint | Контекст, не добавление\n")
    assert ever_headings(patch) == ["## [2026-08-12] practice | Замеры моделей",
                                    "## [2026-08-13] lint | Новое"], ever_headings(patch)
    later = "# Лог\n\n## [2026-08-14] news | Ещё новее\n\n## [2026-08-13] lint | Новое\n"
    missing, _ = check(ever_headings(patch), later)
    assert missing == ["## [2026-08-12] practice | Замеры моделей"], missing
    # Законное переименование из списка RETIRED — не находка.
    assert check(["## [2026-07-31] scout | Финальная спецификация MCP 2026-07-28 "
                  "вышла точно в срок — закрыт открытый статус на странице протокола"],
                 later) == ([], [])

    # Порядок: первая запись — самая свежая.
    assert out_of_order(ok) is None, out_of_order(ok)
    appended = "# Лог\n\n## [2026-08-12] practice | Старое\n\n## [2026-08-13] lint | Новое\n"
    assert out_of_order(appended) == ("2026-08-12", "2026-08-13"), out_of_order(appended)
    # Исторический хвост в обратном порядке ниже по файлу — законен и не находка:
    # сторож смотрит только на то, что первая запись самая свежая.
    tail = ("# Лог\n\n## [2026-08-13] lint | Новое\n\n## [2026-07-07] ingest | Старое\n"
            "\n## [2026-07-08] ingest | Ещё старое\n")
    assert out_of_order(tail) is None, out_of_order(tail)
    assert out_of_order("# Лог\nбез записей") is None
    print("self-test ok")


if __name__ == "__main__":
    sys.exit(main())
