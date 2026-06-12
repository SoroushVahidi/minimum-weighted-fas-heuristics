"""Unit tests for LR-TA (mwfas.lrta)."""

import copy

import pytest

from mwfas.lrta import (
    build_eid_graph,
    find_any_cycle_eids,
    local_ratio_fas_fast,
    topo_order_active,
)
from tests.helpers.assertions import (
    assert_inclusion_minimal_fas,
    assert_valid_fas,
)
from tests.helpers.graph_builders import (
    dag_path,
    parallel_edges,
    self_loop,
    triangle_cycle,
    two_cycle,
    zero_weight_cycle,
)


def _run_lrta(edges, n, add_back=True, tol=1e-12):
    removed, U, V, W0, active, adj = local_ratio_fas_fast(edges, n, tol=tol, add_back=add_back)
    return removed, U, V, W0, active, adj


def test_triangle_returns_acyclic_fas(tol):
    n, edges = triangle_cycle()
    removed, U, V, W0, active, adj = _run_lrta(edges, n, tol=tol)
    assert_valid_fas(n, U, V, W0, active, removed, tol=tol)
    assert len(removed) >= 1


def test_two_cycle_peeling(tol):
    n, edges = two_cycle()
    removed, U, V, W0, active, adj = _run_lrta(edges, n, tol=tol)
    assert_valid_fas(n, U, V, W0, active, removed, tol=tol)


def test_dag_no_removals_needed(tol):
    n, edges = dag_path()
    removed, U, V, W0, active, adj = _run_lrta(edges, n, tol=tol)
    assert len(removed) == 0
    assert_valid_fas(n, U, V, W0, active, removed, tol=tol)


def test_zero_weight_cycle_edge_handled(tol):
    n, edges = zero_weight_cycle()
    removed, U, V, W0, active, adj = _run_lrta(edges, n, tol=tol)
    assert_valid_fas(n, U, V, W0, active, removed, tol=tol)


def test_w0_not_corrupted(tol):
    n, edges = triangle_cycle()
    w0_before = [w for _, _, w in edges]
    removed, U, V, W0, active, adj = _run_lrta(edges, n, tol=tol)
    assert W0[: len(w0_before)] == w0_before or all(abs(a - b) < tol for a, b in zip(W0[: len(w0_before)], w0_before))


def test_residual_weights_nonnegative(tol):
    n, edges = triangle_cycle((1.0, 2.0, 3.0))
    removed, U, V, W0, active, adj = _run_lrta(edges, n, tol=tol)
    assert_valid_fas(n, U, V, W0, active, removed, tol=tol)


def test_addback_inclusion_minimal(tol):
    n, edges = triangle_cycle()
    removed, U, V, W0, active, adj = _run_lrta(edges, n, add_back=True, tol=tol)
    assert_inclusion_minimal_fas(n, U, V, W0, active, removed, adj, tol=tol)


def test_addback_uses_original_weights_not_residual(tol):
    n, edges = triangle_cycle((3.0, 3.0, 1.0))
    removed_no, *_ = _run_lrta(edges, n, add_back=False, tol=tol)
    removed_yes, U, V, W0, active, adj = _run_lrta(edges, n, add_back=True, tol=tol)
    assert len(removed_yes) <= len(removed_no)


def test_deterministic_on_triangle(tol):
    n, edges = triangle_cycle()
    r1, *_ = _run_lrta(edges, n, tol=tol)
    r2, *_ = _run_lrta(edges, n, tol=tol)
    assert r1 == r2


def test_simple_cycle_extraction_finds_cycle():
    n, edges = triangle_cycle()
    U, V, W0, W, active, adj = build_eid_graph(edges, n)
    cyc = find_any_cycle_eids(n, adj, U, V, active)
    assert cyc is not None
    assert len(cyc) >= 2


def test_phase1_only_still_acyclic(tol):
    n, edges = triangle_cycle()
    removed, U, V, W0, active, adj = _run_lrta(edges, n, add_back=False, tol=tol)
    assert_valid_fas(n, U, V, W0, active, removed, tol=tol)


def test_parallel_arcs_supported(tol):
    n, edges = parallel_edges()
    removed, U, V, W0, active, adj = _run_lrta(edges, n, tol=tol)
    assert_valid_fas(n, U, V, W0, active, removed, tol=tol)
