# Plan: Editor Expert Quality Optimization

## Status

- Plan lifecycle state: active
- Terminal disposition: none

## Purpose / big picture

This plan sequences the approved `editor` expert-quality optimization into reviewable implementation work. The change replaces the fixed three-stage report with a concise expert-editor workflow: role-separate instruction/source/target language, edit source text with fidelity and restraint, default visible output to Chinese + English, honor explicit target-language overrides, add notes only when requested, and refuse misleading transformations.

## Source artifacts

- Proposal: `docs/proposals/2026-05-26-editor-expert-quality-optimization.md`
- Spec: `specs/editor-expert-quality-optimization.md`
- Architecture: `docs/architecture/system/architecture.md`
- Test spec: `specs/editor-expert-quality-optimization.test.md`
- Reviews:
  - `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/proposal-review-r5.md`
  - `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/spec-review-r4.md`
  - `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/architecture-review-r2.md`
  - `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/plan-review-r1.md`
  - `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/test-spec-approval-r1.md`
- Superseded plan: `docs/plans/2026-05-25-editor-skill-optimization.md`

## Context and orientation

The runtime behavior is owned by `skills/editor/SKILL.md`. It is currently still the superseded fixed three-stage prompt, so implementation must update the description, expert editing standard, workflow, and output format.

Reviewer-visible behavior is owned by `tests/evals/skills/editor/cases.yaml`. The current fixture also reflects the superseded three-stage workflow and must be replaced with scenarios from `AC17`.

Evidence belongs under `docs/changes/2026-05-26-editor-expert-quality-optimization/`. Baseline evidence must be recorded before editing `skills/editor/SKILL.md`; post-change evidence must compare against the same scenario classes after the prompt changes.

No runtime components, tools, generated prompt assets, installer changes, live model CI, or repository-wide validator changes are planned.

## Non-goals

- Do not optimize skills other than `editor`.
- Do not change `doctor`, `oscp-coach`, or other high-risk skills.
- Do not add runtime tools, scripts, generated assets, external services, or live model calls to CI.
- Do not change installer behavior or repository-wide validation unless implementation proves the existing eval-fixture path cannot represent the spec.
- Do not restore the fixed assessment/`Why`/three-stage report as default output.

## Requirements covered

- R1-R6, AC3-AC4: M2.
- R7-R23, R31-R38, AC5-AC16: M2, with coverage evidence in M1 and M3.
- R24-R30: M2, with eval coverage in M1 and post-change evidence in M3.
- R39-R42: M2 and M3.
- R43-R46, AC17-AC19: M1 and M3.
- R47-R49: M1-M3, with validation and scope checks in M3.
- AC1-AC2: upstream settlement completed during plan authoring.
- AC20-AC24: M3.

## Current Handoff Summary

- Current milestone: M3. Post-change evidence and lifecycle validation
- Current milestone state: closed
- Last reviewed milestone: M3
- Review status: code-review M3 R2 returned clean-with-notes; no review-resolution required
- Remaining in-scope implementation milestones: none
- Next stage: track new artifacts, then verify rerun
- Final closeout readiness: ready to start final closeout
- Reason final closeout is or is not ready: all implementation milestones are closed, review-resolution is closed, and explain-change is complete; final verification is blocked until new authoritative artifacts are tracked.

## Milestones

### M1. Eval fixture and baseline evidence

- Milestone state: closed
- Goal: Replace the stale editor eval fixture with expert-quality scenarios and record baseline behavior before editing `skills/editor/SKILL.md`.
- Requirements: R43-R45, AC17-AC18.
- Files/components likely touched:
  - `tests/evals/skills/editor/cases.yaml`
  - `docs/changes/2026-05-26-editor-expert-quality-optimization/baseline-evidence.md`
- Dependencies:
  - `specs/editor-expert-quality-optimization.test.md` approved or ready enough to guide scenario shape.
  - `skills/editor/SKILL.md` must not be edited before baseline evidence is recorded.
- Tests to add/update:
  - Eval fixture scenarios for professional polish with restraint, already-good restraint, `dim lighting`, Chinese-instruction/English-source, English-instruction/Chinese-source, explicit single-target override, code-switching, non-Chinese/non-English source handling, PR editing, and integrity misuse.
- Implementation steps:
  - Rewrite `tests/evals/skills/editor/cases.yaml` around the approved expert-quality contract.
  - Capture current baseline behavior from the existing fixed three-stage prompt for the same scenario classes.
  - Record baseline mismatch and known failure risk without changing the skill prompt.
- Validation commands:
  - `python tests/validate_skills.py`
  - `python -m unittest tests/test_eval_fixtures.py`
  - `git diff --check`
- Expected observable result: eval scenarios match `AC17`, baseline evidence exists, and prompt file remains unchanged during baseline capture.
- Result: Updated the editor eval fixture with expert-quality scenarios, recorded baseline evidence before prompt edits, added change metadata and in-progress rationale, and confirmed `skills/editor/SKILL.md` has no M1 diff.
- Review result: `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/code-review-m1-r1.md` returned clean-with-notes with no material findings.
- Commit message: `M1: add editor expert evals and baseline evidence`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Baseline capture could accidentally describe intended behavior rather than current behavior.
- Rollback/recovery:
  - Revert the fixture/evidence files for M1; do not touch the prompt until evidence is corrected.

### M2. Editor prompt implementation

- Milestone state: closed
- Goal: Rewrite `skills/editor/SKILL.md` to implement the expert-quality workflow, language-role separation, target-language output contract, and integrity boundary.
- Requirements: R1-R42, R47-R49, AC3-AC16.
- Files/components likely touched:
  - `skills/editor/SKILL.md`
  - README only if it mirrors the changed editor description or output contract.
- Dependencies:
  - M1 baseline evidence must be complete.
  - `specs/editor-expert-quality-optimization.test.md` should be available before implementation.
- Tests to add/update:
  - No automated validator change expected.
  - Prompt behavior is verified through the M1 fixture and M3 evidence.
- Implementation steps:
  - Update frontmatter description to remove fixed three-stage and specific-language support wording while naming expert editing, default Chinese + English output, explicit target overrides, and trigger contexts.
  - Replace the fixed report workflow with role separation, source-language editing, resolved-meaning rendering, cross-checking, and explicit integrity refusal.
  - Define concise target-language-aware output templates, including default CN+EN, explicit target-only output, requested notes, non-CN/EN edited source block, and integrity alternatives.
  - Keep `$ARGUMENTS`, `## Output Format`, pure-prompt boundaries, no emoji, and the 500-line limit.
- Validation commands:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check`
  - `wc -l skills/editor/SKILL.md`
- Expected observable result: `editor` prompt implements the approved output contract and passes repository validation without touching unrelated skills.
- Result: Rewrote `skills/editor/SKILL.md` around the expert-quality role-separation workflow, target-language-aware output templates, explicit target overrides, and integrity-boundary refusal. Updated `README.md` because it mirrored the old fixed three-stage/specific-language contract.
- Review result: `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/code-review-m2-r1.md` requested changes for `F-CODE-EDITOR-M2-001`; `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/code-review-m2-r2.md` returned clean-with-notes with no remaining material findings.
- Review-resolution result: `F-CODE-EDITOR-M2-001` closed after note-bearing and integrity-boundary templates were made to explicitly repeat target-language blocks for every visible target language.
- Commit message: `M2: implement editor expert prompt contract`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - The prompt may overfit the workflow diagram and become too long or procedural for a prompt skill.
  - Explicit target override could weaken the internal cross-check if omitted from instructions.
- Rollback/recovery:
  - Revert `skills/editor/SKILL.md` and any README update from M2; keep M1 evidence available for a narrower rewrite.

### M3. Post-change evidence and lifecycle validation

- Milestone state: closed
- Goal: Record post-change evidence, compare it against baseline scenario classes, and prepare the implementation for code review.
- Requirements: R46-R49, AC19-AC24.
- Files/components likely touched:
  - `docs/changes/2026-05-26-editor-expert-quality-optimization/post-change-evidence.md`
  - `docs/plans/2026-05-26-editor-expert-quality-optimization.md`
  - `docs/changes/2026-05-26-editor-expert-quality-optimization/review-log.md` only when later reviews are recorded.
- Dependencies:
  - M2 prompt implementation complete.
- Tests to add/update:
  - Post-change evidence should cover the same scenario classes as M1.
- Implementation steps:
  - Record post-change evidence for each required scenario class.
  - Compare baseline and post-change behavior against the spec.
  - Run all required validation commands and record line count for `skills/editor/SKILL.md`.
  - Update plan progress, validation notes, and current handoff to request code review.
- Validation commands:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check`
  - `wc -l skills/editor/SKILL.md`
- Expected observable result: evidence and validation are complete enough to hand M1-M3 to `code-review`.
- Result: Added `docs/changes/2026-05-26-editor-expert-quality-optimization/post-change-evidence.md` comparing the optimized prompt against the baseline scenario classes, recorded static prompt-contract proof, noted that no live weakest-model smoke was run, and completed required M3 validation.
- Review result: `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/code-review-m3-r1.md` requested changes for `F-CODE-EDITOR-M3-001`.
- Review-resolution result: `F-CODE-EDITOR-M3-001` closed after the active plan's bottom outcome/readiness sections were updated to match the M3 review-resolution and re-review state.
- Review rerun result: `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/code-review-m3-r2.md` returned clean-with-notes with no remaining material findings.
- Commit message: `M3: record editor expert evidence and validation`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Manual smoke may not be available for the weakest model during implementation.
- Rollback/recovery:
  - Keep deterministic fixture/evidence work; if manual smoke is unavailable, state it explicitly and proceed only if spec-required validation remains satisfied.

## Validation plan

- `python tests/validate_skills.py`: required skill validation and eval-fixture check.
- `python -m unittest tests/test_eval_fixtures.py`: targeted eval-fixture validation after M1.
- `python -m unittest discover tests`: full local unit test suite after prompt/evidence updates.
- `python tests/check_readme_sync.py`: required because the helper exists.
- `git diff --check`: whitespace and patch hygiene.
- `wc -l skills/editor/SKILL.md`: prove prompt remains under the spec line-count limit.

## Risks and recovery

- Risk: Language-role separation fails on mixed-language inputs.
  - Recovery: Keep both mixed-language directions in eval fixture and post-change evidence; revise the prompt before review if either direction is ambiguous.
- Risk: Default Chinese + English output regresses into a report-like structure.
  - Recovery: Enforce no default assessment, no default `Why`, no duplicate source-language block, and notes only when explicitly requested.
- Risk: Explicit single-target override contradicts default bilingual behavior.
  - Recovery: Keep the target-language block pattern shared across default and override templates; test English-only output separately.
- Risk: The old 2026-05-25 plan or spec resurfaces as active guidance.
  - Recovery: Keep old artifacts marked superseded and the new plan active in `docs/plan.md`.

## Dependencies

- Plan review must approve this plan before test-spec authoring or implementation.
- `specs/editor-expert-quality-optimization.test.md` should be authored after plan-review and before implementation.
- M1 baseline evidence must precede any edit to `skills/editor/SKILL.md`.
- No live model CI or validator architecture change is expected.

## Progress

- 2026-05-26: Upstream status settlement completed during plan authoring: proposal accepted, spec approved, architecture approved, review-resolution closed.
- 2026-05-26: Older `docs/plans/2026-05-25-editor-skill-optimization.md` marked superseded by this plan.
- 2026-05-26: New active plan created for the expert-quality optimization path.
- 2026-05-26: Plan-review R1 approved the plan for test-spec.
- 2026-05-26: Test spec created at `specs/editor-expert-quality-optimization.test.md`.
- 2026-05-26: Test-spec approval R1 approved the test spec for implementation.
- 2026-05-26: M1 implemented eval fixture and baseline evidence; milestone moved to review-requested.
- 2026-05-26: Code-review M1 R1 returned clean-with-notes; M1 closed and M2 became the current milestone.
- 2026-05-26: M2 implemented the editor prompt contract and aligned README; milestone moved to review-requested.
- 2026-05-26: Code-review M2 R1 requested changes for `F-CODE-EDITOR-M2-001`; M2 moved to resolution-needed.
- 2026-05-26: Addressed `F-CODE-EDITOR-M2-001`; M2 returned to review-requested for code-review rerun.
- 2026-05-26: Code-review M2 R2 returned clean-with-notes, closed `F-CODE-EDITOR-M2-001`, closed M2, and advanced the active handoff to M3.
- 2026-05-26: M3 added post-change evidence for the same scenario surface as the baseline, ran required validation, and moved to review-requested for code-review M3.
- 2026-05-26: Code-review M3 R1 requested changes for `F-CODE-EDITOR-M3-001`; M3 moved to resolution-needed.
- 2026-05-26: Addressed `F-CODE-EDITOR-M3-001`; M3 returned to review-requested for code-review rerun.
- 2026-05-26: Code-review M3 R2 returned clean-with-notes, closed `F-CODE-EDITOR-M3-001`, closed M3, and advanced the active handoff to final closeout.
- 2026-05-26: Explain-change completed durable change rationale and advanced the active handoff to final verification.
- 2026-05-26: Verify ran final local validation successfully but blocked branch-ready because new authoritative change artifacts are untracked.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-05-26 | Use three implementation milestones: eval/baseline, prompt rewrite, evidence/validation | Keeps baseline capture before prompt edits and gives code review a coherent completed slice | One large milestone that hides evidence ordering |
| 2026-05-26 | Treat the 2026-05-25 editor plan as superseded | The accepted 2026-05-26 proposal supersedes the fixed three-stage editor contract | Continue both editor plans in parallel |
| 2026-05-26 | Keep validator changes out unless forced by fixture limitations | The spec says repository-wide validator changes are out of scope unless the existing eval-fixture path cannot represent the change | Add validator behavior preemptively |
| 2026-05-26 | Use static prompt-contract evidence for M3 instead of live model smoke | The spec forbids live model CI and only recommends weakest-model smoke when available; deterministic validation plus reviewer-readable prompt evidence is sufficient for this milestone handoff | Add live model calls to CI or block M3 on unavailable model smoke |

## Surprises and discoveries

- The existing `tests/evals/skills/editor/cases.yaml` still asserts the superseded fixed three-stage workflow and must be replaced before prompt implementation.
- The existing `skills/editor/SKILL.md` still advertises Chinese, English, and Russian specifically; M2 must remove that specific-language support claim while preserving default Chinese + English target output.
- M1 confirmed `skills/editor/SKILL.md` remained unchanged while baseline evidence was recorded.
- M2 found `README.md` mirrored the old editor 3-phase pipeline, so README was in scope for alignment.
- M3 did not run live weakest-model smoke; the skipped smoke is recorded in `post-change-evidence.md` with static evidence covering the `dim lighting` scenario.

## Validation notes

- 2026-05-26: `python tests/validate_skills.py` passed with the existing non-blocking grandfathered-evals warning for unrelated skills.
- 2026-05-26: `git diff --check` passed.
- 2026-05-26: Test-spec authoring added no executable checks; implementation milestones still own fixture, prompt, evidence, and final validation.
- 2026-05-26 M1: `python tests/validate_skills.py` passed with the existing non-blocking grandfathered-evals warning for unrelated skills.
- 2026-05-26 M1: `python -m unittest tests/test_eval_fixtures.py` passed, 9 tests OK.
- 2026-05-26 M1: `git diff --check` passed.
- 2026-05-26 M1: `git diff -- skills/editor/SKILL.md` produced no output, confirming the prompt was not edited in M1.
- 2026-05-26 code-review M1 R1: reviewer reran `python tests/validate_skills.py`, `python -m unittest tests/test_eval_fixtures.py`, `git diff --check`, and `git diff -- skills/editor/SKILL.md`; all passed with only the existing unrelated grandfathered-evals warning.
- 2026-05-26 M2: `python tests/validate_skills.py` passed with the existing non-blocking grandfathered-evals warning for unrelated skills.
- 2026-05-26 M2: `python -m unittest discover tests` passed, 31 tests OK.
- 2026-05-26 M2: `python tests/check_readme_sync.py` passed.
- 2026-05-26 M2: `git diff --check` passed.
- 2026-05-26 M2: `wc -l skills/editor/SKILL.md` returned 122 lines.
- 2026-05-26 code-review M2 R1: reviewer reran `python tests/validate_skills.py`, `python -m unittest discover tests`, `python tests/check_readme_sync.py`, `git diff --check`, and `wc -l skills/editor/SKILL.md`; all passed with only the existing unrelated grandfathered-evals warning.
- 2026-05-26 M2 review-resolution: `python tests/validate_skills.py` passed with the existing non-blocking grandfathered-evals warning for unrelated skills.
- 2026-05-26 M2 review-resolution: `python -m unittest discover tests` passed, 31 tests OK.
- 2026-05-26 M2 review-resolution: `python tests/check_readme_sync.py` passed.
- 2026-05-26 M2 review-resolution: `git diff --check` passed.
- 2026-05-26 M2 review-resolution: `wc -l skills/editor/SKILL.md` returned 126 lines.
- 2026-05-26 code-review M2 R2: reviewer reran `python tests/validate_skills.py`, `python -m unittest discover tests`, `python tests/check_readme_sync.py`, `git diff --check`, and `wc -l skills/editor/SKILL.md`; all passed with only the existing unrelated grandfathered-evals warning.
- 2026-05-26 M3: `python tests/validate_skills.py` passed with the existing non-blocking grandfathered-evals warning for unrelated skills.
- 2026-05-26 M3: `python -m unittest discover tests` passed, 31 tests OK.
- 2026-05-26 M3: `python tests/check_readme_sync.py` passed.
- 2026-05-26 M3: `git diff --check` passed.
- 2026-05-26 M3: `wc -l skills/editor/SKILL.md` returned 126 lines.
- 2026-05-26 code-review M3 R1: reviewer reran `python tests/validate_skills.py`, `python -m unittest discover tests`, `python tests/check_readme_sync.py`, `git diff --check`, and `wc -l skills/editor/SKILL.md`; all passed with only the existing unrelated grandfathered-evals warning.
- 2026-05-26 code-review M3 R2: reviewer reran `python tests/validate_skills.py`, `python -m unittest discover tests`, `python tests/check_readme_sync.py`, `git diff --check`, and `wc -l skills/editor/SKILL.md`; all passed with only the existing unrelated grandfathered-evals warning.
- 2026-05-26 explain-change: `python tests/validate_skills.py` passed with the existing non-blocking grandfathered-evals warning for unrelated skills.
- 2026-05-26 explain-change: `python -m unittest discover tests` passed, 31 tests OK.
- 2026-05-26 explain-change: `python tests/check_readme_sync.py` passed.
- 2026-05-26 explain-change: `git diff --check` passed.
- 2026-05-26 explain-change: `wc -l skills/editor/SKILL.md` returned 126 lines.
- 2026-05-26 verify: `python tests/validate_skills.py` passed with the existing non-blocking grandfathered-evals warning for unrelated skills.
- 2026-05-26 verify: `python -m unittest discover tests` passed, 31 tests OK.
- 2026-05-26 verify: `python tests/check_readme_sync.py` passed.
- 2026-05-26 verify: `git diff --check` passed.
- 2026-05-26 verify: `wc -l skills/editor/SKILL.md` returned 126 lines.
- 2026-05-26 verify: `git ls-files --others --exclude-standard ...` found new authoritative change artifacts untracked; branch-ready blocked.

## Outcome and retrospective

- M1, M2, and M3 are closed. Post-change evidence and validation are recorded, and all code-review findings are closed.
- The change remains active until final closeout completes verification and PR gates. Current blocker: new authoritative artifacts must be tracked before verify can mark the branch ready.

## Readiness

- See `Current Handoff Summary`.
- Ready to track new change artifacts, then rerun `verify`.
- Not ready for PR handoff until final verification completes.
