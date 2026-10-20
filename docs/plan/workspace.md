# Workspace

The workspace is the container repository that pins each project as a submodule. This is its plan; the law itself and its plan live in the `agent-policy` submodule, and the root `AGENTS.md` is a symlink into it.

## Status

- Every submodule is pinned at a commit its remote holds, and every local checkout matches its remote.
- `agent-policy` is infrastructure rather than a project: it is pinned like a child so the law arrives with a clone, but the catalogue does not assess it.
- pathlm is running experiment 2651, so its supervise.out is a live log; the pinned commit is the one its remote holds.
- No worktree registration points at a missing directory.

## Open questions

None.
