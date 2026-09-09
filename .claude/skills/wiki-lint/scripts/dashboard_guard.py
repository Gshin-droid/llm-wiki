#!/usr/bin/env python3
"""Сторож дашборда: дата в шапке обязана совпадать с датой верхней записи журнала.

    python dashboard_guard.py              # проверить текущее состояние
    python dashboard_guard.py --self-test

Повод — три случая подряд. 12–13.08.2026 опубликованная страница двое суток
показывала позапрошлые новости; 06.08 и 09.09 прогон коммитил dashboard.html,
но правил в нём одну строку каталога, а шапку оставлял вчерашней. Правило
«правка одной строки каталога обновлением дашборда не считается» записано в
CLAUDE.md текстом и три раза не сработало.

Причина конструктивная, а не небрежность: wiki/log.md — канонический журнал, а
dashboard.html — его представление, но представление поддерживается отдельной
рукой параллельно с журналом. Такое всегда разъезжается, вопрос только когда.
Разбор — wiki/concepts/invariant-vidno-znachit-zapisano.md, раздел
«Дополнение (2026-09-09)»; правило уровня всех проектов —
~/.claude/rules/proverki.md, «Представление не поддерживают параллельно с
источником»: либо выводить, либо стеречь совпадение. Здесь второе.

Сторож живёт в CI, а не в локальном pre-commit, по той же причине, что и
остальные: коммиты сюда шлёт облачная рутина, у которой локальных хуков нет.

Инвариант нарочно узкий — сверяются ровно две даты, смысл карточек не
проверяется. По фильтру из wiki/concepts/verification-three-levels.md: замкнут
на самом результате (две строки в двух файлах), ответ тот же через год (модель
не зовём), законных исключений не найдено — дата в шапке старше верхней записи
означает ровно то, что дашборд отстал.

Чего НЕ ловит: прогон, вообще не тронувший dashboard.html — сторож висит на
push с этим файлом. Все три известных случая были другого вида (файл
коммитился, дата не менялась). Если появится и такой — добавляется schedule в
.github/workflows/dashboard-guard.yml, скрипт менять не придётся.
"""
import argparse
import re
import sys

DASH = "wiki/dashboard.html"
LOG = "wiki/log.md"

# <div class="mono">обновлено 2026-09-09 (2 записи) · след. запуск 08:00 (09.10)</div>
DASH_DATE = re.compile(r"обновлено (\d{4}-\d{2}-\d{2})")
# ## [2026-09-09] ingest | Название
LOG_DATE = re.compile(r"^## \[(\d{4}-\d{2}-\d{2})\]", re.M)


def check(dash_text, log_text):
    """Возвращает (дата дашборда, дата верхней записи) или None, если всё сходится.

    Строка 'нет' на месте даты означает, что её не удалось найти вообще, — это
    тоже находка: сторож не должен молчать, когда не смог прочитать то, что
    сверяет (fail closed, ~/.claude/rules/hygiene.md)."""
    d = DASH_DATE.search(dash_text)
    l = LOG_DATE.search(log_text)
    dash = d.group(1) if d else "нет"
    log = l.group(1) if l else "нет"
    return None if (dash == log and d and l) else (dash, log)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()

    if a.self_test:
        self_test()
        return 0

    bad = check(open(DASH, encoding="utf-8").read(),
                open(LOG, encoding="utf-8").read())
    if not bad:
        print(f"дашборд синхронен журналу: {DASH_DATE.search(open(DASH, encoding='utf-8').read()).group(1)}")
        return 0

    dash, log = bad
    print(f"ДАШБОРД ОТСТАЛ: в шапке {DASH} стоит «обновлено {dash}»,\n"
          f"а верхняя запись {LOG} — за {log}.\n\n"
          "Дашборд — представление журнала, а не отдельный документ: пока они\n"
          "расходятся, опубликованная страница показывает позапрошлые новости.\n"
          "Почини: обнови в dashboard.html строку DASHBOARD:UPDATED-LINE, счётчики\n"
          "DASHBOARD:STATS, карточки DASHBOARD:NEWS и каталог — и только потом\n"
          "коммить. Правка одной строки каталога обновлением дашборда не считается.",
          file=sys.stderr)
    return 1


def self_test():
    dash = '<div class="mono">обновлено 2026-09-09 (2 записи) · след. запуск 08:00 (09.10)</div>'
    log_ok = "# Лог\n\n## [2026-09-09] ingest | Новое\n\n## [2026-09-08] lint | Старое\n"
    assert check(dash, log_ok) is None, check(dash, log_ok)

    # Ровно наш случай: журнал уехал вперёд, шапка дашборда осталась вчерашней.
    log_ahead = "# Лог\n\n## [2026-09-10] ingest | Ещё новее\n\n## [2026-09-09] ingest | Новое\n"
    assert check(dash, log_ahead) == ("2026-09-09", "2026-09-10"), check(dash, log_ahead)

    # Дашборд впереди журнала — тоже расхождение, не «ничего страшного».
    log_behind = "# Лог\n\n## [2026-09-08] lint | Старое\n"
    assert check(dash, log_behind) == ("2026-09-09", "2026-09-08")

    # Даты нет вообще — сторож обязан краснеть, а не молчать.
    assert check('<div class="mono">обновлено недавно</div>', log_ok) == ("нет", "2026-09-09")
    assert check(dash, "# Лог\nбез записей") == ("2026-09-09", "нет")

    # Сравнивается именно ПЕРВАЯ запись: порядок «новые сверху» стережёт log_guard,
    # дублировать эту проверку здесь незачем.
    log_disordered = "# Лог\n\n## [2026-09-09] ingest | Новое\n\n## [2026-09-20] lint | Из будущего\n"
    assert check(dash, log_disordered) is None
    print("self-test ok")


if __name__ == "__main__":
    sys.exit(main())
