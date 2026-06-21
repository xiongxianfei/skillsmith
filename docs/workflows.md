# Skillsmith Workflow Guide

## Purpose

This guide maps Skillsmith's local artifacts to the standard spec-driven, test-driven workflow. It tells agents where lifecycle evidence belongs; the specialized stage skills still own the content of proposals, specs, architecture records, plans, reviews, implementation, verification, PR handoff, and learning records.

Treat this file as the project-local workflow contract and artifact-location map. When this guide conflicts with higher-priority governance, follow the source order below and update this guide rather than relying on chat history.

## Source order

Use this order when artifacts conflict:

1. `CONSTITUTION.md`
2. `VISION.md`
3. Approved specs under `specs/` or change-local docs under `docs/changes/`
4. Architecture, workflow, and project-map docs under `docs/`
5. Execution plans and test specs
6. Tests and CI configuration
7. Implementation files
8. README, contribution docs, and chat history

## Standard lifecycle

Non-trivial changes follow this path:

```text
proposal -> proposal-review -> spec -> spec-review -> architecture -> architecture-review -> plan -> plan-review -> test-spec -> implement -> code-review -> review-resolution when triggered -> ci-maintenance when triggered -> explain-change -> verify -> pr
```

Manual invocation of one skill is allowed and remains isolated unless the user explicitly asks to continue through the full workflow or an active workflow-managed context requires continuation.

## Artifact locations

Use existing files when they already own the topic. For new lifecycle artifacts, prefer these paths:

| Artifact type | Canonical location |
|---|---|
| Agent guidance | `AGENTS.md` |
| Constitution | `CONSTITUTION.md` |
| Vision | `VISION.md` |
| Workflow guide | `docs/workflows.md` |
| Project map | `docs/project-map.md` |
| Strategic positioning | `docs/vision/strategic-positioning.md` |
| Change metadata | `docs/changes/<change-id>/change.yaml` |
| Change-local proposal | `docs/changes/<change-id>/proposal.md` |
| Top-level proposal | `docs/proposals/YYYY-MM-DD-slug.md` |
| Durable product or skill spec | `specs/<slug>.md` |
| Durable test spec | `specs/<slug>.test.md` |
| Change-local spec | `docs/changes/<change-id>/spec.md` |
| Change-local architecture | `docs/changes/<change-id>/architecture.md` |
| System architecture | `docs/architecture/system/architecture.md` |
| Plan body | `docs/plans/YYYY-MM-DD-slug.md` |
| Plan lifecycle index | `docs/plan.md` |
| Plan lifecycle archive | `docs/plan-archive.md` |
| Change-local test spec | `docs/changes/<change-id>/test-spec.md` |
| Review record | `docs/changes/<change-id>/reviews/<stage>-r<n>.md` |
| Review log | `docs/changes/<change-id>/review-log.md` |
| Review resolution | `docs/changes/<change-id>/review-resolution.md` |
| Explain-change record | `docs/changes/<change-id>/explain-change.md` |
| Verify report | `docs/changes/<change-id>/verify-report.md` |
| PR handoff | `docs/changes/<change-id>/pr.md` |
| Learn session | `docs/learn/sessions/YYYY-MM-DD-slug.md` |
| Learn topic | `docs/learn/topics/<topic>.md` |
| Cross-change follow-ups | `docs/follow-ups.md` |

Use `docs/changes/<change-id>/` for workflow-managed work that needs traceability across requirements, design, plan, tests, implementation, review, verification, and PR handoff.

Use top-level `specs/` for durable product or skill contracts that should outlive one change.

Use `docs/plans/YYYY-MM-DD-slug.md` for detailed plan bodies. `docs/changes/<change-id>/plan.md` is non-canonical and should be treated as historical or rejected unless an older artifact explicitly explains why it exists.

## Change IDs

Use lowercase dated slugs:

```text
YYYY-MM-DD-short-name
```

Example:

```text
docs/changes/2026-05-25-add-skill-validator-rules/
```

## Plan Index And Archive

`docs/plan.md` is lifecycle index bookkeeping, not a milestone journal. Keep it bounded:

- `Active` contains active or blocked plan bodies that still own current routing.
- `Blocked` contains plans that cannot move without a named decision, dependency, or external event.
- `Done (recent)` contains only a short recent window of terminal plan history when that helps current routing.
- `docs/plan-archive.md` contains older terminal plan history, including superseded, abandoned, archived, or completed plans that no longer have active routing context.

Write plan references in both files as relative Markdown links such as `[Editor plan](plans/YYYY-MM-DD-slug.md)`.

Move superseded entries out of `docs/plan.md` when they no longer carry active routing context. Keep superseded entries in `docs/plan.md` only while the active index genuinely needs the replacement context and the entry names both `superseded by:` and a non-empty `active-context:`.

## Follow-up Routing

Route future work to the artifact that can act on it:

- active plan work goes in the active plan body and `docs/plan.md`;
- review-driven work goes in `review-log.md` and, when needed, `review-resolution.md`;
- release or PR handoff work goes in the change-local PR or verify artifacts;
- durable lessons go in `docs/learn/sessions/` and confirmed topic files;
- cross-change work with no better owner goes in `docs/follow-ups.md`.

Do not put deferred execution work in `docs/project-map.md`; project maps orient readers and do not own future work.

## Stage routing

Use `explore` before proposal when the problem, user value, or option set is not stable.

Use `research` before proposal, spec, architecture, or implementation when current external facts, platform behavior, standards, laws, pricing, security limits, or dependency behavior affect correctness.

Use `proposal` when a direction needs decision framing before requirements.

Use `proposal-review` when a proposal needs challenge before downstream reliance.

Use `spec` when observable behavior, compatibility, safety, validation, or user-facing contracts need to be stated before implementation.

Use `spec-review` when requirements need challenge before architecture, planning, test planning, or implementation.

Use `architecture` when a change affects repository boundaries, dependencies, generated assets, plugin packaging, data flow, control flow, security, performance, migration, or long-lived design decisions.

Use `architecture-review` before implementation when architecture is material or hard to reverse.

Use `plan` when work spans multiple files, milestones, risky edits, migration steps, or separate reviewable slices.

Use `plan-review` before implementation when the execution sequence, validation plan, or recovery path needs challenge.

Use `test-spec` before implementation when requirements need traceable test coverage.

Use `implement` only after the needed upstream artifacts are stable enough to code.

Use `code-review` after implementation and before final closeout for validator, installer, CI, template, high-risk skill, or multi-file changes.

Use `review-resolution` when a material review finding needs action, owner decision, or re-review evidence.

Use `ci-maintenance` only when CI infrastructure or workflow coverage changes are triggered.

Use `explain-change` after meaningful implementation or governance changes when reviewers need durable rationale.

Use `verify` for final branch readiness. `verify` owns branch-ready claims.

Use `pr` after verification when the change is ready for review handoff. `pr` owns PR-body and PR-open readiness.

Use `learn` after incidents, repeated review findings, workflow gaps, validation gaps, or explicit owner requests to preserve lessons.

## Implementation gates

Implementation is allowed only when the required upstream state is present for the change size and risk.

Small editorial changes may proceed directly with validation when they do not change behavior, scope, safety posture, or public contracts.

Adding a skill, changing a skill output contract, changing validation behavior, changing installer behavior, adding dependencies, or repositioning the project requires written requirements first.

Architecture review is required before implementation when a change adds new components, dependencies, generated assets, external services, data flow, plugin packaging behavior, or long-lived repository structure.

## Review and claim routing

Readiness is not Done. Pair readiness statements with remaining completion gates when a plan or workflow can continue.

`verify` owns branch-ready claims. `pr` owns PR-body and PR-open readiness.

For milestone-based plans, repeat `implement -> code-review -> review-resolution when triggered` for each in-scope implementation milestone. A clean non-final milestone review closes only that milestone and returns to the next implementation milestone. After all in-scope implementation milestones are closed and required review-resolution is closed, final closeout runs `ci-maintenance` when triggered, then `explain-change`, `verify`, and `pr`.

Review logs must not list open material findings before review-resolution closeout is treated as closed. A stage-owned non-approval outcome that requires revision needs same-stage re-review or explicit owner closeout evidence.

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

Targeted checks should match the change. Examples include stale-name searches after a rename, README marker checks after a vision sync, fixture checks after validator updates, and plan-index consistency checks after plan lifecycle changes.

## Current known gaps

No current workflow gaps are recorded here. Add gaps only when they affect stage routing or artifact ownership.
