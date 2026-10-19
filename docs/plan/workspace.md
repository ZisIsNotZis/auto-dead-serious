# Workspace

The workspace is the container repository that pins each project as a submodule. This is its plan; the policy's own plan is policy.md.

## Status

- Six submodule pointers are committed at commits their remotes already hold: agentic-animation, dojo, learn_draw, murderMysteryGame, pathlm and sys_gal.
- Four submodules stand on local-only commits, with no remote branch containing them, so their pointers are uncommitted: autofe, flashdb, helpagent and litellmgen. The workspace tree therefore shows exactly those four paths.
- Stale worktree registrations whose directories were already gone are pruned: 32 in autofe, 33 in flashdb, 4 in sys_gal and 1 in agentic-animation.
- autofe's worktree holds 77 uncommitted or untracked paths and pathlm's holds four modified log files; both belong to their own project and do not enter a workspace commit.

## Open questions

- May the four local-only masters be pushed, so their pointers can be pinned and the workspace tree becomes clean? Pushing publishes whatever those branches hold, so it waits for consent; recommended wherever the remote is private.
