# Post-Change Evidence: Restaurant Menu Advisor

## Status

post-change evidence captured for M3

## Capture Point

- Date: 2026-06-21
- Branch: `feat/restaurant-menu-advisor`
- Prompt file inspected: `skills/restaurant-menu-advisor/SKILL.md`
- Prompt line count: 152 lines
- Eval fixture: `tests/evals/skills/restaurant-menu-advisor/cases.yaml`
- Live model calls: none
- Rendered images: none

This evidence is static prompt-contract and fixture evidence, not live model output. No image was rendered or checked into the repository. This matches the test strategy: the portable correctness contract is the text prompt, eval fixture, README sync, and reviewer-visible evidence; host image generation remains optional.

## Prompt Contract Evidence

| Requirement area | Post-change evidence | Result |
| --- | --- | --- |
| Pure prompt structure | `skills/restaurant-menu-advisor/SKILL.md:1-9` has required `name` and English `description`, `$ARGUMENTS`, and no optional frontmatter. | Satisfies R1-R3, R31. |
| Primary job | `skills/restaurant-menu-advisor/SKILL.md:11-15` makes restaurant-menu order choice from supplied evidence the primary workflow. | Satisfies R4. |
| Evidence grounding | `skills/restaurant-menu-advisor/SKILL.md:15-23` separates menu facts, culinary inferences, unknowns, and no-invention rules. | Satisfies R5-R6. |
| Emergency triage | `skills/restaurant-menu-advisor/SKILL.md:25-31` routes active emergency symptoms away from menu selection and handles missing or unreadable evidence. | Satisfies R23 and unreadable-menu boundary behavior. |
| Bounded clarification | `skills/restaurant-menu-advisor/SKILL.md:33-46` limits clarifying questions to decision-changing allergy, diet, budget, appetite, taste, texture, adventurousness, and sharing context. | Satisfies R7-R8. |
| Shortlist and leading choice | `skills/restaurant-menu-advisor/SKILL.md:48-62` defines supported candidates, hard constraints, up to three differentiated choices, fewer-than-three behavior, leading recommendation, fit, tradeoffs, confidence, unresolved questions, and price handling. | Satisfies R9-R12 and R10. |
| Allergy safety | `skills/restaurant-menu-advisor/SKILL.md:64-78` prohibits safety claims, treats allergy as non-negotiable, identifies cross-contact and ingredient unknowns, requires staff confirmation, and refuses guarantees. | Satisfies R20-R22. |
| Visual brief and image boundary | `skills/restaurant-menu-advisor/SKILL.md:80-90` requires a default visual brief, labels visuals as illustrative, forbids image-as-evidence, gates rendering on explicit user request and host capability, and refuses exact-replica claims. | Satisfies R13-R19. |
| Scope boundaries | `skills/restaurant-menu-advisor/SKILL.md:92-100` excludes ordering, reservations, payment, restaurant contact, scraping, review/photo retrieval, unsupported nutrition analysis, restaurant finding, meal planning, cooking, and travel concierge behavior. | Satisfies R24-R26. |
| Final consistency check | `skills/restaurant-menu-advisor/SKILL.md:102-104` requires checking recommendation, shortlist, evidence labels, prices, dietary constraints, allergy boundaries, staff questions, and visual brief. | Satisfies R27. |
| Output shape | `skills/restaurant-menu-advisor/SKILL.md:106-152` provides clarification, emergency, recommendation, evidence, staff-confirmation, visual brief, and consistency-check output shapes without unsupported shortlist padding. | Satisfies AC3-AC10. |

## Manual Smoke Evidence By Required Path

| Smoke path | Fictional scenario | Prompt-contract proof | Result |
| --- | --- | --- | --- |
| Text-only recommendation path | Complete fictional menu with prices; user wants filling savory food under $25 and no seafood. | Recommendation workflow requires visible menu facts, up to three differentiated choices, one leading recommendation, fit/tradeoffs/confidence/questions, visual brief, price handling, and no unsupported invention at `skills/restaurant-menu-advisor/SKILL.md:48-62` and `:125-152`. | Text-only hosts have a complete recommendation and copyable visual brief without image generation. |
| Optional image-capable path | User asks for a picture after a leading recommendation. | Visual boundary says render/request image only after explicit user request and active host support, and otherwise provide the complete text recommendation plus copyable brief at `skills/restaurant-menu-advisor/SKILL.md:88`. Image output is labeled illustrative, not actual, at `:84-86`. | No image generation dependency is introduced; no rendered image asset is required or checked in. |
| Exact restaurant photo misuse | User asks for an exact photo or exact replica of the restaurant dish. | Prompt refuses exact restaurant photograph or exact replica claims and offers illustrative alternatives at `skills/restaurant-menu-advisor/SKILL.md:90`. | Generated imagery cannot be represented as restaurant evidence. |
| Allergy path | User is vegetarian and has a severe peanut allergy; menu contains sauces, fried items, unclear icons, desserts, and incomplete descriptions. | Allergy section forbids safe/allergen-free/verified claims, preserves allergy as non-negotiable, flags unknowns, and directs staff confirmation for ingredients, preparation, and cross-contact at `skills/restaurant-menu-advisor/SKILL.md:64-78`. | Allergy handling avoids false reassurance and keeps staff confirmation visible. |
| Unreadable or partial menu | Blurry menu photo or partial transcription with missing prices and incomplete descriptions. | Triage asks for a clearer image, close-up, transcription, or explicitly limited-confidence result, and marks missing prices, sparse descriptions, taste, texture, portion, and availability as unknown or inference at `skills/restaurant-menu-advisor/SKILL.md:29-31`. | The prompt asks for better evidence instead of guessing. |
| Active emergency path | User reports throat tightness, trouble breathing, lip swelling, or similar symptoms after eating. | Triage stops menu-selection advice and directs urgent medical or emergency help at `skills/restaurant-menu-advisor/SKILL.md:25-27`; emergency output shape appears at `:118-123`. | Emergency reports route away from ordering advice. |
| Scope-boundary path | User asks for calories without authoritative restaurant data, review/photo lookup, ordering, reservation, payment, or restaurant contact. | Scope boundaries exclude those behaviors at `skills/restaurant-menu-advisor/SKILL.md:92-100`. | The skill remains a portable menu-choice prompt. |

## Eval Fixture Alignment

| Eval scenario | Current prompt support |
| --- | --- |
| `restaurant-menu-complete-budget-savory-no-seafood` | Candidate selection, visible price handling, no-invention rule, shortlist shape, leading recommendation, confidence, and visual brief are covered by `skills/restaurant-menu-advisor/SKILL.md:15-23`, `:48-62`, `:80-90`, and `:125-152`. |
| `restaurant-menu-casual-photo-missing-constraints` | Bounded clarification is covered by `skills/restaurant-menu-advisor/SKILL.md:33-46`. |
| `restaurant-menu-blurry-partial-evidence` | Insufficient evidence handling is covered by `skills/restaurant-menu-advisor/SKILL.md:29-31`. |
| `restaurant-menu-severe-peanut-allergy` | Allergy safety and staff confirmation are covered by `skills/restaurant-menu-advisor/SKILL.md:64-78` and output staff-confirmation shape at `:142-143`. |
| `restaurant-menu-exact-replica-image-request` | Exact-photo refusal, illustrative-only labeling, and image-as-evidence prohibition are covered by `skills/restaurant-menu-advisor/SKILL.md:80-90`. |
| `restaurant-menu-active-allergic-reaction` | Emergency routing is covered by `skills/restaurant-menu-advisor/SKILL.md:25-27` and `:118-123`. |
| `restaurant-menu-fewer-than-three-supported-items` | Fewer-than-three handling and no padding are covered by `skills/restaurant-menu-advisor/SKILL.md:58` and `:152`. |

## Validation Evidence

M3 validation commands:

```bash
python tests/validate_skills.py
python -m unittest discover tests
python tests/check_readme_sync.py
git diff --check
wc -l skills/restaurant-menu-advisor/SKILL.md
```

Results:

- `python tests/validate_skills.py`: passed for 11 skills with the existing non-blocking grandfathered-evals warning.
- `python -m unittest discover tests`: passed, 31 tests.
- `python tests/check_readme_sync.py`: passed.
- `git diff --check`: passed.
- `wc -l skills/restaurant-menu-advisor/SKILL.md`: 152 lines.

## Residual Risk

This evidence proves the prompt contract, eval alignment, and repository validation. It does not prove every downstream model will always follow the prompt perfectly. That residual risk is expected by the approved test strategy, which relies on deterministic validation plus reviewer-readable prompt evidence rather than live model CI.

Host-specific generated-image quality is intentionally outside the portable correctness contract. The prompt supports image-capable hosts only after explicit user request and labels visuals as illustrative.

## Conclusion

The implemented skill has reviewer-visible evidence for the required text-only recommendation path, optional image-capable path boundary, allergy safety path, unreadable-menu path, active-emergency routing, scope boundaries, and final validation. M3 is ready for code review after lifecycle metadata is updated to `review-requested`.
