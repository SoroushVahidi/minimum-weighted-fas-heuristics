"""Unit tests for exact DP (mwfas.exact)."""

import pytest

from mwfas.evaluation import compute_forward_backward
from mwfas.exact import exact_min_fas_dp
from tests.helpers.brute_force import brute_force_min_backward
from tests.helpers.graph_builders import dag_path, triangle_cycle, two_cycle


def test_empty_graph():
    min_bw, max_fw, order = exact_min_fas_dp([], 0)
    assert min_bw == 0.0
    assert order == []


def test_triangle_matches_brute_force(tol):
    n, edges = triangle_cycle()
    min_bw, _, order = exact_min_fas_dp(edges, n)
    ref_bw, ref_order = brute_force_min_backward(edges, n)
    assert abs(min_bw - ref_bw) < tol
    scores = {v: i for i, v in enumerate(order)}
    _, _, bw = compute_forward_backward(edges, scores)
    assert abs(bw - min_bw) < tol


def test_dag_optimal_zero_backward(tol):
    n, edges = dag_path()
    min_bw, _, order = exact_min_fas_dp(edges, n)
    assert min_bw < tol


def test_two_cycle(tol):
    n, edges = two_cycle()
    min_bw, _, _ = exact_min_fas_dp(edges, n)
    ref_bw, _ = brute_force_min_backward(edges, n)
    assert abs(min_bw - ref_bw) < tol


def test_n_limit_raises():
    with pytest.raises(ValueError, match="exceeds the DP limit"):
        exact_min_fas_dp([], 21)


def test_parallel_edges_aggregated_in_dp(tol):
    n = 2
    edges = [(0, 1, 1.0), (0, 1, 2.0), (1, 0, 0.5)]
    min_bw, _, _ = exact_min_fas_dp(edges, n)
    ref_bw, _ = brute_force_min_backward(edges, n)
    assert abs(min_bw - ref_bw) < tol


def test_seeded_random_small_graphs(tol):
    import random

    rng = random.Random(42)
    for _ in range(20):
        n = rng.randint(1, 6)
        m = rng.randint(0, n * (n - 1))
        edges = []
        for _ in range(m):
            u, v = rng.randrange(n), rng.randrange(n)
            if u == v:
                continue
            edges.append((u, v, rng.uniform(0, 5)))
        if not edges:
            continue
        min_bw, _, order = exact_min_fas_dp(edges, n)
        ref_bw, _ = brute_force_min_backward(edges, n)
        assert abs(min_bw - ref_bw) < 1e-9
