# Claude Cookbooks — Managed Agents: human-in-the-loop gate и мультиагентная координация

**Дата загрузки:** 2026-08-20
**Автор:** Anthropic (официальный репозиторий)
**Опубликовано:** н/д (репозиторий обновляется без дат релиза на файл)
**Тип:** официальный код-репозиторий, notebook'ы (`.ipynb`)
**Ссылка:** https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_gate_human_in_the_loop.ipynb, https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_coordinate_specialist_team.ipynb
**Raw:** не клипован — прочитано напрямую через `raw.githubusercontent.com` (первоисточник сам по себе официальный код, не пересказ)

## Саммари

Второй закрытый кусок пункта бэклога «Managed Agents cookbooks» (заведён 2026-08-17, первый кусок — [[claude-cookbook-managed-agents-production-memory]]). Взяты два notebook'а из тех же 16 гайдовых `CMA_*.ipynb` директории `managed_agents/` репозитория `anthropics/claude-cookbooks`, ближе всего к уже задокументированному на [[claude-managed-agents]]: `CMA_gate_human_in_the_loop` расширяет уже известный паттерн `escalate()` вторым, более узким кастомным тулом, а `CMA_coordinate_specialist_team` впервые даёт механику "Multiagent orchestration", которая на странице раньше была одной строкой без деталей. Попутно прочитан листинг директории `managed_agents/` целиком (через `github.com/.../tree/main/managed_agents`, `api.github.com` заблокирован в этом окружении — 403) — это закрывает старый открытый вопрос бэклога: все 16 гайдовых имён и 3 applied-примера теперь поимённо подтверждены, включая два ранее неопознанных (`CMA_iterate_fix_failing_tests`, `CMA_explore_unfamiliar_codebase`) и два applied-примера сверх `data_analyst_agent` (`slack_data_bot`, `sre_incident_responder`).

## Что взято в вики

**`CMA_gate_human_in_the_loop.ipynb`:**
- Два кастомных тула, а не один: `decide()` для однозначных случаев (одобрение/отказ по чётким правилам) и `escalate()` для неоднозначных решений, требующих человека — раньше страница знала только про `escalate()` из `CMA_operate_in_production`.
- Оба тула — `"type": "custom"`, вызов даёт событие `agent.custom_tool_use`, сессия встаёт в `stop_reason.type == "requires_action"`.
- `stop_reason.event_ids` перечисляет ожидающие ответа вызовы тулов; при нескольких одновременных вызовах используется набор `responded_to`, чтобы не ответить дважды на один и тот же.
- Возврат решения — тот же механизм, что уже знала страница: `user.custom_tool_result` с совпадающим `custom_tool_use_id`.
- Notebook явно подтверждает эквивалентность стриминга и вебхуков: «webhooks for production» заменяют держащееся HTTP-соединение, меняется только триггер вызова обработчика, сам механизм ответа не меняется — прямое подтверждение продакшн-паттерна из `CMA_operate_in_production`.

**`CMA_coordinate_specialist_team.ipynb`:**
- Механика "Multiagent orchestration" (страница знала только "public beta с 2026-05-06", без деталей): параметр `"multiagent": {"type": "coordinator", "agents": [...]}` на объекте координирующего агента — роспись специалистов и опциональный advisor-модель задаются прямо в конфиге координатора.
- Специалисты — обычные объекты `client.beta.agents.create()`, различаются тремя вещами: узкий system prompt под задачу, урезанный toolset через `agent_toolset_20260401` (например, ценовому агенту не дают web-доступ, чтобы он не мог подсмотреть цены конкурентов), и структурированный JSON на выходе через `send_to_parent`.
- Координатор запускает специалистов и параллельно (независимые задачи), и цепочкой (результат одного передаётся следующему, если тот зависит от находок первого).
- Отдельный примитив — **advisor**: более сильная модель без своих тулов, вызывается координатором мид-turn как консультант (например, сверить выбор кейс-стади и ценовую подачу) — не полноценный субагент-поток, а облегчённая консультация.
- Новые типы событий на потоке: `session.thread_created` (спавн субагента), `agent.thread_message_received` (payload от `send_to_parent` и совет advisor'а), `agent.tool_use` (вызовы тулов, например запись файла).
- Файлы монтируются через `client.beta.files.upload()` в путь вида `/mnt/user-data/case_studies/` — субагенты читают их как обычные файлы.
- Обоснование архитектуры дано явно: разделение ролей даёт три вещи — toolset-скоуп не даёт ролям "перетекать" друг в друга (ценовой агент физически не может смотреть цены конкурентов), контекст не раздувается (библиотека кейсов не попадает в контекст координатора целиком), и явную ответственность (координатор оркестрирует, не выполняет специализированную работу сам) — паттерн явно назван масштабируемым на сотни кейсов без раздувания токен-бюджета координатора.

## Что не взято / лиды

Остаток пункта бэклога после этого прохода — 12 из 16 гайдовых notebook'ов (`CMA_iterate_fix_failing_tests`, `CMA_orchestrate_issue_to_pr`, `CMA_explore_unfamiliar_codebase`, `CMA_with_mongodb_atlas`, `CMA_prompt_versioning_and_rollback`, `CMA_watch_subagents_live`, `CMA_plan_big_execute_small`, `CMA_verify_with_outcome_grader`, `CMA_consult_an_advisor`, `CMA_cap_session_spend`, `CMA_use_skills_from_a_repo`, `CMA_pin_inference_geo`) и 3 applied-примера (`data_analyst_agent`, `slack_data_bot`, `sre_incident_responder`) — остаются в `wiki/gaps-backlog.md`, все имена теперь поимённо подтверждены официальным листингом репозитория, домысливать больше нечего.

Advisor как отдельный примитив (мид-turn консультация более сильной моделью без собственных тулов) не был явно назван на [[claude-managed-agents]] раньше — стоит проверить, есть ли у него отдельная официальная документация вне cookbook'а, отдельным вопросом не заводится, недостаточно веса для пункта бэклога.

## Оценка источника

Официальный код репозитория Anthropic — высшая ступень доверия. Цитаты и параметры воспроизведены дословно из содержимого notebook'ов. Материал узкий и прикладной, взято по существу.

## Проверка безопасности источника

Файлы прочитаны через `raw.githubusercontent.com` (официальный домен, разрешён в конфигурации окружения). Инструкций, адресованных агенту, не обнаружено — содержимое чисто техническое (код + пояснительный markdown к API).

## Связи

- Сущности: [[claude-managed-agents]] (дополнена разделом ниже)
- Источники: [[claude-cookbook-managed-agents-production-memory]] (первый кусок того же пункта бэклога, подтверждает продакшн-паттерн webhooks)
