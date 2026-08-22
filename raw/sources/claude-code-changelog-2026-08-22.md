---
source: официальный CHANGELOG.md репозитория anthropics/claude-code
url: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
retrieved: 2026-08-22
covers: v2.1.236–2.1.240
---

# Changelog

## 2.1.240
- Bug fixes and reliability improvements

## 2.1.239
- Cost estimates now include "1.1× US-only-inference premium for data-residency workspaces"
- Added fullscreen renderer offer on Bedrock, Vertex, Foundry and other previously excluded setups
- Added `/claude-api upgrade` for migrating Python projects from anthropic 0.x to 1.x
- Cloud sessions: synced plugins now display as `name@synced` with enhanced management
- Alpine/musl builds: native image paste, clipboard, and audio-capture add-ons now functional
- Usage-limit messaging expanded to indicate session/weekly limit reset timing
- Fixed Bedrock streaming behind proxies that stripped response headers
- Fixed Claude Code hanging at startup behind HTTPS proxy with Bedrock SSO profile
- Fixed crashes when starting from deleted directories
- Fixed Edit/Write calls pausing ~5 seconds in JetBrains IDE terminals
- Fixed race condition where pressing Esc could allow next turn to finish prematurely
- Fixed WebFetch retaining expired content beyond intended 15-minute window
- Fixed cloud sessions resuming out of plan mode after idle worker restart
- Fixed MCP forms taller than terminal being clipped in fullscreen
- Fixed remote MCP servers staying failed after transient errors
- Fixed custom session titles disappearing after ~64 KB of conversation
- Fixed `/resume` picking sessions from different directories with similar names
- Fixed `/resume` showing sessions as recently changed when only touched/reopened
- Fixed `/resume` in all-projects mode referencing deleted directories
- Fixed dark-ansi theme rendering expanded tool results with same-color text
- Fixed fullscreen renderer prompt reappearing on every launch
- Fixed `.worktreeinclude` patterns starting with `**/` silently matching nothing
- Fixed agents/skills/commands with UTF-8 BOM being ignored
- Fixed `/insights` echoing literal `<message>` tags in responses
- Fixed marketplace `metadata.pluginRoot` having no effect
- Fixed mouse movement in browser terminals inserting text like "35;150;7M"
- Fixed custom theme overrides for status badge colors being ignored
- Fixed OpenTelemetry trace fragmentation with deferred tool executions
- Fixed vim mode: Escape now preserves text instead of clearing prompt
- Fixed `selection:copy` keybinding dropping extended text selections
- Fixed `/voice` startup tip appearing after voice was enabled
- Fixed shell-mode Tab completion dropping `./` from script paths
- Fixed fullscreen mode answering prompts on window focus
- Fixed slash-command panels covering latest messages in fullscreen
- Fixed `/workflows` detail dialog overflowing terminal
- Fixed Linux sandbox making `.git/config.worktree` unreadable
- Fixed hooks failing after session's working directory was deleted
- Fixed `claudeMdExcludes` not excluding symlinked `.claude/rules` files
- Fixed runaway session-title syncing to Remote Control
- Fixed sessions with `/`-prefixed titles being unaddressable
- Fixed text-editing shortcuts leaving broken `[Pasted text #N]` placeholders
- Fixed masked inputs leaking text via Ctrl+Y or prompt history
- Fixed Ctrl+Backspace deleting one character instead of word in search boxes
- Fixed request re-send before rejection was shown
- Improved compaction reminder regarding skill argument handling
- Long file paths on tool-use rows now truncate in middle for single-line display
- Remote sessions maintain keep-alives during long hook execution
- `/goal`: repeat check-ins now back off with increasing intervals
- `/goal`: resuming from picker now restores active goal
- `ListAgents`: sessions now know their own names for peer messaging
- `ListAgents`: now lists live teammates alongside subagents
- `keybindingFlavor: "readline"` now handles Bash word-boundary keys
- Persistent retry mode fails immediately on spend/credit exhaustion errors
- Claude in Chrome: `/clear` closes session's Chrome tab group
- Remote sessions: mobile-uploaded images now include saved file path
- Claude Code web: requests to non-API anthropic.com hosts use session proxy
- Remote Control: clearer messaging when Remote Control isn't account-enabled
- Windows: cross-session messaging now available across machines
- VSCode: "View usage" sits inline in usage-limit banner

## 2.1.238
- Added `keybindingFlavor` setting supporting "readline" mode for Bash-like key bindings
- Plugin marketplaces: `headersHelper` runs command for minting HTTP headers
- Catalog entry `headersHelper` runs during install/update with `[y/N]` confirmation
- Added `claude self-hosted-runner --defer-shutdown-max-min` for graceful shutdown
- Added proxy authorization command/file support for egress proxies
- Fixed unbounded memory growth in long sessions via subagent tool result release
- Fixed custom/project/plugin output styles drifting to default voice mid-session
- Fixed prompt suggestions behavior with usage limit near threshold
- Fixed worktree-isolation Bash refusals with misleading redirect suggestions
- Fixed self-hosted runners occasionally removed after single slow poll
- Fixed MCP elicitation dialogs with URLs >4,096 characters
- Fixed leftover `/tmp/claude-*-cwd` files from killed/timed-out commands
- Fixed held Backspace ignored on terminals with slow links
- Fixed text-wrapping in permission prompt diffs with multi-code-point characters
- Fixed killed suspended sessions leaving terminal in bracketed-paste mode
- Fixed stdio MCP servers receiving discover request before initialize
- Fixed proxy refusal reported as generic network error
- Fixed `/model` cache-miss warning appearing when cache expired
- Fixed per-task Stop from Remote Control doing nothing
- Fixed remote sessions exiting on invalid message role
- Fixed Remote Control inheriting session-scoped environment variables
- Fixed crashed Remote Control session staying unavailable
- Fixed Remote Control messages disappearing mid-turn
- Fixed Remote Control model picks not updating terminal display
- Fixed Remote Control disconnecting on brief network hiccups
- Fixed Remote Control reporting failed reconnect on sign-out
- Fixed `ListAgents`/`SendMessage` "Remote Control not connected" error
- Fixed `ListAgents` exposing idle worker in agent view
- Cross-session messaging: refused messages now report "refused"
- Cross-session messaging: dropped messages now notify sender
- Improved startup: bare `claude` starts sooner on macOS
- Improved Bash permission checking for zsh conditionals
- Improved Remote Control resilience: tolerates 403s for up to 3 minutes
- Updated bundled claude-api skill for Managed Agents Aug 19 release
- Changed Ctrl+L/Cmd+K in fullscreen to repaint only
- Changed `claude mcp list/get` to show disabled servers clearly
- MCP helpers now require folder trust dialog acceptance
- MCP helpers run without inherited credential environment variables

## 2.1.237
- Fixed prompt caching for sessions using LLM gateway or custom base URL
- Added built-in "Concise" output style: "Claude leads with results and skips preamble"

## 2.1.236
- Added `ANTHROPIC_DEFAULT_MODEL` environment variable for new session default
- Added `notify_when_idle` to cross-session `SendMessage` for one-shot notifications
- Sandbox: macOS wildcard read-deny rules now take precedence properly
- Fixed clipboard/housekeeping/background sessions breaking after directory deletion
- Fixed fullscreen renderer failing permanently after single failed start
- Fixed `/model` picker rendering taller than terminal window
- Fixed `SendMessage` rejecting malformed closing tags
- Fixed unhandled promise rejections on subprocess failures
- Fixed fullscreen sometimes not showing new message after resize
- Fixed blank band above prompt after clearing multi-line input
- Fixed managed-settings approval prompt sometimes not appearing
- Fixed terminal tab titles jumping in tmux iTerm integration
- Fixed unclear error when cloud environments list empty/malformed
- Fixed Fable first-time usage-credits prompt auto-selecting after 60 seconds
- Fixed spinner tips never appearing with repeated background error
- Fixed skills hot-reload raising error after directory deletion
- Fixed Clawd mascot rendering unevenly at some font sizes
- Fixed runaway session recaps: text capped at "400 characters, cut at word boundary"
- Improved startup performance via background session counter write
- Improved auto mode: Monitor allow rules set aside while active
- Improved auto mode on Bedrock/Vertex/Foundry: uses same defaults as Claude API
- Improved auto mode: git status check no longer fooled by configuration
- Changed `/model` picker to highlight only newest model's name
- `/goal`: idle sessions check in automatically after 30 minutes
- `/usage`: shows usage-credits spend row for Team/Enterprise members
- SIGTERM in print/SDK mode no longer records interrupted turn
- Pressing Enter on slash-command typo now reports instead of fuzzy-matching
- Remote Control marks session offline within seconds on exit
- `SendMessage` refuses further messages up front when rate limit exceeded
- Aligned session title chip with footer's right edge
- Right-aligned footer items share consistent margin
- VSCode: added screen reader support with live announcements
