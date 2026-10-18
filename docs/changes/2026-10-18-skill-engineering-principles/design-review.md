# Applied design review: skill engineering principles and vocabulary-mastery

**Change:** reviewer-visible architecture/plan evidence for the project-wide principles and the material prompt refinement. This document is not a model evaluation report.

## Why this fits Skillsmith

- The library stays a set of independent portable Markdown skills. No executable skill framework, inheritance, shared runtime loader, hidden tool permissions, external API, installer change, or new CI dependency is introduced.
- The new `docs/architecture/skill-design-principles.md` complements the Constitution and the approved Skill Quality Standard. Its nine principles are reviewer heuristics, not a second canonical policy or a brittle new CI gate.
- The added principles are reachable from the Constitution, quality spec/test-spec, contributor/agent instructions, README, and PR review template. Only the *vocabulary-mastery* skill is changed.

## Evidence of applying principles

| Principle | Before | After or decision |
| --- | --- | --- |
| P1: One job | Vocabulary profile already one standalone task | Retain one-English-item scope; keep editor/tutor/flashcard boundaries |
| P2: Contract | Two full standalone outputs and ten sections defined | Preserve exactly; do not change headings, order, bilingual parity or number of retrieval prompts |
| P3: Simple path | Workflow made sense map, then drafted two parts | One explicit **canonical evidence plan** precedes English/Chinese renders and verification |
| P4: Proportionate DRY | Similar factual requirements repeated in instructions/templates | Resolve senses, IPA, limits, original English samples, and three recall answers **once**; duplicate visible ten-domain templates intentionally so both outputs stay independent |
| P5: Explicit composition | Neighboring skills named | Clarify that mentioning another skill is routing guidance, not automatic invocation, shared state, or dependency |
| P6: Evidence integrity | No fabricated IPA/etymology/audio already required | When evidence is missing, qualify the limitation in **both** versions even if an Example slot cannot be filled |
| P7: Stable interfaces | Published name, trigger, English-only source, two-part format | No rename/installer/default output changes; no migration needed |
| P8: Layered proof | Five vocabulary structural tests and 16 static eval scenarios | Add two focused structural contract tests and two behavioural expectations for cross-language consistency and weak-evidence parity |
| P9: Ownership | Scope and quality rules spread across docs | Keep prompt in `SKILL.md`, tests/evals under `tests/`, principles under `docs/architecture/` with Constitution/spec pointers |

## Reviewer-visible example

**Input**

```text
/vocabulary-mastery record
Context: We recorded the interview. The recording is stored in our archive.
```

**Expected observations, not a claimed live-model result:**

- Part 1: complete English word overview, all ten dimensions, knowledge links, three recall prompts and aligned answers.
- Part 2: independently readable Chinese overview, ten dimensions, links and the **same** retrieval tasks and answers.
- Both explain the selected verbal `recorded` and nominal `recording` senses using the **same original English examples**, labelled pronunciation claims and faithful Chinese interpretation. Neither invents a recording's sound from written text or switches silently to the unrelated achievement sense.
- For `apple`, any lack of a special word-specific prosody or pragmatics property is disclosed in both versions without manufacturing a feature.

## Verification plan and limitations

Run `python -m unittest discover tests`, `python tests/validate_skills.py`, and `python tests/check_readme_sync.py`. The connected container cannot resolve github.com for a full local checkout, so use the repository's GitHub Actions workflow on the PR and record its result honestly. Structural tests demonstrate source constraints; **static evals are expectations and do not establish live-model correctness**.

**Tradeoffs:** A two-version, ten-domain reference is verbose by user choice, and the visible format is intentionally duplicated. The one-analysis/two-rendering rule reduces factual drift without removing either standalone version. Reviewers should require a real behaviour regression before further cosmetic prompt rewriting.
