# Create the general-purpose architecture-overview skill

## Background
Capture the architecture design approach developed here as a reusable skill for software, AI skills and other structured projects. Help readers understand meaningful responsibilities and relationships without forcing generic layers.

## Input
- [Design guide](../design/README.md): established output format and repository conventions.
- Worked architecture example: [purchase](../design/purchase-comparison/02-layered-components.md). Supporting source material: [editor design](../design/editor/README.md) and [email instructions](../skills/email-writer/SKILL.md). Local editor and email overview drafts also informed the layout; their separate publication is outside this task.
- [C4 architecture skill](../skills/c4-architecture/SKILL.md): existing capability boundary.
- [README](../README.md) and [repository rules](../AGENTS.md): catalog, usage, ownership and contribution conventions.
- [OpenAI skill guidance](https://learn.chatgpt.com/docs/build-skills) and [Anthropic authoring guidance](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices): authoring references; apply host-specific guidance to the intended host.

## Output
- Create `skills/architecture-overview/SKILL.md` (planned) as a self-contained skill.
- Modify `README.md` to add its catalog entry and invocation example.
- Modify `design/README.md` to link the skill as the reusable method while retaining repository-specific locations and ownership rules.

Default deliverable, in order:
1. **One Mermaid architecture graph.**
2. **One layer table:** `# | Layer | Responsibility | Components`.
3. **One contexts–components table:** `Context | Component | Layer | Responsibility`.

Allow brief assumptions, boundaries, rationale and source links. Match component names and numbered groups across the graph and tables; add context to the layer table when multiple contexts require disambiguation.

Acceptance examples:
- Purchase guidance distinguishes the primary decision framework from optional candidate comparison.
- A non-skill CSV inventory project explains import, validation, reorder calculation and export without inventing network services.
- Sparse requirements lead to marked assumptions and candidate boundaries, not claims of implementation.
- Existing architecture files are updated through their owning artifact without creating a competing design tree.

## Rules
- Support existing implementations and proposed designs; clearly distinguish their status.
- Identify contexts from coherent models and rules. Do not invent additional contexts to populate a diagram.
- Use meaningful numbered responsibility groups; do not force four layers or generic intake/workflow/output boxes.
- Distinguish capability groups, execution stages and technical layers accurately.
- Use short component names, `and` instead of `&`, and concise relationship labels. Explain arrow semantics and keep them consistent.
- Separate supporting resources and conditional external capabilities from core responsibilities.
- Preserve repository conventions and existing files. Architecture work does not automatically authorize behavior changes.
- Keep formal C4/D2 work within the existing `c4-architecture` capability.
- Keep the reusable method and output contract canonical in the new skill. Use a single concise `SKILL.md`; add no scripts or template package for this initial version.
- For new documentation, follow the project's established location; absent a convention, use `design/<subject>/README.md`. Preserve explicit chat-only requests.

## Approach
Record intended behavior and acceptance examples in the issue or PR before substantive implementation, following repository rules. Use skill-creator when authoring the new skill.

Inspect the intended outcome, requirements and available implementation. Identify the smallest useful set of contexts, responsibilities and relationships, then produce matching graph and tables. Exercise the skill and non-skill acceptance examples, distinguishing illustrative review from observed model results.

Render generated diagrams when tooling is available and inspect labels, boundaries and connections. Check graph/table consistency, affected links and whitespace. Run `python tests/validate_skills.py` and skill-creator's validator for both `architecture-overview` and `purchase-comparison` (coordinate with task 010). Report behavioral review separately from metadata results and record any skipped rendering or validation.

## Progress checklist
- [x] Record intended behavior and acceptance examples in the issue or PR.
- [x] Write the skill with clear discovery scope and output contract.
- [x] Update catalog, usage and design-guide references.
- [x] Exercise skill and non-skill examples; inspect rendered diagrams when tooling is available.
- [x] Check graph/table consistency, metadata, links and whitespace.
- [x] Record actual results and skipped checks.

## Execution result
Created the self-contained [architecture-overview skill](../skills/architecture-overview/SKILL.md), added its README catalog entry and invocation, and made the [design guide](../design/README.md#architecture-overview-format) refer to the skill as the canonical reusable method. Repository paths and ownership rules remain in the guide. No scripts or template package were added.

- `python tests/validate_skills.py`: all 29 skills passed metadata checks.
- Skill-creator `scripts/quick_validate.py` passed for both `skills/architecture-overview` and `skills/purchase-comparison`.
- [Author-produced walkthroughs](reviews/010-011-behavioral-review.md) cover purchase, local CSV inventory, sparse requirements and existing artifacts. Graph/table checks passed for seven purchase components in two groups and four inventory components in three groups.
- Mermaid CLI 12.2.0 rendered both graphs to temporary PNGs using the available Chromium configuration. Visually inspected labels, boundaries and connections: all were legible; optional purchase comparison and external capabilities remained distinct. Initial rendering used obsolete `-w`; reran successfully with `--size 1800` after checking CLI help.
- Local links and whitespace checked. Source authoring guidance was consulted. Input links now point to published editor/email source artifacts rather than unrelated uncommitted overview drafts, which were consulted locally and preserved.
- Behavioral review is illustrative author work, not independent approval or cross-host evaluation. Metadata and rendering checks do not prove behavioral quality. Unrelated functional suites were skipped because no executable code changed.

Link-check limitation: the existing README link to removed `skills/brainstorm/SKILL.md` is already broken on `origin/main` and remains outside this change. All other checked local links and anchors passed (77 in the isolated PR tree).
