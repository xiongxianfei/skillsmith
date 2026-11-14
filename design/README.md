# Skill designs

Designs explain mechanisms, dependencies, decisions and trade-offs that are difficult to understand from operational instructions alone. Start with the subject relevant to the change:

| Subject | Focus |
| --- | --- |
| [Editor](editor/README.md) | Request interpretation, language decisions, editing and grounded teaching |
| [Vocabulary mastery](vocabulary-mastery/README.md) | Shared lexical information, resource loading and bilingual consistency |
| [City experience workflow](city-experience-workflow/README.md) | Research handoffs, selection, location evidence and derived materials |

## Maintaining designs

Use `design/<subject>/README.md` as the entrypoint. Choose explanations, decision tables, worked cases and inline Mermaid diagrams according to what helps readers understand the subject; no fixed set of views is required. Add supporting files only when they improve navigation.

Keep operational instructions and schemas in their owning skill resources and link to them. Preserve consequential rationale and relevant constraints. Distinguish current instructions, proposed changes, illustrative expectations and actual observed results. Record consequential policy changes explicitly; implementation-derived descriptions do not silently override accepted decisions.

Use Mermaid for repository design diagrams and inspect their rendered meaning and legibility when tooling is available. Diagram validity does not establish behavioral correctness. Repository contribution and validation rules remain in [AGENTS.md](../AGENTS.md). The public C4 skill remains available for work that specifically calls for C4/D2 designs.
