#!/usr/bin/env python3
"""
EXP9 preparation: download and convert Wikipedia Adminship Vote Network.

Dataset: SNAP wiki-Vote
  Source: J. Leskovec, D. Huttenlocher, J. Kleinberg.
          "Predicting Positive and Negative Links in Online Social Networks."
          Proc. WWW 2010.
  URL:    https://snap.stanford.edu/data/wiki-Vote.txt.gz

Conversion:
  - Restrict to top-N nodes by total degree (default N=50; smoke N=10).
  - Build pairwise weight matrix: w[u][v] = #times u voted for v.
  - Save as DIMACS weighted arc file and config CSV.
"""
import argparse
import csv
import gzip
import json
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
EXP_DIR = REPO / "experiments" / "exp9_application_case"
RAW_DIR = EXP_DIR / "raw"
CONV_DIR = EXP_DIR / "converted"
CONF_DIR = EXP_DIR / "config"

SNAP_URL = "https://snap.stanford.edu/data/wiki-Vote.txt.gz"
RAW_FILE = RAW_DIR / "wiki-Vote.txt.gz"
DIMACS_FULL = CONV_DIR / "wiki_vote_top50.d"
DIMACS_SMOKE = CONV_DIR / "wiki_vote_top10.d"

FAIL_PATH = EXP_DIR / "EXP9_FEASIBILITY_FAILED.md"


def download_dataset() -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    if RAW_FILE.exists():
        print(f"Raw file already present: {RAW_FILE}")
        return RAW_FILE
    print(f"Downloading {SNAP_URL} …")
    req = urllib.request.Request(SNAP_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp, RAW_FILE.open("wb") as fout:
        fout.write(resp.read())
    print(f"Saved {RAW_FILE} ({RAW_FILE.stat().st_size} bytes)")
    return RAW_FILE


def parse_edges(raw_gz: Path) -> list[tuple[str, str]]:
    with gzip.open(raw_gz, "rt", encoding="utf-8", errors="ignore") as f:
        edges = []
        for line in f:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            parts = line.split()
            if len(parts) >= 2:
                edges.append((parts[0], parts[1]))
    return edges


def build_subgraph(edges: list[tuple[str, str]], top_n: int):
    degree = Counter()
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    top_nodes = {node for node, _ in degree.most_common(top_n)}

    pairwise: dict[tuple[str, str], int] = defaultdict(int)
    for u, v in edges:
        if u in top_nodes and v in top_nodes and u != v:
            pairwise[(u, v)] += 1

    return top_nodes, pairwise


def write_dimacs(pairwise: dict, top_nodes: set, out_path: Path,
                 node_map: dict | None = None) -> dict:
    CONV_DIR.mkdir(parents=True, exist_ok=True)
    # Stable sorted ordering
    sorted_nodes = sorted(top_nodes, key=int)
    if node_map is None:
        node_map = {n: i + 1 for i, n in enumerate(sorted_nodes)}

    arcs = [(node_map[u], node_map[v], w)
            for (u, v), w in pairwise.items()
            if u in node_map and v in node_map]
    arcs.sort()

    n = len(sorted_nodes)
    m = len(arcs)
    total_w = sum(w for _, _, w in arcs)
    density = m / (n * (n - 1)) if n > 1 else 0.0

    with out_path.open("w") as f:
        f.write(f"c Wikipedia Adminship Vote Network (SNAP) — top-{n} nodes\n")
        f.write(f"c Source: Leskovec et al. (2010) https://snap.stanford.edu/data/wiki-Vote.html\n")
        f.write(f"c Nodes: {n}  Arcs: {m}  TotalWeight: {total_w}\n")
        f.write(f"p arc {n} {m}\n")
        for u, v, w in arcs:
            f.write(f"a {u} {v} {w}\n")

    return {
        "n": n, "m": m, "total_weight": total_w,
        "density": round(density, 6),
        "node_map": node_map,
    }


def write_provenance(info_full: dict, info_smoke: dict):
    CONF_DIR.mkdir(parents=True, exist_ok=True)

    prov = {
        "dataset": "Wikipedia Adminship Vote Network",
        "source": "SNAP Stanford Network Analysis Project",
        "citation": (
            "J. Leskovec, D. Huttenlocher, J. Kleinberg. "
            "'Predicting Positive and Negative Links in Online Social Networks.' "
            "Proc. WWW 2010."
        ),
        "url": SNAP_URL,
        "raw_file": str(RAW_FILE.relative_to(REPO)),
        "license": "SNAP public datasets (educational/research use)",
        "application_framing": (
            "Find a hierarchical prestige ranking of Wikipedia users that "
            "minimizes reverse endorsements (backward arcs). Each arc u->v "
            "has weight = number of times user u voted in support of user v's "
            "adminship candidacy. A minimum-BW ordering extracts the best-fitting "
            "hierarchical structure from the endorsement vote graph."
        ),
        "conversion_rule": (
            "Restrict to top-N users by total edge degree; "
            "w_uv = total vote count from u to v across all elections."
        ),
        "anonymization": "Original SNAP integer node IDs are used (no names).",
        "full_instance": {
            "file": str(DIMACS_FULL.relative_to(REPO)),
            **{k: v for k, v in info_full.items() if k != "node_map"},
        },
        "smoke_instance": {
            "file": str(DIMACS_SMOKE.relative_to(REPO)),
            **{k: v for k, v in info_smoke.items() if k != "node_map"},
        },
    }
    (CONF_DIR / "dataset_provenance.json").write_text(json.dumps(prov, indent=2))

    md = f"""# EXP9 Dataset Provenance

## Dataset
**Wikipedia Adminship Vote Network** (SNAP)

## Citation
{prov['citation']}

## URL
{prov['url']}

## Application framing
{prov['application_framing']}

## Conversion rule
{prov['conversion_rule']}

## Full instance (`{prov['full_instance']['file']}`)
- n = {info_full['n']} nodes, m = {info_full['m']} arcs
- Total weight = {info_full['total_weight']}
- Density = {info_full['density']:.6f}

## Smoke instance (`{prov['smoke_instance']['file']}`)
- n = {info_smoke['n']} nodes, m = {info_smoke['m']} arcs
- Total weight = {info_smoke['total_weight']}
- Density = {info_smoke['density']:.6f}

## Anonymization
{prov['anonymization']}
"""
    (CONF_DIR / "dataset_provenance.md").write_text(md)


def write_instance_csv(info_full: dict, info_smoke: dict):
    rows = [
        {
            "instance": "wiki_vote_top50",
            "file_path": str(DIMACS_FULL),
            "file_found": DIMACS_FULL.exists(),
            "dataset": "wikipedia_adminship_vote",
            "top_n": 50,
            "n": info_full["n"],
            "m": info_full["m"],
            "density": info_full["density"],
            "total_weight": info_full["total_weight"],
            "smoke": False,
        },
        {
            "instance": "wiki_vote_top10",
            "file_path": str(DIMACS_SMOKE),
            "file_found": DIMACS_SMOKE.exists(),
            "dataset": "wikipedia_adminship_vote",
            "top_n": 10,
            "n": info_smoke["n"],
            "m": info_smoke["m"],
            "density": info_smoke["density"],
            "total_weight": info_smoke["total_weight"],
            "smoke": True,
        },
    ]
    with (CONF_DIR / "application_instances.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top-n-full", type=int, default=50)
    ap.add_argument("--top-n-smoke", type=int, default=10)
    args = ap.parse_args()

    try:
        raw = download_dataset()
        edges = parse_edges(raw)
        print(f"Parsed {len(edges)} total edges")

        # Full instance
        top_nodes_full, pw_full = build_subgraph(edges, args.top_n_full)
        info_full = write_dimacs(pw_full, top_nodes_full, DIMACS_FULL)
        print(f"Full instance: n={info_full['n']} m={info_full['m']} "
              f"density={info_full['density']:.4f} → {DIMACS_FULL}")

        # Smoke instance (use same node map as subset)
        top_nodes_smoke = set(
            sorted(top_nodes_full, key=int)[:args.top_n_smoke]
        )
        pw_smoke = {(u, v): w for (u, v), w in pw_full.items()
                    if u in top_nodes_smoke and v in top_nodes_smoke}
        info_smoke = write_dimacs(pw_smoke, top_nodes_smoke, DIMACS_SMOKE)
        print(f"Smoke instance: n={info_smoke['n']} m={info_smoke['m']} "
              f"density={info_smoke['density']:.4f} → {DIMACS_SMOKE}")

        write_provenance(info_full, info_smoke)
        write_instance_csv(info_full, info_smoke)

        if FAIL_PATH.exists():
            FAIL_PATH.unlink()
        print("\nEXP9 preparation complete.")

    except Exception as exc:
        import traceback
        msg = f"# EXP9 Feasibility Failed\n\n{exc}\n\n```\n{traceback.format_exc()}\n```\n"
        FAIL_PATH.write_text(msg)
        print(f"FEASIBILITY FAILED: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
