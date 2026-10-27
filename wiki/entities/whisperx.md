# WhisperX

Обёртка над OpenAI Whisper: батчевый инференс (`faster-whisper`), точные word-level таймстемпы через forced alignment (wav2vec2), и — главное для этой записи вики — разделение по говорящим (speaker diarization) через `pyannote.audio`. Попал в вики как вторая половина наводки про локальную расшифровку записей; закрывающая страница — [[gigaam-whisperx-repo-review]].

**Тип:** инструмент (Python-пакет)
**Автор:** Max Bain (Оксфорд, VGG), INTERSPEECH 2023
**Лицензия:** BSD-2-Clause (код); модель диаризации `pyannote/speaker-diarization-community-1` — отдельно CC-BY-4.0 (pyannoteAI)
**Репозиторий:** https://github.com/m-bain/whisperX
**Актуально на:** 2026-10-27

## Что делает

ASR-движок — сам Whisper (`large-v2`/`large-v3`), WhisperX не заменяет и не превосходит его по WER — русской специфики нет, оценка качества текста на русском официальным README не заявлена. Добавляет: батчи для скорости («70x realtime» для large-v2), VAD-препроцессинг (снижает «галлюцинации» без потери WER), forced alignment через wav2vec2 для точных таймстемпов на уровне слова, и класс `DiarizationPipeline` для присвоения сегментам метки говорящего.

## Диаризация

Для включения — HF-токен и принятие лицензии модели `pyannote/speaker-diarization-community-1` на `huggingface.co`. Официальная оговорка качества (раздел «Limitations» README, допроверка 2026-10-27): **«Diarization is far from perfect»**, разделение внахлёст («overlapping speech») решается плохо и у Whisper, и у WhisperX. Отдельный незакрытый пункт TODO самого README: «Improve diarization (word level). Harder than first thought» — присвоение говорящего отдельному слову (не всему сегменту) остаётся нерешённой задачей по признанию автора, не мелкой деталью.

## Отличие VAD от диаризации (важно для наводок «Whisper + pyannote»)

Формулировка «Whisper плюс pyannote» в наводке инбокса смешивает две разные задачи `pyannote`: **VAD** (обнаружение присутствия речи, без меток говорящих — это то, что подключает [[gigaam]]) и **диаризация** (разметка говорящих — то, что подключает WhisperX через отдельную модель `speaker-diarization-community-1`). Это разные модели пакета `pyannote.audio`, легко спутать по одной строке пересказа.

## Берём?

Не ставим этим прогоном — для русской расшифровки с диаризацией архитектурно правильнее связка «[[gigaam]] для ASR + отдельно модель `pyannote/speaker-diarization-community-1` для разметки говорящих», а не замена движка на WhisperX целиком (у него ASR хуже на русском по официальной таблице GigaAM). Решение, ставить ли саму диаризацию при реальной задаче — не автономное, см. [[gigaam-whisperx-repo-review]].

## Источники в вики

- [[gigaam-whisperx-repo-review]]

## Связи

- Концепты: [[asr-benchmark-traps]], [[inverse-text-normalization]]
- Сущности: [[gigaam]]
