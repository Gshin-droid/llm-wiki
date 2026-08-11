---
title: "\"I Connected Claude AI to FreeCAD (And It Models Parts Like an Engineer)\""
source: "https://www.youtube.com/watch?v=6trAkQY5_kc"
author:
  - "[[Make Form]]"
published: 2026-07-16
created: 2026-08-11
description: "#ClaudeFable5 #FreeCAD #MCPClaude AI can now connect to FreeCAD — and in this FreeCAD tutorial, I show the complete FreeCAD MCP setup, step by step. By the end, you'll be doing AI CAD modeling in Fre"
tags:
  - "clippings"
url: "\"https://www.youtube.com/watch?v=6trAkQY5_kc\""
fetched: " 2026-08-11T17:08:16+05:00"
---
![](https://www.youtube.com/watch?v=6trAkQY5_kc)

#ClaudeFable5 #FreeCAD #MCP  
Claude AI can now connect to FreeCAD — and in this FreeCAD tutorial, I show the complete FreeCAD MCP setup, step by step. By the end, you'll be doing AI CAD modeling in FreeCAD just by typing prompts: boxes, fillets, holes, parts from hand-drawn sketches, and even a mathematically generated spur gear, all ready for 3D printing. This is one of the most practical Claude Fable 5 use cases — text to CAD, from install to finished part.  
  
📄 FREE PDF GUIDE (all commands & links): https://drive.google.com/file/d/1qVr3dZtDLR1JPSYMC19enji19svGK8fk/view?usp=sharing  
  
⏱️ TIMESTAMPS  
00:00 Intro – How Claude + FreeCAD Connector Works  
01:25 Step 1: Installing Claude Desktop  
01:55 Step 2: Installing FreeCAD  
02:50 Step 3: Installing UVX  
05:02 Step 4: Installing the FreeCAD MCP Server  
08:01 Configuring Claude Desktop to Connect to MCP  
11:09 Starting the RPC Server & Connecting Claude  
12:16 Testing the Connector: Creating a Test Part & Box  
13:44 Adding a Fillet (Handling Ambiguous Prompts)  
14:33 Adding Holes (Claude Reasons Through Placement)  
15:49 Building a Part from a Hand-Drawn Sketch  
17:10 Designing a Flange with Full Parameters  
17:53 Important Tip: Save Your Work Before Closing  
18:49 Building a Spur Gear from Scratch (No Gears Workbench)  
19:38 Outro & What's Coming Next  
  
🔗 LINKS  
FreeCAD: https://www.freecad.org  
FreeCAD MCP (by neka-nat): https://github.com/neka-nat/freecad-mcp  
Claude Desktop: https://claude.ai/download  
UV installation: https://docs.astral.sh/uv/getting-started/installation  
  
▶️ Previous video — What the FreeCAD connector can do: \[link\]  
  
In this CAD tutorial you'll learn the full Claude MCP setup: installing the FreeCAD MCP server, connecting it to Claude Desktop with UVX, editing the Claude config file, and using AI 3D modeling to build parametric parts with plain-language prompts — perfect for 3D printing, makers, engineers, product design, and anyone learning CAD in 2026.

## Transcript

### Введение – Как работает коннектор Claude + FreeCAD

**0:02** · In this video, we'll go in detail into how to download and set up the FreeCAD connector for Claude and then put it to work modeling some real parts. Claude can now connect to FreeCAD opening up infinite possibilities for engineers, hobbyists, makers, and CAD designers alike. If you haven't seen it yet, we covered what this connector can actually do in our previous video. So, before we dive in, let's quickly look at how this actually works.

**0:25** · When you give a prompt, Claude analyzes it and reasons through what needs to be done.

**0:30** · It then connects to FreeCAD through the MCP connector and executes the corresponding FreeCAD code through the Python API to create the part. FreeCAD sends feedback back a screenshot of the viewport again through the MCP connector.

**0:45** · Claude analyzes that result and based on what it sees, sends the next command.

**0:51** · This loop keeps repeating, which is what lets Claude build up a part step-by-step. This video consists of five simple steps and we'll go into detail on each one, so you can install everything successfully. It's really easy to follow, just stick with me.

**1:06** · Before we jump in, I've attached a free PDF in the description. You can follow along step-by-step. It has all the clear instructions, exact command lines, and direct links you'll need, so you don't have to pause and search for anything yourself. Keep it open alongside this video as we go. Step one, installing Claude desktop.

### Шаг 1: Установка Claude Desktop

**1:27** · First, head over to claude.ai and download the desktop app. The link is also in the attached PDF. I'm on Windows, so I'll click download for Windows, but if you're on a Mac, just choose that version instead. Once it's downloaded, open the installer.

**1:43** · It'll set itself up automatically.

**1:45** · When that's done, sign in to your Claude account.

**1:53** · And you're ready for the next step.

### Шаг 2: Установка FreeCAD

**1:55** · Step two, installing FreeCAD.

**1:57** · Now, let's install FreeCAD itself. Visit the official site freecad.org. The link's in the PDF as well. Click download. Then, choose the installer that matches your operating system. For me, that's the 64-bit Windows installer.

**2:14** · Run through the setup.

**2:19** · Finish, and FreeCAD is installed. At this point, both Clawd and FreeCAD are on your machine, but they can't talk to each other yet.

**2:28** · Now, if you open Clawd desktop and click on the plus button and navigate to connectors, you won't see a FreeCAD option.

**2:37** · And if you open FreeCAD's workbench drop-down, there's no MCP add-on, either.

**2:45** · Step three, installing UVX.

**2:49** · To install FreeCAD MCP, we first need a tool called UVX, a Python package manager and tool runner that lets you run Python CLI tools instantly without a full installation process. To install UVX on Windows, first open the start menu and search for PowerShell.

### Шаг 3: Установка UVX

**3:10** · Once it shows up, right-click it and select run as administrator, or just click run as administrator directly from the search results.

**3:21** · PowerShell will now open.

**3:24** · Next, open the attached PDF I mentioned earlier and scroll to the UVX installation section. Copy the command line shown there.

**3:33** · Switch back to PowerShell and make sure your current directory is set to Windows system32. This is usually the default when PowerShell opens as administrator.

**3:44** · If you'd prefer to grab the command straight from the source instead of the PDF, you can visit the official UV website. The link's provided as well. Go to their installation page, switch the platform to Windows, and copy the same command from there. Now, paste the command into PowerShell and press enter.

**4:03** · PowerShell will download and install UVX automatically.

**4:07** · And once it's done, you'll see a message confirming everything installed successfully.

**4:13** · To verify the installation, let's run a version check. But there's one important step first. Close PowerShell completely and reopen it. If you run the version check without restarting PowerShell, it'll return an error. So, open start, search PowerShell again, right-click it, and select run as administrator.

**4:32** · PowerShell opens fresh. Go back to the PDF and copy the version check command listed there. This checks which version of UVX is installed.

**4:42** · If everything installed correctly, it'll return a version number. Switch back to PowerShell, paste the command, and press enter. It should return the version number, confirming UVX is successfully installed.

**4:57** · With that done, we're ready to move on to the next step.

**5:01** · Step four, installing the FreeCAD MCP server.

### Шаг 4: Установка сервера FreeCAD MCP

**5:05** · Now, let's install the actual FreeCAD MCP server. Open the attached PDF again and click through to this page, github.com/necanat/freecad-mcp.

**5:20** · This repository is the FreeCAD MCP built by necanat. It's what allows Cloud Desktop to control FreeCAD directly.

**5:30** · On that page, click the green code button, then click download zip.

**5:43** · Once it's downloaded, extract the zip to a folder.

**5:55** · Open that extracted folder.

**6:02** · Then open the add-on folder inside it.

**6:05** · You'll find a folder named FreeCAD-MCP.

**6:09** · Copy that entire folder.

**6:13** · Now hold Windows key plus R to open the run dialog.

**6:20** · Type percent appdata percent into the field and click okay.

**6:29** · This opens your appdata roaming folder.

**6:36** · Inside there open the FreeCAD folder and then open the v1-1 folder inside it. If there's already a mod folder in here, open it.

**6:47** · If there isn't one create a new folder.

**6:54** · And name it exactly mod.

**7:01** · Then open it.

**7:03** · And paste it inside this mod folder.

**7:07** · One quick note. If you're using a FreeCAD version earlier than 1.1, the mod folder goes directly inside the main FreeCAD folder, not inside of subfolder.

**7:20** · With that done, open FreeCAD again.

**7:25** · And check the workbench drop down. You should now see the MCP add-on listed.

**7:32** · That confirms it installed correctly.

**7:34** · Select the MCP add-on workbench. You'll see a new toolbar appear with options like start RPC server, stop RPC server, and auto start server. Now, click start RPC server.

**7:47** · If Windows asks for network access permission, click allow.

**7:52** · FreeCAD and the MCP server are now successfully linked.

**7:56** · Next, we need to connect Claude to this MCP server.

### Настройка Claude Desktop для подключения к MCP

**8:01** · Open Claude desktop, which we installed earlier.

**8:04** · Once it's open, go to settings.

**8:07** · You can get there quickly with control plus comma.

**8:10** · The settings panel opens.

**8:12** · Now go to the developer tab. This opens the local MCP servers page.

**8:17** · If you've installed any MCP servers before, you'll see them listed here.

**8:21** · Click the edit config button.

**8:23** · This takes you directly to Claude's configuration file.

**8:27** · It's a dot JSON file located in Claude's application data folder.

**8:31** · Right click that file and select open with notepad.

**8:35** · The file opens.

**8:37** · Don't be intimidated by all the syntax you see.

**8:40** · We're not writing anything from scratch here.

**8:43** · Now, open the downloaded PDF.

**8:45** · You'll see two blocks of code inside it.

**8:49** · We're going to paste one of these configurations into the configuration file.

**8:53** · This tells Claude desktop to launch the FreeCAD MCP server using a tool called UVX, which handles the package automatically. Here's the difference between the two blocks.

**9:04** · The first block is the standard setup.

**9:06** · After Claude runs a command in FreeCAD, it gets back both the text result and an image, a screenshot of the FreeCAD viewport. This means Claude can actually see what it built and react to it visually.

**9:20** · It does consume more tokens per operation, though.

**9:25** · The second block adds a flag called only text feedback. With this, Claude skips the screenshot entirely and only receives text, object names, dimensions, success, or error messages.

**9:38** · No image, but significantly fewer tokens used per operation.

**9:43** · If you're doing short sessions, building just one or two parts, go with the first block.

**9:49** · If you're running longer sessions with a lot of back-to-back operations, the second one keeps things more efficient.

**9:55** · For most beginners, I'd recommend starting with the first.

**9:59** · You can always switch later by editing this one line.

**10:02** · I'm going with the first block.

**10:04** · In the configuration file, find the last but one closing curly brace.

**10:16** · Add a comma right after it. Press enter and paste the block of code in.

**10:24** · The important part to get right, add the comma, then press enter before the last closing curly brace.

**10:32** · If you get that placement wrong, the file won't load correctly.

**10:40** · Once that's done, save the text file and close Notepad.

**10:47** · Now, fully close Cloud Desktop.

**10:53** · Make sure to close it from the system tray as well, not just the window. If it's still running in the background, your configuration changes won't take effect. With the configuration saved and Cloud fully closed, we're ready to bring everything online.

**11:08** · Step six, starting the connection and testing it.

### Запуск RPC-сервера и подключение Claude

**11:11** · Let's start the connection and put it to the test.

**11:14** · First, start FreeCAD.

**11:16** · Go to the workbench drop-down, select the MCP add-on, and click start RPC server. And you can minimize FreeCAD now.

**11:27** · Now, open Cloud Desktop.

**11:32** · Click the plus icon.

**11:34** · Go to connectors and scroll down.

**11:37** · You'll see the FreeCAD connector listed and live.

**11:41** · If it's toggled off for any reason, turn it on.

**11:46** · There's another way to confirm everything's running correctly.

**11:50** · Go to settings, control plus comma, then developer.

**11:54** · Under local MCP servers, you'll see FreeCAD listed as added and running.

**12:03** · That's it. We've successfully connected FreeCAD to Claude.

**12:06** · From here, you can create almost anything in FreeCAD just by describing it in plain language.

**12:13** · Let's put it to the test.

### Тестирование коннектора: создание тестовой детали и коробки

**12:16** · Step seven, testing the connector.

**12:19** · To follow along easily, I've arranged both windows side by side, so we can watch what's happening in both live as we go.

**12:27** · Let's write our first prompt.

**12:29** · Create a new document in FreeCAD called test part.

**12:36** · The first time each tool runs, Claude will ask for permission to use it. I prefer clicking always allow.

**12:44** · FreeCAD creates the document and names it test part successfully.

**12:49** · Now, let's create a simple box.

**12:51** · I'll prompt, create a box in FreeCAD with length 50 mm, width 30 mm, height 20 mm.

**13:03** · It asks for permission again to create the object. I click always allow.

**13:14** · The box is created and the view automatically adjusts to isometric, so we can see it clearly.

**13:21** · Claude also gives us feedback in text.

**13:23** · The box was created inside test part with the given dimensions sitting at the origin.

**13:29** · It follows up on its own asking, "Want me to round the edges with a fillet or chamfer, hollow it out, drill a hole, or add another solid next?"

**13:40** · Fillets can be a bit troublesome in FreeCAD, so let's test that specifically. I'll prompt "Fillet all edges."

### Добавление скругления (обработка неоднозначных запросов)

**13:49** · deliberately without mentioning a radius, just to see how it handles the ambiguity.

**13:55** · Claude thinks for a moment, then asks, "What radius would you like for the fillet?"

**14:03** · It even offers a suggestion on its own.

**14:06** · It recommends keeping the radius under 10 mm to avoid geometry errors.

**14:10** · It gives me a few options to choose from, and I'll go with 2 mm.

**14:25** · After one more permission prompt, it applies the fillet cleanly across all 12 edges.

### Добавление отверстий (Клод объясняет процесс размещения)

**14:33** · Next, let's add some holes.

**14:35** · Again, I'll keep the prompt intentionally vague. "Make four holes on top."

**14:51** · Claude asks for the missing details, hole diameter, which I set to 4 mm, and depth, where I choose through all.

**15:13** · The holes are created, but here's the interesting part. I never told Claude where to place them.

**15:20** · It decided that entirely on its own.

**15:23** · 10 mm inset from the short edge and 8 mm from the long edge.

**15:29** · It explains that this positioning clears the fill it edges comfortably.

**15:33** · That's reasoning through the geometry like an actual CAD engineer would.

**15:37** · This entire design stays parametric.

**15:40** · Fill it radius, whole diameter, whole position, every bit of it can still be changed later just by prompting.

### Создание детали по эскизу, нарисованному от руки

**15:49** · Now, let's push this a level further.

**15:51** · Instead of typing out dimensions, we'll hand FreeCAD a rough hand-drawn sketch instead.

**15:58** · I'll upload a sketch of a simple three-step staircase style part.

**16:03** · Drawn from the front, top, and right side views with all the necessary dimensions marked on it. The prompt is intentionally rough, too. Create this part in FreeCAD.

**16:25** · And in just about 20 seconds, FreeCAD builds the entire part directly from that sketch.

**16:38** · Let's verify the accuracy.

**16:44** · To measure dimensions on the created part, go to tools, then select measure.

**16:49** · I'll measure the distance between these two faces.

**16:52** · It measures exactly 36.

**16:59** · I'll check a couple of the other dimensions, too.

**17:06** · And they all match perfectly.

### Проектирование фланца с полными параметрами

**17:10** · Let's try one more part. But this time, we'll give Claude every detail up front instead of leaving anything for it to decide.

**17:21** · Design a flange in FreeCAD with a base diameter of 100 mm, thickness 10 mm, and a center hole of 20 mm diameter with four bolt holes of 8 mm diameter equally spaced at 70 mm PCD.

**17:40** · Because every parameter is already specified, Claude builds the part in a single pass. No clarifying questions needed this time.

### Важный совет: сохраните свою работу перед закрытием

**17:53** · Here's something important to know before you get too deep into a session.

**17:57** · I enter the prompt, close all the documents.

**18:06** · Claude closes every open document, but without asking or warning first.

**18:13** · Only after they're all closed, does it add a note. One heads-up, if any of those had unsaved changes, that work was closed without saving.

**18:22** · Let me know if you need to recreate anything.

**18:25** · In other words, none of those documents were saved, and there was no warning before they were closed.

**18:30** · Claude can recreate the parts again if you ask, but that means redoing the work, and it costs additional tokens to regenerate.

**18:37** · So, when you're using the FreeCAD connector, make it a habit to save your documents manually or explicitly prompt Claude to save them before moving on or closing anything.

### Создание прямозубой шестерни с нуля (без Gears Workbench)

**18:49** · Let's try something that requires real mathematical and geometric calculation, a gear.

**18:55** · I don't have FreeCAD's gears workbench installed, so Claude can't just pull a ready-made gear template.

**19:01** · It has to build one from scratch. I prompt, design a spur gear in FreeCAD with 20 teeth, module two, face width 20 mm, and a center bore of 10 mm diameter.

**19:18** · Claude responds that since the gears workbench isn't available, it'll need to construct an involute spur gear manually using basic geometry instead.

**19:31** · After running through a series of calculations, it successfully builds the gear.

### Заключение и что будет дальше

**19:38** · And that's the full setup from installing Claude desktop and FreeCAD to linking them through the MCP server. If you followed along with the PDF, you should have this fully working on your own machine right now.

**19:50** · In the next video, we're going even further building a parametric Skadis pegboard from a hand-drawn drawing, a planter pot from an AI-generated image, and a fully parametric compartment organizer all through prompts alone.

**20:04** · If this helped you, hit subscribe so you don't miss it, and I'll see you in the next one.