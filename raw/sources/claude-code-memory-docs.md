# How Claude remembers your project (официальная документация Claude Code)

**URL:** https://code.claude.com/docs/en/memory
**Загружено:** 2026-07-31 (ежедневный процесс закрытия пробелов)
**Тип фиксации:** содержимое получено через WebFetch, страница отдала markdown документации Mintlify практически целиком.

## Полный текст страницы (сокращения отмечены — код-примеры путей/JSON оставлены как есть, повторяющиеся списки настроек компактизированы)

> Give Claude persistent instructions with CLAUDE.md files, and let Claude accumulate learnings automatically with auto memory.

Each Claude Code session begins with a fresh context window. Two mechanisms carry knowledge across sessions:
- **CLAUDE.md files**: instructions you write to give Claude persistent context
- **Auto memory**: notes Claude writes itself based on your corrections and preferences

### CLAUDE.md vs auto memory

Claude Code has two complementary memory systems. Both are loaded at the start of every conversation. Claude treats them as context, not enforced configuration. To block an action regardless of what Claude decides, use a PreToolUse hook instead.

| | CLAUDE.md files | Auto memory |
|---|---|---|
| Who writes it | You | Claude |
| What it contains | Instructions and rules | Learnings and patterns |
| Scope | Project, user, or org | Per repository, shared across worktrees |
| Loaded into | Every session | Every session (first 200 lines or 25KB) |
| Use for | Coding standards, workflows, project architecture | Build commands, debugging insights, preferences Claude discovers |

Subagents can also maintain their own auto memory (see subagent configuration).

### CLAUDE.md files — scope table

| Scope | Location | Purpose | Shared with |
|---|---|---|---|
| Managed policy | macOS `/Library/Application Support/ClaudeCode/CLAUDE.md`, Linux/WSL `/etc/claude-code/CLAUDE.md`, Windows `C:\Program Files\ClaudeCode\CLAUDE.md` | Organization-wide instructions managed by IT/DevOps | All users in organization |
| User instructions | `~/.claude/CLAUDE.md` | Personal preferences for all projects | Just you (all projects) |
| Project instructions | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team-shared instructions | Team members via source control |
| Local instructions | `./CLAUDE.local.md` | Personal project-specific preferences; add to `.gitignore` | Just you (current project) |

Loaded in order broadest→most specific; a project instruction appears in context after a user instruction. `/context` shows what actually loaded ("Memory files").

`/init` generates a starting CLAUDE.md; with `CLAUDE_CODE_NEW_INIT=1` an interactive multi-phase flow (explores codebase via subagent, asks follow-ups, proposes before writing).

Size guidance: target under 200 lines per CLAUDE.md file. Structure/specificity/consistency advice given. `@path/to/import` syntax for imports (max depth 4 hops, external imports outside working dir trigger an approval dialog once per project). Claude Code reads `CLAUDE.md`, not `AGENTS.md` — recommends `@AGENTS.md` import or symlink for shared configs with other tools.

Files load by walking up the directory tree from cwd; all discovered files concatenated (not overriding each other), root→cwd order, `CLAUDE.local.md` appended after `CLAUDE.md` at each level. Nested subdirectory CLAUDE.md files load on demand when Claude reads files there, not at launch. Block-level HTML comments stripped before injection (visible to humans, invisible to Claude/context).

`--add-dir` doesn't load CLAUDE.md from added directories by default; `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` opts in.

`.claude/rules/` — modular per-topic instruction files, optionally scoped via YAML frontmatter `paths: [...]` glob patterns (only load into context when Claude touches matching files). Supports symlinks for sharing across projects. User-level rules `~/.claude/rules/` apply to all projects, loaded before project rules (lower priority).

Managed policy CLAUDE.md: `claudeMd` key in `managed-settings.json` as an alternative to a separate file; cannot be excluded by individual settings; loads before user/project CLAUDE.md. `claudeMdExcludes` setting (glob patterns against absolute paths) to skip specific ancestor CLAUDE.md files in monorepos — mergeable across settings layers, but cannot exclude managed policy files.

### Auto memory

> Auto memory lets Claude accumulate knowledge across sessions without you writing anything. Claude saves notes for itself as it works: build commands, debugging insights, architecture notes, code style preferences, and workflow habits. Claude doesn't save something every session. It decides what's worth remembering based on whether the information would be useful in a future conversation.

**Enable/disable:** on by default. `/memory` → auto memory toggle, saves `autoMemoryEnabled` to `~/.claude/settings.json` (user-level) or a project's `.claude/settings.json` (project-level). Env var `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` also disables it.

**Storage location:** `~/.claude/projects/<project>/memory/`. `<project>` is derived from the git repository, so all worktrees and subdirectories within the same repo share one auto memory directory. Outside a git repo, the project root is used instead. Configurable via `autoMemoryDirectory` in settings.json (any settings scope: user/project/local/policy/`--settings`); must be absolute path or start with `~/`; when set in project `.claude/settings.json` or `.claude/settings.local.json`, honored only after workspace trust dialog is accepted (same gate as hooks).

Directory contents:
```
~/.claude/projects/<project>/memory/
├── MEMORY.md          # Concise index, loaded into every session
├── debugging.md       # Detailed notes on debugging patterns
├── api-conventions.md # API design decisions
└── ...                # Any other topic files Claude creates
```
`MEMORY.md` is an index; Claude reads/writes files in this directory throughout the session, using `MEMORY.md` to track what's stored where.

Auto memory is **machine-local**. All worktrees/subdirectories within the same git repo share one directory; files are **not shared across machines or cloud environments**.

**How it works:** first 200 lines of `MEMORY.md`, or first 25KB, whichever comes first, loaded at start of every conversation. Content beyond that threshold is not loaded at session start. Claude is expected to keep `MEMORY.md` concise, moving detail into topic files.

Since v2.1.210: after Claude writes to `MEMORY.md`, Claude Code measures it against the 200-line/25KB limits. Near the limit → reminder to shorten (one line per entry, move detail to topic files, merge/drop stale entries). Over the limit → write still succeeds, but Claude Code returns an error telling Claude to rewrite the index (everything past the limit is dropped on next load).

Since v2.1.211: the check measures only content that loads — YAML frontmatter and block-level HTML comments are stripped before measuring, so they don't count toward the limit. Before v2.1.211 the raw file was measured.

This limit applies **only to `MEMORY.md`** — CLAUDE.md files load in full regardless of length (though shorter files still produce better adherence).

Topic files (e.g. `debugging.md`, `patterns.md`) are **not** loaded at startup — Claude reads them on demand with standard file tools when needed.

**Subagents:** the main conversation's auto memory is **not** loaded into subagents. Exception: `/fork` (a forked conversation inherits the parent conversation and system prompt). A subagent's own auto memory, enabled via the subagent `memory` field, is a **separate directory** from the main conversation's.

Claude reads/writes memory files during the session — UI messages like "Saved 2 memories" / "Recalled 2 memories" indicate active updates.

Since v2.1.214: when Claude writes a memory file that begins with YAML frontmatter, Claude Code records the write time in a `modified` frontmatter field (ISO 8601). Shows how current a fact is, to both user and Claude re-reading it. Files with existing frontmatter get the field on next write, even if created on earlier versions; Claude Code never adds frontmatter to a file that has none.

**Audit/edit:** auto memory files are plain markdown, editable/deletable anytime. `/memory` browses/opens memory file locations (CLAUDE.md, CLAUDE.local.md, and other memory locations across user/project scopes, including not-yet-existing entries); also toggles auto memory and opens the auto memory folder. `/context` shows what actually loaded into the current session.

Since v2.1.216: GUI editors (VS Code) open the file in a separate window without blocking the session; before that, `/memory` waited for the file to close.

To make Claude save something: "always use pnpm, not npm" or "remember that the API tests require a local Redis instance" → saved to auto memory. To add to CLAUDE.md instead: "add this to CLAUDE.md" or edit via `/memory` yourself.

### Troubleshooting

**CLAUDE.md not followed:** CLAUDE.md content is delivered as a user message after the system prompt, not part of the system prompt itself — no guarantee of strict compliance, especially for vague/conflicting instructions. Debug via `/context` (verify file loaded), check load location, make instructions more specific, look for conflicting instructions across CLAUDE.md files — **"If two files give different guidance for the same behavior, Claude may pick one arbitrarily."** For must-run-at-a-specific-point instructions, use a hook instead (hooks apply regardless of what Claude decides). For system-prompt-level instructions, use `--append-system-prompt` (must be passed every invocation).

**Don't know what auto memory saved:** `/memory` → auto memory folder, browse/read/edit/delete plain markdown.

**CLAUDE.md too large:** >200 lines reduces adherence; use path-scoped rules or trim. `/doctor` (since v2.1.206) proposes trims for a checked-in CLAUDE.md — cuts content Claude can derive from the codebase (directory layouts, dependency lists, architecture overviews), keeps pitfalls/rationale/conventions that differ from tool defaults.

**Instructions lost after `/compact`:** project-root CLAUDE.md survives compaction — re-read from disk and re-injected after `/compact`. Nested subdirectory CLAUDE.md files are **not** re-injected automatically; they reload next time Claude reads a file in that subdirectory. Conversation-only instructions (never written to CLAUDE.md) do not survive.

## Примечание по разбору (это поле — уже часть Ingest, не первоисточник)

Страница **не сравнивает** auto memory с memory tool из Claude Developer Platform API (`platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool`, см. `raw/sources/claude-memory-tool-docs.md`) — ни явной ссылки, ни упоминания API-инструмента на странице нет. Оба документа читались независимо; вывод о том, что это два раздельных механизма, — синтез, а не цитата с этой страницы.
