# Claude Cookbooks — Managed Agents: Data Analyst Agent (applied-пример)

**Дата загрузки:** 2026-09-02
**Автор:** Anthropic (официальный репозиторий)
**Опубликовано:** н/д (репозиторий обновляется без дат релиза на файл)
**Тип:** официальный код-репозиторий, notebook (`.ipynb`)
**Ссылка:** https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/data_analyst_agent.ipynb
**Raw:** не клипован — прочитано через `WebFetch` на `raw.githubusercontent.com` (первоисточник сам по себе официальный код, не пересказ)

## Саммари

Первый из трёх applied-примеров того же пункта бэклога «Managed Agents cookbooks» (заведён 2026-08-17, гайдовая часть 16/16 закрыта 2026-09-01, [[claude-cookbook-managed-agents-skills-geo]]). В отличие от гайдовых `CMA_*.ipynb`, которые демонстрируют один примитив API, `data_analyst_agent.ipynb` — сквозной прикладной пример: агент превращает загруженный CSV в HTML-отчёт с графиками, без вмешательства человека в процессе. Это не новый примитив, а сборка уже известных страницей кусков (Files API, `agent_toolset_20260401`, `environments`/`sessions`) в одну конкретную задачу.

## Что взято в вики

- **System prompt как единственный носитель бизнес-логики.** Агент не получает специальных инструментов для анализа данных — только универсальный `agent_toolset_20260401` (bash/read/write/edit/glob/grep/web_fetch/web_search, веб-тулы отключены явно). Формат отчёта, качество графиков, путь сохранения — всё задано текстом system prompt, а не параметрами платформы: «produce a publication-quality report», графики строить как отдельные объекты `go.Figure()`, встраивать через `fig.to_html(include_plotlyjs=False, full_html=False)`, писать Python-скрипты в файл и исполнять `python3 script.py` (а не интерактивный REPL).
- **Модель — `claude-sonnet-4-6`**, не Opus/Sonnet 5 семейства, которое видит остальная часть страницы источника у большинства других куском этого же пункта бэклога. Не расхождение и не устаревание: нотбук не привязан к дате обновления так же жёстко, как changelog, а более старая/дешёвая модель может быть осознанным выбором авторов примера для задачи такого класса. Зафиксировано как факт нотбука, не перенесено как общая рекомендация.
- **Permission policy по умолчанию — `always_allow`.** У агента `"permission_policy": {"type": "always_allow"}` при создании тулсета — сессия работает без пауз на подтверждение вызовов bash/read/write/edit, при этом web_search/web_fetch отдельно выключены. Иллюстрация уже известного принципа «минимальные привилегии по каждому тулу отдельно» ([[ai-security-by-design]]) на конкретном примере: широкий allow там, где риск (файловая песочница), точечный deny там, где риск не нужен задаче (сеть).
- **Environment: `type: "cloud"`, `networking: {"type": "unrestricted"}`, `packages: {"pip": ["pandas", "plotly"]}`.** Первый на этой странице конкретный пример поля `packages` при создании environment — заранее объявленные pip-зависимости ставятся при сборке контейнера, а не устанавливаются агентом в рантайме.
- **Файлы: вход через Files API, выход через фиксированный путь.** Датасет монтируется в сессию как `resources=[{"type": "file", "file_id": dataset.id, "mount_path": MOUNT_PATH}]`; агент обязан положить результат в `/mnt/session/outputs/report.html` — только этот каталог персистится и становится доступен обратно через Files API (`scope_id=session.id`); всё, что записано вне него, теряется вместе с сессией. Раскрывает практическую сторону уже известного механизма файлового state — не просто «файлы можно передавать», а конкретный контракт входного/выходного пути.
- **Sessions.archive как явный шаг завершения.** Пример заканчивается вызовом `client.beta.sessions.archive(session.id)` — сессия помечается закрытой явно, а не оставляется в неопределённом состоянии после получения результата.

## Что не взято / лиды

Остаются два applied-примера того же пункта: `slack_data_bot` (оборачивает этого же агента в Slack-бота) и `sre_incident_responder` (агент на пейджер-алерте открывает PR и ждёт approval). `slack_data_bot` явно надстраивается над этим нотбуком — логично брать следующим куском, чтобы видеть разницу пример-к-примеру, а не пропускать промежуточное звено.

## Оценка источника

Официальный код репозитория Anthropic — высшая ступень доверия. Извлечение сделано через `WebFetch` по `raw.githubusercontent.com` с явным требованием дословных цитат кода и markdown-ячеек; параметры (`always_allow`, `unrestricted`, точный путь `/mnt/session/outputs/`) подтверждены цитатами модели-посредника, не домыслены.

## Проверка безопасности источника

Содержимое прочитано через официальный домен `raw.githubusercontent.com`. Инструкций, адресованных агенту-разборщику, не обнаружено — материал технический (код + пояснительный markdown), демонстрационный system prompt адресован managed-агенту внутри примера, не агенту этой вики.

## Связи

- Сущности: [[claude-managed-agents]] (дополнена разделом ниже)
- Источники: [[claude-cookbook-managed-agents-skills-geo]], [[claude-cookbook-managed-agents-advisor-budget]], [[claude-cookbook-managed-agents-mongodb-planbig]], [[claude-cookbook-managed-agents-versioning-monitoring]], [[claude-cookbook-managed-agents-iterate-explore]], [[claude-cookbook-managed-agents-issue-outcome-grader]], [[claude-cookbook-managed-agents-hitl-multiagent]], [[claude-cookbook-managed-agents-production-memory]] (предыдущие куски того же пункта бэклога)
- Концепты: [[ai-security-by-design]] (минимальные привилегии по тулу — always_allow на файлах, deny на сети)
