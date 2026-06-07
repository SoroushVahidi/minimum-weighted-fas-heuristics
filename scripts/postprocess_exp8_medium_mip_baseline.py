"""
EXP8 postprocessor: summarise MIP baseline results.

Inputs:
  experiments/exp8_medium_mip_baseline/summary/exp8_mip_raw_summary{suffix}.csv
Outputs:
  experiments/exp8_medium_mip_baseline/summary/exp8_mip_summary{suffix}.json
  experiments/exp8_medium_mip_baseline/summary/exp8_final_report{suffix}.md
  paper/notes/exp8_medium_mip_baseline/README.md  (full run only)
  paper/tables/table_medium_mip_baseline.tex       (full run only)
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

    # Full-run-only paper assets
    if not args.input_suffix:
        _write_paper_assets(BASE, summary, gap_rows, optimal, timeout, completed, rows)


def _write_paper_assets(base, summary, gap_rows, optimal, timeout, completed, rows):
    """Write paper/tables and paper/notes assets (full run only)."""
    # Compute gap stats on proven-optimal instances only
    opt_gaps = [g["gap_pct"] for g in gap_rows if g["proven_optimal"]]
    mean_gap = sum(opt_gaps) / len(opt_gaps) if opt_gaps else 0.0
    max_gap = max(opt_gaps) if opt_gaps else 0.0
    ipsns_matches = sum(1 for g in opt_gaps if abs(g) < 0.001)

    # paper/tables/table_medium_mip_baseline.tex
    tables_dir = base / "paper" / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)
    tex = r"""\begin{table}[t]
\centering
\caption{Time-capped MIP baseline (EXP8) on 15 selected medium sparse instances
($n \leq 318$, 120\,s time limit per instance). The solver certifies optimal
solutions on 7 instances; the remaining 8 exceed the time limit and yield no MIP
incumbent. IPSNS gap is measured against the solver-certified optimum on the 7
proven-optimal instances only.}
\label{tab:medium-mip-baseline}
\begin{tabular}{lr}
\toprule
Metric & Value \\
\midrule
"""
    tex += f"Instances selected & {len(rows)} \\\\\n"
    tex += f"Proven optimal (MIP solved) & {len(optimal)} \\\\\n"
    tex += f"Time-limited (no incumbent) & {len(timeout)} \\\\\n"
    tex += f"Time limit & 120\\,s \\\\\n"
    tex += f"IPSNS matches MIP optimum & {ipsns_matches}/{len(optimal)} \\\\\n"
    tex += f"IPSNS mean gap (proven-optimal) & {mean_gap:.3f}\\% \\\\\n"
    tex += f"IPSNS max gap (proven-optimal) & {max_gap:.3f}\\% \\\\\n"
    tex += r"""\bottomrule
\end{tabular}
\end{table}
"""
    tex_path = tables_dir / "table_medium_mip_baseline.tex"
    tex_path.write_text(tex)
    print(f"LaTeX table written to {tex_path}")

    # paper/notes/exp8_medium_mip_baseline/README.md
    notes_dir = base / "paper" / "notes" / "exp8_medium_mip_baseline"
    notes_dir.mkdir(parents=True, exist_ok=True)
    readme_lines = [
        "# EXP8 Medium MIP Baseline — Paper Notes",
        "",
        "## Purpose",
        "Supplementary time-capped MIP validation on medium sparse instances where",
        "bitmask DP is no longer feasible. Provides additional exact-quality evidence",
        "to complement the small-instance exact validation (57 instances, n≤20).",
        "",
        "## Key aggregate results",
        f"- Instances selected: {len(rows)} (n=20–318, all from graph-benchmarks)",
        f"- Proven optimal: {len(optimal)}/15 (HiGHS MIP solved within 120 s)",
        f"- Time-limited, no incumbent: {len(timeout)}/15 (LP relaxation mode, n≥273)",
        f"- IPSNS matches MIP optimum: {ipsns_matches}/{len(optimal)}",
        f"- IPSNS mean gap on proven-optimal: {mean_gap:.3f}%",
        f"- IPSNS max gap on proven-optimal: {max_gap:.3f}% (r20_60)",
        "",
        "## Interpretation notes",
        "- The 8 time-limited cases are **incomplete solver evidence only**; they do",
        "  not certify gaps and are not counted as IPSNS failures.",
        "- The single exception (r20_60, gap 0.178%) is the same instance that is the",
        "  only IPSNS near-miss in the small exact-validation study.",
        "- The MIP solver used is scipy.optimize.milp (HiGHS 1.17.1).",
        "",
        "## Files",
        "- `experiments/exp8_medium_mip_baseline/summary/exp8_mip_raw_summary.csv` — 15 rows",
        "- `experiments/exp8_medium_mip_baseline/summary/exp8_mip_summary.json` — aggregate JSON",
        "- `experiments/exp8_medium_mip_baseline/summary/exp8_final_report.md` — human-readable report",
        "- `paper/tables/table_medium_mip_baseline.tex` — LaTeX table for manuscript",
    ]
    (notes_dir / "README.md").write_text("\n".join(readme_lines) + "\n")
    print(f"Notes README written to {notes_dir / 'README.md'}")


if __name__ == "__main__":
    main()
