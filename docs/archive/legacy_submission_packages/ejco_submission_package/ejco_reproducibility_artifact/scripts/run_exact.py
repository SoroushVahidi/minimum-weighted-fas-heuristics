#!/usr/bin/env python3
"""Run the exact minimum weighted FAS DP on a single small DIMACS instance."""

import argparse
import time

from mwfas.exact import exact_min_fas_from_dimacs
from mwfas.evaluation import compute_forward_backward


def main():
    parser = argparse.ArgumentParser(
        description="Exact min-weighted FAS via bitmask DP (n <= 20)"
    )
    parser.add_argument("--input", required=True, help="Path to DIMACS instance")
    parser.add_argument("--output", default=None, help="Optional path to write ranking CSV")
    args = parser.parse_args()

    t0 = time.perf_counter()
    edges_indexed, n2i, i2n, min_fas, max_fw, scores = exact_min_fas_from_dimacs(
        args.input, args.output
    )
    elapsed = time.perf_counter() - t0

    n = len(n2i)
    total_w, fw, bw = compute_forward_backward(edges_indexed, scores) if scores else (0.0, 0.0, 0.0)
    print(f"Graph: n={n}, m={len(edges_indexed)}")
    print(f"Total Weight:      {total_w:.6f}")
    print(f"Optimal FW Weight: {max_fw:.6f}")
    print(f"Optimal BW Weight: {min_fas:.6f}")
    print(f"Optimal FW Ratio:  {max_fw/total_w:.6f}" if total_w > 1e-15 else "Optimal FW Ratio:  N/A (empty)")
    print(f"Runtime: {elapsed:.4f}s")
    if args.output:
        print(f"Ranking written: {args.output}")


if __name__ == "__main__":
    main()
