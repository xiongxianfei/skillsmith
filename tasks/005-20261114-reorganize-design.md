# Simplify and reorganize skill design documentation

## Background
Explain how complex skills work and why consequential mechanisms exist, while removing repetitive architecture framing. Sequence diagrams are useful, but no universal sequence-centered format is required.

## Input
- [Repository instructions](../AGENTS.md): ownership and validation.
- Existing editor, vocabulary mastery and city experience designs and their skill instructions.
- Confirmed choices: delete portable-skills.md, use design/<subject>/ and inline Mermaid.

## Output
Delete the shared architecture document; move the three subjects to design/editor/, design/vocabulary-mastery/ and design/city-experience-workflow/. Create design/README.md and a README.md per subject. Retain useful mechanisms, decisions, contracts and examples, convert useful diagrams to Mermaid, remove obsolete D2/SVG/helper artifacts and repair references.

Acceptance: accurate, discoverable designs with no migration-induced broken links; skill behavior and relevant constraints preserved.

## Rules
Follow AGENTS.md. Preserve runtime skill behavior and tests. Keep the public C4 skill's general capabilities intact. Distinguish intended behavior, proposals and actual evidence. Do not duplicate generic host/governance descriptions.

## Approach
Use one README per subject, selecting explanatory material according to the skill's complexity. Verify metadata, local links, diagrams where tooling permits, and whitespace. No runtime changes are intended.

## Progress checklist
- [x] Select content and migrate subjects.
- [x] Convert diagrams and remove obsolete artifacts.
- [x] Repair guidance and references.
- [x] Validate and record results.

## Execution result
Implemented locally on `improve/reorganize-design`, based on fetched `origin/main` (HEAD matched upstream before branching).

- Removed shared architecture and the old architecture tree; migrated three subjects to linked README files under `design/`.
- Preserved useful behavior, decisions, contracts, boundaries and open questions; converted six scenario sequences and added a city workflow diagram as inline Mermaid.
- Removed obsolete subject D2/SVG assets and rendering helpers. Updated navigation and repository-specific C4 guidance; retained historical task descriptions while repairing their navigation links.
- `python tests/validate_skills.py`: all 28 skills passed.
- `git diff --check`: passed.
- Local-link inspection: 50 targets checked; 49 exist. The README link to missing `skills/brainstorm/SKILL.md` is pre-existing (confirmed in HEAD), unrelated to this migration, and remains unresolved.
- Mermaid rendering/visual inspection skipped: `mmdc` is not installed. Diagram text was inspected; rendering success is not claimed.
- Functional and live-model tests skipped because runtime behavior is unchanged.

At the initial implementation handoff, changes were local and uncommitted. The user subsequently requested a PR to `main`. Diagram rendering remains a verification limitation; no merge or independent approval is claimed.
