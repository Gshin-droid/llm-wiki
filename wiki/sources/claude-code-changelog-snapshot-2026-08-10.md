# Claude Code changelog snapshot 2026-08-10

**Дата загрузки:** 2026-08-10
**Источник:** [raw/sources/claude-code-changelog-2026-08-10.md](../../raw/sources/claude-code-changelog-2026-08-10.md), официальный `CHANGELOG.md` репозитория `anthropics/claude-code` (verbatim, сверено напрямую через `raw.githubusercontent.com`)

## Саммари

Прогон разведчика через три дня после предыдущего снапшота (2026-08-07, покрывал до 2.1.223). Вышли **2.1.224**, **2.1.225** и **2.1.226**. Главная новость релиза — **self-hosted environments** и **cross-session `SendMessage`/`ListAgents`**: второе — ровно тот механизм, который виден прямо в системных инструкциях автономных сессий этой вики (`ListAgents`/`SendMessage` — deferred-инструменты, `mcp__Claude_Code_Remote__*` — управление сессиями), задокументированный впервые именно этим релизом. Также релиз **отменяет** ранее задокументированный в вики факт: лимит 200 субагентов на сессию убран для долгоживущих сессий.

## Ключевая находка 1: cross-session `SendMessage`/`ListAgents` (2.1.224–2.1.225)

*"Added cross-session `SendMessage`: Claude Code sessions can now message each other, on any of your machines, with `ListAgents` to discover them (macOS and Linux)"* — до этого релиза `SendMessage`/`ListAgents` (уже упоминались в вики как механизм [[agent-teams|Agent Teams]] и межагентного канала, см. [[ai-security-by-design]]) работали только внутри одной сессии/её субагентов. Теперь это полноценный межмашинный протокол: любая сессия Claude Code на любой из машин пользователя может достучаться до любой другой, `ListAgents` перечисляет их. 2.1.225 добавляет асимметрию для Remote Control-сессий — с ними теперь можно начать разговор по имени, а не только отвечать на входящее сообщение.

Это прямое дополнение к безопасности межагентного канала, уже описанной в [[ai-security-by-design]] (auto mode проверяет `SendMessage`, 2.1.222): теперь тот же канал охватывает не только сессии одной машины, а весь парк. Отсюда же — новые настройки **`crossSessionInbound`/`dialogExpiry`** (2.1.224): входящие межсессионные сообщения к сессии, запущенной с обойдёнными разрешениями (`bypassPermissions`), теперь по умолчанию не доставляются молча, а ждут подтверждения пользователя; сообщения к обычным сессиям доставляются как раньше. Прямое применение принципа "минимальные привилегии" ([[ai-security-by-design]], п. 1) к новому расширенному каналу: чем шире охват `SendMessage` (была одна машина — стал весь парк), тем важнее барьер именно там, где сессия и так работает без подтверждений.

Дополнено в [[claude-desktop-automation-modes]] и [[agent-teams]].

## Ключевая находка 2: self-hosted environments (2.1.224)

*"Added self-hosted environments: `claude self-hosted-runner` turns your own machines or containers into a place Claude Code web, mobile, and desktop sessions can run, on Team and Enterprise plans"*. Новый режим деплоя — рядом с уже описанными в вики облачными Cloud Routines ([[claude-desktop-automation-modes]]) появляется возможность прогонять веб/мобильные/десктопные сессии Claude Code на собственной инфраструктуре пользователя, а не только на managed-инфраструктуре Anthropic. Отличается от [[claude-managed-agents|Claude Managed Agents]] — там self-hosted sandboxes это опция API-фреймворка для агентов, здесь — тот же принцип, но для самого Claude Code как продукта. Официальная документация не читалась целиком (за пределами changelog), поэтому механика (аутентификация раннера, `--base-dir`, к какому типу окружений это ближе — Local или Cloud Routines по таксономии [[claude-desktop-automation-modes]]) не разбирается — открытый вопрос, добавлен пункт в `wiki/gaps-backlog.md`.

Замечание 2.1.225: *"Fixed `claude self-hosted-runner` registering and then failing every session when `--base-dir` cannot be created or written; it now exits at startup with a clear error"* — фича настолько свежая, что в том же спринте чинится собственный баг-фикс раннера.

## Находка 3: расширение маскирования кредов в сэндбоксе (2.1.224)

Дополнение к `sandbox` `mode: "mask"`, задокументированному в [[claude-code-changelog-snapshot-2026-08-04]] (2.1.221) и разобранному в [[claude-code]] (раздел "Permissions и .claudeignore"). Три новых параметра: **`extract`/`onExtractNoMatch`** — точечное маскирование по regex внутри структурированных env-значений (не весь секрет целиком), **`decode: "jwt"` с `maskClaims`** — маскирование конкретных claims внутри JWT, а не токена целиком, **`awsPairs`/`sigv4`** — сэндбокс сам переподписывает AWS SigV4-запросы, не давая команде увидеть исходные ключи. Все три требуют `network.tlsTerminate` и разрешены только из user/managed/`--settings` — та же граница, что и у `sandbox.filesystem.disabled` ([[claude-code-changelog-snapshot-2026-07-22]]): проектный `.claude/settings.json` не может сам себе ослабить или усилить эту настройку. Прямое продолжение принципа минимальных привилегий — инструменту не нужно видеть секрет целиком, чтобы им пользоваться, теперь это верно и для структурированных значений (JWT, AWS-подписи), а не только для файлов-сентинелов.

## Устаревший факт: лимит 200 субагентов на сессию убран (2.1.224)

**Противоречит ранее записанному факту.** [[ai-security-by-design]] и [[claude-code]] документировали (с 2026-07-19, [[claude-code-changelog-snapshot-2026-07-19]]) лимит `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION` = 200 суммарно за сессию как действующий предохранитель от runaway-расхода ресурсов. Changelog 2.1.224: *"Removed the 200-subagent-per-session spawn cap; long-running sessions no longer refuse new agents (concurrency and depth limits still apply)"* — лимит на суммарное число субагентов за сессию убран целиком; остаются в силе только лимит на одновременно бегущих (20 по умолчанию, `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`) и лимит вложенности (3 уровня по умолчанию). Причина в самой формулировке — "long-running sessions no longer refuse new agents": лимит на 200 суммарных бил по долгоживущим сессиям (`/loop`, автономные рутины вроде этой вики), а не по факту одновременного расхода ресурсов, который и так ограничен параллельным лимитом. Обновлены [[ai-security-by-design]] и [[claude-code]] — старое значение помечено устаревшим, не удалено.

## Малое

- **Gateway spend-limit** (2.1.225) — сообщение о достижении лимита расходов через gateway теперь называет сам лимит, время сброса и сообщение оператора (требует gateway версии 2.1.225+).
- **Workspace trust prompt для `claude agents`** (2.1.225) — команда `claude agents` (запуск фоновых агентов) теперь тоже спрашивает доверие к недоверенной директории, как уже делает `claude` — закрывает асимметрию, а не новый механизм.
- **Feedback survey transcript share включает системный промпт** (2.1.224, с согласия пользователя) — при шаринге транскрипта через форму фидбека теперь можно (opt-in) приложить системный промпт последнего запроса — включая содержимое `CLAUDE.md`, определения инструментов и параметры модели; секреты редактируются как раньше, поля срезаются первыми при превышении размера. Не публикация в смысле раздела "Личное не публикуется" в `CLAUDE.md` этой вики (это канал к Anthropic, не в открытый репозиторий), но стоит держать в голове при шаринге фидбека из сессий, где `CLAUDE.md`/skills содержат чувствительные детали.
- Focus view (VSCode) — фикс сворачивания to-do листа и контекста незакрытого вопроса.
- Bash tool description теперь всегда явно уточняет, что вывод команды виден модели, но не обязательно пользователю.
- Плагины: новый источник `archive` — установка из zip по HTTPS без git/npm, с опциональным SHA-256 pinning.

## Связанные страницы

- [[claude-code]] — обновлён раздел changelog, исправлен лимит субагентов
- [[claude-desktop-automation-modes]] — дополнен cross-session SendMessage/self-hosted environments
- [[agent-teams]] — дополнен межмашинный SendMessage
- [[ai-security-by-design]] — исправлен лимит субагентов, дополнено маскирование кредов
- [[claude-code-changelog-snapshot-2026-08-07]] — предыдущий снапшот в серии
