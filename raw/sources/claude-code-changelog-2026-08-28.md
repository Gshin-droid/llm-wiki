---
source: официальный CHANGELOG.md репозитория anthropics/claude-code
url: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
retrieved: 2026-08-28
covers: v2.1.246–2.1.250 (2.1.249 в файле отсутствует)
---

# Changelog

## 2.1.250

- Bug fixes and reliability improvements

## 2.1.248

- Added `--restricted` (or `CLAUDE_CODE_RESTRICTED=1`): removes the built-in tools that run commands or code and `WebFetch` (unless named in `--tools`), keeps file tools inside the working directory, refuses `bypassPermissions`, and ignores user, project and local settings files
- Added `experimental.cacheTtl` (`"5m"` or `"1h"`) to agent frontmatter: a per-agent prompt cache TTL used when no subagent TTL setting is configured
- Added `claude self-hosted-runner --client-label <label>` (or `SELF_HOSTED_RUNNER_CLIENT_LABEL`) to override the label the runner registers with (default: hostname)
- Added server-managed settings diagnostics: a startup warning when the settings fail to load, and a `/doctor` and `/status` line explaining a load failure or why they weren't fetched (Bedrock/Vertex/third-party provider, custom `ANTHROPIC_BASE_URL`)
- Added a warning in `/web-setup` when the GitHub CLI token lacks the `workflow` scope, since pushes to very large repositories can be rejected without it
- Added `/usage-credits` for Enterprise organizations billed through AWS Marketplace, self-serve Enterprise, and Enterprise trials, so members can request a higher usage limit from their admin
- Added cross-session messaging (`SendMessage` / `ListAgents`) between sessions on the same machine on Bedrock, Vertex, and Foundry, and when telemetry is disabled
- Fixed a prompt-cache miss (and lost extended-thinking context) roughly once an hour in long sessions, caused by tool definitions being re-rendered after an OAuth token refresh
- Fixed the `ScheduleWakeup` tool definition changing between a session and its `--resume` when the account had entered usage overage, causing a full prompt-cache miss on the resumed session's first turn
- Fixed Claude Desktop and Cowork sessions disappearing after 30 days: the transcript cleanup now keeps desktop-written sessions while they are in the app (unless org policy manages retention); the new `desktopSessionCleanupPeriodDays` setting caps the exemption
- Fixed being sent to the login screen when another Claude Code process held the token refresh lock while the session token had expired; the request now fails with a retryable error instead
- Windows: Fixed the `claude agents` list not responding to the keyboard after detaching from a session, or when launched in a terminal tab left in win32-input-mode
- Fixed the recommended Console sign-in in `/login` failing with an OAuth error before showing a sign-in URL on machines where it can't be used (for example when `ANTHROPIC_API_KEY` or an API key helper is set); it now falls back to the API-key sign-in
- Fixed model names in `/model` and fast-mode switch notices to render as code, so suffixes like `[1m]` display literally instead of as a link
- Fixed `claude agents` skipping the workspace trust prompt when the `CI` environment variable is set
- Fixed `claude agents` crashing on launch when the PR-status cache held a malformed entry
- Fixed agent view resurrecting a weeks-old background session after the machine was off: such a session now shows as stopped at its real end, and opening it asks before resuming its saved conversation
- Fixed agent view sometimes opening an older conversation, and dropping the typed prompt, when starting a new session
- Fixed `claude agents`: opening a stopped session that you already resumed in another terminal no longer starts a second process on that conversation; the row now says it is open in a terminal
- Fixed `claude agents` and `claude rm` refusing to delete a session ("has commits that are not pushed anywhere") when its worktree branch was already merged into your checked-out default branch (e.g. local `main`) but not yet pushed
- Fixed background sessions waiting silently when a `PermissionRequest` or `PreToolUse` hook prints an invalid answer: the `claude agents` row now names the hook and the schema error
- Fixed hooks silently treating a stdout `{…}` object that isn't valid JSON as plain text; it's now reported as a hook error with the parse message
- Fixed `/mcp` listing a project `.mcp.json` entry that declares the claude.ai connector type under the trusted "claude.ai" heading; it now appears under its real scope
- Fixed MCP servers whose `headersHelper` supplies the `Authorization` header falling into OAuth discovery on a 401 instead of re-running the helper and retrying the call as documented
- Fixed `/login` to a Claude apps gateway hanging when the managed-settings security approval dialog was required
- Fixed gateway model discovery (`CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY`) never running when `apiKeyHelper` is the only credential
- Fixed `claude logs` leaving mouse tracking, bracketed paste and the alternate screen switched on in the terminal it was run from
- Fixed the trust dialog's list of repo permission rules showing a garbled character when a long rule was cut off in the middle of an emoji
- Fixed the permission mode indicator staying hidden behind the "Press Ctrl-C again to exit" hint when you press shift+tab right after ctrl+c
- Fixed `/ultrareview` and locally seeded cloud sessions uploading uncommitted edits to `prod.env`-style and `*.tfvars` files, or to editor swap, temp, and backup copies of credential files (e.g. `key.pem.tmp`, `id_rsa.swo`); they now stay on your machine
- Fixed Remote Control sessions occasionally never showing a permission prompt or the latest messages on the connected device after the CLI silently reconnected
- Fixed cloud sessions occasionally failing at startup when the container's session credentials were not yet readable
- Fixed `claude remote-control` rejecting its own flags (e.g. `--spawn`, `--name`) when a global flag or a wrapper-injected option precedes the subcommand
- Fixed startup warnings (e.g. "N MCP servers need authentication") rendering one column right of the rest of the transcript
- Fixed a backgrounded worktree session losing its checkout: the background session now holds the worktree's lock while it runs, so cleanup and `git worktree remove` leave it alone
- Fixed @-mentions of other sessions not matching names typed with non-Latin characters (for example Korean entered through an IME)
- Fixed an invalid `crossSessionInbound` value being silently ignored: it now warns and holds cross-session messages (user settings) or refuses them (managed settings) until fixed
- Fixed rate-limit, usage, and fast-mode messages telling you to run `/usage-credits` when that command isn't available for your organization (e.g. hidden with `DISABLE_EXTRA_USAGE_COMMAND`)
- [VSCode] Fixed a chat tab getting stuck on "No conversation found" when its session was never saved; it now starts a new conversation instead
- Improved the Workflow tool's prompt footprint: its description is now about 1k tokens instead of 5.7k, with the script-writing reference moved into a bundled `workflow-authoring` skill
- Improved the prompt-footer PR badge to check GitHub less often while the pull request is unchanged; a push or a `gh pr` command still refreshes it right away
- Improved managed settings: client-side timeout, MCP startup-mode, and stream-watchdog env vars no longer trigger the settings-approval prompt
- Improved `/ultrareview <PR#>` to check before launch that the GitHub account connected to your Claude account can access the repository, and to explain how to fix it, instead of failing after the cloud session starts
- Improved cross-session messaging: falls back to a private per-user `/tmp` directory when the default one can't be used, and the notice and `/status` name the directory to fix
- Changed shift+enter in the agent view dispatch input to insert a newline (matching the prompt); ctrl+enter now dispatches and attaches
- Changed `/loop`: self-paced dynamic mode and the no-prompt autonomous default are now always available, including on Bedrock/Vertex/Foundry
- Changed Anthropic telemetry export failures to log at debug level as `[Anthropic telemetry]` instead of `[3P telemetry] OTEL diag error`, so they are not mistaken for your OTel collector failing
- Changed cross-session messaging in Linux user namespaces: root-equivalent trust for unmapped owners is limited to canonical system directories
- Changed `SendMessage` from a subagent to another session: the result now notes that any reply is delivered to the parent session's conversation, not to the subagent

## 2.1.247

- Added the `SendFeedback` tool: when something goes wrong in a session, Claude can draft a feedback report for you to review and send from `/feedback` (turn off with the `feedbackDrafts` setting)
- Added `{id, text, cooldownSessions, priority}` entries, `tipsFile`, and `label` to `spinnerTipsOverride`, so organizations can rotate their own tips alongside the built-in ones
- Added a tip on Bash permission prompts pointing to auto mode, with a one-keystroke "Yes, and switch to auto mode" option
- Added `/claude-api cost-optimize` to profile an existing project's Claude API spend and work through cost levers (caching, token hygiene, batch, effort, model choice) one measured change at a time
- Updated the `/claude-api` skill with Admin API coverage (organization members, invites, workspaces, API keys, rate limit reports, workload identity federation, CMEK)
- Fixed fast arrow-key + Enter sequences acting on the row above the one you navigated to in history search, `/config`, `/mcp`, `/skills`, background tasks, and `/model`
- Fixed sub-agents dying on a first-call model 404: they now use the session's fallback model chain, and the error returned to the parent includes the error type, status, request id, and model
- Fixed a hook or background agent that printed megabytes of error output being able to overflow the conversation and wedge the session on "Prompt is too long"
- Fixed Ctrl keyboard shortcuts not firing under non-Latin (e.g. Cyrillic) keyboard layouts in kitty-protocol terminals
- Fixed text like `<35;150;7M` being inserted into the prompt when a mouse report arrived split across reads right after the escape prefix
- Fixed the Bash sandbox's after-command cleanup deleting a dotfile-managed `~/.claude/settings.json` symlink (nix/home-manager, stow) when it is repointed outside the sandbox's writable area
- Fixed `/terminal-setup` overwriting your entire Zed `keymap.json` instead of merging in its keybinding
- Fixed `/rename` silently confirming when the session registry could not be updated; it now says other sessions may still show the old name
- Fixed `/compact` and "Summarize from here" in sessions started with `--agent` summarizing under the default system prompt instead of the conversation's own
- Fixed a background session showing "opening…" forever in `claude agents` after its terminal host process died; the row now fails within seconds with the reason, and Enter restarts it
- Fixed unbounded memory growth when a hook's or background task's output file could not be written; the file now notes where output was lost
- Fixed `/install-github-app` over SSH: the copy shortcut now says how the sign-in URL was copied instead of always claiming success, and the URL appears immediately when no browser can open
- Fixed shell commands carried over from the foreground logging an internal error or showing a misleading `[exited with code -1]` line when they finish in background sessions
- Fixed a version-less marketplace plugin's live cache directory being deleted and recreated on a second-scope install, which could disrupt a running session using it
- Fixed Remote Control sessions started with `/remote-control` not reporting the working-tree diff to connected clients
- Fixed self-hosted runner sessions reporting `running` before Claude Code had started, which could trigger a premature "Claude is waiting for your input" notification from the Claude desktop app
- Fixed first-run setup exiting with "Unable to connect to Anthropic services" when managed settings configure Claude apps gateway sign-in and Anthropic endpoints are unreachable
- Fixed cloud sessions (Claude Code on the web, desktop and mobile apps) sometimes showing the previous permission mode when you switch modes right after sending a message
- Fixed cloud sessions going silent when the session's container restarts between turns while a background agent, shell, or monitor is still running — the resumed session now reports the lost work
- Improved plugin marketplace hardening: names containing control or invisible characters are rejected, and marketplace-supplied text in `/plugin` and `claude plugin` output is escape-safe
- Improved Bedrock, Vertex, and Foundry sessions (and any with telemetry disabled): Claude is now told when a configured MCP server failed to connect, instead of concluding its tools don't exist
- Changed Sonnet 5's default auto-compact window to its full 1M context, so sessions on the 1M window now auto-compact at about 967K tokens instead of about 934K
- Changed cross-session peer messages to collapse by default to a one-line `Message from @<sender>: <first line>` preview; Ctrl+O expands the full body
- Changed terminal hyperlinks in rendered markdown: link targets that point at a network or automounter path, contain a control character, or lead with an invisible character now render as plain text
- Changed the prompt-footer PR badge to skip its GitHub re-check on terminal refocus when the last check is under a minute old
- Changed analytics to stay off from startup, not only after login, when managed settings force gateway login or a custom OAuth deployment is configured
- Changed Claude apps gateway sign-in requests to identify Claude Code (a `surface=claude_code` device-authorization parameter and a `claude-code/<version>` User-Agent)
- Changed organization sign-in enforcement to exit at start when the administrator's managed settings cannot be read, even if host-supplied or per-user Windows registry settings exist

## 2.1.246

- Added a startup warning for Bash allow rules with a wildcard before the subcommand (e.g. `Bash(git * main)`), since they also match options inserted before the subcommand
- Added an Auto mode tab to `/permissions` for viewing and editing auto mode classifier rules
- Added the turn's completion time to the end-of-turn duration line, e.g. `✻ Sautéed for 23s · done 6:05 PM`
- Fixed fullscreen mode showing a blank transcript after resizing the terminal and jumping to the bottom until the next keypress
- Fixed a severe transcript slowdown when a diff contained a very long single line (e.g. a base64 string); such lines now render truncated with a marker
- Fixed erratic fullscreen scrolling when positioned at an earlier message, including jump-to-bottom getting stuck mid-transcript
- Fixed background sessions failing to open after 45 seconds when Claude Code's starting directory had been deleted, the machine had slept, or the host is slow to start processes
- Fixed background sessions failing to open with "Couldn't start the background service … EACCES" when another Claude Code process was re-installing the npm package at that moment
- Fixed markdown rendering being disabled for a whole message when its first 500 characters contained no markdown, and for `+`/`N)` lists and setext headings
- Fixed MCP tool calls interrupted by an incoming message in headless/remote sessions being reported to the model as "completed with no output" instead of an explicit interrupted error
- Fixed MCP tool arguments being sent as JSON strings when the parameter's schema is empty (`{}`), instead of their real type
- Fixed a command interrupted mid-run showing as "Ran 1 shell command" with no sign it was cut
- Fixed pressing ← or running `/background` during a dynamic workflow restarting its finished subagents; it now asks first and says how many subagents would restart
- Fixed opening a just-started session in `claude agents` while its worker was still booting (common on Windows) stopping it with "was stopped while the respawn was in flight"
- Fixed `claude agents` listing a backgrounded named session twice; backgrounding the same conversation again now numbers the new row (e.g. `my-session (2)`)
- Fixed the background retention sweep removing git worktrees under `.claude/worktrees/` that you created yourself when an old background-session record pointed at them
- Fixed auto mode tool calls being denied as "temporarily unavailable" on very large sessions by scaling the safety-check deadline with prompt size
- Fixed the plugin cache creating duplicate SHA-named directories for the same plugin
- Fixed plugin skills whose frontmatter `name` already includes the `<plugin>:` prefix showing it doubled in the slash menu (e.g. `/plugin:plugin:skill`)
- Fixed `claude plugin update` failing for an installed plugin given its bare name (only the fully-qualified name worked)
- Fixed plugin installation failing when `plugin.json` was saved with a UTF-8 byte-order mark (BOM)
- Fixed `/reload-plugins` reporting 0 skills for plugins that define skills under `skills/*/SKILL.md`
- Fixed hook error messages showing a literal `${CLAUDE_PLUGIN_ROOT}` instead of the resolved plugin path
- Fixed `/rename` replacing the theme's prompt border color (including a custom theme's `promptBorder`) with the default cyan; the border now keeps your theme's color unless you pick one with `/color`
- Fixed custom theme diff colors (`diffAdded`/`diffRemoved` and their dimmed variants) being ignored in diffs and the `/theme` preview
- Fixed a `keybindings.json` binding with an unknown action name silently deadening that key; it is now skipped so the default binding keeps working, and a warning is logged under `--debug`
- Fixed `/stats` activity heatmap showing each day's activity one cell off (Sunday's count under Monday) in timezones east of UTC
- Fixed `/fork` from an already-forked or backgrounded session starting the new session with an empty conversation
- Fixed prompts beginning with `/--` (e.g. Lean doc comments) being rejected as an unknown slash command instead of being sent to Claude
- Fixed the `@` file picker staying open after the typed text stopped matching a real path
- Fixed the status line's cost and duration resetting to zero after navigating to the agents view and back
- Fixed fullscreen mode moving keyboard focus onto the control under the pointer when you clicked the terminal window only to bring it back into focus
- Windows/macOS: Fixed headless sessions not cleaning up stale entries in `~/.claude/sessions` left by sessions that exited uncleanly
- Fixed the UI stopping with a render error on the first tool call when a third-party Anthropic-compatible endpoint (`ANTHROPIC_BASE_URL`) streams a `tool_use` block without an `id`
- Fixed the Write tool reporting "Out of memory" or freezing for a long time after overwriting a very large existing file, even though the file had been written
- Fixed `claude plugin install <name>` exiting silently (or hanging in a terminal) instead of reporting an error when `~/.claude/plugins/known_marketplaces.json` is empty or corrupted
- Fixed resumed sessions failing every turn with a 400 when the saved history contains tool blocks the Anthropic API does not accept (typically written by a third-party API proxy)
- Fixed `curl -fsSL https://claude.ai/install.sh | bash` failing with "Raw mode is not supported" for some Team/Enterprise users with server-managed settings
- Fixed sessions that ended in plan mode resuming outside plan mode in the VS Code extension, and in `claude -p --continue`/`--resume` with a permission prompt tool, when no permission mode was set
- Fixed the `Notification` hook not firing while the sandbox "Network request outside of sandbox" permission prompt is waiting
- Fixed Bash permission checks to always require approval for malformed commands with a dangling `&&` or `||` operator
- Fixed `--strict-mcp-config` sessions prompting to approve `.mcp.json` servers they would never load, which left background sessions waiting at startup
- Fixed telemetry and metrics requests to Anthropic carrying the API key configured for a third-party gateway (`ANTHROPIC_BASE_URL`); a credential is now only sent to its own host
- Fixed a visible API error on the first prompt after idle when `apiKeyHelper` returns short-lived JWTs: an expired cached token is now refreshed before sending, and 401/403 auth errors retry quietly
- Fixed memory growing with session length in the fullscreen and Ctrl+O transcript views: each rendered message row no longer retains a full copy of the transcript-wide tool lookups
- Fixed `/ultrareview` runs and cloud sessions launched at the same time from one repository (e.g. from several worktrees) sometimes starting with another launch's uncommitted changes
- Fixed the task progress count (e.g. `3/5`) shown for background cloud sessions such as `/autofix-pr` occasionally missing a task
- Fixed Remote Control sessions keeping their placeholder name in claude.ai and the Claude app until the second prompt; the auto-generated title now appears after the first prompt
- Fixed MCP tools marked `requiresUserInteraction` still offering "Yes, and don't ask again" in their permission prompt; the option wrote an allow rule the tool then ignored
- Fixed the self-hosted runner ending its live sessions or exiting when a work-poll response is malformed (e.g. an intercepting proxy's HTML page); it now retries the poll
- Improved `/cd`: the new directory's project settings, hooks, `.mcp.json` servers (behind the usual approval prompt), skills, and agents now take effect right after the move instead of on `--resume`
- Improved Bash tool latency on bash shells by replaying snapshot functions without a base64 subshell per function
- Improved subagent results: a subagent that stops at its `maxTurns` limit now returns its output marked as partial, with a hint to continue it via `SendMessage`, instead of appearing finished
- Improved non-interactive sessions (`-p`, SDK, cloud sessions) to automatically continue a response cut off mid-stream by a server error, connection loss, or stall instead of ending with an error
- Improved attribution of usage telemetry to your organization for workload identity federation sessions, events sent while `apiKeyHelper` runs at startup, and after a login token expired while idle
- Changed `/code-review` so Claude can also start it on its own on Bedrock, Vertex AI, and Foundry, through the Claude apps gateway, and when telemetry or non-essential traffic is disabled
- `/goal`: Changed idle sessions to start at most three check-ins on long-running background work per goal; your next message allows three more
- Changed `claude install` and `claude update` to defer a pending managed-settings consent prompt to the next interactive session instead of prompting mid-command
- Changed OpenTelemetry plugin events for plugins synced from claude.ai: `plugin_id_hash` now reflects the plugin's real marketplace, and `enabled_via` is `admin-install` for admin-installed plugins
- Fixed the command sandbox's filesystem configuration not respecting `--setting-sources`
