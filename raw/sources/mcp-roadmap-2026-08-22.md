---
source: официальный блог Model Context Protocol
url: https://blog.modelcontextprotocol.io/posts/mcp-roadmap/
retrieved: 2026-09-01
published: 2026-08-22
---

# The New MCP Roadmap

Опубликовано maintainers MCP 22.08.2026. Обновлённая дорожная карта развития протокола — не спецификация, а объявление направлений после ревизии 2026-07-28.

Прогресс с марта 2026: stateless-архитектура протокола и переработанные примитивы агентской коммуникации, принятые в релизе 2026-07-28.

## Пять приоритетных направлений

### 1. Agentic messaging primitives
Современные агентские нагрузки не укладываются в паттерн request-response. Нужны server-initiated события и зрелость расширения Tasks. Ключевые механизмы: Tasks extension (SEP-2663), `subscriptions/listen`, progress notifications, server-initiated события (webhooks и каналы). Задействованы working groups: Agents, Transports, Triggers & Events.

### 2. HTTP-native transport unification and hardening
После релиза 2026-07-28 удалённый MCP-сервер ничем не отличается от обычной HTTP-нагрузки. Цель — унифицировать режимы развёртывания: Streamable HTTP для удалённых серверов, stdio — для локальных, поверх той же stateless-архитектуры.

### 3. Agent identity and enterprise-ready security
Всё больше вызовов идёт от агентов, работающих как облачные нагрузки, а не от человека в браузере — нужно стандартизировать распознавание идентичности агента и делегирование полномочий (в т.ч. субагентам). Механизмы: Demonstrating Proof of Possession (DPoP, RFC 9449), Workload Identity Federation, ID-JAG grant, расширение Enterprise-Managed Authorization, стандартный token exchange. Продолжается взаимодействие с рабочими группами IETF OAuth и WIMSE.

### 4. Improved primitives
Tool calling — первое, с чем сталкивается разработчик MCP, но обработка результата инструмента не стандартизирована, а клиенты сейчас скачивают весь каталог тулов сразу. Нужна стандартизация контракта результата `tools/call` и «progressive discovery» — постепенное раскрытие тулов вместо загрузки целого каталога, для серверов с большим числом инструментов.

### 5. Improved SDK developer experience
Инвестиции в эргономику SDK, conformance-тестирование на соответствие спецификации, понятные API и документацию по всем поддерживаемым языкам/платформам. Отдельно отмечена ценность чётких реализаций для генерации кода агентами.

## Участие
Через working groups, Specification Enhancement Proposals (SEP) и прямые контрибуции по contributing guide. Точных сроков реализации для большинства пунктов не названо — это направления, а не committed release-план.
