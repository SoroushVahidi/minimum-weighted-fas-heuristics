"""Regression fixtures with committed expected objectives."""

import json
from pathlib import Path

import pytest

from mwfas.evaluation import compute_forward_backward
from mwfas.exact import exact_min_fas_from_dimacs
from mwfas.io import read_graph_dimacs_agg
from mwfas.ipsns import lns_merge_wmsf_lr_best_incumbent
from mwfas.lrta import paper_fas_ranking_from_dimacs_fast
from mwfas.wmsf import wmsf_ranking_from_dimacs_fast

FIXTURES = Path(__file__).resolve().parents[1] / "data" / "tiny_graphs"
EXPECTED = Path(__file__).resolve().parents[1] / "data" / "expected_results" / "regression_fixtures.json"


@pytest.fixture(scope="module")
def expected():
    return json.loads(EXPECTED.read_text(encoding="utf-8"))


@pytest.mark.parametrize("name", ["triangle", "two_cycle", "dag_path"])
def test_known_instance_objectives(name, expected, tmp_path, tol):
    dimacs = FIXTURES / f"{name}.d"
    exp = expected[name]
    edges, _, _ = read_graph_dimacs_agg(dimacs)

    lr_csv = tmp_path / f"{name}_lr.csv"
    _, _, _, lr_scores, _ = paper_fas_ranking_from_dimacs_fast(str(dimacs), str(lr_csv))
    _, _, lr_bw = compute_forward_backward(edges, lr_scores)
    assert abs(lr_bw - exp["lr_ta_bw"]) < tol

    wmsf_csv = tmp_path / f"{name}_wmsf.csv"
    _, _, _, wmsf_scores, _ = wmsf_ranking_from_dimacs_fast(str(dimacs), str(wmsf_csv))
    _, _, wmsf_bw = compute_forward_backward(edges, wmsf_scores)
    assert abs(wmsf_bw - exp["wmsf_bw"]) < tol

    exact_csv = tmp_path / f"{name}_exact.csv"
    _, _, _, opt_bw, _, exact_scores = exact_min_fas_from_dimacs(str(dimacs), str(exact_csv))
    assert abs(opt_bw - exp["exact_bw"]) < tol

    ipsns_csv = tmp_path / f"{name}_ipsns.csv"
    *_, ipsns_scores, _, info = lns_merge_wmsf_lr_best_incumbent(
        dimacs_path=str(dimacs),
        output_ranking_csv_path=str(ipsns_csv),
        iters=exp.get("ipsns_iters", 5),
        rng_seed=exp.get("ipsns_seed", 1),
        log_every=0,
        return_info=True,
    )
    _, _, ipsns_bw = compute_forward_backward(edges, ipsns_scores)
    assert ipsns_bw <= exp["exact_bw"] + tol
    assert info["final_bw"] <= info["best_seed_bw"] + tol
