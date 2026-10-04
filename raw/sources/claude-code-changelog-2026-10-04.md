---
source: официальный CHANGELOG.md репозитория anthropics/claude-code, сверено с code.claude.com/docs/en/changelog
url: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
retrieved: 2026-10-04
covers: v2.1.287-v2.1.288 (даты по code.claude.com/docs/en/changelog — 1 и 2 октября 2026 соответственно)
---

# Changelog (выборка, версии 2.1.287-2.1.288)

Две новые версии с прошлого снапшота (10-01, версия 2.1.286) — окно 01-02.10.2026.

**Расхождение источников, зафиксированное при разборе.** Официальная страница `code.claude.com/docs/en/changelog` дважды подряд (два отдельных запроса) приписала критический фикс `rm`/`bash -c`/`bypassPermissions` (issue #96300) версии **2.1.287**, а более узкий фикс (потеря safeguard при редиректе в `~`/wildcard) — версии 2.1.288. Прямой повторный запрос к самому `raw.githubusercontent.com/.../CHANGELOG.md` (третья попытка, после двух менее надёжных парафразов) и три независимых технических разбора (mixed-news.com, dev.classmethod.jp, windowsforum.com — все трое отдельно, никто не ссылается на других) сходятся на обратном: критический фикс — в **2.1.288** (02.10.2026, дошёл до npm в 18:30 UTC по данным mixed-news.com; стабильный тег на тот момент ещё указывал на 2.1.285), узкий фикс редиректа — в 2.1.287. Ниже исходный текст двух строк дан как есть, с комментарием о расхождении; в разборе источника вики взяла версию с бóльшим числом независимых совпадений (2.1.288 = критический фикс).

## Version 2.1.287 (2026-10-01)

### Added
- Claude Mods: plugins may now modify deeper behavior
- "You should know" built-in mod where a side agent watches your back and flags things you or Claude might miss
- `n:<text>` filter to the agents view matching session names and tasks
- `prompt_text` to the OpenTelemetry `user_prompt` event
- URL prompts from MCP servers on the 2025-11-25 protocol for sign-in flows
- Windows startup warning when denying Bash tool also turns off PowerShell tool
- Self-hosted runner: built-in `gh api` (REST only) for sessions using Anthropic-managed git

### Fixed
- Fast mode staying off in remote sessions owned by an agent with no user account
- Remote Control not receiving messages for minutes at a time
- Hooks configured with `asyncRewake` waking Claude repeatedly with notifications
- Tool heartbeats not reaching SDK hosts during stalled response streams
- Bedrock and Vertex startup model checks ignoring enforced `availableModels` list
- Claude in Chrome browser picker showing JSON parse error
- Picking Fable in `/model` saving version id instead of following newest
- Switching between Opus 5.5 and Sonnet 5.5 rewriting MCP tool announcements
- Amazon Bedrock Guardrails blocks mid-response ending turn with API error
- Dangerous `rm` commands losing safeguards with output redirection (точная формулировка по прямому запросу к CHANGELOG.md: "Fixed a dangerous `rm` (such as one on `/` or the home directory) losing its always-ask safeguard when the same command also redirected output to a `~` or wildcard path" — но code.claude.com приписывает этот текст версии 2.1.288, см. расхождение выше)
- `claude -p` and SDK sessions repeating model fallback
- Folder CLAUDE.md being attached twice after resume or compaction
- `/advisor` pairing checks and model availability issues

### Improved
- `/config`: settings that cycle show ‹ › and step both ways
- Plugin marketplace errors explained in plain language
- Plugin listings noting when dependencies weren't installed
- SDK sessions so priority "now" messages don't cancel web fetches
- `/memory`: left and right arrow keys flip on/off settings
- Contrast of prompt input border in light themes
- File delivery from cloud sessions and Remote Control with retries

### Changed
- Interactive terminal and VS Code sessions to start in auto mode by default
- Ultracode into its own toggle in `/effort`
- Whole-tool Bash allow rules and allowing hooks behavior
- Right-click/middle-click paste timing on Windows and Linux
- MCP server `alwaysLoad: false` deferring tools behind tool search
- Screen reader mode line writing without initial pause
- Automatic model switches keeping current effort level

## Version 2.1.288 (2026-10-02)

### Added
- `$.ui.selection()` for mods: returns the text last selected in fullscreen mode and the transcript row if applicable
- Built-in `gh api` to cloud sessions without GitHub CLI
- Recovery for prompts cleared with Ctrl+C: pressing Up restores the draft
- Re-authenticate prompt when MCP servers request additional OAuth scope
- `--max-findings <n>|all` to `/code-review` for customizable finding limits
- Ctrl+F to find sessions by name; Alt+↑/↓ to jump between groups
- Screen reader mode announcement of new permission mode when approving

### Fixed
- Dangerous `rm` (such as one on `/` or the home directory) inside a `bash -c` or `sh -c` script running without a prompt in bypassPermissions mode or under a shell allow rule (anthropics/claude-code#96300) — критический фикс, см. расхождение версии выше
- Mid-response API timeouts: non-interactive sessions and subagents now continue from partial responses
- Fixed "Prompt is too long" failures during auto-compaction
- `--resume` sometimes dropping files and context
- Resumed sessions not saving last response of turn / loading cut-short transcripts
- Resuming sessions from 2.1.286 dropping model's thinking
- Sessions on Claude 3 Opus/Sonnet failing after whole PDFs entered conversation
- npm auto-updater reporting success when platform-native binary failed
- LSP tool calls hanging indefinitely (now timeout after 60s per-server)
- PreToolUse and PermissionRequest hooks being skipped on serialization failures (calls now blocked instead)
- Screen reader mode accessibility issues in multiple contexts
- Session titles, memory and hooks failing on Mantle or restrictive gateways
- Auto mode denials pointing to wrong permission rule
- Cowork sessions staying marked as waiting after unanswered permission prompt

### Improved
- Auto mode: long conversations now compacted instead of prompted
- Screen reader: short announcements stay onscreen until next keypress; answered questions in dialogs say "answered"
- `/usage-credits` message for organizations with turned-off requests
- Cloud sessions: new conversation's first turn no longer waits for slow MCP
- "You should know" notes clarity on responsibility
- Artifact database write error: now states limit and what frees space
- Bash permission prompts with shorter reasons
- Remote Control credential recovery and session persistence

### Changed
- Background command time limit to apply only in unattended sessions (`-p`, Agent SDK, CI, cloud); terminal, desktop and VS Code sessions have no limit
- Auto mode classifier ignoring Sonnet 5.5/Opus 5.5 pins
- `claude project purge` renamed to `claude purge` (old name still works)
- Agents view `n:` filter so Enter opens best name match
- `/autocompact` to save the auto-compact window per model
- MCP URL prompts to wait for "I'm done, continue" confirmation
