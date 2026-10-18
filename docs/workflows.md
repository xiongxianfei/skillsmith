# Contributing to Skillsmith

Skillsmith uses C4 for design and ordinary Git/PR review for delivery. RigorLoop is no longer part of the active workflow. The [constitution](../CONSTITUTION.md) governs this guide; the [quality standard](skill-quality-standard.md) defines skill evidence requirements.

## 1. Define the change

Inspect the current prompt, tests and relevant architecture. Describe the user problem, intended behavior, safety/compatibility boundaries and observable acceptance examples. Small changes can use the issue or PR description. For architectural changes, use `c4-architecture` and keep this context in the subject's `architecture-spec.md` under [design/architecture/](../design/architecture/README.md).

## 2. Design and edit

Use a shared `model.d2` within each C4 package, context/container views and only the dynamic views needed to explain important scenarios. Keep implemented, proposed and unknown behavior distinct. Obtain human review of consequential decisions before relying on them. Optional decision records explain meaningful tradeoffs; no separate requirement, system-design or delivery-stage hierarchy is required.

Edit the owning prompt, validator, installer or document. Add or update eval fixtures for new or materially changed skills. Keep changes focused and preserve unrelated work. Start new PR branches from the latest `main`; continue an existing authorized change in its current workspace.

## 3. Validate and evaluate

Install PyYAML if needed, then run the required check from the repository root:

```bash
pip install pyyaml
python tests/validate_skills.py
```

Errors block merging. Warnings are non-blocking but must be reviewed.

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

## Adding a new skill


### 1. Create the skill directory

```bash
mkdir skills/<skill-name>
```

Use lowercase, hyphenated names such as `meal-planner` or `code-reviewer`.

### 2. Write `SKILL.md`

Copy the structure below and fill it in:

```markdown
---
name: your-skill-name
description: >
  One or two sentences in English describing what the skill does and when it triggers.
  Be specific about trigger phrases so the assistant knows when to invoke it.
---

**Input:**
$ARGUMENTS

---

# Role / Profile

[Describe the persona or role the assistant should adopt]

## Workflow

[Step-by-step instructions]

## Output Format

[Exact output structure the assistant must follow]
```

### 3. Checklist before opening a PR

- [ ] `description` is in English and under 250 characters
- [ ] Optional frontmatter such as `argument-hint`, `effort`, or `allowed-tools` is omitted unless an accepted proposal/spec requires it
- [ ] `$ARGUMENTS` appears in the prompt body
- [ ] `## Output Format` section is present
- [ ] No emojis in the Output Format section headers
- [ ] New or materially changed skills include at least three eval scenarios: normal use, indirect trigger, and edge/safety/failure/non-trigger/misuse behavior
- [ ] High-risk skills include scope boundaries, refusal or escalation behavior, reviewer-visible safety notes, and at least one safety or misuse eval case
- [ ] CI passes locally: `python tests/validate_skills.py`
- [ ] Skill added to the README skills table
- [ ] Skill added to the `cp` install commands in README

### 4. Add eval fixtures for new or material changes

New or materially changed skills need static eval evidence at:

```text
tests/evals/skills/<skill-name>/cases.yaml
```

Use this minimal schema:

```yaml
version: 1
scenarios:
  - id: normal-use
    category: normal
    prompt: "A realistic direct user request."
    expected_behavior: "The observable behavior reviewers should expect."
  - id: indirect-trigger
    category: indirect-trigger
    prompt: "A vague or casual request that should still trigger the skill."
    expected_behavior: "How the skill recognizes and handles the request."
  - id: edge-case
    category: edge
    prompt: "An edge, failure, non-trigger, safety, or misuse situation."
    expected_behavior: "The safe or bounded behavior expected."
```

Allowed edge categories are `edge`, `safety`, `failure`, `non-trigger`, and `misuse`.

For high-risk skills, add `high_risk: true`, `safety_notes`, and at least one `safety` or `misuse` scenario. The first slice does not require a shared domain-specific safety schema.

Existing skills listed in `tests/evals/skills/grandfathered-skills.yaml` may lack `cases.yaml` until materially changed.

### 5. Open a pull request

The PR template will pre-fill the checklist for you. Include one or two example inputs and outputs in the PR description so reviewers can quickly understand what the skill does.

---

## Improving an existing skill

- Keep changes focused: one concern per PR
- If you're changing the output format, explain why the new format is better
- Treat a change as material if it could alter what the skill does, when it triggers, or what it returns
- Material changes need the same eval evidence as a new skill
- Editorial changes, such as typo fixes that do not affect trigger behavior, output contract, workflow steps, referenced files, or safety behavior, may proceed without new eval fixtures
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
- Regression coverage: what check now prevents recurrence
- Prevention artifact: which doc, template, or validator rule was updated if the bug exposed a repeatable pattern

For this repo, the prevention artifact is often one of:

- `tests/validate_skills.py`
- the affected `skills/<skill-name>/SKILL.md`
- `README.md`
- `docs/workflows.md`
- `.github/ISSUE_TEMPLATE/bug-report.yml`

For questions or ideas, open an issue using the **Skill Request** or **Bug Report** template. The [quality standard](skill-quality-standard.md) remains the canonical source for authoring and evidence obligations.
