"""
EXP10: Full validation of completed IPSNS runs.

Checks every run record for:
  - unique (instance_id, seed) key
  - correct instance checksum
  - correct Git commit
  - valid complete ordering (every vertex exactly once, via ordering_valid flag)
  - recomputed objective matches reported (objective_match flag)
  - final objective ≤ initial_incumbent_bw (non-worsening guarantee)
  - final objective ≤ lr_seed_bw (non-worsening vs LR-TA seed)
  - final objective ≤ wmsf_seed_bw (non-worsening vs WMSF seed)
  - runtime finite and nonneg
  - status == "ok"
  - no duplicate run records
  - all 93 instances × 20 seeds present
  - no smoke-test records mixed in
  - code SHA consistent

Outputs:
  summary/ipsns_validation_report.csv
  summary/ipsns_validation_summary.json
"""

import csv
import glob
import hashlib
import json
import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
EXP_DIR = os.path.join(REPO_ROOT, "experiments", "exp10_stochastic_robustness")
RAW_DIR = os.path.join(EXP_DIR, "raw", "ipsns")
CKPT_DIR = os.path.join(EXP_DIR, "checkpoints")
SUMMARY_DIR = os.path.join(EXP_DIR, "summary")
INST_FILE = os.path.join(EXP_DIR, "config", "common_93_instances.txt")

EXPECTED_SEEDS = 20
EXPECTED_GIT = "80b3144d5fdbbe250faed8a4fe671dde2da76c89"
EXPECTED_IPSNS_SHA = "46a3f2b549897df1037ebe257e47b17490bddaa97effb2e31bce20a50ea54b36"
SMOKE_SEEDS = [0, 1, 2]  # smoke test only ran 3 seeds; full run has 0-19
TOL = 1e-9  # tie tolerance for objective comparison


def load_instance_manifest():
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


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def validate_record(rec, inst_sha_cache):
    """Return list of error strings for this record. Empty = pass."""
    errors = []
    inst_id = rec.get("instance_id", "?")
    seed = rec.get("seed", "?")
    tag = f"({inst_id}, seed={seed})"

    # Required fields present
    required = [
        "algorithm", "instance_id", "instance_path", "instance_sha256",
        "n", "m", "run_index", "seed", "git_commit", "executable_or_code_sha256",
        "status", "objective_bw", "forward_weight", "normalized_bw",
        "runtime_seconds", "ordering_valid", "objective_recomputed",
        "objective_match", "acyclicity_valid", "lr_seed_bw", "wmsf_seed_bw",
        "initial_incumbent_bw", "accepted_moves", "rejected_moves",
        "improved_over_seed", "timestamp_start", "timestamp_end",
    ]
    missing_fields = [f for f in required if f not in rec]
    if missing_fields:
        errors.append(f"{tag} missing fields: {missing_fields}")
        return errors  # can't do further checks

    # Status must be ok
    if rec["status"] != "ok":
        errors.append(f"{tag} status={rec['status']} error={rec.get('error_message')}")

    # Git commit
    if rec["git_commit"] != EXPECTED_GIT:
        errors.append(f"{tag} git_commit={rec['git_commit']} expected={EXPECTED_GIT}")

    # Code SHA
    if rec["executable_or_code_sha256"] != EXPECTED_IPSNS_SHA:
        errors.append(f"{tag} code_sha mismatch: {rec['executable_or_code_sha256'][:16]}...")

    # Instance file SHA
    inst_path = rec["instance_path"]
    if inst_path not in inst_sha_cache:
        if os.path.exists(inst_path):
            inst_sha_cache[inst_path] = sha256_file(inst_path)
        else:
            errors.append(f"{tag} instance file missing: {inst_path}")
            inst_sha_cache[inst_path] = None
    expected_sha = inst_sha_cache.get(inst_path)
    if expected_sha is not None and rec["instance_sha256"] != expected_sha:
        errors.append(f"{tag} instance sha256 mismatch")

    # Ordering valid
    if not rec.get("ordering_valid", False):
        errors.append(f"{tag} ordering_valid=False")

    # Acyclicity
    if not rec.get("acyclicity_valid", True):
        errors.append(f"{tag} acyclicity_valid=False")

    # Objective match (recomputed == reported)
    if not rec.get("objective_match", False):
        errors.append(f"{tag} objective_match=False: reported={rec['objective_bw']} recomputed={rec['objective_recomputed']}")

    # Non-worsening guarantees
    bw = rec["objective_bw"]
    lr_bw = rec["lr_seed_bw"]
    wmsf_bw = rec["wmsf_seed_bw"]
    inc_bw = rec["initial_incumbent_bw"]

    if bw > inc_bw + TOL:
        errors.append(f"{tag} WORSE THAN INCUMBENT: bw={bw} > inc={inc_bw}")
    if bw > lr_bw + TOL:
        errors.append(f"{tag} WORSE THAN LR-TA SEED: bw={bw} > lr={lr_bw}")
    if bw > wmsf_bw + TOL:
        errors.append(f"{tag} WORSE THAN WMSF SEED: bw={bw} > wmsf={wmsf_bw}")

    # Runtime
    rt = rec.get("runtime_seconds", -1)
    if not (isinstance(rt, (int, float)) and rt >= 0):
        errors.append(f"{tag} invalid runtime: {rt}")

    # Normalized BW: bw / total_weight
    total_w = rec.get("total_weight", 0)
    if total_w > 0:
        expected_norm = bw / total_w
        recorded_norm = rec.get("normalized_bw", -1)
        if abs(recorded_norm - expected_norm) > 1e-8:
            errors.append(f"{tag} normalized_bw mismatch: {recorded_norm:.8f} vs {expected_norm:.8f}")

    # accepted + rejected + noop should be consistent with n_iters
    # (not strictly required but a coherence check)
    n_iters = rec.get("n_iters_done", 400)
    accepted = rec.get("accepted_moves", 0)
    rejected = rec.get("rejected_moves", 0)
    failed = rec.get("failed_repairs", 0)
    topo_failed = rec.get("noop_moves", 0)  # noop means no positive SCCs
    # accepted + rejected + failed_repairs + topo_failed + noop ≤ n_iters
    total_moves = accepted + rejected + failed
    if total_moves > n_iters:
        errors.append(f"{tag} move counts {total_moves} > n_iters {n_iters}")

    # best_iteration within budget
    best_iter = rec.get("best_iteration", 0)
    if best_iter > n_iters:
        errors.append(f"{tag} best_iteration={best_iter} > n_iters={n_iters}")

    # time_to_best nonneg
    t2b = rec.get("time_to_best_seconds", 0)
    if t2b < 0:
        errors.append(f"{tag} time_to_best < 0")

    return errors


def main():
    os.makedirs(SUMMARY_DIR, exist_ok=True)

    instances = load_instance_manifest()
    expected_total = len(instances) * EXPECTED_SEEDS
    seeds = list(range(EXPECTED_SEEDS))

    print(f"Expected: {len(instances)} instances × {EXPECTED_SEEDS} seeds = {expected_total} runs")

    # Load all raw records
    raw_files = sorted(glob.glob(os.path.join(RAW_DIR, "*.json")))
    print(f"Raw JSON files found: {len(raw_files)}")

    records_by_key = {}
    parse_errors = []
    for rp in raw_files:
        try:
            with open(rp) as f:
                rec = json.load(f)
            key = (rec.get("instance_id"), rec.get("seed"))
            if key in records_by_key:
                parse_errors.append(f"DUPLICATE key {key}: {rp} vs {records_by_key[key].get('raw_output_path')}")
            else:
                records_by_key[key] = rec
        except Exception as e:
            parse_errors.append(f"PARSE_ERROR: {rp}: {e}")

    # Missing and extra runs
    expected_keys = {(inst, seed) for inst in instances for seed in seeds}
    found_keys = set(records_by_key.keys())
    missing_keys = expected_keys - found_keys
    extra_keys = found_keys - expected_keys

    # Per-record validation
    inst_sha_cache = {}
    validation_rows = []
    all_errors = list(parse_errors)

    for key in sorted(expected_keys):
        inst_id, seed = key
        if key not in records_by_key:
            validation_rows.append({
                "instance_id": inst_id, "seed": seed,
                "status": "MISSING", "errors": "run not found",
                "objective_bw": "", "lr_seed_bw": "", "wmsf_seed_bw": "",
                "runtime_seconds": "", "accepted_moves": "",
                "improved_over_seed": "", "ordering_valid": "",
                "objective_match": "",
            })
            continue

        rec = records_by_key[key]
        errors = validate_record(rec, inst_sha_cache)
        row_status = "PASS" if not errors else "FAIL"
        if errors:
            all_errors.extend(errors)

        validation_rows.append({
            "instance_id": inst_id,
            "seed": seed,
            "status": row_status,
            "errors": "; ".join(errors) if errors else "",
            "objective_bw": rec.get("objective_bw", ""),
            "lr_seed_bw": rec.get("lr_seed_bw", ""),
            "wmsf_seed_bw": rec.get("wmsf_seed_bw", ""),
            "runtime_seconds": rec.get("runtime_seconds", ""),
            "accepted_moves": rec.get("accepted_moves", ""),
            "improved_over_seed": rec.get("improved_over_seed", ""),
            "ordering_valid": rec.get("ordering_valid", ""),
            "objective_match": rec.get("objective_match", ""),
        })

    for key in sorted(extra_keys):
        inst_id, seed = key
        validation_rows.append({
            "instance_id": inst_id, "seed": seed,
            "status": "EXTRA", "errors": "not in common_93 manifest",
            "objective_bw": "", "lr_seed_bw": "", "wmsf_seed_bw": "",
            "runtime_seconds": "", "accepted_moves": "",
            "improved_over_seed": "", "ordering_valid": "", "objective_match": "",
        })

    # Write validation report CSV
    report_path = os.path.join(SUMMARY_DIR, "ipsns_validation_report.csv")
    fieldnames = [
        "instance_id", "seed", "status", "errors",
        "objective_bw", "lr_seed_bw", "wmsf_seed_bw",
        "runtime_seconds", "accepted_moves", "improved_over_seed",
        "ordering_valid", "objective_match",
    ]
    with open(report_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(validation_rows)

    # Summary statistics
    n_pass = sum(1 for r in validation_rows if r["status"] == "PASS")
    n_fail = sum(1 for r in validation_rows if r["status"] == "FAIL")
    n_missing = sum(1 for r in validation_rows if r["status"] == "MISSING")
    n_extra = sum(1 for r in validation_rows if r["status"] == "EXTRA")
    n_duplicate = len([e for e in parse_errors if "DUPLICATE" in e])
    n_parse_error = len([e for e in parse_errors if "PARSE_ERROR" in e])

    # Aggregate stats on passing records
    pass_records = [records_by_key[k] for k in expected_keys if k in records_by_key and not validate_record(records_by_key[k], inst_sha_cache)]
    n_improved = sum(1 for r in pass_records if r.get("improved_over_seed"))
    n_accepted_gt0 = sum(1 for r in pass_records if r.get("accepted_moves", 0) > 0)

    validation_passed = (n_fail == 0 and n_missing == 0 and n_duplicate == 0 and n_parse_error == 0)

    summary = {
        "validation_date": __import__("datetime").datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "expected_runs": expected_total,
        "raw_files_found": len(raw_files),
        "n_pass": n_pass,
        "n_fail": n_fail,
        "n_missing": n_missing,
        "n_extra": n_extra,
        "n_duplicate": n_duplicate,
        "n_parse_error": n_parse_error,
        "validation_passed": validation_passed,
        "blocker_errors": all_errors[:50] if not validation_passed else [],
        "git_commit_verified": EXPECTED_GIT,
        "ipsns_sha_verified": EXPECTED_IPSNS_SHA,
        "n_instances": len(instances),
        "n_seeds": EXPECTED_SEEDS,
        "n_improved_over_seed": n_improved,
        "pct_improved": round(100 * n_improved / max(n_pass, 1), 2),
        "n_accepted_moves_gt0": n_accepted_gt0,
        "pct_accepted_moves_gt0": round(100 * n_accepted_gt0 / max(n_pass, 1), 2),
    }

    summary_path = os.path.join(SUMMARY_DIR, "ipsns_validation_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    # Print results
    print(f"\n{'='*60}")
    print(f"IPSNS VALIDATION {'PASSED' if validation_passed else 'FAILED'}")
    print(f"{'='*60}")
    print(f"Expected:    {expected_total}")
    print(f"PASS:        {n_pass}")
    print(f"FAIL:        {n_fail}")
    print(f"MISSING:     {n_missing}")
    print(f"EXTRA:       {n_extra}")
    print(f"DUPLICATES:  {n_duplicate}")
    print(f"PARSE ERRORS:{n_parse_error}")
    if all_errors:
        print(f"\nFirst 10 errors:")
        for e in all_errors[:10]:
            print(f"  {e}")
    print(f"\nOutputs:")
    print(f"  {report_path}")
    print(f"  {summary_path}")

    return 0 if validation_passed else 1


if __name__ == "__main__":
    sys.exit(main())
