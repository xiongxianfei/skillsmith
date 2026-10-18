# Skillsmith Constitution

## Project purpose

Skillsmith is a reusable prompt-skill library for people who use AI assistants to write, translate, learn, communicate, and make everyday decisions with more care.

The repository serves users who install skills, contributors who author skills, and agents that maintain the catalog. A change is successful only when the skill remains portable Markdown, the expected invocation behavior is clear, and local validation can be reproduced.

## Source of truth order

When project artifacts conflict, agents and reviewers MUST use this order:

1. `CONSTITUTION.md`
2. `VISION.md`
3. Accepted requirements and allocated obligations under `design/requirements/`
4. Reviewed logical behavior under `design/system/` and architecture under `design/architecture/`
5. Execution plans and test specifications
6. Tests and CI configuration
7. Implementation files, including `skills/*/SKILL.md`, scripts, and templates
8. README, contribution docs, and chat history

Chat instructions MAY clarify intent for a current task, but they MUST NOT silently override durable project rules.

## Spec-driven rules

Changes that add a new skill, change a skill's output contract, alter validation rules, change installation behavior, or reposition the project MUST have requirements written before implementation. Durable requirements live under `design/requirements/`. A clearly scoped issue or change-local note MAY suffice for an isolated small change; later managed work MUST explicitly adopt relied-on output into its basis and obtain applicable review.

Requirements MUST identify observable behavior: skill trigger intent, accepted input, output format, safety boundaries, compatibility expectations, and validation commands.

Small editorial corrections MAY proceed without a formal spec when they do not change behavior, scope, safety posture, or public contracts.

## Test-driven rules

Agents SHOULD prove the current behavior before changing it. Bug fixes MUST include a minimal reproduction or a written explanation when automated reproduction is not practical.

New or changed validation behavior MUST be covered in `tests/validate_skills.py` or an equivalent automated check.

New or materially changed skill prompts MUST include eval evidence defined by the approved skill-quality standard. Editorial skill changes MAY proceed without new eval fixtures when they do not alter trigger behavior, output contract, workflow steps, referenced files, or safety behavior.

Skill prompt changes SHOULD include realistic example input and expected output behavior in the PR, a linked issue, or a change-local note unless the change is purely editorial.

Agents MUST NOT claim that a skill, script, installer, or workflow works without running the relevant local command or clearly stating that verification was not run.

## Architecture rules

The repository boundary is simple by design:

- reusable prompts live in `skills/<skill-name>/SKILL.md`;
- validation logic lives in `tests/validate_skills.py`;
- installer behavior lives in `install.sh`;
- GitHub automation lives in `.github/`;
- project identity lives in `VISION.md`;
- durable governance lives in `CONSTITUTION.md` and concise agent guidance in `AGENTS.md`.

Agents MUST keep behavior in the artifact that owns it. Prompt behavior belongs in the skill prompt. Validation behavior belongs in the validator. Installation behavior belongs in the installer. Project identity belongs in the vision.

Agents MUST NOT introduce hidden runtime dependencies, generated prompt behavior, or external services for ordinary skill execution. Skills are pure prompt assets unless a future spec and architecture explicitly change that boundary.

## Security and privacy rules

Skills MUST NOT require secrets, credentials, private local paths, or unpublished personal data.

Docs and examples MUST use fictional or sanitized inputs when demonstrating sensitive domains.

Skills in medical, legal, financial, security, or other high-stakes domains MUST include clear safety boundaries and MUST NOT present themselves as replacements for licensed professionals, emergency services, or official advice.

Agents MUST review dependency changes for supply-chain risk. New runtime or CI dependencies MUST have a clear purpose and a validation path.

## Compatibility rules

Skill files MUST remain plain Markdown with YAML frontmatter. Required frontmatter fields are `name` and `description`.

Skillsmith skills SHOULD omit optional frontmatter such as `argument-hint`, `effort`, and `allowed-tools` unless a later accepted proposal and spec require those fields for a concrete compatibility reason.

Skill names MUST be lowercase and hyphenated. Descriptions MUST be English, trigger-forward, and include explicit "Use this skill whenever..." style guidance when practical.

Every skill body MUST include `$ARGUMENTS` and a `## Output Format` section.

Compatibility with Codex slash commands, Claude Code skills, and copy-paste use in other AI tools SHOULD be preserved. Vendor-specific behavior MAY be documented, but it MUST NOT make the prompt unreadable or unusable elsewhere.

Breaking changes to skill names, output formats, installer paths, or README commands MUST be called out in the PR and paired with migration guidance.

## Verification rules

Before completion, agents MUST run:

```bash
python tests/validate_skills.py
```

Agents SHOULD also run targeted checks relevant to the changed files, such as searching for stale names after a rename or inspecting README marker blocks after a vision sync.

CI on push and pull request to `main` MUST run the same validator. Errors block merge. Warnings are non-blocking but MUST be reviewed and either fixed or acknowledged.

Final handoff MUST report the commands run and any warnings, skipped checks, or known risks.

## Review rules

New non-trivial standard-workflow work MUST receive independent requirement review, integrated system/architecture design review and delivery review before implementation relies on those bases. Delivery review covers both plan quality and verification allocation; a renamed stage MUST NOT silently waive a material obligation. Reviews MUST identify actual subjects, reviewer, findings and current applicability. Authors MUST NOT approve their own work.

After all authorized milestones, one independent whole-change Code Review MUST assess the complete delivered scope. Corrections require proportionate reassessment within that gate. Optional interim advice does not approve milestones. Distinct final Verify MUST assess the current basis, applicable reviews, evidence and unresolved issues before completion is claimed.

Small editorial corrections and explicitly isolated tasks MAY use bounded review appropriate to their scope; they MUST NOT claim full-workflow completion. Publication remains separate: changes go through a PR to `main`.

This amendment takes effect when this adoption is accepted and merged. The adoption itself remains accountable to the prior proposal/spec/architecture/plan review obligations, mapped to attributed assessments in [its review record](docs/changes/2026-10-18-rigorloop-v2-adoption/reviews/design-review.md), plus implementation review and final verification. Local edits and tool installation alone do not adopt policy or grant approval.

## Documentation rules

`README.md` MUST stay current for installation, usage, and the skills table.

`CONTRIBUTING.md` MUST stay current for contributor workflow, PR expectations, and local validation.

`AGENTS.md` MUST stay concise and agent-facing. Detailed durable rules belong here, not duplicated across agent prompts.

`VISION.md` MUST remain the canonical project identity document. README vision front-matter, when present, MUST be derived from `VISION.md`.

When adding a new skill, agents MUST update the README skills table and any install or usage examples that enumerate skills.

When a repeated failure pattern appears, agents SHOULD update the validator, templates, constitution, or contributing docs so the next contributor has a checkable rule.

## Agent behavior rules

Agents MUST inspect the current repository state before editing.

Agents MUST preserve unrelated user changes and MUST NOT revert files they did not intentionally change.

Agents MUST keep edits scoped to the requested change and the artifacts that must stay consistent with it.

Agents MUST state assumptions when requirements are incomplete and MUST ask for clarification before making irreversible or high-risk decisions.

Agents MUST NOT invent CI results, tests, approvals, issue links, release status, or external facts.

Agents MUST NOT silently remove governance, safety boundaries, validation checks, or documented compatibility.

## Standard workflow and manual skill use

After adoption, new non-trivial standard-workflow work uses RigorLoop v2.0.0: `route` → requirement analysis/review → system and architecture design/integrated review → plan/delivery review → implementation → one whole-change Code Review → distinct final Verify → separately authorized PR delivery. Supporting research, exploration and incident work enter the responsible stage; they do not waive its gate.

Git-held definitions own engineering meaning. Supported CLI tasks own current managed Change handoffs; use explicit project/Change identity and inspected revisions. Do not edit private operational storage, invent judgments, blindly replay interrupted mutations, or copy live database files as a backup. Plans retain stable delivery intent; Git evidence snapshots retain historical assessments, not a parallel live queue.

Manual invocation of individual skills is allowed for isolated tasks. Name the skill, follow its artifact rules and report the bounded outcome. Managed work that later relies on isolated output explicitly adopts and reviews it. Historical records retain original meanings and unknown status until evidence supports a disposition; there is no bulk conversion of old approvals.

The [workflow guide](docs/workflows.md) owns setup, detailed stage routing, artifact locations and recovery instructions. It is subordinate to this constitution. Completion claims include changed subjects, actual validation, warnings, unresolved obligations and skipped checks. PR, merge and release are separate actions.
