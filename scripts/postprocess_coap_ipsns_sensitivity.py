#!/usr/bin/env python3
"""Build canonical dataset and analysis summaries from COAP IPSNS sensitivity checkpoints."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mwfas.io import read_graph_dimacs_agg  # noqa: E402
from mwfas.wmsf import kosaraju_scc  # noqa: E402

EXP_ROOT = REPO_ROOT / "experiments/coap_ipsns_sensitivity"
PLAN_PATH = EXP_ROOT / "config/sensitivity_plan.yaml"
CKPT_DIR = EXP_ROOT / "checkpoints/runs"
OUT_DIR = EXP_ROOT / "summary"
CANONICAL_CSV = OUT_DIR / "canonical_runs.csv"
CANONICAL_JSON = OUT_DIR / "canonical_runs.json"
DATA_DICT = OUT_DIR / "canonical_data_dictionary.json"
HASHES = OUT_DIR / "canonical_hashes.json"
ANALYSIS_JSON = OUT_DIR / "analysis_summary.json"
EXP2_SUMMARY = REPO_ROOT / "experiments/exp2_ablation/tables/exp2_ablation_summary.csv"
EXP1B_SUMMARY = REPO_ROOT / "experiments/exp1b_core_benchmark_full_wmsf_seed/tables/exp1b_core_benchmark_paper_summary.csv"

TOL = 1e-9


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_checkpoints() -> list[dict[str, Any]]:
    rows = []
    for path in sorted(CKPT_DIR.glob("*.json")):
        if path.name.endswith(".FAILED.json"):
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("status") != "ok":
            raise ValueError(f"Invalid checkpoint: {path}")
        rows.append(data)
    return rows


def graph_features(file_path: str) -> dict[str, Any]:
    edges_indexed, node_to_index, _index_to_node = read_graph_dimacs_agg(file_path)
    n = len(node_to_index)
    m = len(edges_indexed)
    density = m / (n * (n - 1)) if n > 1 else 0.0
    comps, comp_id = kosaraju_scc(n, edges_indexed)
    nontrivial = [c for c in comps if len(c) > 1]
    n_scc = len(nontrivial)
    if n > 0:
        largest = max((len(c) for c in comps), default=0)
        largest_frac = largest / n
        nontrivial_nodes = sum(len(c) for c in nontrivial)
        nontrivial_frac = nontrivial_nodes / n
    else:
        largest_frac = 0.0
        nontrivial_frac = 0.0
    return {
        "n": n,
        "m": m,
        "density": round(density, 8),
        "scc_count_nontrivial": n_scc,
        "largest_scc_fraction": round(largest_frac, 8),
        "nontrivial_scc_node_fraction": round(nontrivial_frac, 8),
    }


def load_exp2_seed_bw() -> dict[str, float]:
    out: dict[str, float] = {}
    if not EXP2_SUMMARY.is_file():
        return out
    with open(EXP2_SUMMARY, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["variant"] == "best_seed_no_lns" and row["status"] == "ok":
                out[row["instance"]] = float(row["backward_weight"])
    return out


def load_exp2_ipsns400() -> dict[str, float]:
    out: dict[str, float] = {}
    with open(EXP2_SUMMARY, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["variant"] == "ipsns_full" and row["status"] == "ok":
                out[row["instance"]] = float(row["backward_weight"])
    return out


def config_id(row: dict[str, Any]) -> str:
    vp = row["varied_param"]
    if vp == "baseline":
        return "baseline_default"
    if vp == "iters":
        return f"iters_{row['iters']}"
    if vp == "topk_scc":
        return f"topk_{row['topk_scc']}"
    if vp == "destroy_addback_frac":
        return f"addback_{row['destroy_addback_frac']:.2g}"
    if vp == "destroy_remove_frac":
        return f"remove_{row['destroy_remove_frac']:.2g}"
    if vp == "rng_seed":
        return f"rng_{row['rng_seed']}"
    return vp


def build_canonical(rows: list[dict[str, Any]], seed_bw: dict[str, float]) -> list[dict[str, Any]]:
    graph_cache: dict[str, dict[str, Any]] = {}
    canonical: list[dict[str, Any]] = []

    baseline_bw = {
        r["instance"]: float(r["backward_weight"])
        for r in rows
        if r["varied_param"] == "baseline"
    }

    for r in rows:
        fp = r["file_path"]
        if fp not in graph_cache:
            graph_cache[fp] = graph_features(fp)

        inst = r["instance"]
        final_bw = float(r["backward_weight"])
        init_bw = seed_bw.get(inst)
        ref_bw = baseline_bw.get(inst, final_bw)

        abs_vs_seed = (init_bw - final_bw) if init_bw is not None else None
        norm_vs_seed = (abs_vs_seed / init_bw) if init_bw and init_bw > TOL else None
        abs_vs_baseline = ref_bw - final_bw
        norm_vs_baseline = abs_vs_baseline / ref_bw if ref_bw > TOL else 0.0

        row_out = {
            "run_key": r["run_key"],
            "instance": inst,
            "file_path": fp,
            **graph_cache[fp],
            "config_id": config_id(r),
            "varied_param": r["varied_param"],
            "iteration_budget": int(r["iters"]),
            "topk_scc": int(r["topk_scc"]),
            "destroy_addback_frac": float(r["destroy_addback_frac"]),
            "destroy_remove_frac": float(r["destroy_remove_frac"]),
            "tol": float(r["tol"]),
            "rng_seed": int(r["rng_seed"]),
            "wmsf_seed_mode": r["wmsf_seed_mode"],
            "seed_ordering": r["seed_ordering"],
            "scc_select_mode": r["scc_select_mode"],
            "initial_seed_method": "best(LR-TA,WMSF)_no_LNS",
            "initial_bw_best_seed": init_bw,
            "baseline_default_bw": ref_bw,
            "final_bw": final_bw,
            "abs_improvement_vs_best_seed": abs_vs_seed,
            "normalized_improvement_vs_best_seed": norm_vs_baseline if init_bw is None else (
                abs_vs_seed / init_bw if init_bw > TOL else 0.0
            ),
            "abs_improvement_vs_baseline_default": abs_vs_baseline,
            "normalized_improvement_vs_baseline_default": norm_vs_baseline,
            "accepted_moves": None,
            "attempted_moves": None,
            "first_improvement_iteration": None,
            "last_improvement_iteration": None,
            "runtime_sec": float(r["runtime"]),
            "quality_per_runtime": (
                (ref_bw - final_bw) / float(r["runtime"]) if float(r["runtime"]) > 0 else None
            ),
            "termination_reason": "not_logged_in_stage1_driver",
            "runtime_trace_available": False,
        }
        canonical.append(row_out)

    canonical.sort(key=lambda x: (x["instance"], x["config_id"]))
    return canonical


def compare_to_baseline(canonical: list[dict[str, Any]], varied: str) -> dict[str, Any]:
    baseline_by_inst = {
        r["instance"]: r for r in canonical if r["config_id"] == "baseline_default"
    }
    wins = ties = losses = 0
    deltas: list[float] = []
    runtime_ratios: list[float] = []
    per_value: dict[str, dict[str, Any]] = defaultdict(
        lambda: {"wins": 0, "ties": 0, "losses": 0, "deltas": []}
    )

    for row in canonical:
        if row["varied_param"] != varied:
            continue
        inst = row["instance"]
        base = baseline_by_inst[inst]
        d = float(row["final_bw"]) - float(base["final_bw"])
        deltas.append(d)
        bucket = per_value[row["config_id"]]
        bucket["deltas"].append(d)
        if d < -TOL:
            wins += 1
            bucket["wins"] += 1
        elif d > TOL:
            losses += 1
            bucket["losses"] += 1
        else:
            ties += 1
            bucket["ties"] += 1
        if base["runtime_sec"] > 0:
            runtime_ratios.append(row["runtime_sec"] / base["runtime_sec"])

    value_summary = {}
    for cid, b in sorted(per_value.items()):
        ds = b["deltas"]
        value_summary[cid] = {
            "wins": b["wins"],
            "ties": b["ties"],
            "losses": b["losses"],
            "mean_delta_bw": sum(ds) / len(ds) if ds else 0.0,
            "any_effect": any(abs(x) > TOL for x in ds),
        }

    return {
        "varied_param": varied,
        "n_comparisons": len(deltas),
        "wins_vs_baseline_lower_bw": wins,
        "ties": ties,
        "losses_vs_baseline_higher_bw": losses,
        "mean_delta_bw": sum(deltas) / len(deltas) if deltas else 0.0,
        "median_delta_bw": sorted(deltas)[len(deltas) // 2] if deltas else 0.0,
        "mean_runtime_ratio_vs_baseline": (
            sum(runtime_ratios) / len(runtime_ratios) if runtime_ratios else None
        ),
        "any_effect": any(abs(d) > TOL for d in deltas),
        "by_config_value": value_summary,
    }


def iteration_budget_analysis(canonical: list[dict[str, Any]]) -> dict[str, Any]:
    budgets = sorted({r["iteration_budget"] for r in canonical})
    baseline_by_inst = {
        r["instance"]: r
        for r in canonical
        if r["config_id"] == "baseline_default"
    }

    per_budget: dict[int, Any] = {}
    for b in budgets:
        subset = [r for r in canonical if r["iteration_budget"] == b and r["varied_param"] in ("baseline", "iters")]
        # For budget b, take rows where iters==b (includes baseline when b=400)
        rows_b = [r for r in canonical if r["iteration_budget"] == b]
        wins = ties = losses = 0
        per_inst = {}
        for inst, base in baseline_by_inst.items():
            cand = next((r for r in rows_b if r["instance"] == inst), None)
            if not cand:
                continue
            d = float(cand["final_bw"]) - float(base["final_bw"])
            if d < -TOL:
                wins += 1
            elif d > TOL:
                losses += 1
            else:
                ties += 1
            per_inst[inst] = {
                "final_bw": cand["final_bw"],
                "baseline_bw": base["final_bw"],
                "delta_bw": d,
                "runtime_sec": cand["runtime_sec"],
                "quality_per_runtime": (
                    (base["final_bw"] - cand["final_bw"]) / cand["runtime_sec"]
                    if cand["runtime_sec"] > 0 else 0.0
                ),
            }
        bws = [float(r["final_bw"]) for r in rows_b]
        per_budget[b] = {
            "n_instances": len(rows_b),
            "mean_final_bw": sum(bws) / len(bws) if bws else None,
            "median_final_bw": sorted(bws)[len(bws) // 2] if bws else None,
            "wins_ties_losses_vs_baseline400": [wins, ties, losses],
            "per_instance": per_inst,
        }

    # Smallest budget matching best observed per instance
    best_bw_by_inst: dict[str, float] = {}
    for inst in baseline_by_inst:
        inst_rows = [r for r in canonical if r["instance"] == inst]
        best_bw_by_inst[inst] = min(float(r["final_bw"]) for r in inst_rows)

    min_budget_match: dict[str, int] = {}
    for inst, best in best_bw_by_inst.items():
        matching = sorted(
            {
                int(r["iteration_budget"])
                for r in canonical
                if r["instance"] == inst and abs(float(r["final_bw"]) - best) <= TOL
            }
        )
        min_budget_match[inst] = matching[0] if matching else None

    n_match_at = defaultdict(int)
    for b in budgets:
        count = sum(
            1 for inst, best in best_bw_by_inst.items()
            if any(
                r["instance"] == inst
                and int(r["iteration_budget"]) == b
                and abs(float(r["final_bw"]) - best) <= TOL
                for r in canonical
            )
        )
        n_match_at[b] = count

    return {
        "budgets_tested": budgets,
        "per_budget": per_budget,
        "min_budget_matching_best_per_instance": min_budget_match,
        "instances_matching_best_at_budget": dict(n_match_at),
        "budget_matching_all_10": next(
            (b for b in budgets if n_match_at[b] == 10), None
        ),
        "budget_matching_at_least_90pct": next(
            (b for b in budgets if n_match_at[b] >= 9), None
        ),
    }


def rng_analysis(canonical: list[dict[str, Any]]) -> dict[str, Any]:
    rng_rows = [r for r in canonical if r["varied_param"] in ("baseline", "rng_seed")]
    by_seed: dict[int, list[float]] = defaultdict(list)
    for r in rng_rows:
        by_seed[int(r["rng_seed"])].append(float(r["final_bw"]))
    return {
        "seeds_used": sorted(by_seed),
        "n_configs_with_multiple_seeds": 1,
        "note": "Only baseline configuration replicated across seeds 1,2,3; all other configs use seed 1 only.",
        "per_seed_mean_bw": {k: sum(v) / len(v) for k, v in by_seed.items()},
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    fields = list(rows[0].keys())
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--validate-only", action="store_true")
    args = ap.parse_args()

    rows = load_checkpoints()
    if len(rows) != 140:
        raise SystemExit(f"Expected 140 checkpoints, found {len(rows)}")

    keys = [r["run_key"] for r in rows]
    if len(set(keys)) != 140:
        raise SystemExit("Duplicate run keys in checkpoints")

    seed_bw = load_exp2_seed_bw()
    canonical = build_canonical(rows, seed_bw)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(CANONICAL_CSV, canonical)
    CANONICAL_JSON.write_text(json.dumps(canonical, indent=2), encoding="utf-8")

    data_dict = {
        "canonical_runs.csv": {
            col: "see postprocess_coap_ipsns_sensitivity.py"
            for col in (canonical[0].keys() if canonical else [])
        },
        "null_fields_note": (
            "accepted_moves, attempted_moves, first_improvement_iteration, "
            "last_improvement_iteration are null because stage-1 driver used return_info=False."
        ),
    }
    DATA_DICT.write_text(json.dumps(data_dict, indent=2), encoding="utf-8")

    hashes = {
        "canonical_runs.csv": sha256_file(CANONICAL_CSV),
        "canonical_runs.json": sha256_file(CANONICAL_JSON),
        "canonical_data_dictionary.json": sha256_file(DATA_DICT),
    }
    HASHES.write_text(json.dumps(hashes, indent=2), encoding="utf-8")

    analysis = {
        "n_runs": len(canonical),
        "parameter_comparisons": {
            p: compare_to_baseline(canonical, p)
            for p in ("iters", "topk_scc", "destroy_addback_frac", "destroy_remove_frac", "rng_seed")
        },
        "iteration_budget": iteration_budget_analysis(canonical),
        "rng_robustness": rng_analysis(canonical),
        "tolerance": {
            "values_tested": sorted({r["tol"] for r in canonical}),
            "note": "No tolerance variation in stage-1 design; all runs used 1e-12.",
        },
        "exp2_seed_bw_reference": seed_bw,
    }
    ANALYSIS_JSON.write_text(json.dumps(analysis, indent=2), encoding="utf-8")

    if args.validate_only:
        print("Validation OK:", len(rows), "runs")
        return 0

    print(f"Wrote {CANONICAL_CSV}")
    print(f"SHA256 CSV: {hashes['canonical_runs.csv']}")
    print(json.dumps(analysis["parameter_comparisons"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
