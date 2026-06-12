#!/usr/bin/env python3
"""
Wait for DRMacIver production phase to reach 1860/1860, then validate and finalize EXP10.

Usage:
  python3 scripts/wait_and_finalize_exp10.py [--poll-seconds 60]
"""
import argparse
import os
import subprocess
import sys
import time

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
EXP_DIR = os.path.join(REPO_ROOT, "experiments", "exp10_stochastic_robustness")
SCRIPTS = os.path.join(EXP_DIR, "scripts")
CKPT_DIR = os.path.join(EXP_DIR, "checkpoints")
LOG = os.path.join(EXP_DIR, "logs", "wait_and_finalize.log")
EXPECTED = 1860


def log(msg):
    line = f"[{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}] {msg}"
    print(line, flush=True)
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def count_done():
    return len([f for f in os.listdir(CKPT_DIR)
                if f.startswith("drmaciver_") and f.endswith(".done")])


def runner_active():
    r = subprocess.run(["pgrep", "-f", "run_drmaciver_repetitions.py"],
                       capture_output=True, text=True)
    return bool(r.stdout.strip())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--poll-seconds", type=int, default=60)
    parser.add_argument("--skip-wait", action="store_true")
    args = parser.parse_args()

    if not args.skip_wait:
        log("Waiting for DRMacIver production 1860/1860...")
        while True:
            n = count_done()
            active = runner_active()
            log(f"Progress: {n}/{EXPECTED}  runner_active={active}")
            if n >= EXPECTED:
                log("Production phase complete.")
                break
            if not active and n < EXPECTED:
                log(f"Runner exited at {n}/{EXPECTED}; resuming...")
                subprocess.run(
                    [sys.executable, os.path.join(SCRIPTS, "run_drmaciver_repetitions.py")],
                    cwd=REPO_ROOT,
                    stdout=open(os.path.join(EXP_DIR, "logs", "drmaciver_full_run.log"), "a"),
                    stderr=subprocess.STDOUT,
                )
                time.sleep(5)
                continue
            time.sleep(args.poll_seconds)

    steps = [
        ("validate_drmaciver_runs.py", []),
        ("summarize_drmaciver_phase.py", []),
        ("finalize_exp10.py", []),
    ]
    for script, extra in steps:
        path = os.path.join(SCRIPTS, script)
        if not os.path.isfile(path):
            log(f"SKIP missing {script}")
            continue
        log(f"Running {script}...")
        r = subprocess.run([sys.executable, path] + extra, cwd=REPO_ROOT)
        if r.returncode != 0:
            log(f"FAILED: {script} exit={r.returncode}")
            return r.returncode
    log("EXP10 wait-and-finalize complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
