kind:    report
from:    backseat (node owning that project's roadmap; took over at HEAD 4668493)
to:      root
spend:   idle-compute (reading, deciding, one package dispatched; no model call, no GPU, no daemon)
id:      answers your contract "take ownership of the `backseat` project"

**node whose roadmap this changes:** `backseat` (mine) — and one line of it is a `resource` item that is already with the person, not a question for you.
**evidence pointer:** `/home/z/vibe/backseat` @ `4668493`; frozen snapshot `~/backseat-data/snapshots/2026-10-19/backseat.db` (`snapshot_sha256 d007dc75…`, `frames` 26,424 / 1.7 GB / 0 missing); census command in `docs/SCHEMA.md §门槛判定程序`.
**decision needed:** none. One routing request at the end.

## (a) The state I took over

- **Tree:** HEAD `9533708` → my commit `4668493`, working tree clean, 13/13 test files green (`docs/RUNBOOK.md` loop, 12 s). The evidence drops and the two mail commits you made were already in, so nothing of the last package was left uncommitted.
- **Mail:** all four messages landed here (`orientation`, `answers`, `d1b-ruling` incl. the correction, `m0p-report`) and deleted in the same commit that landed them. The m0p package's three unclaimed items are now claimed: the `labels` line, the switch family, and the prompt-effectiveness question.
- **Repairs are real:** batch window `min/max` over cited observations, switch base frame folded into `obs_ids`, out-of-frame epithet refused and counted, `MANIFEST.frames` binds the pixels. `test_witness_basis.py` still asserts the old formula's failure on the same fixture, so it discriminates rather than comments.
- **One number in the record was wrong, and it propagated into your ruling.** "The 104 inverted windows" is two numbers: **104 rows have at least one reference outside their own window (232 of 27,012 refs)**, and only **12 rows have an inverted window**. `docs/SCHEMA.md` now states both separately, and `scripts/d1_census.py` counts them apart so the conflation cannot recur.
- **I built the gate's judge** rather than leaving the numbers in prose: `scripts/d1_census.py` + `tests/test_d1_census.py` (24 assertions) reports D1 A (missing / out-of-window refs / inverted windows), C1 (marker rows whose `payload.switch_base` is recorded **and** ⊆ `obs_ids`), C2 (rows **reusing** a description word-form with no `payload.cast`), over a judgeable population selected by `--since-msg-id`. Exit 0 clean / 1 defects / **2 = population empty, i.e. cannot be established, not a pass**.
- **Measured on the frozen snapshot:** A refs 27,012, bad ids 0, out-of-window 232 in 104 rows, inverted 12. C1: 10,206 marker rows, **0** recorded bases. C2: 21,867 rows carry a person description, 21,737 of them **reuse** a form seen earlier, **0** attributed — and of those reuses **20,176 skip the immediately preceding row**.
- **Two findings from that census that change the plan, not just the numbers:**
  1. the marker the writer uses (`从…切至`) fires on only **24 of the 50** seed-3371 rows; the wider wording the review counted (`由…切至`, `切换为`, `画面切至`, `相较上一帧`, `仍为`…) fires on **47 of 50**. The write rule cannot cover what its own detector never sees.
  2. the epithet memory is **one row deep** (`state["epithets"]` is overwritten each row), so 20,176 cross-row reuses are unpoliceable. The review's 17/50 is exactly that shape.
- **D1 A and C cannot be judged on the frozen snapshot at all** — its rows were written before the repair and are not backfilled, and the judgeable population is rows written after it. So the gate's mechanical half currently reads "cannot be established", not "failing" and not "pass".

## (b) The milestone I commit to next, and what decides it

**M0′ alone; M1′ does not start.** Its deciding observation is one snapshot taken after a repaired live run, on which:

1. `python3 scripts/d1_census.py --db <new snapshot> --since-msg-id 25900` exits **0** (zero A defects, zero C defects on judgeable rows), while the historic block still reports 104 / 232 / 12 as known-degraded;
2. an independent 50-row D1 B on the same new population is **≥ 95 %** under the citation-scope reading;
3. `witness_cursor == count(observations)` and two replays of the same record agree.

The first two need the model endpoint at `127.0.0.1:4000`, which is the person's. Until it runs, the honest state of the gate is "cannot be established", and I record it that way rather than as a pass or a failure.

## (c) What I cannot answer, with the effort

1. **Five channels or channel A (scope).** Not mine: your `direction` raise to the person is still sitting in your own `mail/` and nothing has come back into `backseat/mail/`. *Tried:* measured that exactly one sensor has ever written (`screen`, 42,396 observations), that `bus.py` has screen kinds only and `SCHEMA.md` marks `atspi/fs/git/proc/input/audio` unimplemented, and that no per-channel exit criterion is written. *Closed:* four adapters plus four exit criteria in one package is a multi-day build whose acceptance nobody can state. *Reopens:* the person's answer.
2. **The endpoint (resource).** Same: your `resource` raise is with the person. *Tried:* none in this session beyond reading the state (the pipeline is stopped at cursor 42,395 / observations 42,396, and the rate of that backlog is one row). *Closed:* `idle-compute` cannot stand in for a model endpoint, and fabricating one would make the gate's numbers fiction. *Reopens:* the endpoint, or a named alternate.
3. **What an uncooperative model costs (not yet a question).** It has not materialised: with the rule enforced, a model that will not fill `cast` costs **refused descriptions**, visible in `payload.epithet_refused` and in `run.log`'s `拒绝落行`, not silent carries. The observation that would turn it into a question for the person is a post-repair day of ≥ 200 rows with refusal rate > 50 % — that would mean the rule is eating the text and the prompt, not the rule, is what must change.

## (d) The four open items, one line each

- **Stricter write rule as a gate item — decided: yes, as D1 C, threshold 0 defects (100 %).** It counts "is the basis inside this row", which has two states; a threshold below 100 % would license exactly the defect the review found. B's 95 % stays a sampling judgement and does not share the threshold. Population: rows written after the repair (`id` > 25900), historic rows known-degraded.
- **Widen `SWITCH_RE` — decided: yes, but to a closed enumerated table, with base selection left bounded** (model-named `since`, else the previous small row), so the cost is at most one extra frame and one frame-interval of window per row. Measured cost/benefit: detector 24/50 → 47/50 on seed 3371; 10,206 marker rows today.
- **The `labels` line — decided: `labels` is not in M0′**, migration authorised for M1′; one line in `SCHEMA.md`, and the channel-B table row's 【待用户确认】 removed so the next reader stops reopening it.
- **What measures the epithet mechanism against a real model — decided: nothing measures the model under `idle-compute`; the mechanism is measured by fixtures, the model by two counters** (`epithet_refused` rows / description-bearing rows, and `拒绝落行`), read over a post-repair day and recorded in `RUNBOOK.md` — diagnostics, not a gate, because it measures cooperation the project does not control.

## Package dispatched (named, with spend and clock)

**BS-M0P-封口** — `worker` `a16ee5ba`, contract in `mail/` when it reports: widen the marker table to the closed families, make the epithet memory cumulative (bounded, persisted in `state`) so cross-row reuse must be re-attributed, record retained attributions in `payload.cast` so C2 is checkable after the fact, with tests that assert the old behaviour too. **spend `idle-compute`; wall-clock 60 min**; write area `backseat/witness.py` + `tests/test_witness_basis.py` only (docs are mine, one writer per area). It reports to `backseat/mail/`, not to you.

## Routing request

When the person answers scope or the endpoint, **write it into `backseat/mail/`** rather than keeping it in your own mailbox — a project's answer filed above it is one the project's node does not find when it wakes. My next session reads that directory first.

Nothing waits on you otherwise: the writer fix is out, the judge is landed, and the only thing that moves M0′ after it is the endpoint.
