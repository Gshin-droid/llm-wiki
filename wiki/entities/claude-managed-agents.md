# Claude Managed Agents

**Тип:** продукт (hosted agent harness, часть Claude Developer Platform, beta)
**Актуально на:** 2026-08-24

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
- **Webhooks расширены на environment/memory store** — 4 новых `environment.*` события и 3 `memory_store.*` события; ранее webhooks покрывали только agent/deployment/deployment run (**2026-06-30**, дата исправлена 2026-08-24 — см. «Противоречия» ниже; было ошибочно записано 2026-05-06) и session/vault (2026-05-06, самый первый набор, подтверждено) — теперь весь основной жизненный цикл ресурсов события покрыт.
- **`initial_events` при создании сессии** — можно сразу передать до 50 событий `user.message`/`user.define_outcome` в `POST /v1/sessions`; если список непустой, agent loop стартует в том же вызове, без отдельного запроса на отправку событий.
- **`version` необязателен при обновлении агента** — если передан, работает как optimistic concurrency (несовпадение → 409); если не передан, обновление применяется безусловно.
- Попутно подтверждено: `managed-agents-2026-04-01` (общий beta-заголовок) с 2026-07-22 сам перенял поведение листинга памяти, ранее доступное только под `agent-memory-2026-07-22` (см. раздел "Memory" выше, запись от 2026-07-02) — де-факто расхождение между двумя заголовками для memory-эндпоинтов закрылось.

## Допроверка 2026-08-04 (ежедневное закрытие пробелов, официальные release notes)
Третий визит к этой странице после отставаний 07-21 и 07-24 (см. разделы выше) — по прецеденту закрытых пунктов бэклога 07-22…07-27, где допроверка страниц с историей отставания от `platform.claude.com/docs/en/release-notes/overview` регулярно давала находки. Полный перечень release notes с 2026-06-30 по 2026-08-01 проверен построчно. Единственная запись, затрагивающая Managed Agents, с прошлой проверки (07-22) — **1 августа 2026**: Dreams (research preview) добавил поддержку Claude Opus 5 (учтено в разделе "Экосистема вокруг ядра" выше). Остальные записи между 07-22 и 08-01 — про модели/эффорт/fallback общей платформы, Managed Agents не касаются. Отставания документации от продукта на этот раз не найдено — release notes актуальны на момент проверки.

## Cookbook: production-паттерн и memory stores (2026-08-19, официальный репозиторий)

Первый разбор пункта бэклога «Managed Agents cookbooks» — два notebook'а из `anthropics/claude-cookbooks/managed_agents/` ([[claude-cookbook-managed-agents-production-memory]]), остальные 14 из 16 гайдовых + 3 applied-примера ещё не разобраны.

**Production-паттерн (`CMA_operate_in_production`).** Вместо удержания SSE-соединения — webhook в консоли (Settings → Webhooks) на `session.status_idled` (агент закончил или ждёт результата тула) и `session.budget_reached` (упёрлись в бюджет сессии). Верификация подписи — заголовок `x_anthropic_signature`, HMAC-SHA256 с секретом `whsec_...`. Human-in-the-loop: кастомный тул `escalate()` останавливает сессию в `idled`, обработчик находит необработанный `agent.custom_tool_use` с именем `escalate` в событиях, после решения человека шлёт `user.custom_tool_result` с тем же `custom_tool_use_id`. MCP toolsets вызываются агентом «no round-trip through your application» — без прохода через приложение разработчика. Все ресурсы (не только agent) поддерживают `list`/`retrieve`/`update`/`archive`/`delete`, `update` — optimistic concurrency через `version`.

**Memory stores (`CMA_remember_user_preferences`), уточнение раздела «Экосистема» выше.** Store — «named container for text files, scoped to your workspace» (per-workspace, не per-agent/per-session); типовой продакшн-паттерн — своя БД с маппингом user_id → store_id. Монтируется через `resources: [{"type": "memory_store", "memory_store_id": ..., "access": ..., "instructions": ...}]`, видна агенту как директория `/mnt/memory/{store-name}`; агент читает/пишет обычными файловыми тулами, без отдельного memory-протокола (в отличие от client-side [[claude-memory-tool]] с явными шестью командами). Приложение — через REST: `memory_stores.memories.list(store_id, view="full")`, `memory_stores.memories.create(store_id, path=..., content=...)` для сидирования. Версии иммутабельны (`memory_stores.memory_versions.list`) — аудит и ручная коррекция вне агента. `description` store попадает в системный промпт агента.

## Cookbook: human-in-the-loop gate и мультиагентная координация (2026-08-20, официальный репозиторий)

Третий и четвёртый notebook'ы того же пункта бэклога ([[claude-cookbook-managed-agents-hitl-multiagent]]).

**Human-in-the-loop (`CMA_gate_human_in_the_loop`).** Расширяет уже известный `escalate()` вторым кастомным тулом `decide()` — для однозначных решений по чётким правилам, `escalate()` остаётся для неоднозначных. Оба — `"type": "custom"`, дают событие `agent.custom_tool_use`, сессия встаёт в `stop_reason.type == "requires_action"`; при нескольких одновременных вызовах ответ трекается набором `responded_to`, чтобы не отправить `user.custom_tool_result` дважды на один `custom_tool_use_id`. Notebook прямо подтверждает, что вебхуки — не отдельный механизм, а замена триггера у того же ответа: «webhooks for production» вместо держащегося SSE-соединения, сам протокол ответа не меняется.

**Multiagent orchestration (`CMA_coordinate_specialist_team`), впервые раскрыт механизм за строкой «public beta с 2026-05-06» выше.** Координатор — обычный agent с параметром `"multiagent": {"type": "coordinator", "agents": [...]}`: роспись специалистов и опциональный advisor задаются в его конфиге. Специалисты — обычные `client.beta.agents.create()` с урезанным под роль toolset'ом (`agent_toolset_20260401`) и структурированным выходом через `send_to_parent` — toolset-скоуп физически не даёт ролям "перетекать" друг в друга (например, ценовой агент без web-доступа не может подсмотреть цены конкурентов). Координатор запускает специалистов параллельно и цепочкой (когда один зависит от находок другого). **Advisor** — отдельный примитив: более сильная модель без своих тулов, вызывается координатором мид-turn как консультация, не полноценный субагент-поток. Новые типы событий: `session.thread_created` (спавн субагента), `agent.thread_message_received` (payload от `send_to_parent`/advisor), `agent.tool_use`. Файлы монтируются `client.beta.files.upload()` в `/mnt/user-data/...`, доступны субагентам как обычные файлы.

## Cookbook: issue→PR workflow и outcome grader (2026-08-21, официальный репозиторий)

Пятый и шестой notebook'ы того же пункта бэклога ([[claude-cookbook-managed-agents-issue-outcome-grader]]).

**Issue→PR workflow (`CMA_orchestrate_issue_to_pr`).** Репозиторий монтируется ресурсом `github_repository` (URL, mount path, токен) или зафикстуренным `file`-ресурсом; `environments.create` с `networking: {"type": "limited", "allow_package_managers": true}` и полем `packages` — сеть ограничена, но пакетные менеджеры разрешены явно (третий вариант сетевой конфигурации рядом с уже известными `unrestricted`/`strictAllowlist` из [[claude-code]]). Восстановление после сбоя CI — не повтор, а чтение диагностики упавшей проверки и точечная правка по тексту ошибки; тот же паттерн на комментариях ревью-бота. Состояние воркфлоу между турнами живёт в файловой системе контейнера, не в контексте диалога — независимый финальный турн подтверждает результат чтением файла, а не памятью.

**Outcome grader (`CMA_verify_with_outcome_grader`), первое раскрытие примитива Outcomes** (раньше на странице — одна строка "public beta с 2026-05-06", по аналогии с Multiagent orchestration до 08-20). Событие `user.define_outcome` (не отдельный REST-ресурс) задаёт `description` (задача writer'а) и `rubric` (что проверяет grader, `type: "text"`/`"file"`), `max_iterations` (дефолт 3, максимум 20), под тем же бета-заголовком `managed-agents-2026-04-01`. Grade-and-revise: writer пишет артефакт → платформа поднимает **отдельного grader'а с чистым контекстом** (тот же model/tools, но без видимости рассуждений writer'а) → вердикт `satisfied` или список несовпадений по критериям → writer правит → повтор до `satisfied`/`max_iterations_reached`/`failed`/`interrupted`. Изоляция grader'а — не деталь реализации, а сама защита: grader не принимает правку writer'а на слово, проверяет источник заново с нуля. События потока: `span.outcome_evaluation_start`/`span.outcome_evaluation_end` (`result` + `explanation`). Rubric-принципы источника: требовать конкретных цифр, требовать посимвольного совпадения цитаты с фетчем по `web_fetch`, исключать сторонние подтверждения (зеркала/сниппеты), явные "no-fire zones" вне скоупа проверки, предписанный формат вывода.

## Домен-фильтр web_search/web_fetch и self-hosted memory stores (2026-08-19, официальные release notes)

Два точечных расширения из того же окна, что и cookbook-разборы выше, но не из cookbook, а напрямую из release notes:

- **`allowed_domains`/`blocked_domains`** — впервые можно ограничить, какие сайты доступны тулам `web_search`/`web_fetch` конкретного агента, через `configs`-массив `agent_toolset_20260401` (`web_fetch` дополнительно получил `max_content_tokens`, `web_search` — `user_location`). Раньше `configs`-запись управлялась только `name`/`enabled`/`permission_policy`, без per-tool домен-фильтра — прямое применение минимальных привилегий из [[ai-security-by-design]] к встроенным тулам агента, а не только к MCP/сэндбоксу.
- **Self-hosted sandbox + memory stores** — атрибут «Экосистема» выше указывал self-hosted sandbox и memory stores как две независимые опции; теперь они совместимы: SDK-воркеры (Python/TypeScript/Go) сами скачивают примонтированный store в sandbox по `mount_path` и синхронизируют изменения агента обратно. До этой записи memory stores были доступны только в managed cloud-sandbox.

Источник — [[claude-code-changelog-snapshot-2026-08-22]].

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

## Противоречия

Найдено 2026-08-23 сверкой с сырьём (воскресный прогон рутины 3), **снято 2026-08-24** (ежедневное закрытие пробелов) прямой построчной проверкой официальных release notes (`platform.claude.com/docs/en/release-notes/overview`, раздел за 2026-06-30) — не пересказом и не raw-файлом, а первоисточником напрямую.

Изначально расхождение выглядело так: раздел «Экосистема вокруг ядра» датировал первый набор webhook-событий agent/deployment/deployment-run 2026-05-06, а появление `injection_location` у Vaults — 2026-06-30; `raw/sources/claude-managed-agents-overview.md` (тот же ingest 07-15) для обоих фактов называл 2026-07-02.

**Официальный первоисточник разрешает обе даты одинаково: оба факта — из записи за 30 июня 2026.** Дословно, из раздела «June 30, 2026»: «Webhooks for Claude Managed Agents now cover the agent, deployment, and deployment run lifecycle. […] See the Agent events, Deployment events, and Deployment run events tabs» и отдельным пунктом того же дня: «Claude Managed Agents vaults now support an `injection_location` setting on environment variable credentials […] It controls whether the credential's value is substituted, at egress, into the agent's outbound request headers, the request body, or both.» Ни 2026-05-06 (для webhooks agent/deployment/deployment-run — с этой датой спутан отдельный, действительно случившийся 06.05.2026 первый набор webhooks session/vault, см. запись «May 6, 2026»: «Webhook event types include session and vault lifecycle events»), ни 2026-07-02 (raw-файл, для обоих фактов) первоисточником не подтверждаются.

**Итог:** страничная дата у Vaults (2026-06-30) была верной с самого начала; ошибка была только в дате webhooks agent/deployment/deployment-run — исправлена на 2026-06-30 в разделе «Обновления с 2026-07-22» выше. Дата raw-файла (07-02) для обоих фактов не подтвердилась — сам raw-файл не правится (сырьё неизменяемо), расхождение с ним фиксируется здесь как факт истории, а не как повод сомневаться в исправленной дате.

## Ограничения
Beta-статус (заголовки `managed-agents-2026-04-01` / `agent-memory-2026-07-22`). Stateful по дизайну (session state хранится на сервере Anthropic) — из-за этого **не подходит под Zero Data Retention и HIPAA BAA**. MCP tunnels и Dreams — более узкий research preview, нужен отдельный запрос доступа.

## Связи
- Источники: [[claude-managed-agents-overview]], [[claude-cookbook-managed-agents-production-memory]], [[claude-cookbook-managed-agents-hitl-multiagent]], [[claude-cookbook-managed-agents-issue-outcome-grader]], [[claude-code-changelog-snapshot-2026-08-22]]
- Сущности: [[claude-agent-sdk]], [[claude-code]]
- Концепты: [[claude-memory-tool]] (разграничение client-side memory tool vs server-side memory store), [[mcp-model-context-protocol]] (MCP-серверы как один из tool-типов)
