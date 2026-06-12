#!/usr/bin/env python3
"""Compute forward/backward weight of an ordering against a LOLIB matrix.

Given a LOLIB matrix file and an ordering CSV (node,position), compute:
  forward_weight  = sum C[i][j] for i,j where ordering ranks i before j
  backward_weight = total_off_diagonal - forward_weight
  forward_ratio   = forward_weight / total_off_diagonal

The ordering CSV must have columns 'node' and 'position' (or 'rank').
Nodes are 1-indexed integers matching LOLIB rows/columns.

Outputs a JSON file with the metrics.
"""

import argparse
import csv
import json
import sys


def parse_lolib(path):
    with open(path) as f:
        lines = [l.strip() for l in f if l.strip()]
    n = int(lines[0])
    matrix = []
    for row_idx in range(n):
        vals = list(map(int, lines[row_idx + 1].split()))
        matrix.append(vals)
    return n, matrix


def parse_ordering(path, n):
    """Return a dict {node_1indexed: rank} where lower rank = earlier in ordering."""
    order = {}
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            node = int(row.get("node", row.get("node_id", "")))
            pos = int(row.get("position", row.get("rank", row.get("order", ""))))
            order[node] = pos
    if len(order) != n:
        raise ValueError(f"Ordering has {len(order)} nodes, expected {n}")
    return order


def compute_weights(n, matrix, order):
    forward = 0
    backward = 0
    total = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            w = matrix[i - 1][j - 1]
            total += w
            if order[i] < order[j]:
                forward += w
            else:
                backward += w
    return forward, backward, total


def main():
    ap = argparse.ArgumentParser(description="Evaluate an ordering against a LOLIB matrix")
    ap.add_argument("--lolib", required=True, help="LOLIB matrix file")
    ap.add_argument("--ordering", required=True, help="CSV with node,position columns")
    ap.add_argument("--output", required=True, help="Output JSON metrics file")
    args = ap.parse_args()

    n, matrix = parse_lolib(args.lolib)
    order = parse_ordering(args.ordering, n)
    forward, backward, total = compute_weights(n, matrix, order)

    metrics = {
        "n": n,
        "lolib_file": args.lolib,
        "ordering_file": args.ordering,
        "total_off_diagonal_weight": total,
        "forward_weight": forward,
        "backward_weight": backward,
        "forward_ratio": forward / total if total > 0 else None,
        "check_sum_correct": (forward + backward == total),
    }
    with open(args.output, "w") as f:
        json.dump(metrics, f, indent=2)
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
