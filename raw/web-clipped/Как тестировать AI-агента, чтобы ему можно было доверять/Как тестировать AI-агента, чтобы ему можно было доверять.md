---
title: "\"Как тестировать AI-агента, чтобы ему можно было доверять\""
source: "https://www.youtube.com/watch?v=bFHCK6PB0hA"
author:
  - "[[Дмитрий Березницкий]]"
published: 2026-10-09
created: 2026-10-22
description: "Как тестировать AI-агента, чтобы ему можно было доверять: тесты проходят, а в проде он врёт, зацикливается и дёргает не те инструменты. Разбираем evals для агентов: что на самом деле тестировать, чем"
tags:
  - "clippings"
url: "\"https://www.youtube.com/watch?v=bFHCK6PB0hA\""
fetched: " 2026-10-22T13:35:44+05:00"
---
![](https://www.youtube.com/watch?v=bFHCK6PB0hA)

Как тестировать AI-агента, чтобы ему можно было доверять: тесты проходят, а в проде он врёт, зацикливается и дёргает не те инструменты. Разбираем evals для агентов: что на самом деле тестировать, чем мерить и как отличить регрессию от шума.  
  
В видео:  
— почему при нулевой температуре LLM всё равно отвечает по-разному  
— pass@k и pass^k: почему агент проходит тесты, но ненадёжен  
— что в harness проверяется без единого вызова модели и почему это бесплатно  
— как модель меняется под вами, даже если вы её не трогали  
— почему в памяти агента опаснее не забытый факт, а устаревший  
— LLM-судья видел поломку и всё равно ставил зачёт: как калибровать судью по разметке людей  
— тест с живой моделью падает через раз: регрессия это или шум  
— как суд в Германии спросил с компании за выдумки её чат-бота  
  
Таймкоды:  
0:00 — Введение  
2:14 — Почему обычные тесты не работают: pass@k и pass^k  
8:59 — Что тестировать: harness и модель  
17:30 — Память и tools  
23:59 — Кто ставит оценку: код, LLM-судья, человек  
29:46 — Регрессия или шум. Откуда брать тест-кейсы  
32:57 — Что ещё ломает агентов: от перефразировок до суда  
  
  
Недетерминизм LLM на GPU (Yuan et al.) — https://arxiv.org/html/2506.09501v2  
Метрика pass^k, τ-bench — https://arxiv.org/abs/2406.12045  
Средний успех против стабильности, 16 моделей (Zhou et al.) — https://arxiv.org/abs/2606.00920  
HAL, надёжность агентов (Принстон) — https://hal.cs.princeton.edu/reliability/  
Harness сильнее модели — https://arxiv.org/abs/2605.23950  
Регрессии при обновлении модели, flip rate — https://arxiv.org/abs/2608.13607  
From Recall to Forgetting, устаревшая память — https://arxiv.org/html/2604.20006v1  
Ошибки tools копятся по цепочке — https://arxiv.org/abs/2608.26189  
Судья по результату пропускает тихие сбои — https://arxiv.org/abs/2609.00038  
21 LLM-судья и каппа Коэна (Norman et al.) — https://arxiv.org/abs/2606.19544  
Судья видел дефект и ставил зачёт за тон — https://arxiv.org/abs/2606.10315  
Agent-as-a-Judge — https://arxiv.org/abs/2410.10934  
Hamel Husain и Shreya Shankar о системе evals — https://www.lennysnewsletter.com/p/building-eval-systems-that-improve  
Решение суда Хамма о чат-боте клиники — https://nrwe.justiz.nrw.de/olgs/hamm/j2026/4\_UKl\_3\_25\_Urteil\_20260512.html  
AgentChaos, отказы LLM API — https://arxiv.org/abs/2608.06790

## Transcript

### Введение

**0:00** · I built a system where an agent's work at every development phase is checked by another agent on a different model.

**0:05** · Research, design, code, tests, deploy.

**0:07** · Each of the phases produces some kind of artifact. And this reviewer agent or various reviewer agents give me a report on whether everything is good or bad, and can automatically feed this info back into the dev cycle to make things more automated. And when I started testing this system, I noticed that reviewers at each phase were saying, "Yes, everything is great, it's cool, let's keep going, we like it all.

**0:28** · " But at the same time, I knew for a fact that not everything was actually good. It turned out that the input sent to the checker wasn't the full diff of what had been done or the actual artifacts, but just a brief summary of the phase and what was done there. And of course, based on the brief summary, everything looked fine. In other words, visually it looked perfect, but in reality, it didn't work at all. This has happened to me more than once in agent development, where agents did something completely different from what I expected, even though everything was written as it should be. Perhaps you've encountered this, too.

**0:56** · You roll out your agent to production, and there it starts lying, getting stuck in loops , or calling the wrong tools. And when you start discussing what to do about it, you immediately hear the answer: " Well, we need more tests." And my mind also tells me: "Well, of course, if it doesn't work, it means we need to test it much better so we don't have situations where we roll something out and it doesn't work for some reason."

**1:18** · But we've all written tests, so let's think: when we write a test for an agent, what exactly are we testing? The model, the prompt with the wrapper, the memory, or maybe the tool selection?

**1:28** · And if there is no answer to that question, then it's unclear what these tests are actually catching. I have been building agentic systems in production for the last year and a half . I've made a lot of mistakes during this time, and now I test agents as four separate objects. Each has its own methods and metrics, and they will have their own pitfalls as well. And for an example, let's take a support agent that handles product returns and refunds for us. It searches for orders in the database, checks the return policy, processes refunds, and replies to the customer. And it also remembers previous interactions.

**1:58** · It will have several tools, memory, and, of course, the model under the hood. And based on this example, we can see how to test the specific parts of our agent. Let's recall what we need to test and what to look at. And let's start with why standard tests won't work for us here.

### Почему обычные тесты не работают: pass@k и pass^k

**2:21** · The testing we are used to relies on a single contract. The same input produces the same output. LLMs do not follow this contract. But the reason is not that the model is probabilistic by nature. At zero temperature, the model by definition picks the most probable token. And this non-determinism can arise on the provider's side. Requests are processed there in batches. GPU kernels behave differently depending on the batch size. And the order of floating-point addition changes the result. Roughly speaking, your request is processed alongside someone else's, and the order of calculation may change .

**2:52** · It changes noticeably at standard BF16 precision. The response text diverges for most requests between runs . Moreover, when we tested reasoning models, it diverged almost always and very significantly. The longer the generation, the more likely the responses are to diverge. And that is why, for testing, we will have to run our task several times. It is necessary to understand whether it works or not.

**3:14** · A single run of a task tells us nothing about stability. Therefore, we run the same task several times in a row. And between runs, we keep everything exactly as it is. The prompt, the tool order, and the temperature remain the same as we had before. These are repetitions. They are used to calculate pass@k, which shows the model's own variance. Therefore, if you change something between our runs, like the order of the tools we have, we end up measuring our own edit, and the model's variance gets mixed into a single number.

**3:46** · And from that, it will be hard to understand what exactly is going wrong for us. Because robustness to rephrasing and reordering is a separate test. We will talk about that a little later in this video. Let's return to our Return agent. The client writes: "I want to return order 1 2 3 4 5." This is a hypothetical example, but suppose we ran it five times. Four times the agent found the order and checked the policy, but one time it went straight to processing the refund without a check. And this kind of variance is only caught by our repetitions.

**4:17** · And since we have multiple runs, we need to agree on what it means for our task to be solved or for the agent to have handled it. And for the returns agent, this will be a deterministic check. The correct tool was called, and the refund amount is correct. So let's take four tasks and run each of them five times.

**4:39** · Suppose task A passed all five times and everything was executed. Meanwhile, B failed only once, and task C was successfully completed only once. And task D, in turn, never completed successfully even once. So, we have two metrics. So, the pass metric answers the question: can our agent solve the task at least once over k runs? That is , if there are five of them, then this will be pass-five.

**5:09** · And pass to the power of k will answer the question of how consistently the runs were performed. Meaning it will equal one if all runs were successful. And, accordingly, we can calculate these metrics now. And as we see, pass to the power of K is much stricter than pass at K. So the task counts only if all five runs pass and achieve their goal.

**5:38** · And, accordingly, on the set of these tasks that we are counting for this test case, we get 25%for it. Therefore, in general, this metric will show whether we can rely on this agent to solve specific tasks. Let's go over this one more time. Here are those five runs and those five tasks. Within a single task, we didn't change anything: not the prompts, not the wrapper, not the request. At the same time, different tasks might have slightly different requests. For example, for our refund agent, the request might be: "I need to process a refund for order 555."

**6:10** · And for task B, the request could be: "I want to return my new sneakers or something else." So, we keep everything as stable as possible and simply run the tests again. At the same time, these four tasks will serve as our test set for verifying the agent's performance. You can choose any number of runs for your test case.

**6:32** · So, for production, pass to the power of k is what's important to us, because the same request can come from hundreds of clients, and so on, as it tells us how well our agent solves our clients ' tasks. And if it's 25%, it means we know that 75%of the tasks our clients send us will fail. My co-authors and I calculated the average success and average stability on real models.

**7:00** · In May of this year, they took 16 models and ran each task five times. And after the runs, they found that one model ranked higher on average, while a completely different one was more stable. Researchers from Princeton measured the stability of frontier models this year and wrote that over 24 months of development, model stability has barely increased. A model that handles nearly 80%of tasks is less stable than its predecessor. Now let's return to our table again. Our task D did not pass a single check out of five .

**7:33** · It is in the same suite, meaning it has something in common with all the other tasks. Perhaps this request involved a refund in a different currency, or customers with a very long support history were too complex for our agents to handle. So, if we have many test cases that keep failing, the final results will drop for both Pass@K and the exponent of K. However, if we look at tasks B and C, we can see that, in general, the agent is capable of solving the task. Here it solved it once, and here four times. This means that B failed on a specific run.

**8:07** · Therefore, looking at the metrics, if Pass@K is high but the exponent of K is low, it most likely indicates some instability in our harness. And we will need to pay attention to what exactly is wrong with it. Perhaps we need to add more deterministic parts and rely less on how the model itself makes decisions. So, if we take certain classes of our tasks, combine them into suites, and run them many times, we can track where we have instability and where there are problems.

**8:34** · Pay attention to these test cases, perhaps estimate something, change it, and test it again . And next, we will analyze with you what we should do about this. After all , this is how we can test individual parts of our system. We changed the prompts and saw if things got better or worse. We changed the harness and saw if things got better or worse.

**8:52** · Accordingly, we have a snapshot, we have metrics, which means we can effectively test and measure. Now we have seen that a single run is not enough, and we need to perform many runs. At the same time, the agent's answers fluctuate. And the question arises: "So what exactly are we testing then?" Let's figure it out. Initially, we drew four layers that we can test.

### Что тестировать: harness и модель

**9:16** · Before breaking down each layer, let's determine the order in which we should approach testing them. And let's start from the outside. Let's see if there is a correct result. If there is no correct result, we go deeper into the harness and check if the code is working. Next, we look at the model to see if our response is stable. And only then do we start testing memory and tools. This way, you can quickly find where the failure is without diving into debugging the model until we are sure that, for example, the parser didn't eat half of the response. Let's break it down, starting with our harness.

**9:47** · Let's go over it one more time . A harness is the wrapper, it's all the code surrounding the model. Routing , orchestration, response parsing, retry logic, tool calls, guardrails, prompts, tool descriptions, skill descriptions. All of this will be included in our harness. And part of this is code. It will be stored in our Git repository. And it will be tested exactly like regular code. Suppose our hypothetical returns agent has a small router, and it determines the type of request. Is it a return, a complaint, or a question about delivery?

**10:18** · There is a parser that extracts the order number from the text. Perhaps there is also a retry mechanism for timeouts and guardrails for amounts. That is, if the refund exceeds a certain threshold, it won't go through without approval from a manager who says, "Yes, of course, you can refund this entire incredible amount for this order." Moreover, the harness determines the result more strongly than the model. Change the harness without touching the model, and the variance will be much greater than from changing the model itself.

**10:43** · And if we build some kind of ranking of models for our agent, different harnesses will change this ranking, changing the order of models in our rating depending on what we implemented in them. For example, at one point in our tests, Opus listened perfectly to prohibitions using "not," meaning "don't do this."

**11:05** · But when we tested it on the same "not, " it worked very poorly; however, as soon as we gave it a positive "do it this way," it started showing much better results. That is, if you tuned your harness for a specific model, it might underperform on another due to the specificities of individual models.

**11:22** · Therefore, prompts are essentially not portable between models. We must look at which model works with which prompt format, especially when it comes to Opus and Anthropic. Since they have recently introduced many interesting rules on how to write prompts to work with their new frontier models. So, if part of the harness is code, we can test it without the model. And there will be several test suites here. The first one will never call the model.

**11:50** · That is, we plug in recorded model responses and test our harness. This type of testing is called "record and replay." We record the LLM responses in advance and then use them for testing.

**12:01** · It is cheap and deterministic.

**12:03** · Therefore, we can run this suite on every commit we make. As soon as our fixtures go stale, and they certainly will—for instance, if we changed a prompt, the model, or the order of calls in our orchestrator—we will need to overwrite them, because otherwise, we would be testing our harness against old responses that no longer exist. The second suite runs with a live model, and it is expensive.

**12:24** · Where to run it depends on your budget and whether you are making changes right now or not. Perhaps you have plenty of budget and unlimited tokens; then you can run it on every PR. If you are limited, then it's worth doing at least before a release. Or perhaps you'll include this test as an A/B test : part of the traffic gets one thing, part gets another, and you measure how it works. Therefore, from now on, I will talk about PRs. But if you have a different rhythm, then substitute that rhythm and the way you will launch this test. So, what should we check there if we can't expect an exact match?

**12:56** · We will analyze this a little later. Therefore, for our harness where we work with models, we can test without our LLM if we record the answers in advance, running it on every commit, and it will cost zero dollars in token consumption.

**13:16** · The second part is more expensive, where we already use real responses.

**13:20** · That is, we take our LLM, we set it up for specific parts like PRs, releases, or A/B testing, and this can already be a quite expensive operation. Therefore, it is worth separating them. This is precisely related to that money. If we set up LLM calls for every single move we make, we will burn a huge amount of tokens, especially if we use expensive models for this testing. Regarding the retrieval phase, it also belongs to our harness. If it provides garbage, then, of course, our model will receive garbage as input and output garbage.

**13:51** · Therefore, we will test retrieval separately. Did we send a request there , and did we receive relevant documents ? This is a deterministic check, provided we have labeled once which documents are relevant and which are not, and the LLM will participate there as a judge. Therefore, we can also record the retrieval responses here, which we will plug in to test our harness. The next part of our testing is the model. The model powering our agent changes either by our desire.

**14:21** · We see a new version has come out; maybe it's cheaper, faster, or even smarter.

**14:26** · Any marketing term can be inserted here , and we want to change it. But if we didn't deploy this model ourselves and don't control it, it can actually change without us noticing. It all depends on the provider. In August of this year, researchers measured six pairs of updates from one version to another. They called the metric "flip rate," which is the share of answers that were correct and became incorrect.

**14:47** · On MMLU Pro, between a quarter and a third of previously correct answers break. For math, the spread is wider, from 5%to half. Code holds up the best.

**14:55** · It’s at 10-25%. And yet, average accuracy after an update increased by a couple of points in some places, and by 30 in others. They looked for a signal that would show in advance which case would break, but couldn't find one.

**15:08** · Meaning, you can't guess. The only right thing to do is to test and run our models. Touching on how a model can change even if we didn't seem to change it, what could happen. So, let's talk about pinning. That is, if a model is pinned with a date and name, the direct API fixes the weights, and Anthropic states in its documentation that weights under that ID won't change, but the stack around the weights might.

**15:34** · This could be the router, safety classification, or sampling. Sometimes this is visible in the behavior. Today you asked your model to do something, and it says: "No, I can't do that."

**15:44** · Even though yesterday it did the exact same thing, while the model itself didn't change for you. Now let's look at OpenRouter, which is currently gaining huge popularity. Under a single model name, there can be several dozen vendors. At the same time, they will have different weight quantizations and different deployment settings. And OpenRouter itself, if you don't choose specific providers, will choose for you , sending your request here today and there tomorrow. Here it worked with this vendor now, then with another vendor.

**16:13** · I ran a test, sent eight requests, and they went to six different hosts. At the same time, the same request spent an absolutely different number of tokens on reasoning at different hosts. From a completely minimal 10 tokens for reasoning to a very large set. 300, 400, 500 tokens, 1,000 tokens could go toward reasoning.

**16:34** · Therefore, if you don't pin a specific vendor, you'll be measuring the average across someone else's hardware. So, in all three cases—whether you change the model yourself, or the provider changes some wrapper around it, or you use someone like OpenRouter that can route you to different vendors—we need to run our regression suite on a schedule to understand if everything is okay with this model regarding our agents. And for agents, my regression suite has about 30 to 50 real tasks from our domain.

**17:05** · At the same time, for our returns agent that we came up with today, we can take about 30 real customer inquiries, where we already know which answers were correct. So, you switched the model or updated the prompt and ran this regression suite.

**17:22** · If you don't have any real-world data to build a regression suite on, we’ll talk about that later in the video.

**17:28** · Keep watching. Our next testing layer is our Memory. This June, the MemAgent benchmark was released. It compared five memory strategies. External KV-storage searches the best, but it pays for that with the context window.

### Память и tools

**17:45** · And that means about 20 times more tokens. The other four, from long context to summarization, find almost nothing if the required fact is many sessions back. So, what should we be testing here? That’s an open question . And facts about whether we remembered or forgot something probably aren't exactly what we should be testing in our memory. A study from "Recall of the Forgotten" analyzed errors in recommendation tasks. Out of 20 errors, 16—that's almost two-thirds— happened because an outdated fact wasn't forgotten. In our memory video, we called this "drift."

**18:16** · So, we need to test whether the agent knows how not to rely on outdated memory. Sometimes this means re-verifying a fact in the source . And sometimes, honestly, I don't know . Let's go back to our fictional agent.

**18:29** · A client contacted us a month ago, when the return policy might have been 30 days, but it has since changed to 14.

**18:37** · The agent remembers the previous inquiry and the old policy. What will it answer our client? The correct answer is to apply the new policy and explain that the rules have changed.

**18:47** · And for the outdated memory test, we change the policy in the source, ask the agent, and check if it gives the new or the old one. Second memory test.

**18:54** · I analyzed this in detail in the video about production agents using the story about the Meta alignment director's email. There, the "do not act without my okay" constraint. Didn't survive the compression. This is tested in the exact same way. We fill the context before our completion and check if the constraint stays alive or disappears from our new context window. Therefore, when testing memory, we need to identify the critical points for our agent. What it pulls from memory and how that might affect the entire system . And for that, we need to think through and write tests, and run them as well.

**19:25** · The next part is working with our tools. As we know, our agent can't do anything without tools. Therefore, for each of our test tasks, we specify the expected tool. But we do not compare the text of our agent's response. We look at whether the necessary tool was called with the correct parameters. And this check will be deterministic. Sometimes a task can be solved in several ways. In that case , the expected tool is described as a set.

**19:54** · Which of them were mandatory and which were forbidden, because a rigid sequence breaks at the very first valid workaround. An interesting study came out in August of this year, calculating the cost of a single parameter error, since our tools are often chained together. By the sixth step of the chain, the agent loses about 70%of the capability it shows in a clean context.

**20:18** · Yet the task itself has not become any more complex. The agent trips over its own early mistakes; that is, in our agent's loop, it calls a tool, gets an answer, adds it to the context, calls a new tool, gets an answer, and adds it to the context. In this cycle, the earlier an error occurs with a tool, the more that error will accumulate as we proceed. And we will just burn through the context for nothing, get poor results, and our tests will fail.

**20:42** · As an example, consider our returns agent. Perhaps when it tried to call the "get order by id" tool, it somehow mixed up the identifier and retrieved someone else's order. And what will it do next? It will check the policy and process a refund for someone else's order, which does not belong to the client who made the request. In this case, each tool will visually appear to work correctly, but money will be refunded for the wrong order, and the current client will not receive their refund. That is why it is not enough to test tools one by one. You need to verify the entire chain of specific use cases that our agent performs.

**21:14** · That is, let's take everything the agent did for a single task: the client's code, every tool call with its arguments, every model response; roughly speaking, everything that passed through the context window. This can be called the trajectory of how we are moving toward solving our task. And one should never test a rigid sequence of steps in this log, in this trajectory, because it results in a very fragile test, since agents, as we know, always find other paths to solve the task.

**21:42** · And when we were trying to come up with this test to evaluate the entire trajectory and everything that happened, we might not have foreseen the paths the agent took to reach the correct solution.

**21:53** · Therefore, when we test tools, we have several options. First, we check the arguments with which the tools were called. Were the mandatory tools called to solve the given task? Next, we check if any forbidden tools were called to solve the given task. In one paper, it was calculated that an LLM judge, which only looks at the result, catches 45%of failures. It misses more than half of them. I will talk about the judge in detail a little later.

**22:21** · A silent failure is when our refund is processed correctly. But along the way, the agent peeked into someone else's order and put their data into the context. Or perhaps it even tried to perform actions that were incorrect for solving this task. And this invariant is caught very well. For instance, search order only using IDs from the request or from that client's history. If the agent promises the client compensation along the way that isn't in the policy, it's quite hard to express that in an invariant. And that can be caught by a judge that reads our trajectory.

**22:51** · What happened, what the request was, and what response we plan to provide. And this judge, which receives the entire log of our agent—that is, the full trajectory—is much more expensive than a judge looking only at the result . Therefore, we must test not only the result but the trajectory itself. And these are both tests; one does not cancel out the other. For example, we had an agent that builds cohorts for clients, and it had five tools. After that, we added two more filters for customer profile attributes to it.

**23:21** · But the agent didn't call them and simply responded with text. And the reason was found in the System Prompt. A line had remained there from a previous version.

**23:30** · "We will not build cohorts based on profile attributes." So, the prompt forbade exactly what the new tools were doing, and the model obeyed the prompt.

**23:38** · And when we add a new tool, it means we have changed the setup and run our suite, which calls the actual LLM, where we have defined which tools are expected to be called. This allows us to catch such a problem at the development stage before this agent with these tools ever reaches production. The four layers we looked at answer the question of what to test.

### Кто ставит оценку: код, LLM-судья, человек

**24:02** · Now we need to understand how to decide if our agent succeeded or completely failed. And here, there can also be several levels of evaluation. The first level is the cheapest, which is deterministic checks. Was the correct tool called, was the schema valid, did something prohibited leak, and did we stay within our token budget? Here we also verify the invariants from the block we just discussed. These checks cost us absolutely nothing, and they work instantly. And in my experience, a huge number of our agent's bugs are caught here.

**24:33** · Accordingly, we can say that this check is performed by code.

**24:38** · It is free for us. And here we find— well, probably half of the bugs I have encountered in my practice were found precisely through such checks. The next part will be our judge. And it will evaluate what we cannot check with code . That is, the quality of our response, its completeness, and its tone. LLM judges usually report that they agree with humans over 80 percent of the time . But that’s just the raw agreement rate, and some of it could be coincidental. And this correction for randomness is called Cohen's kappa.

**25:12** · Basically, we take answers already labeled by humans and give the same answers to the judge. Then we check how much more often it agrees with humans than if it had just assigned scores by flipping a coin. Zero is a coin flip, one is a perfect match. In June 2024, Justin Norman and his co-authors ran 21 judges from nine providers. And that was half a million judgments. On MT-Bench, those same judges that had over 80 percent agreement score around 0.45 in kappa. On other datasets, it can go up to 0.9.

**25:42** · So, the number depends heavily on what we are judging.

**25:47** · I personally like a benchmark from another paper. It’s called "Judge Verdict." Have two humans label the same set and calculate the kappa between them. The authors got 0.8. And you should demand that your judge is not much worse than humans. Sajank and his colleagues, in that same June, took a deployed agent that takes orders and compared its judge to human labeling.

**26:10** · Out of nine system issues that humans found, the judge caught two. Its production gate missed all 100 rounds in a batch where humans counted 23 defects. And in almost every note, the judge described the order confirmation or cart error itself, but gave a score based on brand tone; so, it noticed the break, but didn't penalize the score for it. Judges have three known biases.

**26:33** · They were described back in 2023 in the MT-Bench paper. And mainly for pairwise comparison, the first is position bias, where the score depends on the order in which the answers were shown. Also, the judge loves long answers simply for their volume. And there is a third, most controversial one, where a model overrates its own family. I have caught this length bias myself when testing models. In about three out of four cases, the longest answer took first place, and the winner was, on average, more than twice as long as the loser.

**27:02** · But when we broke the evaluation down into things that can be verified, like whether the code compiles, the model ranking flipped, so the only help against length is to move everything verifiable into deterministic checks.

**27:12** · If we compare pairwise, we swap the answers. This is against position bias.

**27:17** · Always pick a judge from a different model family. Keep the scale short. I use a scale of one to four. 1,000 evaluations cost from half a dollar on cheap models to 20 dollars on expensive ones. Furthermore, there is a human overseeing our judge. Once a print, we take 20-30 random sessions from production and label them according to a written rubric. Part of these sessions are labeled by two humans, and we measure the same kappa under them.

**27:41** · how much people agree with each other.

**27:43** · And we can calibrate our judge using these labels. Calibration means we run our judge on the same sessions that humans labeled and compare them. For example, suppose the judge consistently gives a four where humans give a two.

**27:57** · Then we tune the prompt, adjust some rubric, and run it again. We explain to it that this is what a two looks like, and this is what a four looks like. And we keep cycling through this until the data between the humans and our judge converges. However, humans can also label things incorrectly. Annotators often penalize responses with disclaimers, while users rely on the model's answer regardless of disclaimers. So human labeling is also noisy. And unfortunately, there is no final authority here. An agent judge resolves some of the judge's problems.

**28:29** · It doesn't just look at the request log ; it's a separate agent. It has its own tools and its own cycle. It can not only read the log output but also execute code. Call APIs. It checks what a specific tool returned itself. On the DFI benchmark, such a judge outperformed a regular LLM-judge and reached human-level reliability. Take our refund agent: a regular judge reads the log and sees that a refund was issued. But it doesn't check if the correct amount was recorded in the database.

**28:58** · An agent judge, however, will go into the database or call our admin tools and see if it matches or not. It is, of course, much more expensive than a regular judge, as it has a longer cycle, more tools, access to more places, and gathers more information; it needs maintenance, but it provides higher quality than a simple judge that only looks at the result. You can also pair this judge with a critic agent.

**29:23** · The agent answers, the critic writes what's wrong with the answer, and the judge provides an assessment taking the critique into account. In May of '26, researchers showed that a single critique provides almost all the benefits of multi-round model debates, but at a lower cost. But this critic certainly doesn't eliminate the need for humans over the judge. And from time to time, we will need to calibrate our responses with our judge. What should you do if a live model test fails every other time? Is it a regression or is it noise? We once had a regression like that. After an edit, two checks on reply repetition started looking at different things.

### Регрессия или шум. Откуда брать тест-кейсы

**29:55** · One looked at the whole text, the other only at the framing. And a normal reply would sometimes be rejected. We ran each version 14 times. Before the edit, there wasn't a single failure. After that, about every third run would fail, and after the next fix, more than half.

**30:12** · You definitely can't catch this with a single run. But when we fixed it, we ran it 30 times in a row, and there wasn't a single failure. Since then, our rule is: the suite affected by the fix is run 20 times, and the regular smoke test is run five times per PR.

**30:25** · Only a pair of versions will help us understand if it's a regression or just noise. We run the same set of inputs on the old version. This will be our benchmark, our baseline, compared against the new candidate at the same time. If the benchmark also fails intermittently, it's most likely noise.

**30:39** · And such a test needs to be moved to a separate list for review so it doesn't keep marking our PRs as failed. But if the benchmark passes all runs while the candidate passes none, that's definitely a regression. And we compare each task against the baseline. You can't trust the suite average here. A single broken task gets lost in it and just looks like a bit more noise. For the smoke suite, I take up to ten of the most critical tasks and run each five times. The PR is red if a task scored zero out of five, while it scored five out of five on main.

**31:06** · Now about the cost, because you'll be asked : a pair is two runs per PR—the benchmark and the candidate. You don't have to pay double. The benchmark on main rarely changes. So we run it once a day, save the results as a CI artifact, and compare the PR against that. Yes, in 24 hours, the provider might change something underneath us.

**31:25** · That’s that same silent update from the block. In my experience, this happens very rarely. And to catch it, we can run our regression suite. We take the test cases from a failure taxonomy, that is, from the analysis of real failures. It's useless to just make them up. I've tried, and it didn't lead to anything good. Hamel Husain and Shreya Shankar have trained over 2,000 engineers and product managers in this process. Hamel Husain wrote: "Remove everything that prevents you from looking at the data." So, we open 100 agent logs from prod.

**31:57** · A Google Sheet with three columns is enough. We'll have a trace ID, a tag, and one line for notes. We mark every failure with a short tag. Wrong tool. Hallucination, policy lost context on the fifth turn.

**32:09** · After the first few dozen logs, we group the tags into categories. From each, we extract three or four specific cases. And there you have your complete dataset. When should you stop? Husain says: when new logs stop providing anything new. 20 real inputs from prod or the failure taxonomy we just put together. Each input is a customer request plus the expected set of tools, plus the expected result. It will probably take half a day to put this together. But without it, we have nothing to run any tests on. Our usual CI/CD breaks on these features. The answer varies from one run to another.

**32:40** · Everything might crash silently. And each run also costs money. No matter which tool we choose, we need tracing because they all run on top of agent logs. If there isn't a full log yet, we need to enable that logging. A full log is the client code, all tool calls with arguments, all model responses, and tokens. We only have one small block left to discuss. Those very variations that are not included in the N to the power of K set. And this is called metamorphic testing. And we don't necessarily need to know the correct answer here. It is enough to know how two runs should relate to each other.

### Что ещё ломает агентов: от перефразировок до суда

**33:12** · We rephrased the request. We rearranged the documents in the context or asked in a different language, and the agent should call the same tool with the same arguments. That is, once we have formed our test set, we can simply add three paraphrases to each and check that the set of tools has not changed and that the parameters passed remained exactly the same as they were. Models are learning to recognize that they are being tested.

**33:40** · So, a passed eval no longer means the model is behaving as it should. Perhaps it just learned to recognize that you were testing it.

**33:49** · There is another problem when the model finds a shortcut to the metric, but might not even recognize the fact that it is a test. In May 2026, the Higher Regional Court of Hamm in Germany examined such a case. An aesthetic medicine clinic had a chatbot on its website. The bot told clients that the clinic's directors were specialists in plastic and aesthetic surgery. They didn't have that qualification, and the two specialties the bot named don't even exist. It just made them up.

**34:15** · According to the court's decision, a chatbot is a company tool, and its words are attributed directly to the operator. Whether the model hallucinated or processed correct data incorrectly, the court doesn't care.

**34:26** · And the fact that the bot was fed only correct data doesn't save it. The operator is obliged to verify before launch that the bot isn't lying about qualifications. The decision is not yet final, but it is already clear where the courts are heading. And, in my opinion, this company did not conduct proper testing of its agents, because at a minimum, these should be tests for answers the company is responsible for, like qualifications, prices, and guarantees. Judging by the invented specialties, the clinic didn't have such testing. That is why developing evals is incredibly important.

**34:52** · A court decision can depend on whether we chose a bad model that hallucinates or failed to test it, and it went and looked at our old memory. There is also a very large block regarding testing our agent for security. Whether it is possible to extract any personal data through it or break something. We will cover this in one of the following videos when we talk about agent security and how we can achieve a reasonably high level of assurance that our agent won't leak all our company's information elsewhere.

**35:19** · At the same time, everything we have talked about so far tested the agent against healthy infrastructure.

**35:26** · Provider APIs might return timeouts, hit rate limits, or change the response format. Testing against such failures is called chaos engineering. That is, we break the infrastructure around the agent on purpose. In January of this year, AI-Yuzhgb assembled the Reliability Bench. It feeds the agent four types of failures. These are API timeouts, rate limits, and partial responses. Or when the schema shifts; they ran more than 1,000 episodes there . Of all the failures, the rate limit hits the hardest. Success with it is 2.5%lower than with a mix of failures.

**35:57** · And if you rephrase the tasks themselves, success on the first attempt drops by almost nine points. In August, Agent-Chaos was released. It was accepted at ICSE. The authors intercept HTTP between the agent and the LLM API and break the response on the fly. They do not touch the agent's code at all. Either the API doesn't respond, part of the response is missing, or the response arrives fully but the values are corrupted. The share of tasks solved on the first attempt drops by up to 50%due to this. And such tests can immediately show us the bottlenecks in our agent.

**36:28** · For example, if there is no retry logic in our harness, this will surface in the very first run. Therefore, it is possible to test our agents from absolutely different angles. So, Eval is not just some number. Eval is a system. In the beginning, I said that an agent is four objects of testing. Our wrapper, the model, memory, and tools. And each of them can break in a slightly different way. And understanding what works and what doesn't is only possible when we test them separately.

**36:54** · Therefore, the sooner you start implementing a measurement system for your agents, the better your agent will perform in production. And you are also unlikely to end up in a strange situation with a court that will tell you, "Your agent invented non-existent professions," or perhaps your agent will offend the feelings of believers—who will be responsible for that? Therefore, test, verify, and tune your agents so that they work well in production and you won't be ashamed of them. Good luck.

**37:21** · Bye.