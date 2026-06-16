## Result

- Skill: proposal-review
- Review status: changes-requested
- Material findings: `F-PROP-EDITOR-SOURCE-COMPANION-001`
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/reviews/proposal-review-r2.md`
- Review log: `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/review-log.md`
- Review resolution: `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/review-resolution.md`
- Open blockers: `F-PROP-EDITOR-SOURCE-COMPANION-001`
- Immediate next stage: isolated stop; revise proposal lifecycle sections, then rerun proposal-review.

## Material Findings

## Finding F-PROP-EDITOR-SOURCE-COMPANION-001

- Finding ID: F-PROP-EDITOR-SOURCE-COMPANION-001
- Severity: major
- Location: `docs/proposals/2026-06-16-editor-source-plus-companion-language-optimization.md:3`, `docs/proposals/2026-06-16-editor-source-plus-companion-language-optimization.md:449`, `docs/proposals/2026-06-16-editor-source-plus-companion-language-optimization.md:459`, `docs/proposals/2026-06-16-editor-source-plus-companion-language-optimization.md:465`
- Evidence: The proposal status now says `accepted`, but `Readiness` still says "Ready for proposal review as a draft direction" and "This proposal is not accepted." `Next Artifacts` still lists `proposal-review` as pending, and `Follow-on Artifacts` still says `None yet` even though proposal-review records now exist.
- Required outcome: Make the lifecycle sections agree with the accepted proposal state before downstream spec authoring relies on this proposal.
- Safe resolution path: Update `Readiness` to state that the proposal is accepted and ready for spec authoring, while still not claiming spec completion, implementation readiness, verification, branch readiness, or PR readiness. Move the recorded proposal-review artifacts into `Follow-on Artifacts`, and adjust `Next Artifacts` so the next pending stage starts with the spec.
- needs-decision rationale: none

## Review Dimensions

- Problem clarity: pass. The proposal identifies the real problem as prompt weight distribution and default-language behavior, not the existing fidelity-with-restraint editing philosophy.
- User value: pass. The proposed default gives users a polished source-language version plus one useful translation, while preserving learning as a secondary benefit.
- Option diversity: pass. The proposal considers hardcoded Chinese + English, source-language-only output, source + companion output, preserving full learning/template detail, and moving learning rules to a reference file.
- Decision rationale: pass. The recommended source + companion default follows from the stated goal to polish the original and translate the resolved meaning without hardcoding Chinese + English for every source language.
- Scope control: pass. Non-goals and the scope budget keep the work limited to `editor` prompt behavior, eval evidence, and related lifecycle artifacts.
- Architecture awareness: pass. The proposal preserves the pure-prompt boundary and explicitly avoids runtime, installer, CI, generated artifact, and validator changes.
- Testability: pass. The proposed scenarios cover default source + English behavior, English-source fallback, explicit target overrides, target-only output, learning-note compactness, trivial corrections, and integrity priority.
- Risk honesty: pass. The proposal names meaningful risks around English-source fallback, broad language quality claims, learning-note bloat, template consistency, fidelity after removing hidden cross-checks, target-language conflicts, and prompt growth.
- Rollout realism: pass. Rollout and rollback are scoped to prompt/eval artifacts and do not require migration machinery or runtime recovery.
- Readiness for spec: block. The direction is ready, but the tracked proposal artifact has contradictory lifecycle state after acceptance normalization. That must be corrected before spec authoring relies on it.

## Scope Preservation Review

- Scope-preservation result: pass. The proposal visibly classifies the user's initial goals and keeps source + companion output, English default companion, strong editing philosophy, token-footprint reduction, simplified learning, template consolidation, hidden-cross-check removal, rule deduplication, description cleanup, conflict hierarchy, and default teaching behavior in scope.
- Scope-budget result: pass. Broad work items and out-of-scope work are classified clearly enough for downstream reliance.
- Vision fit result: pass. Root `VISION.md` exists, and the proposal uses the exact value `fits the current vision`; the rationale aligns with Skillsmith's reusable writing, translation, learning, and productivity focus.
- Standing artifact gates: pass. `VISION.md` and `CONSTITUTION.md` exist; this is not a bootstrap proposal and does not bypass standing artifact gates.

## Recommended Proposal Edits

- Required edit: resolve `F-PROP-EDITOR-SOURCE-COMPANION-001` by synchronizing `Readiness`, `Next Artifacts`, and `Follow-on Artifacts` with the accepted proposal status and existing proposal-review records.
- Preserve from R1: the downstream spec should still soften the hard three-note cap, define mixed-language instruction handling, specify explicit multi-target behavior, clarify target-only notes behavior, add a complex conflict eval, and keep the spec dense.

## Recommendation

- Recommendation: changes-requested. The proposal direction remains accepted in substance, but the artifact is not ready for spec reliance until the lifecycle sections stop contradicting the accepted status. This review is isolated and does not automatically hand off to spec.
