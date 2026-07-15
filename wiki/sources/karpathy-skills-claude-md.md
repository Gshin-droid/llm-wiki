# Karpathy Skills — CLAUDE.md с гайдлайнами против типичных ошибок LLM

**Источник:** [github.com/multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)
**Загружено:** 2026-07-07
**Raw:** `raw/sources/karpathy-skills-claude-md.md`
**Метрики:** 188.8k звёзд, 19.4k форков (виральный репозиторий, несмотря на простое содержание — один файл правил)

## Саммари
Репозиторий дистиллирует наблюдения [[andrej-karpathy]] о типичных ошибках LLM-агентов при написании кода в один файл `CLAUDE.md` с четырьмя принципами — см. [[llm-coding-guidelines]]. Работает как готовый набор поведенческих правил, который можно добавить в любой проект (Claude Code или Cursor) поверх project-specific инструкций.

## Наблюдение (важно)
Все четыре принципа (think before coding, simplicity first, surgical changes, goal-driven execution) практически дословно совпадают с базовыми правилами, которыми уже руководствуется Claude Code по умолчанию (раздел "Doing tasks" системного промпта: не добавлять фичи сверх запрошенного, не рефакторить лишнее, хирургические правки, no error handling для невозможных сценариев). Это не новое открытие, а формализация уже устоявшейся best practice, которая, судя по популярности репозитория, оказалась востребована как явный, копируемый артефакт.

## Четыре принципа
1. Think Before Coding — явно проговаривать допущения, не выбирать интерпретацию молча
2. Simplicity First — минимум кода, никакой спекулятивной гибкости
3. Surgical Changes — трогать только то, что попросили; не улучшать соседний код
4. Goal-Driven Execution — превращать задачи в проверяемые критерии успеха, чтобы уметь итерироваться самостоятельно

Полный текст — в [[llm-coding-guidelines]] и в raw-файле.

## Установка/использование
- Как Claude Code plugin через marketplace `forrestchang/andrej-karpathy-skills`
- Вручную — положить `CLAUDE.md` в проект
- Для [[cursor]] — `.cursor/rules/karpathy-guidelines.mdc`

## Связанные страницы
- Концепт: [[llm-coding-guidelines]]
- Сущности: [[andrej-karpathy]], [[claude-code]], [[cursor]], [[multica]]
