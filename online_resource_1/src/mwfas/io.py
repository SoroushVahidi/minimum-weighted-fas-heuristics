"""DIMACS graph reader for weighted directed graphs."""

from collections import defaultdict


def read_graph_dimacs_agg(file_path):
    """
    Read DIMACS-like arc lines: a <source> <target> <weight> [...]

    Aggregates parallel arcs (multiple (u,v) become one with summed weight).
    Returns deterministic, sorted edge and node orderings.

    Returns:
        edges_indexed: list of (u_idx, v_idx, w_sum)
        node_to_index: dict mapping node id string to int index
        index_to_node: dict mapping int index to node id string
    """
    agg = defaultdict(float)
    node_ids = set()

    with open(file_path, "r") as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            if line.startswith(("c", "p")):
                continue
            if not line.startswith("a"):
                continue

            parts = line.split()
            if len(parts) < 4:
                continue

            u = parts[1]
            v = parts[2]
            try:
                w = float(parts[3])
            except ValueError:
                continue

            node_ids.add(u)
            node_ids.add(v)
            agg[(u, v)] += w

    node_list = sorted(node_ids)
    node_to_index = {node: i for i, node in enumerate(node_list)}
    index_to_node = {i: node for node, i in node_to_index.items()}

    edges_indexed = [
        (node_to_index[u], node_to_index[v], float(w_sum))
        for (u, v), w_sum in agg.items()
    ]
    edges_indexed.sort(key=lambda e: (e[0], e[1]))
    return edges_indexed, node_to_index, index_to_node
