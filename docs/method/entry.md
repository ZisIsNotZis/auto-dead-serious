# The entrance

A project is entered through one document at its root, so that a layer above it never has to know where that project keeps anything. This is the shape, and the one place it is written down.

## Why a file and not a lookup

The layer above dispatches into a directory. Everything past that door is the project's own business: its plan may sit at `docs/plan/`, at `docs/roadmap.md`, inside a product-shaped subdirectory, or in a ticket series, and the reason is usually history rather than design.

A parent that learns the path has taken on a coupling it pays for on every reorganisation, and it invites the worse failure: a lookup that lands on a historical document which is still well-formed and no longer current. The door is the fix, because the project is the only party that knows which of its own documents are current.

## What the entrance answers

Four things, in this order, and nothing else.

1. **Start.** The command or the entry point that runs this thing.
2. **Continue.** Where the current state lives, and what "next" means in this project's own terms.
3. **Where.** Only the places that differ from the general convention, and what is there.
4. **Not current.** The documents that are historical or superseded, so a reader does not follow a well-formed page into a dead branch.

Where the convention holds, the file stays silent about it. A convention restated is noise that buries the exception, and the exception is the whole reason this file exists.

## The gap today

Of the thirteen projects in the register, one has a `WORKSPACE.md` and it answers two of the four: `learn_draw`. Seven others carry an `AGENTS.md`, which is a copy of a policy and not an entrance. Five carry neither.

So "a child can recover by reading the project" is true for one project out of thirteen, and the gap is not a documentation style question: it is the first package for every project that lacks it, because a contract written without a door is a contract the child will spend its first hour re-deriving.
