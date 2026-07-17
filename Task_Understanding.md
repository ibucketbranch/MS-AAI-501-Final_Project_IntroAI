# AAI-501 Final Team Project - Task Understanding

Owner: Michael Valderrama
Created: 2026-06-30
Purpose: One place that explains exactly what the final project is, how it's graded, what
the technical setup must be, and which datasets/topics are viable. Source of truth is
Canvas; this is the working synthesis.

Sources:
- Final Team Project Introduction (Canvas page)
- Assignment 7.2: Final Team Project (Canvas, /assignments/417476) - includes the rubric
- Course Modules page (point values and due dates)

---

## 1. What the project is (in one paragraph)

As a team (2-3 people), pick a real-world AI/ML problem and a dataset, build a hands-on
solution that applies at least TWO different algorithm types we studied, run an
experimental comparison, and deliver three things: a ~10-page APA 7 report, clean
documented code in a GitHub repo, and a recorded 20-30 minute team presentation. One
person submits for the team. GitHub use is required and is how collaboration is measured.

---

## 2. Hard requirements (the must-haves)

- Team of 2-3; one representative submits all deliverables.
- GitHub REQUIRED for version control and to measure collaboration; README REQUIRED.
- Python code must follow PEP 8.
- At least TWO different algorithm types (e.g., Classification, Clustering, Regression),
  WITH an experimental comparison (compare algorithms, tune hyperparameters, and/or
  combine approaches like Clustering + Classification).
- Dataset >= 1000 examples, public (Kaggle/UCI) or self-provided; not tiny, not made up.
- Do NOT reuse a problem already analyzed in the course.
- Avoid datasets needing excessive preprocessing (some is expected).
- Report ~10 pages excluding appendices, APA 7, Word or PDF.
- Presentation 20-30 min, every member presents an equal share, hosted on YouTube/Vimeo
  with the link on the title slide.
- AI tool disclosure required (cite/explain any ChatGPT/Gemini/Copilot use).
- Turnitin enabled; Draft Coach available.
- NO extensions, ever. Late = not graded. Members can receive different grades by
  contribution.

---

## 3. How it's graded (Assignment 7.2 rubric, 280 pts total)

| Criterion | Weight | Points | What "Meets/Exceeds" looks like |
|-----------|--------|--------|----------------------------------|
| Project Selection and Setup (objectives, dataset, approach) | 15% | 42 | Clear objectives, feasible approach, dataset available, properly scoped |
| AI/ML Algorithm Descriptions, Theory and Source Code | 25% | 70 | Clear algorithm description, explicit theory with proper math/logic, self-documenting code |
| Execution and Output (implementing the algorithms) | 25% | 70 | Code runs on the data; complete results from multiple runs |
| Analyzing Methods, Results, Conclusions | 20% | 56 | Well-presented results, accurate conclusions, successful project |
| Report Format, Citations, Content | 15% | 42 | Proper length, properly cited, professional presentation |

Where the points are: the two heaviest buckets (50% combined) are the algorithm
work and the execution/output. The report and project-setup buckets (30% combined)
reward clarity, scoping, APA citations, and professional polish. Analysis/conclusions is
20%. So: strong, well-compared modeling + a clean APA report is the recipe.

Separate grade items in Module 7:
- Assignment 7.3 Peer Evaluation Form (individual): 45 pts.
- The Proposal (3.3) and Status Update (4.3) are only 5 pts each - low stakes gates, but
  required and the proposal shapes the whole project.

---

## 4. Deliverables and due dates

| # | Deliverable | Module | Due (Mon 11:59pm PT) | Points | Who submits |
|---|-------------|--------|----------------------|--------|-------------|
| 3.3 | 1-2 page Proposal | M3 | Jul 13, 2026 | 5 | team rep |
| 4.3 | Status Update Form | M4 | Jul 20, 2026 | 5 | team rep |
| 7.2 | Final Project: report + code (GitHub) + slides + video | M7 | Aug 10, 2026 | 280 | team rep |
| 7.3 | Peer Evaluation Form | M7 | Aug 10, 2026 | 45 | each member |

### Proposal (3.3) must contain
1. Clear statement of the topic.
2. The problem + algorithms to investigate, and the system to build.
3. Specific related course topics (search, classification, deep learning, NLP, CV, etc.).
4. Examples of expected system behaviors / problem types.
5. The issues you expect to focus on.
6. A reference list (APA 7) - becomes the core of the report's references.

### Final report (7.2) must contain
1. Purpose, goals, scope; references to papers the project/algorithms build on; whether
   you adapted a published algorithm or made a new one; relation to course techniques.
2. Clear specification of the algorithms used, with analysis, evaluation, and critique;
   algorithm comparisons preferably shown graphically.
3. Appendix listing each participant and their detailed contributions.

---

## 5. Technical setup (what to stand up)

- GitHub repo (one owner, all members as collaborators), README required. A Canvas doc
  "Instruction-README_GitHub-AAI" is linked on the assignment page for guidance.
- Suggested repo layout: data/ (or loader if large), notebooks/, src/, report/,
  README.md, requirements.txt.
- Workflow: feature branches + pull requests reviewed by a teammate; frequent small
  commits in each person's own name (commit history is graded as collaboration evidence).
- PEP 8 for all Python (consider a linter like ruff/flake8 + black, as in AAI-500).
- Report in APA 7 (Word/PDF); Turnitin + Draft Coach for a self-check before submit.

---

## 6. Dataset and topic options

All links below are from the assignment page. Rule reminders: >= 1000 rows, 2+ algorithm
types with comparison, not already used in the course, light preprocessing.

Sources:
- Kaggle datasets: https://www.kaggle.com/datasets
- UCI ML Repository: http://archive.ics.uci.edu/ml

Instructor-suggested directions:
- Healthcare imaging - DDSM mammography via Cancer Imaging Archive (CBIS-DDSM):
  https://www.cancerimagingarchive.net/collection/cbis-ddsm/ (image classification, heavier).
- Human Activity Recognition from smartphone sensors (UCI), classify walking/sitting/etc.:
  http://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones
- Gender bias in book reviews (project + code):
  https://md.ekstrandom.net/pubs/book-author-gender and
  https://github.com/BoiseState/bookdata-tools
- Image classification - notMNIST (stylized digits):
  http://yaroslavvb.blogspot.com/2011/09/notmnist-dataset.html
- UCR Time Series archive: https://www.cs.ucr.edu/~eamonn/time_series_data_2018/
- Structured/tabular examples named on the page: Lending Club loan status, credit-card
  fraud, NYSE prediction/clustering, breast cancer benign/malignant, Game of Thrones
  survival. For 10-20 feature tabular sets: explain variable importance, compare against
  a simpler model on the top features (don't just report accuracy).

Fit check (each candidate should pass all):
- [ ] >= 1000 examples
- [ ] Public or self-provided, reasonable preprocessing
- [ ] Not a course dataset already analyzed
- [ ] Supports 2+ algorithm types with a real comparison
- [ ] Clear real-world/business framing
- [ ] 3-5+ references findable for APA 7

Note for solo scenario: if Michael goes solo (pending AVB), favor a tabular
classification + clustering or classification + regression problem with light
preprocessing - achievable by one person in the timeline. Image/time-series options are
richer but heavier; viable but more work solo.

---

## 7. Open questions to resolve
- [x] Team vs. solo -> SOLO, approved by AVB 2026-06-30 (Tue switched schools).
- [ ] Final topic + dataset choice (drives the Jul 13 proposal).
- [ ] Confirm the "sample professional paper" APA 7 example from the assignment page.
- [ ] Read the linked GitHub/README instruction doc for any specific repo requirements.
