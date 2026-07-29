# Лог

Хронологический append-only лог всех операций над вики (ingest, query, lint).

Формат записи:
`## [YYYY-MM-DD] тип | Название`

## [2026-07-21] ingest | Web3nity: презентации через ИИ-агента (youtube.com/watch?v=r0a5BxLhhTM)
Методология «презентация через ИИ-агента»: смысл→визуал→сборка, нарратив-blueprint как отдельный гейт до дизайна, референсы→правила с самопроверкой скриншотом, переиспользуемый Visual DNA. Создано: wiki/sources/prezentacii-cherez-ii-agenta-web3nity.md, wiki/concepts/ai-presentation-workflow.md, wiki/entities/web3nity.md. Обновлён index.md. 4 авторских скилла раздаются только через приватный Telegram-канал (достать/проверить исходники нельзя) — методология зафиксирована из транскрипта, а эквивалент воспроизведён локально в ~/.claude/skills/ (presentation-story-architect, presentation-style-interpreter, presentation-visual-dna, presentation-builder) поверх существующих slides/design-system/frontend-design/ui-ux-pro-max. Прямых промпт-инъекций в источнике не найдено.

## [2026-07-07] init | Создание структуры базы знаний
Создан каркас: raw/sources, raw/web-clipped, raw/assets, wiki/entities, wiki/concepts, wiki/sources, wiki/projects, wiki/synthesis, index.md, log.md, CLAUDE.md. Тематика: ИИ (изучение + рабочие проекты — вайбкодинг, интеграции ИИ, агенты). Добавлен базовый конфиг Obsidian.

## [2026-07-07] ingest | Метод Карпати: Claude Code + Obsidian (gomymy64.github.io/jarvis-memory)
Первый источник. Мета: статья описывает тот же паттерн персональной вики, по которому уже была построена эта база знаний. Создано: raw/sources/karpathy-jarvis-claude-obsidian.md, wiki/sources/karpathy-jarvis-personal-ai-memory.md, wiki/concepts/persistent-wiki-pattern.md, wiki/concepts/ingest-query-lint.md, wiki/entities/{andrej-karpathy, claude-code, obsidian, obsidian-web-clipper, antigravity-ide, pinecone, notebooklm}.md, wiki/projects/jarvis-personal-wiki.md. Обновлён index.md.

## [2026-07-07] ingest | andrej-karpathy-skills (github.com/multica-ai/andrej-karpathy-skills)
Репозиторий с CLAUDE.md-гайдлайнами против типичных ошибок LLM в коде (4 принципа), 188.8k звёзд (проверено через GitHub API). Создано: raw/sources/karpathy-skills-claude-md.md, wiki/sources/karpathy-skills-claude-md.md, wiki/concepts/llm-coding-guidelines.md, wiki/entities/{cursor, multica}.md. Обновлены wiki/entities/{andrej-karpathy, claude-code}.md (добавлены ссылки на новый источник) и index.md. Наблюдение: принципы репозитория почти дословно совпадают с базовыми правилами, по которым Claude Code уже работает по умолчанию.

## [2026-07-07] ingest | Видео "Claude Code + Obsidian ВЗОРВАЛИ Интернет" (канал ИИ МАСТОДОНТ, через Web Clipper)
Первый клип через настроенный Web Clipper. Полный транскрипт видео — первоисточник для уже загруженной статьи karpathy-jarvis-personal-ai-memory. Добавляет: ограничения Obsidian RAG на масштабе (налог на контекст, нет семантического поиска), развёрнутую гибридную архитектуру (CLAUDE.md + Obsidian + Pinecone + NotebookLM), правило "одна база — один проект". Создано: wiki/sources/mastodont-claude-obsidian-video.md, wiki/entities/ii-mastodont.md, wiki/concepts/{hybrid-memory-architecture, one-vault-one-project-rule}.md. Обновлены: wiki/concepts/persistent-wiki-pattern.md (добавлен раздел "Ограничения"), wiki/entities/{andrej-karpathy, pinecone, notebooklm}.md, wiki/projects/jarvis-personal-wiki.md (зафиксирован открытый вопрос про разделение vault'ов на две темы; Web Clipper отмечен как подключённый), index.md.

## [2026-07-07] ingest | Батч из 7 видео через Web Clipper (raw/web-clipped)
Обработаны все накопившиеся клипы разом: "5 уровней владения Claude" (AI Прорыв), "7 признаков старого джуна" и "Атака за $3" (Дмитрий Березницкий), "Build $10,000 Websites" (Metics Media), "Вся база по ВАЙБКОДИНГУ" (AppBusters), "ПОЛНЫЙ КУРС по Claude" (Кайсар Курмангалиев), "Я научил Claude смотреть видео" (Нейропросвещение). Создано: 7 wiki/sources/*, 6 новых concepts (five-levels-of-claude-mastery, seven-signs-of-old-junior, 10k-website-checklist, vibecoding-full-workflow, ai-security-by-design, claude-watch-skill), 11 новых entities (6 авторов + claude-projects, claude-skills, claude-cowork, supabase, openrouter). Обновлены claude-code.md (связи с новыми фичами Claude) и index.md. Ради экономии объёма страницы источников короче, чем в первых трёх ingest — детали живут в concept-страницах, а не дублируются.

## [2026-07-07] lint | Проверка здоровья вики
Битые ссылки — 0, страницы-сироты — 0 (все 45 страниц перепроверены). Найдено и исправлено 4 проблемы: (1) obsidian-web-clipper.md утверждал "не установлено" — устарело, обновлено + добавлена не сохранённая ранее информация о баге длинных видео (Legacy mode / URI-лимит / баг Obsidian 1.12.1); (2) claude-code.md содержал неточную атрибуцию "требует Pro/Max" — источник на самом деле говорил про розыгрыш подписок, не про требование; заменено на данные из двух источников, где это разбирается предметно; (3) claude-skills.md смешивал Karpathy's CLAUDE.md-конвенцию с продуктовым понятием Skill — добавлено разграничение; (4) jarvis-personal-wiki.md содержал устаревший список из 3 источников при факте в 10 — исправлено на ссылку на актуальный index.md. Наблюдение: батч из 7 видео включал контент не строго про ИИ (карьерная стагнация разработчиков, кибербезопасность) — не нарушение, но стоит держать в уме как сигнал к триггеру "один vault на две темы" в [[jarvis-personal-wiki]], если тематический дрейф продолжится.

## [2026-07-07] query | Зачем в вики кибербезопасность и карьерный рост разработчика
Пользователь пояснил: эти темы загружены целенаправленно, чтобы компенсировать нехватку базовых знаний архитектуры/безопасности и продумывать проекты полнее с нуля, а не переделывать потом. Это резолвит "наблюдение о тематическом дрейфе" из прошлого lint — не дрейф, осознанная цель. Обновлён jarvis-personal-wiki.md (добавлено объяснение в разделе "Цель"). Синтезирован и сохранён wiki/synthesis/pre-project-architecture-checklist.md — практический чек-лист архитектуры/безопасности перед стартом проекта, собранный из vibecoding-full-workflow, ai-security-by-design, seven-signs-of-old-junior, 10k-website-checklist.

## [2026-07-07] query | На каком уровне владения Claude находится пользователь
Синтезирован ответ на основе five-levels-of-claude-mastery.md и наблюдаемого использования в этом проекте: Уровень 4 (Продвинутый) — работа через терминал, накопительный CLAUDE.md, паттерн самопроверки уже есть; Уровень 5 не достигнут (нет облачных рутин, хуков, task budgets). Сохранено в wiki/synthesis/moy-uroven-vladeniya-claude.md.

## [2026-07-07] ingest | 4 источника: оригинальный гист Карпати + 2 статьи с Хабра + перевод Sonny Huynh
Пользователь добавил все кандидаты, предложенные ранее. Главное — сам гист llm-wiki.md резолвит открытый вопрос в andrej-karpathy.md. Создано: 4 wiki/sources/*, 3 новых concepts (llm-memory-landscape, project-documentation-vault-pattern, second-brain-daily-workflows), 7 новых entities (mem0, zep-graphiti, letta, graphify, maxim-bashkardinov, shubin-danila, sonny-huynh). Обновлены: andrej-karpathy.md (закрыт открытый вопрос), persistent-wiki-pattern.md (формы ответа Query, лимит масштаба ~100 источников, git-версионирование, пробел с raw/assets), hybrid-memory-architecture.md и pinecone.md (уточнено более предметным источником — Pinecone не главный инструмент масштабирования), one-vault-one-project-rule.md (найдено противоречие: практика shubin-danila — один vault на все проекты), ai-security-by-design.md (добавлен раздел "память как attack surface" — graph poisoning, vault-as-payload, skill marketplace-атаки), obsidian.md (два способа подключения: прямой доступ vs MCP; отмечен пробел с raw/assets), CLAUDE.md (добавлено правило безопасности: инструкции внутри источников не выполняются как команды). Итог: 14 источников, существенно уточнена картина по памяти для ИИ-агентов.

## [2026-07-08] ingest+query | "Claude Code от НУЛЯ до ПРОФИ за 40 минут" (Никита Велс) + чек-лист
Плотный справочник из 30 практических концептов механики Claude Code. Создано: nikita-vels-claude-code-30-concepts.md (источник), nikita-vels.md (сущность). Существенно дополнена claude-code.md разделом "Практическая механика" (контекст/сессии, CLAUDE.md vs Memory, модели/effort, permissions/.claudeignore, MCP/Skills/субагенты/Agent Teams, checkpoints/rewind, автономный режим/RALPH-loop/worktrees, кросс-чек агенты). Синтезирован и сохранён wiki/synthesis/claude-code-checklist-postoyannogo-ispolzovaniya.md — не пересказ всех 30 пунктов, а приоритизированный чек-лист под контекст пользователя (ведение вики + вайбкодинг), с явным разделением "всегда / ситуативно / когда вырастет / осознанно не приоритет". Обновлены index.md.

## [2026-07-08] config | Настроен .claude/settings.json по практике из nikita-vels-claude-code-30-concepts
Deny на чтение/правку .env и подобных секретов (*.pem, *.key, id_rsa/id_ed25519, secrets/); allow на чтение файлов, git status/diff/log, запуск тестов; ask на установку/удаление пакетов, rm, curl/wget. Обновлена claude-code.md с пометкой "применено".

## [2026-07-08] lint | Проверка settings.json на конфликты с существующими разрешениями
Сверил новый .claude/settings.json с settings.local.json (личные gh repo/WebFetch правила — пересечений нет) и глобальным ~/.claude/settings.json (только плагины/тема — пересечений нет). Практический тест (dummy .env → Read) показал, что deny-правило НЕ заблокировало чтение в текущей сессии — вероятно, конфиг создан после старта сессии и не подхвачен. Обновлена claude-code.md пометкой "не подтверждено практикой", нужна перепроверка после перезапуска Claude Code.

## [2026-07-08] lint | Повторный тест settings.json после перезапуска сессии
Перепроверка теста из записи "[2026-07-08] lint | Проверка settings.json на конфликты" — тогда deny-правило не сработало, так как конфиг был создан в уже открытой сессии. После перезапуска сессии повторный тест всех трёх категорий (deny на `.env`, allow на `git status`, ask на `rm -rf`) дал ожидаемый результат — правила реально работают. Гипотеза о перечитывании конфига только при старте новой сессии подтвердилась. Обновлены: wiki/entities/claude-code.md (снята пометка "не подтверждено практикой"), wiki/projects/jarvis-personal-wiki.md (добавлен раздел "Тест правил permissions").

## [2026-07-08] query | Плагин VS Code для статуса Claude Code из видео Никиты Велса
Пользователь спросил про плагин VS Code, выводящий статус Claude Code, упомянутый в [[nikita-vels-claude-code-30-concepts]] ("Концепт 29"). Проверка raw-транскрипта показала: видео названия инструмента не даёт — автор делится скриптом только через личный Telegram, и это не VS Code-плагин, а нативная statusline-фича самого Claude Code (`settings.json` → `statusLine`). По запросу пользователя найден по названию `claude-statusline` конкретный репозиторий (github.com/nilbuild/claude-statusline, ⭐1324), подтверждён напрямую через GitHub API из-за расхождения repo owner/npm namespace в README. Создано: wiki/entities/claude-statusline.md (с пометкой "открытый вопрос" — совпадение по функциональности с видео не равно подтверждённому авторству). Обновлены: wiki/entities/claude-code.md (добавлен раздел "Кастомный статус-бар"), index.md.

## [2026-07-08] lint | Проверка безопасности claude-statusline перед установкой
По запросу пользователя разобран код инструмента [[claude-statusline]] на скрытые закладки перед тем, как он его установит. Файлы получены напрямую (raw GitHub API + npm tarball), прочитаны как текст без исполнения, проанализированы вручную (не через ИИ-суммаризацию — риск влияния возможных prompt-инъекций в самом коде). Итог: закладок/эксфильтрации не найдено — install.js чистый, statusline.sh обращается только к официальному api.anthropic.com за данными о лимитах, используя тот же OAuth-токен, что хранит сам Claude Code. Дополнительно сверен npm-пакет (@kamranahmedse/claude-statusline@1.0.6) побайтово (SHA256) с кодом на GitHub — расхождений нет, подмены при паблише не произошло. Обновлена wiki/entities/claude-statusline.md (раздел "Проверка безопасности").

## [2026-07-08] project | Установка claude-statusline на машину пользователя
По запросу пользователя выполнена установка `npx @kamranahmedse/claude-statusline` после проверки безопасности из предыдущей записи. Столкнулись с false-negative проверкой зависимостей установщика в нативной PowerShell (Unix-style `which` не находит даже реально присутствующие `curl`/`git`) — обошли запуском через Git Bash. `jq` на машине отсутствовал, поставлен через `winget install jqlang.jq`; обнаружено, что WinGet Links-каталог уже в persistent user PATH, но не подхватывается уже открытыми сессиями до перезапуска. Обновлены wiki/entities/claude-statusline.md (раздел "Установка") и wiki/projects/jarvis-personal-wiki.md.

## [2026-07-07] decision | Не разделять vault на две темы
По просьбе пользователя решил вопрос из [[one-vault-one-project-rule]] самостоятельно: оставляем один vault для изучения ИИ и рабочих проектов. Обоснование: это одна предметная область с постоянным перетоком знаний в обе стороны, а не несвязанные темы, для которых правило "одна база — один проект" задумано; проблема масштаба пока не актуальна при текущем объёме вики. Зафиксированы триггеры для пересмотра (рост объёма, конфиденциальные клиентские данные, расхождение тем на практике). Обновлены: wiki/projects/jarvis-personal-wiki.md, wiki/concepts/one-vault-one-project-rule.md.

## [2026-07-08 — 2026-07-09] project/query/decision | Работа над отдельным личным проектом (10 записей)
По запросу пользователя (2026-07-10) эти записи перенесены в отдельный локальный файл (гитигнорится, не в GitHub) — проект не должен быть виден в репозитории вики никому, кому даётся доступ к нему. Здесь оставлена только ссылочная строка, чтобы не терять сам факт хронологии.

## [2026-07-09] ingest | Практические правила создания Claude Skills вместо промтов
Продолжение сессии: изначально пользователь принёс PDF-конспект "Инженеры Anthropic не пишут промты. У них 4 правила" (бренд "HOOK") и попросил пошагово (с паузами на подтверждение) изучить его, найти первоисточник, вывести результат. Найден первоисточник — доклад Barry Zhang & Mahesh Murag "Don't Build Agents, Build Skills Instead" на AI Engineer Code Summit (25.11.2025); одна цитата ("Eric, Anthropic Engineering" про bare-bones tools) осталась неподтверждённой ни в одном проверенном источнике. Затем пользователь запросил углублённое практическое исследование темы "создавать скиллы вместо промтов" — с явным указанием искать не только в вики, а во внешних источниках (блог Anthropic, GitHub, Habr).

Прочитаны и засинтезированы: инженерный блог Anthropic ([[anthropic-official-skills-docs]] — progressive disclosure архитектура), официальный мета-скилл `anthropics/skills/skill-creator` (description-триггер, чеклист готовности, частые ошибки), документация Claude Code (эвристика "когда создавать скилл", локации/приоритет, монорепо), два практических разбора на Habr ([[habr-claude-skills-practical-guide]] — 9 категорий скиллов из практики Anthropic, лайфхаки вроде раздела "Gotchas" и `config.json`, не описанные в официальных доках).

Создано 4 страницы `wiki/sources/`: [[hook-4-pravila-claude-skills]] (исходный PDF, с явной пометкой про неподтверждённую цитату), [[anthropic-code-summit-build-skills-talk]] (первоисточник-доклад), [[anthropic-official-skills-docs]] (официальная методология), [[habr-claude-skills-practical-guide]] (практика сообщества). Синтезирован главный концепт [[skill-authoring-practical-rules]] — единая страница практических правил (description как триггер, три слоя SKILL.md, правило 500 строк, композиционность вместо монолита, итеративное накопление по сессиям, тестирование with/without, частые ошибки, универсальность принципа за пределами Claude Code). Обновлена [[claude-skills]] (бамп "Актуально на", ссылка на новую методологию, авторы фичи). Raw-материалы: PDF скопирован в `raw/sources/hook-4-pravila-claude-skills.pdf`, выдержки веб-исследования сохранены в `raw/sources/anthropic-skills-practical-research-2026-07-09.md`.

## [2026-07-09] ingest | Автономный запуск: MCP 2026-07-28 spec RC + Claude Agent SDK overview + Claude Code changelog snapshot
Автономный ежедневный запуск без пользователя рядом (по расписанию). Найдены и приняты 3 официальных материала, закрывающие реальные пробелы в вики — тема "agentic-паттерны (MCP, Claude Skills, Agent SDK)" была заявлена как ключевая, но у MCP и Agent SDK как таковых не было отдельных страниц (только упоминания вскользь).

1. **[MCP 2026-07-28 Specification Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/)** (официальный блог Model Context Protocol) — крупнейшая ревизия протокола с момента запуска: протокол становится stateless (убран handshake и `Mcp-Session-Id`, масштабирование за обычным round-robin балансировщиком), новое расширение MCP Apps (server-rendered UI в sandboxed iframe), Tasks вынесены из core в расширение, авторизация приближена к OAuth 2.0/OIDC, формальная политика депрекации. Создано: `wiki/sources/mcp-2026-07-28-spec-release-candidate.md`, новый концепт `wiki/concepts/mcp-model-context-protocol.md` (первая полноценная страница про сам протокол — раньше был только вскользь упомянут в нескольких source-страницах).
2. **[Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)** (официальная документация Anthropic) — Claude Agent SDK как библиотека Python/TypeScript, дающая тот же agent loop/инструменты/context management, что у Claude Code, для встраивания в CI/CD и продакшн-приложения; сравнение с Client SDK, CLI и Managed Agents. Создано: `wiki/sources/claude-agent-sdk-overview.md`, новая сущность `wiki/entities/claude-agent-sdk.md`.
3. **[CHANGELOG.md](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)** (репозиторий anthropics/claude-code, снапшот версий 2.1.172–2.1.205) — точечно обновляет уже зафиксированную в вики механику Claude Code: permission mode "default" переименован в "Manual"; субагенты теперь по умолчанию работают в фоне и могут вкладываться до 5 уровней; фоновые агенты теперь сами коммитят/пушат/открывают draft PR по завершении вместо того чтобы спрашивать; Agent Teams создаются неявно (убраны `TeamCreate`/`TeamDelete`); Claude Sonnet 5 получил нативное окно 1M токенов; Claude in Chrome вышел в GA. Создано: `wiki/sources/claude-code-changelog-snapshot-2026-07.md`.

Обновлена [[claude-code]] (бамп "Актуально на" до 2026-07-09, раздел "Практическая механика" синхронизирован с changelog-снапшотом, новая связь с [[claude-agent-sdk]] и [[mcp-model-context-protocol]]). Обновлена [[obsidian]] (ссылка на новый концепт MCP). Обновлён `wiki/index.md`. Raw-материалы сохранены в `raw/sources/{mcp-2026-07-28-spec-release-candidate, claude-agent-sdk-overview, claude-code-changelog-2026-07}.md`.

**Проверка безопасности источников:** ни в одном из трёх материалов не встретилось текста, похожего на инструкцию агенту (все три — официальная техническая документация/changelog, без пользовательского контента). Отдельно отфильтрован недостоверный вторичный тезис из веб-поиска (несколько SEO-блогов утверждали про смену биллинга Claude Agent SDK с 15 июня 2026) — на официальной странице документации этого нет, поэтому в вики как факт не внесён, зафиксирован только как "не проверено" в источнике.

Пропущено: отдельная entity-страница под конкретную версию модели (Claude Sonnet 5) — вне текущего охвата вики (она про инструменты/паттерны, не трекинг релизов моделей); факт про 1M-контекст зафиксирован внутри changelog-снапшота, а не как отдельная страница.

## [2026-07-09] ingest | Автономный запуск: Memory tool (Claude API) + harness-паттерны для долгоживущих агентов
Автономный ежедневный запуск без пользователя рядом. Проверен `CHANGELOG.md` Claude Code на новые версии после 2.1.205 (последний ингест) — новых записей нет, пропущено. Найдены и приняты 2 официальных материала, закрывающих реальные пробелы в теме "память/накопление знаний для LLM" и "agentic-паттерны".

1. **[Memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)** (официальная документация Claude Developer Platform) — встроенный в Messages API файловый инструмент памяти (`/memories`, шесть команд: view/create/str_replace/insert/delete/rename), клиент-сайд исполнение, just-in-time context retrieval, сочетание с context editing/compaction, обязательная защита от path traversal, паттерн multi-session software development (progress log + feature checklist + сквозная верификация перед тем как считать фичу готовой). Закрывает пробел в [[llm-memory-landscape]]: у Anthropic есть нативная альтернатива Mem0/Zep/Letta для тех, кто строит агента на своём API. Создано: `raw/sources/claude-memory-tool-docs.md`, `wiki/sources/claude-memory-tool-docs.md`, новый концепт `wiki/concepts/claude-memory-tool.md`.
2. **[Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)** (блог Anthropic Engineering, содержание — по совпадающим независимым пересказам, прямой WebFetch вернул 403) + **[github.com/anthropics/cwc-long-running-agents](https://github.com/anthropics/cwc-long-running-agents)** (официальный репозиторий-пример, прочитан напрямую) — три примитива для агентов, работающих над задачей через много сессий: Default-FAIL Contract (`PreToolUse`-гейт, требующий evidence перед тем как отметить успех), Fresh-Context Evaluator (независимый субагент без Write/Edit оценивает работу из "чистого" контекста), Agent-Maintained Handoff (`PROGRESS.md` + git-коммиты + `Stop`-хук вместо памяти модели). Плюс встроенная в Claude Code команда `/goal` как более лёгкая альтернатива без кастомных хуков. Создано: `raw/sources/anthropic-long-running-agent-harness.md`, `wiki/sources/anthropic-long-running-agent-harness.md`, новый концепт `wiki/concepts/long-running-agent-harness.md`.

Официальная документация Memory tool сама ссылается на статью про harness как на детальный кейс-стади своего раздела про multi-session разработку — оба материала описывают один и тот же паттерн (progress log + git recovery между сессиями) с двух сторон: как фичу API и как конкретный harness с хуками.

Обновлены: [[llm-memory-landscape]] (новый раздел про нативную альтернативу Mem0/Zep/Letta), [[vibecoding-full-workflow]] (ссылка на harness-паттерн для многосессионных проектов), [[claude-code]] (новый подраздел про `/goal` и harness), [[claude-agent-sdk]] (раздел "Паттерны поверх SDK"). Обновлён `wiki/index.md`.

**Проверка безопасности источников:** в обоих материалах не встретилось текста, похожего на инструкцию агенту — официальная документация и официальный репозиторий, без пользовательского контента. Единственный текст, напоминающий "инструкцию" — системная инструкция самого memory tool ("ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE... ASSUME INTERRUPTION"), но это описание API-фичи для чужих агентов, а не команда этой вики — трактовано корректно как саммари, не выполнено как инструкция.

Пропущено: третий материал не добавлен — после двух качественных официальных источников по заявленным темам дальнейший поиск (агентские паттерны за пределами Anthropic, вайбкодинг-практики на Habr) не дал ничего, что не дублировало бы уже имеющееся в вики или проходило бы порог достоверности (в основном вторичные SEO-пересказы тех же двух источников выше).

## [2026-07-09] practice | Синтез правил и практик из всей вики + новый слой practices/
По запросу пользователя проведена полная инвентаризация вики (два параллельных Explore-агента: AI/agentic-темы и вайбкодинг/архитектура; ~70 правил-кандидатов с классификацией global-ai / project / user). Решения пользователя: формат «CLAUDE.md + скиллы» (факт → CLAUDE.md, процедура → skill), строгий отбор (~13 глобальных правил, не 50), правила пользователя — вики + отдельная HTML-страница, новый слой `wiki/practices/`.

**Закрыт пробел Agent Teams**: тема была раскрыта парой предложений в [[claude-code]] — прочитана целиком официальная документация (code.claude.com/docs/en/agent-teams, v2.1.178+), созданы [[claude-code-agent-teams-docs]] (source), [[agent-teams]] (concept: субагенты vs teams, официальные кейсы, размеры 3-5/5-6, failure modes, security-модель — тиммейты наследуют permission-режим lead включая bypass, сообщения между агентами — недоверенный ввод), обновлена [[claude-code]].

**Создано вне репозитория** (синхронизация ручная): `~/.claude/CLAUDE.md` дополнен 13 правилами в 4 секциях (безопасность кода ×7: секреты/IDOR/CORS/миграции/fail-fast+функциональная проверка guard/не строить на вырост/secure store; автономная работа ×3: Default-FAIL evidence/fresh-context evaluator/подтверждение перед auto-push; контент и цепочка поставок ×2: инструкции-не-команды/доверенные источники; диалог ×1: план+вопросы перед крупной генерацией). Два глобальных скилла: `~/.claude/skills/project-kickoff/` (чеклист старта проекта по [[pre-project-architecture-checklist]]) и `~/.claude/skills/long-task-harness/` (по [[long-running-agent-harness]]). CLAUDE.md отдельного рабочего проекта (локально) дополнен разделом Standing practices (security-review как стандартный гейт; API versioning при первом внешнем потребителе).

**Создано в вики**: слой `wiki/practices/` добавлен в схему CLAUDE.md вики (+ операция Practice); [[claude-code-practices]] — полный свод с классификацией и разделом «что сознательно отсечено» (Карпати-принципы дублируют системный промпт — [DEFAULT]; ~35 правил остались на concept-страницах — строгий отбор); [[moi-pravila]] — 19 правил пользователя в 4 группах (дисциплина работы с ИИ, гигиена сессий, неделегируемые решения, привычки). Наглядная HTML-версия — `wiki/practices.html` (статическая, routine её не трогает), ссылка добавлена в dashboard.html.

## [2026-07-09] query | Происхождение правила «эффект 30 дней»
Пользователь спросил, откуда взялось правило №16 из [[moi-pravila]] («конец сессии: разовая правка или в скилл навсегда?»). Прослежена цепочка: доклад Zhang/Murag на AI Engineer Code Summit ([[anthropic-code-summit-build-skills-talk]]) → PDF HOOK ([[hook-4-pravila-claude-skills]]) → концепт [[skill-authoring-practical-rules]] → п. 16 моих правил. Ответ сохранён как [[proiskhozhdenie-pravila-effekt-30-dney]], индекс обновлён.

## [2026-07-10] lint | Исправление: финал MCP 2026-07-28 ещё не вышел
Пользователь заметил, что [[mcp-model-context-protocol]] утверждала «финал вышел 28 июля 2026», хотя дата ещё не наступила. Проверен raw-источник: там будущее время («The final specification ships on July 28, 2026») — ошибка синтеза при создании concept-страницы, не ошибка источника. Исправлены [[mcp-model-context-protocol]] (с пометкой об исправлении) и уточнена формулировка в [[mcp-2026-07-28-spec-release-candidate]]. Пояснено: `2026-07-28` — идентификатор версии спецификации (MCP версионирует спеки датой планового релиза).

## [2026-07-10] config | Настроены два регулярных автономных процесса поддержания вики
По запросу пользователя формализованы в постоянные процессы два вида работы, которые раньше выполнялись разово ("Автономный запуск" 2026-07-09): **(1)** разведчик практического материала, раз в 2 дня — целенаправленно ищет учебный/практический контент (туториалы, разборы инструментов, воркфлоу, официальные доки с практикой), а не новости/анонсы; находки высокой ценности помечает в новом разделе `⭐ Топ-находки` в начале `wiki/index.md#Sources` (маркер важности по выбору пользователя — отдельный раздел индекса, не трогает сами страницы источников). **(2)** ежедневное закрытие пробелов, по 1-2 темы за проход — работает по новому living-чеклисту `wiki/gaps-backlog.md`, использует только проверенные/первичные источники (та же дисциплина, что уже применялась 2026-07-09 при фильтрации SEO-блогов про биллинг Agent SDK).

Оба процесса зарегистрированы через навык `schedule` как cron-рутины (не через сессионный `CronCreate`, который истекает за 7 дней и не переживает закрытие сессии). `wiki/gaps-backlog.md` создан с тремя начальными пунктами: проверка биллинга Claude Agent SDK через официальную документацию (см. [[claude-agent-sdk]]), подтверждение авторства [[claude-statusline]], и свежий полный lint-проход (последний был 2026-07-07, вики с тех пор выросла более чем вдвое). `CLAUDE.md` дополнен двумя разделами, описывающими оба процесса (под Ingest и под Lint соответственно), чтобы будущие сессии знали об их существовании и не заводили параллельные механизмы. Обновлён `wiki/index.md`.

## [2026-07-10] ingest | Батч из 5 видео (Claude Code + Дзен, OpenCode, GSD & Superpowers, Claude Desktop-автоматизации, облачная инфраструктура)
Пользователь загрузил 6 новых markdown-файлов через Web Clipper в `raw/web-clipped/` (один не смог импортироваться в Obsidian напрямую — файл "OpenCode..." пришлось скачать вручную и положить рядом; технически на вики это никак не повлияло, файл читается так же). Обработаны как 5 источников — два файла "ОБЛАЧНАЯ ИНФРАСТРУКТУРА НА ПАЛЬЦАХ" оказались полными дублями одного видео (разница только в `fetched`-времени), взяты как один источник.

1. **[[woome-ai-dzen-content-automation]]** (канал [[woome-ai]]) — техника контент-фермы: агент-скрапер конкурентов → "система" из файлов вместо промта → параллельная генерация N статей → фильтр AI-детектором. Маркетинговое видео с продажей платного комплекта (`dzen.guru`, срочность в CTA) — взята только техническая часть, финансовые цифры не проверяемы. Создан концепт [[ai-content-farming-workflow]].
2. **[[zproger-opencode-review]]** (канал [[zproger]]) — практический обзор [[opencode]], мультипровайдерной open-source альтернативы Claude Code (~100 провайдеров, локальные модели, три интерфейса запуска, `AGENTS.md`, Skills/MCP на той же структуре, что Claude Code). Добавлен как альтернатива в [[claude-code]].
3. **[[vladilen-minin-gsd-superpowers]]** (канал [[vladilen-minin]]) — два живых кейса [[gsd-get-shit-done]] и [[superpowers]], агентских фреймворков полного SDLC поверх Claude Code/Codex (вместо 2 из 6 фаз у вайбкодинга — все шесть, через spec-driven декомпозицию, параллельных субагентов с ролями, self-check и human verification). Создан концепт [[agentic-sdlc-frameworks]]; [[vibecoding-full-workflow]] дополнен пометкой, что это следующая ступень зрелости, а не замена.
4. **[[nikita-efimov-claude-automations]]** (канал [[nikita-efimov]]) — детальный разбор четырёх способов автоматизации через Claude Desktop (Cowork Scheduler, Local Routines, Cloud Routines, `/loop`), включая лимиты по тарифу, catch-up-поведение и типы триггеров облачных рутин — ранее в вики эта механика была упомянута только вскользь в [[claude-cowork]]. Создан концепт [[claude-desktop-automation-modes]].
5. **[[prostodevops-cloud-infrastructure]]** (канал [[prostodevops]]) — не про ИИ, общие основы облачных вычислений (NIST-определение, IaaS/PaaS/FaaS/SaaS, гипервизоры/контейнеры/Kubernetes, специфика РФ — 152-ФЗ и отечественные ОС). Включено по уже принятому решению держать архитектурные основы для более осознанного проектирования вайбкодинг-проектов. Создан концепт [[cloud-computing-fundamentals]].

Создано 5 wiki/sources/*, 4 новых concepts, 8 новых entities (woome-ai, opencode, zproger, vladilen-minin, gsd-get-shit-done, superpowers, nikita-efimov, prostodevops). Обновлены [[claude-code]] (бамп "Актуально на" до 2026-07-10, два новых раздела механики, альтернатива OpenCode) и [[vibecoding-full-workflow]]. Обновлён `wiki/index.md`.

**Проверка безопасности источников:** все пять — обычные YouTube-описания с рекламой курсов/сообществ/партнёрских ссылок, инструкций в адрес ИИ-агента не найдено.

**Находка для пользователя:** два файла в `raw/web-clipped/ОБЛАЧНАЯ ИНФРАСТРУКТУРА НА ПАЛЬЦАХ/` — точные дубликаты одного видео; можно безопасно удалить один из них вручную в Obsidian, на вики это не влияет.

## [2026-07-10] ingest | Claude Code Model configuration docs — opusplan
Пользователь спросил, есть ли в Claude Code режим автоматического выбора модели по типу задачи (в продолжение вопроса про эвристику 80% Sonnet/20% Opus). Загружена официальная документация [[claude-code-model-config-docs]] (code.claude.com/docs/en/model-config). Ответ: да, `opusplan` — Opus в Plan Mode, автопереключение на Sonnet при выполнении; плюс два независимых автоматических механизма другой природы (fallback-цепочки при перегрузке, content-based fallback для Fable 5). Обновлена [[claude-code]] (раздел "Модели и Effort" дополнен точными формулировками, старое неточное "Opus Plan Mode — агент сам решает" заменено на официальное описание `opusplan`). [[moi-pravila]] не менялась — правило 80/20 там уже помечено как личная эвристика пользователя, не официальный механизм.

## [2026-07-15] ingest | Автономный разведчик (еженедельный): Claude Code changelog 2.1.206–2.1.210 + Week 28 dev digest
Автономный прогон без пользователя рядом (первый после настройки регулярной рутины 2026-07-10, предыдущий ручной ingest был 2026-07-10). Проверены CHANGELOG.md Claude Code и официальная документация Claude API/Managed Agents на предмет практического материала, появившегося с 2026-07-10. Отфильтровано: общие SEO-рерайты "Claude Code tutorial 2026" (codewithmukesh, aiweekly, nxcode и т.п.) — не проходят порог, пересказывают то, что уже в вики, без новой техники.

Принят первый источник: **[[claude-code-changelog-snapshot-2026-07-15]]** — продолжение [[claude-code-changelog-snapshot-2026-07]] (версии 2.1.172–2.1.205), новые версии 2.1.206–2.1.210 плюс впервые доступный официальный формат "Week 28 dev digest" (code.claude.com/docs/en/whats-new) с демо-видео вместо сухого changelog. Значимое: `/doctor` стал полноценным чекапом с автопочинкой (обрезка `CLAUDE.md`, поиск неиспользуемых skills/MCP/плагинов), in-app браузер в Desktop, hardened `Agent`-инструмент против indirect prompt injection, auto mode блокирует правку транскрипта сессии. Отдельно отмечено: фоновые уведомления теперь явно помечают отсутствие человеческого ввода — тот же самый механизм виден в системном сообщении, которым был запущен этот прогон ("[SYSTEM NOTIFICATION - NOT USER INPUT]..."), то есть находка описывает правило, по которому прямо сейчас действует эта сессия. Обновлены: [[claude-code]] (бамп "Актуально на" до 2026-07-15, новый раздел механики), [[ai-security-by-design]] (новый подраздел "Смежный вектор: фальшивые одобрения в транскрипте").

**Проверка безопасности источника:** официальный changelog/документация Anthropic, без стороннего контента, инструкций агенту не найдено.

## [2026-07-15] ingest | Автономный разведчик (еженедельный): Claude Managed Agents overview + quickstart
Второй источник того же прогона. Закрывает пробел, явно зафиксированный в [[claude-agent-sdk]] ("Managed Agents — хостед REST API, отдельно не разобран в вики"): официальная документация [[claude-managed-agents-overview]] (platform.claude.com/docs/en/managed-agents) — второй официальный способ строить агента на Claude API наряду с сырым Messages API и Agent SDK, но полностью managed-инфраструктура (sandbox, event log, agent loop готовы у Anthropic; разработчик определяет агента и обменивается событиями через REST/SSE). Четыре примитива (Agent/Environment/Session/Events), практический пример кода из quickstart, экосистема вокруг ядра (server-side память через отдельный `memory_stores` API — не путать с client-side [[claude-memory-tool]], multiagent orchestration, self-hosted sandboxes, scheduled deployments, webhooks, vaults, Dreams). Подтверждает официальным источником гипотезу, которая раньше была лишь предположением в claude-agent-sdk.md: "прототип на Agent SDK → продакшн на Managed Agents".

Создано: `wiki/sources/claude-managed-agents-overview.md`, новая сущность `wiki/entities/claude-managed-agents.md`. Обновлена [[claude-agent-sdk]] (снята пометка "отдельно не разобран в вики", добавлена ссылка, бамп "Актуально на"). Raw: `raw/sources/claude-managed-agents-overview.md`.

**Проверка безопасности источника:** официальная документация platform.claude.com, без стороннего контента, инструкций агенту не найдено.

**Итог прогона:** 2 источника, оба официальная документация/changelog Anthropic (не туториалы/разборы — таких, прошедших порог качества со времени 2026-07-10, не нашлось; отфильтрованы общие SEO-рерайты про "Claude Code tutorial 2026").

## [2026-07-15] config | Обновление dashboard.html + находка про отставание каталога
Обновлён dashboard.html последним, отдельным коммитом (дата, счётчики страниц 101/40/23/33, две новостные карточки за сегодня, новые/обновлённые строки в каталоге для трёх страниц этого прогона). Попутно обнаружено: каталог-дерево дашборда не обновлялся полноценно с 2026-07-09 — между тем прогоном и этим в вики добавилось ~20 entities/concepts/sources (батчи 2026-07-09 про Skills/MCP/Agent Teams/Model config и батч из 5 видео 2026-07-10), которых нет в `<details class="drawer">`-секциях. Не исправлено в рамках этого прогона (вне области "1-2 свежих источника" и риск ошибок при полной пересборке каталога без вычитки) — зафиксировано пунктом 4 в `wiki/gaps-backlog.md` для ежедневного процесса закрытия пробелов.

## [2026-07-15] ingest | Автономный разведчик (внеочередной второй прогон в тот же день): Dynamic Workflows — официальная документация
Второй прогон разведчика в один день (первый прошёл несколькими часами ранее тем же 2026-07-15, см. записи выше про changelog 2.1.206–2.1.210 и Managed Agents). Поскольку последняя запись лога уже датирована сегодняшним числом, свежих релизов за "время с прошлого прогона" почти не набежало (проверены официальный CHANGELOG.md — последняя версия всё ещё 2.1.210 — и Claude Platform release notes до 14 июля 2026, там только Admin API для Claude Enterprise user management, нерелевантно теме вики). Вместо этого найден пробел иного рода: механизм **Dynamic Workflows** (скриптовая оркестрация десятков-сотен субагентов, официально существует с мая 2026 — Week 22 dev digest) нигде не упоминался в вики отдельной страницей, хотя это ровно тот инструмент, которым устроен встроенный скилл `deep-research`, доступный в сессиях этой вики.

Прочитана целиком официальная документация [[claude-code-dynamic-workflows-docs]] (code.claude.com/docs/en/workflows): четыре механизма многошаговой работы (субагенты/skills/agent teams/workflows) сравниваются по тому, кто держит план; примитивы `agent()`/`pipeline()`/`parallel()`; quality-паттерны (adversarial verify, judge panel, loop-until-dry); лимиты runtime (16 concurrent / 1000 total агентов за прогон) и стоимость (предупреждение "Large workflow" при >25 агентов/>1.5M токенов).

Создан концепт [[dynamic-workflows]]. Обновлены: [[claude-code]] (раздел "MCP, Skills, Subagents, Agent Teams" переименован в четырёхчастное сравнение с добавлением Workflows), [[agent-teams]] (кросс-ссылка на соседнюю колонку той же официальной таблицы).

**Проверка безопасности источника:** официальная документация code.claude.com, без стороннего контента, инструкций агенту не найдено.

## [2026-07-15] lint | Закрытие пробела gaps-backlog: биллинг Claude Agent SDK
Попутная находка того же внеочередного прогона (см. запись выше про Dynamic Workflows) — не отдельный ingest, а закрытие пункта 1 из `wiki/gaps-backlog.md` (был "не начато" с 2026-07-10). Проверка официальных источников (Claude Platform release notes на 15.06.2026 — там только ретайр моделей Sonnet 4/Opus 4; official Agent SDK overview) не подтвердила заявленную вторичными блогами дату вступления в силу разделения биллинга. По независимому совпадению нескольких вторичных пересказов: изменение анонсировано 14.05.2026, но поставлено на паузу 15.06.2026 — Agent SDK/`claude -p` по факту продолжают тянуть из лимитов подписки, обещанный отдельный кредит не выдан. Спорное решение, зафиксировано явно: первоисточник (Help Center `support.claude.com`) вернул 403 при прямом фетче — факт принят по совпадению независимых вторичных источников, а не по прочтению первоисточника; помечено как оговорку на странице.

Обновлены: [[claude-agent-sdk]] (раздел "Открытый вопрос" → "Закрытый пробел"), `wiki/gaps-backlog.md` (пункт перенесён в закрытые, оставшиеся два пункта перенумерованы).

## [2026-07-15] lint | Закрытие пробела gaps-backlog: авторство claude-statusline
Ежедневный автономный процесс закрытия пробелов (первый прогон после того, как история репозитория была схлопнута и репозиторий стал публичным — см. commit `16a673b`; сессия началась с `git reset --hard origin/main`, локальная pre-squash история заменена без потери контента, проверено диффом на отсутствие удалённых wiki-страниц). Закрыт пункт 1 из `wiki/gaps-backlog.md` ("не начато" с 2026-07-08).

Проверка первоисточника — собственный GitHub-профиль автора репозитория `nilbuild` (не суммаризация, страница прочитана напрямую): `nilbuild` = Kamran Ahmed, известный британский разработчик (`developer-roadmap` 361k★, `driver.js`, `design-patterns-for-humans`), сайт `kamran.fyi`, 40.5k подписчиков. Ни в профиле, ни в README `claude-statusline` нет упоминаний русскоязычного контента, Claude Code туториалов или Telegram Никиты Велса. Вопрос закрыт в отрицательную сторону: связи с видео [[nikita-vels-claude-code-30-concepts]] нет, совпадение чисто функциональное.

Обновлены: [[claude-statusline]] (раздел "Открытый вопрос" → "Закрытый пробел"), `wiki/gaps-backlog.md` (пункт перенесён в закрытые, остался один открытый пункт — полный lint вики; пункт про отставание dashboard.html оставлен на следующий прогон как отдельная задача).

**Проверка безопасности источника:** GitHub-профиль и README прочитаны как обычный текст, инструкций агенту не найдено.

## [2026-07-15] config | Закрытие пробела gaps-backlog: каталог dashboard.html досверен с index.md
Второй пункт этого прогона (пункт 2 из `wiki/gaps-backlog.md`, зафиксирован предыдущим прогоном как отставание каталога с 2026-07-09). Не источниковый ingest — сверка `wiki/index.md` (актуальный полный список) с `<details class="drawer">`-секциями `wiki/dashboard.html` построчно по всем 5 разделам.

Обнаружено и исправлено: drawer-count везде уже был верным (авто-пересчитывался по стату), но сами `.tree-row` не дописывались построчно при добавлении новых страниц вне прогонов разведчика — отсутствовали 8 entities (woome-ai, opencode, zproger, vladilen-minin, gsd-get-shit-done, superpowers, nikita-efimov, prostodevops), 5 concepts (agent-teams, ai-content-farming-workflow, agentic-sdlc-frameworks, claude-desktop-automation-modes, cloud-computing-fundamentals), 7 sources (claude-code-agent-teams-docs, claude-code-model-config-docs, woome-ai-dzen-content-automation, zproger-opencode-review, vladilen-minin-gsd-superpowers, nikita-efimov-claude-automations, prostodevops-cloud-infrastructure), 1 synthesis (proiskhozhdenie-pravila-effekt-30-dney, drawer-count 3→4). Все — старые страницы (батч 2026-07-10), badge-new не проставлялся. Все целевые `.md`-файлы проверены на существование перед добавлением ссылок.

Обновлены: `wiki/dashboard.html`, `wiki/gaps-backlog.md` (пункт перенесён в закрытые — бэклог теперь пуст, следующий прогон должен выполнить полный lint-проход и пополнить список заново).

## [2026-07-16] ingest | Автономный разведчик (еженедельный): тихо — ничего не прошло порог качества
Прогон без пользователя рядом. Сессия началась с обнаружения расхождения: локальный клон контейнера был снят до схлопывания истории репозитория (см. запись 2026-07-15 про `git reset --hard origin/main`) и содержал устаревшую несвязанную историю на 2 коммита позади. Исправлено тем же способом — `git reset --hard origin/main` после сверки диффом, что контент не теряется (различия — только более новые страницы в origin и локальные Obsidian-конфиги, которых в origin нет намеренно).

Проверены источники за период с прошлой записи лога (2026-07-15) по сегодня:
- Claude Platform release notes — последняя запись 14.07.2026 (Admin API для Enterprise user management), уже отмечена нерелевантной в прогоне 2026-07-15; новых записей за 15–16.07 нет.
- Claude Code CHANGELOG.md — вышла только одна новая версия, 2.1.211: исключительно багфиксы и мелкие улучшения (флаги stream-json для subagent text/thinking, фиксы permission preview, auto mode, MCP-реконнект и т.п.), без новой именованной фичи. Week 29 dev digest ещё не опубликован — https://code.claude.com/docs/en/whats-new всё ещё показывает Week 28 (уже в вики).
- Общий веб-поиск (новости Claude, туториалы Claude Code, Hacker News/Reddit) — ничего датированного позже 2026-07-15 по существу: повторы уже описанных в вики релизов (Cowork web/mobile, Dynamic Workflows, Claude in Chrome beta) либо SEO-рерайты вида "Claude Code tutorial 2026" (codewithmukesh, aiworkflowcenter, skakarh, nxcode) — тот же паттерн, что уже отбрасывался в прогонах 2026-07-10/07-15.

Решение: ничего не добавлено. Единственный кандидат (patch-версия 2.1.211) отклонён как рутинный багфикс-релиз без практической техники — не проходит порог "значимый релиз/практика" из `CLAUDE.md`.

**Проверка безопасности:** источники не читались как контент для ingest, отдельной проверки не требовалось.

## [2026-07-16] lint | Свежий полный lint-проход вики

Ежедневный процесс закрытия пробелов. Единственный открытый пункт `wiki/gaps-backlog.md` требовал именно этого — свежего полного lint-прохода (предыдущий и единственный был 2026-07-07, вики с тех пор выросла более чем вдвое). Начало прогона также обнаружило и исправило то же расхождение локального клона с origin/main, что и в прогоне 2026-07-16 ранее сегодня (см. запись выше) — контейнер снова стартовал со стейт до предыдущего `git reset --hard origin/main`; исправлено тем же способом, диффом подтверждено отсутствие потери контента.

Механическая проверка: битые `[[wiki-links]]` — не найдено (3 ложных срабатывания grep-регекса на `[[CLAUDE.md]]`, `[[...]]`, `[[файлы]]` — первое устоявшаяся конвенция ссылки на файл вне `wiki/`, остальные — литеральный текст примеров, не ссылки). Страницы-сироты — не найдено, все 105 страниц имеют входящую ссылку.

Смысловая проверка (делегирована агенту, результат проверен): устаревшие "Актуально на" на продуктовых entity-страницах, противоречия между страницами, важные концепты/сущности без страницы, пробелы в данных, устаревшие утверждения в synthesis/practices.

Найдено и исправлено:
1. **[[moy-uroven-vladeniya-claude]]** — устаревший вывод. Страница (2026-07-09) перечисляла "нет облачных рутин по расписанию" как недостающее до уровня 5, но именно этот пробел был закрыт на следующий день, 2026-07-10 (настройка двух cron-рутин — еженедельный разведчик + ежедневное закрытие пробелов). Вывод переписан: пункт вычеркнут с пометкой даты закрытия и ссылкой на лог, список критериев уровня 5 приведён в соответствие с полным перечнем из [[five-levels-of-claude-mastery]] (добавлен пропущенный критерий Autodream), итоговый уровень (4) не изменился — закрыт 1 из 6 критериев уровня 5, а не переход целиком.
2. **[[claude-cowork]]** — не ссылалась на более подробный разбор автоматизации в [[claude-desktop-automation-modes]] (источник 2026-07-10, сам содержит фразу "дополняет [[claude-cowork]]", но обратной ссылки не было). Добавлен раздел "Механика автоматизации (детальнее)" и кросс-ссылки на концепт и источник [[nikita-efimov-claude-automations]].
3. **[[claude-skills]]** — не упоминала сравнение с [[dynamic-workflows]] (источник 2026-07-15, где Skills — один из четырёх сравниваемых механизмов многошаговой работы). Добавлена ссылка.

Проверено и не потребовало действий: `claude-code-checklist-postoyannogo-ispolzovaniya.md` (ссылается на тот же уровень 4 — актуально), entity-страницы `claude-projects`/`opencode`/`gsd-get-shit-done`/`superpowers` (без новых источников с 2026-07-10), `claude-code`/`claude-agent-sdk`/`claude-managed-agents` (2026-07-15, согласованы между собой и с более новыми источниками), биллинг Claude Agent SDK (согласован везде, где упоминается). Codex/Gemini упоминаются по 2 раза вскользь как кросс-чек-инструменты в источниках — ниже порога для отдельной страницы, страница не заведена (см. `wiki/gaps-backlog.md`, зафиксировано как проверенное, не пробел).

Обновлены: `wiki/gaps-backlog.md` (пункт lint перенесён в закрытые с деталями находок, бэклог полностью очищен), [[moy-uroven-vladeniya-claude]], [[claude-cowork]], [[claude-skills]].

**Проверка безопасности:** проверка собственных wiki-страниц, внешние источники не читались, отдельной проверки не требовалось.

## [2026-07-17] lint | Свежий проход по чеклисту (бэклог был пуст)

Ежедневный процесс закрытия пробелов. Бэклог `wiki/gaps-backlog.md` был полностью закрыт прошлым прогоном (07-16) — по протоколу выполнен свежий lint-проход вместо простоя. Ситуация отличается от 07-16: между прогонами не было ни одного нового ingest (разведчик 07-16 тоже ничего не нашёл), поэтому глубокая механическая/смысловая проверка делегирована агенту с явным фокусом на то, что НЕ перепроверялось в прошлый раз.

Проверено: битые `[[wiki-links]]` (чисто — 0, включая новые ложные срабатывания regex на `[[wiki-links]]`/`[[wiki-страницы]]` внутри log.md/gaps-backlog.md/dashboard.html, это цитаты и инструктивный комментарий, не ссылки), страницы-сироты (чисто — 0, все content-страницы имеют входящую ссылку), устаревшие "Актуально на" на продуктовых entity-страницах (чисто — новых релизов с 07-16 нет, флагов не найдено), противоречия между [[claude-agent-sdk]]/[[claude-code]]/[[claude-managed-agents]]/[[dynamic-workflows]]/[[agent-teams]] (чисто — биллинг, версии моделей, сравнительные таблицы согласованы), Codex/Gemini/GPT и другие повторяющиеся инструменты (Whisper/Notion/Vercel/n8n/DeepSeek) на предмет накопления упоминаний сверх порога отдельной страницы (чисто — без изменений с 07-16, все мимоходом внутри уже поглощённых источников).

Найдено и исправлено: [[jarvis-personal-wiki]], раздел "Следующие шаги" — пункт "закрыть открытый вопрос авторства [[claude-statusline]]" не был вычеркнут после фактического закрытия этого вопроса 2026-07-15 (см. запись лога и `wiki/gaps-backlog.md`, закрытые пункты). Страница обновлена (пункт помечен ~~зачёркнутым~~ со ссылкой на закрытие). Не источниковая правка — внутренняя сверка вики самой с собой.

`wiki/gaps-backlog.md` пополнен: поскольку механическая/смысловая проверка второй раз подряд вышла почти пустой, добавлен один содержательный пункт на следующий прогон — не задел вики, а сама повторяемость процесса: два подряд lint-прохода (07-16, 07-17) при отсутствии новых источников с 07-15 сигнализируют, что либо разведчик слишком строго фильтрует (стоит перепроверить критерий отсева), либо реально наступило затишье в релизах отслеживаемых тем — стоит явно решить, есть ли смысл продолжать ежедневный lint при пустом бэклоге, или переключаться на что-то более продуктивное (например, точечный ре-визит concept-страниц старше месяца на предмет углубления, а не только формальной проверки).

**Проверка безопасности:** проверка собственных wiki-страниц, внешние источники не читались, отдельной проверки не требовалось.

## [2026-07-19] ingest | Автономный разведчик (еженедельный): Claude Code changelog v2.1.211–2.1.214 + Week 29 digest

Прогон без пользователя рядом (сессия началась с `git checkout main && git pull origin main` — расхождений с origin не обнаружено, в отличие от прогонов 2026-07-16). Проверены источники за период с последней записи лога (2026-07-17, lint) по сегодня:
- Claude Code CHANGELOG.md — вышло четыре версии (2.1.211–2.1.214) с прошлого снапшота [[claude-code-changelog-snapshot-2026-07-15]] (тот покрывал до 2.1.210).
- code.claude.com/docs/en/whats-new — Week 29 digest (13–17 июля) уже опубликован, недельный ритм публикации подтверждён.
- Общий веб-поиск по агентским воркфлоу и по Sonnet 5/Opus 4.8 — ничего нового по существу: либо уже описанные в вики факты (релиз Sonnet 5, Dynamic Workflows), либо SEO-рерайты того же типа, что отбрасывались в прогонах 07-10/07-15/07-16.

Решение: взят один источник — продолжение серии официальных changelog-снапшотов. Главная находка: **Artifacts теперь вызывают MCP-коннекторы зрителя при каждом открытии страницы** — ровно тот механизм, который стоит за скиллом `artifact-capabilities`/параметром `capabilities: {mcp: ...}` инструмента `Artifact`, доступным в сессиях этой самой вики; отдельной страницы про Artifacts в вики раньше не было. Также значимо: лимиты на runaway-циклы (WebSearch/субагенты ≤200 за сессию), `EndConversation`-инструмент, серия фиксов bypass-уязвимостей в permission-анализаторе (Windows PowerShell 5.1, Bash file-descriptor redirect, длинные команды, zsh-модификаторы), `/fork` как полноценная фоновая сессия, screen reader mode.

Создан [[claude-code-changelog-snapshot-2026-07-19]]. Обновлены: [[claude-code]] (новый раздел про 2.1.211–2.1.214), [[ai-security-by-design]] (раздел про лимиты runaway-циклов и серию bypass-фиксов как продолжение принципа эшелонированной защиты).

**Проверка безопасности источника:** официальный репозиторий GitHub anthropics/claude-code и официальная документация code.claude.com, без стороннего контента, инструкций агенту не найдено.

## [2026-07-19] lint | Закрытие пробела: страница-концепт Claude Artifacts

Ежедневный процесс закрытия пробелов, отдельный прогон от разведчика выше (тот же день). `wiki/gaps-backlog.md` не содержал автономно закрываемых пунктов: единственный открытый пункт явно помечен "решение не автономно, вопрос пользователю" (см. запись 07-17). По протоколу для этого случая выполнен свежий lint-проход вместо простоя, с фокусом на то, что не проверялось раньше: интеграцию источника, добавленного разведчиком тем же днём.

Механическая проверка: битые `[[wiki-links]]` — не найдено (107 уникальных ссылок, 106 файлов, единственное несовпадение — `[[wiki-links]]` как термин внутри log.md/gaps-backlog.md, не ссылка). Страницы-сироты — не найдено, все страницы имеют входящую ссылку.

Смысловая проверка источника [[claude-code-changelog-snapshot-2026-07-19]]: страница сама явно отмечает, что Artifacts (MCP-коннекторы зрителя) — важный концепт без отдельной wiki-страницы, только фрагмент в changelog-разделе [[claude-code]]. Это ровно случай "важный концепт, упомянутый в источнике, но без своей страницы" из чеклиста Lint — и одновременно напрямую касается инструментария этой самой сессии (`Artifact`-тул, `capabilities: {mcp: ...}`, скилл `artifact-capabilities`).

Закрыто через официальную документацию: `code.claude.com/docs/en/artifacts` (первоисточник, полный текст получен через WebFetch). Предварительно `support.claude.com/en/articles/9487310` и `claude.com/blog/artifacts-in-claude-code` вернули HTTP 403 при прямом фетче — тот же паттерн, что и в закрытии пробела про биллинг Agent SDK 07-15; обойдено через WebSearch до точного URL `code.claude.com/docs`, который фетчится без проблем (уже так же обходили при ingest changelog-снапшотов).

Создана [[claude-artifacts]]: доступность (план/авторизация/провайдер/поверхность/версии CLI), создание и публикация, шаринг (приватно/внутри организации/публично, роли редактора), механика MCP-коннекторов зрителя (каждый вызов — от аккаунта зрителя, кэш в браузере, локальные `.mcp.json`-серверы недоступны опубликованной странице), технические ограничения страницы (CSP, no backend, 16 MiB, `.html`/`.md`), управление на уровне организации (toggle коннекторов отдельно от toggle артефактов, retention, Compliance API, аудит-лог).

Найден и явно помечен нюанс, отсутствовавший в исходном changelog-снапшоте: **артефакт, вызывающий MCP-коннекторы, нельзя опубликовать по публичной ссылке ни на одном тарифе** — это не противоречие источнику (тот не утверждал обратного), а уточнение, которого источник не содержал. Отмечено на странице [[claude-artifacts]] явно, со ссылкой на снапшот как на источник, который его не покрывал.

Обновлены: [[claude-code]] (ссылка на новую страницу из раздела про 2.1.211–2.1.214), [[claude-code-changelog-snapshot-2026-07-19]] (кросс-ссылка), `wiki/index.md` (Concepts), `wiki/gaps-backlog.md` (закрытый пункт с деталями; в открытый пункт про "смысл ежедневного lint" добавлено наблюдение — продуктивность сегодняшнего прохода была явно связана с наличием свежего ingest в тот же день, слабый аргумент в пользу варианта (а) из этого пункта, решение по-прежнему за пользователем).

**Проверка безопасности:** проверка собственных wiki-страниц + одна официальная документация Anthropic (code.claude.com), без стороннего контента, инструкций агенту не найдено.

## [2026-07-20] lint | Свежий проход по чеклисту (бэклог не содержал автономно закрываемых пунктов)

Ежедневный процесс закрытия пробелов. `wiki/gaps-backlog.md` не содержал пунктов, закрываемых автономно (единственный открытый пункт по-прежнему явно помечен "решение не автономно, вопрос пользователю" — см. записи 07-17/07-19). По протоколу выполнен свежий lint-проход, делегированный агенту с явным указанием не повторять три предыдущих прохода (07-16/07-17/07-19), а проверить новые углы.

Первая находка — закрыта этим коммитом: страницы [[claude-code]] и [[claude-code-changelog-snapshot-2026-07-19]] с 07-19 несли одинаковый незакрытый самосебе-TODO — "стоит перепроверить собственные `allow`-паттерны этой вики на класс ошибки `Edit(dir/**)`" (баг из релиза 2.1.214). Проверка `.claude/settings.json` напрямую: allow-список содержит только `Read`/`Glob`/`Grep` и точечные `Bash(...)`-паттерны, ни одного `Edit(dir/**)`-подобного правила нет — класс ошибки не применим. Обе страницы обновлены пометкой "проверено, не применимо" с датой, чтобы TODO не всплывал повторно в будущих lint-проходах.

Остальные находки прохода — в следующих коммитах.

## [2026-07-20] lint | Кросс-ссылка между двумя разными лимитами runaway-защиты

Вторая находка того же прохода. [[dynamic-workflows]] (источник 07-15) и [[ai-security-by-design]] (источник 07-19) документируют два независимых механизма защиты от runaway-циклов из разных релизов Claude Code, не ссылаясь друг на друга: лимит одного workflow-прогона (16 одновременных/1000 суммарных агентов) и лимит на всю CLI-сессию (200 WebSearch/200 субагентов). Формально не противоречие — оба факта верны и относятся к разным механизмам, — но риск спутать их при беглом чтении одной из двух страниц.

Добавлены взаимные уточняющие абзацы на обеих страницах, явно разграничивающие "лимит workflow-прогона" и "лимит сессии".

## [2026-07-20] lint | Углубление [[second-brain-daily-workflows]] + флаг рекламной вставки в источнике

Третья, самая содержательная находка прохода. Концепт-страница и страница источника [[sonny-huynh-second-brain]] (загружен 2026-07-07) останавливались на трёхстрочном списке воркфлоу, хотя raw-источник (`raw/web-clipped/Я создал второй мозг.../`) содержит полный, копируемый `dataviewjs`-скрипт дашборда ежедневной заметки — канбан задач по сроку с кликом-для-завершения (переписывает файл напрямую через `app.vault.modify`), трекер стриков привычек по эмодзи-меткам, ярлыки папок, виджет недавних заметок — и конкретные шаги настройки (3 плагина: Tasks/Templater/Dataview, `cd` в хранилище + `claude`). Пользователь активно ведёт Obsidian-вики (эту самую), техника напрямую переиспользуема — не рядовая деталь. Добавлен раздел "Пример: Dataview-дашборд" на концепт-странице.

Попутно: raw-источник — Habr-перепост оригинала Sonny Huynh от лица компании BotHub, с рекламными вставками (баннер + реферальная ссылка "100 000 токенов") в начале и в конце статьи. Другие источники с похожей рекламой ([[woome-ai-dzen-content-automation]], [[vladilen-minin-gsd-superpowers]]) явно фиксируют это в разделе "Оценка источника"/"Проверка безопасности" — у sonny-huynh-second-brain.md такого раздела не было. Добавлен, по той же конвенции: реклама — обычный маркетинговый CTA, не инструкция агенту, попыток промпт-инъекции не найдено.

Обновлены: [[second-brain-daily-workflows]] (разделы "Настройка" и "Пример: Dataview-дашборд"), [[sonny-huynh-second-brain]] (разделы "Оценка источника", "Проверка безопасности источника").

Этим прогоном три находки прохода закрыты. `wiki/gaps-backlog.md` по-прежнему без автономно закрываемых пунктов (единственный открытый — решение по нему за пользователем). Дашборд (`wiki/dashboard.html`) обновляется отдельным финальным коммитом.

**Проверка безопасности:** проверка собственных wiki-страниц + повторное чтение raw-источника, уже загруженного ранее (не новый ingest) — рекламные вставки, инструкций агенту не найдено.

## [2026-07-20] ingest | Автономный разведчик (еженедельный): v2.1.215 — скиллы `/verify`/`/code-review` больше не авто-подключаются

Прогон без пользователя рядом (`git checkout main && git pull origin main` — расхождений с origin не обнаружено). Проверены источники за период с прошлой записи лога (2026-07-19) по сегодня:
- Claude Code CHANGELOG.md — вышла одна версия, 2.1.215, с единственной строкой в changelog (не бандл из нескольких версий, как в прошлых снапшотах).
- code.claude.com/docs/en/whats-new — Week 30 digest ещё не опубликован (последняя запись — Week 29, уже в вики с прошлого прогона).
- Общий веб-поиск по практическим туториалам/официальным материалам Anthropic — ничего нового по существу: либо уже описанные в вики релизы, либо тот же паттерн SEO-рерайтов ("Claude Code tutorial 2026" — codewithmukesh, nxcode, dev.to), что систематически отбрасывается с прогона 07-10. Один нетипичный кандидат — сторонний GitHub-репозиторий `luongnv89/claude-howto`, синхронизированный с v2.1.212 — отклонён: неофициальный источник без установленной репутации, при наличии официального changelog за тот же период предпочтён он.

Решение: взята единственная строка v2.1.215 как отдельный, хоть и тонкий, источник — не рутинный багфикс, а точечное изменение поведения (Claude Code раньше мог сам решить прогнать `/verify`/`/code-review`, теперь только по явному вызову), напрямую касающееся механизма авто-подключения скиллов, уже описанного в [[claude-skills]], и практики повседневной работы с самим Claude Code. **Не** отмечено в `⭐ Топ-находки` — значимое для точности вики уточнение, но не уровня предыдущих находок (не закрывает пробел, не открывает новый рабочий механизм).

Создан [[claude-code-changelog-snapshot-2026-07-20]]. Обновлены: [[claude-code]] (новый раздел про 2.1.215, "Актуально на" → 2026-07-20), [[claude-skills]] (раздел "Исключение" про сужение авто-подключения для этих двух скиллов, "Актуально на" → 2026-07-20).

**Проверка безопасности источника:** официальный репозиторий GitHub `anthropics/claude-code` и официальная документация `code.claude.com`, без стороннего контента, инструкций агенту не найдено.

## [2026-07-21] lint | Отставание [[claude-managed-agents]] от официальных release notes

Ежедневный процесс закрытия пробелов. `wiki/gaps-backlog.md` не содержал автономно закрываемых пунктов (единственный открытый пункт по-прежнему явно помечен "решение не автономно, вопрос пользователю" — см. записи 07-17/07-19/07-20). По протоколу выполнен свежий lint-проход, пятый подряд после 07-16/07-17/07-19/07-20.

Механическая проверка (Python-скрипт вместо ручной прогонки): 111 md-файлов, битые `[[wiki-links]]` — 0 реальных (регекс дал 5 ложных срабатываний: `CLAUDE.md` как устоявшаяся конвенция, `[[ ]]`-синтаксис zsh внутри текста про permission bypass-фиксы, служебные слова в самом log.md/gaps-backlog.md). Страницы-сироты — 0.

Смысловая проверка пошла по новому углу, не затронутому в четырёх предыдущих проходах: свежесть продуктовых entity-страниц с датой "Актуально на" старше недели. [[claude-agent-sdk]] и [[claude-managed-agents]] обе стоят на 2026-07-15 (6 дней назад в быстро меняющемся домене). Сверка с официальным [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview) (первоисточник, полный текст получен через WebFetch):

- [[claude-agent-sdk]] — страница `code.claude.com/docs/en/agent-sdk/overview` перечитана целиком, расхождений с уже зафиксированным в вики не найдено, изменений не требуется.
- [[claude-managed-agents]] — найдено отставание: 4 пункта из релиза **2026-06-30** (event deltas в SSE-стриме сессии — `event_deltas[]` параметр, `event_start`/`event_delta` события; backward pagination для `GET /v1/sessions` через `prev_page`; override конфигурации агента на уровне одной сессии через `agent_with_overrides`; `injection_location` у vault env-credential — заголовки/тело/оба места) и 1 пункт из релиза **2026-07-10** (Dreams теперь явно поддерживает Claude Fable 5 и Claude Sonnet 5) не попали на страницу при её создании 2026-07-15 — то есть отставание образовалось не после ingest, а было уже в момент его. Раздел "Экосистема вокруг ядра" дополнен, добавлен отдельный раздел "Обновления с 2026-06-30", "Актуально на" → 2026-07-21.

Обновлены: [[claude-managed-agents]], `wiki/gaps-backlog.md` (новая запись в "Закрытые пункты").

**Проверка безопасности источника:** официальная документация `platform.claude.com/docs/en/release-notes` и `code.claude.com/docs/en/agent-sdk`, без стороннего контента, инструкций агенту не найдено.

## [2026-07-22] ingest | Автономный разведчик (еженедельный): Claude Code changelog v2.1.216–2.1.217 — `sandbox.filesystem.disabled`

Прогон без пользователя рядом (`git checkout main && git pull origin main` — расхождений с origin не обнаружено). Проверены источники за период с прошлой записи лога (2026-07-21, lint) по сегодня:
- Claude Code CHANGELOG.md — вышло две версии, 2.1.216 и 2.1.217, с прошлого снапшота [[claude-code-changelog-snapshot-2026-07-20]] (покрывал до 2.1.215).
- code.claude.com/docs/en/whats-new — Week 30 digest ещё не опубликован (последняя запись всё ещё Week 29, уже в вики).
- Claude Platform release notes — последняя запись 17.07.2026 (сворачивание legacy Workbench), новых записей за 18–22.07 нет; ничего релевантного теме вики.
- Общий веб-поиск по практическим туториалам/кейсам агентской автоматизации — тот же систематически отбрасываемый паттерн, что и в прогонах 07-10/07-15/07-16/07-20: SEO-рерайты ("Claude Code tutorial 2026" — nxcode, codewithmukesh, aiweekly, aiworkflowcenter, skakarh) и маркетинговые кейс-стади с непроверяемыми цифрами ("+35% продуктивности", без методологии) — ниже порога достоверности.

Решение: взят один источник — продолжение серии официальных changelog-снапшотов, на этот раз с содержательной находкой, а не рутинным багфиксом. Главное: **`sandbox.filesystem.disabled`** (2.1.216) — сэндбокс Bash-инструмента делит изоляцию на файловый и сетевой слои независимо; новая настройка отключает только файловый, оставляя сетевой allowlist в силе (раньше единственным способом снять файловые ограничения было `excludedCommands`, которое снимает и сетевые тоже). Официальная документация (`code.claude.com/docs/en/sandboxing`, прочитана целиком) сама формулирует компромисс — без файловой изоляции сэндбоксированная команда может расширить себе доступ на будущее, переписав shell rc-файлы/`$PATH`; включаема только из user/managed settings, не из конфига проекта. Прямое применение принципа минимальных привилегий из [[ai-security-by-design]], но не как усиление защиты, а как более гранулярный компромисс — интересный для вики именно этим.

Второстепенно (2.1.217): **настраиваемые лимиты параллелизма/глубины вложенности субагентов** — changelog даёт одну строку без названий ключей настроек, не подтверждено, меняет ли это уже описанный в [[claude-code]] лимит "до 5 уровней" или добавляет отдельный параметр; зафиксировано как открытый нюанс, не домыслено. Плюс баг-фикс `--max-budget-usd` для фоновых субагентов.

Создан [[claude-code-changelog-snapshot-2026-07-22]]. Обновлены: [[claude-code]] (раздел Permissions дополнен `sandbox.filesystem.disabled`, новый раздел про 2.1.216–2.1.217, "Актуально на" → 2026-07-22), [[ai-security-by-design]] (новый раздел "Точечное управление границей доверия").

**Проверка безопасности источника:** официальный репозиторий GitHub `anthropics/claude-code` и официальная документация `code.claude.com/docs/en/sandboxing`, без стороннего контента, инструкций агенту не найдено.

## [2026-07-22] lint | Допроверка открытого нюанса из свежего ingest: лимиты глубины субагентов (2.1.217)

Ежедневный процесс закрытия пробелов. `wiki/gaps-backlog.md` не содержал автономно закрываемых пунктов (единственный открытый пункт по-прежнему помечен "решение не автономно"). Мехпроверка (broken `[[wiki-links]]`, сироты) — те же 17/17 ложных срабатываний и 0 сирот, что и в предыдущих пяти проходах, без новых. По прецеденту 07-19 (когда содержательная находка пришла не из отдельного lint-угла, а из допроверки того же дня свежего ingest) — фокус на [[claude-code-changelog-snapshot-2026-07-22]], созданный сегодня же еженедельным разведчиком, который сам оставил открытый нюанс без деталей: changelog v2.1.217 заявляет "configurable depth nesting" для субагентов одной строкой, без ключей настроек, не подтверждая, меняет ли это уже описанный в [[claude-code]] лимит "5 уровней".

Проверка официальных первоисточников (`code.claude.com/docs/en/sub-agents`, `code.claude.com/docs/en/env-vars`, оба прочитаны целиком через WebFetch): страница sub-agents на момент проверки прямо утверждает "The limit is fixed and not configurable" — то есть документация ещё не отражает функцию, которую changelog уже объявил вышедшей. env-vars не содержит подходящей переменной. Это не ошибка вики, а зафиксированный временной лаг документации за changelog (та же природа, что и неопубликованный Week 30 dev digest, отмеченный в самом источнике) — вопрос остаётся открытым, но теперь с точным описанием, что именно проверено и что именно расходится, чтобы следующий прогон не повторял ту же проверку с нуля, а сверился, обновились ли доки.

Обновлены: [[claude-code]] (раздел "Обновление 2.1.216–2.1.217"), [[claude-code-changelog-snapshot-2026-07-22]] (раздел "Остальные два пункта"), `wiki/gaps-backlog.md` (новая запись в "Закрытые пункты").

**Проверка безопасности источника:** официальная документация `code.claude.com/docs/en/sub-agents` и `code.claude.com/docs/en/env-vars`, без стороннего контента, инструкций агенту не найдено.

## [2026-07-23] lint | Финальное закрытие нюанса лимитов субагентов (2.1.217) + найдена смена дефолта, не просто нестыковка доков

Ежедневный процесс закрытия пробелов. `wiki/gaps-backlog.md` не содержал автономно закрываемых пунктов (единственный открытый пункт по-прежнему помечен "решение не автономно"). Третий подряд визит к одному и тому же нюансу (07-22 → 07-22 допроверка → сегодня) — по накопленному прецеденту продуктивнее допроверять страницы с уже зафиксированным отставанием документации, чем гонять общий чеклист заново по кругу.

Официальная страница `code.claude.com/docs/en/sub-agents` (перечитана целиком через WebFetch) наконец обновилась под changelog v2.1.217 и дала полную картину — три раздельных лимита с тремя разными переменными окружения:
- **Глубина вложенности** (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`) — по умолчанию 0, субагент не может спавнить субагента, `Agent`-инструмент отдаёт ошибку.
- **Лимит на сессию** (`CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`) — 200 суммарно, без изменений с v2.1.212.
- **Лимит на параллельно бегущие** (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`, новый в 2.1.217) — по умолчанию 20 одновременно.

Важнее самого факта закрытия — что именно вскрылось при чтении: старый факт вики ("субагенты по умолчанию вкладываются до 5 уровней", источник — снапшот 2026-07-09) оказался не устаревшей формулировкой самого источника (это было верно на момент публикации), а **реальной сменой дефолтного поведения именно в v2.1.217** — сама официальная страница прямо это подтверждает отдельной врезкой ("From v2.1.172 through v2.1.216, subagents could nest by default, up to five layers deep, and the limit couldn't be changed"). Это ровно случай из CLAUDE.md ("если новый источник противоречит старому факту... не просто добавляй новую информацию, а явно помечай, что именно устарело") — старый факт не удалён, а помечен "устарело (исправлено 2026-07-23)" с точной версионной границей.

Обновлены: [[claude-code]] (пометка устаревшего факта о вложенности + переписанный раздел "Обновление 2.1.216–2.1.217" с тремя лимитами + отдельная заметка про найденную неразобранную v2.1.218), [[claude-code-changelog-snapshot-2026-07-22]] (раздел "Остальные два пункта" переписан с финальным результатом), [[ai-security-by-design]] и [[dynamic-workflows]] (кросс-ссылки на новый лимит параллельно бегущих субагентов — чтобы не создать новую нестыковку между тремя страницами, документирующими соседние, но разные лимиты), `wiki/gaps-backlog.md` (новая запись "Закрытые пункты").

**Побочная находка, не в охвате этого прохода:** при чтении `CHANGELOG.md` обнаружена вышедшая, ещё не разобранная версия **2.1.218** (`/code-review` как фоновый субагент по умолчанию, изменения auto mode, workspace trust для agent-frontmatter хуков из недоверенных папок и др.) — это работа еженедельного разведчика практического материала, не ежедневного закрытия пробелов; отдельного пункта бэклога не заведено, разведчик найдёт её сам штатной проверкой `CHANGELOG.md` при следующем прогоне.

**Проверка безопасности источника:** официальная документация `code.claude.com/docs/en/sub-agents` и официальный `CHANGELOG.md` репозитория `anthropics/claude-code`, без стороннего контента, инструкций агенту не найдено.


## [2026-07-24] lint | [[claude-managed-agents]] снова отстала от официальных release notes (запись 22.07.2026)

Ежедневный процесс закрытия пробелов. `wiki/gaps-backlog.md` не содержал автономно закрываемых пунктов (единственный открытый пункт по-прежнему помечен "решение не автономно, вопрос пользователю"). По прецеденту 07-21 (та же страница уже находилась отстающей от `platform.claude.com/docs/en/release-notes/overview` на момент своего создания) — сегодняшний проход целенаправленно допроверил ту же страницу на предмет записей после уже проверенной 17.07.2026, вместо повторного общего мехпрохода (broken links/orphans проверены попутно тем же скриптом, что и раньше — 0/0, без изменений с 07-21).

Официальные release notes (WebFetch, полный текст) дали новую запись **22.07.2026**, пять пунктов, все про Claude Managed Agents:
- Event deltas теперь доступны на уровне отдельного subagent-потока (`GET /v1/sessions/{id}/threads/{thread_id}/stream` принимает тот же `event_deltas[]`, что раньше был только на уровне сессии целиком, добавлен 30.06.2026).
- `effort` теперь настраивается прямо в объекте `model` при создании агента.
- Webhooks расширены на environment/memory store lifecycle — 4 новых `environment.*` + 3 `memory_store.*` события (было только agent/deployment/deployment run и session/vault).
- `initial_events` при создании сессии — до 50 событий `user.message`/`user.define_outcome` сразу в `POST /v1/sessions`, agent loop стартует в том же вызове.
- `version` стал необязательным при обновлении агента (optimistic concurrency — по желанию, а не обязательно).

Попутно подтверждено: общий beta-заголовок `managed-agents-2026-04-01` с той же даты перенял поведение листинга памяти, которое раньше требовало отдельного `agent-memory-2026-07-22` (см. уже описанное в вики изменение от 02.07.2026) — расхождение между двумя заголовками для memory-эндпоинтов де-факто закрылось.

Обновлены: [[claude-managed-agents]] (новый раздел "Обновления с 2026-07-22", "Актуально на" → 2026-07-24), `wiki/gaps-backlog.md` (новая запись в "Закрытые пункты").

**Проверка безопасности источника:** официальная документация `platform.claude.com/docs/en/release-notes/overview`, без стороннего контента, инструкций агенту не найдено.

## [2026-07-25] ingest | Автономный разведчик (еженедельный): запуск Claude Opus 5 + Claude Code v2.1.218–2.1.219

Прогон без пользователя рядом (`git checkout main && git pull origin main` — расхождений с origin не обнаружено). Проверены источники за период с прошлой записи лога (2026-07-24, lint) по сегодня.

Самая значимая находка с момента запуска этой вики: **24 июля 2026 Anthropic официально выпустила Claude Opus 5** (`platform.claude.com/docs/en/release-notes`, полный текст получен через WebFetch) — новый флагман, та же цена, что у Opus 4.8 ($5/$25 за MTok), 1M-контекст теперь единственный вариант (нет меньшего окна), thinking включён по умолчанию (breaking change: отключить можно только при effort `high` и ниже, на `xhigh`/`max` — ошибка 400). Anthropic прямо отмечает, что модель сама добавляет верификацию своей работы без просьбы — унаследованные с прошлых моделей инструкции "добавь шаг верификации" вызывают избыточную повторную проверку. В тот же день Claude Code CHANGELOG.md (два новых релиза — 2.1.218 и 2.1.219, с прошлого снапшота [[claude-code-changelog-snapshot-2026-07-22]]) показал, что **Claude Opus 5 сразу стала дефолтной моделью Claude Code** (v2.1.219), плюс: `/code-review` теперь фоновый субагент по умолчанию, `/deep-research` переведён на manual-only invocation (третье исключение из авто-подключения скиллов после `/verify`/`/code-review`), новая настройка `sandbox.network.strictAllowlist` (сетевой аналог `sandbox.filesystem.disabled`), workspace trust обязателен для хуков в agent-frontmatter из недоверенных папок, и — важно для практики самой этой вики — **официальный дефолт Dynamic Workflows сменился на medium/<15 агентов** (`workflowSizeGuideline`), что подтверждено напрямую в системном промпте текущей сессии, а не только по документации.

Отдельно зафиксировано, а не домыслено: changelog v2.1.219 заявляет ещё одну (уже третью) смену дефолта глубины вложенности субагентов — до 3 уровней. Официальная страница `code.claude.com/docs/en/sub-agents`, перечитанная целиком в этом прогоне, **не подтверждает** это число — всё ещё описывает дефолт как 0/выключено и не упоминает переход к 3. По протоколу вики (не переносить непроверенные числа как факт) — "3" не внесено на страницы, оставлено как открытый пункт `wiki/gaps-backlog.md` для быстрой допроверки следующим прогоном, по прецеденту 07-22/07-23, где аналогичный лаг документации закрылся за 1 день.

Помимо этого — Week 30/31 dev digest (`code.claude.com/docs/en/whats-new`) на момент прогона всё ещё не опубликован (последняя запись — Week 29); общий веб-поиск по практическим туториалам дал только уже привычный паттерн (сторонние обзоры Opus 5 вроде Lenny's Newsletter/VentureBeat/CodeRabbit — использованы только как второстепенный контекст в raw-снапшоте с явной пометкой "не первоисточник", в вики как отдельные источники не заносились).

Создан [[claude-opus-5-launch]]. Обновлены: [[claude-code]] (новый раздел "Обновление 2.1.218–2.1.219 + запуск Claude Opus 5", раздел "Модели и Effort", раздел Permissions, пометка открытого нюанса по глубине вложенности, "Актуально на" → 2026-07-25), [[claude-skills]] (расширен список исключений — `/deep-research`), [[dynamic-workflows]] (подтверждённый дефолт medium/<15 агентов), [[ai-security-by-design]] (`sandbox.network.strictAllowlist`, workspace trust для хуков, пометка открытого нюанса по глубине вложенности), `wiki/gaps-backlog.md` (новый открытый пункт).

**Проверка безопасности источника:** официальные `platform.claude.com/docs/en/release-notes`, `platform.claude.com/docs/en/about-claude/models`, официальный `CHANGELOG.md` репозитория `anthropics/claude-code`, официальная документация `code.claude.com/docs/en/sub-agents`. Инструкций агенту не найдено.

## [2026-07-25] lint | Ежедневное закрытие пробелов: нулевой результат, обе точки бэклога не готовы к закрытию

Ежедневный процесс закрытия пробелов (второй прогон сегодняшнего дня, после утреннего ingest еженедельного разведчика). `wiki/gaps-backlog.md` содержал два открытых пункта: (1) неподтверждённая доками смена дефолта глубины вложенности субагентов до 3, заведённая тем же утром еженедельным разведчиком; (2) вопрос "смысл ежедневного lint при пустом бэклоге", явно помеченный "не автономно".

По пункту (1): страница `code.claude.com/docs/en/sub-agents` перечитана повторно через WebFetch — без изменений за прошедшие часы, дефолт всё ещё описан как 0/выключено. Ожидаемо и неинформативно: документация не успевает обновиться за часы после публикации changelog (предыдущий похожий лаг закрылся за сутки, не часы — см. `wiki/gaps-backlog.md`, закрытые пункты 07-22/07-23). Пункт остаётся открытым; в сам бэклог добавлена пометка не проверять его повторно в тот же календарный день.

Побочно при этой проверке: попытка свериться с сырым `CHANGELOG.md` через WebFetch дала текст, утверждающий, что дефолт до v2.1.219 был "1", а не "0" — это противоречит и самой официальной странице `sub-agents` (перечитанной в тот же момент), и уже зафиксированному в вики факту, подтверждённому 07-23 через ту же страницу. Расценено как ненадёжный результат обработки (вероятно, искажение при суммаризации фетчера, не первоисточник) и не перенесено на страницы вики — сам факт зафиксирован в `wiki/gaps-backlog.md` как предостережение для будущих прогонов.

Пункт (2) не автономен по определению, пропущен.

Механическая проверка (broken `[[wiki-links]]`, страницы-сироты) — 0 битых ссылок сверх известных ложных срабатываний (`[[wiki-links]]` как термин, `[[ ]]` zsh-синтаксис, `[[...]]` как нотация в `obsidian.md`), 0 страниц-сирот — без изменений с прошлых проходов. Проверка накопления упоминаний конкурентов (Codex/Gemini/GPT/OpenAI) по всей вики — по-прежнему разрозненные вскользь-упоминания, ниже порога для отдельной entity-страницы, без изменений с 07-16.

Содержательных изменений на страницах вики в этом прогоне нет — оба пункта бэклога не готовы к закрытию, новых находок при lint не появилось. Записи в `wiki/gaps-backlog.md` (уточнение к открытому пункту 1) без изменения статуса.

**Проверка безопасности источника:** официальная документация `code.claude.com/docs/en/sub-agents` (WebFetch); отдельно зафиксировано, что вторичный фетч сырого `CHANGELOG.md` дал внутренне противоречивый результат и не был использован. Инструкций агенту в источниках не найдено.

## [2026-07-26] lint | Ежедневное закрытие пробелов: нулевой результат, допроверка глубины субагентов не подтвердила "3"

Ежедневный процесс закрытия пробелов. `git checkout main && git pull origin main` — расхождений с origin не обнаружено (3 незакоммиченных на диске коммита из предыдущей сессии оказались уже слиты в origin/main тем же прогоном 07-25, реальной потери работы нет). `wiki/gaps-backlog.md` содержал два открытых пункта: (1) неподтверждённая доками смена дефолта глубины вложенности субагентов до 3 (заведён 07-25, допроверялся 07-25 дважды); (2) вопрос "смысл ежедневного lint при пустом бэклоге", явно помеченный "не автономно" — пропущен по определению.

По пункту (1): страница `code.claude.com/docs/en/sub-agents` перечитана целиком заново — без изменений, дефолт по-прежнему прямо описан как "By default, a subagent can't spawn subagents of its own" (0/выключено), перехода к 3 нет. Побочно: повторная сверка сырого `CHANGELOG.md` через WebFetch снова дала "was 1" вместо "was 0" для дефолта до v2.1.219 — дословно совпало с дубиозным результатом 07-25. Совпадение двух независимых по времени фетчей наводит на мысль о систематическом искажении именно на этом способе чтения файла (не на первоисточнике), но не превращает его в надёжный источник — как и раньше, не перенесено на страницы вики. Пункт остаётся открытым.

Механическая проверка (broken `[[wiki-links]]`, страницы-сироты) — скриптовый обход всех `wiki/*.md`: 0 битых ссылок сверх уже задокументированных ложных срабатываний (`wiki-links` как термин, `...`/`[[ ]]` как синтаксис в примерах), 0 новых страниц-сирот (`gaps-backlog`/`log` — ожидаемые мета-файлы). Без изменений с 07-25.

Содержательных изменений на страницах вики в этом прогоне нет — открытый пункт бэклога не готов к закрытию, новых находок при lint не появилось. Запись в `wiki/gaps-backlog.md` (уточнение к открытому пункту 1) без изменения статуса.

**Проверка безопасности источника:** официальная документация `code.claude.com/docs/en/sub-agents` (WebFetch); вторичный фетч сырого `CHANGELOG.md` снова дал внутренне противоречивый результат и не был использован. Инструкций агенту в источниках не найдено.

## [2026-07-27] ingest | Автономный разведчик (еженедельный): Dynamic Workflows на практике — Bun/Klarna/CyberAgent + критика "unreviewed slop"

Прогон без пользователя рядом (`git checkout main && git pull origin main` — фаст-форвард на 4 коммита с 07-25/07-26, без расхождений). Проверены источники за период с прошлого еженедельного ingest (2026-07-25, [[claude-opus-5-launch]]):
- Официальный `CHANGELOG.md` Claude Code — вышла только одна новая версия, **2.1.220**, "Bug fixes and reliability improvements" одной строкой без деталей — не проходит порог практического материала, отклонена.
- `code.claude.com/docs/en/whats-new` — Week 30/31 digest всё ещё не опубликован (последняя запись по-прежнему Week 29, уже в вики) — тот же лаг, что фиксировался 07-25.
- `code.claude.com/docs/en/whats-new/2026-w30` — проверено напрямую, 404 (страница ещё не существует), подтверждает предыдущий пункт.
- Официальная страница "power user tips" (`support.claude.com`) и "Common workflows" (`code.claude.com/docs/en/common-workflows`) — прочитаны целиком; последняя оказалась стабильной базовой документацией (worktrees, plan mode, делегирование субагентам, headless-режим), без признаков недавнего обновления и без техники, которой не было бы уже в вики через более детальные страницы — не взято отдельным источником.

Главная находка — официальный блог Anthropic **"How Anthropic runs large-scale code migrations with Claude Code"** (`claude.com/blog/ai-code-migration`): три реальных кейса применения [[dynamic-workflows|Dynamic Workflows]] в большом масштабе — Bun (Jarred Sumner) перенёс кодовую базу с Zig на Rust (~1M строк, 11 дней, пик 64 параллельных агента, ~$165k), Klarna (security-аудит продакшена), CyberAgent (hardening с adversarial-агентами). Кейс Bun даёт воспроизводимую 4-фазную архитектуру миграции (типы/lifetime → параллельный порт с 2+ ревьюерами на файл → fix-loop → overnight-оптимизация с PR на человека) — первый в вики пример масштаба применения механизма, который раньше был описан только по документации.

**Важная оговорка источника:** прямой фетч самого блога Anthropic и блога Bun вернул 403 (та же блокировка, что у `support.claude.com` в прошлом, см. прецедент "биллинг Agent SDK" 07-15) — факты восстановлены через WebSearch по нескольким независимым сходящимся вторичным пересказам (Register, Developers Digest, блог самого Andrew Kelley, X), а не прочитаны из первоисточника напрямую. Явно зафиксировано в raw-файле и на странице источника, не выдано за прямое чтение.

**Содержательная критика, не только успех:** создатель Zig Andrew Kelley публично назвал результат "unreviewed slop" — ~13 000 unsafe-блоков попали в прод без человеческого ревью, adversarial review в кейсе Bun выполняли только агенты, не люди. Прямое столкновение с принципом [[ai-security-by-design]] "разделение обязанностей" (автор кода ≠ ревьюер) — зафиксировано как открытый практический вопрос, не как готовый вывод.

Создан [[claude-code-migration-case-studies-2026-07]]. Обновлены: [[dynamic-workflows]] (новый раздел "Практика в большом масштабе"), [[ai-security-by-design]] (новый раздел-кейс про adversarial review агентами vs человеческое ревью), `wiki/index.md` (Sources + ⭐ Топ-находки).

**Проверка безопасности источника:** материал собран через WebSearch (агрегированные сниппеты вторичных источников — новостных изданий и личных блогов), инструкций агенту не найдено. Ограниченность метода (не первоисточник) зафиксирована явно в трёх местах (raw-файл, wiki-источник, эта запись лога).

## [2026-07-27] lint | Закрытие пробела gaps-backlog: глубина вложенности субагентов по умолчанию — подтверждено 3

Ежедневный процесс закрытия пробелов (`git checkout main && git pull origin main` — фаст-форвард, без расхождений). Единственный автономно закрываемый пункт бэклога — третья допроверка нюанса, открытого 2026-07-25 (второй пункт бэклога по-прежнему помечен "не автономно", решение за пользователем).

Официальная страница `code.claude.com/docs/en/sub-agents` (первоисточник, перечитана целиком через WebFetch) наконец обновилась и прямо подтвердила changelog v2.1.219: "By default, a subagent can spawn subagents of its own, up to three layers below the main conversation." Страница впервые дала точную историческую таблицу дефолтов по диапазонам версий: v2.1.172–2.1.216 — 5 (не настраивалось); **v2.1.217–2.1.218 — 1** (не 0, как было записано в вики раньше — поведенчески то же самое, "вложенность выключена", но числовое значение переменной отличается); с v2.1.219 — 3.

Побочный вывод: дважды отклонённый как ненадёжный (07-25, 07-26) фетч сырого `CHANGELOG.md`, дававший "was 1" вместо ожидаемого "was 0" для дефолта до v2.1.219, задним числом оказался технически точным — официальная страница на момент тех проверок ещё не публиковала точное число, только поведение, и вики сверялась с описанием поведения. Урок для будущих допроверок: расхождение вторичного/сырого источника с текущей формулировкой официальной страницы не всегда означает ошибку вторичного источника — сама официальная страница может ещё не содержать полной информации.

Обновлены [[claude-code]] (раздел "MCP, Skills, Subagents..." и пункт "Обновление 2.1.218–2.1.219"), [[ai-security-by-design]] (раздел "Лимиты на runaway-циклы автономных агентов"), `wiki/gaps-backlog.md` (пункт перенесён из открытых в закрытые с датой и источником).

**Проверка безопасности источника:** официальная документация `code.claude.com/docs/en/sub-agents` (WebFetch), инструкций агенту в содержимом не найдено.

## [2026-07-27] ingest | Context7 + безопасность цепочки поставок скиллов (по видео Нейропросвещения)

Пользователь клипнул видео [[romaray-top-5-skills]] («Перестань СТАВИТЬ Claude Skills пачками. Рабочих всего 5», 2026-07-26) и попросил разобрать конкретно Context7. Сам источник по Context7 даёт ~50 секунд без техники, поэтому по прямой просьбе пользователя факты собраны **по первоисточникам**, а видео заингестено как повод и как отдельный (слабый) источник.

**Первоисточники по Context7:** официальная документация `context7.com/docs` и `context7.com/docs/clients/claude-code`, блог Upstash «Context7 Without Context Bloat» (07.01.2026), страница тарифов `context7.com/plans`, отчёт Noma Security о ContextCrush. Создана [[context7]]: механика (resolve-library-id → query-docs), январская переделка архитектуры с переносом реранкинга на сервер (9.7k→3.3k токенов, −38% латентности), два режима подключения (CLI/skill против MCP) с разницей в прозрачности установки, тарифы, ограничения.

**Главная содержательная находка — не Context7, а безопасность.** Единственный ценный блок видео (09:06) ссылался на исследование «4 000 скиллов, 36% уязвимы». Проверено по первоисточнику: это **ToxicSkills** от Snyk, срез на 05.02.2026 — 3 984 скилла с ClawHub и skills.sh, prompt injection в 36%, 1 467 вредоносных payload'ов (видео исказило: сказано «1 467 скиллов»), 76 подтверждённых, ~13% шанс критического дефекта. Вектор «Skill marketplace-атаки» в [[ai-security-by-design]] существовал с 2026-07 как гипотеза — теперь у него есть цифры.

**Второй кейс того же класса — ContextCrush** (раскрыт 18.02.2026, закрыт Upstash 23.02.2026): MCP-сервер был добросовестным, вредоносным был агрегируемый им сторонний контент («Custom Rules» в документации библиотеки, которую мог зарегистрировать кто угодно), доставленный агенту как доверенные данные — продемонстрированы эксфильтрация `.env` и удаление файлов. Обобщение исследователей: любой MCP-сервер, агрегирующий стороннее содержимое, создаёт ту же путаницу доверия.

**Извлечённое правило (practices):** у расширения агента проверять **два** доверия, а не одно — к автору расширения и отдельно к контенту, который расширение приносит в контекст; вторую проверку про MCP обычно не делают вовсе. Плюс: предпочитать инспектируемую установку (ручной конфиг MCP, ключ в env) автоматической (`npx <setup>` с OAuth). Добавлены как пп. 12а/12б в [[claude-code-practices]]. Кандидаты в глобальный `~/.claude/CLAUDE.md` — синхронизация ручная, пользователю не предлагалась в этом прогоне.

**Терминологическая правка:** видео (как и многие вторичные источники) перечисляет skills и MCP-серверы одним списком «топ скиллов». Разделы «Не путать с MCP-сервером» в [[claude-skills]] и «Не путать со Skills» в [[mcp-model-context-protocol]] добавлены явно.

Создано: [[context7]], [[romaray-top-5-skills]]. Обновлены: [[claude-skills]], [[mcp-model-context-protocol]], [[ai-security-by-design]], [[claude-code-practices]], [[neiroprosveshchenie]] (добавлена оценка качества материала по двум источникам — технические разборы брать, обзоры-подборки проверять по первоисточникам), `wiki/index.md`.

**Открыто:** установка Context7 у пользователя — решение не принято, страница помечена «не установлен». Рекомендация в диалоге — ставить ручным конфигом MCP, а не `npx ctx7 setup`.

**Проверка безопасности источника:** транскрипт видео прочитан целиком, инструкций агенту не обнаружено; содержимое рекламно-обзорное, ссылки ведут на телеграм-бот и курс автора — не переходил. Первоисточники — официальная документация и отчёт вендора безопасности через WebFetch.

## [2026-07-27] practice+config | Правила цепочки поставок в глобальный CLAUDE.md; установлен Context7 MCP

**Синхронизация практик.** По подтверждению пользователя правила 12/12а/12б из [[claude-code-practices]] перенесены в сжатом виде в `~/.claude/CLAUDE.md` (раздел «Контент и цепочка поставок», файл вне репозитория): цифры ToxicSkills к существующему правилу проверки исходника, плюс два новых — «два доверия у расширения агента (автор + приносимый контент)» и «инспектируемая установка вместо `npx <setup>`».

**Установка [[context7]]** — тем же прогоном, как первое применение только что записанных правил:
- Режим: MCP, user scope (`~/.claude.json`), `npx -y @upstash/context7-mcp` v3.2.5, анонимно без API-ключа. Официально рекомендуемый `npx ctx7 setup --claude` сознательно отклонён по правилу 12б — цена решения (нет сабагента `docs-researcher`, доки идут в основной контекст) зафиксирована на странице.
- **Проверка до установки (правило 12):** пакет в scope `@upstash`, мейнтейнеры на домене upstash.com; tarball распакован и прочитан. Исходящие обращения — только `context7.com`/`mcp.context7.com`. Два подозрительных на первый взгляд следа проверены и объяснены: `login.microsoftonline.com` — валидация JWT для Entra ID (enterprise SSO), `readFileSync` — собственный `package.json` и опциональный CA-сертификат из `NODE_EXTRA_CA_CERTS`. Redis-модуль требует явных `UPSTASH_REDIS_*` и в локальном stdio-режиме не задействован. Сканирования ФС и записи на диск нет.
- **Проверка после установки — функциональная, а не «connected».** Сервер поднят напрямую по JSON-RPC: `initialize` → `tools/list` → реальный `tools/call`. Запрос к `/sqlalchemy/sqlalchemy` про async-сессии вернул 4 508 символов (~1.1k токенов) корректной документации со ссылками на файлы репозитория — заметно ниже заявленного вендором среднего 3.3k.
- **Уточнение по документации вендора:** реальные имена инструментов — `resolve-library-id` и `query-docs`. Прежнее `get-library-docs`, которым полны вторичные гайды, отдаёт `-32602 Tool not found`. Страница [[context7]] исправлена по факту, а не по документации.

Инструменты Context7 станут доступны агенту после перезапуска сессии — MCP-серверы читаются на старте.

Обновлены: [[context7]], [[claude-code-practices]].

## [2026-07-27] ingest | Гайд по MCP от Web3nity — лестница подключения, каталоги, критерии проверки

Пользователь клипнул видео [[web3nity-mcp-guide]] («Как подключить ИИ-агента к чему угодно: полный гайд по MCP», 24.07.2026) с просьбой оценить, что применимо. Оценка дана до записи: **~70% содержания ниже порога** — объяснение работы LLM, что такое API (на примере такси), аналогия MCP с USB-C; всё покрыто [[mcp-model-context-protocol]] существенно глубже. Взяты три блока, каждый закрывает реальный пробел.

**1. Лестница подключения нового сервиса.** Встроенные плагины → раздел MCP в документации самого сервиса → каталоги → попросить агента собрать подключение. Процедуры «как подключить новый MCP» в вики не было вообще. Записана в [[mcp-model-context-protocol]] с наблюдением, которого в источнике нет явно: порядок ступеней совпадает с порядком убывания доверия.

**2. Каталоги — тоже белое пятно.** Видео называет `mcp.so` и официальный реестр. Проверено по первоисточнику: `registry.modelcontextprotocol.io` — настоящий официальный реестр, превью с 08.09.2025, поддерживают Anthropic/GitHub/Microsoft/PulseMCP, API заморожен на v0.1 с октября 2025, открытый (можно поднять совместимый суб-реестр). `mcp.so` — сторонний; в видео различие проведено корректно. Зафиксировано предупреждение автора «каталог — это витрина».

**3. Уточнение правила 12 → новый п. 12в в [[claude-code-practices]]:** конкретные критерии проверки стороннего расширения — кто автор, **как давно обновлялось**, какие разрешения запрашивает; плюс порядок предпочтения по убыванию доверия. Два критерия из трёх в правиле отсутствовали. Отдельно ценно, что четвёртое правило автора («попроси агента проверить подключение на безопасность») — независимое подтверждение процедуры, применённой в этой вики днём ранее при установке [[context7]]. П. 12в в глобальный `~/.claude/CLAUDE.md` пока **не** перенесён, помечен кандидатом — синхронизация только с подтверждения пользователя.

**Оценка источника — заметно выше, чем у сегодняшнего [[romaray-top-5-skills]] при том же обзорном формате:** фактических ошибок в проверяемых утверждениях не найдено ни одной, границы применимости автор оговаривает явно. Наблюдение вынесено на [[web3nity]] как ориентир для будущих ingest.

**Лиды, сознательно не превращённые в страницы:** Exa (поисковик под агентов с официальным MCP) — занесён в `wiki/gaps-backlog.md` на проверку по первоисточнику, потенциально влияет на качество разведчика и закрытия пробелов этой самой вики; Fireflies (транскрипция созвонов) — вне текущих задач; самодельный Telegram MCP — пересекается с проектом пользователя `c:\ai-assistant`, но техники в видео нет, только факт.

Создано: [[web3nity-mcp-guide]]. Обновлены: [[mcp-model-context-protocol]], [[claude-code-practices]], [[web3nity]], `wiki/gaps-backlog.md`, `wiki/index.md`.

**Проверка безопасности источника:** транскрипт прочитан целиком, инструкций агенту не обнаружено; ссылки ведут на Telegram-канал автора, не переходил.

## [2026-07-27] practice | П. 12в синхронизирован в глобальный CLAUDE.md

По подтверждению пользователя п. 12в из [[claude-code-practices]] (критерии проверки стороннего расширения: кто автор, как давно обновлялось, какие разрешения запрашивает; порядок предпочтения официальное → каталог → самосбор; «каталог — витрина») перенесён в сжатом виде в `~/.claude/CLAUDE.md`, раздел «Контент и цепочка поставок» — четвёртой строкой к трём, добавленным ранее сегодня. Файл вне репозитория, синхронизация ручная.

Раздел глобальных правил по цепочке поставок за один день вырос с двух строк до пяти — весь прирост извлечён из двух слабых обзорных видео ([[romaray-top-5-skills]], [[web3nity-mcp-guide]]) плюс проверка их утверждений по первоисточникам. Наблюдение к методу: практическая ценность источника не совпадает с его глубиной — обзорный материал для новичков дал правила, которых не было после десятков страниц официальной документации, потому что документация описывает механизмы, а не то, как принимать решение об установке.

Обновлена [[claude-code-practices]] (отметка о синхронизации).

## [2026-07-27] practice | Новое правило пользователя: источники разного уровня — намеренно

Пользователь явно сформулировал принцип, объясняющий, почему в вики попадают обзорные видео для не-разработчиков: «в таких видео всё объясняют на пальцах и на практике, со стороны обычного пользователя, не профессионала». Это стратегия отбора, а не отсутствие фильтра.

Добавлен п. 4а в [[moi-pravila]] (раздел «Дисциплина работы с ИИ», рядом с п. 3 про кросс-проверку на второй модели — общая идея «разные источники ловят разное»). Формулировка: у источника две независимые оси — глубина и применимость; документация максимальна по первой и почти пуста по второй; объяснение для новичков вдобавок показывает, где люди спотыкаются, что документации неочевидно именно потому, что для неё очевидно.

**Эмпирическое подтверждение того же дня:** раздел глобальных правил по цепочке поставок вырос с двух строк до пяти; три новые строки пришли из [[romaray-top-5-skills]] и [[web3nity-mcp-guide]] — двух источников, которые сама вики оценила как слабые, — и ноль из спецификаций MCP, разбиравшихся неделями.

**Корректировка собственной практики:** два сегодняшних разбора я открыл вердиктом «источник слабый, ~70% ниже порога» — мерил одной осью там, где их две. Оговорка про проверку фактов остаётся в силе и записана в само правило: видео заявило «1 467 вредоносных скиллов», в исследовании Snyk было «1 467 payload'ов» — претензия к конкретному утверждению, а не к источнику целиком.

Обновлена [[moi-pravila]]. Правило пользовательское, в `~/.claude/CLAUDE.md` не переносится (там правила для агента); в память сессий записано отдельно как поведенческая корректировка.

## [2026-07-27] practice | Уточнение п. 4а: усвояемость как предусловие применимости

Пользователь дополнил только что записанное правило: «важно не только то, что даёт источник, но и то, что я могу воспринять на своём уровне». Это третий фактор к двум осям источника (глубина / применимость) — и он относится не к источнику, а к принимающей стороне.

Содержательно это меняет формулировку правила: материал выше уровня восприятия не «более ценный», он просто не усваивается — усвояемость оказывается не бонусом к применимости, а её предусловием. Привязано к [[five-levels-of-claude-mastery]] и оценке [[moy-uroven-vladeniya-claude]] (уровень 4 из 5), чтобы «свой уровень» был не абстракцией, а зафиксированной точкой, которую можно пересматривать.

Добавлен противовес, которого в реплике пользователя не было, но без которого правило вырождается в отговорку: уровень восприятия — движущаяся цель. Источник чуть выше текущего уровня — рост, сильно выше — шум; фильтровать стоит второе. Признак заниженной планки — из источника ничего не приходится доучивать.

Обновлена [[moi-pravila]] (п. 4а).

## [2026-07-27] ingest | Пайплайн Matt Pocock: проверка по исходникам, пак установлен, Autopilot отложен

Пользователь принёс видео [[nickvels-mattpocock-pipeline]] ([[nikita-vels]], 26.07.2026) + сопроводительный пост из инбокса ассистента (`source: ai-assistant #13`) и попросил **проверить информацию**, а не просто заингестить. Видео и пост описаны одной страницей источника: пост содержит только ссылки и команды установки, отдельного содержания не несёт.

**Проверка по первоисточникам (GitHub API + чтение исходников скиллов), не по пересказу:**
- `mattpocock/skills` — подтверждён: 190 747 звёзд, 16 386 форков, MIT, создан 03.02.2026, последний push 23.07.2026. Все четыре скилла пайплайна на месте, плюс `tdd`, `code-review`, `wayfinder`.
- Tracer Bullet подтверждён дословно в `to-tickets/SKILL.md`.
- **Найдено в исходнике, но отсутствует в пересказе:** исключение для широких рефакторов (expand–contract вместо вертикальных срезов) — существенно, потому что именно там правило «каждый тикет — готовая фича» ломается. И установка пака как нативного плагина Claude Code через `.claude-plugin/marketplace.json`, без npm вообще.
- **Уточнение против источника:** «ручной запуск — слабое место» неверно как оценка. Это заявленный дизайн: `disable-model-invocation: true` во frontmatter `to-tickets` и `wayfinder`.
- **Ошибка источника:** `npx skills add mattpocock/skills` подаётся как установка пака Покока, но npm-пакет `skills` принадлежит `vercel-labs` (мейнтейнер `rauchg` — Guillermo Rauch, CEO Vercel). Лишнее звено в цепочке поставок, не раскрытое в источнике.

**Установка пака — тем же прогоном, по правилу 12б.** Выбран плагин-механизм Claude Code вместо `npx skills`: на одну третью сторону меньше, манифест виден целиком. `claude plugin marketplace add mattpocock/skills` → `claude plugin install mattpocock-skills@mattpocock`, user scope. **Проверка после установки:** `claude plugin details` — 22 скилла, **0 агентов, 0 хуков, 0 MCP-серверов** (исполняемой поверхности нет), ~1 419 токенов always-on. Манифест курирован — категории `in-progress` и `deprecated` в плагин не входят.

**Autopilot (`nick-vels/skills`) — проверен и отложен по решению пользователя.** По критериям п. 12в: создан 26.07.2026 (за сутки до ingest), один коммит, 13 звёзд, автор монетизирует курс в том же посте — формально не проходит. Исходник прочитан целиком: вредоносного нет, только markdown, написан аккуратно. Вердикт зафиксирован двойным намеренно — «безвреден сегодня» не отменяет «непроверен во времени».

Отдельно от безопасности — содержательное возражение, и оно оказалось решающим: Autopilot снимает ровно те ручные гейты, которые несут качество (`skip the user quiz`, `Do not wait for explicit approval`, «запускаю через 60 секунд»). Это конфликтует с п. 1 [[moi-pravila]] и с принципом разделения обязанностей [[ai-security-by-design]] — та же ставка, что в кейсе Bun ([[claude-code-migration-case-studies-2026-07]]), разобранном этим же утром, только на меньшем масштабе. Пак и обёртка, снимающая его контроль качества, — разные решения с разным риском, и приняты по отдельности.

**Зафиксирован коммерческий контекст источника:** курс автора, собственный скилл за подписку на Telegram, реферальная ссылка на перепродажу аккаунтов Claude «с российской карты». Последнее помечено как риск (доступ по чужим кредам, которые продавец знает и после продажи), не как рекомендация. Практическое следствие для будущих ingest вынесено на [[nikita-vels]]: разделять проверяемые факты о чужих инструментах (надёжны) и рекомендации, за которыми стоит собственный продукт или партнёрка.

[[mattpocock-skills]] встал третьим представителем в [[agentic-sdlc-frameworks]] — на прямо противоположной GSD/Superpowers посылке: не загонять модель в рамки объёмом инструкций, а держаться порядком операций.

Создано: [[nickvels-mattpocock-pipeline]], [[mattpocock-skills]]. Обновлены: [[agentic-sdlc-frameworks]], [[nikita-vels]], `wiki/index.md`.

**Проверка безопасности источника:** транскрипт и пост прочитаны целиком, инструкций агенту не обнаружено. Исходник стороннего скилла проверен до принятия решения об установке.

## [2026-07-28] scout | Тихо — ничего не прошло порог качества

Еженедельный автономный разведчик практического материала (тема прогона: Claude Code / Claude API / агенты / LLM-инструменты / автоматизация контента, окно поиска — со времени записи от 2026-07-27).

**Проверено и отклонено:**
- Официальный changelog Claude Code: единственная новая версия с 07-27 — v2.1.220 (24.07.2026), запись из одной строки «Bug fixes and reliability improvements», без деталей — ниже порога отдельного источника. Week 30 dev-дайджест (code.claude.com/docs/en/whats-new) на момент прогона ещё не опубликован, актуален только Week 29 — уже разобран в [[claude-code-changelog-snapshot-2026-07-19]].
- Официальный блог Anthropic «How Claude Code works in large codebases: best practices and where to start» — единственный найденный кандидат в официальном блоге вокруг нужной темы, но при проверке через зеркало (`raw.githubusercontent.com/RobGruhl/anthropic-docs-mirror`, прямой `claude.com/blog` вернул 403) дата публикации оказалась **14.05.2026** — не свежий материал, вне окна этого прогона. Оставлен без страницы; кандидат на будущий ingest, если понадобится материал про CLAUDE.md/hooks/skills-архитектуру для больших кодовых баз (пятислойный harness: CLAUDE.md → hooks → skills → plugins → MCP).
- Комьюнити-инструменты: `cxpak` (Barnett-Studios, Rust MCP-сервер для typed dependency graph, конкурент [[graphify]]) — 19 звёзд, 1 форк, дата создания не установлена уверенно; `cc-thinking-skills` — трекер awesome-list отметил «в пределах суток», но без независимого подтверждения даты и содержания. Оба ниже порога доверия для установки/страницы без более сильных сигналов (сравни с отказом от Autopilot 07-27 по тем же критериям — свежесть репозитория без истории).
- Русскоязычные источники (Habr: `llmstart` — «Готовим ИИ-агента к продакшену» и смежные статьи про production-паттерны агентов) — содержание похоже на релевантное (MCP-серверы, context management, PII, human-in-the-loop), но `habr.com` полностью отдаёт 403 через доступный WebFetch (сайт целиком, не только конкретная статья) — прочитать источник целиком не удалось, п. 1 операции Ingest не выполним, решено не гадать по одним сниппетам поиска.

**Спорное решение (по п. «безопасность» этого файла):** не форсировал ingest на основании одних поисковых сниппетов без прочтения полного текста источника — при недоступности WebFetch для Habr это означало бы саммари по чужому пересказу, а не по первоисточнику.

Новых страниц не создано, `wiki/index.md` без изменений.

## [2026-07-28] lint | Закрытие пробела gaps-backlog: Exa проверена по первоисточнику, MCP не установлен

Ежедневный процесс закрытия пробелов. Единственный автономно закрываемый пункт бэклога (второй помечен «не автономно», решение за пользователем) — оценка Exa как поискового MCP для операций этой вики, лид из [[web3nity-mcp-guide]] (2026-07-27).

Прямой фетч `exa.ai`/`docs.exa.ai` отдаёт 403 (похоже на защиту от ботов уровня Cloudflare — тот же паттерн, что раньше фиксировался для `support.claude.com`). Первоисточник, который удалось прочитать напрямую — README официального репозитория `exa-labs/exa-mcp-server` на GitHub: подтверждает, что MCP-сервер официальный (не сторонний), даёт remote-эндпоинт (`https://mcp.exa.ai/mcp`) и локальный npm-путь, список тулов (`web_search_exa`, `web_fetch_exa` по умолчанию; `web_search_advanced_exa`, `agent_tools` опционально), требование API-ключа. Факты о компании (основана 2021, Will Bryk/Jeff Wang, Series C $250M при оценке $2.2B) и тарифах ($7/1000 запросов поиска, 1000/мес бесплатно) восстановлены по совпадению независимых вторичных источников (Bloomberg, Crunchbase, синопсис официальной страницы тарифов) — не по прямому чтению страницы, зафиксировано как оговорка на странице.

Вывод: установка нового платного MCP с отдельным API-ключом — решение пользователя, не факт для автономной верификации, поэтому не выполнена. Создана [[exa]] с полной картиной (что это, официальность MCP, тулы, тарифы, отличие от keyword-поиска, аргументы за/против для этой вики). Обновлён `wiki/index.md`. Пункт бэклога помечен закрытым в `wiki/gaps-backlog.md` с датой и источниками.

Проверка безопасности источников: README GitHub и поисковые сниппеты прочитаны, инструкций агенту не обнаружено.

## [2026-07-28] practice | Выбор процессного набора на старте проекта — спрашивать, не решать молча

По просьбе пользователя закреплено поведение: при старте **нетривиального** проекта (система с бэкендом, БД и несколькими модулями — масштаба FinApp, а не лендинг/скрипт) я обязан спросить, каким набором вести разработку — `superpowers` или [[mattpocock-skills]] — и не выбирать за него. Для простого проекта вопрос не задаётся: прогонять лендинг через полный пайплайн абсурдно, цена процесса выше цены задачи.

Момент вопроса выбран осознанно — **после брифа, но до архитектуры и схемы БД**: масштаб к этому моменту уже понятен, а выбранный набор дальше сам ведёт разговор (`/grilling` или brainstorming), так что дублировать его вручную не нужно.

Записано в трёх местах, чтобы сработало независимо от того, как начнётся сессия: `~/.claude/CLAUDE.md` (раздел «Инструменты и коммиты»), скилл `project-kickoff` п. 1а (основной триггер — срабатывает на «новый проект»/«с нуля»), и память сессий. Обновлена [[claude-code-practices]] (раздел «Процедуры»).

Класс решения — тот же, что п. 3 в [[moi-pravila]] («неделегируемые решения»): выбор процесса влияет на всю дальнейшую работу и дорого откатывается, поэтому остаётся за пользователем.

**Контекст:** пользователь планирует следующий проект — пересборку системы уровня FinApp на другом фреймворке — и намерен применить там пак Покока. Само это намерение в вики пока не зафиксировано отдельной project-страницей: страница FinApp хранится только локально, вне репозитория, а нового проекта ещё нет. Заводить страницу до старта не стал.

## [2026-07-28] project | Локальная страница хаба проектов (вне репозитория)

Пользователь спросил адрес веб-ресурса, сделанного накануне, — в вики следов не было. Поиск по опубликованным артефактам ничего не дал, ресурс оказался локальным; нашёлся по транскриптам сессий другого проекта. Прецедент к правилу «искать по логу и памяти, прежде чем говорить, что записи нет»: здесь запись отсутствовала по-настоящему, потому что проект делался вне этой вики и в неё не попал.

Заведена страница проекта. **Лежит в `private/` — папка в `.gitignore`, на GitHub не уходит**, по явному требованию пользователя: страница перечисляет личные проекты с путями на диске, статусами и открытыми задачами, а репозиторий публичный. Проверено `git check-ignore` и `git ls-files` — файл не отслеживается и в `git status` не появляется.

`wiki/index.md`: обобщённая строка в разделе Projects уточнена — вместо «есть ещё один личный проект» теперь указано, что личные проекты описаны страницами в `private/`. Имён и путей в публичной части нет намеренно.

Побочно: `.playwright-mcp/` добавлена в `.gitignore` — снимки страниц и логи консоли от браузерного MCP не должны попадать в репозиторий (могут содержать контент открытых страниц).

## [2026-07-28] practice | Решён открытый вопрос бэклога: что делает ежедневная рутина, когда закрывать нечего

Единственный открытый пункт `wiki/gaps-backlog.md`, висевший с 07-17 с пометкой «не автономно», закрыт решением пользователя. Вопрос ставился как выбор: (а) смягчить фильтр отсева еженедельного разведчика или (б) при пустом бэклоге переключать ежедневную рутину на углубление старых concept-страниц.

Разбор прогонов 07-16…07-28 перед решением дал две вещи, которых на момент постановки вопроса не было:

- **Вариант (а) отклонён данными.** Гипотеза «фильтр слишком строг» родилась после единственного тихого прогона разведчика 07-16. С тех пор он находил материал в 5 прогонах из 7 (07-19, 07-20, 07-22, 07-25, 07-27), тихо было только 07-16 и 07-28. Смягчать нечего.
- **Нулевым был не lint целиком, а его механическая часть.** Битые `[[wiki-links]]` и страницы-сироты чисты 5+ проходов подряд (07-16, 07-17, 07-20, 07-21, 07-27) — ни одной находки. Всё содержательное давали прогоны, делавшие другое: допроверку по первоисточнику страниц, где прошлый прогон оставил открытый статус (07-22, 07-23, 07-24, 07-27), и фокус на свежем ingest того же дня (07-19, 07-22).

Принят вариант (б) в расширенной форме — приоритетный список в `CLAUDE.md` (раздел «Ежедневное закрытие пробелов»), до первого сработавшего: пункт бэклога → допроверка флагнутых страниц по первоисточнику → углубление concept-страницы старше месяца. Механический lint переведён с ежедневного на еженедельный.

Отдельно добавлен **кулдаун 3 дня на повторную допроверку одной и той же страницы** — из разбора нулевых прогонов 07-25 и 07-26: оба ломились в одну и ту же проверку глубины вложенности субагентов, пока официальная документация не обновилась (она обновилась только к 07-27). Без кулдауна самый продуктивный шаг вырождается в ежедневный долбёж одной ссылки.

## [2026-07-28] project | Вторая база знаний закрыта как дубль этой вики

Параллельное Obsidian-хранилище, заведённое **2026-07-07 — в тот же день, что и эта вики, и с той же целью** (ИИ: модели, агенты, RAG, промпт-инжиниринг; плюс вайбкодинг), проверено на дублирование и закрыто.

Дубль оказался не только тематическим, но и процессным — операции совпадали до названий: `/news-digest` = разведчик, `/atomize-inbox` = Ingest, `/vault-audit` = Lint, `40_MOC` = `wiki/index.md`, `last_verified` = «Актуально на».

Расхождение вскрылось не в замысле, а в том, что из этого выжило:

| | Закрытое хранилище | Эта вики |
|---|---|---|
| Контент | 1 сырой дайджест + 1 клиппинг, пять тематических папок пустые | 123 страницы, 43 источника |
| Последняя правка | 2026-07-07 (21 день назад) | ежедневно |
| Под версионным контролем | нет вообще | git + GitHub |
| Автоматика | скрипт, отработавший один раз | три облачные рутины, работают |

Уникального контента не нашлось: дайджест новостной и за три недели протух; тема клиппинга (`multica-ai/andrej-karpathy-skills`) раскрыта в [[llm-coding-guidelines]] и [[persistent-wiki-pattern]] — 7 упоминаний по вики; NotebookLM из его скрипта сбора новостей упомянут в 14 местах. Единственное, чего у этой вики нет, — **дневник обучения** (что прошёл, что понял): открытые вопросы ведёт `gaps-backlog.md`, хронологию — этот лог, но собственно дневника нет. Заведение отложено отдельной задачей: без ответа на «кто и когда его заполняет» он умрёт ровно так же, как умерло закрытое хранилище.

Содержимое (4 файла + 3 слэш-команды) лежит в `raw/sources/ai-knowledge-base-archive/` с README, объясняющим, почему ingest не требуется. Копии сверены с оригиналами побайтно до удаления папки.

**Вывод на будущее, шире одного случая:** два хранилища на одну тему — это не про удвоенный объём, а про то, что через месяц на один вопрос находятся два разных ответа и сверять их некому. Признак, по которому здесь принято решение, — не «где красивее структура», а где живой поток: коммиты, свежие правки, работающие рутины.

## [2026-07-29] lint | Допроверка флагнутой страницы: вторая статья про harness оказалась другим паттерном

Ежедневный процесс закрытия пробелов. `wiki/gaps-backlog.md` пуст (единственный исторический пункт закрыт 07-28) — по приоритетному fallback-списку из `CLAUDE.md` перешёл к шагу 2, допроверке страниц с открытым/флагнутым статусом по первоисточнику. Кандидаты: [[exa]] (403 на `exa.ai`/`docs.exa.ai`, проверена вчера 07-28 — под кулдауном 3 дня, пропущена) и [[anthropic-long-running-agent-harness]] (403 на `anthropic.com/engineering/...`, не проверялась с момента ingest 07-09 — вне кулдауна).

Прямой WebFetch на обе статьи блога снова вернул 403, включая попытку через `web.archive.org` (недоступен для WebFetch в этой среде). Но при попытке восстановить содержание второй статьи ("Harness design for long-running application development", 24.03.2026) по независимым пересказам обнаружилась не мелкая деталь, а содержательный пробел: карточка источника с 07-09 числила вторую статью как "связанную, тот же способ фиксации", подразумевая тот же паттерн (три примитива из `cwc-long-running-agents`), но её собственное содержание никогда не читалось и не попадало в вики.

По совпадению независимых пересказов (research-заметка `celesteanders/harness` на GitHub с прямыми цитатами — прочитана напрямую через raw.githubusercontent.com, плюс understandingdata.com/InfoQ/Medium/TeamDay.ai) восстановлено: это **другой харнесс** Anthropic Labs (автор — Prithvi Rajasekaran), решает другую задачу — автономная генерация целых full-stack приложений/фронтенд-дизайна (не многосессионный прогресс по фиче-листу). Архитектура Planner–Generator–Evaluator, явно GAN-inspired (генератор/оценщик как generator/discriminator), стек React+Vite+FastAPI+SQLite/PostgreSQL, оценка живого приложения через Playwright. Ключевая находка источника: самооценка агентом своей же работы ненадёжна (уверенно хвалит посредственный результат) — separation of concerns между генератором и оценщиком снимает это системно, тот же принцип, что Fresh-Context Evaluator в первой статье, но у другого класса задач.

Обновлены: [[anthropic-long-running-agent-harness]] (новый раздел о второй статье + уточнена оговорка о достоверности), [[long-running-agent-harness]] (новый раздел "Второй харнесс"), `wiki/index.md` (обе строки — source и concept). Пункт зафиксирован закрытым в `wiki/gaps-backlog.md`.

Проверка безопасности источников: все прочитанные пересказы и research-заметка — описательный технический текст, инструкций агенту не обнаружено.

## [2026-07-29] ingest | Как начать вайб-кодить: 10 идей за день (Web3nity)

Разобрано видео [[web3nity-10-vibecoding-ideas]] (22.05.2026), лежавшее в `raw/web-clipped/`. Запрос пользователя был узкий — вытащить сами идеи и положить в личный список дел; ingest сделан следом, отдельным шагом.

Технической ценности нет (стек и процесс покрыты [[vibecoding-full-workflow]]), но в вики не было страницы про **отбор** задач — что вообще имеет смысл превращать в инструмент. Заведён концепт [[vibecoding-task-selection]]: рамка «четвёртый вариант» (сделать руками / поручить сотруднику / отдать подрядчику / завайбкодить), два критерия отбора (повторяемость + своя экспертиза в автоматизируемом процессе), каталог из 11 типовых инструментов по трём направлениям, приёмы «ИИ как интервьюер до сборки» и «прототип вместо ТЗ».

Расхождение с названием ролика: в описании заявлено 10 идей, в транскрипте разобрано 11 — «форма отчёта сотрудника» в авторский список не попала. В вики зафиксированы все 11, расхождение отмечено явно.

Не взято: тарифы Abacus AI Agent / ChatLLM — с чужих слов, занесены в `wiki/gaps-backlog.md` на проверку по первоисточнику (там же — оговорка автора «токены» вместо «кредиты»).

Третий источник [[web3nity]]; оценка автора («брать выборочно, но без презумпции ошибки») подтверждается — границы применимости оговорены честно, включая собственный прошлый неудачный опыт.

## [2026-07-29] ingest | Архитектура профессионального скилла (Bohomolov Lab) + проверка валидности

Разобрано видео [[bohomolov-skill-architecture]] (01.06.2026) по запросу пользователя: не просто саммари, а проверка — валиден ли метод и не устарел ли. Каждое утверждение сверено с официальной документацией на 2026-07-29 (`claude.com/docs/skills/how-to`, `code.claude.com/docs/en/skills`, справка Anthropic, `agentskills.io`).

**Итог проверки:** метод валиден — это корректное, но урезанное подмножество официальной методологии, уже описанной в [[skill-authoring-practical-rules]]. Архитектурная часть (SKILL.md как карта, `references`/`scripts`/`assets`, progressive disclosure, композиционность, коннекторы) подтверждена полностью. Инженерной части (description как триггер, eval-цикл с baseline, `skill-creator`) в методе нет вовсе.

**Устарело одно центральное утверждение:** «файл в существующий скилл из чата дописать нельзя, нужно удалять и пересобирать целиком» — на нём автор потерял час за кадром. Сейчас справка описывает правку на месте через Edit with Claude, в том числе многофайловую за один проход. Момент перехода установить не удалось (справка не датирована) — зафиксирован факт на дату проверки, не дата изменения.

**Два уточнения, которых в вики не было** (в этом и ценность источника — не новые факты, а то, что вскрылось при проверке его утверждений):
- claude.ai режет `description` до **200 символов**, спецификация Agent Skills допускает 1024 — скилл по спецификации при загрузке в claude.ai придётся ужимать, причём ужимать ровно то, что отвечает за срабатывание;
- `dependencies` во frontmatter для скриптов с внешними пакетами — без объявления скилл работает только у автора.

Плюс приём самого автора, ранее в вики не сформулированный: вынося правила в отдельный файл, надо **явно запретить дублировать их обратно** в SKILL.md, иначе модель копирует «на всякий случай» и вынос теряет смысл.

Обновлены [[skill-authoring-practical-rules]] (три вставки + новый раздел «Правка существующего скилла»), [[claude-skills]] (уточнения по claude.ai, «Актуально на» → 2026-07-29), создана сущность [[bohomolov-lab]]. Не подтверждённый офдокой формат `.skill` («Save Skill в один клик») занесён в `wiki/gaps-backlog.md`.
