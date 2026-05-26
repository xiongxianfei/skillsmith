# Skillsmith Constitution

## Project purpose

Skillsmith is a reusable prompt-skill library for people who use AI assistants to write, translate, learn, communicate, and make everyday decisions with more care.

The repository serves users who install skills, contributors who author skills, and agents that maintain the catalog. A change is successful only when the skill remains portable Markdown, the expected invocation behavior is clear, and local validation can be reproduced.

## Source of truth order

When project artifacts conflict, agents and reviewers MUST use this order:

1. `CONSTITUTION.md`
2. `VISION.md`
3. Approved specs under `specs/` or change-local docs under `docs/changes/`
4. Architecture or project-map docs under `docs/`
5. Execution plans and test specifications
6. Tests and CI configuration
7. Implementation files, including `skills/*/SKILL.md`, scripts, and templates
8. README, contribution docs, and chat history

Chat instructions MAY clarify intent for a current task, but they MUST NOT silently override durable project rules.

## Spec-driven rules

Changes that add a new skill, change a skill's output contract, alter validation rules, change installation behavior, or reposition the project MUST have requirements written before implementation. The requirements MAY live in a dedicated spec, a change-local document, or a clearly scoped issue when the change is small.

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

Use proposal review when a change affects project direction, catalog scope, safety posture, or contributor policy.

Use spec review when requirements define new skill behavior, validation behavior, installer behavior, compatibility, or safety constraints.

Use architecture review when a change adds new components, dependencies, generated assets, external services, data flow, plugin packaging behavior, or long-lived repository structure.

Use plan review for multi-step changes that touch multiple owned areas or require migration sequencing.

Use code review after implementation for changes to validator logic, installer behavior, CI, templates, or high-risk skills.

Small documentation-only edits MAY use direct maintainer review when the validation command passes and no contract changes are involved.

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

The standard workflow for non-trivial work is:

1. Confirm fit with `VISION.md` and this constitution.
2. Write or locate requirements.
3. Review architecture impact when boundaries, dependencies, or compatibility change.
4. Plan implementation when the change spans multiple files or milestones.
5. Implement with proof first where practical.
6. Run validation and targeted checks.
7. Review the diff.
8. Explain the change and hand off with verification evidence.

Manual invocation of individual skills is allowed for isolated tasks. The agent MUST name the skill being used, follow its artifact rules, and report enough evidence that a reviewer can see what changed and how it was checked.

Workflow completion claims MUST include changed files, validation commands, unresolved questions, and any skipped or blocked checks.
