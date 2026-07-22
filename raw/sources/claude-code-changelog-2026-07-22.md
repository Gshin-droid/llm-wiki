# Claude Code CHANGELOG.md — версии 2.1.216–2.1.217

Источник: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
Дата снятия снапшота: 2026-07-22
Диапазон: две версии, вышедшие с прошлого снапшота ([[claude-code-changelog-snapshot-2026-07-20]], покрывал до 2.1.215)

## 2.1.217

Added emoji shortcode autocomplete (e.g., `:heart:` for ❤️). Improved transcript write failure warnings. Fixed a memory leak where truncated MCP tool outputs retained full untruncated results. Resolved Windows auto-update failures that could remove `claude.exe`. Fixed background session isolation issues with symlinked directories. Corrected auto-compact triggering for Opus 4.8 on Bedrock. Restored corporate mTLS, TLS-verify, OAuth scope, and proxy settings in Desktop sessions. Enhanced screen reader startup announcements. Fixed managed settings for OTEL telemetry endpoints. Resolved `--resume`/`--continue` failures with malformed attachments. Addressed Remote Control permission prompt visibility. Fixed background shell termination issues. Resolved `.CLAUDE.md`/`SKILL.md` brace expansion causing crashes. Improved transcript preview positioning. Enhanced footer PR badge clickability. Adjusted login-expiry warning timing. Capped frontend plugin suggestion impressions. **Implemented concurrency limits for subagents with configurable depth nesting.** **Fixed `--max-budget-usd` enforcement for background subagents.**

## 2.1.216

**Added `sandbox.filesystem.disabled` setting for selective isolation.** Fixed quadratic performance degradation in long sessions. Resolved auto mode OAuth token expiration issues. Improved AskUserQuestion handling. Fixed Claude Code web re-asking questions after idle periods. Addressed multiple UI and session management bugs. Fixed background agent worktree isolation and git redirection. Resolved undeletable background sessions. Corrected daemon lockfile stale PID handling. Enhanced various command validations across Bash and PowerShell. Improved error messages for network paths, workflow symlink following, and MCP reauthentication. Fixed fullscreen mode dialog rendering and clipping issues. Enhanced `/config` validation. Resolved Prometheus metrics endpoint formatting. Fixed plugin skill caching and slash-command autocomplete. Improved telemetry accuracy for permission denials and user interrupts. Enhanced `/fork` confirmation presentation. Improved cloud session stability with conversation recovery on container restarts.

## Дополнительно: официальная документация sandboxing

`sandbox.filesystem.disabled` описана подробно на https://code.claude.com/docs/en/sandboxing (раздел "Disable filesystem isolation", требует v2.1.216+):

- Сэндбокс Claude Code имеет два независимых слоя: filesystem isolation (какие пути можно читать/писать) и network isolation (какие домены доступны). `sandbox.filesystem.disabled: true` отключает **только** первый слой, второй продолжает работать.
- Назначение: инструменты вроде `kubectl`/`terraform`/сложные сборочные тулчейны иногда требуют широкого доступа к файловой системе, но не должны получать сетевой доступ за пределы allowlist — раньше единственным вариантом было `excludedCommands` (полностью вне сэндбокса, теряется и файловая, и сетевая изоляция).
- Явное предупреждение источника: при отключённой файловой изоляции и авто-разрешённых командах сэндбоксированная команда может записать файлы, которые прочитает/выполнит более поздняя команда (shell rc-файлы, исполняемые файлы в `$PATH`, `~/.claude/settings.json`) — и таким образом расширить собственный доступ на следующий прогон. Рекомендация источника: включать `filesystem.disabled` только для доверенных нагрузок, не как общее решение "чтобы не мешало".
- Кто может включить: только `user`/managed settings и флаг `--settings`; `.claude/settings.json`/`.claude/settings.local.json` проекта — не могут (проект не может сам себе ослабить изоляцию). Если managed settings уже задают `sandbox.filesystem` или список `credentials.files` — только managed settings могут переключить `disabled`.
- Побочный эффект отключения: перестают действовать `filesystem.denyRead` и `credentials.files` (deny на чтение конкретных путей вроде `~/.aws/credentials`), при этом `credentials.envVars` (deny/mask переменных окружения) продолжают действовать — они не зависят от файлового слоя.
