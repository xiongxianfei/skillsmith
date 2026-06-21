# M2 Evidence: Restaurant Menu Advisor Prompt And README

## Scope

Milestone M2 adds the portable `restaurant-menu-advisor` prompt skill and public README entries. It keeps the implementation inside the approved pure-prompt boundary.

## Authored Surfaces

- `skills/restaurant-menu-advisor/SKILL.md`
- `README.md`
- `docs/changes/2026-06-21-add-restaurant-menu-advisor/change.yaml`
- `docs/plans/2026-06-21-add-restaurant-menu-advisor.md`
- `docs/plan.md`

## Prompt Contract Inspection

The skill prompt includes:

- required frontmatter only: `name` and English trigger-forward `description`;
- `$ARGUMENTS` and `## Output Format`;
- one primary job: choose what to order from supplied menu evidence;
- evidence labels for menu facts, culinary inferences, and unknowns;
- bounded clarification guidance for decision-changing missing constraints;
- ranked shortlist, leading recommendation, confidence, tradeoffs, unresolved questions, and visual brief;
- no-invention rules for dish names, prices, ingredients, preparation, portions, availability, or restaurant-specific appearance;
- allergy boundaries: no safety claims, allergy is non-negotiable, staff confirmation for ingredients, preparation, and cross-contact;
- active allergic reaction routing away from menu selection;
- illustrative-only visual brief and rendered-image boundaries;
- scope boundaries for scraping, reviews, ordering, reservations, payment, restaurant contact, unsupported nutrition analysis, and generated imagery;
- final consistency check across recommendations, evidence labels, prices, constraints, allergy boundaries, staff questions, and visual brief.

## README Synchronization

README now includes:

- `restaurant-menu-advisor` in the skills table;
- `/restaurant-menu-advisor` in the Claude Code installed-command list;
- `/Skillsmith:restaurant-menu-advisor` in one-session command examples;
- a usage example;
- a skill-detail section.

## Unaffected Surfaces

- `tests/evals/skills/restaurant-menu-advisor/cases.yaml`: unchanged from M1 because the prompt aligns with the approved scenario expectations.
- `install.sh`, `tests/validate_skills.py`, CI, architecture, scripts, dependencies, secrets, generated images, and provider-specific API instructions: unaffected by M2.
- `docs/changes/2026-06-21-add-restaurant-menu-advisor/post-change-evidence.md`: intentionally deferred to M3 manual smoke evidence.

## Validation Evidence

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

## Readiness

M2 implementation is ready for plan metadata update to `review-requested` and code review.
