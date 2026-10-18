# Plan: Create Flashcard And Quiz Generator Skills

> Historical record: retired source paths and prior workflow judgments below identify the original change. See the [current design index](../../design/architecture/README.md) for effective owners; this migration does not renew this record’s approval or completion status.

## Status

- Status: active
- Plan lifecycle state: active
- Terminal disposition: not-terminal

## Purpose / big picture

Implement the approved `flashcard-generator` and `quiz-generator` skills as portable prompt assets with local references, reference schemas, eval evidence, README synchronization, and contributor guidance where needed. The work is additive and must preserve Skillsmith's pure Markdown prompt boundary.

## Source artifacts

- Proposal: `docs/proposals/2026-07-04-flashcard-and-quiz-skills.md`
- Spec: `specs/flashcard-and-quiz-skills.md`
- Architecture: not-required; `docs/changes/2026-07-04-flashcard-and-quiz-skills/reviews/spec-review-r1.md` records `architecture-not-required`.
- Test spec: `specs/flashcard-and-quiz-skills.test.md`
- Reviews:
  - `docs/changes/2026-07-04-flashcard-and-quiz-skills/reviews/proposal-review-r1.md`
  - `docs/changes/2026-07-04-flashcard-and-quiz-skills/reviews/spec-review-r1.md`
  - `docs/changes/2026-07-04-flashcard-and-quiz-skills/reviews/plan-review-r1.md`
  - `docs/changes/2026-07-04-flashcard-and-quiz-skills/reviews/test-spec-review-r1.md`
- Review log: `docs/changes/2026-07-04-flashcard-and-quiz-skills/review-log.md`

## Context and orientation

Skill behavior belongs in `skills/<skill-name>/SKILL.md`. Required structural validation is handled by `tests/validate_skills.py`, which checks frontmatter, `$ARGUMENTS`, `## Output Format`, eval fixture presence for non-grandfathered skills, eval categories, and grandfathering policy.

New skills require `tests/evals/skills/<skill-name>/cases.yaml`. Current eval validation expects `version: 1`, non-empty `scenarios`, `normal` and `indirect-trigger` categories, and at least one edge-like category. The first slice should use one `cases.yaml` per skill and include trigger-boundary scenarios inside those fixtures rather than adding a new validator or a separate trigger-case file unless implementation finds an existing accepted pattern.

README synchronization is checked by `tests/check_readme_sync.py`. Adding two skills requires updating the README skill table and slash-command lists.

No runtime server, direct export integration, external service, generated asset, tool permission, installer change, CI change, or executable schema validation is planned.

## Non-goals

- Do not create `study-artifact-generator`.
- Do not create a third `learning-design` skill.
- Do not build a spaced-repetition scheduler.
- Do not add direct AnkiConnect, LMS, Moodle, H5P, QTI, or external-service integration.
- Do not add executable schema validation, validator changes, or CI schema enforcement.
- Do not change existing Skillsmith skills.
- Do not add live model calls in CI.

## Requirements covered

- R1-R4: M2
- R5-R7: M1, M2
- R8-R20: M2, M3
- R21-R25: M2
- R26: M2, M3
- R27-R30: M1
- R31-R32: M2
- R33-R35: M2, M3
- AC1-AC7: M1, M2
- AC8-AC12: M2, M3

## Current Handoff Summary

- Current milestone: final closeout
- Current milestone state: pr-opened
- Last reviewed milestone: M3
- Review status: PR review findings resolved; review-resolution closed
- Remaining in-scope implementation milestones: none
- Next stage: hosted-ci-and-review
- Final closeout readiness: PR opened; hosted CI/review pending
- Reason final closeout is or is not ready: implementation, reviews, review-resolution, explain-change, verification, and PR handoff are complete; hosted CI and human review remain.

## Milestones

### M1. Eval Fixtures And Trigger Boundaries

- Milestone state: closed
- Goal: Add eval fixtures for both new skills before prompt implementation, including trigger boundaries and source-grounding edge cases.
- Requirements: R5-R7, R27-R30, AC1, AC2, AC4, AC6, AC7
- Files/components likely touched:
  - `tests/evals/skills/flashcard-generator/cases.yaml`
  - `tests/evals/skills/quiz-generator/cases.yaml`
  - `docs/changes/2026-07-04-flashcard-and-quiz-skills/baseline-evidence.md`
  - `docs/changes/2026-07-04-flashcard-and-quiz-skills/change.yaml`
  - this plan
- Tests to add/update:
  - Flashcard fixture with normal Anki generation, indirect trigger, cloze/contrast, non-trigger, both-skill trigger, and source-grounding boundary scenarios.
  - Quiz fixture with normal diagnostic quiz, indirect trigger, MCQ distractor quality, non-trigger, both-skill trigger, and unsupported-material boundary scenarios.
- Steps:
  - Create fixtures using fictional or sanitized source material.
  - Keep expected behavior as observable bullet text accepted by `validate_cases_file`.
  - Run direct fixture validation before skill directories exist.
  - Record baseline evidence that skill directories do not yet exist.
- Validation:
  - `python -c 'from pathlib import Path; from tests.validate_skills import validate_cases_file; [(_ := validate_cases_file(name, Path(f"tests/evals/skills/{name}/cases.yaml")), (_).errors and (_ for _ in ()).throw(AssertionError(_.errors))) for name in ("flashcard-generator", "quiz-generator")]; print("direct eval fixture validation passed")'`
  - `python -m unittest discover tests`
  - `git diff --check`
- Result: Eval fixtures and baseline evidence added; targeted validation passed; ready for code-review M1.
- Risks:
  - Fixture expectations may become too broad to guide implementation.
  - Full validator will not require fixtures until skill directories exist.
- Rollback:
  - Remove the two fixture directories and baseline evidence before prompt implementation.

### M2. Skill Prompts, References, Schemas, And README Sync

- Milestone state: closed
- Goal: Add both skill directories, local references, reference schemas, and public documentation entries.
- Requirements: R1-R26, R31-R35, AC1-AC5, AC8-AC12
- Files/components likely touched:
  - `skills/flashcard-generator/SKILL.md`
  - `skills/flashcard-generator/references/learning-design.md`
  - `skills/flashcard-generator/references/card-quality.md`
  - `skills/flashcard-generator/schemas/flashcard.schema.json`
  - `skills/quiz-generator/SKILL.md`
  - `skills/quiz-generator/references/learning-design.md`
  - `skills/quiz-generator/references/question-quality.md`
  - `skills/quiz-generator/schemas/quiz-item.schema.json`
  - `README.md`
  - `CONTRIBUTING.md`, only if needed for new-skill/eval guidance
  - `docs/changes/2026-07-04-flashcard-and-quiz-skills/change.yaml`
  - this plan
- Tests to add/update:
  - Update README skill table and slash-command enumeration.
  - Adjust eval fixtures only if prompt wording exposes a mismatch.
- Steps:
  - Create both `SKILL.md` files with required frontmatter only, `$ARGUMENTS`, and `## Output Format`.
  - Encode objective extraction, knowledge mapping, artifact generation, validation, and output contracts.
  - Add compact local learning-design references.
  - Add skill-specific quality references.
  - Add reference schemas and state that executable validation is deferred.
  - Update README and contributor guidance if needed.
- Validation:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check`
  - `wc -l skills/flashcard-generator/SKILL.md skills/quiz-generator/SKILL.md`
- Result: Skill prompts, references, reference schemas, and README entries added; targeted validation passed; code-review M2 R1 returned clean-with-notes and closed M2.
- Risks:
  - Prompt bodies could grow too long.
  - Shared learning-design references could drift.
  - Schema wording could imply CI enforcement.
- Rollback:
  - Remove the two skill directories and README/doc additions; keep M1 fixtures only if replanning continues.

### M3. Post-Change Evidence And Lifecycle Update

- Milestone state: closed
- Goal: Record prompt-inspection evidence, manual smoke evidence where feasible, and final planned validation before code-review.
- Requirements: R8-R20, R26, R33-R35, AC1-AC12
- Files/components likely touched:
  - `docs/changes/2026-07-04-flashcard-and-quiz-skills/post-change-evidence.md`
  - `docs/changes/2026-07-04-flashcard-and-quiz-skills/change.yaml`
  - this plan
  - `docs/plan.md`
- Tests to add/update:
  - No production prompt changes expected unless evidence reveals a defect.
- Steps:
  - Record prompt-inspection evidence for objectives-before-artifacts, knowledge map, output contracts, source grounding, and no executable schema validation.
  - Record manual smoke examples for flashcards, quizzes, unsupported material, and both-output fallback where feasible.
  - Run final planned validation.
  - Update lifecycle metadata and current handoff summary for code-review.
- Validation:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check`
- Result: Post-change prompt-inspection and manual smoke evidence recorded; final planned validation passed; code-review M3 R1 returned clean-with-notes and closed M3.
- Risks:
  - Manual smoke may reveal prompt ambiguity late.
  - Evidence may show the schema reference and output contract disagree.
- Rollback:
  - Return to M2 prompt/schema edits and rerun validation before code-review.

## Validation plan

- `python tests/validate_skills.py`: full structural and eval policy validation after skill directories exist.
- Direct `validate_cases_file` invocation for both new fixtures: required in M1 before skill directories exist.
- `python -m unittest discover tests`: broad local test suite.
- `python tests/check_readme_sync.py`: README skill-table and slash-command synchronization.
- `git diff --check`: whitespace sanity check.
- `wc -l skills/flashcard-generator/SKILL.md skills/quiz-generator/SKILL.md`: prompt size awareness.
- Prompt-inspection evidence: objectives, knowledge maps, output contracts, source grounding, schema-reference-only behavior, and both-output fallback.

## Risks and recovery

- Risk: The two skills overlap in trigger behavior.
  - Recovery: Tighten descriptions and eval trigger cases before prompt implementation closes.
- Risk: Flashcards become summaries.
  - Recovery: Strengthen atomicity and card-quality checks in `card-quality.md` and `SKILL.md`.
- Risk: Quizzes become shallow recall lists.
  - Recovery: Strengthen blueprint and cognitive-level requirements.
- Risk: Source grounding is unclear.
  - Recovery: Add explicit source-reference and inference-marking checks.
- Risk: Schema references imply executable enforcement.
  - Recovery: Reword schema references and README/contributor notes to say reference-only.

## Dependencies

- Proposal status: accepted.
- Spec status: approved.
- Architecture: not required for this pure-prompt first slice.
- Plan-review R1 approved this plan.
- Active test spec exists at `specs/flashcard-and-quiz-skills.test.md`.
- Test-spec-review R1 approved implementation handoff.

## Progress

- 2026-07-04: Created plan after spec-review R1 approved the spec and recorded no architecture artifact required.
- 2026-07-04: Implemented M1 by adding direct eval fixtures for `flashcard-generator` and `quiz-generator`, plus baseline evidence showing prompt directories remain absent until M2.
- 2026-07-04: Code-review M1 R1 returned clean-with-notes and closed M1.
- 2026-07-04: Implemented M2 by adding both skill prompts, local learning-design and quality references, reference schemas, README entries, and validation evidence.
- 2026-07-04: Code-review M2 R1 returned clean-with-notes and closed M2.
- 2026-07-04: Began M3 by recording post-change prompt-inspection and manual smoke evidence.
- 2026-07-04: Completed M3 evidence and validation, then moved M3 to code-review handoff.
- 2026-07-04: Code-review M3 R1 returned clean-with-notes and closed M3.
- 2026-07-04: Verify passed and recorded branch-ready evidence in `docs/changes/2026-07-04-flashcard-and-quiz-skills/verify-report.md`.
- 2026-07-05: Opened PR #32 and recorded PR handoff evidence in `docs/changes/2026-07-04-flashcard-and-quiz-skills/pr.md`; hosted CI was in progress at handoff.
- 2026-07-05: Accepted and resolved PR review findings `F-PR32-SKILL-001` and `F-PR32-SKILL-002`; recorded closed review-resolution.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-07-04 | Split implementation into evals, prompt/docs, and evidence milestones | Keeps proof first and separates prompt authoring from final evidence. | One large implementation milestone |
| 2026-07-04 | Keep trigger boundary cases inside `cases.yaml` for the first slice | Current validator understands one fixture file per skill; separate trigger-case files would be reviewer-only unless a later validator change is accepted. | Add separate trigger-case files with no validator support |
| 2026-07-04 | Record architecture as not required | The accepted scope is additive pure-prompt content and docs with no runtime or CI architecture change. | Create unnecessary architecture artifact |

## Surprises and discoveries

- M1 uses direct fixture validation because the full validator only checks eval fixtures for skills that exist under `skills/`.
- `CONTRIBUTING.md` stayed unchanged in M2 because existing guidance already covers new skill directories, optional frontmatter omission, eval fixtures, README updates, and validation commands.
- M3 evidence inspection found the combined-output fallback needed explicit shared-objective and shared-knowledge-map wording in both skill prompts, so that same-slice prompt gap was fixed before code-review handoff.

## Validation notes

- M1 validation passed:
  - `python -c 'from pathlib import Path; from tests.validate_skills import validate_cases_file; [(_ := validate_cases_file(name, Path(f"tests/evals/skills/{name}/cases.yaml")), (_).errors and (_ for _ in ()).throw(AssertionError(_.errors))) for name in ("flashcard-generator", "quiz-generator")]; print("direct eval fixture validation passed")'`
  - `python -m unittest discover tests`
  - `git diff --check`
  - `test ! -e skills/flashcard-generator/SKILL.md && test ! -e skills/quiz-generator/SKILL.md && echo 'skill prompts absent as expected for M1'`
- Code-review M1 R1 reviewer validation passed:
  - `python -c 'from pathlib import Path; from tests.validate_skills import validate_cases_file; [(_ := validate_cases_file(name, Path(f"tests/evals/skills/{name}/cases.yaml")), (_).errors and (_ for _ in ()).throw(AssertionError(_.errors))) for name in ("flashcard-generator", "quiz-generator")]; print("direct eval fixture validation passed")'`
  - `python -m unittest discover tests`
  - `git diff --check HEAD^..HEAD`
  - `test ! -e skills/flashcard-generator/SKILL.md && test ! -e skills/quiz-generator/SKILL.md && echo 'skill prompts absent as expected for M1'`
  - `python tests/validate_skills.py`
- M2 validation passed:
  - `python - <<'PY' ... json/yaml ok`
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check`
  - `wc -l skills/flashcard-generator/SKILL.md skills/quiz-generator/SKILL.md`
- Code-review M2 R1 reviewer validation passed:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check HEAD^..HEAD`
  - `wc -l skills/flashcard-generator/SKILL.md skills/quiz-generator/SKILL.md`
  - scoped diff-name check for CI, validator, installer, and unrelated skill changes
- M3 validation passed:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check`
  - `wc -l skills/flashcard-generator/SKILL.md skills/quiz-generator/SKILL.md`
  - `python - <<'PY' ... yaml ok`
- Code-review M3 R1 reviewer validation passed:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check HEAD^..HEAD`
  - `wc -l skills/flashcard-generator/SKILL.md skills/quiz-generator/SKILL.md`
  - `python - <<'PY' ... yaml ok`
  - scoped diff-name check for CI, validator, installer, and unrelated skill changes
- Verify validation passed:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check main...HEAD`
  - `python - <<'PY' ... json/yaml ok`
  - `wc -l skills/flashcard-generator/SKILL.md skills/quiz-generator/SKILL.md`
  - direct eval fixture validation for both new skills
  - scoped no-integration diff-name check
  - lifecycle state grep
  - `git merge-base HEAD main` and `git rev-parse main`
- Review-resolution PR32 validation passed:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check`
  - `python - <<'PY' ... json/yaml ok`
  - `wc -l skills/flashcard-generator/SKILL.md skills/quiz-generator/SKILL.md`

## Outcome and retrospective

- Filled after completion.

## Readiness

- See `Current Handoff Summary`.
- PR opened; hosted CI/review pending.
