# Agentic AI Foundation (AAIF)

Фонд при Linux Foundation, который держит governance открытых стандартов агентского ИИ вместо одной компании. Соучредители — Anthropic, Block и OpenAI.

**Тип:** организация (governance-фонд)
**Актуально на:** 2026-10-25

## Что под AAIF

- **MCP (Model Context Protocol)** — передан Anthropic раньше (точная дата передачи этим ingest'ом не устанавливалась — не изобретать; известно только, что к 22.10.2026 MCP уже был там). См. [[mcp-model-context-protocol]].
- **Agent Skills** — передан Anthropic 22.10.2026, вместе с именем, лого, GitHub-организацией и доменом `agentskills.io`. См. [[claude-skills]], разбор — [[claude-skills-agentic-ai-foundation]].

## Governance

Описывается донором (Anthropic) как «open, community-driven, and vendor-neutral» — самоописание передающей стороны, не независимая оценка, см. оговорку на [[claude-skills-agentic-ai-foundation]]. Инженеры Anthropic, Google, OpenAI и других компаний сопровождают стандарты как частные лица, не от имени работодателя. Ведущие мейнтейнеры Agent Skills — David Soria Parra и Mahesh Murag (последний — один из создателей Skills в Anthropic, см. [[anthropic-code-summit-build-skills-talk]]). Участвовать и дополнять стандарт можно без вступления в AAIF; фидбек по изменениям спецификации — через Discord проекта.

## Зачем это вики

Governance двух протоколов, уже использующихся в этой вики (Skills — через `wiki-ingest`/`wiki-lint`, MCP — через [[context7]] и другие установленные серверы), теперь сосредоточена в одном месте. Практическое следствие: версионированные релизы спецификации и будущее security guidance для авторов скиллов стоит отслеживать через AAIF, а не только через changelog Claude Code — изменение спецификации может прийти независимо от релиза самого продукта Anthropic.

## Связи

- Источники: [[claude-skills-agentic-ai-foundation]]
- Сущность: [[claude-skills]]
- Концепт: [[mcp-model-context-protocol]], [[skill-authoring-practical-rules]]
