# Raw source: Claude Code changelog v2.1.211–2.1.214 + Week 29 dev digest

**Fetched:** 2026-07-19
**URLs:**
- https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md (versions 2.1.211–2.1.214)
- https://code.claude.com/docs/en/whats-new/2026-w29
- https://code.claude.com/docs/en/whats-new (index, confirms Week 29 is the latest published digest as of fetch time)

## Week 29 digest (July 13–17, 2026), verbatim

> Pull live data into published artifacts through MCP connectors, and use Claude Code with a screen reader in the new screen reader mode.

Releases v2.1.207 → v2.1.212, 2 features, July 13–17.

### Artifacts call your MCP connectors (web)
A published artifact can now call MCP connectors each time someone views it, so a dashboard shows live data and can take actions on demand rather than a snapshot from the session that built it. Each call runs through the viewing account's own connections, and viewers approve access before the page's first connector call. This week also adds public sharing links, editor roles for shared editing on Team and Enterprise plans, and artifacts created from Claude Tag sessions.

Try it: `> Build a dashboard artifact of open pull requests that pulls the live list through my GitHub connector when the page loads.`

Docs: /docs/en/artifacts#pull-live-data-with-mcp-connectors

### Screen reader mode (CLI)
Screen reader mode replaces the visual terminal interface with plain, linear text: instead of boxes, spinners, and in-place redraws, Claude Code prints labeled lines that a screen reader such as VoiceOver or NVDA reads in order, so you can approve permissions and review output end to end. Turn it on per session with a flag, per shell with the `CLAUDE_AX_SCREEN_READER` environment variable, or everywhere with the `axScreenReader` setting.

Try it: `claude --ax-screen-reader`

Docs: /docs/en/accessibility#turn-on-screen-reader-mode

### Other wins (Week 29)
- `/fork` now copies your conversation into a new background session with its own row in `claude agents` while you keep working; the in-session forked subagent it used to launch is now `/subtask`
- Auto mode no longer needs the `CLAUDE_CODE_ENABLE_AUTO_MODE` opt-in on Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry; administrators can turn it off with `disableAutoMode`
- MCP tool calls that run longer than two minutes now move to the background automatically so the session stays usable; tune or disable the threshold with `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS`
- New `claude auto-mode reset` restores the default auto-mode configuration, and `--yes` skips the confirmation prompt
- New corporate launcher support: `CLAUDE_CODE_PROCESS_WRAPPER` or the `processWrapper` setting runs the processes Claude Code starts from its own binary, such as the background service and agent view sessions, through a required wrapper executable
- `vimInsertModeRemaps` setting maps two-key insert-mode sequences such as `jj` to Escape in vim mode
- `--forward-subagent-text` and `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` include subagent text and thinking blocks in stream-json output
- Session-wide caps stop runaway loops: WebSearch calls and subagent spawns each default to 200, tunable with `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` and `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`
- "Always allow" permission rules save at the repository root, so approvals granted in a git worktree persist across sessions and worktrees
- Amazon Bedrock, Google Cloud's Agent Platform, and Claude Platform on AWS now default to Claude Opus 4.8
- The collapsed tool summary line shows a live elapsed-time counter, so long-running tool calls visibly tick instead of looking stuck

## CHANGELOG.md, versions 2.1.211–2.1.214 (selected entries, security/practice-relevant subset)

### 2.1.214 (security-relevant highlights)
- Fixed single-segment `dir/**` allow rules like `Edit(src/**)` auto-approving writes to nested `dir/` directories anywhere in the tree instead of only `<cwd>/dir`
- Fixed a permission-check bypass affecting commands run in Windows PowerShell 5.1 sessions
- Fixed Bash permission checks to fail closed on file-descriptor redirect forms that bash parses differently than the permission analyzer
- Fixed Bash permission checks misjudging very long commands — commands over 10,000 characters now always prompt instead of running automatically
- Fixed Bash permission checks treating zsh variable subscripts and modifiers in `[[ ]]` comparisons as inert text — these commands now prompt for approval
- Fixed Bash permission checks to no longer auto-approve certain `help` and `man` commands that could run unsafe options, command substitutions, or backslash paths
- Fixed permission prompts on remote sessions that could proceed before the local confirmation dialog
- Added the EndConversation tool: Claude can end sessions with highly abusive users or jailbreak attempts, as on claude.ai since 2025
- Changed `file` commands using `-m`/`--magic-file` or `-f`/`--files-from` to require permission instead of being auto-allowed as read-only

### 2.1.213
No changelog entries between 2.1.212 and 2.1.214 (version bump only).

### 2.1.212
- `/fork` now copies your conversation into a new background session (its own row in `claude agents`) while you keep working; the in-session subagent it used to launch is now `/subtask`
- Added `claude auto-mode reset` to restore the default auto-mode configuration, with a confirmation prompt (pass `--yes` to skip)
- Added a session-wide limit on WebSearch tool calls (default 200, tunable via `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`)
- Added a per-session cap on subagent spawns (default 200, override with `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`)
- MCP tool calls running longer than 2 minutes now move to the background automatically
- Deprecated the Task tool's `mode` parameter (now ignored); subagents inherit the parent session's permission mode by default
- Fixed plan mode auto-running file-modifying Bash commands (e.g. `touch`, `rm`) without a permission prompt

### 2.1.211
- Added `--forward-subagent-text` flag and `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` environment variable to include subagent text and thinking in stream-json output
- Fixed permission previews relayed to chat channels not neutralizing bidirectional-override, zero-width, and look-alike quote characters
- Fixed auto mode overriding a PreToolUse hook's `ask` decision for unsandboxed Bash
- Changed "always allow" permission rules to save at the repository root

(Full text of all four versions, including non-security bugfixes, was reviewed but is omitted here as routine maintenance — see wiki summary for what was judged practice-relevant.)
