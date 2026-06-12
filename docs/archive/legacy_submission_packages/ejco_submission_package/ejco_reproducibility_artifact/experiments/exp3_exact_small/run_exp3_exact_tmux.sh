#!/usr/bin/env bash
# EXP3 Exact Small-Instance Optimality Check
# Usage: tmux new-session -d -s mwfas_exp3 \
#   "cd ~/minimum-weighted-fas-heuristics && bash experiments/exp3_exact_small/run_exp3_exact_tmux.sh"
set -uo pipefail

cd ~/minimum-weighted-fas-heuristics

EXP="experiments/exp3_exact_small"
LOG="$EXP/logs/exp3_exact.log"
INSTANCES_ALL="experiments/exp1b_core_benchmark_full_wmsf_seed/configs/benchmark_instances_found_all.txt"
TABLES="$EXP/tables"
SUMMARY="$EXP/summary"
RAW="$EXP/raw"

mkdir -p "$EXP"/{logs,raw,tables,summary}
exec > >(tee -a "$LOG") 2>&1

echo "============================================================"
echo "EXP3 EXACT SMALL-INSTANCE OPTIMALITY CHECK"
echo "Started: $(date)"
echo "Repository: $(pwd)"
echo "============================================================"
echo

echo "=== Git state ==="
git rev-parse HEAD
git log -1 --oneline
echo

echo "=== System info ==="
hostname || true
python --version || true
echo

echo "=== Install / refresh package ==="
python -m pip install -e . -q
python -m pip freeze > "$EXP/configs/pip_freeze.txt"
echo

python - "$INSTANCES_ALL" "$RAW" "$TABLES/exp3_exact_summary.csv" \
        "$SUMMARY/exp3_exact_stats.json" "$SUMMARY/exp3_exact_report.md" <<'PY'
import sys, os, time, json, traceback
from pathlib import Path

sys.path.insert(0, "src")

instances_all  = sys.argv[1]
raw_root       = sys.argv[2]
summary_csv    = sys.argv[3]
stats_json     = sys.argv[4]
report_md      = sys.argv[5]

N_MAX = 20
RNG_SEED = 1
IPSNS_ITERS = 400

from mwfas.io import read_graph_dimacs_agg
from mwfas.evaluation import compute_forward_backward
from mwfas.lrta import paper_fas_ranking_from_dimacs_fast
from mwfas.wmsf import wmsf_ranking_from_dimacs_fast
from mwfas.ipsns import lns_merge_wmsf_lr_best_incumbent
from mwfas.exact import exact_min_fas_from_dimacs

# Read instance list
with open(instances_all) as f:
    all_paths = [l.strip() for l in f if l.strip() and not l.startswith("#")]

# Filter to n <= N_MAX and accessible
small_instances = []
for p in all_paths:
    if not os.path.exists(p):
        continue
    try:
        edges, n2i, i2n = read_graph_dimacs_agg(p)
        n = len(n2i)
        m = len(edges)
        if n <= N_MAX:
            small_instances.append((p, n, m))
    except Exception:
        pass

small_instances.sort(key=lambda x: (x[1], x[2], x[0]))
print(f"Instances with n <= {N_MAX}: {len(small_instances)}")
print(f"Instance sizes: n=0..{max(n for _,n,_ in small_instances) if small_instances else 0}")
print()

# Run each instance
rows = []
for inst_path, n, m in small_instances:
    stem = Path(inst_path).stem
    print(f"=== {stem} (n={n}, m={m}) ===")

    out_dir = Path(raw_root) / stem
    out_dir.mkdir(parents=True, exist_ok=True)

    row = {"instance": stem, "n": n, "m": m}

    # --- Exact DP ---
    t0 = time.perf_counter()
    try:
        e, n2i, i2n, opt_bw, opt_fw, opt_scores = exact_min_fas_from_dimacs(
            inst_path, str(out_dir / f"{stem}_exact.csv")
        )
        exact_time = time.perf_counter() - t0
        total_w, _, _ = compute_forward_backward(e, opt_scores) if opt_scores else (0.0, 0.0, 0.0)
        row.update({
            "total_weight": total_w,
            "exact_bw": opt_bw,
            "exact_fw": opt_fw,
            "exact_time": round(exact_time, 6),
            "exact_status": "ok",
        })
        print(f"  exact:  BW={opt_bw:.6f}  t={exact_time:.4f}s")
    except Exception as exc:
        exact_time = time.perf_counter() - t0
        row.update({
            "total_weight": None, "exact_bw": None, "exact_fw": None,
            "exact_time": round(exact_time, 6), "exact_status": f"error: {exc}",
        })
        print(f"  exact:  ERROR — {exc}")

    # --- LR-TA ---
    t0 = time.perf_counter()
    try:
        e, n2i, i2n, sc, _ = paper_fas_ranking_from_dimacs_fast(
            inst_path, str(out_dir / f"{stem}_lrta.csv"))
        lrta_time = time.perf_counter() - t0
        _, _, lrta_bw = compute_forward_backward(e, sc)
        row.update({"lrta_bw": lrta_bw, "lrta_time": round(lrta_time, 6), "lrta_status": "ok"})
        print(f"  lrta:   BW={lrta_bw:.6f}  t={lrta_time:.4f}s")
    except Exception as exc:
        row.update({"lrta_bw": None, "lrta_time": 0.0, "lrta_status": f"error: {exc}"})
        print(f"  lrta:   ERROR — {exc}")

    # --- WMSF ---
    t0 = time.perf_counter()
    try:
        e, n2i, i2n, sc, _ = wmsf_ranking_from_dimacs_fast(
            inst_path, str(out_dir / f"{stem}_wmsf.csv"))
        wmsf_time = time.perf_counter() - t0
        _, _, wmsf_bw = compute_forward_backward(e, sc)
        row.update({"wmsf_bw": wmsf_bw, "wmsf_time": round(wmsf_time, 6), "wmsf_status": "ok"})
        print(f"  wmsf:   BW={wmsf_bw:.6f}  t={wmsf_time:.4f}s")
    except Exception as exc:
        row.update({"wmsf_bw": None, "wmsf_time": 0.0, "wmsf_status": f"error: {exc}"})
        print(f"  wmsf:   ERROR — {exc}")

    # --- IPSNS ---
    t0 = time.perf_counter()
    try:
        e, n2i, i2n, sc, _ = lns_merge_wmsf_lr_best_incumbent(
            inst_path, str(out_dir / f"{stem}_ipsns.csv"),
            iters=IPSNS_ITERS, rng_seed=RNG_SEED, log_every=0,
            wmsf_seed_mode="full")
        ipsns_time = time.perf_counter() - t0
        _, _, ipsns_bw = compute_forward_backward(e, sc)
        row.update({"ipsns_bw": ipsns_bw, "ipsns_time": round(ipsns_time, 6), "ipsns_status": "ok"})
        print(f"  ipsns:  BW={ipsns_bw:.6f}  t={ipsns_time:.4f}s")
    except Exception as exc:
        row.update({"ipsns_bw": None, "ipsns_time": 0.0, "ipsns_status": f"error: {exc}"})
        print(f"  ipsns:  ERROR — {exc}")

    # --- Gaps ---
    try:
        opt = row.get("exact_bw")
        for algo in ("lrta", "wmsf", "ipsns"):
            bw = row.get(f"{algo}_bw")
            if opt is not None and bw is not None and row.get("total_weight", 0) and row["total_weight"] > 1e-12:
                row[f"{algo}_gap_abs"] = round(bw - opt, 8)
                row[f"{algo}_gap_rel"] = round((bw - opt) / row["total_weight"], 8)
                row[f"{algo}_is_optimal"] = (bw - opt) <= 1e-9
            else:
                row[f"{algo}_gap_abs"] = None
                row[f"{algo}_gap_rel"] = None
                row[f"{algo}_is_optimal"] = (bw == opt) if (opt is not None and bw is not None) else None
    except Exception as exc:
        print(f"  gap computation error: {exc}")

    rows.append(row)

# --- Write summary CSV ---
import pandas as pd

cols = [
    "instance", "n", "m", "total_weight",
    "exact_bw", "lrta_bw", "wmsf_bw", "ipsns_bw",
    "lrta_gap_abs", "wmsf_gap_abs", "ipsns_gap_abs",
    "lrta_gap_rel", "wmsf_gap_rel", "ipsns_gap_rel",
    "lrta_is_optimal", "wmsf_is_optimal", "ipsns_is_optimal",
    "exact_time", "lrta_time", "wmsf_time", "ipsns_time",
    "exact_status", "lrta_status", "wmsf_status", "ipsns_status",
]
df = pd.DataFrame(rows)
for c in cols:
    if c not in df.columns:
        df[c] = None
df = df[cols]
df.to_csv(summary_csv, index=False)
print(f"\nSummary CSV: {summary_csv}  ({len(df)} rows)")

# --- Stats ---
ok = df[(df["exact_status"] == "ok") & (df["n"] > 0)]

def pct_optimal(col):
    if col not in ok.columns or ok[col].isna().all():
        return "N/A"
    v = ok[col].dropna()
    return f"{v.sum()}/{len(v)} ({100*v.mean():.1f}%)" if len(v) > 0 else "N/A"

def mean_gap(col):
    if col not in ok.columns or ok[col].isna().all():
        return "N/A"
    v = ok[col].dropna()
    return f"{v.mean()*100:.4f}%" if len(v) > 0 else "N/A"

stats = {
    "n_instances_total": len(rows),
    "n_instances_exact_ok": int((df["exact_status"] == "ok").sum()),
    "n_instances_nontrivial": int(len(ok)),
    "lrta_optimal": pct_optimal("lrta_is_optimal"),
    "wmsf_optimal": pct_optimal("wmsf_is_optimal"),
    "ipsns_optimal": pct_optimal("ipsns_is_optimal"),
    "lrta_mean_gap_pct": mean_gap("lrta_gap_rel"),
    "wmsf_mean_gap_pct": mean_gap("wmsf_gap_rel"),
    "ipsns_mean_gap_pct": mean_gap("ipsns_gap_rel"),
}
Path(stats_json).write_text(json.dumps(stats, indent=2))
print(f"Stats JSON: {stats_json}")
print(json.dumps(stats, indent=2))

# --- Markdown report ---
non_opt = ok[ok.get("ipsns_is_optimal", pd.Series(dtype=bool)) == False] if "ipsns_is_optimal" in ok.columns else pd.DataFrame()

report = f"""# EXP3: Exact Small-Instance Optimality Check

## Summary

- Instances with n ≤ {N_MAX}: **{stats['n_instances_exact_ok']}** (exact DP successful)
- Non-trivial instances (n > 0): **{stats['n_instances_nontrivial']}**

## Optimality Rates

| Algorithm | Optimal | Mean Rel. Gap |
|-----------|---------|---------------|
| LR-TA     | {stats['lrta_optimal']} | {stats['lrta_mean_gap_pct']} |
| WMSF      | {stats['wmsf_optimal']} | {stats['wmsf_mean_gap_pct']} |
| IPSNS     | {stats['ipsns_optimal']} | {stats['ipsns_mean_gap_pct']} |

## Non-Optimal IPSNS Cases

"""
if "ipsns_is_optimal" in ok.columns:
    non_opt_rows = ok[ok["ipsns_is_optimal"] == False] if len(ok) > 0 else pd.DataFrame()
    if len(non_opt_rows) == 0:
        report += "**None** — IPSNS achieved the exact optimum on all non-trivial instances.\n"
    else:
        report += "| Instance | n | m | exact_bw | ipsns_bw | gap_abs | gap_rel |\n"
        report += "|----------|---|---|----------|----------|---------|----------|\n"
        for _, r in non_opt_rows.iterrows():
            report += f"| {r['instance']} | {r['n']} | {r['m']} | {r['exact_bw']:.4f} | {r['ipsns_bw']:.4f} | {r.get('ipsns_gap_abs', 'N/A'):.4f} | {r.get('ipsns_gap_rel', 'N/A'):.6f} |\n"
else:
    report += "No ipsns_is_optimal column found.\n"

report += f"""
## Key Files

- Summary CSV: `{summary_csv}`
- Stats JSON: `{stats_json}`
- Raw rankings: `{raw_root}/`
"""

Path(report_md).write_text(report)
print(f"Report MD: {report_md}")

# --- Incumbent protection check ---
if "ipsns_is_optimal" in ok.columns:
    n_noopt = int((ok["ipsns_is_optimal"] == False).sum()) if "ipsns_is_optimal" in ok.columns else 0
    print(f"\n=== Incumbent protection check ===")
    for algo in ("lrta", "wmsf"):
        bw_col = f"{algo}_bw"
        ip_col = f"ipsns_bw"
        if bw_col in ok.columns and ip_col in ok.columns:
            viols = (ok[ip_col] > ok[bw_col] + 1e-9).sum()
            print(f"  IPSNS > {algo.upper()} violations: {viols}")

print("\n=== Backward weight pivot ===")
show_cols = ["exact_bw", "lrta_bw", "wmsf_bw", "ipsns_bw"]
disp = ok[["instance","n"] + [c for c in show_cols if c in ok.columns]].sort_values("n")
print(disp.to_string(index=False))
PY

echo
echo "=== Git status ==="
git status
echo

echo "=== Commit EXP3 results ==="
git add \
    src/mwfas/exact.py \
    scripts/run_exact.py \
    "$EXP/configs" "$EXP/summary" "$EXP/tables" \
    experiments/exp3_exact_small/run_exp3_exact_tmux.sh \
    2>/dev/null || true
git commit -m "Add EXP3 exact small-instance optimality check" || true
git push || true

echo
echo "=== Final git log ==="
git log -1 --oneline

echo
echo "============================================================"
echo "EXP3 FINISHED"
echo "Finished: $(date)"
echo "Log: $LOG"
echo "Summary CSV: $TABLES/exp3_exact_summary.csv"
echo "Stats JSON: $SUMMARY/exp3_exact_stats.json"
echo "Report: $SUMMARY/exp3_exact_report.md"
echo "============================================================"
