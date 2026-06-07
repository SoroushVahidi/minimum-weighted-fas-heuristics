"""
EXP8 postprocessor: summarise MIP baseline results.

Inputs:
  experiments/exp8_medium_mip_baseline/summary/exp8_mip_raw_summary{suffix}.csv
Outputs:
  experiments/exp8_medium_mip_baseline/summary/exp8_mip_summary{suffix}.json
  experiments/exp8_medium_mip_baseline/summary/exp8_final_report{suffix}.md
"""
import argparse
import csv
import json
import math
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
OUT_DIR = BASE / "experiments/exp8_medium_mip_baseline/summary"


def load_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def safe_float(v):
    try:
        x = float(v)
        return x if math.isfinite(x) else None
    except (TypeError, ValueError):
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-suffix", default="",
                    help="Suffix used in run script (e.g. 'smoke')")
    args = ap.parse_args()

    suffix = f"_{args.input_suffix}" if args.input_suffix else ""
    raw_csv = OUT_DIR / f"exp8_mip_raw_summary{suffix}.csv"

    if not raw_csv.exists():
        print(f"Input not found: {raw_csv}")
        return

    rows = load_csv(raw_csv)

    completed = [r for r in rows if r.get("status") not in ("error", "skip", "", "solver_error")]
    optimal = [r for r in completed if str(r.get("proven_optimal", "")).lower() in ("true", "1")]
    timeout = [r for r in completed if r.get("status") == "time_limit"]
    errors = [r for r in rows if r.get("status") in ("error", "solver_error")]
    skipped = [r for r in rows if r.get("status") == "skip"]

    runtimes = [safe_float(r.get("runtime_seconds")) for r in completed]
    runtimes = [x for x in runtimes if x is not None]
    mean_rt = sum(runtimes) / len(runtimes) if runtimes else None

    # IPSNS vs MIP incumbent
    gap_rows = []
    for r in completed:
        bw_inc = safe_float(r.get("mip_bw_incumbent"))
        bw_ipsns = safe_float(r.get("ipsns_bw"))
        if bw_inc is not None and bw_ipsns is not None and bw_inc > 0:
            gap = (bw_ipsns - bw_inc) / bw_inc * 100
            gap_rows.append({
                "instance": r["instance"], "n": r.get("n"), "mode": r.get("mode"),
                "mip_bw": bw_inc, "ipsns_bw": bw_ipsns, "gap_pct": round(gap, 4),
                "proven_optimal": str(r.get("proven_optimal", "")).lower() in ("true", "1"),
            })

    ipsns_matches = sum(1 for g in gap_rows if abs(g["gap_pct"]) < 0.001)
    ipsns_better = sum(1 for g in gap_rows if g["gap_pct"] < -0.001)

    # IPSNS vs LP bound
    bound_rows = []
    for r in completed:
        bw_bound = safe_float(r.get("mip_dual_bound_bw"))
        bw_ipsns = safe_float(r.get("ipsns_bw"))
        if bw_bound is not None and bw_ipsns is not None and abs(bw_bound) > 0:
            gap = (bw_ipsns - bw_bound) / abs(bw_bound) * 100
            bound_rows.append({
                "instance": r["instance"], "gap_to_bound_pct": round(gap, 4),
                "mode": r.get("mode"),
            })

    summary = {
        "total_instances": len(rows),
        "completed": len(completed),
        "proven_optimal": len(optimal),
        "time_limit_hit": len(timeout),
        "errors": len(errors),
        "skipped": len(skipped),
        "mean_runtime_seconds": round(mean_rt, 2) if mean_rt else None,
        "ipsns_matches_mip_incumbent": ipsns_matches,
        "ipsns_better_than_mip_incumbent": ipsns_better,
        "gap_vs_incumbent": gap_rows,
        "gap_vs_bound": bound_rows,
    }

    (OUT_DIR / f"exp8_mip_summary{suffix}.json").write_text(
        json.dumps(summary, indent=2)
    )

    # Final report
    lines = [
        f"# EXP8 MIP Baseline — Final Report{' (' + args.input_suffix + ')' if args.input_suffix else ''}",
        "",
        "## Summary",
        f"- Instances: {len(rows)} total, {len(completed)} completed",
        f"- Proven optimal: {len(optimal)}",
        f"- Time limit hit: {len(timeout)}",
        f"- Errors / skipped: {len(errors)} / {len(skipped)}",
        f"- Mean runtime: {round(mean_rt, 1) if mean_rt else 'N/A'} s",
        "",
        "## IPSNS vs MIP Incumbent",
        f"- IPSNS matches MIP incumbent (gap < 0.001%): {ipsns_matches}/{len(gap_rows)}",
        f"- IPSNS better than MIP incumbent: {ipsns_better}/{len(gap_rows)}",
        "",
        "| Instance | n | Mode | MIP BW | IPSNS BW | Gap% | Optimal |",
        "|---|---|---|---|---|---|---|",
    ]
    for g in sorted(gap_rows, key=lambda x: int(x.get("n") or 0)):
        opt_str = "Yes" if g["proven_optimal"] else "No"
        lines.append(
            f"| {g['instance']} | {g['n']} | {g['mode']} | {g['mip_bw']:.1f} "
            f"| {g['ipsns_bw']:.1f} | {g['gap_pct']:.4f} | {opt_str} |"
        )

    if bound_rows:
        lines += [
            "",
            "## IPSNS vs LP/MIP Lower Bound",
            "| Instance | Mode | IPSNS Gap to Bound (%) |",
            "|---|---|---|",
        ]
        for g in bound_rows:
            lines.append(f"| {g['instance']} | {g['mode']} | {g['gap_to_bound_pct']:.4f} |")

    lines += [
        "",
        "## Interpretation",
        f"- {len(optimal)} instance(s) proven optimal; IPSNS matches optimal on {ipsns_matches} of those.",
        f"- LP relaxation bounds available for LP-mode instances (n > 200).",
    ]

    report_path = OUT_DIR / f"exp8_final_report{suffix}.md"
    report_path.write_text("\n".join(lines) + "\n")

    print(f"Summary written to {OUT_DIR / f'exp8_mip_summary{suffix}.json'}")
    print(f"Report written to {report_path}")
    print(f"\nKey findings:")
    print(f"  Completed: {len(completed)}/{len(rows)}")
    print(f"  Proven optimal: {len(optimal)}")
    print(f"  IPSNS matches MIP: {ipsns_matches}/{len(gap_rows)}")


if __name__ == "__main__":
    main()
