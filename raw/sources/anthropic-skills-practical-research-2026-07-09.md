# Raw-выжимка: исследование по теме "создание Skills вместо промтов"

**Собрано:** 2026-07-09, через WebSearch/WebFetch (не Web Clipper — ручной research-проход)
**Метод:** прочитаны официальные источники Anthropic (инженерный блог, GitHub, документация Claude Code) + два практических разбора на Habr.

Это сырой архив выдержек, использованных для страниц `wiki/sources/anthropic-official-skills-docs.md` и `wiki/sources/habr-claude-skills-practical-guide.md`. Полные тексты статей не сохранены — только извлечённые через WebFetch саммари ниже, с URL для проверки.

---

## 1. Anthropic Engineering Blog — "Equipping agents for the real world with Agent Skills"
URL: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

Progressive disclosure — три уровня загрузки контекста:
- Уровень 1 (система): только `name`+`description` всех скиллов в system prompt
- Уровень 2 (активация): полный SKILL.md загружается, когда Claude решает, что скилл релевантен
- Уровень 3+ (навигация): доп. файлы (reference.md, forms.md) — по мере необходимости через Bash

"The amount of context that can be bundled into a skill is effectively unbounded" — за счёт файловой системы и code execution.

Правила: метаданные (`name`+`description`) — решающий фактор триггера; держать ядро лаконичным, разносить по файлам при разрастании; разделять взаимоисключающие контексты по разным файлам для экономии токенов.

Экономия токенов: код как инструмент вместо генерации токенов ("sorting a list via token generation is far more expensive than simply running a sorting algorithm"), отложенная загрузка, детерминированность скриптов.

Кейс: PDF-skill — SKILL.md + reference.md + forms.md + python-скрипт извлечения полей форм; Claude запускает скрипт без загрузки PDF/скрипта в контекст.

Цикл разработки: начать с оценки (гонять на representative tasks, искать пробелы) → итеративно расширять → мониторить реальное использование → просить Claude самому фиксировать успешные подходы и ошибки в скилл → self-reflection при ошибках.

Безопасность: skills — потенциальная attack surface, устанавливать только из доверенных источников, аудировать сетевые вызовы в коде скилла.

## 2. GitHub — anthropics/skills, skill-creator/SKILL.md (официальный мета-скилл)
URL: https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md

Название: kebab-case, не generic (не "helper"/"tool"/"utility").

Description — единственный механизм триггера (Claude видит только name+description):
- ~100 слов, явное "when to use", конкретные контексты, "pushy" тон, разные формулировки одного намерения
- Плохо: "Build dashboards". Хорошо: "How to build a simple fast dashboard... use this skill whenever user mentions dashboards, data visualization, internal metrics... even if they don't explicitly ask for a 'dashboard'"
- Метод оптимизации: 20 eval-запросов (should-trigger / should-not-trigger), фокус на near-misses, реалистичные примеры (конкретные имена файлов/ситуации, не абстракции)

Структура: SKILL.md (frontmatter name+description+опционально compatibility, тело <500 строк) + scripts/ (детерминированный код) + references/ (документация >300 строк или domain-specific, грузится по требованию) + assets/ (шаблоны/иконки).

Правило 500 строк: при приближении — выносить в references/ с явными указателями ("See `references/config-guide.md`").

Scripts: создавать, когда во всех test-кейсах повторяется одна и та же логика (agent постоянно пишет `build_chart.py` заново) — сильный сигнал вынести в bundled script.

Чеклист готовности: явное "когда использовать" в description; тело <500 строк; примеры output-формата; imperative mood; "why" перед "must/never"; test-кейсы 2-3 реалистичных промпта; evals.json; baseline с/без скилла; итерация по фидбеку без overfitting на 2-3 кейса.

Частые ошибки: обобщённый description → undertriggering; SKILL.md >500 строк без иерархии → context overload; hardcoded примеры вместо паттернов; MUST/NEVER без объяснения причины; отсутствие bundled script для повторяющейся работы; отсутствие baseline-сравнения.

Ключевой тезис: "Description — это всё... Создавай для миллионов, не для трёх тест-кейсов."

## 3. Claude Code Docs — "Extend Claude with skills"
URL: https://code.claude.com/docs/en/skills

Эвристика когда создавать скилл: "Create a skill when you keep pasting the same instructions, checklist, or multi-step procedure into chat, or when a section of CLAUDE.md has grown into a procedure rather than a fact. Unlike CLAUDE.md content, a skill's body loads only when it's used, so long reference material costs almost nothing until you need it."

Custom commands слиты со skills: `.claude/commands/deploy.md` и `.claude/skills/deploy/SKILL.md` эквивалентны, оба дают `/deploy`.

Локации и приоритет: Enterprise > Personal (`~/.claude/skills/`) > Project (`.claude/skills/`) > Plugin (namespace `plugin:skill`). При совпадении имён enterprise перекрывает personal, personal — project. Skill того же имени перекрывает bundled skill.

Nested skills в монорепо: `.claude/skills/` подгружаются из под-директорий по мере работы с файлами там; конфликт имён → доступны обе версии, вложенная получает directory-qualified имя (`apps/web:deploy`).

Live change detection: изменения в SKILL.md подхватываются без перезапуска сессии; новая top-level папка skills требует рестарт.

Dynamic context injection: строка вида `` !`git diff HEAD` `` в SKILL.md выполняется и подставляется перед тем, как Claude увидит контент.

Follow Agent Skills open standard (agentskills.io) — работает не только в Claude Code.

## 4. Habr — "Skills для Claude Code: огромный гайд от инженера Anthropic"
URL: https://habr.com/ru/articles/1011524/ (адаптация/пересказ официального claude.com/blog поста "Lessons from building Claude Code: How we use skills")

9 категорий скиллов с примерами: справочники API (`billing-lib`), верификация продукта (`signup-flow-driver` с assertions на каждом шаге), получение данных (`funnel-query`, Grafana-интеграции), бизнес-процессы (`standup-post`, `create-ticket`), скаффолдинг кода, код-ревью (`adversarial-review`), CI/CD (`babysit-pr`), ранбуки (диагностика по симптомам), инфраструктурные операции.

Практика не из офиц. доков:
- Самый ценный раздел скилла — "Gotchas" (типичные ошибки), формируется по мере реальных факапов Claude, а не придумывается заранее
- `config.json` для начальной настройки — если пуст, агент сам спросит юзера
- Память в скиллах: append-only логи (`standups.log`), `${CLAUDE_PLUGIN_DATA}` — стабильная директория, переживает обновления
- Хуки по требованию внутри скилла: `/careful` блокирует `rm -rf`/`DROP TABLE`/force-push, `/freeze` блокирует Edit вне указанной директории
- Description — это условия срабатывания, а не summary
- Органический рост: сначала sandbox-версия скилла, PR в общий marketplace только когда доказал полезность

## 5. Habr — "Навыки (Skills) для Claude: почему папка с Markdown-файлами может оказаться важнее кастомных GPT"
URL: https://habr.com/ru/articles/957614/

Эффективность токенов: скилл занимает "несколько десятков токенов" в контексте (только description), пока не активирован — контраст с кастомными GPT, где system prompt сразу жрёт десятки тысяч токенов.

Пример slack-gif-creator: Claude генерирует Python с использованием классов скилла, применяет встроенную валидацию (лимит 2MB Slack), итеративно чинит при неудаче.

Ключевое отличие от ChatGPT-плагинов/кастомных GPT: не сложный протокол, а "просто дай модели текст, пусть сама разберётся" — работает с любой моделью/инструментом, не привязано к одной платформе.

---

## Дополнительно (уже собрано в предыдущей сессии, источник — доклад)
- Talk: Barry Zhang & Mahesh Murag, "Don't Build Agents, Build Skills Instead", AI Engineer Code Summit, 25.11.2025. YouTube: https://www.youtube.com/watch?v=CEvIs9y1uog
- Разборы: https://www.claudehub.fr/en/blog/dont-build-agents-build-skills-anthropic/, https://cto4.ai/p/anthropic-stop-building-agents-start-building-skills/
- Происхождение концепции: твит Barry Zhang, 16.10.2025 (via https://simonwillison.net/2025/Oct/16/barry-zhang/) — skills выросли из прототипа, доказывающего, что Claude Code — general-purpose агент
