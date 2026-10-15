# Mining real lessons out of existing repositories

We are building a general operating policy for agent-driven development. That policy currently
lives in one file, `/home/z/vibe/AGENTS.yaml`, rendered to `/home/z/vibe/AGENTS.md`. It was written
from first principles and from a handful of incidents. The point of this task is the other half:
go into repositories that have already been worked in for months and recover the lessons that were
paid for but never written down.

You are assigned one or more projects under `/home/z/vibe/`. Read what is already written there and
report what would prevent a future agent from wasting the same time again.

## What to extract

Only what is evidenced in the files. Five categories:

1. **pitfall** - something actually went wrong, and what it cost (time, tokens, data, a wrong conclusion).
2. **know-how** - a non-obvious thing that had to be discovered, especially something an agent would
   not know in advance and could not guess.
3. **detour** - an approach tried and abandoned, and why it was abandoned.
4. **project rule** - the project already wrote a rule for itself. A rule someone bothered to write
   down after being burned is the strongest evidence there is.
5. **doc method** - anything about how the documentation itself was organised, kept current, or went
   stale and turned into a lie (a documented command that does not exist, two files disagreeing,
   a status section nobody updates).

## Where to look

Per project, in this order, and stop when you have enough:

- `AGENTS.md`, `CLAUDE.md`, `README.md`, and any `*.md` at the project root
- everything under `docs/` and `doc/`
- `.scratch/` - work records, tickets, decision logs; usually the richest source of pitfalls
- `.wrapup/` if it exists - campaign scripts, logs, notes
- top-level `*.md` and `*.txt` anywhere else in that project

Never walk a repository: no `find /`, no `ls -R`, no whole-repo `grep -r`, no `git log`. Skip
`node_modules`, `.venv`, `venv`, `__pycache__`, `.git`, and anything named `worktrees`. Read each file
**once**, and never re-read or re-grep a file you already hold.

## Judging each finding

Say which of these it is, for every finding:

- **policy candidate** - a rule the general policy looks like it lacks
- **already covered** - name the policy rule that covers it (read the policy once, see below)
- **project-specific** - it only matters to that project

To judge coverage, read `/home/z/vibe/AGENTS.md` **once** (240 lines). Do not read `AGENTS.yaml`, and do
not read anything else directly under `/home/z/vibe/` - other than your assignment and your own report.

## Hard rules

- **Read-only.** Do not write, edit, move, delete or create anything inside the assigned projects.
  Not one byte. Your only write is your own report file. No `git` command that changes state.
- Separate what a file **says** from what you **infer**. Mark inference as inference.
- A finding without a file and a line or heading is not a finding.
- Budget: at most 25 minutes and about 60 tool calls. **Twenty strong findings beat two hundred weak ones.**
- If a project turns out to have nothing worth reporting, say so in one line and move on. That is a
  useful answer, not a failure.

## Output

Write exactly one file, and nothing else: `/home/z/vibe/.scratch/29-lessons/<slug>.md`

Structure it as one section per assigned project, and inside each section one bullet per finding:

```
- [category] path/to/file.md:LINE - one-line quote or close paraphrase - policy candidate
- [category] docs/X.md#heading - ... - already covered by <rule name>
- [category] .scratch/3-thing.md - ... - project-specific
```

End the report with a section `## Top 5 by value` - the five findings most worth putting into the
general policy, one sentence each on why.

Then reply to me with at most six lines: your slug, the projects you covered, the count of findings
per category, and your top three findings.
