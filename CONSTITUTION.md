# Skillsmith Constitution

## Project purpose

Skillsmith is a library that turns good practices into reusable AI skills and continually improves them through use, feedback, and evaluation.

The repository serves users who install skills, contributors who author skills, and agents that maintain the catalog. A change is successful only when the skill remains portable Markdown, the expected invocation behavior is clear, and local validation can be reproduced.

## Source of truth order

When project artifacts conflict, agents and reviewers MUST use this order:

1. `CONSTITUTION.md`
2. `VISION.md`
3. Accepted behavior and architectural decisions in `design/architecture/`, and the shared quality standard in `docs/skill-quality-standard.md`
4. Tests and CI configuration
5. Implementation files, including `skills/*/SKILL.md`, scripts, and templates
6. README, contribution docs and historical records

Architecture specifications MUST distinguish accepted decisions, observed implementation, proposals and unknowns. Reverse engineering or drawing a diagram does not establish acceptance. Explicit user decisions that change durable policy MUST be reflected in the owning documents.

## Spec-driven rules

Changes that add a new skill, change a skill's output contract, alter validation rules, change installation behavior, or reposition the project MUST describe intended behavior before implementation. Keep design requirements, constraints and acceptance examples together in the relevant `design/architecture/<subject>/architecture-spec.md`; do not create separate requirement or system-design directories. A clearly scoped issue or PR description MAY suffice for a small change that does not need architectural design.

Describe observable behavior: trigger intent, accepted input, output format, safety boundaries, compatibility expectations and validation commands. Use the `c4-architecture` skill for architectural design, with D2 models, focused views and generated SVGs. Keep model and behavior decisions in the same reviewable change.

Small editorial corrections MAY proceed without a formal spec when they do not change behavior, scope, safety posture or public contracts.

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

Changes MUST be reviewed through a PR to `main`. Review depth should match behavior, compatibility and safety risk. Reviewers assess intended behavior, design decisions, the delivered diff and actual validation evidence. Authors MUST NOT claim independent approval of their own work.

C4 designs require human review before being described as approved. Static checks and generated diagrams do not establish architectural correctness or model quality. Non-trivial design decisions should be reviewed before implementation relies on them; proposed changes and unresolved questions must remain visible.

RigorLoop stage gates, CLI handoffs and operational records are no longer required. Historical reviews retain their original scope; they do not approve later changes. Publication, merge and release remain separately authorized actions.

## Documentation rules

Operational change logs MUST NOT be maintained as repository documents. Keep task status and review/validation evidence in the issue or PR; any private working notes belong outside the repository. Preserve useful design decisions in their current owners and historical provenance through fixed Git revisions. Do not recreate retired workflow-record directories. Keep durable design in `design/architecture/` and contributor quality rules in `docs/skill-quality-standard.md`; do not relocate operational logs elsewhere merely to commit them. Publish a sufficient sanitized review/verification account in the PR, with exact subject identities, checks, limitations and accessible source references. Local-only files MUST NOT be the sole evidence supporting an external readiness claim. Use supported private backups when operational continuity is needed.

`README.md` MUST stay current for installation, usage, and the skills table.

`docs/workflows.md` MUST stay current for contributor workflow, PR expectations, and local validation.

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

Use a proportionate workflow: describe the intended behavior → design with `c4-architecture` when architecture is affected → edit the owning artifacts → validate and evaluate → review through a PR.

`design/architecture/` is the only design directory. Keep goals, requirements, behavior, decisions and risks together in each subject specification. Use a plan only when dependencies or risk justify it, recorded in the issue, PR or a local working note. Do not maintain separate proposal/plan directories or routing indexes. No RigorLoop installation, Node upgrade or managed Change is required for this workflow.

The [workflow guide](docs/workflows.md) explains artifact locations and commands. Completion claims include changed subjects, actual validation, warnings, unresolved issues and skipped checks. Operational records stay outside the repository; the PR must contain sufficient reviewable evidence.
