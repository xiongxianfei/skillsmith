# Flashcard and quiz system behavior

## Capabilities

F-LEARN-001 — Generate source-grounded retention cards. F-LEARN-002 — Generate diagnostic quizzes and useful feedback. Both use the [learning artifact requirements](../requirements/flashcard-and-quiz-skills.md); they remain separate user-facing skills with separate output contracts.

| Function | Inputs, behavior and result | Failure and boundary | Requirement basis |
| --- | --- | --- | --- |
| FN-LEARN-001 — Establish objectives and source knowledge | Interpret source material, learner goal, audience and requested difficulty/count; derive objectives and a compact knowledge map | Mark inferred/external context; do not treat unsupported facts as supplied evidence | R5–R11, R26, R34 |
| FN-LEARN-002 — Select and validate retention cards | Select useful retained knowledge, choose suitable card forms, and check atomicity, answerability, context, redundancy and source fidelity | Avoid vague/trivial cards unless requested; do not promise high-stakes outcomes | R12–R15, R34 |
| FN-LEARN-003 — Design and validate diagnostic items | Create an objective/cognitive-level/type/difficulty blueprint, construct items and check alignment, ambiguity, feedback and distractors | MCQ expectations and source limits remain those of the requirement owner | R16–R20, R34 |
| FN-LEARN-004 — Present distinct artifact contracts | Return human-review content and canonical JSON, plus requested export forms; when both skills are requested, share source analysis and preserve separate outputs | Reference schemas describe output; they are not an executable validation service or an LMS integration | R15, R20–R26, R33 |

F-LEARN-001 uses FN-LEARN-001/002/004. F-LEARN-002 uses FN-LEARN-001/003/004. [Portable skill architecture](../architecture/portable-skills.md) owns allocation. No learner database, scheduling service, AnkiConnect or LMS connection is introduced.

## Test intent

Compare flashcard-only, quiz-only, neither and combined requests; assess source grounding, indirect triggers, plausible-but-wrong distractors, ambiguity, limited source support, JSON/output separation and high-stakes uncertainty. Existing fixtures cover the authored skill contracts. Migration does not add executable schema enforcement or claim measured learning effectiveness.
