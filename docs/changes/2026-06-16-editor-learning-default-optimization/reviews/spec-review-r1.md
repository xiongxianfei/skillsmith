# Spec Review R1: Editor Learning Default Optimization

## Result

- Skill: spec-review
- Review status: changes-requested
- Material findings: `F-SPEC-EDITOR-LEARNING-001`, `F-SPEC-EDITOR-LEARNING-002`
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-06-16-editor-learning-default-optimization/reviews/spec-review-r1.md`
- Review log: `docs/changes/2026-06-16-editor-learning-default-optimization/review-log.md`
- Review resolution: `docs/changes/2026-06-16-editor-learning-default-optimization/review-resolution.md`
- Open blockers: `F-SPEC-EDITOR-LEARNING-001`, `F-SPEC-EDITOR-LEARNING-002`
- Immediate next stage: spec revision

## Findings

## Finding F-SPEC-EDITOR-LEARNING-001

- Finding ID: F-SPEC-EDITOR-LEARNING-001
- Severity: blocking
- Location: `specs/editor-learning-default-optimization.md`, examples E6-E7, requirements R6, R23-R24, output templates R33-R35, boundary behavior for trivial-only correction, edge cases EC8-EC10, acceptance criteria AC5 and AC17
- Evidence: R6 requires the skill to include a learning notes block by default for normal requests. R33 and R34 also include the learning notes block in the default and explicit-target templates. But E6 says the skill may "omit itemized edit lessons" for a typo-only correction, R23 says the skill must skip explanations for trivial edits unless they reveal a recurring pattern, EC8 says a typo-only source "does not create a multi-note teaching block," and AC17 only says trivial-only fixes do not produce padded explanations. These statements do not define whether the required default `Learning notes` block still appears, whether it may be empty, or what non-padded content it should contain when there is no substantive lesson.
- Required outcome: The spec must define the observable output contract for default-on `Learning notes` when the source has no substantive lesson, including trivial-only corrections, already-good text, and skipped brittle-rule cases. It must not leave implementation to choose between omitting the block, rendering an empty block, or inventing a lesson.
- Safe resolution path: Revise E6, R23-R24, boundary behavior, EC8-EC10, and AC17 so they state that the `Learning notes` block still appears by default unless explicitly suppressed, but contains at most one concise non-padded note such as a restraint/preservation note or "Only a typo was corrected; there was no broader writing pattern to teach." Keep explicit suppression as the only normal path that removes the block.
- needs-decision rationale: none

## Finding F-SPEC-EDITOR-LEARNING-002

- Finding ID: F-SPEC-EDITOR-LEARNING-002
- Severity: major
- Location: `specs/editor-learning-default-optimization.md`, requirements R12-R13, output templates R33-R34, and acceptance criteria AC12-AC13
- Evidence: R12 says each learning note "SHOULD" use concrete original-to-revised anchoring or an equivalent concrete reference, while R13 says each note "MUST" teach a reusable principle. The output templates show original-to-revised anchoring, and AC12 says learning notes are anchored to concrete edits or translation choices. Because R12 is only SHOULD-level, an implementation could omit anchoring while still satisfying the numbered requirement, even though the proposal and acceptance criteria treat anchoring as central to avoiding generic commentary.
- Required outcome: The spec must make the anchoring requirement normative enough for tests and implementation, while defining any allowed exception for fallback notes that do not have a substantive original-to-revised change.
- Safe resolution path: Change R12 to a MUST for substantive learning notes. Add a narrow exception for restraint, typo-only, no-substantive-lesson, or integrity-boundary fallback notes: those notes must still reference the concrete source condition or edit category rather than generic self-commentary. Align AC12 with that wording.
- needs-decision rationale: none

## Review Dimensions

| Review dimension | Verdict |
| --- | --- |
| requirement clarity | block |
| normative language | concern |
| completeness | concern |
| testability | concern |
| examples | concern |
| compatibility | pass |
| observability | pass |
| security/privacy | pass |
| non-goals | pass |
| acceptance criteria | concern |

## Review Notes

The spec is directionally aligned with the accepted proposal: it preserves deliverable-first output, explicit suppression, response-language-only notes, target-language overrides, fidelity, restraint, and the pure-prompt boundary. The remaining issue is not strategy; it is contract precision around the new mandatory default block.

The user explicitly clarified that the skill must include a `Learning notes` block by default. That means the spec needs a concrete fallback for cases where earlier proposal language wanted to avoid explaining trivial edits or padding notes. "Do not pad" is correct, but downstream work still needs to know what appears under the required block.

## Exact Suggested Spec Edits

- Replace E6's outcome with wording that keeps the block: `Then the skill corrects the typo and includes a Learning notes block with at most one concise note, such as "Only the typo was corrected; there was no broader writing pattern to teach."`
- Revise R12 to: `Each substantive learning note MUST use concrete original-to-revised anchoring or an equivalent concrete reference to the edit or translation choice.`
- Add after R12: `Fallback learning notes for restraint, typo-only, no-substantive-lesson, or integrity-boundary cases MUST reference the concrete source condition or edit category and MUST NOT become generic self-commentary.`
- Revise R23 to state that trivial edits are not explained as grammar lessons, but the default block still appears unless explicitly suppressed.
- Revise AC17 to assert both sides: trivial-only fixes do not produce padded explanations and still render the default block with an allowed concise fallback note unless explicitly suppressed.

## Eventual test-spec readiness

conditionally-ready

The spec has stable examples, requirement IDs, output templates, and acceptance criteria, but test-spec authoring should wait until `F-SPEC-EDITOR-LEARNING-001` and `F-SPEC-EDITOR-LEARNING-002` are resolved because default-block and anchoring tests would otherwise require guessing.

## Stop condition

Resolve `F-SPEC-EDITOR-LEARNING-001` and `F-SPEC-EDITOR-LEARNING-002`, then run renewed spec review before architecture, execution planning, or test-spec authoring relies on this spec.
