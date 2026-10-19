#!/usr/bin/env python3
"""Render a YAML policy SSOT into a Markdown view, and run every mechanical check on it.

Parameterised on purpose: nothing but the defaults is specific to this repository, so the
same command checks any doc set that declares a source and a render.

    --source   the SSOT to check, and the input to the render
    --out      the rendered view; regenerated on write, compared byte for byte on --check
    --check    check only, and confirm the render matches a fresh render of the SSOT

The checks run with the render, never apart from it:
  - one key per line: no manual wrap and no blank line, in the SSOT and in the render
  - the SSOT parses, with duplicate keys refused rather than silently kept
  - every key is snake_case, globally unique and space-free, and every node has a string _text
  - every @ref names a key the renderer actually writes into the view
  - no two nodes carry the same text, because a fact has one home
  - the render is byte-identical to a fresh render of the SSOT

The view also opens with a one-line index of every handle, generated from the same
source so that the map can never drift from the rules it maps.
"""
from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
SRC = HERE / "AGENTS.yaml"
OUT = HERE / "AGENTS.md"

KEY_RE = re.compile(r"[a-z][a-z0-9_]*\*?$")
REF_RE = re.compile(r"(?<![\w@])@([a-z0-9_]+)")
LINE_RE = re.compile(r"^(?:[a-z][a-z0-9_*]*|[ \t]+(?:_text|[a-z][a-z0-9_*]*)):(?:[ \t]\S.*)?$")
FENCE_RE = re.compile(r"^(?:```yaml|```|<!.*-->)$")


class UniqueKeyLoader(yaml.SafeLoader):
    """A loader that refuses a duplicate key instead of silently keeping the last."""


def _mapping_without_duplicates(loader, node, deep=False):
    mapping, marks = {}, {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                None, None,
                f"duplicate key {key!r} (first seen at line {marks[key].line + 1})",
                key_node.start_mark,
            )
        marks[key] = key_node.start_mark
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping_without_duplicates
)


def read(path: Path):
    with path.open(encoding="utf-8") as fh:
        return yaml.load(fh, Loader=UniqueKeyLoader)


def walk(node, path=""):
    """Yield every child key, skipping the reserved _text field, in document order."""
    for key, value in node.items():
        if key == "_text":
            continue
        here = f"{path}/{key}"
        yield key, value, here
        if isinstance(value, dict):
            yield from walk(value, here)


def rendered_keys(node, hidden=False):
    """Yield only the keys the renderer writes out: a hidden node hides its whole subtree."""
    for key, value in node.items():
        if key == "_text" or hidden:
            continue
        if not key.endswith("*"):
            yield key
        if isinstance(value, dict):
            yield from rendered_keys(value, key.endswith("*"))


def convertible(node):
    """The shape the renderer is expected to write for this node."""
    children = {
        key: value
        for key, value in node.items()
        if key != "_text" and not key.endswith("*")
    }
    if not children:
        return node["_text"]
    return {"_text": node["_text"], **{k: convertible(v) for k, v in children.items()}}


def check_layout(path: Path, extra=None) -> list[str]:
    """Every line is one key, one comment or nothing: no manual wrap, no blank line."""
    errors = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            errors.append(f"{path.name}:{number}: blank line")
        elif line.lstrip().startswith("#") or (extra and extra.match(line)):
            continue
        elif not LINE_RE.match(line):
            errors.append(f"{path.name}:{number}: not a single key line (manual wrap?)")
    return errors


def check(doc) -> list[str]:
    errors: list[str] = []

    keys, refs = [], []
    for key, value, path in walk(doc):
        keys.append(key)
        if not KEY_RE.fullmatch(key):
            errors.append(f"bad key shape: {path}")
        if not isinstance(value, dict) or "_text" not in value:
            errors.append(f"node without _text: {path}")
            continue
        if not isinstance(value["_text"], str):
            errors.append(f"_text is not a string: {path}")
            continue
        refs.extend(REF_RE.findall(value["_text"]))

    dupes = [k for k, n in collections.Counter(keys).items() if n > 1]
    if dupes:
        errors.append("duplicate key: " + ", ".join(sorted(dupes)))

    # one meaning in two places: the check cannot see this in the keys, only in the text
    seen: dict[str, str] = {}
    for key, value, path in walk(doc):
        if isinstance(value, dict) and isinstance(value.get("_text"), str):
            text = value["_text"]
            if text in seen:
                errors.append(f"two nodes carry the same text (one home): {seen[text]} and {path}")
            else:
                seen[text] = path

    unknown = sorted(set(refs) - set(rendered_keys(doc)))
    if unknown:
        errors.append("dangling @ref (not rendered into the view): " + ", ".join(unknown))
    return errors


CLAUSE_CUT = re.compile(r"(?:\.\s|;\s|\s-\s)")
INDEX_LIMIT = 140


def first_clause(text: str) -> str:
    """The leading statement of a node, short enough to sit beside its handle."""
    text = " ".join(text.split())
    cut = CLAUSE_CUT.search(text)
    if cut:
        text = text[: cut.start()]
    text = text.rstrip(" .,;:-")
    if len(text) > INDEX_LIMIT:
        text = text[:INDEX_LIMIT].rsplit(" ", 1)[0] + " ..."
    return text


def render_index(doc) -> str:
    """One comment line per handle, so the view opens with a map a reader can hold."""
    lines = []
    for key, value in doc.items():
        if key == "_text":
            continue
        line = f"# {key} - {first_clause(value.get('_text', ''))}"
        if key == "laws":
            children = [child for child in value if child != "_text" and not child.endswith("*")]
            line += ": " + ", ".join(children)
        lines.append(line)
    return "\n".join(lines) + "\n"


def render(doc, source: Path) -> str:
    expected = {key: convertible(value) for key, value in doc.items()}
    body = yaml.safe_dump(
        expected,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
        width=10**6,
    )
    body = "\n".join(line for line in body.splitlines() if line.strip()) + "\n"
    assert yaml.safe_load(body) == expected, "rendering changed the document"
    banner = f"<!-- generated from {source.name} - edit that file -->\n"
    return f"{banner}```yaml\n{render_index(doc)}{body}```\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--source", type=Path, default=SRC, help="the SSOT to check and render")
    parser.add_argument("--out", type=Path, default=OUT, help="the rendered view")
    parser.add_argument("--check", action="store_true", help="check only; do not write the view")
    args = parser.parse_args()

    # Lint the raw text first: a YAML-invalid file never reaches the parser, and a wrap that
    # still parses must be reported as a wrap rather than as a schema surprise.
    errors = check_layout(args.source)
    if args.out.exists():
        errors += check_layout(args.out, extra=FENCE_RE)

    doc = None
    try:
        doc = read(args.source)
    except yaml.YAMLError as exc:
        mark = getattr(exc, "problem_mark", None)
        where = f" (line {mark.line + 1})" if mark else ""
        errors.append(f"{args.source.name}: YAML error{where}: {getattr(exc, 'problem', exc)}")
    if doc is not None:
        errors += check(doc)

    if errors:
        print("checks failed:")
        for err in errors:
            print(" -", err)
        return 1

    text = render(doc, args.source)
    if args.check:
        current = args.out.read_text(encoding="utf-8") if args.out.exists() else ""
        if current != text:
            print(f"{args.out.name} is out of sync with {args.source.name}; re-run without --check.")
            return 1
        print(f"checks passed; {args.out.name} matches {args.source.name}.")
        return 0

    args.out.write_text(text, encoding="utf-8")
    print(f"checks passed; wrote {args.out} ({len(text.splitlines())} lines).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
