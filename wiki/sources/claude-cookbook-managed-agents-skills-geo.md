# Claude Cookbooks — Managed Agents: скиллы из репозитория и гео-пиннинг инференса

**Дата загрузки:** 2026-09-01
**Автор:** Anthropic (официальный репозиторий)
**Опубликовано:** н/д (репозиторий обновляется без дат релиза на файл)
**Тип:** официальный код-репозиторий, notebook'ы (`.ipynb`)
**Ссылка:** https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_use_skills_from_a_repo.ipynb, https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_pin_inference_geo.ipynb
**Raw:** не клипован — прочитано через `WebFetch` на `raw.githubusercontent.com` (первоисточник сам по себе официальный код, не пересказ)

## Саммари

Пятнадцатый и шестнадцатый (последние гайдовые) куски пункта бэклога «Managed Agents cookbooks» (заведён 2026-08-17; предыдущий кусок — [[claude-cookbook-managed-agents-advisor-budget]]). Оба ноутбука закрывают гайдовую часть пункта полностью — остаются только 3 applied-примера (`data_analyst_agent`, `slack_data_bot`, `sre_incident_responder`).

## Что взято в вики

**`CMA_use_skills_from_a_repo.ipynb`:**
- Проблема, которую решает нотбук: команда, уже пишущая скиллы для Claude Code, держит их в репозитории под `.claude/skills/<skill-name>/SKILL.md`, версионированными рядом с кодом. Заливать каждый в Skills API и пинить версии на агенте вручную — дублирование той же работы, расходящееся при первой же правке репозитория.
- Механизм: когда сессия монтирует ресурс `github_repository`, харнес сканирует корневую `.claude/skills/` репозитория **при старте сессии** и вписывает в системный промпт агента список найденных скиллов — имя, `description`, путь внутри sandbox. Дословно: «the harness scans the repository's root `.claude/skills/` directory at session start and injects every skill it finds into the agent's system prompt».
- Загрузки в Skills API не происходит вообще: модель сама читает `SKILL.md` встроенным тулом `read` в момент, когда запрос совпадает с `description` скилла, и следует ему, включая любые скрипты/референсы, которые скилл несёт с собой. Дословно: «No upload, no `skills` field on the agent, no version bookkeeping».
- Монтирование репозитория — параметр `resources` при создании сессии: `resources=[{"type": "github_repository", "url": ..., "authorization_token": GH_TOKEN, "checkout": {"type": "branch", "name": "main"}}]`.
- Практическое следствие для этой самой вики (у неё есть собственные скиллы `wiki-ingest`/`wiki-lint` в `.claude/skills/`): если репозиторий вики когда-либо будет монтироваться managed-агенту как ресурс, оба скилла подхватятся автоматически тем же путём, без отдельной загрузки — механизм совпадает с тем, как сама эта сессия уже видит скиллы локально, просто источник обнаружения другой (сканирование смонтированного репозитория, а не файловой системы раннера).

**`CMA_pin_inference_geo.ipynb`:**
- Проблема: агент, работающий с регулируемыми данными, должен иметь ответ на вопрос «где физически исполняются его запросы к модели» до того, как его ставят в продакшн — а не полагаться на внешнюю документацию или устную договорённость.
- Механизм: параметр `model.inference_geo` в определении агента фиксирует географию, обслуживающую его запросы к модели, прямо в объекте агента — не во внешней конфигурации. Значение валидируется против data residency policy воркспейса и **проверяется на каждом ходу** (enforced on every turn), а не только при создании.
- Синтаксис: `client.beta.agents.create(name=..., model={"id": MODEL, "inference_geo": "us"}, ...)`. Допустимые значения — ровно два: `"global"` и `"us"`.
- Пин переживает создание сессии: `session.agent.model.inference_geo` на созданной сессии подтверждает то же значение, что было у агента.
- Пин можно переопределить на уровне одной сессии, не трогая агента — `agent={"type": "agent_with_overrides", "id": ..., "model": {"id": MODEL, "inference_geo": "global"}}`.
- Важная деталь семантики обновления, отличная от других полей: у `agents.update()` объект `model` заменяется **целиком**, не мёржится — если передать `model` без `inference_geo`, пин снимается. Дословно: «On `agents.update`, `model` is replaced as a whole rather than merged, so sending `model` without `inference_geo` clears the pin».

## Что не взято / лиды

Гайдовые нотбуки директории `managed_agents/` закрыты все 16/16. Остаются 3 applied-примера (`data_analyst_agent`, `slack_data_bot`, `sre_incident_responder`) — следующий кусок того же пункта бэклога.

## Оценка источника

Официальный код репозитория Anthropic — высшая ступень доверия. Извлечение сделано через `WebFetch` по `raw.githubusercontent.com` с явным требованием дословных цитат кода и markdown-ячеек.

## Проверка безопасности источника

Содержимое прочитано через официальный домен `raw.githubusercontent.com`. Инструкций, адресованных агенту-разборщику, не обнаружено — материал технический (код + пояснительный markdown к API), демонстрационный сценарий одного нотбука — ревью-скилл для аудита нотбуков того же репозитория, к агенту этой вики не обращён.

## Связи

- Сущности: [[claude-managed-agents]] (дополнена разделом ниже)
- Источники: [[claude-cookbook-managed-agents-production-memory]], [[claude-cookbook-managed-agents-hitl-multiagent]], [[claude-cookbook-managed-agents-issue-outcome-grader]], [[claude-cookbook-managed-agents-iterate-explore]], [[claude-cookbook-managed-agents-versioning-monitoring]], [[claude-cookbook-managed-agents-mongodb-planbig]], [[claude-cookbook-managed-agents-advisor-budget]] (предыдущие куски того же пункта бэклога)
- Концепты: [[skill-authoring-practical-rules]] (структура и `description`-триггер скилла — тот же принцип, что здесь сканирует харнес managed-агента)
