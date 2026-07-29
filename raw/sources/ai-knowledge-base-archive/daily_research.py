"""
daily_research.py
Ежедневный сбор новостей по темам через notebooklm-py.
Вся тяжёлая работа (поиск + анализ) идёт на стороне NotebookLM/Gemini,
скрипт только дёргает CLI и раскладывает результат по vault.

Использование:
    python daily_research.py

Настройка: впишите NOTEBOOK_ID и список TOPICS ниже.
"""

import subprocess
import datetime
import pathlib

# === НАСТРОЙКИ — впишите свои значения ===
NOTEBOOK_ID = "ad5925c7-4123-4988-a008-af4b073f7e82"
VAULT_INBOX = pathlib.Path(r"C:\ai-knowledge-base\00_Inbox")

TOPICS = [
    "новости agentic coding и AI-агентов за последнюю неделю",
    "обновления Claude Code, Cursor, vibe coding инструментов",
    "новые модели и релизы крупных LLM",
    "новости про Model Context Protocol (MCP)",
]
# ==========================================


def run(cmd: list[str]) -> str:
    """Запускает CLI-команду notebooklm и возвращает stdout."""
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if result.returncode != 0:
        print(f"[ОШИБКА] {' '.join(cmd)}\n{result.stderr}")
    return result.stdout


def main():
    today = datetime.date.today().isoformat()
    report_parts = [f"---\ntitle: Новостной дайджест\ncreated: {today}\nstatus: to-process\n---\n"]
    report_parts.append(f"# Дайджест ИИ + Vibe Coding — {today}\n")

    for topic in TOPICS:
        print(f"Исследую: {topic}")
        # Запускаем быстрый веб-research (блокирующий, ждёт и импортирует источники)
        run([
            "notebooklm", "source", "add-research", topic,
            "--notebook", NOTEBOOK_ID,
            "--mode", "fast",
        ])

        # Просим NotebookLM подготовить сжатую сводку по свежедобавленным источникам
        answer = run([
            "notebooklm", "ask",
            f"Сделай сжатую сводку (5-8 пунктов) по теме '{topic}' "
            f"на основе только что добавленных источников. "
            f"Для каждого пункта: факт, почему важно, источник.",
            "--notebook", NOTEBOOK_ID,
        ])

        if not answer.strip():
            print(f"  [ВНИМАНИЕ] пустой ответ по теме '{topic}' — проверьте вывод [ОШИБКА] выше")
            answer = "_(не удалось получить сводку — см. лог запуска)_"
        else:
            print(f"  получено {len(answer)} символов")

        report_parts.append(f"## {topic}\n\n{answer}\n")

    report_text = "\n".join(report_parts)
    VAULT_INBOX.mkdir(parents=True, exist_ok=True)
    out_file = VAULT_INBOX / f"{today}_news-digest.md"
    out_file.write_text(report_text, encoding="utf-8")
    print(f"Готово: {out_file}")


if __name__ == "__main__":
    main()
