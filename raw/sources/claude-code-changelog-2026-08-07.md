---
source: официальный CHANGELOG.md репозитория anthropics/claude-code
url: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
retrieved: 2026-08-07
covers: v2.1.222–2.1.223
---

## 2.1.223

- Added owner wildcard entries (`"owner/*"`) to the `strictKnownMarketplaces` and `blockedMarketplaces` settings
- Added a warning when workflow agents, forked skills, slash commands, or resumed background agents' requested subagent model is restricted by policy
- Added a `/teleport` hint in cloud sessions showing how to continue locally
- Fixed a Bash permission bypass where a crafted command could hide parts of itself from the permission analyzer
- Fixed permission prompts so commands padded with tabs or invisible Unicode can no longer hide part of the command from review
- Fixed workflow scripts being able to use dynamic `import()` to run code outside the workflow sandbox
- Fixed a permission gap where an agent definition's `bypassPermissions` mode ignored the org bypass-permissions disable policy
- Fixed resuming a session after a mid-session `/cd` coming back empty
- Fixed gateway model discovery hiding Claude models registered under provider-prefixed IDs
- Fixed `modelOverrides` keys that aren't Anthropic model IDs being treated as the session's canonical model ID
- Fixed managed settings: server-delivered settings no longer disable the env block
- Fixed sandboxed commands failing to start on Linux when `sandbox.filesystem.denyWrite` covers the working directory
- Fixed forked background agents getting stuck "already resuming" for the rest of the session
- Fixed a resumed session failing every turn when its history held a malformed diagnostics attachment
- Fixed a rare hang when parsing unusual `git push` output
- Changed `CLAUDE_CODE_DISABLE_1M_CONTEXT` to hold every Claude model with a native 1M window to 200K
- Changed auto-compact to keep sessions on unrecognized model IDs within the assumed context window
- Changed `/review` to be an alias of `/code-review`, which reviews the current diff or a PR
- Changed `/code-review` with no effort level to reuse the level you typed last

## 2.1.222

- Fixed worktree-isolated sessions and their subagents being able to run destructive git commands
- Fixed PreToolUse auto-allow hooks bypassing tool restrictions in background agent tasks
- Fixed `/usage-credits` on Team and Enterprise showing "you've already sent a usage credit request"
- Fixed the startup connectivity check hanging and then failing behind an HTTPS proxy
- Fixed "Connection closed mid-response" errors being reported on responses that had actually completed
- Fixed `/usage` overattributing usage to MCP servers
- Fixed sessions not linking to pull requests created after the branch was pushed
- Fixed org-restricted `model: opus`-style subagent and teammate family aliases dropping to the parent model
- Fixed stream idle timeout firing on custom `ANTHROPIC_BASE_URL` gateways despite server keep-alive pings
- Fixed claude.ai connectors being falsely marked as needing authorization when the session token is invalid
- Fixed tool errors not being displayed for tools no longer available locally
- Fixed `SendMessage` rejecting a long summary — it now truncates instead
- Fixed the spinner's effort label in a subagent's transcript view showing the session's effort level
- Fixed rare crashes when a file watcher hit a filesystem error
- Fixed screen readers re-reading the whole input line on every backspace in `--ax-screen-reader` mode
- Fixed host model-selection keys not taking precedence over a stale on-disk `managed-settings.json`
- Improved auto mode safety: messages sent to other agent sessions via `SendMessage` are now evaluated
- Improved the refusal when Claude tries to invoke a skill with `disable-model-invocation`
- Improved the `/diff` view, the Remote Control workspace diff, and file-edit diffs
- Changed Remote Control auto-start so repo-local settings can no longer turn it on
- Removed ultraplan feature

---

Верификация: полный текст запрошен и получен напрямую через WebFetch на `raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md` (verbatim), одним запросом, покрывающим последние 15+ версий включительно 2.1.212. Расхождений между запрошенным и предыдущим снапшотом (2026-08-04, покрывавшим до 2.1.221) не найдено — версии 2.1.222 и 2.1.223 полностью новые.
