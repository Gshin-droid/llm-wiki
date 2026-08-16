---
source: официальный CHANGELOG.md репозитория anthropics/claude-code
url: https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
retrieved: 2026-08-16
covers: v2.1.232–2.1.233
---

# Changelog

## 2.1.233

- Added support for GitLab merge request URLs in the `--worktree` flag and agent view displays
- Introduced opt-in `forward_user_identity` setting for tracking per-user spend attribution
- Added memory cgroup support for Linux Bash commands to prevent resource exhaustion
- Made WebFetch session URL cache TTL configurable via environment variable
- Fixed cloud sessions being incorrectly marked as lost during permission prompts
- Resolved MCP v2 connection issues with servers that terminate long-held streams
- Fixed notification hooks not firing for permission prompts in Claude Desktop/VS Code
- Addressed Linux CPU core usage issue when sandboxing is enabled
- Fixed bundled skill aliases reporting "Unknown command" in certain configurations
- Prevented argument value re-expansion in skill/command substitution
- Closed NTLM credential leak vector via Windows NT device paths
- Improved self-hosted runner session startup performance
- Enhanced apps gateway error forwarding for upstream providers
- Expanded `claude plugin validate` to check skill markdown frontmatter
- Improved screen reader mode with numbered effort selector and better text handling
- Added print mode diagnostics for unrecognized models
- Adjusted GitHub app setup tip display logic for non-GitHub repositories
- Restricted task-tracking tools on newer model versions with override option
- Fixed Windows auto mode permission issues with Bash commands
- Reverted 2.1.232 Bash changes for Cygwin symlinks and input redirections

## 2.1.232

- Enabled subagent forking by default with full conversation inheritance
- Added `@` mention syntax for direct cross-session communication
- Improved `SendMessage` delivery to bare session names
- Enforced unique session names with automatic variant generation
- Added configuration rows for dialog expiry and cross-session messaging
- Implemented secret redaction for GitLab token families
- Extended GitLab support to plugin marketplaces
- Provided friendlier aliases for marketplace settings keys
- Enhanced gateway policy support for blocked marketplace URLs
- Expanded Desktop settings validation in gateway overlay
- Added boot-time validation for malformed managed settings
- Restored Fable 5 availability for organizations with access
- Fixed PowerShell variable-writing permission bypass
- Resolved Windows symlink traversal security issue
- Fixed nested repository trust inheritance
- Addressed MCP connection timeout handling
- Fixed Remote Control session authentication and reattachment issues
- Corrected Remote Control history restoration
- Improved cloud gateway login error reporting
- Fixed voice mode connection rejection messaging
- Resolved mTLS certificate rotation requiring restart
- Fixed malformed AWS/Vertex region fallback behavior
- Addressed stream idle timeout on various deployments
- Fixed content-sized overlay rendering issues
- Corrected truncated command preview character display
- Fixed plugin marketplace concurrent registration race
- Resolved `/update` and `/tui` restart blocking
- Improved usage-limit guidance accuracy
- Fixed interactive Fable consent messaging
- Enhanced fullscreen streaming responsiveness
- Improved managed settings approval dialog
- Made `/feedback` and `/bug` open immediately during responses
- Optimized plugin installation marketplace refresh
- Enhanced `/code-review` background execution at higher efforts
- Improved clipboard image handling
- Extended Remote Control reconnection persistence
- Fixed Remote Control multi-device takeover behavior
- Updated agent panel completion display
- Improved Remote Control session status indicators
- Implemented Bash input redirection permission checking
- Refined background agent completion messaging
- Fixed cross-session message handling in cowork sessions
- Hardened cross-session messaging socket directory security
- Strengthened Linux filesystem sandbox protection
- Restricted `sandbox.ripgrep` configuration sources
- Removed outdated subagent creation suggestions

## 2.1.231

(уже отражена в предыдущем снапшоте — [[claude-code-changelog-snapshot-2026-08-13]])
