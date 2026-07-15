# GSD (Get Shit Done)

**Тип:** инструмент (open source spec-driven агентский фреймворк поверх Claude Code)
**Актуально на:** 2026-07-10

## Что это
"Lightweight powerful metaprompting, context engineering and spec-driven development system for Claude Code". В отличие от голого вайбкодинга ([[vibecoding-full-workflow]]), автоматизирует весь цикл SDLC: от спецификации и research до планирования по фазам, параллельного исполнения волнами (waves), self-check и человеческой верификации. Генерирует полный комплект проектной документации (`requirements.md`, `roadmap.md`, `architecture.md`, `features.md`, `pitfalls.md`) как побочный артефакт каждой фазы — обеспечивает агенту долгосрочную память о проекте между сессиями.

~70 команд/хуков, 6 базовых достаточно для большинства задач; продвинутые — `milestone`, `quick` (быстрый фикс в обход полного ритуала фаз), `spike`, `sketch`, `mapcodebase`. Более тяжеловесный и токен-затратный, чем [[superpowers]] — позиционируется под enterprise-масштаб.

Установка: `npx get-shit-done`.

## Связи
- Источник: [[vladilen-minin-gsd-superpowers]]
- Концепт: [[agentic-sdlc-frameworks]]
- Соседний инструмент: [[superpowers]] (легче, под меньший масштаб)
- Работает поверх: [[claude-code]]
