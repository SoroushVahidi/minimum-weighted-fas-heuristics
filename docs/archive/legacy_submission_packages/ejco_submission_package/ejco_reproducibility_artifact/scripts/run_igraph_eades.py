"""
CLI wrapper for igraph approx_eades feedback arc set heuristic.

Uses python-igraph v1.0.0 (or later), method="eades".
Fails with a clear status if igraph is not installed.
"""
import argparse
import json
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from mwfas.io import read_graph_dimacs_agg
from mwfas.evaluation import compute_forward_backward


def _write_ranking_csv(index_to_node, order, output_path):
    import pandas as pd
    rows = [{"Node ID": str(index_to_node[v]).strip(), "Order": r}
            for r, v in enumerate(order)]
    pd.DataFrame(rows).to_csv(output_path, index=False)


def run_igraph_eades(input_path, output_path=None):
    t0 = time.time()
    edges_indexed, node_to_index, index_to_node = read_graph_dimacs_agg(input_path)
    n = len(node_to_index)

    try:
        import igraph as ig
        igraph_version = ig.__version__
    except ImportError:
        return {
            "algorithm": "igraph_approx_eades",
            "status": "solver_unavailable",
            "error": "python-igraph not installed (pip install python-igraph)",
            "n_nodes": n,
            "n_edges": len(edges_indexed),
            "total_weight": sum(w for _, _, w in edges_indexed),
            "runtime": time.time() - t0,
        }

    g = ig.Graph(n=n, directed=True)
    edge_list = [(u, v) for u, v, _ in edges_indexed]
    weights = [w for _, _, w in edges_indexed]
    if edge_list:
        g.add_edges(edge_list)
        g.es["weight"] = weights

    fas_ids = g.feedback_arc_set(
        weights=g.es["weight"] if weights else None,
        method="eades"
    )

    g2 = g.copy()
    if fas_ids:
        g2.delete_edges(fas_ids)
    order = list(g2.topological_sorting())

    scores = {v: r for r, v in enumerate(order)}
    total_w, fw, bw = compute_forward_backward(edges_indexed, scores)

    if output_path:
        _write_ranking_csv(index_to_node, order, output_path)

    return {
        "algorithm": "igraph_approx_eades",
        "backward_weight": bw,
        "forward_weight": fw,
        "forward_ratio": fw / total_w if total_w > 0 else 1.0,
        "runtime": time.time() - t0,
        "n_nodes": n,
        "n_edges": len(edges_indexed),
        "total_weight": total_w,
        "error": None,
        "external_version_or_commit": f"python-igraph=={igraph_version}",
        "status": "ok",
    }


def main():
    p = argparse.ArgumentParser(
        description="igraph approx_eades FAS heuristic (python-igraph wrapper)"
    )
    p.add_argument("--input", required=True, help="DIMACS .d instance file")
    p.add_argument("--output", default=None, help="Output ranking CSV path")
    p.add_argument("--summary-output", default=None, help="One-row metrics JSON path")
    args = p.parse_args()

    result = run_igraph_eades(args.input, args.output)

    if args.summary_output:
        with open(args.summary_output, "w") as f:
            json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
