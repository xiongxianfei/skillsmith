# Plan: Editor skill optimization

## Status

- Plan lifecycle state: active
- Terminal disposition: none

## Purpose / big picture

This plan tracks the accepted `editor` skill optimization and the 2026-05-25 user amendment that changed the desired output contract to a required compact three-stage workflow:

1. optimize the input and provide optimization reasons;
2. review language quality before translation;
3. translate the optimized text into Chinese and English.

## Source artifacts

- Proposal: `docs/proposals/2026-05-25-editor-skill-optimization.md`
- Spec: `specs/editor-skill-optimization.md`
- Architecture: not-required; no runtime boundaries, dependencies, generated assets, data flow, or installer behavior change
- Test spec: `specs/editor-skill-optimization.test.md`
- Explain change: `docs/changes/2026-05-25-editor-skill-optimization/explain-change.md`
- Verify report: `docs/changes/2026-05-25-editor-skill-optimization/verify-report.md`
- Reviews:
  - `docs/changes/2026-05-25-editor-skill-optimization/reviews/proposal-review-r2.md`
  - `docs/changes/2026-05-25-editor-skill-optimization/reviews/spec-review-r2.md`
  - `docs/changes/2026-05-25-editor-skill-optimization/reviews/plan-review-r1.md`
  - `docs/changes/2026-05-25-editor-skill-optimization/reviews/test-spec-approval-r1.md`
  - `docs/changes/2026-05-25-editor-skill-optimization/reviews/code-review-m1-r1.md`
  - `docs/changes/2026-05-25-editor-skill-optimization/reviews/code-review-m2-r1.md`
  - `docs/changes/2026-05-25-editor-skill-optimization/reviews/code-review-m3-r1.md`

## Current Handoff Summary

- Current milestone: amendment update
- Current milestone state: implementation-updated
- Last reviewed milestone: M3
- Review status: prior M1-M3 code reviews are recorded, but the post-PR amendment changes the prompt contract and needs renewed review/verification
- Remaining in-scope implementation milestones: amendment review and verification
- Next stage: code-review amendment
- Final closeout readiness: not ready
- Reason final closeout is or is not ready: the prompt, spec, test spec, evidence, and lifecycle docs were updated after the previous verify/PR handoff; code review and final verification need to be rerun for the amended contract.

## Requirements covered

- R1-R4: editor metadata, pure-prompt boundary, `$ARGUMENTS`, and `## Output Format`
- R5-R12: compact three-stage workflow with optimization reasons, language identification, language-quality assessment, and Chinese/English translations
- R13-R18: supported editing modes, ambiguity behavior, and integrity boundary
- R19: prompt line-count and concision
- R20-R24: eval fixture plus baseline and post-change evidence
- R25-R27: no live model CI, no validator behavior change, no unrelated skill optimization
- AC1-AC15: acceptance criteria in `specs/editor-skill-optimization.md`

## Milestone history

### M1. Eval fixture and baseline evidence

- Milestone state: closed
- Result:
  - Added `tests/evals/skills/editor/cases.yaml`.
  - Added `docs/changes/2026-05-25-editor-skill-optimization/baseline-evidence.md`.
  - Confirmed `skills/editor/SKILL.md` was not edited in M1.
  - Code-review M1 R1 returned clean-with-notes and closed M1.

### M2. Editor prompt optimization

- Milestone state: superseded-by-amendment
- Result:
  - Rewrote `skills/editor/SKILL.md` into a conditional, narrow-output prompt.
  - Code-review M2 R1 returned clean-with-notes and closed M2.
  - This M2 contract was later superseded by the user's amended compact three-stage workflow request.

### M3. Post-change evidence and final implementation validation

- Milestone state: superseded-by-amendment
- Result:
  - Added post-change evidence for the earlier narrow-output contract.
  - Code-review M3 R1 returned clean-with-notes and closed M3.
  - Final verify previously passed for the earlier contract, then became stale when the user amended the workflow.

### Amendment update. Three-stage editor workflow

- Milestone state: implementation-updated
- Goal: Update the skill and related docs to the amended compact three-stage workflow.
- Requirements: R1-R27, AC1-AC15
- Files/components touched:
  - `skills/editor/SKILL.md`
  - `tests/evals/skills/editor/cases.yaml`
  - `docs/proposals/2026-05-25-editor-skill-optimization.md`
  - `specs/editor-skill-optimization.md`
  - `specs/editor-skill-optimization.test.md`
  - `docs/changes/2026-05-25-editor-skill-optimization/baseline-evidence.md`
  - `docs/changes/2026-05-25-editor-skill-optimization/post-change-evidence.md`
  - lifecycle artifacts under `docs/changes/2026-05-25-editor-skill-optimization/`
  - all `skills/*/SKILL.md` frontmatter
  - `tests/validate_skills.py` and validator unit fixtures
  - governance and contributor docs for skill metadata
- Implementation steps:
  - Update the skill prompt to require compact Stage 1 optimization results, Stage 2 language-quality assessment with language identification, and Stage 3 Chinese/English translation.
  - Update eval scenarios to assert the amended behavior.
  - Update spec and test spec to remove the stale narrow-output contract.
  - Update baseline and post-change evidence to compare the previous branch behavior with the amended contract.
  - Remove runtime-specific `effort` and `allowed-tools` frontmatter from all skills and align validator, tests, and contributor docs with that metadata policy.
  - Run deterministic validation.
- Validation commands:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check`
  - `wc -l skills/editor/SKILL.md`
- Result:
  - Implementation updated for the amended workflow.
  - Runtime-specific skill frontmatter removed by user request.
  - Prompt line count is 69 lines.
  - Validation passed locally.
  - Ready for renewed code review of the amendment.

## Validation plan

- `python tests/validate_skills.py`: required repository skill validation and eval-fixture checks.
- `python -m unittest tests/test_eval_fixtures.py`: targeted eval fixture validator coverage.
- `python -m unittest discover tests`: full repository test suite after prompt/evidence changes.
- `python tests/check_readme_sync.py`: README sync check because the helper exists on this branch.
- `git diff --check`: whitespace and patch hygiene.
- Manual scenario comparison: baseline and post-change evidence for the amended compact three-stage workflow.
- Line-count check for `skills/editor/SKILL.md`: prove the prompt remains under the hard limit.

## Risks and recovery

- Risk: The amended workflow may over-produce for simple edits.
  - Recovery: This is now intentional user-directed behavior; keep reasons and assessments concise.
- Risk: Translation support narrows to Chinese and English output.
  - Recovery: Preserve the metadata trigger for Chinese, English, and Russian source/translation work, but make the default output Chinese and English as requested.
- Risk: Previous code-review and verify records refer to the superseded narrow-output contract.
  - Recovery: Keep them as historical records, mark the current handoff as requiring renewed review/verification, and update current artifacts to the amended contract.

## Progress notes

- 2026-05-25: Proposal, spec, plan, and test spec were originally accepted for a narrow-output optimization.
- 2026-05-25: M1-M3 were implemented, reviewed, explained, verified, and opened as PR #26.
- 2026-05-25: User amended the desired `editor` workflow to a required three-stage process.
- 2026-05-25: Skill, eval fixture, spec, test spec, evidence, and lifecycle docs were updated to the amended workflow.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-05-25 | Start with `editor` alone | Low-risk skill suitable for proving the quality path | Batch with high-risk skills |
| 2026-05-25 | Keep live model calls out of CI | Prompt behavior is reviewed through deterministic fixtures and manual evidence | Live model CI |
| 2026-05-25 | Amend output contract to mandatory compact three-stage workflow | Explicit user direction after PR handoff | Narrow edited-text-only default |

## Current handoff

Ready for `code-review amendment`.
