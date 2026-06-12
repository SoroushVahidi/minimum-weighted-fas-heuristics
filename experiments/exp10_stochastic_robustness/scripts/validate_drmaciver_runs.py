"""
EXP10: Full validation of completed DRMacIver production runs.

Checks every production record (excludes smoke archive).
Outputs:
  summary/drmaciver_validation_report.csv
  summary/drmaciver_validation_summary.json
"""
import csv
import glob
import hashlib
import json
import os
import sys
from collections import Counter

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
EXP_DIR = os.path.join(REPO_ROOT, "experiments", "exp10_stochastic_robustness")
RAW_DIR = os.path.join(EXP_DIR, "raw", "drmaciver")
SMOKE_RAW = os.path.join(EXP_DIR, "smoke_archive", "drmaciver", "raw")
CKPT_DIR = os.path.join(EXP_DIR, "checkpoints")
SUMMARY_DIR = os.path.join(EXP_DIR, "summary")
INST_FILE = os.path.join(EXP_DIR, "config", "common_93_instances.txt")
MANIFEST_SHA = "df6cdbfce6f5cf25e979f63d0183e9ee3b576894e6def033931bdf9ff55b5426"
EXPECTED_GIT = "80b3144d5fdbbe250faed8a4fe671dde2da76c89"
EXPECTED_FAS_SHA = "907b7abe96ff8fb54d8b70910eb3068744f765e72da5520f2c7aacf70ba996bd"
N_INSTANCES = 93
N_REPS = 20
EXPECTED_KEYS = N_INSTANCES * N_REPS


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_manifest():
    instances = {}
    with open(INST_FILE) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) >= 2:
                instances[parts[0]] = parts[1]
    return instances


def smoke_shas():
    shas = set()
    if os.path.isdir(SMOKE_RAW):
        for fn in os.listdir(SMOKE_RAW):
            if fn.endswith(".json"):
                shas.add(sha256_file(os.path.join(SMOKE_RAW, fn)))
    return shas


def validate_record(rec, inst_sha_cache, smoke_content_shas):
    errors = []
    inst_id = rec.get("instance_id", "?")
    run_idx = rec.get("run_index", "?")
    tag = f"({inst_id}, run={run_idx})"

    if rec.get("algorithm") != "drmaciver":
        errors.append(f"{tag} wrong algorithm")

    path = rec.get("raw_output_path", "")
    if path and "smoke_archive" in path:
        errors.append(f"{tag} smoke archive path in production record")

    if rec.get("status") != "ok":
        errors.append(f"{tag} status={rec.get('status')}")

    if rec.get("git_commit") != EXPECTED_GIT:
        errors.append(f"{tag} git_commit mismatch")

    if rec.get("executable_or_code_sha256") != EXPECTED_FAS_SHA:
        errors.append(f"{tag} binary sha mismatch")

    inst_path = rec.get("instance_path", "")
    if inst_path:
        if inst_path not in inst_sha_cache:
            inst_sha_cache[inst_path] = sha256_file(inst_path) if os.path.exists(inst_path) else None
        exp_sha = inst_sha_cache[inst_path]
        if exp_sha and rec.get("instance_sha256") != exp_sha:
            errors.append(f"{tag} instance sha256 mismatch")

    if not rec.get("ordering_valid"):
        errors.append(f"{tag} ordering_valid=False")

    if not rec.get("objective_match"):
        errors.append(f"{tag} objective_match=False")

    bw = rec.get("objective_bw")
    if bw is None or not (isinstance(bw, (int, float)) and bw >= 0):
        errors.append(f"{tag} invalid objective_bw")

    rt = rec.get("runtime_seconds")
    if rt is None or rt < 0:
        errors.append(f"{tag} invalid runtime")

    if rec.get("pid") is None:
        errors.append(f"{tag} missing pid")

    ts_start = rec.get("timestamp_start", "")
    ts_end = rec.get("timestamp_end", "")
    if ts_start and ts_end and ts_end < ts_start:
        errors.append(f"{tag} timestamp incoherence")

    return errors


def main():
    os.makedirs(SUMMARY_DIR, exist_ok=True)
    manifest = load_manifest()
    assert sha256_file(INST_FILE) == MANIFEST_SHA, "manifest checksum drift"

    smoke_content_shas = smoke_shas()
    inst_sha_cache = {}
    rows = []
    keys = []
    status_counts = Counter()
    pids = []
    tmp_count = len(glob.glob(os.path.join(RAW_DIR, "*.tmp")))

    for rp in sorted(glob.glob(os.path.join(RAW_DIR, "drmaciver_*.json"))):
        content_sha = sha256_file(rp)
        if content_sha in smoke_content_shas:
            rows.append({
                "instance_id": "?", "run_index": "?", "status": "CONTAMINATION",
                "errors": "smoke archive content in production namespace", "file": rp,
            })
            continue
        try:
            with open(rp) as f:
                rec = json.load(f)
        except Exception as e:
            rows.append({"instance_id": "?", "run_index": "?", "status": "PARSE_ERROR",
                         "errors": str(e), "file": rp})
            status_counts["parse_error"] += 1
            continue

        inst_id = rec.get("instance_id")
        run_idx = rec.get("run_index")
        key = (inst_id, run_idx)
        keys.append(key)
        status_counts[rec.get("status", "unknown")] += 1
        if rec.get("pid"):
            pids.append(rec["pid"])

        errors = validate_record(rec, inst_sha_cache, smoke_content_shas)
        rows.append({
            "instance_id": inst_id,
            "run_index": run_idx,
            "status": "PASS" if not errors else "FAIL",
            "record_status": rec.get("status"),
            "objective_bw": rec.get("objective_bw"),
            "runtime_seconds": rec.get("runtime_seconds"),
            "pid": rec.get("pid"),
            "ordering_valid": rec.get("ordering_valid"),
            "objective_match": rec.get("objective_match"),
            "errors": "; ".join(errors),
            "file": os.path.basename(rp),
        })

    key_counts = Counter(keys)
    duplicates = [k for k, c in key_counts.items() if c > 1]
    expected_keys = {(inst, r) for inst in manifest for r in range(N_REPS)}
    present_ok = {(r["instance_id"], r["run_index"]) for r in rows if r["status"] == "PASS"}
    missing = sorted(expected_keys - set(keys))
    unexplained_missing = [k for k in missing
                           if not os.path.exists(os.path.join(CKPT_DIR,
                               f"drmaciver_{k[0]}_run{k[1]:02d}.done"))]

    n_pass = sum(1 for r in rows if r["status"] == "PASS")
    n_fail = sum(1 for r in rows if r["status"] == "FAIL")
    n_contam = sum(1 for r in rows if r["status"] == "CONTAMINATION")

    report_path = os.path.join(SUMMARY_DIR, "drmaciver_validation_report.csv")
    fieldnames = list(rows[0].keys()) if rows else ["instance_id", "run_index", "status", "errors"]
    with open(report_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    summary = {
        "validation_passed": (
            n_fail == 0 and n_contam == 0 and len(duplicates) == 0
            and len(keys) == EXPECTED_KEYS and len(unexplained_missing) == 0
            and tmp_count == 0
        ),
        "expected_keys": EXPECTED_KEYS,
        "records_found": len(rows),
        "pass": n_pass,
        "fail": n_fail,
        "contamination": n_contam,
        "duplicates": len(duplicates),
        "duplicate_keys": [list(k) for k in duplicates[:20]],
        "missing_keys": len(missing),
        "unexplained_missing": len(unexplained_missing),
        "status_counts": dict(status_counts),
        "timeout_count": status_counts.get("timeout", 0),
        "error_count": sum(status_counts.get(s, 0) for s in ("error", "parse_error", "invalid_ordering", "timeout")),
        "tmp_files": tmp_count,
        "unique_pids": len(set(pids)),
        "total_pids_recorded": len(pids),
        "manifest_sha256": MANIFEST_SHA,
        "binary_sha256": EXPECTED_FAS_SHA,
        "git_commit": EXPECTED_GIT,
        "smoke_excluded": True,
    }
    summary_path = os.path.join(SUMMARY_DIR, "drmaciver_validation_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\n{'='*60}")
    print(f"DRMACIVER VALIDATION {'PASSED' if summary['validation_passed'] else 'FAILED'}")
    print(f"{'='*60}")
    print(f"Expected:  {EXPECTED_KEYS}")
    print(f"Found:     {len(rows)}")
    print(f"PASS:      {n_pass}")
    print(f"FAIL:      {n_fail}")
    print(f"DUPLICATES:{len(duplicates)}")
    print(f"MISSING:   {len(missing)}")
    print(f"TMP:       {tmp_count}")
    print(f"Unique PIDs: {len(set(pids))}/{len(pids)}")
    print(f"\nOutputs:\n  {report_path}\n  {summary_path}")
    return 0 if summary["validation_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
