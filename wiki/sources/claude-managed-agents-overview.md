# Claude Managed Agents overview + quickstart (официальная документация)

**Источник:** [Managed Agents overview](https://platform.claude.com/docs/en/managed-agents/overview), [Quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart) — официальная документация Claude Developer Platform
**Загружено:** 2026-07-15
**Raw:** `raw/sources/claude-managed-agents-overview.md`

## Саммари
Закрывает явно зафиксированный пробел в вики: [[claude-agent-sdk]] и [[claude-agent-sdk-overview]] уже упоминали Managed Agents как "хостед REST API Anthropic, отдельно не разобран в вики" — теперь разобран. Это второй официальный способ строить агента на Claude API (наряду с сырым Messages API и Agent SDK): не библиотека для встраивания в свою инфраструктуру, а полностью управляемый Anthropic harness — sandbox, event log, agent loop уже готовы, разработчик только определяет агента и обменивается событиями через REST/SSE.

## Ключевые тезисы
- **Четыре примитива**: Agent (модель + system prompt + tools + MCP + skills, версионируется), Environment (где исполняется — cloud sandbox или self-hosted), Session (конкретный запущенный инстанс агента), Events (обмен сообщениями user/agent через SSE, персистится на сервере).
- **Цикл использования**: создать агента → создать environment → создать session (ссылается на agent+environment) → слать user-события в поток → получать agent.message/agent.tool_use/session.status_idle события → при необходимости слать доп. события мид-execution (steering) или прерывать.
- **Когда использовать вместо Agent SDK**: долгие задачи (минуты-часы, много tool calls), нужна managed cloud-инфраструктура без своего sandbox, self-hosted sandbox для compliance/резидентности данных, cron-расписание сессий (scheduled deployments) без своего планировщика. Подтверждает гипотезу, уже зафиксированную в [[claude-agent-sdk]]: типичный путь — прототип на Agent SDK (свой процесс) → продакшн на Managed Agents (managed sandbox).
- **Практический пример** (Python): `client.beta.agents.create(...)` → `client.beta.environments.create(config={"type": "cloud", ...})` → `client.beta.sessions.create(agent=agent.id, environment_id=environment.id)` → `client.beta.sessions.events.stream(session.id)` + `.send(...)`. Тот же официальный SDK (`anthropic` / `@anthropic-ai/sdk`), что и для обычного Messages API, просто другой namespace (`client.beta.*`).
- **Инструменты из коробки**: `agent_toolset_20260401` включает весь набор (bash, file ops, web search/fetch); плюс MCP-серверы для внешних систем.
- **Beta-статус**: требует заголовок `managed-agents-2026-04-01` почти везде, кроме memory store endpoints — там с 2026-07-02 отдельный `agent-memory-2026-07-22`. Не подходит под Zero Data Retention/HIPAA BAA, потому что stateful по дизайну (session state хранится на сервере Anthropic).
- **Экосистема фич вокруг ядра** (из release notes, апрель–июль 2026): память для агентов (`memory_stores` API — отдельная сущность от client-side memory tool `memory_20250818` в обычном Messages API, см. [[claude-memory-tool]]), multiagent orchestration, self-hosted sandboxes, scheduled deployments, webhooks на lifecycle событий, vaults для credentials, Dreams (реорганизация памяти между сессиями — читает transcript + memory store, выдаёт merged/deduplicated версию).

## Отличие от уже описанного в вики
- vs [[claude-agent-sdk]] — SDK работает в процессе разработчика (своя инфраструктура, session state в JSONL на диске); Managed Agents — инфраструктура и sandbox у Anthropic, доступ через REST/SSE.
- vs [[claude-memory-tool]] — тот memory tool клиент-сайд (агент сам вызывает view/create/str_replace через Messages API, разработчик хранит файлы у себя); memory здесь — server-side `memory_stores` REST API, часть managed-инфраструктуры, с собственным версионированием заголовков.
- vs [[claude-code]] / [[claude-agent-sdk]] — не для интерактивной разработки и не для встраивания в свой процесс, а для продакшн-агентов, которым нужна managed-инфраструктура (например: бэкенд-сервис, который асинхронно порождает долгоживущие агентские задачи по запросу пользователей).

## Связанные страницы
- Создана сущность: [[claude-managed-agents]]
- Обновлена: [[claude-agent-sdk]] (снята пометка "отдельно не разобран в вики", добавлена ссылка)
- Концепт: [[claude-memory-tool]] (разграничение client-side memory tool vs server-side memory store)
