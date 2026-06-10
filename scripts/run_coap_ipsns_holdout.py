#!/usr/bin/env python3
"""Resumable COAP IPSNS tuning/holdout experiment driver."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import multiprocessing as mp
import os
import sys
import time
import traceback
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mwfas.evaluation import compute_forward_backward  # noqa: E402
from mwfas.ipsns import lns_merge_wmsf_lr_best_incumbent  # noqa: E402

DEFAULT_PLAN = REPO_ROOT / "experiments/coap_ipsns_holdout/config/holdout_plan.yaml"
DEFAULT_COMPLETION_DIR = REPO_ROOT / "logs/coap_ipsns_holdout"

REQUIRED_OK = (
    "run_key", "split", "instance", "config_id", "status", "final_bw",
    "best_seed_bw", "runtime", "iters", "rng_seed",
)


@dataclass(frozen=True)
class RunConfig:
    split: str
    instance: str
    file_path: str
    config_id: str
    iters: int
    topk_scc: int
    destroy_addback_frac: float
    destroy_remove_frac: float
    tol: float
    rng_seed: int
    wmsf_seed_mode: str
    seed_ordering: str
    scc_select_mode: str

    def run_key(self) -> str:
        payload = (
            f"{self.split}|{self.instance}|{self.config_id}|{self.iters}|"
            f"{self.topk_scc}|{self.destroy_addback_frac:.6g}|"
            f"{self.destroy_remove_frac:.6g}|{self.tol:.6g}|{self.rng_seed}|"
            f"{self.wmsf_seed_mode}|{self.scc_select_mode}"
        )
        digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]
        return f"{self.split}__{self.instance}__{self.config_id}__{digest}"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_plan(path: Path) -> dict[str, Any]:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_split_csv(path: Path, split: str) -> list[dict[str, str]]:
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["split"] = split
        if not Path(r["file_path"]).exists():
            raise FileNotFoundError(r["file_path"])
    return rows


def build_configs(plan: dict[str, Any]) -> list[RunConfig]:
    base = plan["baseline_params"]
    seeds = plan["rng_seeds"]
    instances = []
    for split_name, rel in plan["splits"].items():
        instances.extend(load_split_csv(REPO_ROOT / rel, split_name))

    configs: list[RunConfig] = []
    for inst in instances:
        for config_id, overrides in plan["candidate_configs"].items():
            params = {**base, **overrides}
            for seed in seeds:
                configs.append(
                    RunConfig(
                        split=inst["split"],
                        instance=inst["instance"],
                        file_path=inst["file_path"],
                        config_id=config_id,
                        iters=int(params["iters"]),
                        topk_scc=int(params.get("topk_scc", base["topk_scc"])),
                        destroy_addback_frac=float(params.get("destroy_addback_frac", base["destroy_addback_frac"])),
                        destroy_remove_frac=float(params.get("destroy_remove_frac", base["destroy_remove_frac"])),
                        tol=float(params["tol"]),
                        rng_seed=int(seed),
                        wmsf_seed_mode=str(params["wmsf_seed_mode"]),
                        seed_ordering=str(params["seed_ordering"]),
                        scc_select_mode=str(params["scc_select_mode"]),
                    )
                )
    configs.sort(key=lambda c: (c.split, c.instance, c.config_id, c.rng_seed))
    return configs


def is_valid_checkpoint(path: Path) -> bool:
    if not path.is_file():
        return False
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return False
    return d.get("status") == "ok" and all(k in d for k in REQUIRED_OK)


def append_jsonl(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, sort_keys=True) + "\n")
        f.flush()
        os.fsync(f.fileno())


def execute_run(cfg: RunConfig, ckpt_dir: Path, tmp_dir: Path) -> dict[str, Any]:
    started = utc_now()
    t0 = time.perf_counter()
    run_key = cfg.run_key()
    tmp_out = tmp_dir / f"{run_key}.csv"
    try:
        result = lns_merge_wmsf_lr_best_incumbent(
            dimacs_path=cfg.file_path,
            output_ranking_csv_path=str(tmp_out),
            seed_ordering=cfg.seed_ordering,
            iters=cfg.iters,
            topK_scc=cfg.topk_scc,
            destroy_addback_frac=cfg.destroy_addback_frac,
            destroy_remove_frac=cfg.destroy_remove_frac,
            tol=cfg.tol,
            rng_seed=cfg.rng_seed,
            log_every=0,
            wmsf_seed_mode=cfg.wmsf_seed_mode,
            scc_select_mode=cfg.scc_select_mode,
            return_info=True,
        )
        edges_indexed, node_to_index, _idx, scores, _F, info = result
        total_w, fw, bw = compute_forward_backward(edges_indexed, scores)
        runtime = time.perf_counter() - t0
        record = {
            **asdict(cfg),
            "run_key": run_key,
            "status": "ok",
            "started_at": started,
            "finished_at": utc_now(),
            "n": len(node_to_index),
            "m": len(edges_indexed),
            "total_weight": round(float(total_w), 6),
            "forward_weight": round(float(fw), 6),
            "final_bw": round(float(bw), 6),
            "best_seed_bw": round(float(info["best_seed_bw"]), 6),
            "lr_seed_bw": round(float(info["lr_seed_bw"]), 6),
            "wmsf_seed_bw": round(float(info["wmsf_seed_bw"]), 6),
            "improved_vs_seed": bool(info["improved"]),
            "n_iters_executed": int(info["n_iters"]),
            "runtime": round(runtime, 6),
            "error": "",
        }
        (ckpt_dir / f"{run_key}.json").write_text(
            json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        return record
    except Exception as exc:
        runtime = time.perf_counter() - t0
        record = {
            **asdict(cfg),
            "run_key": run_key,
            "status": "error",
            "started_at": started,
            "finished_at": utc_now(),
            "runtime": round(runtime, 6),
            "error": f"{type(exc).__name__}: {exc}",
            "traceback": traceback.format_exc(),
        }
        (ckpt_dir / f"{run_key}.FAILED.json").write_text(
            json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        return record


def _worker(args: tuple[RunConfig, str, str]) -> dict[str, Any]:
    cfg, ckpt, tmp = args
    return execute_run(cfg, Path(ckpt), Path(tmp))


def validate_all(configs: list[RunConfig], ckpt_dir: Path) -> tuple[int, int, int]:
    ok = fail = missing = 0
    for cfg in configs:
        key = cfg.run_key()
        if is_valid_checkpoint(ckpt_dir / f"{key}.json"):
            ok += 1
        elif (ckpt_dir / f"{key}.FAILED.json").exists():
            fail += 1
        else:
            missing += 1
    return ok, fail, missing


def write_completion(completion_dir: Path, configs: list[RunConfig], ckpt_dir: Path,
                     results_jsonl: Path, failures_jsonl: Path, started_at: str, skipped: int) -> None:
    completion_dir.mkdir(parents=True, exist_ok=True)
    ok, fail, missing = validate_all(configs, ckpt_dir)
    summary = {
        "experiment_id": "coap_ipsns_holdout",
        "expected_runs": len(configs),
        "completed_runs": ok,
        "skipped_resumed_runs": skipped,
        "failed_runs": fail,
        "missing_runs": missing,
        "started_at": started_at,
        "finished_at": utc_now(),
        "results_jsonl": str(results_jsonl),
        "failures_jsonl": str(failures_jsonl),
        "checkpoints_dir": str(ckpt_dir),
    }
    (completion_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    marker = completion_dir / "COMPLETED.ok"
    if missing or fail:
        if marker.exists():
            marker.unlink()
        print(f"[INCOMPLETE] ok={ok} fail={fail} missing={missing}", flush=True)
    else:
        marker.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
        print(f"[COMPLETE] {marker}", flush=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", type=Path, default=DEFAULT_PLAN)
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--pilot", action="store_true")
    ap.add_argument("--pilot-instances", type=int, default=2)
    ap.add_argument("--pilot-configs", type=int, default=2)
    ap.add_argument("--pilot-seeds", type=int, default=1)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--completion-marker-dir", type=Path, default=DEFAULT_COMPLETION_DIR)
    args = ap.parse_args()

    plan = load_plan(args.plan)
    configs = build_configs(plan)

    if args.pilot:
        inst_names = sorted({c.instance for c in configs})[: args.pilot_instances]
        cfg_ids = sorted({c.config_id for c in configs})[: args.pilot_configs]
        seeds = sorted(set(plan["rng_seeds"]))[: args.pilot_seeds]
        configs = [
            c for c in configs
            if c.instance in inst_names and c.config_id in cfg_ids and c.rng_seed in seeds
        ]

    out_root = REPO_ROOT / plan["output_root"]
    ckpt_dir = REPO_ROOT / plan["checkpoints_dir"]
    results_jsonl = REPO_ROOT / plan["results_jsonl"]
    failures_jsonl = REPO_ROOT / plan["failures_jsonl"]
    manifest_json = REPO_ROOT / plan["manifest_json"]
    tmp_dir = out_root / "tmp_rankings"
    for p in (ckpt_dir, results_jsonl.parent, tmp_dir):
        p.mkdir(parents=True, exist_ok=True)

    manifest_json.write_text(
        json.dumps({
            "generated_at": utc_now(),
            "n_runs": len(configs),
            "configs": [asdict(c) | {"run_key": c.run_key()} for c in configs],
        }, indent=2),
        encoding="utf-8",
    )

    pending = []
    skipped = 0
    for cfg in configs:
        if args.resume and is_valid_checkpoint(ckpt_dir / f"{cfg.run_key()}.json"):
            skipped += 1
            continue
        pending.append(cfg)

    print(f"Planned runs: {len(configs)} pending: {len(pending)} skipped: {skipped}", flush=True)
    if args.dry_run:
        return 0

    started_at = utc_now()
    full_configs = build_configs(plan) if args.pilot else configs
    if not pending:
        if not args.pilot:
            write_completion(
                args.completion_marker_dir, full_configs, ckpt_dir,
                results_jsonl, failures_jsonl, started_at, skipped,
            )
        return 0

    workers = max(1, args.workers)
    if workers == 1:
        for i, cfg in enumerate(pending, 1):
            rec = execute_run(cfg, ckpt_dir, tmp_dir)
            append_jsonl(results_jsonl if rec["status"] == "ok" else failures_jsonl, rec)
            print(f"[{i}/{len(pending)}] {cfg.instance} {cfg.config_id} seed={cfg.rng_seed} {rec['status']}", flush=True)
    else:
        ctx = mp.get_context("spawn")
        with ctx.Pool(workers) as pool:
            for i, rec in enumerate(
                pool.imap_unordered(_worker, [(c, str(ckpt_dir), str(tmp_dir)) for c in pending], 1),
                1,
            ):
                append_jsonl(results_jsonl if rec["status"] == "ok" else failures_jsonl, rec)
                print(f"[{i}/{len(pending)}] {rec.get('instance')} {rec.get('config_id')} {rec['status']}", flush=True)

    if not args.pilot:
        write_completion(
            args.completion_marker_dir, full_configs, ckpt_dir,
            results_jsonl, failures_jsonl, started_at, skipped,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
