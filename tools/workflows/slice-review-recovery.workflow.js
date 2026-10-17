const workerTask = [
  'RECOVERY + FINISH task. A previous worker timed out (30 min, high thinking) after already writing slice-review edits into the two policy files. You must reconcile and finish, not blindly redo. Read /home/z/vibe/AGENTS.md and /home/z/vibe/docs/policy/execution.md FULLY first, plus the existing ticket .scratch/25-slice-review-selfloop/ (baseline/ + validate.py). Edit ONLY the two policy files plus ticket artifacts.',
  '',
  'Step 1 — reconcile the slice-review change already on disk:',
  '- Expected semantics: (a) independent review is a VERTICAL-SLICE gate, at least once before a slice completes, not per task/sub-task, timing flexible within the slice; (b) the worker runs a self-loop — record the acceptance standard, implement, check against it, iterate until it passes; (c) work with no vertical slice (record/policy/documentation-only) is independently reviewed only when the user asks; (d) vertical slice = bounded end-to-end user outcome (Product decisions); (e) keep "self-test is the in-slice loop, not independent acceptance", fresh review, and all boundaries intact.',
  '- The on-disk edits appear to implement this. Verify each (a)-(e) is present, coherent and non-contradictory; fill any gap; remove any leftover inconsistency. State each rule once (AGENTS.md = binding boundary, execution.md = method/pointer).',
  '',
  'Step 2 — ADD the focus/economy rule (the reason is focus, not only cost):',
  '- Every agent, main and sub alike, defaults to the main agent\'s own reasoning budget — normally the session default, which is low. Raise it only when the work is genuinely complex or an agent repeatedly fails. State it plainly; do not hardcode model names in the policy.',
  '- Keep each agent\'s context/mental space small and focused: prefer splitting work over assigning unrelated tasks to one agent, avoid needless long reasoning, and avoid bloating one context with disparate work.',
  '- Placement: concise binding sentence in AGENTS.md; method wording in execution.md, pointing at the core rule.',
  '',
  'Step 3 — fix the ticket validator (it self-reported FAIL on false positives):',
  '- The link check must resolve AGENTS.md -> docs/policy/execution.md anchors against execution.md\'s own headings, not AGENTS.md\'s headings.',
  '- Banned-word checks must not match the ban-list text itself (e.g. the words "errata" / "was X, later" appear legitimately inside the banned-forms list).',
  '- Drop unrelated filesystem mtime checks (things like helpagent/.git or other projects must not make the check fail).',
  'Re-run the corrected validator and record the real result.',
  '',
  'Step 4 — record in the ticket the verified subagent-parameter fact: thinking is controlled only by the model suffix (exact provider/id:off|minimal|low|medium|high|xhigh|max); the dispatch "thinking" field is ignored; builtin worker/reviewer default to high; children inherit the parent model; the builtin high default is overridden per run, and a failed high-thinking run timed out at 30 min (run 2ad01866) while this round uses low. Evidence: subagent models list + guide topic=tool-reference.',
  '',
  'PROCESS: write your own acceptance standard in the ticket first, then edit, then self-check against it, iterate until it passes. Self-test link/anchor and "git diff --check"; record commands+results. Keep tool use lean. Do NOT commit.',
  'Return: file:line summary, the self-derived standard and verification, evidence paths, net size change, residual uncertainty.',
].join('\n');

const w = await runs.run('worker', { agent: 'worker', model: 'deepseek/deepseek-flash:low', task: workerTask, timeoutMs: 900000 });
return { workerOutput: w.output };
