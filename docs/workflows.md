# Contributing to Skillsmith

This guide owns contribution, validation and PR procedures. Use [VISION.md](../VISION.md) for project purpose, [AGENTS.md](../AGENTS.md) for agent conduct, and the [quality standard](skill-quality-standard.md) for skill authoring, safety and evidence requirements.

## 1. Define the change

Inspect the current repository state and relevant prompt, validator, installer or design. Before a substantive change, describe the user problem, intended behavior and validation commands in the issue or PR. Include trigger intent, accepted input, expected output, safety/compatibility boundaries and observable acceptance examples where applicable. A change is substantive if it can alter activation, behavior, output, validation, installation or project scope. Small editorial corrections need no formal design when those contracts stay unchanged.

For a bug, capture the smallest reproduction and current behavior where practical, or explain why automated reproduction is impractical. For architectural changes, use `c4-architecture` and keep behavior, constraints and consequential decisions together in the subject's `architecture-spec.md`; follow the [architecture guide](../design/architecture/README.md#maintaining-a-design). Distinguish implemented, proposed and unknown behavior, and obtain human review of consequential decisions before relying on them.

## 2. Design and edit

Start new PR branches from the latest `main`, using `feat/`, `fix/`, `docs/` or `improve/`; continue an existing authorized change in its current workspace. Keep one concern per PR, preserve unrelated work and edit the owning artifacts. Use the issue, PR or a private working note for task sequencing rather than creating another plan directory.

Treat the entire skill directory as the distributable artifact. Follow the [full-directory guidance](skill-quality-standard.md#full-directory-skill-design) for conditional references, assets, scripts and host prerequisites. Review changes affecting tool permissions and dependencies explicitly; new runtime or CI dependencies need a concrete purpose and validation path.

For a new skill, create `skills/<skill-name>/SKILL.md` with this minimal structure:

```markdown
---
name: your-skill-name
description: >
  Describe what the skill does and when to use it.
---

[Instructions for handling the user's request and producing a useful result.]
```

The validator enforces Agent Skills naming and metadata constraints, including matching the name to the directory; see [required checks](skill-quality-standard.md#required-checks). No body template, `$ARGUMENTS` placeholder or output heading is required. Check intended-host compatibility separately.

Update the README skill table when adding, removing or renaming a skill. Update installation and usage examples only when the change affects them; adding a skill does not require another `cp` example. Explain substantive behavior changes and their expected results, including why any output-format change is useful.

## 3. Validate and evaluate

Install PyYAML if needed, then run the required check from the repository root:

```bash
pip install pyyaml
python tests/validate_skills.py
```

CI runs the same validator on pushes and PRs to `main`; errors block merging. This is the only required automated repository check. It checks required files and metadata, emits no style warnings, and does not establish model quality, safety or host compatibility. No unit-test suite, separate fixtures, fixed scenario count or live-model CI gate is required.

Run focused checks for affected contracts, local links and README synchronization. When changing the validator, check representative valid and invalid inputs; no permanent test suite is required. Document and test local scripts when changed. For changed C4 diagrams, use the package helper to format, check and render, then inspect the SVGs as described in the architecture guide.

Assess changed skill behavior using realistic examples and the [review and evidence guidance](skill-quality-standard.md#review-and-evidence). Support empirical or model-specific claims with actual model evidence; label expected examples separately. Report commands, results, warnings, failures, skipped checks and unresolved questions.

## 4. Review and deliver

All changes go through a PR to `main`. Describe the problem, resulting behavior, relevant decisions and actual validation/evaluation results. Identify the reviewed revision and changed subjects; include realistic input and expected behavior for substantive prompt changes. Explain high-risk safety boundaries and provide migration guidance for breaking changes to skill names, output formats, installer paths or README commands.

For bug fixes, explain the root cause, why the fix addresses it, and how it was verified. If the defect exposes a recurring pattern, update the relevant prompt, validator, template or guidance to help prevent recurrence.

Reviewers assess the complete diff with depth appropriate to its risk. Successful commands do not establish human approval, authors cannot claim independent approval of their own work, and prior reviews do not approve later changes. Put task status and sufficient sanitized review/validation evidence in the PR. Keep private working notes outside the repository; they must not be the sole support for an external readiness claim.

Commit, push, merge and release require applicable user authorization. Use squash merge and delete the branch after merging.

## Keeping documentation current

Update the owning document in the same change. `VISION.md` owns project identity; derive the README introduction from it. The README provides discovery and usage, this guide owns contribution procedures, the quality standard owns authoring requirements, and architecture specifications own intended behavior and design decisions. Keep `AGENTS.md` concise and agent-facing.

Move still-useful guidance into its owner before removing redundant documents. Documentation cleanup does not require preserving historical provenance, adding fixed-commit links or creating archives. Retain current requirements and evidence needed to support active claims, and repair references to removed files. Lessons from use should improve the relevant skill or shared guidance directly.

## Reporting bugs

Use the **Bug Report** issue template with the affected skill or repository area, smallest reproduction, exact input where possible, expected versus actual behavior, relevant output excerpt, and model/host when behavior depends on it. A useful report lets another contributor reproduce the problem without extra back-and-forth. Use **Skill Request** for proposed skills.
