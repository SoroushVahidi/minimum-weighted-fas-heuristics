#!/usr/bin/env python3
"""Run the IPSNS algorithm on a single DIMACS instance."""

import argparse

from mwfas.ipsns import lns_merge_wmsf_lr_best_incumbent


def main():
    parser = argparse.ArgumentParser(
        description="IPSNS: Incumbent-Protected SCC-Neighborhood Search for weighted MFAS"
    )
    parser.add_argument("--input", required=True, help="Path to DIMACS instance (.d file)")
    parser.add_argument("--output", required=True, help="Path to output ranking CSV")
    parser.add_argument("--seed-ordering", choices=["L1", "L2"], default="L2",
                        help="Arc ordering for WMSF seed (default: L2)")
    parser.add_argument("--iters", type=int, default=400, help="Number of LNS iterations (default: 400)")
    parser.add_argument("--topk-scc", type=int, default=15, help="Candidate SCC pool size (default: 15)")
    parser.add_argument("--destroy-addback-frac", type=float, default=0.30,
                        help="Fraction of removed SCC edges to reactivate (default: 0.30)")
    parser.add_argument("--destroy-remove-frac", type=float, default=0.02,
                        help="Fraction of active SCC edges to forcibly remove (default: 0.02)")
    parser.add_argument("--tol", type=float, default=1e-12, help="Numerical zero tolerance (default: 1e-12)")
    parser.add_argument("--rng-seed", type=int, default=1, help="Random seed (default: 1)")
    parser.add_argument("--log-every", type=int, default=10,
                        help="Log progress every N iterations; 0 to disable (default: 10)")
    parser.add_argument("--wmsf-seed-mode", choices=["full", "legacy"], default="full",
                        help="WMSF seed algorithm: 'full' (default) matches standalone WMSF "
                             "(per-SCC, Stabilize, L1+L2 for single-SCC); "
                             "'legacy' uses global removeArcs+minimize, L2-only.")
    args = parser.parse_args()

    lns_merge_wmsf_lr_best_incumbent(
        dimacs_path=args.input,
        output_ranking_csv_path=args.output,
        seed_ordering=args.seed_ordering,
        iters=args.iters,
        topK_scc=args.topk_scc,
        destroy_addback_frac=args.destroy_addback_frac,
        destroy_remove_frac=args.destroy_remove_frac,
        tol=args.tol,
        rng_seed=args.rng_seed,
        log_every=args.log_every,
        wmsf_seed_mode=args.wmsf_seed_mode,
    )


if __name__ == "__main__":
    main()
