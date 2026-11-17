"""Сверка столбца «Где стоит» в wiki/practices/modeli.md с настройками проектов.

Модель со статусом «в деле» и заполненным «Где стоит» обязана быть названа в
каждом указанном файле. Повод — 17.11.2026: таблица держала `qwen3:4b` и
`bge-m3` моделями бота, хотя бот перешёл на другие ещё 03–04.11. Таблица —
представление настроек проектов, а представление без сверки разъезжается с
источником (правило «Представление не поддерживают параллельно с источником»).

Запись в ячейке: `проект:путь/внутри` (проект — id из реестра проектов) или
`~/путь` (от домашней папки). Несколько записей — через запятую.

Сверка локальная: проекты лежат на диске этой машины, рутинам GitHub их не
видно. Поэтому это отчёт для сессии, а не сторож в CI.

Коды выхода: 0 — всё сверено и совпало; 1 — расхождение (модели нет в файле
или файла нет); 2 — сверить было нечего или нечем (нет реестра, нет таблицы,
ноль записей): «чисто» без осмотра не бывает.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PAGE = ROOT / "wiki" / "practices" / "modeli.md"
CODE = re.compile(r"`([^`]+)`")
LINK_TEXT = re.compile(r"\[([^\]]+)\]")


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def model_token(cell):
    """Что искать в файле: первое имя в `коде`, иначе текст ссылки."""
    m = CODE.search(cell) or LINK_TEXT.search(cell)
    return m.group(1).strip("`") if m else None


def rows(text):
    """(модель, статус, где) по всем таблицам, где есть столбцы «Статус» и «Где стоит»."""
    out, head = [], None
    for line in text.splitlines():
        if not line.lstrip().startswith("|"):
            head = None
            continue
        c = cells(line)
        if head is None:
            head = c if "Где стоит" in c and "Статус" in c else []
            continue
        if not head or set(line.replace("|", "").strip()) <= set("-: "):
            continue
        r = dict(zip(head, c))
        out.append((r.get("Модель", ""), r.get("Статус", ""), r.get("Где стоит", "")))
    return out


def resolve(entry, projects):
    if entry.startswith("~/"):
        return Path.home() / entry[2:]
    proj, _, rel = entry.partition(":")
    return Path(projects[proj]) / rel if proj in projects and rel else None


def check(text, projects):
    """Список (ок, сообщение) по каждой записи «Где стоит» у моделей «в деле»."""
    res = []
    for model, status, where in rows(text):
        if "в деле" not in status.lower():
            continue
        entries = CODE.findall(where)
        if not entries:
            continue
        token = model_token(model)
        if not token:
            res.append((False, f"{model}: нет имени модели для поиска"))
            continue
        for e in entries:
            path = resolve(e, projects)
            if path is None:
                res.append((False, f"{token}: «{e}» — проект не найден в реестре"))
            elif not path.is_file():
                res.append((False, f"{token}: {e} — файла нет"))
            # shortcut: ищем имя в любом месте файла, включая комментарии — старое имя
            # в комментарии даст ложное «совпало»; перейти на разбор настроек, если такое случится
            elif token.lower() not in path.read_text(encoding="utf-8", errors="replace").lower():
                res.append((False, f"{token}: в {e} не найдено — таблица отстала от проекта?"))
            else:
                res.append((True, f"{token}: {e}"))
    return res


def load_projects():
    sys.path.insert(0, str(Path.home() / "bin"))
    try:
        import reestr
        return {p["id"]: p["path"] for p in reestr.zagruzit()["projects"]}
    except Exception as e:  # нет реестра на этой машине — сверить нечем
        print(f"реестр проектов не прочитан: {e}")
        return None


def self_test():
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        (d / "cfg.py").write_text('model = "bonsai-2:4b"\n', encoding="utf-8")
        page = (
            "| Модель | Статус | Где стоит |\n|---|---|---|\n"
            "| [`bonsai-2:4b`](x.md) | **в деле** | `p:cfg.py` |\n"
            "| `qwen3:4b` | **в деле** | `p:cfg.py` |\n"
            "| `qwen3:8b` | запас | `p:cfg.py` |\n"
            "| [GigaAM](g.md) (рус.) | **в деле** | `p:nofile.py`, `zz:cfg.py` |\n"
            "| `x` | **в деле** | — |\n"
        )
        r = check(page, {"p": str(d)})
        assert [ok for ok, _ in r] == [True, False, False, False], r  # запас и «—» не сверяются
        assert "не найдено" in r[1][1] and "файла нет" in r[2][1] and "реестре" in r[3][1], r
        assert model_token("[GigaAM](g.md) (рус.)") == "GigaAM"
    print("self-test ok")


def main():
    if "--self-test" in sys.argv:
        return self_test()
    if not PAGE.is_file():
        print(f"нет таблицы {PAGE.relative_to(ROOT)}")
        return 2
    projects = load_projects()
    if projects is None:
        return 2
    res = check(PAGE.read_text(encoding="utf-8"), projects)
    for ok, msg in res:
        print(("ok   " if ok else "РАСХ ") + msg)
    if not res:
        print("сверено 0 записей — «чисто» не объявляется")
        return 2
    bad = sum(not ok for ok, _ in res)
    print(f"сверено {len(res)}, расхождений {bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main() or 0)
