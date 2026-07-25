# Claude Opus 5 — официальный запуск, 24 июля 2026

Источники:
- https://platform.claude.com/docs/en/release-notes/overview (запись "July 24, 2026")
- https://platform.claude.com/docs/en/about-claude/models/overview (таблица "Latest models comparison")
- https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5

Дата снятия снапшота: 2026-07-25.

## Release notes, July 24, 2026 (дословно, ключевые пункты)

- We've launched **Claude Opus 5** (`claude-opus-5`), a step-change improvement over Claude Opus 4.8. Claude Opus 5 supports a 1M token context window (both the default and the maximum), 128k max output tokens, and thinking on by default, at $5 / $25 per MTok, the same pricing as Claude Opus 4.8. Available on the Claude API, Amazon Bedrock, Google Cloud, Microsoft Foundry.
- On Claude Opus 5, disabling thinking is allowed only at effort `high` or below: `thinking: {"type": "disabled"}` with effort `xhigh` or `max` returns a 400 error — a breaking change from Claude Opus 4.8.
- Effort is the primary control for steering Claude Opus 5: full ladder (`low`, `medium`, `high`, `xhigh`, `max`), `max` for capability-critical work.
- Mid-conversation tool changes now in beta on Fable 5, Mythos 5, Opus 4.8, and Opus 5: add/remove tools between turns while preserving prompt cache (`mid-conversation-tool-changes-2026-07-01` beta header).
- `fallbacks` parameter now supports `"default"` mode — Anthropic's recommended fallback models by refusal category (`server-side-fallback-2026-07-01` beta header).
- Fast mode for Claude Opus 4.7 removed entirely: requests with `speed: "fast"` now return an error (no silent fallback to standard, unlike Opus 4.6's removal). Migrate to Opus 5 or Opus 4.8 for fast mode.

## Models overview — таблица сравнения (актуальные модели)

| | Fable 5 | Opus 5 | Sonnet 5 | Haiku 4.5 |
|---|---|---|---|---|
| Описание | Next-gen intelligence, long-running agents | Complex agentic coding + enterprise | Best speed/intelligence combo | Fastest, near-frontier |
| Цена | $10 / $50 за MTok | $5 / $25 за MTok | $3 / $15 (вводная $2/$10 до 31.08.2026) | $1 / $5 |
| Контекст | 1M (default+max) | 1M (default+max, нет меньшего варианта) | 1M | 200k |
| Max output | 128k | 128k | 128k | 64k |
| Extended thinking (ручной) | Нет | Нет | Нет | Да |
| Adaptive thinking | Да (всегда) | Да | Да | Нет |
| Reliable knowledge cutoff | Jan 2026 | May 2026 | Jan 2026 | Feb 2025 |

Effort по умолчанию `high` на Claude API и Claude Code для Opus 5 и Sonnet 5 (на Opus 4.8 — `high` везде, включая claude.ai).

## What's new in Claude Opus 5 — ключевое

**Новая модель:** `claude-opus-5`, 1M-контекст — единственный вариант (нет меньшего окна), 128k max output, thinking on by default.

**Breaking change:** отключение thinking (`type: "disabled"`) разрешено только при effort `high` и ниже; на `xhigh`/`max` — 400 ошибка. При отключённом thinking модель иногда пишет вызов инструмента прямо в текстовый вывод вместо `tool_use` блока, либо оставляет внутренние XML-теги в видимом ответе.

**Поведенческие отличия, отмеченные самим Anthropic (важно для промптинга):**
- Развёрнутые ответы длиннее по умолчанию.
- В агентских сессиях модель чаще проговаривает прогресс пользователю.
- Охотнее делегирует субагентам в мультиагентных системах.
- **Сама проверяет свою работу без явной просьбы** — инструкции вида "добавь финальный шаг верификации" / "используй субагента для проверки", перенесённые с более старых моделей, вызывают избыточную повторную проверку на Opus 5 — рекомендация убрать их.

**Улучшения возможностей:** глубокое рассуждение, агентский кодинг и long-horizon задачи (доводит многофайловые фичи и рефакторинги до конца без заглушек), test-time compute scaling (эффект от `max` effort сильнее, чем у прежних моделей), эффективность на низких effort (`low`/`medium` дают сильное качество за малую долю токенов), **код-ревью и поиск багов** (высокий процент реальных багов за проход, мало false positives, точность держится и на низких effort), vision (диаграммы, репликация UI), long-context (согласованность инструкций/tool-calling/рассуждения по всему 1M окну), офисные задачи (сложные таблицы, презентации), **мультиагентная координация** (эффективные writer-verifier паттерны, редко перезаписывают работу друг друга).

**Fast mode:** research preview, только через Claude API (не Bedrock/GCP/Foundry), $10/$50 за MTok.

**Прочее:** минимальная длина кэшируемого промпта снижена до 512 токенов (было 1024 на Opus 4.8).

**Доступность:** Claude API (всем), AWS Bedrock (`anthropic.claude-opus-5`), Google Cloud, Microsoft Foundry. Opus 4.8 остаётся доступен везде параллельно.

## Сторонний контекст (не первоисточник, для ориентира)
- Cognition (Devin) отметили на FrontierCode 1.1: "Claude Opus 5 approaches Fable-level performance at half the cost", особенно в отладке и root-cause анализе.
- По данным стороннего обзора — сопоставимые или лучшие показатели против Opus 4.8 на agentic safety suite Anthropic, наибольший прирост — устойчивость к prompt injection в кодинге/computer use/browser use.
- Роллаут по провайдерам — 23–24 июля 2026.
