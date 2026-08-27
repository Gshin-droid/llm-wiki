# Claude Cookbooks — Managed Agents: версионирование промпта и живой мониторинг субагентов

**Дата загрузки:** 2026-08-27
**Автор:** Anthropic (официальный репозиторий)
**Опубликовано:** н/д (репозиторий обновляется без дат релиза на файл)
**Тип:** официальный код-репозиторий, notebook'ы (`.ipynb`)
**Ссылка:** https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_prompt_versioning_and_rollback.ipynb, https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_watch_subagents_live.ipynb
**Raw:** не клипован — прочитано напрямую через `raw.githubusercontent.com` (первоисточник сам по себе официальный код, не пересказ)

## Саммари

Девятый и десятый куски пункта бэклога «Managed Agents cookbooks» (заведён 2026-08-17; предыдущие куски — [[claude-cookbook-managed-agents-production-memory]], [[claude-cookbook-managed-agents-hitl-multiagent]], [[claude-cookbook-managed-agents-issue-outcome-grader]], [[claude-cookbook-managed-agents-iterate-explore]]). Оба ноутбука раскрывают механику, которую страница [[claude-managed-agents]] раньше знала только как факт ("`version` необязателен при обновлении", "event deltas на уровне субагента") без сценария применения — здесь показано, зачем это нужно и как выглядит вживую.

## Что взято в вики

**`CMA_prompt_versioning_and_rollback.ipynb`:**
- Каждый `agents.update()` создаёт неизменяемую серверную версию — само обновление не перезаписывает старую конфигурацию, а добавляет новую с инкрементированным номером. Дословно: «Every `agents.update` produces a new immutable version, and sessions choose which version to use by ID.»
- Два способа указать агента при создании сессии — не эквивалентны. Строка `agent=AGENT_ID` берёт **последнюю** версию неявно; объект `{"type": "agent", "id": AGENT_ID, "version": N}` **закрепляет** конкретную версию. До этого ноутбука страница знала только про сам параметр `version` у `update()` (optimistic concurrency), не про то, что версией можно управлять и на стороне `sessions.create`.
- Откат — не redeploy и не отдельная операция, а смена номера версии в конфигурации: старая версия никуда не делась, она просто снова становится той, на которую указывает `version`.
- `client.beta.agents.versions.list(AGENT_ID)` — перечисление всех версий агента; раньше на странице не упоминалось.

**`CMA_watch_subagents_live.ipynb`:**
- Собирает воедино три примитива, до сих пор упомянутых порознь: **event deltas на уровне субагента** (`GET /v1/sessions/{id}/threads/{thread_id}/stream`, добавлено 07-22 по release notes), **`initial_events` при создании сессии** (добавлено 07-22, до 50 событий) и **`effort` в конфигурации модели агента** (добавлено 07-22) — здесь показан код, использующий все три вместе на реальном примере: координатор + два специалиста (ресёрчер стандартов с `web_search` и `effort: high`, писатель уроков без веб-доступа).
- Новая деталь, которой не было ни в одном из прошлых кусков: **гарантия best-effort у дельт** — «Deltas are best-effort and may stop under load. The buffered `agent.message` that follows carries the complete content.» То есть дельты — это UX-превью, а не источник истины; полный текст всегда приходит финальным `agent.message`, и на него, а не на накопленные дельты, следует полагаться при верификации. Ноутбук явно проверяет это свойство: накопленный из дельт текст должен быть префиксом финального сообщения.
- Отключение конкретного тула у агента — не отдельным списком, а флагом внутри самого объявления тула: `{"name": "web_search", "enabled": False}`.
- Уточнение к разделу «Multiagent orchestration» страницы [[claude-managed-agents]]: ростер специалистов координатора **закрепляется на момент создания координатора** — если специалиста обновить (`agents.update`) отдельно, координатор продолжит вызывать старую закреплённую версию; чтобы обновление подхватилось, нужно обновить самого координатора, а не только специалиста.
- Требование SDK для этих возможностей — `anthropic>=0.118.0`, впервые названная в вики конкретная нижняя граница версии клиентской библиотеки для Managed Agents.

## Что не взято / лиды

Остаток пункта бэклога после этого прохода — 6 из 16 гайдовых notebook'ов (`CMA_with_mongodb_atlas`, `CMA_plan_big_execute_small`, `CMA_consult_an_advisor`, `CMA_cap_session_spend`, `CMA_use_skills_from_a_repo`, `CMA_pin_inference_geo`) и 3 applied-примера (`data_analyst_agent`, `slack_data_bot`, `sre_incident_responder`) — остаются в `wiki/gaps-backlog.md`.

Не проверено и стоит проверить при следующем куске: применим ли тот же паттерн закрепления версии (`{"type": "agent", "id": ..., "version": ...}`) к environment или только к agent — оба ноутбука работали только с версией агента.

## Оценка источника

Официальный код репозитория Anthropic — высшая ступень доверия. Извлечение сделано через `WebFetch` по `raw.githubusercontent.com` с явным требованием дословных цитат кода и markdown-ячеек, а не свободного пересказа — прямой доступ к сырому JSON-ноутбуку через Bash/curl в этом прогоне был заблокирован разрешениями окружения (не сетевым фильтром: тот же домен `raw.githubusercontent.com` открылся штатно через `WebFetch`).

## Проверка безопасности источника

Содержимое прочитано через официальный домен `raw.githubusercontent.com`. Инструкций, адресованных агенту, не обнаружено — материал технический (код + пояснительный markdown к API).

## Связи

- Сущности: [[claude-managed-agents]] (дополнена разделом ниже)
- Источники: [[claude-cookbook-managed-agents-production-memory]], [[claude-cookbook-managed-agents-hitl-multiagent]], [[claude-cookbook-managed-agents-issue-outcome-grader]], [[claude-cookbook-managed-agents-iterate-explore]] (предыдущие куски того же пункта бэклога)
