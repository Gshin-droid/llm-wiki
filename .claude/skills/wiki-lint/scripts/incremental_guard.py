#!/usr/bin/env python3
"""Сторож инкрементальности: одна находка — один коммит.

Зачем. 10.07.2026 весь разбор был сделан и потерян на лимите подписки ровно
перед финальным пушем. Лечение записано правилом в CLAUDE.md: доведённая
находка коммитится и пушится сразу, следующая — своим коммитом. Правило
текстом ничего не гарантирует; этот сторож делает его нарушение видимым.

Что проверяется. Ни один коммит не добавляет больше одной новой страницы
в wiki/sources/. Коммит, добавляющий две и больше, означает, что разбор
копился в рабочем каталоге, — и если прогон умрёт на лимите посередине,
потеряется всё накопленное.

Почему это инвариант, а не эвристика (критерий — wiki/concepts/
verification-three-levels.md). Замкнуто на самом объекте: число добавленных
файлов считается из диффа, модель для этого не нужна. Ответ не изменится
через год. Законное исключение ровно одно — человек осознанно собирает
несколько разборов в один коммит; оно объявляется словом [батч] в сообщении
коммита. Объявленное исключение переводит эвристику в инвариант: правило
знает, когда оно не действует.

Отказ здесь виден — сборка краснеет, и её видно и человеку, и в письме о
прогоне. Поэтому ложный отказ не молчалив, и блокировать можно.

Запуск:
    python incremental_guard.py <base-sha>     # режим CI
    python incremental_guard.py --selftest     # самопроверка логики
"""

import subprocess
import sys

SOURCES_PREFIX = "wiki/sources/"
BATCH_MARKER = "[батч]"
LIMIT = 1


def git(*args):
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, encoding="utf-8", check=True
    ).stdout


def commits_in_range(base, head="HEAD"):
    out = git("rev-list", "--no-merges", f"{base}..{head}")
    return [line.strip() for line in out.splitlines() if line.strip()]


def added_sources(sha):
    """Новые .md-страницы источников, добавленные этим коммитом."""
    out = git("show", "--name-only", "--diff-filter=A", "--pretty=format:", sha)
    return [
        f.strip()
        for f in out.splitlines()
        if f.strip().startswith(SOURCES_PREFIX) and f.strip().endswith(".md")
    ]


def message(sha):
    return git("log", "-1", "--pretty=format:%s%n%b", sha)


def check(base, head="HEAD"):
    """Возвращает (осмотрено_коммитов, список_нарушений)."""
    violations = []
    shas = commits_in_range(base, head)
    for sha in shas:
        added = added_sources(sha)
        if len(added) > LIMIT and BATCH_MARKER not in message(sha):
            violations.append((sha, added))
    return len(shas), violations


def main():
    if len(sys.argv) < 2:
        print("нужен base-sha; для самопроверки — --selftest", file=sys.stderr)
        return 2

    base = sys.argv[1]
    # Первый push ветки: предыдущего коммита нет, сравнивать не с чем.
    if not base or set(base) == {"0"}:
        print("Сторож инкрементальности: базового коммита нет, сравнивать не с чем.")
        return 0

    try:
        examined, violations = check(base)
    except subprocess.CalledProcessError as e:
        # Тот случай, ради которого пишется охват: не смогли посмотреть —
        # это «не проверено», а не «чисто».
        print(f"Сторож инкрементальности: НЕ ПРОВЕРЕНО, git отказал: {e}", file=sys.stderr)
        return 2

    if not violations:
        print(f"Сторож инкрементальности: осмотрено коммитов {examined}, нарушений нет.")
        return 0

    print(f"Сторож инкрементальности: осмотрено коммитов {examined}, нарушений {len(violations)}.\n")
    for sha, added in violations:
        print(f"  {sha[:8]} добавляет страниц источников: {len(added)}")
        for f in added:
            print(f"      {f}")
    print(
        "\nОдна доведённая находка — один коммит и push. Копить разборы в рабочем\n"
        f"каталоге нельзя: прогон обрывается на лимите без предупреждения.\n"
        f"Осознанный batch человека объявляется словом {BATCH_MARKER} в сообщении коммита."
    )
    return 1


def selftest():
    """Проверяет саму логику решения, без обращения к git."""
    def decide(added_count, msg):
        return added_count > LIMIT and BATCH_MARKER not in msg

    assert decide(2, "ingest: две находки") is True, "две страницы без метки — нарушение"
    assert decide(1, "ingest: одна находка") is False, "одна страница — норма"
    assert decide(0, "dashboard: счётчики") is False, "без новых страниц — норма"
    assert decide(5, f"ingest: разбор инбокса {BATCH_MARKER}") is False, "метка снимает отказ"
    assert decide(2, "ingest: батч") is True, "метка нужна в квадратных скобках, а не словом"

    # фильтр путей: считаются только страницы источников
    sample = ["wiki/sources/a.md", "wiki/concepts/b.md", "wiki/sources/notes.txt", "wiki/sources/c.md"]
    picked = [f for f in sample if f.startswith(SOURCES_PREFIX) and f.endswith(".md")]
    assert picked == ["wiki/sources/a.md", "wiki/sources/c.md"], picked

    print("Самопроверка сторожа инкрементальности: пройдена.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
