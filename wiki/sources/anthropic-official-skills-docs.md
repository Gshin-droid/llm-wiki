# Официальная методология Anthropic по Agent Skills

**Источники:**
- [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) — инженерный блог Anthropic
- [anthropics/skills — skill-creator/SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) — официальный мета-скилл для создания скиллов
- [Extend Claude with skills](https://code.claude.com/docs/en/skills) — документация Claude Code

**Загружено:** 2026-07-09
**Raw:** `raw/sources/anthropic-skills-practical-research-2026-07-09.md`

## Саммари
Три официальных документа Anthropic, дающих полную практическую методологию создания скиллов — от архитектурного принципа (progressive disclosure) до пошагового чеклиста (skill-creator) и продуктовых деталей (где хранятся, как приоритизируются, монорепо). Это основной первоисточник для [[skill-authoring-practical-rules]] — там же сведены все правила в единую практическую страницу.

## Progressive disclosure — архитектурный принцип
Три уровня раскрытия контекста:
1. **Система** — только `name`+`description` всех скиллов в system prompt (дёшево)
2. **Активация** — полный `SKILL.md` грузится, когда Claude решил, что скилл релевантен
3. **Навигация** — дополнительные файлы (`references/*.md`) грузятся по требованию через Bash

Официальная формулировка: «The amount of context that can be bundled into a skill is effectively unbounded» — благодаря файловой системе и code execution вместо удержания всего в контексте разом.

## Когда создавать скилл (эвристика Claude Code docs)
«Create a skill when you keep pasting the same instructions, checklist, or multi-step procedure into chat, or when a section of CLAUDE.md has grown into a procedure rather than a fact.» Ключевое отличие от CLAUDE.md: тело скилла грузится только при использовании, поэтому длинный референсный материал почти ничего не стоит, пока не понадобился — а CLAUDE.md читается целиком в каждой сессии.

## Practical rules (из skill-creator)
- **Description = единственный триггер.** Claude видит только `name`+`description`, решение подключать скилл или нет принимается по ним, а не по телу файла.
- ~100 слов, явное «когда использовать», «pushy» тон, разные формулировки одного и того же намерения, near-miss примеры (что НЕ должно триггерить).
- Правило 500 строк: тело SKILL.md, приближающееся к 500 строкам — сигнал выносить в `references/` с явными указателями.
- `scripts/` — когда логика повторяется в разных тест-кейсах (сигнал: agent заново пишет один и тот же скрипт).
- Тестирование: 2-3 реалистичных промпта → `evals.json` → сравнение with/without skill → grading → итерация без overfitting на тест-кейсы.

## Продуктовые детали (Claude Code docs)
- Локации: Enterprise > Personal (`~/.claude/skills/`) > Project (`.claude/skills/`) > Plugin — приоритет в этом порядке при совпадении имён.
- Custom commands слиты со skills: `.claude/commands/deploy.md` ≡ `.claude/skills/deploy/SKILL.md`.
- Монорепо: скиллы из `packages/frontend/.claude/skills/` подхватываются при работе с файлами в этой директории; конфликт имён разрешается directory-qualified именем (`apps/web:deploy`).
- Live change detection: правки в SKILL.md подхватываются без рестарта сессии.
- Dynamic context injection: `` !`git diff HEAD` `` в теле SKILL.md — команда выполняется и результат подставляется до того, как Claude увидит файл.
- Skills следуют открытому стандарту [Agent Skills](https://agentskills.io) — не привязаны к одному инструменту.

## Связанные страницы
- Синтез: [[skill-authoring-practical-rules]]
- Первоисточник концепции: [[anthropic-code-summit-build-skills-talk]]
- Практика сообщества: [[habr-claude-skills-practical-guide]]
- Сущность: [[claude-skills]]
