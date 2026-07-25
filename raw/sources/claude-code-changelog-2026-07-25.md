# Claude Code CHANGELOG.md — версии 2.1.218–2.1.219

Источник: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
Дата снятия снапшота: 2026-07-25
Диапазон: две версии, вышедшие с прошлого снапшота ([[claude-code-changelog-snapshot-2026-07-22]], покрывал до 2.1.217)

## 2.1.219

- Introduced Claude Opus 5 as default, featuring 1M context and fast mode pricing
- Added `sandbox.network.strictAllowlist` to block non-approved hosts without prompting
- Implemented `DirectoryAdded` hook firing after mid-session directory registration
- Enhanced stream-json with `mcp_server_errors` listing skipped MCP config entries
- Added `workflowSizeGuideline` settings for customizing workflow agent count recommendations
- Enabled nested subagent forwarding in stream-json output at spawn depth 2+
- Fixed text output loss on mid-stream API errors during `/config -p`
- Enhanced MCP connection errors with HTTP status details and whitespace warnings
- Restored permissions approved during self-hosted runner restarts
- Corrected Fable model row cache display for eligible plans
- Improved SIGTERM handling during runner initialization for clean deregistration
- Added structured failure categories for runner and session failures
- Fixed Opus row display to show context window information
- Corrected copy-on-select behavior in GNU screen environments
- Fixed Remote Control fast-mode status after model switches
- Enhanced bash path validation with warnings for invalid `CLAUDE_CODE_GIT_BASH_PATH`
- Fixed Vim mode navigation from empty prompts
- Improved screen-reader keystroke feedback
- Enhanced error messaging for Remote Control availability restrictions
- Improved `--teleport` output showing repo checkout information
- **Changed dynamic workflows to medium-size default (fewer than 15 agents)**
- Updated MCP allowlist/denylist variable resolution precedence
- Refined model picker highlighting to emphasize newest releases
- Added current workflow size to status line with config navigation hint
- Removed Opus 4.7 from fast mode support
- Updated claude-api skill with Opus 5 default and migration path
- **Increased subagent nesting depth to 3 levels by default**

## 2.1.218

- Redesigned `/code-review` to run as background subagent
- Added screen-reader announcements for word/line deletion operations
- Fixed Windows path corruption with `\u`-prefixed segments
- Prevented accidental conversation loss via arrow key navigation
- Fixed multi-line paste collapsing with incorrect newline encoding
- Corrected `/context` token usage after compaction
- Enhanced `/ultrareview` to accept descriptive arguments
- Fixed `/code-review ultra` in non-interactive sessions
- Improved gateway spend metering for mapped model ARNs
- Fixed emoji truncation mojibake and tool error handling
- Resolved engine teardown race creating phantom turns
- Eliminated spurious interruption messages and unpaired tool blocks
- Fixed VoiceOver space echoing in screen-reader mode
- Enhanced plugin panel cursor positioning for accessibility
- Resolved crashes from deeply nested directory/UI tree operations
- Fixed PR event loss on immediate session exit
- Improved Bedrock setup wizard profile verification
- Enhanced turn duration measurements with monotonic clock
- Fixed MCP authentication notice overcounting
- Corrected prompt history entry handling race conditions
- Fixed context-overflow retry loop with backgrounding caps
- **Enforced workspace trust for untrusted folder hooks**
- Resolved fork-session lineage loss during compaction
- Fixed malformed delta attachment session crashes
- Improved `/ultrareview` error feedback for corrections
- **Enhanced auto mode dangerous-command adjudication**
- Improved sandbox command restrictions for IDE interactions
- Enhanced trust dialog repository clarity
- **Changed `/deep-research` to manual-only invocation**
- Adjusted plan mode Bash assumptions for auto classifier
- Added fast-mode change announcements
- Modified benign setting changes to skip approval prompts
- Restricted agent names from containing `:` character
- Expanded skill boolean value acceptance options
- Fixed remote session heartbeat continuation post-restart

## Расхождение: changelog заявляет смену дефолта глубины вложенности, официальная документация — ещё нет (проверено 2026-07-25)

Changelog-строка v2.1.219 — "Increased subagent nesting depth to 3 levels by default". Официальная страница `code.claude.com/docs/en/sub-agents` перечитана целиком в этом прогоне (WebFetch) на предмет этой конкретной строки — и **не подтверждает** смену: текст по состоянию на 2026-07-25 всё ещё гласит "By default, a subagent can't spawn subagents of its own" и приводит только историческую врезку "From Claude Code v2.1.172 through v2.1.216, subagents could nest by default, up to five layers deep, and the limit couldn't be changed" (то есть описывает переход 5-уровней → 0, зафиксированный в v2.1.217, и ни словом не упоминает переход к 3). Ни в разделе про `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`, ни в разделе про переменные окружения нового значения по умолчанию "3" не встретилось.

Это третий цикл того же паттерна лага документации за changelog, что и в 07-22/07-23 (тогда доки досогласовались за 1 день). Не считаю changelog-строку недостоверной, но и не переношу "3" в вики-страницы как подтверждённый факт до тех пор, пока официальная документация не даст того же числа — зафиксировано как открытый пункт на [[claude-code]] и в `wiki/gaps-backlog.md`, для допроверки следующим прогоном.
