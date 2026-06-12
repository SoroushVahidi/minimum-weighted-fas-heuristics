"""CLI for weighted Eades–Lin–Smyth ordering baseline."""
import argparse
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from mwfas.baselines import weighted_eades_ordering_from_dimacs


def main():
    p = argparse.ArgumentParser(
        description="Weighted Eades-Lin-Smyth greedy ordering (in-repo weighted adaptation)"
    )
    p.add_argument("--input", required=True, help="DIMACS .d instance file")
    p.add_argument("--output", default=None, help="Output ranking CSV path")
    p.add_argument("--summary-output", default=None, help="One-row metrics JSON path")
    args = p.parse_args()

    _, _, _, _, metrics = weighted_eades_ordering_from_dimacs(
        args.input, args.output
    )

    if args.summary_output:
        with open(args.summary_output, "w") as f:
            json.dump(metrics, f, indent=2)

    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
