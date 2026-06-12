"""
CLI wrapper for DRMacIver Feedback-Arc-Set C tool.

Source: https://github.com/DRMacIver/Feedback-Arc-Set (commit 16ff24a)
Binary: experiments/exp4_external_baselines/external_tools/Feedback-Arc-Set/fas

Converts DIMACS .d to DRMacIver input format, runs the binary, parses output.
Fails with a clear status if the binary is not found.
"""
import argparse
import json
import subprocess
import sys
import os
import tempfile
import time
import re

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from mwfas.io import read_graph_dimacs_agg
from mwfas.evaluation import compute_forward_backward

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FAS_BINARY = os.path.join(
    REPO_ROOT,
    "experiments/exp4_external_baselines/external_tools/Feedback-Arc-Set/fas"
)
DRMACIVER_COMMIT = "16ff24a92fde886e58819180a9fe686e60991c5c"


def _write_ranking_csv(index_to_node, order, output_path):
    import pandas as pd
    rows = [{"Node ID": str(index_to_node[v]).strip(), "Order": r}
            for r, v in enumerate(order)]
    pd.DataFrame(rows).to_csv(output_path, index=False)


def _parse_ordering_line(line):
    """
    Parse 'Optimal ordering: a b [c d] || [e f] g' into a flat list.

    Brackets indicate ties (order within doesn't matter; we keep appearance order).
    '||' separates condorcet partitions; we keep left-to-right order across partitions.
    """
    # Remove 'Optimal ordering:' prefix
    s = re.sub(r"^Optimal ordering:\s*", "", line.strip())
    # Remove brackets and ||, leaving space-separated integers
    s = s.replace("[", " ").replace("]", " ").replace("||", " ")
    tokens = s.split()
    order = []
    for tok in tokens:
        try:
            order.append(int(tok))
        except ValueError:
            pass
    return order


def run_drmaciver_fas(input_path, output_path=None):
    t0 = time.time()
    edges_indexed, node_to_index, index_to_node = read_graph_dimacs_agg(input_path)
    n = len(node_to_index)

    if not os.path.isfile(FAS_BINARY) or not os.access(FAS_BINARY, os.X_OK):
        return {
            "algorithm": "drmaciver_fas",
            "status": "external_tool_unavailable",
            "error": f"fas binary not found or not executable at {FAS_BINARY}",
            "n_nodes": n,
            "n_edges": len(edges_indexed),
            "total_weight": sum(w for _, _, w in edges_indexed),
            "runtime": time.time() - t0,
        }

    # Build DRMacIver input: n\ni j w\n...
    lines = [str(n)]
    for u, v, w in edges_indexed:
        lines.append(f"{u} {v} {w}")
    input_str = "\n".join(lines) + "\n"

    try:
        result = subprocess.run(
            [FAS_BINARY],
            input=input_str,
            capture_output=True,
            text=True,
            timeout=300,
        )
    except subprocess.TimeoutExpired:
        return {
            "algorithm": "drmaciver_fas",
            "status": "timeout",
            "error": "fas binary timed out (>300s)",
            "n_nodes": n,
            "n_edges": len(edges_indexed),
            "total_weight": sum(w for _, _, w in edges_indexed),
            "runtime": time.time() - t0,
        }
    except Exception as e:
        return {
            "algorithm": "drmaciver_fas",
            "status": "error",
            "error": str(e),
            "n_nodes": n,
            "n_edges": len(edges_indexed),
            "total_weight": sum(w for _, _, w in edges_indexed),
            "runtime": time.time() - t0,
        }

    stdout = result.stdout.strip()
    if result.returncode != 0 or not stdout:
        return {
            "algorithm": "drmaciver_fas",
            "status": "error",
            "error": f"fas exited {result.returncode}: {result.stderr[:200]}",
            "n_nodes": n,
            "n_edges": len(edges_indexed),
            "total_weight": sum(w for _, _, w in edges_indexed),
            "runtime": time.time() - t0,
        }

    lines_out = stdout.splitlines()
    order_line = None
    for l in lines_out:
        if "Optimal ordering" in l:
            order_line = l
            break

    if order_line is None:
        return {
            "algorithm": "drmaciver_fas",
            "status": "parse_error",
            "error": f"no 'Optimal ordering' line in output: {stdout[:200]}",
            "n_nodes": n,
            "n_edges": len(edges_indexed),
            "total_weight": sum(w for _, _, w in edges_indexed),
            "runtime": time.time() - t0,
        }

    order = _parse_ordering_line(order_line)

    if sorted(order) != list(range(n)):
        return {
            "algorithm": "drmaciver_fas",
            "status": "invalid_ordering",
            "error": f"ordering contains {len(order)} elements, expected {n}",
            "n_nodes": n,
            "n_edges": len(edges_indexed),
            "total_weight": sum(w for _, _, w in edges_indexed),
            "runtime": time.time() - t0,
        }

    scores = {v: r for r, v in enumerate(order)}
    total_w, fw, bw = compute_forward_backward(edges_indexed, scores)

    if output_path:
        _write_ranking_csv(index_to_node, order, output_path)

    return {
        "algorithm": "drmaciver_fas",
        "backward_weight": bw,
        "forward_weight": fw,
        "forward_ratio": fw / total_w if total_w > 0 else 1.0,
        "runtime": time.time() - t0,
        "n_nodes": n,
        "n_edges": len(edges_indexed),
        "total_weight": total_w,
        "error": None,
        "external_version_or_commit": DRMACIVER_COMMIT,
        "status": "ok",
    }


def main():
    p = argparse.ArgumentParser(
        description="DRMacIver FAS C tool wrapper (https://github.com/DRMacIver/Feedback-Arc-Set)"
    )
    p.add_argument("--input", required=True, help="DIMACS .d instance file")
    p.add_argument("--output", default=None, help="Output ranking CSV path")
    p.add_argument("--summary-output", default=None, help="One-row metrics JSON path")
    args = p.parse_args()

    result = run_drmaciver_fas(args.input, args.output)

    if args.summary_output:
        with open(args.summary_output, "w") as f:
            json.dump(result, f, indent=2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
