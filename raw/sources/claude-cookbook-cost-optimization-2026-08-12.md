---
source: официальный notebook Claude Cookbooks (anthropics/claude-cookbooks)
url: https://github.com/anthropics/claude-cookbooks/blob/main/cost_optimization/cost_optimization.ipynb
raw_url: https://raw.githubusercontent.com/anthropics/claude-cookbooks/main/cost_optimization/cost_optimization.ipynb
retrieved: 2026-08-17
notebook_added: 2026-08-12 (PR #824/#825, "cj-ant")
method: WebFetch дважды (первый проход — общая структура и цифры, второй — верификация цифр и точных формулировок markdown-ячеек); прямого построчного дампа JSON нет, инструмент отдаёт саммари модели поверх содержимого файла
---

# Cost Optimization on the Claude API (Claude Cookbooks)

Официальный обучающий notebook Anthropic. Сквозной пример — агент адъюдикации автостраховых случаев для вымышленной компании Acme Insurance: агент расследует случай и выносит вердикт (approve / deny / refer to supervisor / escalate to fraud unit).

## Инструменты агента в примере
Восемь инструментов расследования: `get_claim`, `get_policy`, `get_customer_history`, `check_fraud_signals`, `lookup_repair_estimate`, `get_damage_photos`, `calculate_payout`, `request_docs`. Плюс четыре терминальных инструмента вердикта.

## Чеклист из семи шагов (порядок применения)
1. **Baseline** — «get it working on a capable model, build an eval, and measure a baseline».
2. **Prompt caching** — «reuse your tokens on subsequent turns instead of reprocessing them».
3. **Input token management** — «let the model discover context via tools» (вынос больших справочников за инструмент retrieval вместо системного промпта).
4. **Agent-loop efficiency** — «keep multi-turn context from compounding».
5. **Output token management** — «hand the model tighter generation constraints».
6. **Batch API** — «defer non-interactive workloads to an async queue».
7. **Model selection** — «find the cheapest tier that still clears your quality bar».

## Цифры (подтверждены двумя независимыми проходами fetch)
- Baseline: **10/10** верных вердиктов на eval-наборе, **$0.29/задача**.
- Prompt caching (автокэширование, два хода подряд): **−32%** стоимости.
- Byte-stable prefix (статический префикс не меняется побайтово между вызовами): **−44%** относительно нестабильного префикса.
- Explicit cache breakpoints (стабильный контент явно вынесен перед переменным по-заявочным): **−54%** на трёх кейсах.
- Batch API: скидка **50%** на стоимость токенов (общеизвестная цифра платформы, в этом notebook не переоткрывается, а используется).

## Код-паттерны, упомянутые в notebook
- `cache_control={"type": "ephemeral"}` для автоматического кэширования.
- Переменный контент (метки времени и т.п.) — в user-сообщении, а не в system prompt, чтобы не портить byte-stable префикс.
- Крупный справочник (упомянут объём ~11K токенов) вынесен за инструмент, вызываемый по необходимости, вместо статичной вставки в system prompt.
- `defer_loading: True` в tool search — отложенная подгрузка схем редко используемых инструментов.

## Таблица цен по моделям, показанная в notebook
Второй проход fetch вернул таблицу (Fable $10/$50, Opus $5/$25, Sonnet $2/$10, Haiku $1/$5 за MTok вход/выход) — **не перепроверена построчным чтением файла**, взята только со слов инструмента-саммаризатора; расходится с ценой Opus 5 fast mode ($10/$50), уже зафиксированной на [[claude-opus-5-launch]]. В саму страницу источника эта таблица цен не внесена как факт — см. секцию «Что не взято» на странице [[claude-cookbook-cost-optimization]].

## Проверка безопасности
Материал — официальный обучающий notebook Anthropic, инструкций, адресованных агенту-разборщику, не содержит.
