# AAI-501 Final Team Project - Team Coordination Plan

> SUPERSEDED 2026-06-30: AVB approved a SOLO project (Tue switched schools). The team
> coordination sections below no longer apply. Use Project_Breakdown_Milestones.md (solo)
> and AAI-501_Project_Planner.xlsx as the active plan. Kept for reference only.

Owner: Michael Valderrama
Created: 2026-06-29
Purpose: Keep a 2-3 person team aligned from kickoff through final submission. This is the
coordination layer (roles, cadence, deadlines, GitHub). The graded content lives in the
proposal, status update, paper, code, and presentation.

Reference: Final_Team_Project_Instructions.md (in this folder).

---

## 1. Key dates (hard - no extensions)

| Milestone | Module | Due (Mon, 11:59pm PT) | Days from today |
|-----------|--------|------------------------|-----------------|
| Module 1 Teammate Survey | M1 | Jun 29, 2026 (TODAY) | 0 |
| Teams assigned by instructor | M1 | end of Week 1 | this week |
| Proposal (Assignment 3.3) | M3 | Jul 13, 2026 | 14 |
| Status Update Form (Assignment 4.3) | M4 | Jul 20, 2026 | 21 |
| Final Project: paper + code + slides + video (7.2) | M7 | Aug 10, 2026 | 42 |
| Peer Evaluation Form - individual (7.3) | M7 | Aug 10, 2026 | 42 |

Late = not graded. Build to internal deadlines 2-3 days ahead of each due date.

---

## 2. Immediate actions (this week)

- [ ] TODAY: submit the Module 1 Teammate Survey on Canvas (due tonight).
- [ ] Once the instructor assigns the team, send a kickoff message within 24 hours
      (intro, time zone, weekly availability, preferred channel).
- [ ] Agree on a primary comms channel (Slack class workspace, or a team thread) and a
      backup (USD email).
- [ ] Set a recurring 30-45 min team sync (suggest weekly, same slot each week).
- [ ] Create the GitHub repo (one owner), add all members as collaborators, add a README.
- [ ] Agree on who is the "team representative" that submits each deliverable on Canvas.

---

## 3. Roles (rotate or fix - decide as a team)

With 2-3 people, everyone touches everything, but name an owner per area so nothing drops:

- Repo / GitHub lead: sets up repo, README, branch rules, merges PRs, keeps commit
  history clean (commits also "measure collaboration" per the rubric).
- Data lead: sourcing the dataset, loading, cleaning, EDA, feature selection.
- Modeling lead(s): implements the 2+ algorithms and the experimental comparison.
- Writing / submission lead: assembles the proposal, status form, and final paper in
  APA 7; owns Canvas submission and deadline tracking.
- Presentation lead: builds slides, coordinates the recording, posts the video link.

Note: every member must contribute equally and must present an equal share of the video.
Track contributions as you go - the final paper needs a per-person contributions appendix,
and the peer evaluation is individual.

---

## 4. GitHub setup (required by the rubric)

- One repo, private during work or public for submission (a public link can go in the
  report and Canvas). README required.
- README should include: project title, team members, problem statement, dataset source
  + license, how to run the code, and environment/requirements.
- Suggested layout:
  - `data/` (or a link + loader script if the dataset is large)
  - `notebooks/` exploration and experiments
  - `src/` reusable code
  - `report/` the paper and figures
  - `README.md`, `requirements.txt`
- Workflow: short-lived feature branches, pull requests reviewed by a teammate, frequent
  small commits in each person's own name (the history is graded for collaboration).
- Follow PEP 8 for all Python.

---

## 5. Topic and scope (drives the proposal)

Pick a problem that is comparable in complexity to a course assignment and needs at least
two different algorithm families with an experimental comparison.

Decision checklist before committing to a topic:
- [ ] Dataset has >= 1000 examples, public source (Kaggle / UCI) or self-provided.
- [ ] Not a problem already analyzed in the course.
- [ ] Reasonable preprocessing (not excessive).
- [ ] Maps to >= 2 algorithm types we have studied (e.g., Classification + Clustering,
      or multiple classifiers compared, or Regression + feature selection).
- [ ] A clear real-world / business framing.
- [ ] At least 3-5 references identified (papers/articles) for APA 7.

Capture the chosen topic, dataset link, and the 2+ algorithms in
`Proposal_Draft.md` as soon as the team agrees.

---

## 6. Phase-by-phase timeline

### Phase 1 - Kickoff and topic (Weeks 1-3, by Jul 13)
- Form team, set cadence and channels, stand up GitHub.
- Brainstorm 2-3 candidate topics; each member skims one dataset + one paper.
- Converge on one topic by ~Jul 6 to leave a week for the proposal.
- Draft the 1-2 page proposal (problem, algorithms, course topics, expected behaviors,
  focus issues, reference list in APA 7).
- Internal deadline: proposal ready Jul 11; rep submits by Jul 13.

### Phase 2 - Status update (Week 4, by Jul 20)
- Lock the dataset, finish EDA and cleaning, get a baseline model running.
- Fill in the Status Update Form: progress, what is working, blockers, next steps.
- Internal deadline: status ready Jul 18; rep submits by Jul 20.

### Phase 3 - Build and experiment (Weeks 5-6)
- Implement the 2+ algorithms; run the experimental comparison (tuning, feature
  selection, alternate models).
- Produce comparison figures (graphical comparisons are preferred by the rubric).
- Keep committing to GitHub; draft report sections as results land.

### Phase 4 - Finalize (Week 7, by Aug 10)
- Finish the ~10-page APA 7 report (purpose/scope, algorithm spec + critique, graphical
  comparisons, per-person contributions appendix).
- Clean and document the code (PEP 8); finalize README and public GitHub link.
- Build slides; record the 20-30 min presentation (everyone presents); upload video,
  put the link on the title slide.
- Internal deadline: everything ready Aug 8; rep submits 7.2 by Aug 10.
- Each member individually submits the 7.3 Peer Evaluation by Aug 10.

---

## 7. Communication norms

- Weekly sync (live) + async updates in the team channel between syncs.
- Each member posts a short weekly update: done / doing / blocked.
- 24-hour response expectation on direct asks; flag blockers early.
- If a teammate goes quiet or contribution is uneven, raise it in the team first, then
  contact the instructor promptly (the syllabus expects this).

---

## 8. Deliverable submission map

| Deliverable | Format | Who submits | Where |
|-------------|--------|-------------|-------|
| Teammate Survey | form | each member | Canvas (M1) |
| Proposal | 1-2 pp, APA 7 (Word/PDF) | team rep | Canvas (3.3) |
| Status Update | form | team rep | Canvas (4.3) |
| Final paper + code | ~10 pp APA 7 + repo/zip | team rep | Canvas (7.2) + GitHub |
| Slides + video | slides + YouTube/Vimeo link | team rep | Canvas (7.2) |
| Peer Evaluation | form | each member individually | Canvas (7.3) |

---

## 9. Open items
- [ ] Confirm exact teammate names and contact info once assigned.
- [ ] Confirm whether your Slack class workspace is the agreed channel.
- [ ] Pick the topic and dataset; start Proposal_Draft.md.
- [ ] Confirm the Module 7 scoring rubric specifics (read it in Module 7 when available).
