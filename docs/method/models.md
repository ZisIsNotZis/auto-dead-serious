# Models

Which model serves which work, and why the answer is not "the cheapest one".

## The rule

Development uses the strongest model available. Doing the work well beats doing it cheaply, and a weaker model is slower in wall-clock terms because its mistakes come back. A cheap model is for automation, meaning work whose success is decided by a check rather than by judgement.

The price clock is a reason to wait, never a reason to choose a weaker model. It moves when a spend happens, not what the spend buys.

## What is available, stated by the person

| model | price | clock | verdict |
| --- | --- | --- | --- |
| `deepseek-flash` | low | peak and idle | strongest available, so it carries development |
| `deepseek-pro` | higher | peak and idle | never used: not updated, dearer, and weaker than flash |
| `gpt-6-luna` | cheapest | none | automation only; the intelligence gap is large |
| `gpt-6.1-sol` | above deepseek | none | unused: dearer than flash and worse in his experience |
| volcano `deepseek-v4.1-flash` | below the official plan | none, billed by rounded length per quota with cache hits ignored | unused today: opaque billing, no service level, a slightly weaker quantised build, not updated |
| zai `glm-5.3-flash` | free | none | weaker than deepseek, so it does not advance work |
| copilot | free, sharing one pool between luna and sol | none | the free pool is why luna is the automation default |

## Free and prepaid allowances

Three kinds of allowance behave differently and the difference decides the hour, not the price.

A **rate that follows the clock** is money not yet spent, so waiting is free and the idle window wins whenever the work is throughput-bound.

A **prepaid monthly allowance** is already spent. An unused one expires to nothing, so it is used at any hour and on work whose failure is cheap. This is the one case where paying peak rates is right: there is no peak rate to pay, only a balance that decays on its own.

A **free pool**, meaning copilot's shared quota and zai's `glm-5.3-flash`, is also already owned, and it is the natural home of automation, whose success a check decides rather than a judgement.

## Where the keys and the gateway are

Every provider's key is in the environment, and a local gateway answers on `127.0.0.1:4000` with a connected database. Automation that does not run inside pi reaches `luna` through that gateway rather than the provider directly, because the copilot protocol is involved and `luna` requires the responses interface; a direct call is a way to spend an afternoon on a protocol instead of on the work.

## What this means for the portfolio

A project's `model_work` is the model that advances it, and it is `deepseek-flash` while that remains the strongest. Its `model_product` is what the product calls at runtime, which is a cost the product owns rather than the root, and it takes `gpt-6-luna` because automation there is judged by checks.

When a provider bills by the clock, the project's `window` says whether waiting for the idle rate is free. When the provider does not, `window` is `any` regardless of how token-heavy the work is, because there is nothing to wait for.
