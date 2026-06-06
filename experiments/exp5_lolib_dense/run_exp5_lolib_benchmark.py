"""EXP5 LOLIB Dense Benchmark Runner.

Runs 8 algorithms on each LOLIB-converted DIMACS instance listed in the manifest.
Outputs a long-format summary CSV.

Usage:
    python run_exp5_lolib_benchmark.py \
        --manifest configs/exp5_lolib_instances.txt \
        --out-dir . \
        --log logs/exp5_lolib_tmux.log \
        --summary summary/exp5_lolib_raw_summary.csv \
        [--ipsns-iters 200] [--random-trials 100] [--random-seed 42]
"""
import argparse
import csv
import os
import sys
import time

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(REPO_ROOT, "src"))
sys.path.insert(0, os.path.join(REPO_ROOT, "scripts"))

from mwfas.io import read_graph_dimacs_agg
from mwfas.evaluation import compute_forward_backward
from mwfas.lrta import paper_fas_ranking_from_dimacs_fast
from mwfas.wmsf import wmsf_ranking_from_dimacs_fast
from mwfas.ipsns import lns_merge_wmsf_lr_best_incumbent
from mwfas.baselines import (
    order_by_borda_net_score_from_dimacs,
    weighted_eades_ordering_from_dimacs,
    random_multistart_ordering_from_dimacs,
)
from run_igraph_eades import run_igraph_eades
from run_drmaciver_fas import run_drmaciver_fas

SUMMARY_COLS = [
    "instance", "family", "n", "m", "total_weight",
    "algorithm", "backward_weight", "forward_weight", "forward_ratio",
    "runtime", "status", "error",
    "source_type", "external_version_or_commit",
]


def _make_row(inst_name, family, alg, metrics):
    status = metrics.get("status", "ok" if not metrics.get("error") else "error")
    return {
        "instance": inst_name,
        "family": family,
        "n": metrics.get("n_nodes", ""),
        "m": metrics.get("n_edges", ""),
        "total_weight": metrics.get("total_weight", ""),
        "algorithm": alg,
        "backward_weight": metrics.get("backward_weight", ""),
        "forward_weight": metrics.get("forward_weight", ""),
        "forward_ratio": metrics.get("forward_ratio", ""),
        "runtime": metrics.get("runtime", ""),
        "status": status,
        "error": metrics.get("error", ""),
        "source_type": metrics.get("source_type", ""),
        "external_version_or_commit": metrics.get("external_version_or_commit", ""),
    }


def run_internal(alg_name, fn, inst_path, out_csv, source_type="in-repo", **kwargs):
    t0 = time.time()
    try:
        result = fn(dimacs_path=inst_path, output_ranking_csv_path=out_csv, **kwargs)
        edges_indexed = result[0]
        scores = result[3]
        total_w, fw, bw = compute_forward_backward(edges_indexed, scores)
        n = len(result[1])
        m = len(edges_indexed)
        return {
            "algorithm": alg_name,
            "backward_weight": bw,
            "forward_weight": fw,
            "forward_ratio": fw / total_w if total_w > 0 else 1.0,
            "runtime": time.time() - t0,
            "n_nodes": n,
            "n_edges": m,
            "total_weight": total_w,
            "error": None,
            "source_type": source_type,
        }
    except Exception as e:
        return {
            "algorithm": alg_name,
            "error": f"{type(e).__name__}: {str(e)[:200]}",
            "status": "error",
            "runtime": time.time() - t0,
            "source_type": source_type,
        }


def run_baseline(alg_name, fn, inst_path, out_csv, source_type="in-repo", **kwargs):
    t0 = time.time()
    try:
        result = fn(inst_path, out_csv, **kwargs)
        metrics = result[4]
        metrics["source_type"] = source_type
        return metrics
    except Exception as e:
        return {
            "algorithm": alg_name,
            "error": f"{type(e).__name__}: {str(e)[:200]}",
            "status": "error",
            "runtime": time.time() - t0,
            "source_type": source_type,
        }


def run_external(alg_name, fn, inst_path, out_csv, source_type="external-wrapper"):
    t0 = time.time()
    try:
        metrics = fn(inst_path, out_csv)
        metrics["source_type"] = source_type
        return metrics
    except Exception as e:
        return {
            "algorithm": alg_name,
            "error": f"{type(e).__name__}: {str(e)[:200]}",
            "status": "error",
            "runtime": time.time() - t0,
            "source_type": source_type,
        }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True,
                    help="CSV from configs/exp5_lolib_instances.txt")
    ap.add_argument("--out-dir", required=True,
                    help="Experiment root (raw/ subdir will be created here)")
    ap.add_argument("--log", required=True)
    ap.add_argument("--summary", required=True)
    ap.add_argument("--ipsns-iters", type=int, default=200)
    ap.add_argument("--random-trials", type=int, default=100)
    ap.add_argument("--random-seed", type=int, default=42)
    args = ap.parse_args()

    raw_dir = os.path.join(args.out_dir, "raw")
    os.makedirs(raw_dir, exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(args.log)), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(args.summary)), exist_ok=True)

    with open(args.manifest, newline="") as f:
        manifest = list(csv.DictReader(f))

    print(f"[EXP5] {len(manifest)} instances from {args.manifest}")
    print(f"[EXP5] Summary: {args.summary}")
    print(f"[EXP5] Log:     {args.log}")
    print(f"[EXP5] IPSNS iters: {args.ipsns_iters}, random trials: {args.random_trials}", flush=True)

    rows = []
    log_lines = []

    def log(msg):
        ts = time.strftime("%H:%M:%S")
        line = f"[{ts}] {msg}"
        print(line, flush=True)
        log_lines.append(line)

    for i, rec in enumerate(manifest):
        inst_path = rec["dimacs_path"]
        inst_name = rec["instance"]
        family = rec["family"]
        inst_raw_dir = os.path.join(raw_dir, inst_name)
        os.makedirs(inst_raw_dir, exist_ok=True)

        log(f"[{i+1}/{len(manifest)}] {inst_name} (family={family}, n={rec['n']})")

        def out(alg):
            return os.path.join(inst_raw_dir, f"{alg}.csv")

        # 1. LR-TA
        m = run_internal(
            "lrta_full", paper_fas_ranking_from_dimacs_fast,
            inst_path, out("lrta_full"), source_type="in-repo"
        )
        rows.append(_make_row(inst_name, family, "lrta_full", m))
        log(f"  lrta_full: bw={m.get('backward_weight')} t={m.get('runtime',0):.2f}s err={m.get('error')}")

        # 2. WMSF
        m = run_internal(
            "wmsf_seed", wmsf_ranking_from_dimacs_fast,
            inst_path, out("wmsf_seed"), source_type="in-repo"
        )
        rows.append(_make_row(inst_name, family, "wmsf_seed", m))
        log(f"  wmsf_seed: bw={m.get('backward_weight')} t={m.get('runtime',0):.2f}s err={m.get('error')}")

        # 3. IPSNS
        m = run_internal(
            "ipsns_full", lns_merge_wmsf_lr_best_incumbent,
            inst_path, out("ipsns_full"), source_type="in-repo",
            iters=args.ipsns_iters, rng_seed=1, log_every=0, wmsf_seed_mode="full"
        )
        rows.append(_make_row(inst_name, family, "ipsns_full", m))
        log(f"  ipsns_full: bw={m.get('backward_weight')} t={m.get('runtime',0):.2f}s err={m.get('error')}")

        # 4. Borda
        m = run_baseline(
            "borda_net_score", order_by_borda_net_score_from_dimacs,
            inst_path, out("borda_net_score"), source_type="in-repo"
        )
        rows.append(_make_row(inst_name, family, "borda_net_score", m))
        log(f"  borda: bw={m.get('backward_weight')} t={m.get('runtime',0):.3f}s err={m.get('error')}")

        # 5. Weighted Eades
        m = run_baseline(
            "weighted_eades", weighted_eades_ordering_from_dimacs,
            inst_path, out("weighted_eades"), source_type="in-repo"
        )
        rows.append(_make_row(inst_name, family, "weighted_eades", m))
        log(f"  weades: bw={m.get('backward_weight')} t={m.get('runtime',0):.3f}s err={m.get('error')}")

        # 6. Random multistart
        m = run_baseline(
            "random_multistart", random_multistart_ordering_from_dimacs,
            inst_path, out("random_multistart"), source_type="in-repo",
            trials=args.random_trials, seed=args.random_seed
        )
        rows.append(_make_row(inst_name, family, "random_multistart", m))
        log(f"  random({args.random_trials}): bw={m.get('backward_weight')} t={m.get('runtime',0):.3f}s err={m.get('error')}")

        # 7. igraph approx_eades
        m = run_external(
            "igraph_approx_eades", run_igraph_eades,
            inst_path, out("igraph_approx_eades"), source_type="external-wrapper"
        )
        rows.append(_make_row(inst_name, family, "igraph_approx_eades", m))
        log(f"  igraph: bw={m.get('backward_weight')} t={m.get('runtime',0):.3f}s err={m.get('error')}")

        # 8. DRMacIver FAS
        m = run_external(
            "drmaciver_fas", run_drmaciver_fas,
            inst_path, out("drmaciver_fas"), source_type="external-wrapper"
        )
        rows.append(_make_row(inst_name, family, "drmaciver_fas", m))
        log(f"  drmaciver: bw={m.get('backward_weight')} t={m.get('runtime',0):.3f}s err={m.get('error')}")

    with open(args.summary, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=SUMMARY_COLS)
        writer.writeheader()
        writer.writerows(rows)

    with open(args.log, "a") as f:
        f.write("\n".join(log_lines) + "\n")

    n_ok = sum(1 for r in rows if r["status"] == "ok")
    n_err = sum(1 for r in rows if r["status"] not in ("ok", ""))
    log(f"[EXP5] Done. {len(manifest)} instances, {len(rows)} rows, "
        f"{n_ok} ok, {n_err} errors. Summary: {args.summary}")


if __name__ == "__main__":
    main()
