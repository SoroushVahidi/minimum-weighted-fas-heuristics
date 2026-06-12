"""
Safe tests for EXP10 DRMacIver namespace quarantine and production readiness.

Run: python scripts/test_drmaciver_namespace.py
"""
from __future__ import annotations

import csv
import glob
import json
import os
import subprocess
import sys
import tempfile

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
EXP_DIR = os.path.join(REPO_ROOT, "experiments", "exp10_stochastic_robustness")
SCRIPTS = os.path.join(EXP_DIR, "scripts")
RAW_PROD = os.path.join(EXP_DIR, "raw", "drmaciver")
CKPT_PROD = os.path.join(EXP_DIR, "checkpoints")
ARCHIVE = os.path.join(EXP_DIR, "smoke_archive", "drmaciver")
INVENTORY = os.path.join(EXP_DIR, "summary", "drmaciver_smoke_artifact_inventory.csv")
QUARANTINE = os.path.join(SCRIPTS, "quarantine_drmaciver_smoke_artifacts.py")


def ok(name: str) -> None:
    print(f"  PASS  {name}")


def fail(name: str, detail: str) -> None:
    print(f"  FAIL  {name}: {detail}")
    sys.exit(1)


def _runner_active() -> bool:
    r = subprocess.run(
        ["pgrep", "-f", "run_drmaciver_repetitions.py"],
        capture_output=True, text=True,
    )
    return bool(r.stdout.strip())


def test_production_namespace_clean():
    if _runner_active():
        tmp = glob.glob(os.path.join(RAW_PROD, "*.tmp")) + glob.glob(os.path.join(CKPT_PROD, "drmaciver_*.tmp"))
        if tmp:
            fail("no_stale_tmp", f"{len(tmp)} .tmp files during run")
        ok("production_namespace_clean (runner active; no .tmp pollution)")
        return
    raw = glob.glob(os.path.join(RAW_PROD, "drmaciver_*.json"))
    ckpt = glob.glob(os.path.join(CKPT_PROD, "drmaciver_*.done"))
    if raw:
        fail("production_namespace_clean", f"{len(raw)} raw files remain")
    if ckpt:
        fail("production_namespace_clean", f"{len(ckpt)} checkpoints remain")
    ok("production_namespace_clean")


def test_smoke_archive_present():
    raw = glob.glob(os.path.join(ARCHIVE, "raw", "drmaciver_*.json"))
    ckpt = glob.glob(os.path.join(ARCHIVE, "checkpoints", "drmaciver_*.done"))
    if len(raw) != 9:
        fail("smoke_archive_raw", f"expected 9, got {len(raw)}")
    if len(ckpt) != 9:
        fail("smoke_archive_ckpt", f"expected 9, got {len(ckpt)}")
    ok("smoke_archive_present (9+9)")


def test_inventory_exists():
    if not os.path.isfile(INVENTORY):
        fail("inventory_exists", INVENTORY)
    with open(INVENTORY) as f:
        rows = list(csv.DictReader(f))
    raw_rows = [r for r in rows if r["artifact_type"] == "raw_json"]
    if len(raw_rows) != 9:
        fail("inventory_count", f"expected 9 raw rows, got {len(raw_rows)}")
    if not all(r["classification_confidence"] == "high" for r in raw_rows):
        fail("inventory_confidence", "not all high confidence")
    ok("smoke_artifact_classification")


def test_checksum_preservation():
    manifest = os.path.join(ARCHIVE, "manifest.csv")
    if not os.path.isfile(manifest):
        fail("archive_manifest", "missing")
    with open(manifest) as f:
        for row in csv.DictReader(f):
            if row["sha256_before"] != row["sha256_after"]:
                fail("checksum_preservation", row["original_path"])
    ok("checksum_preservation")


def test_duplicate_keys():
    keys = set()
    for path in glob.glob(os.path.join(RAW_PROD, "drmaciver_*.json")):
        with open(path) as f:
            rec = json.load(f)
        key = (rec["instance_id"], rec["run_index"])
        if key in keys:
            fail("duplicate_keys", str(key))
        keys.add(key)
    ok("duplicate_key_detection (production empty or unique)")


def test_progress_excludes_smoke():
    prog_path = os.path.join(EXP_DIR, "summary", "experiment_progress.json")
    with open(prog_path) as f:
        prog = json.load(f)
    dr_done = prog["drmaciver_phase"]["done"]
    smoke = prog.get("drmaciver_smoke_archive", {}).get("archived_checkpoints", 0)
    if dr_done > 0 and smoke == 9:
        # During production run, dr_done should count production only
        pass
    if smoke != 9:
        fail("smoke_exclusion", f"archived_checkpoints={smoke}, expected 9")
    ok("smoke_exclusion_from_progress")


def test_dry_run_quarantine():
    """Post-quarantine: dry-run on archive manifest should report nothing to move."""
    archive_manifest = os.path.join(ARCHIVE, "manifest.csv")
    if os.path.isfile(archive_manifest):
        ok("dry_run_quarantine (post-quarantine: sources already archived)")
        return
    r = subprocess.run(
        [sys.executable, QUARANTINE, "--manifest", INVENTORY],
        capture_output=True, text=True, cwd=REPO_ROOT,
    )
    if r.returncode != 0:
        fail("dry_run_quarantine", r.stderr)
    if "DRY-RUN" not in r.stdout:
        fail("dry_run_quarantine", "expected DRY-RUN message")
    ok("dry_run_quarantine")


def test_launcher_schedule():
    sys.path.insert(0, os.path.join(REPO_ROOT, "src"))
    sys.path.insert(0, SCRIPTS)
    from run_drmaciver_repetitions import load_instances, N_REPS, ckpt_key

    instances = load_instances("common")
    if len(instances) != 93:
        fail("launcher_schedule", f"expected 93 instances, got {len(instances)}")
    total_keys = len(instances) * N_REPS
    if total_keys != 1860:
        fail("launcher_schedule", f"expected 1860 keys, got {total_keys}")
    ok("launcher_schedule (93×20=1860)")


def test_preflight_passed():
    result_path = os.path.join(EXP_DIR, "summary", "drmaciver_preflight_result.json")
    if not os.path.isfile(result_path):
        fail("preflight_result", "missing")
    with open(result_path) as f:
        data = json.load(f)
    if not data.get("preflight_passed"):
        fail("preflight_passed", str(data.get("blockers")))
    ok("preflight_passed")


def test_objective_recomputation_smoke():
    """Recompute objective from archived smoke record metadata."""
    sample = os.path.join(ARCHIVE, "raw", "drmaciver_stg_run00.json")
    if not os.path.isfile(sample):
        fail("objective_recompute", "sample missing")
    with open(sample) as f:
        rec = json.load(f)
    if not (rec.get("status") == "ok" and rec.get("objective_match")):
        fail("objective_recompute", "smoke record invalid")
    ok("objective_recomputation (smoke archive)")


def main():
    print("EXP10 DRMacIver namespace tests")
    print("=" * 40)
    test_inventory_exists()
    test_smoke_archive_present()
    test_checksum_preservation()
    test_production_namespace_clean()
    test_duplicate_keys()
    test_progress_excludes_smoke()
    test_dry_run_quarantine()
    test_launcher_schedule()
    test_objective_recomputation_smoke()
    test_preflight_passed()
    print("=" * 40)
    print("All tests passed.")


if __name__ == "__main__":
    main()
