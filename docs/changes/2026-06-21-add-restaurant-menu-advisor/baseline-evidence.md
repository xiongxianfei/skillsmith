# Baseline Evidence: Restaurant Menu Advisor M1

## Scope

Milestone M1 adds reviewer-visible eval evidence before implementing the production prompt. It does not add `skills/restaurant-menu-advisor/SKILL.md`, README entries, manual smoke evidence, or post-change prompt behavior.

## Baseline State

- `skills/restaurant-menu-advisor/SKILL.md` is absent before M2 prompt implementation.
- `tests/evals/skills/restaurant-menu-advisor/cases.yaml` now exists as the M1 proof surface.
- The fixture uses fictional menus and sanitized allergy or emergency scenarios.

## Eval Fixture Coverage

The fixture includes:

- `normal`: complete menu, budget, taste preference, and no-seafood constraint.
- `indirect-trigger`: casual "Which of these should I get tonight?" menu-photo situation with missing constraints.
- `failure`: blurry or partial menu evidence with no invention of details.
- `safety`: severe peanut allergy plus vegetarian preference, with staff-confirmation and cross-contact boundaries.
- `misuse`: exact restaurant photo or replica request, with illustrative-only image boundary.
- `active-medical-emergency`: throat tightness and lip swelling after eating, routed away from menu selection.
- `edge`: fewer than three supported items, with no padded shortlist.

The fixture records `high_risk: true` and reviewer-visible `safety_notes` because allergy-related false reassurance can cause harm.

## Validation Evidence

Direct eval fixture validation was run because the full skill validator only associates eval fixtures with existing skill directories, and the M1 baseline intentionally keeps `skills/restaurant-menu-advisor/SKILL.md` absent until M2.

```bash
python -c 'from pathlib import Path; from tests.validate_skills import validate_cases_file; result = validate_cases_file("restaurant-menu-advisor", Path("tests/evals/skills/restaurant-menu-advisor/cases.yaml")); assert not result.errors, result.errors; print("direct eval fixture validation passed")'
```

Result: passed.

```bash
test ! -e skills/restaurant-menu-advisor/SKILL.md && echo 'skills/restaurant-menu-advisor/SKILL.md absent before M2'
```

Result: passed.

## Aligned Surfaces

- `skills/restaurant-menu-advisor/SKILL.md`: intentionally absent until M2.
- `README.md`: intentionally unchanged until M2, when the skill directory exists.
- `docs/changes/2026-06-21-add-restaurant-menu-advisor/post-change-evidence.md`: intentionally absent until M3 manual smoke evidence.
- `install.sh`, `tests/validate_skills.py`, CI, architecture, scripts, dependencies, secrets, generated images, and provider-specific API instructions: unaffected by M1.

## Readiness

M1 proof is ready for milestone validation and code review after the plan and change metadata are updated to `review-requested`.
