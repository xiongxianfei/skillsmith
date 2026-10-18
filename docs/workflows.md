# Contributor workflow

Skillsmith uses C4 for design and ordinary Git/PR review for delivery. RigorLoop is no longer part of the active workflow. The [constitution](../CONSTITUTION.md) governs this guide; the [quality standard](skill-quality-standard.md) defines skill evidence requirements.

## 1. Define the change

Inspect the current prompt, tests and relevant architecture. Describe the user problem, intended behavior, safety/compatibility boundaries and observable acceptance examples. Small changes can use the issue or PR description. For architectural changes, use `c4-architecture` and keep this context in the subject's `architecture-spec.md` under [design/architecture/](../design/architecture/README.md).

## 2. Design and edit

Use a shared `model.d2` within each C4 package, context/container views and only the dynamic views needed to explain important scenarios. Keep implemented, proposed and unknown behavior distinct. Obtain human review of consequential decisions before relying on them. Optional decision records explain meaningful tradeoffs; no separate requirement, system-design or delivery-stage hierarchy is required.

Edit the owning prompt, validator, installer or document. Add or update eval fixtures for new or materially changed skills. Keep changes focused and preserve unrelated work. Start new PR branches from the latest `main`; continue an existing authorized change in its current workspace.

## 3. Validate and evaluate

Run the required check from the repository root:

```bash
python tests/validate_skills.py
```

Run `python tests/check_readme_sync.py` when changing the catalog or its documentation, and relevant unit tests when changing validation code. Static fixtures describe expected behavior; they do not replace the model evidence required by the quality standard.

For changed C4 diagrams, put D2 on PATH and run the package's helper:

```bash
python3 design/architecture/<subject>/scripts/architecture.py format
python3 design/architecture/<subject>/scripts/architecture.py check
python3 design/architecture/<subject>/scripts/architecture.py render
```

Inspect the rendered SVGs for readability and semantic accuracy. Python and D2 serve architecture checks; D2 is not a product runtime dependency. If a check cannot run, report that explicitly.

## 4. Review and deliver

Use a PR to `main` with the problem, resulting behavior, relevant design decisions and actual validation/evaluation results. Report warnings, failures, skipped checks and open questions. Reviewers assess the complete diff with depth appropriate to its risk; do not infer human design approval from successful commands.

New `docs/changes/` records remain local and ignored. Put sufficient sanitized evidence in the PR so reviewers do not need local records. Existing tracked history stays historical. Commit, push, merge and release require the applicable user authorization.
