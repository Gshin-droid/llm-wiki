# Индекс

Каталог всех страниц вики. Обновляется при каждой загрузке источника или синтезе.

## Entities
_(люди, компании, инструменты)_

- [[andrej-karpathy]] — автор метода/гиста, лежащего в основе паттерна персональной вики
- [[claude-code]] — CLI-агент Anthropic, движок этой вики
- [[obsidian]] — markdown-редактор с графом связей, IDE для просмотра вики
- [[obsidian-web-clipper]] — расширение браузера для сохранения статей; установлено и используется с 2026-07-07 (31 файл в `raw/web-clipped/`)
- [[antigravity-ide]] — альтернативная IDE для запуска Claude Code (не используется)
- [[pinecone]] — векторная БД для масштабирования (не используется)
- [[notebooklm]] — RAG-система Google, контраст с паттерном этой вики (не используется)
- [[cursor]] — AI-native IDE, альтернатива Claude Code
- [[multica]] — организация, публикует репозиторий с гайдлайнами Карпати; продукт Multica — open-source self-hostable платформа делегирования задач 20 coding-агентам (допроверка 08-17)
- [[ii-mastodont]] — автор видео-разбора метода Карпати (18М просмотров)
- [[claude-projects]] — функция Claude.ai: память/контекст под конкретную роль
- [[claude-skills]] — переносимые "умения" для Claude
- [[claude-cowork]] — режим "агент за компьютером" (Desktop, с 08-2026 также web/mobile)
- [[supabase]] — Backend-as-a-Service для вайбкодинг-проектов
- [[openrouter]] — агрегатор нейросетевых моделей
- [[ai-proryv]] — автор видео про 5 уровней владения Claude
- [[dmitry-bereznitsky]] — разработчик, автор видео про карьеру и AI-кибербезопасность
- [[metics-media]] — канал про сайты за $10k через Claude Code
- [[appbusters]] — школа вайбкодинга
- [[qaisar-kurmangaliev]] — автор полного курса по Claude
- [[neiroprosveshchenie]] — автор техники "просмотра" видео через Claude
- [[memora]] — MCP-сервер памяти для агентов: цепочки замещения, детерминированные выжимки с якорями на исходные записи; разобран как чужая реализация нашей же рамки, ставить не планируется
- [[mem0]] — memory-фреймворк для агентов на API
- [[zep-graphiti]] — temporal knowledge graph для памяти
- [[letta]] — memory-as-OS фреймворк (бывший MemGPT); допроверка 08-10: флагман сместился в coding-агента с памятью (Letta Code)
- [[graphify]] — локальный граф архитектуры кода
- [[maxim-bashkardinov]] — автор гайда Obsidian+Claude через MCP для документации проекта
- [[shubin-danila]] — автор обзора ландшафта LLM-памяти
- [[sonny-huynh]] — автор паттерна "второй мозг" с ежедневными воркфлоу
- [[nikita-vels]] — автор справочника из 30 практических концептов Claude Code
- [[claude-statusline]] — statusline-скрипт для Claude Code CLI (лимиты, директория, git-ветка)
- [[claude-agent-sdk]] — библиотека Python/TypeScript для встраивания agent loop Claude Code в свои приложения
- [[woome-ai]] — автор видео про контент-фермы Claude Code + Дзен
- [[opencode]] — open-source мультипровайдерный CLI-агент для кодинга, альтернатива Claude Code
- [[zproger]] — автор обзора OpenCode
- [[vladilen-minin]] — автор кейсов GSD/Superpowers
- [[gsd-get-shit-done]] — spec-driven агентский фреймворк полного SDLC, мультихост; допроверка 08-12: проект переехал в GSD Core (`open-gsd/gsd-core`), старый репозиторий архивирован
- [[superpowers]] — TDD-ориентированный набор скиллов с автообнаружением, лёгкая альтернатива GSD; автор Jesse Vincent (obra), 270k+ звёзд, 11 хостов установки (допроверка 08-12)
- [[nikita-efimov]] — автор разбора автоматизаций Claude Desktop
- [[prostodevops]] — DevOps-образовательный канал
- [[claude-managed-agents]] — hosted agent harness Anthropic: agent/environment/session/events, память/мультиагентность/self-hosted sandboxes поверх Claude API; допроверка 08-19/08-20 — production-паттерн (webhooks), memory stores, human-in-the-loop и мультиагентная координация по официальным cookbook'ам
- [[web3nity]] — автор методологии «презентация через ИИ-агента» (YouTube + Telegram)
- [[context7]] — сервис/MCP-сервер Upstash с актуальной документацией библиотек; установлен 2026-07-27
- [[mattpocock-skills]] — пак скиллов Matt Pocock: пайплайн grilling→spec→tickets→implement, tracer-bullet нарезка; установлен 2026-07-27
- [[exa]] — поисковый API + официальный MCP для ИИ-агентов, neural search; оценён по бэклогу, не установлен
- [[marina-mogilko]] — предприниматель, автор выступления про пять уровней внедрения ИИ в бизнес
- [[bohomolov-lab]] — автор серии Inside Claude (YouTube + Telegram), разбор архитектуры многофайлового скилла
- [[comrad404]] — автор канала обзоров ИИ-инструментов; разбор понятия «харнес», необычно добросовестный для формата
- [[paragonzone]] — канал про ИИ-инструменты; разбор безопасности вайбкодинг-проектов на собственном стенде
- [[freecad]] — открытый параметрический CAD-редактор; площадка практического кейса MCP с визуальной обратной связью (скриншот вьюпорта)
- [[make-form]] — автор туториала «Claude + FreeCAD через MCP»

- [[deepseek-harness]] — открытый (MIT) агентный харнес DeepSeek: сменны все компоненты, включая цикл агента; полная трасса рассуждений отдаётся пользователю, а не прячется; статус developer preview, подписка Claude в него не переносится

- [[mitchell-hashimoto]] — сооснователь HashiCorp, ввёл термин «харнес-инжиниринг» (февраль 2026) и принцип «ошибка должна стать структурно невозможной — кодом, а не промптом»

## Concepts
_(идеи, модели, принципы)_

- [[persistent-wiki-pattern]] — вики вместо RAG: накопление знаний вместо повторного извлечения (+ ограничения на масштабе и по числу писателей)
- [[agent-memory-five-questions]] — пять решений, которые память агента принимает за тебя дефолтами: синтез на входе или на запросе, кто пишет и что при конфликте, чем факт привязан к источнику, как узнать что память соврала, что канон и что кэш; почему заброшенная вики стареет как дезинформация, а не как пробел
- [[ingest-query-lint]] — пять операций ведения вики (Ingest/Query/Project/Practice/Lint); Query не ограничен markdown-формой по первоисточнику, Lint разделён на еженедельный механический и ежедневный содержательный ритм
- [[llm-coding-guidelines]] — четыре принципа Карпати против типичных ошибок LLM в коде
- [[hybrid-memory-architecture]] — 4-элементная архитектура: CLAUDE.md + Obsidian + Pinecone + NotebookLM
- [[one-vault-one-project-rule]] — не смешивать темы в одном vault'е (открытый вопрос для этой вики)
- [[five-levels-of-claude-mastery]] — модель зрелости использования Claude, от поисковика до автономной системы
- [[seven-signs-of-old-junior]] — карьерная стагнация разработчиков, включая ИИ-зависимость
- [[10k-website-checklist]] — воркфлоу немассового веб-дизайна через Claude Code
- [[vibecoding-full-workflow]] — сквозной процесс разработки приложения через ИИ-агента
- [[ai-security-by-design]] — как ИИ изменил кибербезопасность и принципы защиты (безопасность самого агента)
- [[vibecoding-app-security]] — безопасность того, что собрал агент: пять классов дыр с самопроверкой за 10 минут, деградация кода при итерациях (+37,6% после пяти), граница «свои данные / чужие», потолок скилла-ограждения
- [[claude-watch-skill]] — Claude анализирует кадры видео по тайм-кодам, не только транскрипт
- [[llm-memory-landscape]] — три разные задачи "памяти для ИИ": о пользователе, о коде, о знаниях
- [[project-documentation-vault-pattern]] — Obsidian-вики как документация кодового проекта, альтернатива персональной вики
- [[second-brain-daily-workflows]] — ежедневные продуктивностные воркфлоу Obsidian+Claude (не про накопление знаний)
- [[ai-data-layer-core-files]] — четыре core-файла о себе (досье, tone of voice, анти-ИИ, конституция), метод сбора через интервью и граница делегирования агентам
- [[context-engineering-claude-5]] — официальные правила Anthropic под поколение 5: правила → суждение, примеры → интерфейс, что живёт в CLAUDE.md, что в скиллах, что в references; и где эти правила НЕ применимы
- [[skill-authoring-practical-rules]] — как создавать Skills вместо промтов: description-триггер, три слоя, композиционность, итеративное накопление, гранулярность против ходов агента (замер 2026-07-29), границы работы скилла
- [[mcp-model-context-protocol]] — открытый протокол подключения агентов к внешним сервисам: архитектура, крупнейшая ревизия спецификации 2026-07-28 — вышла финалом 28.07 (stateless core, MRTR, MCP Apps, Tasks, CIMD)
- [[claude-memory-tool]] — официальный файловый инструмент памяти Claude API: just-in-time context retrieval, six-команд протокол, multi-session паттерн
- [[claude-artifacts]] — интерактивная веб-страница как носитель результата сессии: «снимок работы, а не приложение», MCP-коннекторы зрителя, ограничения публикации
- [[agent-harness]] — обвязка между моделью и работой: агент = модель + харнес; восемь частей, пять болей и чем они чинятся, внутренний/внешний харнес, кейс +13,7 пункта на неизменной модели
- [[long-running-agent-harness]] — два харнесса Anthropic для долгоживущих агентов: три примитива многосессионного прогресса (Default-FAIL Contract, Fresh-Context Evaluator, Agent-Maintained Handoff) + отдельный GAN-inspired Planner–Generator–Evaluator для автономной генерации целых приложений
- [[agent-teams]] — команды агентов Claude Code: когда team вместо субагентов, размеры, failure modes, security-модель
- [[ai-content-farming-workflow]] — техника контент-фермы через ИИ-агента: скрапинг конкурентов, "система" файлов вместо промта, параллельная генерация
- [[agentic-sdlc-frameworks]] — GSD и Superpowers: агентские фреймворки, автоматизирующие весь SDLC, а не только код
- [[claude-desktop-automation-modes]] — четыре способа автоматизации через Claude Desktop: Cowork Scheduler, Local/Cloud Routines, `/loop`
- [[cloud-computing-fundamentals]] — основы облачных вычислений: NIST-определение, IaaS/PaaS/FaaS/SaaS, специфика РФ (152-ФЗ)
- [[dynamic-workflows]] — скриптовая оркестрация десятков-сотен субагентов в Claude Code: примитивы agent/pipeline/parallel, quality-паттерны (adversarial verify, judge panel, loop-until-dry), место среди субагентов/skills/agent teams
- [[ai-presentation-workflow]] — методология презентаций через ИИ-агента: смысл→визуал→сборка, нарратив-гейт до дизайна, референсы→правила; реализована как 4 локальных скилла
- [[vibecoding-task-selection]] — отбор задач для вайбкодинга: рамка «четвёртый вариант» (руками/сотруднику/подрядчику/завайбкодить), критерии повторяемости и своей экспертизы, каталог из 11 типовых инструментов
- [[geo-ai-answer-visibility]] — GEO: видимость в ответах ИИ-поисковиков — общий механизм (текстовый краулер + robots.txt) и асимметрия видео (Gemini/YouTube против текстовых краулеров ChatGPT/Perplexity)
- [[claude-api-cost-optimization]] — официальный чеклист экономии стоимости вызова Claude API (кэш, токены, batch, модель) — рычаг, дополняющий маршрутизацию между моделями

- [[spatiotemporal-composability]] — обратимые компоненты: почему харнес умеет только расти и что даёт возможность снимать плагин без следа; что из идеи переносится на чужой харнес, а что нет

- [[invariant-vidno-znachit-zapisano]] — «всё, что попадает в запрос к модели, обязано быть восстановимо из журнала»: вторая половина правила о тихом успехе, почему проверка охвата журнала сделана отчётом, а не сторожем, и что переведёт её в код

- [[verification-three-levels]] — лестница проверок агента (инварианты в коде → замеры на эталонах → человек), правило спуска на уровень ниже, три вопроса «инвариант или эвристика», почему заблокированный правильный ответ хуже пропущенной ошибки, чеклист к своей обвязке

## Sources
_(саммари загруженных источников)_

### ⭐ Топ-находки
_(отбирает автономный разведчик практического материала — см. `CLAUDE.md` → операция Ingest.)_
- [[claude-cookbook-cost-optimization]] — официальный notebook Anthropic: семишаговый чеклист снижения стоимости агента на Claude API с измеренной экономией (кэш до −54%) на реальном примере, применим прямо в шлюзе [[delegirovanie-deshevym-modelyam]]
- [[claude-code-changelog-snapshot-2026-07-15]] — hardened Agent tool против prompt injection, `/doctor` как полноценный чекап, защита от фальшивых "одобрений пользователя" в транскрипте (тот же механизм виден в системных уведомлениях этого прогона)
- [[claude-managed-agents-overview]] — официальный API для агентов в managed sandbox-инфраструктуре, закрывает пробел, явно отмеченный в claude-agent-sdk.md
- [[claude-code-dynamic-workflows-docs]] — скриптовая оркестрация субагентов (Dynamic Workflows), закрывает пробел: механизм существовал с мая 2026, но не имел отдельной страницы; ровно тот инструмент, которым устроен встроенный скилл deep-research
- [[claude-code-changelog-snapshot-2026-07-19]] — Artifacts вызывают MCP-коннекторы зрителя при открытии страницы (ровно механизм скилла `artifact-capabilities`, доступного в сессиях этой вики), плюс лимиты на runaway-циклы (WebSearch/субагенты), `EndConversation`, серия фиксов bypass-уязвимостей в permission-анализаторе
- [[claude-opus-5-launch]] — Claude Opus 5 (24.07.2026) стал дефолтной моделью Claude Code v2.1.219: та же цена, что у Opus 4.8, thinking по умолчанию (breaking change для effort xhigh/max), Dynamic Workflows получили официальный дефолт medium/<15 агентов — подтверждённый напрямую в системном промпте сессий этой вики
- [[anthropic-context-engineering-claude-5]] — первоисточник Anthropic: >80% системного промпта Claude Code вырезано без потери качества на evals; прямо задевает личный `~/.claude/CLAUDE.md` и скиллы пользователя — что оставить, что сжать в принцип, что увезти в скилл (разбор кандидатов — [[claude-code-practices]], п. 6а)
- [[claude-code-migration-case-studies-2026-07]] — Dynamic Workflows на реальном масштабе: Bun (Zig→Rust, ~1M строк за 11 дней), Klarna (security-аудит), CyberAgent (hardening) — воспроизводимая 4-фазная архитектура + честная критика (adversarial review агентами ≠ человеческое ревью)
- [[mcp-2026-07-28-spec-final]] — финальный релиз крупнейшей ревизии MCP вышел точно в срок (28.07.2026): stateless core подтверждён, плюс новое против RC — Multi Round-Trip Requests, header-based routing, кэшируемые list-ответы, CIMD вместо Dynamic Client Registration; закрывает открытый статус на [[mcp-model-context-protocol]], актуально для уже установленных MCP-серверов вики (Context7)
- [[claude-code-routines-docs]] — официальная документация Cloud Routines и `/loop`/scheduled tasks: точная таблица трёх способов расписания, self-paced `/loop` через `ScheduleWakeup`, `loop.md`, и впервые названный/датированный (v2.1.214) security-механизм триггера рутины как не-живого подтверждения пользователя — дословно совпадает с тем, что видно в системных инструкциях автономных прогонов этой самой вики
- [[claude-code-changelog-snapshot-2026-08-04]] — changelog v2.1.221 уточняет git-поведение фоновых сессий: draft PR только когда задача этого требует, следование git-инструкциям `CLAUDE.md` — официальная параллель дисциплине «инкрементальный коммит и пуш» этой самой вики; плюс `sandbox` `mode: "mask"` для credential-файлов и `prompt-audit` для скилла `claude-api`
- [[claude-code-changelog-snapshot-2026-08-07]] — changelog v2.1.222–2.1.223: побег из сэндбокса Dynamic Workflows через `import()` (прямо касается механизма, которым эта вики оркеструет пакетные прогоны), Ultraplan удалён, продолжение серии bypass-фиксов permission-анализатора (worktree-изоляция не держала git, `PreToolUse` auto-allow bypass в фоновых задачах), auto mode теперь проверяет и `SendMessage`
- [[claude-code-auto-mode-default]] — официальная документация: с 14.08.2026 auto mode становится дефолтным режимом разрешений для новых сессий на Pro/Max/Team вместо Manual; не переопределяет уже заданный пользователем или организацией дефолт
- [[claude-code-changelog-snapshot-2026-08-13]] — changelog v2.1.227–2.1.231: hardening скиллов, синхронизированных с claude.ai (больше не перекрывают локальные команды, тело не исполняет `!`/`@` на машине пользователя), сэндбокс IPv6 fail-closed, `/commit-push-pr` больше не авто-одобряет опасные git-флаги, self-hosted runner получил server-supplied хуки

- [[berezhnitsky-agent-memory-lies]] — пять вопросов к памяти агента и почему вики врёт незаметно: заброшенная структурная база стареет пробелами, заброшенная вики — порчей пересказа; прямо по этой вики, два правила из него внесены в `CLAUDE.md` 2026-08-07 (якорь к источнику, еженедельная сверка страницы с сырьём)
- [[chroma-context-rot]] — допроверка по официальному репозиторию авторов: точность GPT-4.1 падает со 100% до 18% уже на 10 000 токенах контекста (пример из первых рук, не пересказ), два порядка раньше заявленного лимита окна
- [[claude-code-self-hosted-environments-docs]] — официальный практический гайд (concept + quickstart): environment/runner/session, раннер запирается на одного пользователя, сеть только исходящая — но инференс модели всё равно у Anthropic, self-hosting не открывает Bedrock/GCP/Foundry/LLM gateway; закрывает пробел, открытый тем же днём changelog-снапшотом

### Все источники
- [[claude-cookbook-managed-agents-versioning-monitoring]] — официальные notebook'ы Claude Cookbooks (`managed_agents/`): закрепление версии агента при создании сессии (`agent={"type": "agent", "id": ..., "version": N}`) против неявной последней версии, откат через смену номера; живой мониторинг мультиагентной команды — дельты best-effort, гарантированно полный текст только в финальном `agent.message`
- [[claude-cookbook-managed-agents-iterate-explore]] — официальные notebook'ы Claude Cookbooks (`managed_agents/`): канонический паттерн стриминга событий сессии, `sessions.resources.add()` — подгрузка ресурса посреди уже идущей сессии
- [[claude-code-changelog-snapshot-2026-08-25]] — официальный changelog Claude Code (в. 2.1.241–2.1.245): раздельный TTL промпт-кэша (`promptCacheTtl`/`subagentPromptCacheTtl` — час на основном диалоге, 5 минут на субагентах), разбивка `/usage` по `/loop`-циклам; платформенные release notes за то же окно проверены и пусты
- [[makeform-freecad-mcp-tutorial]] — туториал: подключение Claude к FreeCAD через сторонний MCP-сервер; цикл с визуальной обратной связью (скриншот вьюпорта), обработка неоднозначных промптов, честно названный риск (закрытие несохранённых документов без подтверждения)
- [[bereznitsky-harness-engineering]] — харнес-инжиниринг на живых агентах из продакшена: происхождение термина у Хашимото, четыре функции OpenAI, семь слоёв академической таксономии, три уровня проверки; четыре опорных утверждения проверены по первоисточникам и подтвердились
- [[claude-cookbook-managed-agents-issue-outcome-grader]] — официальные notebook'ы Claude Cookbooks (`managed_agents/`): issue→PR workflow с recovery-паттернами (чтение диагностики вместо слепого повтора), outcome grader — первое раскрытие примитива Outcomes (изолированный grader с чистым контекстом, `user.define_outcome`, grade-and-revise цикл)
- [[claude-cookbook-managed-agents-hitl-multiagent]] — официальные notebook'ы Claude Cookbooks (`managed_agents/`): human-in-the-loop через два кастомных тула (`decide()`/`escalate()`), мультиагентная координация (`multiagent: {type: coordinator}`, advisor-примитив, toolset-скоуп по ролям); полный список 16 гайдовых + 3 applied notebook'ов подтверждён поимённо
- [[deepseek-harness-zproger-review]] — обзор DeepSeek Harness: демонстрация полной трассы агента в интерфейсе; факты сверены отдельно, четыре расхождения с первоисточниками зафиксированы (звёзды, счёт плагинов, Cordis, непроговорённый статус preview)
- [[claude-code-changelog-snapshot-2026-08-19]] — официальный changelog Claude Code (в. 2.1.234–2.1.235): auto mode сам возобновляет сессию после сброса лимита использования, встроенный скилл `claude-api` сжат с ~200k+ до ~25k токенов, продолжение серии bypass-фиксов (NT-namespace path rejection, session-scoped permission answers в фоновых субагентах); Workbench→Playground (18.08, платформенные release notes) проверен и отброшен — консольный анонс без CLI/API-практики
- [[claude-cookbook-managed-agents-production-memory]] — официальные notebook'ы Claude Cookbooks (`managed_agents/`): production-паттерн через webhooks (`session.status_idled`, HMAC-подпись, human-in-the-loop `escalate()`) и memory stores (per-workspace, монтируются как `/mnt/memory/{store-name}`, файловые тулы + REST-доступ приложения)
- [[claude-cookbook-cost-optimization]] — официальный notebook Claude Cookbooks (2026-08-12): чеклист оптимизации стоимости Claude API — baseline, prompt caching (byte-stable префикс, explicit breakpoints), input/output token management, batch API, model selection
- [[claude-code-changelog-snapshot-2026-08-16]] — официальный changelog Claude Code (в. 2.1.232–2.1.233): форк субагента наследует диалог целиком по умолчанию, `@`-упоминание для прямого обращения к сессии, продолжение серии bypass-фиксов (PowerShell, Windows symlink/NTLM, cross-session messaging), первое упоминание GitLab в этой вики
- [[claude-code-changelog-snapshot-2026-08-13]] — официальный changelog Claude Code (в. 2.1.227–2.1.231): hardening скиллов из claude.ai, сэндбокс IPv6 fail-closed, `/commit-push-pr` без авто-одобрения опасных флагов, self-hosted runner — server-supplied хуки, `ListAgents` различает offline/cloud
- [[claude-code-auto-mode-default]] — официальная документация Claude Code (`permission-modes`): auto mode — дефолтный режим разрешений для новых сессий с 14.08.2026 на Pro/Max/Team, требования доступности, границы (не переопределяет свой/org-дефолт)
- [[memora-openrouter-embeddings-dating]] — официальный GitHub-репозиторий `OpenRouterTeam/ai-sdk-provider`: поддержка эмбеддингов в SDK и путь `/embeddings` в коде датированы 2025-12-06, на 8+ месяцев раньше релизных заметок Memora; закрывает датировку противоречия про OpenRouter
- [[meta-agents-rule-of-two]] — официальный пост Meta (31.10.2025): точная формулировка «правила двух» (те же три условия, что у смертельной троицы Willison), граница «в рамках одной сессии», human-in-the-loop при необходимости всех трёх; домен заблокирован сетевым прокси, факты по совпадению независимых источников
- [[memora-agent-memory-mcp]] — репозиторий Memora как первоисточник: разбор аварии «эмбеддинги не считались месяцами, а система отчитывалась здоровой», принципы против петли пересказа, цепочки замещения; плюс найденное противоречие про эндпоинт эмбеддингов OpenRouter
- [[claude-code-self-hosted-environments-docs]] — официальная документация Claude Code: self-hosted environments (concept + quickstart), environment/runner/session, аутентификация раннера общим секретом, network paths (только исходящие), lifecycle раннера (запирается на одного пользователя, `--drain-grace-sec`/`--retire-at`), быстрый старт с командами
- [[claude-code-changelog-snapshot-2026-08-10]] — официальный changelog Claude Code (в. 2.1.224–2.1.226): self-hosted environments (`claude self-hosted-runner`, Team/Enterprise), cross-session `SendMessage`/`ListAgents` расширен на весь парк машин пользователя, расширение маскирования кредов сэндбокса (JWT/AWS SigV4), лимит 200 субагентов на сессию убран (устарел прежний факт)
- [[minja-memory-injection-attack]] — официальный код атаки MINJA (NeurIPS 2025, `github.com/dsh3n77/MINJA`): indication prompt + progressive shortening на трёх агентах (RAP/EHR/QA), реальные промпт-шаблоны атаки; полный текст статьи заблокирован сетевым прокси, точные ISR/ASR и абляция «пустая vs заполненная память» не подтверждены
- [[chroma-context-rot]] — официальный репозиторий Chroma (`chroma-core/context-rot`): методология трёх экспериментов (NIAH extension/LongMemEval/Repeated Words), точность GPT-4.1 100%→18% на переходе 5 000→10 000 токенов на примере реальных данных; полный отчёт (research.trychroma.com) заблокирован сетевым прокси окружения
- [[berezhnitsky-agent-memory-lies]] — память LLM-агента как инженерная система: развилка «синтез на входе / хранение сырым», три механизма отказа при нескольких писателях, смертельная троица + MINJA + правило двух, четыре формы хранения знания, «канон против кэша»
- [[claude-code-memory-docs]] — официальная документация Claude Code: auto-memory (формат `MEMORY.md`+топики, `~/.claude/projects/<project>/memory/`, machine-local per-repo, лимит 200 строк/25KB) против `CLAUDE.md`, конфликт не разрешается формально, независима от memory tool в API
- [[mogilko-ai-system-five-levels]] — пять уровней внедрения ИИ в бизнес: что класть в файлы о себе, как их собирать интервью, чего не отдавать агентам
- [[anthropic-context-engineering-claude-5]] — официальная статья Anthropic (24.07.2026): из системного промпта Claude Code убрали >80% без потери качества; шесть сдвигов «раньше → теперь» и разметка слоёв контекста
- [[karpathy-jarvis-personal-ai-memory]] — метод Карпати: Claude Code + Obsidian как персональная AI-память (первоисточник паттерна этой вики)
- [[karpathy-skills-claude-md]] — репозиторий с CLAUDE.md-гайдлайнами против типичных ошибок LLM (188.8k звёзд)
- [[mastodont-claude-obsidian-video]] — полный видео-транскрипт метода Карпати с ограничениями и гибридной архитектурой
- [[ai-proryv-5-levels-claude]] — 5 уровней владения Claude
- [[berezhnitsky-7-signs-old-jun]] — 7 признаков старого джуна
- [[metics-media-10k-website]] — сайт за $10k через Claude Code
- [[berezhnitsky-attack-for-3-dollars]] — как ИИ обрушил барьер входа в кибератаки
- [[appbusters-vibecoding-45-min]] — полный курс по вайбкодингу за 45 минут
- [[qaisar-claude-full-course]] — полный курс по Claude на 2026 год
- [[romaray-claude-watch-video]] — как научить Claude "смотреть" видео
- [[karpathy-llm-wiki-gist]] — оригинальный гист Карпати (первоисточник паттерна этой вики)
- [[bashkardinov-obsidian-claude-guide]] — Obsidian+Claude через MCP для документации кодового проекта
- [[shubin-llm-memory-landscape]] — обзор Mem0/Zep/Letta/Graphify/Karpathy-вики
- [[sonny-huynh-second-brain]] — "второй мозг" с ежедневными воркфлоу
- [[nikita-vels-claude-code-30-concepts]] — 30 практических концептов механики Claude Code
- [[nikita-vels-claude-code-full-course]] — трёхчасовая версия того же курса (апрель 2026): разобрана по дельте, новое — критерий «MCP или скилл» по частоте и обмен агентов через папку `Runtime`; первый источник, пропущенный через каскад дешёвых моделей
- [[comrad404-what-is-harness]] — разбор понятия «харнес» целиком: терминология, восемь частей, пять болей, ландшафт инструментов; центральная цифра проверена по блогу LangChain
- [[paragon-vibecoding-security]] — как вскрывают приложения, собранные нейросетью: демонстрация на стенде; все три числа материала проверены по первоисточникам (arXiv, GitGuardian)
- [[hook-4-pravila-claude-skills]] — маркетинговый конспект "4 правила Anthropic" (вторичный источник, есть неподтверждённая цитата)
- [[anthropic-code-summit-build-skills-talk]] — первоисточник: доклад Barry Zhang & Mahesh Murag на AI Engineer Code Summit
- [[anthropic-official-skills-docs]] — официальная методология Anthropic: инженерный блог + skill-creator + доки Claude Code
- [[habr-claude-skills-practical-guide]] — практика сообщества: 9 категорий скиллов, лайфхаки (Gotchas, config.json, хуки)
- [[mcp-2026-07-28-spec-release-candidate]] — крупнейшая ревизия спецификации MCP: stateless core, MCP Apps, Tasks, авторизация OAuth/OIDC
- [[claude-agent-sdk-overview]] — официальная документация Claude Agent SDK: капабилити, сравнение с Client SDK/CLI/Managed Agents
- [[claude-code-changelog-snapshot-2026-07]] — снапшот официального changelog Claude Code (в. 2.1.172–2.1.205): Manual mode, фоновые субагенты по умолчанию, auto-commit/PR у фоновых агентов
- [[claude-memory-tool-docs]] — официальная документация Memory tool: file-based память API, six команд, паттерн multi-session разработки
- [[anthropic-long-running-agent-harness]] — две статьи блога + репозиторий `cwc-long-running-agents`: harness-паттерны для долгоживущих агентов (многосессионный прогресс + отдельный GAN-inspired харнесс для полных приложений, допроверен 2026-07-29)
- [[claude-code-agent-teams-docs]] — официальная документация Agent Teams (v2.1.178+): архитектура lead/teammates/task list/mailbox, security-модель
- [[claude-code-model-config-docs]] — официальная документация Model configuration: алиасы моделей, `opusplan` (task-based автопереключение Opus↔Sonnet), fallback-цепочки, content-based fallback Fable 5
- [[woome-ai-dzen-content-automation]] — Claude Code + Дзен: контент-ферма, промо-видео с рабочей технической частью
- [[zproger-opencode-review]] — практический обзор OpenCode: провайдеры, Plan/Build, Skills/MCP
- [[vladilen-minin-gsd-superpowers]] — два живых кейса GSD и Superpowers: SaaS на DeepSeek API, контент-генератор
- [[nikita-efimov-claude-automations]] — Cowork Scheduler / Local & Cloud Routines / `/loop` в Claude Desktop
- [[prostodevops-cloud-infrastructure]] — облачные вычисления с нуля: модели, механика, специфика РФ (дубликат файла в raw)
- [[claude-code-changelog-snapshot-2026-07-15]] — снапшот changelog Claude Code (в. 2.1.206–2.1.210) + Week 28 dev digest: `/doctor`-чекап, in-app браузер, hardened Agent tool, защита от фальшивых "одобрений" в транскрипте
- [[claude-managed-agents-overview]] — официальная документация Claude Managed Agents: hosted agent harness (agent/environment/session/events), сравнение с Agent SDK, память/мультиагентность/self-hosted sandboxes/scheduled deployments
- [[claude-code-dynamic-workflows-docs]] — официальная документация Dynamic Workflows: скриптовая оркестрация субагентов, примитивы agent/pipeline/parallel, сравнение с субагентами/skills/agent teams, quality-паттерны, лимиты и стоимость
- [[claude-code-changelog-snapshot-2026-07-19]] — снапшот changelog Claude Code (в. 2.1.211–2.1.214) + Week 29 dev digest: Artifacts + MCP-коннекторы зрителя, `/fork` как фоновая сессия, лимиты runaway-циклов, `EndConversation`, серия фиксов bypass в permission-анализаторе, screen reader mode
- [[claude-code-changelog-snapshot-2026-07-20]] — снапшот changelog Claude Code (в. 2.1.215): скиллы `/verify` и `/code-review` больше не подключаются автоматически, только по явному вызову
- [[claude-code-changelog-snapshot-2026-07-22]] — снапшот changelog Claude Code (в. 2.1.216–2.1.217): `sandbox.filesystem.disabled` — избирательное отключение файловой изоляции сэндбокса с сохранением сетевой, плюс настраиваемые лимиты параллелизма/глубины субагентов и фикс `--max-budget-usd` для фоновых субагентов
- [[claude-opus-5-launch]] — официальный запуск Claude Opus 5 (24.07.2026, та же цена что у Opus 4.8, thinking по умолчанию, breaking change для effort xhigh/max) + Claude Code v2.1.218–2.1.219 (Opus 5 как дефолт, `/code-review` фоновым субагентом, `/deep-research` manual-only, `sandbox.network.strictAllowlist`, workspace trust для хуков агентов, дефолт Dynamic Workflows medium/<15 агентов, неподтверждённая доками смена глубины вложенности субагентов до 3)
- [[claude-code-migration-case-studies-2026-07]] — практика Dynamic Workflows в большом масштабе: официальный блог Anthropic про кейсы Bun/Klarna/CyberAgent (прочитан через вторичные источники — первоисточник вернул 403), 4-фазная архитектура миграции + adversarial review, и критика Zig-creator'а как содержательный контрпример "agent review агентами ≠ human review"
- [[prezentacii-cherez-ii-agenta-web3nity]] — методология презентаций через ИИ-агента (смысл→визуал→сборка); 4 авторских скилла за Telegram-стеной, воспроизведены локально
- [[nickvels-mattpocock-pipeline]] — пайплайн Matt Pocock (grilling→spec→tickets→implement) с проверкой всех утверждений по исходникам репозитория; отдельно разобран и отложен Autopilot
- [[web3nity-mcp-guide]] — вводный гайд по MCP (слабый источник, ~70% ниже порога); взяты лестница подключения нового сервиса, каталоги MCP-серверов и критерии проверки стороннего расширения
- [[romaray-top-5-skills]] — обзор «топ-5 скиллов» (слабый источник, разобран с поправками); ценен блоком про безопасность — исследование ToxicSkills от Snyk, и как повод развернуть [[context7]] по первоисточникам
- [[web3nity-10-vibecoding-ideas]] — каталог задач для вайбкодинга не-разработчику: рамка отбора, 11 типовых инструментов, границы применимости; тарифы Abacus не проверены
- [[bohomolov-skill-architecture]] — 4 апгрейда однофайлового скилла до многофайловой структуры; архитектурная часть подтверждена офдокой, «пересобирать скилл ради одного файла» устарело, eval-цикла и description-триггера в методе нет
- [[mcp-2026-07-28-spec-final]] — официальный блог MCP: финальная спецификация 2026-07-28, MRTR, header-based routing, кэшируемые list-ответы, точный список stable/deprecated, SDK-поддержка по языкам
- [[geo-ai-search-official-docs]] — официальная документация OpenAI/Perplexity/Google/Gemini о том, как контент попадает в ответы ИИ-поисковиков: robots.txt как реальный переключатель, текстовые краулеры против нативной работы Gemini с видео
- [[claude-code-routines-docs]] — официальная документация Cloud Routines и `/loop`/scheduled tasks: таблица трёх способов расписания, self-paced `/loop` через `ScheduleWakeup`, `loop.md`, security-механизм `<routine-fire-payload>`/фрейминга триггера (v2.1.214)
- [[claude-code-changelog-snapshot-2026-08-04]] — снапшот changelog Claude Code (в. 2.1.220–2.1.221): git-поведение фоновых сессий уточнено (draft PR не всегда), `sandbox` `mode: "mask"` для credential-файлов, `prompt-audit` для скилла `claude-api`, Focus view (VSCode)
- [[claude-code-changelog-snapshot-2026-08-07]] — снапшот changelog Claude Code (в. 2.1.222–2.1.223): побег из сэндбокса Dynamic Workflows через `import()`, удаление Ultraplan, продолжение серии bypass-фиксов permission-анализатора (worktree/git, `PreToolUse` auto-allow, обфускация Bash-команд), auto mode проверяет `SendMessage`
- [[claude-code-changelog-snapshot-2026-08-22]] — changelog Claude Code (в. 2.1.236–2.1.240, `/claude-api upgrade` под миграцию SDK) + официальные Claude Platform release notes: Python SDK v1.0 (breaking changes), новый browser use tool, computer use tool вышел из беты, разом out-of-beta Files/Agent Skills/Admin API, домен-фильтр web_search/web_fetch и self-hosted memory stores у Managed Agents

## Projects
_(рабочие проекты: вайбкодинг, интеграции ИИ, агенты)_

- [[devkit-conveyer-razrabotki]] — свой конвейер разработки: принцип «инструмент обязан доказать, что смотрел» (учёт охвата и канарейка против зелёного «пройдено»), склейка готового вместо своего, гейты по жёсткости, отброшенные альтернативы
- [[jarvis-personal-wiki]] — сама эта вики как проект: структура, решения, статус
- [[humanizer-ru-skill-refactor]] — эксперимент: монолитный скилл разложен по многофайловой архитектуре и замерен A/B-прогонами; три итерации, цифры по токенам/ходам/качеству
- _(несколько личных рабочих проектов описаны страницами в `private/` — папка в `.gitignore`, на GitHub не уходит)_

## Practices
_(действующие правила, извлечённые из знаний вики; живые документы)_

- [[claude-code-practices]] — полный свод правил для Claude Code: безопасность кода, автономная работа, контент/цепочка поставок, оркестрация; что вошло в глобальный CLAUDE.md/скиллы и что отсечено; с 19.08 — п. 12: у смонтированного правила записывается, что его снимает, иначе свод умеет только расти
- [[moi-pravila]] — якорь-страница: сами правила пользователя с 2026-07-30 живут только локально, в `private/` вне репозитория
- [[delegirovanie-deshevym-modelyam]] — что сгружать дешёвым моделям и как проверять: лестница исполнителей, каскад с оценщиком качества, замеры на пяти материалах, генерация длинного текста и раздача ролей между моделями, разбор готовых решений (LiteLLM, `llm`, агрегаторы)
- [[poisk-uyazvimostey-instrumenty]] — чем машинно искать дыры в своём коде: пять классов инструментов через `uvx` без установки, правило «severity ничего не говорит о твоём проекте», разбор шума 50:1 из реального прогона и три класса дыр, которые не ловит ни один сканер
- [[ustanovka-instrumentov-na-windows]] — три грабли одной установки, все многоразовые: манифест пакетного менеджера ссылается на файл поставщика и умирает вместе с уборкой архива (404 на любой версии, перебор бесполезен); PATH не догоняет уже запущенные окна, и «пропало» означает «перезапусти»; Git Bash не считает `.bat` исполняемым, лечится обёрткой без расширения

## Synthesis
_(ответы на вопросы, сравнения, анализ)_

- [[pre-project-architecture-checklist]] — чек-лист архитектуры/безопасности перед стартом вайбкодинг-проекта, чтобы не переделывать
- [[moy-uroven-vladeniya-claude]] — оценка текущего уровня владения Claude по модели 5 уровней
- [[claude-code-checklist-postoyannogo-ispolzovaniya]] — практический чек-лист Claude Code для повседневного использования
- [[audit-nashey-obvyazki]] — что из разобранного про харнес у нас уже стоит и чего нет: шесть частей из восьми закрыты, пробел один и кучный — ловим ошибки формы, не ловим повторяющееся бесполезное поведение
- [[ustroystvo-agentnoy-obolochki]] — как устроен агент внутри, по документации dsh: ход и шаг, восемь точек вмешательства, журнал как источник видимого модели; что там правда ново, а что лозунг, и какие две вещи оттуда переносятся к нам
- [[karta-shvov-nashey-obvyazki]] — фаза цикла → чем в неё вмешиваться (хуки, скиллы, права, MCP, CI) → чем за это платишь; решающее дерево «куда класть новое правило» и почему `CLAUDE.md` — последний вариант, а не первый
- [[proiskhozhdenie-pravila-effekt-30-dney]] — цепочка происхождения правила «разовая правка или в скилл навсегда?»: от доклада Zhang/Murag до п. 16 моих правил
- [[opencode-vs-claude-code]] — сравнение двух CLI-агентов: мультипровайдерность против оркестрации, запрет subscription-OAuth в сторонних инструментах (ToS, февраль 2026), когда что выбирать
