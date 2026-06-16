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
| `skills/editor/SKILL.md` | Replaced the hardcoded Chinese + English default with source-language plus companion-language resolution, removed hidden Chinese + English cross-check rendering, simplified learning-note rules, and consolidated output templates into one base shape plus modification rules. | Implements the approved visible language contract and prompt-weight reduction while preserving fidelity, integrity, explicit target handling, target-only behavior, and default learning notes. | Spec R1-R63; test spec T1-T9, T11-T12. | `python tests/validate_skills.py`; stale-text search; prompt line count. |
| `README.md` | Updated the editor table row and detail section to describe source-language plus companion-language output instead of Chinese/English output. | README mirrors public skill behavior and would otherwise advertise the old default. | Spec compatibility/migration section; test spec T13. | `python tests/check_readme_sync.py`; stale-text search. |
| `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/post-change-evidence.md` | Recorded post-change prompt-contract evidence, scenario-class comparison, prompt line count, and validation evidence. | The spec requires post-change evidence against the same scenario classes used for baseline. | Spec R67; test spec T11. | M3 validation; manual evidence review. |
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

M2 intentionally does not:

- record post-change scenario evidence;
- close the final explanation artifact;
- claim final verification, branch readiness, or PR readiness.

Those surfaces belong to M3 and downstream lifecycle stages.

M3 adds post-change scenario evidence and validation records, but still does not claim code-review approval for M3, final verification, branch readiness, or PR readiness.

## Current Handoff

M1 is ready for code-review after validation passes and the milestone handoff commit is created.

This artifact does not claim code-review approval, final verification, branch readiness, PR readiness, or final lifecycle closeout.
