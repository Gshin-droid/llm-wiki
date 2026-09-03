# Claude Cookbooks — Managed Agents: Slack Data Bot (applied-пример)

**Дата загрузки:** 2026-09-03
**Автор:** Anthropic (официальный репозиторий)
**Опубликовано:** н/д (репозиторий обновляется без дат релиза на файл)
**Тип:** официальный код-репозиторий, notebook (`.ipynb`)
**Ссылка:** https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/slack_data_bot.ipynb
**Raw:** не клипован — прочитано через `WebFetch` на `raw.githubusercontent.com` (первоисточник сам по себе официальный код, не пересказ)

## Саммари

Второй из трёх applied-примеров пункта бэклога «Managed Agents cookbooks» (заведён 2026-08-17, гайдовая часть 16/16 закрыта 2026-09-01, первый applied-пример — [[claude-cookbook-managed-agents-data-analyst]]). Прямая надстройка над предыдущим: тот же агент-аналитик оборачивается в Slack-бота на Bolt for Python (`slack_bolt`, Socket Mode). Ключевое отличие от гайдовых `CMA_*.ipynb` и первого applied-примера — здесь нет создания агента/environment/toolset с нуля: бот **ссылается** на уже существующего агента по `id`+`version` и на уже существующий environment по `id`, оба берутся из переменных окружения. Показывает не платформенный примитив, а интеграционный слой: как продакшн-обёртка вообще устроена вокруг уже готового агента.

## Что взято в вики

- **Готовый агент подключается по закреплённой версии, не создаётся заново.** `ANALYST_AGENT = {"id": os.environ["ANALYST_AGENT_ID"], "version": int(os.environ["ANALYST_AGENT_VERSION"])}` — прямое применение паттерна из [[claude-cookbook-managed-agents-versioning-monitoring]] (08-27): продакшн-обвязка пинит конкретную версию агента явно, а не берёт последнюю неявно строкой `agent=AGENT_ID`. Это первый на странице источника пример, где закрепление версии показано не как демонстрация примитива, а как то, что реальный сервис обязан делать по умолчанию.
- **Одна Slack-тема = одна сессия.** Словарь `thread_sessions: dict[str, str]` в памяти процесса связывает `thread_ts` Slack-треда с `session.id`; при упоминании бота создаётся новая сессия (`sessions.create`), при ответе в том же треде (`on_thread_reply`) — та же сессия продолжается через `sessions.events.send` с новым `user.message`, без пересоздания. Session как единица диалога — уже известный факт платформы, здесь показано его прямое соответствие Slack-треду как единице разговора в интерфейсе.
- **Файл из Slack переливается в Files API, а не идёт в сессию напрямую.** Файл скачивается по `slack_file["url_private"]` с Bearer-токеном бота, затем `client.beta.files.upload(...)` кладёт его в Files API, и только после этого `file_id` монтируется в сессию тем же паттерном `resources=[{"type": "file", "file_id": ..., "mount_path": "/mnt/session/uploads/data.csv"}]`, что и в первом applied-примере. Slack — не альтернативный канал загрузки файлов в агента, а внешний источник, который приводится к тому же контракту Files API.
- **Прогресс ретранслируется в Slack через `sessions.events.stream`, не через один финальный ответ.** `relay_stream()` читает событийный поток сессии построчно: на первый `agent.tool_use` шлёт в тред «Running analysis...» (один раз, не на каждый вызов тула), на `agent.message` копит последний текстовый блок как готовое саммари, на `session.status_idle` завершает цикл, на `session.status_terminated` — отдельная ветка: сообщение в тред со ссылкой на трейс сессии (`https://platform.claude.com/sessions/{session_id}`) вместо тихого обрыва. Первый на странице источника пример, что делает продакшн-код при аварийном завершении сессии — раньше только упоминалось событие `session.status_terminated`, без обработчика.
- **Бета-заголовок у Files API — `managed-agents-2026-04-01`.** Итоговые файлы читаются через `client.beta.files.list(scope_id=session_id, betas=["managed-agents-2026-04-01"])`, то есть Files API в связке с managed-agents session scope всё ещё под этим бета-флагом на дату нотбука — конкретика, которой не было в прошлых кусках (там `betas` не показывался явно).
- **Текст ответа проходит конвертацию markdown → Slack mrkdwn** (`mrkdwn.convert(summary)`) и обрезается на 3900 символов с пометкой `_(truncated)_` — практическая деталь показа результата агента человеку, а не платформенный примитив, но показывает, что «текстовый ответ агента» и «то, что можно вставить в чужой UI» — разные форматы, которые обвязка обязана согласовать сама.

## Что не взято / лиды

Toolset/system prompt/permission policy самого агента-аналитика этим нотбуком не переопределяются — они целиком унаследованы из `data_analyst_agent.ipynb` (уже разобрано в [[claude-cookbook-managed-agents-data-analyst]]), нотбук их не показывает вообще, только берёт готовый `id`/`version`. Не разобрано отдельно: код создания `ANALYST_AGENT_ID`/`ANALYST_ENV_ID` (вероятно, вынесен в отдельный сетап-шаг того же нотбука или предполагается взятым из предыдущего) — в извлечённой цитате его нет, взять при возврате к этому нотбуку, если понадобится точный текст. Остаётся один applied-пример того же пункта бэклога — `sre_incident_responder` (агент на пейджер-алерте открывает PR и ждёт approval).

## Оценка источника

Официальный код репозитория Anthropic — высшая ступень доверия. Извлечение сделано через `WebFetch` по `raw.githubusercontent.com` с явным требованием дословных цитат кода и markdown-ячеек; имена переменных окружения, точные вызовы SDK (`sessions.create`, `sessions.events.send`, `sessions.events.stream`, `files.upload`, `files.list`) и бета-флаг подтверждены цитатами модели-посредника, не домыслены.

## Проверка безопасности источника

Содержимое прочитано через официальный домен `raw.githubusercontent.com`. Инструкций, адресованных агенту-разборщику, не обнаружено — материал технический (код + пояснительный markdown), демонстрационный Slack-бот адресован собственному Slack-workspace примера, не агенту этой вики.

## Связи

- Сущности: [[claude-managed-agents]] (дополнена разделом ниже)
- Источники: [[claude-cookbook-managed-agents-data-analyst]] (агент, который здесь оборачивается в бота), [[claude-cookbook-managed-agents-versioning-monitoring]] (закрепление версии агента), [[claude-cookbook-managed-agents-skills-geo]], [[claude-cookbook-managed-agents-advisor-budget]], [[claude-cookbook-managed-agents-mongodb-planbig]], [[claude-cookbook-managed-agents-iterate-explore]], [[claude-cookbook-managed-agents-issue-outcome-grader]], [[claude-cookbook-managed-agents-hitl-multiagent]], [[claude-cookbook-managed-agents-production-memory]] (предыдущие куски того же пункта бэклога)
- Концепты: [[ai-security-by-design]] (закрепление версии как продакшн-дисциплина, не только демонстрация примитива)
