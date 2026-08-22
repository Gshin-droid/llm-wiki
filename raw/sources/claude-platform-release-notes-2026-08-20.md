---
source: официальные Claude Platform release notes
url: https://platform.claude.com/docs/en/release-notes/overview
retrieved: 2026-08-22
covers: записи 2026-08-18 — 2026-08-20 (диапазон с прошлой сверки 2026-08-19, покрывавшей до 08-16)
---

### August 20, 2026

* We've released **v1.0 of the Python SDK**. The SDK's HTTP layer moves from `httpx` to httpx2, a maintained, API-compatible fork: build custom `http_client`, `Timeout`, and transport objects from `httpx2` (the `DefaultHttpxClient` helpers are unchanged), and call `httpx2.alias_httpx()` at startup if you rely on tracing or mocking libraries that patch `httpx`. v1.0 requires Python 3.10 or later and removes long-deprecated surface, including the legacy Text Completions API, the `temperature`, `top_p`, and `top_k` parameters on Messages methods, and the tool runner's client-side `compaction_control`. On the async client, `.with_raw_response` results now need `await response.parse()`, and `AnthropicBedrock` now raises an error when no AWS region is configured instead of defaulting to `us-east-1`. See the v1 migration guide for every change with before-and-after snippets.

### August 19, 2026

* The computer use tool is out of beta on the Claude API as the `computer_toolset_20260801` toolset: no beta header, batch actions (several actions in one turn), `zoom` enabled by default, and per-member configuration through `configs`. Earlier beta versions remain available. Upgrading an existing integration changes the request shape and tool handling.
* We've launched the browser use tool (`browser_toolset_20260801`), a client toolset for driving a browser that your application hosts. It works inside a browser viewport rather than a whole desktop, reading the page itself (its accessibility tree, elements, forms, and tabs) and adding element references, form input, tab management, download reporting, and opt-in file upload on top of screenshot-and-click control.
* Both toolsets are available for Claude Fable 5, Claude Mythos 5, Claude Opus 5, Claude Sonnet 5, and Claude Opus 4.8 on the Claude API.
* The Files API is out of beta on the Claude API. Requests to the `/v1/files` endpoints, and Messages API requests that reference an uploaded file, no longer require the `files-api-2025-04-14` beta header. Requests sent without the header use the current response format: file expiration (`expires_in_seconds` on upload, `expires_at` on the file object), and `page`/`next_page` pagination plus an `ids[]` filter when listing files. Requests that still send the header keep working and return the previous response format.
* Agent Skills and the Skills API (`/v1/skills`) are out of beta on the Claude API. Requests no longer require the `skills-2025-10-02` beta header, including Messages API requests that load Skills through the `container` parameter. Requests that still send the header continue to work unchanged.
* The Admin API user-management endpoints for Claude Enterprise (claude.ai) organizations (members, invites, groups, and custom roles) are out of beta. The `anthropic-beta: ce-user-management-2026-07-13` header is no longer required on group and custom-role requests; requests that still send it are accepted unchanged.
* You can now restrict which sites a Claude Managed Agents agent's `web_search` and `web_fetch` tools can reach. Set `allowed_domains` or `blocked_domains` on the tool's entry in the `agent_toolset_20260401` `configs` array; `web_fetch` also accepts `max_content_tokens` and `web_search` accepts `user_location`. Each `configs` entry is identified by its `name` and typed by an optional `type`, and requests that pass only `name`, `enabled`, and `permission_policy` continue to work; in the typed SDKs, `configs` entries become per-tool types.
* Claude Managed Agents sessions that run in a self-hosted sandbox can now attach memory stores. The Python, TypeScript, and Go SDK workers download each attached store into the sandbox at its `mount_path` and sync the agent's changes back to the store.
* The session viewer in the Claude Console has been redesigned with a timeline minimap, a transcript grouped by model request, and an Inspector panel for session details and cost, raw events, per-tool statistics, mounted resources, and per-thread activity.

### August 18, 2026

* Workbench is now Playground in the Claude Console. Playground supports every Messages API parameter and includes templates that demonstrate API features such as code execution and web search. It shows the full SDK request and the API response for each run.
