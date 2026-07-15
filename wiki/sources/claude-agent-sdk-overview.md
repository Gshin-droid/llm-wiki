# Agent SDK overview (официальная документация)

**Источник:** [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview) — официальная документация Anthropic
**Загружено:** 2026-07-09
**Raw:** `raw/sources/claude-agent-sdk-overview.md`

## Саммари
Официальная страница документации Claude Agent SDK — библиотеки на Python/TypeScript, дающей программный доступ к тому же agent loop, инструментам и context management, что работают внутри [[claude-code]]. Закрывает пробел в вики: тема "agentic-паттерны (MCP, Claude Skills, Agent SDK)" была заявлена как одна из ключевых, но у самого Agent SDK до сих пор не было отдельной страницы — он упоминался только через призму Claude Code как продукта.

## Ключевые тезисы
- **Что это:** библиотека (не CLI, не хостед-сервис), которая даёт агенту built-in инструменты (Read/Write/Edit/Bash/Monitor/Glob/Grep/WebSearch/WebFetch/AskUserQuestion) без необходимости самому писать tool execution.
- **Установка:** `npm install @anthropic-ai/claude-agent-sdk` (бандлит нативный бинарник Claude Code) или `pip install claude-agent-sdk` (Python 3.10+).
- **Капабилити "из коробки":** built-in tools, hooks (PreToolUse/PostToolUse/Stop/SessionStart/SessionEnd/UserPromptSubmit и др.), субагенты (`AgentDefinition`, вызов через инструмент `Agent`), MCP (`mcp_servers` опция — пример: Playwright MCP для браузера), permissions (`allowed_tools`), sessions (resume/fork с полным контекстом).
- **Читает те же файлы конфигурации, что Claude Code:** `.claude/skills/*/SKILL.md`, `.claude/commands/*.md` (legacy), `CLAUDE.md`/`.claude/CLAUDE.md`, plugins — из рабочей директории и `~/.claude/`.
- **Три точки сравнения:**
  - vs Anthropic Client SDK (сырой API) — Client SDK заставляет разработчика самому писать tool loop, Agent SDK делает это сам.
  - vs Claude Code CLI — те же возможности, разный интерфейс: CLI для интерактивной разработки и одноразовых задач, SDK для CI/CD и продакшн-автоматизации; воркфлоу переносятся между ними напрямую.
  - vs Managed Agents (хостед REST API Anthropic) — Agent SDK работает в собственном процессе/инфраструктуре разработчика с session state в JSONL на диске; Managed Agents — Anthropic держит sandbox и event log, разработчик только исполняет tool calls. Типичный путь: прототип на Agent SDK → продакшн на Managed Agents.
- **Аутентификация** не только через `ANTHROPIC_API_KEY`, но и Bedrock/Claude Platform on AWS/Vertex/Azure Foundry. Явно запрещено third-party продуктам предлагать вход через claude.ai или использовать лимиты claude.ai-подписки — только API key.
- **Branding:** партнёрам разрешено называть "Claude Agent"/"Claude" внутри своего продукта, запрещено называться "Claude Code" или имитировать его брендинг.

## Не подтверждено (отфильтровано)
Веб-поиск также вернул вторичные SEO-блоги, утверждающие про смену биллинга Agent SDK с 15 июня 2026 года (метрика отдельно от интерактивного Claude Code). Это НЕ встречается на официальной странице документации и не включено как факт — только зафиксировано как то, что стоит проверить отдельно через platform.claude.com/docs (pricing), если станет актуально.

## Связанные страницы
- Сущность: [[claude-agent-sdk]] — новая карточка продукта
- Концепт: [[mcp-model-context-protocol]] — MCP как одна из капабилити SDK
- Сущность: [[claude-code]] — общий harness, отличия CLI vs SDK
