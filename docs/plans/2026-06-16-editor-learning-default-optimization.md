# Plan: Editor Learning Default Optimization

## Status

- Plan lifecycle state: active
- Terminal disposition: none

## Purpose / big picture

This plan sequences the accepted `editor` learning-default optimization into reviewable implementation work. The change replaces the current notes-on-request behavior with a default `Learning notes` block after the polished or translated deliverable, while preserving explicit suppression, deliverable-first output, response-language framing, target-language overrides, fidelity, restraint, and integrity boundaries.

## Source artifacts

- Proposal: `docs/proposals/2026-06-16-editor-learning-default-optimization.md`
- Spec: `specs/editor-learning-default-optimization.md`
- Architecture: not-required; spec-review R3 records no runtime architecture impact for this pure prompt behavior change.
- Test spec: `specs/editor-learning-default-optimization.test.md`
- Reviews:
  - `docs/changes/2026-06-16-editor-learning-default-optimization/reviews/proposal-review-r2.md`
  - `docs/changes/2026-06-16-editor-learning-default-optimization/reviews/spec-review-r3.md`
  - `docs/changes/2026-06-16-editor-learning-default-optimization/reviews/plan-review-r1.md`
  - `docs/changes/2026-06-16-editor-learning-default-optimization/reviews/test-spec-approval-r1.md`
- Review resolution: `docs/changes/2026-06-16-editor-learning-default-optimization/review-resolution.md`
- Prior related spec extended by this change: `specs/editor-expert-quality-optimization.md`

## Context and orientation

The prompt behavior is owned by `skills/editor/SKILL.md`. It currently still says notes appear only when explicitly requested and uses `Note` / `说明` labels, so the implementation must revise the description, non-negotiables, workflow, labels, and output templates around default `Learning notes` / `学习要点`.

Reviewer-visible behavior is owned by `tests/evals/skills/editor/cases.yaml`. The current fixture still expects no default explanatory notes in several editor scenarios, so it must be updated before prompt implementation to cover default learning notes, explicit suppression, ambiguity fallback, fallback notes for no-substantive-lesson cases, and integrity-boundary learning behavior.

Change-local evidence belongs under `docs/changes/2026-06-16-editor-learning-default-optimization/`. Baseline evidence must be recorded before editing `skills/editor/SKILL.md`; post-change evidence must compare the same scenario classes against the revised prompt contract.

No runtime components, tools, generated prompt assets, installer behavior, repository-wide validator behavior, dependencies, or live model CI are planned.

## Non-goals

- Do not redesign the whole `editor` skill.
- Do not make `editor` a standalone writing-coach skill.
- Do not change skills other than `editor`.
- Do not add tools, scripts, generated assets, external services, installer behavior, validator behavior, dependencies, or live model CI.
- Do not add a long assessment, grading section, report section, or default `Why` section.
- Do not produce bilingual learning notes by default.
- Do not change default visible target-language behavior except where the approved spec adds learning notes after visible deliverables.
- Do not implement before plan-review and test-spec are complete.

## Requirements covered

- R1-R5, AC2-AC4: M2.
- R6-R11, R31, R33-R35a, AC5-AC11: M2, with eval coverage from M1 and evidence in M3.
- R12-R18, R21-R25, AC12-AC17: M2, with eval coverage from M1 and evidence in M3.
- R19-R20, R22, AC15: M2 and M3.
- R26-R30, AC10-AC11: M2, with suppression and ambiguity evals from M1 and evidence in M3.
- R32, AC18: M2, with integrity-boundary eval coverage from M1 and evidence in M3.
- R36: M2.
- R37-R38, AC19-AC20: M1 and M3.
- AC1: completed before plan authoring through upstream status settlement.
- AC21: M1-M3 validation and final implementation handoff.

## Current Handoff Summary

- Current milestone: M2. Editor prompt learning-default implementation
- Current milestone state: review-requested
- Last reviewed milestone: M1. Eval fixture and baseline evidence
- Review status: M2 implementation ready for code-review
- Remaining in-scope implementation milestones: M2, M3
- Next stage: code-review for M2
- Final closeout readiness: not ready
- Reason final closeout is or is not ready: M2, M3, explain-change closeout, verification, and PR handoff remain.

## Milestones

### M1. Eval fixture and baseline evidence

- Milestone state: closed
- Goal: Update the editor eval fixture for the learning-default contract and record baseline evidence before changing `skills/editor/SKILL.md`.
- Requirements: R37-R38, AC19-AC20, plus eval coverage for R6-R35a.
- Files/components likely touched:
  - `tests/evals/skills/editor/cases.yaml`
  - `docs/changes/2026-06-16-editor-learning-default-optimization/baseline-evidence.md`
- Dependencies:
  - Plan-review must approve this plan.
  - Test spec must define traceable cases before implementation starts.
  - `skills/editor/SKILL.md` must remain unchanged until baseline evidence is recorded.
- Tests to add/update:
  - Default substantive edit with `Learning notes` and concrete anchoring.
  - Explicit English target with `Learning notes`.
  - Explicit no-notes suppression.
  - Ambiguous brevity fallback.
  - Trivial-only correction with exactly one fallback note.
  - Already-good text with at most one restraint note.
  - Brittle-rule fallback or qualified rule.
  - Mixed-language response framing for learning labels.
  - Integrity-boundary refusal with truth-preserving note behavior.
- Implementation steps:
  - Update `tests/evals/skills/editor/cases.yaml` to stop expecting no default notes and to require the approved learning-default scenarios.
  - Capture current baseline behavior for the same scenario classes before prompt edits.
  - Record baseline learning value, bloat risk, over-editing risk, and fidelity observations in `baseline-evidence.md`.
- Validation commands:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check`
- Expected observable result: eval fixture expresses the approved learning-default behavior, baseline evidence exists, and `skills/editor/SKILL.md` has no M1 diff.
- Implementation result: eval fixture now expresses the approved learning-default behavior, baseline evidence exists, and `skills/editor/SKILL.md` has no M1 diff.
- Review result: code-review M1 R1 returned clean-with-notes with no material findings.
- Commit message: `M1: add editor learning evals and baseline evidence`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Baseline evidence could accidentally describe intended behavior rather than current behavior.
  - Updating evals before prompt implementation will intentionally create a gap between current prompt and desired behavior.
- Rollback/recovery:
  - Revert fixture and baseline evidence changes for M1; do not touch the prompt until baseline evidence is corrected.

### M2. Editor prompt learning-default implementation

- Milestone state: review-requested
- Goal: Update `skills/editor/SKILL.md` so the prompt implements default `Learning notes`, explicit suppression, fallback-note behavior, anchoring, and no-padding rules while preserving the expert editor contract.
- Requirements: R1-R36, AC2-AC18.
- Files/components likely touched:
  - `skills/editor/SKILL.md`
  - `README.md` only if it mirrors the changed editor description or output contract.
- Dependencies:
  - M1 baseline evidence complete.
  - Test spec complete.
- Tests to add/update:
  - No validator logic change expected.
  - Prompt behavior is checked against the eval fixture and M3 evidence.
- Implementation steps:
  - Update frontmatter description to mention learning from edits to shared text without advertising standalone writing coaching.
  - Replace notes-on-request rules with default `Learning notes` / `学习要点` behavior.
  - Define explicit output-only/no-explanation suppression and ambiguous brevity fallback.
  - Add substantive-note anchoring rules and fallback-note rules for trivial-only, already-good, brittle-rule, no-substantive-lesson, and integrity-boundary cases.
  - Update default, explicit target-language, and explicit suppression output templates.
  - Preserve language-role separation, target-language overrides, source-language editing, fidelity, restraint, and integrity boundaries from the existing expert editor contract.
- Validation commands:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check`
  - `wc -l skills/editor/SKILL.md`
- Expected observable result: `skills/editor/SKILL.md` implements the approved default learning-notes contract and remains a pure prompt skill with `name: editor`, `$ARGUMENTS`, and `## Output Format`.
- Implementation result: `skills/editor/SKILL.md` implements default `Learning notes`, explicit suppression, fallback-note behavior, anchoring, no-padding rules, response-language labels, target-language templates, and integrity-boundary note behavior. README was updated because it mirrors editor behavior.
- Commit message: `M2: implement editor learning notes default`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Default notes could reintroduce report-generator bloat.
  - Suppression matching could become too broad and hide the new default.
  - Fallback notes could become generic self-commentary if not constrained.
- Rollback/recovery:
  - Revert `skills/editor/SKILL.md` and README changes from M2; keep M1 fixture and evidence available for a narrower implementation.

### M3. Post-change evidence and validation

- Milestone state: planned
- Goal: Record post-change evidence, compare it against baseline scenario classes, and prepare the implementation for code review.
- Requirements: R37-R38, AC19-AC21.
- Files/components likely touched:
  - `docs/changes/2026-06-16-editor-learning-default-optimization/post-change-evidence.md`
  - `docs/plans/2026-06-16-editor-learning-default-optimization.md`
  - `docs/changes/2026-06-16-editor-learning-default-optimization/review-log.md` only when later reviews are recorded.
- Dependencies:
  - M2 prompt implementation complete.
- Tests to add/update:
  - Post-change evidence should cover the same scenario classes as M1 and the test spec.
- Implementation steps:
  - Record post-change evidence for default substantive learning notes, explicit suppression, ambiguous brevity fallback, typo fallback, restraint fallback, brittle-rule behavior, mixed-language labels, explicit target output, and integrity boundaries.
  - Compare post-change behavior against baseline for learning value, bloat, over-editing, and fidelity.
  - Run required validation commands and record prompt line count.
  - Update plan progress, validation notes, and current handoff to request code review.
- Validation commands:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check`
  - `wc -l skills/editor/SKILL.md`
- Expected observable result: post-change evidence and validation are complete enough to hand M1-M3 to code review.
- Commit message: `M3: record editor learning evidence and validation`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Static evidence may not prove behavior on the weakest supported model.
  - Prompt line count or complexity may grow enough to reduce portability.
- Rollback/recovery:
  - Keep deterministic fixture and evidence work; if weakest-model smoke is unavailable, state it explicitly and proceed only if spec-required validation remains satisfied.

## Validation plan

- `python tests/validate_skills.py`: required skill validation and eval-fixture check.
- `python -m unittest discover tests`: full local unit test suite after fixture, prompt, and evidence changes.
- `python tests/check_readme_sync.py`: required because the helper exists in this repository.
- `git diff --check`: whitespace and patch hygiene.
- `wc -l skills/editor/SKILL.md`: prompt-size sanity check after prompt edits.

## Risks and recovery

- Risk: Default `Learning notes` causes report-like verbosity.
  - Recovery: Keep notes after deliverables, cap them, and require fallback notes instead of padded explanations.
- Risk: Suppression behavior becomes too permissive.
  - Recovery: Keep suppression explicit-only and test ambiguous brevity cues separately.
- Risk: The prompt invents edits to create lessons.
  - Recovery: Keep no-over-editing requirements and already-good/trivial-only eval cases.
- Risk: The new spec conflicts with the prior expert editor notes-on-request spec.
  - Recovery: Treat `specs/editor-learning-default-optimization.md` as superseding only the conflicting notes/default-teaching requirements, especially prior R23 and AC12.
- Risk: README mirrors old editor behavior.
  - Recovery: Update README only if inspection shows the changed editor description or output contract is duplicated there.

## Dependencies

- Spec status must be approved before downstream reliance; this was settled during plan authoring.
- Plan-review must approve this plan before test-spec authoring or implementation.
- Test spec must be written and reviewed before implementation starts.
- M1 baseline evidence must precede any edit to `skills/editor/SKILL.md`.
- No architecture artifact is required for this pure prompt behavior change unless plan-review identifies a repository-boundary gap.

## Progress

- 2026-06-16: Upstream status settlement completed during plan authoring: `specs/editor-learning-default-optimization.md` moved from `draft` to `approved` based on spec-review R3 with no material findings.
- 2026-06-16: Created active plan for editor learning-default optimization and added it to `docs/plan.md`.
- 2026-06-16: Plan-review R1 approved the execution plan for test-spec authoring.
- 2026-06-16: Test spec was authored at `specs/editor-learning-default-optimization.test.md` and owner-approved by `docs/changes/2026-06-16-editor-learning-default-optimization/reviews/test-spec-approval-r1.md`.
- 2026-06-16: M1 implementation updated `tests/evals/skills/editor/cases.yaml` with learning-default scenarios before prompt edits.
- 2026-06-16: M1 implementation recorded baseline evidence in `docs/changes/2026-06-16-editor-learning-default-optimization/baseline-evidence.md` while `skills/editor/SKILL.md` had no diff.
- 2026-06-16: M1 implementation added change-local metadata pack: `change.yaml` and active `explain-change.md`.
- 2026-06-16: M1 was review-requested for code review.
- 2026-06-16: Code-review M1 R1 closed M1 clean-with-notes with no material findings.
- 2026-06-16: M2 implementation updated `skills/editor/SKILL.md` to replace notes-on-request behavior with default `Learning notes` while preserving the expert editor contract.
- 2026-06-16: M2 implementation updated `README.md` because the editor table row and skill detail section mirror the changed output contract.
- 2026-06-16: M2 is review-requested for code review.

## Aligned-surface audit

| Surface | M1 status | Rationale |
| --- | --- | --- |
| `skills/editor/SKILL.md` | unaffected with rationale | M1 must capture baseline before prompt edits; prompt implementation is M2. |
| `tests/evals/skills/editor/cases.yaml` | updated | M1 owns eval fixture coverage for the learning-default contract. |
| `docs/changes/2026-06-16-editor-learning-default-optimization/baseline-evidence.md` | added | M1 owns baseline-first evidence before prompt edits. |
| `README.md` | unaffected with rationale | README does not change until prompt behavior changes in M2, and only if it mirrors editor behavior. |
| `tests/validate_skills.py` | unaffected with rationale | No validator behavior change is in scope; existing fixture schema represents the proof surface. |
| `install.sh` | unaffected with rationale | No installation behavior change is in scope. |

### M2 aligned-surface audit

| Surface | M2 status | Rationale |
| --- | --- | --- |
| `skills/editor/SKILL.md` | updated | M2 owns prompt implementation for default `Learning notes`. |
| `README.md` | updated | README mirrors editor behavior in the skills table and detail section. |
| `tests/evals/skills/editor/cases.yaml` | unaffected with rationale | Eval fixture was already updated in M1 and remains the proof surface for M2 behavior. |
| `docs/changes/2026-06-16-editor-learning-default-optimization/post-change-evidence.md` | unaffected with rationale | Post-change evidence belongs to M3 after prompt implementation review. |
| `tests/validate_skills.py` | unaffected with rationale | No validator behavior change is in scope. |
| `install.sh` | unaffected with rationale | No installation behavior change is in scope. |

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-06-16 | Use three implementation milestones: eval/baseline, prompt implementation, post-change evidence/validation | Preserves baseline-before-edit ordering and keeps review slices coherent | One large milestone that hides evidence ordering |
| 2026-06-16 | Treat architecture as not required for this slice | Spec-review R3 records no runtime architecture impact and the change stays inside prompt/eval/evidence artifacts | Create architecture artifact for a pure prompt output-contract change |
| 2026-06-16 | Keep fallback-note cases in the same prompt implementation milestone as default notes | The fallback behavior is part of the same output contract and should be implemented consistently | Split fallback notes into a later follow-up |

## Surprises and discoveries

- `skills/editor/SKILL.md` still says notes appear only when explicitly requested.
- `tests/evals/skills/editor/cases.yaml` still contains expected behavior that rejects default explanatory notes, so fixture updates must happen before prompt implementation.
- No separate editor workflow diagram was found in the current sandbox during proposal authoring; if one appears before implementation, it should be updated with the same default teaching logic.

## Validation notes

- 2026-06-16: `python tests/validate_skills.py` passed during plan authoring with the existing non-blocking grandfathered-evals warning.
- 2026-06-16: `python -m unittest discover tests` passed during plan authoring.
- 2026-06-16: `python tests/check_readme_sync.py` passed during plan authoring.
- 2026-06-16: `git diff --check` passed during plan authoring.
- 2026-06-16: M1 fixture-first `python tests/validate_skills.py` passed with the existing non-blocking grandfathered-evals warning for unrelated skills.
- 2026-06-16: M1 `python tests/validate_skills.py` passed with the existing non-blocking grandfathered-evals warning for unrelated skills.
- 2026-06-16: M1 `python -m unittest discover tests` passed, 31 tests OK.
- 2026-06-16: M1 `python tests/check_readme_sync.py` passed.
- 2026-06-16: M1 `git diff -- skills/editor/SKILL.md` produced no output; prompt was not edited.
- 2026-06-16: M1 `git diff --check` passed.
- 2026-06-16: M1 trailing-whitespace check on changed M1 artifacts passed.
- 2026-06-16: Code-review M1 R1 direct checks passed: required scenario IDs present, `python tests/validate_skills.py` passed with the existing unrelated grandfathered-evals warning, `git diff --check HEAD~1..HEAD` passed, and `git diff HEAD~1..HEAD -- skills/editor/SKILL.md` produced no output.
- 2026-06-16: M2 `python tests/validate_skills.py` passed with the existing non-blocking grandfathered-evals warning for unrelated skills.
- 2026-06-16: M2 `python -m unittest discover tests` passed, 31 tests OK.
- 2026-06-16: M2 `python tests/check_readme_sync.py` passed.
- 2026-06-16: M2 `git diff --check` passed.
- 2026-06-16: M2 `wc -l skills/editor/SKILL.md` returned 175 lines.
- 2026-06-16: M2 stale notes-on-request search passed; only the retained `No default Why` rule remains by design.

## Outcome and retrospective

- M1 is closed by code-review M1 R1. M2 implementation is review-requested. M3 remains unimplemented; downstream gates remain.

## Readiness

- See `Current Handoff Summary`.
- Ready for code-review of M2. Readiness is not Done; M2 review, M3, explain-change closeout, verify, and PR handoff remain.
