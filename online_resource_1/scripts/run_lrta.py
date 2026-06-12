#!/usr/bin/env python3
"""Run the LR-TA algorithm on a single DIMACS instance."""

import argparse
import time

from mwfas.lrta import paper_fas_ranking_from_dimacs_fast
from mwfas.evaluation import compute_forward_backward


def main():
    parser = argparse.ArgumentParser(description="LR-TA: Local-Ratio Topological Add-back for weighted MFAS")
    parser.add_argument("--input", required=True, help="Path to DIMACS instance (.d file)")
    parser.add_argument("--output", required=True, help="Path to output ranking CSV")
    parser.add_argument("--tol", type=float, default=1e-12, help="Numerical zero tolerance (default: 1e-12)")
    args = parser.parse_args()

    t0 = time.perf_counter()
    edges_indexed, node_to_index, index_to_node, scores, F_removed = (
        paper_fas_ranking_from_dimacs_fast(
            dimacs_path=args.input,
            output_ranking_csv_path=args.output,
            tol=args.tol,
        )
    )
    elapsed = time.perf_counter() - t0

    total_w, fw, bw = compute_forward_backward(edges_indexed, scores)
    print(f"Wrote ranking: {args.output}")
    print(f"Graph: n={len(node_to_index)} nodes, m={len(edges_indexed)} edges")
    print(f"Total Weight:   {total_w:.6f}")
    print(f"Forward Weight: {fw:.6f}")
    print(f"Backward Weight:{bw:.6f}")
    print(f"Forward Ratio:  {fw/total_w:.6f}")
    print(f"FAS size (edges removed): {len(F_removed)}")
    print(f"Running time: {elapsed:.3f}s ({elapsed/60:.3f} min)")


if __name__ == "__main__":
    main()
