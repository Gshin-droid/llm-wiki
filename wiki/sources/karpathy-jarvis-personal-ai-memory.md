# Метод Карпати: Claude Code + Obsidian как персональная AI-память

**Источник:** [gomymy64.github.io/jarvis-memory](https://gomymy64.github.io/jarvis-memory/#steps) ("Claude Code + Obsidian ВЗОРВАЛИ Интернет | Метод Андрея Карпати")
**Загружено:** 2026-07-07
**Raw:** `raw/sources/karpathy-jarvis-claude-obsidian.md`

## Саммари

Гайд описывает построение персональной системы памяти "Jarvis": Claude Code постепенно строит и поддерживает персистентную вики в Obsidian вместо классического RAG (загрузка файлов → извлечение фрагментов по запросу без накопления). Ключевая идея — знания компилируются один раз и живут в виде взаимосвязанных markdown-страниц, которые Claude сам обновляет при появлении новых источников.

**Важно:** это тот же паттерн, по которому построена текущая вики (`C:\jarvis`) — фактически данный источник является первоисточником для [[CLAUDE.md]]-схемы, которая уже была применена при инициализации этого vault'а.

## Пять ключевых навыков
- Построение базы знаний под цели и стратегии пользователя
- Web scraping — превращение URL в текст/изображения/сущности
- Интеграция с браузером через Web Clipper
- Генерация synthesis-документов
- Понимание, когда использовать Obsidian vs Pinecone vs NotebookLM

## Стек инструментов (8 частей)
[[obsidian]], [[antigravity-ide]], [[claude-code]], [[obsidian-web-clipper]], [[pinecone]], [[notebooklm]], Karpathy's Gist, статья на Habr.

## 8 шагов внедрения
1. Установить Obsidian, включить Dark Mode
2. Создать папку Jarvis, открыть в Antigravity, запустить Claude
3. Задать Claude системные промпты с правилами вики и структурой папок
4. Дать первый источник — Claude скрейпит и создаёт первые wiki-страницы
5. Установить Web Clipper, настроить vault и шаблон
6. Подключить папку к Obsidian как vault, посмотреть граф
7. Задать synthesis-вопрос — Claude сохраняет ответ в `wiki/synthesis/`
8. При масштабировании — подключить Pinecone (большие архивы) и NotebookLM (deep research)

## Архитектура (три слоя)
См. [[persistent-wiki-pattern]] — Raw Sources (неизменяемые) → Wiki (генерируемая Claude) → Schema (CLAUDE.md).

## Операции
См. [[ingest-query-lint]] — Ingest / Query / Lint.

## Связанные страницы
- Концепты: [[persistent-wiki-pattern]], [[ingest-query-lint]]
- Сущности: [[andrej-karpathy]], [[claude-code]], [[obsidian]], [[antigravity-ide]], [[obsidian-web-clipper]], [[pinecone]], [[notebooklm]]
- Проект: [[jarvis-personal-wiki]]
