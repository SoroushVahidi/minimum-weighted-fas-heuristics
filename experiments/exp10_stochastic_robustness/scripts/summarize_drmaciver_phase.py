"""
EXP10: DRMacIver-only variability summaries (production namespace).

Outputs:
  summary/drmaciver_per_instance_summary.csv
  summary/drmaciver_variability_summary.csv
  summary/drmaciver_phase_conclusions.md
"""
import csv
import glob
import json
import math
import os
import sys
from collections import defaultdict

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
EXP_DIR = os.path.join(REPO_ROOT, "experiments", "exp10_stochastic_robustness")
RAW_DIR = os.path.join(EXP_DIR, "raw", "drmaciver")
SMOKE_RAW = os.path.join(EXP_DIR, "smoke_archive", "drmaciver", "raw")
SUMMARY_DIR = os.path.join(EXP_DIR, "summary")


def percentile(sorted_vals, p):
    if not sorted_vals:
        return float("nan")
    n = len(sorted_vals)
    idx = (n - 1) * p / 100.0
    lo = int(idx)
    hi = min(lo + 1, n - 1)
    frac = idx - lo
    return sorted_vals[lo] + frac * (sorted_vals[hi] - sorted_vals[lo])


def load_production_records():
    smoke_files = set()
    if os.path.isdir(SMOKE_RAW):
        smoke_files = {os.path.basename(p) for p in glob.glob(os.path.join(SMOKE_RAW, "*.json"))}
    records = []
    for rp in sorted(glob.glob(os.path.join(RAW_DIR, "drmaciver_*.json"))):
        if os.path.basename(rp) in smoke_files:
            continue
        try:
            with open(rp) as f:
                rec = json.load(f)
            records.append(rec)
        except Exception:
            pass
    return records


def instance_stats(recs):
    bws = sorted(r["objective_bw"] for r in recs if r.get("status") == "ok")
    rts = sorted(r["runtime_seconds"] for r in recs if r.get("status") == "ok")
    n_ok = len(bws)
    n_fail = len(recs) - n_ok
    if n_ok == 0:
        return {}
    mean_bw = sum(bws) / n_ok
    std_bw = math.sqrt(sum((v - mean_bw) ** 2 for v in bws) / n_ok) if n_ok > 1 else 0.0
    return {
        "n_success": n_ok,
        "n_failed": n_fail,
        "n_total_attempts": len(recs),
        "bw_min": bws[0],
        "bw_q1": percentile(bws, 25),
        "bw_median": percentile(bws, 50),
        "bw_mean": mean_bw,
        "bw_q3": percentile(bws, 75),
        "bw_max": bws[-1],
        "bw_std": std_bw,
        "bw_iqr": percentile(bws, 75) - percentile(bws, 25),
        "bw_cv": std_bw / mean_bw if mean_bw > 1e-9 else 0.0,
        "n_distinct_bw": len(set(bws)),
        "rt_min": rts[0] if rts else None,
        "rt_median": percentile(rts, 50) if rts else None,
        "rt_mean": sum(rts) / len(rts) if rts else None,
        "rt_max": rts[-1] if rts else None,
        "n_distinct_pids": len(set(r.get("pid") for r in recs if r.get("pid"))),
    }


def main():
    os.makedirs(SUMMARY_DIR, exist_ok=True)
    records = load_production_records()
    by_inst = defaultdict(list)
    for r in records:
        by_inst[r["instance_id"]].append(r)

    per_rows = []
    var_rows = []
    zero_var = 0
    multi_var = 0
    for inst in sorted(by_inst):
        recs = by_inst[inst]
        st = instance_stats(recs)
        if not st:
            continue
        row = {"instance_id": inst, **st}
        if recs:
            row["n"] = recs[0].get("n")
            row["m"] = recs[0].get("m")
            row["density"] = recs[0].get("density")
        per_rows.append(row)
        var_rows.append({
            "instance_id": inst,
            "n_distinct_bw": st["n_distinct_bw"],
            "bw_spread": st["bw_max"] - st["bw_min"],
            "bw_cv": st["bw_cv"],
            "bw_iqr": st["bw_iqr"],
        })
        if st["n_distinct_bw"] <= 1:
            zero_var += 1
        else:
            multi_var += 1

    per_path = os.path.join(SUMMARY_DIR, "drmaciver_per_instance_summary.csv")
    var_path = os.path.join(SUMMARY_DIR, "drmaciver_variability_summary.csv")
    with open(per_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(per_rows[0].keys()) if per_rows else ["instance_id"])
        w.writeheader()
        w.writerows(per_rows)
    with open(var_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["instance_id", "n_distinct_bw", "bw_spread", "bw_cv", "bw_iqr"])
        w.writeheader()
        w.writerows(sorted(var_rows, key=lambda x: -x["bw_spread"]))

    var_sorted = sorted(var_rows, key=lambda x: -x["bw_spread"])
    concl_path = os.path.join(SUMMARY_DIR, "drmaciver_phase_conclusions.md")
    with open(concl_path, "w") as f:
        f.write("# EXP10 DRMacIver Phase Conclusions\n\n")
        f.write(f"**Production records analyzed:** {len(records)}\n")
        f.write(f"**Instances with data:** {len(per_rows)}/93\n\n")
        f.write(f"## Variability\n\n")
        f.write(f"- Zero objective variance: {zero_var}/{len(per_rows)} instances\n")
        f.write(f"- Two or more distinct values: {multi_var}/{len(per_rows)} instances\n\n")
        f.write("### Top 10 by BW spread\n\n")
        for v in var_sorted[:10]:
            f.write(f"- {v['instance_id']}: spread={v['bw_spread']:.4f}, "
                    f"distinct={v['n_distinct_bw']}, CV={v['bw_cv']:.6f}\n")
        f.write("\n## Stochastic initialization\n\n")
        pids_all = set(r.get("pid") for r in records if r.get("pid"))
        f.write(f"- Total distinct PIDs across all runs: {len(pids_all)}\n")
        f.write("- 0.12s inter-launch gap enforced by runner\n")
        f.write("- Identical objectives may reflect convergence, not necessarily identical seeds\n")

    print(f"Wrote {per_path}, {var_path}, {concl_path}")
    print(f"Instances: {len(per_rows)}, zero-var={zero_var}, multi-var={multi_var}")


if __name__ == "__main__":
    main()
