"""Extract the raw query text for every prompt in the Performance-Cost pool.

The tidy long table keeps only a hash and length of each query (the text itself
is bulky and identical across models). The LLM-as-router experiment needs the
actual text, so this script walks the same files as load_bench.py and writes one
row per prompt_id with its origin_query, taken from the first run file that
covers it.

Usage:
    python src/extract_queries.py --raw-dir data/raw/bench-release --out data/processed/queries.parquet
"""

import argparse
import json
from pathlib import Path

import pandas as pd

from load_bench import COST_DATASETS, FLAGSHIP_MODELS, SPLITS


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--raw-dir", required=True,
                        help="Path to the extracted bench-release folder")
    parser.add_argument("--out", required=True,
                        help="Output parquet path (prompt_id, query)")
    args = parser.parse_args()

    raw_dir = Path(args.raw_dir)
    queries = {}
    for ds in COST_DATASETS:
        for path in sorted((raw_dir / ds).rglob("*.json")):
            with open(path) as f:
                run = json.load(f)
            if run.get("demo", False):
                continue
            if (run["dataset_name"] not in COST_DATASETS
                    or run["split"] not in SPLITS
                    or run["model_name"] not in FLAGSHIP_MODELS):
                continue
            for rec in run["records"]:
                pid = f"{run['dataset_name']}:{rec['index']}"
                if pid not in queries:
                    queries[pid] = rec.get("origin_query") or ""

    df = pd.DataFrame({"prompt_id": list(queries), "query": list(queries.values())})
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(out, index=False)
    print(f"wrote {len(df):,} queries to {out}")


if __name__ == "__main__":
    main()
