---
title: How Anthropic runs large-scale code migrations with Claude Code
type: web-article (официальный блог Anthropic) + convergent secondary reporting
primary_url: https://claude.com/blog/ai-code-migration
fetched: не удалось — сервер вернул 403 (тот же паттерн, что и support.claude.com/claude.com/blog в прошлых прогонах)
captured: 2026-07-27
---

# Заметка о недоступности первоисточника

Прямой фетч `https://claude.com/blog/ai-code-migration` вернул HTTP 403 (WebFetch). Та же судьба у вторичного первоисточника — блога Bun (`https://bun.com/blog/bun-in-rust`) и ряда обзоров (InfoQ, TheRegister, DevelopersDigest, SimonWillison) — все вернули 403 при прямом фетче через доступный инструмент.

Содержимое ниже восстановлено через WebSearch (несколько независимых поисковых запросов), который агрегирует контент иначе и не упёрся в те же блокировки. Цифры сходятся между независимыми пересказами (Register, Developers Digest, Bun-адъютант посты, X/Jarred Sumner, Andrew Kelley blog) — это даёт разумную уверенность, но это **не эквивалент прочтения первоисточника**. Прецедент: закрытие пробела "биллинг Claude Agent SDK" (2026-07-15) использовало тот же метод при том же типе блокировки.

## Собранные факты

### Официальный блог Anthropic (`claude.com/blog/ai-code-migration`)
Пошаговый гайд по крупномасштабным миграциям кода через Dynamic Workflows. Собственная практика Anthropic: за последний месяц (до публикации) отдельные разработчики внутри компании мигрировали 10 кодовых пакетов (от десятков до сотен тысяч строк) через Claude Fable 5, Claude Opus 4.8 и Dynamic Workflows.

### Кейс Bun: Zig → Rust (Jarred Sumner, создатель Bun)
- Итог: ~750 000–1 009 272 строк Rust (расхождение между источниками; порядок величины — больше миллиона строк итогового кода), заменивших ~535k строк Zig
- 99.8% существующего тест-сьюта Bun прошло без изменений в поведении
- 11 дней от первого коммита до мержа
- Пик — 64 параллельных агента Claude одновременно, ~50 отдельных Dynamic Workflows прогонов за весь период, один инженер как оркестратор
- Модель: pre-release Claude Fable 5
- Стоимость API: ~$165 000

**Архитектура воркфлоу (фазы):**
1. Отдельный workflow вычисляет правильный Rust lifetime для каждого поля каждой структуры во всей Zig-кодовой базе
2. Следующий workflow пишет каждый `.rs`-файл как behavior-identical порт соответствующего `.zig`-файла — сотни агентов параллельно, по 2+ ревьюера на файл
3. Fix-loop: гоняет сборку и тест-сьют, пока оба не станут чистыми
4. Overnight-воркфлоу: убирает лишние копирования данных (оптимизация), каждый фикс — отдельный PR на финальный ревью

**Quality gates:**
- Adversarial review на каждое изменение (2+ независимых ревьюера на одного имплементора)
- Пофазовые машинные проверки (`cargo check` на каждый crate → CLI smoke tests)
- TS тест-сьют Bun (1.38M+ assertions) должен пройти в CI на всех 6 платформах перед мержем

### Критика: Andrew Kelley (создатель Zig)
Назвал результат "unreviewed slop". Аргументы:
- ~13 000 unsafe-блоков попали в продакшн без человеческого ревью
- Вопрос: как тест-сьют может быть достаточным доказательством отсутствия багов в непроверенном коде такого масштаба
- Не техническая претензия к Rust vs Zig, а расхождение "систем ценностей" двух проектов (по формулировке самого Kelley)
- Community response (Hacker News) — расколота: часть отмечает, что компилятор Rust поймал тысячи багов в процессе порта; часть встревожена именно фактом непроверенных unsafe-блоков в проде

### Klarna (Alessio Vallero, Senior Engineering Manager)
Dynamic Workflows — для масштабных security-аудитов продакшен-кода: поиск отсутствующей аутентификации, хрупкой валидации входных данных, небезопасных паттернов, скопированных между микросервисами.

### CyberAgent (Ken Takao, Lead Systems Engineer; один из крупнейших ad-tech в Японии)
Workflows — для hardening-проходов по продакшен-сервисам, с adversarial-агентами, проверяющими друг друга перед выдачей финального результата.

## Источники (все — вторичные пересказы, не первоисточник)
- https://www.theregister.com/devops/2026/07/14/zig-creator-calls-buns-claude-rust-rewrite-unreviewed-slop/5270743
- https://www.developersdigest.tech/blog/bun-rust-rewrite-agent-fleet-case-study
- https://www.developersdigest.tech/blog/zig-anthropic-bun-rewrite-controversy
- https://andrewkelley.me/post/my-thoughts-bun-rust-rewrite.html
- https://x.com/jarredsumner/status/2060050578026189172
- https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/ (не прочитан напрямую, 403)
- https://enterprisedna.co/resources/ai-pulse/ai-pulse-2026-07-20-claude-code-s-bun-in-rust-rewrite-is-a-live-governance-fight/

## Проверка на инструкции-в-содержимом
Обнаружено не было — весь материал прочитан через агрегирующие сниппеты WebSearch, инструкций агенту не встречалось.
