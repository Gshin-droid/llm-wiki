# Effective harnesses for long-running agents (блог + репозиторий-пример)

**Источники:**
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (блог Anthropic Engineering — содержание получено через агрегированные пересказы, прямой WebFetch вернул 403)
- [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps) (связанная статья, тот же способ фиксации)
- [github.com/anthropics/cwc-long-running-agents](https://github.com/anthropics/cwc-long-running-agents) (официальный репозиторий с реализацией — прочитан напрямую, первичный источник для деталей ниже)

**Загружено:** 2026-07-09
**Raw:** `raw/sources/anthropic-long-running-agent-harness.md`

## Саммари
Официальный паттерн Anthropic для агентов, работающих над задачей часы/дни через много отдельных сессий (типично для вайбкодинга — фича за фичей, а не за один диалог). Отвечает на конкретную проблему: новая сессия начинается без памяти о предыдущей, согласованность прогресса через границы контекстных окон не гарантирована сама по себе. Прямо дополняет [[vibecoding-full-workflow]] (который описывает разработку в рамках одной активной сессии) практикой для случая, когда проект переживает саму сессию.

## Три примитива (из репозитория `cwc-long-running-agents`)
1. **Default-FAIL Contract** — каждая фича стартует с `"passes": false` в файле результатов; `PreToolUse`-хук не даёт агенту отметить успех, пока он не открыл evidence (скриншот/лог/вывод теста) через Read. Агент физически не может соврать себе об успехе.
2. **Fresh-Context Evaluator** — отдельный субагент без прав Write/Edit проверяет diff/скриншоты из контекста, который никогда не видел саму разработку; возвращает PASS/NEEDS_WORK, находки становятся стартовым промптом следующей сессии.
3. **Agent-Maintained Handoff** — агент пишет `PROGRESS.md` в начале каждой сессии, коммитит на чекпоинтах; backstop-хук `commit-on-stop.sh` подхватывает незакоммиченное при остановке. `git log` + progress-файл заменяют память, которую агент физически не может унести между сессиями.

Плюс встроенный short-cut — команда **`/goal`** в Claude Code: одна строка с критерием завершения ("every feature in PROGRESS.md is implemented, committed, and its tests pass"), отдельная быстрая модель сама проверяет выполнение после каждого хода — без кастомных хуков и файла-контракта.

## Ключевая связь с memory tool
Официальная документация [[claude-memory-tool]] прямо ссылается на этот кейс-стади как на детальную реализацию своего раздела "Multi-session software development pattern" — то есть Anthropic описывает один и тот же паттерн (progress log + git recovery между сессиями) на двух уровнях: как фичу API (memory tool) и как конкретный harness с хуками для Claude Code/Agent SDK.

## Оговорка по достоверности
Прямой блог (`anthropic.com/engineering/...`) отдал 403 на WebFetch (анти-бот защита) — тезисы блога зафиксированы по совпадающим пересказам нескольких независимых изданий (InfoQ, ZenML LLMOps Database, Medium), а не прочитаны из первых рук. README самого репозитория `anthropics/cwc-long-running-agents` прочитан напрямую и является надёжным первичным источником для всех технических деталей выше.

## Связанные страницы
- Концепт: [[long-running-agent-harness]] — новая карточка концепта
- Концепт: [[claude-memory-tool]] — тот же паттерн со стороны API
- Концепт: [[vibecoding-full-workflow]] — дополняет однoсессионный воркфлоу
- Сущность: [[claude-code]] — хуки, субагенты, `/goal`
- Сущность: [[claude-agent-sdk]] — `PreToolUse`/`Stop` колбэки, `evaluator_optimizer` паттерн
