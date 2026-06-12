"""Unit tests for WMSF (mwfas.wmsf)."""

import copy

import pytest

from mwfas.evaluation import compute_forward_backward
from mwfas.wmsf import (
    build_eid_graph_inout,
    wmsf_minimizeFas_scc,
    wmsf_removeArcs_scc,
    wmsf_stabilizeFas_scc,
    kosaraju_scc,
)
from tests.helpers.assertions import assert_inclusion_minimal_fas, assert_valid_fas
from tests.helpers.brute_force import fas_weight_from_removed, reference_backward_weight
from tests.helpers.graph_builders import scores_from_order, triangle_cycle, two_cycle


def _scc_graph(edges, n, tol=1e-12):
    U, V, W0, active, out_adj, in_adj = build_eid_graph_inout(edges, n, tol=tol)
    return U, V, W0, active, out_adj, in_adj


def test_removeArcs_makes_acyclic(tol):
    n, edges = triangle_cycle()
    U, V, W0, active, out_adj, in_adj = _scc_graph(edges, n, tol=tol)
    F, safe_tmp = wmsf_removeArcs_scc(n, U, V, W0, active, out_adj, in_adj, ordering="L2", tol=tol)
    for eid in F:
        active[eid] = 0
    for eid in safe_tmp:
        active[eid] = 1
    assert_valid_fas(n, U, V, W0, active, F, tol=tol)


def test_safe_edges_restored(tol):
    n, edges = triangle_cycle()
    U, V, W0, active, out_adj, in_adj = _scc_graph(edges, n, tol=tol)
    active_before = bytearray(active)
    F, safe_tmp = wmsf_removeArcs_scc(n, U, V, W0, active, out_adj, in_adj, ordering="L2", tol=tol)
    for eid in safe_tmp:
        assert active[eid] == 1
    for eid in safe_tmp:
        assert active_before[eid] == 1


def test_two_cycle_l1_vs_l2_selection(tol):
    n, edges = two_cycle(5.0, 2.0)
    U, V, W0, active1, out_adj, in_adj = _scc_graph(edges, n, tol=tol)
    active2 = bytearray(active1)
    F1, _ = wmsf_removeArcs_scc(n, U, V, W0, active1, out_adj, in_adj, ordering="L1", tol=tol)
    F2, _ = wmsf_removeArcs_scc(n, U, V, W0, active2, out_adj, in_adj, ordering="L2", tol=tol)
    assert len(F1) >= 1 and len(F2) >= 1


def test_minimizeFas_inclusion_minimal(tol):
    n, edges = triangle_cycle()
    U, V, W0, active, out_adj, in_adj = _scc_graph(edges, n, tol=tol)
    F, safe_tmp = wmsf_removeArcs_scc(n, U, V, W0, active, out_adj, in_adj, ordering="L2", tol=tol)
    for eid in F:
        active[eid] = 0
    F = wmsf_minimizeFas_scc(n, U, V, W0, active, out_adj, F, tol=tol)
    assert_inclusion_minimal_fas(n, U, V, W0, active, F, out_adj, tol=tol)


def test_safe_edge_recursive_chain(tol):
    """Regression: deleting u->v must enqueue out(u) and in(v) for safe-edge closure."""
    n = 4
    edges = [(0, 1, 1.0), (1, 2, 1.0), (2, 3, 1.0), (3, 0, 100.0)]
    U, V, W0, active, out_adj, in_adj = _scc_graph(edges, n, tol=tol)
    F, safe_tmp = wmsf_removeArcs_scc(n, U, V, W0, active, out_adj, in_adj, ordering="L2", tol=tol)
    for eid in F:
        active[eid] = 0
    for eid in safe_tmp:
        active[eid] = 1
    assert_valid_fas(n, U, V, W0, active, F, tol=tol)


def test_stabilization_may_change_objective_documented(tol):
    """Stabilization is not guaranteed non-worsening; record whether worsening occurs."""
    n, edges = triangle_cycle((5.0, 4.0, 1.0))
    U, V, W0, active, out_adj, in_adj = _scc_graph(edges, n, tol=tol)
    F, _ = wmsf_removeArcs_scc(n, U, V, W0, active, out_adj, in_adj, ordering="L2", tol=tol)
    for eid in F:
        active[eid] = 0
    F = wmsf_minimizeFas_scc(n, U, V, W0, active, out_adj, F, tol=tol)
    bw_before = fas_weight_from_removed(edges, {(U[e], V[e]) for e in F}, tol=tol)
    F2 = set(F)
    active2 = bytearray(active)
    wmsf_stabilizeFas_scc(n, U, V, W0, active2, out_adj, in_adj, F2, tol=tol)
    bw_after = fas_weight_from_removed(edges, {(U[e], V[e]) for e in F2}, tol=tol)
    # Test documents behavior; worsening is allowed by manuscript scope.
    assert bw_after >= bw_before - tol


def test_kosaraju_single_scc_triangle():
    n, edges = triangle_cycle()
    comps, comp_id = kosaraju_scc(n, edges)
    assert len(comps) == 1
    assert len(comps[0]) == 3
