# Add task filename recommendations and remove workflow documentation

## Background
Recommend compact, consistent task filenames and simplify repository contribution guidance. Start from latest main while preserving unrelated local edits.

## Input
- [skills/task-writer/SKILL.md](../skills/task-writer/SKILL.md) and the installed copy at `~/.codex/skills/task-writer/SKILL.md`: naming behavior.
- [AGENTS.md](../AGENTS.md), [README.md](../README.md), and [architecture index](../design/architecture/README.md): remaining guidance and references.
- `docs/workflows.md`: contribution document to retire.

## Output
- Modify both task-writer copies to recommend `tasks/NNN-YYYYMMDD-short-name.md` when no existing convention applies.
- Delete `docs/workflows.md`; modify `AGENTS.md`, `README.md`, `design/architecture/README.md`, `design/architecture/portable-skills.md`, and `design/architecture/vocabulary-mastery-c4/architecture-spec.md` to retain essential instructions and repair references.
- Create this task record. Preserve existing task filenames, tests, CI, and skill designs.

## Rules
Follow [AGENTS.md](../AGENTS.md), with the user's explicit decision retiring the separate workflow guide. Keep drafting separate from saving; preserve unrelated edits and installed-skill differences. No new tooling or replacement workflow document.

## Approach
Fetch latest main and use an isolated branch. Add a small naming section, remove the workflow guide, and retain essential contribution rules in AGENTS.md. Validate metadata, local links and representative naming decisions before updating the installed skill and opening a PR.

Acceptance examples: no numbered tasks gives 001; a highest number of 009 gives 010 even on another date; existing conventions take precedence; editing a task preserves its name; drafting alone creates no file. Dates represent creation, not deadlines; numbering never resets by date.

## Progress checklist
- [x] Sync and create an isolated branch.
- [x] Update repository and installed skill guidance.
- [x] Remove workflow documentation and repair references.
- [x] Verify metadata, naming scenarios, links and diff.
- [ ] Deliver through a PR and record results.

## Execution result
Implemented on `improve/task-naming-and-workflow-cleanup` in the isolated `../skillsmith-task-cleanup` worktree, based on refreshed main at `c8b73b7`. Original workspace edits and the earlier unnumbered task remain untouched. Both task-writer copies now match.

Validation:
- `python tests/validate_skills.py`: all 27 skills passed.
- Skill-creator `quick_validate.py` against repository and installed task-writer: both passed.
- Checked 75 local Markdown link targets: all resolved.
- No active guidance references to the deleted workflow guide remain; this task retains its deletion path as a record.
- `git diff --check`: passed.
- Author review of the five acceptance scenarios found the intended naming and save boundaries explicit. This is design review, not observed model behavior.

No warnings or failures were observed. Functional suites, diagram rendering and live-model evaluation were skipped because executable code and diagrams were unchanged and this is a small instruction edit. PR delivery is pending; independent review and merge are not claimed.
