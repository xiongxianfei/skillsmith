# Proposal: Create `flashcard-generator` and `quiz-generator` skills

> Historical record: retired source paths and prior workflow judgments below identify the original change. See the [current design index](../../design/architecture/README.md) for effective owners; this migration does not renew this record’s approval or completion status.

## Status

accepted

## Problem

Skillsmith should support high-quality learning artifact generation, but flashcards and quizzes should not be collapsed into one broad study-artifact skill.

Flashcards and quizzes look similar on the surface, but they optimize for different learning jobs:

| Artifact | Primary job | Main risk |
|---|---|---|
| Flashcards | Durable recall and long-term retention | Cards become broad, vague, ungrounded, duplicated, or not worth remembering. |
| Quizzes | Diagnostic assessment and transfer | Questions become shallow, ambiguous, leading, misaligned, or poor at diagnosing misconceptions. |

The supplied design direction recommends two skills for a serious learning system: `flashcard-generator` for spaced-repetition-ready prompts and `quiz-generator` for diagnostic questions, rubrics, distractors, feedback, and adaptive follow-up. It also recommends a shared learning-design reference rather than a third skill, because the two workflows share theory but need different triggers, schemas, validators, and quality bars.

This aligns with current skill-authoring guidance. OpenAI describes skills as reusable workflows for recurring tasks and notes that skills often work best as smaller building blocks rather than one massive end-to-end skill. Anthropic's skill documentation says each skill requires a `SKILL.md` with `name` and `description`, and the description should explain both what the skill does and when to use it.

The proposal should therefore create two focused skills with a shared learning-design foundation:

```text
flashcard-generator
quiz-generator
```

The goal is not merely to generate cards and questions. The better workflow is:

```text
source material
-> learning objectives
-> knowledge map
-> artifact generation
-> quality validation
-> exportable output
```

The supplied design direction identifies this intermediate learning model as the difference between a demo and a real learning system.

## Goals

1. Create a new `flashcard-generator` skill for source-grounded, spaced-repetition-ready flashcards.
2. Create a new `quiz-generator` skill for source-grounded diagnostic quizzes, comprehension checks, MCQs, short-answer items, rubrics, feedback, and follow-up prompts.
3. Keep the skills separate so each has a clear trigger description, output contract, quality bar, and evaluation surface.
4. Share learning-design principles between the skills without creating a third runtime skill.
5. Have both skills extract learning objectives before generating artifacts.
6. Have both skills build or infer a compact knowledge map before artifact generation.
7. Use canonical JSON as the structured output source of truth, with Markdown for human review.
8. Support practical exports: flashcards as Markdown, JSON, CSV or TSV, and Anki-oriented output; quizzes as Markdown, JSON, answer keys, feedback or rationales, and LMS-oriented structures where requested.
9. Add eval fixtures for both skills before implementation is considered complete.
10. Keep the first slice prompt-centered and portable, with no direct AnkiConnect, LMS API, live model CI, or external service integration.

## Non-goals

1. Do not create one broad `study-artifact-generator` skill as the production design.
2. Do not create a third `learning-design` skill.
3. Do not build a full spaced-repetition scheduler.
4. Do not integrate directly with Anki, Moodle, H5P, QTI tools, or LMS APIs in the first slice.
5. Do not require live model calls in CI.
6. Do not generate ungrounded educational content when the user provides source material.
7. Do not produce medical, legal, financial, or high-stakes exam-prep guarantees without a later high-risk review path.
8. Do not add executable validators unless a later plan explicitly accepts that implementation cost.
9. Do not optimize existing Skillsmith skills outside the learning-artifact scope.

## Vision fit

fits the current vision

This proposal fits Skillsmith's direction toward focused, reusable, reviewable Markdown skills. It adds two practical learning skills while preserving skill boundaries, source grounding, eval-driven quality, and portable prompt-first behavior.

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
|---|---|---|
| Generate a proposal | in scope | Entire artifact |
| Create two skills | in scope | Goals, Recommended Direction |
| Follow best practices | in scope | Context, Testing and Verification Strategy |
| Use the supplied flashcard and quiz design direction | in scope | Problem, Context, Recommended Direction |
| Keep flashcards and quizzes distinct | in scope | Goals, Options Considered |
| Use shared learning-design guidance | in scope | Scope Budget, Recommended Direction |
| Avoid a weak generate-flashcards-and-quizzes demo | in scope | Problem, Recommended Direction, Testing and Verification Strategy |

## Scope budget

| Work item | Treatment | Reason |
|---|---|---|
| `skills/flashcard-generator/SKILL.md` | core to this proposal | One of the two requested skills. |
| `skills/quiz-generator/SKILL.md` | core to this proposal | One of the two requested skills. |
| Shared learning-design guidance | core to this proposal | Both skills need common principles for objectives, grounding, retrieval, feedback, and difficulty. |
| Local reference files under each skill | core to this proposal | Keeps each skill portable while sharing the same design content. |
| Flashcard schema reference | core to this proposal | The first slice should include a reference JSON Schema as the flashcard output contract, without executable validation. |
| Quiz item schema reference | core to this proposal | The first slice should include a reference JSON Schema as the quiz output contract, without executable validation. |
| Eval fixtures for both skills | core to this proposal | New skills need scenario evidence under the skill-quality standard. |
| Trigger evals | core to this proposal | Two nearby skills need clear activation boundaries. |
| Direct AnkiConnect integration | deferable follow-up | Useful later but adds tool and API complexity. |
| Full QTI, H5P, or Moodle export validation | deferable follow-up | Valuable but too broad for the first skill creation slice. |
| Executable validators | deferable follow-up | Start with prompt-level validation and evals; scripts can come later. |
| A third learning-design skill | out of scope | Shared theory is not itself a user-facing workflow. |
| Repository-wide validator changes | out of scope | This proposal should use the existing skill-quality path unless downstream requirements prove a gap. |

## Context

The supplied design direction recommends two production skills rather than one combined MVP skill. It says `flashcard-generator` should optimize for retention, spaced repetition, atomic prompts, export formats, and card-quality validation, while `quiz-generator` should optimize for diagnostic assessment, comprehension, transfer, rubrics, distractors, feedback, and adaptive follow-up.

The same direction explains why the split is practical: flashcards and quizzes have different primary purposes, question styles, learning-theory emphasis, output formats, quality risks, and validation checks.

For both skills, the proposed workflow should avoid generating artifacts directly from paragraphs. It should first infer learning objectives and a compact knowledge map, then generate artifacts and validate them for source grounding, answerability, alignment, difficulty, ambiguity, correctness, explanation quality, and redundancy.

OpenAI's current skills guidance says a typical `SKILL.md` defines what the skill does, required inputs, step-by-step instructions, required output format, and final checks. Anthropic's skill documentation says metadata is loaded at startup and the `SKILL.md` body is loaded when triggered, which supports concise descriptions and progressive disclosure for detailed reference content.

## Options Considered

### Option 1: One combined `study-artifact-generator` skill

This would be easiest to invoke:

```text
study-artifact-generator
Modes:
- flashcards
- quiz
- both
```

It is acceptable for an MVP, but it blurs quality standards and trigger behavior. Flashcard quality and quiz quality are different enough that a combined skill would either become too broad or under-specify one side.

Disposition: rejected for production.

### Option 2: Two skills with duplicated full theory

This keeps the skills independent but creates drift. If retrieval practice, source grounding, or objective extraction rules change, two large copies must be updated.

Disposition: rejected.

### Option 3: Two skills with compact local shared references

Create two distinct skills and give each a compact local learning-design reference derived from the same source. This keeps the skills self-contained while preserving a shared quality foundation.

Disposition: recommended.

### Option 4: Two skills plus a third `learning-design` skill

This is conceptually clean but operationally risky. The learning-design content is a reference, not a user-facing workflow. A third skill also depends on reliable skill composition, which should not be assumed.

Disposition: rejected for first slice.

### Option 5: Two skills plus executable validators and export scripts immediately

This would improve structural validation, but it expands scope into scripts, schema enforcement, export edge cases, and tool permissions.

Disposition: deferred follow-up.

## Recommended Direction

Adopt Option 3: two focused skills with compact local shared references.

Proposed repository shape:

```text
skills/
  flashcard-generator/
    SKILL.md
    references/
      learning-design.md
      card-quality.md
    schemas/
      flashcard.schema.json

  quiz-generator/
    SKILL.md
    references/
      learning-design.md
      question-quality.md
    schemas/
      quiz-item.schema.json

tests/
  evals/
    skills/
      flashcard-generator/
        cases.yaml
        trigger-cases.yaml
      quiz-generator/
        cases.yaml
        trigger-cases.yaml
```

The two `references/learning-design.md` files may initially contain the same concise content. If duplication becomes hard to maintain, a later proposal can introduce a repository-level shared source and a sync or check mechanism. The first slice should keep each skill package self-contained.

The schema files should be strict enough to document required fields and output shape, but they should be reference contracts only in the first slice. Executable schema validation should wait until the prompt outputs stabilize and the project accepts the added CI behavior.

### `flashcard-generator`

Purpose: create high-quality spaced-repetition flashcards from source material.

The skill should not merely summarize. It should decide what is worth remembering, what must first be understood, what the smallest testable unit is, what card type best fits the knowledge, what context is needed to avoid orphan facts, and what examples or contrasts prevent confusion.

Draft trigger description:

```yaml
description: >
  Use this skill when the user wants spaced-repetition flashcards, Anki cards,
  cloze deletions, memory prompts, durable recall practice, or retention cards
  from notes, documents, code, papers, courses, or project material. Generate
  source-grounded, atomic cards with tags, explanations, and exportable
  Markdown, JSON, CSV, or TSV.
```

Default assumptions:

| Field | Default |
|---|---|
| Audience | general professional learner |
| Goal | durable understanding and recall |
| Card count | 15-30 unless the user requests otherwise |
| Export | Markdown plus canonical JSON |
| Difficulty | mixed, weighted toward useful retrieval |
| Source grounding | required for factual cards |

Proposed workflow:

1. Identify the learner goal, audience, source material, desired count, and export format if provided.
2. Extract learning objectives.
3. Build a compact knowledge map covering facts, concepts, procedures, distinctions, examples, non-examples, common misconceptions, and prerequisites.
4. Select only knowledge worth retaining.
5. Generate candidate cards using appropriate card types: basic Q/A, cloze, bidirectional, contrast, example/non-example, procedure, and failure-mode.
6. Validate each card for one idea, source grounding, answerability, specificity, novelty, readiness for memorization, and usefulness.
7. Rewrite or drop failed cards.
8. Return final cards in the requested format.

Output contract:

1. brief deck summary;
2. learning objectives;
3. cards table for human review;
4. canonical JSON;
5. requested export format when requested.

Quality bar:

| Check | Rule |
|---|---|
| Atomicity | One card tests one idea. |
| Source grounding | Factual answers trace to source or are marked as inferred. |
| Answerability | The prompt makes the expected answer type clear. |
| Minimum information | Avoid broad prompts like "Explain OAuth." |
| Context | Project-specific cards include enough context to avoid orphan facts. |
| Duplicates | Near-duplicates are merged or intentionally bidirectional. |
| Usefulness | Do not create cards that are technically true but not worth reviewing. |

### `quiz-generator`

Purpose: create diagnostic and learning-oriented quiz questions from source material.

The skill should test more than recall. It should support recall, comprehension, contrast, application, prediction, diagnosis, transfer, and tradeoff judgment.

Draft trigger description:

```yaml
description: >
  Use this skill when the user wants quizzes, diagnostic questions,
  comprehension checks, MCQs, short-answer questions, answer keys, rubrics,
  feedback, or assessment items from notes, documents, code, courses, papers,
  or project material. Generate source-grounded questions aligned to learning
  objectives and cognitive levels.
```

Default assumptions:

| Field | Default |
|---|---|
| Purpose | diagnostic learning quiz |
| Audience | general professional learner |
| Difficulty | mixed |
| Question count | 7-10 unless requested otherwise |
| Output | Markdown plus canonical JSON |
| Feedback | include answer key, rationales, and remediation unless user asks for interactive mode |

Proposed workflow:

1. Identify quiz purpose, audience, difficulty, item count, question types, and export format if provided.
2. Extract learning objectives.
3. Create a quiz blueprint covering objective coverage, cognitive-level distribution, question-type distribution, and difficulty distribution.
4. Generate questions from the blueprint.
5. Validate each item for objective alignment, source grounding, answerability, ambiguity, appropriate difficulty, useful feedback, and redundancy.
6. For MCQs, use a clear stem, provide one best answer unless multiple-select is explicitly requested, use plausible but clearly wrong distractors, avoid grammatical clues, avoid all-of-the-above and none-of-the-above by default, and explain each option.
7. Return final quiz.

Output contract:

1. quiz blueprint;
2. questions;
3. answer key;
4. rationales and feedback;
5. common misconception or remediation where useful;
6. canonical JSON;
7. requested export format when requested.

Quality bar:

| Check | Rule |
|---|---|
| Objective alignment | Every item maps to a learning objective. |
| Answer correctness | The answer key is correct. |
| Cognitive distribution | Items match the requested or inferred blueprint. |
| Distractor quality | Distractors are plausible but clearly wrong. |
| Feedback quality | Feedback explains why the answer is right or wrong. |
| Ambiguity | No multiple defensible answers unless marked. |
| Transfer | Include application, prediction, diagnosis, or transfer when appropriate. |

### Shared learning-design reference

Both skills should include a compact `references/learning-design.md`.

It should encode only principles both skills actually need:

```text
1. Extract learning objectives before artifacts.
2. Ground factual items in the source.
3. Prefer retrieval over recognition when possible.
4. Keep each item focused on one idea.
5. Make difficulty effortful but answerable.
6. Include misconceptions and edge cases when useful.
7. Align artifacts to learning objectives.
8. Validate before returning.
```

The first version should avoid a long literature review inside `SKILL.md`. More detailed learning theory can live in reference files through progressive disclosure.

Each skill should keep its own local copy of this reference in the first slice so either skill remains portable when copied or installed by itself. A centralized source plus sync check is a follow-up only if local duplication becomes hard to maintain.

When a user asks for both flashcards and a quiz, prefer skill composition when the runtime supports it. The documented fallback should extract shared learning objectives and a compact knowledge map once, then return separate flashcard and quiz sections using each skill's own output contract and separate JSON payloads.

## Expected Behavior Changes

1. A user asking "Turn this paper into Anki cards" triggers `flashcard-generator`.
2. A user asking "Make a 10-question diagnostic quiz from this onboarding doc" triggers `quiz-generator`.
3. A user asking "Summarize this article in one paragraph" triggers neither skill.
4. A user asking "Create flashcards and a quiz from this codebase overview" can use both skills sequentially if the platform supports composition.
5. Flashcard output is source-grounded, atomic, exportable, and not merely a summary.
6. Quiz output includes a blueprint, answer key, rationales, and useful feedback rather than a flat list of questions.
7. Both skills generate from learning objectives and a knowledge map, not directly from raw paragraphs.

## Architecture Impact

Expected touched areas:

```text
docs/proposals/2026-07-04-flashcard-and-quiz-skills.md

skills/flashcard-generator/SKILL.md
skills/flashcard-generator/references/learning-design.md
skills/flashcard-generator/references/card-quality.md
skills/flashcard-generator/schemas/flashcard.schema.json

skills/quiz-generator/SKILL.md
skills/quiz-generator/references/learning-design.md
skills/quiz-generator/references/question-quality.md
skills/quiz-generator/schemas/quiz-item.schema.json

tests/evals/skills/flashcard-generator/cases.yaml
tests/evals/skills/flashcard-generator/trigger-cases.yaml
tests/evals/skills/quiz-generator/cases.yaml
tests/evals/skills/quiz-generator/trigger-cases.yaml

README.md
CONTRIBUTING.md
```

No runtime services are expected.

No new tool permissions are expected.

No scripts are expected in the first slice unless the later plan explicitly accepts schema validation as implementation work.

## Testing and Verification Strategy

Because these are new skills, baseline evidence should compare representative prompts without the skill against the proposed skill behavior. The point is to show that the new skills improve artifact quality, not merely produce plausible-looking lists.

OpenAI's skills guidance says strong instructions typically include the job to be done, required inputs, a step-by-step process, the required output format, and final quality checks. The evals should therefore test not only the final output but whether the skill follows the intended process.

Required `flashcard-generator` eval scenarios:

```yaml
- id: flashcard-normal-anki-cards
  category: normal
  prompt: |
    Turn this onboarding note into Anki-ready flashcards:

    Idempotency prevents duplicate side effects when clients retry requests after
    timeouts. Payment APIs commonly require an idempotency key so the server can
    recognize a retry and return the original result instead of charging again.
  expected_behavior:
    - Produces source-grounded flashcards.
    - Uses atomic prompts.
    - Includes at least one failure-mode or application card.
    - Includes canonical JSON.
    - Does not create broad prompts like "Explain idempotency."

- id: flashcard-cloze-contrast
  category: normal
  prompt: |
    Make cloze and contrast cards from this:

    Authentication verifies who a user is. Authorization determines what that
    user is allowed to do.
  expected_behavior:
    - Produces cloze cards only where context is strong.
    - Produces a contrast card for authentication vs authorization.
    - Preserves the distinction accurately.
    - Does not duplicate equivalent cards unnecessarily.

- id: flashcard-source-grounding-boundary
  category: edge
  prompt: |
    Create flashcards from this note and add any important related facts you know:

    OAuth authorization codes are exchanged for tokens.
  expected_behavior:
    - Grounds cards in the provided source.
    - Marks any inferred or external context clearly, or avoids adding it.
    - Does not fabricate unsupported details.
    - Keeps cards answerable without hidden context.
```

Required `quiz-generator` eval scenarios:

```yaml
- id: quiz-normal-diagnostic
  category: normal
  prompt: |
    Create an 8-question diagnostic quiz from this onboarding note:

    Idempotency prevents duplicate side effects when clients retry requests after
    timeouts. Payment APIs commonly require an idempotency key so the server can
    recognize a retry and return the original result instead of charging again.
  expected_behavior:
    - Produces a quiz blueprint.
    - Includes learning objectives.
    - Includes a mix of recall, comprehension, application, and diagnosis.
    - Includes answer key and rationales.
    - Uses source-grounded questions.

- id: quiz-mcq-distractor-quality
  category: normal
  prompt: |
    Make 4 multiple-choice questions from this:

    A retry can repeat an operation. Idempotency makes retrying safe by ensuring
    the repeated request has the same effect as the original request.
  expected_behavior:
    - Uses clear stems.
    - Provides one best answer per MCQ.
    - Uses plausible distractors that are clearly wrong.
    - Explains why each option is right or wrong.
    - Does not use grammatical clues or "all of the above" by default.

- id: quiz-unsupported-material-boundary
  category: edge
  prompt: |
    Create a quiz from this short note and include advanced questions:

    OAuth is used for authorization.
  expected_behavior:
    - Does not invent unsupported advanced facts as if source-grounded.
    - Either limits questions to source-supported material or clearly marks inferred context.
    - Avoids ambiguous questions with multiple defensible answers.
```

Create at least 12 trigger cases in the first slice, then expand toward 20 after review. Initial trigger examples:

```yaml
- query: "Turn this paper into Anki cards"
  should_trigger: flashcard-generator

- query: "Make cloze deletion cards from these notes"
  should_trigger: flashcard-generator

- query: "Create memory prompts for spaced repetition"
  should_trigger: flashcard-generator

- query: "Make a 10-question diagnostic quiz from this onboarding doc"
  should_trigger: quiz-generator

- query: "Generate MCQs with answer keys and feedback"
  should_trigger: quiz-generator

- query: "Create a comprehension check from this chapter"
  should_trigger: quiz-generator

- query: "Summarize this article in one paragraph"
  should_trigger: neither

- query: "Rewrite this document to be clearer"
  should_trigger: neither

- query: "Create flashcards and a quiz from this codebase overview"
  should_trigger: both
```

Minimum local validation:

```bash
python tests/validate_skills.py
python -m unittest discover tests
git diff --check
```

Run only if the helper exists in the branch:

```bash
python tests/check_readme_sync.py
```

No live model calls should be added to CI in this slice.

## Rollout and Rollback

Rollout should follow the standard Skillsmith lifecycle: proposal review, requirements spec, spec review, execution plan, plan review, durable test specification, implementation, code review, final verification, and PR handoff. The implementation slice should add eval fixtures before or alongside skill authoring, add both skill directories and compact references, update README and contribution docs, and run local validation.

Rollback is straightforward:

```text
remove skills/flashcard-generator/
remove skills/quiz-generator/
remove tests/evals/skills/flashcard-generator/
remove tests/evals/skills/quiz-generator/
revert README/CONTRIBUTING references
```

No runtime services, tool permissions, or CI model calls are introduced, so rollback should be limited to repository content.

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| The two skills overlap and trigger incorrectly. | Use trigger evals with should-trigger, should-not-trigger, and both-skill cases. |
| Flashcards become summaries. | Require atomicity, minimum-information prompts, and card-quality validation. |
| Quizzes become shallow recall lists. | Require blueprinting, cognitive-level distribution, and application or diagnosis items. |
| Generated facts are ungrounded. | Require source refs or explicit inference marking. |
| Shared learning theory becomes bloated. | Keep `SKILL.md` concise and move only necessary details into local references. |
| Schemas add too much first-slice work. | Treat schemas as reference contracts first; executable validation is follow-up. |
| Export claims exceed implementation. | Core output is Markdown plus JSON; specific Anki or LMS exports are generated only when requested and validated manually first. |
| A user asks for both outputs at once. | Allow sequential use of both skills if composition works; otherwise return both sections using the two contracts without creating a third skill. |
| High-stakes learning contexts create safety risk. | Avoid guarantees and require source grounding; create separate review gates for regulated or high-stakes exam contexts if needed. |

## Open Questions

None blocking before proposal review.

The proposal-level calibration is:

1. Include `schemas/flashcard.schema.json` and `schemas/quiz-item.schema.json` as reference JSON Schema contracts in the first slice, but defer executable CI schema validation until outputs stabilize.
2. Keep local `references/learning-design.md` copies in both skill directories for portability, with only truly shared principles duplicated.
3. Prefer skill composition for requests that ask for both flashcards and quizzes. Where composition is unavailable, document a fallback that extracts shared learning objectives and a compact knowledge map once, then returns separate flashcard and quiz sections with separate canonical JSON payloads.

The downstream spec should turn these decisions into explicit requirements without adding direct Anki, LMS, live model CI, or schema-validator integration.

## Decision Log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-07-04 | Create two skills: `flashcard-generator` and `quiz-generator` | They optimize different learning jobs and quality bars. | One combined production skill |
| 2026-07-04 | Use shared learning-design references, not a third skill | Shared theory supports both workflows but is not itself a user-facing task. | Third `learning-design` skill |
| 2026-07-04 | Extract objectives before artifacts | Prevents raw paragraph-to-card/question generation. | Direct generation from source paragraphs |
| 2026-07-04 | Use canonical JSON plus Markdown | JSON supports downstream export; Markdown supports review. | Markdown-only output |
| 2026-07-04 | Keep first slice prompt-first | Avoids scripts, APIs, and export-validator scope creep. | Immediate Anki/LMS integration |
| 2026-07-04 | Require trigger evals | Two nearby skills need clear activation boundaries. | Rely only on descriptions |
| 2026-07-04 | Include reference JSON Schema files without executable validation | Reviewers need stable output contracts, but CI validation adds failure modes and scope before outputs stabilize. | Reference examples only; immediate CI schema validation |
| 2026-07-04 | Duplicate compact learning-design references locally in each skill | Local copies preserve skill portability without requiring repo-level shared dependencies or sync tooling. | Centralized shared reference in the first slice |
| 2026-07-04 | Document a both-output fallback while preferring composition | Combined user requests are real, but the proposal should preserve separate skill contracts and avoid a third broad skill. | Create `study-artifact-generator`; fail when composition is unavailable |

## Next Artifacts

1. `proposal-review` result for this proposal.
2. `specs/flashcard-and-quiz-skills.md`.
3. `spec-review` result.
4. Execution plan.
5. `plan-review` result.
6. `specs/flashcard-and-quiz-skills.test.md`.
7. Eval fixtures for both skills.
8. Implementation of the two skill directories.

Potential later follow-ups after the first slice:

1. executable JSON schema validation;
2. Anki TSV export hardening;
3. QTI, Moodle, or H5P export profiles;
4. AnkiConnect integration;
5. repair-loop workflow from missed flashcards;
6. adaptive quiz remediation workflow;
7. dedicated high-stakes exam-prep review policy.

## Follow-on Artifacts

None yet

## Readiness

Ready for proposal review as a draft direction.

This proposal is not accepted, spec-ready, implementation-ready, verified, or PR-ready until proposal review records a decision and downstream lifecycle artifacts are completed in order.

## References

[Using skills | OpenAI](https://openai.com/academy/skills/)

[Agent Skills - Claude Platform Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
