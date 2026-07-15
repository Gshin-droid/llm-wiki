# Agent SDK overview (официальная документация)

**URL:** https://code.claude.com/docs/en/agent-sdk/overview (редиректы: docs.claude.com → platform.claude.com → code.claude.com)
**Загружено:** 2026-07-09 (автономный ежедневный запуск)
**Тип фиксации:** содержимое получено через WebFetch, страница отдала markdown практически как есть (документация в формате Mintlify).

## Полный текст страницы (как получен инструментом)

> Build production AI agents with Claude Code as a library

Build AI agents that autonomously read files, run commands, search the web, edit code, and more. The Agent SDK gives you the same tools, agent loop, and context management that power Claude Code, programmable in Python and TypeScript.

### Get started
- TypeScript: `npm install @anthropic-ai/claude-agent-sdk` (bundles a native Claude Code binary as optional dependency — Claude Code CLI не нужен отдельно).
- Python: `pip install claude-agent-sdk`, требует Python 3.10+.
- Аутентификация: `ANTHROPIC_API_KEY` (Console) либо через Bedrock (`CLAUDE_CODE_USE_BEDROCK=1`), Claude Platform on AWS (`CLAUDE_CODE_USE_ANTHROPIC_AWS=1`), Google Vertex (`CLAUDE_CODE_USE_VERTEX=1`), Microsoft Foundry (`CLAUDE_CODE_USE_FOUNDRY=1`).
- Явное ограничение: "Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK."

### Capabilities (та же функциональность, что в Claude Code)
- **Built-in tools**: Read, Write, Edit, Bash, Monitor (наблюдение за фоновым скриптом построчно), Glob, Grep, WebSearch, WebFetch, AskUserQuestion.
- **Hooks**: PreToolUse, PostToolUse, Stop, SessionStart, SessionEnd, UserPromptSubmit и др. — колбэки для валидации/логирования/блокировки/трансформации поведения агента.
- **Subagents**: определяются через `AgentDefinition`/`agents` опцию, вызываются через инструмент `Agent` (должен быть в `allowed_tools`); сообщения из контекста субагента несут `parent_tool_use_id`.
- **MCP**: подключение внешних систем (БД, браузеры, API — сотни готовых серверов) через `mcp_servers` опцию; пример — Playwright MCP для браузерной автоматизации.
- **Permissions**: `allowed_tools` — тонкий контроль, какие инструменты агент может использовать без вопросов.
- **Sessions**: контекст сохраняется между обращениями; `resume=session_id` — продолжить с полным контекстом; можно форкать сессии для разных подходов.

### Поддержка файловой конфигурации Claude Code
SDK по умолчанию читает `.claude/` в рабочей директории и `~/.claude/` (можно ограничить через `setting_sources`/`settingSources`):
| Feature | Локация |
|---|---|
| Skills | `.claude/skills/*/SKILL.md` |
| Commands (legacy) | `.claude/commands/*.md` |
| Memory | `CLAUDE.md` или `.claude/CLAUDE.md` |
| Plugins | программно, опция `plugins` |

### Сравнение с другими способами работы с Claude
**Agent SDK vs Client SDK (Anthropic Messages API)**: Client SDK — прямой доступ к API, tool loop реализует разработчик сам; Agent SDK — Claude сам управляет tool loop.

**Agent SDK vs Claude Code CLI**: те же возможности, разный интерфейс. CLI — интерактивная разработка, одноразовые задачи. SDK — CI/CD, кастомные приложения, продакшн-автоматизация. Многие команды используют оба: CLI для повседневной разработки, SDK для продакшна; воркфлоу переносятся напрямую между ними.

**Agent SDK vs Managed Agents**: Managed Agents — хостед REST API, Anthropic запускает агента и sandbox, приложение отправляет события и получает стрим результатов. Agent SDK — библиотека, agent loop работает в собственном процессе разработчика.
| | Agent SDK | Managed Agents |
|---|---|---|
| Runs in | свой процесс/инфраструктура | инфраструктура Anthropic |
| Интерфейс | Python/TypeScript библиотека | REST API |
| Agent работает над | файлами своей инфраструктуры | managed sandbox на сессию |
| Session state | JSONL на своей файловой системе | hosted event log у Anthropic |
| Custom tools | in-process функции | Claude триггерит, вызывающая сторона исполняет и возвращает результат |
| Best for | локальный прототип, агенты, работающие напрямую с файловой системой/сервисами | продакшн-агенты без операционного sandbox/session-инфраструктуры, долгоживущие асинхронные сессии |

Типичный путь: прототип на Agent SDK локально → продакшн на Managed Agents.

### Changelog / issues
- TypeScript SDK: github.com/anthropics/claude-agent-sdk-typescript
- Python SDK: github.com/anthropics/claude-agent-sdk-python

### Branding guidelines (для партнёров)
Разрешено: "Claude Agent", "Claude" (в уже обозначенном как "Agents" меню), "{ИмяАгента} Powered by Claude". Запрещено: "Claude Code"/"Claude Code Agent" и ASCII-арт/визуальные элементы, имитирующие Claude Code. Продукт не должен выглядеть как сам Claude Code или продукт Anthropic.

### License
Commercial Terms of Service Anthropic, включая использование для продуктов/сервисов для собственных клиентов, кроме компонентов с отдельной лицензией.

## Дополнительный контекст из веб-поиска (не с этой страницы, вторичные источники — только для ориентира, не как факт)
Поиск также вернул вторичные SEO-блоги (totalum.app, devtoolpicks.com, techsy.io и др.) про "билинг Agent SDK меняется с 15 июня 2026" — эта тема НЕ подтверждена официальной страницей выше и не включена в саммари вики как факт, только упомянута как то, что стоит проверить отдельно при необходимости.
