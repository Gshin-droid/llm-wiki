---
source: официальный CHANGELOG.md репозитория anthropics/claude-code
url: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
retrieved: 2026-10-01
covers: v2.1.284-v2.1.286 (даты по code.claude.com/docs/en/changelog — 28, 29 и 30 сентября 2026 соответственно)
---

# Changelog (выборка, версии 2.1.284-2.1.286)

Три новые версии с прошлого снапшота (09-28, версия 2.1.283) — окно 28-30.09.2026.

## Version 2.1.284 (2026-09-28)

### Added
- Claude Sonnet 5.5 model as default Sonnet on Anthropic API
- Dollar amounts to spend limits in `/usage` and status line
- Keybinding actions for effort slider control
- `/rate-limit-options` command for subscribers
- `/mcp reconnect all` for retrying failed connections
- Gateway warnings for empty `availableModels` policies

### Fixed
- Damaged response streams showing raw errors instead of retrying
- "Prompt is too long" errors persisting after compacting
- Unavailable models showing bare messages without proper notices
- MCP tool calls failing mid-reconnection
- Fullscreen rendering issues with scroll position and terminal output
- Vim mode cursor placement and text manipulation bugs
- Permission prompt issues in narrow terminals
- Various Remote Control and artifact publishing issues

### Improved
- Usage-limit wait display consolidation
- Startup time by building only needed schema parts
- Artifact page design with visible planning steps
- List navigation with page keys and mouse support
- Compaction spinner showing elapsed time

## Version 2.1.285 (2026-09-29)

### Added
- `CLAUDE_CODE_DISABLE_WEB_FETCH` environment variable
- `claude --desktop` command for opening desktop app
- `claude plugin configure` for plugin option management
- `allowedProviders` managed setting to limit API provider choices

### Fixed
- Plugin and marketplace installs ignoring SSH configuration
- Claude Code refusing to start when denied managed settings access
- Cloud sessions refusing artifact updates after restart
- Files left out after single failed download in Remote Control
- Model switching mid-session leaving wrong token limits
- SSH passphrase prompts interfering with fetches
- MCP servers staying available after being switched off
- Various permission prompt and artifact publishing issues

### Improved
- Plugin marketplace error messages naming refusal reasons
- Bedrock and Vertex model fallback handling
- Artifact tool publish results using fewer tokens
- SDK liveness during non-streaming fallback requests
- Performance with many permission rules and MCP tools

## Version 2.1.286 (2026-09-30)

### Added
- Permission prompt now displays "2 of 5" style counts when multiple requests stack
- Mouse support for "N more" list rows in fullscreen mode with hover/pressed states
- Improved commit guidance when project includes a `verify` skill

### Fixed
- Claude Code processes opening duplicate login browsers when auth credentials expire
- `claude --resume` and `--continue` losing turns after parallel tool calls
- API 400 errors from tools returning non-text objects
- Cloud sessions with large histories never waking up
- Gateway spend meter pricing and token counting issues
- macOS sessions showing incorrect login status after successful `/login`
- Model unavailability causing all turns to fail without fallback retry
- Remote Control sessions remaining connected after policy disablement
- Fallback model retries running at wrong speed
- MCP authentication reminder repeating after successful re-authentication
- Various file attachment, redaction, and transcript issues
- Subagent transcript display issues and hand-back message formatting

### Improved
- List scrollbars in fullscreen with arrow navigation
- External editor opening at cursor position for line-aware editors
- Slash command suggestions responsiveness with many skills installed
- Output style picker now opens on current style
