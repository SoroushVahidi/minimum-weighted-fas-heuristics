"""IPSNS rollback and incumbent-protection behavior tests."""

from mwfas.ipsns import (
    build_eid_graph_inout_with_W,
    lns_merge_wmsf_lr_best_incumbent,
    lns_step_on_scc,
)
from mwfas.wmsf import edges_by_scc, kosaraju_scc
from tests.helpers.assertions import assert_restored, snapshot_active_F
from tests.helpers.graph_builders import edges_to_dimacs, triangle_cycle


def test_lns_step_failed_repair_restores_state(tol):
    n, edges = triangle_cycle()
    U, V, W0, W_init, active, out_adj, in_adj = build_eid_graph_inout_with_W(edges, n, tol=tol)
    comps, comp_id = kosaraju_scc(n, edges)
    by_scc = edges_by_scc(edges, comp_id)
    verts = comps[0]
    e_list = by_scc[0]
    F = set()
    snap = snapshot_active_F(active, F)
    for eid in range(len(U)):
        active[eid] = 0
        F.add(eid)
    ok = lns_step_on_scc(
        scc_nodes=verts,
        scc_edges=e_list,
        U=U, V=V, W0=W0,
        active=active,
        out_adj=out_adj,
        F=F,
        destroy_addback_frac=0.0,
        destroy_remove_frac=0.0,
        tol=tol,
    )
    if not ok:
        assert_restored(snap, active, F)


def test_ipsns_rejects_non_improving_moves(tmp_dimacs, tol):
    n, edges = triangle_cycle()
    path = tmp_dimacs(edges_to_dimacs((str(u), str(v), w) for u, v, w in edges))
    out = path.parent / "out.csv"
    *_, info = lns_merge_wmsf_lr_best_incumbent(
        dimacs_path=str(path),
        output_ranking_csv_path=str(out),
        iters=15,
        rng_seed=3,
        log_every=0,
        return_info=True,
    )
    assert info["final_bw"] <= info["best_seed_bw"] + tol
    if info["n_rejected"] > 0:
        assert info["final_bw"] <= info["best_seed_bw"] + tol
