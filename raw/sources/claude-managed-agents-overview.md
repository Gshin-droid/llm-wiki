# Raw: Claude Managed Agents — overview + quickstart (официальная документация)

Источники:
- https://platform.claude.com/docs/en/managed-agents/overview
- https://platform.claude.com/docs/en/managed-agents/quickstart
- Дополнительный контекст из https://platform.claude.com/docs/en/release-notes/overview (записи апрель–июль 2026 про Managed Agents)

Загружено: 2026-07-15.

## Overview (полный текст)

Pre-built, configurable agent harness that runs in managed infrastructure. Best for long-running tasks and asynchronous work.

Anthropic offers two ways to build with Claude:
| | Messages API | Claude Managed Agents |
|---|---|---|
| What it is | Direct model prompting access | Pre-built, configurable agent harness that runs in managed infrastructure |
| Best for | Custom agent loops and fine-grained control | Long-running tasks and asynchronous work |

Claude Managed Agents provides the harness and infrastructure for running Claude as an autonomous agent. Instead of building your own agent loop, tool execution, and runtime, you get a fully managed environment where Claude can read files, run commands, browse the web, and execute code securely. Built-in prompt caching, compaction, and other performance optimizations.

Also available on Claude Platform on AWS (some feature/session-behavior differences).

### Core concepts
- **Agent** — the model, system prompt, tools, MCP servers, and skills
- **Environment** — configuration for where sessions run: Anthropic-managed cloud sandbox, or self-hosted sandbox on your own infrastructure
- **Session** — a running agent instance within an environment, performing a specific task and generating outputs
- **Events** — messages exchanged between your application and the agent (user turns, tool results, status updates)

### How it works
1. Create an agent (model, system prompt, tools, MCP servers, skills — created once, referenced by ID across sessions)
2. Create an environment (cloud sandbox or self-hosted sandbox)
3. Start a session (references agent + environment)
4. Send events and stream responses (SSE, event history persisted server-side)
5. Steer or interrupt (send additional user events mid-execution, or interrupt)

### When to use
- Long-running execution (minutes/hours, multiple tool calls)
- Cloud infrastructure (secure sandboxes, pre-installed packages, network access)
- Self-hosted execution (compliance/data-residency)
- Minimal infrastructure (no need to build own agent loop/sandbox/tool execution)
- Stateful sessions (persistent filesystem + conversation history across interactions)
- Scheduled execution (cron via scheduled deployments)

### Supported tools
Bash, file operations (read/write/edit/glob/grep), web search and fetch, MCP servers.

### Beta access
Currently in beta. All endpoints require `managed-agents-2026-04-01` beta header, EXCEPT memory store endpoints which use `agent-memory-2026-07-22` instead (as of 2026-07-02, replacing the old header for memory calls; old header still works for memory until 2026-07-22). MCP tunnels and "dreaming" (memory reorganization) are more limited research preview, need separate access request.

Stateful by design — sessions long-running, resume cleanly, store conversation history/sandbox state/outputs server-side. NOT eligible for Zero Data Retention or HIPAA BAA because of this. Sessions and uploaded files can be deleted via API at any time.

## Quickstart (ключевые шаги + пример кода)

Guided setup alternative: `/claude-api managed-agents-onboard` slash command in latest Claude Code.

1. Install CLI (`ant`, via brew/curl/go install) or SDK (`pip install anthropic`, `npm install @anthropic-ai/sdk`, etc — same SDK as Messages API, just under `client.beta.agents/environments/sessions`)
2. `export ANTHROPIC_API_KEY=...`
3. Create agent:
```python
from anthropic import Anthropic
client = Anthropic()
agent = client.beta.agents.create(
    name="Coding Assistant",
    model="claude-opus-4-8",
    system="You are a helpful coding assistant. Write clean, well-documented code.",
    tools=[{"type": "agent_toolset_20260401"}],
)
```
`agent_toolset_20260401` tool type enables the full pre-built toolset (bash, file ops, web search, etc).

4. Create environment:
```python
environment = client.beta.environments.create(
    name="quickstart-env",
    config={"type": "cloud", "networking": {"type": "unrestricted"}},
)
```

5. Create session (references agent.id + environment.id).

6. Send message + stream response:
```python
with client.beta.sessions.events.stream(session.id) as stream:
    client.beta.sessions.events.send(session.id, events=[{
        "type": "user.message",
        "content": [{"type": "text", "text": "Create a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt"}],
    }])
    for event in stream:
        match event.type:
            case "agent.message": ...  # streamed text
            case "agent.tool_use": ...  # tool name
            case "session.status_idle": break  # agent finished
```

### What's happening under the hood
1. Provisions a sandbox per environment config
2. Runs the agent loop — Claude decides which tools to use
3. Executes tools inside the sandbox (file writes, bash, etc)
4. Streams events in real time
5. Emits `session.status_idle` when done

## Дополнительные факты из release notes (апрель–июль 2026), не покрытые overview/quickstart
- Launched in public beta 2026-04-08, alongside the `ant` CLI (versioning API resources in YAML files)
- Multiagent orchestration + Outcomes: public beta с 2026-05-06
- Memory for Managed Agents: public beta с 2026-04-23 (`GET /v1/memory_stores/{id}/memories` и др.) — отдельная сущность от client-side memory tool (`memory_20250818`) в обычном Messages API
- Self-hosted sandboxes: доступны с 2026-05-19, как альтернатива исполнению tool calls в инфраструктуре Anthropic
- Scheduled deployments: cron-расписание для сессий, без необходимости строить свой планировщик — упомянуто как launched в цикле Fable 5 (2026-06-09)
- Webhooks: agent/deployment/deployment-run lifecycle события (2026-07-02) — можно реагировать на publish новой версии агента, паузу деплоя, failed scheduled run без polling
- Vaults: секьюрное внедрение credentials (env vars) в sandbox агента, с настройкой `injection_location` (headers/body/both) с 2026-07-02
- Dreams (research preview, 2026-05-06): читает existing memory store + past session transcripts, выдаёт реорганизованный memory store с merged duplicates, заменёнными stale entries, новыми инсайтами — требует отдельный beta header `dreaming-2026-04-21`
- `agent-memory-2026-07-22` beta header (добавлен 2026-07-02): меняет поведение list-memories — стабильный server-defined порядок (`order_by`/`order` игнорируются), `depth` принимает только 0/1/omitted, `path_prefix` должен заканчиваться на `/` и матчит целые path segments. Курсоры пагинации несовместимы между старым и новым заголовком. С 2026-07-22 старый заголовок `managed-agents-2026-04-01` перейдёт на то же поведение.
- Claude Platform on AWS: webhooks, multiagent orchestration, self-hosted sandboxes доступны там же с 2026-05-29; `GET /v1/environments/{id}/work` (self-hosted sandbox pending work) — с 2026-06-10

## Сравнение с соседними способами (для контекста, уже частично зафиксировано в вики через claude-agent-sdk.md)
Managed Agents = Anthropic держит sandbox и event log, разработчик исполняет tool calls, которые триггерит Claude. Типичный путь: прототип на Agent SDK (свой процесс/инфраструктура) → продакшн на Managed Agents (Anthropic-инфраструктура) — эта связка уже была зафиксирована как гипотеза в claude-agent-sdk.md, здесь подтверждена официальной документацией самого Managed Agents.

## Заметка про безопасность источника
Официальная документация platform.claude.com, без пользовательского/стороннего контента. Инструкций в адрес агента не встречено.
