"""Property-style invariant tests (deterministic seeded generation)."""

import random

import pytest

from mwfas.evaluation import compute_forward_backward
from mwfas.exact import exact_min_fas_dp
from mwfas.ipsns import lns_merge_wmsf_lr_best_incumbent
from mwfas.lrta import local_ratio_fas_fast
from mwfas.wmsf import build_eid_graph_inout, wmsf_removeArcs_scc, wmsf_minimizeFas_scc
from tests.helpers.assertions import assert_inclusion_minimal_fas, assert_valid_fas
from tests.helpers.brute_force import brute_force_min_backward
from tests.helpers.graph_builders import edges_to_dimacs


def _random_edges(rng, n, m):
    edges = []
    for _ in range(m):
        u, v = rng.randrange(n), rng.randrange(n)
        if u == v:
            continue
        edges.append((u, v, rng.uniform(0.1, 5.0)))
    return edges


@pytest.mark.parametrize("seed", range(5))
def test_lrta_fas_invariant(seed, tol):
    rng = random.Random(seed)
    n = rng.randint(2, 6)
    edges = _random_edges(rng, n, rng.randint(n, n * 2))
    if not edges:
        pytest.skip("empty edge set")
    removed, U, V, W0, active, adj = local_ratio_fas_fast(edges, n, tol=tol)
    assert_valid_fas(n, U, V, W0, active, removed, tol=tol)


def test_exact_matches_brute_many_seeds(tol):
    rng = random.Random(123)
    for _ in range(15):
        n = rng.randint(1, 6)
        edges = _random_edges(rng, n, rng.randint(0, n * 2))
        min_bw, _, _ = exact_min_fas_dp(edges, n)
        ref_bw, _ = brute_force_min_backward(edges, n)
        assert abs(min_bw - ref_bw) < 1e-9


def test_objective_equivalence_random_scores(tol):
    rng = random.Random(7)
    edges = _random_edges(rng, 5, 8)
    order = list(range(5))
    rng.shuffle(order)
    scores = {v: i for i, v in enumerate(order)}
    total, fw, bw = compute_forward_backward(edges, scores)
    assert abs(total - fw - bw) < tol


def test_ipsns_not_worse_than_seed(tmp_dimacs, tol):
    rng = random.Random(0)
    n = 4
    edges = _random_edges(rng, n, 6)
    path = tmp_dimacs(
        edges_to_dimacs((str(u), str(v), w) for u, v, w in edges)
    )
    out = path.parent / "out.csv"
    *_, info = lns_merge_wmsf_lr_best_incumbent(
        dimacs_path=str(path),
        output_ranking_csv_path=str(out),
        iters=10,
        rng_seed=11,
        log_every=0,
        return_info=True,
    )
    assert info["final_bw"] <= info["best_seed_bw"] + tol
