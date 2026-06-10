"""
Deterministic medium sparse instance selection for EXP8 MIP baseline.

Target: 12-20 instances spanning n=20..400, mixing gain and tie cases,
including the IPSNS near-miss instance (r20_60).
"""
import csv
import math
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
EXP4_RAW = BASE / "experiments/exp4_external_baselines/summary/exp4_raw_summary.csv"
FEAT_CSV = BASE / "paper/notes/structural_risk_reduction/graph_features_sparse.csv"
OUT_DIR = BASE / "experiments/exp8_medium_mip_baseline/config"
OUT_DIR.mkdir(parents=True, exist_ok=True)

BENCH_ROOTS = [
    Path.home() / "benchmark_sources/graph-benchmarks",
]

# ── helpers ──────────────────────────────────────────────────────────────────

def read_csv(path):
    with open(path, newline="", errors="ignore") as f:
        return list(csv.DictReader(f))

def find_file(inst_name, roots):
    """Search benchmark roots for the instance file."""
    for root in roots:
        for p in root.rglob(f"{inst_name}.d"):
            return p
        for p in root.rglob(f"{inst_name}.dimacs"):
            return p
    return None

def mip_var_count(n):
    return n * (n - 1) // 2

def mip_constraint_count(n):
    return 2 * n * (n - 1) * (n - 2) // 6

# ── load EXP4 results ────────────────────────────────────────────────────────
exp4 = read_csv(EXP4_RAW)

# Build pivot: instance -> alg -> {bw, rt, n, m}
pivot = {}
for r in exp4:
    if r["status"] != "ok" or not r.get("backward_weight", "").strip():
        continue
    inst = r["instance"]
    alg = r["algorithm"]
    try:
        bw = float(r["backward_weight"])
        rt = float(r.get("runtime") or 0)
        n = int(float(r.get("n") or 0))
        m = int(float(r.get("m") or 0))
    except ValueError:
        continue
    pivot.setdefault(inst, {})[alg] = {"bw": bw, "rt": rt, "n": n, "m": m}

# Load structural features
feat = {}
if FEAT_CSV.exists():
    for row in read_csv(FEAT_CSV):
        feat[row["instance"]] = row

# ── candidate pool ────────────────────────────────────────────────────────────
# Keep nonneg instances with IPSNS and LR-TA results, n in [20..400]
# MIP feasibility heuristic: n*(n-1)/2 <= 100,000 vars → n <= 447
# Use triangle constraint count <= 10M → n*(n-1)*(n-2)/3 <= 10M → n <= ~285

MAX_N = 400      # hard cap
MIN_N = 20       # include the near-miss (n=20) instance

candidates = {}
for inst, algs in pivot.items():
    if "ipsns_full" not in algs or "lrta_full" not in algs:
        continue
    n = algs["ipsns_full"]["n"] or algs["lrta_full"]["n"]
    if n < MIN_N or n > MAX_N:
        continue
    lrta_bw = algs["lrta_full"]["bw"]
    ipsns_bw = algs["ipsns_full"]["bw"]
    if lrta_bw < 0:   # exclude negative-weight instances
        continue
    gain = lrta_bw - ipsns_bw
    candidates[inst] = {
        "n": n,
        "m": algs["ipsns_full"]["m"],
        "lrta_bw": lrta_bw,
        "ipsns_bw": ipsns_bw,
        "wmsf_bw": algs.get("wmsf_full", {}).get("bw"),
        "drmaciver_bw": algs.get("drmaciver_fas", {}).get("bw"),
        "gain_ipsns_over_lrta": gain,
        "mip_vars": mip_var_count(n),
        "mip_constraints": mip_constraint_count(n),
        "density": float(feat.get(inst, {}).get("density") or 0) or None,
    }

print(f"Candidate pool: {len(candidates)} instances (n={MIN_N}..{MAX_N}, nonneg)")
for inst in sorted(candidates, key=lambda x: candidates[x]["n"]):
    c = candidates[inst]
    print(f"  {inst:20s} n={c['n']:4d} gain={c['gain_ipsns_over_lrta']:8.1f} "
          f"vars={c['mip_vars']:6d} constr={c['mip_constraints']:8d}")

# ── selection ────────────────────────────────────────────────────────────────
selected = {}

# Group 1: instances where IPSNS strictly improves over LR-TA (gain > 0)
gain_instances = sorted([i for i in candidates if candidates[i]["gain_ipsns_over_lrta"] > 0],
                        key=lambda x: (candidates[x]["n"], x))
for i in gain_instances:
    selected[i] = "ipsns_gain"
    print(f"  Selected (gain): {i}")

# Group 2: n=20..75 ties/small (include the near-miss r20_60 if available)
for i in sorted([x for x in candidates if candidates[x]["n"] <= 75 and x not in selected],
                key=lambda x: candidates[x]["n"]):
    selected[i] = "small_tie"
    print(f"  Selected (small_tie): {i}")

# Group 3: density quartiles from remaining candidates (fill to 15)
remaining = sorted([i for i in candidates if i not in selected],
                   key=lambda x: candidates[x]["n"])
# Take at intervals to cover n range
while len(selected) < 15 and remaining:
    i = remaining.pop(0)
    selected[i] = "medium_tie"
    print(f"  Selected (medium_tie): {i}")

# Trim to 20 max deterministically
if len(selected) > 20:
    all_sel = sorted(selected.keys(), key=lambda x: (candidates[x]["n"], x))
    selected = {k: selected[k] for k in all_sel[:20]}

print(f"\nFinal selection: {len(selected)} instances")

# ── resolve file paths ────────────────────────────────────────────────────────
rows = []
for inst in sorted(selected, key=lambda x: candidates[x]["n"]):
    c = candidates[inst]
    fp = find_file(inst, BENCH_ROOTS)
    n = c["n"]
    rows.append({
        "instance": inst,
        "file_path": str(fp) if fp else "",
        "file_found": fp is not None,
        "selection_reason": selected[inst],
        "n": n,
        "m": c["m"],
        "density": round(c["density"] or 0, 6),
        "mip_vars": c["mip_vars"],
        "mip_constraints": c["mip_constraints"],
        "lrta_bw": round(c["lrta_bw"], 2),
        "ipsns_bw": round(c["ipsns_bw"], 2),
        "wmsf_bw": round(c["wmsf_bw"], 2) if c["wmsf_bw"] is not None else "",
        "drmaciver_bw": round(c["drmaciver_bw"], 2) if c["drmaciver_bw"] is not None else "",
        "gain_ipsns_over_lrta": round(c["gain_ipsns_over_lrta"], 2),
    })
    status = "OK" if fp else "FILE NOT FOUND"
    print(f"  {inst:20s} n={n:4d} {selected[inst]:15s} vars={c['mip_vars']:6d} [{status}]")

with open(OUT_DIR / "selected_instances.csv", "w", newline="") as f:
    if rows:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

found = sum(1 for r in rows if r["file_found"])
print(f"\nWritten: {OUT_DIR / 'selected_instances.csv'}")
print(f"Files found: {found}/{len(rows)}")
if found < len(rows):
    print("WARNING: some instance files not found; they will be skipped in EXP8.")
