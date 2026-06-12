"""CLI smoke tests on tiny fixtures."""

import subprocess
import sys
from pathlib import Path

import os
import pandas as pd
import pytest

REPO = Path(__file__).resolve().parents[2]
FIXTURE = REPO / "tests" / "data" / "tiny_graphs" / "triangle.d"
SCRIPTS = REPO / "scripts"


def _run(script, extra_args):
    cmd = [sys.executable, str(SCRIPTS / script), "--input", str(FIXTURE), *extra_args]
    env = {**os.environ, "PYTHONPATH": str(REPO / "src")}
    return subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO), env=env)


@pytest.mark.parametrize(
    "script,extra",
    [
        ("run_lrta.py", ["--output", "OUT"]),
        ("run_wmsf.py", ["--output", "OUT", "--ordering", "L2"]),
        ("run_exact.py", []),
        ("run_ipsns.py", ["--output", "OUT", "--iters", "2", "--rng-seed", "1", "--log-every", "0"]),
    ],
)
def test_cli_smoke(script, extra, tmp_path):
    args = []
    for a in extra:
        if a == "OUT":
            args.append(str(tmp_path / "rank.csv"))
        else:
            args.append(a)
    if script == "run_exact.py":
        args.extend(["--output", str(tmp_path / "exact.csv")])
    r = _run(script, args)
    assert r.returncode == 0, r.stderr + r.stdout
    if script != "run_exact.py" or "--output" in extra or True:
        out_csv = tmp_path / ("rank.csv" if script != "run_exact.py" else "exact.csv")
        if out_csv.exists():
            df = pd.read_csv(out_csv)
            assert "Node ID" in df.columns and "Order" in df.columns
