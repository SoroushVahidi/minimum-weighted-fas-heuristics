"""Unit tests for mwfas.evaluation."""

from mwfas.evaluation import compute_forward_backward

from tests.helpers.brute_force import reference_backward_weight, reference_forward_weight


def test_backward_matches_reference(tol):
    edges = [(0, 1, 3.0), (1, 2, 2.0), (2, 0, 1.0)]
    scores = {0: 0, 1: 1, 2: 2}
    total, fw, bw = compute_forward_backward(edges, scores)
    assert abs(total - 6.0) < tol
    assert abs(fw - reference_forward_weight(edges, scores)) < tol
    assert abs(bw - reference_backward_weight(edges, scores)) < tol
    assert abs(total - fw - bw) < tol


def test_dag_has_zero_backward(tol):
    edges = [(0, 1, 1.0), (1, 2, 4.0)]
    scores = {0: 0, 1: 1, 2: 2}
    _, fw, bw = compute_forward_backward(edges, scores)
    assert bw < tol
    assert abs(fw - 5.0) < tol


def test_equivalent_orderings_same_objective(tol):
    edges = [(0, 1, 1.0), (0, 2, 2.0)]
    s1 = {0: 0, 1: 1, 2: 2}
    s2 = {0: 0, 2: 1, 1: 2}
    _, _, bw1 = compute_forward_backward(edges, s1)
    _, _, bw2 = compute_forward_backward(edges, s2)
    assert abs(bw1 - bw2) < tol


def test_zero_weight_edges(tol):
    edges = [(0, 1, 0.0), (1, 0, 5.0)]
    scores = {0: 0, 1: 1}
    total, fw, bw = compute_forward_backward(edges, scores)
    assert abs(total - 5.0) < tol
    assert abs(bw - 5.0) < tol


def test_integer_weights(tol):
    edges = [(0, 1, 1), (1, 2, 2)]
    scores = {0: 2, 1: 0, 2: 1}
    _, _, bw = compute_forward_backward(edges, scores)
    assert abs(bw - 1.0) < tol
