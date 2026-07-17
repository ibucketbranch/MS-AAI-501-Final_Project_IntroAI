# AAI-501 Final Project - Breakdown & Milestone Matrix (SOLO, AEQ Routing)

Owner: Michael Valderrama
Topic: Cost-aware LLM routing ("AEQ" / accountant for tokens) on LLMRouterBench.
Mode: SOLO, approved by AVB.
Anchor: Thu Jul 16, 2026, 8:51 PM PT. Hard dates are Mondays, 11:59pm PT. No extensions.
Status legend: [ ] not started, [~] in progress, [x] done, [!] blocked/overdue.

Dataset: LLMRouterBench (github.com/ynulihao/LLMRouterBench, Findings@ACL'26).
23,945 prompts, 391,645 records. Per record: prompt, prompt_tokens, completion_tokens,
cost, score. Public precomputed results, so it is measured data, not generated.

Two algorithm types (locked): Classification (route to cost-optimal model) and
Regression (predict cost). Comparison: algorithm vs algorithm, plus baselines
(always-cheapest, always-strongest). Optional: K-means on prompt economic profile.

---

## 1. Milestone summary (the gates)

| Milestone | Window | Hard due | Graded | Status |
|-----------|--------|----------|--------|--------|
| M0 Setup: repo + README + CI | overdue, do now | - | - | [!] |
| M1 Topic + dataset locked | done | - | - | [x] |
| M2 Proposal submitted (3.3) | submitted Jul 14 3:23am (flagged late) | Jul 13 | 5 pts | [x] |
| M3 Data + baseline + Status (4.3) | Jul 17 - Jul 20 | Jul 20 | 5 pts | [ ] LIVE |
| M4 Modeling + experiments | Jul 21 - Aug 3 | - | - | [ ] |
| M5 Report + code + slides + video (7.2) | Aug 4 - Aug 10 | Aug 10 | 280 pts | [ ] |
| M6 Peer evaluation (7.3) | Aug 8 - Aug 10 | Aug 10 | 45 pts | [ ] |

Internal rule: finish each graded item 2 days before its hard date. M2 landed on time.
M3 is the live one to protect.

---

## 2. Detailed task matrix (owner = Me)

### M0 - Setup (OVERDUE, do alongside M3)
| Task | Target | Deliverable | Status |
|------|--------|-------------|--------|
| Create GitHub project repo + README | Jul 17 | Repo live | [ ] |
| Push staged CI (lint.yml + ruff.toml from github_ci_setup/) | Jul 17 | Green Actions check | [ ] |
| Repo structure: data/ notebooks/ src/ report/ | Jul 17 | Skeleton | [ ] |

Branch naming (project repo, MS-AAI-501-Project): bare `M0`, `M3`, `M4`, `M5`, same
token style as the `M1` branch already live in the course repo. Unlike the course
repo, milestone branches here DO merge into main (PR once the ruff check is green) --
main has to be the graded deliverable, not just a backup. See
AAI-501_Agent_Swarm_Prompts.md for the exact handoff prompts.

### M1 - Topic & dataset (DONE)
| Task | Deliverable | Status |
|------|-------------|--------|
| Shortlist + fit-check candidates | Fit_Check_Options_A_B.md | [x] |
| Data feasibility pass (AEQ) | LLMRouterBench verified | [x] |
| Pick topic + dataset | Cost-aware routing locked | [x] |
| Collect starter references (APA 7) | 4 refs in proposal | [x] |

### M2 - Proposal (CLOSED)
| Task | Deliverable | Status |
|------|-------------|--------|
| Write proposal (all 5 required elements) | Assignment_3.3_Proposal_AEQ_Routing.docx | [x] |
| AI-fingerprint scrub | verified clean | [x] |
| Export PDF (Canvas rejects .docx) | ...AEQ_Routing.pdf | [x] |
| Submit 3.3 on Canvas | Submitted Jul 14, 3:23am, flagged late, ungraded | [x] |
| Send AVB the late note | Draft ready, not sent yet, your call | [ ] OPEN |

### M3 - Data, baseline & Status Update (Jul 17 - Jul 20) -- GRADED 4.3, LIVE
| Task | Target | Deliverable | Depends on | Status |
|------|--------|-------------|------------|--------|
| Download bench-release data into repo | Jul 17 | Raw data local | Repo | [ ] |
| Reshape JSON records (wide per-model -> long) | Jul 17 | Tidy dataframe | Raw data | [ ] |
| EDA: cost + score distributions per model, token counts, task mix | Jul 18 | EDA notebook | Tidy df | [ ] |
| DEFINE THE ROUTING LABEL (cheapest model clearing a quality threshold) | Jul 18 | Documented rule + label column | EDA | [ ] |
| Light feature set (prompt_tokens, task category) - no heavy embeddings | Jul 19 | Feature table | Label | [ ] |
| Baseline model #1 (logistic regression router) | Jul 19 | Baseline metrics | Features | [ ] |
| Baselines: always-cheapest / always-strongest cost+quality | Jul 19 | Reference numbers | Tidy df | [ ] |
| Submit Status Update Form (4.3) | Jul 20 | Submitted | Baseline | [ ] |

New vs. the old plan: label construction and the wide-to-long reshape replace the old
"encoding/missing" and "feature selection" tasks. The label rule is the highest-risk
design decision in the project. Write down the threshold and defend it.

### M4 - Modeling & experiments (Jul 21 - Aug 3)
| Task | Target | Deliverable | Status |
|------|--------|-------------|--------|
| Router classifier tuned (e.g., random forest vs logistic) | Jul 26 | Model + metrics | [ ] |
| Cost regression model tuned (2nd algorithm type) | Jul 30 | Model + metrics | [ ] |
| Experimental comparison + threshold sensitivity | Aug 1 | Comparison table | [ ] |
| Graphical comparison: cost-vs-quality curves, confusion matrix, importances | Aug 3 | Figures | [ ] |
| Draft report sections as results land | Aug 3 | Report draft | [ ] |

### M5 - Finalize (Aug 4 - Aug 10) -- GRADED 7.2
| Task | Target | Deliverable | Status |
|------|--------|-------------|--------|
| ~10-page APA 7 report | Aug 7 | Report PDF | [ ] |
| Contributions appendix (solo) | Aug 7 | Appendix | [ ] |
| Clean + document code (PEP 8), final README, public repo link | Aug 7 | Repo final | [ ] |
| Slides | Aug 6 | Deck | [ ] |
| Record 20-30 min video (you present all) | Aug 8 | Video | [ ] |
| Upload video, link on title slide | Aug 8 | Link | [ ] |
| Turnitin / Draft Coach check | Aug 8 | Clean report | [ ] |
| Submit 7.2 + Peer Eval 7.3 | Aug 10 | Submitted | [ ] |

---

## 3. Rubric coverage (280 pts)

| Criterion (pts) | Covered by |
|-----------------|------------|
| Project Selection & Setup (42) | M1 topic lock + proposal + business framing |
| Algorithm Descriptions, Theory, Code (70) | M4 classifier + regressor, theory in report, PEP 8 code |
| Execution & Output (70) | M3-M4 runs producing complete results |
| Analysis, Results, Conclusions (56) | M4 comparison + threshold sensitivity + conclusions |
| Report Format, Citations, Content (42) | M5 APA report + verified references |

Delivery note: code ships as a documented Jupyter notebook in the public GitHub repo.
Google Colab / NotebookLM are NOT required by the assignment.

---

## 4. Risk watch (AEQ-specific)
- Label design is the top risk. "Cost-optimal" depends on a quality threshold you pick.
  State it, and run a sensitivity check so it does not look arbitrary.
- Leakage: the same prompt appears across models. Split by prompt, never let one prompt
  land on both sides of train/test.
- Scope: keep features light (prompt_tokens, task category). Text embeddings pull this
  into NLP and blow the timeline.
- Reference accuracy: author lists on the routing papers still need verification before
  the final report.
- Repo is not live yet and GitHub is a graded requirement. Fix in M0 this week.
- M2 is already late. Do not let M3 slip too.
