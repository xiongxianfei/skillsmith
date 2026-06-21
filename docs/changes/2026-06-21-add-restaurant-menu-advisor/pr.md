# PR Handoff: Restaurant Menu Advisor

## Result

- Skill: pr
- Status: opened
- Branch: `feat/restaurant-menu-advisor`
- Base: `main`
- PR title: `feat: add restaurant menu advisor skill`
- PR URL: https://github.com/xiongxianfei/skillsmith/pull/31
- Open blockers: none
- Readiness: PR opened; hosted CI in progress/pending at handoff

## Readiness Checks

| Check | Result | Evidence |
| --- | --- | --- |
| Working tree | pass | `git status --short` was clean before PR artifact authoring. |
| Branch and base | pass | Current branch is `feat/restaurant-menu-advisor`; merge-base with `main` is `fd367d98c8fc4728b6d3e448b16286210b13e4a1`. |
| Commits scoped | pass | Branch contains the workflow-managed proposal, spec, plan, implementation, review, explain-change, verify, and PR handoff commits for the restaurant-menu-advisor change. |
| Validation | pass | Verify report records local validation passing: `validate_skills`, unit tests, README sync, whitespace check. |
| CI status | pending | Hosted CI has not run locally; it is expected after PR open. |
| Lifecycle state | pass | `docs/plan.md`, plan body, and `change.yaml` show final closeout, branch-ready, next stage `pr`. |
| Required change pack | pass | `change.yaml`, `explain-change.md`, `verify-report.md`, reviews, and review log exist under `docs/changes/2026-06-21-add-restaurant-menu-advisor/`. |
| Review resolution | pass | `review-resolution.md` has `Closeout status: closed`; review log has no open findings. |
| Secrets/debug artifacts | pass | Verify found no scripts, secrets, API credentials, generated images, dependency changes, installer changes, validator changes, or CI changes. |

## PR Body

## Summary
- Add a portable `restaurant-menu-advisor` prompt skill for choosing what to order from supplied restaurant-menu evidence.
- Add high-risk eval evidence, README discovery updates, lifecycle artifacts, and workflow artifact-location cleanup.

## Why
- Choosing from unfamiliar menus benefits from a reusable, evidence-grounded workflow rather than ad hoc prompting.
- Allergy-related menu advice is safety-sensitive, so the skill avoids allergen-safety claims and routes ingredient, preparation, and cross-contact questions to restaurant staff.
- The visual-preview goal is preserved as an illustrative visual brief without requiring image-generation APIs or treating generated imagery as restaurant evidence.

## Spec / plan / architecture
- Proposal: `docs/proposals/2026-06-21-add-restaurant-menu-advisor.md`
- Spec: `specs/restaurant-menu-advisor.md`
- Test spec: `specs/restaurant-menu-advisor.test.md`
- Architecture / ADRs: not required; spec-review R1 records the accepted pure-prompt boundary.
- Plan: `docs/plans/2026-06-21-add-restaurant-menu-advisor.md`
- Explain-change: `docs/changes/2026-06-21-add-restaurant-menu-advisor/explain-change.md`
- Verify report: `docs/changes/2026-06-21-add-restaurant-menu-advisor/verify-report.md`

## What changed
- Added `skills/restaurant-menu-advisor/SKILL.md` with required frontmatter, `$ARGUMENTS`, `## Output Format`, menu evidence grounding, bounded clarification, shortlist/leading-pick workflow, allergy boundaries, visual-brief boundaries, scope limits, and a final consistency check.
- Added `tests/evals/skills/restaurant-menu-advisor/cases.yaml` with `high_risk: true`, safety notes, and normal/indirect/failure/safety/misuse/emergency/edge scenarios.
- Updated `README.md` so the new skill appears in the skill table, install command list, one-session command examples, usage example, and skill details.
- Added proposal/spec/test-spec/plan/review/evidence/explain/verify artifacts for the workflow-managed change.
- Clarified workflow artifact locations in `docs/workflows.md` and moved superseded plan history to `docs/plan-archive.md`.

## Tests and verification
- [x] `python tests/validate_skills.py` — passed for 11 skills with the existing non-blocking grandfathered-evals warning.
- [x] `python -m unittest discover tests` — passed, 31 tests.
- [x] `python tests/check_readme_sync.py` — passed.
- [x] `git diff --check HEAD` — passed.
- [x] `wc -l skills/restaurant-menu-advisor/SKILL.md` — 152 lines.
- [ ] CI — pending after PR open; local checks match `.github/workflows/validate.yml`.

## Requirement coverage
- R1-R3, R31 → T1, T2, T12, T14 → `skills/restaurant-menu-advisor/SKILL.md`, `python tests/validate_skills.py`
- R4-R12, R27 → T3-T5, T10, T13 → prompt workflow and `post-change-evidence.md`
- R13-R19 → T3, T7, T13 → visual brief/image boundary instructions and evidence
- R20-R23 → T6, T8, T13 → allergy and emergency safety paths in prompt, evals, and evidence
- R24-R26, R32 → T9, T12, T13 → scope boundaries and diff inspection
- R28-R29 → T2 → high-risk eval fixture with safety notes and required scenarios
- R30 → T11, T14 → README sync updates and `check_readme_sync`
- R33-R34, AC13-AC16 → T14 and manual/static evidence → validation commands and `post-change-evidence.md`

## Review resolution summary
- Accepted: 3
- Rejected: 0
- Deferred: 0
- Partially accepted: 0
- Needs decision: 0
- Review-resolution: `docs/changes/2026-06-21-add-restaurant-menu-advisor/review-resolution.md`

## Risks and rollback
- Downstream models may still fail to follow the prompt in a given session; mitigated with explicit prompt boundaries, eval scenarios, and manual/static evidence.
- Host-specific image generation remains outside the portable correctness contract; the skill labels visuals as illustrative and gates rendering on explicit user request plus host support.
- Allergy handling remains safety-sensitive; the skill avoids safety guarantees and directs the diner to confirm ingredients, preparation, and cross-contact with staff.
- Rollback is additive: remove `skills/restaurant-menu-advisor/`, its eval fixture, README entries, and change-local lifecycle artifacts if needed.

## Reviewer notes
- Focus review on the allergy and generated-image safety boundaries in `skills/restaurant-menu-advisor/SKILL.md`.
- Confirm the static eval fixture is enough for this prompt-only skill and that no hidden runtime or provider dependency slipped in.
- Hosted CI is expected to run after PR open; it was not observed locally.

## Follow-ups
- None required before review.

## Opened PR

- URL: https://github.com/xiongxianfei/skillsmith/pull/31
- State: open
- Draft: no
- Initial hosted CI status: `Validate skill files` in progress/pending at handoff.
