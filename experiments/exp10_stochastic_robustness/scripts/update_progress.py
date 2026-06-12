"""
EXP10: Update experiment_progress.json dashboard.
When COMPLETED.ok exists and both phases are 100%, status is COMPLETE (frozen).
"""
import json, os, subprocess, datetime, glob

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
EXP_DIR = os.path.join(REPO_ROOT, "experiments", "exp10_stochastic_robustness")
CKPT_DIR = os.path.join(EXP_DIR, "checkpoints")
SUMMARY_DIR = os.path.join(EXP_DIR, "summary")

SMOKE_ARCHIVE_CKPT = os.path.join(EXP_DIR, "smoke_archive", "drmaciver", "checkpoints")


def count_done(prefix, total):
    n = len([f for f in os.listdir(CKPT_DIR) if f.startswith(prefix) and f.endswith(".done")])
    return n, total


def count_smoke_archived(prefix):
    if not os.path.isdir(SMOKE_ARCHIVE_CKPT):
        return 0
    return len([f for f in os.listdir(SMOKE_ARCHIVE_CKPT) if f.startswith(prefix) and f.endswith(".done")])

def active_pids():
    try:
        r = subprocess.run(["pgrep", "-f", "run_ipsns_repetitions|run_drmaciver_repetitions"],
                           capture_output=True, text=True)
        return [int(p) for p in r.stdout.strip().split() if p]
    except Exception:
        return []

def get_log_tail(log_path, n=3):
    if not os.path.exists(log_path):
        return []
    lines = []
    with open(log_path) as f:
        for line in f:
            lines.append(line.rstrip())
    return lines[-n:]

os.makedirs(SUMMARY_DIR, exist_ok=True)

ipsns_done, ipsns_total = count_done("ipsns_", 1860)
dr_done, dr_total = count_done("drmaciver_", 1860)
dr_smoke_archived = count_smoke_archived("drmaciver_")
pids = active_pids()

ipsns_log = os.path.join(EXP_DIR, "logs", "ipsns_full_run.log")
dr_log = os.path.join(EXP_DIR, "logs", "drmaciver_runner.log")

completed_ok = os.path.exists(os.path.join(SUMMARY_DIR, "COMPLETED.ok"))
ipsns_complete = ipsns_done == ipsns_total and ipsns_total > 0
dr_complete = dr_done == dr_total and dr_total > 0
final_status = "COMPLETE" if completed_ok and ipsns_complete and dr_complete and not pids else "NONFINAL"

# Preserve timestamp when experiment is finalized (avoid noisy diffs on dashboard reads).
progress_path = os.path.join(SUMMARY_DIR, "experiment_progress.json")
prev_ts = None
if final_status == "COMPLETE" and os.path.exists(progress_path):
    try:
        with open(progress_path) as pf:
            prev_ts = json.load(pf).get("timestamp")
    except Exception:
        prev_ts = None
timestamp = prev_ts or datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

progress = {
    "timestamp": timestamp,
    "status": final_status,
    "ipsns_phase": {
        "done": ipsns_done, "total": ipsns_total,
        "pct": round(100 * ipsns_done / ipsns_total, 1),
        "complete": ipsns_done == ipsns_total,
        "log_tail": get_log_tail(ipsns_log),
    },
    "drmaciver_phase": {
        "done": dr_done, "total": dr_total,
        "pct": round(100 * dr_done / dr_total, 1) if dr_total else 0.0,
        "complete": dr_done == dr_total,
        "log_tail": get_log_tail(dr_log),
        "note": "production namespace only; smoke archive excluded",
    },
    "drmaciver_smoke_archive": {
        "archived_checkpoints": dr_smoke_archived,
        "note": "preflight/smoke outputs quarantined from production namespace",
    },
    "drmaciver_prior_contamination_corrected": {
        "prior_reported_done": 9,
        "corrected_at": "2026-06-12T03:35:42Z",
        "reason": "9 smoke checkpoints were previously counted in production namespace",
    },
    "active_pids": pids,
    "validation_done": os.path.exists(os.path.join(SUMMARY_DIR, "ipsns_validation_summary.json")),
    "summaries_done": os.path.exists(os.path.join(SUMMARY_DIR, "ipsns_phase_conclusions.md")),
    "preflight_done": os.path.exists(os.path.join(SUMMARY_DIR, "drmaciver_preflight_report.md")),
    "completed_ok": completed_ok,
}

out = progress_path
with open(out, "w") as f:
    json.dump(progress, f, indent=2)

print(f"IPSNS:     {ipsns_done}/{ipsns_total} ({progress['ipsns_phase']['pct']}%)"
      f"  {'COMPLETE' if ipsns_done==ipsns_total else 'in progress'}")
print(f"DRMacIver: {dr_done}/{dr_total} ({progress['drmaciver_phase']['pct']}%)"
      f"  {'COMPLETE' if dr_done==dr_total else 'not started' if dr_done==0 else 'in progress'}")
print(f"Active PIDs: {pids}")
print(f"Written: {out}")
