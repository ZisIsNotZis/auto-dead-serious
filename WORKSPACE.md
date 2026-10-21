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

One project directory is a git repository with no remote: `prompt_fixed_point`, which has no commits yet. Its absence from `.gitmodules` and from the index is deliberate rather than forgotten; it stays untracked until it has commits and a remote, because a pin to a commit nobody else can fetch is worse than an explained gap. `petfleet` had the same shape and now has a private remote and a pin, after a night of work sat on one disk.

## Inspection

From the aggregator root, replace `<child>` with the relevant checkout path:

```sh
git submodule status -- <child>
git -C <child> status --short
```

The first command reports the child's checked-out revision relative to the
parent pin; the second reports that child's local changes. Neither changes the
checkout or runs the child's tests.
