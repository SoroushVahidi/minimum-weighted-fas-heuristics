"""Shared pytest fixtures for mwfas test suite."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = Path(__file__).resolve().parent / "data"
TINY_GRAPHS = DATA_DIR / "tiny_graphs"
EXPECTED = DATA_DIR / "expected_results"


@pytest.fixture
def tol():
    return 1e-12


@pytest.fixture
def repo_root():
    return REPO_ROOT


@pytest.fixture
def tiny_graphs_dir():
    return TINY_GRAPHS


@pytest.fixture
def expected_results():
    path = EXPECTED / "regression_fixtures.json"
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


@pytest.fixture
def tmp_dimacs(tmp_path):
    """Factory: write DIMACS lines to a temp file and return path."""

    def _write(lines: list[str]) -> Path:
        p = tmp_path / "graph.d"
        p.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return p

    return _write
