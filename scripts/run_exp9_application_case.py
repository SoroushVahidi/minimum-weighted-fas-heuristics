#!/usr/bin/env python3
"""
EXP9: Application Case Study — Wikipedia Adminship Vote Network.

Runs LR-TA, WMSF, IPSNS, DRMacIver/FAS, igraph Eades, and Weighted Eades on
the prepared application instance(s). Uses subprocess calls to the existing
runner scripts for consistency with EXP4/EXP7. Does NOT modify EXP1b–EXP8.

Usage:
  python3 scripts/run_exp9_application_case.py          # full run
  python3 scripts/run_exp9_application_case.py --smoke  # top-10 smoke test
"""
import argparse
import csv
import json
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = REPO / "scripts"

CONFIG_CSV = REPO / "experiments/exp9_application_case/config/application_instances.csv"
OUT_DIR = REPO / "experiments/exp9_application_case"
SUMMARY_PATH = OUT_DIR / "summary/exp9_raw_summary.csv"
LOG_PATH = OUT_DIR / "logs/exp9_tmux.log"
RANKINGS_DIR = OUT_DIR / "rankings"

SUMMARY_COLS = [
    "instance", "dataset", "top_n", "n", "m", "density", "total_weight",
    "algorithm", "backward_weight", "runtime_seconds", "status", "error",
]

IPSNS_ITERS = 400

PY = sys.executable


def _parse_bw(stdout: str) -> float | None:
    """Extract backward weight from algorithm stdout."""
    for pattern in [
        r"Backward Weight[:\s]+([0-9.eE+\-]+)",
        r"backward_weight[:\s]+([0-9.eE+\-]+)",
        r'"backward_weight":\s*([0-9.eE+\-]+)',
    ]:
        m = re.search(pattern, stdout, re.IGNORECASE)
        if m:
            return float(m.group(1))
    return None


def _parse_json_bw(stdout: str) -> float | None:
    """Try to parse JSON from stdout and extract backward_weight."""
    # Search for last JSON object in stdout
    for chunk in reversed(re.findall(r'\{[^{}]+\}', stdout, re.DOTALL)):
        try:
            d = json.loads(chunk)
            if "backward_weight" in d:
                return float(d["backward_weight"])
        except json.JSONDecodeError:
            pass
    return None


def run_algorithm(alg_name: str, cmd: list[str]) -> tuple[float, float, str]:
    """Run algorithm subprocess; return (bw, runtime, status)."""
    t0 = time.perf_counter()
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=600
        )
        rt = time.perf_counter() - t0
        stdout = result.stdout + result.stderr

        if result.returncode != 0 and "solver_unavailable" not in stdout:
            return float("nan"), rt, f"exit_{result.returncode}: {result.stderr[:200]}"

        bw = _parse_bw(stdout) or _parse_json_bw(stdout)
        if bw is None:
            return float("nan"), rt, f"no_bw_found"
        return bw, rt, "ok"
    except subprocess.TimeoutExpired:
        return float("nan"), time.perf_counter() - t0, "timeout"
    except Exception as exc:
        return float("nan"), time.perf_counter() - t0, f"error: {exc}"


def run_all_algorithms(row: dict) -> list[dict]:
    dimacs_path = Path(row["file_path"])
    n, m = int(row["n"]), int(row["m"])
    total_w = float(row["total_weight"])

    base = {
        "instance": row["instance"],
        "dataset": row["dataset"],
        "top_n": row["top_n"],
        "n": n, "m": m,
        "density": row["density"],
        "total_weight": total_w,
    }

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        algos = [
            ("LR-TA", [PY, str(SCRIPTS / "run_lrta.py"),
                       "--input", str(dimacs_path),
                       "--output", str(tmp / "lrta.csv")]),
            ("WMSF", [PY, str(SCRIPTS / "run_wmsf.py"),
                      "--input", str(dimacs_path),
                      "--output", str(tmp / "wmsf.csv")]),
            ("IPSNS", [PY, str(SCRIPTS / "run_ipsns.py"),
                       "--input", str(dimacs_path),
                       "--output", str(tmp / "ipsns.csv"),
                       "--iters", str(IPSNS_ITERS), "--log-every", "0"]),
            ("DRMacIver/FAS", [PY, str(SCRIPTS / "run_drmaciver_fas.py"),
                               "--input", str(dimacs_path)]),
            ("igraph_eades", [PY, str(SCRIPTS / "run_igraph_eades.py"),
                              "--input", str(dimacs_path)]),
            ("weighted_eades", [PY, str(SCRIPTS / "run_weighted_eades.py"),
                                "--input", str(dimacs_path)]),
        ]

        results = []
        for alg_name, cmd in algos:
            print(f"  Running {alg_name} …", flush=True)
            bw, rt, status = run_algorithm(alg_name, cmd)
            bw_str = f"{bw:.4f}" if bw == bw else ""
            print(f"    BW={bw_str}  rt={rt:.3f}s  [{status}]")
            results.append({
                **base,
                "algorithm": alg_name,
                "backward_weight": bw_str,
                "runtime_seconds": round(rt, 4),
                "status": "ok" if status == "ok" else status,
                "error": "" if status == "ok" else status,
            })

    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true",
                    help="Run only the smoke-test (top-10) instance")
    args = ap.parse_args()

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    RANKINGS_DIR.mkdir(parents=True, exist_ok=True)

    if not CONFIG_CSV.exists():
        print(f"Config CSV not found: {CONFIG_CSV}")
        print("Run scripts/prepare_exp9_application_case.py first.")
        sys.exit(1)

    with CONFIG_CSV.open() as f:
        instances = list(csv.DictReader(f))

    if args.smoke:
        instances = [r for r in instances if r.get("smoke", "").lower() in ("true", "1")]
        if not instances:
            instances = instances[:1]
        print("=== EXP9 SMOKE TEST ===")
    else:
        instances = [r for r in instances if r.get("smoke", "").lower() not in ("true", "1")]
        print("=== EXP9 FULL RUN ===")

    all_results = []
    for row in instances:
        if row.get("file_found", "").lower() != "true":
            print(f"Instance file not found: {row['file_path']} — skipping")
            continue
        print(f"\n[{row['instance']}] n={row['n']} m={row['m']} density={row['density']}")
        results = run_all_algorithms(row)
        all_results.extend(results)

    with SUMMARY_PATH.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=SUMMARY_COLS)
        writer.writeheader()
        writer.writerows(all_results)

    print(f"\nWrote {len(all_results)} rows to {SUMMARY_PATH}")


if __name__ == "__main__":
    main()
