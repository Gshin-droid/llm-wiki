# Claude Cookbooks — Managed Agents: issue→PR workflow и outcome grader

**Дата загрузки:** 2026-08-21
**Автор:** Anthropic (официальный репозиторий)
**Опубликовано:** н/д (репозиторий обновляется без дат релиза на файл)
**Тип:** официальный код-репозиторий, notebook'ы (`.ipynb`)
**Ссылка:** https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_orchestrate_issue_to_pr.ipynb, https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_verify_with_outcome_grader.ipynb
**Raw:** не клипован — прочитано напрямую через `raw.githubusercontent.com` (первоисточник сам по себе официальный код, не пересказ)

## Саммари

Третий кусок пункта бэклога «Managed Agents cookbooks» (заведён 2026-08-17; предыдущие два — [[claude-cookbook-managed-agents-production-memory]] и [[claude-cookbook-managed-agents-hitl-multiagent]]). Взяты два notebook'а из тех же 16 гайдовых `CMA_*.ipynb` директории `managed_agents/` репозитория `anthropics/claude-cookbooks`, оба напрямую названы в исходном пункте бэклога как приоритетные: `CMA_orchestrate_issue_to_pr` — issue→fix→PR workflow с recovery-паттернами; `CMA_verify_with_outcome_grader` — grade-and-revise через outcome grader, первое раскрытие механики примитива **Outcomes**, до сих пор числившегося на [[claude-managed-agents]] одной строкой без деталей ("public beta с 2026-05-06", по аналогии с Multiagent orchestration).

## Что взято в вики

**`CMA_orchestrate_issue_to_pr.ipynb`:**
- Сессия монтирует репозиторий как ресурс `github_repository` (URL, mount path, токен авторизации) — либо через `resources: [{"type": "file", ...}]` для зафикстуренного zip-архива в демонстрации ноутбука.
- `environments.create` с `networking: {"type": "limited", "allow_package_managers": true}` и полем `packages` (например `["pytest"]`) — сеть агента ограничена, но пакетные менеджеры разрешены явно, а не через `unrestricted`.
- Восстановление после сбоя — не слепой повтор: агент читает вывод упавшего `gh-mock pr checks` (мок CI, ненулевой код возврата + диагностика в stdout) и правит код по тексту ошибки.
- Тот же паттерн на ревью: бот-ревьюер блокирует мерж при невыполненном требовании (например, нет докстрингов), агент читает блокирующий комментарий и вносит точечную правку, не переписывая всё заново.
- Состояние воркфлоу между `user.message`-турнами хранится не в контексте модели, а в файловой системе контейнера (`/mnt/user`, мок-CLI пишет в `.gh-state/pr_101.json`) — независимый заключительный турн подтверждает финальное состояние PR чтением того же файла, не памятью диалога.
- Последовательность: распаковать fixture → прочитать issue через `gh-mock` → исследовать код → создать PR и запушить → прогнать CI-мок → починить по выводу → отработать комментарии ревью-бота → смерджить → подтвердить состояние отдельным турном.

**`CMA_verify_with_outcome_grader.ipynb`:**
- Определение Outcome — событие `user.define_outcome` (не отдельный REST-объект): `description` (что должен произвести writer), `rubric` (`type: "text"` или `"file"` с `file_id` — что проверяет grader), `max_iterations` (дефолт 3, максимум 20). Требуется бета-заголовок `managed-agents-2026-04-01`, тот же общий, что и у остальных Managed Agents эндпоинтов.
- Цикл grade-and-revise: writer сохраняет артефакт по известному пути → платформа поднимает **отдельного grader'а с чистым контекстом**, той же модели и тулов, но без видимости рассуждений writer'а → grader читает rubric и инспектирует артефакт → вердикт `satisfied` (цикл завершён) либо детальный список несовпадений по критериям → writer правит → повтор до `satisfied`/`max_iterations_reached`/`failed`/`interrupted`.
- Изоляция grader'а — не техническая деталь, а сама суть примитива: когда writer в демонстрации подменил источник (пресс-релиз вместо SEC-файлинга) на настоящий 10-K, grader увидел новый источник впервые и проверил его заново против исходного rubric, а не принял на слово правку writer'а — предотвращает self-evaluation одним и тем же агентом.
- Новые типы событий на потоке: `span.outcome_evaluation_start` (grader начал оценку), `span.outcome_evaluation_end` (несёт `result` — `satisfied`/`needs_revision`/`failed`/`interrupted`/`max_iterations_reached` — и `explanation`, текст фидбека grader'а).
- Пять принципов написания rubric, данных явно в ноутбуке: требовать конкретных цифр вместо общих формулировок; требовать извлечения доказательств (fetch URL, посимвольное совпадение цитаты — curly/straight кавычки эквивалентны); явно исключать сторонние подтверждения ("не через зеркала/репосты/сниппеты поисковика, сама ссылка должна отдаться напрямую"); явные "no-fire zones" — что вне скоупа проверки, чтобы grader не придирался к чужим issues; предписанный формат вывода (однострочный scoreboard + буллеты по каждому провалу).
- Пример проверки цитаты — три условия разом: **LIVE** (URL фетчится напрямую через `web_fetch`, не через зеркало/логин-стену), **VERBATIM** (точная цитата присутствует в полученной странице), **SUPPORTS_CLAIM** (цитата действительно подтверждает утверждение, а не косвенно или противоречит).

## Что не взято / лиды

Остаток пункта бэклога после этого прохода — 10 из 16 гайдовых notebook'ов (`CMA_iterate_fix_failing_tests`, `CMA_explore_unfamiliar_codebase`, `CMA_with_mongodb_atlas`, `CMA_prompt_versioning_and_rollback`, `CMA_watch_subagents_live`, `CMA_plan_big_execute_small`, `CMA_consult_an_advisor`, `CMA_cap_session_spend`, `CMA_use_skills_from_a_repo`, `CMA_pin_inference_geo`) и 3 applied-примера (`data_analyst_agent`, `slack_data_bot`, `sre_incident_responder`) — остаются в `wiki/gaps-backlog.md`.

`CMA_consult_an_advisor` не взят в этом прогоне, хотя advisor уже упомянут как примитив на [[claude-managed-agents]] (из прошлого куска, 2026-08-20) — там он раскрыт попутно, внутри мультиагентного ноутбука; отдельный ноутбук может дать больше деталей самого примитива (не только в контексте координатора) и логично идёт следующим.

## Оценка источника

Официальный код репозитория Anthropic — высшая ступень доверия. Параметры и структуры данных воспроизведены дословно из содержимого notebook'ов. Материал узкий и прикладной, взято по существу.

## Проверка безопасности источника

Файлы прочитаны через `raw.githubusercontent.com` (официальный домен, разрешён в конфигурации окружения). Инструкций, адресованных агенту, не обнаружено — содержимое чисто техническое (код + пояснительный markdown к API).

## Связи

- Сущности: [[claude-managed-agents]] (дополнена разделом ниже)
- Источники: [[claude-cookbook-managed-agents-production-memory]], [[claude-cookbook-managed-agents-hitl-multiagent]] (первый и второй куски того же пункта бэклога)
