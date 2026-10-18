# Contributing to Skillsmith

Skillsmith uses C4 for design and ordinary Git/PR review for delivery. RigorLoop is no longer part of the active workflow. [VISION.md](../VISION.md) owns project purpose, [AGENTS.md](../AGENTS.md) owns agent conduct and engineering principles, and the [quality standard](skill-quality-standard.md) owns skill requirements. This guide owns contribution, validation and delivery procedures.

## 1. Define the change

Before adding a skill, changing output or validation rules, altering installation behavior, or repositioning the project, write the intended behavior and validation commands. Inspect the current prompt, tests and relevant architecture. Describe the user problem, trigger intent, accepted input, output format, safety/compatibility boundaries and observable acceptance examples where applicable. Small changes can use the issue or PR description. For architectural changes, use `c4-architecture` and keep this context in the subject's `architecture-spec.md` under [design/architecture/](../design/architecture/README.md).

Small editorial corrections need no formal design when behavior, scope, safety and public contracts stay unchanged. Where practical, capture current behavior before changing it. A bug fix needs a minimal reproduction or a written explanation of why automated reproduction is impractical.

## 2. Design and edit

Use a shared `model.d2` within each C4 package, context/container views and only the dynamic views needed to explain important scenarios. Keep implemented, proposed and unknown behavior distinct. Obtain human review of consequential decisions before relying on them. Optional decision records explain meaningful tradeoffs; no separate requirement, system-design or delivery-stage hierarchy is required.

Edit the owning prompt, validator, installer or document. Describe the expected result of substantive skill changes in the PR; no separate test fixtures are required. Keep changes focused and preserve unrelated work. Start new PR branches from the latest `main`; continue an existing authorized change in its current workspace.

Review dependency changes for supply-chain risk; new runtime or CI dependencies need a concrete purpose and validation path. When changing the validator, check representative valid and invalid inputs before handoff; no separate permanent test suite is required.

Keep current design decisions in the subject architecture specification. When delivery sequencing needs a plan, use the issue, PR description or a local working note; do not recreate a separate proposal/plan directory or an active-plan index.

## 3. Validate and evaluate

Install PyYAML if needed, then run the required check from the repository root:

```bash
pip install pyyaml
python tests/validate_skills.py
```

Run the validator before handoff. CI must run the same validator on pushes and PRs to `main`. Errors block merging. It checks required files and metadata, with no style warnings. Also run focused checks for affected contracts, links and documentation synchronization.

This is the only automated repository test. Check README catalog entries manually when adding, removing or renaming skills. Use focused inspection for documentation and actual model evidence for any claimed model-quality result; required-metadata validation alone proves neither.

For changed C4 diagrams, put D2 on PATH and run the package's helper:

```bash
python3 design/architecture/<subject>/scripts/architecture.py format
python3 design/architecture/<subject>/scripts/architecture.py check
python3 design/architecture/<subject>/scripts/architecture.py render
```

Inspect the rendered SVGs for readability and semantic accuracy. Python and D2 serve architecture checks; D2 is not a product runtime dependency. If a check cannot run, report that explicitly.

## 4. Review and deliver

Use a PR to `main` with the problem, resulting behavior, relevant design decisions and actual validation/evaluation results. Identify the reviewed revision and changed subjects; include realistic input and expected behavior for substantive prompt changes. Breaking changes to skill names, output formats, installer paths or README commands need explicit migration guidance. Report warnings, failures, skipped checks and open questions. Reviewers assess the complete diff with depth appropriate to its risk; do not infer human design approval from successful commands. Historical reviews retain their original scope and do not approve later changes.

Put task status and sufficient sanitized review/validation evidence in the issue or PR. Keep private working notes outside the repository, with a private backup when continuity requires it. Local-only files must not be the sole support for an external readiness claim. Preserve historical provenance with fixed Git links and migrate durable decisions into their owning architecture or quality documents; do not recreate workflow-record directories. Commit, push, merge and release require the applicable user authorization.

## Keeping documentation current

Update the owning document in the same change. `VISION.md` is the canonical identity; derive the README vision block from it. Keep README installation, usage and catalog entries current, including slash commands and any examples that enumerate skills. Maintain this guide for contributor procedures and keep `AGENTS.md` concise and agent-facing.

When failures recur, improve the relevant validator, template, quality rule or contributor guidance so the lesson becomes checkable. Preserve unique evidence and provenance without adding competing copies of current rules.

## Adding a new skill

### 1. Create the skill directory

```bash
mkdir skills/<skill-name>
```

Prefer descriptive, lowercase, hyphenated names such as `meal-planner` or `code-reviewer`. Naming patterns are not enforced by the validator; check any restrictions of the intended host separately.

### 2. Write `SKILL.md`

Start with valid YAML frontmatter containing non-empty strings for `name` and `description`, then write instructions suited to the skill:

```markdown
---
name: your-skill-name
description: >
  Describe what the skill does and when to use it.
---

[Instructions for handling the user's request and producing a useful result.]
```

No body template is required. Add headings, examples or `$ARGUMENTS` when useful for the skill and its intended host. The validator does not check body structure, naming patterns, language, length or optional metadata values.

### 3. Checklist before opening a PR

- [ ] `SKILL.md` has valid YAML frontmatter with non-empty string `name` and `description`
- [ ] The description explains what the skill does and when to use it
- [ ] Input handling and any optional metadata suit the intended host
- [ ] Substantive behavior changes and their expected result are explained in the PR
- [ ] High-risk skills include scope boundaries, refusal or escalation behavior, reviewer-visible safety notes
- [ ] CI passes locally: `python tests/validate_skills.py`
- [ ] Skill added to the README skills table
- [ ] Skill added to the `cp` install commands in README

### 4. Open a pull request

The PR template will pre-fill the checklist for you. Include one or two example inputs and outputs in the PR description so reviewers can quickly understand what the skill does.

---

## Improving an existing skill

- Keep changes focused: one concern per PR
- If you're changing the output format, explain why the new format is better
- Treat a change as material if it could alter what the skill does, when it triggers, or what it returns
- Explain material changes with concrete expected behavior; no fixture files or fixed scenario counts are required
- Editorial changes, such as typo fixes that do not affect trigger behavior, output contract, workflow steps, referenced files, or safety behavior, need no additional scenario documentation
- CI must pass after your changes

---

## Reporting bugs

Record bugs so another contributor can reproduce them without extra back-and-forth:

- Include the affected skill or repo area
- Include the smallest reproduction you can find
- Paste the exact input when possible
- State expected behavior and actual behavior separately
- Include the model used if behavior varies by model
- Add the relevant output excerpt or screenshot if the failure is formatting-related

A bug report is actionable when someone else can reproduce it from the issue alone.

---

## Fixing bugs

When you fix a bug, capture the full trail in the PR:

- Root cause: what was actually wrong
- Fix: why the change is correct
- Verification: the smallest useful check or reproduction showing the fix
- Prevention artifact: which doc, template, or validator rule was updated if the bug exposed a repeatable pattern

For this repo, the prevention artifact is often one of:

- `tests/validate_skills.py`
- the affected `skills/<skill-name>/SKILL.md`
- `README.md`
- `docs/workflows.md`
- `.github/ISSUE_TEMPLATE/bug-report.yml`

For questions or ideas, open an issue using the **Skill Request** or **Bug Report** template. The [quality standard](skill-quality-standard.md) remains the canonical source for authoring and evidence obligations.
