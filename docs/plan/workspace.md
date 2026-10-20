# Workspace

The workspace is the container repository that pins each project as a submodule. This is its plan; the law itself and its plan live in the `agent-policy` submodule, and the root `AGENTS.md` is a symlink into it.

## Status

- Every submodule is pinned at a commit its remote holds, and every local checkout matches its remote.
- `agent-policy` is infrastructure rather than a project: `scripts/catalogue.py` declares it in its registry, so the pin carries the law like a child while the catalogue assesses no such thing.
- pathlm is running experiment 2651, so its supervise.out is a live log; the pinned commit is the one its remote holds.
- No worktree registration points at a missing directory.

## Open questions

None.
