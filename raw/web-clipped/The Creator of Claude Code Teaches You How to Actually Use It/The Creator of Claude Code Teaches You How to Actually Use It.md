---
title: "\"The Creator of Claude Code Teaches You How to Actually Use It\""
source: "https://www.youtube.com/watch?v=jsoKH4Pvld0"
author:
  - "[[JawcoAI]]"
published: 2026-06-04
created: 2026-09-28
description: "The person who actually invented Claude Code, Boris Cherny, walks through how he uses the tool he built at Anthropic. If you've been guessing at the \"right\" way to use Claude Code, this is it from the"
tags:
  - "clippings"
url: "\"https://www.youtube.com/watch?v=jsoKH4Pvld0\""
fetched: " 2026-09-28T14:08:51+05:00"
---
![](https://www.youtube.com/watch?v=jsoKH4Pvld0)

The person who actually invented Claude Code, Boris Cherny, walks through how he uses the tool he built at Anthropic. If you've been guessing at the "right" way to use Claude Code, this is it from the source.  
  
Workshop featuring Boris Cherny, creator & head of Claude Code at Anthropic.  
  
#ClaudeCode #Anthropic #AItools #AIcoding #ClaudeAI

## Transcript

**0:01** · Hello.

**0:04** · Everyone, I'm Boris. I'm a member of technical staff here at Anthropic and I created Quad Code.

**0:10** · And here to talk to you a little bit about some practical tips and tricks for using Quad Code.

**0:16** · Um it's going to be very practical. I'm not going to go too much into the history or the theory or anything like this.

**0:22** · Uh and yeah, before we start actually, can we get a quick show of hands who has used Quad Code before?

**0:29** · Yeah. All right, that's what we like to see.

**0:31** · For everyone that didn't raise your hands, I know you're not supposed to do this while people are talking, but if you can open your laptop and type this.

**0:43** · And this will help you install Quad Code just so you can follow along for the rest of the talk.

**0:52** · All you need is Node.js. If If you have it, this should work.

**1:01** · Yeah, if you Well, you don't have to You don't have to follow along, but if you don't have it yet, yeah, this is your chance to install it so you can follow along.

**1:11** · So, what is Quad Code? Quad Code is a new kind of AI assistant and there's been different generations of AI assistants for coding. Most of them have been about completing, you know, like a line at a time, completing a few lines of code at a time.

**1:25** · Quad Code is not for that. It's fully agentic. So, it's meant for building features, for writing entire functions, entire files, fixing entire bugs at at the same time.

**1:38** · And what's kind of cool about Quad Code is it works with all of your tools and you don't have to change out your workflow. You don't have to swap everything to start using it. So, whatever IDE you use, if you use VS Code or if you use Xcode or if you use JetBrains IDEs, there's some people at Anthropic that you can't pry them from their cold, dead hands, but they use Quad Code.

**1:59** · Because Quad Code works with every single IDE, every terminal out there.

**2:03** · It'll work locally, over remote SSH, over tmux, whatever environment you're in, you can run it.

**2:12** · It's general purpose, and this is something where if you haven't used these kind of free-form coding assistance in the in the past, it can be kind of hard to figure out how to get started cuz you open it up and you just see a prompt bar, and you might wonder like, "What do I What do I do with this?

**2:25** · What do I type in?"

**2:27** · It's a power tool, so you can use it for a lot of things, but also because it can do so much, we don't try to guide you towards a particular workflow. Because really, you should be able to use it however you want as an engineer.

**2:42** · As you open up Quad Code for the first time, there's a few things that we recommend doing to get your environment set up. And these are pretty straightforward. So, run terminal setup.

**2:50** · This will give you shift enter for new lines, so you don't have to do like backslashes to enter new lines. This is, you know, it it makes it a little bit nicer to use.

**2:58** · Do /theme to set light mode or dark mode or daltonize themes.

**3:04** · Um you can do /install GitHub app. So, today when we announced the GitHub app, where you can @mention uh Quad on any GitHub issue or pull request. So, to install it, just run this command in in your terminal.

**3:18** · Um you can customize the set of allowed tools that you can use, so you're not prompted for it every time. This is pretty convenient. Um for stuff that I'm prompted about a bunch, I'll definitely customize it in this way, so I don't have to accept it every time.

**3:29** · And something that I actually do is for a lot of my prompts, I won't hand type them into Quad Code.

**3:35** · If you're on macOS, you can go into your system settings under accessibility's dictation, and you can enable it. And so, something I do is you just hit like that dictation key twice, and you can just speak your prompt.

**3:47** · And it helps a lot to have specific prompts. So, this is actually pretty awesome. You can just talk to Quad Code and uh like you would another engineer, and you don't have to type a lot of code.

**3:59** · So, when you're starting out with Claude Code, it's so free form and it can do everything, what do you start with? The thing I recommend above everything else is starting with code base Q&amp;A. So, just asking your question asking questions to your code base.

**4:12** · This is something that we teach new hires at Anthropic. So, on the first day in technical onboarding, you learn about Claude Code, you download it, you get it set up, and then you immediately start asking questions about the code base.

**4:23** · And in the past when you're doing technical onboarding, it's something that taxes the team a lot, right? You have to ask other engineers on the team questions.

**4:31** · You have to look around the code and this takes a while. You have to figure out how to use the tools. This This takes a long time.

**4:37** · With Claude Code, you can just ask Claude Code, and it'll explore the code base, it'll answer these kind of questions. And so, at Anthropic, onboarding used to take about two or three weeks for technical hires, it's now about two or three days.

**4:51** · What's also kind of cool about Q&amp;A is we uh we don't do any sort of indexing. So, there's no remote database with your code. We don't upload it anywhere. Your code stays local. We do not train generative models on the code.

**5:02** · So, it's there, you control it. There's no indices or anything like this.

**5:06** · And what that means is also there's no setup. So, you start Claude, you download it, you start it, there's no indexing. You don't have to wait, you can just use it right away.

**5:16** · This is a technical talk. So, um I'm going to show some very specific prompts and very specific code samples that you can and up level your Claude Code experience.

**5:25** · So, some kind of questions that you can ask is uh you know, like how is this particular piece of code used? Or how do I instantiate this thing? And Claude Code, it won't just do like a text search and try to answer this. It'll often go a level deeper, and it'll try to find examples of how is this class instantiated? How is it used?

**5:41** · And it'll give you a much deeper answer to something that you would get out of a week your documentation instead of just like command F.

**5:49** · Something that I do a lot also is ask it about Git history.

**5:52** · So, for example, you know, why does this function have 15 arguments? And why are the arguments named this weird way?

**5:59** · And this is something I bet in all of our code bases, you have some function like this or some class like this.

**6:04** · And Cloud Code can look through Git history. And it'll look to figure out how did these arguments get introduced and who introduced them and what was the situation? What are the issues that those commits link to? And it'll look through all this and summarize it. And you don't have to tell it that in all these in all this detail. You just ask it. So, just say look through Git history and it'll know to do this.

**6:23** · The reason it knows it, by the way, is not because we prompted it to. There's nothing in the system prompt about looking through Git history. It knows it because the model is awesome. And if you tell it to use Git, it'll know how to use Git.

**6:34** · So, we're lucky to be building on such a good model.

**6:38** · I often ask about uh GitHub issues. So, um you know, I can use web fetch and I can fetch issues and look up context on issues, too. And this is pretty awesome.

**6:48** · Uh and this is something that I do every single Monday in our weekly stand-up is I ask what did I ship this week? And Cloud Code looks at the log. It knows my username and it'll just give me a nice read-out of everything I I shipped. And I'll just copy and paste that into a doc somewhere.

**7:06** · So, yeah, that's tip number one. For people that have not used Cloud Code before, if you're just showing it to someone for the first time, onboarding your team, the thing we definitely recommend is start with code base Q&amp;A.

**7:15** · Don't start by using fancy tools. Don't start by editing code. Just start by asking questions about the code base.

**7:20** · And that'll teach people how to prompt.

**7:22** · And it'll start teaching them this boundary of like what can Cloud Code do?

**7:25** · What is it capable of versus what do you need to hold its hand with a little bit more? What can be one-shotted? What can be two-shotted, three-shotted? What do you need to use interactive mode for in a repple?

**7:38** · Once you're pretty comfortable with Q&amp;A, you can dive into editing code.

**7:41** · This is the next thing.

**7:43** · And the cool thing about uh any sort of agentic you know, like using a lemon a agentic way is you give it tools and it is just like magical. It figures out how to use the tools.

**7:53** · And with quad code we give it a pretty small set of tools. It's not a lot.

**7:57** · And so it has a tool to edit files. It has a tool to run bash commands. It has a tool to search files. And it'll string these together to explore the code, brainstorm, and then finally make edits.

**8:09** · And you don't have to prompt it specifically to use this tool and this tool and this tool. You just say, you know, do this thing and it'll figure out how to do it. It'll string it together in the right way that makes sense for quad code.

**8:22** · There's a lot of ways to use this.

**8:23** · Something I like to do sometimes is before having quad jump in to write code, I'll ask it to brainstorm a little bit or make a plan.

**8:32** · This is something we highly recommend and something I see sometimes is people, you know, they take quad code and they ask it, "Hey, implement this enormous like 3,000 line feature." And sometimes it gets this right on the first shot.

**8:44** · But sometimes what happens is the thing that it builds is not at all the thing that you wanted.

**8:49** · And the easiest way to get the result you want is ask it to think first. So, brainstorm ideas, make a plan, run it by me, ask for approval before you write code.

**8:58** · And you don't have to use plan mode. You don't have to use any special tools to do this. All you have to do is ask quad and it'll know to do this. So, just say, "Before you write code, make a plan."

**9:07** · That's it.

**9:10** · This is also I want to think with this one this commit push PR. This is a really common incantation that I use.

**9:15** · There's nothing special about it, but quad is kind of smart enough to interpret this. So, it'll make a commit, it'll push it to the branch, make a branch, and then make a pull request for me on GitHub. You don't have to explain anything. It'll look through the code, it'll look through the history. It'll look through the git log by itself to figure out the commit format and all the stuff. And it'll make the commit and push it the right way.

**9:33** · Again, we're not system prompting it to do this. It just knows how to do this.

**9:37** · The model was good.

**9:41** · As you get a little bit more advanced, you're going to want to start to plug in your team's tools. And this is where Quad Code starts to really shine.

**9:48** · And there's generally two kinds of tools. So, one is bash tools. And an example of this I just made up this like Barley CLI. This isn't a real thing.

**9:56** · Um but you can say use the CLI to do something. And you can tell Quad Code about this. And you can tell it to use, for example, like {dash} {dash} help to figure out how to use it. And this is efficient.

**10:06** · If you find yourself using it a lot, you can also dump this into your quad.md, which we'll talk about in a bit. So, Quad can remember this across sessions.

**10:12** · But this is a common pattern we follow at Anthropic. And we see external customers use, too.

**10:18** · And same thing with MCP. Um Quad Code can use bash tools. It can use MCP tools. So, you know, just tell it about the tools. And you can add MCP tool, and you can tell it how to use it, and it'll it'll just start using it.

**10:30** · And this is extremely powerful cuz when you start to use code on a new code base, you can just give it all of your tools, all the tools your team already uses for this code base, and Quad Code can use it on your behalf.

**10:47** · There's a few common workflows.

**10:50** · And this is the one that I talked about already. So, kind of do a little bit of exploration, do a little bit of planning, and ask ask me for confirmation before you start to write code.

**10:59** · These other two on the right are extremely powerful.

**11:02** · When Quad has some way to check its work, so for example, by writing unit tests or screenshotting in Puppeteer or screenshotting the iOS simulator, then it can iterate.

**11:13** · And this is incredible because if you give it, for example, a mock and you say build this web UI, it'll get it pretty good.

**11:19** · But if you let it iterate two or three times, often it gets it almost perfect.

**11:23** · So, the trick is give it some sort of tool that it can use for feedback to check its work. And then based on that, it will iterate by itself, and you're going to get a much better result.

**11:32** · So, for whatever your domain is, if it's unit test or integration test or screenshots for apps or web or anything, just give it a way to see its result, and it'll iterate and get better.

**11:46** · So, these are the next steps. Teach Claude how to use your tools and figure out the right workflow. Um if you want Claude to jump in a code, if you want it to brainstorm a little bit, make a plan, if you want it to iterate, kind of have some sense of that. So, you know how to prompt Claude to do what you want.

**12:03** · As you go deeper, beyond tools, you want to start to give Claude more context.

**12:07** · And the more context, the smarter the decisions will be because as an engineer working in a code base, you have a ton of context in your head about your systems and all the history and and everything else. So, you can there's different ways to give this to Claude.

**12:19** · And as you give Claude more context, it will do better.

**12:22** · There's different ways to do this. The simplest one is what we call Claude.md.

**12:27** · And Claude.md is the special file name.

**12:30** · The simplest place to put it is in the project root. So, the same directory you start Claude in, put a Claude.md in there. And that'll get automatically read into context at the start of every session. And essentially, the first user turn will include the Claude.md.

**12:45** · You can also have a local Claude.md. And uh this one you don't usually check into source control. So, Claude.md you should check into source control, share with your team so that you can write it once and share it with your team.

**12:57** · This one you don't check in. It's just for you.

**13:00** · The kinds of things you put in Claude.md, it's like common bash commands, common MCP tools, uh architectural decisions, important files, anything that you would kind of typically need to know in order to work in this code base.

**13:12** · Try to keep it pretty short cuz if it gets too long, it's just going to use up a bunch of context, and it's usually not that useful. So, just try to keep it as short as you can.

**13:20** · And for for example, in our code base, we have uh common bash commands, we have a style guide, we have a few core files, kind of things like that.

**13:29** · Other other quad MDs, you can put them in other nested child directories, and quad will pull them in on demand.

**13:36** · So, these are the quad MDs that will get pulled in automatically.

**13:39** · But then also, you can put in put quad MDs in nested directories, and those will get put those will get automatically pulled when quad works in those directories.

**13:48** · And of course, if you're you know, a company, maybe you want a quad MD that's shared across all the different code bases, and you want to manage it on behalf of your users, and you can put it in your enterprise root, and that'll get pulled in automatically.

**14:03** · There's a ton of ways to pull in context. I actually had a lot of trouble putting this slide together just to communicate the breadth of ways you can do this.

**14:10** · But quad MD is pulled in automatically.

**14:12** · You can also use slash commands. So, this is dot quad slash commands, and this can be in your home directory, or it can be checked into your project. And this is for slash commands.

**14:21** · And over here, we have a few examples of the slash commands that we have in quad code itself.

**14:29** · And so, for example, if you're in the quad code repo, and you see issues getting labeled, that's actually this workflow running here. It's label GitHub issues.

**14:37** · And we have a GitHub action running, the same one we talked about this morning, where quad code will run this command, and it's just a slash command. It'll run, and it'll label the issues so humans don't have to. It just saves us a bunch of time.

**14:50** · And of course, you can add mention files to pull them into context.

**14:53** · And like I said before, quad MDs in a nested directory get pulled in when quad works in that directory.

**15:03** · So, give quad more context, and it's definitely worth taking the time to tune context. You can run it through a prompt improver, consider who the context is for, if you want to pull it in every time, if you want to pull it in on demand, if you want to share it with a team, if it's a personal preference.

**15:18** · Definitely take the time to tune it.

**15:19** · This will improve performance dramatically Uh, if you do it right.

**15:27** · As you get more advanced, you're going to want to think about this a little bit more of this kind of hierarchy of different ways to pull in everything. So, like not just Quad MD, but also config and uh kind of everything about Quad you can pull in in this hierarchical way.

**15:42** · So, projects uh are specific to your Git repo, and this you can check in or you can make it just for you.

**15:48** · You can also have global configs that are for across all your projects, or you can have enterprise policies. And this is essentially a global config that you roll out for all of your employees, everyone on your team automatically.

**16:00** · And this slide is like pretty information dense, but the point is this applies to a lot of stuff. So, you can do this for slash commands, you can do it for permissions. So, for example, if you have a bash command that you would run for all your employees, uh like all your employees use this like test command for example, you can actually just check it into this enterprise policies file, and then any employee when they run this command, it will be auto-approved, which is pretty convenient.

**16:23** · And you can also use this to block commands. So, for example, let's say there's a URL that should never be fetched, um just add it to this config, and that'll make it so an employee cannot override it, and that that URL can never be fetched.

**16:35** · So, pretty convenient both to unblock people and also just to keep your code base safe.

**16:40** · And then same thing for MCP servers.

**16:42** · Have a MCP JSON file, check it into the code base, that way anytime someone runs Quad code in your code base, they'll be prompted to install the MCP servers, and share it with the team.

**16:55** · If you're not sure which of these to use, this is like a kind of an insane matrix cuz we support a lot of stuff, and engineer workflows are very flexible, and every company is different, so we kind of want to support everything. So, if you're not sure how to get started, I would recommend start with shared project context.

**17:09** · You write this once, and then you share it with everyone on the team, and you get this kind of network effect where, you know, someone does a little bit of work, and everyone on the team benefits.

**17:20** · There's a lot of tools built into Quad to manage this. Uh so, as an example, if you run {slash} memory, you can see all the different memory files that are getting pulled in. So, maybe I have an enterprise policy, I have my user memory, I have project Quad MD, and then maybe there's a nested Quad MD. That's only pulled in for certain directories.

**17:39** · And then, similarly, when you do {slash} memory, you can edit particular memory files. When you type pound sign to remember something, you can pick which memory you want it to go to.

**17:51** · So, yeah, that's the next tip. Take the time to configure Quad MD, MCP servers, all the stuff that your team uses so that you can use it once, configure it once, and then share it with everyone.

**18:04** · Um an example of this is uh in our apps repo uh for Anthropic. This is like the repo that we have all of our web and apps code in. There's a Puppeteer MCP server, and then we share this with the team.

**18:16** · Um and there's an MCP JSON checked in.

**18:18** · So, any engineer working in that repo can use Puppeteer in order to pilot end-to-end tests and to screenshot automatically and iterate so that every engineer doesn't have to install it themselves.

**18:31** · This is a talk about pro tips, so I I just want to take a quick interlude to talk about some common key bindings that people may not know. It's a It's very hard to build for terminal. It's also very fun. It feels like rediscovering this new design language. But, something about terminals is is It's extremely minimal. And so, sometimes it's hard to discover these key bindings. Um here's just a quick reference sheet. So, anytime, you can hit shift tab to accept edits.

**18:55** · Uh and this switches you into auto accept edits mode. So, bash commands still need approval, but edits are auto accepted. And you can always ask Quad to undo them later.

**19:03** · Um for example, I'll do this if I know Quad's on the right track or if it's writing unit tests and iterating on tests. I'll usually just switch into auto accept mode so I don't have to okay every single edit.

**19:14** · Anytime you want Claude to remember something, so for example, if it's not using a tool correctly and you want it to use it correctly from then on, just type the pound sign and then tell it what to remember and it'll remember it.

**19:24** · It'll incorporate it into Claude MD automatically.

**19:27** · If you ever want to drop down to bash mode, so just run a bash command, you can hit the exclamation mark and type in your command. That'll run locally, but that also goes into the context window.

**19:36** · So, Claude will see it on the next turn.

**19:39** · Um and this is pretty good for long-running commands if you know exactly what you want to do or any command that you want to get into context. And Claude will see the command and the output.

**19:48** · You can at mention files and folders uh anytime. You can hit escape to stop what Claude is doing. Um no matter what Claude is doing, you can always safely hit escape. It's not going to corrupt the session. It's not going to mess anything up.

**19:59** · So, maybe Claude is doing a file edit.

**20:01** · I'll hit escape. I'll tell it what to do differently. Or maybe it suggested a 20-line edit and I'm like, "Actually, 19 of these lines look perfect, but one line you should change." I'll hit escape. I'll tell it that and then I'll tell it to redo that edit.

**20:14** · Uh you can hit escape twice to jump back in history.

**20:17** · Um and then after you're done with the session, you can start Claude with a resume to resume that session if you want. Um or {dash} {dash} continue.

**20:25** · And then anytime if you want to see more output, hit control R and that'll show you the entire output, the same thing that Claude sees in its context window.

**20:39** · The next thing I want to talk about is the Claude Code SDK. So, we talked about this at the top. Uh right after this, Sid is doing a session, I think just across the hallway, and he's going to go super deep on the SDK. If you hadn't played around with this, if you use the {dash} P flag in Claude, this is what the SDK is. And we've been adding a bunch of features over the last few weeks to make it even even better.

**21:00** · Um so, yeah, you can you can build on top of this. You can do cool stuff. This is exactly the thing that Claude Code uses. It's exactly the same SDK.

**21:08** · And so, for example, something you can do is Claude P. So, this is the the CLI SDK. You can pass a You can pass a prompt.

**21:15** · You can pass some allowed tools, which could include specific bash commands.

**21:19** · And you can tell it which format you want. So, you might want JSON, or you might want streaming JSON, if you want to process this somehow.

**21:26** · So, this is awesome for for building on.

**21:28** · We use this in CI all the time. We use this for incident response. We use this in all sorts of pipelines. So, really convenient. Just think of it as like a Unix utility. You give it a prompt, it gives you JSON. You can use this in any way. You can pipe into it, you can pipe out of it.

**21:45** · The piping is also pretty cool. So, you can use like, for example, get status and pipe this in, and you know, use JQ to select the result. It The combinations are endless, and it's sort of this new idea. It's like a super intelligent Unix utility. And I think we barely scratched the surface of how to use this. We're just figuring this out.

**22:04** · You can read from like a GCP bucket, read, you know, like a giant log, and pipe it in, and tell Claude to figure out what's interesting about this log.

**22:11** · Um you can fetch data from like the Sentry uh CLI. You can also pipe it in, and have Claude do something with it.

**22:23** · The final thing, and this is probably like the most advanced use cases we see.

**22:27** · I'm sort of a Claude normie. So, I'll have usually like one Claude running at a time, and maybe I'll have like a few terminal tabs for a few different repos running at a time. When I look at power users in and out of Anthropic, almost always they're going to have like SSH sessions. They'll have uh like tmux tunnels into their Claude sessions.

**22:44** · They're going to have a bunch of checkouts of the same repo, so that they can run a bunch of Clauds in parallel in that repo. Or they're using Git worktrees to have some kind of isolation as they do this.

**22:54** · And we're actively working on making this easier to use, but uh for now, like, these these are some ideas for how to do more work in parallel with Cloud you can run as many sessions as you want and there's a lot that you can get done in parallel.

**23:10** · So yeah, that's it. I wanted to also leave some time for Q&amp;A.

**23:14** · So I think this is the last slide that I have and yeah, if folks have questions there's mics on both sides.

**23:21** · And yeah, would love to answer any questions.

**23:25** · \[applause\] Skip the bind command.

**23:38** · \[laughter\] I did.

**23:40** · Which bind?

**23:46** · Hey Boris, thanks for building a cloud code and I was wondering what was the hardest implementation like part of the implementation for you of building it.

**23:56** · I think there's a lot of tricky parts. I think one part that is especially tricky is the things that we do to make bash commands safe. Bash is inherently pretty dangerous and it can change system state in unexpected ways but at the same time if you have to manually approve every single bash command it's super annoying as an engineer and you can't really be productive cuz you're just constantly approving every command.

**24:22** · And just kind of navigating how to do this safely in a way that that scales across the different kinds of code bases people have cuz not everyone runs their code in a docker container.

**24:31** · Um was was pretty tricky and essentially the thing we landed on is there's some commands that are read-only. There's some static analysis that we do in order to figure out which commands can be combined in safe ways and then we have this pretty complex tiered permission system so that you can allow list and block list commands at different levels.

**24:50** · Hi Boris.

**24:51** · You mentioned giving an image to cloud code which made me wonder if there's some sort of multimodal functionality that I'm not aware of. Is that Are you just pointing it at an image on the file system or something?

**25:02** · Yeah, so Claude code is fully multimodal. Um it has been from the start. It's in a terminal, so it's a little uh hard to discover. Uh but yeah, you can take a image and just drag and drop it in. That'll work. Uh you can give it a file path. That'll work. Um you can copy and paste the image in and that works, too.

**25:20** · Um so I'll use this pretty often for if I have like a mock of something, I'll just drag and drop drop in the mock. I'll tell it to implement it. I'll give it a puppetier server so it can iterate against it. And yeah, it's just fully automated.

**25:33** · Um hey, uh why did you build a CLI tool instead of an IDE?

**25:40** · Yeah, it's a it's a good question. I think there's probably two reasons. One is uh we started this at Anthropic and at Anthropic people use a broad range of IDEs. And some people use VS Code, other people use Zed or Xcode or Vim or Emacs. And it was just hard to build something that works for everyone. And so terminal was just a common denominator.

**26:00** · The second thing is at Anthropic, we're uh we see up close how fast the model is getting better. And so I think there's a good chance that by the end of the year people aren't using IDEs anymore.

**26:13** · And so we want to get ready for this future and we want to avoid over-investing in UI and other layers on top given that the the way the models are progressing, it just it may not be useful work pretty soon.

**26:28** · Yeah.

**26:29** · How much have you I don't know if this is Is this on?

**26:32** · How much have you used Claude Code for machine learning modeling? And almost that auto ML experience. I was curious what the experience has been so far with that.

**26:41** · Yeah, I think I think the question was how much are we using Claude Code for machine learning and and modeling. We actually use it for this a bunch, so both engineers and researchers at Anthropic use Claude Code every day. Um, I think about 80% of people at Anthropic that are technical use Claude code every day.

**26:59** · And hopefully you can see that in the product and kind of the amount of love and dog fooding we've put into it. Um, but this includes researchers who use tools like the notebook notebook tool to edit and run notebooks.

**27:09** · Okay, very cool. Thank you.

**27:13** · All right, I think that's it. \[applause\] Thanks.

**27:27** · \[music\]