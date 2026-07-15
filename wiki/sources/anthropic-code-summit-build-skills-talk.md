# "Don't Build Agents, Build Skills Instead" (Barry Zhang & Mahesh Murag)

**Источник:** доклад на AI Engineer Code Summit, 25.11.2025. YouTube: https://www.youtube.com/watch?v=CEvIs9y1uog
**Загружено:** 2026-07-09 (через пересказы — claudehub.fr, cto4.ai; прямая расшифровка видео не читана)
**Raw:** ссылки зафиксированы в `raw/sources/anthropic-skills-practical-research-2026-07-09.md`

## Саммари
Ведущая сессия трека CODE на AI Engineer Code Summit. Barry Zhang и Mahesh Murag — создатели [[claude-skills|Agent Skills]] в Anthropic. Это **первоисточник** для маркетингового конспекта [[hook-4-pravila-claude-skills]]. Zhang хронологически показал путь Anthropic в 2025: effective agents → MCP → Claude Code → Claude Agent SDK → Skills.

## Ключевые тезисы
- Skills — папки на файловой системе с markdown-документацией и Python-скриптами, инкапсулирующие доменную экспертизу.
- Три аспекта жизненного цикла скилла: систематическая оценка/тестирование, версионирование во времени, композиционность (комбинируются друг с другом и с MCP/pandas).
- Кейс с Python-скриптом для слайдов: Claude каждую сессию заново писал один и тот же скрипт под стили — решение: сохранить скрипт в скилл, дальше Claude просто запускает готовый код.
- Цитата (пересказ cto4.ai): «Our goal is that Claude on day 30 of working with you is going to be a lot better than Claude on day one» — скилл накапливает edge-кейсы/голос/процесс пользователя, промт — нет.

## Происхождение концепции
Твит Barry Zhang, 16.10.2025 (за месяц до доклада): «Skills actually came out of a prototype I built demonstrating that Claude Code is a general-purpose agent... It was a natural conclusion once we realized that bash + filesystem were all we needed.» (via [simonwillison.net](https://simonwillison.net/2025/Oct/16/barry-zhang/))

## Ограничение источника
Полная расшифровка видео не прочитана — саммари собрано по двум независимым пересказам (claudehub.fr, cto4.ai), которые совпадают в ключевых фактах. Для дословных цитат кроме указанных выше — сверяться с видео напрямую.

## Связанные страницы
- Вторичный конспект: [[hook-4-pravila-claude-skills]]
- Официальная методология (тот же материал, но от Anthropic напрямую): [[anthropic-official-skills-docs]]
- Концепт: [[skill-authoring-practical-rules]]
- Сущность: [[claude-skills]]
