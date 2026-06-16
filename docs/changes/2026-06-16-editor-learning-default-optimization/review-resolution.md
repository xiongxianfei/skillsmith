# Review Resolution: Editor Learning Default Optimization

## Status

closed

## Findings

## Resolution: Spec Review R1

### `F-SPEC-EDITOR-LEARNING-001`

- Source: `docs/changes/2026-06-16-editor-learning-default-optimization/reviews/spec-review-r1.md`
- Required outcome: define the observable output contract for default-on `Learning notes` when the source has no substantive lesson, including trivial-only corrections, already-good text, and skipped brittle-rule cases.
- Disposition: accepted
- Resolution status: closed by spec-review-r2
- Resolution summary: The spec now defines the default `Learning notes` block as mandatory for every non-empty, non-suppressed editing or translation request. The block must not be empty. For substantive edits, it contains anchored learning notes. For trivial-only, already-strong, no-substantive-lesson, brittle-rule, or similar fallback cases, it contains exactly one concise non-padded fallback note. Explicit suppression remains the normal path that removes the block.
- Rationale: The product requirement is default teaching. Earlier wording prevented padding but left implementers to choose between omitting the block, rendering an empty block, or inventing a lesson. The revised contract keeps default teaching observable without rewarding over-editing or noise.

### `F-SPEC-EDITOR-LEARNING-002`

- Source: `docs/changes/2026-06-16-editor-learning-default-optimization/reviews/spec-review-r1.md`
- Required outcome: make the anchoring requirement normative enough for tests and implementation, while defining allowed exceptions for fallback notes that do not have a substantive original-to-revised change.
- Disposition: accepted
- Resolution status: closed by spec-review-r2
- Resolution summary: The spec now makes concrete anchoring mandatory for substantive learning notes. Fallback notes are narrowly exempt from original-to-revised anchoring only when there is no substantive edit or safe reusable principle; they must still reference the concrete source condition, edit category, or integrity issue.
- Rationale: Anchoring is central to avoiding generic self-commentary. Making it normative gives test-spec and implementation a stable contract while preserving a practical fallback for no-substantive-lesson cases.
