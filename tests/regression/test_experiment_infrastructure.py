"""Experiment infrastructure tests using isolated temporary directories only."""

import json
import os
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
EXP10_SCRIPTS = REPO / "experiments" / "exp10_stochastic_robustness" / "scripts"


def test_atomic_write_pattern(tmp_path):
    target = tmp_path / "out.json"
    tmp = tmp_path / "out.json.tmp"
    tmp.write_text(json.dumps({"x": 1}), encoding="utf-8")
    os.replace(tmp, target)
    assert target.is_file()
    assert not tmp.exists()


def test_checkpoint_done_gating(tmp_path):
    ckpt = tmp_path / "run_001.done"
    ckpt.write_text("ok\n", encoding="utf-8")
    assert ckpt.exists()
    completed = tmp_path / "COMPLETED.ok"
    completed.write_text("all\n", encoding="utf-8")
    assert completed.read_text().strip() == "all"


def test_malformed_json_rejected(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text("{not json", encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        json.loads(bad.read_text())


def test_exp10_namespace_helpers_importable():
    """Utility modules import without touching production EXP10 directories."""
    import importlib.util

    path = EXP10_SCRIPTS / "update_progress.py"
    spec = importlib.util.spec_from_file_location("update_progress", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert hasattr(mod, "CKPT_DIR")


def test_isolated_checkpoint_resume(tmp_path):
    """Simulate resume: skip if .done exists."""
    ckpt_dir = tmp_path / "checkpoints"
    ckpt_dir.mkdir()
    done = ckpt_dir / "job_1.done"
    pending = ckpt_dir / "job_2.done"
    done.touch()

    def should_run(job_id):
        return not (ckpt_dir / f"job_{job_id}.done").exists()

    assert not should_run(1)
    assert should_run(2)
    (ckpt_dir / "job_2.done").touch()
    assert not should_run(2)
