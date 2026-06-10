#!/usr/bin/env python3
"""Convert a LOLIB .lop matrix file to DIMACS .d arc format.

LOLIB format:
  Line 1: n (integer)
  Lines 2..n+1: n space-separated integer weights per line
  C[i][j] = weight of arc (i+1) -> (j+1), 1-indexed; diagonal is ignored.

DIMACS output:
  c <source_filename>
  p sp <n> <m>
  a <from> <to> <weight>
  ...
Only nonzero off-diagonal arcs are written; zero-weight arcs are equivalent
to absent arcs in the MWFAS objective.
"""

import argparse
import json
import os
import sys


def parse_lolib(path):
    with open(path) as f:
        lines = [l.strip() for l in f if l.strip()]
    n = int(lines[0])
    if len(lines) < n + 1:
        raise ValueError(f"Expected {n+1} lines, got {len(lines)}")
    matrix = []
    for row_idx in range(n):
        vals = list(map(int, lines[row_idx + 1].split()))
        if len(vals) != n:
            raise ValueError(
                f"Row {row_idx+1}: expected {n} values, got {len(vals)}"
            )
        matrix.append(vals)
    return n, matrix


def write_dimacs(path, n, matrix, source_name, allow_negative=False):
    arcs = []
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            w = matrix[i][j]
            if w < 0 and not allow_negative:
                raise ValueError(
                    f"Negative weight {w} at C[{i}][{j}]; pass --allow-negative to override"
                )
            if w != 0:
                arcs.append((i + 1, j + 1, w))

    with open(path, "w") as f:
        f.write(f"c {source_name}\n")
        f.write(f"p sp {n} {len(arcs)}\n")
        for u, v, w in arcs:
            f.write(f"a {u} {v} {w}\n")

    return arcs


def write_metadata(path, source_file, n, matrix, arcs):
    all_off_diag = [matrix[i][j] for i in range(n) for j in range(n) if i != j]
    total_weight = sum(all_off_diag)
    nonzero_weights = [w for w in all_off_diag if w != 0]
    meta = {
        "source_file": source_file,
        "n": n,
        "total_off_diagonal_weight": total_weight,
        "arcs_written": len(arcs),
        "zero_weight_arcs_omitted": n * (n - 1) - len(arcs),
        "min_weight": min(nonzero_weights) if nonzero_weights else 0,
        "max_weight": max(nonzero_weights) if nonzero_weights else 0,
        "conversion_mode": "nonzero_arcs_only",
        "note": "Zero-weight off-diagonal arcs are omitted; they contribute 0 to objective.",
    }
    with open(path, "w") as f:
        json.dump(meta, f, indent=2)
    return meta


def main():
    ap = argparse.ArgumentParser(description="Convert LOLIB matrix to DIMACS arc format")
    ap.add_argument("--input", required=True, help="LOLIB .lop file")
    ap.add_argument("--output", required=True, help="Output DIMACS .d file")
    ap.add_argument("--metadata", required=True, help="Output metadata .json file")
    ap.add_argument(
        "--allow-negative",
        action="store_true",
        help="Allow negative weights (not standard LOLIB)",
    )
    args = ap.parse_args()

    n, matrix = parse_lolib(args.input)
    source_name = os.path.basename(args.input)

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(args.metadata)), exist_ok=True)

    arcs = write_dimacs(args.output, n, matrix, source_name, args.allow_negative)
    meta = write_metadata(args.metadata, args.input, n, matrix, arcs)

    print(
        f"Converted: {source_name} → {args.output} | "
        f"n={n}, arcs={len(arcs)}, total_weight={meta['total_off_diagonal_weight']}"
    )


if __name__ == "__main__":
    main()
