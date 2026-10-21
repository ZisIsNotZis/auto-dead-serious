# Checkout facts

Optional local inspection notes for this aggregator.

## Layout

`.gitmodules` maps child checkout paths to repository URLs; these names can
differ (for example, `drive` maps to `suzhou-drive`). The parent index records
pinned gitlinks, while each child has its own index and working tree. A changed
child checkout and a changed parent pin are distinct states.

The existing private-project slug convention uses a trailing `_private`
(for example, `colleague_private`). Local names do not verify remote visibility.

## Local-only checkouts

Two project directories are git repositories with no remote: `petfleet` and `prompt_fixed_point`. The parent index cannot pin them, so their absence from `.gitmodules` and from the index is deliberate rather than forgotten. They stay untracked here until each has a remote, because a pin to a commit nobody else can fetch is worse than an explained gap.

## Inspection

From the aggregator root, replace `<child>` with the relevant checkout path:

```sh
git submodule status -- <child>
git -C <child> status --short
```

The first command reports the child's checked-out revision relative to the
parent pin; the second reports that child's local changes. Neither changes the
checkout or runs the child's tests.
