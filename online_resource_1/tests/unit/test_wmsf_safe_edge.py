"""WMSF safe-edge propagation regression tests."""

from mwfas.wmsf import build_eid_graph_inout, wmsf_removeArcs_scc
from tests.helpers.assertions import assert_valid_fas


def test_safe_edge_closure_revisits_in_and_out_adjacency(tol):
    """
    Graph with external source edge into SCC: 0->1 is safe (indeg[0]=0), temporarily
    removed then restored. Wrong adjacency revisit would break acyclic completion.
    """
    n = 3
    edges = [(0, 1, 1.0), (1, 2, 1.0), (2, 1, 5.0)]
    U, V, W0, active, out_adj, in_adj = build_eid_graph_inout(edges, n, tol=tol)
    F, safe_tmp = wmsf_removeArcs_scc(n, U, V, W0, active, out_adj, in_adj, ordering="L2", tol=tol)
    for eid in F:
        active[eid] = 0
    for eid in safe_tmp:
        active[eid] = 1
    assert_valid_fas(n, U, V, W0, active, F, tol=tol)


def test_wrong_adjacency_would_fail_on_fork_graph(tol):
    """
    Fork: 0->1, 0->2, 1->3, 2->3, 3->0. Safe-edge propagation must enqueue both
  branches when head of heavy edge is removed.
    """
    n = 4
    edges = [(0, 1, 1.0), (0, 2, 1.0), (1, 3, 1.0), (2, 3, 1.0), (3, 0, 20.0)]
    U, V, W0, active, out_adj, in_adj = build_eid_graph_inout(edges, n, tol=tol)
    F, safe_tmp = wmsf_removeArcs_scc(n, U, V, W0, active, out_adj, in_adj, ordering="L2", tol=tol)
    for eid in F:
        active[eid] = 0
    for eid in safe_tmp:
        active[eid] = 1
    assert_valid_fas(n, U, V, W0, active, F, tol=tol)
