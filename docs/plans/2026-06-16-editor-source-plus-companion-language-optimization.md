# Plan: Editor source-language plus companion-language optimization

## Status

- Plan lifecycle state: active
- Terminal disposition: none

## Purpose / big picture

Implement the accepted editor optimization by changing the skill from a hardcoded Chinese + English default to a source-language + one companion-language contract, while preserving the existing editing philosophy of fidelity with restraint.

This plan keeps the change scoped to prompt behavior, eval evidence, and mirrored documentation. It does not introduce runtime code, live model CI, repository-wide validators, or long-term preference storage.

## Source artifacts

- Proposal: `docs/proposals/2026-06-16-editor-source-plus-companion-language-optimization.md`
- Spec: `specs/editor-source-plus-companion-language-optimization.md`
- Architecture: no canonical architecture artifact required; `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/reviews/architecture-review-r1.md` approved the no-impact architecture rationale.
- Review log: `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/review-log.md`
- Review resolution: `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/review-resolution.md`
- Test spec: `specs/editor-source-plus-companion-language-optimization.test.md`

## Context and orientation

- `skills/editor/SKILL.md` owns the editor prompt behavior. The current prompt is about 188 lines and still centers the visible default around Chinese + English, including hidden cross-check work that this change should remove.
- `tests/evals/skills/editor/cases.yaml` owns reviewer-visible editor eval scenarios. Existing cases are aligned with earlier learning-default behavior and need source + companion-language coverage.
- `README.md` currently describes `editor` as using Chinese/English output. If implementation changes visible editor behavior, README wording must be updated to avoid stale public-facing documentation.
- Change-local evidence should live under `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/`, especially baseline and post-change evidence.
- No runtime architecture, installer, persistence, API, deployment, or CI workflow change is expected.

## Non-goals

- Do not weaken fidelity, restraint, meaning preservation, integrity checks, or unsupported-certainty rules.
- Do not remove learning notes entirely.
- Do not make teaching the primary deliverable.
- Do not add live model CI, scripts, tools, validator changes, or preference storage.
- Do not optimize unrelated skills.
- Do not guarantee expert-quality handling for every possible source language beyond the bounded eval evidence in this change.

## Requirements covered

- Source-language and companion-language defaults: R1-R7, R57-R61, AC2, AC17-AC18.
- Companion-language resolution, explicit targets, multi-target requests, target-only requests, and English-source fallback: R8-R27, R51-R56, AC3-AC7, AC15.
- Learning-note simplification and output consolidation: R28-R50, AC8-AC14.
- Prompt concision, description cleanup, visible-version verification, and removal of hidden cross-check work: R62-R67, AC16, AC19-AC20.
- Spec readiness: AC1 is already satisfied by the approved spec and no-impact architecture review.

## Current Handoff Summary

- Current milestone: M1. Eval fixture and baseline evidence
- Current milestone state: planned
- Last reviewed milestone: plan
- Review status: plan-review approved; test spec authored
- Remaining in-scope implementation milestones: M1-M3
- Next stage: implement M1
- Final closeout readiness: not-ready
- Reason final closeout is not ready: the plan still needs baseline evidence, implementation milestones, code review, change explanation, final verification, and PR handoff.

## Milestones

### M1. Eval fixture and baseline evidence

- State: planned
- Goal: update reviewer-visible editor eval cases for the new language contract and capture baseline evidence before editing the prompt.
- Requirements covered: R13-R56, R64-R67, AC3-AC16, AC19-AC20.
- Files likely touched:
  - `tests/evals/skills/editor/cases.yaml`
  - `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/baseline-evidence.md`
- Scope:
  - Add or update eval cases for Chinese source defaulting to Chinese + English, Russian source defaulting to Russian + English, English source avoiding duplicate English, English source with non-English instruction-language fallback, mixed-language instruction handling, explicit target override, multi-target explicit requests, target-only with notes, target-only with no notes, long-source notes that may exceed three when warranted, trivial corrections without padded teaching, and a complex integrity + explicit target + no-notes conflict.
  - Record pre-change behavior against the current prompt, including current output-language defaults, duplicate-English risk, learning-note weight, template proliferation, hidden cross-check language, and prompt line count.
- Dependencies:
  - Plan-review must approve or request changes before implementation.
  - Test-spec should be written before eval or production prompt changes.
  - Baseline evidence must be captured before `skills/editor/SKILL.md` is edited.
- Validation:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check`
- Result: pending

### M2. Editor prompt implementation

- State: planned
- Goal: revise `editor` to implement the source-language + companion-language contract while reducing prompt weight.
- Requirements covered: R1-R67, AC2-AC18.
- Files likely touched:
  - `skills/editor/SKILL.md`
  - `README.md` if it mirrors editor behavior
- Scope:
  - Make the description trigger-focused and remove detailed execution policy from frontmatter.
  - Add the priority order: integrity, explicit user constraints, source fidelity, core deliverable, teaching, brevity.
  - Define source language, instruction language, response framing language, companion language, and visible output languages.
  - Implement deterministic companion-language resolution, including English default for non-English sources, non-English instruction-language fallback for English sources, and Chinese fallback when no non-English instruction language is available.
  - Define mixed-language instruction handling consistently with the spec.
  - Support explicit target override, multi-target explicit requests, and target-only requests.
  - Keep learning notes default-on but compact, suppressible, anchored when substantive, and rarely more than three unless the source warrants more.
  - Replace template proliferation with one base template and modification rules.
  - Remove hidden cross-check rendering of languages the user cannot inspect.
  - Keep `## Output Format` and `$ARGUMENTS`, and keep the prompt under 500 lines. The revised prompt should be shorter than the pre-change prompt unless the implementation records a justification.
- Dependencies:
  - M1 baseline evidence must exist before prompt edits.
- Validation:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check`
  - `wc -l skills/editor/SKILL.md`
- Result: pending

### M3. Post-change evidence and validation

- State: planned
- Goal: record post-change evidence, run validation, and prepare the implementation for code review.
- Requirements covered: R62-R67, AC2-AC20.
- Files likely touched:
  - `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/post-change-evidence.md`
  - `docs/plans/2026-06-16-editor-source-plus-companion-language-optimization.md`
  - `docs/plan.md`
- Scope:
  - Record post-change prompt line count and compare it to the baseline.
  - Record expected behavior for the updated eval scenarios.
  - Confirm visible outputs preserve meaning and tone without hidden language renderings.
  - Update this plan's progress, handoff summary, validation notes, and milestone states.
  - Hand off to code-review with validation evidence.
- Dependencies:
  - M2 must be implemented and locally validated.
- Validation:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check`
  - `wc -l skills/editor/SKILL.md`
- Result: pending

## Validation plan

Run these commands during implementation closeout unless a command is unavailable, in which case record the reason:

```bash
python tests/validate_skills.py
python -m unittest discover tests
python tests/check_readme_sync.py
git diff --check
wc -l skills/editor/SKILL.md
```

No live model calls should be added to CI.

## Risks and recovery

- Risk: the prompt silently regresses to hardcoded Chinese + English behavior.
  - Recovery: keep explicit eval coverage for Chinese, Russian, English, and mixed-language cases, and revert the M2 prompt slice if validation shows the default is not deterministic.
- Risk: target-only requests and learning notes conflict.
  - Recovery: encode and test the spec rule that target-only suppresses source output, but learning notes remain unless explicitly suppressed.
- Risk: mixed-language instruction handling becomes inconsistent.
  - Recovery: implement the deterministic majority-language and first-clear-non-English fallback rule from the spec and cover it in evals.
- Risk: prompt simplification accidentally weakens fidelity or integrity handling.
  - Recovery: keep hierarchy and misuse eval coverage; restore any removed integrity language needed for behavior.
- Risk: the revised prompt grows instead of shrinking.
  - Recovery: trim duplicated workflow/output rules first; if still larger, record a justification tied to accepted requirements.
- Risk: README becomes stale.
  - Recovery: update the editor row or section when implementation changes public behavior, then run README sync validation if available.

## Dependencies

- Plan-review before test-spec or implementation.
- Test-spec before changing eval fixtures or the production prompt.
- Baseline evidence before editing `skills/editor/SKILL.md`.
- No canonical architecture artifact is required because architecture-review approved the no-impact rationale.

## Progress

- 2026-06-16: Proposal accepted after proposal-review.
- 2026-06-16: Spec approved after spec-review.
- 2026-06-16: Architecture-review approved no canonical architecture update.
- 2026-06-16: Execution plan created and plan index updated.
- 2026-06-16: Plan-review approved the execution plan for test-spec.
- 2026-06-16: Test spec created at `specs/editor-source-plus-companion-language-optimization.test.md`; implementation may begin with M1 only.
- 2026-06-16: Owner approved the test spec for implementation use.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-06-16 | Use three implementation milestones: eval/baseline, prompt implementation, post-change evidence. | Separates evidence capture from prompt edits and keeps review handoffs clear. | Single large implementation milestone. |
| 2026-06-16 | Do not create a canonical architecture artifact. | Architecture-review approved that this is prompt/test/documentation work with no runtime design impact. | Add an ADR or architecture doc with no durable design decision. |
| 2026-06-16 | Treat README update as conditional implementation scope. | README currently mirrors editor output behavior, but exact wording should be changed only with the prompt implementation. | Update README during plan authoring. |

## Surprises and discoveries

- None yet.

## Validation notes

- 2026-06-16 plan authoring validation:
  - `python tests/validate_skills.py` passed with one non-blocking grandfathered-evals warning for unrelated existing skills.
  - `python tests/check_readme_sync.py` passed.
  - `git diff --check` passed.
  - `python -m unittest discover tests` passed, 31 tests.
- 2026-06-16 test-spec authoring validation:
  - `python tests/validate_skills.py` passed with one non-blocking grandfathered-evals warning for unrelated existing skills.
  - `python tests/check_readme_sync.py` passed.
  - `git diff --check` passed.
  - `python -m unittest discover tests` passed, 31 tests.

## Outcome and retrospective

- Pending.

## Readiness

This plan is ready for M1 implementation.

It is not code-review-ready, verified, branch-ready, or PR-ready. Those states require milestone execution, validation evidence, implementation review, durable change explanation, and final verification.
