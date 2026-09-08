# 01 — Markdown style consolidation + tool-bypass closure

- **Status:** done
- **Blocked by:** none
- **Assignee/lock:** agent (pi, volc2/glm-5.3-flash)

## Issue

PO reports persistent violations: manual markdown line-wrapping, python-script edits
bypassing the edit tool, redundant Q&A sections written as content, unstructured prose-wall
markdown. Fix by consolidation and explicitness: Doc 6.1 (Markdown style) groups the
format rules with the why; Doc 4.1 pins the five Q&A pairs as a verification artifact
stored beside the doc, never content inside it; Proper tools 12 bans scripting around the
edit tool (python/heredoc rewrites) outside genuine batch transformations.

## Acceptance criteria

- [x] Doc 6 split into 6 + 6.1 (Markdown style); 4.1 amended; Sessions 12 amended.
- [x] zh parity maintained (147 lines each).
- [x] `git diff --check` clean. Review skipped per PO's standing preference for dictated fixes.

## Comments

- 2026-09-04 (agent, pi coding agent, volc2/glm-5.3-flash) — Created and claimed.
