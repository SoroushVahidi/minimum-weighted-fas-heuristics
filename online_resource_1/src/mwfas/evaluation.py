"""Objective/evaluation functions for weighted FAS solutions."""


def compute_forward_backward(edges_indexed, scores):
    """
    Compute total, forward, and backward weight given a node ranking (scores).

    An edge (u, v, w) is forward if scores[u] < scores[v].

    Args:
        edges_indexed: list of (u, v, w)
        scores: dict mapping node index to rank

    Returns:
        (total_weight, forward_weight, backward_weight)
    """
    total_w = 0.0
    fw = 0.0
    for u, v, w in edges_indexed:
        total_w += w
        if scores[u] < scores[v]:
            fw += w
    bw = total_w - fw
    return total_w, fw, bw
