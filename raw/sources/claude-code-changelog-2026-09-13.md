---
source: официальный CHANGELOG.md репозитория anthropics/claude-code
url: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
retrieved: 2026-09-13
covers: v2.1.268–v2.1.270
---

# Changelog

## 2.1.270
- Fixed read-only git commands in Bash unexpectedly asking for permission after a session had been running for a while (regression in 2.1.269)

## 2.1.269
- Added `claude plugin eval`: run a plugin's eval suite against Claude Code and get scored, reproducible results (JSON + HTML report); see `claude plugin eval --help`
- Added `/output-style [name]` to list and switch output styles, including over Remote Control and in cloud and other headless sessions
- Added a diff of the files a Bash command changed to the Bash tool result when the Bash tool handles file edits (setting `bashEditDiffEnabled`)
- Added `OTEL_METRICS_INCLUDE_REPOSITORY` to tag OpenTelemetry metrics and events with `vcs.*` repository attributes; commit events get `vcs.ref.head.*` with `OTEL_LOG_TOOL_DETAILS`
- Added `CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS` to extend the LLM gateway `/v1/models` discovery timeout (default 3s)
- Added `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` (1–256) to raise the Workflow tool's per-run concurrent agent limit for inference-bound fan-outs
- Fixed the prompt cache being partially invalidated on the turn after a response was cut off at the output-token limit and automatically resumed
- Fixed the attribution reminder overriding a CLAUDE.md or memory rule against commit and pull request attribution; lines set by managed settings still apply
- Fixed `/goal` runs silently stalling after API errors, network drops, or token limits: the goal now retries with backoff, or pauses and says why, including until a usage limit resets
- Fixed sessions getting permanently stuck on "Prompt is too long" when auto-compaction had no complete earlier exchange to summarize (mostly Agent SDK sessions with very large prompts)
- Fixed prompt cache misses in cloud sessions by waiting briefly for server configuration before the first request
- Fixed `/btw` answers that contained made-up tool calls and output: the side question is now told not to write them, and any that appear are flagged as not executed
- Fixed plugin archives extracted for a session being readable by other local users, extracted files keeping world-writable bits from the archive, and stale files surviving re-extraction
- Fixed `Edit()` deny rules and the write-path check not applying to the file a Bash `tee` command writes; a `Bash(tee:*)` allow rule no longer covers destinations outside the working directories
- Fixed organization plugins enabled through managed settings not loading in headless sessions and on Claude Desktop (once Desktop bundles this CLI version); they load from the next session
- Fixed missing cursor in the permission-rule, auto-mode-rule, add-directory, session-rename and feedback-review text fields when the terminal's native cursor is enabled
- Fixed plugin LSP servers that reject `shutdown` params (e.g. rust-analyzer) being left running at session end; `exit` is now sent even if `shutdown` fails
- Fixed CMYK JPEG images failing to attach with "cannot decode"; they are now converted and resized like other JPEGs
- Fixed F1/F2/F4 not working in kitty-protocol terminals and Delete in st, Alt+arrows acting as Escape in rxvt-unicode, and Shift+punctuation typing the unshifted key in WezTerm (regression in 2.1.247)
- Changed `/ultrareview --post` to post the PR comment directly when the findings arrive and print the comment link, instead of starting a second cloud session to post it
- Changed skills synced from claude.ai in cloud sessions to be named `anthropic-skills:<name>`, matching Claude Desktop; the bare name still works when nothing else uses it
- [Claude Code on the web] Fixed `/model default` in a cloud session leaving every later message failing in organizations that restrict which models Claude Code can use
- [Claude Code on the web] Fixed one-off scheduled routines occasionally running a second time after a transient server error
- [Claude Code on the web] Fixed routine runs that use subagents sometimes being treated as finished too early, which could skip the retry after a real failure or start a duplicate run
- (Full version has additional VSCode/Claude Tag/Windows entries omitted here as non-material to this wiki's themes)

## 2.1.268
- Added to the Claude apps gateway: with `pricing:` set in `gateway.yaml`, signed-in Claude Code clients receive the same rates through managed settings, so `/cost` and telemetry match the spend meter
- Added a startup warning for gateways when `access_control.allow_cidrs` is empty, and a one-time warning the first time a request arrives from a public address
- Added the `gatewayInternalNetworks` managed setting, letting administrators allow `/login` to a Claude apps gateway on their organization's own public IPv4 block
- Added `claude self-hosted-runner --remove-session-state` (default off): delete each session's per-session directories under `<base-dir>/_sessions/` when the session ends
- Added `configDirectory` to the output of `claude auth status --json`
- Added `--json` to `claude plugin install`, `uninstall`, `update`, `enable` and `disable`, and `errorDetails`/`noteDetails` to each row of `claude plugin list --json`
- Added browser-tab icons for published artifacts, chosen by Claude to match each page
- Fixed every turn failing with HTTP 400 on third-party Anthropic-compatible endpoints (`ANTHROPIC_BASE_URL`) since 2.1.265: a regex in the Artifact tool's input schema that those endpoints reject
- Fixed WebFetch hanging indefinitely on a server that keeps the response open without finishing; a fetch now fails after 300 seconds. Set `CLAUDE_CODE_WEBFETCH_DEADLINE_MS` to override the deadline (0 turns it off)
- Fixed a respawned in-process teammate picking up tools or a system prompt from a same-named agent file in a folder you have not trusted
- Fixed sustained high CPU usage: a busy loop in long-running idle sessions no longer pins a CPU core, and rapid terminal focus reports during a session recap no longer keep the CPU high
- Fixed Claude sometimes replying "your message came through empty" after an MCP tool call
- Fixed deny and ask permission rules on symlinked directories (`/etc`, `/tmp`, `/var` on macOS; `/bin` on Linux) not applying when a path was given by its real location, and Bash commands ignoring deny rules written on a symlinked path spelling
- Fixed a case where a Read or Edit deny rule did not apply when an `env -C`, `eval` or similar command the permission checker cannot analyze was on the same line
- Fixed plugin and marketplace errors showing a token or password from a git source URL
- Fixed `/mcp` and `/plugin` server details, `claude mcp list`/`get`, and MCP login errors showing secrets resolved from `${VAR}` placeholders in MCP configs
- Fixed prompt caching and extended thinking breaking mid-session for SDK sessions using `excludeDynamicSections`: the first message is no longer re-rendered each request
- Fixed a running session silently switching to the organization's default model when another Claude Code process refreshed a stale model-access entry
- Fixed workload identity federation via a profile (as claude-code-action configures it): processes sharing the profile could fail mid-run with `401 … jti reused`
- Changed the task-tracking tools (TaskCreate/Get/Update/List, TodoWrite) to be offered only on Claude 3.x, Opus 4.0–4.7, Sonnet 4.0–4.6, Haiku 4.5; set `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` elsewhere
- Changed plain `WebFetch` deny and ask rules to no longer apply to Artifact tool reads and updates; use an `Artifact` rule (or `WebFetch(domain:claude.ai)`) to block or gate them
- [Code Review] Added a note under the still-open findings list in follow-up reviews: resolving a finding's thread, not just replying to it, stops later reviews from counting it as open
- [Code Review] Fixed reviews sometimes ending as incomplete when one of the agents verifying a finding failed midway; the review now replaces that agent and reaches a verdict
- (Full version has additional VSCode/Claude Tag/Windows entries omitted here as non-material to this wiki's themes)
