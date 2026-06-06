"""
Local-Ratio Topological Add-back (LR-TA) algorithm for weighted MFAS.

Phase 1: iterative local-ratio cycle reductions until the graph is a DAG.
Phase 2: add-back removed edges (heavy first) that can be restored without
         creating a cycle, using topological rank pruning for speed.
"""

import heapq

from .io import read_graph_dimacs_agg
from .evaluation import compute_forward_backward


# ---------------------------------------------------------------------------
# Graph representation: edge-ID arrays + active bytearray (outgoing only)
# ---------------------------------------------------------------------------

def build_eid_graph(edges_indexed, n_nodes, tol=1e-12):
    """
    Convert edges_indexed into parallel edge-id arrays for fast iteration.

    Returns:
        U, V  : endpoint arrays (int)
        W0    : original weights (float)
        W     : mutable reduced weights (float)
        active: bytearray, 1 if edge is active
        adj   : list of outgoing edge-id lists per node
    """
    m = len(edges_indexed)
    U = [0] * m
    V = [0] * m
    W0 = [0.0] * m
    W = [0.0] * m
    active = bytearray(m)
    adj = [[] for _ in range(n_nodes)]

    for eid, (u, v, w) in enumerate(edges_indexed):
        U[eid] = u
        V[eid] = v
        W0[eid] = float(w)
        W[eid] = float(w)
        if w > tol:
            active[eid] = 1
        adj[u].append(eid)

    return U, V, W0, W, active, adj


# ---------------------------------------------------------------------------
# Cycle detection (iterative DFS, resets only touched nodes)
# ---------------------------------------------------------------------------

def find_any_cycle_eids(n_nodes, adj, U, V, active):
    """
    Find any directed cycle in the active graph via iterative DFS.

    Returns a list of edge IDs forming a cycle, or None if acyclic.
    """
    state = bytearray(n_nodes)
    parent = [-1] * n_nodes
    parent_eid = [-1] * n_nodes
    next_ptr = [0] * n_nodes
    visited_nodes = []

    def reset():
        for x in visited_nodes:
            state[x] = 0
            parent[x] = -1
            parent_eid[x] = -1
            next_ptr[x] = 0
        visited_nodes.clear()

    for s in range(n_nodes):
        if state[s] != 0:
            continue

        stack = [s]
        state[s] = 1
        visited_nodes.append(s)

        while stack:
            u = stack[-1]
            i = next_ptr[u]
            out = adj[u]
            while i < len(out) and active[out[i]] == 0:
                i += 1
            next_ptr[u] = i

            if i >= len(out):
                state[u] = 2
                stack.pop()
                continue

            eid = out[i]
            v = V[eid]
            next_ptr[u] = i + 1

            if state[v] == 0:
                parent[v] = u
                parent_eid[v] = eid
                state[v] = 1
                visited_nodes.append(v)
                stack.append(v)
            elif state[v] == 1:
                cycle_eids = [eid]
                cur = u
                while cur != v:
                    pe = parent_eid[cur]
                    if pe == -1:
                        break
                    cycle_eids.append(pe)
                    cur = parent[cur]
                    if cur == -1:
                        break
                if cur == v:
                    cycle_eids.reverse()
                    reset()
                    return cycle_eids

    reset()
    return None


# ---------------------------------------------------------------------------
# Topological sort (Kahn, deterministic via min-heap)
# ---------------------------------------------------------------------------

def topo_order_active(n_nodes, adj, V, active):
    """
    Kahn topological sort on the active subgraph.

    Returns (order, rank) where rank[node] gives its position 0..n-1.
    Raises RuntimeError if the active graph is not acyclic.
    """
    indeg = [0] * n_nodes
    for u in range(n_nodes):
        for eid in adj[u]:
            if active[eid]:
                indeg[V[eid]] += 1

    heap = []
    for i in range(n_nodes):
        if indeg[i] == 0:
            heapq.heappush(heap, i)

    order = []
    while heap:
        u = heapq.heappop(heap)
        order.append(u)
        for eid in adj[u]:
            if not active[eid]:
                continue
            v = V[eid]
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(heap, v)

    if len(order) != n_nodes:
        raise RuntimeError("Topological sort failed: active graph is not acyclic.")

    rank = [0] * n_nodes
    for r, node in enumerate(order):
        rank[node] = r
    return order, rank


# ---------------------------------------------------------------------------
# Reachability check (stamp-based visited, pruned by topo rank interval)
# ---------------------------------------------------------------------------

def make_reachability_checker(n_nodes, adj, V, active):
    """
    Return a closure reachable(src, target, rank, rank_limit) that tests
    whether target is reachable from src in the active graph, pruning
    nodes whose rank exceeds rank_limit.
    """
    visited = [0] * n_nodes
    stamp = 0

    def reachable(src, target, rank, rank_limit):
        nonlocal stamp
        stamp += 1
        st = stamp

        if src == target:
            return True
        if rank[src] > rank_limit:
            return False

        stack = [src]
        visited[src] = st

        while stack:
            x = stack.pop()
            for eid in adj[x]:
                if not active[eid]:
                    continue
                y = V[eid]
                if rank[y] > rank_limit:
                    continue
                if y == target:
                    return True
                if visited[y] != st:
                    visited[y] = st
                    stack.append(y)
        return False

    return reachable


# ---------------------------------------------------------------------------
# Core LR-TA algorithm
# ---------------------------------------------------------------------------

def local_ratio_fas_fast(edges_indexed, n_nodes, tol=1e-12):
    """
    Compute a minimal weighted FAS via local-ratio cycle reductions + add-back.

    Phase 1 (cycle reductions): repeatedly find a cycle, subtract the minimum
    edge weight from all edges on the cycle; edges reduced to zero are removed.

    Phase 2 (add-back): attempt to restore removed edges, heaviest first,
    accepting each edge that does not create a new cycle (tested via topo
    rank O(1) fast path, then reachability with rank-interval pruning).

    Returns:
        removed_eids : set of edge IDs in the final FAS
        U, V, W0     : edge endpoint and weight arrays
        active       : bytearray indicating the final DAG
        adj          : adjacency lists
    """
    U, V, W0, W, active, adj = build_eid_graph(edges_indexed, n_nodes, tol=tol)
    removed_eids = set()

    # Phase 1: cycle reductions
    while True:
        cyc = find_any_cycle_eids(n_nodes, adj, U, V, active)
        if cyc is None:
            break

        eps = min(W[eid] for eid in cyc)

        if eps <= tol:
            eid0 = cyc[0]
            if active[eid0]:
                active[eid0] = 0
                W[eid0] = 0.0
                removed_eids.add(eid0)
            continue

        for eid in cyc:
            new_w = W[eid] - eps
            W[eid] = new_w
            if new_w <= tol and active[eid]:
                active[eid] = 0
                W[eid] = 0.0
                removed_eids.add(eid)

    # Phase 2: add-back (heavy first)
    removed_list = sorted(removed_eids, key=lambda eid: (-W0[eid], U[eid], V[eid]))
    _, rank = topo_order_active(n_nodes, adj, V, active)
    reachable = make_reachability_checker(n_nodes, adj, V, active)

    for eid in removed_list:
        u = U[eid]
        v = V[eid]

        if rank[u] < rank[v]:
            active[eid] = 1
            removed_eids.discard(eid)
            continue

        if not reachable(v, u, rank=rank, rank_limit=rank[u]):
            active[eid] = 1
            removed_eids.discard(eid)
            _, rank = topo_order_active(n_nodes, adj, V, active)

    return removed_eids, U, V, W0, active, adj


# ---------------------------------------------------------------------------
# End-to-end entry point
# ---------------------------------------------------------------------------

def paper_fas_ranking_from_dimacs_fast(dimacs_path, output_ranking_csv_path, tol=1e-12):
    """
    Run LR-TA on a DIMACS instance and write a ranking CSV.

    The CSV has columns: Node ID, Order.

    Returns:
        edges_indexed, node_to_index, index_to_node, scores, F_removed_pairs
    """
    import pandas as pd

    edges_indexed, node_to_index, index_to_node = read_graph_dimacs_agg(dimacs_path)
    n = len(node_to_index)

    removed_eids, U, V, W0, active, adj = local_ratio_fas_fast(edges_indexed, n, tol=tol)

    order, rank = topo_order_active(n, adj, V, active)

    rows = [{"Node ID": str(index_to_node[i]).strip(), "Order": int(rank[i])} for i in range(n)]
    rows.sort(key=lambda r: r["Order"])
    pd.DataFrame(rows).to_csv(output_ranking_csv_path, index=False)

    F_removed_pairs = {(U[eid], V[eid]) for eid in removed_eids}
    scores = {i: int(rank[i]) for i in range(n)}
    return edges_indexed, node_to_index, index_to_node, scores, F_removed_pairs
