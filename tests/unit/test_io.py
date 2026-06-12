"""Unit tests for mwfas.io."""

from pathlib import Path

import pytest

from mwfas.io import read_graph_dimacs_agg


def test_aggregates_parallel_edges(tmp_dimacs, tol):
    path = tmp_dimacs(
        [
            "c parallel",
            "a 1 2 1.5",
            "a 1 2 2.5",
            "a 2 1 0.5",
        ]
    )
    edges, n2i, i2n = read_graph_dimacs_agg(path)
    assert len(n2i) == 2
    assert len(edges) == 2
    w12 = next(w for u, v, w in edges if n2i["1"] == u and n2i["2"] == v)
    assert abs(w12 - 4.0) < tol


def test_skips_comments_and_blank_lines(tmp_dimacs):
    path = tmp_dimacs(["", "c header", "p sp 3 2", "a 0 1 1"])
    edges, n2i, _ = read_graph_dimacs_agg(path)
    assert len(edges) == 1
    assert "0" in n2i and "1" in n2i


def test_noncontiguous_vertex_ids(tmp_dimacs):
    path = tmp_dimacs(["a 10 20 3", "a 20 30 1"])
    edges, n2i, i2n = read_graph_dimacs_agg(path)
    assert len(n2i) == 3
    assert edges[0][0] < edges[0][1]


def test_scientific_notation(tmp_dimacs, tol):
    path = tmp_dimacs(["a 1 2 1e-3"])
    edges, _, _ = read_graph_dimacs_agg(path)
    assert abs(edges[0][2] - 1e-3) < tol


def test_malformed_rows_skipped(tmp_dimacs):
    path = tmp_dimacs(["a 1 2", "a x y z", "a 1 2 1"])
    edges, n2i, _ = read_graph_dimacs_agg(path)
    assert len(edges) == 1


def test_negative_weights_currently_accepted(tmp_dimacs):
    """Contract: parser aggregates negative weights; benchmark excludes them downstream."""
    path = tmp_dimacs(["a 1 2 -1"])
    edges, _, _ = read_graph_dimacs_agg(path)
    assert edges[0][2] == -1.0


def test_empty_file(tmp_dimacs):
    path = tmp_dimacs([])
    edges, n2i, i2n = read_graph_dimacs_agg(path)
    assert edges == []
    assert n2i == {}
    assert i2n == {}


def test_tiny_fixture_triangle(tiny_graphs_dir, tol):
    path = tiny_graphs_dir / "triangle.d"
    edges, n2i, _ = read_graph_dimacs_agg(path)
    assert len(n2i) == 3
    assert len(edges) == 3
    assert abs(sum(w for _, _, w in edges) - 6.0) < tol
