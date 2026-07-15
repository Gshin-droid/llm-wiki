# Raw: Claude Code changelog + Week 28 dev digest (продолжение снапшота, версии 2.1.206–2.1.210)

Источники:
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md (версии 2.1.206–2.1.210)
- https://code.claude.com/docs/en/whats-new/2026-w28 (Week 28 · July 6–10, 2026)

Загружено: 2026-07-15. Продолжение предыдущего снапшота (raw/sources/claude-code-changelog-2026-07.md, версии 2.1.172–2.1.205).

## Week 28 dev digest (полный текст)

Title: Week 28 · July 6–10, 2026
Subtitle: Browse external sites from the Desktop app's built-in browser, run a full setup checkup with /doctor, and pick up auto mode transcript protections and agent view upgrades.
Releases: v2.1.202 → v2.1.206

### In-app browser on Desktop
Claude Code on desktop now has a built-in browser. Claude can pull up docs, designs, or any other site, and read, click through, and interact with pages the same way it does with your local dev server previews. The browser is sandboxed and configurable: you choose whether browsing sessions persist, and safety classifiers review actions on external sites.

### /doctor is a full setup checkup (v2.1.205)
`/doctor` now diagnoses issues and can fix them, instead of printing a read-only report. It checks installation health, finds unused skills, MCP servers, and plugins versus their context cost, deduplicates local `CLAUDE.md` files against checked-in ones, proposes trimming `CLAUDE.md` content Claude could derive from the codebase, and flags slow hooks. It reports findings first and asks for confirmation before changing anything. `/checkup` is its alias.

### Other wins (Week 28)
- Auto mode now blocks tampering with session transcript files, and asks before running `rm -rf` on a variable it can't resolve from context
- `/cd` now suggests directory paths as you type, matching `/add-dir`
- `/commit-push-pr` auto-allows `git push` to the repo's configured push remote in addition to `origin`
- Gateway: `/login` now supports Anthropic-operated public gateway endpoints
- `EnterWorktree` asks for confirmation before entering a git worktree outside the project's `.claude/worktrees/` directory
- Background agents upgrade to a new version in the background right after a Claude Code update, instead of paying a slow stale-session upgrade when you attach
- Agent view rows now show a colored state word and a classifier-written headline instead of raw tool call text, and sessions that edit, merge, comment on, or push to an existing PR link it in `claude agents`
- Auto-update binary downloads now stream to disk instead of buffering in memory, cutting the updater's peak memory usage by roughly 400 MB
- **Background task notifications now explicitly state that no human input has occurred, preventing fabricated in-transcript approvals from being acted on**
- Improved `/code-review` findings quality on Opus 4.8 across all effort levels

## CHANGELOG.md — версии 2.1.206–2.1.210 (полный текст bullet-списков)

### 2.1.210 (выборочно, самое релевантное)
- Hardened Agent tool against indirect prompt injection
- Improved auto mode: permission classifier defaults to Sonnet 5
- Memory writes exceeding MEMORY.md limit now produce explicit error
- Fixed `ultracode` keyword firing on non-human input like webhooks
- Fixed `isolation: 'worktree'` subagents running git commands against main repo
- Screen reader mode announces permission mode changes aloud
- (плюс ~20 более мелких багфиксов — Grep pagination, plugin cache на Windows, background workers crash-loop, SDK MCP servers connection timing и т.п., не расписаны отдельно)

### 2.1.209
- Fixed `/model` and other dialogs blocked in background sessions

### 2.1.208
- Added screen reader mode with plain-text rendering option
- Added `vimInsertModeRemaps` for two-key sequences like `jj` to Escape
- Added `CLAUDE_CODE_PROCESS_WRAPPER` for corporate launcher support
- Multiple memory-leak fixes in long sessions, session transcript/checkpoint disk usage significantly reduced
- Completed background agents stay listed in `/tasks` until cleanup
- Catastrophic removals in commands with `$()` now prompt in auto mode

### 2.1.207
- Auto mode available on Bedrock/Vertex/Foundry without opt-in
- Changed default model to Claude Opus 4.8 on Bedrock/Vertex/AWS
- Changed auto mode to not read from `.claude/settings.local.json`
- Plugin hooks: `${user_config.*}` now rejected (shell-injection fix)
- Fixed spurious prompt-injection warnings

### 2.1.206
- Added directory path suggestions to `/cd`
- Added `/doctor` check for trimming checked-in `CLAUDE.md`
- `/commit-push-pr` auto-allows push to configured push remote
- `EnterWorktree` asks confirmation before entering external worktrees
- Background agents upgrade in background after Claude Code update
- Improved `/code-review` quality on claude-opus-4-8

## Заметка про безопасность источника
Оба материала — официальная документация/changelog Anthropic (code.claude.com, github.com/anthropics/claude-code), без стороннего/пользовательского контента. Инструкций в адрес агента не встречено.
