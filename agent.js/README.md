# agent.js

A coding agent that runs in the browser tab and needs no server: a URL, the user's own token, a workspace in the browser's file system, and a tree of agents that survives the page being killed.

**Not for** anyone who needs unattended runs (close the tab and nothing runs), anyone who needs a real shell today, or anyone who wants us to hold their credential. It is the sibling of `agent.sh`, not a port of it: there the model writes bash and gets a shell; here it writes JavaScript and gets a Worker.

## Status

Not started. No manager, no roadmap, no code. The design was settled in conversation on 2026-10-22 and is recorded in one place: `inbox/2026-10-22-design-tree.md`, which carries the expectation, the branches we walked and rejected, the prior art, and what has to be measured before the first package.

Two gating questions are still the person's, and the degree is recorded as `decide` *assumed* rather than stated. Both are in that message.

## How to start

Read `inbox/` first. Nothing else exists yet.

## How to continue

When a manager owns this directory it writes its own document here and this file becomes the door to it. Until then `inbox/` is the project.
