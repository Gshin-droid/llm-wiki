---
url: https://github.com/multica-ai/andrej-karpathy-skills
title: "andrej-karpathy-skills — Behavioral guidelines to reduce common LLM coding mistakes"
fetched: 2026-07-07
stats: "188,807 stars / 19,391 forks / 124 open issues (via GitHub API, 2026-07-07)"
---

# Repository Overview: Andrej Karpathy Skills

## Purpose
Гайдлайны поведения для Claude Code (и Cursor), основанные на наблюдениях Andrej Karpathy о типичных ошибках LLM при написании кода. Дистиллирует его инсайты в практические принципы для улучшения AI-assisted разработки.

## Core Content — CLAUDE.md (полный текст)

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

### 1. Think Before Coding
**Don't assume. Don't hide confusion. Surface tradeoffs.**
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

### 2. Simplicity First
**Minimum code that solves the problem. Nothing speculative.**
- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.
- Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

### 3. Surgical Changes
**Touch only what you must. Clean up only your own mess.**
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it — don't delete it.
- Remove imports/variables/functions that YOUR changes made unused. Don't remove pre-existing dead code unless asked.
- The test: every changed line should trace directly to the user's request.

### 4. Goal-Driven Execution
**Define success criteria. Loop until verified.**
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"
- For multi-step tasks, state a brief plan with verify steps.
- Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.

## Repository Structure
- `CLAUDE.md` — основной файл гайдлайнов
- `CURSOR.md` — адаптация для Cursor
- `EXAMPLES.md` — практические примеры
- `.cursor/rules/karpathy-guidelines.mdc` — Cursor project rules
- `.claude-plugin/` — конфигурация плагина Claude Code
- `README.md` / `README.zh.md` — документация (англ. + кит.)

## Установка
- Claude Code Plugin через marketplace (`forrestchang/andrej-karpathy-skills`)
- Per-project: добавить `CLAUDE.md` в проект вручную
- Cursor: `.cursor/rules/karpathy-guidelines.mdc`

## Автор/организация
Публикует multica-ai, лицензия MIT. Автор ведёт X (@jiayuan_jy), связан со смежным проектом Multica — для запуска coding-агентов.
