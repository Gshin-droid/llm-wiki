---
source: official docs, code.claude.com
urls:
  - https://code.claude.com/docs/en/self-hosted-environments
  - https://code.claude.com/docs/en/self-hosted-environments-quickstart
fetched: 2026-08-10
note: полный verbatim-текст двух официальных страниц документации Claude Code, получен через WebFetch. Раздел "What's new" (whats-new, Week 29 dev digest, без новой недельной записи с 07-17 — проверено тем же прогоном) не относится к этому источнику, зафиксирован отдельно только как факт "нет новой недели" в wiki/log.md.
---

# Self-hosted environments (concept page)

Source: https://code.claude.com/docs/en/self-hosted-environments

Self-hosted environments are in public beta on Team and Enterprise plans and are off by default. See Availability and limitations for the enablement path and what's excluded.

A self-hosted environment executes Claude Code cloud sessions on infrastructure your organization operates. A cloud session is any session that runs somewhere other than the developer's machine: developers start them from claude.ai, the mobile and desktop apps, the terminal with `claude --cloud`, and scheduled routines, and by default they execute on Anthropic's infrastructure. In a self-hosted environment, those same sessions execute inside your network, and the developer experience is otherwise the same apart from the differences in Availability and limitations and the deploy page's known issues.

If your team doesn't use cloud sessions, there's nothing here to configure: sessions in a terminal or IDE always run on the developer's own machine. If you want to run Claude Code on your own always-on machine and drive it from other devices, use Remote Control, which is also available on Pro and Max plans.

## How self-hosted environments work

Self-hosting has three parts:
- **Environment**: a named destination that cloud sessions can be sent to. Your organization creates environments in claude.ai admin settings, and each one groups a set of runners.
- **Runner**: a program running on hosts inside your network. Runners execute the sessions; the idea is the same as a self-hosted CI runner.
- **Session**: one Claude Code task a developer started.

When a developer starts a cloud session, the session-start UI shows an environment picker listing Anthropic-hosted environments alongside any your organization has created. If they choose yours, Anthropic's control plane places the session on your environment's queue, where a runner claims it, clones the repository the developer chose, and starts a Claude Code process on your host to run it. The runner authenticates to your git host with credentials you configure. Sessions reach your internal services from inside your network, and your git host the same way when it's internal; the traffic to Anthropic — queue polling, the session's event stream, and model inference — is outbound HTTPS to api.anthropic.com. Anthropic never connects into your network.

The two Claude Code boxes in the architecture diagram are session processes: one runner executing two sessions at once, up to its configured capacity. A runner serves one user at a time, locking to that user's account when it claims its first session, so checked-out code never mixes between users.

You can start runners yourself and keep them running, or run the autoscaling orchestrator, a second process you host, which starts runners as sessions queue; each runner exits on its own when its work finishes.

## Availability and limitations

- **Plans**: public beta for Team and Enterprise organizations. Off by default; an Owner or admin turns on "Allow self-hosted environments" on the Cloud environments admin page, which requires Claude Code on the web to be enabled for the organization.
- **Zero Data Retention**: unavailable for organizations with Zero Data Retention enabled.
- **Model inference**: sessions use the Anthropic API, and inference can't be routed through Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, or an LLM gateway.
- **Surfaces**: sessions started from Claude Code on the web, the mobile and desktop apps, scheduled routines, and the terminal (`claude --cloud` or a scripted `--environment` dispatch) can run in self-hosted environments. Claude Tag, Claude Security, and Code Review sessions don't route to them yet.
- **Repositories**: sessions check out repositories from GitHub.
- **Billing**: sessions in a self-hosted environment consume your organization's Claude Code usage the same way sessions in Anthropic-hosted environments do.

## Why self-host

Most teams are better served by Anthropic-hosted environments, which need no infrastructure to run or maintain. Self-hosting is for teams whose network, tooling, or compliance requirements call for keeping session execution on infrastructure they control. In exchange:
- **Network access**: sessions run inside your network and can reach internal services, databases, and registries without exposing them to the public internet.
- **Custom tooling**: pre-install compilers, SDKs, and internal CLIs in your runner image so every session starts ready to build.
- **Compliance**: repository checkouts and build artifacts stay on infrastructure you control. Session content still goes to api.anthropic.com for model inference.

## Key concepts

| Term | What it is |
|---|---|
| Environment | A named group of your runners, created in claude.ai settings. Sessions are routed to an environment, not to an individual runner. |
| Environment secret | The single shared credential runners use to authenticate and register with the environment. Shown once at environment creation, labeled "environment key" in the admin UI. |
| Runner | The long-lived process you deploy. A runner registers with the environment, receives a runner token, and polls for sessions. |
| Session | One Claude Code task, started from claude.ai, the mobile app, or another Anthropic surface such as a scheduled routine or an agent. Each session runs as a child Claude Code process the runner spawns. |

In API fields, token claims, and metric names, the environment appears as `pool`, and the environment ID is the `pool_id`.

A runner serves one user at a time. The first session a runner picks up locks the runner to that user, and the runner then runs sessions only for that user, up to a configured capacity. The minimum fleet size is therefore the number of users you expect to be active at once.

## Session lifecycle
1. A runner with free capacity claims the session and holds a lease on it.
2. The runner clones the repository into its working directory and spawns a child Claude Code process.
3. The child streams events back over HTTPS while the runner keeps polling; each poll refreshes the lease and doubles as the heartbeat.
4. If the runner stops polling for about 60 seconds, the server requeues the session for another runner.

## Runner lifecycle
The first session a runner picks up locks the runner to the account of the user who started that session, and the runner runs up to `--capacity` concurrent sessions for that account. What happens once they finish depends on `--drain-grace-sec`:
- **At the default of 0**: the runner exits as soon as its active sessions finish, without polling for more, so the orchestrator you deploy it under (e.g. Kubernetes) can restart it with a fresh disk, ready to serve any account.
- **At a positive value**: the runner keeps polling the locked account's queue for that many seconds before exiting.

This lifecycle isolates each user's checked-out code without requiring the runner to delete disk state between users.

A kill that delivers SIGTERM needs no flag: the runner drains normally. If infrastructure instead destroys hosts at a known wall-clock time without a signal (sandbox lifetime cap, spot-instance reclamation), pass `--retire-at <epoch-seconds>` set a few minutes before that time; at retire time the runner stops taking new work, releases each active session so it resumes on a fresh runner, and exits 0 once all sessions are released. Without `--retire-at`, a signal-less host kill is indistinguishable from a crash — the control plane records a lost worker and the session requeues to another runner.

## Network paths
No inbound connectivity from Anthropic is required:
- **Control plane**: the runner polls api.anthropic.com for work and posts setup-progress/failure events, all outbound HTTPS. Polling doubles as the heartbeat.
- **SCM connector**: the optional orchestrator SCM connector tunnel is the only WebSocket connection.
- **Git**: the runner clones from/pushes to your git host over HTTPS or SSH with credentials your deployment provides, including per-session minted credentials and an optional Anthropic git proxy that routes git through api.anthropic.com instead.
- **Session child**: the child Claude Code process holds the session's event stream to api.anthropic.com, and makes its own outbound calls for model inference and git commands during the session.

Model inference uses the Anthropic API; the session authenticates with an Anthropic-issued, session-scoped OAuth token, so inference can't be routed through third-party providers or an LLM gateway in self-hosted environments. Corporate egress proxies are supported (HTTPS_PROXY/NO_PROXY etc., inherited by sessions from the runner). Session streaming uses server-sent events over HTTPS, so a proxy in the path must not buffer responses.

## What stays on your infrastructure
Repository checkouts, build artifacts, secrets, and any files a session creates or modifies stay on the machines you provision. The conversation itself (prompts, responses, tool results) goes to api.anthropic.com for model inference, and Anthropic stores the session transcript so you can resume the session from another supported surface. Session orchestration, queueing, and the claude.ai interface remain Anthropic-hosted — a self-hosted environment moves session execution into your network, not the control plane.

---

# Self-hosted environments quickstart

Source: https://code.claude.com/docs/en/self-hosted-environments-quickstart

Set up your first self-hosted environment: install Claude Code, create the environment, start a runner, and route a session to it.

A self-hosted environment runs Claude Code cloud sessions on infrastructure your organization operates, executed by runner processes you deploy. This quickstart stands up your first one, the smallest that works: one runner on a single host, running one test session.

## Prerequisites

### Organization and roles
- "Allow self-hosted environments" turned on by an Owner or admin on the Cloud environments admin page (claude.ai/admin-settings/cloud-environments); the "New" button doesn't appear until it is.
- A GitHub connection for your organization, so developers can pick repositories when they start sessions.

### Host and network
- A Linux or macOS host or container with outbound HTTPS to api.anthropic.com, to claude.ai and its download hosts, and to your git host for the clone. Windows isn't supported as a runner host; run the runner in a Linux container instead. Developer workstations aren't affected, since sessions start from claude.ai in a browser.
- A clock synchronized to real time (e.g. NTP). Authentication fails when the clock is more than five minutes off.

### Software on the runner host
- **Claude Code v2.1.224 or later** — the runner is part of the standard `claude` binary; earlier versions don't recognize the `self-hosted-runner` subcommand. The native installer's default `latest` channel carries each release as soon as published; the `stable` channel, Homebrew cask, and stable apt/dnf/apk repos trail by about a week.
- **Git 2.24 or newer**.

Confirm readiness: `claude self-hosted-runner --help` — a ready host prints the runner's usage text (flags such as `--environment-secret-file`). On versions older than 2.1.224 the command prints general `claude --help` instead.

## Set up an environment and runner

Guided setup: an interactive Claude Code session walks through creating the environment in the admin UI, starts a local runner with the saved secret file, confirms registration, and writes a cheat sheet to `./runner-setup/CHEAT-SHEET.md`. Run on a machine signed in via `claude auth login` with an account holding Owner/admin role; not available with API keys or third-party model providers.

```
claude self-hosted-runner setup
```

Manual steps:

1. **Create an environment.** Cloud environments page → admin settings → Self-hosted environments → New → name it → Create. On the wizard's second step, "Copy environment key" copies the environment secret. claude.ai shows the secret once, and it can't be retrieved later; it expires 365 days after creation. The environment's `ccpool_...` ID stays visible in its detail dialog (needed for the `aud` check in token verification and for dispatching test sessions from CI). If lost/rotated, create a new secret from the environment's Configuration tab, roll it out to runners, then revoke the old one — runners holding a revoked secret fail their next authenticated poll and exit, logging `poll auth failed`.

2. **Start a runner.**
```bash
mkdir -p /etc/claude
(umask 077 && cat > /etc/claude/environment-secret)
mkdir -p '<writable-dir>'
claude self-hosted-runner --environment-secret-file '/etc/claude/environment-secret' --base-dir '<writable-dir>'
```
The secret-write command reads from the terminal so the secret stays out of shell history: paste, Enter, Ctrl-D; the subshell's umask makes the file readable only by its owner. `--base-dir` (default `/workspace`) is where the runner checks out repositories and creates per-session directories. If the runner exits, restart it by hand — production deployments run it under an orchestrator that restarts exited runners, normally with a fresh filesystem per restart.

3. **Verify the runner appears.** Cloud environments page: status changes from "No runners deployed" to "Healthy" within seconds; open the environment → Activity to see the runner itself.

4. **Route a session to the environment.** Start a session at claude.ai/code, select the environment from the picker (self-hosted environments appear alongside Anthropic-hosted ones). The runner clones with whatever git credentials the host already has — pick a repository the host can already clone, or a public one. The next available runner picks up the queued session and logs `Picked up session <session-id>` with its active count and capacity.

The runner exits by design once its active sessions finish (see Runner lifecycle). For production, deploy it under an orchestrator that restarts it on exit.

## Send a follow-up message to a running session

From any machine logged in via `claude auth login` (doesn't need to be the machine that started the session):
```
claude -p "your message" --cloud <session-id>
```
`<session-id>` accepts the bare `session_...`/`cse_...` ID or the session's claude.ai/code URL. Success prints "Sent to cloud session." with the session ID and a view link. The command works the same against Anthropic-hosted sessions.

## What's next
- Deploy to production: hardening, egress control, git credentials, Kubernetes/Compose recipes
- Customize sessions: wrapper scripts, lifecycle hooks, on-demand runners, MCP servers, permissions
- Test end to end: CI smoke test dispatching a session and reading Claude's replies
