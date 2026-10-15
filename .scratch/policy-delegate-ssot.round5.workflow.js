const workerTask = [
  'ROUND 5 (FINAL polish) — close the two round-4 report-only P2 notes. Edit ONLY /home/z/vibe/AGENTS.md and /home/z/vibe/.scratch/24-delegation-ssot-context/evidence.md (plus regenerated ticket artifacts). Read both targets first. Current bound revision: AGENTS.md sha256 3f6584bc… (6,673 B), docs/policy/execution.md sha256 f6ab19fd… (10,481 B), HEAD c82765e.',
  '',
  'P2-A (AGENTS.md:22, weakened obligation): the explicit persistence verb was lost. Restore it concisely, keeping the single-home pointer, e.g. "When permitted, split a splittable assignment into same-layer siblings, defining and recording complete coverage and ownership (enumeration in [Task routing](docs/policy/execution.md#task-routing))." No duplication of the enumeration.',
  '',
  'P2-B (stale evidence rows): evidence.md currently carries round-3 statements that are now false against AGENTS.md:22 — at approximately line 186 ("records coverage/owners/interfaces/deps/integration owner … AGENTS.md:22") and line 231 ("AGENTS.md:22 requires recording complete coverage, owners, interfaces, dependencies and an integration owner. Holds."). Tickets are append-style, so do NOT rewrite history: append a round-5 correction section that explicitly marks those rows as round-3-revision statements superseded by the round-4/5 wording and states what now holds.',
  '',
  'Self-consistency sweep (bounded): scan evidence.md for any OTHER assertion about the current AGENTS.md / execution.md text that is false after rounds 4-5, and mark each superseded in the round-5 section. Do not restructure earlier sections.',
  '',
  'Constraints:',
  '- Concise; minimal bytes; do not drop or weaken any accepted rule.',
  '- Re-run validate.py, link/anchor and "git diff --check"; regenerate diffs, metrics and final-manifest.json.',
  '- Do NOT commit; leave changes unstaged.',
  '',
  'Return: file:line summary, which P2 each closes, evidence paths, net size change, residual uncertainty. Do not claim PASS.',
].join('\n');

const reviewTask = [
  'Fresh independent FINAL review after round 5. Do not rely on worker claims: read /home/z/vibe/AGENTS.md and /home/z/vibe/docs/policy/execution.md fully, the diff, and the ticket evidence under /home/z/vibe/.scratch/24-delegation-ssot-context/. This is the last planned round: report only MATERIAL (blocking) defects; classify anything cosmetic as non-blocking.',
  '',
  'Confirm the ten criteria hold: (1) Main unconditional highest-priority delegation, context-age binding, unavailable-delegation blocker; (2) ticket per task as log home, append-style tickets only; (3) non-ticket docs = current facts, one home per fact, in-place rewrite, banned list, no dup/stale/conflict; (4) "Preserve other entries" scoped to ticket ledger; (5) fresh by default, inherit only when a context-free description costs more, review never inherits; (6) (D) split only when permitted, with coverage/ownership recorded and enumeration single-homed; (7) (E) SMART + explicit task/AC on fresh handoffs, fork handoffs designate role only; (8) (F) minimal inter-agent messages, results on disk, short done/not-done report to Main; (9) (G) ticket vs fact-document classes disjoint; (10) concise, no weakened boundaries, links resolve, revision-bound evidence consistent.',
  '',
  'Confirm P2-A (explicit record obligation restored at AGENTS.md:22 without duplication) and P2-B (stale round-3 evidence rows marked superseded; no remaining false current-text claims in evidence.md) are CLOSED. Confirm no new stale/false evidence claim was introduced.',
  '',
  'Falsify the four scenarios: under-specified fresh task; whole-task restatement to a fork child; long report to Main; in-place rewrite of a ticket / append to a fact document. Report PASS/FAIL per criterion, P2-A/P2-B status, before/after size, and any MATERIAL defect with file:line. Do NOT repair.',
].join('\n');

const verifyTask = [
  'Independent command reproduction after round 5. READ and RUN only; do NOT edit, create or delete anything.',
  'Run exactly and report raw output:',
  '1. cd /home/z/vibe && sha256sum AGENTS.md docs/policy/execution.md',
  '2. cd /home/z/vibe && python3 .scratch/24-delegation-ssot-context/validate.py; echo EXIT=$?',
  '3. cd /home/z/vibe && git diff --check -- AGENTS.md docs/policy/execution.md; echo EXIT=$?',
  '4. cd /home/z/vibe && git status --short AGENTS.md docs/policy/execution.md; git diff --cached --stat',
  '5. cd /home/z/vibe && wc -l -c AGENTS.md docs/policy/execution.md; git rev-parse HEAD',
  'Then read /home/z/vibe/.scratch/24-delegation-ssot-context/final-manifest.json and state whether observed sha256 values, bytes, lines and HEAD match it. Report raw evidence only; state any mismatch explicitly.',
].join('\n');

const w = await runs.run('worker5', { agent: 'worker', task: workerTask });
const r = await runs.run('review5', { agent: 'reviewer', task: reviewTask });
const v = await runs.run('verify5', { agent: 'worker', task: verifyTask });
return { workerOutput: w.output, reviewOutput: r.output, verifyOutput: v.output };
