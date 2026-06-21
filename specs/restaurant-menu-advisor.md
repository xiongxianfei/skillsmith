# Spec: `restaurant-menu-advisor` Skill

## Status

approved

## Related proposal

- Proposal: `docs/proposals/2026-06-21-add-restaurant-menu-advisor.md`
- Proposal review: `docs/changes/2026-06-21-add-restaurant-menu-advisor/reviews/proposal-review-r2.md`

## Goal and context

Add one portable Skillsmith skill named `restaurant-menu-advisor` that helps a diner decide what to order from supplied restaurant-menu evidence. The skill must return a small, evidence-grounded shortlist, one leading recommendation, and a portable illustrative visual brief for the leading dish.

The skill must remain a plain Markdown prompt asset. It must not require an AI API, external service, account credential, database, checked-in generated image, hidden runtime dependency, or provider-specific tool permission for correct operation.

Allergy behavior is safety-sensitive. The skill may help identify uncertainty and restaurant-staff questions, but it must not declare a dish allergen-free or safe to eat based on menu text, model knowledge, cuisine convention, or generated imagery.

## Glossary

- **Menu evidence:** User-supplied menu text, menu photo content visible to the active host, a pasted dish list, or other restaurant-provided readable dish evidence.
- **Menu fact:** A dish name, price, description, category, preparation note, dietary label, or ingredient explicitly visible in the supplied menu evidence.
- **Culinary inference:** A qualified taste, texture, richness, portion-style, cuisine, or likely appearance inference based on explicit menu facts and general culinary knowledge.
- **Unknown:** A dish attribute not established by supplied menu evidence.
- **Leading recommendation:** The one dish the skill recommends most strongly for the user's stated context.
- **Shortlist:** A ranked set of supported dish choices, normally three, each differentiated by fit and tradeoff.
- **Visual brief:** A copyable text description for an illustrative dish image. It is not evidence of the restaurant's actual dish, portion, plating, garnish, cookware, or ingredients.
- **Rendered image:** An optional AI-generated image produced by an image-capable host after explicit user request.
- **Cross-contact:** Allergen transfer through shared surfaces, fryers, utensils, preparation areas, or other kitchen handling.

## Examples first

Example E1: complete menu and preferences
Given a user pastes a fictional restaurant menu with prices and says they want a filling, savory dinner under $25 with no seafood
When the skill responds
Then it returns a ranked shortlist of up to three supported dishes, names one leading recommendation, grounds each item in visible menu facts, notes relevant culinary inferences and unknowns, and includes an illustrative visual brief for the leading dish.

Example E2: missing constraints
Given a user uploads a readable menu image and says "What should I get tonight?"
When allergy status, budget, appetite, and preferences are missing
Then the skill asks only a bounded set of high-information questions likely to change the recommendation instead of ranking the full menu immediately.

Example E3: severe allergy
Given a user says they have a severe peanut allergy and provides a menu with sauces and desserts
When the skill recommends dishes
Then it does not call any dish safe, flags relevant unknowns, distinguishes allergy from preference, and lists staff-confirmation questions about ingredients, preparation, and cross-contact before the user orders.

Example E4: unreadable or partial menu
Given the supplied menu image is blurry or only shows half of several dish descriptions
When the skill cannot read enough evidence
Then it asks for a clearer image, close-up, or transcription and avoids inventing dish names, prices, ingredients, or preparation.

Example E5: image request
Given the user has already received a leading recommendation and asks for a picture
When the active host supports image generation
Then the skill may render or request rendering from the visual brief, labels it as an AI-generated illustration, and does not add factual claims from the image.

Example E6: exact-replica request
Given the user asks for "an exact photo of what this restaurant will serve"
When only menu evidence is supplied
Then the skill refuses the exactness claim and offers a clearly labeled illustrative visual brief or generated illustration instead.

Example E7: active allergic reaction
Given the user says their throat is swelling after eating
When the skill is invoked
Then it stops menu-selection advice and directs the user toward urgent medical or emergency help.

## Requirements

R1. The skill MUST be added as `skills/restaurant-menu-advisor/SKILL.md` with YAML frontmatter `name: restaurant-menu-advisor`.

R2. The skill description MUST be English, trigger-forward, and identify both the skill's function and situations where it applies, including menu photos, pasted menus, and casual asks such as "what should I order?"

R3. The skill body MUST include the literal `$ARGUMENTS` placeholder and a `## Output Format` section.

R4. The skill MUST have one primary job: help the user decide what to order from supplied restaurant-menu evidence.

R5. The skill MUST ground dish recommendations in supplied menu evidence and distinguish menu facts from culinary inferences and unknowns.

R6. The skill MUST NOT invent dish names, prices, ingredients, preparation methods, dietary labels, portions, restaurant-specific plating, or availability when they are not present in supplied menu evidence.

R7. The skill MUST ask clarification questions only when missing information could materially change the recommendation.

R8. When clarification is needed, the skill MUST keep questions bounded and prioritize allergy status, dietary restrictions, budget, appetite, taste preferences, texture preferences, adventurousness, and sharing context.

R9. When enough evidence and constraints are available, the skill MUST return a ranked shortlist of normally three differentiated choices: best overall fit, lower-uncertainty or familiar choice, and more adventurous choice.

R10. If fewer than three suitable menu items are supported by the evidence and constraints, the skill MUST return only the supported choices and explain the constraint rather than padding the shortlist.

R11. The skill MUST identify one leading recommendation when enough evidence exists to choose one.

R12. For the leading recommendation, the skill MUST state fit, tradeoffs, confidence, and unresolved questions that could affect the decision.

R13. The skill MUST include a concise visual brief for the leading recommendation by default when a leading recommendation is made.

R14. The visual brief MUST be derived from the dish name and explicit menu evidence, with inferred visual details qualified as illustrative or likely.

R15. The skill MUST state that the visual brief or rendered image is not the restaurant's actual photograph and may differ in ingredients, portion, plating, garnish, tableware, and presentation.

R16. The skill MUST NOT use a visual brief or rendered image as evidence for ingredients, allergens, preparation, portion, or safety.

R17. The skill MUST render or request a rendered image only when the user explicitly asks for an image and the active host supports image generation.

R18. When an image is rendered, the skill MUST label it as an AI-generated illustration and avoid restaurant branding or exact-replica claims.

R19. If the active host does not support image generation, the skill MUST still provide a complete text-only recommendation and a copyable visual brief.

R20. When the user mentions an allergy, the skill MUST avoid allergen-safety claims and MUST direct the user to confirm ingredients, preparation, and cross-contact with restaurant staff.

R21. When the user mentions an allergy, the skill MUST distinguish allergy requirements from preferences or dislikes and avoid treating an allergy as a negotiable taste preference.

R22. When menu evidence suggests possible allergen uncertainty, shared preparation, sauces, marinades, desserts, fried items, or unclear labels, the skill MUST surface relevant staff-confirmation questions.

R23. When the user reports symptoms consistent with an active allergic reaction or medical emergency, the skill MUST stop menu-selection advice and direct the user toward urgent medical or emergency help.

R24. The skill MUST NOT estimate calories, macros, nutrition, or medical suitability unless the user supplies authoritative restaurant data and explicitly asks for that analysis.

R25. The skill MUST NOT scrape menus, reviews, social media, or real dish photographs as part of its required workflow.

R26. The skill MUST NOT place orders, make reservations, process payment, communicate with restaurant systems, or claim to contact restaurant staff.

R27. The skill MUST include a final consistency check that verifies the recommendation, shortlist, evidence labels, price handling, dietary constraints, allergy boundaries, staff-confirmation questions, and visual brief do not contradict each other.

R28. The implementation MUST add `tests/evals/skills/restaurant-menu-advisor/cases.yaml` with `high_risk: true` and reviewer-visible safety notes.

R29. The eval fixture MUST cover normal, indirect-trigger, failure, safety, misuse, active-medical-emergency, and fewer-than-three-supported-items scenarios.

R30. The README skills table and any enumerated installation or usage examples MUST be updated so the new skill is visible to users.

R31. The implementation MUST NOT add optional frontmatter such as `argument-hint`, `effort`, or `allowed-tools` unless a later accepted proposal and spec require it.

R32. The implementation MUST NOT introduce new runtime dependencies, CI dependencies, scripts, image assets, secrets, external services, or provider-specific API instructions.

R33. The implementation MUST pass `python tests/validate_skills.py`.

R34. The implementation SHOULD pass `python -m unittest discover tests` and `python tests/check_readme_sync.py` because the change touches eval and README synchronization behavior.

## Inputs and outputs

Inputs:

- Menu evidence supplied by the user through text, image, or other readable content available to the active host.
- Optional user constraints: allergies, dietary restrictions, dislikes, budget, appetite, taste and texture preferences, adventurousness, sharing context, and image request.
- Optional authoritative restaurant nutrition data when the user explicitly asks for nutrition analysis.

Outputs:

- Clarification questions when material constraints are missing.
- Otherwise, a decision-oriented response with a ranked shortlist, one leading recommendation, evidence labels, tradeoffs, confidence, unknowns, staff-confirmation questions when needed, and a visual brief.
- Optional rendered image only after explicit image request on an image-capable host.

The skill output is advisory text. It does not create persistent state, orders, reservations, payment records, accounts, API calls, or stored preference profiles.

## State and invariants

- The skill remains portable Markdown and must be useful in text-only hosts.
- Supplied menu evidence is the only source for restaurant-specific facts.
- Culinary inference must remain qualified and separable from menu facts.
- Generated imagery is supporting output only and never factual evidence.
- Allergy handling must remain conservative and must not imply restaurant-verified safety.
- The skill does not retain user allergy, diet, budget, or preference information beyond the current conversation.
- The skill's primary workflow remains menu choice, not restaurant discovery, meal planning, cooking, nutrition coaching, or travel planning.

## Error and boundary behavior

- If menu evidence is unreadable, partial, contradictory, or insufficient, the skill MUST ask for clearer evidence or provide an explicitly limited-confidence result.
- If the user asks for a recommendation without any menu evidence, the skill MUST request menu evidence rather than inventing likely restaurant dishes.
- If the user asks for a guaranteed allergen-safe dish, the skill MUST refuse the guarantee and redirect to restaurant-staff confirmation.
- If the user asks for an exact restaurant dish photograph or exact replica, the skill MUST refuse the exactness claim and offer an illustrative brief or image.
- If the user asks for ordering, reservation, payment, or restaurant contact actions, the skill MUST state that those actions are outside scope.
- If user preferences conflict with available menu evidence, the skill MUST explain the conflict and choose from supported items only when possible.
- If no suitable item can be recommended from the evidence and constraints, the skill MUST say so and identify what additional evidence or staff confirmation is needed.

## Compatibility and migration

This is an additive new skill. It must not rename or change existing skills, existing skill output contracts, installer behavior, validator behavior, CI behavior, or repository architecture.

The new skill must be compatible with existing Skillsmith validation rules for skill frontmatter, `$ARGUMENTS`, `## Output Format`, README synchronization, and eval fixtures.

Rollback is removal of:

- `skills/restaurant-menu-advisor/`
- `tests/evals/skills/restaurant-menu-advisor/`
- the corresponding README entries

Change-local lifecycle artifacts should remain as historical decision evidence unless a later workflow artifact marks them superseded or abandoned.

## Observability

The implementation has no runtime telemetry, logs, metrics, traces, or audit events.

Reviewer-visible observability is provided through:

- static eval fixture cases and expected behavior;
- manual smoke evidence recorded during implementation or review;
- local validation commands and their outputs;
- review records under `docs/changes/2026-06-21-add-restaurant-menu-advisor/`.

## Security and privacy

- The skill MUST NOT request secrets, credentials, account data, private local paths, or identifying medical history.
- The skill MUST ask only for decision-relevant allergy, dietary, budget, appetite, and preference information.
- Examples and eval cases involving allergies or medical symptoms MUST use fictional or sanitized inputs.
- The skill MUST NOT present itself as medical advice, emergency support, or a substitute for restaurant-staff ingredient and cross-contact confirmation.
- The skill MUST route active allergic reaction reports toward urgent medical or emergency help rather than menu selection.

## Accessibility and UX

- The default response SHOULD be concise enough for a diner actively choosing at a restaurant.
- The output MUST be scannable, with the leading recommendation easy to identify.
- Clarification questions MUST be few enough to answer quickly and MUST focus on decision-changing constraints.
- The visual brief MUST be text-copyable so text-only users can still use it.
- The skill MUST avoid in-app or provider-specific UI instructions because the artifact is portable Markdown.

## Performance expectations

The skill has no runtime performance contract beyond prompt usability.

The skill body SHOULD remain concise enough for normal skill-loading behavior and should avoid long food encyclopedias, broad cuisine education, or exhaustive menu tours.

The output SHOULD avoid ranking every menu item unless the supplied menu is already very small and doing so remains concise.

## Edge cases

EC1. Menu evidence has dishes but no prices; the skill may still recommend but must not invent prices and must mark budget fit as unknown.

EC2. Menu evidence has prices but no descriptions; the skill must ground recommendations in visible categories, names, and prices and label taste or texture as inference.

EC3. The user has multiple constraints, such as vegetarian and nut allergy; the skill must handle both and must not let one erase the other.

EC4. A menu has dietary icons without a legend; the skill must treat icon meaning as unknown unless the legend is visible or supplied.

EC5. A dish name implies a common allergen, but the menu description is incomplete; the skill must flag uncertainty and staff-confirmation questions rather than guaranteeing exclusion.

EC6. The user asks for the cheapest, most filling option; the skill must use visible prices and menu descriptions, and must mark portion size as inferred or unknown.

EC7. The user wants shared dishes for a group; the skill must account for sharing context if supplied and ask for group constraints when they could change the recommendation.

EC8. A menu contains fewer than three suitable items; the skill must return fewer than three choices and explain why.

EC9. The user asks for nutrition analysis without authoritative restaurant nutrition data; the skill must explain the data limitation before any analysis.

EC10. The user asks to compare restaurant reviews or photos; the skill must state that required scraping or retrieval is out of scope unless the user supplies that evidence directly.

EC11. The user asks for an image before a leading recommendation exists; the skill must either ask for enough menu evidence to choose a dish or create only a clearly illustrative brief tied to supplied evidence.

EC12. The user says they are experiencing throat swelling, trouble breathing, or a similar emergency symptom; the skill must stop ordering advice and direct urgent medical or emergency action.

## Non-goals

- Do not build a standalone web app, mobile app, API backend, user account system, database, or persistent preference store.
- Do not place orders, make reservations, process payments, or communicate with restaurants.
- Do not scrape menus, reviews, social media, or real dish photographs as required workflow.
- Do not guarantee generated images match the real restaurant dish.
- Do not treat generated imagery as evidence.
- Do not declare dishes allergen-free or safe to eat.
- Do not become a general meal planner, cooking assistant, restaurant finder, travel concierge, or nutrition coach.
- Do not change validator, installer, CI, or repository architecture unless a later reviewed artifact identifies a concrete incompatibility.

## Acceptance criteria

AC1. `skills/restaurant-menu-advisor/SKILL.md` exists with required frontmatter, `$ARGUMENTS`, and `## Output Format`.

AC2. The skill description is English and trigger-forward, including menu evidence and casual order-choice phrasing.

AC3. The prompt instructs the assistant to ground recommendations in supplied menu evidence and label facts, inferences, and unknowns.

AC4. The prompt instructs the assistant to ask bounded clarification questions only when missing information could change the recommendation.

AC5. The default recommendation output includes a ranked shortlist, one leading recommendation, tradeoffs, confidence, unresolved questions, and a visual brief when enough evidence exists.

AC6. The prompt prohibits inventing menu items, prices, ingredients, preparation, portions, and restaurant-specific appearance.

AC7. The prompt includes allergy-specific safety boundaries: no safety claims, staff-confirmation questions, and cross-contact uncertainty.

AC8. The prompt routes active allergic reaction or emergency symptom reports away from menu selection toward urgent medical or emergency help.

AC9. The prompt labels visual briefs and rendered images as illustrative and prevents using them as evidence.

AC10. The prompt allows rendered images only after explicit user request and host capability.

AC11. `tests/evals/skills/restaurant-menu-advisor/cases.yaml` exists, uses `high_risk: true`, includes reviewer-visible safety notes, and covers the required scenario categories from R29.

AC12. README documentation includes the new skill in the public skills table and any enumerated usage or installation surfaces affected by the new skill.

AC13. `python tests/validate_skills.py` passes.

AC14. `python -m unittest discover tests` and `python tests/check_readme_sync.py` pass or any skipped check is explicitly justified in the implementation handoff.

AC15. No new runtime dependencies, CI dependencies, scripts, image assets, secrets, external services, or provider-specific API instructions are introduced.

AC16. Manual smoke evidence covers text-only output, optional image-capable behavior, allergy handling without safety claims, and unreadable-menu behavior.

## Open questions

None block spec-review.

The spec resolves the proposal's two bounded questions as follows:

1. A concise visual brief appears by default when the skill makes a leading recommendation.
2. The public skill name remains `restaurant-menu-advisor`.

## Next artifacts

1. Execution plan after spec-review approval.
2. Plan review for the execution plan.
3. `specs/restaurant-menu-advisor.test.md` after plan-review approval.

## Follow-on artifacts

- `docs/changes/2026-06-21-add-restaurant-menu-advisor/reviews/spec-review-r1.md`
- `docs/plans/2026-06-21-add-restaurant-menu-advisor.md`
- `docs/changes/2026-06-21-add-restaurant-menu-advisor/reviews/plan-review-r1.md`
- `specs/restaurant-menu-advisor.test.md`

## Readiness

Spec-review R1 approved this spec and recorded that no separate architecture artifact is required for the current pure-prompt boundary. Plan-review R1 approved the execution plan, and `specs/restaurant-menu-advisor.test.md` is the active test spec. The next stage is `implement` M1. No implementation completion, verification, branch readiness, or PR readiness is claimed.
