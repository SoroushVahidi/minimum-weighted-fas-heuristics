"""
EXP10: IPSNS repeated-run driver.

Runs IPSNS with 20 seeds (0..19) on each of the 93 common instances.
Checkpointed: skips already-completed (instance, seed) pairs.
Schema: one JSON record per (instance, seed) in raw/ipsns/.
Combined into summary/run_level_results_ipsns.csv by postprocess.py.

Usage:
    python scripts/run_ipsns_repetitions.py [--instances common|diagnostic] [--smoke]
    python scripts/run_ipsns_repetitions.py --resume   # same as default; skips done
"""
import argparse
import csv
import hashlib
import json
import os
import platform
import socket
import subprocess
import sys
import tempfile
import time

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO_ROOT, "src"))

EXP_DIR = os.path.join(REPO_ROOT, "experiments", "exp10_stochastic_robustness")
RAW_DIR = os.path.join(EXP_DIR, "raw", "ipsns")
CKPT_DIR = os.path.join(EXP_DIR, "checkpoints")

IPSNS_PARAMS = dict(
    iters=400,
    topK_scc=15,
    destroy_addback_frac=0.30,
    destroy_remove_frac=0.02,
    tol=1e-12,
    seed_ordering="L2",
    wmsf_seed_mode="full",
    scc_select_mode="weighted",
    log_every=0,
)
SEEDS = list(range(20))


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def get_src_sha():
    files = [
        "src/mwfas/lrta.py", "src/mwfas/wmsf.py", "src/mwfas/ipsns.py",
        "src/mwfas/evaluation.py", "src/mwfas/io.py",
    ]
    combined = {}
    for f in files:
        p = os.path.join(REPO_ROOT, f)
        if os.path.exists(p):
            combined[f] = sha256_file(p)
    return combined


def get_git_commit():
    try:
        r = subprocess.run(["git", "-C", REPO_ROOT, "rev-parse", "HEAD"],
                           capture_output=True, text=True, timeout=5)
        return r.stdout.strip()
    except Exception:
        return "unknown"


def load_instances(kind="common"):
    if kind == "diagnostic":
        manifest = os.path.join(EXP_DIR, "config", "diagnostic_subset.txt")
    else:
        manifest = os.path.join(EXP_DIR, "config", "common_93_instances.txt")
    instances = {}
    with open(manifest) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) >= 2:
                instances[parts[0]] = parts[1]
    return instances


def ckpt_key(inst_name, seed):
    return f"ipsns_{inst_name}_seed{seed:02d}.done"


def is_done(inst_name, seed):
    return os.path.exists(os.path.join(CKPT_DIR, ckpt_key(inst_name, seed)))


def mark_done(inst_name, seed):
    os.makedirs(CKPT_DIR, exist_ok=True)
    with open(os.path.join(CKPT_DIR, ckpt_key(inst_name, seed)), "w") as f:
        f.write("done\n")


def out_path(inst_name, seed):
    return os.path.join(RAW_DIR, f"ipsns_{inst_name}_seed{seed:02d}.json")


def run_one(inst_name, inst_path, seed, git_sha, src_sha, meta):
    from mwfas.ipsns import lns_merge_wmsf_lr_best_incumbent
    from mwfas.io import read_graph_dimacs_agg
    from mwfas.evaluation import compute_forward_backward

    inst_sha = sha256_file(inst_path)
    edges_indexed_check, nmap, _ = read_graph_dimacs_agg(inst_path)
    n = len(nmap)
    m = len(edges_indexed_check)
    total_w = sum(w for _, _, w in edges_indexed_check)

    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tf:
        tmp_csv = tf.name

    record = {
        "algorithm": "ipsns",
        "instance_id": inst_name,
        "instance_path": inst_path,
        "instance_sha256": inst_sha,
        "n": n,
        "m": m,
        "density": m / (n * (n - 1)) if n > 1 else 0.0,
        "run_index": seed,
        "seed": seed,
        "git_commit": git_sha,
        "executable_or_code_sha256": src_sha.get("src/mwfas/ipsns.py", ""),
        "hostname": meta["hostname"],
        "cpu_model": meta["cpu_model"],
        "ram_gb": meta["ram_gb"],
        "python_version": meta["python_version"],
        "dependency_versions": meta["dependency_versions"],
        "timeout_seconds": None,
        "total_weight": total_w,
    }

    ts_start = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    t0 = time.perf_counter()

    try:
        result = lns_merge_wmsf_lr_best_incumbent(
            dimacs_path=inst_path,
            output_ranking_csv_path=tmp_csv,
            rng_seed=seed,
            return_info=True,
            **IPSNS_PARAMS,
        )
        runtime = time.perf_counter() - t0
        ts_end = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

        edges_indexed, node_to_index, index_to_node, scores, F_removed_pairs, info = result
        n_actual = len(node_to_index)

        # Recompute objective independently
        total_w2, fw, bw_recomp = compute_forward_backward(edges_indexed, scores)
        objective_match = abs(bw_recomp - info["final_bw"]) < 1e-6

        # Check ordering is permutation of 0..n-1
        order_vals = sorted(scores.values())
        ordering_valid = order_vals == list(range(n_actual))

        # Acyclicity: the recomputed BW is the ground truth; if IPSNS returned a valid
        # ordering (permutation), the output is implicitly acyclic (the active graph was DAG)
        acyclicity_valid = ordering_valid  # DAG guaranteed by topo-sort construction

        record.update({
            "status": "ok",
            "objective_bw": float(bw_recomp),
            "forward_weight": float(fw),
            "normalized_bw": float(bw_recomp) / float(total_w2) if total_w2 > 1e-9 else 0.0,
            "runtime_seconds": float(runtime),
            "ordering_valid": ordering_valid,
            "objective_recomputed": float(bw_recomp),
            "objective_match": objective_match,
            "acyclicity_valid": acyclicity_valid,
            "lr_seed_bw": float(info["lr_seed_bw"]),
            "wmsf_seed_bw": float(info["wmsf_seed_bw"]),
            "initial_incumbent_bw": float(info["best_seed_bw"]),
            "accepted_moves": int(info["n_accepted"]),
            "rejected_moves": int(info["n_rejected"]),
            "failed_repairs": int(info["n_failed_repair"]),
            "noop_moves": int(info["n_noop"]),
            "best_iteration": int(info["best_iter"]),
            "time_to_best_seconds": float(info["time_to_best"]),
            "n_iters_done": int(info["n_iters"]),
            "improved_over_seed": bool(info["improved"]),
            "timestamp_start": ts_start,
            "timestamp_end": ts_end,
            "error_message": None,
            "raw_output_path": out_path(inst_name, seed),
        })
    except Exception as e:
        runtime = time.perf_counter() - t0
        ts_end = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        record.update({
            "status": "error",
            "objective_bw": None,
            "runtime_seconds": float(runtime),
            "ordering_valid": False,
            "objective_match": False,
            "acyclicity_valid": False,
            "timestamp_start": ts_start,
            "timestamp_end": ts_end,
            "error_message": str(e),
            "raw_output_path": out_path(inst_name, seed),
        })
    finally:
        try:
            os.unlink(tmp_csv)
        except Exception:
            pass

    return record


def write_record_atomic(record, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(record, f, indent=2)
    os.replace(tmp, path)  # atomic on POSIX


def get_machine_meta():
    try:
        import pkg_resources
        deps = {p.key: p.version for p in pkg_resources.working_set
                if p.key in ("pandas", "numpy", "scipy", "python-igraph")}
    except Exception:
        deps = {}
    try:
        with open("/proc/cpuinfo") as f:
            cpu_lines = [l for l in f if "model name" in l]
        cpu = cpu_lines[0].split(":")[1].strip() if cpu_lines else "unknown"
    except Exception:
        cpu = platform.processor() or "unknown"
    try:
        import psutil
        ram_gb = round(psutil.virtual_memory().total / 1e9, 1)
    except Exception:
        ram_gb = None
    return {
        "hostname": socket.gethostname(),
        "cpu_model": cpu,
        "ram_gb": ram_gb,
        "python_version": sys.version,
        "dependency_versions": deps,
    }


def count_done(instances):
    total = len(instances) * len(SEEDS)
    done = sum(1 for n in instances for s in SEEDS if is_done(n, s))
    return done, total


def main():
    parser = argparse.ArgumentParser(description="EXP10 IPSNS repetition runner")
    parser.add_argument("--instances", choices=["common", "diagnostic"], default="common")
    parser.add_argument("--smoke", action="store_true", help="Run 3 instances × 3 seeds only")
    parser.add_argument("--resume", action="store_true", help="Resume (default behavior; flag for clarity)")
    args = parser.parse_args()

    instances = load_instances(args.instances)
    if args.smoke:
        instances = {k: v for k, v in instances.items() if k in ("stg", "s27", "r20_60")}
        seeds = [0, 1, 2]
    else:
        seeds = SEEDS

    git_sha = get_git_commit()
    src_sha = get_src_sha()
    meta = get_machine_meta()

    done_before, total = count_done(instances)
    print(f"EXP10 IPSNS: {len(instances)} instances × {len(seeds)} seeds = {len(instances)*len(seeds)} runs")
    print(f"Already done: {done_before}/{len(instances)*len(seeds)}")
    print(f"Git: {git_sha}")

    n_done = 0
    n_error = 0
    t_batch_start = time.time()

    for inst_name, inst_path in sorted(instances.items()):
        for seed in seeds:
            if is_done(inst_name, seed):
                continue

            rec_path = out_path(inst_name, seed)
            # Skip if record exists and is valid
            if os.path.exists(rec_path):
                try:
                    with open(rec_path) as f:
                        existing = json.load(f)
                    if existing.get("status") == "ok":
                        mark_done(inst_name, seed)
                        continue
                except Exception:
                    pass  # Re-run if record is corrupt

            t_run_start = time.perf_counter()
            record = run_one(inst_name, inst_path, seed, git_sha, src_sha, meta)
            runtime = time.perf_counter() - t_run_start

            write_record_atomic(record, rec_path)

            if record["status"] == "ok":
                mark_done(inst_name, seed)
                n_done += 1
                print(f"  [OK] {inst_name:30} seed={seed:2d} BW={record['objective_bw']:.1f}"
                      f"  improved={record.get('improved_over_seed',False)}"
                      f"  t={runtime:.2f}s")
            else:
                n_error += 1
                print(f"  [ERR] {inst_name:30} seed={seed:2d} ERROR: {record.get('error_message','')}")

    elapsed = time.time() - t_batch_start
    done_after, total = count_done(instances)
    print(f"\nDone. Completed {n_done} new runs, {n_error} errors.")
    print(f"Total done: {done_after}/{total}  Elapsed: {elapsed:.1f}s")

    if done_after == len(instances) * len(seeds):
        print("All IPSNS runs complete.")


if __name__ == "__main__":
    main()
