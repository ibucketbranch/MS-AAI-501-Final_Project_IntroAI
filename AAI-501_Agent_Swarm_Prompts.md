# M3 Agent Swarm Prompts (AEQ Routing, AAI-501 Final Project)

Hand these to Claude Code or Cursor. Each prompt is self-contained (no memory of this
chat), so it repeats the context it needs. Copy one prompt per agent/session.

Repo: github.com/ibucketbranch/MS-AAI-501-Project (not cloned locally yet -- Prompt 1
handles that). CI files are already staged at
`/Users/hudsonclaw/Projects/MS-AAI-USD/AAI-501/Final_Team_Project/github_ci_setup/`
(lint.yml, ruff.toml, SETUP.md) -- Prompt 1 copies them in.

## How to run it

Each task gets its own branch, not a shared one. Prompts 2, 3, and 4 still have a real
data dependency on each other (label needs the reshaped data, baseline needs the
label), so the branches aren't fully parallel-cuttable -- each one gets cut from main
AFTER the prior branch is merged in, not from each other and not all up front. That's
what the "Merge step" blocks between prompts below are for: I've worked out the exact
commands and the order, you (or whichever agent runs next) just run them.

One thing I won't do myself: actually execute git commands against your course repos.
That's a standing rule for me, not a preference -- so "I manage the merge" means I plan
the sequence and hand you the exact runbook, not that I click the buttons. Takes about
10 seconds per step, you can paste the Merge step block into a terminal yourself or
have the next agent run it as its first move.

Sequence:
1. Prompt 1 -- repo bootstrap, commits straight to main.
2. Prompt 2 -- branch `M3-data-pull` off main.
3. Merge step A -- fold `M3-data-pull` into main, cut `M3-eda-label` off the updated main.
4. Prompt 3 -- works on `M3-eda-label`.
5. Merge step B -- fold `M3-eda-label` into main, cut `M3-baseline` off the updated main.
6. Prompt 4 -- works on `M3-baseline`. Closes the M3 milestone.
7. Merge step C -- fold `M3-baseline` into main, cut `M3-status-update` off the updated main.
8. Prompt 5 -- works on `M3-status-update`.
9. Merge step D -- fold `M3-status-update` into main.

Before anything commits or pushes: review the diff yourself. That is your repo, your
call, not the agent's.

Local repo path (same for every prompt below, once Prompt 1 clones it):
`~/Projects/MS-AAI-USD/AAI-501/Final_Team_Project/MS-AAI-501-Project`
Two ways an agent picks this up: open Cursor or Claude Code with that folder as the
workspace root (its working directory then just is the repo, no path needed in the
prompt), or paste the prompts as-is below, which now spell the path out explicitly so
it works even in a fresh terminal session pointed somewhere else.

## Branch naming

Same `M#` token you already use in the course repo (git@github.com:ibucketbranch/MS-AAI-501.git
has a live `M1` branch), but since each task now gets its own branch, each one is
`M3-<task>`: `M3-data-pull`, `M3-eda-label`, `M3-baseline`, `M3-status-update`. All
roll up under the M3 milestone from Project_Breakdown_Milestones.md. No M1/M2 branch,
those milestones (topic lock, proposal) never touched this repo.

One deliberate difference from the course repo's rule, worth flagging: in the course
repo, module branches are backup and never merge into main. Here, main has to end up
being the graded deliverable, so it can't stay empty. Convention for this repo: work
happens on a task branch, then it merges into main (via the Merge step runbooks below)
once its ruff check is green. `main` should always reflect the current, buildable
state of the project, since that's what a grader opening the repo link actually sees.

## Verified facts about the dataset (pulled from the actual LLMRouterBench README,
not assumed)

I checked github.com/ynulihao/LLMRouterBench directly. A few things in earlier drafts
of these prompts were wrong or too vague, fixed below:

- **The data is not in the git repo.** It's a separate download, `bench-release.tar.gz`,
  offered three ways: Baidu Netdisk, Google Drive, or Hugging Face
  (huggingface.co/datasets/NPULH/LLMRouterBench). Hugging Face is the only one that's
  cleanly scriptable (no browser click-through), so that's the one to use.
- **There are two separate settings, and only one has real dollar costs.** "Performance"
  covers 20 lightweight open models (~7B) with no meaningful per-token pricing.
  "Performance-Cost" covers 13 flagship paid models (Claude-sonnet-4, Gemini-2.5-flash/pro,
  GPT-5-chat/medium, Qwen3-235B (+thinking variant), DeepSeek-V3/V3.1-terminus/R1, GLM-4.6,
  Kimi-K2, Intern-S1) across 10 datasets (AIME, LiveMathBench, LiveCodeBench, SWE-Bench,
  GPQA, HLE, MMLU-Pro, SimpleQA, ArenaHard, tau2-Bench), with real input/output pricing per
  model. For an "accountant for tokens" project, that's the one to pull. Pulling the full
  391,645-record combined set would drag in cost-free data that doesn't fit the premise.
- **Real file structure after extraction:** `results/bench/<dataset>/<split>/<model>/<timestamp>.json`.
  Each file has top-level `performance`, `cost`, `counts`, plus a `records` list. Each
  record has: `index`, `origin_query`, `prompt`, `prediction`, `ground_truth`, `score`,
  `prompt_tokens`, `completion_tokens`, `cost`, `raw_output`. Use `prompt` (not
  `origin_query`) for token/feature work, it's the fully-templated version actually sent
  to the model. Dataset, split, and model come from the folder path, not from inside the JSON.
- **No task-category field exists.** Derive it from the dataset name using the README's
  own grouping: Math (AIME, LiveMathBench), Code (LiveCodeBench, SWE-Bench), Knowledge
  (GPQA, HLE, MMLU-Pro, SimpleQA), Instruction Following (ArenaHard), Tool Use (tau2-Bench).
- **The `score` field is not one consistent metric.** It's accuracy for most datasets,
  Pass@1 for the code datasets, LLM-as-judge for HLE/SimpleQA/ArenaHard, success rate for
  tau2-Bench. A single global score cutoff for the routing label doesn't hold up across
  that mix. This is now baked into Prompt 3 below.
- License is MIT, no restriction on using or reshaping the data for coursework.

---

## Prompt 1 -- Repo bootstrap + CI

```
I'm a solo grad student (USD MS-AAI, course AAI-501) setting up the GitHub repo for
my final project. Repo: git@github.com:ibucketbranch/MS-AAI-501-Project.git (empty or
near-empty, mine, private-turned-public for grading). Clone it to
~/Projects/MS-AAI-USD/AAI-501/Final_Team_Project/MS-AAI-501-Project (or wherever makes
sense on this machine -- ask me if the path is ambiguous).

Set up this structure:
  data/          -- raw and processed data (add data/raw/ to .gitignore, the LLMRouterBench
                    files are large and get pulled fresh, not committed)
  notebooks/     -- Jupyter notebooks
  src/           -- any shared Python helpers (routing label logic, feature building)
  report/        -- final report, slides
  README.md
  requirements.txt -- pandas, numpy, scikit-learn, matplotlib, pyarrow, jupyter,
                    huggingface_hub. This is a lean list for the reshape/EDA/modeling
                    work in THIS repo, not the full LLMRouterBench framework's own
                    requirements.txt (that one installs an LLM-serving/eval stack we
                    don't need, we're only consuming its precomputed results). Every
                    later agent should activate a venv against this file and add to it
                    if a new import comes up, rather than installing ad hoc.
  .gitignore     -- Python defaults + data/raw/ + .venv/ + .env

Copy the CI I already staged into the new repo, don't regenerate it:
  github_ci_setup/.github/workflows/lint.yml -> .github/workflows/lint.yml
  github_ci_setup/ruff.toml -> ruff.toml
Source folder: /Users/hudsonclaw/Projects/MS-AAI-USD/AAI-501/Final_Team_Project/github_ci_setup/

The lint.yml runs astral-sh/ruff-action@v3 with "check --output-format=concise" on
push/PR. ruff.toml sets line-length 88, target py311, rules E/W/F/I/UP/B, and includes
.ipynb files. Do not change these, they're already tuned to match a teammate's setup
from a prior course project.

Write a short README: project title "Cost-Aware Routing of Large Language Models:
Predicting the Cheapest Capable Model for Each Request," one paragraph on the problem
(an accountant for LLM token spend -- pick the cheapest model that still clears a
quality bar for a given prompt), the two algorithm types (classification for the
routing decision, regression for cost prediction), the dataset (LLMRouterBench,
github.com/ynulihao/LLMRouterBench, Findings@ACL'26 -- specifically its
"Performance-Cost" setting: 13 flagship models with real per-token pricing across 10
datasets, a subset of the benchmark's full 391,645-record / 23,945-prompt release,
picked because that's the only slice with real dollar costs), and the repo layout
above. Plain language, no marketing tone, written like a student explaining the
project to a classmate, not a pitch deck. No em dashes.

Init git if needed, first commit with the scaffold + README + CI, straight to main
(nothing to merge yet). Do NOT push main to origin without showing me the diff first
and letting me say go.
```

---

## Prompt 2 -- Pull the dataset, reshape it (branch: M3-data-pull)

```
I'm a solo grad student (USD MS-AAI, AAI-501) working with the LLMRouterBench dataset
for a class project on LLM routing economics (LLMRouterBench: Findings@ACL'26,
github.com/ynulihao/LLMRouterBench). It's public, precomputed results, not something
I'm generating myself.

Scope: LLMRouterBench actually ships two separate settings. I only want the
"Performance-Cost" setting -- 13 flagship paid models (Claude-sonnet-4,
Gemini-2.5-flash, Gemini-2.5-pro, GPT-5-chat, GPT-5-medium, Qwen3-235b-a22b-2507,
Qwen3-235b-a22b-thinking-2507, Deepseek-v3-0324, Deepseek-v3.1-terminus,
Deepseek-r1-0528, GLM-4.6, Kimi-k2-0905, Intern-s1) across 10 datasets (AIME,
LiveMathBench, LiveCodeBench, SWE-Bench, GPQA, HLE, MMLU-Pro, SimpleQA, ArenaHard,
tau2-Bench). That's the only setting with real per-token dollar pricing, which is the
whole premise of the project. Do not pull the other "Performance" setting (20
lightweight open models, no real cost data), it doesn't fit the story and just adds
noise.

Data source: the data is NOT in the git repo, it's a separate download,
bench-release.tar.gz, offered via Hugging Face (huggingface.co/datasets/NPULH/LLMRouterBench),
Google Drive, or Baidu Netdisk. Use Hugging Face, it's the only one that's cleanly
scriptable (huggingface_hub, already in requirements.txt from Prompt 1). If it turns
out to need a Hugging Face login/token to download, stop and tell me rather than
trying to work around it.

File structure after extraction: results/bench/<dataset>/<split>/<model>/<timestamp>.json.
Each file has top-level performance/cost/counts fields plus a "records" list. Each
record has: index, origin_query, prompt, prediction, ground_truth, score,
prompt_tokens, completion_tokens, cost, raw_output. Dataset, split, and model come from
the folder path, not from inside the JSON. Use the "prompt" field (not origin_query)
for any token/feature work later, it's the fully templated text actually sent to the
model. If more than one timestamp file exists for the same dataset/split/model, use
the most recent one and note that you did.

Task:
1. Pull bench-release.tar.gz from Hugging Face, extract it, but only walk/load the 10
   Performance-Cost datasets x 13 models described above into
   data/raw/ in my project repo at
   ~/Projects/MS-AAI-USD/AAI-501/Final_Team_Project/MS-AAI-501-Project/data/raw/.
2. Reshape into one tidy long-format table: one row per (dataset, split, model, index),
   columns for prompt_tokens, completion_tokens, cost, score, prompt, and a
   task_category column derived from the dataset name using this mapping -- Math:
   AIME, LiveMathBench. Code: LiveCodeBench, SWE-Bench. Knowledge: GPQA, HLE, MMLU-Pro,
   SimpleQA. Instruction Following: ArenaHard. Tool Use: tau2-Bench.
3. Save the tidy table to data/processed/llmrouterbench_long.parquet (or .csv if
   parquet gives you trouble, but parquet is preferred for size).
4. Report the actual row/record counts you end up with (this is a 10-dataset,
   13-model subset of the full 391,645-record benchmark, so it will be smaller than
   that number, that's expected, don't treat it as a mismatch to fix).
5. Write this up as a short Jupyter notebook, notebooks/01_data_pull_reshape.ipynb --
   code cells for the pull/reshape, a markdown cell after each code block explaining
   what happened and why (not a code comment, an actual markdown cell). Written like a
   student narrating their own work, first person ("I reshaped..." not "the data was
   reshaped"), plain language, no filler, no em dashes, no hype words like "robust" or
   "seamless." State assumptions explicitly where a judgment call was required.

Create and check out a new branch, M3-data-pull, off main, and do all of this there.
Commit on that branch, not on main. Don't merge or push, I'll handle that once I've
looked at the notebook.
```

### Merge step A (run after Prompt 2, before Prompt 3)

```
git checkout main
git pull origin main          # skip if you haven't pushed main yet
git merge --no-ff M3-data-pull -m "Merge M3-data-pull: raw pull + wide-to-long reshape"
git push origin main
git checkout -b M3-eda-label
```

---

## Prompt 3 -- EDA + define the routing label (branch: M3-eda-label)

```
I'm a solo grad student (USD MS-AAI, AAI-501), continuing a class project on LLM
routing economics using the LLMRouterBench dataset. Repo path:
~/Projects/MS-AAI-USD/AAI-501/Final_Team_Project/MS-AAI-501-Project. There's already a
tidy long-format table at data/processed/llmrouterbench_long.parquet in that repo --
one row per (prompt_id, model), columns for prompt_tokens, completion_tokens, cost,
score, and some task/prompt metadata. Read that in, don't re-pull or re-reshape it.

Task:
1. New notebook, notebooks/02_eda_label.ipynb.
2. EDA: cost and score distributions per model (plots, labeled axes/titles/units),
   token count distributions, task-category mix if that field exists. Use .head() on
   dataframes in the notebook, not full dumps.
3. This is the important part -- define the routing label. For each prompt, the label
   is the cheapest model that still clears a quality threshold on that prompt. One
   thing to build in from the start: the "score" field is NOT one consistent metric
   across this dataset. It's accuracy for most datasets, Pass@1 for the code datasets
   (LiveCodeBench, SWE-Bench), LLM-as-judge for HLE/SimpleQA/ArenaHard, success rate
   for tau2-Bench. A single global score cutoff (like "score >= 0.7") does not mean
   the same thing across those, so do not use one. I need you to:
   a. Define the threshold PER DATASET, relative to that dataset's own score
      distribution for that prompt (e.g., within X points of the best-scoring model
      on that specific prompt, or a per-dataset percentile). Explain why a relative,
      per-dataset threshold is the right call given the metric mix, don't just assert it.
   b. Build the label column: for each prompt, among models that clear the threshold,
      pick the lowest-cost one. If none clear it, decide and document a fallback rule
      (e.g., label = the highest-scoring model available) rather than silently
      dropping the prompt.
   c. Run a sensitivity check: show how the label distribution (which models get
      picked how often) shifts if the threshold moves up or down a bit. This is a
      grading requirement, the threshold can't look arbitrary.
4. Markdown cell after every code block explaining what it shows and why, first person,
   plain language, no em dashes, no hype vocabulary (avoid: delve, leverage, robust,
   seamless, unlock, game-changer, cutting-edge, and similar). State assumptions up
   front. This is the single highest-risk design decision in the project -- be
   explicit and defend the choice in prose, don't just show code.
5. Save the labeled table to data/processed/llmrouterbench_labeled.parquet.

You should already be on the M3-eda-label branch (cut off main after the data-pull
work was merged in). Commit there, not on main. Don't merge or push, I'll handle that
once I've reviewed the threshold choice.
```

### Merge step B (run after Prompt 3, before Prompt 4)

```
git checkout main
git pull origin main
git merge --no-ff M3-eda-label -m "Merge M3-eda-label: EDA + routing label + sensitivity check"
git push origin main
git checkout -b M3-baseline
```

---

## Prompt 4 -- Features + baseline models, leakage-safe (branch: M3-baseline)

```
I'm a solo grad student (USD MS-AAI, AAI-501), continuing a class project on LLM
routing economics. Repo path:
~/Projects/MS-AAI-USD/AAI-501/Final_Team_Project/MS-AAI-501-Project. There's a labeled
table at data/processed/llmrouterbench_labeled.parquet in that repo -- one row per
(prompt_id, model), with a routing label column already built (cheapest model per
prompt that clears a quality threshold; see notebooks/02_eda_label.ipynb for how it
was defined, don't redefine it).

Task:
1. New notebook, notebooks/03_baseline_router.ipynb.
2. Feature set stays light on purpose (scope guard for a 3-4 week class project):
   prompt_tokens and task_category (the column built in the data-pull notebook, derived
   from dataset name). No text embeddings, no fine-tuning the prompt text itself --
   that turns this into an NLP project and blows the timeline.
3. Split by prompt (dataset + index, since that's what identifies a unique prompt in
   this data), not by row. The same prompt appears once per model in this table, so a
   random row split would leak the same prompt into both train and test. Use a
   prompt-level train/test split (GroupShuffleSplit grouped on the prompt identifier).
   Set a fixed random_state=42 everywhere a split or model has one, so this is
   reproducible if I or a grader re-runs it.
4. Build two baselines for comparison, not fed through any model:
   - always-cheapest: pick the lowest-cost model for every prompt, report resulting
     average cost and quality (score against the threshold).
   - always-strongest: pick the highest-scoring model for every prompt, same reporting.
5. Build baseline model 1: logistic regression classifier predicting the routing label
   (which model to pick) from the light feature set. Report accuracy, and something
   better than accuracy given this is a routing/business-cost problem -- at minimum,
   report the realized average cost and average quality if you followed the model's
   picks, so it's comparable to the two hand-built baselines above.
6. Markdown cell after every code block, first person, plain language, no em dashes,
   no hype words. Be honest about what's weak here -- a first-pass baseline is
   supposed to be beatable, say so if the logistic regression barely beats
   always-cheapest, don't oversell it.

You should already be on the M3-baseline branch (cut off main after the eda-label work
was merged in). Commit there, not on main. This closes out the modeling half of the
M3 milestone. Don't merge or push, I'll handle that once I've reviewed the numbers.
```

### Merge step C (run after Prompt 4, before Prompt 5)

```
git checkout main
git pull origin main
git merge --no-ff M3-baseline -m "Merge M3-baseline: features + baseline router + comparison baselines"
git push origin main
git checkout -b M3-status-update
```

---

## Prompt 5 -- Status Update writeup, Assignment 4.3 (branch: M3-status-update)

```
I'm a solo grad student (USD MS-AAI, AAI-501). I need a draft writeup for a Status
Update assignment (Canvas Assignment 4.3, due soon) covering the project-to-date work
on a cost-aware LLM routing project (dataset: LLMRouterBench). Repo path:
~/Projects/MS-AAI-USD/AAI-501/Final_Team_Project/MS-AAI-501-Project. I have three
notebooks already done in that repo:
  notebooks/01_data_pull_reshape.ipynb -- data pull + wide-to-long reshape
  notebooks/02_eda_label.ipynb -- EDA + the routing label definition/threshold + sensitivity check
  notebooks/03_baseline_router.ipynb -- light features, prompt-level train/test split, baseline logistic regression router vs always-cheapest/always-strongest

Read those three notebooks (code and markdown cells) and draft a status update in
markdown, report/status_update_4.3.md, covering: what's been done, the one big design
decision so far (the routing label / quality threshold) and why I chose it, the
baseline results, and what's next (M4: tuned classifier, a second algorithm -- cost
regression, experimental comparison, report).

Voice: solo master's student status update, first person ("I built...", "I found..."),
plain and direct, no corporate status-report tone, no em dashes, no hype vocabulary
(delve, leverage, robust, seamless, game-changer, cutting-edge, and similar), no
forward-looking filler like "moving forward" or "the future of." State what's actually
uncertain or unfinished rather than smoothing it over. Keep it to what the assignment
needs, don't pad it.

I still need to check the actual Assignment 4.3 form on Canvas for required fields
before submitting -- just get me a clean draft of the content, I'll fit it to whatever
form fields Canvas wants.

You should already be on the M3-status-update branch (cut off main after the baseline
work was merged in). Commit there, not on main. Don't merge or push, I'll handle that
once I've reviewed the draft.
```

### Merge step D (run after Prompt 5 -- closes the M3 milestone)

```
git checkout main
git pull origin main
git merge --no-ff M3-status-update -m "Merge M3-status-update: 4.3 status update draft"
git push origin main
```

Main now has the full M3 milestone: repo scaffold, tidy data, EDA + label with
sensitivity check, leakage-safe baseline router, and the 4.3 draft. That's what a
grader clicking the repo link sees.
