---
url: https://gomymy64.github.io/jarvis-memory/#steps
title: "Claude Code + Obsidian ВЗОРВАЛИ Интернет | Метод Андрея Карпати"
fetched: 2026-07-07
note: Страница — JS SPA (GitHub Pages), извлечён текстовый контент через рендер-фетч, не полный HTML.
---

# Claude Code + Obsidian: Personal Knowledge System

## Title
"Claude Code + Obsidian ВЗОРВАЛИ Интернет | Метод Андрея Карпати"

## Main Concept
Гайд учит строить "Jarvis" — персональную AI-систему памяти на базе Claude Code и Obsidian. Claude постепенно строит и поддерживает персистентную вики — структурированные, взаимосвязанные markdown-файлы, которые накапливают и синтезируют знания, вместо повторного извлечения из сырых документов при каждом запросе.

## Five Core Skills
1. Knowledge Base Construction — персональный AI-ассистент, понимающий цели и стратегии пользователя
2. Web Scraping — превращение URL в извлечённый текст, изображения и структурированные сущности
3. Browser Integration — сохранение статей в один клик через Web Clipper
4. Synthesis Documents — генерация взаимосвязанных wiki-саммари
5. Architecture Understanding — когда использовать Obsidian, Pinecone или NotebookLM

## Required Tools (8-part stack)
- Obsidian (free)
- Antigravity IDE (free preview)
- Claude Code (Pro/Max)
- Obsidian Web Clipper (free)
- Pinecone (freemium)
- NotebookLM (free)
- Karpathy's original Gist
- Habrahabr article

## Eight-Step Implementation
1. Скачать Obsidian, включить Dark Mode, оставить открытым
2. Создать пустую папку "Jarvis"; открыть в Antigravity; запустить Claude через терминал
3. Дать Claude два системных промпта, устанавливающих правила управления вики и архитектуру папок (raw/sources/, wiki/entities/, wiki/synthesis/ и т.д.)
4. Дать первый источник (URL); Claude скрейпит контент и создаёт первые wiki-страницы
5. Установить расширение Web Clipper; настроить vault и шаблон назначения
6. Подключить папку Jarvis к Obsidian как vault; визуализировать граф связей
7. Задать Claude синтез-вопрос; система генерирует новую страницу в wiki/synthesis/ с цитатами
8. Осознать ограничения системы; интегрировать Pinecone для больших архивов и NotebookLM для глубокого research

## Architecture (Three Layers)
- **Raw Sources** — неизменяемая курированная коллекция (статьи, PDF, изображения)
- **Wiki** — сгенерированные markdown-файлы с саммари, сущностями, концептами, синтезом
- **Schema** — CLAUDE.md, конфигурационный файл, управляющий операциями

## Key Operations
- **Ingest** — загрузить источник; Claude читает, обсуждает выводы, пишет саммари, обновляет 10-15 страниц
- **Query** — задать вопрос; Claude ищет по индексу, синтезирует ответ с цитатами, сохраняет ценные ответы как новые wiki-страницы
- **Lint** — периодическая проверка здоровья: противоречия, страницы-сироты, битые ссылки

Ключевая мысль источника: "утомительная часть баз знаний — не чтение, а бухгалтерия" — обновление ссылок и консистентности на десятках файлов автоматизируется через LLM, снижая трение поддержки.
