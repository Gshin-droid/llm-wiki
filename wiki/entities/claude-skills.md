# Claude Skills

**Тип:** функция продукта (Claude.ai / Claude Code)
**Актуально на:** 2026-07-09

## Что это
Переносимая папка с инструкцией (`SKILL.md`) и опциональными скриптами/референсами, которая один раз устанавливается и "прокачивает" Claude в конкретной области — не разовая задача, а устойчивое умение, применимое в разных проектах и чатах. Вызывается командой `/` или подключается автоматически, когда Claude решает, что скилл релевантен задаче (см. архитектуру progressive disclosure в [[skill-authoring-practical-rules]]). Официально — открытый стандарт [Agent Skills](https://agentskills.io), не привязан к одному инструменту.

Создатели фичи в Anthropic — Barry Zhang и Mahesh Murag; концепция выросла из прототипа, доказывавшего, что Claude Code — general-purpose агент на связке bash + файловая система (см. [[anthropic-code-summit-build-skills-talk]]).

## Как создавать (практическая методология)

Полный свод правил — description как единственный триггер, три слоя (Description/Instructions/Tools), правило 500 строк, композиционность вместо монолита, итеративное накопление по сессиям, тестирование with/without — см. отдельную страницу [[skill-authoring-practical-rules]].

Примеры из загруженных источников:
- **Frontend Design** (by Anthropic) — банит заезженные шрифты/раскладки, подталкивает к небанальному дизайну (см. [[metics-media-10k-website]])
- **UI/UX Pro Max** — 57 стилей, 95 палитр, 56 пар шрифтов, вызывается явно при "большом дизайн-вмешательстве" (см. [[metics-media-10k-website]])
- Библиотека готовых скилов на aitmpl.com — сотни (~847 на момент [[qaisar-claude-full-course]]) готовых умений: SEO-оптимизатор, генератор PPTX и т.д.

## Не путать с CLAUDE.md-конвенцией
[[llm-coding-guidelines|Karpathy's CLAUDE.md-гайдлайны]] ([[karpathy-skills-claude-md]]) концептуально похожи (тоже "устанавливается один раз, действует постоянно"), но технически это не Skill в продуктовом смысле (не SKILL.md, не подключается через `/`-команду или маркетплейс), а просто файл с инструкциями, который читает любой агент в начале работы в проекте. Разные механизмы, общая идея.

Это третий уровень в [[five-levels-of-claude-mastery]].

Один из четырёх механизмов многошаговой работы в Claude Code наряду с субагентами, agent teams и workflows — сравнение по тому, кто держит план выполнения, см. [[dynamic-workflows]].

## Связи

- Источники: [[ai-proryv-5-levels-claude]], [[metics-media-10k-website]], [[qaisar-claude-full-course]], [[karpathy-skills-claude-md]], [[anthropic-official-skills-docs]], [[anthropic-code-summit-build-skills-talk]], [[habr-claude-skills-practical-guide]], [[hook-4-pravila-claude-skills]]
- Концепт: [[five-levels-of-claude-mastery]], [[skill-authoring-practical-rules]], [[dynamic-workflows]]
- Отличие от [[claude-projects]]: skill — переносимое умение на любой контекст, project — память под конкретную роль.
