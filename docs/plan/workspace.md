# Workspace

The workspace is the container repository that pins each project as a submodule. This is its plan; the law itself and its plan live in the `agent-policy` submodule, and the root `AGENTS.md` is a symlink into it.

## Status

- Every submodule is pinned at a commit its remote holds, and every local checkout matches its remote.
- `agent-policy` is infrastructure rather than a project: `scripts/catalogue.py` declares it in its registry, so the pin carries the law like a child while the catalogue assesses no such thing.
- Two submodules are mid-experiment, so their checkouts move while their remote already holds the commit each is pinned to. Which two, and what they are doing inside, is theirs to say and not this file's to describe.
- No worktree registration points at a missing directory.

## Open questions

None.
