kind:    direction
spend:   taste
from:    root
to:      person
id:      raised from `agent.js`'s design record of 2026-10-22

Two questions about what the browser-side agent is allowed to promise. Neither is
a detail its manager may take under `decide`, because both change what the
product claims and therefore what the first contract's acceptance can say. Say
one word each and the manager starts with the answer in hand; leave them and the
project sits at the door.

**1. Durability: installed app only, or a plain tab as well?**

- **Installed only** (Chrome install, Safari add-to-home-screen). Then "close it
  and reopen it and the whole tree resumes" is a promise we can keep: Safari's
  7-day wipe of script-written storage exempts installed apps, and Chrome grants
  persistent storage to installed ones. The cost is one sentence in the product
  — "add it to your home screen".
- **Plain tab as well.** Then we must tell people that a browser may delete their
  workspace after a week of not touching it, and the storage work grows: an
  export path and a mirror to the user's own git remote become part of the first
  milestone rather than a later one.

I recommend the first. It is honest, it costs no engineering, and it converts
the "keep this tab open" instruction into something the user can actually do.

**2. Execution: "runs your JS/TS in the tab", or "runs anything"?**

- **JS/TS only.** Compile with a WebAssembly build of esbuild inside a Worker and
  run it there. No licence, no shell, no server, milliseconds per call. It covers
  the web-app class of work, which is the class this product is for, and it is a
  claim we can defend.
- **Anything.** Real `npm install` in the tab means a licensed runtime
  (WebContainers: paid for commercial use, and it needs cross-origin isolation
  headers), and everything else — a Rust build, a CUDA job — means shipping the
  workspace to a machine we pay for, which is a price shown at the call site.

I recommend "JS/TS only" as the promise and remote compute as the named
exception, because "runs anything" is either a licence or somebody else's
invoice, and neither fits "all our side pays is a CDN".

## effort

Both are one line to answer and are recorded here because the first contract's
acceptance line depends on them. The design record that raises them is
`agent.js/inbox/2026-10-22-design-tree.md`; the answer changes nothing about the
core architecture, only what the first milestone promises and what it may skip.
Nothing is running, so nothing waits on the answer today.
