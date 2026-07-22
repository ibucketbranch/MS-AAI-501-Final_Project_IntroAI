# Results (draft)

Draft section for the final report. All numbers computed on the same 2,434 held-out test prompts (notebook 05).

## Strategy comparison

| Strategy | Mean cost (USD) | Mean score |
|----------|-----------------|------------|
| Regressor-derived router | 0.0006 | 0.513 |
| Always cheapest (deepseek-v3-0324) | 0.0008 | 0.429 |
| Best single value model (qwen3-235b-a22b-2507, fixed) | 0.0009 | 0.538 |
| Oracle label (ceiling) | 0.0055 | 0.822 |
| Random forest router (tuned) | 0.0073 | 0.536 |
| Logistic router (tuned) | 0.0115 | 0.564 |
| OpenRouter (reference) | 0.0225 | 0.495 |
| Always strongest (gemini-2.5-pro) | 0.0615 | 0.597 |

The results show a wide economic spread across strategies that all consume the identical traffic. The regressor-derived router produced the cheapest routing on the chart, under-cutting even the always-cheapest fixed model, because no single model is the cheapest on every prompt. The logistic router achieved the highest quality among the trained strategies (0.564), recovering 94 percent of the always-strongest score at 19 percent of its cost. The random forest router landed between them.

Two comparisons discipline these numbers. First, the fixed strategy of sending every prompt to qwen3-235b-a22b-2507 scored 0.538 at $0.0009, which dominates the tuned random forest router outright and out-scores the regressor-derived router. A router must beat the best single model to justify its existence, and on these features only the logistic router clears that bar on quality, at a price premium. Second, OpenRouter, the commercial reference shipped with the benchmark, was beaten on both cost and quality by all three trained strategies.

The oracle ceiling (0.822 at $0.0055) shows that near-perfect routing is not expensive; the difficulty is informational, not economic. The gap between the trained routers and the oracle is the cost of predicting from pre-call features alone.

## Threshold sensitivity

Rebuilding the labels at threshold 0.5 (accepting arenahard draws as capable) relabeled 2.1 percent of prompts. Retrained on those labels, the logistic router's test numbers did not move at the reported precision, the random forest shifted by $0.0003 and 0.002 score, and the oracle ceiling dipped from 0.822 to 0.813. No strategy ranking changed, so the threshold-1.0 results carry the report.

## Published context

The LLMRouterBench paper reports that its strongest baseline, Avengers-Pro, sits essentially on the Pareto frontier of the Performance-Cost setting (near-zero average Pareto distance), with top methods reaching up to a 4 percent performance gain over the best single model or a 31.7 percent cost saving at held accuracy. The paper also reports that several routers, including commercial ones, fail to outperform the best single model, a pattern this study reproduced independently: the trained routers here bought their cost savings by accepting a small quality discount against the best single model rather than beating it. Closing that final gap is what the published state of the art achieves with substantially heavier inputs (query embeddings and clustered model-expertise profiles) than the deliberately light pre-call feature set used here.

## Figures to carry into the final report

- Cost-vs-quality frontier with all strategies and every fixed model (notebook 05)
- Confusion matrix of the winning classifier, classes ordered cheap to expensive (notebook 03)
- Random forest feature importances (notebook 03)
- Model menu scatter and per-dataset score heatmap from the EDA (notebook 01)
