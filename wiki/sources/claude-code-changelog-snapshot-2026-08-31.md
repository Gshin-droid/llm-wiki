# Claude Code changelog 2026-08-31

**Дата загрузки:** 2026-08-31
**Автор:** [[claude-code]]
**Опубликовано:** 2026-08-31 (версия)
**Тип:** официальная документация (changelog)
**Ссылка:** https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
**Raw:** `raw/sources/claude-code-changelog-2026-08-31.md`

## Саммари

Прогон новостного разведчика через три дня после предыдущего снапшота (2026-08-28, покрывал 2.1.246–2.1.250). Вышла одна версия — **2.1.251**, без headline-анонса, но с самой плотной за всё окно наблюдения пачкой security-фиксов (пять независимых находок в одной версии) и тремя добавлениями прямого практического веса: hook-события переключения модели, стриминг тулкоплов субагента в Remote Control и видимость промпт-кэша/спенд-лимита в `/cost`/`/usage`. Официальные **Claude Platform release notes** проверены отдельно — новых записей после 27.08 нет, окно с прошлого снапшота пустое.

## Находка 1: пять bypass-фиксов в одной версии — крупнейшая пачка серии

Серия, которую эта вики отслеживает на [[ai-security-by-design]] с 07-19 (обычно 1–2 находки на снапшот), в 2.1.251 дала сразу пять независимых фиксов:

- *"Fixed file tools (Read, Write, Edit) following a symlink swapped inside the working directory after the permission check, which could read or write outside the approved location"* — TOCTOU-гонка: файл проверяется на разрешение, затем **между проверкой и обращением** симлинк подменяется на путь вне рабочей директории, и файловый инструмент следует за ним. Не точечный обход конкретного пути (как прежние Windows/NT-находки), а гонка во времени — новый подкласс внутри уже известного семейства «файловый примитив обходит проверку».
- *"Fixed plugin commands declared in a marketplace entry being able to point outside the plugin directory; such paths are now rejected with a path-traversal error"* — path traversal в командах плагина, прямое продолжение темы цепочки поставок расширений ([[deepseek-harness-zproger-review]], раздел на [[ai-security-by-design]]).
- *"Fixed project settings being able to enable detailed beta tracing or raw API body logging, and a lower-scope beta tracing endpoint bypassing an OTLP collector pinned by managed settings or a host app"* — project-level settings могли включить подробный beta-трейсинг/логирование сырых тел API-запросов и обойти OTLP-коллектор, закреплённый managed settings или хост-приложением; наблюдаемость обходила административный контроль.
- *"Fixed the Workflow tool reading (and quoting in errors) a `scriptPath` outside what the session may read before the permission check ran"* — Dynamic Workflows (механизм, которым эта вики оркеструет пакетные прогоны) читал файл скрипта до, а не после проверки разрешений; прямое продолжение темы 08-07 (побег из сэндбокса Workflow через `import()`).
- *"Fixed Grep and Glob not applying `Read(...)` deny rules to files reached through a symlinked search path"* — deny-правила `Read(...)` не применялись к файлам, до которых Grep/Glob добирались через симлинк в пути поиска.

Общее у всех пяти — не новый вектор атаки, а конкретное расширение зоны действия уже существующих проверок (permission check, deny-правила, managed settings) на путь, который эти проверки раньше не покрывали: время (гонка), файловый путь (симлинк/traversal), или источник конфигурации (project settings против managed). Подтверждает наблюдение, уже записанное на [[ai-security-by-design]] 08-16 — один и тот же механизм регулярно даёт течь в разных местах месяцами после того, как выглядел «готовым».

Дополнено в [[ai-security-by-design]].

## Находка 2: `PreModelSwitch`/`PostModelSwitch` — новые hook-события

*"Added `PreModelSwitch` and `PostModelSwitch` hook events (block, confirm, or annotate a model switch); `SessionStart` resume hooks now receive session staleness and the estimated re-cache cost"*.

Первые хуки этой вики, привязанные конкретно к смене модели внутри сессии (ручной `/model`, авто-переключение `opusplan`, fallback-цепочки — все задокументированы на [[claude-code]] в разделе «Модели и Effort»). До этого переключение модели было немым событием: хук может теперь заблокировать его, потребовать подтверждения или просто аннотировать факт для журнала/статуслайна. Вторая часть находки — `SessionStart`-хуки при резюме сессии получают возраст сессии и оценку стоимости пере-кэширования, что напрямую пересекается с TTL-темой на [[claude-api-cost-optimization]]: резюмирующий хук теперь может решить, стоит ли продолжать сессию с холодным кэшем, зная цену заранее, а не постфактум.

Дополнено в [[claude-code]].

## Находка 3: видимость спенд-лимита и промпт-кэша в `/usage`/`/cost`

*"Added a Spend limit bar to `/usage` and a `rate_limits.spend_limit` status line field for developers behind a Claude apps gateway with spend limits"* и *"Added a per-session prompt-cache line to `/cost` (hit ratio, misses, tokens re-cached, warm/cold) and a matching `prompt_cache` object for status line scripts"*.

Оба пункта — видимость, не новая механика: спенд-лимит шлюза организации и статистика попаданий промпт-кэша (hit ratio, misses, warm/cold) существовали и раньше, но не были видны без ручного разбора логов. Прямое продолжение линии дополнений [[claude-api-cost-optimization]] от 08-25/08-28 (TTL кэша) — теперь у той же страницы появляется штатный способ **проверить**, что настроенный TTL действительно снижает промахи, а не полагаться на теорию.

Дополнено в [[claude-api-cost-optimization]].

## Малое

- **Стриминг тулкоплов foreground-субагента в Remote Control** — *"live streaming of a foreground subagent's tool calls and results to Remote Control clients (background subagents, the default, still show status only)"*; фоновые субагенты (дефолт этой вики для автономных прогонов) по-прежнему показывают только статус, находка касается foreground-режима.
- **CLI-команды `attach`/`logs`/`stop`/`respawn`/`rm`** появились в `claude --help`; `--resume`-подсказка для работающей фоновой сессии теперь называет точную команду `claude attach <id>`.
- Ряд фиксов без изменения практической механики этой вики: пустые text-content-block ошибки после хода из одного thinking, дефолтный режим первого запуска, Opus 5 effort xhigh/max при выключенном thinking (отправляется как `high` вместо ошибки), доставка `SendMessage` через Claude Desktop от другой сессии, лаг TUI на параллельных субагентах, финальный ответ тиммейта в agent teams, ответы безымянным субагентам, `disableAutoMode` из managed settings.
- **Платформенные release notes** проверены отдельно (`platform.claude.com/docs/en/release-notes/api`) — новых записей после 27.08.2026 нет, окно с прошлого снапшота пустое.

## Оценка источника

Официальный `CHANGELOG.md` репозитория `anthropics/claude-code` — высшая презумпция доверия по `references/source-evaluation.md`. Прямой `raw.githubusercontent.com`-фетч через Bash не пробовался в этот заход (устойчивый паттерн отказа разрешениями окружения в прогонах 08-19…08-28); текст получен через `WebFetch` тем же официальным доменом с явным требованием дословных цитат, свёрен построчно с ответом модели-посредника.

## Проверка безопасности источника

Открытая официальная документация Anthropic, только описание изменений продукта. Исполняемых инструкций или текста, замаскированного под команды агенту, не обнаружено.

## Связи
- [[claude-code]] — новый раздел changelog («Обновление 2.1.251»), дата «Актуально на» сдвинута на 2026-08-31
- [[ai-security-by-design]] — дополнена разделом про пять bypass-фиксов 2.1.251
- [[claude-api-cost-optimization]] — дополнена разделом про видимость спенд-лимита и промпт-кэша
- [[claude-code-changelog-snapshot-2026-08-28]] — предыдущий снапшот в серии
