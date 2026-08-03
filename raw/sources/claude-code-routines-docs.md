# Automate work with routines / Run prompts on a schedule (официальная документация Claude Code)

**URL 1:** https://code.claude.com/docs/en/routines.md
**URL 2:** https://code.claude.com/docs/en/scheduled-tasks.md
**Загружено:** 2026-08-03 (еженедельный автономный разведчик практического материала)
**Тип фиксации:** содержимое получено через WebFetch напрямую, обе страницы отдали markdown документации Mintlify целиком, без ошибок доступа.

## routines.md — ключевые выдержки

> A routine is a saved Claude Code configuration: a prompt, one or more repositories, and a set of connectors, packaged once and run automatically. Routines execute on Anthropic-managed cloud infrastructure, so they keep working when your laptop is closed.

Триггеры: **Scheduled** (recurring или one-off), **API** (POST на per-routine endpoint с bearer-токеном), **GitHub** (pull_request/release события). Комбинируются в одной рутине.

> Routines run autonomously as full Claude Code cloud sessions: there is no permission-mode picker and no approval prompts during a run.

> When a trigger fires, the session receives the routine's saved prompt as its assigned task and carries it out, rather than treating it as untrusted content that arrived mid-conversation. The trigger attests only that the prompt was stored ahead of time by an authorized session on your account, so the fired prompt is not live user input and can't act as approval or consent for actions during the run. Content the session fetches during the run keeps its normal handling. (min-version 2.1.214 — before that, the session received the same prompt framed as an untrusted background notification and could refuse to act on it.)

`/schedule` (алиас `/routines`) создаёт cloud-рутину из CLI разговорно; `/schedule list|update|run` управляют существующими. Только schedule-триггер доступен из CLI — API/GitHub добавляются только через веб-форму.

Schedule-триггер: пресеты hourly/daily/weekdays/weekly, кастомный cron через `/schedule update`, минимальный интервал — 1 час. One-off runs не расходуют дневной лимит запусков рутины (расходуют обычный usage подписки).

API-триггер: `POST /v1/claude_code/routines/{id}/fire` с `Authorization: Bearer <token>`, заголовком `anthropic-beta: experimental-cc-routine-2026-04-01`. Поле `text` — фрифлоу, не парсится.

> The text value doesn't reach the routine as a bare message. It arrives wrapped in a `<routine-fire-payload>` block that labels it as untrusted data and tells Claude not to follow instructions inside it unless the routine's own prompt says to.

GitHub-триггер: события `pull_request`/`release` с фильтрами (author/title/body/base branch/head branch/labels/is draft/is merged, операторы equals/contains/starts with/is one of/is not one of/matches regex). Требует установки Claude GitHub App (не то же самое, что `/web-setup`).

Ветки: коммиты идут в `claude/`-префиксные ветки (принимаются всегда); пуш в другую ветку блокируется, если ветка protected, по ней уже открыт чужой PR, или на ней коммиты не только пользователя.

Environments: Default = Trusted network access (только default allowlist доменов), коннекторы MCP идут через серверы Anthropic и не требуют доменов в allowlist отдельно.

Usage: рутины расходуют обычный usage подписки + дневной кап запусков на аккаунт (число не указано на этой странице явно, см. `claude.ai/code/routines`). One-off runs не считаются в дневной кап.

## scheduled-tasks.md — ключевые выдержки

Сравнительная таблица трёх способов расписания:

| | Cloud (Routines) | Desktop | `/loop` |
|---|---|---|---|
| Runs on | Anthropic cloud | Your machine | Your machine |
| Requires machine on | No | Yes | Yes |
| Requires open session | No | No | Yes |
| Persistent across restarts | Yes | Yes | Restored on `--resume` if unexpired |
| Access to local files | No (fresh clone) | Yes | Yes |
| Permission prompts | No (runs autonomously) | Configurable per task | Inherits from session |
| Minimum interval | 1 hour | 1 minute | 1 minute |

`/loop` — bundled skill. Поведение зависит от того, что дано:
- `/loop 5m check the deploy` — фиксированный cron-интервал.
- `/loop check the deploy` — интервал выбирает сам Claude динамически (1 минута — 1 час) после каждой итерации, основываясь на наблюдаемом состоянии; печатает выбранную задержку и причину. Может использовать `Monitor`-тул вместо поллинга.
- `/loop` (без промпта) — встроенный maintenance-промпт (продолжить незавершённую работу → обиходить PR текущей ветки → cleanup-проходы) или `loop.md`, если есть.

(min-version 2.1.196) Скедулед-файр запускает только скиллы, которые Claude разрешено вызывать самому — `disable-model-invocation: true` скиллы (включая встроенные `/verify`, `/code-review`), скиллы, скрытые `skillOverrides` или `Skill`-deny-правилом, и билтин-команды типа `/permissions` доходят как обычный текст, не исполняются.

`loop.md`: `.claude/loop.md` (project, приоритет) или `~/.claude/loop.md` (user) — заменяет встроенный maintenance-промпт для голого `/loop`. Лимит 25000 байт, обрезается сверх. Правки применяются со следующей итерации.

Остановка: `Esc` во время ожидания снимает pending wakeup. В self-paced режиме Claude сам может завершить луп через `ScheduleWakeup(stop: true)`. (min-version 2.1.202 — до этого единственный способ завершить луп самому — не перепланировать следующий wakeup.) Если итерация не перепланировала и не остановила луп явно — Claude Code сам ставит один fallback wakeup через ~20 минут и завершает луп, если и та итерация не перепланирует.

Jitter: recurring-задачи файрят до 30 минут позже расписания (или до половины интервала для интервалов чаще часа) — оффсет детерминирован от task ID. One-shot задачи на `:00`/`:30` файрят до 90 секунд раньше.

Seven-day expiry: recurring-задачи истекают через 7 дней после создания (файрят финальный раз и удаляются). Cloud Routines/Desktop scheduled tasks — не истекают.

Инструменты под капотом: `CronCreate` (5-полевой cron, до 50 задач на сессию), `CronList`, `CronDelete` (по 8-символьному ID).

`CLAUDE_CODE_DISABLE_CRON=1` — полностью отключает scheduler, cron-тулы и `/loop`.
