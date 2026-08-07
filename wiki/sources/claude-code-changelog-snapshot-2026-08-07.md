# Claude Code changelog snapshot 2026-08-07

**Дата загрузки:** 2026-08-07
**Источник:** [raw/sources/claude-code-changelog-2026-08-07.md](../../raw/sources/claude-code-changelog-2026-08-07.md), официальный `CHANGELOG.md` репозитория `anthropics/claude-code` (verbatim, сверено напрямую через `raw.githubusercontent.com`)

## Саммари

Прогон разведчика через три дня после предыдущего снапшота (2026-08-04, покрывал до 2.1.221). Вышли **2.1.222** и **2.1.223** — обе версии продолжают серию фиксов bypass-уязвимостей в permission-анализаторе, уже прослеженную в вики с 2026-07-19/07-25, и добавляют две содержательные новости: удалён экспериментальный **Ultraplan** и найден побег из сэндбокса самих Dynamic Workflows.

## Ключевая находка 1: побег из сэндбокса workflow-скриптов через `import()`

**2.1.223**: *"Fixed workflow scripts being able to use dynamic `import()` to run code outside the workflow sandbox"*. [[dynamic-workflows|Dynamic Workflows]] — тот самый механизм, которым в сессиях этой вики оркестрируются пакетные прогоны (`Workflow`-инструмент, JS-скрипт без доступа к файловой системе/Node API по спецификации) — до этого фикса позволял произвольному workflow-скрипту динамическим `import()` выйти за пределы заявленной песочницы и выполнить код вне неё. Прямое нарушение принципа "простота — враг безопасности" ([[ai-security-by-design]], п. 4) в собственной реализации: явно документированное ограничение ("No filesystem or Node.js API access") имело дыру в самом языке исполнения скрипта, а не в декларируемых правах. Добавлено в [[dynamic-workflows]] и [[ai-security-by-design]].

## Ключевая находка 2: Ultraplan удалён (2.1.222 — `"Removed ultraplan feature"`)

Ultraplan вошёл в вики только как беглое упоминание в официальном Week 15 dev digest ([[claude-desktop-automation-modes]] косвенно, через `code.claude.com/docs/en/whats-new`) — "draft a plan in the cloud from your CLI, review and comment on it in a web editor, then run it remotely or pull it back local", ранний preview с апреля 2026. Отдельной страницы в вики не заводилось. Официальный changelog не даёт причины удаления. Зафиксировано как закрытие незаведённого лида — отдельной правки concept/entity-страниц не требуется, поскольку страницы про фичу не существовало.

## Продолжение серии bypass-фиксов permission-анализатора (2.1.222–2.1.223)

Вики уже трижды фиксировала этот паттерн (07-19, 07-25/07-20-запись про 2.1.214, и общий вывод в [[ai-security-by-design]] — "один и тот же механизм регулярно даёт течь в разных местах"). Новые находки того же класса:

- **Worktree-изоляция не держала git** (2.1.222): *"Fixed worktree-isolated sessions and their subagents being able to run destructive git commands"* — заявленная изоляция `isolation: 'worktree'` (используется, например, в примерах Dynamic Workflows этой вики для параллельной правки файлов) не блокировала деструктивные git-команды до этого фикса.
- **PreToolUse auto-allow bypass в фоновых агентах** (2.1.222): auto-allow правила хуков `PreToolUse` могли обходить ограничения инструментов именно в background agent tasks — сценарий, прямо релевантный автономным прогонам этой вики (Cloud Routines).
- **Bash: команда прячет часть себя** (2.1.223): *"a crafted command could hide parts of itself"* от permission-анализатора; отдельным пунктом — символы табуляции/невидимый Unicode внутри команды маскируют часть от ревью. Тот же класс обфускации, что и обходы через zsh `[[ ]]`-условия (07-19) и длинные команды (07-25), новый конкретный вектор.
- **`bypassPermissions` игнорировал org-политику отключения** (2.1.223): режим `bypassPermissions` в frontmatter агента не уважал организационный запрет на этот режим.

Практический вывод не меняется, только усиливается частотой: правила `allow`/`bypassPermissions`/изоляция worktree в `.claude/settings.json` не статично надёжны, находки продолжают поступать помесячно.

## Безопасность межагентных сообщений: `SendMessage` теперь проверяется auto mode (2.1.222)

*"Improved auto mode safety: messages sent to other agent sessions via `SendMessage` are now evaluated"* — раньше классификатор auto mode проверял действия одного агента, но не содержимое сообщений, которыми агенты обмениваются друг с другом (`SendMessage`, используется, например, в [[agent-teams]] и при возобновлении фоновых воркеров). Прямое расширение защиты от indirect prompt injection (уже описанной для `Agent`-инструмента в 2.1.210, [[ai-security-by-design]]) на межагентный канал связи.

## Малое

- `/teleport`-подсказка в облачных сессиях — как продолжить работу локально.
- `owner/*`-wildcard в `strictKnownMarketplaces`/`blockedMarketplaces` — управление доверенными маркетплейсами скиллов на уровне владельца репозитория, не только точного имени.
- `/review` теперь алиас `/code-review`; повторный вызов `/code-review` без указания effort переиспользует последний введённый уровень.
- `CLAUDE_CODE_DISABLE_1M_CONTEXT` теперь ограничивает 200K вообще все модели с нативным 1M-окном, не только конкретно упомянутые ранее.

## Связанные страницы

- [[claude-code]] — обновлён раздел changelog
- [[dynamic-workflows]] — новый фикс побега из сэндбокса `import()`
- [[ai-security-by-design]] — продолжение серии bypass-фиксов, новый раздел про SendMessage
- [[claude-code-changelog-snapshot-2026-08-04]] — предыдущий снапшот в серии
