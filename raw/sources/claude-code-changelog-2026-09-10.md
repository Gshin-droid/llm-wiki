---
source: официальный CHANGELOG.md репозитория anthropics/claude-code
url: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
retrieved: 2026-09-10
covers: v2.1.261–v2.1.267
---

# Changelog

## 2.1.267
- Added `maxEffortLevel` setting to cap effort across all providers while allowing users to select lower levels
- Added `--system-prompt-snapshot off` flag for fresh system prompt rendering on each request
- Fixed Cowork scheduled tasks failing at startup for organizations requiring sandboxing
- Fixed Workflow `agent()` calls with large schemas being refused instead of checked by safety classifier
- Fixed marketplace entry path bypass vulnerability on macOS and Linux
- Fixed managed settings admission logic inverting for unreadable entries
- Fixed reasoning being dropped when MCP servers re-send tools
- Fixed tool disappearance mid-conversation from disconnected MCP rewriting tool lists
- Fixed background workers adding tools mid-session breaking prompt-cache
- Fixed mid-session MCP tools breaking prompt-cache in sessions without ToolSearch
- Fixed `/model` re-sending all tool definitions (prompt-cache miss)
- Fixed resumed sessions rewriting inline tool sets
- Fixed resumed sessions re-rendering tool descriptions
- Fixed prompt-cache misses with claude.ai connector tool changes
- Fixed resumed sessions rewriting MCP announcements and dropping thinking
- Fixed print-mode session resume breaking prompt-cache
- (full bug-fix/improvement/changed list, ~50 entries total — terminal/UI/VSCode/Claude Tag items omitted here, see upstream CHANGELOG.md for the complete text)

## 2.1.266
- Fixed environment variable `CLAUDE_CODE_USE_GATEWAY` forcing gateway sign-in and breaking API key configurations

## 2.1.265
- Added `user.email` and `user.groups` to telemetry for gateway sessions
- Added support for `--plugin-dir` pointing to plugin folders with dynamic loading
- Added 1 GB cap on tool results saved to disk
- Fixed plugin path backslash bypassing containment checks
- Fixed plugin directories starting with `..` wrongly refused
- Fixed occasional re-login requirements for SDK/VS Code sessions
- Fixed advisor tool re-decided per request
- Fixed artifact publish accepting nonexistent connector tools
- Fixed legacy HTTP+SSE MCP servers never connecting
- (full list, ~35 entries total — terminal/UI/VSCode items omitted here, see upstream CHANGELOG.md for the complete text)

## 2.1.263
- Bug fixes and reliability improvements

## 2.1.261
- Added organization policy loading diagnostics to `/status` and `claude doctor`
- Added `bashOutputMaxChars` and `taskOutputMaxChars` settings (up to 128K)
- Added `--append-subagent-system-prompt-file` for large prompts
- Added `/skill-doctor` to identify unused skills and their context cost
- Fixed Bedrock setup wizard hanging and timeout issues
- Fixed cloud sessions losing synced plugins
- Fixed resumed sessions losing hook output around parallel tool calls
- Fixed high CPU usage on failed background agent resume
- (full list, ~45 entries total — terminal/UI/VSCode items omitted here, see upstream CHANGELOG.md for the complete text)
