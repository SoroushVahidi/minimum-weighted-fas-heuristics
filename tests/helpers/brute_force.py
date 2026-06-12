"""Independent reference implementations for tests (not production code)."""

from __future__ import annotations

import itertools
import math


def brute_force_min_backward(edges_indexed, n_nodes: int) -> tuple[float, list[int]]:
    """Exact minimum backward weight by enumerating all permutations (tiny n only)."""
    if n_nodes == 0:
        return 0.0, []
    if n_nodes > 8:
        raise ValueError("brute_force_min_backward supports n <= 8 only")

    total_w = sum(w for _, _, w in edges_indexed)
    best_bw = math.inf
    best_order: list[int] = []

    for perm in itertools.permutations(range(n_nodes)):
        scores = {v: i for i, v in enumerate(perm)}
        bw = reference_backward_weight(edges_indexed, scores)
        if bw < best_bw - 1e-15:
            best_bw = bw
            best_order = list(perm)
    return best_bw, best_order


def reference_backward_weight(edges_indexed, scores: dict[int, int]) -> float:
    """Independent backward-weight definition."""
    total = 0.0
    backward = 0.0
    for u, v, w in edges_indexed:
        total += w
        if scores[u] >= scores[v]:
            backward += w
    return backward


def reference_forward_weight(edges_indexed, scores: dict[int, int]) -> float:
    fw = 0.0
    for u, v, w in edges_indexed:
        if scores[u] < scores[v]:
            fw += w
    return fw


def fas_weight_from_removed(edges_indexed, removed_pairs: set[tuple[int, int]], tol=1e-12) -> float:
    s = 0.0
    for u, v, w in edges_indexed:
        if (u, v) in removed_pairs and w > tol:
            s += w
    return s
