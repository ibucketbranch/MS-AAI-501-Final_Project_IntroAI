# CI Setup for MS-AAI-501-Project (solo)

Replicates the linting CI Tue built for the AAI-500 team, adapted for your solo
AAI-501 project. Target repo: https://github.com/ibucketbranch/MS-AAI-501-Project

## What's here
- `.github/workflows/lint.yml` - Ruff linter (PEP 8) on every push and pull request.
  This is a copy of Tue's AAI-500 `lint.yml` (uses `astral-sh/ruff-action@v3`).
- `.github/workflows/export_html.yml.template` - OPTIONAL. Auto-builds an HTML report
  from your notebook on push to main. Needs a deploy-key secret first (instructions
  inside the file). Enable later, once you have a notebook and the secret.
- `ruff.toml` - explicit PEP 8 rules so lint behavior is predictable.

The team's `merge_notebooks.yml` is intentionally NOT included - it merged multiple
members' notebooks, which is irrelevant solo.

## Install into the repo (copy/paste)
From a local clone of MS-AAI-501-Project:

```bash
# from the repo root
mkdir -p .github/workflows
cp /Users/hudsonclaw/Projects/MS-AAI-USD/AAI-501/Final_Team_Project/github_ci_setup/.github/workflows/lint.yml .github/workflows/lint.yml
cp /Users/hudsonclaw/Projects/MS-AAI-USD/AAI-501/Final_Team_Project/github_ci_setup/ruff.toml ruff.toml
git add .github/workflows/lint.yml ruff.toml
git commit -m "ci: add ruff lint workflow and config"
git push
```

After pushing, open the repo's **Actions** tab - you'll see "Ruff Linter" run on the
commit. A green check = passing; red X = lint errors to fix.

## Run it locally before you push (so CI won't fail you)
```bash
pip install ruff
ruff check .          # lint (same as CI)
ruff check --fix .    # auto-fix what it can
ruff format .         # auto-format to PEP 8
```

## VS Code (Tue's recommendation)
Install the **Ruff** extension (publisher: Astral Software, id `charliermarsh.ruff`)
to autoformat to PEP 8 on save, so your code is clean before CI ever runs.

## Enabling the optional HTML export later
1. Rename `export_html.yml.template` to `export_html.yml`.
2. Edit the notebook path inside it to your real notebook (e.g. `src/analysis.ipynb`).
3. Add the `DEPLOY_KEY_MAIN` deploy-key secret (full steps are in the file header).
