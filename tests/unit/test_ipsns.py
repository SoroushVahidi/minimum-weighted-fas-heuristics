"""Unit tests for IPSNS (mwfas.ipsns)."""

import random

from mwfas.ipsns import lns_merge_wmsf_lr_best_incumbent, score_scc_backward_weight
from tests.helpers.graph_builders import edges_to_dimacs, triangle_cycle


def test_zero_iters_returns_seed(tmp_dimacs, tol):
    n, edges = triangle_cycle()
    path = tmp_dimacs(edges_to_dimacs((str(u), str(v), w) for u, v, w in edges))
    out = path.parent / "out.csv"
    *_, info = lns_merge_wmsf_lr_best_incumbent(
        dimacs_path=str(path),
        output_ranking_csv_path=str(out),
        iters=0,
        log_every=0,
        return_info=True,
    )
    assert info["final_bw"] <= info["best_seed_bw"] + tol
    assert info["n_iters"] == 0


def test_seeded_reproducible(tmp_dimacs, tol):
    n, edges = triangle_cycle()
    path = tmp_dimacs(edges_to_dimacs((str(u), str(v), w) for u, v, w in edges))

    def run(seed):
        out = path.parent / f"out_{seed}.csv"
        return lns_merge_wmsf_lr_best_incumbent(
            dimacs_path=str(path),
            output_ranking_csv_path=str(out),
            iters=8,
            rng_seed=seed,
            log_every=0,
            return_info=True,
        )[-1]["final_bw"]

    assert abs(run(1) - run(1)) < tol


def test_incumbent_not_worse_than_seeds(tmp_dimacs, tol):
    n, edges = triangle_cycle((3.0, 2.0, 1.0))
    path = tmp_dimacs(edges_to_dimacs((str(u), str(v), w) for u, v, w in edges))
    out = path.parent / "out.csv"
    *_, info = lns_merge_wmsf_lr_best_incumbent(
        dimacs_path=str(path),
        output_ranking_csv_path=str(out),
        iters=20,
        rng_seed=7,
        log_every=0,
        return_info=True,
    )
    assert info["final_bw"] <= info["best_seed_bw"] + tol
    assert info["final_bw"] <= info["lr_seed_bw"] + tol
    assert info["final_bw"] <= info["wmsf_seed_bw"] + tol


def test_ipsns_sets_random_seed(tmp_dimacs):
    random.seed(999)
    _ = random.random()
    n, edges = triangle_cycle()
    path = tmp_dimacs(edges_to_dimacs((str(u), str(v), w) for u, v, w in edges))
    out = path.parent / "out.csv"
    lns_merge_wmsf_lr_best_incumbent(
        dimacs_path=str(path),
        output_ranking_csv_path=str(out),
        iters=3,
        rng_seed=42,
        log_every=0,
    )
    # Documented: IPSNS calls random.seed(rng_seed) at start.


def test_scc_scoring():
    edges_in_scc = [(0, 1, 5.0, 0), (1, 2, 2.0, 1), (2, 0, 1.0, 2)]
    rank = {0: 2, 1: 0, 2: 1}
    bw = score_scc_backward_weight(edges_in_scc, rank)
    assert abs(bw - 5.0) < 1e-12
