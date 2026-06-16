# Explain Change: Editor Learning Default Optimization

## Status

active

## Summary

This change updates the `editor` skill contract so polished or translated deliverables remain first, then concise `Learning notes` appear by default unless explicitly suppressed.

The implementation is split into three milestones. M1 updates reviewer-visible eval coverage and records baseline evidence before any prompt edit. M2 will update `skills/editor/SKILL.md`. M3 will record post-change evidence and validation.

## M1 Rationale

M1 changes the proof surface before changing behavior:

| File | M1 change | Reason |
| --- | --- | --- |
| `tests/evals/skills/editor/cases.yaml` | Replaces stale notes-on-request expectations with learning-default scenarios. | The eval fixture must express the accepted contract before prompt implementation. |
| `docs/changes/2026-06-16-editor-learning-default-optimization/baseline-evidence.md` | Records current prompt behavior while `skills/editor/SKILL.md` is still unchanged. | The plan requires baseline-first evidence and comparison of learning value, bloat, over-editing, and fidelity. |
| `docs/changes/2026-06-16-editor-learning-default-optimization/change.yaml` | Adds change-local lifecycle metadata and M1 validation. | Keeps the workflow state auditable for reviewers. |
| `docs/plans/2026-06-16-editor-learning-default-optimization.md` | Tracks M1 progress, validation, and handoff state. | `implement` owns keeping the active plan current during execution. |

## Scope Control

M1 intentionally does not edit `skills/editor/SKILL.md`. The prompt still contains the old notes-on-request contract during baseline capture. That makes the baseline evidence meaningful and keeps the behavior change reserved for M2.

No runtime tools, scripts, generated assets, dependencies, installer behavior, validator behavior, README behavior, or live-model CI are added in M1.

## M2 Rationale

M2 implements the approved prompt behavior change:

| File | M2 change | Reason |
| --- | --- | --- |
| `skills/editor/SKILL.md` | Replaces notes-on-request behavior with default `Learning notes`, explicit suppression, fallback-note rules, anchoring, no-padding, response-language labels, and updated output templates. | Implements spec R1-R36 and preserves the expert editor contract while making teaching default. |
| `README.md` | Updates the editor table row and detail section to mention concise learning notes by default and no-notes overrides. | README mirrors the public editor behavior and must not advertise the old output contract. |
| `docs/plans/2026-06-16-editor-learning-default-optimization.md` | Records M2 progress, aligned-surface audit, validation, and review-requested handoff. | `implement` owns keeping the active plan current. |
| `docs/changes/2026-06-16-editor-learning-default-optimization/change.yaml` | Records M2 validation and handoff state. | Keeps lifecycle metadata reviewable. |

M2 does not change the validator, installer, eval fixture, or other skills. The eval fixture was intentionally updated in M1 before prompt implementation.

## M3 Rationale

M3 adds the post-change proof surface and records final implementation-slice validation:

| File | M3 change | Reason |
| --- | --- | --- |
| `docs/changes/2026-06-16-editor-learning-default-optimization/post-change-evidence.md` | Adds post-change prompt-contract evidence for the same scenario classes used in baseline, including learning value, bloat, over-editing, fidelity, suppression, labels, target-language behavior, and integrity boundaries. | Implements spec R37-R38 and test-spec T14 without adding live model CI. |
| `docs/plans/2026-06-16-editor-learning-default-optimization.md` | Records M3 progress, aligned-surface audit, validation, and review-requested handoff. | Keeps the active plan current for milestone-aware review. |
| `docs/changes/2026-06-16-editor-learning-default-optimization/change.yaml` | Records M3 validation and handoff state. | Keeps lifecycle metadata reviewable. |

M3 does not change the prompt, README, eval fixture, validator, installer, or runtime behavior. The remaining proof question is code review of the M3 evidence and handoff state.

## Validation Evidence

M1-M3 validation is recorded in the active plan and `change.yaml`. The expected validation warning is the existing non-blocking grandfathered-evals warning for unrelated skills without eval fixtures.

## Current Handoff

M1 and M2 are closed. M3 is review-requested for `code-review`.
