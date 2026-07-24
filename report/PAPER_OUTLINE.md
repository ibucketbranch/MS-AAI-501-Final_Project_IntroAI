# Final Report Outline -- Cost-Aware Routing of Large Language Models

Rebuilt 2026-07-23 from the proposal, milestones doc, report drafts, and executed
notebooks 01-06. Target: ~10 pages APA 7 excluding appendices, due Aug 10 (7.2).
Thesis: the hard part of routing is not picking per request, it is knowing your menu.

Story arc in three beats:
1. Routing works: the logistic router keeps 94% of the strongest model's quality at
   19% of its cost, and every trained strategy beats the commercial OpenRouter
   reference on both axes.
2. The surprise: one cheap model (qwen3-235b-a22b-2507) is strong enough that a fixed
   choice rivals the trained routers. Honest evaluation reproduced, independently and
   at course scale, the benchmark paper's own finding that most routers fail to beat
   the best single model.
3. The closer: an LLM handed the same menu (notebook 06, claude-haiku-4.5) rediscovers
   the same conclusion by itself, sending 95% of traffic to that one model.

---

## 1. Introduction: Purpose, Goals, and Scope (~1.5 pp)
Rubric: Project Selection & Setup (42) + Report Format (42, partial).
- The budgeting question; the "accountant for token spend" framing (proposal, Michael's
  own coinage, keep it).
- LLMRouterBench Performance-Cost setting; why measured public data fits the problem.
- Adapted published framings (RouteLLM label logic, benchmark evaluation setting), not
  a new algorithm. Course tie: Ch 7 supervised learning, ML lifecycle, evaluation.
- The two tasks (classification + regression) and the deliberate scope limits: light
  pre-call features, offline replay.
- DRAFTED: voice-check sample already written (see session; move into paper file).

## 2. Data and the Routing Label (~1.5 pp)
Rubric: Execution & Output (70, partial). Source: methods_draft.md, notebooks 01-02.
- Flattening to 173,688 (prompt, model) records; 12,166 usable prompts, nine datasets;
  tau2 exclusion stated honestly (gpt-5-chat never run on it).
- The label rule: cheapest model clearing threshold 1.0; 18% no-solver fallback to
  cheapest overall; the milestones doc called this the highest-risk design decision,
  defend it here.
- Sensitivity design: threshold 0.5 relabels 2.1% of prompts (results in sec. 4).
- Leakage-safe prompt-level 80/20 split, stratified by dataset.
- OpenRouter held aside as reference, never used in training.

## 3. Algorithms: Theory and Specification (~2 pp)
Rubric: Algorithm Descriptions, Theory & Code (70). Source: methods_draft, notebooks 03-04.
- Multinomial logistic regression: theory, tuning (C=10, no class weighting won),
  macro-F1 selection rationale (protect rare frontier-only classes).
- Random forest (Breiman, 2001): theory, tuning (300 unrestricted trees).
- Cost regression (second algorithm type): log10 target (costs span 4 orders of
  magnitude, 2,226 zero-cost records), tuned RF regressor, R2 0.79, dollar MAE $0.0073
  vs $0.014 average bill.
- Regressor-derived router: capability screen from training data only (>=50% category
  solve rate), route to cheapest predicted-price capable model.
- Code pointer: public repo, PEP 8, ruff CI, tests on the label rule.

## 4. Experimental Results (~2.5 pp)
Rubric: Execution & Output (70, partial) + Analysis (56, partial). Source: results_draft,
notebook 05.
- Scoreboard table (2,434 held-out prompts): regressor router $0.0006/0.513;
  always-cheapest $0.0008/0.429; fixed qwen $0.0009/0.538; oracle $0.0055/0.822;
  RF $0.0073/0.536; logistic $0.0115/0.564; OpenRouter $0.0225/0.495; always-strongest
  $0.0615/0.597.
- Figures (all already rendered): cost-vs-quality frontier (nb 05), confusion matrix
  ordered cheap-to-expensive (nb 03), RF feature importances (nb 03), EDA menu scatter
  + per-dataset heatmap (nb 01).
- Threshold sensitivity: no ranking changes; oracle 0.822 -> 0.813 at tau 0.5.
- The oracle line to keep: near-perfect routing is not expensive; the difficulty is
  informational, not economic.

## 5. Discussion (~1.5 pp)
Rubric: Analysis, Results & Conclusions (56). Source: results_draft, notebook 06.
- Beat two in full: fixed qwen dominance; a router must beat the best single model to
  justify its existence; only the logistic router clears the bar, at a premium.
- OpenRouter beaten on both axes by all trained strategies.
- Published ceiling paragraph (AVB suggestion #2): Avengers-Pro near-zero Pareto
  distance; the field's routers often fail to beat the best single model; what closes
  the gap (embeddings, expertise clusters) vs this study's deliberate light features.
- LLM-as-router (AVB suggestion #3): 300-prompt matched sample, haiku router at
  $0.0011/0.502, 95% of traffic to qwen, 13/300 replies tried to solve the prompt
  instead of routing; router's own inference cost (~$0.0008/request) doubles its
  effective cost, still far under the tuned classifiers.
- Limitations: one benchmark, English prompts, offline replay, no tool-selection or
  live-traffic test, light features by design.

## 6. Conclusion (~0.5 pp)
- Answer the title question honestly; the menu-knowledge thesis; what a follow-up with
  embeddings would test (the oracle gap is the prize).

## References (APA 7)
- Li et al. (2026) LLMRouterBench, Findings of ACL 2026, arXiv:2601.07206 (author list
  verified Jul 21).
- Ong et al. (2024) RouteLLM, arXiv:2406.18665.
- Breiman (2001) Random forests. Machine Learning 45(1).
- Poole & Mackworth (2023) AI: Foundations of Computational Agents, 3rd ed.
- Pedregosa et al. (2011) scikit-learn, JMLR 12 (add, code dependency).

## Appendices (excluded from page count)
- A: Contributions (solo statement, per rubric).
- B: AI tool disclosure (program 7-element standard, first person).
- Repo link in report body AND Canvas submission comment (instructions require both).

## Remaining build checklist
- [ ] Assemble sections into report/final_paper.md -> export docx/PDF (APA title page)
- [ ] Voice check on section 1 sample (awaiting Michael's redline)
- [ ] Turnitin / Draft Coach pass before submit
- [ ] Slides + 20-30 min video (separate deliverable, Aug 6-8 window)
- [ ] One loose end from milestones: "Send AVB the late note" still marked OPEN
