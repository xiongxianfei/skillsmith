# Plan: Editor skill optimization

## Status

- Plan lifecycle state: active
- Terminal disposition: none

## Purpose / big picture

This plan sequences the accepted `editor` skill optimization into reviewable implementation work. The change must prove current behavior first, add the required eval fixture, then update only `skills/editor/SKILL.md` so the skill returns concise, intent-sensitive editing and translation outputs without a fixed three-stage report.

## Source artifacts

- Proposal: `docs/proposals/2026-05-25-editor-skill-optimization.md`
- Spec: `specs/editor-skill-optimization.md`
- Architecture: not-required; no runtime boundaries, dependencies, generated assets, data flow, or installer behavior change
- Test spec: `specs/editor-skill-optimization.test.md`
- Reviews:
  - `docs/changes/2026-05-25-editor-skill-optimization/reviews/proposal-review-r2.md`
  - `docs/changes/2026-05-25-editor-skill-optimization/reviews/spec-review-r2.md`
  - `docs/changes/2026-05-25-editor-skill-optimization/reviews/plan-review-r1.md`
  - `docs/changes/2026-05-25-editor-skill-optimization/reviews/test-spec-approval-r1.md`

## Upstream status settlement

- Upstream artifact: `specs/editor-skill-optimization.md`
- Review evidence: spec-review R2 approved with no material findings; review log records `spec approved`
- Previous status: draft
- New status: approved
- Settlement result: updated
- Settlement blocker: none

## Context and orientation

- The behavior owner is `skills/editor/SKILL.md`.
- The eval evidence owner is `tests/evals/skills/editor/cases.yaml`.
- Change lifecycle evidence lives under `docs/changes/2026-05-25-editor-skill-optimization/`.
- The current `editor` prompt is a pure Markdown prompt with YAML frontmatter, `$ARGUMENTS`, and `## Output Format`.
- The current prompt forces a Chinese-language three-stage flow: deep text optimization, language-quality assessment, and Chinese-English bilingual translation.
- The approved spec requires conditional output modes, no default notes for simple edits, no automatic Chinese-English bilingual output, targeted Russian translation behavior, and integrity-boundary handling.
- `editor` is in the grandfathering baseline, but this material prompt change requires `tests/evals/skills/editor/cases.yaml` before merge.

## Non-goals

- Do not optimize any skill other than `editor`.
- Do not modify high-risk skills such as `doctor` or `oscp-coach`.
- Do not add live model CI, runtime tools, scripts, generated prompt assets, or external dependencies.
- Do not rename `editor`.
- Do not remove translation support.
- Do not change repository-wide validator behavior unless implementation proves the existing eval-fixture path cannot represent this material skill change.
- Do not proceed to implementation before plan review and test spec are complete.

## Requirements covered

- R1-R4: M2
- R5-R18: M2, with fixture coverage from M1 and test-spec traceability
- R19-R20: M2 and M3
- R21-R23: M1
- R24-R25: M1 and M3
- R26-R28: M1-M3 scope checks
- AC1: already satisfied by spec
- AC2: M1
- AC3: M1
- AC4: M3
- AC5-AC10: M2 and M3
- AC11: M2 and M3
- AC12-AC15: M3

## Current Handoff Summary

- Current milestone: M1
- Current milestone state: review-requested
- Last reviewed milestone: none
- Review status: M1 implementation complete; code-review requested
- Remaining in-scope implementation milestones: M1 pending review, M2, M3
- Next stage: code-review M1
- Final closeout readiness: not ready
- Reason final closeout is or is not ready: implementation, code review, explain-change, verification, and PR handoff have not started.

## Milestones

### M1. Eval fixture and baseline evidence

- Milestone state: review-requested
- Goal: Add the required `editor` eval fixture and record baseline behavior before modifying the skill prompt.
- Requirements: R21, R22, R23, R24, R26, R28, AC2, AC3, AC11
- Files/components likely touched:
  - `tests/evals/skills/editor/cases.yaml`
  - `docs/changes/2026-05-25-editor-skill-optimization/baseline-evidence.md`
  - `docs/changes/2026-05-25-editor-skill-optimization/review-log.md`
- Dependencies:
  - Approved spec
  - Approved plan
  - Approved test spec
- Tests to add/update:
  - Static eval fixture with scenarios for proofreading, indirect PR-description editing, integrity-boundary misuse, and targeted Russian translation
  - Baseline evidence for the current prompt on those same scenarios
- Implementation steps:
  - Create `tests/evals/skills/editor/cases.yaml` using the scenarios from the proposal/spec.
  - Record current `skills/editor/SKILL.md` behavior against each scenario before editing the skill prompt.
  - Confirm the fixture categories satisfy the skill-quality validator: normal, indirect-trigger, and misuse coverage.
- Validation commands:
  - `python tests/validate_skills.py`
  - `python -m unittest tests/test_eval_fixtures.py`
  - `git diff --check`
- Expected observable result: The repository has concrete eval evidence for the material `editor` change before the prompt is modified.
- Commit message: `M1: add editor eval fixture and baseline evidence`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Baseline evidence could accidentally describe desired behavior rather than current behavior.
  - Fixture expectations could drift from the approved spec.
- Rollback/recovery:
  - Revert `tests/evals/skills/editor/cases.yaml` and baseline evidence if the fixture shape or scenarios are rejected during review.
- Result:
  - Added `tests/evals/skills/editor/cases.yaml`.
  - Added `docs/changes/2026-05-25-editor-skill-optimization/baseline-evidence.md`.
  - Confirmed `skills/editor/SKILL.md` was not edited in M1.
  - Validation passed and M1 is ready for code review.

### M2. Editor prompt optimization

- Milestone state: planned
- Goal: Update only `skills/editor/SKILL.md` to satisfy the approved output contract while keeping the skill concise and portable.
- Requirements: R1-R20, R26, R27, R28, AC5, AC6, AC7, AC8, AC9, AC10, AC11
- Files/components likely touched:
  - `skills/editor/SKILL.md`
  - `docs/changes/2026-05-25-editor-skill-optimization/review-log.md`
- Dependencies:
  - M1 closed
- Tests to add/update:
  - No executable test changes expected beyond the M1 fixture unless implementation exposes a validator gap
  - Manual comparison against M1 baseline scenarios
- Implementation steps:
  - Preserve `name: editor`, `$ARGUMENTS`, `allowed-tools: ""`, and `## Output Format`.
  - Rewrite the workflow into conditional output modes: proofread/polish, rewrite, targeted translation, requested notes, and integrity-boundary handling.
  - Remove the mandatory deep optimization, language-quality assessment, and Chinese-English bilingual translation pipeline.
  - Keep translation support for Chinese, English, and Russian, with targeted translation returning only the requested language by default.
  - Keep change notes conditional and concise.
  - Check line count against the current prompt and record whether the optimized prompt is shorter.
- Validation commands:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `git diff --check`
- Expected observable result: The `editor` skill prompt matches the spec contract and stays pure prompt without touching unrelated skills or validator behavior.
- Commit message: `M2: optimize editor skill prompt`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - The prompt could become too terse and lose helpful translation or edit-quality behavior.
  - The description could be changed unnecessarily and alter trigger behavior outside the slice.
  - The rewrite could accidentally broaden unsupported-language behavior beyond the accepted contract.
- Rollback/recovery:
  - Revert `skills/editor/SKILL.md` to the pre-M2 version while keeping M1 fixture evidence available for another prompt revision.

### M3. Post-change evidence and final implementation validation

- Milestone state: planned
- Goal: Compare optimized behavior against the same scenarios, update durable evidence, and prepare for code review.
- Requirements: R19, R20, R25, R26, R27, R28, AC4, AC10, AC11, AC12, AC13, AC14, AC15
- Files/components likely touched:
  - `docs/changes/2026-05-25-editor-skill-optimization/post-change-evidence.md`
  - `docs/changes/2026-05-25-editor-skill-optimization/review-log.md`
  - `docs/plans/2026-05-25-editor-skill-optimization.md`
  - `docs/plan.md`
- Dependencies:
  - M2 closed
- Tests to add/update:
  - Post-change scenario evidence for the same M1 fixture cases
  - Validation notes covering required local commands
- Implementation steps:
  - Record optimized behavior on each M1 scenario.
  - Compare optimized behavior to baseline evidence and call out behavior improvements or residual risks.
  - Record prompt length result and any length justification if needed.
  - Run full required validation commands.
  - Update the current handoff summary to `review-requested` for code review.
- Validation commands:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check`
- Expected observable result: Reviewers can compare baseline and optimized behavior, validation passes, and M3 is ready for code review.
- Commit message: `M3: record editor optimization evidence`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Post-change evidence could show the prompt still over-produces.
  - README sync could unexpectedly fail if metadata changed.
- Rollback/recovery:
  - Reopen M2 for prompt adjustment if evidence does not satisfy the spec.
  - Revert M3 evidence-only files if they are incomplete or inaccurate.

## Validation plan

- `python tests/validate_skills.py`: required repository skill validation and eval-fixture checks.
- `python -m unittest tests/test_eval_fixtures.py`: targeted eval fixture validator coverage after M1.
- `python -m unittest discover tests`: full repository test suite after prompt/evidence changes.
- `python tests/check_readme_sync.py`: README sync check if helper exists; it exists on this branch.
- `git diff --check`: whitespace and patch hygiene.
- Manual scenario comparison: required baseline and post-change evidence for the four approved editor scenarios.
- Line-count check for `skills/editor/SKILL.md`: prove the prompt is shorter or justify any length increase.

## Risks and recovery

- Risk: The baseline-first process becomes too heavy for one skill.
  - Recovery: Keep evidence files concise and tied only to the four approved scenarios.
- Risk: The optimized prompt under-explains substantial edits.
  - Recovery: Adjust conditional notes behavior within R13-R14 rather than reintroducing default notes.
- Risk: Translation support regresses.
  - Recovery: Use the targeted Russian scenario as a hard review signal and add another scenario only if plan review or test spec requires it.
- Risk: The implementation touches validator behavior or unrelated skills.
  - Recovery: Revert unrelated changes and keep scope to `editor`, its fixture, and evidence files.
- Risk: Prompt length increases.
  - Recovery: Either simplify the prompt or record a concrete behavior-based justification before review.

## Dependencies

- Approved proposal and proposal-review evidence are present.
- Approved spec and spec-review evidence are present.
- Plan-review must approve this plan before test-spec.
- Test spec must exist before implementation.
- No architecture artifact is required unless plan-review identifies a long-lived design or boundary issue.

## Progress

- 2026-05-25: Created execution plan after spec-review R2 approved the spec.
- 2026-05-25: Plan-review R1 approved the plan; drafted `specs/editor-skill-optimization.test.md`.
- 2026-05-25: Owner approved `specs/editor-skill-optimization.test.md` as active proof surface.
- 2026-05-25: Implemented M1 by adding the editor eval fixture and baseline evidence before prompt edits.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-05-25 | Use three implementation milestones | Separates baseline evidence, prompt change, and post-change comparison so reviewers can verify the quality process. | Single combined implementation milestone |
| 2026-05-25 | Do not require a separate architecture artifact | The change is a pure prompt and static eval fixture update with no runtime boundary, dependency, installer, or data-flow change. | Add architecture stage by default |
| 2026-05-25 | Keep test-spec after plan-review | Matches the corrected workflow and lets the test spec trace requirements to planned milestones. | Write test-spec immediately after spec-review |

## Surprises and discoveries

- None yet.

## Validation notes

- `python tests/validate_skills.py` passed after test spec approval metadata update.
- `git diff --check` passed after test spec approval metadata update.
- `python tests/validate_skills.py` passed for M1; 10 skills checked, and the remaining eval warning now excludes `editor`.
- `python -m unittest tests/test_eval_fixtures.py` passed for M1; 9 tests ran.
- `git diff --check` passed for M1.

## Outcome and retrospective

- Pending implementation and downstream closeout.

## Readiness

- See `Current Handoff Summary`.
- Ready for `code-review M1`; not ready for M2, final closeout, verification, or PR.
