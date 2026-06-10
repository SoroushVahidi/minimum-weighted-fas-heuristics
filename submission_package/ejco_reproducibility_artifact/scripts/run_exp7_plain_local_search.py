"""
EXP7: Plain Local Search Comparator.

Runs generic order-local improvement heuristics (adjacent-swap LS and
single-vertex insertion LS) from the LR-TA seed on the EXP6 selected
20-instance subset. Compares results against IPSNS from EXP4/EXP6.

Does NOT modify any EXP1b-EXP6 outputs or algorithm code.
"""
import argparse
import csv
import sys
import time
import traceback
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mwfas.io import read_graph_dimacs_agg
from mwfas.evaluation import compute_forward_backward
from mwfas.lrta import local_ratio_fas_fast, topo_order_active
from mwfas.wmsf import (
    build_eid_graph_inout, kosaraju_scc, edges_by_scc,
    _build_local_scc_graph, _wmsf_pipeline_scc,
)

CONFIG_CSV = REPO_ROOT / "experiments/exp7_plain_local_search/config/selected_instances.csv"
OUT_DIR = REPO_ROOT / "experiments/exp7_plain_local_search"
SUMMARY_PATH = OUT_DIR / "summary/exp7_raw_summary.csv"
LOG_PATH = OUT_DIR / "logs/exp7_tmux.log"

SUMMARY_COLS = [
    "instance", "method", "seed_method", "budget_label",
    "n", "m", "total_weight",
    "seed_bw", "backward_weight",
    "improvement_over_seed",
    "runtime_seconds", "seed_runtime_seconds", "ls_runtime_seconds",
    "accepted_moves", "passes_completed", "stopped_reason",
    "status", "error",
]

MAX_PASSES_ADJ = 20       # adjacent-swap: max passes before stopping
MAX_MOVES_INS = 200       # insertion LS: max accepted moves
TIME_LIMIT_INS = 60.0     # insertion LS: seconds per instance


# ---------------------------------------------------------------------------
# LR-TA seed (no CSV output needed)
# ---------------------------------------------------------------------------

def get_lrta_scores(edges_indexed, n):
    """Run LR-TA and return (scores, order_list) without writing a CSV."""
    removed_eids, U, V, W0, active, adj = local_ratio_fas_fast(
        edges_indexed, n, tol=1e-12, add_back=True
    )
    order_list, rank = topo_order_active(n, adj, V, active)
    scores = {i: int(rank[i]) for i in range(n)}
    return scores, order_list


# ---------------------------------------------------------------------------
# WMSF seed (no CSV output needed)
# ---------------------------------------------------------------------------

def get_wmsf_scores(edges_indexed, n):
    """Run WMSF and return scores without writing a CSV."""
    from mwfas.lrta import topo_order_active as _topo

    comps, comp_id = kosaraju_scc(n, edges_indexed)
    by_scc = edges_by_scc(edges_indexed, comp_id)
    U, V, W0, active_glob0, out_adj_glob, in_adj_glob = build_eid_graph_inout(
        edges_indexed, n, tol=1e-12
    )

    best_bw = float("inf")
    best_scores = None

    for ordering_choice in ("L1", "L2"):
        active_glob = bytearray(active_glob0)
        F_global = set()

        for scc_idx, verts in enumerate(comps):
            e_list = by_scc.get(scc_idx, [])
            if len(verts) <= 1:
                for (u, v, w, eid) in e_list:
                    if u == v and w > 1e-12:
                        F_global.add(eid)
                        active_glob[eid] = 0
                continue
            if not e_list:
                continue
            k, U2, V2, W02, eidG, active2, out2, in2 = _build_local_scc_graph(
                verts, e_list, tol=1e-12
            )
            F2, _ = _wmsf_pipeline_scc(
                k, U2, V2, W02, active2, out2, in2, ordering=ordering_choice, tol=1e-12
            )
            for eid2 in F2:
                eg = eidG[eid2]
                F_global.add(eg)
                active_glob[eg] = 0

        _, rank = _topo(n, out_adj_glob, V, active_glob)
        scores = {i: int(rank[i]) for i in range(n)}
        _, _, bw = compute_forward_backward(edges_indexed, scores)
        if bw < best_bw:
            best_bw = bw
            best_scores = scores

    return best_scores or {}


# ---------------------------------------------------------------------------
# Edge weight lookup
# ---------------------------------------------------------------------------

def build_ew(edges_indexed):
    """Build {(u,v): w} dict for O(1) edge weight lookup."""
    ew = {}
    for u, v, w in edges_indexed:
        ew[(u, v)] = w
    return ew


def scores_to_order(scores, n):
    """Convert {node: rank} to a list ordered by rank."""
    order = sorted(range(n), key=lambda x: scores.get(x, 0))
    return order


# ---------------------------------------------------------------------------
# Adjacent-swap local search
# ---------------------------------------------------------------------------

def adjacent_swap_ls(order, ew, max_passes=MAX_PASSES_ADJ):
    """
    Best-improvement adjacent-swap LS.

    In each pass, scan all adjacent pairs and accept every swap that strictly
    decreases backward weight (greedy scan with immediate application).
    Stop when a full pass finds no improvement or max_passes is reached.

    Returns (final_order, accepted_moves, passes_completed, stopped_reason).
    """
    order = list(order)
    n = len(order)
    accepted = 0
    stopped_reason = "local_optimum"

    for pass_num in range(1, max_passes + 1):
        improved_this_pass = False
        for i in range(n - 1):
            a = order[i]
            b = order[i + 1]
            # delta = new BW contribution of this pair - old BW contribution
            # Before: a→b forward, b→a backward  →  contribution = ew.get((b,a),0)
            # After:  b→a forward, a→b backward  →  contribution = ew.get((a,b),0)
            delta = ew.get((a, b), 0.0) - ew.get((b, a), 0.0)
            if delta < 0.0:
                order[i], order[i + 1] = order[i + 1], order[i]
                accepted += 1
                improved_this_pass = True

        if not improved_this_pass:
            return order, accepted, pass_num, "local_optimum"

    return order, accepted, max_passes, "max_passes"


# ---------------------------------------------------------------------------
# Single-vertex insertion local search
# ---------------------------------------------------------------------------

def insertion_ls(order, ew, max_moves=MAX_MOVES_INS, time_limit=TIME_LIMIT_INS):
    """
    Best-improvement single-vertex insertion LS.

    For each vertex in the current ordering, find the globally best position
    (maximum BW decrease) and apply the move if it is improving.
    Repeat passes until no improving move exists, the move budget is exhausted,
    or the time limit is reached.

    Returns (final_order, accepted_moves, passes_completed, stopped_reason).
    """
    order = list(order)
    n = len(order)
    accepted = 0
    passes = 0
    t0 = time.perf_counter()
    stopped_reason = "local_optimum"

    improved = True
    while improved:
        if time.perf_counter() - t0 >= time_limit:
            stopped_reason = "time_limit"
            break
        if accepted >= max_moves:
            stopped_reason = "max_moves"
            break

        improved = False
        passes += 1

        i = 0
        while i < n:
            if time.perf_counter() - t0 >= time_limit:
                stopped_reason = "time_limit"
                improved = False
                break
            if accepted >= max_moves:
                stopped_reason = "max_moves"
                improved = False
                break

            vi = i
            v = order[vi]
            best_delta = 0.0
            best_j = vi

            # Try moving v to the right (to position j > vi)
            # Node at original position j goes from "after v" to "before v"
            cumul = 0.0
            for j in range(vi + 1, n):
                u = order[j]
                cumul += ew.get((v, u), 0.0) - ew.get((u, v), 0.0)
                if cumul < best_delta:
                    best_delta = cumul
                    best_j = j

            # Try moving v to the left (to position j < vi)
            # Node at original position j goes from "before v" to "after v"
            cumul = 0.0
            for j in range(vi - 1, -1, -1):
                u = order[j]
                cumul += ew.get((u, v), 0.0) - ew.get((v, u), 0.0)
                if cumul < best_delta:
                    best_delta = cumul
                    best_j = j

            if best_delta < 0.0 and best_j != vi:
                order.pop(vi)
                order.insert(best_j, v)
                accepted += 1
                improved = True
                # After the move, re-scan from same position index
                # (the element at vi has changed)
                # Don't advance i: reprocess position vi with new element
            else:
                i += 1

    return order, accepted, passes, stopped_reason


# ---------------------------------------------------------------------------
# Per-instance runner
# ---------------------------------------------------------------------------

def run_instance(inst_path, inst_name):
    """Run all EXP7 methods on one instance. Returns list of result dicts."""
    results = []

    edges_indexed, node_to_index, index_to_node = read_graph_dimacs_agg(str(inst_path))
    n = len(node_to_index)
    m = len(edges_indexed)
    total_w, _, _ = compute_forward_backward(edges_indexed, {i: 0 for i in range(n)})
    total_w = sum(w for _, _, w in edges_indexed)

    ew = build_ew(edges_indexed)

    # ── LR-TA seed ──
    t_seed = time.perf_counter()
    lrta_scores, lrta_order = get_lrta_scores(edges_indexed, n)
    lrta_seed_rt = time.perf_counter() - t_seed
    _, _, lrta_bw = compute_forward_backward(edges_indexed, lrta_scores)

    # ── Method A: adjacent-swap LS from LR-TA ──
    t_ls = time.perf_counter()
    adj_order, adj_moves, adj_passes, adj_reason = adjacent_swap_ls(
        lrta_order, ew, max_passes=MAX_PASSES_ADJ
    )
    ls_rt_A = time.perf_counter() - t_ls
    adj_scores = {adj_order[i]: i for i in range(n)}
    _, _, adj_bw = compute_forward_backward(edges_indexed, adj_scores)

    results.append({
        "instance": inst_name,
        "method": "lrta_adj_swap_ls",
        "seed_method": "lrta",
        "budget_label": f"max_passes={MAX_PASSES_ADJ}",
        "n": n, "m": m, "total_weight": round(total_w, 4),
        "seed_bw": round(lrta_bw, 4),
        "backward_weight": round(adj_bw, 4),
        "improvement_over_seed": round(lrta_bw - adj_bw, 4),
        "runtime_seconds": round(lrta_seed_rt + ls_rt_A, 6),
        "seed_runtime_seconds": round(lrta_seed_rt, 6),
        "ls_runtime_seconds": round(ls_rt_A, 6),
        "accepted_moves": adj_moves,
        "passes_completed": adj_passes,
        "stopped_reason": adj_reason,
        "status": "ok", "error": "",
    })

    # ── Method B: insertion LS from LR-TA ──
    t_ls = time.perf_counter()
    ins_order, ins_moves, ins_passes, ins_reason = insertion_ls(
        lrta_order, ew, max_moves=MAX_MOVES_INS, time_limit=TIME_LIMIT_INS
    )
    ls_rt_B = time.perf_counter() - t_ls
    ins_scores = {ins_order[i]: i for i in range(n)}
    _, _, ins_bw = compute_forward_backward(edges_indexed, ins_scores)

    results.append({
        "instance": inst_name,
        "method": "lrta_insert_ls",
        "seed_method": "lrta",
        "budget_label": f"max_moves={MAX_MOVES_INS};time={TIME_LIMIT_INS}s",
        "n": n, "m": m, "total_weight": round(total_w, 4),
        "seed_bw": round(lrta_bw, 4),
        "backward_weight": round(ins_bw, 4),
        "improvement_over_seed": round(lrta_bw - ins_bw, 4),
        "runtime_seconds": round(lrta_seed_rt + ls_rt_B, 6),
        "seed_runtime_seconds": round(lrta_seed_rt, 6),
        "ls_runtime_seconds": round(ls_rt_B, 6),
        "accepted_moves": ins_moves,
        "passes_completed": ins_passes,
        "stopped_reason": ins_reason,
        "status": "ok", "error": "",
    })

    # ── Method C: insertion LS from best(LR-TA, WMSF) ──
    t_wmsf = time.perf_counter()
    try:
        wmsf_scores = get_wmsf_scores(edges_indexed, n)
        wmsf_rt = time.perf_counter() - t_wmsf
        _, _, wmsf_bw = compute_forward_backward(edges_indexed, wmsf_scores)
    except Exception as exc:
        wmsf_rt = time.perf_counter() - t_wmsf
        wmsf_scores = lrta_scores
        wmsf_bw = lrta_bw
        print(f"  WMSF failed ({exc}); falling back to LR-TA seed for method C")

    if wmsf_bw <= lrta_bw:
        best_scores = wmsf_scores
        best_bw = wmsf_bw
        best_seed_name = "wmsf"
        best_seed_rt = wmsf_rt
    else:
        best_scores = lrta_scores
        best_bw = lrta_bw
        best_seed_name = "lrta"
        best_seed_rt = lrta_seed_rt

    best_order = scores_to_order(best_scores, n)
    t_ls = time.perf_counter()
    bsins_order, bsins_moves, bsins_passes, bsins_reason = insertion_ls(
        best_order, ew, max_moves=MAX_MOVES_INS, time_limit=TIME_LIMIT_INS
    )
    ls_rt_C = time.perf_counter() - t_ls
    bsins_scores = {bsins_order[i]: i for i in range(n)}
    _, _, bsins_bw = compute_forward_backward(edges_indexed, bsins_scores)

    results.append({
        "instance": inst_name,
        "method": "bestseed_insert_ls",
        "seed_method": best_seed_name,
        "budget_label": f"max_moves={MAX_MOVES_INS};time={TIME_LIMIT_INS}s",
        "n": n, "m": m, "total_weight": round(total_w, 4),
        "seed_bw": round(best_bw, 4),
        "backward_weight": round(bsins_bw, 4),
        "improvement_over_seed": round(best_bw - bsins_bw, 4),
        "runtime_seconds": round(best_seed_rt + ls_rt_C, 6),
        "seed_runtime_seconds": round(best_seed_rt, 6),
        "ls_runtime_seconds": round(ls_rt_C, 6),
        "accepted_moves": bsins_moves,
        "passes_completed": bsins_passes,
        "stopped_reason": bsins_reason,
        "status": "ok", "error": "",
    })

    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true",
                    help="Smoke test: run only first --max-instances instances")
    ap.add_argument("--max-instances", type=int, default=2)
    args = ap.parse_args()

    with open(CONFIG_CSV, newline="") as f:
        config = list(csv.DictReader(f))

    if args.smoke:
        config = config[:args.max_instances]
        print(f"[SMOKE] Running {len(config)} instances")

    (OUT_DIR / "summary").mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "logs").mkdir(parents=True, exist_ok=True)

    all_rows = []
    total = len(config)

    for idx, cfg in enumerate(config):
        inst = cfg["instance"]
        inst_path = Path(cfg["file_path"])
        if not inst_path.exists():
            print(f"[SKIP] {inst}: file not found at {inst_path}")
            all_rows.append({
                "instance": inst, "method": "ALL", "seed_method": "",
                "budget_label": "", "n": "", "m": "", "total_weight": "",
                "seed_bw": "", "backward_weight": "",
                "improvement_over_seed": "",
                "runtime_seconds": 0, "seed_runtime_seconds": 0, "ls_runtime_seconds": 0,
                "accepted_moves": 0, "passes_completed": 0,
                "stopped_reason": "file_not_found", "status": "skip", "error": "",
            })
            continue

        print(f"[{idx+1}/{total}] {inst} (n={cfg.get('n','?')}) ...", flush=True)
        try:
            rows = run_instance(inst_path, inst)
            for r in rows:
                rt = r["ls_runtime_seconds"]
                print(f"  {r['method']}: bw={r['backward_weight']} "
                      f"improve={r['improvement_over_seed']} "
                      f"moves={r['accepted_moves']} "
                      f"reason={r['stopped_reason']} "
                      f"ls_rt={rt:.2f}s")
            all_rows.extend(rows)
        except Exception as exc:
            tb = traceback.format_exc()
            print(f"  ERROR: {exc}")
            for method in ("lrta_adj_swap_ls", "lrta_insert_ls", "bestseed_insert_ls"):
                all_rows.append({
                    "instance": inst, "method": method, "seed_method": "",
                    "budget_label": "", "n": cfg.get("n", ""), "m": "", "total_weight": "",
                    "seed_bw": "", "backward_weight": "",
                    "improvement_over_seed": "",
                    "runtime_seconds": 0, "seed_runtime_seconds": 0, "ls_runtime_seconds": 0,
                    "accepted_moves": 0, "passes_completed": 0,
                    "stopped_reason": "error", "status": "error",
                    "error": f"{type(exc).__name__}: {str(exc)[:300]}",
                })

        # Write incrementally
        with open(SUMMARY_PATH, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=SUMMARY_COLS, extrasaction="ignore")
            w.writeheader()
            w.writerows(all_rows)

    print(f"\nDone. Wrote {len(all_rows)} rows to {SUMMARY_PATH}")


if __name__ == "__main__":
    main()
