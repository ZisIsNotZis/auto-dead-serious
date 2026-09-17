# Remote coordination

Load when:
- Only when `WORKSPACE.md` records remote mode because the user requested it or another external writer is known to share the branch or repository; a configured remote alone is insufficient.

Do not load when:
- Coordination mode is local, including multiple local subagents working in isolated worktrees.

Applies while:
- External writers may race on shared branches, tickets, ordinals, handoffs, or tracker state.

Exit when:
- Required shared state is synchronized and ownership released; unload for later work only after `WORKSPACE.md` records local mode and no external handoff remains.

## R-REM — Remote coordination

**R-REM.1 — Ownership and locks.** Record exclusive ownership in the shared ticket or tracker before work starts. Acquire from freshly fetched state, update status and owner, and begin only after the shared write succeeds. A rejected update triggers refetch and state inspection, not blind retry or sleep. If another owner won, leave a concise handoff or dependency note and switch work. Treat stale ownership as a user-visible risk; takeover requires explicit authority and a recorded transition.

**R-REM.2 — Isolated worktrees and handoff.** Each writer uses an isolated checkout, branch, or worktree. Shared ticket state is written from a clean main-capable checkout without disturbing implementation work. Handoff records branch or revision, status, completed evidence, remaining work, blocker, and next step, then releases ownership. When no network remote exists but writers share a filesystem, a local bare repository may provide synchronization; without shared state, use the core serious-blocker gate.

**R-REM.3 — Synchronization.** At ownership and ticket transitions: fetch, inspect arrived shared-state changes, fast-forward from the shared branch, edit, commit, and push normally. Never force-push or auto-rebase shared state. A non-fast-forward rejection is a race signal: refetch, compare ownership and touched files, resolve from original intent, and retry only when disjoint or explicitly reconciled. Reads may use remote refs without altering the active checkout.

**R-REM.4 — Bounded observation.** Prefer event notification. Otherwise poll only while remote work is active and at bounded transition points or a documented interval, recording the last observed shared revision. Polling reports new state; integration happens at the next safe point. Every wait has a deadline and an observable state change; do not implement backoff as bare sleeps.

**R-REM.5 — Shared ordinals.** Allocate ticket and feature ordinals from freshly fetched shared state as maximum existing numeric prefix plus one. Before publishing, detect duplicates. On collision, refetch and either join the same work or renumber the later unrelated item, repeating until the shared tree is unique. Add persistent allocation tooling only when recurrence justifies it.

**R-REM.6 — Tracker mapping.** Use a formal tracker only when the project actually has one. Map ticket status, owner, and handoff to its native state and assignee fields; keep local files only when they are the declared record or needed pre-publication. Do not invent tracker ceremony in a repository that uses local tickets.
