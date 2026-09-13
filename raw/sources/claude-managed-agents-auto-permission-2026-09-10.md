---
source: официальные Claude Platform release notes + документация permission-policies / sessions-connect
url: https://platform.claude.com/docs/en/managed-agents/permission-policies ; https://platform.claude.com/docs/en/cli-sdks-libraries/cli/sessions-connect
retrieved: 2026-09-13
covers: запись release notes за 2026-09-10
---

# Release notes — 10 сентября 2026

## Claude Managed Agents Permission Policies — `auto` Mode
- Permission policies now include `auto`: the server evaluates each agent or MCP tool call and runs it, denies it, or pauses for approval
- `agent.tool_use` and `agent.mcp_tool_use` events report evaluation results in an `evaluation` field alongside `evaluated_permission`
- See: Let the server evaluate each call with `auto`

## `ant` CLI Sessions Connect
- Added `ant beta:sessions connect` command to attach terminal to Claude Managed Agents sessions
- Follow sessions live, send messages, and allow/deny tool calls awaiting approval
- `--web` flag serves the Claude Console's session viewer locally
- See: Connect to a Managed Agents session from your terminal

---

# permission-policies.md (ключевые разделы, дословные цитаты)

Permission policy types: `always_allow` (executes automatically), `always_ask` (session pauses for approval), `auto` (server evaluates each call and runs/denies/pauses it).

Each toolset kind has its own default: the agent toolset defaults to `always_allow`, and MCP toolsets default to `always_ask`. No toolset uses `auto` by default — must be set explicitly per toolset (`default_config.permission_policy`) or per tool (`configs` entry override), for both the agent toolset and MCP toolsets.

"Let the server evaluate each call with `auto`": the server evaluates the tool, its input, and session content up to that point — can treat two calls to the same tool differently. Three outcomes: runs (safe), denied (high-risk — agent gets error `Permission to use {tool_name} has been denied.`, `is_error: true`, client cannot override), or pauses for approval (server reaches no determination, behaves like `always_ask`).

Event example:
```json
{
  "type": "agent.tool_use",
  "name": "bash",
  "input": {"command": "rm -rf /workspace/reports"},
  "evaluated_permission": "deny",
  "evaluation": {
    "type": "auto",
    "evaluated_permission": {"type": "deny", "reason_code": "high_risk"}
  }
}
```

Table of `evaluation` forms: `{"type": "always_allow"}` → allow; `{"type": "always_ask"}` → ask; `{"type": "auto", "evaluated_permission": {"type": "allow"}}` → allow (server determined safe); `{"type": "auto", ..., "type": "ask", "reason_code": "indeterminate"}` → ask; `{"type": "auto", ..., "type": "deny", "reason_code": "high_risk"}` → deny.

"What you post in `user.message` events counts as your intent, and it can lead the server to allow a call it would otherwise deny. The server does not read intent from a tool result, a fetched webpage, an MCP server's response, or a message between session threads. It assesses that content but does not take instructions from it. [...] If you relay untrusted end-user input in `user.message` events, the server reads that input as your intent too, and it can get a call allowed."

Warning (verbatim): "`auto` is not a human checkpoint. If the server determines that a call is safe, the call runs before anyone sees it, and its effects might not be reversible. If a person must review a tool's calls before they run, configure `always_ask` on that tool."

`evaluation` absent in two cases: tool not enabled in session (denied without evaluation), or events recorded before `evaluation` was introduced (read as `always_allow`/`always_ask` by `evaluated_permission`). `agent.custom_tool_use` events carry neither field — permission policies don't govern custom tools (application-executed, controlled by the developer).

# sessions-connect.md (ключевые разделы, дословные цитаты)

"`ant beta:sessions connect` attaches your terminal to an existing Claude Managed Agents session. It loads the session's transcript and follows it live as the agent works. You can also step in: send a message, interrupt the agent, or allow or deny a tool call that is waiting for approval. With `--web`, it opens the session in the Claude Console's session viewer in your browser instead."

Keys: Enter (send `user.message`), Esc (interrupt, `user.interrupt`), Ctrl+O (toggle detail: tool inputs/results, token usage, status events), Page Up/Down (scroll), Ctrl+C (detach, session keeps running).

"When a tool call is waiting for your approval, the input line changes to **Allow tool call?** This happens under an `always_ask` policy, or under `auto` when the server reaches no determination." Choices: Yes / No / No, and tell the agent why (sent as `deny_message`).

`--web`: serves Console's session viewer from local server on `127.0.0.1`, opens browser. "Your credentials never leave the CLI: the page sends requests only to the local `ant` process, which makes the API requests." URL usable once, within two minutes of being printed.
