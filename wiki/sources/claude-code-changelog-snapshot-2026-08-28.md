# Claude Code changelog 2026-08-28

**Дата загрузки:** 2026-08-28
**Автор:** [[claude-code]]
**Опубликовано:** 2026-08-26 — 2026-08-28 (версии)
**Тип:** официальная документация (changelog)
**Ссылка:** https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
**Raw:** `raw/sources/claude-code-changelog-2026-08-28.md`

## Саммари

Прогон новостного разведчика через три дня после предыдущего снапшота (2026-08-25, покрывал до 2.1.245). Вышли **2.1.246–2.1.250** (2.1.249 в файле отсутствует — не опубликована или пропущена нумерация). Официальные **Claude Platform release notes** за то же окно (26–27 августа) тоже проверены: Compliance API (сессии Cowork/Claude Code) вышел из беты, Admin API появился в `ant` CLI и SDK-клиентах, добавлены personal/service account keys, бета-заголовки `files-api-2025-04-14`/`skills-2025-10-02` перестали требоваться в очередной партии SDK — всё организационное/enterprise, без веса для практики этой вики (нет managed-организации, нет Admin API использования), не разбирается отдельно.

Главная версия окна — **2.1.248**: без единого headline-анонса, но с двумя пунктами прямого практического веса — новым режимом минимальных привилегий `--restricted` и расширением TTL промпт-кэша до гранулярности одного агента. Плюс в 2.1.247 — `/claude-api cost-optimize`, CLI-команда, дословно реализующая чеклист, уже задокументированный в этой вики.

## Находка 1: `--restricted` — режим минимальных привилегий на уровне процесса (2.1.248)

*"Added `--restricted` (or `CLAUDE_CODE_RESTRICTED=1`): removes the built-in tools that run commands or code and `WebFetch` (unless named in `--tools`), keeps file tools inside the working directory, refuses `bypassPermissions`, and ignores user, project and local settings files"*.

Не точечный bypass-фикс (как почти вся серия находок 07-19…08-19 на [[ai-security-by-design]]), а новый **явный режим запуска**: убирает инструменты исполнения кода/команд и `WebFetch` целиком (если явно не разрешены через `--tools`), запирает файловые инструменты в рабочей директории, отказывается запускаться с `bypassPermissions` и игнорирует user/project/local settings — то есть режим нельзя ослабить ни флагом, ни конфигом снаружи. Это прямое воплощение принципа 1 («минимальные привилегии») и принципа 6 («безопасность по умолчанию») из [[ai-security-by-design]], но применённое не патчем к существующему поведению, а отдельным явным режимом для задач, которым в принципе не нужен весь набор инструментов агента (например, только чтение и анализ). Не заменяет сэндбокс (`sandbox.filesystem.disabled`/`sandbox.network.strictAllowlist`) — сокращает набор инструментов, а не изолирует их исполнение.

Дополнено в [[ai-security-by-design]].

## Находка 2: `experimental.cacheTtl` — TTL промпт-кэша на уровне одного агента (2.1.248)

*"Added `experimental.cacheTtl` (`"5m"` or `"1h"`) to agent frontmatter: a per-agent prompt cache TTL used when no subagent TTL setting is configured"*.

Прямое продолжение находки прошлого снапшота ([[claude-code-changelog-snapshot-2026-08-25]], 2.1.243): `promptCacheTtl`/`subagentPromptCacheTtl` дали раздельный TTL для основного диалога и субагентов **как класса**; теперь можно задать TTL для **конкретного** агента в его frontmatter (`.claude/agents/*.md`), в обход дефолта субагентов. Полезно для агента, который системно работает дольше пяти минут между обращениями к модели (например, ждёт внешнего процесса), но не заслуживает часового TTL всей категории субагентов. Помечена `experimental` — единственная находка окна с таким статусом, стоит держать в уме нестабильность API перед тем, как полагаться на неё в production-конфигурации.

Дополнено в [[claude-api-cost-optimization]].

## Находка 3: `/claude-api cost-optimize` — CLI-реализация уже задокументированного чеклиста (2.1.247)

*"Added `/claude-api cost-optimize` to profile an existing project's Claude API spend and work through cost levers (caching, token hygiene, batch, effort, model choice) one measured change at a time"*.

Список рычагов в описании команды — caching, token hygiene, batch, effort, model choice — совпадает по порядку и по составу с чеклистом на [[claude-api-cost-optimization]] (prompt caching → input token management → agent-loop efficiency → output token management → batch API → model selection), собранным из отдельного официального notebook'а ([[claude-cookbook-cost-optimization]]). Раньше методология существовала как самостоятельный документ, который нужно было применять вручную шаг за шагом; теперь то же самое — встроенная subcommand, профилирующая **конкретный** проект и предлагающая рычаги по одному измеренному изменению за раз, а не общий текст. Прямое подтверждение того, что чеклист в вики не устарел — Anthropic формализовала его в инструмент почти дословно тем же порядком шагов.

Дополнено в [[claude-api-cost-optimization]].

## Малое

- **Cross-session messaging расширен на Bedrock/Vertex/Foundry и на конфигурации с отключённой телеметрией** (2.1.248) — *"Added cross-session messaging (`SendMessage` / `ListAgents`) between sessions on the same machine on Bedrock, Vertex, and Foundry, and when telemetry is disabled"*. Не противоречит уже записанному в [[claude-code-changelog-snapshot-2026-08-10]] межмашинному `SendMessage` (тот работал на обычном Anthropic API) — это отдельное расширение того же канала на деплойменты, где межмашинная версия раньше не работала вовсе, только в пределах одной машины. Дополнено в [[claude-code]].
- **`SendFeedback`-инструмент** (2.1.247) — Claude сам может подготовить черновик фидбека о проблеме сессии для отправки через `/feedback`.
- **Auto mode вкладка в `/permissions`** (2.1.246) — просмотр и правка classifier-правил auto mode из интерфейса, не через settings.json напрямую.
- **`claude self-hosted-runner --client-label`** (2.1.248) — метка раннера, переопределяющая дефолтный hostname; дополняет [[claude-code-self-hosted-environments-docs]].
- **Server-managed settings diagnostics** (2.1.248) — `/doctor`/`/status` теперь явно объясняют, почему managed settings не загрузились или не были запрошены.
- **`/usage-credits` для Enterprise через AWS Marketplace** (2.1.248) — организационная функция запроса повышенного лимита, не относится к практике этой вики.
- Десятки рутинных багфиксов терминала/UI/MCP/плагинов — в raw-снапшоте целиком, на страницу вынесены только пункты с прямым практическим весом.
- **Claude Platform release notes 26–27.08** — Compliance API (сессии Cowork/Claude Code) вне беты, Admin API в `ant` CLI/SDK, personal/service account keys, снятие бета-заголовков Files/Skills API в очередной партии SDK — все организационные/enterprise, проверены и сознательно не разбираются: не пересекаются ни с одной практикой, которую ведёт эта вики.

## Оценка источника

Официальный `CHANGELOG.md` репозитория `anthropics/claude-code` — высшая презумпция доверия по `references/source-evaluation.md`. Прямой `raw.githubusercontent.com`-фетч через Bash отклонён разрешениями окружения сессии (тот же паттерн, что 08-19…08-28 — не сетевой фильтр); текст получен через `WebFetch` тем же официальным доменом с явным требованием дословных цитат, свёрен построчно с ответом модели-посредника.

## Проверка безопасности источника

Открытая официальная документация Anthropic, только описание изменений продукта. Исполняемых инструкций или текста, замаскированного под команды агенту, не обнаружено.

## Связи
- [[claude-code]] — обновлён раздел changelog («Обновление 2.1.246–2.1.250»), дата «Актуально на» сдвинута на 2026-08-28
- [[ai-security-by-design]] — дополнена разделом про `--restricted`
- [[claude-api-cost-optimization]] — дополнена пометками про `experimental.cacheTtl` и `/claude-api cost-optimize`
- [[claude-code-changelog-snapshot-2026-08-25]] — предыдущий снапшот в серии
