# Restaurant menu advisor system behavior

## Capability

F-MENU-001 — Choose from supplied menu evidence. A diner receives supported choices, a leading recommendation and an illustrative visual brief, with explicit uncertainty and allergy boundaries. The [requirements](../requirements/restaurant-menu-advisor.md) own all obligations and output dimensions.

| Function | Inputs, logical behavior and result | Failure and exclusions | Requirement basis |
| --- | --- | --- | --- |
| FN-MENU-001 — Establish menu evidence and constraints | Read supplied menu evidence and relevant preferences, restrictions and allergy information; ask bounded clarification only when it affects the choice | Missing/unreadable evidence requests clarification rather than imagined dishes; active emergency stops menu advice | R5–R8, R20–R26; error/boundary behavior |
| FN-MENU-002 — Compare supported choices | Rank differentiated supported items, select one leading recommendation, explain fit/tradeoffs/confidence and unresolved questions | Return fewer choices when fewer are supported; no allergen-safety or unsupported nutrition guarantees | R9–R12, R20–R24 |
| FN-MENU-003 — Describe and check the recommendation | Create a qualified visual brief, optionally request an illustrative image only on explicit request and capable host; check consistency against the menu and constraints | Text-only hosts still produce a complete response; imagery is never factual evidence or an exact restaurant photograph | R13–R19, R27 |

All three Functions realize F-MENU-001. [Portable skill architecture](../architecture/portable-skills.md) allocates their implementation. The process holds only conversational evidence; it does not create orders, reservations, payment state, retained profiles or restaurant API calls.

## Test intent

Exercise normal/indirect menu requests, partial menu evidence, missing prices, fewer than three supported items, explicit image requests, exact-photo misuse, allergy uncertainty and active medical-emergency escalation. Assess the same output for internal consistency and distinguish factual menu content from inference. Existing eval fixtures and preserved change-specific test plans supply examples; no new model execution is claimed by this migration.
