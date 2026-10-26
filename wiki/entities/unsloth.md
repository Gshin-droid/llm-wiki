# Unsloth

Библиотека и Desktop-приложение для быстрого и экономного по памяти дообучения (fine-tuning) открытых LLM — QLoRA с собственными оптимизированными ядрами. В вики раньше упоминался только как издатель сжатых GGUF-сборок чужих моделей (например, `unsloth/embeddinggemma-2-GGUF`); с разбором [[unsloth-decision-model-training]] попал как полноценная сущность — автор `FastDecisionModel`/`DecisionTrainer`, официального рецепта дообучения моделей решений того же класса, что [[laya]] и [[jev-typesafe]].

**Тип:** инструмент / компания
**Актуально на:** 2026-10-26 (release notes v0.1.904-beta/v0.1.906-beta, README `unslothai/notebooks`)
**Разработчик:** Daniel Han-Chen и команда Unsloth · **Репозитории:** `github.com/unslothai/unsloth` (Apache-2.0), `github.com/unslothai/unsloth-zoo` (LGPL-3.0), `github.com/unslothai/notebooks`

## Decision models (2026-10)

`FastDecisionModel.from_pretrained` превращает обычную LLM (Qwen, Llama, Gemma) в модель решений: вход — состояние и вопросы, выход — выбор/да-нет/оценка с калиброванной вероятностью, без генерации текста. Голова — «Clef-style» (по собственному описанию — тот же дизайн, что у Cloudflare Clef). Обучение — QLoRA через `DecisionTrainer`, калибровка — `FastDecisionModel.calibrate` на отложенной выборке. Поддерживает дообучение моделей решений с нуля и доведение уже готовых чекпоинтов, включая [[laya]] («Laya (fine-tuned)» в бенчмарк-таблице — 77%, 2,5 ГБ, 10 минут обучения). Можно обучать на Mac (release v0.1.906-beta: «Train Laya and Clef decision models on Mac»), экспортировать в GGUF и запускать через `llama.cpp`.

Своя Decision API (в составе Unsloth Desktop) регистрирует дообученную модель под именами `laya`, `default` или `jev-latest` — подмена без изменения кода, который зовёт один из этих эндпоинтов.

**Лицензия расходится внутри проекта.** Основной пакет — Apache-2.0, `unsloth-zoo` — LGPL-3.0, но конкретно файл `unsloth/models/decision_from_lm.py` несёт заголовок `SPDX-License-Identifier: AGPL-3.0-only` (прочитано напрямую). AGPL — сетевой копилефт: обязательства распространяются именно на код decision-моделей, если он когда-нибудь будет отдавать инференс как сетевой сервис, а не только использоваться для локального обучения.

## Доступность

`unsloth.ai` (официальная документация) недостижим из автономного прогона этой вики (`getaddrinfo ENOTFOUND`, зафиксировано 2026-10-26) — первоисточник документации читан по копии, захваченной в raw-файл при отправке в инбокс, не напрямую. `github.com`/`raw.githubusercontent.com` (репозитории, release notes, лицензии) открылись штатно и читались напрямую.

## Связи

- Источники в вики: [[unsloth-decision-model-training]], [[embeddinggemma-2-model-card]] (GGUF-сборка как побочный издатель)
- Сущности: [[laya]], [[jev-typesafe]]
- Концепты: [[kalibrovka-uverennosti-resheniy]]
