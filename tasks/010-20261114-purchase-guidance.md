# Align purchase-comparison with its decision-framework-first design

## Background
Make a personalized decision framework the primary outcome: identify the purchase category, brainstorm attributes with recommended weights, explore options with recommended scores, and let the user adjust them. Comparing named products becomes optional. The user has explicitly chosen recommendations for **both attribute weights and option scores**.

## Input
- [Proposed purchase architecture](../design/purchase-comparison/02-layered-components.md) and [purchase design entrypoint](../design/purchase-comparison/README.md): proposed behavior and design status to reconcile.
- [Purchase skill](../skills/purchase-comparison/SKILL.md): existing workflow, evidence rules, scoring mathematics and spreadsheet contract.
- Category references: [keyboard](../skills/purchase-comparison/references/keyboard.md), [mouse](../skills/purchase-comparison/references/mouse.md) and [mousepad](../skills/purchase-comparison/references/mousepad.md).
- [README](../README.md), [design guide](../design/README.md) and [repository rules](../AGENTS.md): catalog, ownership and contribution conventions.

## Output
- Modify `skills/purchase-comparison/SKILL.md` to implement the proposed workflow and update its discovery description.
- Modify the introductions in `skills/purchase-comparison/references/keyboard.md`, `mouse.md` and `mousepad.md` to support contextual suggestions without embedding universal preference defaults.
- Modify `design/purchase-comparison/README.md` and `design/purchase-comparison/02-layered-components.md` to match the resulting instructions and record the resolved option-score decision.
- Modify purchase descriptions in `README.md` and `design/README.md`.

The primary response provides an attribute table with importance weights, reasons and assumptions; an options table with suitability scores, trade-offs and reasons; and a clear opportunity to adjust the recommendations.

Acceptance examples:
- A keyboard-category request produces useful attributes, suggested weights and option scores without requiring candidate models.
- Existing user scores override suggestions.
- Different stated uses produce appropriately different recommendations and explanations.
- Optional comparison preserves unknown specifications, missing-preference warnings and `X` rejection.
- No available spreadsheet capability or tracker produces no claim of file generation or updates.

## Rules
- Distinguish **attribute importance** from **option suitability**.
- Label recommendations as suggestions; preserve user-provided values and distinguish adopted preferences from suggestions.
- Default suggested weights to 1–5 and option scores to 0–5. These are presentation defaults, not restrictions on existing user values.
- Preserve evidence requirements, unknown-value handling, rejection rules and conditional spreadsheet/tracker capabilities.
- Retain existing scoring mathematics. Document unresolved normalization cases, including negative weights, scores outside 0–5 and a zero denominator, without inventing a replacement.
- Keep the skill name `purchase-comparison` and preserve unrelated changes. Follow the linked repository rules for authoring and delivery.

## Approach
Before substantive implementation, record the intended behavior and acceptance examples in the issue or PR, following repository rules.

1. Resolve category and relevant context, reusing known information and stating assumptions.
2. Brainstorm attributes and recommend weights with reasons.
3. Explore options and recommend scores with reasons.
4. Help the user personalize the framework; finish successfully without requiring product models.
5. Research and rank candidates only when requested, using user-provided or adopted preferences.

Review representative outputs against the acceptance examples. Run `python tests/validate_skills.py` and skill-creator's validator for the changed skill; check affected links and whitespace. Record behavioral review separately from metadata validation, including any skipped checks and remaining limitations.

## Progress checklist
- [ ] Record intended behavior and acceptance examples in the issue or PR.
- [ ] Update instructions, references, design status and catalog descriptions.
- [ ] Review representative outputs against the acceptance examples.
- [ ] Run metadata and skill-creator validation; check affected links and whitespace.
- [ ] Record actual results and remaining limitations.

## Execution result
Pending execution and verification.
