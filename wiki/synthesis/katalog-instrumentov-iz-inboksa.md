# Каталог инструментов из инбокса: «может пригодиться»

Вопрос пользователя 2026-10-19 при разборе инбокса ассистента: что делать с анонсами инструментов, которые сейчас не используются. Решение пользователя: **«не наш стек» — не причина отказа**, инструменты выбираются под задачи и интересы. Поэтому они не отбрасываются, а ложатся сюда строкой: первоисточник и одна фраза «что умеет». Полный разбор — когда появится задача.

Каталог — не рекомендация и не проверка. Цифры («в 50 раз быстрее», «99% задач») — заявления самих проектов, независимо не проверены. Перед установкой любого пункта — обычный порядок: прочитать исходник ([[ai-security-by-design]], [[zabor-i-stena-prava-agenta]]).

Первоисточники нашёл субагент (поиск), 4 из 15 перепроверены выборочно (`google/artemis`, `jangles-byte/Pythia`, `stablyai/orca`, `MiniMax-AI/minimax-code` — репозитории существуют, лицензии совпадают). Звёзды — на 2026-10-19.

## Агенты и оболочки для программирования

| Инструмент | Первоисточник | Что умеет | Лицензия |
|---|---|---|---|
| Cline Desktop | [docs.cline.bot](https://docs.cline.bot/getting-started/installing-cline) | Настольное приложение Cline для моделей с открытыми весами: параллельные сессии, задачи по расписанию, импорт сессий из Claude Code/Codex/OpenCode. macOS, Windows в бете | открытый код |
| MiniMax Code | [MiniMax-AI/minimax-code](https://github.com/MiniMax-AI/minimax-code) | Терминальный агент MiniMax: TUI, `mcode exec` для CI, режим ACP для редакторов, свой ключ к совместимому API. Замер «76,7% против 63,3% у Claude Code» в посте — тест самой компании на 30 задачах | MIT |
| Orca | [stablyai/orca](https://github.com/stablyai/orca) | Оболочка над несколькими CLI-агентами (Claude Code, Codex, OpenCode и др.): каждый в своём git worktree, один промпт — несколько агентов, сравнение и слияние лучшего | MIT |
| Pi в браузере | [HF Space](https://huggingface.co/spaces/deyunma/MiniCPM5-2B-WebGPU-Pi) | Агент для программирования целиком в браузере через WebGPU, модель MiniCPM5-2B (int4), ~1,84 ГБ при первой загрузке, без сервера | Apache-2.0 |
| tgrep | [microsoft/tgrep](https://github.com/microsoft/tgrep) | Поиск по коду для агентов: триграммный индекс, клиент-сервер со слежением за изменениями. Смысл — на больших кодовых базах | MIT |

## Управление устройствами

| Инструмент | Первоисточник | Что умеет | Лицензия |
|---|---|---|---|
| ARTEMIS (Google) | [google/artemis](https://github.com/google/artemis) | Инструкции на естественном языке → автоматизация Android, подключается к агентам по MCP. Заявленные 99%+ — самооценка проекта. При установке сам ставит службу специальных возможностей на телефон (выключается переменной `ARTEMIS_HELPER_AUTO_INSTALL=false`) | Apache-2.0 |

## Память, контекст, аудит решений агента

| Инструмент | Первоисточник | Что умеет | Лицензия |
|---|---|---|---|
| OpenViking | [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | Память, знания и навыки агента в одной файловой системе `viking://` с ls/read/grep, сводка у каждой папки. Сосед [[llm-memory-landscape]] | AGPLv3 |
| semantica | [semantica-agi/semantica](https://github.com/semantica-agi/semantica) | Решения ИИ как узлы графа с происхождением по W3C PROV-O, экспорт аудита. Не объясняет рассуждение модели — только фиксирует цепочку. Сосед [[invariant-vidno-znachit-zapisano]] | MIT |

## Локальные модели и данные

| Инструмент | Первоисточник | Что умеет | Лицензия |
|---|---|---|---|
| needle | [cactus-compute/needle](https://github.com/cactus-compute/needle) | Крошечная модель для малых устройств (бинарник 8–29 МБ, ~28 МБ памяти), главное — вызов инструментов и извлечение структуры | Apache-2.0 |
| Pythia | [jangles-byte/Pythia](https://github.com/jangles-byte/Pythia) | Локальный «оракул» на Ollama: 40+ бесплатных живых лент событий, глобус Osiris, прогнозы MiroFish, API для агента на localhost | MIT |

## Контент, дизайн, маркетинг

| Инструмент | Первоисточник | Что умеет | Лицензия |
|---|---|---|---|
| Animator | [ashishjamarkattel/Animator](https://github.com/ashishjamarkattel/Animator) | Объясняющее видео «рисование на доске» по промпту: сценарий, иллюстрации, озвучка Gemini TTS, MP4. Нужен ключ Gemini | не указана |
| Klyaksa | [klyaksa.vjpe.click](https://klyaksa.vjpe.click/), [каталог Glama](https://glama.ai/mcp/connectors/app.klyaksa/klyaksa) | Онлайн-доска, на которой агент рисует схемы через MCP. **Не подтверждено:** сайт при проверке отдал 404, описание — из поиска | не найдена |
| NotFair | [nowork-studio/NotFair](https://github.com/nowork-studio/NotFair) | Навыки агента для SEO, GEO и рекламы (Google Ads, Search Console, X/LinkedIn/Meta Ads, GA4, WordPress); по README 48 навыков, в посте 45. Сосед [[geo-ai-answer-visibility]] | MIT |
| Наборы иконок | itshover.com/icons, web.iconly.pro, nucleoapp.com, iconsax.io, isocons.app, hugeicons.com, morphicons.com, movingicons.dev/icons | Обычные, анимированные и стилизованные иконки для интерфейсов. **Сайты не открывались** — список из поста | — |

## Не опознано

- **«computer»** из топа репозиторий недели — «агент управляет компьютером». Однозначного совпадения нет; кандидаты `simular-ai/agent-s` и `suitedaces/computer-agent` не выбраны.
- **omarchy** из того же топа нашёлся ([omacom/omarchy](https://github.com/omacom/omarchy), Linux от DHH на Arch + Hyprland), но в посте он «минималистичный», а сам проект называет себя «opinionated» — описание поста не сходится, в каталог не внесён.

## Связи

- [[agent-harness]] — оболочки агентов (Orca, MiniMax Code, Cline Desktop)
- [[llm-memory-landscape]] — OpenViking
- [[zabor-i-stena-prava-agenta]] — порядок перед установкой
