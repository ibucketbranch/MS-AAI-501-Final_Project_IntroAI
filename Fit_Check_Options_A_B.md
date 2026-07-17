# AAI-501 Final Project - Dataset Fit-Check: Option A vs Option B

Owner: Michael Valderrama | Mode: SOLO | Date: 2026-07-01
Purpose: Go/no-go fit-check on the two finalist datasets against the assignment rules,
with a two-algorithm plan and starter APA references for the proposal (due Jul 13).

Rules being checked: >=1000 rows; public; not a course dataset; light preprocessing;
2+ algorithm types WITH an experimental comparison; solo-feasible by Aug 10.

---

## Option A - AI4I 2020 Predictive Maintenance (UCI) -- hardware / AI-SI lane

| Check | Result |
|-------|--------|
| Rows | 10,000 - PASS (>=1000) |
| Features | 14 columns: air temp (K), process temp (K), rotational speed (rpm), torque (Nm), tool wear (min), product quality type L/M/H, + failure labels |
| Public | PASS - UCI ML Repository (also Kaggle mirrors) |
| Missing data | None - synthetic, clean -> light preprocessing PASS |
| Not a course dataset | PASS (new) |
| Target | Binary "machine failure" + 5 modes: TWF (46), HDF (115), PWF (95), OSF (98), RNF (19) |
| Class balance | ~3.4% failures - SEVERE imbalance (this is a feature, not a bug: strong analysis angle) |
| Solo feasibility | HIGH - small/clean, well-documented |

Two-algorithm plan (satisfies 2+ types + comparison):
- Algorithm 1: Logistic Regression (interpretable baseline) with class weighting.
- Algorithm 2: Random Forest and/or XGBoost (non-linear, feature importance).
- Comparison lens: classifier-vs-classifier; full-feature vs. top-k features (feature
  selection); imbalance handling (class weights / SMOTE) vs. none; evaluate with
  PR-AUC, recall, F1 - NOT raw accuracy (accuracy is misleading at 3.4% positives).
- Optional 3rd lens: K-Means to cluster operating regimes (temp/torque/speed) and see
  which regimes carry failure risk -> ties to your SI "which signals drive yield" framing.

Why it fits you: it is literally your hardware / AI-SI chip world - sensor signals to
failure, "which measurements matter," yield/reliability. Strong personal narrative.

Watch-outs: the imbalance means you MUST frame metrics correctly (PR-AUC/recall). RNF
(random failures, n=19) is near-noise - expect and discuss that it is not learnable.

Starter references (APA 7 - verify/expand to 3-5):
- Matzka, S. (2020). Explainable artificial intelligence for predictive maintenance
  applications. In 2020 Third International Conference on Artificial Intelligence for
  Industries (AI4I) (pp. 69-74). IEEE. https://doi.org/10.1109/AI4I49448.2020.00023
- Carvalho, T. P., Soares, F. A. A. M. N., Vita, R., Francisco, R. da P., Basto, J. P.,
  & Alcala, S. G. S. (2019). A systematic literature review of machine learning methods
  applied to predictive maintenance. Computers & Industrial Engineering, 137, 106024.
  https://doi.org/10.1016/j.cie.2019.106024
- Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). SMOTE: Synthetic
  minority over-sampling technique. Journal of Artificial Intelligence Research, 16,
  321-357. https://doi.org/10.1613/jair.953

---

## Option B - Human Activity Recognition Using Smartphones (UCI) -- wearables / edge-AI

| Check | Result |
|-------|--------|
| Rows | 10,299 - PASS (>=1000) |
| Features | 561 (time + frequency domain, from accelerometer + gyroscope) |
| Public | PASS - UCI ML Repository (also Kaggle mirror) |
| Missing data | None - pre-processed, normalized to [-1,1] -> very light prep PASS |
| Not a course dataset | PASS (new); also INSTRUCTOR-SUGGESTED on the assignment page |
| Target | 6 activities: walking, walking upstairs, walking downstairs, sitting, standing, laying |
| Structure | 30 subjects; predefined train/test split (~7,352 train / 2,947 test) |
| Solo feasibility | HIGH - clean, split provided, huge prior art |

Two-algorithm plan (satisfies 2+ types + comparison):
- Algorithm 1: multiclass classifier - SVM (classic strong baseline on this set).
- Algorithm 2: Random Forest (feature importance) or Logistic Regression (interpretable).
- Dimensionality lens: PCA to compress 561 features; compare full-feature vs. PCA-reduced
  models; K-Means/visualization to show static vs. dynamic activity clusters.
- Comparison: classifier-vs-classifier + full vs. PCA-reduced; metrics = accuracy, macro-F1,
  confusion matrix (sitting vs. standing is the classic hard pair - good to discuss).

Why it fits you: on-device / edge-AI angle overlaps your AI-SI chip interest (feature
extraction on a wearable), and it maps to your active life (walking/biking). Instructor
already lists it, so topic approval is essentially guaranteed.

Watch-outs: 561 features is a lot - lean on PCA/feature selection (that is the point,
and it earns rubric marks). Respect the subject-wise train/test split (do not shuffle
subjects across it) to avoid leakage.

Starter references (APA 7 - verify/expand to 3-5):
- Anguita, D., Ghio, A., Oneto, L., Parra, X., & Reyes-Ortiz, J. L. (2013). A public
  domain dataset for human activity recognition using smartphones. In ESANN 2013
  Proceedings (pp. 437-442).
- Reyes-Ortiz, J.-L., Oneto, L., Sama, A., Parra, X., & Anguita, D. (2016). Transition-
  aware human activity recognition using smartphones. Neurocomputing, 171, 754-767.
  https://doi.org/10.1016/j.neucom.2015.07.085
- Lara, O. D., & Labrador, M. A. (2013). A survey on human activity recognition using
  wearable sensors. IEEE Communications Surveys & Tutorials, 15(3), 1192-1209.
  https://doi.org/10.1109/SURV.2012.110112.00192

---

## Side-by-side

| Dimension | A: AI4I Predictive Maintenance | B: HAR Smartphones |
|-----------|-------------------------------|--------------------|
| Rows x features | 10,000 x 14 | 10,299 x 561 |
| Preprocessing load | Very light (clean) | Light (normalized, split given) |
| Core ML story | Imbalanced failure classification + feature importance | Multiclass activity classification + PCA |
| Distinctive angle | Class imbalance, "which sensor drives failure" | High-dimensional reduction, edge-AI |
| Personal fit | Hardware / AI-SI identity (strongest) | Edge-AI + active lifestyle; instructor-listed |
| Approval risk | Low | Very low (instructor-suggested) |
| Rubric leverage | Imbalance + comparison + interpretability | PCA + comparison + confusion analysis |
| Main watch-out | Metrics must be PR-AUC/recall, not accuracy | Manage 561 features; respect subject split |

## Recommendation
Both are GREEN and solo-safe. Pick on identity:
- Choose A if you want the project to shout "hardware / AI-SI" and you are comfortable
  handling class imbalance carefully.
- Choose B for the smoothest approval and lightest prep, with a clean edge-AI story.

Either way the proposal (Jul 13) structure is the same. Next: pick one, and I will draft
the 1-2 page proposal (problem, algorithms, course topics, expected behaviors, focus
issues, references) straight from this fit-check.
