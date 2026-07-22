# Cost-Aware Routing of Large Language Models

**Overview:** AAI-501 final project (USD MS in Applied AI, solo, Michael Valderrama). The project predicts the cheapest capable LLM for each request, a cost-aware routing layer built and evaluated on the LLMRouterBench Performance-Cost benchmark.

**Dataset**

- LLMRouterBench (Findings of ACL 2026): [paper](https://arxiv.org/abs/2601.07206), [GitHub](https://github.com/ynulihao/LLMRouterBench), [Hugging Face](https://huggingface.co/datasets/NPULH/LLMRouterBench)
- Performance-Cost setting: 10 datasets, 13 flagship models, 12,166 fully covered prompts, one record per (prompt, model) with tokens, dollar cost, and score
- Raw data is not committed. Download `bench-release.tar.gz` from the Hugging Face link into `data/raw/` and extract, then run the loader below.

**Repo layout**

| Path | What it holds |
|------|---------------|
| `src/load_bench.py` | Flattens the bench-release JSONs into one tidy parquet (run with `--raw-dir` and `--out`) |
| `src/routing_label.py` | The routing label rule: cheapest model clearing the quality threshold |
| `notebooks/01_eda.ipynb` | EDA: cost and quality landscape of the 13-model pool |
| `notebooks/02_labels_and_baseline.ipynb` | Label construction, threshold sensitivity, baseline logistic router vs always-cheapest and always-strongest |
| `tests/` | Smoke tests for the label rule (run by CI) |
| `report/` | Report drafts for the final deliverable |

**Reproduce**

```
python3.13 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python src/load_bench.py --raw-dir data/raw/bench-release --out data/processed/records_long.parquet
.venv/bin/jupyter nbconvert --to notebook --execute --inplace notebooks/01_eda.ipynb notebooks/02_labels_and_baseline.ipynb
```

**Baseline results so far** (test prompts, quality threshold 1.0)

| Strategy | Mean cost (USD) | Mean score |
|----------|-----------------|------------|
| Always cheapest | 0.0008 | 0.43 |
| Always strongest | 0.0615 | 0.60 |
| Logistic router | 0.0115 | 0.56 |
| Oracle label | 0.0055 | 0.82 |

**Planning docs** from the proposal phase live in the repo root (`Project_Breakdown_Milestones.md`, `Final_Team_Project_Plan.md`, proposal PDFs).
