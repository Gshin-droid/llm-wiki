# Claude Managed Agents

**Тип:** продукт (hosted agent harness, часть Claude Developer Platform, beta)
**Актуально на:** 2026-07-24

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
- **Dreams** (research preview) — читает memory store + прошлые транскрипты сессий, выдаёт реорганизованную память (merged duplicates, заменённые устаревшие записи, новые инсайты). С 2026-07-10 поддерживает Claude Fable 5 и Claude Sonnet 5 (список поддерживаемых моделей ограничен, актуальный — в официальных доках).

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
- Источники: [[claude-managed-agents-overview]]
- Сущности: [[claude-agent-sdk]], [[claude-code]]
- Концепты: [[claude-memory-tool]] (разграничение client-side memory tool vs server-side memory store), [[mcp-model-context-protocol]] (MCP-серверы как один из tool-типов)
