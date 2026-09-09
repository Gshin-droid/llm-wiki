# Apache Maka (Incubating) — официальная документация (прочитано 2026-09-09)

Собрано из семи документов репозитория `github.com/apache/maka`, прочитанных напрямую через `raw.githubusercontent.com`. Наводка — пост из инбокса ассистента `raw/inbox-assistant/2026-09-08-вайб-кодинг-если-вам-не-нравится,-что-при-работе-с-ии-истори.md` (`ai-assistant #27`, канал «Вайб-кодинг», 08.09.2026).

Прочитаны: `ARCHITECTURE.md`, `README.md`, `docs/blogs/log-is-the-runtime.md`, `docs/architecture/runtime-resume-architecture.md`, `docs/skill-catalog-policy.md`, `docs/workspace-privacy-context.md`, `packages/cli/README.md`. **Исходники кода не читались — только документация.**

## README: что за проект

«A high-performance agent workspace that keeps a complete record of everything it did.»

Заявленные принципы: log-based runtime (каждое сообщение модели, вызов инструмента и решение — дописываемое событие `RuntimeEvent`); local-first (сессии, настройки и записи остаются на машине); своя модель (облачное API, локальная или совместимый шлюз); единственная исполнительная власть — Desktop/TUI/CLI суть тонкие клиенты одного Runtime Host.

Статус: **incubating** в Apache Software Foundation, лицензия Apache 2.0. Прямое предупреждение: «Data formats, CLI commands, and experimental capabilities may still change.» Платформы: macOS — stable; Windows и Linux — preview, сборки неподписанные. Сборка из исходников: Node.js 22.19+ (CI на 24), npm 11, git, ripgrep для инструмента Grep. Модель не входит в комплект: на первом запуске Settings → Models.

## ARCHITECTURE.md: слои

Runtime Host — единственная исполнительная власть; Desktop, TUI, CLI, боты и подсистема замеров просят у него работу, своего рантайма не держат.

- **Слой 1 — Runtime Event Log:** «the canonical source for model messages, tool calls, tool results, and termination facts». Обрезка и сжатие контекста меняют проекции входа для провайдера, не трогая историю.
- **Слой 2 — SessionManager и AgentRun:** жизненный цикл исполнения; Runtime Host держит допуск клиентов, их возможности и границу публичного протокола.
- **Слой 3 — Agent Graph:** планирование зависимой работы через дочерние сессии, все активации идут через тот же Runtime.
- **Слой 4 — Storage.**

Границы пакетов: `packages/core` (сессия, событие, права, контракты протокола), `packages/storage` (хранилища, SQLite), `packages/runtime` (SessionManager, AgentRun, адаптеры моделей, инструменты, контекст, восстановление), `packages/runtime-host` (единственная исполнительная власть, публичный протокол), `packages/eval`, `packages/cli` (TUI, `maka run`, `maka eval`), `apps/desktop/src/main`.

## docs/blogs/log-is-the-runtime.md

Тезис: применён принцип баз данных «Log Is the Database».

Формула: `Agent State(t) = Project(RuntimeEvents[0...t], policy, runtime configuration)`

Проблема обычных обвязок: при падении процесса восстановление ненадёжно; частичные правки инструментов не имеют безопасной семантики повтора; стотысячетокенные выводы переполняют контекст; и главное — системы «truncate early messages and overwrite them with generated summaries», безвозвратно теряя исходную историю и усложняя отладку и переоценку на моделях покрупнее.

`RuntimeEvent` — типизированная запись. Виды содержимого: `Text`, `Thinking`, `FunctionCall`, `FunctionResponse`, `Error`. Метаданные: `sessionId`, `turnId`, `runId`, `invocationId`, монотонный `event_seq`. Всё в SQLite, таблица `runtime_events`.

Проекции поверх журнала:

- `projectRuntimeEventStoredMessages()` — сообщения и карточки интерфейса
- `buildRuntimeEventModelReplayPlan()` — payload для провайдера: служебные события вырезаются, вызовы и ответы спариваются
- `classifyRuntimeEventTerminalFact()` — чем кончился Run: успех, отказ, обрыв
- `buildContinuationReplayPlan()` — какой префикс переносится в новый Run после падения

Сжатие: контрольная точка — материализованное представление раннего префикса плюс дословный свежий хвост. Канонический журнал строго append-only, меняется только логика проекции. Контрольная точка записывает покрытый префикс, границу завершения и отпечатки целостности. Дословно: «summaries are lossy representations that influence future decisions, compaction projections must be verified and persisted durably before being exposed to the model». Сохраняется переиспользование KV-кэша: системные промпты и схемы не меняются, следующие запросы дописывают токены.

Обрезка больших результатов: вывод откладывается в хранилище, в контекст ставится «lightweight placeholder» с метаданными и ручкой доступа; чтение — постранично. Порядок: **«archive first, placeholder second»**. Канонический журнал сохраняет исходный вывод, заглушки живут только в проекции для модели.

Инварианты:

1. **Детерминизм** — та же начальная точка плюс тот же упорядоченный журнал дают то же состояние на любом узле
2. **Долговечность** — зафиксированный префикс и снимки целы, восстановление детерминировано
3. **Восстановление** — чтение истории «through immutable prefix windows bounded by a `highWater` mark», криптографические отпечатки привязывают восстановление к проверенным отрезкам
4. **Безопасность инструментов** — при неопределённой идемпотентности «the runtime blocks continuation rather than executing an unsafe blind retry»
5. **Сохранность фактов** — канонический журнал не переписывается, меняются только способы его читать

Признанный размен: append-only «does not remove complexity. It moves complexity away from maintaining a mutable current state and into constructing appropriate views over stable history». Цена — рост журнала, версионирование проекций, жизненный цикл архивов. Выгода — понятные границы восстановления, полный аудит и возможность переосмыслить историю по мере смены моделей.

## docs/architecture/runtime-resume-architecture.md

Четыре объяснения, когда после перезапуска нет результата инструмента:

1. инструмент не запускался;
2. запустился, но файл не записал;
3. файл содержит ожидаемый результат, но итог не зафиксирован;
4. файл записан и затем изменён пользователем или внешним процессом.

Система отказывается предполагать успех и отказывается автоматически повторять — любой из двух выборов создаёт ложную историю.

Пять правил: возобновление создаёт новое исполнение, а не оживляет старый сокет, промис или процесс; `RuntimeEvent` — единственный канонический источник фактов восстановления; отсутствующий результат не есть отказ и не доказывает, что инструмент не работал; когда безопасность не доказуема — система паркуется (`park`); идентичность рабочей области доказывает логическую идентичность, а не содержимое файлов.

Границы фиксации:

- **T1 (диспетчеризация)** — одна короткая транзакция SQLite: проверяется или фиксируется канонический вызов, пишется невидимое модели событие `actions.toolDispatch`, пересчитывается `canonicalArgsHash`, создаются журнал операции и проекции. «If T1 fails, the tool implementation must not execute.»
- **T2 (итог)** — после внешнего эффекта, другая короткая транзакция: проверяется идентичность операции, фиксируется событие-ответ, обновляются журнал и проекция. «The result cannot reach the model before T2 succeeds.»
- **Терминальное событие** — Run завершён, только когда его терминальное событие долговечно. «There is no second commit window for a crash to land between.»

`RecoveryResolver` раскладывает каждую операцию по шести состояниям: `completed` (переиспользовать, никогда не перезапускать), `definitely_not_dispatched`, `indeterminate` (блокирует продолжение, требует сверки), `completed` из recovery bundle, `parked` (постоянная остановка v1, второй попытки нет), `corruption` (сирота, дубль или конфликт идентичности — fail closed).

Частичные ответы модели: «discard mutable partials; keep only paired function calls and responses; never feed an unresolved call back to the provider».

Идемпотентность: точный повтор обязан совпасть побайтово и по идентичности; отдельные писатели на T1, T2 и recovery bundle; строки журнала ссылаются на своё событие; конфликтующий повтор, факты-сироты и дрейф идентичности отвергаются.

Чего **не** обещают: восстановить старый поток провайдера, промис или указатель инструкции; ровно-однократность для произвольного Bash, удалённых API и дочерних процессов; автоматическое улаживание реального эффекта T1-без-T2; использование UUID рабочей области как доказательства содержимого файлов; побитовое воспроизведение проводного формата провайдера; самоотчёт модели вместо `RuntimeEvent` или факта на диске; одинаковые доказательства долговечности на Windows и POSIX.

Файлы: `packages/core/src/runtime-event.ts`, `tool-ledger-scanner.ts`, `tool-recovery-bundle.ts`; `packages/storage/src/sqlite-runtime-schema.ts`, `sqlite-runtime-store.ts`, `workspace-identity.ts`; `packages/runtime/src/recovery-resolver.ts`, `runtime-resume.ts`, `tool-runtime.ts`, `runtime-kernel.ts`.

## ARCHITECTURE.md, раздел Eval

Эксперимент = «benchmark + executor + subjects + tasks + repetitions». Ячейка = «task × repetition × subject».

Различаются три вещи: **repetition** (новая экспериментальная выборка), **infra retry** (замена попытки для той же ячейки) и **continuation** (внутреннее поведение Runtime Host). A/B — просто эксперимент с двумя ветками; Harbor и Pier — адаптеры исполнителя, а не отдельные процессы.

Ядро результата: «score, normalized usage, attributable cost, duration, status or failure reason, and artifacts». При нескольких попытках: **«the earliest valid attempt is authoritative; operators cannot choose a preferred outcome».**

## docs/skill-catalog-policy.md

Порядок поиска строгий: проектные пути → пути совместимости рабочей области → пользовательские; внутри каталога — по отображаемому имени; первый найденный дубль побеждает, остальные остаются в описи для осмотра.

Пять детерминированных фильтров отбора: порядок источников; исключить отключённые; исключить те, чьи явные `required-tools`/`required-capabilities` недоступны; сначала закреплённые пользователем; добавлять, пока не исчерпан бюджет каталога модели.

Бюджет: **«2% of its context window, clamped to 4,000–8,000 estimated tokens»** (4 символа на токен). Для моделей с неизвестным окном — `MAX_SKILLS_PROMPT_CHARS = 18000`. Когда бюджет не вместил записи, «the prompt contains only a constant-size count, not an unbounded list of ids».

Тела скиллов в системный промпт не попадают: грузится ограниченный каталог, полные инструкции подтягивает read-only инструмент `Skill` при совпадении задачи.

Доверие: «Bundled provenance is not an execution authority over local workspace content». Удаление скилла из комплектных каталогов прекращает распространение, но не удаляет локальные копии; валидный включённый локальный скилл остаётся вызываемым по обычным правилам прав и возможностей хоста. Явный вызов: порядок разрешения `ref` → `id` → `name`; запрос более чем на 50 различных скиллов падает с `too_many_requests`.

## docs/workspace-privacy-context.md

`WorkspacePrivacyContext` — нарочно вырожденный контракт: одно поле `incognitoActive: boolean`.

Власть над состоянием только у Runtime Host; отрисовщики не устанавливают истину, а лишь просят изменить и показывают. Авторитетное состояние — `packages/core/src/runtime-policy.ts`, `privacy.incognitoActive` по умолчанию `false`; проверка — `validateWorkspacePrivacyContext()` в `packages/core/src/incognito.ts`; настройки правятся из `apps/desktop/src/renderer/settings/general-settings-page.tsx`.

Правило: **«Boundaries that cannot resolve a valid authoritative context must fail closed»** — валидатор отвергает некорректный ввод, а не превращает отсутствующие или неверные данные в `false`.

Обязанность потребителя: «`incognitoActive: false` only means that incognito mode did not block the operation» — свои настройки, права и правила хранения применяются отдельно.

**Признанное самими авторами отклонение:** гейт уведомлений о завершении прогона (`apps/desktop/src/main/notifications-ipc-main.ts`) читает устаревшие значения `privacy.incognitoActive` из локальных настроек, потому что патчи приватности до того хранилища не доходят, — и может поднять уведомление с данными сессии.

## packages/cli/README.md

Два dist-тега: `maka-agent@nightly` (полный CLI) и `latest` (alpha-заглушка: только `doctor`, справка и версия). Предупреждение: не делать `npm update --global maka-agent` — он идёт за `latest` и может понизить функциональность.

- Интерактивно: `maka` из папки проекта; `/setup` меняет провайдеров, `/model` — модель.
- Неинтерактивно: `maka run "<задача>"`.
- Права: по умолчанию спрашивает перед привилегированными операциями; флаг `--yolo` даёт полный доступ к файлам и сети — «use only in controlled environments».
- Замеры: `maka eval run experiment.json --out .maka-eval/run-001`.
- Удалённый Runtime Host: `maka runtime-host setup --principal <имя> --preset terminal-client`, далее `maka runtime-host service check-update|update-policy|reconcile-update|uninstall`.
- Сессии и учётные данные — в профильных папках платформы; удаление пакета локальные данные не стирает.
