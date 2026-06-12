"""Tiny synthetic graph builders for tests."""

from __future__ import annotations

from typing import Iterable


def edges_to_dimacs(edges: Iterable[tuple[int | str, int | str, float]], header: str = "c test graph") -> list[str]:
    lines = [header, "p sp 0 0"]
    for u, v, w in edges:
        lines.append(f"a {u} {v} {w}")
    return lines


def triangle_cycle(weights=(3.0, 2.0, 1.0)):
    w01, w12, w20 = weights
    n = 3
    edges = [(0, 1, w01), (1, 2, w12), (2, 0, w20)]
    return n, edges


def two_cycle(w_forward=5.0, w_backward=2.0):
    n = 2
    edges = [(0, 1, w_forward), (1, 0, w_backward)]
    return n, edges


def dag_path(weights=(1.0, 2.0, 3.0)):
    n = 4
    edges = [(0, 1, weights[0]), (1, 2, weights[1]), (2, 3, weights[2])]
    return n, edges


def parallel_edges():
    n = 2
    edges = [(0, 1, 1.0), (0, 1, 2.0), (1, 0, 0.5)]
    return n, edges


def self_loop():
    n = 2
    edges = [(0, 0, 4.0), (0, 1, 1.0)]
    return n, edges


def zero_weight_cycle():
    n = 3
    edges = [(0, 1, 0.0), (1, 2, 1.0), (2, 0, 1.0)]
    return n, edges


def safe_edge_chain():
    """Graph where safe-edge propagation should discover a chain of safe arcs."""
    n = 4
    edges = [
        (0, 1, 1.0),
        (1, 2, 1.0),
        (2, 3, 1.0),
        (3, 0, 10.0),  # heavy back edge closes SCC
    ]
    return n, edges


def scores_from_order(order: list[int]) -> dict[int, int]:
    return {v: i for i, v in enumerate(order)}
