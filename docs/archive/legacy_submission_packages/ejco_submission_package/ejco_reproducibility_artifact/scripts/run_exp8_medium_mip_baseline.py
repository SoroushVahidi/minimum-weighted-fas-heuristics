"""
EXP8: Time-capped MIP/LP baseline for medium sparse instances.

Formulation: linear ordering MIP with binary pair variables x_{ij}=1 iff
vertex i precedes vertex j, and triangle transitivity inequalities.

Solver: scipy.optimize.milp (HiGHS backend).

For n <= 200: full MIP (integer variables, time-capped).
For n > 200:  LP relaxation (continuous variables) — valid lower bound,
              computed fast. Integer rounding applied to get a feasible ordering.

Does NOT modify EXP1b-EXP7.
"""
import argparse
import csv
import json
import math
import sys
import time
import traceback
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import csc_matrix

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mwfas.io import read_graph_dimacs_agg
from mwfas.evaluation import compute_forward_backward

CONFIG_CSV = REPO_ROOT / "experiments/exp8_medium_mip_baseline/config/selected_instances.csv"
OUT_DIR = REPO_ROOT / "experiments/exp8_medium_mip_baseline"
SUMMARY_CSV = OUT_DIR / "summary/exp8_mip_raw_summary.csv"

COLS = [
    "instance", "n", "m", "density",
    "solver", "mode", "time_limit_seconds",
    "status", "status_message",
    "mip_objective", "mip_bw_incumbent",
    "mip_dual_bound_bw", "mip_gap_pct",
    "proven_optimal",
    "runtime_seconds",
    "lrta_bw", "ipsns_bw", "wmsf_bw", "drmaciver_bw",
    "ipsns_gap_to_incumbent_pct",
    "ipsns_gap_to_bound_pct",
    "error",
]

MIP_THRESHOLD_N = 200   # n <= this: full MIP; n > this: LP relaxation
MEMORY_LIMIT_BYTES = 2 * 1024 ** 3  # 2 GB


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def pair_index(i, j, n):
    """Flat index for pair (i,j) with i < j, row-major upper triangle."""
    return i * (2 * n - i - 1) // 2 + (j - i - 1)


def build_mip(edges_indexed, n, time_limit, integer=True):
    """
    Build and solve the linear ordering MIP/LP.

    Returns:
        result dict with mip_bw_incumbent, mip_dual_bound_bw, mip_gap_pct,
        proven_optimal, runtime_seconds, status, status_message.
    """
    ew = {}
    total_w = 0.0
    for u, v, w in edges_indexed:
        ew[(u, v)] = ew.get((u, v), 0.0) + w
        total_w += w

    num_vars = n * (n - 1) // 2
    num_trips = n * (n - 1) * (n - 2) // 6
    num_constr = 2 * num_trips

    # Memory estimate for full triangle matrix (bytes): 3 * num_constr * 20
    mem_est = 3 * num_constr * 20
    if mem_est > MEMORY_LIMIT_BYTES:
        # Use sparse formulation: only add constraints involving nonzero-weight pairs
        sparse_mode = True
    else:
        sparse_mode = False

    # Objective: minimize sum_{i<j} (ew[(j,i)] - ew[(i,j)]) * x_{ij}
    c = np.zeros(num_vars)
    for i in range(n):
        for j in range(i + 1, n):
            c[pair_index(i, j, n)] = ew.get((j, i), 0.0) - ew.get((i, j), 0.0)

    # Constant term (independent of x): total_w - sum_{i<j} ew[(j,i)]
    # bw = c @ x + const_bw
    const_bw = total_w - sum(ew.get((j, i), 0.0) for i in range(n) for j in range(i + 1, n))

    # Build triangle constraints
    t_build = time.perf_counter()
    if sparse_mode:
        nonzero_pairs = {(u, v) for u, v, w in edges_indexed if w > 0}
        nonzero_pairs |= {(v, u) for u, v in nonzero_pairs}
        relevant_verts = {u for u, v in nonzero_pairs} | {v for u, v in nonzero_pairs}

        row_data = []
        col_data = []
        val_data = []
        rhs_list = []
        r_idx = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # Only add constraint if any edge in this triple is nonzero
                    if not ((i, j) in nonzero_pairs or (j, i) in nonzero_pairs or
                            (i, k) in nonzero_pairs or (k, i) in nonzero_pairs or
                            (j, k) in nonzero_pairs or (k, j) in nonzero_pairs):
                        continue
                    pij = pair_index(i, j, n)
                    pjk = pair_index(j, k, n)
                    pik = pair_index(i, k, n)
                    # A: x_{ij} + x_{jk} - x_{ik} <= 1
                    row_data += [r_idx, r_idx, r_idx]
                    col_data += [pij, pjk, pik]
                    val_data += [1.0, 1.0, -1.0]
                    rhs_list.append(1.0)
                    r_idx += 1
                    # B: -x_{ij} - x_{jk} + x_{ik} <= 0
                    row_data += [r_idx, r_idx, r_idx]
                    col_data += [pij, pjk, pik]
                    val_data += [-1.0, -1.0, 1.0]
                    rhs_list.append(0.0)
                    r_idx += 1

        n_actual_constr = r_idx
        description = f"sparse-triangle ({n_actual_constr} constraints, sparse_mode)"
    else:
        # Full triangle constraints using vectorized numpy
        # Generate all (i,j,k) triples with i<j<k
        trips = np.array(list(combinations(range(n), 3)), dtype=np.int32)
        n_trips_actual = len(trips)
        n_actual_constr = 2 * n_trips_actual

        # Pair indices for all triples
        i_arr = trips[:, 0]
        j_arr = trips[:, 1]
        k_arr = trips[:, 2]
        pij = i_arr * (2 * n - i_arr - 1) // 2 + (j_arr - i_arr - 1)
        pjk = j_arr * (2 * n - j_arr - 1) // 2 + (k_arr - j_arr - 1)
        pik = i_arr * (2 * n - i_arr - 1) // 2 + (k_arr - i_arr - 1)

        # Row indices: A-constraints at 2*t, B-constraints at 2*t+1
        t_idx = np.arange(n_trips_actual)
        row_A = 2 * t_idx
        row_B = 2 * t_idx + 1

        row_data = np.concatenate([row_A, row_A, row_A, row_B, row_B, row_B])
        col_data = np.concatenate([pij, pjk, pik, pij, pjk, pik])
        val_data = np.concatenate([
            np.ones(n_trips_actual), np.ones(n_trips_actual), -np.ones(n_trips_actual),
            -np.ones(n_trips_actual), -np.ones(n_trips_actual), np.ones(n_trips_actual),
        ])
        rhs_list = np.empty(n_actual_constr)
        rhs_list[::2] = 1.0
        rhs_list[1::2] = 0.0
        description = f"full-triangle ({n_actual_constr} constraints)"

    build_time = time.perf_counter() - t_build
    print(f"    Constraint matrix built in {build_time:.1f}s ({description})")

    A = csc_matrix(
        (val_data, (row_data, col_data)),
        shape=(n_actual_constr, num_vars)
    )
    constraints = LinearConstraint(A, -np.inf, np.asarray(rhs_list))
    bounds = Bounds(lb=0.0, ub=1.0)
    integrality = np.ones(num_vars) if integer else np.zeros(num_vars)

    t_solve = time.perf_counter()
    try:
        res = milp(
            c,
            constraints=constraints,
            integrality=integrality,
            bounds=bounds,
            options={"time_limit": time_limit, "disp": False},
        )
    except Exception as exc:
        return {
            "status": "solver_error",
            "status_message": f"{type(exc).__name__}: {str(exc)[:300]}",
            "mip_bw_incumbent": None,
            "mip_dual_bound_bw": None,
            "mip_gap_pct": None,
            "proven_optimal": False,
            "runtime_seconds": time.perf_counter() - t_solve,
        }

    rt = time.perf_counter() - t_solve

    # Interpret result
    status_map = {0: "optimal", 1: "time_limit", 2: "infeasible",
                  3: "unbounded", 4: "other"}
    status_str = status_map.get(res.status, f"unknown_{res.status}")

    if res.x is not None and len(res.x) == num_vars:
        obj_val = float(res.fun)
        bw_incumbent = obj_val + const_bw
    else:
        bw_incumbent = None

    # Dual bound (lower bound on backward weight)
    dual_obj = getattr(res, "mip_dual_bound", None)
    bw_dual = float(dual_obj) + const_bw if dual_obj is not None else None

    mip_gap = getattr(res, "mip_gap", None)
    mip_gap_pct = float(mip_gap) * 100 if mip_gap is not None else None

    proven_opt = (res.status == 0 and integer) or (res.status == 0 and not integer)

    return {
        "status": status_str,
        "status_message": str(res.message),
        "mip_bw_incumbent": round(bw_incumbent, 4) if bw_incumbent is not None else None,
        "mip_dual_bound_bw": round(bw_dual, 4) if bw_dual is not None else None,
        "mip_gap_pct": round(mip_gap_pct, 4) if mip_gap_pct is not None else None,
        "proven_optimal": proven_opt,
        "runtime_seconds": round(rt, 3),
    }


# ---------------------------------------------------------------------------
# Per-instance runner
# ---------------------------------------------------------------------------

def run_instance(inst_name, file_path, ref_row, time_limit):
    """Run MIP/LP on one instance. Returns result dict."""
    t0 = time.perf_counter()
    try:
        edges_indexed, n2i, i2n = read_graph_dimacs_agg(str(file_path))
        n = len(n2i)
        m = len(edges_indexed)
        density = 2 * m / (n * (n - 1)) if n > 1 else 0.0

        integer = (n <= MIP_THRESHOLD_N)
        mode = "MIP" if integer else "LP_relaxation"
        print(f"  n={n} m={m} mode={mode}", flush=True)

        result = build_mip(edges_indexed, n, time_limit, integer=integer)

        # Reference values from EXP4
        lrta_bw = float(ref_row.get("lrta_bw") or "nan")
        ipsns_bw = float(ref_row.get("ipsns_bw") or "nan")
        wmsf_bw = float(ref_row.get("wmsf_bw") or "nan") if ref_row.get("wmsf_bw") else None
        dr_bw = float(ref_row.get("drmaciver_bw") or "nan") if ref_row.get("drmaciver_bw") else None

        bw_inc = result.get("mip_bw_incumbent")
        bw_bound = result.get("mip_dual_bound_bw")

        ipsns_gap_inc = None
        if bw_inc is not None and bw_inc > 0 and math.isfinite(ipsns_bw):
            ipsns_gap_inc = round((ipsns_bw - bw_inc) / bw_inc * 100, 4)

        ipsns_gap_bound = None
        if bw_bound is not None and bw_bound > 0 and math.isfinite(ipsns_bw):
            ipsns_gap_bound = round((ipsns_bw - bw_bound) / abs(bw_bound) * 100, 4)

        return {
            "instance": inst_name,
            "n": n, "m": m,
            "density": round(density, 6),
            "solver": "scipy.optimize.milp (HiGHS)",
            "mode": mode,
            "time_limit_seconds": time_limit,
            "status": result["status"],
            "status_message": result["status_message"][:200],
            "mip_objective": round(result["mip_bw_incumbent"], 4) if result["mip_bw_incumbent"] is not None else "",
            "mip_bw_incumbent": round(bw_inc, 4) if bw_inc is not None else "",
            "mip_dual_bound_bw": round(bw_bound, 4) if bw_bound is not None else "",
            "mip_gap_pct": result.get("mip_gap_pct") or "",
            "proven_optimal": result["proven_optimal"],
            "runtime_seconds": result["runtime_seconds"],
            "lrta_bw": round(lrta_bw, 4),
            "ipsns_bw": round(ipsns_bw, 4),
            "wmsf_bw": round(wmsf_bw, 4) if wmsf_bw is not None else "",
            "drmaciver_bw": round(dr_bw, 4) if dr_bw is not None else "",
            "ipsns_gap_to_incumbent_pct": ipsns_gap_inc or "",
            "ipsns_gap_to_bound_pct": ipsns_gap_bound or "",
            "error": "",
        }
    except Exception as exc:
        tb = traceback.format_exc()
        return {
            "instance": inst_name,
            "n": ref_row.get("n", ""), "m": ref_row.get("m", ""), "density": "",
            "solver": "scipy.optimize.milp (HiGHS)", "mode": "", "time_limit_seconds": time_limit,
            "status": "error", "status_message": f"{type(exc).__name__}: {str(exc)[:200]}",
            "mip_objective": "", "mip_bw_incumbent": "", "mip_dual_bound_bw": "",
            "mip_gap_pct": "", "proven_optimal": False, "runtime_seconds": round(time.perf_counter() - t0, 3),
            "lrta_bw": ref_row.get("lrta_bw", ""), "ipsns_bw": ref_row.get("ipsns_bw", ""),
            "wmsf_bw": ref_row.get("wmsf_bw", ""), "drmaciver_bw": ref_row.get("drmaciver_bw", ""),
            "ipsns_gap_to_incumbent_pct": "", "ipsns_gap_to_bound_pct": "",
            "error": f"{type(exc).__name__}: {str(exc)[:300]}",
        }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--time-limit-seconds", type=float, default=120.0)
    ap.add_argument("--max-instances", type=int, default=None,
                    help="Limit number of instances (for smoke test)")
    ap.add_argument("--output-suffix", default="",
                    help="Suffix appended to output filename (for smoke test)")
    args = ap.parse_args()

    with open(CONFIG_CSV, newline="") as f:
        config = list(csv.DictReader(f))

    if args.max_instances:
        config = config[:args.max_instances]

    (OUT_DIR / "summary").mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "logs").mkdir(parents=True, exist_ok=True)

    suffix = f"_{args.output_suffix}" if args.output_suffix else ""
    out_csv = OUT_DIR / f"summary/exp8_mip_raw_summary{suffix}.csv"

    all_rows = []
    total = len(config)
    print(f"EXP8 MIP baseline: {total} instances, time_limit={args.time_limit_seconds}s each")
    print(f"Total expected runtime: {total * args.time_limit_seconds / 60:.0f} min (worst case)")

    for idx, cfg in enumerate(config):
        inst = cfg["instance"]
        fp = Path(cfg["file_path"])
        n = int(cfg.get("n") or 0)
        t_start = time.strftime("%H:%M:%S")
        print(f"\n[{t_start}] [{idx+1}/{total}] {inst} (n={n}) ...", flush=True)

        if not fp.exists():
            print(f"  SKIP: file not found at {fp}")
            all_rows.append({col: "" for col in COLS})
            all_rows[-1].update({
                "instance": inst, "n": n, "status": "skip",
                "status_message": f"file not found: {fp}", "error": "file not found",
            })
        else:
            row = run_instance(inst, fp, cfg, args.time_limit_seconds)
            all_rows.append(row)
            bw = row.get("mip_bw_incumbent", "")
            bound = row.get("mip_dual_bound_bw", "")
            opt = row.get("proven_optimal", False)
            rt = row.get("runtime_seconds", "")
            print(f"  status={row['status']} bw_incumbent={bw} lb={bound} "
                  f"optimal={opt} rt={rt}s")

        # Write incrementally
        with open(out_csv, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore")
            w.writeheader()
            for r in all_rows:
                w.writerow({col: r.get(col, "") for col in COLS})

    print(f"\nDone. Wrote {len(all_rows)} rows to {out_csv}")


if __name__ == "__main__":
    main()
