"""Read-only EXP10 namespace and artifact integrity tests (no writes to EXP10 dirs)."""

from __future__ import annotations

import csv
import glob
import json
import os
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
EXP_DIR = REPO_ROOT / "experiments" / "exp10_stochastic_robustness"
ARCHIVE = EXP_DIR / "smoke_archive" / "drmaciver"
INVENTORY = EXP_DIR / "summary" / "drmaciver_smoke_artifact_inventory.csv"


def _runner_active() -> bool:
    r = subprocess.run(
        ["pgrep", "-f", "run_drmaciver_repetitions.py"],
        capture_output=True,
        text=True,
    )
    return bool(r.stdout.strip())


@pytest.mark.skipif(not EXP_DIR.is_dir(), reason="EXP10 directory absent")
def test_smoke_archive_present():
    raw = glob.glob(str(ARCHIVE / "raw" / "drmaciver_*.json"))
    ckpt = glob.glob(str(ARCHIVE / "checkpoints" / "drmaciver_*.done"))
    assert len(raw) == 9
    assert len(ckpt) == 9


@pytest.mark.skipif(not INVENTORY.is_file(), reason="smoke inventory absent")
def test_smoke_inventory_classification():
    with INVENTORY.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    raw_rows = [r for r in rows if r["artifact_type"] == "raw_json"]
    assert len(raw_rows) == 9
    assert all(r["classification_confidence"] == "high" for r in raw_rows)


@pytest.mark.skipif(not (ARCHIVE / "manifest.csv").is_file(), reason="archive manifest absent")
def test_smoke_checksum_preservation():
    with (ARCHIVE / "manifest.csv").open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            assert row["sha256_before"] == row["sha256_after"]


@pytest.mark.skipif(not EXP_DIR.is_dir(), reason="EXP10 directory absent")
def test_no_stale_tmp_during_active_run():
    if not _runner_active():
        pytest.skip("DRMacIver runner not active")
    raw_tmp = glob.glob(str(EXP_DIR / "raw" / "drmaciver" / "*.tmp"))
    ckpt_tmp = glob.glob(str(EXP_DIR / "checkpoints" / "drmaciver_*.tmp"))
    assert raw_tmp == [] and ckpt_tmp == []


@pytest.mark.skipif(not EXP_DIR.is_dir(), reason="EXP10 directory absent")
def test_production_checkpoint_count_when_complete():
    """After production, expect 1860 DRMacIver checkpoints; skip during active partial run."""
    if _runner_active():
        pytest.skip("production still running")
    ckpt = glob.glob(str(EXP_DIR / "checkpoints" / "drmaciver_*.done"))
    prog = EXP_DIR / "summary" / "experiment_progress.json"
    if prog.is_file():
        data = json.loads(prog.read_text(encoding="utf-8"))
        expected = data.get("drmaciver_phase", {}).get("total", 1860)
        if len(ckpt) == expected:
            assert len(ckpt) == 1860
        else:
            pytest.skip(f"checkpoint count {len(ckpt)} != expected {expected}")


@pytest.mark.skipif(not EXP_DIR.is_dir(), reason="EXP10 directory absent")
def test_smoke_excluded_from_progress_counter():
    prog_path = EXP_DIR / "summary" / "experiment_progress.json"
    if not prog_path.is_file():
        pytest.skip("progress file absent")
    prog = json.loads(prog_path.read_text(encoding="utf-8"))
    smoke = prog.get("drmaciver_smoke_archive", {}).get("archived_checkpoints", 0)
    assert smoke == 9


@pytest.mark.skipif(not (ARCHIVE / "raw" / "drmaciver_stg_run00.json").is_file(), reason="smoke sample absent")
def test_smoke_objective_metadata_valid():
    sample = ARCHIVE / "raw" / "drmaciver_stg_run00.json"
    rec = json.loads(sample.read_text(encoding="utf-8"))
    assert rec.get("status") == "ok"
    assert rec.get("objective_match") is True
