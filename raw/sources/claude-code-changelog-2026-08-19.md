---
source: официальный CHANGELOG.md репозитория anthropics/claude-code
url: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
retrieved: 2026-08-19
covers: v2.1.234–2.1.235
---

# Changelog

## 2.1.235

**Spellcheck & UI Fixes:**
- Added optional `spellcheck` setting that "underlines misspelled words in the prompt input as you type, using your installed `aspell`, `hunspell`, or `ispell`"
- Fixed prompt input highlights appearing shifted in multi-line prompts
- Fixed slash commands showing HTML entities instead of actual characters

**Performance & Stability:**
- Improved memory and CPU usage during cloud sessions by eliminating redundant event stream re-scanning
- Fixed whole-prompt-cache invalidation when language servers disconnected mid-session
- Fixed nested markdown list misalignment at depth 3+

**Permission & Dialog Improvements:**
- Fixed Shift+Tab in permission prompts approving edits unintentionally
- Improved permission dialogs to match display text with actual grant coverage
- Fixed Agent tool advertising unavailable defaults with clearer error messages

**Session Management:**
- Fixed expanded task lists always starting collapsed when resuming sessions
- Fixed `SendMessage` silently dropping oversized cross-session messages

**Terminal & Display:**
- Improved embedded `grep` to fail fast on pathological patterns
- Fixed context-limit errors when auto-compact is disabled
- Vim mode now preserves cursor position when toggling transcript view
- Fixed dialog navigation with rapid arrow keys and Enter

**Other Fixes:**
- Fixed Remote Control applying enterprise-gateway availability checks
- [VSCode] Fixed focus jumping between Claude tabs on window restoration

## 2.1.234

**Session & Configuration:**
- Added `CLAUDE_CODE_PROJECT_DIR_NAME` environment variable for custom per-project transcript directories
- Added `selection:clear` keybinding action for clearing in-app text selections
- Added GitLab merge request badge to footer and statusline showing MR status

**Security Enhancements:**
- Claude now uses your account email only for identification, not third-party services
- Implemented Windows NT-namespace path rejection to harden against NTLM credential leaks
- Fixed session-scoped permission answers being dropped in background subagent prompts

**Auto Mode & Features:**
- Claude Code continues automatically when usage limits reset; configure in `/config`
- Fixed auto mode denying sandboxed commands after conversation compaction

**API & Streaming:**
- Fixed crash when API responses contained thinking blocks missing required fields
- Fixed markdown rendering becoming extremely slow for unusual Unicode sequences
- Fixed `SendMessage` rejecting recipients from `ListAgents` near character limits

**Repository & Git:**
- Fixed repository detection misreading git remote hosts with unusual userinfo
- Fixed MCP diagnostics printing resolved secrets in conflict warnings

**Marketplace & Plugins:**
- Fixed `strictKnownMarketplaces` accepting SCP-style git sources with mismatched hosts

**Terminal & Display:**
- Fixed modal text losing characters when copied in fullscreen
- Fixed horizontal rules running into following lines in markdown
- Fixed consecutive shell commands splitting into multiple rows with task updates

**Permission & Dialogs:**
- Fixed dialogs dismissed when `!` shell commands finished mid-prompt
- Fixed queued `!` commands being sent as plain text after editing
- Fixed queued messages reappearing in prompt history
- Fixed `/tui` restart losing permission mode and tool restrictions

**Remote Control:**
- Fixed files sent during Remote Control sessions failing to upload
- Fixed stale-token reminder appearing in auto-resumed turns after `/login`
- Fixed permission previews relaying outside admitted channel servers
- Fixed credential masking hiding commands and paths from approvers
- Improved session awareness when switching accounts or organizations

**Cross-Session Messaging:**
- Fixed `SendMessage` silently dropping when cross-session messaging disabled
- Improved messaging to show sender and body inline instead of collapsed

**Transcript & UI:**
- Improved auto-generated session titles to be concise names rather than sentences
- Your own prompts now render markdown with highlighted code and lists

**Other Improvements:**
- Reduced context cost of built-in `claude-api` skill from ~200k+ to ~25k tokens
- `/permissions` now opens mid-turn with changes applying to remaining work
- `/add-dir` works while Claude is operating
- `/goal` clears with notice on unrecoverable errors
- `claude setup-token` rejects unexpected arguments
- Vim mode preserves NORMAL mode and cursor across panel toggling
- Removed redundant "Allowed by auto mode classifier" lines
- Dimmed elapsed-time counter on tool headers
