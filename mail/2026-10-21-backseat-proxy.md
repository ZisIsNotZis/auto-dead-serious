kind:    resource
spend:   tokens
from:    root
to:      person
id:      raised from the first orientation report of `backseat`

One running service, asked for because a gate item cannot be measured without it.

The M0′ gate includes "cursor backlog 0". That needs the pipeline alive, which
needs your LiteLLM proxy at `127.0.0.1:4000`; it was refusing connections and the
daemon has been down since 2026-10-19, with the cursor one row behind. Idle local
compute cannot stand in for an endpoint the project does not own.

Reopens on: you starting the proxy, or naming an alternate endpoint and model.

## effort

Tried: `pgrep`, the daemon's `run.log` tail, and a comparison of
`state.witness_cursor` against `count(observations)` — the pipeline is stopped,
not slow. Closed because starting a metered external endpoint is a spend and the
endpoint is yours.

## root's row

cost: whatever the proxy's own usage costs while a backlog drains.
priority: with the quiet window for `flashdb` — both are the same act, giving a
project a working window on this machine.
recommendation: start it for one evening; the backlog is one row of observations
behind, so the act is minutes.
