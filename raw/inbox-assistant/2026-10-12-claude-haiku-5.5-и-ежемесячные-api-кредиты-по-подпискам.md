---
source: ai-assistant #73
type: url
captured: 2026-10-12 10:23:15
via: "сводка обсуждений"
url: "https://www.anthropic.com/claude-haiku-5-5"
---

# Claude Haiku 5.5 и ежемесячные API-кредиты по подпискам

В посте сообщается о Haiku 5.5: примерно на 75% дешевле Haiku 4.5, с настраиваемой глубиной рассуждений, рассчитана на быстрые задачи и роль субагента. Кэширование Sonnet 5.5 подешевело вдвое, а подписчики получают ежемесячные API-кредиты: Max 5x $100, Max 20x $200, Team до $500 на пользователя. В обсуждении один участник утверждает, что кредиты работают только для облачных сессий через GitHub, а другой считает сравнения с конкурентами спекуляцией на тестах по токенам. Независимых проверок в чате нет.

Найдено в обсуждении практиков вайбкодинга, 09.10.2026. Пересказ без цитат и без привязки к источнику обсуждения.

## Introducing Claude Haiku 5.5

https://www.anthropic.com/claude-haiku-5-5

Introducing Claude Haiku 5.5: the cheapest, fastest, and most capable small model we’ve ever released.
Claude Haiku 5.5 is designed for high-volume, cost-sensitive tasks. It reliably handles quick and repetitive workloads (like summaries, compactions, database queries, and classification requests). It pairs well with Opus 5.5 and Sonnet 5.5 as a subagent on coding work. And, since it’s also our fastest model to date, it works especially well for speed-sensitive tasks like live customer support and browser use.¹
Haiku 5.5 is available at a much lower price than Haiku 4.5. On average, it now costs around 75% less to run.²
Along with this launch, we’re making improvements to the value of our model range. We’re halving the price of Claude Sonnet 5.5’s cache reads, which means Sonnet 5.5 now runs around 20% cheaper on most agentic work. And we’re introducing a new monthly API credit for our Claude Max and Team subscribers, designed to support our users in building new agents and applications that run on the Claude Platform.
Performance
Here’s how Claude Haiku 5.5 performs across a range of benchmarks:
| Haiku 5.5 | Haiku 4.5 | GPT-6 Luna | Sonnet 5.5For reference | |
|---|---|---|---|---|
| Knowledge workGDPval-AA v2.1 | 1620 | 735 | 1437 | 1840 | 
| Knowledge workAA-Briefcase v1.1 | 1578 | 614 | 1336 | 1824 | 
| Computer useOSWorld 2.1 | 72.4%Offline subset | 15.7%Offline subset | 48.9%Offline subset | 83.9%Offline subset | 
| Multidisciplinary reasoningHumanity’s Last Exam | 45.9%no tools | 10.2%no tools | — | 56.9%no tools | 
| 57.4%with tools | 18.7%with tools | — | 64.5%with tools | |
| Agentic codingTerminal-Bench 4.0 | 39.2% | 0.0% | 16.4% | 70.6% | 
| Agentic codingFrontierCode 1.1 (Main) | 46.4% | — | 42.4% | 52.1%Xhigh | 
| Visual reasoningChartography | 46.4%no tools | 6.4%no tools | 29.1%no tools | 61.6%no tools | 
For details on how we run our evaluations, see the Haiku 5.5 System Card.
Haiku 5.5 is our first Haiku-class model to come with an adjustable effort setting. This means that, as with our other models, users can decide whether to optimize for cost or intelligence. The charts below show how Haiku 5.5 performs on three benchmarks at each effort setting:
In early testing, our customers reported results consistent with the performance and cost improvements shown above. Here’s what they told us about the new model:
Pricing
The table below shows how Claude Haiku 5.5’s pricing compares to our other models. Haiku 5.5 is especially good value when used for tasks with prompts up to 100,000 tokens, which make up around 90% of requests to our previous Haiku model.
| Price per 1 million tokens | Haiku 5.5 prompts up to / over 100k | Haiku 4.5 | Sonnet 5.5 | 
|---|---|---|---|
| Cache reads | $0.01 / $0.05 | $0.10 | $0.10 | 
| Cache writes | $0.125 / $0.625 | $1.25 | $2.50 | 
| Input tokens | $0.10 / $0.50 | $1.00 | $2.00 | 
| Output tokens | $0.50 / $2.50 | $5.00 | $10.00 | 
Safety
Alignment. Claude Haiku 5.5 shows major improvements across almost all of our alignment evaluations relative to Haiku 4.5. In particular, we found far fewer instances of misaligned behavior, and a lower willingness to cooperate with misuse. The model’s system card describes our evaluation process and results in more detail.
Safeguards. Consistent with its capabilities, Haiku 5.5’s cybersecurity safeguards are more restrictive than Haiku 4.5’s, but somewhat less restrictive than those we’ve applied to other recent models. In cybersecurity, they permit a wider range of defensive tasks than our safeguards for Sonnet 5.5, but they still block penetration testing and other techniques more likely to be used by attackers.
Haiku 5.5’s biology safeguards are the same as for Sonnet 5, Sonnet 5.5, and Opus 5. They allow research biology questions but restrict access to requests that we judge as likely to cause harm. Organizations working on wider-ranging biology and cyber activities can apply to our Life Sciences Verification Program and Cyber Verification Program.
Availability
Claude Haiku 5.5 is available now on all platforms, including Amazon Web Services, Google Cloud, and Microsoft Azure. On the Claude Platform, developers can get started with claude-haiku-5-5. 
See our migration guide for details.
Further updates
Alongside our new pricing for Claude Haiku 5.5, we’re making further improvements to the value of our models and products.
First, starting today, we’re lowering the price of cache reads on Claude Sonnet 5.5. Cache reads now cost 50% less: $0.10 per million tokens rather than $0.20. Because cache reads make up a large share of models’ token consumption, this reduces the cost of Sonnet 5.5 on most agentic tasks by around 20%.
For instance, here’s what the price cut means for Sonnet 5.5’s performance relative to cost on Terminal-Bench 4.0:
This chart illustrates an important difference between Haiku 5.5 and our larger models. Sonnet 5.5 and Opus 5.5 remain better choices for complex agentic coding tasks like those measured by Terminal-Bench 4.0. By contrast, Haiku 5.5 is best suited to more narrowly scoped tasks that might otherwise have been cost-prohibitive with previous versions of Claude—like compaction, summarization, or subagent work.
Second, this week, we’ll roll out a new monthly API credit to all Max and Team subscribers for use on the Claude Platform. Max 5x users will get $100 in credits per month, Max 20x users will get $200, and Team subscribers will receive up to $500, pooled across their users. These credits are designed to allow our users to experiment with building tools, apps, and agents that call our API. They can be used on any of our models. For more information, see our Help Center article.
For developers, we’re also updating our Claude Python and TypeScript SDKs to add support for computer use and browser use in beta. Haiku 5.5 is especially well-suited to these tasks, given its combination of speed, capability, and price. You can read more about this in our Claude Platform docs.
Footnotes
1 Claude Haiku 5.5 is our fastest model to date at each model’s standard speed, although it runs less quickly than our Opus models in Fast Mode.
2 Claude Haiku 5.5 is priced 90% lower than Claude Haiku 4.5 for requests up to 100,000 tokens, and 50% lower for requests over 100,000 tokens. On Haiku 4.5, 90% of requests fell into the former category. This calculation also accounts for changes between Haiku 4.5 and Haiku 5.5 in how many tokens are used to complete a given piece of work: Haiku 5.5 has an updated tokenizer (similar to Sonnet 5.5’s and Opus 5.5’s), which means it uses slightly more tokens per task.

## Monthly API credits for Max and Team plans | Claude Help Center

https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans

Max and Team plans include monthly credits for the Claude Platform. Use them to build Claude into your own apps and agents with the Claude API. This article explains who's eligible, how to claim your credit, what it covers, and what happens when it runs out.
Available on Max and Team plans, including discounted Team plans. Free, Pro, and Enterprise plans aren't eligible.
Monthly credits by plan
| Plan | Monthly credit | 
| Max 5x | $100 | 
| Max 20x | $200 | 
| Team (Standard seats) | $20 per seat* | 
| Team (Premium seats) | $100 per seat* | 
| Discounted Team plans (Nonprofit, Scientists) | $20 USD per Standard seat and $100 USD per Premium seat* | 
* On Team plans, credits for all seats are pooled into one monthly balance, capped at $500. For example, a team with three Standard seats and two Premium seats receives $260 a month. The pool is calculated from the seats on the plan when the credits are granted.
Eligibility
- Active plan. Your Max or Team subscription must be active and in good standing. 
- Seven days on the plan. New subscribers can claim once they've been on an eligible plan for seven days. 
- Mobile subscriptions. You can subscribe on the web, iOS, or Android. Claim your credits on claude.ai in a web browser. 
- No payment method needed. You don't need to add a card on Claude Platform to claim or use the credit. 
How to claim your credit
To claim your credit, you link a Claude Console organization to your plan. Credits go to that organization each month.
Before you begin, you need:
- On your Claude plan: Max: be the subscriber. Team: be a Primary Owner or Owner 
- In the Console organization: the Owner, Admin, or Billing role. If you don't have a Console organization yet, you can create one during the claim flow or at platform.claude.com. 
To claim your credit:
- On claude.ai, go to Settings > Billing as a Max subscriber or Organization settings > Billing as a Team Owner or Primary Owner. 
- In the API credits section, select "Link organization." 
- Choose the Console organization you want to receive the credits, or create a new one. 
- Review the Supplemental Credit Terms, then Link organization. 
Your credits appear in that organization's balance, ready to use.
Important: You can link only one Console organization, and each Console organization can receive credits from only one plan. You can't change the linked organization yourself, so choose the one you plan to build in. To change it later, contact support.
Tip: Sign in to the Claude Console with the same email you use on claude.ai. If you’re seeing errors during the linking flow, please try again in a few hours.
What the credits cover
The credits work with any available Claude model on the Claude Platform, including:
- The Claude API (Messages API and Message Batches API) 
- The Playground in the Claude Console 
- Claude Managed Agents 
- The Claude Agent SDK 
The credits don’t apply to:
- Interactive Claude Code in the terminal, IDE, desktop, or web 
- Extra usage in Claude, Claude Code, or Claude Cowork 
- Claude on Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry 
How the credits work
- Refreshes each billing cycle. New credits arrive shortly after your plan payment goes through. On annual plans, credits arrive monthly. 
- Doesn't roll over. Unused credits expire at the end of each billing cycle. 
- Used first. Your monthly credits are spent before any credits you've purchased. 
- Shared across the organization. Everyone with an API key in the linked organization draws from the same balance. 
- Separate from your plan limits. The credits don’t change your usage limits in Claude, Claude Code, or Claude Cowork. 
- Visible in the Console. All credits appear under Settings > Billing in Claude Console with their amount and expiry date. 
What happens when your credits run out
- If the organization has purchased credits or auto-reload, usage continues and draws from those. 
- If the organization has no other credits, API requests stop until your next monthly credits arrive. Usage is never charged to your Claude plan. To keep going, buy credits or turn on auto-reload in the Console. 
- If your organization is invoiced through Anthropic sales, usage beyond the credits is billed as usual. 
If your plan changes
- Cancel, downgrade to an ineligible plan, or refund. New credits stop. Credits you already have stay usable until they expire. 
- Upgrade from Max 5x to Max 20x. You receive prorated credits right away, then $200 each billing cycle after that. 
- Move from Max to Team. Your Max link ends. A Team Owner or Primary Owner can claim the team's credits once the Team plan has been active for seven days. 
For Team Owners and Primary Owners
One claim for the whole team. One owner links a Console organization and claims the pooled credit, up to $500 a month.
The pool follows your seat count. It's calculated from the seats on your plan each time credits are deposited. For example, a team with three Standard seats and two Premium seats receives $260 a month. Adding another Premium seat would increase the next cycle’s credits to $360.
Control who spends it. Everyone with an API key in the linked organization can use the balance. To limit usage by project or teammate, set workspace spend limits in the Console.
Frequently asked questions
Why can't I use the credits for Claude Code?
The credits are for building your own apps and agents on the Claude Platform. They don't cover interactive Claude Code sessions or extra usage after you hit your plan's limits.
Why don't I see the offer yet?
We’re rolling out API credits over a few days so we might not have gotten to you yet. The offer appears after you've been on an eligible plan for seven days. If you're past seven days and still don't see it, check that you're on a Max or Team plan and that you have one of the required roles. If you think you should be eligible but don’t see the API credits, contact support.
Is this the same as the Agent SDK credits announced in June?
No. That credit isn't available. API credits cover the Claude API, Claude Managed Agents, and the Claude Agent SDK, and you claim it into a Console organization.
Can I split my credits across multiple organizations?
No. Credits go to a single Console organization.
I'm on a Pro plan. Can I get this credit?
No. The credits are available on Max and Team plans only.
Does this cover claude -p ?
API credits cover claude -p and the Claude Agent SDK when you run them yourself with an API key from your linked Claude Console organization, because that usage is billed as Agent SDK usage. When you're signed in with your Claude plan instead, claude -p and Agent SDK usage still draw from your plan's usage limits and don't use your API credits. Runs started by the Claude Code GitHub Action, an IDE extension or the Claude desktop app count as Claude Code usage, so API credits don't cover them, even with -p.
