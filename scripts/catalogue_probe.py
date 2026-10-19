#!/usr/bin/env python3
"""Correlation probe: did separating idea from delivery state break the fused idea dimensions?

Compares the idea triples produced by the divergence-forcing audit against the ones produced by
the earlier blended pass. High correlation in both groups means the three columns carry one
latent judgement and must not be weighted three times; a drop means the fusion was a scoring
artifact. Prints the numbers and the sentence the catalogue quotes.
"""
import json
import statistics as st
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1] / "docs/result/catalogue-redesign/assessments.json"
KEYS = ("non_obviousness", "depth_of_thought", "transferability")


def corr(x, y):
    mx, my = st.mean(x), st.mean(y)
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    den = (sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y)) ** 0.5
    return num / den if den else float("nan")


def triples(records):
    rows = []
    for a in records:
        idea = a["display"]["idea"]
        rows.append(tuple(idea[k] for k in KEYS))
    return rows


def report(rows):
    cols = list(zip(*rows))
    pairs = [(0, 1), (1, 2), (0, 2)]
    return {f"{KEYS[i][:3]}~{KEYS[j][:3]}": round(corr(cols[i], cols[j]), 2) for i, j in pairs}


def main():
    data = json.loads(SOURCE.read_text())
    audited = [a for a in data["assessments"] if any(t.startswith("audit re-score") for t in a["display"]["trajectory"])]
    rest = [a for a in data["assessments"] if a not in audited]
    print(f"audited n={len(audited)}  blended n={len(rest)}")
    print("audited  ", report(triples(audited)))
    print("blended  ", report(triples(rest)))
    print("all      ", report(triples(data["assessments"])))


if __name__ == "__main__":
    main()
