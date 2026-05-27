# Proposal Review R1: Editor Expert Quality Optimization

## Review result

Status: changes-requested

Material findings:

- `F-PROP-EDITOR-EXPERT-001`
- `F-PROP-EDITOR-EXPERT-002`

Recording status: recorded after review text was provided by the user.

Reviewed proposal:

- `docs/proposals/2026-05-26-editor-expert-quality-optimization.md`

## Summary

The proposal is directionally strong. It correctly reframes `editor` around expert judgment, preserves the clarified bilingual Chinese/English final-output requirement, keeps the work limited to one low-risk skill, and rejects persona-only prompting in favor of persona plus guardrails.

The review requested revision before acceptance because the output contract was still ambiguous and the supersession relationship with the previous editor optimization change was under-specified.

## Material findings

### `F-PROP-EDITOR-EXPERT-001`: output contract is still ambiguous

Severity: major

Location: Goals, Recommended Direction, Expected Behavior Changes

Evidence:

The proposal said it would replace the fixed three-stage report with an expert-first contract, but proposed defaults such as "the edited text plus final Chinese and English versions" left unclear whether Chinese or English source text would be duplicated as both edited source text and final language output. Russian source behavior and translation-oriented requests were also not precise enough for downstream spec authors.

Required outcome:

The proposal should make one proposal-level output decision clear enough that the spec can implement it without guessing.

Safe resolution path:

Clarify that Chinese and English final versions are always required; for Chinese or English source text, the edited source-language version is the corresponding final version; simple edits should not duplicate source-language content or include default assessment/why sections; Russian source text includes optimized Russian only when the user asks to edit or polish the Russian source itself.

### `F-PROP-EDITOR-EXPERT-002`: supersession of the previous editor change is under-specified

Severity: major

Location: Problem, Next Artifacts, Follow-on Artifacts

Evidence:

The proposal said that, if accepted, it would supersede the fixed three-stage default in the previous editor proposal and spec, but it did not explicitly retire or replace the earlier change path. This could leave downstream agents treating two competing editor behavior contracts as active.

Required outcome:

Add an explicit supersession plan for the earlier editor optimization artifacts.

Safe resolution path:

Identify the prior proposal, spec, and unresolved downstream work as superseded if this proposal is accepted; name `2026-05-26-editor-expert-quality-optimization` as the new authoritative change ID; explain which prior findings do or do not carry forward; and point the older review log toward this proposal as the replacement path.

## Review dimensions

| Dimension | Verdict | Notes |
|---|---:|---|
| Problem clarity | pass | Fixed-report behavior is identified as the current problem. |
| User value | pass | Expert-quality editing is concrete and useful. |
| Option diversity | pass | Status quo, persona-only, persona-plus-guardrails, strict style guide, and skill splitting are considered. |
| Decision rationale | pass | Option 3 follows from weak-model and fidelity concerns. |
| Scope control | pass | Single-skill scope, no high-risk pairing, no tools, no live CI. |
| Architecture awareness | pass | Expected touched areas are bounded and runtime architecture is unchanged. |
| Testability | concern | Eval categories are good, but output de-duplication needed clarification before spec. |
| Risk honesty | pass | Over-transformation, weak models, verbosity, translation, unsupported language, and high-risk spillover are named. |
| Rollout realism | pass | Plan, plan-review, and test-spec order is present and rollback is simple. |
| Readiness for spec | concern | Ready after fixing output contract and supersession plan. |

## Recommended non-material edits

1. Add concrete eval prompts for all seven scenarios.
2. Add a review checklist.
3. Make description-update expectations explicit because the current skill description still advertises a fixed three-stage report.

## Required next step

Revise the proposal, then run proposal review again. Do not proceed to spec until the proposal is accepted or the findings are explicitly dispositioned.
