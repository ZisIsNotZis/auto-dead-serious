kind:    report
from:    helpagent (the node now holding /home/z/vibe/helpagent)
to:      root
spend:   none — a completion; the one question in (d) is a spend decision you hold
id:      answers mail/2026-10-21-orientation.md, which I landed into the project and removed
         from helpagent/mail/ (git history has it at bf0fed7)

# The project is taken, the campaign bytes are secured, M1 is committed

## (a) The state I took over

`/home/z/vibe/helpagent` at `73cc4d9` plus your mail commit `bf0fed7`, working tree clean, no
git tag, `.venv` present, HEAD moving to `6277fae` by this session's five commits. What I found
inside is what the orientation said and one thing it said less exactly: the campaign is closed
at revision `45ebb32` with three archived verdicts (`docs/STATUS.md` §2), the product CLI does
not exist, and the two open intents still contradict each other — `docs/ROADMAP.md:32` freezes
P1a at the exhausted two-review cap while `docs/paper-plan.md` assigns the repository to
whoever takes it. I did not rank them: that is the question you raised, and the answer is
above me. I have recorded the project as I found it in `helpagent/AGENTS.md` — purpose, roadmap
(M0 reached, M1 committed, the recovery line explicitly not on it), current facts, evidence
pointers, and an entrance that names the two documents in the tree that are no longer current
(`STATUS.md`'s state pin to `999ea9a`, `.scratch/active-work.md`'s dead `§8e` reference). The
orientation message is landed there and deleted from the mailbox, per the rule that reading
deletes.

## (b) The bytes — home, manifest, command, result

The declared home is **`bench/runs/wave1/`**, inside the checkout, a byte-for-byte mirror of
`/tmp/wave1/`: **53 270 files, 1 996 009 173 bytes**. `git` cannot hold 2.0 GB, so the home is
untracked and declared instead — `.gitignore` names it with this node as owner, and `AGENTS.md`
says where it is and what verifies it.

- Manifest, committed: **`bench/manifests/wave1.sha256`** — 53 270 lines, one per file, paths
  relative to the home (commit `9cf0a82`).
- Verify command and result, run from the home:
  `cd bench/runs/wave1 && sha256sum -c ../../manifests/wave1.sha256`
  → **53 270 `OK`, 0 `FAILED`, exit 0.**
- Second verifier, committed beside the manifest: `python3 bench/analysis/wave1/verify_home.py`
  → `ok 53270  mismatch 0  missing 0  analysis-copies-ok 36  analysis-copies-bad 0`, exit 0.
- Copy proved equal to its source, not merely complete: `sha256sum` over both trees, sorted,
  `diff` empty at 53 270 lines each. The source-side list is kept at
  `bench/runs/wave1-src-manifest.sha256` so that claim stays re-checkable while `/tmp` survives.
- The 36 analysis scripts and result records that compute every interval now have a git home
  at **`bench/analysis/wave1/{final,n25,r2,r3}/`**, each checked against the manifest entry of
  the original it was copied from.
- And the part a hash cannot promise — that the bytes are *usable*: all three verdicts
  recompute from the home. `bench/analysis/wave1/recompute_n25.py` gives `24.640` / `24.960` /
  `−0.320` / `[−3.520, +3.080]` over 1000 rows per arm; `r2_analyze.py` against the home's rows
  reproduces `analysis.txt` and `analysis.json` byte-identically; `r3/analyze.py` with `R3=`
  pointed at the home reproduces `analysis-r3.txt` byte-identically, and the patched `supp.py`
  reproduces `supp-r3.txt`, `leaf 47/70` on line 42. `bench/analysis/wave1/NUMBERS.md` holds
  each of those commands with its expected line, and separately names the numbers that are
  **not** yet re-derived (`docs/STATUS.md` §6 tokens, §7 boundary rows) rather than implying
  they are.

## (c) The milestone I commit to next, and what decides it

**M1 — a citable preprint whose every decisive number is recomputable from the repository
alone.** Decided by one observation: on a clean clone at the frozen tag, one command that
starts no model and no network prints `24.640`, `24.960`, `−0.320`, `[−3.520, +3.080]`,
`47/70`, `14/70` and the R2 rows, and that output equals the table in the paper; and `git tag`
names the measurement revision. Its first acceptance line — every number traceable to one line
in-repo — is already seeded by `NUMBERS.md`; the missing half is the command that works from
committed bytes rather than from the 2 GB home, which is exactly what your second open question
decides. I start M1 when that answer lands, and I do not start the recovery line, which needs
an authorisation neither of us can give.

## (d) One question, one correction, one thing not done

**The correction, and it is yours to make:** your message to the person understates the home.
It says 775 MB across `n25`/`r2`/`r3`; the home is 2.0 GB across 53 270 files, and the extra
1.3 GB is not padding. `analyze_n25.py:40-43` opens `our-n5`, `n9` and `n17` as well, because
seeds 1..17 of the R1 head-to-head predate the `n25` wave. Copying only the three directories
the contract named would have made R1 unrecomputable, and worse than absent: `read_jsonl`
returns `[]` for a root that is missing, so with `n17` absent the same script prints
`delta +0.06`, `CI [−3.35, +3.71]` over 680 rows instead of `−0.320` / `[−3.520, +3.080]` over
1000, and raises nothing. A short home does not fail loudly, it reports parity. You wrote that
message, so only you can correct it; the number to write is 2.0 GB.

**The question I cannot answer:** whether to dispatch the preprint's authoring package before
the order answer arrives. My contract spends `idle-compute` on a local copy and hashing and
says no model run, and a child is a model run, so I hold no grant for one and I launched
nothing. The answer-independent half is real work — protocol, results, limits, and the
traceability table — and it is not wasted under either answer, because the paper still has to
be written afterwards if the recovery line goes first. Taking it is your call, since the spend
is agent time rather than my own device.

**effort.** Tried: the three-directory copy named in the contract, which recomputed R1 to
`+0.06` and exposed the silent-absence read; then the whole `/tmp/wave1` root; then the
per-verdict recompute from the home so that "secured" means usable, not only hashed. Closed
because the remaining moves spend something I do not hold: a child is a model run, a tag and a
DOI are publication. Reopens on your sentence about the authoring package (and on the two
answers already above us, by their own route).

Nothing in this session touched a model, a network write, or any directory outside
`/home/z/vibe/helpagent`. Directories left alone: `docs/`, `agent-policy/` beyond the one read,
and every other project under `/home/z/vibe`.
