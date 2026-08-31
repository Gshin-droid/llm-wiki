---
source: официальный CHANGELOG.md репозитория anthropics/claude-code
url: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
retrieved: 2026-08-31
covers: v2.1.251
---

# Changelog

## 2.1.251

- Added `PreModelSwitch` and `PostModelSwitch` hook events (block, confirm, or annotate a model switch); `SessionStart` resume hooks now receive session staleness and the estimated re-cache cost
- Added live streaming of a foreground subagent's tool calls and results to Remote Control clients (background subagents, the default, still show status only)
- Added a Spend limit bar to `/usage` and a `rate_limits.spend_limit` status line field for developers behind a Claude apps gateway with spend limits
- Added a per-session prompt-cache line to `/cost` (hit ratio, misses, tokens re-cached, warm/cold) and a matching `prompt_cache` object for status line scripts
- Added `attach`, `logs`, `stop`, `respawn`, and `rm` to `claude --help`; the `--resume` message for a running background session now names the exact `claude attach <id>` command
- Fixed file tools (Read, Write, Edit) following a symlink swapped inside the working directory after the permission check, which could read or write outside the approved location
- Fixed plugin commands declared in a marketplace entry being able to point outside the plugin directory; such paths are now rejected with a path-traversal error
- Fixed project settings being able to enable detailed beta tracing or raw API body logging, and a lower-scope beta tracing endpoint bypassing an OTLP collector pinned by managed settings or a host app
- Fixed the Workflow tool reading (and quoting in errors) a `scriptPath` outside what the session may read before the permission check ran
- Fixed Grep and Glob not applying `Read(...)` deny rules to files reached through a symlinked search path
- Fixed conversations getting stuck on "text content blocks must be non-empty" errors after a turn where the model produced only thinking
- Fixed the first launch on a fresh install starting in default mode instead of auto mode for accounts whose startup default is auto mode
- Fixed Opus 5 requests failing with "effort … is not supported when thinking is disabled" when effort was xhigh/max and thinking was turned off; effort is now sent as `high` in that case
- Fixed replying to a message Claude Desktop delivered from another session: `SendMessage` to that session id now delivers through Claude Desktop instead of failing with "not reachable"
- Fixed TUI lag with many parallel subagents: per-second progress ticks now replace their predecessor instead of piling up in the transcript
- Fixed agent teams: a teammate's final answer not reaching the team lead — it now arrives in the idle notification instead of a content-free "available" notice
- Fixed background subagents being unable to reply to a message from an unnamed sibling or parent agent (`from` was the agent type, which is not an address)
- Fixed managed-settings `disableAutoMode` arriving mid-session not moving an already-running auto-mode session back to default mode
- (full bug-fix/improvement/changed list: ~60 entries total — terminal/UI/plugin/MCP/Windows/VSCode items omitted here, see upstream CHANGELOG.md for the complete text)
