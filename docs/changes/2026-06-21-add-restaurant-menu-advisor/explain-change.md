# Explain Change: Restaurant Menu Advisor

## Summary

This branch adds a portable `restaurant-menu-advisor` Skillsmith skill and the lifecycle evidence needed to review it. The implementation is intentionally prompt-only: it adds one skill, one high-risk eval fixture, README discovery updates, deterministic validation evidence, manual prompt-contract evidence, and review records. It does not add an app, API, provider integration, generated image asset, script, secret, dependency, installer change, validator change, or CI change.

The branch also reconciles workflow artifact locations that were surfaced during the same workflow: proposals live under `docs/proposals/`, durable specs under `specs/`, plan bodies under `docs/plans/`, review records under `docs/changes/<change-id>/reviews/`, and old terminal plan history under `docs/plan-archive.md`.

## Problem

The user wanted a reusable way to decide what to order from a restaurant menu, including a likely-dish visual preview, without depending on an AI API, standalone app, hidden runtime service, or vendor-specific image feature. The problem is safety-sensitive when allergies are mentioned because menu text cannot prove complete ingredients or kitchen cross-contact controls.

The resulting change needed to preserve Skillsmith's skill contract: portable Markdown skills under `skills/<name>/SKILL.md`, required `$ARGUMENTS`, required `## Output Format`, README synchronization, eval evidence for new skills, and reviewer-visible high-risk safety evidence.

## Decision Trail

| Decision point | Outcome | Source |
| --- | --- | --- |
| Proposal option selected | Option 3: portable recommendation skill with an illustrative visual brief. Do-nothing, recommendation-only, tool-dependent image rendering, and separate visualizer skill were rejected. | `docs/proposals/2026-06-21-add-restaurant-menu-advisor.md` |
| Proposal review | R1 requested a do-nothing option and path clarification; R2 approved after resolution. | `docs/changes/2026-06-21-add-restaurant-menu-advisor/reviews/proposal-review-r1.md`, `proposal-review-r2.md`, `review-resolution.md` |
| Requirements | R1-R34 define the skill file contract, menu grounding, clarification, shortlist, visual boundary, allergy handling, non-goals, eval fixture, README sync, and validation. | `specs/restaurant-menu-advisor.md` |
| Architecture | Separate architecture artifact not required because the accepted boundary is additive pure Markdown prompt/eval/docs work. | `docs/changes/2026-06-21-add-restaurant-menu-advisor/reviews/spec-review-r1.md` |
| Test strategy | Static eval fixture plus deterministic repo validation and manual prompt-contract evidence. No live model or generated-image CI. | `specs/restaurant-menu-advisor.test.md` |
| Plan milestones | M1 eval fixture, M2 skill and README sync, M3 post-change evidence. All three code-review rounds closed with no material findings. | `docs/plans/2026-06-21-add-restaurant-menu-advisor.md`, `review-log.md` |

## Diff Rationale By Area

| File | Change | Reason | Source artifact | Test/evidence |
| --- | --- | --- | --- | --- |
| `skills/restaurant-menu-advisor/SKILL.md` | Added the new prompt skill with required frontmatter, `$ARGUMENTS`, menu-evidence workflow, bounded clarification, shortlist, leading recommendation, allergy boundary, visual brief boundary, scope limits, consistency check, and output format. | Implements the core portable skill while keeping image generation optional and illustrative only. | R1-R27, R31-R32, AC1-AC10, AC15 | `m2-evidence.md`, `post-change-evidence.md`, code-review M2/M3 |
| `tests/evals/skills/restaurant-menu-advisor/cases.yaml` | Added `version: 1`, `high_risk: true`, safety notes, and seven fictional scenarios covering normal, indirect trigger, failure, safety, misuse, active emergency, and fewer-than-three edge behavior. | Provides reviewer-visible evidence for a new high-risk skill before prompt implementation. | R20-R24, R28-R29, AC11 | Direct `validate_cases_file`, `validate_skills`, code-review M1 |
| `README.md` | Added the skill to the skill table, installed command list, one-session command examples, copy-paste usage examples, and skill detail section. | Keeps public catalog and install/use surfaces synchronized with the new skill directory. | R30, AC12 | `python tests/check_readme_sync.py`, code-review M2 |
| `docs/proposals/2026-06-21-add-restaurant-menu-advisor.md` | Recorded the accepted proposal under the top-level proposal location and added the do-nothing baseline and clarified visual-image treatment. | Preserves the product decision and closes proposal-review R1 findings. | Proposal-review PR-R1-001 through PR-R1-003 | `review-resolution.md`, proposal-review R2 |
| `specs/restaurant-menu-advisor.md` | Added the durable behavior contract and acceptance criteria for the skill. | Makes the implementation testable and prevents the prompt from drifting into unsupported app, scraping, ordering, nutrition, or safety guarantees. | Proposal recommended direction | Spec-review R1 |
| `specs/restaurant-menu-advisor.test.md` | Added traceable test cases T1-T14 and manual QA coverage. | Maps requirements to deterministic checks, fixture expectations, manual smoke evidence, and closeout validation. | R1-R34, AC1-AC16 | Test-spec approval R1 |
| `docs/plans/2026-06-21-add-restaurant-menu-advisor.md` | Added and maintained the execution plan, milestone states, risks, recovery paths, validation notes, and handoff summary. | Coordinates the multi-step change and records why eval evidence came before the prompt. | Plan-review R1 | Code-review M1-M3 |
| `docs/changes/2026-06-21-add-restaurant-menu-advisor/change.yaml` | Added change metadata, validation history, current routing, review state, and open-finding status. | Gives the workflow a machine-readable current state and durable pointers to proposal/spec/test/plan/reviews. | Workflow guide | Validation entries and review log |
| `docs/changes/2026-06-21-add-restaurant-menu-advisor/baseline-evidence.md` | Recorded M1 baseline proof that the eval fixture existed before the skill prompt. | Makes the test-first sequence visible and explains why direct fixture validation was needed before the skill directory existed. | Plan M1, T2 | Code-review M1 |
| `docs/changes/2026-06-21-add-restaurant-menu-advisor/m2-evidence.md` | Recorded prompt-contract and README synchronization evidence after adding the skill. | Gives reviewers a concise inspection surface for M2 without relying on memory. | Plan M2, T1, T11-T13 | Code-review M2 |
| `docs/changes/2026-06-21-add-restaurant-menu-advisor/post-change-evidence.md` | Recorded text-only, image-boundary, exact-replica misuse, allergy, unreadable-menu, emergency, scope-boundary, eval-alignment, and validation evidence. | Provides the required manual/static smoke evidence before final review. | Plan M3, AC16, T3-T10, T13-T14 | Code-review M3 |
| `docs/changes/2026-06-21-add-restaurant-menu-advisor/review-log.md` and `reviews/*.md` | Added proposal, spec, plan, test-spec, and code-review records. | Keeps review outcomes, material findings, approvals, and milestone closeout visible. | Workflow guide and stage skills | All reviews recorded; open findings empty |
| `docs/changes/2026-06-21-add-restaurant-menu-advisor/review-resolution.md` | Recorded closure of proposal-review R1 findings. | Required because R1 had material findings; later review approved the revisions. | Proposal-review R1/R2 | Closeout status closed |
| `docs/workflows.md` | Clarified source order, artifact-location table, plan archive, follow-up routing, and stage routing. | Rectifies artifact placement so proposal/spec/plan/review/explain paths are not ambiguous. | User workflow-location request | Downstream artifacts follow the clarified paths |
| `docs/plan.md` | Converted active plan rows to relative links, added the restaurant plan, and kept only active routing context. | Makes the plan index current and bounded. | `docs/workflows.md` | Current row routes to this explain-change stage before this artifact is committed |
| `docs/plan-archive.md` | Added archive home and moved the superseded editor skill optimization plan out of active routing. | Puts terminal plan history in the right place instead of keeping stale routing in the active plan index. | `docs/workflows.md` | Manual diff inspection |

## Tests Added Or Changed

| Test or evidence ID | What it proves | Why this level is appropriate |
| --- | --- | --- |
| Eval fixture scenario `restaurant-menu-complete-budget-savory-no-seafood` | Complete-menu recommendation returns a grounded shortlist, leading choice, tradeoffs, confidence, and visual brief without inventing facts. | Static eval expectations are the repository standard for skill behavior. |
| Eval fixture scenario `restaurant-menu-casual-photo-missing-constraints` | Casual menu-choice phrasing triggers bounded clarification rather than a long intake or full-menu ranking. | Covers indirect trigger behavior required by the skill-quality standard. |
| Eval fixture scenario `restaurant-menu-blurry-partial-evidence` | Partial evidence asks for clearer input or limited-confidence output instead of hallucinating names, prices, ingredients, or preparation. | Covers normal failure behavior without requiring live OCR. |
| Eval fixture scenario `restaurant-menu-severe-peanut-allergy` | Allergy handling avoids safety guarantees and directs staff confirmation for ingredients, preparation, and cross-contact. | High-risk static scenario is proportionate for a prompt-only skill. |
| Eval fixture scenario `restaurant-menu-exact-replica-image-request` | Exact restaurant photo/replica claims are refused; illustrative visual support remains available. | Covers generated-image misuse without requiring image generation. |
| Eval fixture scenario `restaurant-menu-active-allergic-reaction` | Active emergency symptoms stop menu advice and route toward urgent help. | Covers safety routing required by R23. |
| Eval fixture scenario `restaurant-menu-fewer-than-three-supported-items` | The shortlist is not padded when fewer than three suitable choices are supported. | Covers the edge behavior from R10. |
| `python tests/check_readme_sync.py` | README skill table and slash-command mentions stay synchronized with skill directories. | Directly checks the documentation surface affected by M2. |
| `post-change-evidence.md` | Static prompt-contract smoke evidence covers text-only, image-capable boundary, allergy, unreadable-menu, emergency, and scope-boundary paths. | The approved strategy avoids live model or generated-image CI while keeping behavior reviewable. |

No executable production test code was added because the product artifact is a Markdown prompt. The deterministic repository checks validate skill structure, eval fixture schema, README synchronization, and existing validator behavior.

## Validation Evidence Available Before Final Verify

Commands recorded during implementation and review:

```bash
python -c 'from pathlib import Path; from tests.validate_skills import validate_cases_file; result = validate_cases_file("restaurant-menu-advisor", Path("tests/evals/skills/restaurant-menu-advisor/cases.yaml")); assert not result.errors, result.errors; print("direct eval fixture validation passed")'
python tests/validate_skills.py
python -m unittest discover tests
python tests/check_readme_sync.py
git diff --check
git diff --check HEAD
wc -l skills/restaurant-menu-advisor/SKILL.md
```

Available results:

- `python tests/validate_skills.py` passed for 11 skills. It consistently reported the existing non-blocking grandfathered-evals warning for older skills without eval fixtures.
- `python -m unittest discover tests` passed with 31 tests.
- `python tests/check_readme_sync.py` passed.
- `git diff --check` and `git diff --check HEAD` passed.
- `wc -l skills/restaurant-menu-advisor/SKILL.md` reported 152 lines.
- No hosted CI result is recorded yet.

## Review Resolution Summary

Material findings existed only in proposal-review R1:

| Count | Disposition |
| --- | --- |
| 3 | accepted and closed |
| 0 | open |
| 0 | needs-decision |

`docs/changes/2026-06-21-add-restaurant-menu-advisor/review-resolution.md` records the closure. Proposal-review R2 approved the revised proposal. Spec-review R1, plan-review R1, test-spec approval R1, and code-review M1-M3 recorded no material findings.

## Alternatives Rejected

The proposal rejected:

- do nothing/status quo, because ad hoc prompting keeps the inconsistency, hallucination, and false-reassurance risks;
- recommendation-only skill, because it drops the useful visual-preview goal;
- tool-dependent combined skill, because requiring image generation or an external API breaks portability;
- separate `restaurant-menu-advisor` and `dish-visualizer` skills, because splitting the workflow is premature before the visual behavior proves independently useful;
- standalone app/API/persistence/order integration, because those are different product and architecture boundaries.

The implementation also avoided validator, installer, CI, dependency, script, and architecture changes because the accepted product boundary did not require them.

## Scope Control

Preserved non-goals:

- no restaurant orders, reservations, payments, or restaurant contact;
- no menu scraping, review scraping, social-media lookup, or real dish photo retrieval;
- no generated image asset checked into the repo;
- no claim that a visual brief or generated image is the restaurant's real dish, portion, plating, garnish, tableware, ingredient list, or safety evidence;
- no allergen-free or safe-to-eat claim from menu text, model knowledge, cuisine convention, or generated imagery;
- no nutrition, calorie, macro, or medical-suitability analysis unless authoritative restaurant data is supplied and explicitly requested;
- no standalone app, API, account system, database, persistent profile, or provider API instructions;
- no changes to installer, validator, CI, or repository architecture.

## Risks And Follow-Ups

Remaining risks:

- A downstream model may still fail to follow the prompt in a specific session. This is an expected residual risk for a prompt skill and is mitigated by explicit instructions, eval scenarios, and reviewable prompt-contract evidence.
- Host-specific image rendering quality remains outside the portable correctness contract. The skill only permits rendering after explicit request and host support, and labels output as illustrative.
- Allergy advice remains safety-sensitive. The prompt prohibits safety guarantees and keeps staff confirmation prominent, but restaurant staff remain the source for current ingredients, preparation, and cross-contact controls.
- Hosted CI has not been recorded yet; that belongs to later verification/PR stages.

Current workflow state after this explain-change artifact is recorded: implementation milestones are closed and the next stage is `verify`. This explanation does not claim final verify, branch readiness, PR body readiness, PR open readiness, or hosted CI-final status.
