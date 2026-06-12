"""Independently verify committed regression expected objectives."""

import json
from pathlib import Path

import pytest

from mwfas.exact import exact_min_fas_dp
from mwfas.io import read_graph_dimacs_agg
from tests.helpers.brute_force import brute_force_min_backward

FIXTURES = Path(__file__).resolve().parents[1] / "data" / "tiny_graphs"
EXPECTED = Path(__file__).resolve().parents[1] / "data" / "expected_results" / "regression_fixtures.json"


@pytest.mark.parametrize("name", ["triangle", "two_cycle", "dag_path"])
def test_exact_bw_matches_brute_force_and_dp(name, tol):
    dimacs = FIXTURES / f"{name}.d"
    edges, n2i, _ = read_graph_dimacs_agg(dimacs)
    n = len(n2i)
    exp = json.loads(EXPECTED.read_text(encoding="utf-8"))[name]
    dp_bw, _, _ = exact_min_fas_dp(edges, n)
    bf_bw, _ = brute_force_min_backward(edges, n)
    assert abs(dp_bw - bf_bw) < tol
    assert abs(dp_bw - exp["exact_bw"]) < tol
