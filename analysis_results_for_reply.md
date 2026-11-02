# Follow-up analyses for the professor reply

All numbers are on the same 2,434 held-out test prompts used in the report, same split (random_state=42, test_size=0.2, stratified by dataset). Costs are mean USD per prompt to 4 decimals, quality is mean recorded score to 3 decimals. Nothing here calls an API; it all replays the recorded benchmark data.

Sanity check on the port: at threshold 1.0 this script reproduces the graded notebooks exactly (logistic 0.0115 / 0.564, forest 0.0073 / 0.535, regressor 0.0006 / 0.513, fixed qwen 0.0009 / 0.538, oracle 0.0055 / 0.821).

## 1. Threshold sweep

The routing label is the cheapest model whose recorded score clears a threshold. The report uses 1.0, notebook 07 also checked 0.5. I swept 0.5, 0.6, 0.7, 0.8, 0.9, 1.0. The logistic and forest routers were retrained at every threshold. The cost regressor was trained once (it never sees the label), but its capability screen was rebuilt at each threshold, which is the part of that router the threshold actually touches. Fixed qwen does not depend on the threshold at all, so it is a constant reference line.

| threshold | label change vs ref | logistic cost | logistic quality | forest cost | forest quality | regressor cost | regressor quality | fixed qwen cost | fixed qwen quality | oracle cost | oracle quality |
|-----------|---------------------|---------------|------------------|-------------|----------------|----------------|-------------------|-----------------|--------------------|-------------|----------------|
| 0.5       | 2.1%                | 0.0115        | 0.564            | 0.0070      | 0.534          | 0.0006         | 0.508             | 0.0009          | 0.538              | 0.0055      | 0.813          |
| 0.6       | 0.0%                | 0.0115        | 0.564            | 0.0073      | 0.535          | 0.0006         | 0.513             | 0.0009          | 0.538              | 0.0055      | 0.821          |
| 0.7       | 0.0%                | 0.0115        | 0.564            | 0.0073      | 0.535          | 0.0006         | 0.513             | 0.0009          | 0.538              | 0.0055      | 0.821          |
| 0.8       | 0.0%                | 0.0115        | 0.564            | 0.0073      | 0.535          | 0.0006         | 0.513             | 0.0009          | 0.538              | 0.0055      | 0.821          |
| 0.9       | 0.0%                | 0.0115        | 0.564            | 0.0073      | 0.535          | 0.0006         | 0.513             | 0.0009          | 0.538              | 0.0055      | 0.821          |
| 1.0       | 0.0%                | 0.0115        | 0.564            | 0.0073      | 0.535          | 0.0006         | 0.513             | 0.0009          | 0.538              | 0.0055      | 0.821          |

**Read the sweep with this caveat first.** The recorded scores only ever take the values 0, 0.5, 1, and the fractional ones come from arenahard alone. Any threshold above 0.5 therefore selects the same set of capable models. Across the 6 thresholds swept, the label rule produced only **2 distinct label sets**, not 6. So this is a two-point check dressed as a sweep, and it is the same two points notebook 07 already reported. The extra rows are confirmation that nothing hides between them, not independent evidence.

Ranking by quality (best first):

- 0.5: logistic > fixed qwen > forest > regressor
- 0.6: logistic > fixed qwen > forest > regressor
- 0.7: logistic > fixed qwen > forest > regressor
- 0.8: logistic > fixed qwen > forest > regressor
- 0.9: logistic > fixed qwen > forest > regressor
- 1.0: logistic > fixed qwen > forest > regressor

Ranking by cost (cheapest first):

- 0.5: regressor < fixed qwen < forest < logistic
- 0.6: regressor < fixed qwen < forest < logistic
- 0.7: regressor < fixed qwen < forest < logistic
- 0.8: regressor < fixed qwen < forest < logistic
- 0.9: regressor < fixed qwen < forest < logistic
- 1.0: regressor < fixed qwen < forest < logistic

**Takeaway.** No ranking flips. The quality order and the cost order of the four strategies are identical at every threshold, and the largest movement in any single number across the whole sweep is 0.009 in quality. Given the caveat above, the honest claim is narrow: the conclusion is insensitive to the threshold because the data is close to binary, not because the sweep explored a wide space.

## 2. Classifier and regressor agreement

The two routers pick the same model on **62.1%** of test prompts, Cohen's kappa **0.281**. The gap between those two numbers is the whole story: both routers default to the same cheap model, so most of the raw agreement is what chance alone would produce.

| category      | prompts | agreement |
|---------------|---------|-----------|
| aime          | 12      | 0.0%      |
| hle           | 432     | 0.0%      |
| livecodebench | 211     | 0.0%      |
| swe-bench     | 100     | 0.0%      |
| livemathbench | 24      | 8.3%      |
| mmlupro       | 600     | 78.5%     |
| arenahard     | 150     | 91.3%     |
| gpqa          | 40      | 97.5%     |
| simpleqa      | 865     | 99.7%     |

Restricted to the 923 prompts where at least one router leaves qwen3-235b-a22b-2507, agreement is **0.0%**.

That 0% is not a rounding artifact. Every single prompt the two routers agree on is a prompt where both chose qwen3-235b-a22b-2507; there are **0 prompts** in the test set where they agree on any other model. The classifier and the capability-screened regressor share a default and share nothing else.

**Takeaway.** The categories where they diverge completely are aime (0.0%), hle (0.0%), livecodebench (0.0%). Those are the escalation categories, which answers the question directly: the overlap is concentrated entirely on the easy traffic, and on every prompt where routing has something to decide the two approaches disagree. They are not redundant.

## 3. Qwen price break-even

The multiplier m scales the per-token prices of `qwen3-235b-a22b-2507`. Recorded cost is linear in the per-token prices, so scaling both prices by m scales that model's recorded cost by exactly m. No re-pricing from raw tokens is needed.

One correction to the framing before the numbers: the logistic router sends **72.8%** of test traffic to qwen3-235b-a22b-2507, not the ~95% in the brief. The two cost curves are therefore not locked together, and a short-run crossover does exist.

### Short run (routing decisions held fixed)

| multiplier m | fixed qwen cost | router cost | router premium | router cheaper |
|--------------|-----------------|-------------|----------------|----------------|
| 1            | 0.0009          | 0.0115      | 0.0107         | no             |
| 1.5          | 0.0013          | 0.0117      | 0.0104         | no             |
| 2            | 0.0017          | 0.0119      | 0.0101         | no             |
| 3            | 0.0026          | 0.0122      | 0.0096         | no             |
| 5            | 0.0043          | 0.0128      | 0.0085         | no             |
| 10           | 0.0087          | 0.0145      | 0.0058         | no             |

Router mean cost is linear in m: 0.011188 + 0.000332m. Fixed qwen is 0.000869m (6 decimals here so the crossover below reproduces; rounding these to 4 does not). The router's intercept is large because the traffic it sends elsewhere is expensive, and its slope is small because only 72.8% of its traffic is exposed to the price change.

They cross at **m = 20.85**. At or above roughly a 21x qwen price increase the router is both cheaper than fixed qwen and higher quality (0.564 vs 0.538), so the quality edge becomes free. Below that it is still a premium, and none of the multipliers the brief asked about reach it.

### Long run (relabel and retrain under the new prices)

| multiplier m | retrained router cost | retrained router quality | fixed qwen cost | fixed qwen quality | oracle cost | oracle quality | baseline share of traffic |
|--------------|-----------------------|--------------------------|-----------------|--------------------|-------------|----------------|---------------------------|
| 2            | 0.0116                | 0.561                    | 0.0017          | 0.538              | 0.0056      | 0.821          | 37.2%                     |
| 5            | 0.0117                | 0.480                    | 0.0043          | 0.538              | 0.0057      | 0.821          | 0.0%                      |

Traffic at m = 2 (top 3):

- qwen3-235b-a22b-2507: 37.2%
- deepseek-v3.1-terminus: 28.2%
- gpt-5: 17.7%

Traffic at m = 5 (top 3):

- gemini-2.5-flash: 44.2%
- deepseek-v3.1-terminus: 29.9%
- gpt-5: 17.7%

**Takeaway.** The label rule adapts cleanly: the oracle column shows where the money should go, and the traffic lists show it leaving qwen3-235b-a22b-2507 entirely by m = 5. The trained router does not capture that adaptation. Its cost barely moves after retraining and stays well above fixed qwen at every multiplier tested, and at the top multiplier its quality falls below fixed qwen too. So the retrain-as-hedge argument holds for the labeling rule but is not supported by this router at this accuracy. That is a limitation worth stating plainly rather than a result to lean on.
