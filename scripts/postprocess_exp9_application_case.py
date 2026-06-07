#!/usr/bin/env python3
"""
EXP9 postprocessor: summarize application case study results.

Inputs:
  experiments/exp9_application_case/summary/exp9_raw_summary.csv
  experiments/exp9_application_case/config/dataset_provenance.json

Outputs:
  experiments/exp9_application_case/summary/exp9_application_summary.csv
  experiments/exp9_application_case/summary/exp9_final_report.md
  paper/notes/exp9_application_case/README.md
  paper/tables/table_application_case.tex
"""
import csv
import json
import math
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
EXP_DIR = REPO / "experiments" / "exp9_application_case"
RAW_CSV = EXP_DIR / "summary" / "exp9_raw_summary.csv"
PROV_JSON = EXP_DIR / "config" / "dataset_provenance.json"


def safe_float(v):
    try:
        x = float(v)
        return x if math.isfinite(x) else None
    except (TypeError, ValueError):
        return None


def main():
    if not RAW_CSV.exists():
        print(f"Input not found: {RAW_CSV}")
        return

    with RAW_CSV.open(newline="") as f:
        rows = list(csv.DictReader(f))

    prov = {}
    if PROV_JSON.exists():
        prov = json.loads(PROV_JSON.read_text())

    # Group by instance
    instances = sorted(set(r["instance"] for r in rows))
    ok_rows = [r for r in rows if r.get("status") == "ok"]
    err_rows = [r for r in rows if r.get("status") == "error"]

    # Best algorithm per instance
    by_instance: dict[str, list] = {}
    for r in ok_rows:
        by_instance.setdefault(r["instance"], []).append(r)

    summary_rows = []
    for inst, inst_rows in by_instance.items():
        bws = {r["algorithm"]: safe_float(r["backward_weight"]) for r in inst_rows
               if safe_float(r["backward_weight"]) is not None}
        rts = {r["algorithm"]: safe_float(r["runtime_seconds"]) for r in inst_rows}
        if not bws:
            continue
        best_alg = min(bws, key=bws.__getitem__)
        ipsns_bw = bws.get("IPSNS")
        lrta_bw = bws.get("LR-TA")
        wmsf_bw = bws.get("WMSF")
        ref = inst_rows[0]
        summary_rows.append({
            "instance": inst,
            "dataset": ref["dataset"],
            "n": ref["n"],
            "m": ref["m"],
            "density": ref["density"],
            "total_weight": ref["total_weight"],
            "best_algorithm": best_alg,
            "best_bw": bws[best_alg],
            "ipsns_bw": ipsns_bw if ipsns_bw else "",
            "lrta_bw": lrta_bw if lrta_bw else "",
            "wmsf_bw": wmsf_bw if wmsf_bw else "",
            "ipsns_vs_lrta": (
                round((lrta_bw - ipsns_bw) / lrta_bw * 100, 3)
                if ipsns_bw and lrta_bw else ""
            ),
        })

    # Write application summary CSV
    summ_path = EXP_DIR / "summary" / "exp9_application_summary.csv"
    if summary_rows:
        with summ_path.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(summary_rows[0].keys()))
            w.writeheader()
            w.writerows(summary_rows)

    # Full report
    report_lines = ["# EXP9 Application Case Study — Final Report", "",
                    "## Dataset", "",
                    f"**{prov.get('dataset', 'Wikipedia Adminship Vote')}**", "",
                    f"Source: {prov.get('citation', 'Leskovec et al. WWW 2010')}", "",
                    f"Application framing: {prov.get('application_framing', '')}", ""]

    report_lines += ["## Algorithm results by instance", ""]
    for inst, inst_rows in by_instance.items():
        bws = {r["algorithm"]: safe_float(r["backward_weight"]) for r in inst_rows}
        rts = {r["algorithm"]: safe_float(r["runtime_seconds"]) for r in inst_rows}
        ref = inst_rows[0]
        report_lines += [
            f"### {inst}",
            f"n={ref['n']}, m={ref['m']}, density={ref['density']}, "
            f"total_weight={ref['total_weight']}",
            "",
            "| Algorithm | BW | Runtime (s) | Status |",
            "|---|---|---|---|",
        ]
        for r in sorted(inst_rows, key=lambda x: (safe_float(x["backward_weight"]) or 1e18)):
            bw = r["backward_weight"]
            rt = r["runtime_seconds"]
            st = r["status"]
            report_lines.append(f"| {r['algorithm']} | {bw} | {rt} | {st} |")
        report_lines.append("")

    report_lines += ["## Error summary", ""]
    if err_rows:
        for r in err_rows:
            report_lines.append(f"- {r['instance']} / {r['algorithm']}: {r['error'][:120]}")
    else:
        report_lines.append("No errors.")

    report_path = EXP_DIR / "summary" / "exp9_final_report.md"
    report_path.write_text("\n".join(report_lines) + "\n")
    print(f"Report written to {report_path}")

    # paper/notes
    notes_dir = REPO / "paper" / "notes" / "exp9_application_case"
    notes_dir.mkdir(parents=True, exist_ok=True)
    (notes_dir / "README.md").write_text("\n".join(report_lines) + "\n")

    # paper/tables/table_application_case.tex (for full instance only)
    full_rows = [r for r in summary_rows if "top50" in r.get("instance", "")]
    if full_rows:
        sr = full_rows[0]
        bws_all = {r["algorithm"]: safe_float(r["backward_weight"])
                   for r in by_instance.get(sr["instance"], [])
                   if safe_float(r["backward_weight"]) is not None}
        tables_dir = REPO / "paper" / "tables"
        tables_dir.mkdir(parents=True, exist_ok=True)
        tex = r"""\begin{table}[t]
\centering
\caption{Application case study: Wikipedia adminship vote network (EXP9).
The top-50 most-active users form a directed weighted graph where each arc
weight equals the number of endorsement votes cast. Backward weight (BW) counts
the total weight of arcs that violate the returned prestige ranking.
A minimum-BW ordering minimises reverse endorsements.}
\label{tab:application-case}
\begin{tabular}{lrr}
\toprule
Algorithm & BW & Runtime (s) \\
\midrule
"""
        order = ["IPSNS", "LR-TA", "WMSF", "DRMacIver/FAS",
                 "igraph_eades", "weighted_eades"]
        for alg in order:
            bw = bws_all.get(alg)
            rt_row = next((r for r in by_instance.get(sr["instance"], [])
                           if r["algorithm"] == alg), None)
            rt = safe_float(rt_row["runtime_seconds"]) if rt_row else None
            bw_str = f"{bw:,.0f}" if bw is not None else "---"
            rt_str = f"{rt:.2f}" if rt is not None else "---"
            label = alg.replace("_", r"\_")
            tex += f"{label} & {bw_str} & {rt_str} \\\\\n"
        tex += r"""\bottomrule
\multicolumn{3}{p{0.92\linewidth}}{\footnotesize
Instance: top-50 Wikipedia users by vote activity.
"""
        tex += f"$n={sr['n']}$ nodes, $m={sr['m']}$ arcs, density $={sr['density']}$, "
        tex += f"total weight $={int(float(sr['total_weight'])):,}$.} \\\\\n"
        tex += r"""\end{tabular}
\end{table}
"""
        (tables_dir / "table_application_case.tex").write_text(tex)
        print(f"LaTeX table written to {tables_dir / 'table_application_case.tex'}")


if __name__ == "__main__":
    main()
