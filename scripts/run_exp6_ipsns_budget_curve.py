"""
EXP6: IPSNS Budget Curve Runner.
Runs IPSNS at multiple iteration budgets on selected instances.
Does NOT modify EXP1b-EXP5 results.
"""
import argparse
import csv
import os
import sys
import time
import traceback
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mwfas.ipsns import lns_merge_wmsf_lr_best_incumbent
from mwfas.evaluation import compute_forward_backward

SUMMARY_COLS = [
    "instance", "budget", "algorithm",
    "n", "m", "total_weight",
    "backward_weight", "forward_weight", "forward_ratio",
    "runtime", "status", "error",
    "rng_seed", "wmsf_seed_mode",
]

CONFIG_CSV = REPO_ROOT / "experiments/exp6_ipsns_budget_curve/config/selected_instances.csv"
OUT_DIR = REPO_ROOT / "experiments/exp6_ipsns_budget_curve"
SUMMARY_PATH = OUT_DIR / "summary/exp6_raw_summary.csv"
LOG_PATH = OUT_DIR / "logs/exp6_tmux.log"


def read_config():
    with open(CONFIG_CSV, newline="") as f:
        return list(csv.DictReader(f))


def run_one(inst_path, iters, rng_seed=1, wmsf_seed_mode="full"):
    t0 = time.perf_counter()
    tmp_out = OUT_DIR / "raw" / f"tmp_{Path(inst_path).stem}_iters{iters}.csv"
    tmp_out.parent.mkdir(parents=True, exist_ok=True)
    try:
        result = lns_merge_wmsf_lr_best_incumbent(
            dimacs_path=str(inst_path),
            output_ranking_csv_path=str(tmp_out),
            iters=iters,
            rng_seed=rng_seed,
            log_every=0,
            wmsf_seed_mode=wmsf_seed_mode,
            return_info=False,
        )
        edges_indexed, node_to_index, index_to_node, scores, _ = result[:5]
        total_w, fw, bw = compute_forward_backward(edges_indexed, scores)
        n = len(node_to_index)
        m = len(edges_indexed)
        rt = time.perf_counter() - t0
        return {
            "n": n, "m": m,
            "total_weight": round(total_w, 4),
            "backward_weight": round(bw, 4),
            "forward_weight": round(fw, 4),
            "forward_ratio": round(fw / total_w, 8) if total_w > 0 else 1.0,
            "runtime": round(rt, 6),
            "status": "ok",
            "error": "",
        }
    except Exception as e:
        rt = time.perf_counter() - t0
        return {
            "runtime": round(rt, 6),
            "status": "error",
            "error": f"{type(e).__name__}: {str(e)[:300]}",
        }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--budgets", default="10,25,50,100,200,400",
                    help="Comma-separated list of IPSNS iteration budgets")
    ap.add_argument("--smoke", action="store_true",
                    help="Smoke-test mode: run only first --max-instances instances")
    ap.add_argument("--max-instances", type=int, default=2)
    ap.add_argument("--rng-seed", type=int, default=1)
    ap.add_argument("--wmsf-seed-mode", default="full")
    args = ap.parse_args()

    budgets = [int(b.strip()) for b in args.budgets.split(",") if b.strip()]
    config = read_config()
    if args.smoke:
        config = config[:args.max_instances]
        print(f"[SMOKE] Running {len(config)} instances, budgets={budgets}")

    (OUT_DIR / "summary").mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "logs").mkdir(parents=True, exist_ok=True)

    rows = []
    total = len(config) * len(budgets)
    done = 0

    for cfg in config:
        inst = cfg["instance"]
        inst_path = Path(cfg["file_path"])
        if not inst_path.exists():
            print(f"[SKIP] {inst}: file not found at {inst_path}")
            continue

        for budget in budgets:
            alg_label = f"ipsns_budget_{budget}"
            t_start = time.strftime("%H:%M:%S")
            print(f"[{t_start}] [{done+1}/{total}] {inst} budget={budget} ...", flush=True)

            metrics = run_one(inst_path, budget, args.rng_seed, args.wmsf_seed_mode)

            row = {
                "instance": inst,
                "budget": budget,
                "algorithm": alg_label,
                "rng_seed": args.rng_seed,
                "wmsf_seed_mode": args.wmsf_seed_mode,
            }
            row.update(metrics)
            # ensure all cols present
            for col in SUMMARY_COLS:
                row.setdefault(col, "")
            rows.append(row)
            done += 1

            bw = metrics.get("backward_weight", "err")
            rt = metrics.get("runtime", 0)
            print(f"  -> bw={bw} rt={rt:.2f}s status={metrics.get('status')}", flush=True)

            # Write incrementally
            with open(SUMMARY_PATH, "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=SUMMARY_COLS, extrasaction="ignore")
                w.writeheader()
                w.writerows(rows)

    print(f"\nDone. Wrote {len(rows)} rows to {SUMMARY_PATH}")


if __name__ == "__main__":
    main()
