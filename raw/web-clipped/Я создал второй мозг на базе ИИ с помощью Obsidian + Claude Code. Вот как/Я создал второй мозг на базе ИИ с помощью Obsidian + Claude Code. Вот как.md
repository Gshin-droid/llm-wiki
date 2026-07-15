---
title: "\"Я создал второй мозг на базе ИИ с помощью Obsidian + Claude Code. Вот как\""
source: "https://habr.com/ru/companies/bothub/articles/985736/"
author:
  - "[[Мыслительный автор]]"
published: 2026-01-16
created: 2026-07-07
description: "Хватит делать заметки, которые пылятся. Пора создать систему, которая действительно думает вместе с вами. Я перепробовал все системы продуктивности. Базы данных Notion, которые превращались в цифровые..."
tags:
  - "clippings"
url: "\"https://habr.com/ru/companies/bothub/articles/985736/\""
fetched: " 2026-07-07T17:13:28+05:00"
---
[![](https://habrastorage.org/getpro/habr/branding/dee/dbf/75a/deedbf75a83f9ce41f3a64d7779131eb.png)](https://bothub.chat/?invitedBy=iTNi-351UcHgc1BxGFWim&utm_source=habr&utm_medium=banner)

[Автор оригинала: Sonny Huynh](https://sonnyhuynhb.medium.com/i-built-an-ai-powered-second-brain-with-obsidian-claude-code-heres-how-b70e28100099)

*Хватит делать заметки, которые пылятся. Пора создать систему, которая действительно думает вместе с вами.*

Я перепробовал все системы продуктивности. Базы данных Notion, которые превращались в цифровые кладбища. Доски Miro, которые выглядели впечатляюще, но никогда не помогали мне *делать* что-либо. Хаос Apple Notes. Всё по полной программе.

А потом что-то щёлкнуло. Я перестал пытаться создать лучшую систему заметок и начал строить кое-что другое: **второй мозг, который действительно работает со мной**.

Секрет? Сочетание локального, простого текстового формата Obsidian с возможностью Claude Code реально *работать* с вашими файлами. Не просто искать по ним. Не просто суммировать их. По-настоящему манипулировать, генерировать и улучшать их программно.

Вот система, которую я создал, и как вы можете построить свою.

![Скриншот системы](https://habrastorage.org/r/w1560/getpro/habr/upload_files/488/95a/ec4/48895aec40d1b5224c0d287e1e853817.png)

Скриншот системы

---

### Архитектура (она проще, чем вы думаете)

Магия здесь в том, что **Obsidian хранит всё в простых markdown-файлах на вашей машине**. Никаких проприетарных форматов. Никакой привязки к облаку. Просто папки с.md файлами, которые Claude Code может читать, записывать и напрямую манипулировать ими.

Три слоя просты: ваше хранилище Obsidian (простые markdown-файлы, которые принадлежат вам), Claude Code (читает, создаёт и манипулирует этими файлами), и результирующий «второй мозг» (автоматически связанные заметки, сгенерированные саммари, умное извлечение задач).

---

### Настройка фундамента

Сначала давайте установим всё необходимое. Я предполагаю, что у вас уже установлен Obsidian. Если нет — скачайте его с [obsidian.md](http://obsidian.md/) (бесплатно для личного использования).

### Шаг 1: Установите плагины, которые действительно важны

В Obsidian перейдите в Settings — Community Plugins и установите:

**Tasks:** Это основа. Он позволяет писать задачи где угодно в хранилище и запрашивать их откуда угодно.

**Templater:** Гораздо мощнее встроенных шаблонов. Можно запускать JavaScript, динамически подтягивать даты, даже вызывать внешние API.

**Dataview:** Думайте об этом как о SQL для ваших заметок. Запрашивайте своё хранилище как базу данных.

Вот и всё. Три плагина. Не попадайте в кроличью нору плагинов. Эти три покрывают 90% того, что вам нужно.

#### Шаг 2: Настройте Claude Code

Если вы ещё этого не сделали, установите Claude Code:

```bash
npm install -g @anthropic-ai/claude-codeОбъяснить с
```

Затем перейдите в папку вашего хранилища Obsidian в терминале:

```bash
cd ~/Documents/ObsidianVaultclaudeОбъяснить с
```

Вот и всё. Claude Code теперь имеет доступ ко всей вашей базе знаний.

---

### Рабочие процессы, которые изменили всё

Вот где становится интересно. Это реальные рабочие процессы, которые я использую ежедневно:

#### Рабочий процесс 1: Утренний мозговой штурм

Каждое утро я открываю терминал и набираю:

```
claude "Создай сегодняшнюю ежедневную заметку, используя мой шаблон. Подтяни все задачи со вчера, которые ещё открыты, и свяжи с проектами, над которыми я работал на этой неделе."Объяснить с
```

Claude Code читает мой шаблон Templater, генерирует ежедневную заметку, сканирует вчерашний файл на незавершённые задачи и создаёт мне отправную точку. **То, что раньше занимало 15 минут копирования-вставки, теперь занимает 30 секунд.**

#### Рабочий процесс 2: Обработка заметок со встреч

После любой встречи я сбрасываю свои сырые заметки в файл. Затем:

```
claude "Прочитай мою заметку со сегодняшнего стендапа и извлеки все пункты действий. Отформатируй их как Obsidian Tasks с датами выполнения на основе того, что обсуждалось. Помести их в мой файл tasks.md."Объяснить с
```

Он парсит такие вещи, как «Джон упомянул, что нам нужно закончить API к пятнице» и создаёт:

```
- [ ] Завершить реализацию API 📅 2026-01-10 #work/apiОбъяснить с
```

Плагин Tasks затем подхватывает это, и оно появляется в запросах моей ежедневной заметки. Ноль ручного форматирования.

#### Рабочий процесс 3: Еженедельный обзор

Пятница после обеда:

```
claude "Сгенерируй мой еженедельный обзор. Суммируй, над чем я работал, на основе ежедневных заметок этой недели, перечисли выполненные задачи, выяви заблокированные проекты и предложи приоритеты на следующую неделю."Объяснить с
```

Он создаёт форматированный markdown-документ, который реально помогает мне осмыслить неделю. Не рутина. Настоящий инструмент рефлексии.

---

### Система шаблонов

Вот взгляд на мой шаблон ежедневной заметки. Templater обрабатывает его, и Claude Code может генерировать заметки, следующие той же структуре:

```markdown
# <% tp.date.now("YYYY-MM-DD dddd") %>

## Фокус на сегодня
- 

## Задачи
\`\`\`tasks
not done
due before <% tp.date.now("YYYY-MM-DD") %>Объяснить с
```
```javascript
// ============ НАСТРОЙКИ (CONFIG) ============
const habitEmojis = ["🚶", "🍽️", "😴", "💻", "🪥"];
function isHabit(task) {
  return habitEmojis.some(emoji => task.text.includes(emoji));
}

// ВАЖНО: Ключи слева ("Work") должны совпадать с названиями ваших папок,
// а значение text справа ("Работа") — это то, что будет отображаться на экране.
const folderLabels = {
  "Work": { text: "Работа", color: "#3498db", emoji: "💼" },
  "Business": { text: "Бизнес", color: "#27ae60", emoji: "💳" },
  "Health": { text: "Здоровье", color: "#e74c3c", emoji: "🏃" },
  "Investing": { text: "Инвестиции", color: "#9b59b6", emoji: "💰" }
};

// ============ ЗАГОЛОВОК (HEADER) ============
const header = dv.el("div", "");
header.style.cssText = \`
  display: flex; justify-content: space-between; align-items: center;
  margin-bottom: 20px; padding-bottom: 16px;
  border-bottom: 1px solid var(--background-modifier-border);
\`;

const greeting = header.createDiv();
const hour = new Date().getHours();
const greetText = hour < 12 ? "Доброе утро" : hour < 17 ? "Добрый день" : "Добрый вечер";
// Можете заменить "Sonny" на свое имя
greeting.createEl("h2", {text: \`${greetText}, Sonny\`}).style.cssText = "margin: 0;";

const dateDiv = header.createDiv();
const today = new Date();
// Формат даты на русском
const options = { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' };
dateDiv.textContent = today.toLocaleDateString('ru-RU', options);
dateDiv.style.cssText = "font-size: 0.9em; opacity: 0.7; text-transform: capitalize;";

// ============ СТАТИСТИКА (STATS ROW) ============
const statsRow = dv.el("div", "");
statsRow.style.cssText = \`
  display: flex; gap: 12px; margin-bottom: 20px; flex-wrap: wrap;
\`;

// Получение данных
const allTasks = dv.pages().file.tasks;
// Корректировка начала недели (если у вас понедельник - начало, возможно потребуется minus({days: today.getDay() - 1}))
const thisWeekStart = dv.date("today").minus({days: today.getDay()});
const completedThisWeek = allTasks.where(t => t.completed && !isHabit(t)).length;
const openTasks = allTasks.where(t => !t.completed && !isHabit(t)).length;

// Расчет стрика привычек
// ВАЖНО: Убедитесь, что папка называется "Daily Journal" или измените название ниже
const dailyNotes = dv.pages('"Daily Journal"')
  .where(p => p.file.name.match(/^\d{4}-\d{2}-\d{2}$/))
  .sort(p => p.file.name, 'desc')
  .limit(7);

let habitsDoneToday = 0;
let habitsTotal = 6;
const todayStr = dv.date("today").toFormat("yyyy-MM-dd");
for (const note of dailyNotes) {
  if (note.file.name === todayStr) {
    const habits = note.file.tasks.where(t => isHabit(t));
    habitsDoneToday = habits.where(t => t.completed).length;
    habitsTotal = habits.length || 6;
    break;
  }
}

function createStatCard(emoji, label, value, subtext, color) {
  const card = statsRow.createDiv();
  card.style.cssText = \`
    background: var(--background-secondary);
    padding: 14px 18px; border-radius: 8px;
    min-width: 140px; border-left: 4px solid ${color};
  \`;
  card.createDiv({text: \`${emoji} ${label}\`}).style.cssText = "font-size: 0.8em; opacity: 0.7; margin-bottom: 4px;";
  card.createDiv({text: value}).style.cssText = \`font-size: 1.4em; font-weight: bold; color: ${color};\`;
  if (subtext) card.createDiv({text: subtext}).style.cssText = "font-size: 0.75em; opacity: 0.5;";
}

createStatCard("✅", "Завершено", completedThisWeek.toString(), "за неделю", "#27ae60");
createStatCard("📋", "Открыто", openTasks.toString(), "задач осталось", "#3498db");
createStatCard("🏃", "Привычки", \`${habitsDoneToday}/${habitsTotal}\`, "сегодня", habitsDoneToday >= habitsTotal ? "#27ae60" : "#f39c12");

// ============ БЫСТРОЕ ДОБАВЛЕНИЕ (QUICK ADD) ============
const quickSection = dv.el("div", "");
quickSection.style.cssText = \`
  background: var(--background-secondary);
  padding: 12px 16px; border-radius: 8px;
  margin-bottom: 20px; display: flex; gap: 8px; align-items: center;
\`;
quickSection.createSpan({text: "⚡"}).style.marginRight = "4px";
const quickNote = quickSection.createSpan({text: "Быстрое действие: Открыть сегодняшнюю заметку для записи мыслей"});
quickNote.style.cssText = "flex: 1; font-size: 0.85em; opacity: 0.7;";
const todayLink = quickSection.createEl("a", {text: "→ Открыть сегодня"});
todayLink.style.cssText = "font-size: 0.85em; cursor: pointer;";
// ВАЖНО: Проверьте путь к папке "Daily Journal"
todayLink.onclick = () => app.workspace.openLinkText(\`Daily Journal/${todayStr}\`, "", false);

// ============ ЯРЛЫКИ ПАПОК (FOLDER SHORTCUTS) ============
const shortcutsSection = dv.el("div", "");
shortcutsSection.style.cssText = \`
  display: flex; gap: 12px; margin-bottom: 24px; flex-wrap: wrap;
\`;

for (const [folder, info] of Object.entries(folderLabels)) {
  const card = shortcutsSection.createDiv();
  card.style.cssText = \`
    background: var(--background-secondary);
    padding: 16px 20px; border-radius: 8px;
    cursor: pointer; transition: transform 0.1s;
    border-top: 3px solid ${info.color};
    min-width: 120px; text-align: center;
  \`;
  card.onmouseenter = () => card.style.transform = "translateY(-2px)";
  card.onmouseleave = () => card.style.transform = "translateY(0)";
  card.onclick = () => app.workspace.openLinkText(folder, "", false);

  card.createDiv({text: info.emoji}).style.cssText = "font-size: 1.5em; margin-bottom: 6px;";
  card.createDiv({text: info.text}).style.cssText = "font-size: 0.9em; font-weight: 500;";
}

// ============ КАНБАН ЗАДАЧ (TASKS KANBAN) ============
const kanbanTitle = dv.el("h3", "📋 Задачи");
kanbanTitle.style.cssText = "margin: 0 0 12px 0;";

const dvToday = dv.date("today");

// Расчет границ календарной недели
const jsToday = new Date();
const dayOfWeek = jsToday.getDay(); // 0 = Воскресенье
// В России неделя обычно начинается с понедельника, логика ниже для воскресенья как начала
// Если нужно с Пн: const daysUntilSunday = 7 - (dayOfWeek === 0 ? 7 : dayOfWeek);
const thisWeekEnd = dvToday.plus({days: 6 - dayOfWeek}); 
const nextWeekEnd = thisWeekEnd.plus({days: 7}); 

const tasks = dv.pages().file.tasks.where(t => !t.completed && !isHabit(t));

const todayTasks = tasks.filter(t => {
  if (!t.due) return false;
  return t.due.ts <= dvToday.ts || t.text.includes("🔁");
});

const thisWeekTasks = tasks.filter(t => {
  if (!t.due) return false;
  return t.due.ts > dvToday.ts && t.due.ts <= thisWeekEnd.ts;
});

const nextWeekTasks = tasks.filter(t => {
  if (!t.due) return false;
  return t.due.ts > thisWeekEnd.ts && t.due.ts <= nextWeekEnd.ts;
});

const laterTasks = tasks.filter(t => {
  if (!t.due) return false;
  return t.due.ts > nextWeekEnd.ts;
});

const noDueTasks = tasks.filter(t => !t.due);

const kanban = dv.el("div", "");
kanban.style.cssText = \`
  display: flex; gap: 12px; margin-bottom: 24px;
  overflow-x: auto; padding-bottom: 8px;
\`;

function getLabel(task) {
  for (const [folder, info] of Object.entries(folderLabels)) {
    if (task.path.includes(folder)) return info;
  }
  return null;
}

async function completeTask(task) {
  const file = app.vault.getAbstractFileByPath(task.path);
  if (!file) return;
  const content = await app.vault.read(file);
  const lines = content.split("\n");
  if (lines[task.line]) {
    const todayDate = new Date().toISOString().split('T')[0];
    lines[task.line] = lines[task.line].replace("- [ ]", "- [x]").replace(/$/, \` ✅ ${todayDate}\`);
    await app.vault.modify(file, lines.join("\n"));
  }
}

function renderColumn(container, title, color, taskList) {
  const col = container.createDiv();
  col.style.cssText = \`
    flex: 1; min-width: 220px; max-width: 300px;
    background: var(--background-secondary);
    border-radius: 8px; padding: 12px;
    border-top: 3px solid ${color};
  \`;

  const colHeader = col.createDiv();
  colHeader.style.cssText = "display: flex; justify-content: space-between; margin-bottom: 10px;";
  colHeader.createEl("h4", {text: title}).style.cssText = "margin: 0; font-size: 0.9em;";
  colHeader.createSpan({text: taskList.length.toString()}).style.cssText = \`
    background: ${color}33; color: ${color};
    padding: 2px 8px; border-radius: 10px; font-size: 0.75em;
  \`;

  const list = col.createDiv();
  list.style.cssText = "max-height: 40vh; overflow-y: auto;";

  if (taskList.length === 0) {
    const empty = list.createDiv({text: "Нет задач"});
    empty.style.cssText = "color: var(--text-muted); font-size: 0.85em; padding: 8px; text-align: center;";
  } else {
    for (const task of taskList) {
      const item = list.createDiv();
      item.style.cssText = \`
        background: var(--background-primary);
        padding: 8px 10px; margin-bottom: 6px;
        border-radius: 5px; font-size: 0.85em;
        border-left: 3px solid var(--interactive-accent);
      \`;

      const topRow = item.createDiv();
      topRow.style.cssText = "display: flex; align-items: flex-start; gap: 8px;";

      const checkbox = topRow.createEl("input", {type: "checkbox"});
      checkbox.style.cssText = "margin-top: 2px; cursor: pointer;";
      checkbox.onclick = async (e) => {
        e.preventDefault();
        item.style.opacity = "0.5";
        item.style.textDecoration = "line-through";
        await completeTask(task);
      };

      const text = task.text
        .replace(/[📅🛫⏫🔼🔽🔁✅]\s*\d{4}-\d{2}-\d{2}/g, "")
        .replace(/[📅🛫⏫🔼🔽🔁]/g, "").trim();
      topRow.createSpan({text}).style.cssText = "flex: 1;";

      if (task.link) {
        const link = topRow.createEl("a", {text: "↗"});
        link.style.cssText = "font-size: 0.75em; opacity: 0.5; cursor: pointer;";
        link.onclick = (e) => { e.preventDefault(); app.workspace.openLinkText(task.link.path, "", false); };
      }

      const label = getLabel(task);
      if (label) {
        const labelSpan = item.createSpan({text: label.text});
        labelSpan.style.cssText = \`
          display: inline-block; margin-top: 6px; margin-left: 22px;
          padding: 2px 8px; font-size: 0.65em;
          background: ${label.color}; color: white; border-radius: 10px;
        \`;
      }
    }
  }
}

renderColumn(kanban, "🔴 Сегодня", "#e74c3c", todayTasks.array());
renderColumn(kanban, "🟠 Эта неделя", "#f39c12", thisWeekTasks.array());
renderColumn(kanban, "🔵 След. неделя", "#3498db", nextWeekTasks.array());
renderColumn(kanban, "🟣 Позже", "#9b59b6", laterTasks.array());
renderColumn(kanban, "⚪ Без даты", "#95a5a6", noDueTasks.array());

// ============ ПРИВЫЧКИ (HABITS STREAK) ============
const habitsTitle = dv.el("h3", "🏃 Привычки (7 дней)");
habitsTitle.style.cssText = "margin: 0 0 12px 0;";

// ВАЖНО: Текст привычек здесь должен точно совпадать с текстом задач в заметках
const habits = [
  {name: "Пройти 10к шагов", emoji: "🚶"},
  {name: "Есть до 2000 калорий", emoji: "🍽️"},
  {name: "Спать 7 часов", emoji: "😴"},
  {name: "1 час работы над проектом", emoji: "💻"},
  {name: "Почистить зубы (утро)", emoji: "🪥"},
  {name: "Почистить зубы (вечер)", emoji: "🪥"}
];

const habitsContainer = dv.el("div", "");
habitsContainer.style.cssText = \`
  background: var(--background-secondary);
  padding: 16px; border-radius: 8px; margin-bottom: 24px;
\`;

for (const habit of habits) {
  const row = habitsContainer.createDiv();
  row.style.cssText = "display: flex; align-items: center; gap: 12px; margin-bottom: 8px;";

  const label = row.createSpan({text: \`${habit.emoji} ${habit.name}\`});
  label.style.cssText = "width: 240px; font-size: 0.85em;";

  const dots = row.createDiv();
  dots.style.cssText = "display: flex; gap: 4px;";

  const notesReversed = [...dailyNotes].reverse();
  for (const note of notesReversed) {
    const dot = dots.createDiv();
    dot.style.cssText = \`
      width: 28px; height: 28px; border-radius: 4px;
      display: flex; align-items: center; justify-content: center;
      font-size: 0.7em;
    \`;

    const tasks = note.file.tasks.where(t => t.text.includes(habit.name));
    if (tasks.length === 0) {
      dot.style.background = "var(--background-primary)";
      dot.textContent = "—";
      dot.style.opacity = "0.3";
    } else if (tasks[0].completed) {
      dot.style.background = "#27ae60";
      dot.textContent = "✓";
      dot.style.color = "white";
    } else {
      dot.style.background = "#e74c3c";
      dot.textContent = "✗";
      dot.style.color = "white";
    }
    dot.title = note.file.name;
  }
}

// ============ НЕДАВНИЕ ЗАМЕТКИ (RECENT NOTES) ============
const recentTitle = dv.el("h3", "📝 Недавние заметки");
recentTitle.style.cssText = "margin: 0 0 12px 0;";

const recentNotes = dv.pages()
  .where(p => !p.file.path.includes(".obsidian") && !p.file.name.match(/^\d{4}-\d{2}-\d{2}$/))
  .sort(p => p.file.mtime, 'desc')
  .limit(5);

const recentContainer = dv.el("div", "");
recentContainer.style.cssText = \`
  background: var(--background-secondary);
  border-radius: 8px; overflow: hidden;
\`;

for (const note of recentNotes) {
  const row = recentContainer.createDiv();
  row.style.cssText = \`
    padding: 10px 14px; cursor: pointer;
    border-bottom: 1px solid var(--background-modifier-border);
    display: flex; justify-content: space-between; align-items: center;
  \`;
  row.onmouseenter = () => row.style.background = "var(--background-primary)";
  row.onmouseleave = () => row.style.background = "transparent";
  row.onclick = () => app.workspace.openLinkText(note.file.path, "", false);

  row.createSpan({text: note.file.name}).style.cssText = "font-size: 0.9em;";

  const folder = note.file.folder || "Корень";
  const folderSpan = row.createSpan({text: folder});
  folderSpan.style.cssText = "font-size: 0.75em; opacity: 0.5;";
}Объяснить с
```

**Понимание того, как на самом деле работают языковые модели, помогает использовать их эффективнее** - там, где они сильны, и с осторожностью там, где могут ошибиться.

**BotHub** открывает доступ к современным AI-моделям без барьеров!

![](https://habrastorage.org/r/w1560/getpro/habr/upload_files/2c4/bcc/67a/2c4bcc67ac65964c408a8c7608765a55.png)

Для доступа к сервису не требуется VPN, и можно использовать российскую карту.

> [**По ссылке вы можете получить 100 000 бесплатных токенов**](https://bothub.chat/?invitedBy=m_aGCkuyTgqllHCK0dUc7) **для первых задач и приступить к работе прямо сейчас!**

Спасибо за прочтение!

+8