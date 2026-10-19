# Architecture design

`design/architecture/` is Skillsmith's only design directory. Use the `c4-architecture` skill to maintain architecture here. Each subject's `architecture-spec.md` holds its goals, required behavior, constraints, decisions, scenarios and open questions alongside the C4 model and views. Separate requirement and system-design directories are no longer used.

| Subject | Start here | Coverage |
| --- | --- | --- |
| Shared platform and portable skills | [Portable skill architecture](portable-skills.md) | Prompt distribution, validation, review and ownership boundaries |
| City experience Research → Plan workflow | [C4 design](city-experience-workflow/architecture-spec.md) | Three-skill responsibilities, location contracts and itinerary render artifacts; pending human review |
| Editor | [C4 design](editor-c4/README.md) | Context, container, editing/learning and boundary scenarios; implementation-derived specification |
| Vocabulary mastery | [C4 design](vocabulary-mastery-c4/README.md) | Context, container, bilingual reference and boundary scenarios; implementation-derived specification |

The two C4 packages are prepared for human review; their existence does not establish approval or successful model evaluation. Other catalog skills do not yet have C4 packages. Consult their prompts and relevant historical examples before proposing changes, and add design only when needed.

## Maintaining a design

- Keep requirements and observable acceptance examples in the relevant `architecture-spec.md`; distinguish current implementation, proposed changes and unknowns.
- Define stable entities and relationships in `model.d2`. Context and container views import that model; dynamic views reuse its participants.
- Keep D2 sources under `views/` and generated SVGs under `diagrams/`. Use the package's `scripts/architecture.py` to format, check and render changed diagrams, then inspect them visually.
- Add a decision record only when a consequential tradeoff needs explanation. Human review establishes acceptance; passing diagram checks does not.

The [quality standard](../../docs/skill-quality-standard.md) governs skill authoring and evidence. The [workflow guide](../../docs/workflows.md) explains the small design, implementation, validation and PR cycle.

## Historical sources

The retired [requirements](https://github.com/xiongxianfei/skillsmith/tree/93c9bf750ceea7585c06fd93fcceecac5f7e8d26/design/requirements) and [system designs](https://github.com/xiongxianfei/skillsmith/tree/93c9bf750ceea7585c06fd93fcceecac5f7e8d26/design/system) remain available at a fixed Git revision, including editor, restaurant-menu, flashcard and quiz contracts and their provenance. Their removal from the working layout does not change product behavior or erase previously documented constraints. Consult these sources when extending coverage; record the resulting decisions in the current C4 specification rather than restoring a parallel hierarchy.

RigorLoop adoption documents and reviews are historical. RigorLoop is no longer part of the active workflow. No earlier approval is transferred to these C4 designs.

Earlier [proposals](https://github.com/xiongxianfei/skillsmith/tree/00224740db8a8e18e10579d8b38377ef0c1b04cf/docs/proposals) and [delivery plans](https://github.com/xiongxianfei/skillsmith/tree/00224740db8a8e18e10579d8b38377ef0c1b04cf/docs/plans), including their decision logs, evidence notes and limitations, are preserved at this fixed revision. The old [plan index](https://github.com/xiongxianfei/skillsmith/blob/00224740db8a8e18e10579d8b38377ef0c1b04cf/docs/plan.md) and [archive index](https://github.com/xiongxianfei/skillsmith/blob/00224740db8a8e18e10579d8b38377ef0c1b04cf/docs/plan-archive.md) are historical snapshots, not current work queues. Their working-tree directories and indexes have been removed. Current design belongs in the subject specification; task sequencing belongs in the issue, PR or a local working note. Useful shared decision rationale is retained in [portable skill architecture](portable-skills.md#retained-design-rationale).

Retired [change evidence](https://github.com/xiongxianfei/skillsmith/tree/1d6ce5bee418b59fcfdd4a8cc98304a491e3e49a/docs/changes) is preserved at a fixed Git revision, including original review findings, baseline/post-change evidence and later editor/vocabulary requirement drafts. The working-tree records have been removed; local-only evidence was backed up outside the repository. Historical assessments retain their original scope and do not establish current approval or model quality.
