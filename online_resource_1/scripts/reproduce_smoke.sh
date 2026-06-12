#!/usr/bin/env bash
# Level A: smoke validation from artifact root
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
export PYTHONPATH="$ROOT/src:${PYTHONPATH:-}"

echo "=== OR1 smoke validation ==="
python3 - <<'PY'
import os, sys
sys.path.insert(0, "src")
from mwfas.io import read_graph_dimacs_agg
from mwfas.evaluation import compute_forward_backward
from mwfas.lrta import local_ratio_fas_fast, topo_order_active
from mwfas.exact import exact_min_fas_dp
from mwfas.topo_extraction import backward_weight_from_rank, topo_kahn_min_vertex

fixtures = "tests/data/tiny_graphs"
for fn in sorted(os.listdir(fixtures)):
    if not fn.endswith(".d"):
        continue
    path = os.path.join(fixtures, fn)
    edges, n2i, _ = read_graph_dimacs_agg(path)
    n = len(n2i)
    removed, U, V, W0, active, adj = local_ratio_fas_fast(edges, n)
    order, rank = topo_order_active(n, adj, V, active)
    assert len(order) == len(set(order)) == n
    bw = backward_weight_from_rank(edges, rank)
    ex_bw, _, _ = exact_min_fas_dp(edges, n)
    assert ex_bw <= bw + 1e-6 + 1e-9 * max(bw, 1)
    print(f"OK {fn}: lrta_bw={bw:.4g} exact_bw={ex_bw:.4g}")

# topo extraction identity smoke
edges = [(0, 2, 1.0), (1, 2, 1.0), (1, 0, 10.0)]
n = 3
removed, U, V, W0, active, adj = local_ratio_fas_fast(edges, n)
_, rank = topo_kahn_min_vertex(n, adj, V, active)
assert backward_weight_from_rank(edges, rank) >= 0
print("OK topo_extraction smoke")
print("Smoke validation PASSED")
PY
