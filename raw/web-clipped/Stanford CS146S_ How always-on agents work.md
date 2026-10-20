---
title: "\"Stanford CS146S: How always-on agents work\""
source: "https://www.youtube.com/watch?v=L1OBRtfPS34"
author:
  - "[[leerob]]"
published: 2026-10-11
created: 2026-10-20
description: "Learn more about the product, infrastructure, and harness details used to build Grok Bot, a new type of always-on and proactive agent."
tags:
  - "clippings"
url: "\"https://www.youtube.com/watch?v=L1OBRtfPS34\""
fetched: " 2026-10-20T09:17:55+05:00"
---
![](https://www.youtube.com/watch?v=L1OBRtfPS34)

Learn more about the product, infrastructure, and harness details used to build Grok Bot, a new type of always-on and proactive agent.

## Transcript

### Introduction to always-on agents

**0:00** · So, as mentioned, I'm Lee. We're going to talk a little bit today about how this new category of always-on, proactive, persistent agents work and kind of give you some of the understandings of the building blocks for how these are made. Um just as a, you know, fun statement up here, some of the things we'll talk about are in progress we're working on at SpaceX.

**0:20** · Um and in week one, you all built this very kind of simple harness that helps you understand the core idea, which is that you have a model, it can call tools in a loop, and that's actually very powerful. It unlocks a lot of new capabilities for the models.

**0:36** · Um but, it does come with some drawbacks. Notably, you close your laptop and the process stops. It's no longer running. Uh and I want to talk about how you can take this simple idea, it's very powerful for how to get more out of models, and extend it to this new type of agent, which is an always-on agent.

**0:53** · So, rather than just running in your terminal, this can run on server. It can run in the cloud. You can close your computer. Uh it can restart. It can survive crashes, for example.

**1:02** · This agent has its own computer. So, not just your laptop, but a Linux machine in the cloud where it has its own desktop, files, browser, and more. Maybe some 3D apps.

**1:13** · Um it can save files on the machine. It can understand more about your progress over time and build up a memory of how you work with it. Um unlike a harness in the terminal that is responding to every message that you send, this type of always-on agent is more like a colleague where it doesn't always immediately send you a message.

**1:34** · It knows when to be quiet. Sometimes it might just want to work in the background a little bit and only come back to you when there's an important update. Uh and it can be triggered more than just you typing. So, it's not just you prompting it in the terminal. Maybe there was a Slack message or an email or some other type of event that wakes up this agent to go do work. Um and ideally the hope with these type of always-on agents is that they can do work over very long periods of time, not just hours or days, but maybe even weeks or months.

**2:03** · And that just requires a little bit of a different architecture, which we'll get into.

**2:08** · So, we're going to go uh decently in depth on how we built this architecture, how we built the harness, um kind of what's got us here today, and where we're going in the future. And we'll get into some of the specifics of how we've engineered this system to be proactive, to be persistent, and to follow instructions very well. And of course, time at the end for questions if you all want to ask anything about this or uh anything outside of uh what we've covered today.

### The evolution of AI development

**2:35** · So, first, how we got here.

**2:39** · There's kind of been four eras of developers working with AI so far, I would say. The first one was uh copy-pasting code out of ChatGPT and putting it into your editor of choice, which feels like, you know, decades ago at this point, but it was really only a few years ago.

**2:55** · Uh and then, once the model started to get better at being able to have kind of that simplified harness we talked about uh in, you know, in the last uh lecture, uh they were able to edit files, run shell commands, kind of have this very simple interface for how you work with them in the terminal. And this really took off because all of a sudden, the model had this new capability where it could go do more proactive work for you and be more, you know, productive.

**3:22** · Then, this third era was taking the coding agents and where they were kind of simple to start and giving them these dedicated apps. And at this point, people were starting to run many agents in parallel. Maybe they're running them in the cloud, not just on their machine.

**3:37** · Uh but still, at this point, you were kind of the bottleneck in that you were reviewing every command that they were running. You wanted to make sure every shell command was just right. You're kind of really watching them and being in the loop on everything. And now, with improvements in models, in harnesses, and products, we're now in this new era where you're starting to have these always-on agents. And they can kind of run ambiently in the background where they have their own computer, they have their own memory, they learn new skills on the job, and they keep working after you go, you know, go to bed or go do other work.

**4:08** · A good example of this is we've kind of moved away from this world of prompting an agent every single day, although we still do that sometimes, but you can set up agents where it will kind of just run in the background. So, maybe in the the before times, it was you would prompt an agent, you would wait, prompt an agent, you would wait, and if it asked you to run a shell command, you'd have to approve or, you know, disallow that command. Uh and now, instead of kind of queuing commands, you can steer the agent. And you might say, "Hey, go check this thread." And then immediately after, "Oh, by the way, you know, actually go do that on Thursday."

**4:39** · And prior generations of models would get kind of confused when you would immediately interrupt it and give it some other command, but now they kind of understand, just like how you might ramble on talking to a friend and they can kind of parse that these two things are related. The models and the harnesses can now handle that. And if you say, "Hey, go send this email, go send this Slack message."

**4:59** · Um there are additional safety checks in place, which a lot of companies are calling auto review, which is essentially a separate AI model that's checking all of the commands that get run. So, you know, kind of funnily enough, that's actually more secure than the fatigue of having to watch hundreds of shell commands and approve each one.

**5:20** · We've kind of reached the point where if you did a blind test with what the AI model's checking on the commands and what a human's checking on the commands, most of the time the the model's actually doing a better job.

**5:30** · Um kind of paradoxically, but as the models have gotten better, the interface has gotten quite a bit more simple, actually. And this type of always-on agent we're calling a bot, but as you'll notice, there's actually quite a few of these new types of products popping up right now and gaining a lot of traction.

**5:50** · And I think the main reason is because we all know how to text, you know, everyone knows how to text, everyone is pretty proficient with using their phones, and we've kind of distilled down this way of working with AI that feels like you're just texting a friend, but it can actually go and do real work for you. It's not just answering questions in a Q&amp;A style setting anymore, it's actually going and doing longer tasks like you would hand off to a coworker, for example.

### Key capabilities of modern models

**6:14** · Um so, there's been a few changes specifically in the models that have enabled this to happen. Um I'll go over six, but there's, you know, quite a bit more. The first one is that the models just over the past year, 2 years, have really gotten better at being able to follow instructions over a longer period of time, where they don't get confused or make mistakes. And now models can pretty confidently run for hours or days with the right uh compression and compaction, which we'll talk about in a little bit. Two, models now can essentially hand off to helpers.

**6:45** · And those helpers are called sub agents. And the reason why a sub agent is helpful is the the model has kind of its working memory of the process that it's on, and that's going to fill up eventually. Uh so, it's nice if it can hand off to these helpers that have a fresh set of working memory, and that effectively can give it an unlimited context, basically, where it can go and do work that might be expensive in terms of the tokens it's using or the tools that it's calling, and then come back to the main agent and report its updates. And I'll have some diagrams of that later.

**7:18** · Um models now not only are just better at calling tools. I mean, just a few years ago they basically couldn't call tools very well, and they would hallucinate all the time. It's funny, you don't really hear people talk about hallucinations anymore, because it's kind of a solved problem, mostly. Um but not only can they call tools, but you can give them very powerful tools, the same way as if you onboarded somebody onto your team. So, obviously, running shell commands and files, but also you give them a full computer, a full Linux uh computer. You allow them to make demo videos and such.

**7:48** · They can click around on a screen just like a human would and they're getting increasingly better at doing that, otherwise known as computer use, which basically means that any SaaS product or any website that didn't expose an API or an MCP server can be used headlessly, basically. So, autonomously through computer use by these models and these bots. Um you can store all of the information in files, and the reason you can do that is because it's actually very easy for the models then to recall and search this information, which we'll talk about.

**8:17** · And then finally, you can just kind of show the bot how to do some work and it will kind of turn that into skills or memories or routines or things that it can reuse later.

**8:29** · So, on the file thing, for example, this is kind of a simplified example, but you might remember or you might imagine that when you're working with a bot, under the hood it might look something like this. You build up this profile or this understanding of the user, and that's going to be included in every single prompt. Maybe you like, you know, lowercase text-like messaging and every single message should have that. Also, as you're working with these bots over time, you're building up kind of like a working log, just like if you were working with a colleague and they were writing down notes every day of the work that they've done.

**9:01** · That's all being put into files that the model can then decide to search or use later. If you say, "Hey, what did I do last week?" It just can can go and look that up. And the models are very good at using Linux commands, running shell commands to go grep and search and look through these files.

**9:18** · Similarly, with skills, you are essentially taking your knowledge of how to do a specific task and encoding it into a markdown file, the very specific process you need to do, the things that you believe make that, you know, successful or unsuccessful.

**9:33** · And that's not just your skills, there's a whole ecosystem now of companies and developers writing these skills for how to send a great email or, you know, how to build a great API or many different things. And and for example, in Grokbot there is a whole system of plugins. So basically any tool that you want to use, there's a plugin you can install which uses skills or servers. And then also routines, which if you're familiar with cron jobs, you know, you're running some prompt basically on some kind of schedule, which is pretty useful as well. So basically everything is computer.

### Architecture of an always-on agent

**10:05** · Um part three. So let's go a little bit further into the kind of the mind of this always-on agent or going behind the scenes.

**10:13** · Um what does it mean for the agent to be always-on? You can kind of read this chart from left to right, but it starts out with the server being asleep and also this computer that the agent can use being asleep. And so whether you send it a message or some kind of trigger decides to make the agent start up, which we'll talk about in a second.

**10:35** · That's basically loading up and booting up all of the state for this agent and it's running on a server. If it decides that it needs to use a computer, maybe it wants to go use the computer's browser or, you know, go click around on the computer, it can start up the computer as well. And then once you're done using it, it also has the ability then to basically put those to sleep.

**10:53** · Why is this important? It would be, you know, expensive and also there's not enough computers in the world to just have those computers running all of the time for everyone as well as that's a lot of server usage, too. And so this state can then be persisted to, you know, a database, the the conversation logs, the memories, the routines, all of that.

**11:13** · How does the agent get woken up then?

**11:16** · Well, obviously you can prompt it directly, but I think what's increasingly interesting is having other things running in the background that can then decide when you want to go reach out to your bots. Maybe that is somebody pinging you on Slack and your bots can live in Slack. Maybe that's a phone call or a meeting that you put your bot in. It's increasingly common now at SpaceX where we see bots joining meetings for employees where they could make it to the meeting, but they want their bot to go and just take notes and come back to them, which is kind of funny.

**11:43** · Um maybe you had some routine or some background work that was taking, you know, hours or days to do and then you want to come back and give you a summary. That all happens and then we have basically a router that dedupes that and figures out how to put it into the conversation and then it's has this heuristic of do I need to bug the user about this or not? Because not everything is actually important. Just like if you have a a co-worker working on something, it would be pretty annoying if every single time they made progress on something, they came and bugged you like, "Hey, check it out.

**12:13** · Like I made progress on this thing." You really only need a status update maybe, I don't know, every day depending on the task.

**12:19** · Um so I talked about how the agent has this computer, this Linux box. Um this is running a Firecracker virtual machine and the reason this is really helpful is because it's it's very easy then to essentially snapshot the state of the machine and shut it down and start it back up. And on this machine, you of course have files, but you can kind of connect into the machine and have a live view of the machine and actually control it yourself if you want. Um the machine can of course run commands, which is great if you're going to run some shell commands.

**12:48** · Maybe you don't want it on your personal laptop, you want it in this other environment that is, you know, secured and locked down. And then another interesting thing is, of course it has Chrome and it can use a browser, but you can also make it essentially have like virtual desktops. So if you're running five bots, 10 bots, and each one of them needs their own browser, you can essentially let them have different screens. And all of this again is kind of shared infrastructure between these \[clears throat\] bots where they can go call on these computers.

**13:15** · Um so we talked about kind of the the triggers that will wake up the agent.

**13:19** · That's kind of on the left. So different apps or Slack messages or emails. Um then you have this middle piece, which is the server, and then on the right is the computer that we just talked about where you can run files and and commands and other things. So, let's talk a little bit more about the server. I already mentioned, you know, commands will come in, they get put into this queue, and then it calls the purple box, which is the agent loop. And this is what we covered last week. Like this is a model calling tools in a loop. And then, when you shut it down, you can kind of save the state to the database or storage.

**13:50** · Um so, it's like it's it's interesting, I think, to look at this and realize there's this one kind of small piece that can then have all of these abstractions built on top to create uh a very powerful product uh when you give it all of these helpful tools and you connect it to all of these different services.

### Server-side agent mechanics

**14:07** · The reason agent runs on the server is uh a pretty common practice in computing where you want to have kind of a thin client and a thick server. And computing has kind of oscillated between these things over the years, but for example, a few good reasons for this is let's say you need to push an update to the, you know, the agent code. It would, you know, kind of suck if you had to push an App Store update just to get that code out there versus just pushing a bunch of server updates very quickly.

**14:30** · Um also, sometimes you need to do heavy computation work, you know, like transcription or image generation or something, and that's probably going to be faster on a server than on device, depending on uh what the devices are.

**14:44** · Um and, you know, it's there's very established ways that we know how to scale servers, especially with variable traffic and variable growth. Um but the most critical thing here is that if you put the agent loop on the virtual machine, then you can't shut down the virtual machine independently from the uh from the agent server. So, yeah, you want to save everything on the server, um so, you can always kind of rebuild that virtual machine.

**15:10** · For example, let's say you need to do some critical zero-day Linux uh update on the on the VM. Well, it would be great to be able to rebuild that and not, you know, blow away the entire agent loop and have downtime in the application. Um Uh when you hit send, this is maybe a a little in the weeds, so I'll just kind of gloss through it, but basically, um if you want to dig more into learning more about distributed systems and thinking about um you know, strong versus eventual consistency, which are just fun topics to get into.

**15:42** · Uh you know, you send a message and you kind of want the client to immediately identify that and acknowledge it. Then when you go into the turn, you're obviously putting these um tools in a loop with the model, saving that to the database, and then the clients are essentially putting subscriptions with all of the servers, so they know if something changed and they're listening for these signals.

**16:02** · If they get a signal, then they can go and essentially fetch the latest information from the server, and there's some fancy deduplicating you can do to make sure if, you know, if there were some kind of retries, um that you would not show, you know, multiple messages in the the list.

**16:18** · And so, uh the like underlying infrastructure primitives to think about here, um is a workflow versus a job queue. And the main difference here is with a job queue, let's say you're kind of going along on steps, you ask your agent to go and do some kind of complicated task, uh and it's making its way from step one to step two to step three, but then for some reason there was an infrastructure issue, um there was some problem.

**16:42** · With a normal queue, if that crashes and you go to restart it, well, now you have to replay steps one, two, and three, which is obviously that that could be pretty problematic. So, what you really want here is you want a durable workflow, which means that it's safe for you to actually retry that, and when you retry after a failure, it picks right up on step three.

**17:00** · And this is like kind of a solved problem in some ways in um distributed systems and in infrastructure, so we use an open source uh tool called Temporal, which is interesting to look into if you're if you're curious, so that we don't have to rebuild a lot of this very complicated stuff from scratch. Of course, you still have to run the infrastructure for it, but some of the pieces to put together there.

**17:21** · Um so, let's say a new message comes in.

**17:25** · There's different priorities based on whether I'm messaging my agents or messaging my bots versus if it's in a group chat or a Slack thread or some background routine, for example. So, if I say, "Oh, actually, you know, change the date for this event." We actually want that agent loop to stop, and my message is going to have priority over everything else that's happening, which kind of makes sense.

**17:47** · Um for everybody else, you're kind of putting things into the queue in the back of the line, and if you're if the if the agent gets, you know, three or four messages very quickly, it's able to kind of batch those together, so it's just one turn.

**18:00** · You can kind of figure out whatever heuristic you want there.

**18:03** · Um and then it kind of goes through and does each turn at a time.

### Building the agent harness

**18:08** · Okay. So, let's talk about the the harness itself. And this is going to kind of take the the basic harness that we talked about last week and add some some new tools, some new concepts to it.

**18:21** · The biggest difference with the Grokbot harness, um and probably some of the other tools like this uh on the market, is the way we've done the thin client thick server architecture is there's only one tool that communicates between the client and the server, and it's just send to user.

**18:40** · And the great thing about this is that it's actually very architecturally simple, where the client is just texting the server in some ways, and you're putting a lot of these heavier tools on the server, and there's many of those tools. There's you're running shell commands, reading files, but also calling on a cloud agent or recording your screen or doing demos, for example.

**19:00** · Um and this I I I think has worked pretty well because now, regardless of where you spin up a new client, whether it's a mobile app, a server, um a desktop app, uh email, Slack, it all just has this one single tool that communicates back and forth with the server. On the client though, even though it just has this one tool, when it receives the tool, it can decide how it wants to display that in a rich and interactive way that makes the most sense for the user.

**19:23** · So, if it gets uh information back from the server that the user's trying to log into something, it can kind of show these unique sign-in forms and connect to tools like one password. It can go and call on services like uh Stripe Link or use XMoney or uh other services to go and allow people to pay for their services. You can If you're trying to do something that is non uh is you can't reverse it, sending an email or a Slack message, it might come back and ask you to, you know, edit and approve a draft before you send it.

**19:54** · And then sometimes it just you can know, you can just leave an emoji reaction if you don't actually need to uh send a message.

**20:00** · Um so, going back to what I was saying with dynamic tool discovery, so for uh for any model, there's a context window, which is kind of its working memory, and that's some limit in tokens, and if you just jam every single tool possible into that uh context window, you're not going to have a lot of space.

**20:20** · And the way the tools work is you have kind of the the name of the tool, you have the schema, you have all these different details, and if you start installing your Google Drive connector, your Gmail connector, your YouTube connector, like all these different services that use MTP servers, which all have tools, you're going to start looking at something like the top, where a lot of the blocks are already filled, uh and the problem with that is it doesn't give the model as much space to actually do the work of the conversation.

**20:48** · Um so, one kind of context engineering or harness trick um that a lot of the the more popular harnesses now use is uh it's called dynamic context or I think uh some other folks call it the tool search tool, which is a fun name, but basically, you're only putting the names of the tools into the every message that gets sent to the model and then the model can decide okay, I actually want to go use this tool. I can go read the information from a file.

**21:17** · It's kind of files and a file system all the way down for all of these things.

**21:23** · And that just helps you save on your context usage, which then also helps save on costs, save on usage, just better for everybody.

**21:31** · In general, the principle here really is to try the cheapest option or the most reliable option first and kind of work your way up the ladder here. So, the easiest one is just what, you know, what the agent or what the bot already knows based on the conversation history. If it doesn't, if it's not in the immediate context, maybe there's a plugin, an MCP server, some kind of API that it can go and pull, you know, your your banking information from Plaid, for example.

**21:57** · Maybe that doesn't work and it needs to go do some kind of web search to see, you know, what was the score of the Cubs game last night.

**22:06** · Um maybe if it doesn't have that, it actually needs to go to the computer and open up the browser and do some searches on there. And finally, like maybe it needs to go and actually use the entire desktop. So, run scripts or run commands or build things on that Linux computer.

**22:21** · And only if all of those fail, then go bug the user and ask them to go give input or approve something. And this really helps it feel like what it would be like to work with a colleague is like they're not going to bug you for all these different things. Ideally, they're going to try a lot of these options first.

**22:37** · Um on that computer, so the the Linux machine that the agent is able to use, there's kind of three different ways that it can retrieve information from it.

**22:47** · Um of course, it can just take a screenshot of the screen, but there's more efficient ways of doing this.

**22:53** · Um it could also look at the HTML of the page, but you can also look at the accessibility tree, which is a nice way of like cutting down a lot of the uh token usage and basically to help you find the buttons or links or other elements that you want the browser to click on. Of course, if none of that works, you can just click on pixels. So, some websites, for example, have modals or dialogues that pop up that you need to click. And so, your model, your agent needs to have that functionality as well.

**23:19** · Or, again, kind of worst case on that ladder is you go back to the user and like, "Oh, there's a like a two-factor auth code or there's some kind of CAPTCHA or or something like that."

**23:30** · Um so, the idea is that kind of putting the pieces together, you have this main agent, and it's kind of like your orchestrator.

**23:41** · And the main agent, you want to keep the conversation as sparse as possible because it now has the ability to go call on all of these different helpers.

**23:51** · And the helpers are just sub-agents. And so, this is helpful because if you hand it off to a helper to go run a bunch of shell commands or do a lot of expensive tool calls, all of that work that ultimately is ending up in some answer to a question or a task, none of that is bloating the conversation and the context of the main agent. It's only coming back with the result. And this is how you get to a product that feels like it has infinite context. Obviously, there infinite context is not a real thing. Every model has a context limit.

**24:20** · But there are these tricks and workarounds such that, especially when you train models to get better at this, that it doesn't feel like you're running up against the limits of the context window, and you don't feel a degradation of the model's quality as you get further along that as well.

**24:34** · So, we have these different helpers, each with different skills. Each one of these is its own durable workflow. So, going back to the queues versus workflows thing, that means if it fails, the video helper crashes, something, you know, uses up too much memory or something, that can restart and keep going without losing progress along the way.

**24:53** · And then the main agent it is kind of like a co-worker where it's managing a to-do list. You have a few things you can do. You can go check on it. You can send it a message. You know, you can stop the helpers, for example.

**25:05** · Um and so, a lot of this is modeled after the ideal way you would scale uh you know, a team of engineers working on a very complicated problem.

**25:12** · So, uh like just a few little interesting tidbits from building this out on the team. Um I think we'll talk a little bit more about prompt caching here, but um ideally you don't add or remove new tools during turns. Um and just like I mentioned with the slide with all of the uh boxes, if you have extremely long tool descriptions or schemas, that's going to take up a lot of space in the context window, which is bad for pricing. It's bad for usage. Ideally, you want to minimize that.

**25:40** · So, there's plenty of optimizations you can make here and on the engineering side to just trim that down.

**25:46** · Um Another interesting one is like you might hear people talk about how, oh, like we can have a harness that just has one tool. And that one tool is like running shell commands. And this is true, and you can model a lot of things this way. But, if you see the model doing, you know, 90% of its time doing shell commands for this one thing, it actually can be more efficient to make a dedicated tool for some of that stuff.

**26:06** · Um and it's it's a bit more legible for people actually reviewing \[clears throat\] how the product is working. Uh and the last one's kind of funny, too. Uh obviously, if you're writing errors for humans, it's helpful to make it very descriptive. Like, okay, this thing failed. Like, click on this link or here's what you need to do next.

**26:21** · Turns out that's also very helpful for agents. So, there's there is some DX in designing um good error messages for agents, too.

**26:29** · And when you're trusting your bots to go and do work over a long period of time, it is very important that you trust them to be secure with your information, to be secure with how it operates. So, even working on its own separate machine, not polluting anything on your machine, still you would like it if, you know, a model reviews every shell command before it goes. So, auto review.

**26:51** · It would be great if, you know, when these untrusted inputs like a email in your inbox could be a phishing email or some webhook, you don't want to send that to the model and act like it was a user instruction. And there's plenty of work to do here uh in the industry on just making sure that that is uh properly protected from um prompt injections. Um for these kind of uh non-reversible things like sending emails, right? You want to really ask the user first. And then also, you can build in some workflows into the product to keep passwords and other things outside of the model conversations.

### Context engineering techniques

**27:26** · Okay.

**27:27** · Context engineering is al- also known as harness engineering.

**27:31** · Like, I feel like it's kind of the same thing. They've evolved over time. But basically, what are some tips and tricks we can do to minimize the amount of context that's being used in these harnesses, um which is good for efficiency, for reducing costs, um and other reasons.

**27:47** · I talked about prompt caching. Um this is a good example of why it's really important. So, if you think about when you're working with a a coding agent or any agent, most of the tokens used are actually, ideally, cached tokens because you're sending it a conversation and then you're doing a change. You're You're adding one more message. And then you're basically resending the entire conversation over again. So, if you look at the pricing for models, there's huge discounts, of course, on if a token is cached. And you want to keep them in the cached window as long as possible.

**28:15** · And so, a way to do this is you try to keep the tool definitions, the system prompts, all this information as static as possible between different calls so that you don't break the cache and then have to pay for the un-cached tokens every single time. So, if you have that fixed part at the top, then, you know, when you get down to the bottom and you only have the newest message that comes in, that's the only delta that you're paying the un-cached tokens for. And there's a a whole art and science uh to this as well.

**28:47** · Basically, because that main agent in the most ideal sense, this is the one you're having this very, very, very long conversation with that's compacting or compressing, so summarizing the context many, many times over without you even noticing sometimes, which we'll show an example of. So, you really want to keep that context small.

**29:07** · Um some ways of doing that is anytime there's a very long output, rather than stuffing that in the context, you can just put it in a file. And the agents are very good at reading files. Uh so, this actually works pretty well, which is just like reading a skill or reading a memory, for example. If you give the model a screenshot, um or some other very expensive work, you just delegate that out to a helper.

**29:30** · Again, so it goes to the sub-agent, and it doesn't affect the main agent's context. Um and then also, in an ideal world, you want to kind of be always gardening and trimming and removing unnecessary stuff from this conversation, from this context window, as you're going, both for cost, but for also recall and just making sure the model's performing well.

**29:52** · So, if there's a cash cash miss, it's kind of like a bug in the system, really. Um and if if you go all the way back to uh all the way back to January of this year, uh when Open Claw was really getting popular and people were using it uh inside of subscription plans for uh model providers, this was a very new usage pattern that model providers hadn't really seen, and the the harness hadn't really yet been optimized for this type of workflow. So, there was a lot of cash misses.

**30:21** · And when you're doing something like this, where agents are running all the time, uh that's obviously problematic. So, lots of fixes had to go in to make that robust to keeping the cash uh keeping the prompt cache as much as possible.

**30:35** · Um so, like a fun uh a fun trick here is just trying to keep everything in the prompt in order, such that even if you deploy a new change where you want to test out some new change to the system prompt or add a new tool, you can you can almost hash each section and always keep a fixed order. Like let's say you're doing a AB test and you want to put a new piece of the prompt in there, you really don't want that to screw up the prompt order for everybody else, otherwise you just busted the cash and then that's that's problematic.

**31:05** · Um another fun one is when you open the chat and you start typing um the server can actually go and prepare the prompt early uh to basically warm the cash almost like if you're on a website and you go to hover on a link, it can go and pre-fetch the next page. Um so there's like tons and tons of little engineering optimizations that compound how far these models can go in terms of token usage uh and how smart they can be when you use them for a very long periods of time.

**31:32** · And the key thing is that when you're working over a very long period of time, you essentially have to get very good at compaction or summarization because let's say the model has a 200,000 token context window, you're going and going and going, eventually it's going to hit a point where it needs to summarize and all compression is lossy.

**31:49** · So you have to figure out the best algorithm to do the compression and not lose important details and there's I'm sure entire uh PhDs just for this problem like it's very it's very very tough to do right, but just to show an example like let's say you're going back and forth with your with your bot, uh you have over 100,000 tokens uh and then you go and do something else. Well, there is this time period where the model providers have uh like a cash window when the cash is still warm. Maybe it's 10 minutes, maybe it's 60 minutes.

**32:19** · Uh one trick that we do which I think is really helpful is while you're still within the warm cash period, you should probably do the the compaction right now because it's you have this long conversation, it's going to be much cheaper. So just go ahead, do the compaction and now when the user comes back in 30 minutes or whatever, they're starting from this summary. And the summary now is going to be much cheaper for them to continue adding messages on. So, lots of work to do there to make it um to make the algorithm very high quality for how you do summarization.

### Managing agent memory

**32:51** · When you talk about compaction and what information you choose to include in the agent's memory, I kind of think about it in a few different layers. The first one is like facts about the user that are very important to be included every single time. Going back to earlier when I said, "Oh, like the user always wants to have lowercase text." That probably needs to be in every single message, otherwise it would be really weird if one message now has uppercase letters.

**33:17** · Uh if you're going like full Sam Altman style. Um then uh you probably also have some prompts that you want or some facts that you want to include in there.

**33:25** · And there's many different ways you can make this algorithm to determine what are the most important facts to keep.

**33:31** · So, ideally there's this kind of garbage collection of this fact And like if you think about it, this is kind of how our brains work. It's like this fact right now is important to keep. It's relevant for this conversation today. You're probably not thinking about you know, a soccer match right now. Uh and your brain is very good at keeping those ones in context right now and kind of remembering them for later. We tried to model some of that here where the the the harness has of course these core facts. It also has these dated logs of kind of your past conversation history essentially.

**34:03** · And then also these kind of scratchpad notes. So, there's like little things that you've been working on right now that are designed to be ephemeral and they will go away, but they might be relevant just for the next 30 minutes or an hour. And everything else can be found through files. This is the magic of files of the models being good at running commands is like they can always just go look stuff up and they're actually very good at doing that.

**34:27** · So, where where is this going?

### Training and product iteration

**34:29** · There's this flywheel of training the model to get better at the product. And just as a high-level refresher on kind of the stages of training a large language model, uh first you have pre-training where the model learns uh a general understanding of the world from large amounts of internet text or other private data. Then you have supervised fine-tuning where you're teaching the model how to behave uh in a certain way, maybe as a chat assistant or as an agent.

**34:58** · And then finally you have reinforcement learning where it's kind of like teaching the model how to play games and get better at those games. Um and in the context of these always-on agents, it's very helpful, for example, to train the model to see examples of the harness and to know how to work inside of the harness in SFT. Um so it can understand the tools that you have available. It's helpful to train the model to be better at instruction following during reinforcement learning.

**35:25** · How to understand the right skill to call when there's hundreds of skills, for example, how to click on the right spots when you're given in the browser and needs to kind of click around. Um and not only the training itself, but also how you serve the model, the inference that you do. The main agent you're talking with, you know, ideally you want it to have very low latency.

**35:45** · You want it to come back to you right away, give you really fast replies, and you can tune the harness and the inference to do that. But then when you go hand it off to a helper and you're asking it to go do some work for a very, very long period of time, the difference between 10 minutes and 12 minutes is kind of negligible at that point. So that allows you to kind of control uh how you optimize things.

**36:06** · Um the way that this kind of flywheel works is that, let's say your agent gets something wrong.

**36:13** · Um ideally then that gets turned into some kind of evaluation. So uh the model, you know, accidentally uh called this tool when it wasn't supposed to. Um then on the back end you can go and fix the harness, you can fix the bug, you can fix the prompt, maybe it's an inference issue. Uh you can check and make sure it's actually fixed in the evals and then ship the change. Uh and you know, the the teams uh and the products uh the teams working on these products, they're kind of doing this every single day. They're finding bugs, they're fixing it, they're measuring it with evals. That's kind of this inner loop that you're always getting better at.

**36:44** · But then there's this outer loop, which is like every few months or every month or however long, um you're training new models. And ideally the new models are learning from all of these bugs and these failures, and they're kind of climbing on the evals to get better at the things that you care about. And you can drop the new versions into the product and make sure that they're improving at all these different things. And the fun thing about this is then when the new models come out, they have new capability jumps. Um it allows you to use the product in new ways. So, there hasn't really been a lot of training data, for example, on using bots in a group chat.

**37:14** · This is kind of an emergent thing that's being figured out.

**37:18** · Uh and it's important to get it right.

**37:20** · Obviously, uh if you've seen things like Multibook or the Hugging Face incident, like there are ways that that goes poorly. So, it's important to be able to train the models how to behave well in a multi-agent system where uh different bots are talking to each other, for example.

**37:34** · Um And so, ideally, you're always kind of running these inner loops and outer loops uh as a product team building these type of harnesses at a company uh working on on AI together.

### Future outlook and conclusions

**37:45** · Um one of the principles that we had at Cursor uh and now uh at SpaceX is to delete the product. And what we mean by this is you kind of have to internalize and assume that the models today are the worst they'll ever be, which means that in 6 months uh you might need to completely rebuild the UI. Like most of the stuff that I've talked about today, uh it's a pretty big update from if I would have given this talk 6 months ago or definitely a year ago, because we've learned a lot of uh new practical ways of building harnesses and doing context engineering.

**38:17** · So, a good strategy here is you you really want to try to build for the next generation of the model. Like how do you build as little as possible and get by while making just a really really simple interface to work with these models and allow them to to to think and act for you.

**38:35** · So, some things that I think will happen in the next 6 to 12 months. We'll see. I think these are decently safe bets, but you know, right now let's say you have your agents or your bots working for maybe a few hours, maybe a day depending on how tough it is. I think it's very possible that pretty soon your agents will be working for weeks or months.

**38:58** · And it does bring up some kind of interesting questions in terms of how we train and evaluate those models. I think the models are going to get better and better about how they recall on past information in in conversations. Plenty of different approaches in research here for the type of algorithms used or the representation of the data under the hood. Maybe it's a graph, maybe it's files, maybe something else.

**39:21** · I think ideally if you have this digital colleague, you give it literally all the tools that you have if you were onboarding a real human. And so I think organizations are still warming up to that idea, of course. So there's more to do there. I think the interfaces will maybe get even easier. I think some people will prefer to just talk to their kind of bots or agents as a in a speech to speech way. Maybe they'll have their like Johnny Ive device that is hopefully really cool and they can like talk to that all day.

**39:53** · I think the models and the products will get really good at learning skills on the job and then encoding that into files and instructions, skills, taking that raw intelligence and actually making it useful for whatever whatever task you're asking it to do.

**40:09** · And people and companies are going to get much better I think about uh, writing down how all of these kind of bespoke processes work so that they're legible for agents to use. So, some interesting problems I think that like could just spark ideas for you all to to research or to look into. The first one is like going back to this idea of agents that run for a month, what do you do when you need to evaluate an agent that runs for a month, but the models ship every month?

**40:35** · You know, it's like \[laughter\] you can't fully evaluate that the model is, uh, sufficiently, uh, behaving as expected. So, you either have to figure out how to do a better eval or, you know, not ship models as fast. And I think that's going to be a problem that the industry has to figure out in the next 6 months. Um, memory, obviously there we talked about the different algorithms.

**40:56** · I think there's so much to do on the security side for how to make a secure harness, how to make the infrastructure \[clears throat\] around these agents, um, very secure, uh, and so they can't be taken over by bad actors.

**41:10** · I think we didn't really talk about it too much, but the heuristics around when the agent is silent or when it kind of bugs you, uh, I don't think that we have it perfect yet and I think trying to thread the needle between being proactive and suggesting like, oh hey, like I saw that you missed class yesterday. Like I I I had, uh, a recording there and I took the notes and like here's the thing, like maybe that's helpful or maybe that's kind of annoying, you know, and like trying to figure out the right the right balance there.

**41:38** · Um, I also think that it's a pretty safe bet to assume that at this time next year there will be significantly, significantly more tokens flowing in the world, which means that optimizing the inference, optimizing the models, optimizing the harnesses, trying to drive down the tokens to, uh, be more efficient will also, the token usage to be more efficient, I think will also be very important. So, there's kind of these new building blocks to think about.

**42:06** · I believe it was Alex from Open Router that that on on X, he had a really good take on this. There was people saying like, "Oh, every app today it looks the same. You've got the sidebar, you know, you've got the agent, we got the chat box. Like, everybody's building the same thing." And he was like, "Yeah, that's like in 2005." He said, "Everybody's building the same thing. They've got a server, they've got a database, they've got some like crud interface to like update and delete things."

**42:31** · And the reality is, this is just kind of the new normal now where every new product is going to have to have some kind of agentic side to it, either integrating or it will become a you know, a headless piece of data for another agent to use.

**42:48** · And so we've talked about a lot of these products today, durable workflows, sandboxes, computers in the cloud, memory skills, uh connecting to \[clears throat\] other services, doing voice, payments, identity, e-vals, observability. Each one of those boxes is like multiple billions of dollars of VC capital, and it's probably trillions.

**43:07** · There's 20 startups for each one of those, and there's so many different things to explore in all of those because they kind of are the new primitives for the next generation of companies, the next generation of products. And they all have to integrate and be part of harnesses. So there's there's definitely a lot to do there. A few things to take away and then we'll have time for questions. Obviously you all are engineers, you're thinking about how to write software. It's more important than ever to think about the broader system design and the architecture of the code that you're working on because that the decisions you make there will really compound.

**43:38** · Um so I'm still I'm still pro looking at code. You know, I still look at the code that I'm writing. Some people not looking at code. I still think it's helpful, especially to understand the architecture that you're shipping. It's crazy how much that's changed in just a couple years. Um secondly, you know, it sounds like you all were kind of messing around with building own versions or understanding of how the harness worked in last week.

**44:01** · I encourage you to think about some of the things that I did today and try to apply that and think about how you might build a version for yourself. I'm pretty sure there's like open Grokbot on GitHub somewhere where somebody's like, you know, slot forked our code and made and made a version.

**44:19** · And you could probably set up like the the GUI for that with, you know, a sandbox somewhere and you know, a VM and like all sorts of different things. So that could be interesting if you want to learn a little bit more about how these pieces work.

**44:33** · And then finally, I would not shy away from just learning a little bit more about how LLMs work. You know, we gave a little bit of the TLDR here of how they're trained, but there's so much more you can go into here without necessarily going deep in ML or deep into the science part of it. But I think it's helpful to understand just like when you're building a web app, it's helpful to know how databases work because increasingly the there are so many decisions you make at the product and the harness level that are influenced by the models themselves.

**45:02** · And having an intuition of how that works, I think will make you very well positioned for whatever role you're operating in.

**45:11** · And that's all I have today.

**45:13** · \[applause\] Thank you.