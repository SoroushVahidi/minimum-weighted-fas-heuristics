#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import math
import re
from datetime import datetime, timezone
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
PAPER = ROOT / "paper"
TABLES_DIR = PAPER / "tables"
FIGURES_DIR = PAPER / "figures"
NOTES_DIR = PAPER / "notes"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text())


def read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def fmt_int(value: float | int) -> str:
    return f"{int(round(float(value))):,}"


def fmt_float(value: float, digits: int = 2) -> str:
    return f"{value:.{digits}f}"


def approx_equal(a: float, b: float, tol: float = 1e-6) -> bool:
    return abs(float(a) - float(b)) <= tol


def latex_escape(text: str) -> str:
    return (
        text.replace("\\", "\\textbackslash{}")
        .replace("&", "\\&")
        .replace("%", "\\%")
        .replace("_", "\\_")
        .replace("#", "\\#")
    )


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def parse_exp5_family_rows(report_text: str) -> dict[str, dict[str, float | int]]:
    family_rows: dict[str, dict[str, float | int]] = {}
    in_family_table = False
    for raw_line in report_text.splitlines():
        line = raw_line.strip()
        if line == "### Per-Family Breakdown":
            in_family_table = True
            continue
        if in_family_table and line.startswith("### "):
            break
        if not in_family_table or not line.startswith("|"):
            continue
        if "Family" in line or "---" in line:
            continue
        parts = [p.strip().replace("**", "") for p in line.strip("|").split("|")]
        if len(parts) != 6:
            continue
        family = parts[0]
        if family not in {"SGB", "IO", "RandA1"}:
            continue
        ipsns_best = int(parts[2].split("/")[0])
        drmaciver_best = int(parts[3].split("/")[0])
        family_rows[family] = {
            "ipsns_best": ipsns_best,
            "drmaciver_best": drmaciver_best,
            "ipsns_mean_bw": float(parts[4].replace(",", "")),
            "drmaciver_mean_bw": float(parts[5].replace(",", "")),
        }
    return family_rows


def build_tables_and_figures() -> None:
    sources = {
        "digest_json": ROOT / "experiments/combined/summary/manuscript_results_digest.json",
        "exp1b_stats": ROOT / "experiments/exp1b_core_benchmark_full_wmsf_seed/summary/exp1b_core_benchmark_stats.json",
        "exp2_stats": ROOT / "experiments/exp2_ablation/summary/exp2_ablation_stats.json",
        "exp3_stats": ROOT / "experiments/exp3_exact_small/summary/exp3_exact_stats.json",
        "exp4_stats": ROOT / "experiments/exp4_external_baselines/summary/exp4_external_stats.json",
        "exp4_table": ROOT / "experiments/exp4_external_baselines/tables/exp4_external_paper_summary.csv",
        "exp5_stats": ROOT / "experiments/exp5_lolib_dense/summary/exp5_lolib_stats.json",
        "exp5_table": ROOT / "experiments/exp5_lolib_dense/tables/exp5_lolib_paper_summary.csv",
        "exp5_report": ROOT / "experiments/exp5_lolib_dense/summary/exp5_final_report.md",
    }

    digest = read_json(sources["digest_json"])
    exp1b = read_json(sources["exp1b_stats"])
    exp2 = read_json(sources["exp2_stats"])
    exp3 = read_json(sources["exp3_stats"])
    exp4 = read_json(sources["exp4_stats"])
    exp4_table = read_csv(sources["exp4_table"])
    exp5 = read_json(sources["exp5_stats"])
    exp5_table = read_csv(sources["exp5_table"])
    exp5_report_text = sources["exp5_report"].read_text()
    exp5_families = parse_exp5_family_rows(exp5_report_text)

    checks: list[dict[str, object]] = []

    def record_check(name: str, observed: object, expected: object, ok: bool) -> None:
        checks.append({"name": name, "observed": observed, "expected": expected, "ok": ok})

    record_check("EXP1b instances", exp1b["n_instances"], 105, exp1b["n_instances"] == 105)
    record_check("EXP1b nonempty errors", exp1b["n_nonempty_errors"], 0, exp1b["n_nonempty_errors"] == 0)
    record_check(
        "EXP1b incumbent violations",
        exp1b["incumbent_protection_violations_external"],
        0,
        exp1b["incumbent_protection_violations_external"] == 0,
    )
    record_check(
        "EXP2 successful runs",
        sum(int(v["n_ok"]) for v in exp2.values()),
        80,
        sum(int(v["n_ok"]) for v in exp2.values()) == 80,
    )
    record_check("EXP3 standard instances", exp3["n_instances_standard"], 57, exp3["n_instances_standard"] == 57)
    record_check(
        "EXP3 IPSNS optimal",
        exp3["standard_instances"]["ipsns_optimal"],
        "56/57 (98.2%)",
        exp3["standard_instances"]["ipsns_optimal"] == "56/57 (98.2%)",
    )
    record_check(
        "EXP3 IPSNS mean gap pct",
        exp3["standard_instances"]["ipsns_mean_gap_pct"],
        "0.0006%",
        exp3["standard_instances"]["ipsns_mean_gap_pct"] == "0.0006%",
    )
    record_check("EXP4 standard instances", exp4["n_standard"], 97, exp4["n_standard"] == 97)
    record_check(
        "EXP4 IPSNS complete",
        int(exp4["per_algorithm"]["ipsns_full"]["n_complete"]),
        97,
        int(exp4["per_algorithm"]["ipsns_full"]["n_complete"]) == 97,
    )
    record_check(
        "EXP4 DRMaciver complete",
        int(exp4["per_algorithm"]["drmaciver_fas"]["n_complete"]),
        93,
        int(exp4["per_algorithm"]["drmaciver_fas"]["n_complete"]) == 93,
    )
    record_check(
        "EXP4 DRMaciver relative gap pct",
        round(float(exp4["per_algorithm"]["drmaciver_fas"]["mean_rel_gain_ipsns_pct"]), 2),
        21.61,
        approx_equal(round(float(exp4["per_algorithm"]["drmaciver_fas"]["mean_rel_gain_ipsns_pct"]), 2), 21.61, 1e-2),
    )
    record_check("EXP5 instances", exp5["n_instances_total"], 50, exp5["n_instances_total"] == 50)
    record_check("EXP5 IPSNS best count", exp5["ipsns_global_best"], 5, exp5["ipsns_global_best"] == 5)
    record_check(
        "EXP5 DRMaciver best count",
        int(exp5_table.loc[exp5_table["algorithm"] == "drmaciver_fas", "n_global_best"].iloc[0]),
        45,
        int(exp5_table.loc[exp5_table["algorithm"] == "drmaciver_fas", "n_global_best"].iloc[0]) == 45,
    )
    record_check(
        "EXP5 DRMaciver mean BW",
        round(float(exp5_table.loc[exp5_table["algorithm"] == "drmaciver_fas", "mean_backward_weight"].iloc[0]), 0),
        571687.0,
        approx_equal(
            round(float(exp5_table.loc[exp5_table["algorithm"] == "drmaciver_fas", "mean_backward_weight"].iloc[0]), 0),
            571687.0,
            1.0,
        ),
    )
    record_check(
        "EXP5 family rows parsed",
        sorted(exp5_families.keys()),
        ["IO", "RandA1", "SGB"],
        sorted(exp5_families.keys()) == ["IO", "RandA1", "SGB"],
    )

    # Table: experiment overview
    table_experiment_overview = r"""\begin{table}[t]
\centering
\small
\caption{Overview of the five committed experimental components used in the manuscript. EXP1b checks seed safety on the full internal benchmark; EXP2 studies design choices; EXP3 validates small instances against exact optimization; EXP4 compares against external baselines on the primary sparse benchmark; and EXP5 tests transfer to dense LOLIB instances.}
\label{tab:experiment-overview}
\resizebox{\linewidth}{!}{%
\begin{tabular}{p{0.09\linewidth}p{0.40\linewidth}p{0.10\linewidth}p{0.25\linewidth}}
\toprule
Experiment & Purpose & Instances & Main setting \\
\midrule
EXP1b & Internal safety check for LR-TA, WMSF, and IPSNS & 105 & sparse weighted DIMACS digraphs \\
EXP2 & Add-back, refinement, and iteration ablation & 10 & representative sparse subset \\
EXP3 & Exact validation against bitmask dynamic programming & 57 & standard nonnegative instances with $n \le 20$ \\
EXP4 & External baseline comparison on the primary claim-bearing benchmark & 97 & standard nonnegative sparse instances \\
EXP5 & Dense transfer test and scope boundary analysis & 50 & LOLIB complete weighted ordering instances \\
\bottomrule
\end{tabular}
}
\end{table}
"""
    write_text(TABLES_DIR / "table_experiment_overview.tex", table_experiment_overview)

    # Table: EXP4 sparse baselines
    exp4_order = [
        "ipsns_full",
        "lrta_full",
        "wmsf_seed",
        "drmaciver_fas",
        "igraph_approx_eades",
        "weighted_eades",
        "borda_net_score",
        "random_multistart",
    ]
    exp4_labels = {
        "ipsns_full": "IPSNS (ours)",
        "lrta_full": "LR-TA (ours)",
        "wmsf_seed": "WMSF seed",
        "drmaciver_fas": "DRMacIver/FAS",
        "igraph_approx_eades": "igraph Eades",
        "weighted_eades": "Weighted Eades",
        "borda_net_score": "Borda net score",
        "random_multistart": "Random multistart",
    }
    exp4_rows = []
    for alg in exp4_order:
        row = exp4_table.loc[exp4_table["algorithm"] == alg].iloc[0]
        exp4_rows.append(
            f"{exp4_labels[alg]} & {int(row['n_complete'])}/{int(row['n_total'])} & {fmt_int(row['mean_bw'])} & "
            f"{fmt_float(float(row['mean_runtime_s']), 2)} & {int(row['n_times_best'])} & {fmt_float(float(row['mean_rel_gain_ipsns_pct']), 2)}\\% \\\\"
        )
    exp4_tex = "\n".join(
        [
            r"\begin{table}[t]",
            r"\centering",
            r"\small",
            r"\caption{Comparison on the 97 standard nonnegative sparse instances used for the primary claim-bearing benchmark. BW denotes backward weight; lower values are better. Relative excess is the mean percentage by which an algorithm's BW exceeds IPSNS on completed instances.}",
            r"\label{tab:sparse-external-baselines}",
            r"\resizebox{\linewidth}{!}{%",
            r"\begin{tabular}{lrrrrr}",
            r"\toprule",
            r"Method & Complete & Mean BW & Mean RT (s) & Best & Relative excess \\",
            r"\midrule",
            *exp4_rows,
            r"\bottomrule",
            r"\end{tabular}",
            r"}",
            r"\par\vspace{2pt}\parbox{0.94\linewidth}{\footnotesize\raggedright DRMaciver is the strongest external comparator on this benchmark, but it completes 93 of 97 instances because two DAG cases return empty-tournament errors and two large sparse instances time out in the wrapper used here.}",
            r"\end{table}",
            "",
        ]
    )
    write_text(TABLES_DIR / "table_sparse_external_baselines.tex", exp4_tex)

    # Table: EXP3 exact validation
    exp3_tex = "\n".join(
        [
            r"\begin{table}[t]",
            r"\centering",
            r"\caption{Exact validation on the 57 standard nonnegative instances with $n \le 20$. Mean gap is measured against exact bitmask dynamic programming on each instance.}",
            r"\label{tab:exact-validation}",
            r"\begin{tabular}{lrrr}",
            r"\toprule",
            r"Method & Optimal & Optimality rate & Mean gap \\",
            r"\midrule",
            r"IPSNS (ours) & 56/57 & 98.2\% & 0.0006\% \\",
            r"LR-TA (ours) & 55/57 & 96.5\% & 0.0590\% \\",
            r"WMSF seed & 51/57 & 89.5\% & 0.0961\% \\",
            r"\bottomrule",
            r"\end{tabular}",
            r"\par\vspace{2pt}\parbox{0.94\linewidth}{\footnotesize This table supports empirical near-optimality on small instances only; it does not imply a general approximation guarantee. The only IPSNS near-miss is instance \texttt{r20\_60}.}",
            r"\end{table}",
            "",
        ]
    )
    write_text(TABLES_DIR / "table_exact_validation.tex", exp3_tex)

    # Table: EXP2 ablation
    exp2_rows = [
        ("lr_no_addback", "LR without add-back"),
        ("lrta_full", "LR-TA"),
        ("wmsf_seed", "WMSF seed"),
        ("best_seed_no_lns", "Best seed, no refinement"),
        ("ipsns_50iters", "IPSNS, 50 iterations"),
        ("ipsns_full", "IPSNS, 400 iterations (default)"),
        ("ipsns_no_scc_priority", "IPSNS, no SCC priority"),
    ]
    base_lrta = float(exp2["lrta_full"]["mean_bw"])
    ablation_rows = []
    for key, label in exp2_rows:
        stats = exp2[key]
        rel_vs_lrta = ((float(stats["mean_bw"]) - base_lrta) / base_lrta) * 100.0
        ablation_rows.append(
            f"{label} & {fmt_float(float(stats['mean_bw']), 1)} & {rel_vs_lrta:+.2f}\\% & {fmt_float(float(stats['mean_runtime']), 3)} \\\\"
        )
    exp2_tex = "\n".join(
        [
            r"\begin{table}[t]",
            r"\centering",
            r"\caption{Ablation study on 10 representative sparse instances. Relative change is measured against LR-TA. Negative percentages indicate improvement.}",
            r"\label{tab:ablation}",
            r"\begin{tabular}{lrrr}",
            r"\toprule",
            r"Variant & Mean BW & Relative change & Mean RT (s) \\",
            r"\midrule",
            *ablation_rows,
            r"\bottomrule",
            r"\end{tabular}",
            r"\par\vspace{2pt}\parbox{0.94\linewidth}{\footnotesize The add-back phase accounts for the largest mean improvement (about 5.9\%), while IPSNS contributes a further 0.75\% on this subset. The equal 50- and 400-iteration means support the default iteration budget only as subset-level evidence, not as a universal tuning rule.}",
            r"\end{table}",
            "",
        ]
    )
    write_text(TABLES_DIR / "table_ablation.tex", exp2_tex)

    # Table: EXP5 scope
    exp5_order = [
        "drmaciver_fas",
        "ipsns_full",
        "lrta_full",
        "wmsf_seed",
        "igraph_approx_eades",
        "weighted_eades",
        "random_multistart",
        "borda_net_score",
    ]
    exp5_labels = {
        "drmaciver_fas": "DRMacIver/FAS",
        "ipsns_full": "IPSNS (ours)",
        "lrta_full": "LR-TA (ours)",
        "wmsf_seed": "WMSF seed",
        "igraph_approx_eades": "igraph Eades",
        "weighted_eades": "Weighted Eades",
        "random_multistart": "Random multistart",
        "borda_net_score": "Borda net score",
    }
    exp5_rows = []
    for alg in exp5_order:
        row = exp5_table.loc[exp5_table["algorithm"] == alg].iloc[0]
        exp5_rows.append(
            f"{exp5_labels[alg]} & {fmt_int(row['mean_backward_weight'])} & {int(row['n_global_best'])}/50 & "
            f"{fmt_float(float(row['mean_runtime_s']), 2)} \\\\"
        )
    family_rows = []
    for family in ["SGB", "IO", "RandA1"]:
        vals = exp5_families[family]
        family_rows.append(
            f"{family} & {int(vals['ipsns_best'])}/{25 if family == 'SGB' else 10 if family == 'IO' else 15} & "
            f"{int(vals['drmaciver_best'])}/{25 if family == 'SGB' else 10 if family == 'IO' else 15} & "
            f"{fmt_int(vals['ipsns_mean_bw'])} / {fmt_int(vals['drmaciver_mean_bw'])} \\\\"
        )
    exp5_tex = "\n".join(
        [
            r"\begin{table}[t]",
            r"\centering",
            r"\small",
            r"\caption{Dense LOLIB transfer test on 50 complete weighted ordering instances. Lower BW is better. The upper panel reports overall performance; the lower panel isolates the two most relevant methods by family to make the dense-scope boundary explicit.}",
            r"\label{tab:lolib-scope}",
            r"\resizebox{\linewidth}{!}{%",
            r"\begin{tabular}{lrrr}",
            r"\toprule",
            r"Method & Mean BW & Best & Mean RT (s) \\",
            r"\midrule",
            *exp5_rows,
            r"\midrule",
            r"\multicolumn{4}{l}{\textit{Family breakdown for IPSNS and DRMaciver}} \\",
            r"Family & IPSNS best & DRMaciver best & Mean BW (IPSNS / DRMaciver) \\",
            *family_rows,
            r"\bottomrule",
            r"\end{tabular}",
            r"}",
            r"\par\vspace{2pt}\parbox{0.94\linewidth}{\footnotesize\raggedright DRMaciver is tournament-native and is the best overall dense LOLIB method in this study (45/50 instances, 3.88\% lower mean BW than IPSNS). EXP5 is therefore a transfer test and scope boundary, not evidence for universal dominance on dense linear-ordering problems.}",
            r"\end{table}",
            "",
        ]
    )
    write_text(TABLES_DIR / "table_lolib_scope.tex", exp5_tex)

    # Figures
    plt.rcParams.update(
        {
            "font.size": 9,
            "axes.labelsize": 9,
            "axes.titlesize": 9,
            "legend.fontsize": 8,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
        }
    )

    # Figure 1: EXP4 relative excess vs IPSNS
    rel_fig = exp4_table.copy()
    rel_fig["label"] = rel_fig["algorithm"].map(exp4_labels)
    rel_fig = rel_fig.set_index("algorithm").loc[exp4_order].reset_index()
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    colors = ["0.2"] + ["0.55"] * (len(rel_fig) - 1)
    ax.bar(rel_fig["label"], rel_fig["mean_rel_gain_ipsns_pct"], color=colors, edgecolor="black", linewidth=0.5)
    ax.set_ylabel("Mean BW excess over IPSNS (%)")
    ax.set_ylim(bottom=0)
    ax.tick_params(axis="x", rotation=35)
    ax.set_axisbelow(True)
    ax.grid(axis="y", color="0.88", linewidth=0.6)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "exp4_relative_bw.pdf")
    plt.close(fig)

    # Figure 2: EXP4 win counts
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    ax.bar(rel_fig["label"], rel_fig["n_times_best"], color="0.6", edgecolor="black", linewidth=0.5)
    ax.set_ylabel("Number of global-best instances")
    ax.set_ylim(0, 100)
    ax.tick_params(axis="x", rotation=35)
    ax.set_axisbelow(True)
    ax.grid(axis="y", color="0.88", linewidth=0.6)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "exp4_win_counts.pdf")
    plt.close(fig)

    # Figure 3: EXP5 family scope
    families = ["SGB", "IO", "RandA1"]
    ipsns_best = [int(exp5_families[f]["ipsns_best"]) for f in families]
    dr_best = [int(exp5_families[f]["drmaciver_best"]) for f in families]
    x = range(len(families))
    width = 0.36
    fig, ax = plt.subplots(figsize=(5.6, 3.2))
    ax.bar([i - width / 2 for i in x], ipsns_best, width=width, label="IPSNS", color="0.65", edgecolor="black", linewidth=0.5)
    ax.bar([i + width / 2 for i in x], dr_best, width=width, label="DRMacIver/FAS", color="0.25", edgecolor="black", linewidth=0.5)
    ax.set_xticks(list(x))
    ax.set_xticklabels(families)
    ax.set_ylabel("Global-best instances")
    ax.set_ylim(0, 26)
    ax.legend(frameon=False, loc="upper left")
    ax.set_axisbelow(True)
    ax.grid(axis="y", color="0.88", linewidth=0.6)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "exp5_lolib_scope.pdf")
    plt.close(fig)

    generated_files = [
        str(TABLES_DIR / "table_experiment_overview.tex"),
        str(TABLES_DIR / "table_sparse_external_baselines.tex"),
        str(TABLES_DIR / "table_exact_validation.tex"),
        str(TABLES_DIR / "table_ablation.tex"),
        str(TABLES_DIR / "table_lolib_scope.tex"),
        str(FIGURES_DIR / "exp4_relative_bw.pdf"),
        str(FIGURES_DIR / "exp4_win_counts.pdf"),
        str(FIGURES_DIR / "exp5_lolib_scope.pdf"),
    ]

    provenance = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "script": str(Path(__file__).relative_to(ROOT)),
        "source_files": {k: str(v.relative_to(ROOT)) for k, v in sources.items()},
        "checks": checks,
        "generated_files": [str(Path(p).relative_to(ROOT)) for p in generated_files],
        "notes": [
            "EXP4 tables and figures are generated from the committed paper summary CSV.",
            "EXP5 overall metrics are generated from the committed paper summary CSV.",
            "EXP5 per-family DRMaciver and IPSNS means/best counts are parsed from the committed final report because the compact paper summary CSV does not include the family-level DRMaciver rows.",
            "No experiment values are inferred from uncommitted files.",
        ],
    }
    write_text(NOTES_DIR / "results_asset_provenance.json", json.dumps(provenance, indent=2))

    md_lines = [
        "# Results Asset Provenance",
        "",
        f"- Generated at (UTC): `{provenance['generated_at_utc']}`",
        f"- Script: `{provenance['script']}`",
        "",
        "## Source files",
        "",
    ]
    for key, value in provenance["source_files"].items():
        md_lines.append(f"- `{key}`: `{value}`")
    md_lines.extend(["", "## Verification checks", "", "| Check | Observed | Expected | Status |", "|---|---:|---:|---|"])
    for check in checks:
        status = "ok" if check["ok"] else "mismatch"
        md_lines.append(
            f"| {check['name']} | `{check['observed']}` | `{check['expected']}` | {status} |"
        )
    md_lines.extend(["", "## Generated files", ""])
    for path in provenance["generated_files"]:
        md_lines.append(f"- `{path}`")
    md_lines.extend(["", "## Notes", ""])
    for note in provenance["notes"]:
        md_lines.append(f"- {note}")
    write_text(NOTES_DIR / "results_asset_provenance.md", "\n".join(md_lines) + "\n")


if __name__ == "__main__":
    build_tables_and_figures()
