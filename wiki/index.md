# Индекс

Каталог всех страниц вики. Обновляется при каждой загрузке источника или синтезе.

## Entities
_(люди, компании, инструменты)_

- [[andrej-karpathy]] — автор метода/гиста, лежащего в основе паттерна персональной вики
- [[claude-code]] — CLI-агент Anthropic, движок этой вики
- [[obsidian]] — markdown-редактор с графом связей, IDE для просмотра вики
- [[obsidian-web-clipper]] — расширение браузера для сохранения статей (пока не подключено)
- [[antigravity-ide]] — альтернативная IDE для запуска Claude Code (не используется)
- [[pinecone]] — векторная БД для масштабирования (не используется)
- [[notebooklm]] — RAG-система Google, контраст с паттерном этой вики (не используется)
- [[cursor]] — AI-native IDE, альтернатива Claude Code
- [[multica]] — организация, публикует репозиторий с гайдлайнами Карпати
- [[ii-mastodont]] — автор видео-разбора метода Карпати (18М просмотров)
- [[claude-projects]] — функция Claude.ai: память/контекст под конкретную роль
- [[claude-skills]] — переносимые "умения" для Claude
- [[claude-cowork]] — режим Claude Desktop с доступом к файлам компьютера
- [[supabase]] — Backend-as-a-Service для вайбкодинг-проектов
- [[openrouter]] — агрегатор нейросетевых моделей
- [[ai-proryv]] — автор видео про 5 уровней владения Claude
- [[dmitry-bereznitsky]] — разработчик, автор видео про карьеру и AI-кибербезопасность
- [[metics-media]] — канал про сайты за $10k через Claude Code
- [[appbusters]] — школа вайбкодинга
- [[qaisar-kurmangaliev]] — автор полного курса по Claude
- [[neiroprosveshchenie]] — автор техники "просмотра" видео через Claude
- [[mem0]] — memory-фреймворк для агентов на API
- [[zep-graphiti]] — temporal knowledge graph для памяти
- [[letta]] — memory-as-OS фреймворк (бывший MemGPT)
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
- [[gsd-get-shit-done]] — spec-driven агентский фреймворк полного SDLC поверх Claude Code
- [[superpowers]] — TDD-ориентированный набор скиллов с автообнаружением, лёгкая альтернатива GSD
- [[nikita-efimov]] — автор разбора автоматизаций Claude Desktop
- [[prostodevops]] — DevOps-образовательный канал
- [[claude-managed-agents]] — hosted agent harness Anthropic: agent/environment/session/events, память/мультиагентность/self-hosted sandboxes поверх Claude API
- [[web3nity]] — автор методологии «презентация через ИИ-агента» (YouTube + Telegram)
- [[context7]] — сервис/MCP-сервер Upstash с актуальной документацией библиотек; установлен 2026-07-27
- [[mattpocock-skills]] — пак скиллов Matt Pocock: пайплайн grilling→spec→tickets→implement, tracer-bullet нарезка; установлен 2026-07-27
- [[exa]] — поисковый API + официальный MCP для ИИ-агентов, neural search; оценён по бэклогу, не установлен

## Concepts
_(идеи, модели, принципы)_

- [[persistent-wiki-pattern]] — вики вместо RAG: накопление знаний вместо повторного извлечения (+ ограничения на масштабе)
- [[ingest-query-lint]] — три базовые операции ведения вики
- [[llm-coding-guidelines]] — четыре принципа Карпати против типичных ошибок LLM в коде
- [[hybrid-memory-architecture]] — 4-элементная архитектура: CLAUDE.md + Obsidian + Pinecone + NotebookLM
- [[one-vault-one-project-rule]] — не смешивать темы в одном vault'е (открытый вопрос для этой вики)
- [[five-levels-of-claude-mastery]] — модель зрелости использования Claude, от поисковика до автономной системы
- [[seven-signs-of-old-junior]] — карьерная стагнация разработчиков, включая ИИ-зависимость
- [[10k-website-checklist]] — воркфлоу немассового веб-дизайна через Claude Code
- [[vibecoding-full-workflow]] — сквозной процесс разработки приложения через ИИ-агента
- [[ai-security-by-design]] — как ИИ изменил кибербезопасность и принципы защиты
- [[claude-watch-skill]] — Claude анализирует кадры видео по тайм-кодам, не только транскрипт
- [[llm-memory-landscape]] — три разные задачи "памяти для ИИ": о пользователе, о коде, о знаниях
- [[project-documentation-vault-pattern]] — Obsidian-вики как документация кодового проекта, альтернатива персональной вики
- [[second-brain-daily-workflows]] — ежедневные продуктивностные воркфлоу Obsidian+Claude (не про накопление знаний)
- [[skill-authoring-practical-rules]] — как создавать Skills вместо промтов: description-триггер, три слоя, композиционность, итеративное накопление
- [[mcp-model-context-protocol]] — открытый протокол подключения агентов к внешним сервисам: архитектура, крупнейшая ревизия спецификации 2026-07-28 (stateless core, MCP Apps, Tasks)
- [[claude-memory-tool]] — официальный файловый инструмент памяти Claude API: just-in-time context retrieval, six-команд протокол, multi-session паттерн
- [[long-running-agent-harness]] — три примитива Anthropic для многосессионных агентов: Default-FAIL Contract, Fresh-Context Evaluator, Agent-Maintained Handoff
- [[agent-teams]] — команды агентов Claude Code: когда team вместо субагентов, размеры, failure modes, security-модель
- [[ai-content-farming-workflow]] — техника контент-фермы через ИИ-агента: скрапинг конкурентов, "система" файлов вместо промта, параллельная генерация
- [[agentic-sdlc-frameworks]] — GSD и Superpowers: агентские фреймворки, автоматизирующие весь SDLC, а не только код
- [[claude-desktop-automation-modes]] — четыре способа автоматизации через Claude Desktop: Cowork Scheduler, Local/Cloud Routines, `/loop`
- [[cloud-computing-fundamentals]] — основы облачных вычислений: NIST-определение, IaaS/PaaS/FaaS/SaaS, специфика РФ (152-ФЗ)
- [[dynamic-workflows]] — скриптовая оркестрация десятков-сотен субагентов в Claude Code: примитивы agent/pipeline/parallel, quality-паттерны (adversarial verify, judge panel, loop-until-dry), место среди субагентов/skills/agent teams
- [[ai-presentation-workflow]] — методология презентаций через ИИ-агента: смысл→визуал→сборка, нарратив-гейт до дизайна, референсы→правила; реализована как 4 локальных скилла

## Sources
_(саммари загруженных источников)_

### ⭐ Топ-находки
_(отбирает автономный разведчик практического материала — см. `CLAUDE.md` → операция Ingest.)_
- [[claude-code-changelog-snapshot-2026-07-15]] — hardened Agent tool против prompt injection, `/doctor` как полноценный чекап, защита от фальшивых "одобрений пользователя" в транскрипте (тот же механизм виден в системных уведомлениях этого прогона)
- [[claude-managed-agents-overview]] — официальный API для агентов в managed sandbox-инфраструктуре, закрывает пробел, явно отмеченный в claude-agent-sdk.md
- [[claude-code-dynamic-workflows-docs]] — скриптовая оркестрация субагентов (Dynamic Workflows), закрывает пробел: механизм существовал с мая 2026, но не имел отдельной страницы; ровно тот инструмент, которым устроен встроенный скилл deep-research
- [[claude-code-changelog-snapshot-2026-07-19]] — Artifacts вызывают MCP-коннекторы зрителя при открытии страницы (ровно механизм скилла `artifact-capabilities`, доступного в сессиях этой вики), плюс лимиты на runaway-циклы (WebSearch/субагенты), `EndConversation`, серия фиксов bypass-уязвимостей в permission-анализаторе
- [[claude-opus-5-launch]] — Claude Opus 5 (24.07.2026) стал дефолтной моделью Claude Code v2.1.219: та же цена, что у Opus 4.8, thinking по умолчанию (breaking change для effort xhigh/max), Dynamic Workflows получили официальный дефолт medium/<15 агентов — подтверждённый напрямую в системном промпте сессий этой вики
- [[claude-code-migration-case-studies-2026-07]] — Dynamic Workflows на реальном масштабе: Bun (Zig→Rust, ~1M строк за 11 дней), Klarna (security-аудит), CyberAgent (hardening) — воспроизводимая 4-фазная архитектура + честная критика (adversarial review агентами ≠ человеческое ревью)

### Все источники
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
- [[hook-4-pravila-claude-skills]] — маркетинговый конспект "4 правила Anthropic" (вторичный источник, есть неподтверждённая цитата)
- [[anthropic-code-summit-build-skills-talk]] — первоисточник: доклад Barry Zhang & Mahesh Murag на AI Engineer Code Summit
- [[anthropic-official-skills-docs]] — официальная методология Anthropic: инженерный блог + skill-creator + доки Claude Code
- [[habr-claude-skills-practical-guide]] — практика сообщества: 9 категорий скиллов, лайфхаки (Gotchas, config.json, хуки)
- [[mcp-2026-07-28-spec-release-candidate]] — крупнейшая ревизия спецификации MCP: stateless core, MCP Apps, Tasks, авторизация OAuth/OIDC
- [[claude-agent-sdk-overview]] — официальная документация Claude Agent SDK: капабилити, сравнение с Client SDK/CLI/Managed Agents
- [[claude-code-changelog-snapshot-2026-07]] — снапшот официального changelog Claude Code (в. 2.1.172–2.1.205): Manual mode, фоновые субагенты по умолчанию, auto-commit/PR у фоновых агентов
- [[claude-memory-tool-docs]] — официальная документация Memory tool: file-based память API, six команд, паттерн multi-session разработки
- [[anthropic-long-running-agent-harness]] — блог + репозиторий `cwc-long-running-agents`: harness-паттерны для долгоживущих агентов
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

## Projects
_(рабочие проекты: вайбкодинг, интеграции ИИ, агенты)_

- [[jarvis-personal-wiki]] — сама эта вики как проект: структура, решения, статус
- _(есть ещё один личный рабочий проект — хранится только локально, не в этом репозитории)_

## Practices
_(действующие правила, извлечённые из знаний вики; живые документы)_

- [[claude-code-practices]] — полный свод правил для Claude Code: безопасность кода, автономная работа, контент/цепочка поставок, оркестрация; что вошло в глобальный CLAUDE.md/скиллы и что отсечено
- [[moi-pravila]] — правила для меня: дисциплина работы с ИИ, гигиена сессий, неделегируемые решения, привычки (наглядная версия — practices.html)

## Synthesis
_(ответы на вопросы, сравнения, анализ)_

- [[pre-project-architecture-checklist]] — чек-лист архитектуры/безопасности перед стартом вайбкодинг-проекта, чтобы не переделывать
- [[moy-uroven-vladeniya-claude]] — оценка текущего уровня владения Claude по модели 5 уровней
- [[claude-code-checklist-postoyannogo-ispolzovaniya]] — практический чек-лист Claude Code для повседневного использования
- [[proiskhozhdenie-pravila-effekt-30-dney]] — цепочка происхождения правила «разовая правка или в скилл навсегда?»: от доклада Zhang/Murag до п. 16 моих правил
