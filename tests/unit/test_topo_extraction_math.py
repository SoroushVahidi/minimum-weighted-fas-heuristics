"""
Mathematical identities and counterexamples for topological extraction.

Expected values are computed independently (not via production evaluation alone).
"""

from __future__ import annotations

import itertools

import pytest

from mwfas.evaluation import compute_forward_backward
from mwfas.lrta import topo_order_active
from mwfas.topo_extraction import (
    apply_extraction_rule,
    backward_set_pairs,
    backward_weight_from_rank,
    extraction_gap,
    insertion_refine_order,
    removed_weight_from_eids,
    scores_from_rank,
)
from tests.helpers.brute_force import reference_backward_weight


def _rank_from_order(order: list[int]) -> list[int]:
    rank = [0] * len(order)
    for i, v in enumerate(order):
        rank[v] = i
    return rank


def _independent_backward_weight(edges, order: list[int]) -> float:
    scores = {v: i for i, v in enumerate(order)}
    return reference_backward_weight(edges, scores)


def _build_adj(n, edges, active_mask=None):
    adj = [[] for _ in range(n)]
    U, V, W0 = [], [], []
    for eid, (u, v, w) in enumerate(edges):
        U.append(u)
        V.append(v)
        W0.append(w)
        if active_mask is None or active_mask[eid]:
            adj[u].append(eid)
    active = bytearray([1 if active_mask is None or active_mask[eid] else 0 for eid in range(len(edges))])
    return U, V, W0, active, adj


# --- Counterexample 1: two topo orders, different backward weight ---
def test_counterexample_two_orders_differ():
    # Original graph: 0->1 (10), 0->2 (1), 1->2 (1). Active DAG: 0->1, 0->2, 1->2 (remove nothing)
    edges = [(0, 1, 10.0), (0, 2, 1.0), (1, 2, 1.0)]
    order_a = [0, 1, 2]
    order_b = [0, 2, 1]  # also valid topo of same DAG
    bw_a = _independent_backward_weight(edges, order_a)
    bw_b = _independent_backward_weight(edges, order_b)
    assert bw_a == 0.0
    assert abs(bw_b - 1.0) < 1e-12  # arc (1,2) backward


# --- Counterexample 2: removed edge can be forward in a valid topo order ---
def test_counterexample_removed_edge_forward_in_order():
    # Active: 0->2, 1->2. Removed: (1,0) weight 10.
    edges = [(0, 2, 1.0), (1, 2, 1.0), (1, 0, 10.0)]
    order_forward = [1, 0, 2]
    rank = _rank_from_order(order_forward)
    b = backward_set_pairs(edges, rank)
    assert (1, 0) not in b
    assert _independent_backward_weight(edges, order_forward) < 1e-12


# --- Counterexample 3: B_pi strict subset of F ---
def test_counterexample_backward_strict_subset_of_removed():
    edges = [(0, 2, 1.0), (1, 2, 1.0), (1, 0, 5.0)]
    removed = {(1, 0)}
    order = [1, 0, 2]
    rank = _rank_from_order(order)
    b = backward_set_pairs(edges, rank)
    assert b == set()
    assert len(b) < len(removed)
    w_f = sum(w for u, v, w in edges if (u, v) in removed)
    w_b = _independent_backward_weight(edges, order)
    assert w_f == 5.0 and w_b == 0.0


# --- Counterexample 4: min-id tie-break worse than max-id on same active DAG ---
def test_counterexample_min_id_worse_than_max_id():
    edges = [(0, 2, 1.0), (1, 2, 1.0), (1, 0, 10.0)]
    n = 3
    active_mask = [True, True, False]
    U, V, W0, active, adj = _build_adj(n, edges, active_mask)
    _, rank_min = topo_order_active(n, adj, V, active)
    _, rank_max = apply_extraction_rule("max_id", n, adj, V, W0, active)
    bw_min = backward_weight_from_rank(edges, rank_min)
    bw_max = backward_weight_from_rank(edges, rank_max)
    assert bw_min > bw_max + 1.0


# --- Counterexample 5: insertion refinement can improve ---
def test_counterexample_insertion_improves():
    edges = [(0, 2, 1.0), (1, 2, 1.0), (1, 0, 10.0)]
    order_bad = [0, 1, 2]
    prec = [(0, 2), (1, 2)]
    refined = insertion_refine_order(
        edges, order_bad, max_passes=2, active_precedence=prec
    )
    assert _independent_backward_weight(edges, refined) < _independent_backward_weight(edges, order_bad) - 1.0


# --- Counterexample 6: zero-weight removed, weight equality but set inequality ---
def test_counterexample_zero_weight_removed_set_inequality():
    edges = [(0, 2, 1.0), (1, 2, 1.0), (1, 0, 0.0)]
    removed = {(1, 0)}
    order = [1, 0, 2]
    rank = _rank_from_order(order)
    b = backward_set_pairs(edges, rank)
    assert b == set()
    assert removed != b
    w_removed = sum(w for u, v, w in edges if (u, v) in removed)
    w_b = _independent_backward_weight(edges, order)
    assert w_removed == 0.0
    assert w_b == 0.0


# --- Identities ---
def test_backward_subset_of_removed_for_active_dag():
    edges = [(0, 1, 2.0), (1, 2, 3.0), (2, 0, 4.0)]
    n = 3
    # active DAG 0->1->2, removed (2,0)
    active_mask = [True, True, False]
    U, V, W0, active, adj = _build_adj(n, edges, active_mask)
    removed_eids = {2}
    _, rank = topo_order_active(n, adj, V, active)
    b = backward_set_pairs(edges, rank)
    removed_pairs = {(U[e], V[e]) for e in removed_eids}
    assert b.issubset(removed_pairs)


def test_nonnegative_weight_inequality():
    edges = [(0, 1, 2.0), (1, 2, 3.0), (2, 0, 4.0)]
    n = 3
    active_mask = [True, True, False]
    U, V, W0, active, adj = _build_adj(n, edges, active_mask)
    removed_eids = {2}
    _, rank = topo_order_active(n, adj, V, active)
    w_b = backward_weight_from_rank(edges, rank)
    w_f = removed_weight_from_eids(U, V, W0, removed_eids)
    assert w_b <= w_f + 1e-12


def test_strict_positive_equality_iff_set_equality():
    edges = [(0, 1, 2.0), (1, 2, 3.0), (2, 0, 4.0)]
    n = 3
    active_mask = [True, True, False]
    U, V, W0, active, adj = _build_adj(n, edges, active_mask)
    removed_eids = {2}
    _, rank = topo_order_active(n, adj, V, active)
    b = backward_set_pairs(edges, rank)
    removed_pairs = {(U[e], V[e]) for e in removed_eids}
    w_b = backward_weight_from_rank(edges, rank)
    w_f = removed_weight_from_eids(U, V, W0, removed_eids)
    if all(W0[e] > 0 for e in removed_eids):
        assert (abs(w_b - w_f) < 1e-12) == (b == removed_pairs)


def test_extraction_determinism():
    edges = [(0, 1, 1.0), (0, 2, 2.0), (1, 3, 3.0), (2, 3, 4.0)]
    n = 4
    U, V, W0, active, adj = _build_adj(n, edges)
    o1, r1 = topo_order_active(n, adj, V, active)
    o2, r2 = topo_order_active(n, adj, V, active)
    assert o1 == o2 and r1 == r2


def test_independent_recomputation_matches_production():
    edges = [(0, 1, 3.0), (1, 2, 2.0), (2, 0, 1.0)]
    order = [0, 1, 2]
    scores = scores_from_rank(_rank_from_order(order))
    prod = compute_forward_backward(edges, scores)[2]
    ref = reference_backward_weight(edges, scores)
    assert abs(prod - ref) < 1e-12


def test_all_topo_orders_valid_linear_extensions():
    edges = [(0, 1, 1.0), (0, 2, 1.0), (1, 3, 1.0), (2, 3, 1.0)]
    n = 4
    U, V, W0, active, adj = _build_adj(n, edges)
    for perm in itertools.permutations(range(n)):
        ok = True
        for u, v, _ in edges:
            if perm[u] > perm[v]:
                ok = False
                break
        if ok:
            rank = _rank_from_order(list(perm))
            # must be topological
            for u, v, _ in edges:
                assert rank[u] < rank[v]


def test_extraction_gap_nonnegative():
    edges = [(0, 1, 1.0), (1, 2, 1.0), (2, 0, 5.0)]
    n = 3
    active_mask = [True, True, False]
    U, V, W0, active, adj = _build_adj(n, edges, active_mask)
    removed_eids = {2}
    _, rank = topo_order_active(n, adj, V, active)
    gap = extraction_gap(
        removed_weight_from_eids(U, V, W0, removed_eids),
        backward_weight_from_rank(edges, rank),
    )
    assert gap >= -1e-12
