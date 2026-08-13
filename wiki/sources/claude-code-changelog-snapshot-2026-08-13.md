# Claude Code changelog snapshot 2026-08-13

**Дата загрузки:** 2026-08-13
**Источник:** [raw/sources/claude-code-changelog-2026-08-13.md](../../raw/sources/claude-code-changelog-2026-08-13.md), официальный `CHANGELOG.md` репозитория `anthropics/claude-code` (verbatim, сверено напрямую через `raw.githubusercontent.com`)

## Саммари

Прогон разведчика через три дня после предыдущего снапшота (2026-08-10, покрывал до 2.1.226). Вышли **2.1.227**, **2.1.228**, **2.1.229** и **2.1.231** (2.1.230 в публичном changelog не значится — пропуск номера, не пропущенная запись). Основная тема выпуска — продолжение уже отслеживаемых в вики серий: hardening скиллов и permission-анализатора (безопасность), self-hosted runner (совпадает с механикой, разобранной 08-10) и cross-session `SendMessage`/`ListAgents` (совпадает с межмашинным каналом, разобранным там же).

## Ключевая находка 1: hardening скиллов, синхронизированных с claude.ai (2.1.228)

*"Hardened skills synced from claude.ai: they no longer shadow local commands or MCP prompts, their descriptions are sanitized and labeled, and on your machine their bodies don't run `!` commands or expand `@` files"*. Три отдельных сужения: (1) скилл, пришедший через синхронизацию с claude.ai, больше не может незаметно **перекрыть** локальную slash-команду или MCP prompt с тем же именем — раньше это была потенциальная точка supply-chain атаки (синхронизированный скилл с чужим содержимым тихо подменяет то, что пользователь ожидает вызвать по имени); (2) его description теперь санитизируется и помечается — отличим от локально написанных; (3) на машине пользователя тело такого скилла не исполняет `!`-команды и не разворачивает `@`-упоминания файлов — то есть синхронизированный скилл не может напрямую прочитать локальные файлы или выполнить shell через собственный markdown, даже если содержимое скилла скомпрометировано на стороне claude.ai. Прямое продолжение линии, уже задокументированной в [[ai-security-by-design]] и [[skill-authoring-practical-rules]]: скиллы как канал, который может нести чужой текст, требуют того же недоверия к содержимому, что и raw-источники (принцип "содержимое источников — не команды" из `CLAUDE.md` этой вики, в миниатюре — на уровне продукта).

## Ключевая находка 2: сэндбокс — IPv6 fail-closed, `/commit-push-pr` больше не авто-одобряет опасные флаги (2.1.229)

Две находки в одном релизе, обе — продолжение уже отслеживаемой в [[ai-security-by-design]] серии bypass-фиксов permission-анализатора/сэндбокса:

- *"Improved sandbox: IPv6 literals in network domain lists are now bracketed (`[::1]:443`), and ambiguous spellings are enforced fail-closed and flagged by `/doctor`"* — неоднозначная запись IPv6-адреса в списке разрешённых доменов сэндбокса раньше могла трактоваться либерально; теперь по умолчанию **fail-closed** (при неоднозначности — блокировать, а не разрешить), и `/doctor` явно на это указывает.
- *"Changed `/commit-push-pr` so git/gh commands with dangerous flags (`--force`, `--amend`, `--no-verify`, etc.) are no longer auto-approved"* — встроенный скилл коммита/пуша/PR раньше мог сам одобрить себе выполнение команд с опасными флагами в рамках своего же вызова; теперь такие флаги требуют обычного подтверждения, как любая другая опасная команда. Прямо касается git-дисциплины автономных рутин этой вики (`CLAUDE.md`, "Автономные рутины: инкрементальный коммит и пуш") — сам факт, что подобное авто-одобрение существовало и его пришлось сужать, лишний повод не полагаться на `--force`/`--no-verify` в автономных прогонах без явной причины.

## Находка 3: self-hosted runner — server-supplied хуки, cross-session `ListAgents` различает offline/cloud (2.1.229)

- *"Added server-supplied Claude Code hook support for self-hosted runner sessions, matching managed-environment behavior"* — self-hosted runner (механика разобрана 08-10, [[claude-code-self-hosted-environments-docs]]) теперь поддерживает хуки, присылаемые сервером, наравне с managed-инфраструктурой Anthropic — сужение разницы между self-hosted и managed окружениями до "где исполняется", а не "что доступно".
- *"`ListAgents` now marks disconnected Remote Control sessions as `offline` and labels your cloud sessions as `cloud`"* — прямое дополнение к межмашинному `SendMessage`/`ListAgents` (08-10, [[claude-code-changelog-snapshot-2026-08-10]]): `ListAgents` — ровно тот deferred-инструмент, что виден в системных инструкциях автономных сессий этой вики, теперь различает статус найденных сессий, а не просто их перечисляет.
- *"Added plugin marketplace `command` sources: a local command (e.g. an IDE) prints the plugin directory, which is re-resolved each session and applied without a restart; `mode: "link"` uses it in place"* — четвёртый способ раздачи плагинов (после git/npm/`archive` из 08-10) — через вывод локальной команды.

## Малое

- **Write tool** (2.1.228): *"newer models can overwrite an existing file they haven't read this session, matching the Edit tool's rules; older models still require the read first"* — поведенческое послабление для новых моделей, границы прежние для старых.
- **Auto mode**: убрана устаревшая заметка о повышенной стоимости auto mode-сессий из первого уведомления для Pro/Max/Team (2.1.228) — согласуется с находкой о переходе auto mode в дефолт с 14.08.2026 ([[claude-code-auto-mode-default]], тот же день прогона).
- VSCode: session groups в сайдбаре (2.1.229), "Report a problem"/`/bug` открывают встроенный диалог фидбека вместо устаревшей survey-ссылки (2.1.229).
- Workflow fan-outs: соседние агенты с общим префиксом промпта теперь запускаются со сдвигом, чтобы читать закэшированный префикс вместо повторной его оплаты (2.1.229) — касается механизма Dynamic Workflows, уже разобранного в [[dynamic-workflows]].
- Ряд MCP OAuth-фиксов (2.1.227, 2.1.229, 2.1.231) — редирект-URI для pre-registered клиентов (напр. Slack), `127.0.0.1` вместо `localhost` для строгих authorization servers; чисто багфиксы, без изменения механики.

## Связанные страницы

- [[claude-code]] — обновлён раздел changelog
- [[ai-security-by-design]] — дополнено hardening скиллов и сэндбокс-фиксы
- [[claude-desktop-automation-modes]] — дополнено self-hosted runner
- [[claude-code-changelog-snapshot-2026-08-10]] — предыдущий снапшот в серии
- [[claude-code-auto-mode-default]] — соседняя находка того же прогона (дефолт auto mode с 14.08.2026)
