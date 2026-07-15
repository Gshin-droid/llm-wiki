# MCP 2026-07-28 Specification Release Candidate

**URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
**Загружено:** 2026-07-09 (автономный ежедневный запуск)
**Тип фиксации:** содержимое получено через WebFetch (HTML→markdown, обработано моделью), не побайтовая копия страницы.

## Извлечённое содержимое (саммари инструмента WebFetch)

### Overview
The Model Context Protocol released a release candidate on May 21, 2026, for the `2026-07-28` specification—described as "the largest revision of the protocol since launch". The final specification ships on July 28, 2026, and contains breaking changes requiring a ten-week validation window for SDK maintainers.

### Stateless Protocol Core
The most significant change removes protocol-level session management. Previously, clients established sessions via an `initialize`/`initialized` handshake that generated an `Mcp-Session-Id` header, pinning them to specific server instances. The new stateless design eliminates both the handshake and session ID, allowing "any MCP request can land on any server instance."

Client metadata (protocol version, capabilities, client info) now travels in a `_meta` field on every request. This enables deployment behind "a plain round-robin load balancer" without sticky routing or shared session stores. Applications can still maintain state using explicit handle patterns — tools return identifiers that models pass back as arguments on subsequent calls.

### Server-to-Client Communication Restructuring
Two SEPs reshape how servers request client input mid-call:
- Servers may only issue requests while actively processing a client request (no unsolicited prompts).
- Multi Round-Trip Requests replace Server-Sent Events streams with `InputRequiredResult` payloads containing prompts and request state that clients echo back with responses.

### Enhanced Operability
- `Mcp-Method` and `Mcp-Name` headers enable routing without body inspection.
- List responses include `ttlMs` and `cacheScope` metadata (modeled on HTTP Cache-Control).
- W3C Trace Context propagation in `_meta` standardizes distributed tracing across SDKs.

### MCP Apps Extension
Server-rendered interactive HTML interfaces ship in sandboxed iframes. Tools declare UI templates ahead of time for prefetching and security review. All UI actions traverse "the same JSON-RPC base protocol" and audit paths as direct tool calls.

### Tasks Extension
Tasks transitioned from experimental core feature to an extension based on production redesigns. Servers answer `tools/call` with task handles; clients drive progress via `tasks/get`, `tasks/update`, `tasks/cancel`. Server-directed creation: clients advertise capability, servers decide when calls should run as tasks. `tasks/list` was removed.

### Authorization Hardening
Six SEPs align authorization with OAuth 2.0 / OpenID Connect practice:
- Clients must validate the `iss` parameter per RFC 9207 to mitigate mix-up attacks.
- Clients declare OpenID Connect `application_type` during Dynamic Client Registration.
- Credentials bind to issuing authorization servers; re-registration required when resources migrate.
- Clarified refresh token requests and scope accumulation during step-up authentication.

### Deprecation Policy
Roots, Sampling, and Logging deprecate under a formal lifecycle: at least twelve months between deprecation and earliest possible removal; deprecated methods keep functioning within one year of release; removal requires a separate SEP.

### JSON Schema Expansion
Tool schemas now support full JSON Schema 2020-12 (composition `oneOf`/`anyOf`/`allOf`, conditionals, `$ref`). Output schemas unrestricted. Implementations must avoid auto-dereferencing external URIs and bound schema depth/validation time.
Error code for missing resources changed from `-32002` to JSON-RPC standard `-32602`.

### Governance Evolution
Three governance SEPs: feature lifecycle policy (prevents breaking changes in future releases), Extensions framework (opt-in capabilities stabilize independently), Standards Track SEPs require matching conformance suite scenarios before Final status.

## Дополнительные результаты поиска (контекст)
- InfoQ (2026-07): "AI Model Context Protocol Adds Centralised Auth for Enterprise" — Enterprise-Managed Authorisation extension продвинута до stable, принята Anthropic, Microsoft, Okta.
- TechCrunch (2026-06-30): X выпустил официальный MCP-сервер для своего API.
- The New Stack: разбор дорожной карты MCP на 2026 год, тот же контекст stateless core.
