# Claude Code changelog + Platform release notes 2026-08-22

**Дата загрузки:** 2026-08-22
**Автор:** [[claude-code]]
**Опубликовано:** 2026-08-19 — 2026-08-22
**Тип:** официальная документация (changelog + release notes)
**Ссылка:** https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md ; https://platform.claude.com/docs/en/release-notes/overview
**Raw:** `raw/sources/claude-code-changelog-2026-08-22.md`, `raw/sources/claude-platform-release-notes-2026-08-20.md`

## Саммари

Прогон новостного разведчика через три дня после предыдущего снапшота (2026-08-19, покрывал до 2.1.235). Вышли **2.1.236–2.1.240** Claude Code — без единого headline-фикса, зато официальные **Claude Platform release notes** за то же окно (08-19–08-20) принесли заметно больше: **Python SDK v1.0** с ломающими изменениями, **browser use tool** — новый агентский инструмент, **computer use tool** вышел из беты, и разом out-of-beta ушли Files API, Agent Skills API, Admin API user-management. Обе стороны платформы связаны напрямую: новая subcommand `/claude-api upgrade` в Claude Code 2.1.239 — это ровно миграционный помощник под breaking changes SDK v1.0, вышедший на день позже.

**Оговорка источника.** Оба фрагмента получены через `WebFetch` (модель-посредник извлекает текст по URL), а не построчным `curl`/`raw.githubusercontent.com`, как в снапшотах 08-16/08-19 — сетевой доступ этого прогона отличался (см. «Проверка безопасности источника»). Текст changelog сверен по номерам версий и формулировкам, дословность отдельных фраз не подтверждена побайтово.

## Находка 1: Python SDK v1.0 — первая мажорная версия с breaking changes (2026-08-20)

Официальная запись `platform.claude.com` от 20.08: HTTP-слой SDK переехал с `httpx` на **httpx2** (поддерживаемый API-совместимый форк) — кастомные `http_client`/`Timeout`/transport-объекты нужно строить из `httpx2`, а библиотекам трассировки/моков, патчащим `httpx` напрямую, требуется вызов `httpx2.alias_httpx()` при старте. Требует Python 3.10+. Из SDK убрано давно депрекированное: legacy Text Completions API, параметры `temperature`/`top_p`/`top_k` у методов Messages, клиентский `compaction_control` тул-раннера. У асинхронного клиента `.with_raw_response` теперь требует `await response.parse()`; `AnthropicBedrock` без сконфигурированного региона AWS теперь падает ошибкой вместо тихого дефолта на `us-east-1`.

Прямая связь с Claude Code: релиз **2.1.239** (на день позже) добавил `/claude-api upgrade` — subcommand встроенного скилла `claude-api` для миграции Python-проектов с `anthropic` 0.x на 1.x. Не совпадение по времени — миграционный помощник вышел ровно под этот breaking release. Для любого кода, использующего `anthropic` Python SDK (включая примеры `client.beta.agents.create(...)` на странице [[claude-managed-agents]]), апгрейд на 1.x требует ревизии: убранные параметры сэмплинга и Text Completions API в этой вики нигде не используются напрямую, но правило важно знать наперёд.

## Находка 2: browser use tool — новый агентский инструмент, computer use вышел из беты (2026-08-19)

Anthropic развела единый "computer use" на два инструмента:

- **`computer_toolset_20260801`** (был в бете) — теперь без beta-заголовка, добавлены **batch actions** (несколько действий за один ход модели вместо одного клика на ход) и `zoom` включён по умолчанию; per-member конфигурация через `configs`. Старые бета-версии тула остаются доступны для обратной совместимости.
- **`browser_toolset_20260801`** (новый) — client-side тулсет для управления браузером, который хостит приложение разработчика, а не весь десктоп. Работает внутри viewport браузера: читает саму страницу (accessibility tree, элементы, формы, вкладки) и добавляет element references, ввод в формы, управление вкладками, отчёт о загрузках и опциональную загрузку файлов — поверх обычного screenshot-and-click.

Оба тулсета доступны на Claude Fable 5, Claude Mythos 5, Claude Opus 5, Claude Sonnet 5 и Claude Opus 4.8. Практическое отличие для выбора: computer use — управление целой машиной (нужен полноценный desktop-сэндбокс), browser use — только вкладка браузера приложения, дешевле и безопаснее по площади атаки, если задаче не нужен весь рабочий стол.

## Находка 3: разом out-of-beta — Files, Agent Skills, Admin API user-management (2026-08-19)

Три отдельных куска платформы синхронно потеряли статус беты в один день:

- **Files API** — `/v1/files` и Messages-запросы со ссылкой на загруженный файл больше не требуют заголовка `files-api-2025-04-14`; без заголовка отдаётся текущий формат ответа (`expires_at`, `page`/`next_page`-пагинация, фильтр `ids[]`). Запросы со старым заголовком продолжают работать по-старому.
- **Agent Skills / Skills API** (`/v1/skills`) — заголовок `skills-2025-10-02` больше не обязателен, включая загрузку skills через параметр `container` в Messages API.
- **Admin API user-management для Claude Enterprise** — заголовок `ce-user-management-2026-07-13` больше не обязателен для group/custom-role запросов.

Ни одно из трёх не меняет практическую механику для этой вики — все три уже использовались через бету там, где применимо (Skills — тот механизм, что стоит за самим `claude-skills`). Записано ради полноты: снятие беты обычно сигналит, что API-поверхность стабилизировалась и дальше будет меняться реже.

## Находка 4: точечные расширения Claude Managed Agents (2026-08-19)

Две вещи прямо касаются уже задокументированной страницы [[claude-managed-agents]]:

- **`allowed_domains`/`blocked_domains` на `web_search`/`web_fetch`** — впервые агенту можно ограничить, какие сайты доступны его тулам, через `configs`-массив `agent_toolset_20260401` (`web_fetch` также получил `max_content_tokens`, `web_search` — `user_location`). До сих пор `agent_toolset_20260401` управлялся только `name`/`enabled`/`permission_policy` без per-tool домен-фильтра.
- **Self-hosted sandbox теперь поддерживает memory stores** — SDK-воркеры (Python/TypeScript/Go) сами скачивают примонтированный store в sandbox по `mount_path` и синхронизируют изменения агента обратно. Раньше memory stores (см. раздел «Экосистема» на [[claude-managed-agents]]) были доступны только в managed cloud-sandbox.

Плюс редизайн session viewer в Console (timeline-минимапа, транскрипт по группам model request, Inspector-панель) — не API-изменение, чисто UI Console.

## Что не взято

- Аренда Workbench→Playground (18.08) — уже разобрана и осознанно отброшена прошлым снапшотом ([[claude-code-changelog-snapshot-2026-08-19]]), повторно не пересказывается.
- Полный список рутинных багфиксов 2.1.236–2.1.240 (десятки пунктов terminal/UI/Remote Control) — в raw-снапшоте, на страницу вынесены только пункты с практическим эффектом (`ANTHROPIC_DEFAULT_MODEL`, `self-hosted-runner --defer-shutdown-max-min`, `headersHelper` для маркетплейсов плагинов, `notify_when_idle` у `SendMessage`, cost estimate с data-residency премией) — см. раздел changelog на [[claude-code]].
- Дословная точность отдельных формулировок changelog не проверена букве-в-букву (см. оговорку источника выше) — при следующей сверке стоит перечитать прямым `raw.githubusercontent.com`, если сетевой доступ это позволит.

## Оценка источника

Официальная документация Anthropic обеих категорий (Claude Code changelog + Claude Platform release notes) — высшая презумпция доверия по `references/source-evaluation.md`. Единственная оговорка — метод получения (WebFetch-посредник, не прямой построчный фетч), см. выше; это снижает уверенность в дословности цитат, не в фактической части (номера версий, названия полей API, даты).

## Проверка безопасности источника

Оба документа — открытая официальная документация Anthropic, никаких пользовательских данных или исполняемых инструкций внутри текста; инструкций, замаскированных под команды агенту, не обнаружено.

## Связи
- [[claude-code]] — обновлён раздел changelog, дата «Актуально на» сдвинута на 2026-08-22
- [[claude-managed-agents]] — дополнена «Экосистема» (domain-фильтр web_search/web_fetch, self-hosted memory stores)
- [[claude-code-changelog-snapshot-2026-08-19]] — предыдущий снапшот в серии
- [[claude-api-cost-optimization]] — соседний официальный чеклист того же API-поверхности
