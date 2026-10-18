# Flashcard And Quiz Skills requirements

Current requirement owner, migrated from the approved source without changing product behavior. IDs R/AC/EC/E retain their source-local identity under `flashcard-and-quiz-skills`. The [source dispositions](../../docs/changes/2026-10-18-rigorloop-v2-adoption/source-disposition.md) preserve exact sources, historical delivery conditions and supersession. One-time rollout instructions are historical evidence, not new product changes.

## Goal and context

Skillsmith will add two focused learning artifact skills: `flashcard-generator` for source-grounded spaced-repetition cards and `quiz-generator` for diagnostic quizzes and assessment items. The skills remain portable prompt assets. They share compact learning-design principles, but they keep separate trigger descriptions, output contracts, quality bars, eval fixtures, and reference files.

The first slice is prompt-centered. It includes skill prompts, local references, reference JSON Schema files, eval fixtures, README synchronization, and contributor guidance only where needed. It does not add runtime integrations, live model CI, executable schema validation, external services, or a broad combined study-artifact skill.

## Glossary

- Flashcard: an atomic retrieval prompt intended for durable recall, spaced repetition, or Anki-style review.
- Quiz item: a diagnostic or learning-oriented question with answer key, rationale, feedback, and objective alignment.
- Learning objective: an observable learner outcome extracted or inferred from source material before artifact generation.
- Knowledge map: a compact intermediate model of facts, concepts, procedures, distinctions, examples, non-examples, prerequisites, and misconceptions.
- Canonical JSON: the structured output payload that acts as the source of truth for downstream export.
- Reference schema: a JSON Schema file that documents expected output shape but is not enforced by CI in this slice.
- Source-grounded: factual content is traceable to user-provided material or clearly marked as inferred or external.

## Examples first

Example E1: Anki-style flashcards from onboarding notes
Given a user asks "Turn this onboarding note into Anki-ready flashcards" and provides text about idempotency keys
When `flashcard-generator` runs
Then it extracts learning objectives, builds a compact knowledge map, returns atomic source-grounded cards, includes at least one application or failure-mode card, and includes canonical JSON.

Example E2: Diagnostic quiz from source material
Given a user asks "Create an 8-question diagnostic quiz from this onboarding note" and provides text about retry behavior and duplicate side effects
When `quiz-generator` runs
Then it returns a quiz blueprint, learning objectives, mixed cognitive levels, questions, answer key, rationales, feedback, and canonical JSON.

Example E3: Non-trigger summary request
Given a user asks "Summarize this article in one paragraph"
When skill selection is considered
Then neither `flashcard-generator` nor `quiz-generator` is the primary skill.

Example E4: Combined flashcard and quiz request
Given a user asks "Create flashcards and a quiz from this codebase overview"
When the runtime supports skill composition
Then both workflows may run sequentially from shared learning objectives and a compact knowledge map.
When composition is unavailable
Then the fallback returns separate flashcard and quiz sections using each skill's output contract and separate canonical JSON payloads.

Example E5: Unsupported material boundary
Given a user asks for advanced flashcards or quiz questions from a short source note such as "OAuth is used for authorization"
When the skill generates artifacts
Then it does not present unsupported advanced facts as source-grounded and either limits output to source-supported material or clearly marks inferred context.

## Requirements

<a id="r1"></a>

R1. The repository MUST add `skills/flashcard-generator/SKILL.md` with frontmatter `name: flashcard-generator` and an English trigger-forward `description`.

<a id="r2"></a>

R2. The repository MUST add `skills/quiz-generator/SKILL.md` with frontmatter `name: quiz-generator` and an English trigger-forward `description`.

<a id="r3"></a>

R3. Each new skill body MUST include `$ARGUMENTS` and a `## Output Format` section.

<a id="r4"></a>

R4. Each new skill MUST omit optional frontmatter such as `argument-hint`, `effort`, and `allowed-tools`.

<a id="r5"></a>

R5. `flashcard-generator` MUST be triggered by requests for spaced-repetition flashcards, Anki cards, cloze deletions, memory prompts, durable recall practice, or retention cards from notes, documents, code, papers, courses, or project material.

<a id="r6"></a>

R6. `quiz-generator` MUST be triggered by requests for quizzes, diagnostic questions, comprehension checks, MCQs, short-answer questions, answer keys, rubrics, feedback, or assessment items from notes, documents, code, courses, papers, or project material.

<a id="r7"></a>

R7. The trigger descriptions MUST distinguish flashcard generation from quiz generation and MUST NOT make generic summary, rewrite, or paragraph-summary requests primary triggers.

<a id="r8"></a>

R8. Each skill MUST identify or infer learner goal, audience, source material, count, difficulty, and requested export format when that information is available.

<a id="r9"></a>

R9. Each skill MUST extract learning objectives before generating artifacts.

<a id="r10"></a>

R10. Each skill MUST build or infer a compact knowledge map before generating artifacts.

<a id="r11"></a>

R11. Each skill MUST prefer source-grounded factual content and MUST mark inferred or external context when the user asks for related facts beyond the supplied source.

<a id="r12"></a>

R12. `flashcard-generator` MUST select only knowledge worth retaining and MUST avoid broad, vague, duplicate, premature, or trivia-focused cards unless the user explicitly requests trivia.

<a id="r13"></a>

R13. `flashcard-generator` MUST support appropriate card types, including basic Q/A, cloze, bidirectional, contrast, example/non-example, procedure, and failure-mode cards.

<a id="r14"></a>

R14. `flashcard-generator` MUST validate card quality for atomicity, source grounding, answerability, specificity, context, duplicate handling, and usefulness before returning final cards.

<a id="r15"></a>

R15. `flashcard-generator` output MUST include a deck summary, learning objectives, human-review card table, canonical JSON, and requested export format when requested.

<a id="r16"></a>

R16. `quiz-generator` MUST create a quiz blueprint before item generation, covering objective coverage, cognitive-level distribution, question-type distribution, and difficulty distribution.

<a id="r17"></a>

R17. `quiz-generator` MUST support recall, comprehension, contrast, application, prediction, diagnosis, transfer, and tradeoff judgment where appropriate for the source and user request.

<a id="r18"></a>

R18. `quiz-generator` MUST validate item quality for objective alignment, source grounding, answerability, ambiguity, appropriate difficulty, useful feedback, and redundancy before returning final questions.

<a id="r19"></a>

R19. For MCQs, `quiz-generator` MUST use clear stems, one best answer unless multiple-select is explicitly requested, plausible but clearly wrong distractors, no grammatical clues, no "all of the above" or "none of the above" by default, and explanations for each option.

<a id="r20"></a>

R20. `quiz-generator` output MUST include a quiz blueprint, questions, answer key, rationales and feedback, misconception or remediation where useful, canonical JSON, and requested export format when requested.

<a id="r21"></a>

R21. The implementation MUST include local `references/learning-design.md` files under both new skill directories, with compact shared principles only.

<a id="r22"></a>

R22. The implementation MUST include flashcard-specific quality guidance in `skills/flashcard-generator/references/card-quality.md`.

<a id="r23"></a>

R23. The implementation MUST include quiz-specific quality guidance in `skills/quiz-generator/references/question-quality.md`.

<a id="r24"></a>

R24. The implementation MUST include `skills/flashcard-generator/schemas/flashcard.schema.json` and `skills/quiz-generator/schemas/quiz-item.schema.json` as reference JSON Schema contracts.

<a id="r25"></a>

R25. The reference schemas MUST document required canonical JSON fields and output shape, but this slice MUST NOT add executable schema validation or CI schema enforcement.

<a id="r26"></a>

R26. Requests that ask for both flashcards and quizzes MUST be handled by composition when available or by a documented fallback that extracts shared learning objectives and a knowledge map once, then returns separate outputs with separate canonical JSON payloads.

<a id="r27"></a>

R27. The implementation MUST add eval fixtures for both new skills under `tests/evals/skills/<skill-name>/cases.yaml`.

<a id="r28"></a>

R28. Each eval fixture MUST satisfy the approved skill-quality standard, including normal intended use, indirect trigger coverage, and at least one edge, safety, failure, non-trigger, or misuse scenario.

<a id="r29"></a>

R29. The eval evidence MUST cover source-grounding boundaries for unsupported or externally inferred facts.

<a id="r30"></a>

R30. Trigger eval evidence MUST cover flashcard-only, quiz-only, neither-skill, and both-skill requests.

<a id="r31"></a>

R31. README skill table and slash-command enumeration MUST be synchronized for the two new skills.

<a id="r32"></a>

R32. Contributor or implementation guidance MUST be updated only where needed to keep new-skill eval and documentation expectations clear.

<a id="r33"></a>

R33. The first slice MUST NOT add direct AnkiConnect, Moodle, H5P, QTI, LMS API, external service, live model CI, runtime dependency, installer behavior, or CI behavior changes.

<a id="r34"></a>

R34. The skills MUST NOT provide medical, legal, financial, or high-stakes exam-prep guarantees and MUST preserve source-grounding and uncertainty boundaries for high-stakes learning contexts.

<a id="r35"></a>

R35. Skill files SHOULD stay under 300 lines where practical and MUST remain below the approved hard line limit unless a later accepted exception is recorded.

## Inputs and outputs

Inputs:

- User-provided notes, documents, code excerpts, papers, course material, project material, or pasted source text.
- Optional learner audience, goals, difficulty, count, desired artifact types, requested export format, and source-grounding preferences.
- Skill-local references and reference schemas.

Outputs:

- `flashcard-generator`: deck summary, learning objectives, card table, canonical JSON, and requested flashcard export.
- `quiz-generator`: quiz blueprint, questions, answer key, rationales, feedback, misconception or remediation notes where useful, canonical JSON, and requested quiz export.
- Repository artifacts: new skill directories, references, schemas, eval fixtures, README updates, and targeted contributor documentation updates if needed.

## State and invariants

- The two skills remain separate runtime skills.
- Shared learning-design guidance is duplicated locally in both skill directories for portability in this slice.
- Canonical JSON is the structured output source of truth.
- Reference schemas are documentation contracts only until a later accepted proposal and spec adds executable validation.
- Skills remain pure Markdown prompt assets.
- No existing skill behavior is intentionally changed by this slice.

## Error and boundary behavior

- If source material is too thin for the requested artifact count or difficulty, the skill MUST either reduce scope, ask for more source material when necessary, or clearly mark inferred context.
- If a user asks for unsupported related facts, the skill MUST NOT present them as source-grounded.
- If a prompt requests both flashcards and a quiz, the result MUST preserve separate output contracts and JSON payloads.
- If a user requests high-stakes guarantees, the skills MUST avoid guarantees and keep guidance source-grounded and uncertainty-aware.
- If a requested export profile is not fully specified by the first slice, the skill MUST provide best-effort structured output and avoid claiming tool-level compatibility that has not been validated.

## Security and privacy

- Eval fixtures and examples MUST use fictional or sanitized source material.
- Skills MUST NOT require secrets, credentials, private local paths, unpublished personal data, or external service access.
- High-stakes learning requests MUST be bounded by source grounding, uncertainty marking, and no guarantee language.

## Accessibility and UX

No interactive UI is introduced. Skill outputs should be structured, scannable Markdown with copyable JSON blocks and export sections where requested.

## Performance expectations

No runtime performance contract applies. Prompt length should remain reviewable and should use progressive disclosure through one-level-deep reference files where detail would bloat `SKILL.md`.

## Edge cases

<a id="ec1"></a>

EC1. User asks for generic summary: neither new skill should be the primary trigger.

<a id="ec2"></a>

EC2. User asks for "Anki cards" without count: `flashcard-generator` uses its default count range unless source size suggests fewer cards.

<a id="ec3"></a>

EC3. User asks for "MCQs with feedback": `quiz-generator` uses MCQ rules and explains each option.

<a id="ec4"></a>

EC4. User asks for both outputs: composition or fallback returns separate sections and JSON payloads.

<a id="ec5"></a>

EC5. Source is too short for advanced questions or many cards: output is constrained to source-supported material or marks inference.

<a id="ec6"></a>

EC6. User requests direct Anki or LMS integration: skill provides portable export text only and does not call external APIs.

<a id="ec7"></a>

EC7. User asks for high-stakes exam or regulated-domain guarantees: skill avoids guarantees and uses source-grounded, uncertainty-aware framing.

## Non-goals

- Do not create `study-artifact-generator`.
- Do not create a third `learning-design` skill.
- Do not build a spaced-repetition scheduler.
- Do not integrate with AnkiConnect, Moodle, H5P, QTI, LMS APIs, or external services.
- Do not add executable schema validators or CI schema validation.
- Do not require live model calls in CI.
- Do not optimize unrelated Skillsmith skills.

## Acceptance criteria

These criteria retain their original IDs. Creation, baseline and first-slice timing conditions describe the original delivery; continuing behavior and evidence obligations remain applicable to future material changes. Moving this contract does not renew prior acceptance.

<a id="ac1"></a>

AC1. `python tests/validate_skills.py` passes after the two new skill directories and eval fixtures are added, aside from existing acknowledged warnings.

<a id="ac2"></a>

AC2. `python -m unittest discover tests` passes.

<a id="ac3"></a>

AC3. `python tests/check_readme_sync.py` passes after README synchronization.

<a id="ac4"></a>

AC4. `git diff --check` passes.

<a id="ac5"></a>

AC5. Both new `SKILL.md` files include required frontmatter, `$ARGUMENTS`, and `## Output Format`.

<a id="ac6"></a>

AC6. Both new eval fixtures include normal, indirect-trigger, edge-like, and source-grounding-boundary coverage.

<a id="ac7"></a>

AC7. Trigger evidence covers flashcard-only, quiz-only, neither, and both-skill requests.

<a id="ac8"></a>

AC8. Prompt inspection confirms learning objectives and knowledge map steps precede artifact generation in both skills.

<a id="ac9"></a>

AC9. Prompt inspection confirms flashcard and quiz output contracts match this spec.

<a id="ac10"></a>

AC10. Prompt inspection confirms schema references are reference-only and no executable schema validation is added.

<a id="ac11"></a>

AC11. README enumerates both new skills consistently.

<a id="ac12"></a>

AC12. No direct external integration, runtime dependency, live model CI, or installer behavior change is introduced.

## Open questions

None.

## Compatibility and migration

- This is an additive change.
- Existing skills, installer behavior, validator behavior, CI behavior, and README install commands remain compatible.
- New skills are not grandfathered and require eval fixtures before merge.
- Rollback removes the two skill directories, their eval fixtures, README and contributor-doc references, and any change-local artifacts tied only to this initiative.

## Observability

- Static validation remains `python tests/validate_skills.py`.
- Unit and helper checks remain `python -m unittest discover tests` and `python tests/check_readme_sync.py`.
- Reviewers observe behavior through eval fixtures, manual smoke evidence, prompt inspection, schema references, README sync, and review records.
- No runtime telemetry, logs, metrics, or traces are introduced.
