# Skillsmith Workflow Guide

## Purpose

This guide maps Skillsmith's local artifacts to the standard spec-driven, test-driven workflow. It tells agents where lifecycle evidence belongs; the specialized stage skills still own the content of proposals, specs, plans, reviews, implementation, verification, and PR handoff.

## Source order

Use this order when artifacts conflict:

1. `CONSTITUTION.md`
2. `VISION.md`
3. Approved specs under `specs/` or change-local docs under `docs/changes/`
4. Architecture and project-map docs under `docs/`
5. Execution plans and test specs
6. Tests and CI configuration
7. Implementation files
8. README, contribution docs, and chat history

## Standard lifecycle

Non-trivial changes follow this path:

```text
proposal -> proposal-review -> spec -> spec-review -> architecture -> architecture-review -> plan -> plan-review -> test-spec -> implement -> code-review -> review-resolution when triggered -> ci-maintenance when triggered -> explain-change -> verify -> pr
```

Manual invocation of one skill is allowed and remains isolated unless the user explicitly asks to continue through the full workflow.

## Artifact locations

Use existing files when they already own the topic. For new lifecycle artifacts, prefer these paths:

```text
CONSTITUTION.md
VISION.md
AGENTS.md
CLAUDE.md
docs/workflows.md
docs/project-map.md
docs/vision/strategic-positioning.md
docs/changes/<change-id>/change.yaml
docs/changes/<change-id>/proposal.md
docs/changes/<change-id>/spec.md
docs/changes/<change-id>/architecture.md
docs/changes/<change-id>/plan.md
docs/changes/<change-id>/test-spec.md
docs/changes/<change-id>/review-log.md
docs/changes/<change-id>/review-resolution.md
docs/changes/<change-id>/explain-change.md
docs/changes/<change-id>/verify-report.md
docs/changes/<change-id>/pr.md
specs/<slug>.md
specs/<slug>.test.md
```

Use `docs/changes/<change-id>/` for multi-stage work that needs traceability across requirements, design, plan, tests, implementation, review, verification, and PR handoff.

Use top-level `specs/` for durable product or skill contracts that should outlive one change.

## Change IDs

Use lowercase dated slugs:

```text
YYYY-MM-DD-short-name
```

Example:

```text
docs/changes/2026-05-25-add-skill-validator-rules/
```

## Stage routing

Use `explore` before proposal when the problem, user value, or option set is not stable.

Use `research` before proposal, spec, architecture, or implementation when current external facts, platform behavior, standards, laws, pricing, security limits, or dependency behavior affect correctness.

Use `proposal` when a direction needs decision framing before requirements.

Use `spec` when observable behavior, compatibility, safety, validation, or user-facing contracts need to be stated before implementation.

Use `architecture` when a change affects repository boundaries, dependencies, generated assets, plugin packaging, data flow, control flow, security, performance, migration, or long-lived design decisions.

Use `plan` when work spans multiple files, milestones, risky edits, migration steps, or separate reviewable slices.

Use `test-spec` before implementation when requirements need traceable test coverage.

Use `implement` only after the needed upstream artifacts are stable enough to code.

Use `code-review` after implementation and before final closeout for validator, installer, CI, template, high-risk skill, or multi-file changes.

Use `explain-change` after meaningful implementation or governance changes when reviewers need durable rationale.

Use `verify` for final branch readiness. `verify` owns branch-ready claims.

Use `pr` after verification when the change is ready for review handoff. `pr` owns PR-body and PR-open readiness.

Use `learn` after incidents, repeated review findings, workflow gaps, validation gaps, or explicit owner requests to preserve lessons.

## Implementation gates

Implementation is allowed only when the required upstream state is present for the change size and risk.

Small editorial changes MAY proceed directly with validation.

Adding a skill, changing a skill output contract, changing validation behavior, changing installer behavior, adding dependencies, or repositioning the project requires written requirements first.

Architecture review is required before implementation when a change adds new components, dependencies, generated assets, external services, data flow, plugin packaging behavior, or long-lived repository structure.

## Validation evidence

Every workflow closeout must report:

- changed files;
- validation commands run;
- warnings or skipped checks;
- unresolved questions;
- next stage or stop condition.

The default validation command is:

```bash
python tests/validate_skills.py
```

Targeted checks should match the change. Examples include stale-name searches after a rename, README marker checks after a vision sync, and fixture checks after validator updates.

## Current known gaps

No current workflow gaps are recorded here. Add gaps only when they affect stage routing or artifact ownership.
