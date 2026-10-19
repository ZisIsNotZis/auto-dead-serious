# Catalogue validation
Authored execution-evidence record for the current assessment source set; scores and membership facts are owned by catalogue/*.json and the generated catalogue/README.md, not this record.
## Bound revision
Observed at 2026-10-19T11:09:01+08:00 in parent /home/z/vibe, based on parent ca6ae15e46e022e716c9474f16926838a9c50074 plus the scoped catalogue worktree changes.
The checker binds assessment JSON, rubric/product contract, public comparison, producer script, registry and expected browsing view to SHA-256 66f83a90e4d57428d1ada7cecd1d1dab0816ae2cd211731127882de92390a25b; rerun the command below to verify this exact source set. Child HEADs are checked against each record's observation, and parent gitlinks against the current index; dirty-source content is not reproduced by this check.
## Commands and observations
From the parent root, python3 scripts/catalogue.py --render completed and printed: PASS 75 assessments: exact coverage, schema, current pins/HEADs, evidence files, generated view.
python3 scripts/catalogue.py --check completed with the same PASS and source digest; this checks exact .gitmodules coverage, valid scores/confidence/routes/metadata, membership consistency, local evidence-file existence, matching child Git roots/HEADs and parent pins, and generated consistency.
python3 scripts/catalogue.py --self-test completed and printed: PASS negative controls: missing project, duplicate project, bad score, boolean score, unsafe removal, unsafe evidence path, missing evidence file, stale pin; unknown accepted.
The negative controls mutate in-memory record copies only; none changed actual records, files, Git state or child work. They distinguish the claimed structural failures from a merely green happy-path check.
git diff --check -- docs/plan/catalogue.md docs/method/catalogue.md docs/result/catalogue-comparison.md scripts/catalogue.py produced no errors before staging; final staged whitespace verification is part of the delivery commit.
git diff --name-only -- README.md README.zh-CN.md .gitmodules printed no paths; no parent front door or membership registry was modified.
## Semantic calibration
The parent read all investigator reports and reconciled candidate-queue interpretation, the supported-private-route verdict, specification-only progress, dojo's conditional expected usefulness against its current product scope, and the availability inference for local_lm_research; affected reasons explicitly attribute parent calibration. The method owns those semantics and catalogue/*.json owns each applied judgement.
Public comparison evidence and retrieval limits are in catalogue-comparison.md; the work did not perform one exhaustive novelty audit per project. All records keep the non-repetition route unknown where documentary comparison cannot settle it.
## Unverified boundaries
No child installation, tests, build, benchmark, app, model, rendering, hardware interaction or agent/provider operation was executed. No visual-quality, security, numerical-correctness, global-originality or real-user-effectiveness acceptance is claimed.
Evidence-file existence is mechanically checked; individual prose locators and the truth/semantic support of every cited claim are not mechanically established. Source-inspection judgements remain bounded investigator/parent inference, not fresh independent acceptance.
PathLM's dirty live outputs and private personal payloads remained excluded. No submodule was removed, initialized or cleaned, and no child repair was performed.
