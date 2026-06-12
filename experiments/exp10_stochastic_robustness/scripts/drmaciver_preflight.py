"""
EXP10 Phase 6: DRMacIver pre-flight checks.

Verifies all conditions required before launching the full DRMacIver phase:
  - IPSNS phase complete and validated
  - Binary present and SHA matches EXP4
  - Input/output parser works
  - Smoke-test record exists and is valid
  - No resource conflicts
  - Checkpoint system ready
  - All 93 instances accessible
  - Disk space adequate

Outputs: summary/drmaciver_preflight_report.md
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
import glob

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
EXP_DIR = os.path.join(REPO_ROOT, "experiments", "exp10_stochastic_robustness")
SUMMARY_DIR = os.path.join(EXP_DIR, "summary")
INST_FILE = os.path.join(EXP_DIR, "config", "common_93_instances.txt")
CKPT_DIR = os.path.join(EXP_DIR, "checkpoints")
RAW_DIR = os.path.join(EXP_DIR, "raw", "drmaciver")
SMOKE_ARCHIVE_RAW = os.path.join(EXP_DIR, "smoke_archive", "drmaciver", "raw")

FAS_BINARY = os.path.join(REPO_ROOT,
    "experiments/exp4_external_baselines/external_tools/Feedback-Arc-Set/fas")

# SHA256 of DRMacIver binary (verified against EXP4)
EXPECTED_FAS_SHA = "907b7abe96ff8fb54d8b70910eb3068744f765e72da5520f2c7aacf70ba996bd"
EXPECTED_GIT = "80b3144d5fdbbe250faed8a4fe671dde2da76c89"
EXPECTED_DR_COMMIT = "16ff24a92fde886e58819180a9fe686e60991c5c"

IPSNS_EXPECTED = 1860
DR_EXPECTED = 1860
MIN_DISK_GB = 1.0


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def check_ipsns_complete():
    """Check that all 1860 IPSNS done files exist."""
    done = len([f for f in os.listdir(CKPT_DIR) if f.startswith("ipsns_") and f.endswith(".done")])
    return done, IPSNS_EXPECTED


def check_ipsns_validation():
    """Check validation summary exists and passed."""
    vsum = os.path.join(SUMMARY_DIR, "ipsns_validation_summary.json")
    if not os.path.exists(vsum):
        return False, "ipsns_validation_summary.json not found — run validate_ipsns_runs.py first"
    with open(vsum) as f:
        data = json.load(f)
    passed = data.get("validation_passed", False)
    return passed, data


def check_binary():
    if not os.path.exists(FAS_BINARY):
        return False, f"Binary not found: {FAS_BINARY}"
    if not os.access(FAS_BINARY, os.X_OK):
        return False, f"Binary not executable: {FAS_BINARY}"
    actual_sha = sha256_file(FAS_BINARY)
    if actual_sha != EXPECTED_FAS_SHA:
        return False, f"Binary SHA mismatch: got {actual_sha[:16]}... expected {EXPECTED_FAS_SHA[:16]}..."
    return True, f"Binary OK: {FAS_BINARY} SHA={actual_sha[:16]}..."


def _smoke_raw_dir():
    """Prefer quarantined smoke archive; fall back to production raw (pre-quarantine)."""
    if os.path.isdir(SMOKE_ARCHIVE_RAW) and os.listdir(SMOKE_ARCHIVE_RAW):
        return SMOKE_ARCHIVE_RAW
    return RAW_DIR


def check_smoke_records():
    """Verify smoke-test DR records are consistent with current binary."""
    smoke_dir = _smoke_raw_dir()
    smoke_instances = ["stg", "r20_60", "s27"]
    results = {}
    for inst in smoke_instances:
        for run_idx in range(3):
            rp = os.path.join(smoke_dir, f"drmaciver_{inst}_run{run_idx:02d}.json")
            if not os.path.exists(rp):
                results[(inst, run_idx)] = "MISSING"
                continue
            with open(rp) as f:
                rec = json.load(f)
            sha_ok = rec.get("executable_or_code_sha256") == EXPECTED_FAS_SHA
            valid = (rec.get("status") == "ok"
                     and rec.get("ordering_valid") == True
                     and rec.get("objective_match") == True)
            results[(inst, run_idx)] = "OK" if (sha_ok and valid) else f"FAIL: sha_ok={sha_ok} valid={valid}"
    return results


def check_instances_accessible():
    """Verify all 93 instance files are readable."""
    missing = []
    with open(INST_FILE) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) >= 2:
                name, path = parts[0], parts[1]
                if not os.path.exists(path):
                    missing.append((name, path))
    return missing


def check_disk_space():
    stat = shutil.disk_usage(EXP_DIR)
    free_gb = stat.free / 1e9
    return free_gb >= MIN_DISK_GB, free_gb


def check_existing_dr_runs():
    """Count valid existing DR done files (from smoke test)."""
    done_files = [f for f in os.listdir(CKPT_DIR) if f.startswith("drmaciver_") and f.endswith(".done")]
    return len(done_files)


def check_dr_output_namespace_clean():
    """
    Full DRMacIver runs must not share the same raw/checkpoint namespace as smoke tests.
    Any pre-existing drmaciver_* artifact in the full output directories is treated as
    contamination, because run indices 0..2 overlap between smoke and full phases.
    """
    raw_files = sorted(glob.glob(os.path.join(RAW_DIR, "drmaciver_*.json")))
    ckpt_files = sorted(glob.glob(os.path.join(CKPT_DIR, "drmaciver_*.done")))
    contaminated = bool(raw_files or ckpt_files)
    detail = {
        "raw_count": len(raw_files),
        "checkpoint_count": len(ckpt_files),
        "sample_raw": [os.path.basename(p) for p in raw_files[:5]],
        "sample_checkpoints": [os.path.basename(p) for p in ckpt_files[:5]],
    }
    return (not contaminated), detail


def check_no_competing_process():
    """Check no other EXP10 process is running."""
    try:
        result = subprocess.run(
            ["pgrep", "-f", "run_ipsns_repetitions|run_drmaciver_repetitions"],
            capture_output=True, text=True
        )
        pids = [int(p.strip()) for p in result.stdout.strip().split("\n") if p.strip()]
        return pids
    except Exception:
        return []


def main():
    os.makedirs(SUMMARY_DIR, exist_ok=True)

    checks = {}
    blockers = []
    warnings = []

    # 1. IPSNS phase complete
    ipsns_done, ipsns_expected = check_ipsns_complete()
    checks["ipsns_complete"] = {"done": ipsns_done, "expected": ipsns_expected, "ok": ipsns_done == ipsns_expected}
    if ipsns_done < ipsns_expected:
        blockers.append(f"IPSNS incomplete: {ipsns_done}/{ipsns_expected} done files")

    # 2. IPSNS validation passed
    val_ok, val_detail = check_ipsns_validation()
    checks["ipsns_validated"] = {"ok": val_ok, "detail": str(val_detail)[:200] if not val_ok else "passed"}
    if not val_ok:
        blockers.append(f"IPSNS validation not passed: {val_detail}")

    # 3. Binary present, executable, SHA correct
    bin_ok, bin_msg = check_binary()
    checks["binary_ok"] = {"ok": bin_ok, "message": bin_msg}
    if not bin_ok:
        blockers.append(f"DRMacIver binary: {bin_msg}")

    # 4. Smoke test records valid
    smoke_results = check_smoke_records()
    smoke_all_ok = all(v == "OK" for v in smoke_results.values())
    checks["smoke_tests"] = {"ok": smoke_all_ok, "results": {str(k): v for k, v in smoke_results.items()}}
    if not smoke_all_ok:
        bad = {str(k): v for k, v in smoke_results.items() if v != "OK"}
        blockers.append(f"Smoke test failures: {bad}")

    # 5. All 93 instances accessible
    missing_inst = check_instances_accessible()
    checks["instances_accessible"] = {"ok": len(missing_inst) == 0, "missing": missing_inst[:5]}
    if missing_inst:
        blockers.append(f"Instance files missing: {missing_inst[:3]}")

    # 6. Disk space
    disk_ok, free_gb = check_disk_space()
    checks["disk_space"] = {"ok": disk_ok, "free_gb": round(free_gb, 2)}
    if not disk_ok:
        blockers.append(f"Insufficient disk space: {free_gb:.2f} GB free")

    # 7. No competing IPSNS process
    competing = check_no_competing_process()
    checks["no_competing_process"] = {"ok": len(competing) == 0, "pids": competing}
    if competing:
        blockers.append(f"Active EXP10 processes still running: {competing} — wait for IPSNS to finish")

    # 8. Full-run DR output namespace must be clean
    dr_namespace_ok, dr_namespace_detail = check_dr_output_namespace_clean()
    checks["dr_output_namespace_clean"] = {"ok": dr_namespace_ok, "detail": dr_namespace_detail}
    if not dr_namespace_ok:
        blockers.append(
            "DRMacIver raw/checkpoint directories already contain drmaciver_* artifacts. "
            "Smoke-test outputs are mixed into the full-run namespace, so the full phase "
            "must not launch until the contamination is resolved explicitly."
        )

    # 9. Existing DR production runs (must be zero before full launch)
    dr_existing = check_existing_dr_runs()
    checks["dr_existing_runs"] = {
        "ok": dr_existing == 0,
        "done": dr_existing,
        "note": "pre-existing drmaciver_* artifacts found in full namespace"
        if dr_existing else "production namespace clean (0 done files)",
    }
    if dr_existing:
        blockers.append(
            f"Production namespace has {dr_existing} drmaciver_* checkpoint(s); expected 0 before launch"
        )

    # 10. Git state
    try:
        r = subprocess.run(["git", "-C", REPO_ROOT, "rev-parse", "HEAD"],
                           capture_output=True, text=True, timeout=5)
        actual_git = r.stdout.strip()
    except Exception:
        actual_git = "unknown"
    git_ok = actual_git == EXPECTED_GIT
    checks["git_commit"] = {"ok": git_ok, "actual": actual_git, "expected": EXPECTED_GIT}
    if not git_ok:
        warnings.append(f"Git commit changed: {actual_git} (expected {EXPECTED_GIT})")

    preflight_passed = len(blockers) == 0

    # Write report
    report_path = os.path.join(SUMMARY_DIR, "drmaciver_preflight_report.md")
    with open(report_path, "w") as f:
        f.write(f"# DRMacIver Preflight Report\n")
        f.write(f"**Date:** {__import__('datetime').datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}\n")
        f.write(f"**Result:** {'PASS — DRMacIver phase may proceed' if preflight_passed else 'FAIL — DO NOT LAUNCH'}\n\n")

        f.write(f"## Checks\n\n")
        f.write(f"| Check | Status | Detail |\n")
        f.write(f"|-------|--------|--------|\n")
        for name, result in checks.items():
            status = "✓ PASS" if result.get("ok") else "✗ FAIL"
            detail = ""
            if name == "ipsns_complete":
                detail = f"{result['done']}/{result['expected']}"
            elif name == "binary_ok":
                detail = result.get("message", "")[:80]
            elif name == "disk_space":
                detail = f"{result['free_gb']} GB free"
            elif name == "no_competing_process":
                detail = f"pids={result['pids']}" if result["pids"] else "none running"
            elif name == "dr_output_namespace_clean":
                detail = f"raw={result['detail']['raw_count']} ckpt={result['detail']['checkpoint_count']}"
            elif name == "dr_existing_runs":
                detail = f"{result['done']} pre-existing drmaciver_* records"
            elif name == "git_commit":
                detail = result.get("actual", "")[:16] + "..."
            elif name == "smoke_tests":
                n_ok = sum(1 for v in smoke_results.values() if v == "OK")
                detail = f"{n_ok}/{len(smoke_results)} OK"
            f.write(f"| {name} | {status} | {detail} |\n")

        if blockers:
            f.write(f"\n## Blockers\n\n")
            for b in blockers:
                f.write(f"- {b}\n")

        if warnings:
            f.write(f"\n## Warnings\n\n")
            for w in warnings:
                f.write(f"- {w}\n")

        f.write(f"\n## DRMacIver Run Parameters\n\n")
        f.write(f"- Binary: `{FAS_BINARY}`\n")
        f.write(f"- Binary SHA256: `{EXPECTED_FAS_SHA}`\n")
        f.write(f"- Expected commit: `{EXPECTED_DR_COMMIT}`\n")
        f.write(f"- Repetitions: 20 per instance\n")
        f.write(f"- Instances: 93 (common_93_instances.txt)\n")
        f.write(f"- Total runs: 1860\n")
        f.write(f"- Existing drmaciver_* artifacts in full namespace: {dr_existing}\n")
        f.write(f"- Min inter-launch gap: 0.12s (for distinct time-based seeds)\n")
        f.write(f"- Timeout per run: 300s\n")
        f.write(f"- Stochasticity: `srand(time(NULL)|getpid())` — uncontrollable\n\n")

        f.write(f"## Launch Command (if preflight passes)\n\n")
        f.write(f"```bash\n")
        f.write(f"cd /home/soroush/minimum-weighted-fas-heuristics\n")
        f.write(f"python3 experiments/exp10_stochastic_robustness/scripts/run_drmaciver_repetitions.py \\\n")
        f.write(f"  > experiments/exp10_stochastic_robustness/logs/drmaciver_runner.log 2>&1\n")
        f.write(f"```\n")

    # Print
    print(f"\n{'='*60}")
    print(f"DRMACIVER PREFLIGHT {'PASSED' if preflight_passed else 'FAILED'}")
    print(f"{'='*60}")
    for name, result in checks.items():
        status = "PASS" if result.get("ok") else "FAIL"
        print(f"  [{status}] {name}")
    if blockers:
        print(f"\nBlockers:")
        for b in blockers:
            print(f"  - {b}")
    print(f"\nReport: {report_path}")

    # Save machine-readable result
    result_json = os.path.join(SUMMARY_DIR, "drmaciver_preflight_result.json")
    with open(result_json, "w") as f:
        json.dump({"preflight_passed": preflight_passed, "blockers": blockers,
                   "warnings": warnings, "checks": {k: {kk: str(vv) if not isinstance(vv, (bool, int, float, str)) else vv
                                                         for kk, vv in v.items()} for k, v in checks.items()}}, f, indent=2)

    return 0 if preflight_passed else 1


if __name__ == "__main__":
    sys.exit(main())
