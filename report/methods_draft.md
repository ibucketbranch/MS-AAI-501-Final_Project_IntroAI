# Methods (draft)

Draft section for the final report. Team/data-perspective academic voice. Numbers verified against notebooks 01-05 as of Jul 21.

## Data

The study used LLMRouterBench (Li et al., 2026), a routing benchmark that records how a shared pool of large language models answered the same prompts, with per-response token counts, dollar costs, and correctness scores. The analysis was restricted to the benchmark's Performance-Cost setting: 13 flagship models evaluated across 10 source datasets spanning mathematics, code, scientific reasoning, factual recall, and instruction following. Each record pairs one prompt with one model and carries the prompt and completion token counts, the dollar cost of the response, and a quality score. Nine of the ten datasets score responses as 0 or 1; arenahard also awards 0.5 for a draw against a reference answer.

The released files were flattened into a single long table of 173,688 (prompt, model) records covering 12,446 prompts. Analysis required the full 13-model menu per prompt, which excluded the tau2 dataset entirely (one model, gpt-5-chat, was never run on it) and two prompts whose query text did not align across models. The working sample was 12,166 prompts across nine datasets. The commercial OpenRouter router, whose per-prompt results ship with the benchmark as one of its ten built-in baselines, was held aside as a reference strategy and never used in label construction or training.

## Routing label

The prediction target for the classification task was defined per prompt as the cheapest model whose score cleared a quality threshold. The primary threshold was 1.0, meaning the model actually solved the prompt. When no model cleared the bar (18 percent of prompts), the label fell back to the cheapest model overall, on the reasoning that when every answer fails the only remaining objective is minimizing spend. A sensitivity threshold of 0.5, which additionally accepts arenahard draws, relabeled 2.1 percent of prompts and left every downstream comparison effectively unchanged.

## Features and split

The feature set was deliberately light and restricted to information available before any model is called: the prompt's character length, the median prompt-token count across the pool as a tokenizer-neutral size measure, and the task category. Text embeddings were excluded by design to keep the study inside a defensible scope. The train/test split (80/20, stratified by dataset) was made at the prompt level; because the modeling table holds one row per prompt, no prompt can appear on both sides, avoiding the leakage that a row-level split of the long table would create.

## Models

Two required algorithm types were trained. For classification, a multinomial logistic regression and a random forest were tuned with 5-fold cross-validation on the training prompts, scored by macro F1 to protect the rare but valuable classes (prompts only frontier models solve). The searches selected C = 10 without class weighting for the logistic model, and 300 unrestricted trees for the forest; balanced class weights lost the search for both. For regression, the dollar cost of a (prompt, model) call was predicted from the same pre-call features plus the model identity, with the target on a log10 scale (offset 0.0001) because costs span four orders of magnitude and 2,226 records cost zero. A tuned random forest regressor (depth 12, minimum leaf 2) reached R2 = 0.79 on log cost, with a dollar-scale MAE of $0.0073 against an average bill of $0.014.

The regressor was converted into a third routing strategy by pairing it with a capability screen computed on training data only: a model counted as capable on a task category if it solved at least half of that category's training prompts, and each test prompt was routed to the cheapest predicted-price capable model, falling back to the cheapest model where no model qualified (hle and swe-bench).

## References

Li, H., Zhang, Y., Guo, Z., Wang, C., Tang, S., Zhang, Q., Chen, Y., Qi, B., Ye, P., Bai, L., Wang, Z., & Hu, S. (2026). LLMRouterBench: A massive benchmark and unified framework for LLM routing. Findings of ACL 2026. arXiv:2601.07206. (Author list verified against the arXiv record on Jul 21.)
