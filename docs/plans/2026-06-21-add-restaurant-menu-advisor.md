# Plan: Add Restaurant Menu Advisor Skill

## Status

- Status: active
- Plan lifecycle state: active
- Terminal disposition: not-terminal

## Purpose / big picture

Implement the approved `restaurant-menu-advisor` skill as a portable prompt asset with reviewer-visible eval evidence and public documentation. The work is deliberately additive: one new skill, one eval fixture, README synchronization, and change-local validation evidence. It must preserve Skillsmith's pure Markdown skill boundary and the spec's allergy and generated-image safety constraints.

## Source artifacts

- Proposal: `docs/proposals/2026-06-21-add-restaurant-menu-advisor.md`
- Spec: `specs/restaurant-menu-advisor.md`
- Architecture: not-required; `docs/changes/2026-06-21-add-restaurant-menu-advisor/reviews/spec-review-r1.md` records that the current pure-prompt boundary does not require a separate architecture artifact.
- Test spec: `specs/restaurant-menu-advisor.test.md`
- Reviews:
  - `docs/changes/2026-06-21-add-restaurant-menu-advisor/reviews/proposal-review-r2.md`
  - `docs/changes/2026-06-21-add-restaurant-menu-advisor/reviews/spec-review-r1.md`
  - `docs/changes/2026-06-21-add-restaurant-menu-advisor/reviews/plan-review-r1.md`
  - `docs/changes/2026-06-21-add-restaurant-menu-advisor/reviews/test-spec-approval-r1.md`
- Review log: `docs/changes/2026-06-21-add-restaurant-menu-advisor/review-log.md`

## Context and orientation

The product behavior belongs in `skills/restaurant-menu-advisor/SKILL.md`. The repository validates skill structure with `tests/validate_skills.py`, including required `name` and `description` frontmatter, `$ARGUMENTS`, and `## Output Format`.

New, non-grandfathered skills require `tests/evals/skills/<skill-name>/cases.yaml`. The validator checks that eval fixtures include `version: 1`, non-empty scenarios, `normal` and `indirect-trigger` categories, at least one edge-like category, and, for `high_risk: true`, `safety_notes` plus a safety or misuse scenario.

README synchronization is reviewer-visible through `tests/check_readme_sync.py`, which compares the skill table and slash-command mentions against installed skill directories. Adding `restaurant-menu-advisor` requires updating the README skill table and any enumerated slash-command lists that would otherwise miss the new command.

No runtime server, data persistence, installer change, CI change, external service, generated image asset, provider API, or tool permission is planned.

## Non-goals

- Do not build a standalone app, API backend, account system, or persistent preference store.
- Do not add runtime dependencies, CI dependencies, scripts, image assets, secrets, external services, or provider-specific API instructions.
- Do not scrape menus, reviews, social media, or dish photos.
- Do not place orders, make reservations, process payment, or contact restaurants.
- Do not change existing skills, validator behavior, installer behavior, CI behavior, or repository architecture.
- Do not claim any generated image is the restaurant's actual dish or evidence for ingredients, portion, plating, allergens, or safety.
- Do not declare dishes allergen-free or safe to eat.

## Requirements covered

- R1-R4: M2
- R5-R12: M2
- R13-R19: M2, M3
- R20-R24: M1, M2, M3
- R25-R27: M2, M3
- R28-R29: M1
- R30: M2
- R31-R32: M2, M3
- R33-R34: M1, M2, M3
- AC1-AC10: M2
- AC11: M1
- AC12: M2
- AC13-AC15: M1, M2, M3
- AC16: M3

## Current Handoff Summary

- Current milestone: M2
- Current milestone state: review-requested
- Last reviewed milestone: M1
- Review status: code-review M1 R1 clean-with-notes; no material findings
- Remaining in-scope implementation milestones: M2, M3
- Next stage: code-review M2
- Final closeout readiness: not ready
- Reason final closeout is or is not ready: M2 code-review, M3 implementation, downstream code-review, explain-change, verify, and PR handoff remain open.

## Milestones

### M1. Eval Fixture And Baseline Proof

- Milestone state: closed
- Goal: Add reviewer-visible eval evidence before implementing the prompt, including safety and misuse coverage for the high-risk allergy path.
- Requirements: R20-R24, R28-R29, R33-R34, AC11, AC13-AC15
- Files/components likely touched:
  - `tests/evals/skills/restaurant-menu-advisor/cases.yaml`
  - `docs/changes/2026-06-21-add-restaurant-menu-advisor/baseline-evidence.md`
  - `docs/changes/2026-06-21-add-restaurant-menu-advisor/change.yaml`
  - this plan
  - `docs/plan.md`
- Dependencies:
  - Plan-review approval.
  - Active test spec at `specs/restaurant-menu-advisor.test.md`.
- Tests to add/update:
  - Add `tests/evals/skills/restaurant-menu-advisor/cases.yaml` with `high_risk: true`, safety notes, and normal, indirect-trigger, failure, safety, misuse, active-medical-emergency, and fewer-than-three-supported-items scenarios.
  - Record baseline proof that the new skill does not yet exist before M2 prompt implementation.
- Implementation steps:
  - Create the eval fixture with fictional or sanitized menu and allergy examples.
  - Include expected behavior that checks evidence grounding, bounded clarification, no safety claims, no image-as-evidence, and active emergency routing.
  - Record baseline evidence that `skills/restaurant-menu-advisor/SKILL.md` is absent before prompt implementation.
  - Run direct eval-fixture validation for `restaurant-menu-advisor`, because the full validator only checks eval directories for skills that already exist.
- Validation commands:
  - `python -c 'from pathlib import Path; from tests.validate_skills import validate_cases_file; result = validate_cases_file("restaurant-menu-advisor", Path("tests/evals/skills/restaurant-menu-advisor/cases.yaml")); assert not result.errors, result.errors'`
  - `python -m unittest discover tests`
  - `git diff --check`
- Expected observable result: Reviewer-visible eval cases exist and trace to the approved safety-sensitive scenarios before the production prompt is implemented.
- Commit message: `M1: add restaurant menu advisor eval fixture`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Eval expectations could be too vague to guide implementation.
  - The full validator will not prove an eval fixture for an absent skill directory.
- Rollback/recovery:
  - Tighten expected behavior text before prompt implementation.
  - Use the direct `validate_cases_file` command above for M1, then full `python tests/validate_skills.py` after M2 creates the skill directory.

### M2. Skill Prompt And README Synchronization

- Milestone state: review-requested
- Goal: Add the `restaurant-menu-advisor` prompt skill and public README entries while preserving portability and the safety boundaries in the spec.
- Requirements: R1-R19, R20-R27, R30-R34, AC1-AC15
- Files/components likely touched:
  - `skills/restaurant-menu-advisor/SKILL.md`
  - `README.md`
  - `tests/evals/skills/restaurant-menu-advisor/cases.yaml`
  - `docs/changes/2026-06-21-add-restaurant-menu-advisor/m2-evidence.md`
  - `docs/changes/2026-06-21-add-restaurant-menu-advisor/change.yaml`
  - this plan
  - `docs/plan.md`
- Dependencies:
  - M1 eval coverage available, or M1/M2 intentionally combined after plan-review.
  - No architecture change introduced.
- Tests to add/update:
  - Update README skill table and slash-command enumeration to include `/restaurant-menu-advisor`.
  - Update eval fixture only to keep it aligned with implementation wording if needed.
- Implementation steps:
  - Create `skills/restaurant-menu-advisor/SKILL.md` with required frontmatter only.
  - Include `$ARGUMENTS` and `## Output Format`.
  - Encode the menu-evidence workflow, bounded clarification, shortlist, leading recommendation, visual brief, allergy safety, emergency routing, and final consistency check.
  - Avoid optional frontmatter, tool permissions, provider API instructions, checked-in images, and hidden runtime dependencies.
  - Update README table and enumerated command surfaces.
- Validation commands:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check`
  - `wc -l skills/restaurant-menu-advisor/SKILL.md`
- Expected observable result: The new skill is installed as a valid Skillsmith prompt, public docs enumerate it, and validation passes without introducing runtime or CI dependencies.
- Commit message: `M2: add restaurant menu advisor skill`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Prompt may become too long or overbroad.
  - README command enumeration may drift.
  - Allergy boundary could sound like safety assurance if wording is too confident.
- Rollback/recovery:
  - Trim nonessential food advice and keep one primary workflow.
  - Use `tests/check_readme_sync.py` output to fix README drift.
  - Reword allergy handling around unknowns and staff confirmation.

### M3. Manual Smoke Evidence And Final Implementation Slice Closeout

- Milestone state: planned
- Goal: Record behavior evidence for the text-only path, optional image-capable path, allergy path, unreadable-menu path, and final repository validation.
- Requirements: R13-R19, R20-R27, R31-R34, AC13-AC16
- Files/components likely touched:
  - `docs/changes/2026-06-21-add-restaurant-menu-advisor/post-change-evidence.md`
  - `docs/changes/2026-06-21-add-restaurant-menu-advisor/change.yaml`
  - this plan
  - `docs/plan.md`
- Dependencies:
  - M2 prompt and README changes implemented.
- Tests to add/update:
  - Manual smoke notes using fictional or sanitized examples for text-only, image-capable, allergy, and unreadable-menu behavior.
  - No production prompt changes expected unless smoke evidence reveals a spec gap or implementation defect.
- Implementation steps:
  - Record text-only smoke evidence that the visual brief is useful without image generation.
  - Record image-capable smoke evidence or explicitly document if the active host cannot render images; the proof must still verify that the prompt labels images as illustrative.
  - Record allergy smoke evidence showing no allergen-safe claim.
  - Record unreadable-menu smoke evidence showing a clearer-evidence request instead of guessing.
  - Run the full planned validation set and update lifecycle state.
- Validation commands:
  - `python tests/validate_skills.py`
  - `python -m unittest discover tests`
  - `python tests/check_readme_sync.py`
  - `git diff --check`
- Expected observable result: Reviewers can see implementation behavior evidence and final validation results before code-review and later explain-change/verify stages.
- Commit message: `M3: record restaurant menu advisor evidence`
- Milestone closeout:
  - validation passed
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone committed
- Risks:
  - Manual smoke may reveal prompt ambiguity late.
  - Image-capable rendering may be unavailable in the active host.
- Rollback/recovery:
  - If smoke reveals prompt ambiguity, return to M2 prompt edits and rerun M2 review.
  - If image rendering is unavailable, record text-only proof plus prompt inspection proving explicit-request and illustrative-label behavior.

## Validation plan

- `python tests/validate_skills.py`: required structural validation for all skills and eval fixture policy.
- Direct `validate_cases_file` invocation for `tests/evals/skills/restaurant-menu-advisor/cases.yaml`: required in M1 before the skill directory exists.
- `python -m unittest discover tests`: broad test suite covering validator, eval fixture, README sync helper, and CI contract tests.
- `python tests/check_readme_sync.py`: targeted README skill-table and slash-command synchronization check.
- `git diff --check`: whitespace sanity check before review.
- `wc -l skills/restaurant-menu-advisor/SKILL.md`: prompt size awareness for the new skill.
- Manual smoke evidence: text-only path, optional image-capable path, allergy path, and unreadable-menu path.

## Risks and recovery

- Risk: The skill overreaches into restaurant search, ordering, nutrition, or meal planning.
  - Recovery: Re-anchor the prompt to the one primary menu-choice workflow and non-goals.
- Risk: Allergy language creates false reassurance.
  - Recovery: Reword to prohibit safety claims and require staff confirmation of ingredients, preparation, and cross-contact.
- Risk: Visual brief implies exact restaurant presentation.
  - Recovery: Add stronger illustrative-only labels and consistency checks.
- Risk: README or eval fixtures drift from the new skill.
  - Recovery: Use `python tests/check_readme_sync.py` and `python tests/validate_skills.py` to identify and fix drift.
- Risk: The implementation adds hidden runtime or provider-specific behavior.
  - Recovery: Remove tool/API instructions and keep image rendering optional, explicit-request, and host-capability dependent.

## Dependencies

- Proposal status: accepted.
- Spec status: approved.
- Architecture: not required for the current pure-prompt boundary.
- Plan-review R1 approved this plan.
- Active test spec exists at `specs/restaurant-menu-advisor.test.md` and is owner-approved in test-spec approval R1.
- Code-review is required after each implementation milestone because this is a new high-risk eval fixture and multi-file skill change.

## Progress

- 2026-06-21: Created execution plan after spec-review R1 approved the spec and recorded no architecture artifact required.
- 2026-06-21: Plan-review R1 approved the plan.
- 2026-06-21: Authored active test spec at `specs/restaurant-menu-advisor.test.md`; next stage is implement M1.
- 2026-06-21: Owner approved `specs/restaurant-menu-advisor.test.md` in `docs/changes/2026-06-21-add-restaurant-menu-advisor/reviews/test-spec-approval-r1.md`.
- 2026-06-21: Started M1 implementation for the high-risk eval fixture and baseline proof.
- 2026-06-21: Implemented M1 by adding `tests/evals/skills/restaurant-menu-advisor/cases.yaml` and `docs/changes/2026-06-21-add-restaurant-menu-advisor/baseline-evidence.md`; milestone is ready for code-review M1.
- 2026-06-21: Code-review M1 R1 closed M1 with no material findings; next stage is implement M2.
- 2026-06-21: Started M2 implementation for the prompt skill and README synchronization.
- 2026-06-21: Implemented M2 by adding `skills/restaurant-menu-advisor/SKILL.md`, updating README discovery surfaces, and recording `docs/changes/2026-06-21-add-restaurant-menu-advisor/m2-evidence.md`; milestone is ready for code-review M2.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-06-21 | Use three implementation milestones: eval first, prompt/docs second, smoke evidence third | Keeps safety proof visible before prompt implementation and separates behavior evidence from prompt authoring. | One large implementation milestone; prompt before eval fixture |
| 2026-06-21 | Route directly to plan-review without architecture artifact | Spec-review R1 records no architecture artifact is required for the pure-prompt boundary. | Architecture artifact for an additive prompt-only change |
| 2026-06-21 | Keep test-spec after plan-review | The workflow requires plan sequencing before traceable test-spec authoring. | Author test-spec before plan-review |

## Surprises and discoveries

- Full `python tests/validate_skills.py` does not prove an eval fixture for a skill directory that intentionally does not exist yet, so M1 relies on the direct `validate_cases_file` command for fixture proof before M2 creates the skill.

## Aligned-surface audit

- `skills/restaurant-menu-advisor/SKILL.md`: added in M2 with required frontmatter, `$ARGUMENTS`, `## Output Format`, and approved safety boundaries.
- `README.md`: synchronized in M2 with the new skill table row, slash command mentions, usage example, and skill detail section.
- `tests/evals/skills/restaurant-menu-advisor/cases.yaml`: unchanged in M2 because the M2 prompt aligns with the M1 scenario expectations.
- `docs/changes/2026-06-21-add-restaurant-menu-advisor/post-change-evidence.md`: intentionally absent until M3 manual smoke evidence.
- `install.sh`, `tests/validate_skills.py`, CI, architecture, scripts, dependencies, secrets, generated images, and provider-specific API instructions: unaffected by M2.

## Validation notes

- 2026-06-21: `python tests/validate_skills.py` passed during plan authoring, with the existing non-blocking grandfathered-eval warning.
- 2026-06-21: Test-spec authoring checks passed: `python tests/validate_skills.py` with the existing non-blocking grandfathered-eval warning, `python -m unittest discover tests` ran 31 tests, `python tests/check_readme_sync.py` passed, and `git diff --check` passed.
- 2026-06-21: M1 direct fixture validation passed: `python -c 'from pathlib import Path; from tests.validate_skills import validate_cases_file; result = validate_cases_file("restaurant-menu-advisor", Path("tests/evals/skills/restaurant-menu-advisor/cases.yaml")); assert not result.errors, result.errors; print("direct eval fixture validation passed")'`.
- 2026-06-21: M1 broad checks passed: `python -m unittest discover tests` ran 31 tests, `python tests/validate_skills.py` passed with the existing non-blocking grandfathered-eval warning, `python tests/check_readme_sync.py` passed, and `git diff --check` passed.
- 2026-06-21: Code-review M1 R1 reviewer reruns passed: direct `validate_cases_file`, `python tests/validate_skills.py` with the existing non-blocking grandfathered-eval warning, `python -m unittest discover tests` ran 31 tests, `python tests/check_readme_sync.py`, and `git diff --check HEAD`.
- 2026-06-21: M2 checks passed: `python tests/validate_skills.py` passed for 11 skills with the existing non-blocking grandfathered-eval warning, `python -m unittest discover tests` ran 31 tests, `python tests/check_readme_sync.py` passed, `git diff --check` passed, and `wc -l skills/restaurant-menu-advisor/SKILL.md` reported 152 lines.

## Outcome and retrospective

- Pending implementation and downstream review.

## Readiness

- See `Current Handoff Summary`.
- Ready for `code-review` M2. Not ready for M3 implementation, explain-change, verify, branch readiness, or PR readiness.
