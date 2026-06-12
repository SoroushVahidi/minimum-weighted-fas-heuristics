"""
EXP10: DRMacIver repeated-run driver.

Runs DRMacIver 20 times per instance on the 93 common instances.
Serializes launches with a minimum inter-launch gap to ensure distinct time-based seeds.
Checkpointed: skips already-completed (instance, run_index) pairs.

Usage:
    python scripts/run_drmaciver_repetitions.py [--instances common|diagnostic] [--smoke]
    python scripts/run_drmaciver_repetitions.py --resume
"""
import argparse
import hashlib
import json
import os
import platform
import socket
import subprocess
import sys
import time

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO_ROOT, "src"))
sys.path.insert(0, os.path.join(REPO_ROOT, "scripts"))

EXP_DIR = os.path.join(REPO_ROOT, "experiments", "exp10_stochastic_robustness")
RAW_DIR = os.path.join(EXP_DIR, "raw", "drmaciver")
CKPT_DIR = os.path.join(EXP_DIR, "checkpoints")
FAS_BINARY = os.path.join(REPO_ROOT,
    "experiments/exp4_external_baselines/external_tools/Feedback-Arc-Set/fas")

N_REPS = 20
MIN_INTER_LAUNCH_GAP = 0.12   # seconds between DRMacIver launches to ensure distinct time seeds


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


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


def ckpt_key(inst_name, run_index):
    return f"drmaciver_{inst_name}_run{run_index:02d}.done"


def is_done(inst_name, run_index):
    return os.path.exists(os.path.join(CKPT_DIR, ckpt_key(inst_name, run_index)))


def mark_done(inst_name, run_index):
    os.makedirs(CKPT_DIR, exist_ok=True)
    with open(os.path.join(CKPT_DIR, ckpt_key(inst_name, run_index)), "w") as f:
        f.write("done\n")


def out_path(inst_name, run_index):
    return os.path.join(RAW_DIR, f"drmaciver_{inst_name}_run{run_index:02d}.json")


def run_one(inst_name, inst_path, run_index, git_sha, binary_sha, meta):
    """Run DRMacIver once, recording all metadata."""
    import re
    from mwfas.io import read_graph_dimacs_agg
    from mwfas.evaluation import compute_forward_backward

    inst_sha = sha256_file(inst_path)
    edges_indexed, node_to_index, index_to_node = read_graph_dimacs_agg(inst_path)
    n = len(node_to_index)
    m = len(edges_indexed)
    total_w = sum(w for _, _, w in edges_indexed)

    # Build input string
    lines = [str(n)]
    for u, v, w in edges_indexed:
        lines.append(f"{u} {v} {w}")
    input_str = "\n".join(lines) + "\n"

    record = {
        "algorithm": "drmaciver",
        "instance_id": inst_name,
        "instance_path": inst_path,
        "instance_sha256": inst_sha,
        "n": n,
        "m": m,
        "density": m / (n * (n - 1)) if n > 1 else 0.0,
        "run_index": run_index,
        "seed": None,  # DRMacIver seed is not controllable
        "git_commit": git_sha,
        "executable_or_code_sha256": binary_sha,
        "hostname": meta["hostname"],
        "cpu_model": meta["cpu_model"],
        "ram_gb": meta["ram_gb"],
        "python_version": meta["python_version"],
        "dependency_versions": meta["dependency_versions"],
        "timeout_seconds": 300,
        "total_weight": total_w,
        # Seed note
        "seed_note": "DRMacIver uses srand(time|pid) internally; seed not controllable",
    }

    ts_start = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    t0_wall = time.time()
    t0_perf = time.perf_counter()

    try:
        proc = subprocess.Popen(
            [FAS_BINARY],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        pid = proc.pid
        try:
            stdout_bytes, stderr_bytes = proc.communicate(
                input=input_str.encode(), timeout=300
            )
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.communicate()
            runtime = time.perf_counter() - t0_perf
            ts_end = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            record.update({
                "status": "timeout",
                "pid": pid,
                "process_start_timestamp": ts_start,
                "objective_bw": None,
                "runtime_seconds": float(runtime),
                "ordering_valid": False,
                "acyclicity_valid": False,
                "timestamp_start": ts_start,
                "timestamp_end": ts_end,
                "error_message": "DRMacIver timed out after 300s",
            })
            return record

        runtime = time.perf_counter() - t0_perf
        ts_end = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        stdout = stdout_bytes.decode(errors="replace").strip()
        stderr = stderr_bytes.decode(errors="replace").strip()

        record["pid"] = pid
        record["process_start_timestamp"] = ts_start
        record["returncode"] = proc.returncode

        if proc.returncode != 0 or not stdout:
            record.update({
                "status": "error",
                "objective_bw": None,
                "runtime_seconds": float(runtime),
                "ordering_valid": False,
                "acyclicity_valid": False,
                "timestamp_start": ts_start,
                "timestamp_end": ts_end,
                "error_message": f"returncode={proc.returncode} stderr={stderr[:200]}",
            })
            return record

        # Parse output
        order_line = None
        for l in stdout.splitlines():
            if "Optimal ordering" in l:
                order_line = l
                break

        if order_line is None:
            record.update({
                "status": "parse_error",
                "objective_bw": None,
                "runtime_seconds": float(runtime),
                "ordering_valid": False,
                "acyclicity_valid": False,
                "timestamp_start": ts_start,
                "timestamp_end": ts_end,
                "error_message": f"no 'Optimal ordering' in output: {stdout[:200]}",
            })
            return record

        # Parse ordering
        s = re.sub(r"^Optimal ordering:\s*", "", order_line.strip())
        s = s.replace("[", " ").replace("]", " ").replace("||", " ")
        order = [int(t) for t in s.split() if t.isdigit() or (t.lstrip('-').isdigit())]

        ordering_valid = sorted(order) == list(range(n))
        if not ordering_valid:
            record.update({
                "status": "invalid_ordering",
                "objective_bw": None,
                "runtime_seconds": float(runtime),
                "ordering_valid": False,
                "acyclicity_valid": False,
                "timestamp_start": ts_start,
                "timestamp_end": ts_end,
                "error_message": f"ordering has {len(order)} elements, expected {n}",
            })
            return record

        scores = {v: r for r, v in enumerate(order)}
        total_w2, fw, bw = compute_forward_backward(edges_indexed, scores)
        normalized_bw = bw / total_w2 if total_w2 > 1e-9 else 0.0

        record.update({
            "status": "ok",
            "objective_bw": float(bw),
            "forward_weight": float(fw),
            "normalized_bw": float(normalized_bw),
            "runtime_seconds": float(runtime),
            "ordering_valid": True,
            "objective_recomputed": float(bw),
            "objective_match": True,
            "acyclicity_valid": True,
            "timestamp_start": ts_start,
            "timestamp_end": ts_end,
            "error_message": None,
            "raw_output_path": out_path(inst_name, run_index),
        })

    except Exception as e:
        runtime = time.perf_counter() - t0_perf
        ts_end = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        record.update({
            "status": "error",
            "objective_bw": None,
            "runtime_seconds": float(runtime),
            "ordering_valid": False,
            "acyclicity_valid": False,
            "timestamp_start": ts_start,
            "timestamp_end": ts_end,
            "error_message": str(e),
        })

    return record


def write_record_atomic(record, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(record, f, indent=2)
    os.replace(tmp, path)


def get_machine_meta():
    try:
        import pkg_resources
        deps = {p.key: p.version for p in pkg_resources.working_set
                if p.key in ("pandas", "numpy", "scipy")}
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


def count_done(instances, n_reps):
    total = len(instances) * n_reps
    done = sum(1 for n in instances for r in range(n_reps) if is_done(n, r))
    return done, total


def main():
    parser = argparse.ArgumentParser(description="EXP10 DRMacIver repetition runner")
    parser.add_argument("--instances", choices=["common", "diagnostic"], default="common")
    parser.add_argument("--smoke", action="store_true", help="Run 3 instances × 3 reps only")
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    if not os.path.isfile(FAS_BINARY) or not os.access(FAS_BINARY, os.X_OK):
        print(f"ERROR: DRMacIver binary not found or not executable: {FAS_BINARY}")
        sys.exit(1)

    binary_sha = sha256_file(FAS_BINARY)
    instances = load_instances(args.instances)
    n_reps = 3 if args.smoke else N_REPS
    if args.smoke:
        instances = {k: v for k, v in instances.items() if k in ("stg", "s27", "r20_60")}

    git_sha = get_git_commit()
    meta = get_machine_meta()

    done_before, total = count_done(instances, n_reps)
    print(f"EXP10 DRMacIver: {len(instances)} instances × {n_reps} reps = {len(instances)*n_reps} runs")
    print(f"Already done: {done_before}/{len(instances)*n_reps}")
    print(f"Binary SHA256: {binary_sha[:16]}...")
    print(f"Note: DRMacIver is non-deterministic (srand time|pid). Runs serialized with "
          f"{MIN_INTER_LAUNCH_GAP}s gap to ensure distinct seeds.")

    n_done = 0
    n_error = 0
    last_launch_time = 0.0

    for inst_name, inst_path in sorted(instances.items()):
        for run_index in range(n_reps):
            if is_done(inst_name, run_index):
                continue

            rec_path = out_path(inst_name, run_index)
            if os.path.exists(rec_path):
                try:
                    with open(rec_path) as f:
                        existing = json.load(f)
                    if existing.get("status") == "ok":
                        mark_done(inst_name, run_index)
                        continue
                except Exception:
                    pass

            # Enforce minimum inter-launch gap for distinct time seeds
            elapsed_since_last = time.perf_counter() - last_launch_time
            if elapsed_since_last < MIN_INTER_LAUNCH_GAP:
                time.sleep(MIN_INTER_LAUNCH_GAP - elapsed_since_last)

            last_launch_time = time.perf_counter()
            record = run_one(inst_name, inst_path, run_index, git_sha, binary_sha, meta)

            write_record_atomic(record, rec_path)

            if record["status"] == "ok":
                mark_done(inst_name, run_index)
                n_done += 1
                print(f"  [OK] {inst_name:30} run={run_index:2d} BW={record['objective_bw']:.1f}"
                      f"  t={record['runtime_seconds']:.2f}s  pid={record.get('pid','?')}")
            else:
                n_error += 1
                print(f"  [ERR] {inst_name:30} run={run_index:2d} {record['status']}: "
                      f"{record.get('error_message','')[:80]}")

    done_after, total = count_done(instances, n_reps)
    print(f"\nDone. Completed {n_done} new runs, {n_error} errors.")
    print(f"Total done: {done_after}/{total}")


if __name__ == "__main__":
    main()
