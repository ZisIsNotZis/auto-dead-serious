# Remote coordination

Load when:
- The user requests remote coordination or an external writer is known to share state. On first discovery, stop competing writes and apply collision safeguards immediately; update shared `WORKSPACE.md` only after ownership is established. A configured remote alone is insufficient.

Do not load when:
- Coordination is local and no external writer is known, including isolated local subagents.

Applies while:
- Writers may race on shared branches, tickets, handoffs, or tracker state.

Exit when:
- Shared state is synchronized and ownership released; return to local mode only when no external handoff remains.

## R-REM — Shared-state safety

**R-REM.1 — Establish ownership.** Identify a shared record and synchronization method with the other writer before claiming work; changing local `WORKSPACE.md` alone is not a lock. Claim exclusive ownership from fresh shared state and begin shared writes only after the claim succeeds. If no reliable shared record or agreement is available, avoid competing writes and surface the concrete blocker. A stale owner's work is not free to take without an authorized, recorded transition.

**R-REM.2 — Isolation and handoff.** Use separate branches or worktrees. Publish shared tracker changes from a clean checkout without disturbing implementation state. A handoff names owner, branch/revision, completed evidence, remaining work, blocker, and next action, then releases ownership.

**R-REM.3 — Races.** Fetch and inspect shared changes at ownership and publication transitions; update with normal fast-forward and push, never force-push shared state. On a rejected write, refetch and compare ownership and touched files; retry only after resolving the race, not blindly or after a sleep.

**R-REM.4 — Observation.** Prefer notifications; otherwise check at bounded transition points while remote work is active. Each wait needs a deadline and observable state change. Do not poll a remote merely because one is configured.

**R-REM.5 — Optional allocation.** If shared numeric ticket IDs exist, allocate from current shared state and check collisions before publication. Use a formal tracker only if the project has one, mapping ownership and status to its native fields rather than creating parallel ceremony.
