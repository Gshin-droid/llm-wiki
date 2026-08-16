# Claude Code changelog snapshot 2026-08-16

**Дата загрузки:** 2026-08-16
**Источник:** [raw/sources/claude-code-changelog-2026-08-16.md](../../raw/sources/claude-code-changelog-2026-08-16.md), официальный `CHANGELOG.md` репозитория `anthropics/claude-code` (verbatim, сверено напрямую через `raw.githubusercontent.com`)

## Саммари

Прогон разведчика через три дня после предыдущего снапшота (2026-08-13, покрывал до 2.1.231). Вышли **2.1.232** и **2.1.233** — оба крупные, десятки пунктов каждый. Три темы: (1) фичи кросс-сессионного канала связи — форк субагента по умолчанию наследует весь диалог, `@`-упоминание для прямого обращения к другой сессии; (2) очередная волна bypass-фиксов permission-анализатора и сэндбокса, продолжающая серию, отслеживаемую в [[ai-security-by-design]] с 07-19; (3) первое упоминание **GitLab** в этой вики — до сих пор весь цикл разработки (`--worktree`, plugin marketplaces, secret redaction) был описан только для GitHub.

## Ключевая находка 1: форк субагента наследует диалог целиком, `@`-упоминание для прямого обращения (2.1.232)

*"Enabled subagent forking by default with full conversation inheritance"* — до этого релиза форк субагента (тот же механизм, что стоит за `/fork`, см. [[claude-code]] раздел "Обновление 2.1.211–2.1.214") создавал новую фоновую сессию, но не обязательно передавал ей весь диалог целиком; теперь наследование полного диалога — поведение по умолчанию. Практически: форкнутый субагент стартует не с чистого листа, а зная всё, что видел родитель на момент форка — меньше повторного объяснения контекста, но и больше данных, унаследованных без явного отбора (в терминах [[ai-security-by-design]] — расширение поверхности того, что доступно порождённому агенту).

*"Added `@` mention syntax for direct cross-session communication"* — прямое продолжение межмашинного канала `SendMessage`/`ListAgents`, разобранного 08-10 и 08-13 ([[claude-code-changelog-snapshot-2026-08-10]], [[claude-code-changelog-snapshot-2026-08-13]]): вместо вызова `SendMessage` с именем сессии как параметром теперь можно упомянуть сессию прямо в тексте (`@session-name`) — эргономика поверх уже существующего механизма, не новый канал. Тем же релизом *"Improved `SendMessage` delivery to bare session names"* и *"Enforced unique session names with automatic variant generation"* — раньше два конфликтующих имени сессии могли создавать неоднозначность адресата; теперь имена уникализируются автоматически.

## Ключевая находка 2: продолжение серии bypass-фиксов — PowerShell, Windows symlink, cross-session messaging, Linux sandbox (2.1.232), NTLM (2.1.233)

Та же категория, что уже отслеживается в [[ai-security-by-design]] с 07-19 (Bash-анализатор) и с 08-10 (межмашинный канал) — механизм продолжает давать течь месяцами:

- *"Fixed PowerShell variable-writing permission bypass"* — команда PowerShell могла записать переменную в обход разрешений.
- *"Resolved Windows symlink traversal security issue"* — обход через симлинк на Windows, тот же класс, что Windows NT device paths ниже.
- *"Fixed nested repository trust inheritance"* — вложенный репозиторий (submodule/вложенный клон) мог неверно наследовать статус доверия родительского.
- *"Hardened cross-session messaging socket directory security"* — сам новый канал `@`-упоминаний/`SendMessage` выше получил укрепление сокет-директории, которой он пользуется.
- *"Strengthened Linux filesystem sandbox protection"*, *"Restricted `sandbox.ripgrep` configuration sources"* — сужение того, откуда конфигурация `ripgrep`-инструмента внутри сэндбокса может подтягиваться.
- *"Implemented Bash input redirection permission checking"* (2.1.232) — редирект ввода (`<`) в Bash-командах теперь тоже проверяется анализатором прав, ранее находка того же класса про redirect касалась только file-descriptor вывода (07-19).
- **2.1.233**: *"Closed NTLM credential leak vector via Windows NT device paths"* — NT device path (`\\.\`-нотация) мог использоваться, чтобы утащить NTLM-креды в обход обычной файловой проверки; тот же общий класс, что и Windows symlink traversal выше, но отдельный вектор.

Ни один из фиксов не меняет практическую механику, уже описанную в вики — все они закрывают конкретные дыры в уже существующих механизмах (permission-анализатор, сэндбокс, межагентный канал), не вводят новых правил.

## Находка 3: первое упоминание GitLab в этой вики (2.1.232–2.1.233)

До этого снапшота весь цикл разработки, описанный в вики (worktree, plugin marketplaces, secret redaction, agent view) был завязан только на GitHub. Этот релиз явно расширяет то же самое на GitLab:
- *"Added support for GitLab merge request URLs in the `--worktree` flag and agent view displays"* (2.1.233) — worktree можно завести прямо по ссылке на GitLab MR, не только GitHub PR.
- *"Implemented secret redaction for GitLab token families"* (2.1.232) — GitLab-токены попали в тот же список маскируемых секретов, что и GitHub-токены.
- *"Extended GitLab support to plugin marketplaces"* (2.1.232) — маркетплейсы плагинов (до сих пор — git/npm/`archive`/`command`, см. [[claude-code-changelog-snapshot-2026-08-13]]) теперь можно раздавать и через GitLab-репозитории.

Не мультипровайдерность в духе [[opencode]] (там выбор LLM-провайдера), а расширение платформы хостинга кода, на которой Claude Code умеет работать нативно — для этой вики не актуально практически (репозиторий на GitHub), но меняет границу продукта.

## Малое

- **Fable 5 доступность восстановлена для организаций с доступом** (2.1.232, *"Restored Fable 5 availability for organizations with access"*) — багфикс, не изменение модели; сама Fable 5 уже описана в [[claude-code]] как фолбэк для самых тяжёлых автономных задач и как модель, на которую переключает content-based fallback.
- **Ограничение task-tracking инструментов на новых версиях моделей, с опцией override** (2.1.233) — не раскрыто подробнее в changelog; возможно, связано с уже отмеченной в [[claude-code]] ("Модели и Effort") склонностью Opus 5 к избыточной самопроверке — направление то же (новые модели получают более узкое дефолтное поведение вместо более широкого), но прямой связи changelog не называет, оставлено как открытый вопрос.
- `forward_user_identity` — opt-in настройка для атрибуции расходов по пользователю (Enterprise-функция, не применима к этой вики).
- Memory cgroup для Linux Bash — защита от исчерпания ресурсов, тот же принцип "безопасность по умолчанию", что и лимиты runaway-циклов ([[ai-security-by-design]]).
- `claude plugin validate` теперь проверяет frontmatter скилл-markdown — расширение существующей команды валидации плагинов.
- Самокоррекция: 2.1.233 откатывает часть Bash-изменений 2.1.232 для Cygwin-симлинков и input redirections — редкий случай, когда фикс безопасности предыдущей версии сам оказался регрессией и был частично отменён в следующей же версии.

## Связанные страницы

- [[claude-code]] — обновлён раздел changelog
- [[ai-security-by-design]] — дополнена серия bypass-фиксов
- [[claude-code-changelog-snapshot-2026-08-13]] — предыдущий снапшот в серии
