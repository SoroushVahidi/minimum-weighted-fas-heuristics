#!/usr/bin/env python3
"""Run all three algorithms on every instance listed in configs/benchmark_instances.txt."""

import argparse
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mwfas.lrta import paper_fas_ranking_from_dimacs_fast
from mwfas.wmsf import wmsf_ranking_from_dimacs_fast
from mwfas.ipsns import lns_merge_wmsf_lr_best_incumbent
from mwfas.evaluation import compute_forward_backward


def run_all(instances_file, dataset_dir, results_dir, ipsns_iters=400, rng_seed=1):
    os.makedirs(os.path.join(results_dir, "raw"), exist_ok=True)

    with open(instances_file) as f:
        instances = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    summary_rows = []

    for inst in instances:
        input_path = os.path.join(dataset_dir, inst) if not os.path.isabs(inst) else inst
        if not os.path.exists(input_path):
            print(f"[SKIP] not found: {input_path}")
            continue

        stem = os.path.splitext(os.path.basename(input_path))[0]
        print(f"\n=== {stem} ===")

        for algo, run_fn, kwargs in [
            ("lrta",  paper_fas_ranking_from_dimacs_fast,       {}),
            ("wmsf",  wmsf_ranking_from_dimacs_fast,            {"ordering": "L2"}),
            ("ipsns", lns_merge_wmsf_lr_best_incumbent,         {"iters": ipsns_iters, "rng_seed": rng_seed, "log_every": 0}),
        ]:
            out_csv = os.path.join(results_dir, "raw", f"{stem}_{algo}_ranking.csv")
            t0 = time.perf_counter()
            edges_indexed, node_to_index, _, scores, _ = run_fn(
                dimacs_path=input_path,
                output_ranking_csv_path=out_csv,
                **kwargs,
            )
            elapsed = time.perf_counter() - t0
            total_w, fw, bw = compute_forward_backward(edges_indexed, scores)
            ratio = fw / total_w if total_w > 0 else 0.0
            print(f"  {algo}: BW={bw:.6f}  FW_ratio={ratio:.6f}  time={elapsed:.2f}s")
            summary_rows.append({
                "instance": stem,
                "algorithm": algo,
                "n": len(node_to_index),
                "m": len(edges_indexed),
                "total_weight": total_w,
                "forward_weight": fw,
                "backward_weight": bw,
                "forward_ratio": ratio,
                "time_sec": elapsed,
                "output_csv": out_csv,
            })

    try:
        import pandas as pd
        summary_path = os.path.join(results_dir, "processed", "summary.csv")
        os.makedirs(os.path.dirname(summary_path), exist_ok=True)
        pd.DataFrame(summary_rows).to_csv(summary_path, index=False)
        print(f"\nSummary written to {summary_path}")
    except ImportError:
        pass

    return summary_rows


def main():
    parser = argparse.ArgumentParser(description="Reproduce all experiments")
    parser.add_argument("--instances", default="configs/benchmark_instances.txt",
                        help="File listing benchmark instance paths (default: configs/benchmark_instances.txt)")
    parser.add_argument("--dataset-dir", default="",
                        help="Directory prepended to relative instance paths")
    parser.add_argument("--results-dir", default="results",
                        help="Root directory for output CSVs (default: results/)")
    parser.add_argument("--ipsns-iters", type=int, default=400,
                        help="IPSNS LNS iterations (default: 400)")
    parser.add_argument("--rng-seed", type=int, default=1, help="Random seed (default: 1)")
    args = parser.parse_args()

    run_all(
        instances_file=args.instances,
        dataset_dir=args.dataset_dir,
        results_dir=args.results_dir,
        ipsns_iters=args.ipsns_iters,
        rng_seed=args.rng_seed,
    )


if __name__ == "__main__":
    main()
