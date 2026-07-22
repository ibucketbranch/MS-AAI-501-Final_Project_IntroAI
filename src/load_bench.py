"""Flatten the LLMRouterBench bench-release JSON files into one tidy long table.

Each source JSON holds one (dataset, split, model) run: a summary header plus a
records list with per-prompt tokens, cost, and score. This script walks the
extracted bench-release folder, keeps only the Performance-Cost setting that the
LLMRouterBench paper defines (10 datasets, 13 flagship models, specific splits,
see config/baseline_config_performance_cost.yaml in their repo), and writes one
row per (prompt, model) to a parquet file.

Usage:
    python src/load_bench.py --raw-dir data/raw/bench-release --out data/processed/records_long.parquet

I filter on the metadata fields inside each JSON (dataset_name, split,
model_name, demo) instead of trusting folder names, because the folder layout
is not consistent across datasets (arenahard nests differently, for example).
"""

import argparse
import hashlib
import json
from pathlib import Path

import pandas as pd

# The Performance-Cost setting from the LLMRouterBench repo,
# config/baseline_config_performance_cost.yaml. Fixed for this whole project so
# my results stay comparable to the paper's own baseline tables.
COST_DATASETS = [
    "aime",
    "livemathbench",
    "gpqa",
    "hle",
    "livecodebench",
    "mmlupro",
    "swe-bench",
    "simpleqa",
    "tau2",
    "arenahard",
]
FLAGSHIP_MODELS = [
    "claude-sonnet-4",
    "deepseek-v3-0324",
    "deepseek-v3.1-terminus",
    "deepseek-r1-0528",
    "gemini-2.5-flash",
    "gemini-2.5-pro",
    "gpt-5-chat",
    "gpt-5",
    "qwen3-235b-a22b-2507",
    "qwen3-235b-a22b-thinking-2507",
    "glm-4.6",
    "kimi-k2-0905",
    "intern-s1",
]
# openrouter is one of the paper's built-in routing baselines. I load it as a
# reference line for the comparison charts, never as a routing candidate.
REFERENCE_MODELS = ["openrouter"]
SPLITS = ["test", "hybrid", "v1", "test_3000", "verified"]


def load_run_file(path):
    """Read one run JSON and return its per-prompt rows, or [] if filtered out."""
    with open(path) as f:
        run = json.load(f)

    if run.get("demo", False):
        return []
    if run["dataset_name"] not in COST_DATASETS:
        return []
    if run["split"] not in SPLITS:
        return []
    model = run["model_name"]
    if model not in FLAGSHIP_MODELS + REFERENCE_MODELS:
        return []

    rows = []
    for rec in run["records"]:
        query = rec.get("origin_query") or ""
        rows.append(
            {
                "dataset": run["dataset_name"],
                "split": run["split"],
                "model": model,
                "is_reference": model in REFERENCE_MODELS,
                # prompt_id ties the same prompt together across models so the
                # train/test split later can go by prompt, not by row
                "prompt_id": f"{run['dataset_name']}:{rec['index']}",
                # short hash of the query text, used to verify that the same
                # index really is the same prompt across models
                "query_hash": hashlib.sha1(query.encode()).hexdigest()[:12],
                "query_chars": len(query),
                "prompt_tokens": rec["prompt_tokens"],
                "completion_tokens": rec["completion_tokens"],
                "cost": rec["cost"],
                "score": rec["score"],
            }
        )
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "--raw-dir",
        required=True,
        help="Path to the extracted bench-release folder",
    )
    parser.add_argument(
        "--out",
        required=True,
        help="Output parquet path for the tidy long table",
    )
    args = parser.parse_args()

    raw_dir = Path(args.raw_dir)
    if not raw_dir.is_dir():
        raise SystemExit(f"raw dir not found: {raw_dir}")

    rows = []
    files_kept = 0
    for ds in COST_DATASETS:
        for path in sorted((raw_dir / ds).rglob("*.json")):
            file_rows = load_run_file(path)
            if file_rows:
                files_kept += 1
                rows.extend(file_rows)

    df = pd.DataFrame(rows)
    print(f"kept {files_kept} run files -> {len(df):,} rows")
    print(df.groupby("dataset")["prompt_id"].nunique().rename("prompts"))

    # Sanity check: for one prompt_id, every model should have seen the same
    # query text. A mismatch would mean index does not line up across models.
    core = df[~df.is_reference]
    bad = (
        core.groupby("prompt_id")["query_hash"].nunique().gt(1).sum()
    )
    print(f"prompt_ids where the query text differs across models: {bad}")

    # A model can be missing a prompt (failed run, subset difference). The
    # label rule needs the full price menu per prompt, so report coverage.
    counts = core.groupby("prompt_id")["model"].nunique()
    n_models = core["model"].nunique()
    print(
        f"models in pool: {n_models}; prompts with all models present: "
        f"{(counts == n_models).sum():,} of {counts.size:,}"
    )

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(out, index=False)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
