#!/usr/bin/env bash
# EXP2 Ablation Study — run script
# Usage: tmux new-session -d -s mwfas_exp2 \
#          "cd ~/minimum-weighted-fas-heuristics && bash experiments/exp2_ablation/run_exp2_ablation_tmux.sh"
# Do NOT start this while mwfas_exp1 is still running.
set -u
set -o pipefail

cd ~/minimum-weighted-fas-heuristics

EXP="experiments/exp2_ablation"
LOG="$EXP/logs/exp2_ablation.log"
INSTANCES="$EXP/configs/exp2_ablation_instances.txt"
RAW="$EXP/raw"
TABLES="$EXP/tables"
SUMMARY="$EXP/summary"

mkdir -p "$EXP"/{logs,raw,tables,summary}
exec > >(tee -a "$LOG") 2>&1

echo "============================================================"
echo "EXP2 ABLATION STUDY — MWFAS MERGED PAPER"
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
uname -a || true
python --version || true
echo

echo "=== Install / refresh package ==="
python -m pip install -e . -q
python -m pip freeze > "$EXP/configs/pip_freeze.txt"
echo

echo "=== Instance list ==="
cat "$INSTANCES"
COUNT=$(wc -l < "$INSTANCES")
echo "Total instances: $COUNT"
echo

# ---------------------------------------------------------------------------
# Helper: run one variant on all instances, write per-instance CSVs, return
# a per-instance summary row via stdout as TSV: instance<TAB>bw<TAB>runtime
# ---------------------------------------------------------------------------
run_variant() {
    local VARIANT="$1"
    local OUT_DIR="$RAW/$VARIANT"
    mkdir -p "$OUT_DIR"
    echo "--- Variant: $VARIANT ---"

    while IFS= read -r inst_path || [ -n "$inst_path" ]; do
        [ -z "$inst_path" ] && continue
        [[ "$inst_path" == \#* ]] && continue

        stem=$(basename "$inst_path" .d)
        out_csv="$OUT_DIR/${stem}_${VARIANT}.csv"

        if [ ! -f "$inst_path" ]; then
            echo "  [$VARIANT] SKIP (not found): $inst_path"
            echo -e "$stem\tNOT_FOUND\tNOT_FOUND"
            continue
        fi

        python - "$inst_path" "$out_csv" "$VARIANT" <<'PY'
import sys, time, traceback
inst_path = sys.argv[1]
out_csv   = sys.argv[2]
variant   = sys.argv[3]

sys.path.insert(0, "src")

from mwfas.evaluation import compute_forward_backward

def run():
    t0 = time.perf_counter()

    if variant == "lrta_full":
        from mwfas.lrta import paper_fas_ranking_from_dimacs_fast
        edges, n2i, i2n, scores, _ = paper_fas_ranking_from_dimacs_fast(
            dimacs_path=inst_path, output_ranking_csv_path=out_csv)

    elif variant == "wmsf_seed":
        from mwfas.wmsf import wmsf_ranking_from_dimacs_fast
        edges, n2i, i2n, scores, _ = wmsf_ranking_from_dimacs_fast(
            dimacs_path=inst_path, output_ranking_csv_path=out_csv, ordering="L2")

    elif variant == "best_seed_no_lns":
        # Run both; pick whichever has lower BW.
        import os, shutil
        from mwfas.lrta import paper_fas_ranking_from_dimacs_fast
        from mwfas.wmsf import wmsf_ranking_from_dimacs_fast
        tmp_lr = out_csv + ".lr_tmp.csv"
        tmp_wm = out_csv + ".wm_tmp.csv"
        edges, n2i, i2n, scores_lr, _ = paper_fas_ranking_from_dimacs_fast(
            dimacs_path=inst_path, output_ranking_csv_path=tmp_lr)
        _, fw_lr, bw_lr = compute_forward_backward(edges, scores_lr)
        _, n2i2, i2n2, scores_wm, _ = wmsf_ranking_from_dimacs_fast(
            dimacs_path=inst_path, output_ranking_csv_path=tmp_wm, ordering="L2")
        _, fw_wm, bw_wm = compute_forward_backward(edges, scores_wm)
        if bw_lr <= bw_wm:
            shutil.copy(tmp_lr, out_csv)
            scores = scores_lr
        else:
            shutil.copy(tmp_wm, out_csv)
            scores = scores_wm
        os.remove(tmp_lr); os.remove(tmp_wm)

    elif variant in ("ipsns_50iters", "ipsns_100iters", "ipsns_full"):
        iters_map = {"ipsns_50iters": 50, "ipsns_100iters": 100, "ipsns_full": 400}
        from mwfas.ipsns import lns_merge_wmsf_lr_best_incumbent
        edges, n2i, i2n, scores, _ = lns_merge_wmsf_lr_best_incumbent(
            dimacs_path=inst_path, output_ranking_csv_path=out_csv,
            iters=iters_map[variant], rng_seed=1, log_every=0)

    elif variant == "lr_no_addback":
        raise NotImplementedError(
            "lr_no_addback requires add_back=False parameter in "
            "local_ratio_fas_fast() (src/mwfas/lrta.py line 216). "
            "See experiments/exp2_ablation/README.md for the required change.")

    elif variant == "ipsns_no_scc_priority":
        raise NotImplementedError(
            "ipsns_no_scc_priority requires scc_select_mode='random' parameter in "
            "lns_merge_wmsf_lr_best_incumbent() (src/mwfas/ipsns.py line 617). "
            "See experiments/exp2_ablation/README.md for the required change.")

    else:
        raise ValueError(f"Unknown variant: {variant}")

    elapsed = time.perf_counter() - t0
    total, fw, bw = compute_forward_backward(edges, scores)
    print(f"OK\t{bw:.6f}\t{elapsed:.4f}")

try:
    run()
except NotImplementedError as e:
    print(f"NOT_IMPLEMENTED\t{e}\t0")
except Exception as e:
    traceback.print_exc(file=sys.stderr)
    print(f"ERROR\t{e}\t0")
PY
    done < "$INSTANCES"
    echo
}

# ---------------------------------------------------------------------------
# Run all variants and collect results into a summary CSV
# ---------------------------------------------------------------------------
SUMMARY_CSV="$TABLES/exp2_ablation_summary.csv"

python - "$INSTANCES" "$RAW" "$SUMMARY_CSV" \
    "lrta_full" "wmsf_seed" "best_seed_no_lns" \
    "ipsns_50iters" "ipsns_100iters" "ipsns_full" \
    "lr_no_addback" "ipsns_no_scc_priority" <<'PY'
import sys, os, time, traceback, csv, json
from pathlib import Path

sys.path.insert(0, "src")
from mwfas.evaluation import compute_forward_backward

instances_file = sys.argv[1]
raw_root       = sys.argv[2]
summary_csv    = sys.argv[3]
variants       = sys.argv[4:]

with open(instances_file) as f:
    instances = [l.strip() for l in f if l.strip() and not l.startswith("#")]

ITERS_MAP = {"ipsns_50iters": 50, "ipsns_100iters": 100, "ipsns_full": 400}

rows = []

for inst_path in instances:
    stem = Path(inst_path).stem
    print(f"\n=== {stem} ===")
    if not Path(inst_path).exists():
        print(f"  [SKIP] not found: {inst_path}")
        for v in variants:
            rows.append({"instance": stem, "variant": v, "status": "NOT_FOUND",
                         "backward_weight": None, "runtime_sec": None, "error": None})
        continue

    row_base = {"instance": stem}

    for variant in variants:
        out_dir = Path(raw_root) / variant
        out_dir.mkdir(parents=True, exist_ok=True)
        out_csv = str(out_dir / f"{stem}_{variant}.csv")

        t0 = time.perf_counter()
        try:
            if variant == "lrta_full":
                from mwfas.lrta import paper_fas_ranking_from_dimacs_fast
                edges, n2i, i2n, scores, _ = paper_fas_ranking_from_dimacs_fast(
                    dimacs_path=inst_path, output_ranking_csv_path=out_csv)

            elif variant == "wmsf_seed":
                from mwfas.wmsf import wmsf_ranking_from_dimacs_fast
                edges, n2i, i2n, scores, _ = wmsf_ranking_from_dimacs_fast(
                    dimacs_path=inst_path, output_ranking_csv_path=out_csv, ordering="L2")

            elif variant == "best_seed_no_lns":
                import shutil
                from mwfas.lrta import paper_fas_ranking_from_dimacs_fast
                from mwfas.wmsf import wmsf_ranking_from_dimacs_fast
                tmp_lr = out_csv + ".lr_tmp"
                tmp_wm = out_csv + ".wm_tmp"
                edges, n2i, i2n, sc_lr, _ = paper_fas_ranking_from_dimacs_fast(
                    dimacs_path=inst_path, output_ranking_csv_path=tmp_lr)
                _, _, bw_lr = compute_forward_backward(edges, sc_lr)
                _, n2i2, i2n2, sc_wm, _ = wmsf_ranking_from_dimacs_fast(
                    dimacs_path=inst_path, output_ranking_csv_path=tmp_wm, ordering="L2")
                _, _, bw_wm = compute_forward_backward(edges, sc_wm)
                if bw_lr <= bw_wm:
                    shutil.copy(tmp_lr, out_csv); scores = sc_lr
                else:
                    shutil.copy(tmp_wm, out_csv); scores = sc_wm
                os.remove(tmp_lr); os.remove(tmp_wm)

            elif variant in ITERS_MAP:
                from mwfas.ipsns import lns_merge_wmsf_lr_best_incumbent
                edges, n2i, i2n, scores, _ = lns_merge_wmsf_lr_best_incumbent(
                    dimacs_path=inst_path, output_ranking_csv_path=out_csv,
                    iters=ITERS_MAP[variant], rng_seed=1, log_every=0)

            elif variant == "lr_no_addback":
                raise NotImplementedError(
                    "Requires add_back=False in local_ratio_fas_fast(); "
                    "see README.md")

            elif variant == "ipsns_no_scc_priority":
                raise NotImplementedError(
                    "Requires scc_select_mode='random' in lns_merge_wmsf_lr_best_incumbent(); "
                    "see README.md")

            else:
                raise ValueError(f"Unknown variant: {variant}")

            elapsed = time.perf_counter() - t0
            _, _, bw = compute_forward_backward(edges, scores)
            print(f"  {variant}: BW={bw:.6f}  time={elapsed:.2f}s")
            rows.append({"instance": stem, "variant": variant, "status": "ok",
                         "backward_weight": bw, "runtime_sec": round(elapsed, 4),
                         "error": None})

        except NotImplementedError as e:
            elapsed = time.perf_counter() - t0
            print(f"  {variant}: NOT_IMPLEMENTED — {e}")
            rows.append({"instance": stem, "variant": variant,
                         "status": "not_implemented", "backward_weight": None,
                         "runtime_sec": round(elapsed, 4), "error": str(e)})

        except Exception as e:
            elapsed = time.perf_counter() - t0
            print(f"  {variant}: ERROR — {e}")
            traceback.print_exc()
            rows.append({"instance": stem, "variant": variant, "status": "error",
                         "backward_weight": None, "runtime_sec": round(elapsed, 4),
                         "error": str(e)})

import pandas as pd

df = pd.DataFrame(rows, columns=[
    "instance", "variant", "status", "backward_weight", "runtime_sec", "error"])

# Pivot for easy comparison
ok = df[df["status"] == "ok"]
if not ok.empty:
    piv = ok.pivot_table(index="instance", columns="variant",
                         values="backward_weight", aggfunc="first")
    piv = piv.reindex(columns=[v for v in variants if v in piv.columns])
    print("\n=== Backward weight pivot (lower is better) ===")
    print(piv.to_string())

    # Incumbent protection check for IPSNS variants
    ipsns_variants = [v for v in variants if v.startswith("ipsns_")]
    seed_variants = [v for v in ["lrta_full", "wmsf_seed"] if v in piv.columns]
    if seed_variants and ipsns_variants:
        best_seed = piv[seed_variants].min(axis=1)
        print("\n=== Incumbent protection check ===")
        for iv in ipsns_variants:
            if iv in piv.columns:
                viols = (piv[iv] > best_seed + 1e-9).sum()
                print(f"  {iv}: violations = {viols}")

df.to_csv(summary_csv, index=False)
print(f"\nSummary CSV: {summary_csv}")
print(f"Rows: {len(df)}")

# Write stats JSON
stats = {}
if not ok.empty and "lrta_full" in ok["variant"].values:
    for v in variants:
        sub = ok[ok["variant"] == v]
        if not sub.empty:
            stats[v] = {
                "mean_bw": float(sub["backward_weight"].mean()),
                "median_bw": float(sub["backward_weight"].median()),
                "mean_runtime": float(sub["runtime_sec"].mean()),
                "n_ok": int(len(sub)),
            }
        else:
            stats[v] = {"status": "not_implemented_or_error"}

stats_path = Path("experiments/exp2_ablation/summary/exp2_ablation_stats.json")
stats_path.write_text(json.dumps(stats, indent=2))
print(f"Stats JSON: {stats_path}")
print(json.dumps(stats, indent=2))
PY

echo
echo "=== Preview summary CSV ==="
head -20 "$SUMMARY_CSV" || true
echo

echo "=== Git status ==="
git status
echo

echo "=== Commit EXP2 results ==="
git add "$EXP/configs" "$EXP/summary" "$EXP/tables" "$EXP/logs" \
        run_exp2_ablation_tmux.sh 2>/dev/null || true
git commit -m "Add EXP2 ablation results" || true
git push || true
echo

echo "=== Final commit ==="
git log -1 --oneline
echo

echo "============================================================"
echo "EXP2 ABLATION STUDY FINISHED"
echo "Finished: $(date)"
echo "Log: $LOG"
echo "Summary CSV: $SUMMARY_CSV"
echo "Stats JSON: $SUMMARY/exp2_ablation_stats.json"
echo "============================================================"
