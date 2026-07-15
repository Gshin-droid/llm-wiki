# Memory tool (официальная документация Claude Developer Platform)

**URL:** https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
**Загружено:** 2026-07-09 (автономный ежедневный запуск)
**Тип фиксации:** содержимое получено через WebFetch, страница отдала markdown документации Mintlify практически как есть (код-примеры по языкам сокращены до сути — оставлен Python).

## Полный текст страницы (сокращённый, факты и структура сохранены)

> Let Claude store and retrieve information across conversations by implementing the memory tool's file operations in your application.

The memory tool lets Claude store and retrieve information across conversations in a directory of memory files. Claude can create, read, update, and delete files that persist between sessions, building up knowledge over time without keeping everything in the context window.

Memory supports **just-in-time context retrieval**. Rather than loading all relevant information up front, an agent records what it learns in memory files and reads them back on demand. This keeps the active context focused on the current task, which matters for long-running sessions that would otherwise overwhelm the context window. Ссылка на смежную статью: [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).

The memory tool operates **client-side**: Claude requests file operations, and your application executes them. You control where and how the data is stored through your own infrastructure.

Feature eligible for Zero Data Retention (ZDR): при ZDR-соглашении данные, отправленные через эту фичу, не сохраняются после ответа API.

### Use cases
- Maintain project context across multiple agent sessions
- Apply lessons from past interactions, decisions, and feedback to new tasks
- Build up a knowledge base over time

### How it works
When the memory tool is enabled, Claude automatically checks its memory directory (`/memories`) before starting a task. As it works, Claude stores what it learns in files and reads them back in later conversations to continue earlier work. The `/memories` path is a prefix your handler maps onto real storage (per-user directory, DB keys, etc). Memory lives entirely in the calling application, not on Anthropic's servers. Security requirement: restrict all memory operations to the `/memories` directory (path traversal protection).

### Example interaction (упрощено)
1. User: "Help me respond to this customer service ticket."
2. Claude calls `memory` tool: `{"command": "view", "path": "/memories"}`
3. App returns directory listing (`customer_service_guidelines.xml`, `refund_policies.xml`).
4. Claude calls `view` on the relevant file.
5. App returns file contents with line numbers.
6. Claude answers using that context.

### Getting started
- `tools` entry: `{"type": "memory_20250818", "name": "memory"}` — no input schema needed (Anthropic-provided tool).
- Available on **all Claude 4 and later models**. Generally available on the Messages API — no beta header required.
- Client must implement a handler for each of the six commands below, with path validation.

### Basic usage (Python)
```python
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=2048,
    messages=[{"role": "user", "content": "Help me respond to this customer service ticket."}],
    tools=[{"type": "memory_20250818", "name": "memory"}],
)
```

SDK helpers: `BetaAbstractMemoryTool` (Python/C#), `betaMemoryTool` (TypeScript), `BetaMemoryToolHandler` (Java). Python и TypeScript SDK также поставляют готовую реализацию на локальной файловой системе — `BetaLocalFilesystemMemoryTool`. Go/Ruby SDK не имеют memory-хелпера — нужно реализовывать tool-use loop вручную.

### Tool commands (шесть команд, клиент обязан их реализовать)
1. **view** — показывает содержимое директории (листинг с размерами, до 2 уровней вложенности, без скрытых файлов/`node_modules`) или файла (с построчной нумерацией, опционально `view_range: [start, end]`). Поддерживает просмотр картинок (.jpg/.jpeg/.png), обрезает текст длиннее 16000 символов. Лимит — 999,999 строк на файл.
2. **create** — создаёт новый файл (`path`, `file_text`); тул-дескрипшн говорит Claude, что команда "creates or overwrites" — на практике реализация может как выдать ошибку "already exists", так и перезаписать.
3. **str_replace** — замена текста (`old_str` → `new_str`, `new_str` опционален = удаление). Ошибка, если `old_str` не найден или найден несколько раз (не уникален).
4. **insert** — вставка текста после указанной строки (`insert_line`, `0` = начало файла).
5. **delete** — удаляет файл или директорию рекурсивно; корневую `/memories` удалять нельзя.
6. **rename** — переименование/перемещение (`old_path` → `new_path`); не перезаписывает существующий `new_path`, корень `/memories` переименовать нельзя.

### Prompting guidance
Когда memory tool присутствует в `tools`, API автоматически добавляет системную инструкцию (не нужно слать самому):
```
IMPORTANT: ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE.
MEMORY PROTOCOL:
1. Use the `view` command of your `memory` tool to check for earlier progress.
2. ... (work on the task) ...
   - As you make progress, record status / progress / thoughts etc in your memory.
ASSUME INTERRUPTION: Your context window might be reset at any moment, so you risk losing any progress that is not recorded in your memory directory.
```
Можно дополнительно попросить держать директорию памяти организованной/лаконичной, ограничить, что именно писать в память (например: "Only write down information relevant to <topic>").

### Security considerations (ответственность разработчика, не тула)
- **Sensitive information:** Claude обычно отказывается писать чувствительные данные в память — для гарантии нужна отдельная валидация на стороне приложения.
- **File storage size:** ограничивать размер файлов памяти, ограничивать объём, возвращаемый `view`, давать Claude "листать" через `view_range`.
- **Memory expiration:** периодически удалять давно неиспользуемые файлы памяти.
- **Path traversal protection** (явное предупреждение): путь вида `/memories/../../secrets.env` может выйти за пределы директории памяти. Обязательные меры — валидировать, что все пути начинаются с `/memories`; резолвить пути в каноническую форму и проверять, что они остаются внутри; отклонять `../`, `..\`, URL-encoded варианты (`%2e%2e%2f`); использовать встроенные средства языка (например, Python `pathlib.Path.resolve()` + `relative_to()`).

### Context editing integration
Memory tool сочетается с **context editing** (Anthropic очищает отдельные результаты инструментов на клиенте) для управления долгими диалогами.

### Using with compaction
Также сочетается с **compaction** (сервер сам суммаризирует весь диалог при приближении к лимиту контекстного окна). Для по-настоящему долгоживущих агентов рекомендуется использовать оба: compaction держит активный контекст маленьким без ручной бухгалтерии на клиенте, memory сохраняет то, что должно пережить суммаризацию.

### Multi-session software development pattern (ключевой раздел для этой вики)
Для софтверных проектов, растянутых на несколько агентных сессий, рекомендуется настраивать файлы памяти **осознанно заранее**, а не писать их по ходу дела:

1. **Initializer session** — первая сессия настраивает файлы памяти до начала содержательной работы: progress log (что сделано/что дальше), feature checklist (объём работы), ссылка на init/startup-скрипт проекта.
2. **Subsequent sessions** — каждая новая сессия начинает с чтения этих файлов памяти — восстанавливает состояние проекта без повторного исследования кодовой базы.
3. **End-of-session update** — перед завершением сессия обновляет progress log — что сделано, что осталось.

**Ключевой принцип:** работать над одной фичей за раз. Отмечать фичу завершённой только после сквозной верификации, что она реально работает, а не когда код написан. Это держит progress log точным от сессии к сессии.

Ссылка на детальный кейс-стади этого паттерна (initializer script, структура progress-файла, git-based recovery): [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) — см. отдельно зафиксированный источник `anthropic-long-running-agent-harness`.

## Проверка безопасности источника
Официальная техническая документация Anthropic, без пользовательского контента — инструкций агенту в тексте не обнаружено (кроме системной инструкции самого memory tool, которая является частью описания API-фичи, а не команды к этой вики).
