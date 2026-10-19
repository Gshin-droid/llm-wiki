---
source: ai-assistant #74
type: url
captured: 2026-10-12 10:23:43
via: "сводка обсуждений"
url: "https://github.com/mach10x/strata"
---

# Strata: локальный запуск крупной модели Qwen3.8-Flash-Next

Опенсорсный Strata позволяет гонять Qwen3.8-Flash-Next локально, без аккаунтов и внешних серверов. Заявленные требования: видеокарта NVIDIA или AMD от 12 ГБ VRAM и минимум 32 ГБ оперативки, для всех основных сборок нужно 64 ГБ. Качество и скорость в чате не обсуждали, это только анонс.

Найдено в обсуждении практиков вайбкодинга, 09.10.2026. Пересказ без цитат и без привязки к источнику обсуждения.

## GitHub - mach10x/strata: Qwen3.8-Flash-Next on any consumer hardware: one-click install for Windows / Linux. Strata inference engine, OpenAI/Anthropic API on localhost, optional image input.

https://github.com/mach10x/strata

Run a 125-billion-parameter AI model on your own gaming PC
NVIDIA or AMD graphics card (12 GB or more) · Windows or Linux · free and open source
A voxel pagoda garden, 1 shot prompt running on an RTX 5070 with Strata (IQ3_S, 128K context) ·
full video (49 s)
Strata runs Qwen3.8-Flash-Next - a large, smart AI model that normally needs a server - on a normal PC. It chats, writes code, reads pictures and works with your apps and coding agents, and nothing leaves your PC.
Measured on two ordinary gaming PCs. "Writes answers" is how fast the reply appears in a short chat; "reads your prompt" is how fast it takes in what you send (a 32K-token document, code or chat history). A token is about ¾ of a word, so 60 tokens per second is faster than you can read.
| NVIDIA: RTX 5070 (12 GB), Ryzen 5 7600, 64 GB RAM | AMD: RX 9070 XT (16 GB), Ryzen 9 3900X, 47 GB RAM | ||||||||||||||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 
 | 
 | 
A card with more VRAM is faster: an RTX 3090 (24 GB) should write roughly 100-140 tokens per second. Long chats, other cards: speed of each model, community results.
Strata is free. If it runs well on your PC, a coffee keeps the work on it going.
| Graphics card | NVIDIA GeForce RTX 20, 30, 40 or 50 series, or AMD Radeon RX 7900 XT / XTX, RX 7800 XT / 7700 XT, RX 9060 XT, RX 9070 / 9070 XT, Radeon AI PRO R9700 or RX 6800 / 6900 series - with 12 GB of VRAM or more | 
| RAM | 32 GB or more - how much decides which model fits; 64 GB runs every size | 
| Disk | about 80 GB free, on an SSD if you can (the first start is much faster) | 
| System | Windows 10 / 11 or Linux, and a current graphics driver from NVIDIA or AMD | 
Everything else is installed for you. Two or three cards can share the model (multi-GPU). The full list: docs/INSTALL.md.
Use an AI coding assistant (Claude Code, Cursor, Codex, GitHub Copilot, ...)? Paste this into it:
Set up Strata on this PC for me: https://github.com/Niko1221/Strata - follow docs/AI_SETUP.md in that repository.
It checks your graphics card, RAM and disk, picks the model that fits, installs it, starts it and tells you how to connect your apps. AI tools can also install, start and stop Strata themselves through its MCP server.
Download Strata and unzip it (or git clone it).
Windows: double-click START-HERE.bat. Linux: run ./setup.sh in the Strata folder.
The same steps for NVIDIA and AMD: the installer finds your card and sets up the right engine for it. It asks which
model, which size, how much context (how much text it keeps in mind) and whether it should read pictures - press
Enter each time for the recommended answer. Then it downloads the model (~70 GB; you can stop and it continues where
it left off) and starts it. Your browser opens the Strata app at http://127.0.0.1:8080.
While the model starts, your PC can be slow or stop responding for 1-3 minutes (longest the first time): Strata loads 35-55 GB into your RAM and locks part of it for the graphics card. That's normal - wait, and don't close the window. The window tells you what it is doing.
Next time, run START-HERE.bat (or ./setup.sh) again: it starts right away, nothing is downloaded twice. Close
its window to stop the model. Updating, Docker, several cards, where the files go and every option:
docs/INSTALL.md.
The installer recommends one for your RAM. The same model comes in sizes that are compressed more or less: smaller is faster, larger is a bit smarter.
| Your RAM | Take | Why | 
|---|---|---|
| 32 GB | Coder | it fits 32 GB, and it is made for code (with a 24 GB card, Q2_0 and IQ2_XS run too) | 
| 48 GB | IQ2_XS (or Q2_0, the fastest) | the larger sizes do not fit | 
| 64 GB | IQ2_XS (recommended), or IQ3_XXS / IQ3_S | every size fits; IQ3_S is the best, and the slowest | 
| 96 GB or more | IQ3_S, or Unsloth's 4-bit (experimental) | room for the largest sizes with everything else open | 
- Coder - a coding version with half of the experts removed: 91% of the full model's SWE-bench Verified score (by its authors), fits 32 GB of RAM. Weaker outside coding.
- Swift 1.5 - a fine-tune that thinks much shorter before it answers, so you get the answer sooner, at about the same quality.
- Unsloth UD-Q4_K_XL (experimental) - the closest to the full model, but most of it is read from the SSD while it answers: 7-8.5 tokens/s on a 64 GB PC.
- OrcaRouter's Uncensored IQ3_XXS - a manual setup, not in the installer's menu.
Sizes, downloads and what fits where: docs/MODELS.md. You can add another model later with
SETUP.bat (Linux: ./setup.sh --setup).
The Strata app's Monitor (left) while a coding agent writes the pagoda garden from the video (right)
- In the browser: http://127.0.0.1:8080- Chat, a live Monitor of the model and your GPU/CPU/RAM, and About with the settings and addresses.
- Your apps and coding agents: add an "OpenAI-compatible" provider with base URL http://127.0.0.1:8080/v1, any API key and any model name. Apps that use Anthropic's API:http://127.0.0.1:8080/v1/messages(Claude Code:ANTHROPIC_BASE_URL=http://127.0.0.1:8080).
- Thinking: choose off, low, medium or high in the chat menu or your app's "reasoning effort". Off is fastest; high is best for hard questions.
- Pictures: say yes to "Images?" in setup, then click Picture in the chat, or attach them in your app (AMD cards: on Linux through the processor, not on Windows yet).
- From your phone or another PC: START-HERE.bat --setup --host 0.0.0.0 --api-key <secret>- always with a key.
- Good to know: it answers one request at a time. The first message of a chat is read in full (about 1 minute per 30,000 tokens); follow-ups start in seconds.
More: where your chats are stored, the API.
- My PC froze the first time Strata started. Normal while it loads the model: wait, don't close the window. Still frozen after 10 minutes? Restart the PC, close other programs and try again, or pick a smaller size.
- It stopped while downloading or installing. Run START-HERE.bat(or./setup.sh) again: it continues where it stopped.
- It's very slow and the disk light keeps blinking, or "the engine stopped unexpectedly". Not enough free RAM: close other programs (browsers use a lot), or pick a smaller size (Q2_0 or IQ2_XS).
- It says port 8080 is already in use. Strata is already running - look for its window.
More problems and their fixes: docs/TROUBLESHOOTING.md. Still stuck? Open an
issue and attach strata-<model>.log from the Strata folder.
Models like this one normally run on servers with hundreds of gigabytes of graphics memory. Your graphics card has 12-24 GB. Strata makes it fit by sharing the work across your whole PC - like a kitchen, where the things you use all the time stay on the counter and the rest waits in the pantry.
- The model is a team of 24,576 small specialists ("experts"), and each word needs only 10 of them.
- Your graphics card keeps the few thousand experts that are asked most often; your RAM holds all of them, and your processor works on the rest at the same time. Your SSD holds a big lookup table.
- Guess, then check: a small helper guesses the next few words and the big model checks them all at once, so you get the same answer, 1.6-1.8x sooner.
- Long texts are read in big pieces (up to 8,192 tokens at a time): over 1,000 tokens per second.
The longer explanation: docs/HOW_IT_WORKS.md. Every part and its numbers: the details and the paper.
The model is Qwen3.8-Flash-Next by the Qwen team, compressed by ISTA-DASLab, UkisAI (Swift 1.5) and Unsloth; Strata is built with parts of llama.cpp / ggml. All credits: docs/HOW_IT_WORKS.md. Strata is open source under the MIT License; a few parts and every model carry their own licenses (which ones).
Strata is free and open source. If it is useful to you, you can support its development:
