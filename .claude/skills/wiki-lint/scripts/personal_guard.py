#!/usr/bin/env python3
"""Сторож личного: путь с машины не уезжает в публичный репозиторий.

Зачем. Вики публичная и опубликована сайтом — что попало в коммит, стало
открытой веб-страницей. Правило «личное не публикуется» записано и в
CLAUDE.md проекта, и в глобальных правилах пользователя, но текст правила
ничего не гарантирует. Локальный pre-commit у человека это ловит, а коммиты
сюда шлют ещё и облачные рутины ночью: у них локальных хуков нет вовсе —
они работают из свежего клона. Проверка на стороне GitHub — единственная,
через которую проходят все писатели сразу.

Что проверяется. В строках, **добавленных** коммитом, не должно быть путей
файловой системы с конкретной машины: `C:\\...`, `C:/...`, `/home/...`,
`/Users/...`, `/c/my_...`. Правило намеренно про форму пути, а не про
конкретные имена: имя пользователя, записанное в сам сторож, было бы той же
утечкой, которую он ищет.

Почему только добавленные строки: в репозитории уже лежат девять законных
упоминаний такой формы — сама эта регулярка, разбор правила в practices,
цитаты старых находок в логе. Сторож, ругающийся на неизменённый текст,
краснел бы всегда и приучил бы не смотреть на себя.

Почему это инвариант, а не эвристика (критерий — wiki/concepts/
verification-three-levels.md). Замкнуто на самом объекте: форма пути видна
из диффа, модель для этого не нужна. Ответ не изменится через год. Законное
исключение есть — разбор самого правила, где путь нужен как пример; оно
объявляется словом [путь-осознанно] в сообщении коммита. Объявленное
исключение переводит эвристику в инвариант: правило знает, когда оно не
действует.

Отказ здесь виден — сборка краснеет, и её видно и человеку, и в письме о
прогоне. Поэтому ложный отказ не молчалив, и блокировать можно.

Чего сторож НЕ ловит (осознанно, не забыто): смысл. «Пользователь живёт
там-то», «подписка стоит столько-то» — обычный текст без особой формы,
формой его не отличить от разбора источника. Это остаётся на человеке и на
правилах в CLAUDE.md.

Запуск:
    python personal_guard.py <base-sha>     # режим CI
    python personal_guard.py --selftest     # самопроверка логики
"""

import re
import subprocess
import sys

# Одна буква диска, и перед ней нет других букв: без этого "https://" читается
# как диск "s:" и любая строка с адресом становится ложной находкой (случай
# 13.08.2026, та же регулярка в lint_wiki.py).
DISK_PATH = re.compile(r"(?<![A-Za-z])[A-Za-z]:[\\/]|/home/|/Users/|/c/my_")
MARKER = "[путь-осознанно]"
# Сторож содержит примеры путей в докстроке, в self-test и в комментарии своего
# workflow — на себя он ругаться не должен, иначе первый же его коммит красный.
# Исключение именно по этим двум путям, а не по расширению или папке: любой
# другой файл, включая соседние скиллы, проверяется как обычно.
SELF = (
    ".claude/skills/wiki-lint/scripts/personal_guard.py",
    ".github/workflows/personal-guard.yml",
)


def git(*args):
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, encoding="utf-8", check=True
    ).stdout


def commits_in_range(base, head="HEAD"):
    out = git("rev-list", "--no-merges", f"{base}..{head}")
    return [line.strip() for line in out.splitlines() if line.strip()]


def added_lines(sha):
    """[(файл, строка)] — то, что коммит добавил, без удалённого и контекста."""
    out = git("show", "--unified=0", "--pretty=format:", "--no-color", sha)
    return parse_diff(out)


def parse_diff(diff_text):
    result, path = [], None
    for line in diff_text.splitlines():
        if line.startswith("+++ "):
            path = line[6:].strip() if line.startswith("+++ b/") else None
        elif line.startswith("+") and not line.startswith("+++") and path:
            result.append((path, line[1:]))
    return result


def violations_in(pairs):
    return [(f, ln) for f, ln in pairs if f not in SELF and DISK_PATH.search(ln)]


def message(sha):
    return git("log", "-1", "--pretty=format:%s%n%b", sha)


def check(base, head="HEAD"):
    """Возвращает (осмотрено_коммитов, список_нарушений)."""
    found = []
    shas = commits_in_range(base, head)
    for sha in shas:
        bad = violations_in(added_lines(sha))
        if bad and MARKER not in message(sha):
            found.append((sha, bad))
    return len(shas), found


def main():
    if len(sys.argv) < 2:
        print("нужен base-sha; для самопроверки — --selftest", file=sys.stderr)
        return 2

    base = sys.argv[1]
    # Первый push ветки: предыдущего коммита нет, сравнивать не с чем.
    if not base or set(base) == {"0"}:
        print("Сторож личного: базового коммита нет, сравнивать не с чем.")
        return 0

    try:
        examined, found = check(base)
    except subprocess.CalledProcessError as e:
        # Не смогли посмотреть — это «не проверено», а не «чисто».
        print(f"Сторож личного: НЕ ПРОВЕРЕНО, git отказал: {e}", file=sys.stderr)
        return 2

    if not found:
        print(f"Сторож личного: осмотрено коммитов {examined}, путей с машины не добавлено.")
        return 0

    print(f"Сторож личного: осмотрено коммитов {examined}, коммитов с находками {len(found)}.\n")
    for sha, bad in found:
        print(f"  {sha[:8]} добавляет строки с путём с машины: {len(bad)}")
        for f, ln in bad[:10]:
            print(f"      {f}: {ln.strip()[:110]}")
    print(
        "\nРепозиторий публичный и опубликован сайтом: попавшее в коммит становится\n"
        "открытой веб-страницей. Путь с диска выдаёт устройство машины и имя\n"
        "пользователя — личному место в private/ и в памяти, а не здесь.\n"
        f"Осознанное исключение (разбор самого правила) объявляется словом {MARKER}\n"
        "в сообщении коммита."
    )
    return 1


def selftest():
    """Проверяет саму логику решения, без обращения к git."""
    diff = (
        "+++ b/wiki/sources/x.md\n"
        "+обычная строка про инструмент\n"
        "+ссылка https://example.com/path — не диск\n"
        "+запускается из C:/my_projects/jarvis\n"
        "-удалённая строка с /Users/someone/ не считается\n"
        "+++ b/.claude/skills/wiki-lint/scripts/personal_guard.py\n"
        "+DISK_PATH = re.compile(...)  # /Users/ в самом стороже\n"
        "+++ b/.github/workflows/personal-guard.yml\n"
        "+# падает на путях вида C:/... — пример в комментарии своего же workflow\n"
    )
    pairs = parse_diff(diff)
    assert len(pairs) == 5, pairs                      # пять добавленных строк
    bad = violations_in(pairs)
    assert len(bad) == 1, bad                          # только путь с диска
    assert bad[0][0] == "wiki/sources/x.md", bad       # и не в самом стороже
    assert "C:/my_projects" in bad[0][1], bad

    # Адрес сайта — не диск: без этого правило краснело бы на каждой ссылке.
    assert violations_in([("a.md", "см. https://claude.com/docs")]) == []
    assert violations_in([("a.md", "путь raw/web-clipped/статья.md")]) == []
    # Оба написания разделителя и обе домашние папки — находка.
    for line in (r"C:\my_projects\jarvis", "C:/Users/кто-то", "/home/user/.claude", "/c/my_x"):
        assert violations_in([("a.md", line)]), line

    # Объявленное исключение снимает отказ, но только в квадратных скобках.
    def decide(bad_found, msg):
        return bool(bad_found) and MARKER not in msg
    assert decide(bad, "wiki: разбор источника") is True
    assert decide(bad, f"practices: пример пути {MARKER}") is False
    assert decide(bad, "practices: путь осознанно") is True
    assert decide([], "любое сообщение") is False

    print("Самопроверка сторожа личного: пройдена.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
