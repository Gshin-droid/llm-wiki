# Claude Managed Agents

**Тип:** продукт (hosted agent harness, часть Claude Developer Platform, beta)
**Актуально на:** 2026-08-04

## Что это
Полностью управляемый Anthropic harness для запуска Claude как автономного агента: sandbox, event log и agent loop уже готовы на стороне Anthropic, разработчик только определяет агента (модель/system prompt/tools/MCP/skills) и обменивается событиями через REST API + Server-Sent Events. В отличие от [[claude-agent-sdk]] — не библиотека для встраивания в свою инфраструктуру, а хостед-сервис: своей инфраструктуры/sandbox строить не нужно.

## Четыре примитива
- **Agent** — модель, system prompt, tools, MCP-серверы, skills; создаётся один раз, версионируется, переиспользуется в разных сессиях.
- **Environment** — где исполняется: cloud sandbox (управляется Anthropic) или self-hosted sandbox (своя инфраструктура, для compliance/резидентности данных).
- **Session** — конкретный запущенный инстанс агента в рамках environment, решает конкретную задачу.
- **Events** — обмен сообщениями между приложением и агентом (user turns, tool results, status updates) через SSE-поток; история персистится на сервере.

## Когда использовать (вместо Agent SDK / Messages API)
Долгие задачи (минуты-часы, много вызовов инструментов), нужна managed-инфраструктура без своего sandbox, self-hosted sandbox под compliance, cron-расписание сессий (scheduled deployments) без своего планировщика, stateful-сессии с персистентным файловым состоянием между обращениями.

Типичный путь развития продукта: прототип на [[claude-agent-sdk|Agent SDK]] (свой процесс и инфраструктура) → продакшн на Managed Agents (инфраструктура и sandbox у Anthropic).

## Экосистема вокруг ядра
- **Memory** (`memory_stores` REST API, beta с 2026-04-23) — server-side память агента, отдельная от client-side [[claude-memory-tool|memory tool]] обычного Messages API. С 2026-07-02 у memory-эндпоинтов свой beta-заголовок `agent-memory-2026-07-22` (стабильный порядок листинга, ограничения на `depth`/`path_prefix`), отдельно от общего `managed-agents-2026-04-01`.
- **Multiagent orchestration** и **Outcomes** — public beta с 2026-05-06.
- **Self-hosted sandboxes** — с 2026-05-19, sandbox на своей инфраструктуре вместо инфраструктуры Anthropic.
- **Scheduled deployments** — сессии по cron-расписанию без своего планировщика.
- **Webhooks** — события жизненного цикла agent/deployment/deployment run (публикация новой версии, пауза деплоя, упавший scheduled run) — без polling.
- **Vaults** — секьюрное внедрение credentials (env vars) в sandbox агента. С 2026-06-30 у env var credential есть настройка `injection_location` — куда именно подставляется значение на выходе (заголовки исходящего запроса, тело запроса, или оба места).
- **Dreams** (research preview) — читает memory store + прошлые транскрипты сессий, выдаёт реорганизованную память (merged duplicates, заменённые устаревшие записи, новые инсайты). С 2026-07-10 поддерживает Claude Fable 5 и Claude Sonnet 5, с 2026-08-01 — также Claude Opus 5 (список поддерживаемых моделей ограничен, актуальный — в официальных доках).

## Обновления с 2026-06-30 (найдено при lint-проходе 2026-07-21, official release notes)
Точечные API-возможности, добавленные после первоначального ingest страницы (2026-07-15), не покрытые тем снапшотом:
- **Event deltas** в потоке событий сессии (`event_deltas[]` параметр на `GET /v1/sessions/{id}/events/stream`) — события `event_start`/`event_delta` показывают текст ответа агента по мере генерации, до прихода полного `agent.message`.
- **Backward pagination** для списка сессий — `GET /v1/sessions` теперь возвращает `prev_page` курсор рядом с `next_page`.
- **Override конфигурации агента на уровне сессии** — при создании сессии можно передать `agent` с `type: "agent_with_overrides"`, заменив модель/system prompt/tools/MCP/skills только для этой сессии, не трогая сам объект агента.

## Обновления с 2026-07-22 (закрыто 2026-07-24, ежедневное закрытие пробелов, официальные release notes)
Продолжение того же отставания, что и раздел выше (страница создана 2026-07-15, официальные release notes с тех пор пополнились новой партией точечных изменений):
- **Event deltas теперь и на уровне отдельного subagent-потока** — `GET /v1/sessions/{id}/threads/{thread_id}/stream` принимает тот же параметр `event_deltas[]`, что и потоковая выдача на уровне сессии (добавлена 2026-06-30, см. раздел выше) — можно превью-стримить текст конкретного субагента, не всей сессии сразу.
- **`effort` в конфигурации модели агента** — уровень effort (см. [[claude-code|effort в Claude Code]]) теперь настраивается прямо в объекте `model` при создании агента, а не только через сам Messages API.
- **Webhooks расширены на environment/memory store** — 4 новых `environment.*` события и 3 `memory_store.*` события; ранее webhooks покрывали только agent/deployment/deployment run (2026-05-06) и session/vault (2026-05-06, самый первый набор) — теперь весь основной жизненный цикл ресурсов события покрыт.
- **`initial_events` при создании сессии** — можно сразу передать до 50 событий `user.message`/`user.define_outcome` в `POST /v1/sessions`; если список непустой, agent loop стартует в том же вызове, без отдельного запроса на отправку событий.
- **`version` необязателен при обновлении агента** — если передан, работает как optimistic concurrency (несовпадение → 409); если не передан, обновление применяется безусловно.
- Попутно подтверждено: `managed-agents-2026-04-01` (общий beta-заголовок) с 2026-07-22 сам перенял поведение листинга памяти, ранее доступное только под `agent-memory-2026-07-22` (см. раздел "Memory" выше, запись от 2026-07-02) — де-факто расхождение между двумя заголовками для memory-эндпоинтов закрылось.

## Допроверка 2026-08-04 (ежедневное закрытие пробелов, официальные release notes)
Третий визит к этой странице после отставаний 07-21 и 07-24 (см. разделы выше) — по прецеденту закрытых пунктов бэклога 07-22…07-27, где допроверка страниц с историей отставания от `platform.claude.com/docs/en/release-notes/overview` регулярно давала находки. Полный перечень release notes с 2026-06-30 по 2026-08-01 проверен построчно. Единственная запись, затрагивающая Managed Agents, с прошлой проверки (07-22) — **1 августа 2026**: Dreams (research preview) добавил поддержку Claude Opus 5 (учтено в разделе "Экосистема вокруг ядра" выше). Остальные записи между 07-22 и 08-01 — про модели/эффорт/fallback общей платформы, Managed Agents не касаются. Отставания документации от продукта на этот раз не найдено — release notes актуальны на момент проверки.

## Cookbook: production-паттерн и memory stores (2026-08-19, официальный репозиторий)

Первый разбор пункта бэклога «Managed Agents cookbooks» — два notebook'а из `anthropics/claude-cookbooks/managed_agents/` ([[claude-cookbook-managed-agents-production-memory]]), остальные 14 из 16 гайдовых + 3 applied-примера ещё не разобраны.

**Production-паттерн (`CMA_operate_in_production`).** Вместо удержания SSE-соединения — webhook в консоли (Settings → Webhooks) на `session.status_idled` (агент закончил или ждёт результата тула) и `session.budget_reached` (упёрлись в бюджет сессии). Верификация подписи — заголовок `x_anthropic_signature`, HMAC-SHA256 с секретом `whsec_...`. Human-in-the-loop: кастомный тул `escalate()` останавливает сессию в `idled`, обработчик находит необработанный `agent.custom_tool_use` с именем `escalate` в событиях, после решения человека шлёт `user.custom_tool_result` с тем же `custom_tool_use_id`. MCP toolsets вызываются агентом «no round-trip through your application» — без прохода через приложение разработчика. Все ресурсы (не только agent) поддерживают `list`/`retrieve`/`update`/`archive`/`delete`, `update` — optimistic concurrency через `version`.

**Memory stores (`CMA_remember_user_preferences`), уточнение раздела «Экосистема» выше.** Store — «named container for text files, scoped to your workspace» (per-workspace, не per-agent/per-session); типовой продакшн-паттерн — своя БД с маппингом user_id → store_id. Монтируется через `resources: [{"type": "memory_store", "memory_store_id": ..., "access": ..., "instructions": ...}]`, видна агенту как директория `/mnt/memory/{store-name}`; агент читает/пишет обычными файловыми тулами, без отдельного memory-протокола (в отличие от client-side [[claude-memory-tool]] с явными шестью командами). Приложение — через REST: `memory_stores.memories.list(store_id, view="full")`, `memory_stores.memories.create(store_id, path=..., content=...)` для сидирования. Версии иммутабельны (`memory_stores.memory_versions.list`) — аудит и ручная коррекция вне агента. `description` store попадает в системный промпт агента.

## Практический пример (Python SDK)
```python
from anthropic import Anthropic
client = Anthropic()

agent = client.beta.agents.create(
    name="Coding Assistant",
    model="claude-opus-4-8",
    system="You are a helpful coding assistant.",
    tools=[{"type": "agent_toolset_20260401"}],
)
environment = client.beta.environments.create(
    name="env", config={"type": "cloud", "networking": {"type": "unrestricted"}},
)
session = client.beta.sessions.create(agent=agent.id, environment_id=environment.id)

with client.beta.sessions.events.stream(session.id) as stream:
    client.beta.sessions.events.send(session.id, events=[{
        "type": "user.message",
        "content": [{"type": "text", "text": "..."}],
    }])
    for event in stream:
        if event.type == "session.status_idle":
            break
```
Тот же официальный SDK (`anthropic` / `@anthropic-ai/sdk`), что и для обычного Messages API — просто другой namespace (`client.beta.agents/environments/sessions`).

## Ограничения
Beta-статус (заголовки `managed-agents-2026-04-01` / `agent-memory-2026-07-22`). Stateful по дизайну (session state хранится на сервере Anthropic) — из-за этого **не подходит под Zero Data Retention и HIPAA BAA**. MCP tunnels и Dreams — более узкий research preview, нужен отдельный запрос доступа.

## Связи
- Источники: [[claude-managed-agents-overview]], [[claude-cookbook-managed-agents-production-memory]]
- Сущности: [[claude-agent-sdk]], [[claude-code]]
- Концепты: [[claude-memory-tool]] (разграничение client-side memory tool vs server-side memory store), [[mcp-model-context-protocol]] (MCP-серверы как один из tool-типов)
