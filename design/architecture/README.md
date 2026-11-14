# Architecture design

`design/architecture/` is Skillsmith's only design directory. Use the `c4-architecture` skill to maintain architecture here. Each subject's `architecture-spec.md` holds its goals, required behavior, constraints, decisions, scenarios and open questions alongside the C4 model and views.

| Subject | Start here | Coverage |
| --- | --- | --- |
| Shared skill architecture | [Shared skill architecture](portable-skills.md) | Prompt distribution, validation, review and ownership boundaries |
| City experience Research → Plan workflow | [C4 design](city-experience-workflow/architecture-spec.md) | Three-skill responsibilities, location contracts and itinerary render artifacts; pending human review |
| Editor | [C4 design](editor-c4/README.md) | Context, container, editing/learning and boundary scenarios; implementation-derived specification |
| Vocabulary mastery | [C4 design](vocabulary-mastery-c4/README.md) | Context, container, bilingual reference and boundary scenarios; implementation-derived specification |

These designs are prepared for human review; their existence does not establish approval or successful model evaluation. For skills without C4 coverage, inspect their prompts and relevant evidence before adding design.

## Maintaining a design

- Keep requirements and observable acceptance examples in the relevant `architecture-spec.md`; distinguish current implementation, proposed changes and unknowns.
- Define stable entities and relationships in `model.d2`. Context and container views import that model; dynamic views reuse its participants.
- Keep D2 sources under `views/` and generated SVGs under `diagrams/`. Use the package's `scripts/architecture.py` to format, check and render changed diagrams, then inspect them visually.
- Add a decision record only when a consequential tradeoff needs explanation. Human review establishes acceptance; passing diagram checks does not.

See the [repository instructions](../../AGENTS.md) for validation and PR requirements.
