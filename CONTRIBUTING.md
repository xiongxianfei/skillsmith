# Contributing to Skillsmith

Thanks for your interest in contributing. This guide covers everything you need to add a new skill or improve an existing one.

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
  Be specific about trigger phrases so Claude knows when to auto-invoke it.
argument-hint: <what the user should pass as input>
allowed-tools: ""
# Optional Claude Code tuning only; not required for portable behavior:
# effort: <low|medium|high|xhigh|max>
---

**Input:**
$ARGUMENTS

---

# Role / Profile

[Describe the persona or role Claude should adopt]

## Workflow

[Step-by-step instructions]

## Output Format

[Exact output structure Claude must follow]
```

### 3. Checklist before opening a PR

- [ ] `description` is in English and under 250 characters
- [ ] `argument-hint` is in English
- [ ] `effort` is omitted or uses an accepted value such as `low`, `medium`, `high`, `xhigh`, or `max`
- [ ] `allowed-tools: ""` is set for pure prompt skills
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
- `CONTRIBUTING.md`
- `.github/ISSUE_TEMPLATE/bug-report.yml`

---

## Running the validator locally

```bash
pip install pyyaml
python tests/validate_skills.py
python tests/check_readme_sync.py
```

Errors block merging. Warnings are non-blocking but should be reviewed.

---

## Skill writing tips

| Do | Don't |
|----|-------|
| Write `description` in English | Write `description` in Chinese or Russian |
| Use `$ARGUMENTS` to capture input | Forget `$ARGUMENTS` so input gets silently dropped |
| Define a clear `## Output Format` | Leave output structure implicit |
| Keep `description` under 250 chars | Write multi-paragraph descriptions |
| Omit `effort` unless the skill needs runtime-specific tuning | Rely on `effort` for portable behavior |
| Use plain section headers | Add emojis to Output Format headers |

See `specs/skill-quality-standard.md` for the canonical quality standard. This guide summarizes contributor workflow and should not duplicate that standard in full.

---

## Questions?

Open an issue using the **Skill Request** or **Bug Report** template.
