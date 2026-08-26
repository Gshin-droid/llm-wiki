# Claude Cookbooks — Managed Agents: итеративный фикс тестов и разведка чужого кода

**Дата загрузки:** 2026-08-26
**Автор:** Anthropic (официальный репозиторий)
**Опубликовано:** н/д (репозиторий обновляется без дат релиза на файл)
**Тип:** официальный код-репозиторий, notebook'ы (`.ipynb`)
**Ссылка:** https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_iterate_fix_failing_tests.ipynb, https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_explore_unfamiliar_codebase.ipynb
**Raw:** не клипован — прочитано напрямую через `raw.githubusercontent.com` (первоисточник сам по себе официальный код, не пересказ)

## Саммари

Седьмой и восьмой куски пункта бэклога «Managed Agents cookbooks» (заведён 2026-08-17; предыдущие куски — [[claude-cookbook-managed-agents-production-memory]], [[claude-cookbook-managed-agents-hitl-multiagent]], [[claude-cookbook-managed-agents-issue-outcome-grader]]). Оба взятых notebook'а — не про новый примитив API, а про **вход в тему**: `CMA_iterate_fix_failing_tests` учит канонический паттерн стриминга событий на самой простой задаче (почини баг → перезапусти тест), `CMA_explore_unfamiliar_codebase` — про то, что агент обязан проверять документацию по коду, а не доверять ей на слово.

## Что взято в вики

**`CMA_iterate_fix_failing_tests.ipynb`:**
- Каноническая последовательность работы с сессией, повторяющаяся во всех остальных ноутбуках директории: открыть SSE-стрим **до** отправки события, затем `sessions.events.send`, дождаться `session.status_idle` c `stop_reason.type == "end_turn"` — и только тогда выходить из цикла чтения. Вынесено в переиспользуемые хелперы `stream_until_end_turn`/`wait_for_idle_status`, а не разбросано по коду примера.
- Схема ресурсов: файлы через `client.beta.files.upload()` монтируются в session как read-only `/mnt/session/uploads/`; агент сначала копирует их в писабельный `/mnt/user`, работает там, финальный результат кладёт в `/mnt/session/outputs/` — читаемое приложением место отделено от рабочей директории агента.
- Демонстрация нарочно вложенная: `mean()` зависит от `add()` и `divide()`, оба с багом. Педагогическая цель прямая — агент не должен чинить симптом на каждом уровне отдельно: если оба падают из-за одной причины в `add()`, починка `add()` автоматически чинит `divide()` и `mean()`, а «перечинивание» уже исправленного — сигнал, что агент не читает трассу целиком.
- `permission_policy: always_allow` в конфиге тула — автономный проход без разрешения на каждый вызов, для контролируемой demo-сессии.

**`CMA_explore_unfamiliar_codebase.ipynb`:**
- Тестовый фикстур нарочно лживый: `ARCHITECTURE.md` описывает монолит, а код внутри архива уже переехал на микросервисы — проверяется, что агент **сверяет документацию с фактическим деревом файлов**, а не пересказывает `.md` как истину.
- Новый паттерн ресурсов, не встречавшийся в прошлых кусках пункта: `sessions.resources.add()` — файл добавляется **посреди уже идущей сессии**, без пересоздания. В демонстрации агенту подсовывают `DEPLOY_HISTORY.md` после того, как он уже начал расследование и явно нашёл пробел в контексте — то есть ресурс подгружается по требованию хода расследования, а не заранее весь целиком.
- Остальной инструментарий обычный: `ls`/`grep`/`read` из общего тулсета, `always_allow` для автономного прохода, `archive()` на все три ресурса (session/environment/agent) в конце.

## Что не взято / лиды

Остаток пункта бэклога после этого прохода — 8 из 16 гайдовых notebook'ов (`CMA_with_mongodb_atlas`, `CMA_prompt_versioning_and_rollback`, `CMA_watch_subagents_live`, `CMA_plan_big_execute_small`, `CMA_consult_an_advisor`, `CMA_cap_session_spend`, `CMA_use_skills_from_a_repo`, `CMA_pin_inference_geo`) и 3 applied-примера (`data_analyst_agent`, `slack_data_bot`, `sre_incident_responder`) — остаются в `wiki/gaps-backlog.md`.

Оба взятых ноутбука концептуально проще предыдущих шести — не открыли нового примитива API (memory, outcomes, multiagent, webhooks уже разобраны раньше). Ценность в другом: `sessions.resources.add()` — первое подтверждение, что ресурсы session можно менять на лету, а не только при создании; стоит проверить, применим ли тот же метод к другим типам ресурсов (`memory_store`, `github_repository`) при следующем подходящем куске.

## Оценка источника

Официальный код репозитория Anthropic — высшая ступень доверия. Структуры вызовов воспроизведены дословно из содержимого notebook'ов.

## Проверка безопасности источника

Файлы прочитаны через `raw.githubusercontent.com` (официальный домен, разрешён в конфигурации окружения). Инструкций, адресованных агенту, не обнаружено — содержимое чисто техническое (код + пояснительный markdown к API).

## Связи

- Сущности: [[claude-managed-agents]] (дополнена разделом ниже)
- Источники: [[claude-cookbook-managed-agents-production-memory]], [[claude-cookbook-managed-agents-hitl-multiagent]], [[claude-cookbook-managed-agents-issue-outcome-grader]] (предыдущие куски того же пункта бэклога)
