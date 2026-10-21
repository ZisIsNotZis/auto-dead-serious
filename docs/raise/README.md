# Raise

One directory per question that a layer could not answer. This is the inbox the person reads.

```
docs/raise/<id>/
  ask.md      written once by the layer that raised it, and never rewritten:
              `kind:` one of direction, cost, resource, contract
              `spend:` what answering or acting on it costs: taste, tokens, money, gpu, disk
              `from:` the node that raised it
              then the question, in prose, with no recommendation unless the kind allows one
  effort.md   what was tried, why each path is closed, and the observation that would reopen one
  notes.tsv   one row per layer that touched it: node, opinion, time
```

A layer that receives this directory bounces it, adds a row, or moves it one level up. It never rewrites `ask.md`.

`tools/needs.py` renders `docs/needs-you.md` from whatever is here. Nothing is pushed to the person; the file is read.
