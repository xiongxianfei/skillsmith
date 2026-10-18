# Skill engineering principles and vocabulary-mastery refinement

## Status

Change requirements, 2026-10-18. Establish a reusable project-wide set of *applied design principles* subordinate to Skillsmith's Constitution and its existing approved Skill Quality Standard. Apply them to the merged `/vocabulary-mastery` skill. This work is proposed through a PR and becomes project guidance when reviewed and merged.

## Intent and architecture boundary

- Build on, **do not replace or duplicate**, `CONSTITUTION.md` and `specs/skill-quality-standard.md`.
- Add one applied engineering-principles document at `docs/architecture/skill-design-principles.md` with named principles, software analogies, actionable review questions, examples, and legitimate tradeoffs.
- Establish discoverability through a brief pointer from `CONSTITUTION.md`, the approved skill quality standard, `AGENTS.md`, `CONTRIBUTING.md`, the PR template, and the README contributing section. Do not make a second authoritative source of validation requirements.
- Favor **reviewer-observable heuristics** over brittle automated style gates; current objective validator and CI remain canonical and unchanged.
- Principles must address: (1) single mission/cohesion, (2) explicit input/output and failure contracts, (3) simple uniform workflows/KISS/YAGNI, (4) portable self-contained prompt behavior and proportionate DRY, (5) composability via skill boundaries without imaginary orchestration/inheritance, (6) truthfulness and evidence, (7) stable compatibility/versioning, (8) layered verification and falsifiability, and (9) maintainability and ownership.

## Requirements for the vocabulary-mastery improvement

- **Do not change the selected output contract**: one English word/fixed phrase in; **Part 1: full English reference**, **Part 2: full independent Simplified Chinese reference**; each contains a word overview, all ten dimensions in order, knowledge connections, exactly three recall prompts and answers, and matching accuracy notes when appropriate.
- The skill's entire `SKILL.md`, including the two output templates, remains **English-only**; the Chinese *runtime response* must be natural and independently readable, with matching original English example sentences and faithful Chinese translations.
- Preserve explicit skill routing boundaries: editor for polishing, language-tutor for interactive teaching, flashcard-generator for export and study cards.
- Refactor the behavioral workflow around **one canonical lexical analysis/evidence plan**, used to render and independently verify the two language versions. Do not pretend there is a runtime file, cache, hidden persistent profile, API, or guaranteed automated cross-skill invocation.
- Reduce redundant or ambiguous rules where safe, but allow duplicated *output templates* where needed to make both independently complete. Document the user-selected verbosity as a justified tradeoff rather than adding an unsolicited quick mode.
- Ensure source/evidence safeguards remain: IPA labelled with accent only when confident; text cannot substantiate a learner's actual speech; no invented morphology, etymology, idioms, prosody, corpus citations, frequency facts, or universal dialect judgments; weak dimensions explicitly state lack of a special phenomenon.
- Preserve sense/part-of-speech alignment and sample sentences between versions; the three recall prompts and answers must test the same underlying facts, not be rewritten into new tasks in Chinese.
- The change should stay prompt-only (no new skill, dependencies, tools, auto-generated assets, or changes to installation).

## Tests and review evidence

- Extend `tests/evals/skills/vocabulary-mastery/cases.yaml` with grounded cases for context selection, parity failures, weak dimensions, output completeness, and routing, without inventing model pass results.
- Refine `tests/test_vocabulary_mastery_contract.py` to assert only objective properties: English-only skill source, ordering, two complete templates, required domain mapping, and presence of a canonical-plan/verification instruction; avoid brittle checks that depend on inconsequential wording.
- Include reviewer-visible specific examples and before/after behavior in the PR (or change-local note).
- Attempt local `python -m unittest discover tests`, `python tests/validate_skills.py`, `python tests/check_readme_sync.py`; if checkout is blocked, verify via the existing GitHub Actions workflow and disclose this limitation.
- Inspect diff for scope, review warnings, and disclose absence of live model evaluation.

## Acceptance criteria

1. Project design principles are discoverable and non-conflicting with existing governance, with a practical review checklist.
2. The vocabulary skill has one coherent canonical analysis workflow, remains independently executable, and still promises two complete English/Chinese outputs in the user-selected fixed format.
3. Existing structural and integration tests pass; new targeted fixture expectations are reviewer-visible.
4. Existing skill contracts and installer/CI behavior stay unchanged.
