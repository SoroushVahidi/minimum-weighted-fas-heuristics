#!/usr/bin/env python3
"""EXP11: topological-extraction sensitivity on final active DAGs."""

from __future__ import annotations

import csv
import json
import os
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mwfas.io import read_graph_dimacs_agg
from mwfas.lrta import local_ratio_fas_fast
from mwfas.topo_extraction import (
    active_precedence_pairs,
    apply_extraction_rule,
    backward_weight_from_rank,
    extraction_gap,
    insertion_refine_order,
    removed_weight_from_eids,
    topo_kahn_min_vertex,
)

EXP_DIR = Path(__file__).resolve().parents[1]
CONFIG = EXP_DIR / "config" / "instances.txt"
SUMMARY = EXP_DIR / "summary"
EPS = 1e-9


def _git_head() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True
        ).strip()
    except Exception:
        return "unknown"


def _capture_lrta_state(dimacs_path: str):
    edges_indexed, node_to_index, _ = read_graph_dimacs_agg(dimacs_path)
    n = len(node_to_index)
    removed, U, V, W0, active, adj = local_ratio_fas_fast(edges_indexed, n)
    return edges_indexed, U, V, W0, active, adj, removed


def main():
    SUMMARY.mkdir(parents=True, exist_ok=True)
    instances = [
        ln.strip()
        for ln in CONFIG.read_text().splitlines()
        if ln.strip() and not ln.strip().startswith("#")
    ]
    rules = ["current_min_id", "max_id", "weighted_net"]
    rows = []
    t0 = time.time()
    for inst_path in instances:
        inst = Path(inst_path).stem
        for method in ("lrta",):
            try:
                edges, U, V, W0, active, adj, removed = _capture_lrta_state(inst_path)
            except Exception as exc:
                rows.append(
                    {
                        "instance": inst,
                        "method": method,
                        "rule": "error",
                        "bw": "",
                        "w_F": "",
                        "gap": "",
                        "rel_improve_vs_current": "",
                        "error": str(exc)[:200],
                    }
                )
                continue
            n = len(adj)
            _, rank_current = topo_kahn_min_vertex(n, adj, V, active)
            bw_current = backward_weight_from_rank(edges, rank_current)
            w_f = removed_weight_from_eids(U, V, W0, removed)
            gap_current = extraction_gap(w_f, bw_current)
            for rule in rules:
                if rule == "current_min_id":
                    _, rank = topo_kahn_min_vertex(n, adj, V, active)
                else:
                    _, rank = apply_extraction_rule(rule, n, adj, V, W0, active)
                bw = backward_weight_from_rank(edges, rank)
                rel = (bw_current - bw) / max(bw_current, EPS)
                rows.append(
                    {
                        "instance": inst,
                        "method": method,
                        "rule": rule,
                        "bw": bw,
                        "w_F": w_f,
                        "gap": extraction_gap(w_f, bw),
                        "rel_improve_vs_current": rel,
                        "error": "",
                    }
                )
            order, _ = topo_kahn_min_vertex(n, adj, V, active)
            prec = active_precedence_pairs(U, V, active)
            if n <= 500:
                refined = insertion_refine_order(
                    edges, order, max_passes=1, active_precedence=prec
                )
            else:
                refined = order
            rank_ref = [0] * n
            for i, v in enumerate(refined):
                rank_ref[v] = i
            bw_ref = backward_weight_from_rank(edges, rank_ref)
            rows.append(
                {
                    "instance": inst,
                    "method": method,
                    "rule": "insertion_refine",
                    "bw": bw_ref,
                    "w_F": w_f,
                    "gap": extraction_gap(w_f, bw_ref),
                    "rel_improve_vs_current": (bw_current - bw_ref) / max(bw_current, EPS),
                    "error": "",
                }
            )

    out_csv = SUMMARY / "exp11_per_instance.csv"
    fields = [
        "instance",
        "method",
        "rule",
        "bw",
        "w_F",
        "gap",
        "rel_improve_vs_current",
        "error",
    ]
    with out_csv.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    improvements = []
    for inst in {r["instance"] for r in rows if not r["error"]}:
        cur = next(
            r
            for r in rows
            if r["instance"] == inst and r["rule"] == "current_min_id" and not r["error"]
        )
        alts = [
            r
            for r in rows
            if r["instance"] == inst and r["rule"] != "current_min_id" and not r["error"]
        ]
        best_alt = min(alts, key=lambda r: float(r["bw"]))
        improvements.append(float(cur["bw"]) - float(best_alt["bw"]))

    agg = {
        "branch": subprocess.check_output(
            ["git", "branch", "--show-current"], cwd=REPO_ROOT, text=True
        ).strip(),
        "head": _git_head(),
        "n_instances": len(instances),
        "runtime_seconds": time.time() - t0,
        "median_improvement_best_alt": sorted(improvements)[len(improvements) // 2]
        if improvements
        else 0.0,
        "max_improvement_best_alt": max(improvements) if improvements else 0.0,
        "instances_improved": sum(1 for x in improvements if x > EPS),
        "instances_tied": sum(1 for x in improvements if abs(x) <= EPS),
        "median_extraction_gap_wF_minus_bw": sorted(
            float(r["gap"]) for r in rows if r["rule"] == "current_min_id" and not r["error"]
        )[len(instances) // 2]
        if instances
        else 0.0,
    }
    (SUMMARY / "exp11_aggregate.json").write_text(json.dumps(agg, indent=2))
    md = SUMMARY / "EXP11_RESULTS.md"
    md.write_text(
        f"# EXP11 results\n\n"
        f"- HEAD: `{agg['head']}`\n"
        f"- Instances: {agg['n_instances']}\n"
        f"- Runtime: {agg['runtime_seconds']:.1f}s\n"
        f"- Median best-alt improvement over current: {agg['median_improvement_best_alt']:.6g}\n"
        f"- Max best-alt improvement: {agg['max_improvement_best_alt']:.6g}\n"
        f"- Instances improved / tied: {agg['instances_improved']} / {agg['instances_tied']}\n"
        f"- Median w(F)-w(B_pi) under current rule: {agg['median_extraction_gap_wF_minus_bw']:.6g}\n"
    )
    print(json.dumps(agg, indent=2))


if __name__ == "__main__":
    main()
