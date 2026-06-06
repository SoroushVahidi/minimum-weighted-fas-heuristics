"""
Weighted Minimum Spanning Forest (WMSF) heuristic for weighted MFAS.

Implements the paper049 algorithm:
  Per SCC: removeArcs -> MinimizeFas -> StabilizeFas -> MinimizeFas

For single-SCC graphs, both L1 and L2 arc orderings are tried and the
better result (lower backward weight) is kept.
"""

import heapq
import math
from collections import defaultdict, deque

from .io import read_graph_dimacs_agg
from .evaluation import compute_forward_backward
from .lrta import topo_order_active, make_reachability_checker


# ---------------------------------------------------------------------------
# Graph representation: edge-ID arrays with out AND in adjacency
# ---------------------------------------------------------------------------

def build_eid_graph_inout(edges_indexed, n_nodes, tol=1e-12):
    """Build edge-ID arrays with both outgoing and incoming adjacency lists."""
    m = len(edges_indexed)
    U = [0] * m
    V = [0] * m
    W0 = [0.0] * m
    active = bytearray(m)
    out_adj = [[] for _ in range(n_nodes)]
    in_adj = [[] for _ in range(n_nodes)]

    for eid, (u, v, w) in enumerate(edges_indexed):
        U[eid] = u
        V[eid] = v
        W0[eid] = float(w)
        if w > tol:
            active[eid] = 1
        out_adj[u].append(eid)
        in_adj[v].append(eid)

    return U, V, W0, active, out_adj, in_adj


# ---------------------------------------------------------------------------
# SCC decomposition (Kosaraju, deterministic)
# ---------------------------------------------------------------------------

def kosaraju_scc(n_nodes, edges_indexed):
    """
    Compute SCCs via Kosaraju's algorithm.

    Returns:
        comps   : list of SCCs, each a list of vertex indices
        comp_id : list mapping each vertex to its SCC index
    """
    outN = [[] for _ in range(n_nodes)]
    inN = [[] for _ in range(n_nodes)]
    for (u, v, _w) in edges_indexed:
        outN[u].append(v)
        inN[v].append(u)

    seen = bytearray(n_nodes)
    order = []

    for s in range(n_nodes):
        if seen[s]:
            continue
        stack = [(s, 0)]
        seen[s] = 1
        while stack:
            u, it = stack[-1]
            if it >= len(outN[u]):
                order.append(u)
                stack.pop()
                continue
            v = outN[u][it]
            stack[-1] = (u, it + 1)
            if not seen[v]:
                seen[v] = 1
                stack.append((v, 0))

    comp_id = [-1] * n_nodes
    comps = []
    cid = 0

    for s in reversed(order):
        if comp_id[s] != -1:
            continue
        comp = []
        stack = [s]
        comp_id[s] = cid
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in inN[u]:
                if comp_id[v] == -1:
                    comp_id[v] = cid
                    stack.append(v)
        comps.append(comp)
        cid += 1

    return comps, comp_id


def edges_by_scc(edges_indexed, comp_id):
    """Return a dict mapping SCC index to its internal edge list (u,v,w,global_eid)."""
    by = defaultdict(list)
    for eid, (u, v, w) in enumerate(edges_indexed):
        if comp_id[u] == comp_id[v]:
            by[comp_id[u]].append((u, v, w, eid))
    return by


# ---------------------------------------------------------------------------
# Acyclicity check
# ---------------------------------------------------------------------------

def _is_acyclic_active(n_nodes, out_adj, V, active):
    try:
        _, rank = topo_order_active(n_nodes, out_adj, V, active)
        return True, rank
    except RuntimeError:
        return False, None


# ---------------------------------------------------------------------------
# WMSF Step 1: removeArcs (Section 2.1 of paper049)
# ---------------------------------------------------------------------------

def wmsf_removeArcs_scc(n_nodes, U, V, W0, active, out_adj, in_adj, ordering="L2", tol=1e-12):
    """
    Remove arcs to make the SCC acyclic using the given arc ordering (L1 or L2).

    Steps:
      1. Preprocess 2-cycles: remove the earlier arc in the ordering.
      2. Temporarily remove safe arcs (source-like or sink-like nodes).
      3. Delete arcs by ordering, checking acyclicity every alpha deletions.
      4. Restore safe arcs.
    """
    Win = [0.0] * n_nodes
    Wout = [0.0] * n_nodes
    for eid in range(len(U)):
        if not active[eid]:
            continue
        Wout[U[eid]] += W0[eid]
        Win[V[eid]] += W0[eid]

    eids = [eid for eid in range(len(U)) if active[eid]]

    if ordering.upper() == "L1":
        eids.sort(key=lambda eid: (W0[eid], U[eid], V[eid], eid))
    else:
        def keyL2(eid):
            denom = Win[U[eid]] + Wout[V[eid]]
            if denom <= 0.0:
                denom = 1.0
            return (W0[eid] / denom, W0[eid], U[eid], V[eid], eid)
        eids.sort(key=keyL2)

    F = set()

    # 2-cycle preprocessing
    pos = {eid: i for i, eid in enumerate(eids)}
    pair_to_eid = {(U[eid], V[eid]): eid for eid in eids}

    for eid in eids:
        if not active[eid]:
            continue
        u, v = U[eid], V[eid]
        rev = pair_to_eid.get((v, u))
        if rev is not None and active[rev] and pos[eid] < pos[rev]:
            active[eid] = 0
            F.add(eid)

    # safe arcs trimming
    indeg = [0] * n_nodes
    outdeg = [0] * n_nodes
    for u in range(n_nodes):
        for eid in out_adj[u]:
            if active[eid]:
                outdeg[u] += 1
                indeg[V[eid]] += 1

    q = deque()
    for eid in range(len(U)):
        if not active[eid]:
            continue
        u, v = U[eid], V[eid]
        if indeg[u] == 0 or outdeg[v] == 0:
            q.append(eid)

    safe_tmp = []
    while q:
        eid = q.popleft()
        if not active[eid]:
            continue
        u, v = U[eid], V[eid]
        if not (indeg[u] == 0 or outdeg[v] == 0):
            continue
        active[eid] = 0
        safe_tmp.append(eid)
        outdeg[u] -= 1
        indeg[v] -= 1
        for ee in out_adj[u]:
            if active[ee]:
                q.append(ee)
        for ee in in_adj[v]:
            if active[ee]:
                q.append(ee)

    # delete by ordering with periodic acyclicity check
    m_act = sum(1 for eid in range(len(U)) if active[eid])
    alpha = max(1, m_act // max(1, n_nodes))
    since_check = 0

    for eid in eids:
        if not active[eid]:
            continue
        active[eid] = 0
        F.add(eid)
        since_check += 1
        if since_check >= alpha:
            since_check = 0
            ok, _ = _is_acyclic_active(n_nodes, out_adj, V, active)
            if ok:
                break

    ok, _ = _is_acyclic_active(n_nodes, out_adj, V, active)
    if not ok:
        for eid in eids:
            if not active[eid]:
                continue
            active[eid] = 0
            F.add(eid)
            ok, _ = _is_acyclic_active(n_nodes, out_adj, V, active)
            if ok:
                break

    for eid in safe_tmp:
        active[eid] = 1

    return F, safe_tmp


# ---------------------------------------------------------------------------
# WMSF Step 2: MinimizeFas (Section 2.2 of paper049)
# ---------------------------------------------------------------------------

def wmsf_minimizeFas_scc(n_nodes, U, V, W0, active, out_adj, F, tol=1e-12):
    """
    Attempt to restore removed edges (heavy first) without creating cycles.

    Uses O(1) topo-rank fast path; falls back to reachability with rank pruning.
    """
    for eid in F:
        active[eid] = 0

    _, rank = topo_order_active(n_nodes, out_adj, V, active)
    reachable = make_reachability_checker(n_nodes, out_adj, V, active)

    cand = sorted(F, key=lambda eid: (-W0[eid], U[eid], V[eid], eid))

    for eid in cand:
        u, v = U[eid], V[eid]
        if rank[u] < rank[v]:
            active[eid] = 1
            F.discard(eid)
            continue
        if not reachable(v, u, rank=rank, rank_limit=rank[u]):
            active[eid] = 1
            F.discard(eid)
            _, rank = topo_order_active(n_nodes, out_adj, V, active)

    return F


# ---------------------------------------------------------------------------
# WMSF Step 3: StabilizeFas (Definition 2.1 + Section 2.3 of paper049)
# ---------------------------------------------------------------------------

def wmsf_stabilizeFas_scc(n_nodes, U, V, W0, active, out_adj, in_adj, F, tol=1e-12):
    """
    Stabilize the FAS by swapping in/out arc sets for nodes where it reduces cost.

    Runs for at most log2(n) passes or until no change occurs.
    """
    WinG = [0.0] * n_nodes
    WoutG = [0.0] * n_nodes
    for eid in range(len(U)):
        WoutG[U[eid]] += W0[eid]
        WinG[V[eid]] += W0[eid]

    max_passes = max(1, int(math.log2(max(2, n_nodes))))
    for _ in range(max_passes):
        order, _ = topo_order_active(n_nodes, out_adj, V, active)
        changed = False

        for v in order:
            WinStar = sum(W0[eid] for eid in in_adj[v] if active[eid])
            WoutStar = sum(W0[eid] for eid in out_adj[v] if active[eid])

            removed_in = WinG[v] - WinStar
            removed_out = WoutG[v] - WoutStar

            if removed_in > WoutStar + tol:
                for eid in out_adj[v]:
                    if active[eid]:
                        active[eid] = 0
                        F.add(eid)
                        changed = True
                for eid in in_adj[v]:
                    if (not active[eid]) and (eid in F):
                        active[eid] = 1
                        F.discard(eid)
                        changed = True

            elif removed_out > WinStar + tol:
                for eid in in_adj[v]:
                    if active[eid]:
                        active[eid] = 0
                        F.add(eid)
                        changed = True
                for eid in out_adj[v]:
                    if (not active[eid]) and (eid in F):
                        active[eid] = 1
                        F.discard(eid)
                        changed = True

        if not changed:
            break

    return F


# ---------------------------------------------------------------------------
# SCC pipeline helpers
# ---------------------------------------------------------------------------

def _sync_active_from_F(active, m, F):
    for eid in range(m):
        active[eid] = 0 if (eid in F) else 1


def _wmsf_pipeline_scc(k, U2, V2, W02, active2, out2, in2, ordering, tol=1e-12):
    """Run the paper-faithful SCC pipeline: removeArcs -> Minimize -> Stabilize -> Minimize."""
    F2, _ = wmsf_removeArcs_scc(k, U2, V2, W02, active2, out2, in2, ordering=ordering, tol=tol)
    for e in F2:
        active2[e] = 0

    F2 = wmsf_minimizeFas_scc(k, U2, V2, W02, active2, out2, F2, tol=tol)
    _sync_active_from_F(active2, len(U2), F2)

    F2 = wmsf_stabilizeFas_scc(k, U2, V2, W02, active2, out2, in2, F2, tol=tol)
    _sync_active_from_F(active2, len(U2), F2)

    F2 = wmsf_minimizeFas_scc(k, U2, V2, W02, active2, out2, F2, tol=tol)
    _sync_active_from_F(active2, len(U2), F2)

    return F2, active2


def _build_local_scc_graph(verts, e_list, tol=1e-12):
    """Build a local (re-indexed) graph for one SCC."""
    verts_sorted = sorted(verts)
    loc = {v: i for i, v in enumerate(verts_sorted)}
    k = len(verts_sorted)

    edges_local = [(loc[u], loc[v], w, eid_global) for (u, v, w, eid_global) in e_list]
    m_scc = len(edges_local)

    U2 = [0] * m_scc
    V2 = [0] * m_scc
    W02 = [0.0] * m_scc
    eidG = [0] * m_scc
    active2 = bytearray(m_scc)
    out2 = [[] for _ in range(k)]
    in2 = [[] for _ in range(k)]

    for eid2, (uu, vv, ww, eg) in enumerate(edges_local):
        U2[eid2] = uu
        V2[eid2] = vv
        W02[eid2] = float(ww)
        eidG[eid2] = eg
        if ww > tol:
            active2[eid2] = 1
        out2[uu].append(eid2)
        in2[vv].append(eid2)

    return k, U2, V2, W02, eidG, active2, out2, in2


# ---------------------------------------------------------------------------
# End-to-end entry point
# ---------------------------------------------------------------------------

def wmsf_ranking_from_dimacs_fast(dimacs_path, output_ranking_csv_path, ordering="L2", tol=1e-12):
    """
    Run WMSF on a DIMACS instance and write a ranking CSV.

    For single-SCC graphs, both L1 and L2 orderings are tried and the better
    result (lower backward weight) is kept.

    Returns:
        edges_indexed, node_to_index, index_to_node, scores, F_removed_pairs
    """
    import pandas as pd

    edges_indexed, node_to_index, index_to_node = read_graph_dimacs_agg(dimacs_path)
    n = len(node_to_index)

    comps, comp_id = kosaraju_scc(n, edges_indexed)
    by_scc = edges_by_scc(edges_indexed, comp_id)

    U, V, W0, active_glob0, out_adj_glob, in_adj_glob = build_eid_graph_inout(
        edges_indexed, n, tol=tol
    )

    nontrivial = [c for c in comps if len(c) > 1]
    whole_single_scc = len(nontrivial) == 1 and len(nontrivial[0]) == n

    def run_one(ordering_choice):
        active_glob = bytearray(active_glob0)
        F_global = set()

        for scc_idx, verts in enumerate(comps):
            e_list = by_scc.get(scc_idx, [])

            if len(verts) <= 1:
                for (u, v, w, eid) in e_list:
                    if u == v and w > tol:
                        F_global.add(eid)
                        active_glob[eid] = 0
                continue

            if not e_list:
                continue

            k, U2, V2, W02, eidG, active2, out2, in2 = _build_local_scc_graph(
                verts, e_list, tol=tol
            )
            F2, _ = _wmsf_pipeline_scc(
                k, U2, V2, W02, active2, out2, in2, ordering=ordering_choice, tol=tol
            )

            for eid2 in F2:
                eg = eidG[eid2]
                F_global.add(eg)
                active_glob[eg] = 0

        _, rank = topo_order_active(n, out_adj_glob, V, active_glob)
        scores = {i: int(rank[i]) for i in range(n)}
        _, _, bw = compute_forward_backward(edges_indexed, scores)
        return bw, scores, F_global, active_glob

    if whole_single_scc:
        bw1, scores1, F1, active1 = run_one("L1")
        bw2, scores2, F2, active2 = run_one("L2")
        best_scores, best_F = (scores1, F1) if bw1 <= bw2 else (scores2, F2)
    else:
        _, best_scores, best_F, _ = run_one(ordering)

    rows = [{"Node ID": str(index_to_node[i]).strip(), "Order": int(best_scores[i])} for i in range(n)]
    rows.sort(key=lambda r: r["Order"])
    pd.DataFrame(rows).to_csv(output_ranking_csv_path, index=False)

    F_removed_pairs = {(U[eid], V[eid]) for eid in best_F}
    return edges_indexed, node_to_index, index_to_node, best_scores, F_removed_pairs
