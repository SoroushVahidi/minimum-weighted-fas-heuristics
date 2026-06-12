"""
Exact minimum weighted FAS solver via bitmask DP.

Works on small graphs (n <= 20). Finds the vertex ordering that minimises the
total backward-edge weight, equivalent to minimising the FAS weight.

Algorithm (O(n * 2^n) time after O(n^2 * 2^n) precomputation of incoming sums,
or O(3^n) for the naive version — both fast enough for n <= 20):

  dp[S] = maximum total forward weight achievable with vertices in S arranged
          in some order among themselves.

  Transition: dp[S] = max over v in S of  dp[S minus v] + inc(v, S minus v)
              where inc(v, T) = total weight of edges u->v for u in T.

  v is placed last in S; edges u->v for u in S minus v are forward.

  min FAS weight = total_weight - dp[(1<<n) - 1]
"""

from .io import read_graph_dimacs_agg
from .evaluation import compute_forward_backward


def exact_min_fas_dp(edges_indexed, n_nodes):
    """
    Compute the exact minimum weighted FAS weight via bitmask DP.

    Suitable for n_nodes <= 20 (practically instant for n <= 15).

    Args:
        edges_indexed : list of (u, v, w) with integer node indices 0..n-1
        n_nodes       : number of nodes

    Returns:
        min_fas_weight : float — minimum total backward weight
        max_fw_weight  : float — maximum total forward weight
        optimal_order  : list of node indices in the optimal ordering
                         (empty for n=0)
    """
    if n_nodes == 0:
        return 0.0, 0.0, []

    if n_nodes > 20:
        raise ValueError(
            f"n_nodes={n_nodes} exceeds the DP limit of 20. "
            "Use an ILP solver for larger instances."
        )

    # Build adjacency matrix (handles parallel arcs via read_graph_dimacs_agg)
    adj = [[0.0] * n_nodes for _ in range(n_nodes)]
    total_w = 0.0
    for u, v, w in edges_indexed:
        adj[u][v] += w
        total_w += w

    N = 1 << n_nodes
    dp = [-1.0] * N
    dp[0] = 0.0
    last = [-1] * N  # last vertex placed in ordering for state S

    # Iterate over all non-empty subsets S in order of increasing value
    # (which corresponds to increasing subset size when combined with the
    # transition, since T = S ^ low < S always)
    for S in range(1, N):
        tmp = S
        while tmp:
            low = tmp & (-tmp)
            v = low.bit_length() - 1
            T = S ^ low  # S without v (v is placed last in ordering of S)

            # Sum of incoming edge weights to v from all u in T
            incoming = 0.0
            t = T
            while t:
                lbit = t & (-t)
                u = lbit.bit_length() - 1
                incoming += adj[u][v]
                t ^= lbit

            val = dp[T] + incoming
            if val > dp[S]:
                dp[S] = val
                last[S] = v

            tmp ^= low

    full = N - 1
    max_fw = dp[full]
    min_fas_w = total_w - max_fw

    # Reconstruct optimal ordering (last → first, then reverse)
    optimal_order = []
    S = full
    while S > 0:
        v = last[S]
        if v < 0:
            break
        optimal_order.append(v)
        S ^= (1 << v)
    optimal_order.reverse()

    return min_fas_w, max_fw, optimal_order


def exact_min_fas_from_dimacs(dimacs_path, output_ranking_csv_path=None):
    """
    Run exact minimum weighted FAS DP on a DIMACS instance.

    Reads the graph, runs the bitmask DP, optionally writes a ranking CSV.

    Args:
        dimacs_path             : path to the DIMACS file
        output_ranking_csv_path : if given, write the optimal ranking CSV

    Returns:
        edges_indexed, node_to_index, index_to_node,
        min_fas_weight, max_fw_weight, optimal_scores
        where optimal_scores[i] = rank of node i in the optimal ordering
    """
    edges_indexed, node_to_index, index_to_node = read_graph_dimacs_agg(dimacs_path)
    n = len(node_to_index)

    if n == 0:
        if output_ranking_csv_path:
            import pandas as pd
            pd.DataFrame(columns=["Node ID", "Order"]).to_csv(
                output_ranking_csv_path, index=False
            )
        return edges_indexed, node_to_index, index_to_node, 0.0, 0.0, {}

    min_fas_w, max_fw, optimal_order = exact_min_fas_dp(edges_indexed, n)

    # Build scores dict: node_index → rank position
    optimal_scores = {optimal_order[r]: r for r in range(n)}

    if output_ranking_csv_path:
        import pandas as pd
        rows = [
            {"Node ID": str(index_to_node[i]).strip(), "Order": int(optimal_scores[i])}
            for i in range(n)
        ]
        rows.sort(key=lambda r: r["Order"])
        pd.DataFrame(rows).to_csv(output_ranking_csv_path, index=False)

    return edges_indexed, node_to_index, index_to_node, min_fas_w, max_fw, optimal_scores
