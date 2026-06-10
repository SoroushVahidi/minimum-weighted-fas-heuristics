#!/usr/bin/env python3
"""Select stratified tuning/holdout instance sets for COAP IPSNS stage-2 validation."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EXP1B = REPO_ROOT / "experiments/exp1b_core_benchmark_full_wmsf_seed/tables/exp1b_core_benchmark_paper_summary.csv"
EXP2_INST = {
    "bad1", "bad2", "bad3", "bad4", "bad5", "bad6", "bad7", "bad", "grid", "r1000"
}
BENCH_LIST = REPO_ROOT / "experiments/exp1b_core_benchmark_full_wmsf_seed/configs/benchmark_instances_found_all.txt"
OUT_DIR = REPO_ROOT / "experiments/coap_ipsns_holdout/config"

REQUIRED_HOLDOUT = {"r20_60"}


def load_rows() -> list[dict]:
    rows = []
    with open(EXP1B, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if float(row["ipsns_bw"]) < 0:
                continue
            if row["instance"] in EXP2_INST:
                continue
            row["n"] = int(row["n"])
            row["m"] = int(row["m"])
            row["density"] = row["m"] / (row["n"] * (row["n"] - 1)) if row["n"] > 1 else 0.0
            row["lrta_bw"] = float(row["lrta_bw"])
            row["ipsns_bw"] = float(row["ipsns_bw"])
            row["gain"] = float(row.get("ipsns_gain_over_best_seed") or 0.0)
            row["ipsns_improves"] = row["ipsns_bw"] < row["lrta_bw"] - 1e-9
            rows.append(row)
    return rows


def path_for_instance(name: str, path_map: dict[str, str]) -> str:
    if name in path_map:
        return path_map[name]
    raise KeyError(name)


def build_path_map() -> dict[str, str]:
    mapping = {}
    with open(BENCH_LIST, encoding="utf-8") as f:
        for line in f:
            p = line.strip()
            if not p:
                continue
            mapping[Path(p).stem] = p
    return mapping


def score_stratum(row: dict) -> tuple:
    # coarse buckets for stratification
    if row["n"] < 50:
        size = "tiny"
    elif row["n"] < 300:
        size = "small"
    elif row["n"] < 1000:
        size = "medium"
    else:
        size = "large"
    if row["density"] < 0.005:
        dens = "sparse"
    elif row["density"] < 0.05:
        dens = "mid"
    else:
        dens = "dense"
    improve = "gain" if row["ipsns_improves"] else ("tie" if abs(row["gain"]) < 1e-9 else "mixed")
    return (size, dens, improve)


def select(rows: list[dict], k: int, reserved: set[str]) -> list[dict]:
    chosen: list[dict] = []
    used: set[str] = set()
    for name in sorted(reserved):
        cand = next(r for r in rows if r["instance"] == name)
        chosen.append(cand)
        used.add(name)
    # one per stratum first
    by_stratum: dict[tuple, list[dict]] = {}
    for r in rows:
        if r["instance"] in used:
            continue
        by_stratum.setdefault(score_stratum(r), []).append(r)
    for stratum in sorted(by_stratum):
        pool = sorted(by_stratum[stratum], key=lambda r: (-abs(r["gain"]), r["instance"]))
        if pool:
            chosen.append(pool[0])
            used.add(pool[0]["instance"])
    # fill remaining by descending |gain| then runtime proxy (large n)
    rest = [r for r in rows if r["instance"] not in used]
    rest.sort(key=lambda r: (-abs(r["gain"]), -r["n"], r["instance"]))
    for r in rest:
        if len(chosen) >= k:
            break
        chosen.append(r)
        used.add(r["instance"])
    return chosen[:k]


def write_csv(path: Path, rows: list[dict], path_map: dict[str, str]) -> None:
    fields = [
        "instance", "file_path", "n", "m", "density", "lrta_bw", "ipsns_bw",
        "ipsns_gain_over_best_seed", "ipsns_improves", "stratum",
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({
                "instance": r["instance"],
                "file_path": path_map[r["instance"]],
                "n": r["n"],
                "m": r["m"],
                "density": round(r["density"], 8),
                "lrta_bw": r["lrta_bw"],
                "ipsns_bw": r["ipsns_bw"],
                "ipsns_gain_over_best_seed": r["gain"],
                "ipsns_improves": r["ipsns_improves"],
                "stratum": "|".join(score_stratum(r)),
            })


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tuning-k", type=int, default=18)
    ap.add_argument("--holdout-k", type=int, default=25)
    args = ap.parse_args()

    path_map = build_path_map()
    rows = load_rows()
    tuning = select(rows, args.tuning_k, reserved=set())
    holdout_used = set(REQUIRED_HOLDOUT)
    holdout = select(rows, args.holdout_k, reserved=holdout_used)
    holdout_names = {r["instance"] for r in holdout}
    tuning = [r for r in tuning if r["instance"] not in holdout_names]
    if len(tuning) < args.tuning_k:
        extra = [r for r in rows if r["instance"] not in holdout_names and r not in tuning]
        extra.sort(key=lambda r: (-abs(r["gain"]), -r["n"]))
        for r in extra:
            if len(tuning) >= args.tuning_k:
                break
            if r["instance"] not in {x["instance"] for x in tuning}:
                tuning.append(r)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(OUT_DIR / "tuning_instances.csv", tuning, path_map)
    write_csv(OUT_DIR / "holdout_instances.csv", holdout, path_map)
    meta = {
        "source": str(EXP1B),
        "excluded_exp2_instances": sorted(EXP2_INST),
        "required_holdout": sorted(REQUIRED_HOLDOUT),
        "eligible_pool_size": len(rows),
        "tuning_count": len(tuning),
        "holdout_count": len(holdout),
        "overlap": sorted(set(r["instance"] for r in tuning) & holdout_names),
    }
    (OUT_DIR / "selection_metadata.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(json.dumps(meta, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
