"""
Simple external-comparison baselines for minimum weighted FAS.

All functions return a metrics dict with keys:
  algorithm, backward_weight, forward_weight, forward_ratio,
  runtime, n_nodes, n_edges, total_weight, error

Ordering CSVs have columns: Node ID, Order (0 = first/leftmost).
"""

import time
import random as _random

from .io import read_graph_dimacs_agg
from .evaluation import compute_forward_backward


def _write_ranking_csv(index_to_node, order, output_path):
    import pandas as pd
    rows = [
        {"Node ID": str(index_to_node[v]).strip(), "Order": r}
        for r, v in enumerate(order)
    ]
    pd.DataFrame(rows).to_csv(output_path, index=False)


def _metrics(algorithm, edges_indexed, scores, n, t0, error=None):
    if error:
        return {
            "algorithm": algorithm,
            "backward_weight": None,
            "forward_weight": None,
            "forward_ratio": None,
            "runtime": time.time() - t0,
            "n_nodes": n,
            "n_edges": len(edges_indexed),
            "total_weight": sum(w for _, _, w in edges_indexed),
            "error": error,
        }
    total_w, fw, bw = compute_forward_backward(edges_indexed, scores)
    return {
        "algorithm": algorithm,
        "backward_weight": bw,
        "forward_weight": fw,
        "forward_ratio": fw / total_w if total_w > 0 else 1.0,
        "runtime": time.time() - t0,
        "n_nodes": n,
        "n_edges": len(edges_indexed),
        "total_weight": total_w,
        "error": None,
    }


def order_by_borda_net_score_from_dimacs(input_path, output_path=None):
    """
    Rank vertices by weighted out-degree minus weighted in-degree (descending).

    Tie-break: ascending node index (deterministic).
    This is the simplest sensible ordering heuristic for weighted FAS.
    """
    t0 = time.time()
    edges_indexed, node_to_index, index_to_node = read_graph_dimacs_agg(input_path)
    n = len(node_to_index)

    out_w = [0.0] * n
    in_w = [0.0] * n
    for u, v, w in edges_indexed:
        out_w[u] += w
        in_w[v] += w

    order = sorted(range(n), key=lambda v: (-(out_w[v] - in_w[v]), v))
    scores = {v: r for r, v in enumerate(order)}

    if output_path:
        _write_ranking_csv(index_to_node, order, output_path)

    return edges_indexed, node_to_index, index_to_node, \
        scores, _metrics("borda_net_score", edges_indexed, scores, n, t0)


def weighted_eades_ordering_from_dimacs(input_path, output_path=None):
    """
    Weighted Eades–Lin–Smyth greedy ordering.

    Based on: P. Eades, X. Lin, W. F. Smyth, "A fast and effective heuristic for
    the feedback arc set problem," Info. Proc. Letters 47(6), 1993.

    This is an in-repository weighted adaptation, NOT official author code.

    Algorithm:
      While vertices remain:
        1. Move all weighted-sources (total incoming weight = 0) to the LEFT.
        2. Move all weighted-sinks   (total outgoing weight = 0) to the RIGHT.
        3. Otherwise, pick vertex with maximum (out_weight - in_weight); move LEFT.
           Ties broken by ascending node index.

    Assumes non-negative edge weights. Returns an error dict if negative weights found.
    """
    t0 = time.time()
    edges_indexed, node_to_index, index_to_node = read_graph_dimacs_agg(input_path)
    n = len(node_to_index)

    if any(w < 0 for _, _, w in edges_indexed):
        m = _metrics("weighted_eades", edges_indexed, {}, n, t0,
                     error="negative_weights_detected")
        return edges_indexed, node_to_index, index_to_node, {}, m

    # Build mutable adjacency: in_w[v], out_w[v], and per-edge structures
    in_w = [0.0] * n
    out_w = [0.0] * n
    # Adjacency: successors[u] = {v: w}, predecessors[v] = {u: w}
    succ = [dict() for _ in range(n)]
    pred = [dict() for _ in range(n)]
    for u, v, w in edges_indexed:
        if v in succ[u]:
            succ[u][v] += w
        else:
            succ[u][v] = w
        if u in pred[v]:
            pred[v][u] += w
        else:
            pred[v][u] = w
        out_w[u] += w
        in_w[v] += w

    remaining = set(range(n))
    left = []
    right = []

    def remove_vertex(v):
        remaining.discard(v)
        for nb, w in list(succ[v].items()):
            if nb in remaining:
                in_w[nb] -= w
                del pred[nb][v]
        for nb, w in list(pred[v].items()):
            if nb in remaining:
                out_w[nb] -= w
                del succ[nb][v]
        succ[v].clear()
        pred[v].clear()

    while remaining:
        # Drain sources (zero incoming weight)
        found = True
        while found:
            found = False
            sources = sorted(v for v in remaining if in_w[v] <= 1e-12)
            if sources:
                for v in sources:
                    left.append(v)
                    remove_vertex(v)
                found = True

        # Drain sinks (zero outgoing weight)
        found = True
        while found:
            found = False
            sinks = sorted(v for v in remaining if out_w[v] <= 1e-12)
            if sinks:
                for v in sinks:
                    right.append(v)
                    remove_vertex(v)
                found = True

        if not remaining:
            break

        # Pick max net-score vertex
        v = min(remaining, key=lambda u: (-(out_w[u] - in_w[u]), u))
        left.append(v)
        remove_vertex(v)

    # right was built in removal order → these should be placed rightmost
    order = left + list(reversed(right))
    scores = {v: r for r, v in enumerate(order)}

    if output_path:
        _write_ranking_csv(index_to_node, order, output_path)

    return edges_indexed, node_to_index, index_to_node, \
        scores, _metrics("weighted_eades", edges_indexed, scores, n, t0)


def random_multistart_ordering_from_dimacs(
    input_path, output_path=None, trials=100, seed=1
):
    """
    Best of `trials` uniformly random permutations, by minimum backward weight.

    Fully deterministic given the same seed and trial count.
    This is a random lower-bound reference, not a serious heuristic.
    """
    t0 = time.time()
    edges_indexed, node_to_index, index_to_node = read_graph_dimacs_agg(input_path)
    n = len(node_to_index)

    rng = _random.Random(seed)
    best_bw = float("inf")
    best_order = list(range(n))

    vertices = list(range(n))
    for _ in range(trials):
        rng.shuffle(vertices)
        scores = {v: r for r, v in enumerate(vertices)}
        _, _, bw = compute_forward_backward(edges_indexed, scores)
        if bw < best_bw:
            best_bw = bw
            best_order = list(vertices)

    scores = {v: r for r, v in enumerate(best_order)}

    if output_path:
        _write_ranking_csv(index_to_node, best_order, output_path)

    return edges_indexed, node_to_index, index_to_node, \
        scores, _metrics("random_multistart", edges_indexed, scores, n, t0)
