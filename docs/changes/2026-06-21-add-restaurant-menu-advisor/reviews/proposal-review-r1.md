# Proposal Review R1: Restaurant Menu Advisor

## Review status

changes-requested

## Reviewed artifact

- Proposal: `docs/proposals/2026-06-21-add-restaurant-menu-advisor.md`
- Review stage: proposal-review
- Reviewer: external proposal-review result supplied by user
- Date: 2026-06-21

## Summary

The proposal direction is sound and close to ready: Option 3, a portable pure-prompt skill with an illustrative visual brief, fits the stated product and repository constraints. The review requested one material option-quality edit and one path-consistency clarification before downstream reliance, plus one non-blocking clarity edit.

## Review dimensions

| Dimension | Result | Note |
|---|---|---|
| Problem clarity | pass | Problem is stated independently of solution and calls out allergy-related safety sensitivity. |
| User value | pass | Value is concrete: faster decision-making, reduced regret, differentiated shortlist, and one leading choice. |
| Option diversity | concern | Build options were diverse, but the status-quo/do-nothing baseline was missing. |
| Decision rationale | pass | Recommendation follows stated criteria and dispositions are reasoned. |
| Scope control | pass | Non-goals and scope budget protect the first slice. |
| Architecture awareness | pass | Additive prompt, eval, and documentation artifacts only; no runtime service or dependency. |
| Testability | pass | Eval matrix covers normal, indirect-trigger, failure, safety, misuse, non-trigger, and edge scenarios. |
| Risk honesty | pass | Major risks include hallucination, allergen false reassurance, and image-as-evidence confusion. |
| Rollout realism | pass | Rollout is additive, with clear rollback and narrower image-specific rollback. |
| Readiness for spec | pass | Open questions are bounded and non-blocking. |

## Scope-preservation result

pass

All initial goals are visibly classified with valid treatment values. No deferred or rejected goal lacks rationale. One clarity note is recorded as `PR-R1-003`.

## Scope-budget result

pass

The proposal is broad and multi-workstream. The scope budget is present, uses valid treatment values, and routes deferred or separate-proposal work.

## Vision-fit result

pass as asserted

The `Vision fit` section starts with the exact enum value `fits the current vision` and gives coherent rationale. The original reviewer noted that they could not independently verify this against `VISION.md` because only the proposal and review standard were supplied in their review context.

## Material findings

### Finding ID: PR-R1-001

- Severity: Medium
- Location: `## Options considered`
- Evidence: The proposal considered recommendation-only, tool-dependent, portable visual brief, and split-skill variants, but did not evaluate the status quo: relying on general-purpose chat or a copy-paste prompt without adding a durable catalog entry. The proposal-review skill rule says not to ignore the do-nothing option.
- Required outcome: Add a status-quo/do-nothing option to `## Options considered` with an explicit disposition and a one-line rationale for why a reusable skill beats ad hoc prompting.
- Safe resolution path: Add the option using reasoning already present in the Problem section. No owner decision required.

### Finding ID: PR-R1-002

- Severity: Low
- Location: `## Context` vs `## Architecture impact`; cross-check `## Next artifacts`
- Evidence: Context said the proposal uses a change-local path under `docs/changes/<change-id>/`, but Architecture impact listed the proposal itself at `docs/proposals/2026-06-21-add-restaurant-menu-advisor.md` while spec and test-spec live under `docs/changes/<change-id>/`.
- Required outcome: Reconcile the proposal's own location across Context and Architecture impact. If proposals live in `docs/proposals/` while the change pack lives in `docs/changes/<change-id>/`, correct Context so it does not claim the proposal itself uses the change-local path.
- Safe resolution path: Reconcile against the `docs/workflows.md` artifact-location table.

## Recommended edit

### Finding ID: PR-R1-003

- Severity: Low clarity note
- Location: `## Initial intent preservation`
- Evidence: The row for "Generate a picture of the likely dish before ordering" was marked simply `in scope`, while the proposal actually guarantees a visual brief and treats rendered image generation as conditional on host capability and explicit user request.
- Recommended outcome: Qualify the row so it remains clear that the text brief is guaranteed while rendered image generation is conditional.

## Recording

- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-06-21-add-restaurant-menu-advisor/reviews/proposal-review-r1.md`
- Review log: `docs/changes/2026-06-21-add-restaurant-menu-advisor/review-log.md`
- Review resolution: `docs/changes/2026-06-21-add-restaurant-menu-advisor/review-resolution.md`

## Open blockers

`PR-R1-001` and `PR-R1-002` block proposal approval until revised and re-reviewed. `PR-R1-003` is recommended but not independently blocking.

## Immediate next stage

Author resolves `PR-R1-001` and `PR-R1-002`, ideally also `PR-R1-003`, then reruns lightweight proposal-review. No automatic downstream handoff to `spec`.
