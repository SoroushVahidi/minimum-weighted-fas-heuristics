"""
Topological-order extraction utilities and post-processing alternatives.

These functions do not modify FAS-construction algorithms. They evaluate how
different linear extensions of the same active DAG affect backward weight.
"""

from __future__ import annotations

import heapq
from typing import Callable, Iterable

from .evaluation import compute_forward_backward


def scores_from_rank(rank: list[int]) -> dict[int, int]:
    return {i: int(rank[i]) for i in range(len(rank))}


def backward_weight_from_rank(edges_indexed, rank: list[int]) -> float:
    scores = scores_from_rank(rank)
    _, _, bw = compute_forward_backward(edges_indexed, scores)
    return bw


def backward_set_pairs(edges_indexed, rank: list[int]) -> set[tuple[int, int]]:
    """B_pi = {(u,v) in A : rank[v] < rank[u]} using strict backward convention."""
    b = set()
    for u, v, w in edges_indexed:
        if rank[u] > rank[v]:
            b.add((u, v))
    return b


def removed_weight_from_eids(U, V, W0, removed_eids: Iterable[int], tol: float = 1e-12) -> float:
    return sum(W0[eid] for eid in removed_eids if W0[eid] > tol)


def extraction_gap(removed_w: float, backward_w: float) -> float:
    """w(F) - w(B_pi) for nonnegative weights."""
    return removed_w - backward_w


def topo_kahn_min_vertex(
    n_nodes: int,
    adj,
    V,
    active,
) -> tuple[list[int], list[int]]:
    """Repository default: Kahn with min-heap on vertex index."""
    from .lrta import topo_order_active

    return topo_order_active(n_nodes, adj, V, active)


def topo_kahn_max_vertex(n_nodes: int, adj, V, active) -> tuple[list[int], list[int]]:
    """Kahn with max-heap on vertex index (alternative tie-break)."""
    indeg = [0] * n_nodes
    for u in range(n_nodes):
        for eid in adj[u]:
            if active[eid]:
                indeg[V[eid]] += 1

    heap: list[int] = []
    for i in range(n_nodes):
        if indeg[i] == 0:
            heapq.heappush(heap, -i)

    order: list[int] = []
    while heap:
        u = -heapq.heappop(heap)
        order.append(u)
        for eid in adj[u]:
            if not active[eid]:
                continue
            v = V[eid]
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(heap, -v)

    if len(order) != n_nodes:
        raise RuntimeError("Topological sort failed: active graph is not acyclic.")

    rank = [0] * n_nodes
    for r, node in enumerate(order):
        rank[node] = r
    return order, rank


def topo_kahn_weighted_net(
    n_nodes: int,
    adj,
    V,
    W0,
    active,
) -> tuple[list[int], list[int]]:
    """Kahn with priority by active weighted out-degree minus in-degree (desc), then vertex id."""
    out_w = [0.0] * n_nodes
    in_w = [0.0] * n_nodes
    for u in range(n_nodes):
        for eid in adj[u]:
            if active[eid]:
                w = W0[eid]
                out_w[u] += w
                in_w[V[eid]] += w

    indeg = [0] * n_nodes
    for u in range(n_nodes):
        for eid in adj[u]:
            if active[eid]:
                indeg[V[eid]] += 1

    # max-heap via negated tuple: higher net score first, then smaller vertex id
    heap: list[tuple[float, int, int]] = []
    for i in range(n_nodes):
        if indeg[i] == 0:
            heapq.heappush(heap, (-(out_w[i] - in_w[i]), i, i))

    order: list[int] = []
    while heap:
        _, _, u = heapq.heappop(heap)
        order.append(u)
        for eid in adj[u]:
            if not active[eid]:
                continue
            v = V[eid]
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(heap, (-(out_w[v] - in_w[v]), v, v))

    if len(order) != n_nodes:
        raise RuntimeError("Topological sort failed: active graph is not acyclic.")

    rank = [0] * n_nodes
    for r, node in enumerate(order):
        rank[node] = r
    return order, rank


def insertion_refine_order(
    edges_indexed,
    order: list[int],
    max_passes: int = 2,
    *,
    active_precedence: list[tuple[int, int]] | None = None,
) -> list[int]:
    """
    Precedence-preserving single-vertex insertion refinement.

    When ``active_precedence`` is supplied as (u,v) pairs for the active DAG,
    every trial order must keep each active arc forward. This ensures the
    refinement is a linear extension of the same acyclic active graph.
    """
    n = len(order)

    def bw_for_order(ord_list: list[int]) -> float:
        scores = {node: i for i, node in enumerate(ord_list)}
        _, _, bw = compute_forward_backward(edges_indexed, scores)
        return bw

    def respects_active(ord_list: list[int]) -> bool:
        if not active_precedence:
            return True
        pos = {v: i for i, v in enumerate(ord_list)}
        return all(pos[u] < pos[v] for u, v in active_precedence)

    cur = list(order)
    best_bw = bw_for_order(cur)
    for _ in range(max_passes):
        improved = False
        for v in list(cur):
            old_pos = cur.index(v)
            cur.pop(old_pos)
            best_local = None
            best_local_bw = best_bw
            for new_pos in range(len(cur) + 1):
                trial = cur[:new_pos] + [v] + cur[new_pos:]
                if not respects_active(trial):
                    continue
                _, _, bw = compute_forward_backward(edges_indexed, scores := {node: i for i, node in enumerate(trial)})
                if bw < best_local_bw - 1e-15:
                    best_local_bw = bw
                    best_local = new_pos
            if best_local is not None:
                cur.insert(best_local, v)
                best_bw = best_local_bw
                improved = True
            else:
                cur.insert(old_pos, v)
        if not improved:
            break
    return cur


def active_precedence_pairs(U, V, active) -> list[tuple[int, int]]:
    return [(U[eid], V[eid]) for eid in range(len(U)) if active[eid]]


EXTRACTION_RULES: dict[str, Callable] = {
    "current_min_id": topo_kahn_min_vertex,
    "max_id": topo_kahn_max_vertex,
}


def apply_extraction_rule(
    rule_name: str,
    n_nodes: int,
    adj,
    V,
    W0,
    active,
) -> tuple[list[int], list[int]]:
    if rule_name == "weighted_net":
        return topo_kahn_weighted_net(n_nodes, adj, V, W0, active)
    if rule_name == "current_min_id":
        return topo_kahn_min_vertex(n_nodes, adj, V, active)
    if rule_name == "max_id":
        return topo_kahn_max_vertex(n_nodes, adj, V, active)
    raise ValueError(f"unknown extraction rule: {rule_name}")
