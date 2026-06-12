"""CLI for Borda net score baseline."""
import argparse
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from mwfas.baselines import order_by_borda_net_score_from_dimacs


def main():
    p = argparse.ArgumentParser(description="Borda net score ordering baseline")
    p.add_argument("--input", required=True, help="DIMACS .d instance file")
    p.add_argument("--output", default=None, help="Output ranking CSV path")
    p.add_argument("--summary-output", default=None, help="One-row metrics JSON path")
    args = p.parse_args()

    _, _, _, _, metrics = order_by_borda_net_score_from_dimacs(
        args.input, args.output
    )

    if args.summary_output:
        with open(args.summary_output, "w") as f:
            json.dump(metrics, f, indent=2)

    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
