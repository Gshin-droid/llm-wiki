# Obsidian

**Тип:** инструмент (markdown-редактор / IDE для вики)
**Актуально на:** 2026-07-07

## Что это
Бесплатный локальный markdown-редактор с поддержкой wiki-ссылок `[[...]]` и графа связей. В [[persistent-wiki-pattern|паттерне персональной вики]] выступает "IDE" для просмотра — пользователь листает вики, ходит по ссылкам, смотрит граф, читает обновлённые страницы, которые пишет Claude Code.

## Роль в этой вики
Vault настроен на `C:\jarvis`, базовый конфиг лежит в `.obsidian/` (тема, wiki-links, граф с цветовой раскраской по типу страниц: entities/concepts/sources/projects/synthesis).

## Способы подключения к Claude (два разных подхода)
1. **Прямой доступ к файловой системе** (используется в этой вики) — Claude Code запускается прямо в папке vault, читает/пишет markdown-файлы напрямую, без посредников. Просто и достаточно для персональной вики.
2. **Через [[mcp-model-context-protocol|MCP]]** (см. [[project-documentation-vault-pattern]]) — плагин Local REST API в Obsidian + MCP-сервер (например, `obsidian-mcp-plugin`), даёт агенту доступ к vault даже при закрытом Obsidian, но требует больше настройки (API-ключи, сертификаты). Более уместно для командной работы над кодовым проектом, чем для личной вики.

## Известный пробел в этой вики
`raw/assets/` создана, но не настроена как Attachment folder path и не подключён хоткей на "Download attachments for current file" (Settings → Files and links) — из-за этого изображения из клипнутых статей не скачиваются локально, только по ссылкам, которые могут сломаться. См. [[persistent-wiki-pattern]].

## Связи
- Источники: [[karpathy-jarvis-personal-ai-memory]], [[karpathy-llm-wiki-gist]], [[bashkardinov-obsidian-claude-guide]]
- Дополняется расширением [[obsidian-web-clipper]]
- Концепты: [[persistent-wiki-pattern]], [[project-documentation-vault-pattern]]
