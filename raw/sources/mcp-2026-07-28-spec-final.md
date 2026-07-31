# The 2026-07-28 Specification (MCP, финальный релиз)

**URL:** https://blog.modelcontextprotocol.io/posts/2026-07-28/
**Загружено:** 2026-07-31 (автономный еженедельный разведчик)
**Тип фиксации:** содержимое получено через WebFetch (HTML→markdown, обработано моделью), не побайтовая копия страницы.

## Извлечённое содержимое (саммари инструмента WebFetch)

### Publication Date
July 28, 2026

### Overview
The Model Context Protocol released version 2026-07-28, transforming MCP from "a bidirectional stateful protocol into a request/response stateless protocol." This represents the protocol's most significant evolution since its initial launch.

### Major Changes

**Stateless Protocol Core**
The specification eliminates the `initialize`/`initialized` handshake and `Mcp-Session-Id` headers. Each request now carries protocol version, client identity, and capabilities in metadata. Servers can handle requests on any instance behind round-robin load balancers without shared state management. Optional `server/discover` RPC allows clients to query capabilities proactively.

**Multi Round-Trip Requests (MRTR)**
Replaces server-initiated requests that previously required open streams. Tools can request user input mid-execution (confirmations, missing parameters) by returning `resultType: "input_required"` with needed requests, and clients retry with answers in `inputResponses`.

**Header-Based Routing**
HTTP requests now include `Mcp-Method` and `Mcp-Name` headers, enabling gateways and rate limiters to route and meter traffic without parsing JSON payloads.

**Cacheable List Results**
`tools/list`, `prompts/list`, `resources/list`, and `resources/read` responses now include `ttlMs` and `cacheScope` parameters for intelligent client-side caching strategies.

**Authorization Hardening**
- Implements RFC 9207 issuer validation to prevent authorization-server mix-up attacks
- Supports `application_type` in Dynamic Client Registration for localhost redirects in desktop/CLI apps
- Credentials bound to issuing authorization servers
- Formally deprecates Dynamic Client Registration in favor of Client ID Metadata Documents (CIMD)

**Tasks Extension**
Tasks transition from experimental core to the `io.modelcontextprotocol/tasks` extension, featuring poll-based `tasks/get` and new `tasks/update` operations. Notifications consolidate into a single `subscriptions/listen` stream.

### Stability Status

**Stable/Generally Available:**
- Stateless protocol core
- MRTR
- Header-based routing
- List caching
- Authorization updates
- Tasks extension
- Formal extensions framework

**Deprecated (12-month minimum offramp):**
- Roots, Sampling, and Logging features
- Legacy HTTP+SSE transport
- Dynamic Client Registration (replaced by CIMD)

### SDK Support
All Tier 1 SDKs support the specification: TypeScript, Python, Go, and C#. The Rust SDK supports it in beta.

### Industry Adoption
Major ecosystem partners including AWS, Cloudflare, Google Cloud, Microsoft, Anthropic, and numerous other organizations have committed to supporting the specification, emphasizing enterprise scalability and stateless operation as key advantages.

## Дополнительно: анонс Anthropic (не первоисточник, восстановлено по поисковым сниппетам)

Прямой фетч `claude.com/blog/bringing-mcp-2026-07-28-to-claude` вернул 403 (та же защита, что и у других страниц `claude.com/blog` в этой вики — зеркало `raw.githubusercontent.com/RobGruhl/anthropic-docs-mirror` для этой конкретной статьи не нашлось, 404). Ниже — сводка по фрагментам поисковой выдачи, не по полному тексту:

- Claude расширяет поддержку спецификации 2026-07-28: stateless core, усиленные OAuth/OIDC, версионированные расширения Apps и Tasks.
- Новые фичи коннекторов: embedded UI, enterprise-managed auth, observability, приватные network tunnels.
- **MCP tunnels** (research preview) — подключение Claude к MCP-серверам внутри приватной сети без публичного интернета, без входящих firewall-правил.
- Раскатка идёт по продуктам Claude постепенно ("rolling out across Claude products soon"), точные даты по продуктам не названы в доступных сниппетах.

Смежные заголовки блога Anthropic, найденные тем же поиском, но не прочитанные (потенциальные источники для будущего ingest): "Interactive connectors and MCP Apps", "New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels", "Remote MCP support in Claude Code".
