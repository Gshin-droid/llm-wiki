---
source: официальная документация Claude Code, code.claude.com/docs/en/permission-modes
url: https://code.claude.com/docs/en/permission-modes
retrieved: 2026-08-13
section: "Eliminate prompts with auto mode"
---

## Анонс (callout на странице)

> Starting August 14, 2026, auto mode becomes the default permission mode for new sessions on Pro, Max, and Team plans. You can switch modes at any time. A default you set yourself stays in place unless you accept the one-time switch prompt, and a default your organization manages is unchanged. For details, see [the announcement](https://claude.com/blog/auto-mode-default-in-claude-code) on the blog.

(Блог `claude.com/blog/auto-mode-default-in-claude-code` не открылся — сетевой прокси окружения заблокировал `claude.com` при этом прогоне; факты ниже только из doc-страницы.)

## Что такое auto mode (контекст, без изменений в этом релизе)

Auto mode lets Claude execute without routine permission prompts. A separate classifier model reviews actions before they run, blocking anything that escalates beyond your request, targets unrecognized infrastructure, or appears driven by hostile content Claude read. Explicit ask rules still force a prompt.

The classifier also reviews each message Claude sends to another agent with `SendMessage`, plain or structured, before Claude Code delivers it, both in auto mode and in plan mode while the classifier reviews commands; the send review requires Claude Code v2.1.222 or later.

Auto mode also nudges Claude to keep working without stopping for clarifying questions, though Claude still asks when your prompt or a skill explicitly relies on it.

> Auto mode reduces permission prompts but does not guarantee safety. Use it for tasks where you trust the general direction, not as a replacement for review on sensitive operations.

## Требования для доступности auto mode

- **Plan**: All plans.
- **Organization**: on Team and Enterprise, auto mode is available by default. Administrators can turn it off for the organization by setting `permissions.disableAutoMode` to `"disable"` in managed settings.
- **Model**: on the Anthropic API and Claude Platform on AWS, Claude Opus 4.6 or later, Sonnet 4.6 or later, or Fable 5. On Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, and signed-in Claude apps gateway sessions, only Claude Sonnet 5, Opus 4.7 or later, and Fable 5. Older models, including Sonnet 4.5, Opus 4.5, Haiku, and claude-3 models, are not supported on any provider.
- **Provider**: available by default on the Anthropic API, Claude Platform on AWS, Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, and signed-in Claude apps gateway sessions.

## Как задать auto mode как дефолт вручную (существующий механизм)

```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

Claude Code v2.1.142 и позже игнорируют `auto` в `.claude/settings.json`/`.claude/settings.local.json` (репозиторий не может сам себе выдать auto mode) — значение нужно ставить в `~/.claude/settings.json`. В сессии, запущенной расширением VS Code, `defaultMode` из файла настроек не задаёт стартовый режим — режим выбирается из индикатора расширения.

`/doctor` уже предлагает этот дефолт пользователю (существующий механизм, не новый в этом релизе).
