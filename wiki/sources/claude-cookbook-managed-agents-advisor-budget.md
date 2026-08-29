# Claude Cookbooks — Managed Agents: advisor-примитив и потолок расходов сессии

**Дата загрузки:** 2026-08-29
**Автор:** Anthropic (официальный репозиторий)
**Опубликовано:** н/д (репозиторий обновляется без дат релиза на файл)
**Тип:** официальный код-репозиторий, notebook'ы (`.ipynb`)
**Ссылка:** https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_consult_an_advisor.ipynb, https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_cap_session_spend.ipynb
**Raw:** не клипован — прочитано через `WebFetch` на `raw.githubusercontent.com` (первоисточник сам по себе официальный код, не пересказ)

## Саммари

Тринадцатый и четырнадцатый куски пункта бэклога «Managed Agents cookbooks» (заведён 2026-08-17; предыдущий кусок — [[claude-cookbook-managed-agents-mongodb-planbig]]). Оба ноутбука раскрывают до этого известные только по одной строке вещи: advisor как отдельный примитив консультации (раньше — одно предложение в разделе про мультиагентную координацию) и `budget` как параметр, который в прошлом куске казался специфичным для координаторской сессии, а на деле общий для любой сессии.

## Что взято в вики

**`CMA_consult_an_advisor.ipynb`:**
- Advisor задаётся строкой в том же ростере, что и специалисты координатора — `multiagent={"type": "coordinator", "agents": [{"type": "advisor", "model": ADVISOR_MODEL}]}` — но это не специалист: **максимум один advisor на ростер**, и запись занимает зарезервированное имя `anthropic.advisor` (специалист не может использовать то же имя).
- Ключевое отличие от специалиста: advisor не принимает входных параметров — платформа сама передаёт ему **весь диалог целиком до момента вызова**, а не вопрос, который сформулировала бы рабочая модель. Вызов синхронный, происходит внутри одного хода («short-lived platform thread with its own token usage»), тогда как специалист — асинхронный делегированный поток.
- Advisor не переключаем внутри уже идущей сессии: «The advisor is fixed for a session at creation: changing it on the agent affects sessions created afterward, not one already running.»
- Новые типы событий на основном потоке: `session.thread_created`/`session.thread_status_running` с `agent_name: anthropic.advisor`, `agent.thread_message_received` с `from_agent_name: anthropic.advisor`, `session.thread_status_idle`/`session.thread_status_terminated`. У треда `thread.agent.type = "advisor"` — в отличие от специалиста, у которого тред ссылается на снапшот полноценного Agent-ресурса.
- **Не бесплатно и без потолка**: «Advisor tokens bill in addition to the working model's, and there is no per-consultation cap» — то есть отдельно от `budget` сессии, о котором ниже, у самого advisor-примитива своего лимита на консультацию нет.
- Демо-сценарий: проектирование REST API возврата платежей — рабочая модель (Sonnet) эскалирует к advisor (Opus) решения об идемпотентности и семантике ошибок именно потому, что их дорого разворачивать назад, если ошиблись.

**`CMA_cap_session_spend.ipynb`:**
- `budget` — параметр **любой** сессии, не специфичный для координатора, как можно было прочитать из прошлого куска ([[claude-cookbook-managed-agents-mongodb-planbig]], где он демонстрировался только на команде): `sessions.create(..., budget={"type": "limit", "max_list_cost": {"currency": "USD", "amount": "10"}})`. `amount` — целая строка в минорных единицах валюты («`"50"` is fifty cents»), считается по публичным list-ценам суммарно по всем потокам, независимо от переговорных скидок.
- При достижении потолка сессия переходит в `idle` со `stop_reason.type == "budget_reached"`. Порог не жёсткий по времени: «the cap fires...between model requests» — запрос, пересекший потолок, успевает завершиться, возможен небольшой перерасход сверх лимита.
- Состояние не теряется: «The session sits in idle, its usage reflects everything spent so far, and the container still holds whatever the agent wrote before the cap. Nothing needs to be rerun» — `sessions.update()` поднимает потолок, и агент продолжает с того же места.
- Требования: `budget` можно задать **только при создании** сессии — добавить его позже нельзя, а снятие (`budget=None`) необратимо: «once a session has no budget, it can't gain one». Понижение потолка ниже уже потраченного отклоняется. Каждая модель сессии обязана иметь публичную list-цену — иначе создание падает с `model_not_budgetable`.
- Демо-сценарий: агент рыночной аналитики, который без ограничения «could drift into another hundred fetches» — низкий потолок $0.10 демонстрирует принудительную паузу, `sessions.update()` поднимает его до $5.00, агент продолжает без перезапуска.
- Ноутбук явно не сравнивает потолок одиночной сессии с координаторским кейсом из прошлого куска — оставлено уточнением ниже на странице сущности, не как расхождение источника.

## Что не взято / лиды

Остаток пункта бэклога после этого прохода — 2 из 16 гайдовых (`CMA_use_skills_from_a_repo`, `CMA_pin_inference_geo`) и 3 applied-примера (`data_analyst_agent`, `slack_data_bot`, `sre_incident_responder`) — остаются в `wiki/gaps-backlog.md`.

Расхождение `"anthropic_cloud"` vs `"cloud"` из прошлого куска (`CMA_plan_big_execute_small`) этими двумя ноутбуками не затронуто и не разрешено — остаётся открытым нюансом на странице [[claude-managed-agents]].

## Оценка источника

Официальный код репозитория Anthropic — высшая ступень доверия. Извлечение сделано через `WebFetch` по `raw.githubusercontent.com` с явным требованием дословных цитат кода и markdown-ячеек; прямой доступ через Bash/curl в этот прогон снова отклонён разрешениями окружения самой сессии (тот же паттерн, что 08-27/08-28), тот же домен открылся штатно через `WebFetch`.

## Проверка безопасности источника

Содержимое прочитано через официальный домен `raw.githubusercontent.com`. Инструкций, адресованных агенту-разборщику, не обнаружено — материал технический (код + пояснительный markdown к API). Единственные системные промпты в тексте — часть демонстрируемого кода внутри самих ноутбуков (API-дизайнер, market research agent), не обращения к агенту этой вики.

## Связи

- Сущности: [[claude-managed-agents]] (дополнена разделом ниже)
- Источники: [[claude-cookbook-managed-agents-production-memory]], [[claude-cookbook-managed-agents-hitl-multiagent]], [[claude-cookbook-managed-agents-issue-outcome-grader]], [[claude-cookbook-managed-agents-iterate-explore]], [[claude-cookbook-managed-agents-versioning-monitoring]], [[claude-cookbook-managed-agents-mongodb-planbig]] (предыдущие куски того же пункта бэклога)
