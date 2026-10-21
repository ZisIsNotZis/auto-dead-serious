# Mail

Every node has this directory under its own path, and it holds every message about that node in either direction. A message names its target, so direction is a field rather than a folder.

```
kind:    direction | cost | resource | contract
spend:   taste | tokens | money | gpu | disk
from:    the node that wrote it
to:      the node it is for, or `person`
id:      the id of the message it answers, when it answers one

the question or the instruction

## effort
what was tried, why each path is closed, and what would reopen one
```

This directory is tracked. A message that exists on one machine and not another is a decision taken and then lost. It is created the first time something is written, and it does not need to exist before then.

`tools/needs.py` renders `docs/needs-you.md` from the files here addressed to `person`. Reading deletes a message; deletion is tidying, not answering, and it is committed like any other change.
