---
source: официальные platform.claude.com/docs (models overview + release notes) и CHANGELOG.md репозитория anthropics/claude-code
urls:
  - https://platform.claude.com/docs/en/about-claude/models/overview
  - https://platform.claude.com/docs/en/release-notes/api
  - https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
retrieved: 2026-09-04
published: 2026-09-01 (модель) / версии Claude Code 2.1.257–2.1.260 (даты отдельных версий в самом CHANGELOG.md не указаны, окно между 2026-08-31 и 2026-09-04)
---

# Models overview — таблица сравнения (фрагмент, актуально на 2026-09-04)

| Feature | Claude Fable 5.1 | Claude Opus 5 | Claude Sonnet 5 | Claude Haiku 4.5 |
|---|---|---|---|---|
| Description | For demanding reasoning and long-horizon agentic work | For complex agentic coding and enterprise work | The best combination of speed and intelligence | The fastest model with near-frontier intelligence |
| Pricing | $10 / input MTok, $50 / output MTok | $5 / input MTok, $25 / output MTok | $2 / input MTok, $10 / output MTok | $1 / input MTok, $5 / output MTok |
| Claude API ID | `claude-fable-5-1` | `claude-opus-5` | `claude-sonnet-5` | `claude-haiku-4-5-20251001` |
| Thinking | Adaptive (always on) | Adaptive | Adaptive | Extended |
| Default effort | `high` | `high` | `high` | Not supported |
| Context window | 1M tokens | 1M tokens | 1M tokens | 200K tokens |
| Max output | 128K tokens | 128K tokens | 128K tokens | 64K tokens |
| Reliable knowledge cutoff | Jun 2026 | May 2026 | Jan 2026 | Feb 2025 |
| Retirement | Not sooner than September 1, 2027 | Not sooner than July 24, 2027 | Not sooner than June 30, 2027 | Not sooner than October 15, 2026 |

Текст под таблицей: "start with Claude Opus 5 for most workloads. Use Claude Fable 5.1 for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5 at higher effort still fall short."

Про кэш: "Pricing: Base price per million tokens. Batch API requests are 50% off; prompt cache reads cost 10% of the base input price (2.5% on Claude Fable 5.1 and Claude Mythos 5.1)."

Legacy models (still available), список включает: Claude Fable 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Opus 4.5, Claude Sonnet 4.6, Claude Sonnet 4.5.

# Release notes (platform.claude.com/docs/en/release-notes/api)

## September 1, 2026 — Claude Fable 5.1 Launch

Дословная цитата анонса: "We've launched Claude Fable 5.1 (`claude-fable-5-1`), the successor to Claude Fable 5 for long-running agentic coding, knowledge work, and research, alongside Claude Mythos 5.1 (`claude-mythos-5-1`) for Project Glasswing participants. Both models support a 1M token context window by default, 128k max output tokens, and always-on adaptive thinking, at $10 / $50 USD per MTok, the same as Claude Fable 5, with cache reads cut to $0.25 per MTok."

Дополнительные пункты того же release notes:
- Доступность: Claude API, Amazon Bedrock, Claude Platform on AWS, Google Cloud, Microsoft Foundry.
- "Prompt cache reads on Claude Fable 5.1 and Claude Mythos 5.1 cost $0.25 USD per million tokens: 0.025x the base input price, compared with 0.1x on other models."
- "`tool_choice` types `any` and `tool` aren't supported and return a 400 error. `auto` and `none` are unchanged."
- Thinking-блоки сохраняются только для той же или более новой модели (совместимость истории диалога при смене модели).
- "Per-message effort changes are in beta on Claude Fable 5.1, Claude Mythos 5.1, and Claude Opus 5."
- Текст ответа несёт водяной знак Anthropic ("Anthropic's text watermark").
- "Like Claude Fable 5, both models require 30-day data retention and aren't available under zero data retention unless expressly authorized by Anthropic."

## August 27, 2026 (соседняя запись release notes, для контекста)

"In Python SDK 1.2.0, TypeScript SDK 0.122.0, Go SDK 1.68.0, Java SDK 2.59.0, Ruby SDK 1.67.0, and C# SDK 12.44.0, `client.beta.files` and `client.beta.skills` no longer send the `files-api-2025-04-14` and `skills-2025-10-02` beta headers and return the same shapes as `client.files` and `client.skills`."

# Claude Code CHANGELOG.md — версии 2.1.257–2.1.260 (пункты, проверенные точечными запросами к сырому файлу; полный список версии содержит и рутинные фиксы, здесь только отобранное)

## 2.1.257
- "Added Claude Fable 5.1 (`claude-fable-5-1`), now the default Fable model — 1M context" (Fable 5.1 доступна в `/model` picker Claude Code, становится дефолтом внутри семейства Fable)
- "Added a Containment Escape rule to auto mode so cloud metadata-credential fetches, egress evasion, and cross-tenant reach are no longer auto-approved unless your environment marks them expected."
- Добавлена настройка формата времени/часового пояса для таймстампов.
- `/doctor`-предупреждение об устаревших sandbox mask файлах.
- Разовый запрос разрешения на первое чтение файла за пределами рабочей директории (было — блокировка/иное поведение).
- Улучшено сохранение промпт-кэша при смене effort в середине сессии.
- Расширено покрытие промпт-кэша для Fable 5.1 на результаты инструментов.

## 2.1.258
- Фикс запуска Claude Code на macOS 12 (Monterey) — критичный фикс совместимости.
- Фикс: удалённые/scheduled-сессии не работали после re-send подтверждения разрешения.

## 2.1.259
- "Added `managedMcpServers` managed setting: organizations can provide HTTP/SSE MCP servers to every user (same entry shape as `.mcp.json`); entries that name a command to run are skipped" — org-level провижининг MCP-серверов, локальные command-based entries игнорируются (снижение риска произвольного исполнения команд через managed-конфиг).
- Добавлен `--permission-prompts none` для unattended headless-хостов.
- Фикс: одновременные сессии могли тихо затирать изменения друг друга.
- Фикс: Bash `Read()` deny-правила не покрывали значения опций и редиректы.
- Фикс: промпт-кэш инвалидировался при обновлении OAuth-токена.

## 2.1.260
- Diff panel в fullscreen-режиме — показывает незакоммиченные изменения, переключатель `/diff`.
- Диагностика промпт-кэш-миссов в `/cost` и статус-строке.
- `/reload-plugins` для headless-сессий.
- Фикс: `/model`-picker не показывал Fable 5.1 для eligible-организаций.
- Фикс: промпт-кэширование на Fable 5.1 повторно отправляло контекст после результатов инструментов.
- Фикс: правила разрешений со скобками ошибочно считались невалидными.
- Фикс: макОS git-конфиг скрывался от сэндбоксированных git-операций.

Проверка нумерации версий: заголовки 2.1.253–2.1.256 в файле отсутствуют — файл переходит от 2.1.252 напрямую к 2.1.257 (публичный CHANGELOG.md пропускает внутренние номера; не первый такой разрыв в наблюдаемой серии).
