# Skill designs

Designs explain mechanisms, dependencies, decisions and trade-offs that are difficult to understand from operational instructions alone. Start with the subject relevant to the change. The [glossary](glossary.md) defines DDD terminology and context-scoped editor terms:

| Subject | Focus |
| --- | --- |
| [Editor](editor/README.md) | Request interpretation, language decisions, editing and grounded teaching |
| [Vocabulary mastery](vocabulary-mastery/README.md) | Shared lexical information, resource loading and bilingual consistency |
| [City experience workflow](city-experience-workflow/README.md) | Research handoffs, selection, location evidence and derived materials |
| [Email writer](email-writer/README.md) | Goal-based drafting, factual checks and output preferences |
| [Purchase comparison](purchase-comparison/README.md) | Personalized decision frameworks, suggested weights and scores, and optional evidence-based comparison |

## Maintaining designs

Use `design/<subject>/README.md` as the entrypoint. Choose explanations, decision tables, worked cases and inline Mermaid diagrams according to what helps readers understand the subject; no fixed set of views is required. Add supporting files only when they improve navigation. Optional numbered topic pages, such as `02-layered-components.md`, can provide a reading order while the subject README remains the entrypoint.

Keep operational instructions and schemas in their owning skill resources and link to them. Preserve consequential rationale and relevant constraints. Distinguish current instructions, proposed changes, illustrative expectations and actual observed results. Record consequential policy changes explicitly; implementation-derived descriptions do not silently override accepted decisions.

Use Mermaid for repository design diagrams and inspect their rendered meaning and legibility when tooling is available. Diagram validity does not establish behavioral correctness. Repository contribution and validation rules remain in [AGENTS.md](../AGENTS.md). The public C4 skill remains available for work that specifically calls for C4/D2 designs.

## Architecture Overview format

Use the [architecture-overview skill](../skills/architecture-overview/SKILL.md) as the canonical reusable method and output contract. It defines the Mermaid graph, layer table and contexts–components table, including status, boundary and consistency checks. The [purchase comparison overview](purchase-comparison/02-layered-components.md) is a worked example.

Keep repository documentation under `design/<subject>/`, with `README.md` as the entrypoint and optional numbered topic pages for navigation. Existing filenames and owning artifacts take precedence. Other design views remain optional; adopting the skill does not require migrating existing subjects. Operational behavior remains in the owning skill resources, and contribution and validation rules remain in [AGENTS.md](../AGENTS.md).
