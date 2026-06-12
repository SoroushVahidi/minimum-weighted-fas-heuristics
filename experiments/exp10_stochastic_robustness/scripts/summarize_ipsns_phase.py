"""
EXP10 Phase 4: IPSNS-only robustness summaries.

Reads all completed IPSNS run records and produces:
  summary/ipsns_per_instance_summary.csv    -- per-instance statistics across 20 seeds
  summary/ipsns_seed_improvement.csv        -- per (instance, seed) improvement data
  summary/ipsns_variability_summary.csv     -- variability ranking of instances
  summary/ipsns_phase_conclusions.md        -- written conclusions for manuscript preparation

Run after validate_ipsns_runs.py passes.
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
RAW_DIR = os.path.join(EXP_DIR, "raw", "ipsns")
SUMMARY_DIR = os.path.join(EXP_DIR, "summary")


def load_all_records():
    records = []
    for rp in sorted(glob.glob(os.path.join(RAW_DIR, "*.json"))):
        try:
            with open(rp) as f:
                rec = json.load(f)
            if rec.get("status") == "ok":
                records.append(rec)
        except Exception:
            pass
    return records


def percentile(sorted_vals, p):
    if not sorted_vals:
        return float("nan")
    n = len(sorted_vals)
    idx = (n - 1) * p / 100.0
    lo = int(idx)
    hi = lo + 1
    frac = idx - lo
    if hi >= n:
        return sorted_vals[-1]
    return sorted_vals[lo] + frac * (sorted_vals[hi] - sorted_vals[lo])


def cv(vals, mean):
    if mean == 0 or mean is None:
        return float("nan")
    std = math.sqrt(sum((v - mean) ** 2 for v in vals) / len(vals))
    return std / abs(mean)


def instance_stats(recs):
    bws = sorted(r["objective_bw"] for r in recs)
    n = len(bws)
    if n == 0:
        return {}

    mean_bw = sum(bws) / n
    variance = sum((v - mean_bw) ** 2 for v in bws) / n
    std_bw = math.sqrt(variance)
    q1 = percentile(bws, 25)
    median_bw = percentile(bws, 50)
    q3 = percentile(bws, 75)
    iqr_bw = q3 - q1
    min_bw = bws[0]
    max_bw = bws[-1]
    n_distinct = len(set(bws))
    coeff_var = cv(bws, mean_bw)

    # Improvement over selected seed
    seeds_improved = [r for r in recs if r.get("improved_over_seed")]
    n_improved = len(seeds_improved)
    improvements = [r["initial_incumbent_bw"] - r["objective_bw"] for r in seeds_improved]
    median_improvement = percentile(sorted(improvements), 50) if improvements else 0.0
    max_improvement = max(improvements) if improvements else 0.0

    # Fraction with zero accepted moves
    n_zero_accepted = sum(1 for r in recs if r.get("accepted_moves", 0) == 0)

    # Runtime stats
    runtimes = sorted(r["runtime_seconds"] for r in recs)
    median_rt = percentile(runtimes, 50)

    # Time to best
    t2b = sorted(r.get("time_to_best_seconds", 0.0) for r in recs)
    median_t2b = percentile(t2b, 50)

    # Accepted moves
    accepted = sorted(r.get("accepted_moves", 0) for r in recs)
    median_accepted = percentile(accepted, 50)

    # Best iteration
    best_iters = sorted(r.get("best_iteration", 0) for r in recs)
    median_best_iter = percentile(best_iters, 50)

    # Sample representative seed BW (use LR-TA seed bw as reference)
    seed_bw = recs[0].get("initial_incumbent_bw", float("nan"))  # should be same for all seeds

    return {
        "n_seeds": n,
        "min_bw": min_bw,
        "q1_bw": q1,
        "median_bw": median_bw,
        "mean_bw": mean_bw,
        "q3_bw": q3,
        "max_bw": max_bw,
        "std_bw": std_bw,
        "iqr_bw": iqr_bw,
        "cv_bw": coeff_var,
        "n_distinct_bw": n_distinct,
        "n_improved": n_improved,
        "pct_improved": 100.0 * n_improved / n,
        "median_improvement": median_improvement,
        "max_improvement": max_improvement,
        "n_zero_accepted": n_zero_accepted,
        "pct_zero_accepted": 100.0 * n_zero_accepted / n,
        "median_runtime": median_rt,
        "median_time_to_best": median_t2b,
        "median_accepted_moves": median_accepted,
        "median_best_iteration": median_best_iter,
        "incumbent_bw_at_start": seed_bw,
    }


def fmt(v, decimals=4):
    if isinstance(v, float) and math.isnan(v):
        return ""
    if isinstance(v, float):
        return f"{v:.{decimals}f}"
    return str(v)


def main():
    os.makedirs(SUMMARY_DIR, exist_ok=True)

    records = load_all_records()
    print(f"Loaded {len(records)} valid IPSNS records")

    # Group by instance
    by_inst = defaultdict(list)
    for r in records:
        by_inst[r["instance_id"]].append(r)

    # --- ipsns_per_instance_summary.csv ---
    per_inst_rows = []
    for inst_id in sorted(by_inst.keys()):
        recs = by_inst[inst_id]
        stats = instance_stats(recs)
        if not stats:
            continue
        row = {"instance_id": inst_id, "n": recs[0].get("n", ""), "m": recs[0].get("m", "")}
        row.update(stats)
        per_inst_rows.append(row)

    per_inst_fields = [
        "instance_id", "n", "m",
        "n_seeds", "min_bw", "q1_bw", "median_bw", "mean_bw", "q3_bw", "max_bw",
        "std_bw", "iqr_bw", "cv_bw", "n_distinct_bw",
        "n_improved", "pct_improved", "median_improvement", "max_improvement",
        "n_zero_accepted", "pct_zero_accepted",
        "median_runtime", "median_time_to_best",
        "median_accepted_moves", "median_best_iteration",
        "incumbent_bw_at_start",
    ]
    per_inst_path = os.path.join(SUMMARY_DIR, "ipsns_per_instance_summary.csv")
    with open(per_inst_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=per_inst_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(per_inst_rows)
    print(f"Wrote: {per_inst_path}")

    # --- ipsns_seed_improvement.csv ---
    seed_rows = []
    for r in sorted(records, key=lambda x: (x["instance_id"], x["seed"])):
        seed_rows.append({
            "instance_id": r["instance_id"],
            "seed": r["seed"],
            "objective_bw": r["objective_bw"],
            "lr_seed_bw": r["lr_seed_bw"],
            "wmsf_seed_bw": r["wmsf_seed_bw"],
            "initial_incumbent_bw": r["initial_incumbent_bw"],
            "improved_over_seed": r.get("improved_over_seed", False),
            "improvement_abs": r["initial_incumbent_bw"] - r["objective_bw"],
            "improvement_pct": 100.0 * (r["initial_incumbent_bw"] - r["objective_bw"]) / r["initial_incumbent_bw"] if r["initial_incumbent_bw"] > 0 else 0.0,
            "accepted_moves": r.get("accepted_moves", 0),
            "rejected_moves": r.get("rejected_moves", 0),
            "best_iteration": r.get("best_iteration", 0),
            "runtime_seconds": r.get("runtime_seconds", ""),
            "time_to_best_seconds": r.get("time_to_best_seconds", ""),
        })
    seed_path = os.path.join(SUMMARY_DIR, "ipsns_seed_improvement.csv")
    seed_fields = [
        "instance_id", "seed", "objective_bw", "lr_seed_bw", "wmsf_seed_bw",
        "initial_incumbent_bw", "improved_over_seed", "improvement_abs",
        "improvement_pct", "accepted_moves", "rejected_moves",
        "best_iteration", "runtime_seconds", "time_to_best_seconds",
    ]
    with open(seed_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=seed_fields)
        writer.writeheader()
        writer.writerows(seed_rows)
    print(f"Wrote: {seed_path}")

    # --- ipsns_variability_summary.csv ---
    var_rows = sorted(per_inst_rows, key=lambda r: -r.get("cv_bw", 0) if not (isinstance(r.get("cv_bw"), float) and math.isnan(r.get("cv_bw", 0))) else 0)
    var_fields = ["instance_id", "n", "cv_bw", "std_bw", "iqr_bw", "n_distinct_bw", "pct_improved", "pct_zero_accepted", "min_bw", "max_bw", "median_bw"]
    var_path = os.path.join(SUMMARY_DIR, "ipsns_variability_summary.csv")
    with open(var_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=var_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(var_rows)
    print(f"Wrote: {var_path}")

    # --- Aggregate statistics for conclusions ---
    all_bws_by_inst = {inst: sorted(r["objective_bw"] for r in recs) for inst, recs in by_inst.items()}
    total_runs = len(records)
    total_improved = sum(1 for r in records if r.get("improved_over_seed"))
    pct_improved_global = 100.0 * total_improved / total_runs

    # Compare each run's BW to EXP4 seed=0 result (which was the original single-run result)
    # We use seed=0 as the proxy for the EXP4 result since EXP4 used a fixed seed
    seed0_by_inst = {r["instance_id"]: r["objective_bw"] for r in records if r["seed"] == 0}
    # Best BW across all seeds per instance
    best_per_inst = {inst: min(bws) for inst, bws in all_bws_by_inst.items()}
    # How often is seed=0 at the best?
    seed0_at_best = sum(1 for inst in seed0_by_inst if abs(seed0_by_inst[inst] - best_per_inst.get(inst, float("inf"))) < 1e-9)
    # Instances where different seeds give different results
    high_variability = [inst for inst, bws in all_bws_by_inst.items() if len(set(bws)) > 1]
    # CV
    cvs = [r.get("cv_bw", 0) for r in per_inst_rows if not (isinstance(r.get("cv_bw"), float) and math.isnan(r.get("cv_bw", 0)))]
    mean_cv = sum(cvs) / len(cvs) if cvs else 0

    # Budget analysis: what fraction of instances have best_iteration < 400?
    # (if median_best_iteration << 400, budget is excess)
    early_convergence = [r for r in per_inst_rows if r.get("median_best_iteration", 400) < 200]
    late_convergence = [r for r in per_inst_rows if r.get("median_best_iteration", 0) >= 350]

    # Instances where seed=0 is WORSE than median
    seed0_vs_median = {}
    for inst in seed0_by_inst:
        if inst in all_bws_by_inst:
            bws = all_bws_by_inst[inst]
            med = percentile(sorted(bws), 50)
            seed0_vs_median[inst] = seed0_by_inst[inst] - med

    seed0_worse = {inst: diff for inst, diff in seed0_vs_median.items() if diff > 1e-9}
    seed0_better = {inst: diff for inst, diff in seed0_vs_median.items() if diff < -1e-9}

    n_inst = len(by_inst)
    n_fully_done = sum(1 for inst, recs in by_inst.items() if len(recs) == 20)

    # Write conclusions
    conclusions_path = os.path.join(SUMMARY_DIR, "ipsns_phase_conclusions.md")
    with open(conclusions_path, "w") as f:
        f.write(f"# EXP10 IPSNS Phase Conclusions\n")
        f.write(f"**Generated:** {__import__('datetime').datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')}\n")
        f.write(f"**Instances with all 20 seeds:** {n_fully_done}/{n_inst}\n")
        f.write(f"**Total valid runs analyzed:** {total_runs}\n\n")
        f.write(f"---\n\n")

        f.write(f"## 1. Is IPSNS low variance or high variance?\n\n")
        f.write(f"**Across-seed variability:** {len(high_variability)}/{n_inst} instances ({100*len(high_variability)/n_inst:.1f}%) produce at least two distinct BW values across 20 seeds.\n")
        f.write(f"**Mean CV across instances:** {mean_cv:.6f}\n")
        if mean_cv < 0.01:
            f.write(f"**Conclusion: IPSNS is LOW VARIANCE.** The coefficient of variation is below 1% on average, indicating highly consistent results across different random seeds.\n\n")
        elif mean_cv < 0.05:
            f.write(f"**Conclusion: IPSNS is MODERATE VARIANCE.** CV is modest (< 5%), indicating broadly consistent but occasionally variable results.\n\n")
        else:
            f.write(f"**Conclusion: IPSNS shows notable cross-seed variance on some instances.** CV > 5% on average.\n\n")

        f.write(f"## 2. How frequently does IPSNS improve the seed?\n\n")
        f.write(f"- Global improvement rate: {total_improved}/{total_runs} runs ({pct_improved_global:.2f}%) improved strictly over the initial incumbent\n")
        f.write(f"- Instances where ≥1 seed improved: {len([inst for inst, recs in by_inst.items() if any(r.get('improved_over_seed') for r in recs)])}/{n_inst}\n\n")

        f.write(f"## 3. Are 20 seeds producing materially different solutions?\n\n")
        f.write(f"- {len(high_variability)} instances ({100*len(high_variability)/n_inst:.1f}%) have non-constant BW across seeds\n")
        f.write(f"- {n_inst - len(high_variability)} instances are completely deterministic across seeds (all seeds return identical BW)\n\n")

        f.write(f"## 4. Is the original EXP4 seed (seed=0) typical, unusually strong, or unusually weak?\n\n")
        f.write(f"- seed=0 matches the best observed BW on {seed0_at_best}/{len(seed0_by_inst)} instances ({100*seed0_at_best/max(len(seed0_by_inst),1):.1f}%)\n")
        f.write(f"- Instances where seed=0 is WORSE than median: {len(seed0_worse)} ({list(seed0_worse.items())[:5]})\n")
        f.write(f"- Instances where seed=0 is BETTER than median: {len(seed0_better)}\n")
        if seed0_at_best / max(len(seed0_by_inst), 1) > 0.90:
            f.write(f"**Conclusion:** seed=0 is representative — it achieves the best result on ≥90% of instances.\n\n")
        else:
            f.write(f"**Conclusion:** seed=0 is NOT consistently the best; some instances benefit from other seeds.\n\n")

        f.write(f"## 5. Instances where seed choice materially changes the result\n\n")
        material_diff = [(inst, max(bws) - min(bws)) for inst, bws in all_bws_by_inst.items() if max(bws) - min(bws) > 1e-9]
        material_diff.sort(key=lambda x: -x[1])
        f.write(f"- {len(material_diff)} instances have any BW spread across seeds\n")
        f.write(f"- Top 10 by absolute BW spread:\n")
        for inst, spread in material_diff[:10]:
            bws = all_bws_by_inst[inst]
            f.write(f"  - {inst}: spread={spread:.1f} (min={min(bws):.1f}, max={max(bws):.1f}, med={percentile(sorted(bws),50):.1f})\n")
        f.write(f"\n")

        f.write(f"## 6. Is the 400-iteration budget fully used before best solution is found?\n\n")
        f.write(f"- {len(early_convergence)} instances have median best_iteration < 200 (budget likely excessive)\n")
        f.write(f"- {len(late_convergence)} instances have median best_iteration ≥ 350 (budget is binding)\n")
        f.write(f"- For instances with any improvement: median best_iteration shown in ipsns_per_instance_summary.csv\n\n")

        f.write(f"## 7. Pathological or unstable instances\n\n")
        high_cv_insts = [(r["instance_id"], r.get("cv_bw", 0)) for r in per_inst_rows
                         if not (isinstance(r.get("cv_bw"), float) and math.isnan(r.get("cv_bw", 0)))
                         and r.get("cv_bw", 0) > 0.02]
        high_cv_insts.sort(key=lambda x: -x[1])
        if high_cv_insts:
            f.write(f"Instances with CV > 2% (potentially unstable across seeds):\n")
            for inst, cv_val in high_cv_insts[:10]:
                f.write(f"  - {inst}: CV={cv_val:.4f}\n")
        else:
            f.write(f"No instances with CV > 2% — IPSNS is stable across all seeds.\n")
        f.write(f"\n")

        f.write(f"## 8. Notes for Manuscript\n\n")
        f.write(f"- These IPSNS-only conclusions do not yet reflect paired comparison with DRMacIver (EXP10 DRMacIver phase pending)\n")
        f.write(f"- EXP4 single-run result (seed=0 proxy) was {'representative' if seed0_at_best/max(len(seed0_by_inst),1) > 0.90 else 'not uniformly representative'}\n")
        f.write(f"- Recommended manuscript wording for robustness: to be finalized after paired DRMacIver analysis\n")

    print(f"Wrote: {conclusions_path}")
    print(f"\nSummary: {n_fully_done}/{n_inst} instances fully done. Analyzed {total_runs} runs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
