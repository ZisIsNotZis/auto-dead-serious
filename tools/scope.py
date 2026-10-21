#!/usr/bin/env python3
"""Refuse a sentence about a project that lives above it.

Everything about a project lives under that project's directory; the only trace it leaves
above is its name and the path that name resolves to. This checks the half of that rule
which can be checked: the workspace's own documents may not name a project at all, so the
only place a name appears above is the register that resolves it.

    python3 tools/scope.py --check
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
REGISTER = HERE / "docs" / "plan" / "portfolio.tsv"
ALLOWED = {"docs/plan/portfolio.tsv"}
EXEMPT = HERE / "docs" / "plan" / "scope-exempt.txt"


def exemptions() -> list[str]:
    out = []
    for line in EXEMPT.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        out.append(line.split("\t")[0])
    return out


def exempt(path: str, patterns: list[str]) -> bool:
    from fnmatch import fnmatch
    return any(fnmatch(path, p) for p in patterns)


def register() -> list[tuple[str, str]]:
    rows = REGISTER.read_text(encoding="utf-8").strip().split("\n")[1:]
    return [(r.split("\t")[0], r.split("\t")[1]) for r in rows if r.strip()]


def own_files(dirs: set[str]) -> list[str]:
    out = subprocess.run(["git", "ls-files", "*.md"], cwd=HERE, capture_output=True, text=True)
    return [p for p in out.stdout.split("\n") if p and p.split("/")[0] not in dirs]


def main() -> int:
    rows = register()
    dirs = {d for _, d in rows}
    failures, skipped = [], []
    patterns = exemptions()
    for path in own_files(dirs):
        if path in ALLOWED or not (HERE / path).exists():
            continue
        if exempt(path, patterns):
            skipped.append(path)
            continue
        text = (HERE / path).read_text(encoding="utf-8", errors="ignore")
        for name, _ in rows:
            if name in text:
                failures.append(f"{path} names {name}, which lives in {name}/")
    print(f"note: {len(skipped)} files exempted by docs/plan/scope-exempt.txt")
    if failures:
        print("\n".join(f"FAIL {f}" for f in failures))
        return 1
    print(f"ok: {len(rows)} names resolve above and no other document names one")
    return 0


if __name__ == "__main__":
    sys.exit(main())
