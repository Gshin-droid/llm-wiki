---
source: официальный CHANGELOG.md репозитория anthropics/claude-code
url: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
retrieved: 2026-10-07
covers: v2.1.289-v2.1.292 (даты по code.claude.com/docs/en/changelog — 3, 5, 6, 6 октября 2026 соответственно)
---

# Changelog (выборка, версии 2.1.289-2.1.292)

Четыре новые версии с прошлого снапшота (10-04, версия 2.1.288) — окно 03-06.10.2026.

## Version 2.1.292 (2026-10-06)

Added:
- Added `--marketplace <source>` to `claude plugin install` for simplified plugin sourcing
- Added an `effort` parameter to the Agent tool enabling customizable sub-agent execution levels
- Added `CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS` environment variable for configurable backoff timing
- Added `prompt.autocomplete` event hook for mods
- Added prompt caching to `$.model.complete` for mods
- Added workflow agents to `agent.spawn` mod hook

Security / permission fixes:
- Fixed subagent definitions with `permissionMode: auto` entering auto mode when auto mode is unavailable
- Fixed sandboxed commands being able to read the staged file copies of `/ultrareview` uploads under `~/.claude/seed-admin`
- Fixed a managed sandbox read-deny path (and user ones beside it) that appears or re-points mid-session not dropping project grants inside it or ending credential injection from files it covers
- Fixed a notebook or PDF read on macOS and Windows being able to return a file outside what was approved, through a link swapped in mid-read
- Fixed a tampered on-disk cache of server-managed settings being able to switch off or unseat the built-in policy plugin while the settings fetch failed
- Fixed `rm -rf` on the 8.3 short name or another alternate Windows spelling of the home folder or a drive not being treated as removing it
- Security: Fixed PreToolUse hook approvals and auto mode bypassing the permission prompt for file reads from network (UNC) paths
- Fixed a skill's or slash command's `allowed-tools` rule coming back in a later turn when you leave auto mode or plan mode partway through that turn
- Fixed multiple security issues with file reads through symlinks and permission bypasses (summary bullet covering several of the above)
- Fixed PreToolUse hook approvals and auto mode bypassing permission prompts for network (UNC) paths

Other fixes:
- Fixed an MCP tool with a name longer than 128 characters making every request fail
- Fixed `claude plugin` commands running before managed settings loaded on first run
- Fixed scheduled tasks and background commands not being waited for in one-shot runs
- Fixed plan mode not being restored when resuming sessions
- Fixed `/loop` and saved scheduled tasks issues after `/resume`, `/branch`, or `/clear`
- Fixed background session's `/loop` stopping when process restarted
- Fixed Grep and Glob reporting no matches when files couldn't be read
- Fixed Read tool returning only first entry with PDF page lists
- Fixed @-mentioned text files over 256KB being silently left out
- Fixed usage limit alert repeating per background agent
- Fixed Remote Control viewers seeing an empty subagent pane for background subagents
- Fixed various UI and interaction bugs (vim mode, fullscreen mode, pasted text, etc.)
- Fixed plugin hooks, cloud sessions, Slack integration, and Code Review issues
- Improved startup, rendering speed, hook output handling, sandbox auto-allow
- Changed MCP protocol version negotiation and artifact publishing behavior

## Version 2.1.291 (2026-10-06)

- Fixed a regression in 2.1.290 where cloud sessions could drop answers to permission prompts
- Fixed a regression in 2.1.288 where the last messages of a session could be lost when quitting

## Version 2.1.290 (2026-10-05)

- Added `serverToolUses` to the result of a mod's `turn.step` hook (advisor tracking)
- Added `agentId` to the `tool.check` event of plugin hooks (subagent permission differentiation)
- Added `ceiling` to the question and verdict (organization-mandated approval levels)
- Added `ThemeKey` and `Color` types to plugin hooks typings
- Added Deny button to Claude apps gateway sign-in approval page
- Added `claude attach <name>` and `claude logs <name>` with partial session name matching
- Added `/claude-api managed-agents-onboard` commands for setup
- Fixed requests failing behind proxies rejecting beta headers
- Fixed long sessions with hundreds of images getting stuck
- Fixed turn ending prematurely when API's output content filter stopped reply
- Fixed resumed subagents losing thinking and prompt cache
- Fixed WebFetch silently dropping text past 100,000 characters
- Fixed mid-response API timeouts failing the turn (extended thinking session recovery)
- Fixed long conversations failing with "Prompt is too long" (proper auto-compaction)
- Multiple fixes for Remote Control, permissions, sandboxing, and file handling

## Version 2.1.289 (2026-10-03)

- Fixed a deny or ask rule on a nested part of a compound shell command not holding over user-installed mod approvals on managed machines
- Fixed the terminal freezing on short code blocks with many unclosed `<script>` tags
- Fixed `Read` deny rules not applying to files @-mentioned, changed, or selected in the IDE through a symlink
- Reverted a 2.1.288 change to `claude auth status` that may have made sign-outs more frequent
- Fixed plugin loading and display issues
- Fixed user-installed plugin rewriting organization MCP server descriptions
- Added `agent.spawn` for teammates and idle/waiting states in `$.agent.list()`
- Fixed sessions ending with interface errors from plugin failures
- Improved plugin marketplace errors and validation
- Improved how quickly large files open in a plugin code pane
