"""
Deterministic instance selection for EXP6 (IPSNS budget curve).
Selects 20 representative instances from the 97-instance standard sparse set.
"""
import csv
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
EXP4_RAW = BASE / "experiments/exp4_external_baselines/summary/exp4_raw_summary.csv"
FEAT_CSV = BASE / "paper/notes/structural_risk_reduction/graph_features_sparse.csv"
INST_LIST = BASE / "experiments/exp4_external_baselines/configs/exp4_instances.txt"
OUT_DIR = BASE / "experiments/exp6_ipsns_budget_curve/config"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ── helpers ───────────────────────────────────────────────────────────────

def read_csv(path):
    with open(path, newline="", errors="ignore") as f:
        return list(csv.DictReader(f))


def read_inst_list(path):
    mapping = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                p = Path(line)
                mapping[p.stem] = p
    return mapping

# ── load data ─────────────────────────────────────────────────────────────
exp4 = read_csv(EXP4_RAW)
inst_map = read_inst_list(INST_LIST)

# Only consider IPSNS-OK standard instances with existing source files
ipsns_ok = {r["instance"] for r in exp4
            if r["algorithm"] == "ipsns_full" and r["status"] == "ok"}
lrta_bw = {r["instance"]: float(r["backward_weight"])
           for r in exp4
           if r["algorithm"] == "lrta_full" and r["status"] == "ok"
           and r.get("backward_weight", "").strip()}
ipsns_bw = {r["instance"]: float(r["backward_weight"])
            for r in exp4
            if r["algorithm"] == "ipsns_full" and r["status"] == "ok"
            and r.get("backward_weight", "").strip()}

# Filter to instances that have both IPSNS and LR-TA results and source files exist
# Also exclude trivially small instances (n < 10) to ensure budget curve is informative
_all_valid = [i for i in ipsns_ok
              if i in lrta_bw and i in inst_map and inst_map[i].exists()]

# Load n from EXP4 raw summary for filtering
n_from_exp4 = {}
for r in exp4:
    if r["algorithm"] == "ipsns_full" and r["status"] == "ok" and r.get("n", "").strip():
        try:
            n_from_exp4[r["instance"]] = int(float(r["n"]))
        except ValueError:
            pass

# Also exclude instances where EXP4 full IPSNS runtime > 60s (impractical for budget curve)
rt_from_exp4 = {}
for r in exp4:
    if r["algorithm"] == "ipsns_full" and r["status"] == "ok" and r.get("runtime", "").strip():
        try:
            rt_from_exp4[r["instance"]] = float(r["runtime"])
        except ValueError:
            pass

valid = [i for i in _all_valid
         if n_from_exp4.get(i, 0) >= 10
         and rt_from_exp4.get(i, 999) <= 60.0]
print(f"Valid instances (n>=10, RT<=60s, source file exists): {len(valid)} of {len(_all_valid)}")

# Compute IPSNS gain over LR-TA
gain = {i: lrta_bw[i] - ipsns_bw[i] for i in valid}

# Load structural features if available
feat = {}
if FEAT_CSV.exists():
    for row in read_csv(FEAT_CSV):
        inst = row["instance"]
        if inst in valid:
            feat[inst] = {
                "density": float(row["density"]) if row.get("density") else None,
                "n": int(float(row["n"])) if row.get("n") else None,
            }

# ── selection ─────────────────────────────────────────────────────────────
selected = {}  # inst -> reason

# Group 1: Top-5 IPSNS gain instances (highest gain over LR-TA)
top_gain = sorted([i for i in valid if gain[i] > 0],
                  key=lambda x: -gain[x])[:5]
for i in top_gain:
    if i not in selected:
        selected[i] = "top_gain_vs_lrta"

# Group 2: 5 zero-gain / tie instances (gain == 0)
zero_gain = [i for i in valid if gain[i] == 0]
# Sort by n (size) to get a spread
zero_sorted = sorted(zero_gain,
                     key=lambda x: feat.get(x, {}).get("n", 0) or 0)
picks = []
if len(zero_sorted) >= 5:
    # Pick at evenly spaced positions
    step = max(1, len(zero_sorted) // 5)
    for j in range(5):
        idx = min(j * step, len(zero_sorted) - 1)
        picks.append(zero_sorted[idx])
else:
    picks = zero_sorted[:5]
for i in picks:
    if i not in selected:
        selected[i] = "zero_gain_tie"

# Group 3: Density quantiles (5 instances from different density ranges)
if feat:
    dens_sorted = sorted([i for i in valid if feat.get(i, {}).get("density") is not None],
                         key=lambda x: feat[x]["density"])
    n_d = len(dens_sorted)
    if n_d >= 5:
        step = n_d // 5
        for qi in range(5):
            idx = qi * step
            i = dens_sorted[idx]
            if i not in selected:
                selected[i] = f"density_q{qi+1}"
            else:
                # Try adjacent
                for delta in [1, -1, 2, -2]:
                    alt = idx + delta
                    if 0 <= alt < n_d and dens_sorted[alt] not in selected:
                        selected[dens_sorted[alt]] = f"density_q{qi+1}"
                        break

# Group 4: Size (n) quantiles (5 instances from different size ranges)
if feat:
    size_sorted = sorted([i for i in valid if feat.get(i, {}).get("n") is not None],
                         key=lambda x: feat[x]["n"])
    n_s = len(size_sorted)
    if n_s >= 5:
        step = n_s // 5
        for qi in range(5):
            idx = qi * step
            i = size_sorted[idx]
            if i not in selected:
                selected[i] = f"size_q{qi+1}"
            else:
                for delta in [1, -1, 2, -2]:
                    alt = idx + delta
                    if 0 <= alt < n_s and size_sorted[alt] not in selected:
                        selected[size_sorted[alt]] = f"size_q{qi+1}"
                        break

# If we don't have 20 yet, fill with remaining high-gain instances
remaining = sorted([i for i in valid if i not in selected],
                   key=lambda x: -gain[x])
while len(selected) < 20 and remaining:
    i = remaining.pop(0)
    selected[i] = "gain_fill"

# Trim to 20 deterministically (keep first 20 by gain, then name)
if len(selected) > 20:
    all_sel = sorted(selected.keys(), key=lambda x: (-gain[x], x))
    selected = {i: selected[i] for i in all_sel[:20]}

print(f"Selected {len(selected)} instances.")

# ── write output ──────────────────────────────────────────────────────────
rows = []
for i in sorted(selected):
    rows.append({
        "instance": i,
        "file_path": str(inst_map[i]),
        "selection_reason": selected[i],
        "gain_vs_lrta": round(gain.get(i, 0), 4),
        "lrta_bw": round(lrta_bw.get(i, 0), 4),
        "ipsns_bw_exp4": round(ipsns_bw.get(i, 0), 4),
        "density": round(feat.get(i, {}).get("density") or 0, 6),
        "n": feat.get(i, {}).get("n") or "",
    })

with open(OUT_DIR / "selected_instances.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

print(f"Written: {OUT_DIR / 'selected_instances.csv'}")
print("\nSelected instances:")
for r in rows:
    print(f"  {r['instance']:30s} {r['selection_reason']:25s} gain={r['gain_vs_lrta']:8.1f} "
          f"density={r['density']:.4f} n={r['n']}")
