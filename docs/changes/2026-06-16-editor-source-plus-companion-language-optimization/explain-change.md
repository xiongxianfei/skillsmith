# Explain Change: Editor Source Plus Companion Language Optimization

## Status

active

## Summary

This change updates the `editor` lifecycle artifacts and proof surfaces for a prompt optimization that will change the default visible output contract from hardcoded Chinese + English to polished source language plus one companion language.

M1 does not edit `skills/editor/SKILL.md`. It establishes the proof surface first by replacing stale editor eval expectations and recording baseline prompt-contract evidence before any production prompt change.

## M1 Diff Rationale

| File | Change | Reason | Source artifact | Test/evidence |
| --- | --- | --- | --- | --- |
| `tests/evals/skills/editor/cases.yaml` | Replaced old learning-default eval scenarios that still expected Chinese + English defaults with source-language plus companion-language scenarios. | The approved spec requires eval evidence for Chinese, Russian, English fallback, explicit target override, target-only behavior, compact notes, trivial correction, integrity priority, and the complex integrity + explicit target + no-notes conflict. | Spec R64-R65; test spec T3-T10. | `python tests/validate_skills.py`; manual scenario coverage. |
| `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/baseline-evidence.md` | Recorded current prompt behavior and line count before editing `skills/editor/SKILL.md`. | The spec requires baseline evidence before prompt edits and post-change evidence against the same scenario classes later. | Spec R66-R67; test spec T11. | Prompt inspection and `wc -l` evidence. |
| `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/change.yaml` | Added compact change metadata for source artifacts, milestone state, review records, and validation tracking. | The implement workflow requires a change-local baseline pack for ordinary non-trivial work. | Implement workflow. | YAML parsed by `python tests/validate_skills.py` indirectly only if referenced by skill validation; manual review for metadata. |
| `docs/plans/2026-06-16-editor-source-plus-companion-language-optimization.md` | Advanced M1 from planned to implementing during work, then to review-requested after validation. | The active plan must remain the source for milestone state and validation evidence. | Implement workflow and plan M1. | Plan review-ready state after validation. |
| `docs/plan.md` | Updated the active plan index to show M1 awaiting code review. | Lifecycle bookkeeping should reflect the current handoff state. | Implement workflow. | Manual index check. |

## Scope Control

M1 intentionally does not:

- edit `skills/editor/SKILL.md`;
- edit `README.md`;
- add or change validator behavior;
- add live model CI;
- add runtime dependencies, tools, scripts, generated assets, installer behavior, or architecture artifacts;
- claim post-change prompt behavior.

Those surfaces belong to later milestones after M1 review.

## Current Handoff

M1 is ready for code-review after validation passes and the milestone handoff commit is created.

This artifact does not claim code-review approval, final verification, branch readiness, PR readiness, or final lifecycle closeout.
