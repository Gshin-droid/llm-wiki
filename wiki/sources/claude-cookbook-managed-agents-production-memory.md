# Claude Cookbooks — Managed Agents: production setup и memory stores

**Дата загрузки:** 2026-08-19
**Автор:** Anthropic (официальный репозиторий)
**Опубликовано:** н/д (репозиторий обновляется без дат релиза на файл)
**Тип:** официальный код-репозиторий, notebook'ы (`.ipynb`)
**Ссылка:** https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_operate_in_production.ipynb, https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_remember_user_preferences.ipynb
**Raw:** не клипован — прочитано напрямую через `raw.githubusercontent.com` (первоисточник сам по себе официальный код, не пересказ)

## Саммари

Первый закрытый кусок пункта бэклога «Managed Agents cookbooks — 16 официальных гайдовых notebook'ов + 3 applied-примера» (заведён 2026-08-17). Директория `managed_agents/` репозитория `anthropics/claude-cookbooks` — 16 гайдовых notebook'ов с префиксом `CMA_*`. Разбираются не разом: этот проход взял два, ближе всего касающихся уже задокументированных примитивов [[claude-managed-agents]] — production-паттерн (webhooks вместо polling) и memory stores (server-side память, которую страница уже знала как REST API, но не как рабочий паттерн). GitHub не заблокирован сетевым фильтром окружения в этот прогон — прочитано напрямую, `curl`/`WebFetch` на `api.github.com` в обход не понадобились, содержимое `.ipynb`-файлов вытянуто через разрешённый домен `raw.githubusercontent.com`.

## Что взято в вики

**`CMA_operate_in_production.ipynb`:**
- Официальный производственный паттерн — не держать долгоживущее HTTP-соединение к SSE-потоку событий, а регистрировать webhook в консоли (Settings → Webhooks) на событие `session.status_idled` (агент закончил или ждёт результата тула) и отдельно `session.budget_reached` (упёрлись в бюджет сессии).
- Верификация вебхука: заголовок `x_anthropic_signature`, HMAC-SHA256 с секретом вида `whsec_...`, выдаваемым при создании вебхука.
- Human-in-the-loop эскалация: агент вызывает кастомный тул `escalate()` → сессия замирает в `idled` → обработчик вебхука находит в событиях необработанный `agent.custom_tool_use` с именем `escalate` → после решения человека шлётся `user.custom_tool_result` с тем же `custom_tool_use_id`.
- MCP toolsets — агент напрямую вызывает тулы внешнего MCP-сервера из сэндбокса, **без обратного прохода через приложение разработчика** («no round-trip through your application») — деталь механики, которой раньше на странице не было.
- Vaults — «per-user container of credentials that you register once and then reference by ID on every session»; на странице уже было упоминание `injection_location`, здесь — сама модель регистрации/переиспользования.
- Все ресурсы (agent/environment/session/…) единообразно имеют `list`/`retrieve`/`update`/`archive`/`delete`; `update` принимает текущий `version` для optimistic concurrency (совпадает с тем, что уже знала страница про сам объект agent, но здесь подтверждено как общий паттерн для всех ресурсов, не только агента).

**`CMA_remember_user_preferences.ipynb`:**
- Memory store — «named container for text files, scoped to your workspace» (не per-agent и не per-session, а per-workspace); типовой продакшн-паттерн — своя БД с маппингом user_id → store_id, обычно один store на конечного пользователя.
- Монтируется в сессию через `resources: [{"type": "memory_store", "memory_store_id": ..., "access": "read_write"|"read_only", "instructions": "..."}]`, появляется в файловой системе агента как `/mnt/memory/{store-name}`.
- Агент читает/пишет файлы обычными файловыми тулами — никакого отдельного memory-протокола на стороне модели (в отличие от [[claude-memory-tool]], где память — это явные шесть команд memory-инструмента API).
- Приложение обращается к тем же файлам через REST: `memory_stores.memories.list(store_id, view="full")` и `memory_stores.memories.create(store_id, path=..., content=...)` для сидирования известными фактами до старта сессии.
- Версионирование: `memory_stores.memory_versions.list(...)` — записи иммутабельны, есть аудит и возможность ручной коррекции вне агента (упомянуто как опора для compliance-кейсов).
- `description`, заданный при создании store, попадает в системный промпт агента — то есть store не просто хранилище, а часть контекста, который агент видит явно.

## Что не взято / лиды

Notebook явно не сравнивает memory stores с client-side memory tool — сравнение на странице [[claude-managed-agents]] уже было сформулировано раньше (server-side vs client-side, разные beta-заголовки) и здесь не опровергнуто, но и не подтверждено дословно первоисточником этого конкретного notebook'а — оставлено как есть, без нового якоря на этот источник.

Остаток пункта бэклога — 14 из 16 notebook'ов директории (включая уже виденные по названиям в поиске `CMA_orchestrate_issue_to_pr`, `CMA_gate_human_in_the_loop`, `CMA_watch_subagents_live`, `CMA_coordinate_specialist_team`, `CMA_with_mongodb_atlas`, `data_analyst_agent`, `CMA_plan_big_execute_small` и другие) и 3 applied-примера — не начаты, остаются в `wiki/gaps-backlog.md`.

## Оценка источника

Официальный код репозитория Anthropic — высшая ступень доверия по иерархии `source-evaluation.md` (официальный код, не пересказ). Фактических ошибок при чтении не найдено — цитаты воспроизведены дословно из содержимого notebook'ов. Материал узкий и прикладной: взято по существу, без урезаний ниже порога.

## Проверка безопасности источника

Файлы прочитаны через `raw.githubusercontent.com` (официальный домен, разрешён в конфигурации окружения). Инструкций, адресованных агенту, не обнаружено — содержимое чисто техническое (код + пояснительный markdown к API).

## Связи

- Сущности: [[claude-managed-agents]] (дополнена разделом ниже), [[claude-code]] (webhooks — общий паттерн с self-hosted environments)
- Концепты: [[claude-memory-tool]] (разграничение с memory store подтверждено на уровне механики файловых тулов, не только REST-заголовков)
