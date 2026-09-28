---
source: официальный CHANGELOG.md репозитория anthropics/claude-code
url: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
retrieved: 2026-09-28
covers: v2.1.283 (дата релиза по code.claude.com/docs/en/changelog — 2026-09-25; в самом CHANGELOG.md версия не датирована отдельно)
---

# Changelog (выборка, версия 2.1.283)

Единственная новая версия с прошлого снапшота (09-25, диапазон 2.1.274–2.1.282). Полный список пунктов версии — ниже, без урезания (версия компактнее прошлых диапазонов).

## Added
- Added `x-claude-code-prompt-id` to gateway hint headers for grouping requests
- Added `availableModelsMatch` managed setting with `"exact"` option for model version control
- Added `deniedModels` managed setting to block specific models
- Added MCP tool, WebFetch and WebSearch outputs to `tool.output` OpenTelemetry span event
- Added `/doctor prompt-audit` command to audit CLAUDE.md files and prompting patterns
- Added click-to-expand for truncated messages in fullscreen mode
- Added `path` to `--plugin-dir` load-failure entries in stream-json system/init
- Added opt-in `load_test_mode` block to Claude apps gateway config
- Added `mantle` upstream provider to Claude apps gateway for Amazon Bedrock

## Fixed (выборка из полного списка)
- Fixed SDK sessions losing deferred tool calls or finished tool results on early turn end
- Fixed MCP progress notifications discarded when long-running tool calls moved to background
- Fixed stdio MCP servers left running when session ended during startup
- Fixed HTTP 404 from stateless remote MCP server leaving it unusable for session duration
- Fixed weekly Fable limit not appearing in `/usage` with telemetry disabled
- Fixed `/model` picker showing hardcoded Haiku version instead of pinned model
- Fixed dynamic workflows re-running on fallback model instead of retrying configured model
- Fixed `DISABLE_PROMPT_CACHING_HAIKU` having no effect when Haiku is main model
- Fixed `/context` not counting MCP server instructions
- Fixed Windows PowerShell tool allowing deletion of protected system locations
- (плюс несколько десятков рутинных фиксов plugin/vim-mode/UI без заметного веса для практики)

## Improved
- `/mcp` tool list display, scrolling, and organization blocking indicators
- MCP tool result images now saved to files for Bash and Read tools
- `/tasks` dialog with status icons, paging, and better layout
- Compaction spinner timing and token counting
- `prompt-audit` output organization and thinking keyword handling
- First-reply and first-request latency; startup performance by deferring UI loading

## Changed
- Interactive sessions on third-party providers to start in auto mode
- `/model` picker to drop "(1M context)" for Opus
- Skill deny rules to also block skills delivered as plugins
- `claude plugin eval` to require git 2.31 or later
- Artifact watching auto-disarm after 3.5 hours of inactivity

## Версии после 2.1.283 в файле
Не найдены — 2.1.283 самая новая на момент снапшота (28.09.2026).
