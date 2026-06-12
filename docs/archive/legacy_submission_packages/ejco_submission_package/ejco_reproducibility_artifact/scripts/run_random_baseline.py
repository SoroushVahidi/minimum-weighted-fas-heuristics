"""CLI for random-multistart ordering baseline."""
import argparse
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from mwfas.baselines import random_multistart_ordering_from_dimacs


def main():
    p = argparse.ArgumentParser(
        description="Random multistart ordering baseline (best of N random permutations)"
    )
    p.add_argument("--input", required=True, help="DIMACS .d instance file")
    p.add_argument("--output", default=None, help="Output ranking CSV path")
    p.add_argument("--summary-output", default=None, help="One-row metrics JSON path")
    p.add_argument("--trials", type=int, default=100, help="Number of random trials")
    p.add_argument("--seed", type=int, default=1, help="Random seed")
    args = p.parse_args()

    _, _, _, _, metrics = random_multistart_ordering_from_dimacs(
        args.input, args.output, trials=args.trials, seed=args.seed
    )

    if args.summary_output:
        with open(args.summary_output, "w") as f:
            json.dump(metrics, f, indent=2)

    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
