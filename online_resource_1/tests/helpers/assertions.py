"""Shared assertion helpers for algorithm tests."""

from __future__ import annotations

from copy import deepcopy

from mwfas.lrta import topo_order_active

from .brute_force import fas_weight_from_removed, reference_backward_weight


def assert_acyclic_active(n_nodes, adj, V, active, msg="active graph must be acyclic"):
    try:
        topo_order_active(n_nodes, adj, V, active)
    except RuntimeError as exc:
        raise AssertionError(msg) from exc


def assert_valid_fas(n_nodes, U, V, W0, active, removed_eids, tol=1e-12):
    out_adj = [[] for _ in range(n_nodes)]
    for eid in range(len(U)):
        if active[eid]:
            out_adj[U[eid]].append(eid)
    assert_acyclic_active(n_nodes, out_adj, V, active)

    for eid in range(len(U)):
        if W0[eid] <= tol:
            continue
        in_fas = eid in removed_eids
        is_active = bool(active[eid])
        assert in_fas != is_active, f"edge {eid} active/F inconsistency"


def assert_inclusion_minimal_fas(n_nodes, U, V, W0, active, removed_eids, out_adj, tol=1e-12):
    """Inclusion-minimal: no removed edge can be re-added without creating a cycle."""
    from mwfas.lrta import make_reachability_checker

    _, rank = topo_order_active(n_nodes, out_adj, V, active)
    reachable = make_reachability_checker(n_nodes, out_adj, V, active)

    for eid in list(removed_eids):
        u, v = U[eid], V[eid]
        if W0[eid] <= tol:
            continue
        if rank[u] < rank[v]:
            raise AssertionError(f"edge {eid} could be re-added via rank rule")
        if not reachable(v, u, rank=rank, rank_limit=rank[u]):
            raise AssertionError(f"edge {eid} could be re-added via reachability")


def assert_scores_match_order(scores, order):
    assert len(scores) == len(order)
    for i, v in enumerate(order):
        assert scores[v] == i


def assert_objective_consistent(edges_indexed, scores, prod_total, prod_fw, prod_bw, tol=1e-9):
    ref_bw = reference_backward_weight(edges_indexed, scores)
    assert abs(prod_bw - ref_bw) <= tol, f"backward mismatch prod={prod_bw} ref={ref_bw}"
    assert abs(prod_total - prod_fw - prod_bw) <= tol
    assert abs(prod_total - sum(w for _, _, w in edges_indexed)) <= tol


def snapshot_active_F(active, F):
    return (bytearray(active), set(F))


def assert_restored(before, after_active, after_F):
    b_act, b_F = before
    assert list(after_active) == list(b_act)
    assert set(after_F) == set(b_F)
