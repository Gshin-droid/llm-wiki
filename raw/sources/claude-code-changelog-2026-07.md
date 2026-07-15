# Claude Code CHANGELOG.md — снапшот версий 2.1.172–2.1.205

**URL:** https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md (raw: https://raw.githubusercontent.com/anthropics/claude-code/refs/heads/main/CHANGELOG.md)
**Загружено:** 2026-07-09 (автономный ежедневный запуск)
**Тип фиксации:** WebFetch вернул топ ~30 версий (наиболее свежие сверху), дословно приведены ниже.

## 2.1.205
- Auto mode now blocks tampering with session transcript files
- Fixed `--json-schema` producing unstructured output with invalid schemas
- Fixed messages lost when turns end at `--max-turns` limit
- Fixed Windows worktree removal deleting files outside worktree with junctions
- Fixed background agents showing stale status after resumption
- Improved auto mode to ask before running `rm -rf` on unresolved variables

## 2.1.204
- Fixed hook events not streaming during SessionStart hooks in headless sessions

## 2.1.203
- Added login-expiration warning for background sessions
- Added grey pause badge when in manual permission mode
- Fixed background sessions becoming unresponsive after daemon token expiration
- Fixed context-usage indicator re-analyzing entire transcript after each turn
- Fixed background agents inheriting stale PATH from daemon on Windows
- Fixed worktree creation rejecting nested repositories

## 2.1.202
- Added "Dynamic workflow size" setting for controlling workflow scale
- Added OpenTelemetry attributes for workflow-spawned agents
- Fixed `/rename` on background sessions being reverted on job restart
- Fixed transient mTLS handshake failures during certificate rotation

## 2.1.201
- Claude Sonnet 5 sessions no longer use mid-conversation system role

## 2.1.200
- Changed `AskUserQuestion` dialogs to no longer auto-continue by default
- Changed "default" permission mode to "Manual" across all interfaces
- Fixed background sessions becoming permanently unresponsive after token staleness

## 2.1.199
- Stacked slash-skill invocations now load up to 5 leading skills
- Fixed SSL certificate errors showing misleading guidance before retries
- Fixed streaming responses discarded on mid-stream overloaded errors
- Fixed subagents cut off by rate limits silently failing

## 2.1.198
- Subagents now run in background by default
- Claude in Chrome is now generally available
- Added background agent notifications with Notification hook
- Added `/dataviz` skill for chart and dashboard design
- Background agents now auto-commit, push, and open draft PRs

## 2.1.197
- Introduced Claude Sonnet 5 with native 1M-token context window

## 2.1.196
- Added organization default models support
- Added readable default session names for easier identification
- Added clickable file attachments in chat
- Improved background agent reliability with process handoff on Windows

## 2.1.195
- Added `CLAUDE_CODE_DISABLE_MOUSE_CLICKS` to disable clicks while keeping scroll
- Fixed hook matchers with hyphens accidentally substring-matching

## 2.1.193
- Added `autoMode.classifyAllShell` for routing all shell commands through classifier
- Added auto-mode denial reasons to transcript and permission interface
- Added live file path autocomplete to bash mode
- Added automatic memory-pressure reaping for idle background shells

## 2.1.191
- Added `/rewind` support for resuming before `/clear` was run
- Fixed background agents resurrecting after being stopped
- Fixed `/voice` showing generic message when org policy disabled it

## 2.1.190
- Bug fixes and reliability improvements

## 2.1.187
- Added `sandbox.credentials` setting blocking credential file access
- Added org-configured model restrictions to model picker
- Added mouse click support to select menus in fullscreen mode

## 2.1.186
- Added `claude mcp login/logout` for CLI authentication without interactive menu
- Added status filtering to `/workflows` agent detail view
- Added "Skills" section to `/plugin` Installed tab
- Fixed streaming requests failing after machine wake from sleep

## 2.1.185
- Stream-stall hint now reads "Waiting for API response" instead of "No response"

## 2.1.183
- Improved auto mode: destructive git and infrastructure commands now blocked
- Added model-restriction warnings when deprecated models auto-update

## 2.1.181
- Added `/config key=value` syntax to set settings from prompt
- Added `sandbox.allowAppleEvents` opt-in for sandboxed macOS commands
- Added `CLAUDE_CLIENT_PRESENCE_FILE` for suppressing mobile notifications

## 2.1.179
- Fixed mid-stream connection drops preserving partial responses
- Fixed mouse-wheel scrolling in WSL2 under Windows Terminal
- Fixed sandbox denial causing session to become unusable

## 2.1.178
- Agent teams removed TeamCreate/TeamDelete; teams now implicit
- Added `Tool(param:value)` syntax for permission rules
- Improved auto mode evaluating subagent spawns before launch

## 2.1.176
- Session titles now generated in conversation language
- Added `footerLinksRegexes` setting for custom link badges
- Fixed availableModels not blocking model redirects via environment variables

## 2.1.175
- Added `enforceAvailableModels` managed setting constraining default model

## 2.1.174
- Added `wheelScrollAccelerationEnabled` setting for fullscreen mode
- Fixed `/model` picker hiding model families that Default resolves to

## 2.1.173
- Fixed Fable 5 model names with `[1m]` suffix not being normalized

## 2.1.172
- Sub-agents can now spawn up to 5 levels deep
- Bedrock reads AWS region from config files when env var unset
- Added search bar for browsing marketplace plugins
