# Claude Agent SDK

**Тип:** инструмент (библиотека Python/TypeScript от Anthropic)
**Актуально на:** 2026-07-15

## Что это
Библиотека, дающая программный доступ к тому же agent loop, встроенным инструментам и context management, что работают внутри [[claude-code]] — "Claude Code как библиотека". В отличие от CLI, встраивается в собственное приложение разработчика: свой процесс, своя инфраструктура, session state в JSONL на диске.

```python
from claude_agent_sdk import query, ClaudeAgentOptions
async for message in query(prompt="Find and fix the bug in auth.py",
                            options=ClaudeAgentOptions(allowed_tools=["Read", "Edit", "Bash"])):
    print(message)
```

## Место среди способов работать с Claude
Три соседних инструмента, которые легко перепутать:
- **[[claude-code]] (CLI)** — интерактивная разработка в терминале, одноразовые задачи.
- **Claude Agent SDK (эта страница)** — библиотека для встраивания в CI/CD и собственные продакшн-приложения; те же возможности, что у CLI, воркфлоу переносятся напрямую.
- **[[claude-managed-agents|Managed Agents]]** (хостед REST API — разобран отдельно 2026-07-15) — Anthropic сам держит sandbox и event log, приложение только исполняет tool calls, которые триггерит Claude. Типичный путь развития: прототип на Agent SDK → продакшн на Managed Agents.
- **Anthropic Client SDK** (сырой Messages API) — самый низкий уровень: разработчик сам пишет tool loop; Agent SDK берёт это на себя.

## Капабилити из коробки
- **Built-in tools**: Read, Write, Edit, Bash, Monitor, Glob, Grep, WebSearch, WebFetch, AskUserQuestion.
- **Hooks**: PreToolUse, PostToolUse, Stop, SessionStart, SessionEnd, UserPromptSubmit и др. — колбэки для контроля поведения агента.
- **Субагенты**: `AgentDefinition`, вызываются через инструмент `Agent`.
- **[[mcp-model-context-protocol|MCP]]**: подключение внешних систем через `mcp_servers` — то же самое поле, что у Claude Code CLI.
- **Permissions**: `allowed_tools` — тонкий контроль без диалоговых запросов.
- **Sessions**: resume/fork с полным контекстом.
- Читает ту же файловую конфигурацию, что Claude Code: `.claude/skills/`, `CLAUDE.md`, plugins — из рабочей директории и `~/.claude/`.

## Установка и аутентификация
`npm install @anthropic-ai/claude-agent-sdk` (TypeScript, бандлит нативный бинарник Claude Code) или `pip install claude-agent-sdk` (Python 3.10+). Аутентификация — `ANTHROPIC_API_KEY`, либо Bedrock/Claude Platform on AWS/Google Vertex/Azure Foundry. Явный запрет: сторонним продуктам на Agent SDK нельзя предлагать вход через claude.ai или использовать лимиты подписки claude.ai — только API-ключ (то есть биллинг для SDK принципиально отдельный от Pro/Max, о которых идёт речь в [[claude-code]]).

## Паттерны поверх SDK: долгоживущие агенты и память
Два официальных паттерна строятся прямо на капабилити выше и относятся к любому агенту на SDK (не только к Claude Code CLI):
- **[[claude-memory-tool]]** — тот же принцип "файлы вместо контекста", но как встроенный тул Messages API (`memory_20250818`) — не нужно даже писать собственный `Read`/`Write`-based механизм.
- **[[long-running-agent-harness]]** — три примитива для многосессионной работы поверх уже перечисленных Hooks/Субагентов: Default-FAIL Contract через `PreToolUse`, Fresh-Context Evaluator через отдельный `query()`-вызов без Write/Edit, Agent-Maintained Handoff через `Stop`-хук + git.

## Закрытый пробел: биллинг Agent SDK с 15 июня 2026 (было "Открытый вопрос", проверено 2026-07-15)
Ранее здесь стоял открытый вопрос: вторичные статьи утверждали, что с 15.06.2026 метрика Agent SDK/`claude -p` отделена от лимитов подписки Claude Code. Проверка через официальные источники ([Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview) на 15 июня 2026 — запись только про ретайр моделей Sonnet 4/Opus 4, ни слова про биллинг; [официальный Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview) — тоже не упоминает разделение) **не подтвердила заявленное изменение как вступившее в силу**. Ретроспективно вторичные источники (независимо друг от друга — codersera, digitalapplied, vantagepoint, usagebox, pravinkumar и др.) сходятся на одном и том же уточнении: Anthropic анонсировала разделение биллинга 14 мая 2026 (отдельный доллар-номинированный кредит для Pro/Max/Team/Enterprise: ~$20/$100/$200 в месяц), но **поставила изменение на паузу 15 июня 2026** — то есть в день, когда оно должно было вступить в силу. Anthropic Agent SDK/`claude -p`/сторонние приложения по факту продолжают тянуть из лимитов подписки, как и раньше; обещанный отдельный кредит не выдаётся, пока Anthropic не объявит новую дату.

**Оговорка о степени проверки:** прямой источник этого уточнения — официальный Claude Help Center (`support.claude.com`), но статья вернула 403 при попытке прямого фетча (похоже на бот-защиту, не пейволл) — факт восстановлен по независимому совпадению нескольких вторичных пересказов одной и той же официальной формулировки, не по собственному прочтению первоисточника. Не путать с фактом на строке выше ("биллинг для SDK принципиально отдельный от Pro/Max") — та фраза о другом: сторонним продуктам на Agent SDK по ToS запрещено предлагать своим конечным пользователям вход через claude.ai/лимиты подписки (обязаны использовать API-ключ) — это ограничение действовало и продолжает действовать независимо от истории с паузой 15 июня, которая касалась личного использования Agent SDK/`claude -p` разработчиком под собственным Pro/Max.

См. также `wiki/gaps-backlog.md` — пункт 1 закрыт этой записью.

## Связи
- Источники: [[claude-agent-sdk-overview]]
- Сущности: [[claude-code]], [[claude-managed-agents]]
- Концепты: [[mcp-model-context-protocol]]
