# Proposal: Add a portable `restaurant-menu-advisor` skill

## Status

accepted

## Problem

Choosing from an unfamiliar restaurant menu is a recurring decision problem. A diner may need to balance taste, texture, appetite, budget, dietary constraints, allergies, sharing preferences, and willingness to try unfamiliar food while making a decision quickly. General-purpose chat can help, but ad hoc prompts often produce inconsistent shortlists, invent ingredients or preparation details, overlook uncertainty, or present generated food imagery as though it depicts the restaurant's actual dish.

The workflow becomes more safety-sensitive when a diner mentions a food allergy. A menu description cannot establish ingredient completeness or kitchen cross-contact controls, so a recommendation system can create harmful false reassurance if it labels a dish "safe."

The selected direction is a reusable Skillsmith skill rather than a standalone application. The skill therefore needs to work as portable Markdown with no AI API, external service, account credential, database, or hidden runtime dependency. It should preserve the useful visual-preview idea without making image generation a requirement for correct operation.

## Goals

1. Add one reusable Skillsmith skill whose primary job is helping a diner decide what to order from supplied restaurant-menu evidence.
2. Reduce decision time and regret by returning a small, differentiated shortlist and one clear leading recommendation.
3. Ground every recommendation in visible menu information and clearly separate menu facts, culinary inferences, and unknowns.
4. Collect only the missing constraints that materially affect the decision, especially allergy status, dietary restrictions, budget, appetite, taste and texture preferences, adventurousness, and whether dishes will be shared.
5. Provide a portable visual preview for the leading choice through an illustrative dish-visualization brief.
6. Allow an image-capable host to render that brief when the user explicitly requests an image, while preserving a complete text-only result on hosts without image generation.
7. Prevent generated imagery from being represented as the restaurant's actual photograph, plating, portion, or ingredient list.
8. Treat allergy-related behavior as safety-sensitive: avoid allergen-safety claims, identify relevant unknowns, and direct the diner to confirm ingredients, preparation, and cross-contact with restaurant staff.
9. Satisfy Skillsmith's current quality contract for trigger metadata, `$ARGUMENTS`, output structure, eval evidence, README synchronization, deterministic validation, and reviewer-visible safety evidence.

## Non-goals

1. Do not place restaurant orders, make reservations, process payment, or communicate with restaurant systems.
2. Do not build a standalone web or mobile application, API backend, user account system, or persistent preference store in this change.
3. Do not guarantee that a generated image matches the restaurant's real dish, portion, garnish, cookware, tableware, or presentation.
4. Do not declare a dish allergen-free or safe to eat based on a menu, model knowledge, generated image, or cuisine convention.
5. Do not estimate calories, macros, nutrition, or medical suitability unless the user supplies authoritative restaurant data and explicitly asks for analysis.
6. Do not scrape menus, reviews, social media, or real dish photographs as a required part of the workflow.
7. Do not turn the skill into a general meal planner, cooking assistant, restaurant finder, or travel concierge.
8. Do not change validator, installer, CI, or repository architecture unless downstream requirements identify a concrete incompatibility.
9. Do not add `allowed-tools`, scripts, image assets, secrets, or provider-specific API instructions.

## Vision fit

fits the current vision

This change captures a repeatable everyday decision workflow in inspectable, portable Markdown. It aims to improve reusable judgment rather than add a one-off novelty prompt, and it preserves the project's refusal to depend on hidden services or vendor-specific runtime behavior.

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
|---|---|---|
| Add a new skill to Skillsmith | in scope | Goals; Recommended direction; Architecture impact |
| Recommend what to order for dinner at a restaurant | in scope | Problem; Goals; Expected behavior changes |
| Generate a picture of the likely dish before ordering | in scope | Goals 5-6; Recommended direction; Scope budget (text brief guaranteed; rendered image conditional) |
| Work without an AI API and use an existing AI subscription or copy-paste workflow | in scope | Problem; Recommended direction; Architecture impact |
| Follow skill-authoring and repository best practices | in scope | Context; Testing and verification strategy; Risks and mitigations |
| Build a standalone application | out of scope | Non-goals; Scope budget |

## Scope budget

| Work item | Treatment | Reason |
|---|---|---|
| `restaurant-menu-advisor` prompt skill | core to this proposal | It is the selected product direction and the smallest reusable artifact that solves the recurring workflow. |
| Evidence-grounded menu comparison and ranking | core to this proposal | This is the skill's primary job and user value. |
| Bounded preference and constraint clarification | core to this proposal | Recommendations are unreliable without a small amount of relevant context. |
| Portable dish-visualization brief | core to this proposal | It preserves the visual-preview goal without creating a tool or API dependency. |
| Automatic image rendering by a capable host | first-slice candidate | Useful when available, but it is not part of the portable correctness contract and should occur only after explicit user request. |
| Allergy and cross-contact safety boundary | same-slice dependency | The skill could otherwise create materially harmful false reassurance. |
| New-skill eval fixture, including safety and misuse cases | same-slice dependency | New skills are not grandfathered and need reviewer-visible behavioral evidence. |
| README skill-table, command-list, and install-example synchronization | same-slice dependency | Public catalog and installation documentation must remain aligned with the new skill. |
| Manual model smoke evidence | same-slice dependency | The skill is behavior-heavy and includes a safety-sensitive path plus optional image-capable behavior. |
| Validator, CI, or installer changes | out of scope | Current repository mechanisms already support an additive pure-prompt skill and static eval fixture. |
| Persistent taste profiles, group voting, or feedback analytics | deferable follow-up | These may improve repeated use but require product and data-lifecycle decisions beyond a portable prompt. |
| Real restaurant photo retrieval, menu crawling, ordering, or reservation integrations | separate proposal | These introduce external services, data sources, permissions, and architecture changes. |
| Standalone application or API-backed product | separate proposal | This is a different product boundary and conflicts with the current no-API implementation constraint. |

## Context

Skillsmith's current vision favors a small catalog of durable skills that encode recurring workflows and remain understandable as portable Markdown. The constitution assigns prompt behavior to `skills/<skill-name>/SKILL.md`, requires written requirements for a new skill, preserves the pure-prompt boundary, and requires README synchronization and local validation. The workflow guide supports top-level proposals under `docs/proposals/` and routes change-local lifecycle records through `docs/changes/<change-id>/`, which is why this proposal lives in `docs/proposals/` while review, spec, test-spec, and later evidence use the change-local pack.

The approved skill-quality standard favors one clear primary job, concise skill bodies, function-first trigger descriptions, stable output contracts, a consistency check where silent drift is possible, and static eval scenarios covering normal use, indirect triggers, and edge or safety behavior. The current validator also requires new, non-grandfathered skills to provide `tests/evals/skills/<skill-name>/cases.yaml`.

Anthropic's current skill-authoring guidance is directionally consistent with the repository standard: skill metadata is the discovery surface, the loaded instruction body should stay concise, and skills should be tested with realistic evaluations. The proposed skill should therefore spend its prompt budget on decision quality, evidence boundaries, and safety rather than general explanations of food or restaurants.

Food-allergy dining guidance advises diners to ask restaurant staff what is in a dish, how it is prepared, and how cross-contact is avoided. That supports a hard product boundary: the skill can identify questions and uncertainty, but restaurant staff remain the source for current ingredient and kitchen-process confirmation.

Project-local evidence considered:

- `VISION.md`
- `CONSTITUTION.md`
- `AGENTS.md`
- `docs/workflows.md`
- `docs/project-map.md`
- `specs/skill-quality-standard.md`
- `specs/skill-quality-standard.test.md`
- `CONTRIBUTING.md`
- `.github/pull_request_template.md`
- `tests/validate_skills.py`
- `tests/check_readme_sync.py`

External reference points:

- Anthropic, [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- Food Allergy Research & Education, [Dining out with food allergies](https://www.foodallergy.org/resources/dining-out)

## Options considered

### Option 0: Do nothing

Rely on general-purpose chat, one-off prompting, or a copy-paste menu prompt without adding a durable Skillsmith catalog entry.

This avoids adding catalog surface, but it preserves the inconsistency, hallucination, missing uncertainty boundaries, image-authority confusion, and allergy false-reassurance risks identified in the problem statement. It also leaves no reusable, inspectable contract for future diners or reviewers.

**Disposition:** rejected.

### Option 1: Recommendation-only skill

Create a concise menu-ranking skill and omit all visualization behavior.

This gives the cleanest prompt boundary and broadest compatibility, but it silently drops the user's demonstrated visual-preview value. It also misses an opportunity to make uncertainty about likely appearance explicit.

**Disposition:** rejected.

### Option 2: Tool-dependent combined skill

Create one skill that requires an image-generation tool or external API and returns recommendations plus rendered dish images.

This most directly reproduces the current personal workflow, but it breaks Skillsmith's pure-prompt portability, excludes users without the same tool surface, adds provider-specific behavior, and risks making image generation look authoritative.

**Disposition:** rejected.

### Option 3: Portable recommendation skill with an illustrative visual brief

Create one `restaurant-menu-advisor` skill with a single primary job: decide what to order from the supplied menu. The text result always includes an evidence-grounded recommendation and a portable visualization brief for the leading dish. When the host supports image generation and the user explicitly requests a picture, it may render the brief as a clearly labeled illustration.

This preserves the user's combined workflow while keeping image generation outside the portable correctness contract. It also makes the generated visual inspectable as a description before rendering.

**Disposition:** recommended.

### Option 4: Separate `restaurant-menu-advisor` and `dish-visualizer` skills

Split decision support and visual rendering into independently triggered skills.

This creates clean component boundaries, but it adds catalog surface, requires users or agents to compose two skills, and is premature before evidence shows that dish visualization is valuable as an independent workflow.

**Disposition:** deferred follow-up.

## Recommended direction

Adopt Option 3 and add a new skill named `restaurant-menu-advisor`.

Candidate discovery metadata:

```yaml
---
name: restaurant-menu-advisor
description: >
  Restaurant menu advisor that compares dishes with the diner's preferences,
  budget, appetite, dietary constraints, and allergies, then returns a ranked
  shortlist and visual brief. Use for menu photos or asks like "what should I
  order?"
---
```

The downstream spec should preserve one primary workflow:

1. Ground the analysis in the user's supplied menu text, image, or other readable menu evidence.
2. Ask a bounded set of high-information clarification questions only when missing information could change the recommendation.
3. Separate explicit menu facts from culinary inferences and unknowns.
4. Return a small ranked set, normally three differentiated choices: best overall fit, lower-uncertainty or familiar choice, and more adventurous choice. When fewer suitable items exist, report that constraint rather than pad the list.
5. Select one leading recommendation and state the fit, tradeoffs, confidence, and any restaurant-staff questions that remain.
6. Produce an illustrative visualization brief derived from the dish name and explicit menu evidence. Inferred visual details should remain visibly qualified.
7. Render an image only after an explicit request and only when the active host supports image generation. The result should be labeled as an AI-generated illustration whose actual ingredients, portion, and plating may differ.
8. Run a final consistency check so the recommendation, evidence labels, price, dietary constraints, staff-confirmation questions, and visual brief do not contradict one another.

The visualization is supporting output, not evidence. The skill should never infer ingredients, allergen status, portion, or preparation from its own generated image.

For safety review, the eval fixture should use `high_risk: true`. Ordinary menu advice is low stakes, but allergy-related reliance can have severe consequences; the repository's lightweight high-risk review path is proportionate and provides the required safety notes and safety or misuse scenario.

## Expected behavior changes

After implementation:

- A user who uploads or pastes a restaurant menu and asks what to order receives a concise, evidence-grounded shortlist instead of an unstructured tour of the entire menu.
- A user who gives incomplete preference information receives only the clarifications that are likely to change the decision.
- Menu facts, likely taste or texture, and unknown details are distinguishable.
- The response identifies one leading dish, meaningful alternatives, tradeoffs, uncertainty, and relevant questions for staff.
- The user receives a copyable visual brief for the leading dish and may receive a clearly labeled generated illustration on an image-capable host after requesting it.
- Generated visuals are not represented as restaurant photographs and are not used as evidence for ingredients or allergen safety.
- Users who mention allergies receive stronger uncertainty handling and staff-confirmation guidance rather than a safety guarantee.
- Users who report an active allergic reaction are routed away from menu selection toward urgent medical or emergency guidance.
- Unreadable, partial, or contradictory menu evidence results in a request for clearer input or an explicit limited-confidence result rather than invented details.

## Architecture impact

Expected repository changes are limited to additive prompt, eval, and documentation artifacts:

```text
docs/proposals/2026-06-21-add-restaurant-menu-advisor.md
specs/restaurant-menu-advisor.md
specs/restaurant-menu-advisor.test.md
skills/restaurant-menu-advisor/SKILL.md
tests/evals/skills/restaurant-menu-advisor/cases.yaml
README.md
```

No application server, database, provider API, secret, generated image asset, or runtime dependency is introduced. `install.sh` already copies skill directories, so no installer change is expected. Current validator and README-sync behavior should be sufficient for this additive skill.

A separate architecture artifact is not expected for the recommended pure-prompt direction. Architecture review becomes relevant only if a downstream change introduces tool permissions, scripts, external services, persistent data, or generated assets.

## Testing and verification strategy

The first implementation should provide static eval evidence with concrete prompts and observable behavior. Recommended coverage:

| Scenario | Category | Expected proof |
|---|---|---|
| Complete menu plus budget and taste preferences | normal | Produces a grounded shortlist, one leading choice, tradeoffs, evidence labels, and a matching visual brief. |
| Casual request such as "Which of these should I get tonight?" with a menu image | indirect-trigger | Recognizes the menu-decision workflow and asks only material missing questions. |
| Blurry or partial menu | failure | Identifies unreadable or missing evidence and avoids inventing names, prices, ingredients, or preparation. |
| Severe food allergy mentioned | safety | Avoids declaring any dish safe, distinguishes allergy from preference, and surfaces staff-confirmation questions about ingredients and cross-contact. |
| User asks for an exact replica of the restaurant's real dish | misuse | Refuses the exactness claim while offering a clearly labeled illustrative brief or image. |
| User reports throat swelling after eating | non-trigger or safety | Stops menu advice and directs the user toward urgent medical or emergency help. |
| Menu contains fewer than three suitable items | edge | Returns only supported choices and explains the constraint instead of fabricating alternatives. |

The fixture should include reviewer-visible safety notes and `high_risk: true`. All examples should be fictional or sanitized.

Manual smoke evidence should cover:

1. A text-only or non-image path, proving the visual brief remains useful without image generation.
2. An image-capable path, proving the rendered image is explicitly illustrative and does not add unsupported ingredients or restaurant-specific claims.
3. At least one allergy scenario, proving the response does not imply allergen safety.
4. At least one unreadable-menu scenario, proving the workflow asks for better evidence instead of guessing.

Repository checks after implementation:

```bash
python -m unittest discover tests
python tests/validate_skills.py
python tests/check_readme_sync.py
```

A targeted installation smoke check may also copy the repository to a temporary target and confirm that `restaurant-menu-advisor` is installed with the existing mechanism.

Manual review should verify that:

- the description is English, trigger-forward, and under the contributor length limit;
- optional frontmatter is omitted;
- `$ARGUMENTS` and `## Output Format` are present;
- the prompt has one primary job and remains comfortably below the soft length threshold;
- workflow and output terminology are consistent;
- the final consistency check catches contradictions between menu evidence, recommendation, dietary constraints, and visualization;
- no live model or provider API is added to CI.

No validation has been run at proposal stage because implementation artifacts do not yet exist.

## Rollout and rollback

The change is additive and does not alter existing skill names or output contracts. It can roll out through the normal feature branch and pull-request path after proposal review, specification, test specification, implementation, and review.

README entries should ship in the same implementation slice as the skill so users do not receive a hidden or undocumented command. The new skill should not be added to the grandfathering baseline; its eval fixture should exist before merge.

Rollback is low-risk:

- remove `skills/restaurant-menu-advisor/`;
- remove `tests/evals/skills/restaurant-menu-advisor/`;
- remove the corresponding README table row and command references;
- retain the change artifacts as historical decision evidence, marking the proposal or downstream disposition accurately.

If image rendering proves inconsistent across hosts, the narrower rollback is to preserve the recommendation workflow and portable visual brief while removing any claim that the skill itself renders images.

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| The model invents menu items, ingredients, prices, preparation, or portion size. | Ground recommendations in supplied evidence, label inference and unknowns, and include a final consistency check. |
| A diner interprets a recommendation as an allergen-safety guarantee. | Classify the fixture as high risk, prohibit safety claims, distinguish allergy from preference, and require restaurant-staff confirmation of ingredients, preparation, and cross-contact. |
| A generated image is mistaken for the restaurant's actual dish. | Label it as an AI-generated illustration, avoid restaurant branding or exact-replica claims, and keep the visual from serving as factual evidence. |
| The visual brief adds unsupported garnishes or ingredients. | Derive it from explicit menu evidence, qualify inferred styling, and check it against the textual recommendation before rendering. |
| A blurry menu causes confident hallucination. | Treat insufficient evidence as a normal failure state and ask for a clearer image, transcription, or close-up. |
| The intake becomes too long for a diner seated at a restaurant. | Use bounded, high-information clarification and default to a concise decision-oriented output. |
| Recommendations feel overconfident despite subjective taste. | Show tradeoffs and calibrated confidence, and include differentiated alternatives rather than claiming an objectively best dish. |
| The skill behaves differently across ChatGPT, Claude, and other hosts. | Guarantee a portable text result and visual brief; treat actual image rendering as optional host capability rather than a cross-platform contract. |
| The skill over-triggers on cooking, restaurant search, or active medical emergencies. | Use a specific trigger description and include non-trigger or routing eval cases. |
| Sensitive allergy information is unnecessarily retained or repeated. | Ask only for decision-relevant constraints, avoid requesting identifying health history, and do not introduce persistence. |
| The combined recommendation and visualization scope becomes too broad. | Keep menu choice as the primary job; defer independent visualization tooling, real-photo search, and application features. |

## Open questions

None block proposal review.

The downstream spec should settle two bounded details:

1. Whether the visual brief appears in every default result or only after the user chooses a finalist. This proposal recommends including a concise brief for the leading choice by default and rendering an image only on explicit request.
2. Whether the public command name remains `restaurant-menu-advisor` or is shortened. This proposal recommends the explicit name because it improves discovery and avoids collision with general meal-planning intent.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-06-21 | Recommend one `restaurant-menu-advisor` skill | It captures the recurring decision workflow with a clear primary job and fits the current catalog model. | Standalone application; general-purpose meal assistant |
| 2026-06-21 | Guarantee a portable visual brief rather than image rendering | Preserves the user's visual-preview goal without an API, tool permission, or vendor dependency. | No visual support; required image-generation tool |
| 2026-06-21 | Allow explicit-request rendering on capable hosts | Provides practical value where available without making it part of the portable correctness contract. | Automatic rendering on every request |
| 2026-06-21 | Treat allergy behavior as high risk for eval purposes | False reassurance about allergens or cross-contact can cause severe harm, and the repository already provides a proportionate safety-evidence path. | Ordinary edge case only |
| 2026-06-21 | Keep generated imagery separate from evidence | A generated image cannot verify actual ingredients, portion, preparation, or plating. | Use generated appearance to enrich factual claims |
| 2026-06-21 | Keep app, persistence, web retrieval, and ordering integrations out of scope | They introduce different product, data, permission, and architecture decisions. | Include all future product features in the first skill |

## Next artifacts

1. Lightweight proposal-review R2 for the revised draft.
2. `specs/restaurant-menu-advisor.md` after the direction is accepted.
3. Architecture artifact only if proposal review or specification introduces tools, scripts, external services, persistent data, or generated assets.
4. `docs/plans/2026-06-21-add-restaurant-menu-advisor.md` after spec-review approval.
5. Plan review for the execution plan.
6. `specs/restaurant-menu-advisor.test.md` after plan-review approval, mapping the behavior and safety boundaries to eval scenarios and repository checks.

## Follow-on artifacts

- `docs/changes/2026-06-21-add-restaurant-menu-advisor/reviews/proposal-review-r1.md`
- `docs/changes/2026-06-21-add-restaurant-menu-advisor/reviews/proposal-review-r2.md`
- `docs/changes/2026-06-21-add-restaurant-menu-advisor/review-log.md`
- `docs/changes/2026-06-21-add-restaurant-menu-advisor/review-resolution.md`

## Readiness

The proposal is accepted after proposal-review R2 approved the revised direction and closed the R1 findings. The next stage is `spec`. No specification, implementation, verification, branch, or pull-request readiness is claimed.
