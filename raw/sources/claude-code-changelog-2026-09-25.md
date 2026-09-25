---
source: официальный CHANGELOG.md репозитория anthropics/claude-code
url: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
retrieved: 2026-09-25
covers: v2.1.274–v2.1.282 (v2.1.272–v2.1.273 в файле отсутствуют)
---

# Changelog (выборка, версии 2.1.274–2.1.282)

Полный список версий длиннее сотен строк каждая (в основном рутинные UI/VSCode/Claude Tag фиксы). Ниже — пункты, отобранные как имеющие вес для практики этой вики; полный текст доступен по `url` выше.

## 2.1.282 (дата не указана отдельно в файле, следует за 2.1.281 от 23.09)
- Fixed continued/resumed sessions re-sending earlier messages in changed form
- Fixed extended thinking being dropped when slash commands run during model work
- Fixed continued conversations losing extended thinking when relaunched with modified `--tools` list
- Fixed sessions failing with "Invalid `data` in `redacted_thinking` block" error
- Fixed compaction failing on refused summarization requests; now retries on fallback model
- Fixed CLAUDE.md/rules read through symlinks reaching macOS `/Network` or `/home`
- Fixed Bash permission rules with mid-pattern `:*` being skipped from settings files
- Fixed managed settings ignoring mistyped boolean lock key values
- Fixed managed `permissions`, `autoMode`, `worktree`, `attribution` settings ignored when nested value invalid
- Fixed repository/user skills pre-approving own tools under managed `allowManagedPermissionRulesOnly`
- Added `maxProseWidth` setting capping Claude's prose width in wide terminals
- Added startup notice and `/status`/`claude doctor` entries listing ignored telemetry variables

## 2.1.281 (September 23, 2026)
- Added Claude apps gateway support for newer Claude Desktop keys in policy blocks (`blockReadsOutsideWorkingDirectories`, `disableBypassPermissionsMode`)
- Added `assume_role` on Bedrock upstreams for IAM role assumption (cross-account via STS)
- Added `guardrail: {id, version}` on Bedrock upstreams applying Amazon Bedrock guardrails
- Added `telemetry.resource_attributes` to gateway config for fixed telemetry labels
- Added `"attribution": false` in `settings.json` hiding all commit/PR attribution
- Added auto mode recommendation to `/insights`
- Fixed crash during API request retry
- Fixed turn retrying indefinitely ignoring `--max-turns`
- Fixed resumed sessions re-sending earlier turns in changed form
- Fixed resuming very large session restoring only last messages
- Fixed session resumed after restart missing prompt cache
- Fixed prompt cache lost when MCP server disconnects mid-conversation
- Fixed responses cut short by proxy shown as complete
- Fixed tool calls running twice on duplicated stream events
- Fixed responses failing with "Content block not found" when proxy drops event
- Fixed stop reason lost when proxy sends trailing usage frame
- Fixed `CLAUDE_CODE_RETRY_WATCHDOG` failing after 429/529 waits
- Changed auto mode reviewing read-only/sandboxed commands
- Changed `CLAUDE_CODE_AUTO_MODE_SERVER` applying on direct API

## 2.1.280 (следует за 2.1.278, до 23.09)
- Added Claude Opus 5.5 as default Opus model — см. [[claude-opus-5-5-launch]]
- Changed default model Pro/Team Standard from Sonnet to Opus

## 2.1.278
- Changed auto mode defaulting to server-side classifier not charging overhead
- Changed auto mode on API/Enterprise/Bedrock/Vertex/Foundry/gateways to default server classifier
- Added `Auto mode server` row to `/status`

## 2.1.277
- Added AGENTS.md support reading instead of CLAUDE.md
- (плюс: связанный по теме фикс `installed_plugins.json` без коммита — уже разобран в вики как относящийся к Plugin4Shell, см. [[plugin4shell-vulnerability]])

## 2.1.276
- Fixed every request failing with `400 … Input tag 'advisor_20260301'`

## 2.1.275/2.1.274 — рутинные фиксы (MCP, память, self-hosted runner), без headline-изменений практики.
