# Reorganize README to help users find and use the right skill

## Background

Make Skillsmith easier to browse by grouping skills around user goals, explaining overlapping choices, and providing practical examples. Keep implementation confined to the README; save this task record separately at the user's request.

## Input

- [README.md](../README.md): catalog, usage examples, installation instructions and migration notes.
- [skills/](../skills/): owning skill instructions for verifying descriptions and examples.
- [AGENTS.md](../AGENTS.md): contribution and validation rules.

## Output

Modify `README.md` to include:

- A catalog grouped into writing and communication; learning and practice; travel and local discovery; shopping and personal style; health and reflection.
- A work and development group, with one primary entry per skill across all six groups, retaining its link, command and concise purpose.
- A short selection guide comparing `email-writer`, `editor` and `communicator`; `flashcard-generator` and `quiz-generator`; and `travel-planner`, `city-attraction-research` and `city-itinerary-builder`.
- Three copyable request examples for writing, learning and travel, each with an expected-result description.

Acceptance: readers can identify a relevant skill, distinguish nearby alternatives and understand what input to provide. Catalog links resolve and descriptions agree with skill instructions.

## Rules

Follow [AGENTS.md](../AGENTS.md). Preserve existing user changes, installation guidance, migration notes, useful specialized usage details, contribution information and license information. Do not rename skills, move directories, change skill behavior, or add tooling or architecture documents. Examples describe expected behavior and must not imply successful model testing.

## Approach

Start from latest `main` in an isolated branch and account for existing README edits without overwriting them. Review skill descriptions, group the catalog, and consolidate selection guidance and examples. Check catalog coverage, local links, Markdown readability and example accuracy. Run `python tests/validate_skills.py` and `git diff --check`; report pre-existing failures separately. Functional suites and model evaluations are unnecessary for this documentation-only change.

## Progress checklist

- [x] Review skill coverage and preserve relevant existing README content.
- [x] Group the catalog and add skill-selection guidance.
- [x] Add or reuse three practical request examples with expected results.
- [x] Verify links, coverage, accuracy, metadata and the scoped implementation diff.

## Execution result

Implemented in [README.md](../../20260525-skillsmith-readme-navigation/README.md) on branch `docs/readme-navigation`, in the isolated sibling worktree `../20260525-skillsmith-readme-navigation`, based on refreshed `main` at `c75eb98`. The original checkout was left untouched during implementation. Its pre-existing README changes matched latest main after newline normalization; unrelated changes, including a deleted skill file, were preserved in that checkout.

All 29 skills have one catalog entry across six groups. Added the selection guide and three request examples, reused the flashcard example, and retained specialized learning examples and skill details. Installation, migration, contribution and license information remain intact.

Validation performed in the isolated worktree:

- `python tests/validate_skills.py`: all 29 skills passed metadata checks.
- Ad hoc catalog and link checks: 29 unique entries with matching commands, three-column catalog rows, and 41 resolving local links or anchors.
- Preservation checks: installation and migration text retained; content from Other models through License unchanged.
- `git diff --check`: passed.
- Implementation scope check: only `README.md` modified before this task record was saved.

Descriptions and examples were reviewed against skill instructions. No validation failures remained. Functional suites and model evaluations were skipped because this is documentation-only; metadata validation does not demonstrate model quality or host compatibility. Changes remain uncommitted, with no push or PR created. This task record is saved in the original checkout at the user's subsequent request.
