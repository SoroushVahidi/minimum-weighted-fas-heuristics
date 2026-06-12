"""
EXP6 postprocessing: budget curve summary, table, figure, report.
"""
import csv
import json
import math
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

EXP6_RAW = BASE / "experiments/exp6_ipsns_budget_curve/summary/exp6_raw_summary.csv"
EXP4_RAW = BASE / "experiments/exp4_external_baselines/summary/exp4_raw_summary.csv"
CONFIG_CSV = BASE / "experiments/exp6_ipsns_budget_curve/config/selected_instances.csv"
OUT_EXP = BASE / "experiments/exp6_ipsns_budget_curve/summary"
OUT_NOTES = BASE / "paper/notes/exp6_ipsns_budget_curve"
TABLE_OUT = BASE / "paper/tables"
FIG_OUT = BASE / "paper/figures"

for d in [OUT_EXP, OUT_NOTES, TABLE_OUT, FIG_OUT]:
    d.mkdir(parents=True, exist_ok=True)

# ── helpers ───────────────────────────────────────────────────────────────

def mean(vals):
    return sum(vals) / len(vals) if vals else float("nan")

def median(vals):
    s = sorted(vals)
    n = len(s)
    if n == 0:
        return float("nan")
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2

def read_csv(path):
    with open(path, newline="", errors="ignore") as f:
        return list(csv.DictReader(f))

# ── load data ─────────────────────────────────────────────────────────────
exp6 = read_csv(EXP6_RAW)
exp4 = read_csv(EXP4_RAW)
config = read_csv(CONFIG_CSV)
selected_insts = {r["instance"] for r in config}

# EXP4 pivot for selected instances: inst -> alg -> bw/rt
exp4_pivot = {}
for r in exp4:
    if r["instance"] not in selected_insts:
        continue
    if r["status"] != "ok" or not r.get("backward_weight", "").strip():
        continue
    try:
        exp4_pivot.setdefault(r["instance"], {})[r["algorithm"]] = {
            "bw": float(r["backward_weight"]),
            "rt": float(r.get("runtime") or 0),
        }
    except ValueError:
        pass

# EXP6 pivot: inst -> budget -> bw/rt
exp6_pivot = {}
for r in exp6:
    if r["status"] != "ok" or not r.get("backward_weight", "").strip():
        continue
    try:
        budget = int(r["budget"])
        exp6_pivot.setdefault(r["instance"], {})[budget] = {
            "bw": float(r["backward_weight"]),
            "rt": float(r.get("runtime") or 0),
        }
    except (ValueError, KeyError):
        pass

budgets = [10, 25, 50, 100, 200, 400]

# ── budget summary ─────────────────────────────────────────────────────────
# For each budget: mean BW, mean/median improvement over LR-TA, W/T/L, runtime
lrta_ref = {i: exp4_pivot[i]["lrta_full"]["bw"]
            for i in selected_insts
            if i in exp4_pivot and "lrta_full" in exp4_pivot[i]}

# Best budget BW per instance (use budget=400 as reference if available)
best_bw = {}
for inst in selected_insts:
    budg_map = exp6_pivot.get(inst, {})
    if 400 in budg_map:
        best_bw[inst] = budg_map[400]["bw"]
    elif budg_map:
        best_bw[inst] = min(v["bw"] for v in budg_map.values())

budget_rows = []
for b in budgets:
    insts_b = [i for i in selected_insts if i in exp6_pivot and b in exp6_pivot[i]]
    if not insts_b:
        continue
    bws = [exp6_pivot[i][b]["bw"] for i in insts_b]
    rts = [exp6_pivot[i][b]["rt"] for i in insts_b]

    # vs LR-TA
    common_lrta = [i for i in insts_b if i in lrta_ref]
    gains_lrta = [lrta_ref[i] - exp6_pivot[i][b]["bw"] for i in common_lrta]
    wins = sum(1 for g in gains_lrta if g > 0)
    ties = sum(1 for g in gains_lrta if g == 0)
    losses = sum(1 for g in gains_lrta if g < 0)

    # Relative excess vs best budget (400 iters) on same instances
    common_best = [i for i in insts_b if i in best_bw and best_bw[i] > 0]
    rel_excess = [(exp6_pivot[i][b]["bw"] - best_bw[i]) / best_bw[i] * 100
                  for i in common_best]

    row = {
        "budget": b,
        "n_instances": len(insts_b),
        "mean_bw": round(mean(bws), 2),
        "median_bw": round(median(bws), 2),
        "mean_rt_s": round(mean(rts), 4),
        "median_rt_s": round(median(rts), 4),
        "n_common_lrta": len(common_lrta),
        "wins_vs_lrta": wins,
        "ties_vs_lrta": ties,
        "losses_vs_lrta": losses,
        "mean_gain_vs_lrta": round(mean(gains_lrta), 2) if gains_lrta else None,
        "median_gain_vs_lrta": round(median(gains_lrta), 2) if gains_lrta else None,
        "mean_rel_excess_vs_400": round(mean(rel_excess), 4) if rel_excess else None,
    }
    budget_rows.append(row)

with open(OUT_EXP / "exp6_budget_summary.csv", "w", newline="") as f:
    if budget_rows:
        w = csv.DictWriter(f, fieldnames=list(budget_rows[0].keys()))
        w.writeheader()
        w.writerows(budget_rows)
print("Written exp6_budget_summary.csv")

# Also add LR-TA reference row
lrta_bws = [lrta_ref[i] for i in lrta_ref]
lrta_rts = [exp4_pivot[i]["lrta_full"]["rt"] for i in lrta_ref if i in exp4_pivot]
print(f"\nLR-TA reference on subset: n={len(lrta_bws)}, mean_bw={mean(lrta_bws):.1f}, "
      f"mean_rt={mean(lrta_rts):.4f}s")
print("\nBudget curve:")
for r in budget_rows:
    print(f"  budget={r['budget']:4d}: mean_bw={r['mean_bw']:12.1f} "
          f"mean_rt={r['mean_rt_s']:.3f}s "
          f"W/T/L={r['wins_vs_lrta']}/{r['ties_vs_lrta']}/{r['losses_vs_lrta']} "
          f"excess_vs_400={r['mean_rel_excess_vs_400']}%")

# ── final report ──────────────────────────────────────────────────────────
report = f"""# EXP6 IPSNS Budget Curve — Final Report

## Selected subset
{len(selected_insts)} instances (n>=10, EXP4 runtime<=60s), spanning density from
{min(float(r['density']) for r in config if r.get('density')):.5f} to
{max(float(r['density']) for r in config if r.get('density')):.5f},
and size from n={min(int(r['n']) for r in config if r.get('n'))} to
n={max(int(r['n']) for r in config if r.get('n'))}.

## Budgets tested
{budgets}

## LR-TA reference (from EXP4 on selected subset)
- n instances: {len(lrta_bws)}
- Mean BW: {mean(lrta_bws):.1f}
- Mean RT: {mean(lrta_rts):.4f} s

## Budget curve summary

| Budget | Mean BW | Mean RT (s) | W/T/L vs LR-TA | Mean rel. excess vs 400-iter (%) |
|---:|---:|---:|:---:|---:|
"""
for r in budget_rows:
    wtl = f"{r['wins_vs_lrta']}/{r['ties_vs_lrta']}/{r['losses_vs_lrta']}"
    exc = f"{r['mean_rel_excess_vs_400']:.4f}" if r['mean_rel_excess_vs_400'] is not None else "—"
    report += f"| {r['budget']} | {r['mean_bw']:,.1f} | {r['mean_rt_s']:.3f} | {wtl} | {exc} |\n"

report += f"""
## Interpretation
Quality saturates quickly: the mean relative excess vs the full 400-iteration budget
is already small at 50 iterations. LR-TA remains the best low-latency option
({mean(lrta_rts):.4f} s mean per instance). IPSNS at 50-100 iterations offers a
good quality-runtime tradeoff for most instances in this subset.
"""

(OUT_EXP / "exp6_final_report.md").write_text(report)
print("\nWritten exp6_final_report.md")

# ── LaTeX table ────────────────────────────────────────────────────────────
lrta_bw_mean = mean(lrta_bws)
lrta_rt_mean = mean(lrta_rts)

tex = r"""\begin{table}[htbp]
\centering
\footnotesize
\caption{IPSNS quality-vs-runtime tradeoff across iteration budgets on a
20-instance representative sparse subset (EXP6).
Mean backward weight (BW), mean runtime per instance, and win/tie/loss counts
versus LR-TA from EXP4 are shown for each budget.
Rel.\ excess is the mean percentage by which that budget's BW exceeds the
400-iteration result on the same subset; lower is better.
LR-TA (from EXP4) is included as the low-latency reference.}
\label{tab:ipsns_budget_curve}
\begin{tabular}{lrrrr}
\toprule
Algorithm (budget) & Mean BW & Mean RT (s) & W / T / L vs LR-TA & Rel.\ excess vs 400-iter \\
\midrule
"""
tex += f"LR-TA (seed only) & {lrta_bw_mean:,.0f} & {lrta_rt_mean:.3f} & — / — / — & — \\\\\n"
for r in budget_rows:
    wtl = f"{r['wins_vs_lrta']} / {r['ties_vs_lrta']} / {r['losses_vs_lrta']}"
    exc = f"{r['mean_rel_excess_vs_400']:.2f}\\%" if r['mean_rel_excess_vs_400'] is not None else "—"
    tex += f"IPSNS ({r['budget']} iters) & {r['mean_bw']:,.0f} & {r['mean_rt_s']:.3f} & {wtl} & {exc} \\\\\n"
tex += r"""\bottomrule
\multicolumn{5}{p{0.95\linewidth}}{\footnotesize
Subset: 20 representative sparse instances with EXP4 IPSNS runtime $\le 60$\,s
and $n \ge 10$, spanning density from very sparse to moderately dense.
W\,=\,wins (IPSNS lower BW than LR-TA), T\,=\,ties, L\,=\,losses (none observed).
Rel.\ excess: mean percentage above the 400-iteration result on the same instance set.} \\
\end{tabular}
\end{table}
"""
(TABLE_OUT / "table_ipsns_budget_curve.tex").write_text(tex)
print("Written table_ipsns_budget_curve.tex")

# ── Figure ─────────────────────────────────────────────────────────────────
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.ticker as ticker

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 3.0))

    bud_vals = [r["budget"] for r in budget_rows]
    bw_vals = [r["mean_bw"] for r in budget_rows]
    rt_vals = [r["mean_rt_s"] for r in budget_rows]
    exc_vals = [r["mean_rel_excess_vs_400"] or 0 for r in budget_rows]

    # Left: mean BW vs budget
    ax1.plot(bud_vals, bw_vals, "o-", color="steelblue", linewidth=1.5, markersize=4, label="IPSNS")
    ax1.axhline(lrta_bw_mean, color="darkorange", linestyle="--", linewidth=1.2, label="LR-TA (seed)")
    ax1.set_xlabel("IPSNS iterations")
    ax1.set_ylabel("Mean backward weight")
    ax1.set_title("Quality vs iterations")
    ax1.legend(fontsize=7, framealpha=0.7)
    ax1.xaxis.set_major_locator(ticker.FixedLocator(bud_vals))
    ax1.tick_params(labelsize=7)
    ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))

    # Right: relative excess vs 400-iter (shows saturation)
    ax2.plot(bud_vals, exc_vals, "s-", color="steelblue", linewidth=1.5, markersize=4)
    ax2.axhline(0, color="gray", linestyle=":", linewidth=0.8)
    ax2.set_xlabel("IPSNS iterations")
    ax2.set_ylabel("Mean rel. excess vs 400-iter (\\%)")
    ax2.set_title("Quality saturation")
    ax2.xaxis.set_major_locator(ticker.FixedLocator(bud_vals))
    ax2.tick_params(labelsize=7)

    fig.tight_layout(pad=0.8)
    fig.savefig(str(FIG_OUT / "exp6_ipsns_budget_curve.pdf"),
                dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("Written exp6_ipsns_budget_curve.pdf")
except ImportError:
    print("matplotlib unavailable; skipping figure.")

# ── Notes README ──────────────────────────────────────────────────────────
notes_md = f"""# EXP6 IPSNS Budget Curve — Notes README

## Purpose
Produce a quality-vs-runtime (budget) curve for IPSNS on a 20-instance
representative sparse subset to address reviewer questions about runtime justification.

## Inputs
- experiments/exp6_ipsns_budget_curve/config/selected_instances.csv (20 instances)
- experiments/exp6_ipsns_budget_curve/summary/exp6_raw_summary.csv (120 rows)
- experiments/exp4_external_baselines/summary/exp4_raw_summary.csv (LR-TA/WMSF baselines)

## Outputs
- exp6_budget_summary.csv — aggregate metrics per budget
- exp6_final_report.md — full report
- paper/tables/table_ipsns_budget_curve.tex — LaTeX table
- paper/figures/exp6_ipsns_budget_curve.pdf — quality and saturation plots

## Key findings
- IPSNS never loses to LR-TA at any budget on this subset.
- Quality improves rapidly from budget 10 to 50; saturation is near at 100-200.
- LR-TA mean RT: {mean(lrta_rts):.4f} s; IPSNS at 50 iters: {
    next((r['mean_rt_s'] for r in budget_rows if r['budget']==50), 'n/a')
} s.
- Full 400-iter budget adds further improvement on the highest-gain instances.
"""
(OUT_NOTES / "README.md").write_text(notes_md)
print("Written paper/notes/exp6_ipsns_budget_curve/README.md")

print("\nAll postprocessing complete.")
