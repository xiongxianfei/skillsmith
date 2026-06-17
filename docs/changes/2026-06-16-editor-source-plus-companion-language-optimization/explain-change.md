# Explain Change: Editor Source Plus Companion Language Optimization

## Status

closed

## Summary

This change updates the `editor` skill from a hardcoded Chinese + English default to a source-language plus companion-language contract. The source text is polished in its original language first, then rendered into one companion language by default.

The companion language defaults to English for non-English source text. For English source text, the prompt avoids duplicate English output by using a clearly non-English instruction language when available, otherwise Chinese. The change also keeps learning notes default-on while simplifying their rules, removes hidden Chinese + English cross-check rendering, and consolidates output behavior around one base template plus modification rules.

## Problem

The previous `editor` direction had the right editing philosophy, but the prompt weight and default-language behavior had drifted. It over-focused on learning-note fallback cases and output template permutations, and it treated Chinese + English as the universal visible default even when the source language was neither Chinese nor English.

The accepted goal was to preserve fidelity with restraint while making the visible output contract more general: polished source language plus one companion language.

## Decision Trail

The accepted proposal chose source language plus one companion language over hardcoded Chinese + English, source-only output, and exhaustive template retention. Proposal review accepted the direction and asked the spec to soften the three-note cap, define mixed-language instruction handling, specify multi-target behavior, clarify target-only notes behavior, and cover a complex integrity conflict.

The approved spec records the final contract in `specs/editor-source-plus-companion-language-optimization.md`:

- R1-R4 keep the skill portable and addressable.
- R5-R7 make the description trigger-focused instead of policy-heavy.
- R8-R27 preserve fidelity, source/target separation, companion-language resolution, visible-version verification, and removal of hidden cross-check rendering.
- R28-R37 define the base output shape, explicit targets, multi-targets, target-only behavior, and translation-only behavior.
- R38-R50 keep learning notes default-on, compact, concrete, and suppressible.
- R51-R56 put integrity above explicit user constraints, deliverables, teaching, and brevity.
- R57-R67 require prompt concision, removal of stale Chinese + English defaults, eval evidence, baseline evidence, and post-change evidence.

Architecture review approved a no-impact architecture rationale: this is a leaf prompt, eval, README, and lifecycle-evidence change with no runtime, persistence, API, installer, CI, or ADR impact.

The execution plan split work into three implementation milestones:

- M1: update editor eval fixture and capture baseline evidence before prompt edits.
- M2: implement the editor prompt and README wording.
- M3: record post-change evidence and validation for the final prompt state.

## Diff Rationale By Area

| File | Change | Reason | Source artifact | Test/evidence |
| --- | --- | --- | --- | --- |
| `tests/evals/skills/editor/cases.yaml` | Replaced stale editor eval expectations with source-language plus companion-language cases. | Required eval evidence for Chinese, Russian, Spanish, English fallback, mixed directive handling, explicit targets, multi-targets, target-only behavior, learning notes, trivial correction, and integrity conflicts. | Spec R64-R65; test spec T3-T10, T14. | `python tests/validate_skills.py`; manual scenario coverage in baseline/post-change evidence. |
| `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/baseline-evidence.md` | Recorded pre-change prompt behavior and line count before editing `skills/editor/SKILL.md`. | The spec requires baseline evidence before prompt edits and comparison against the same scenario classes after implementation. | Spec R66-R67; test spec T11. | Prompt inspection; `wc -l` evidence. |
| `skills/editor/SKILL.md` | Replaced hardcoded Chinese + English default with source-language plus companion-language resolution, added deterministic English-source fallback, simplified learning notes, consolidated output rules, and removed hidden Chinese + English cross-check rendering. | Implements the accepted visible language contract and prompt-weight reduction while preserving fidelity, integrity, target handling, target-only behavior, and default learning notes. | Spec R1-R63; test spec T1-T9, T11-T12. | `python tests/validate_skills.py`; stale-text search; prompt line count. |
| `README.md` | Updated the editor table row and detail section to describe source-language plus companion-language output. | Public documentation would otherwise advertise the old Chinese/English default. | Spec compatibility/migration section; test spec T13. | `python tests/check_readme_sync.py`; stale-text search. |
| `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/post-change-evidence.md` | Recorded final prompt-contract evidence, scenario-class comparison, line counts, and validation evidence. | Required to prove the optimized prompt aligns with the same scenario classes captured at baseline. | Spec R57-R58, R67; test spec T11. | M3 validation; manual evidence review. |
| `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/change.yaml` | Tracks source artifacts, milestone state, validation, reviews, and open findings through final explain-change closeout. | Keeps change-local lifecycle metadata current for the workflow. | Plan milestones; review outcomes. | Manual metadata review; validation commands listed below. |
| `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/review-log.md` | Indexes proposal/spec/architecture/plan/code review outcomes through M3 R2. | Keeps formal review evidence discoverable. | Workflow review recording rules. | Code-review records. |
| `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/review-resolution.md` | Records closure of the proposal lifecycle finding and M3 stale-handoff finding. | Material findings must have final dispositions before downstream closeout. | Code-review M3 R1; proposal-review R2. | Code-review M3 R2 accepted the fix; targeted validation passed. |
| `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/reviews/*.md` | Added review records for lifecycle gates and M1-M3 code reviews. | Formal review results must be durable and indexed. | Proposal/spec/architecture/plan/code-review skills. | Review artifacts and review log. |
| `docs/plans/2026-06-16-editor-source-plus-companion-language-optimization.md` | Tracks milestone state, validation notes, decisions, surprises, and current handoff through final closeout. | The active plan is the source for milestone state and next-stage routing. | Plan and code-review handoff requirements. | Plan/index consistency checks. |
| `docs/plan.md` | Updates the active plan index as the lifecycle moves from implementation to final closeout and then verify. | Prevents stale project-level routing. | Workflow plan index convention. | Manual index check. |
| `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/explain-change.md` | This final rationale explains the complete change from proposal through implementation and review. | Required before final verification so reviewers do not have to reconstruct why files changed. | Explain-change skill; active plan final closeout. | This closeout plus validation below. |

## Tests Added Or Changed

- T1 checks the portable skill contract: `name: editor`, English description, `$ARGUMENTS`, and `## Output Format`.
- T2 checks that the description triggers the skill without encoding execution policy.
- T3 checks non-English source defaults to source language plus English.
- T4 checks English-source fallback and mixed-language instruction resolution.
- T5 checks explicit target-language override, multi-target output, and target-equals-source deduplication.
- T6 checks target-only output and note suppression are not conflated.
- T7 checks learning notes remain default, compact, anchored, and non-padded.
- T8 checks integrity outranks misleading transformation requests, including explicit target and no-notes constraints.
- T9 checks the compact prompt contract and removal of stale Chinese + English cross-check text.
- T10 checks the editor eval fixture covers required behavior scenarios.
- T11 checks baseline and post-change evidence.
- T12 checks repository boundaries and deterministic validation remain unchanged.
- T13 checks README and migration wording.
- T14 checks security and privacy boundaries in prompt/eval examples.

The test level is appropriate for this repository because `editor` is a portable prompt skill. There is no live model harness in scope; behavioral proof is reviewer-visible eval fixture coverage plus baseline/post-change prompt evidence and deterministic repository validation.

## Validation Evidence Available Before Final Verify

Validation has been run repeatedly through planning, implementation, review, and review-resolution. The latest relevant evidence before final verify includes:

- `python tests/validate_skills.py`: passed with the existing non-blocking grandfathered-evals warning for unrelated skills.
- `python -m unittest discover tests`: passed, 31 tests.
- `python tests/check_readme_sync.py`: passed.
- `git diff --check`: passed.
- `wc -l skills/editor/SKILL.md tests/evals/skills/editor/cases.yaml`: final prompt is 117 lines; eval fixture is 274 lines.
- Stale hardcoded Chinese + English default / hidden cross-check search: passed for `skills/editor/SKILL.md` and `README.md`.
- Stale active handoff search: passed for `explain-change.md`, `review-resolution.md`, `change.yaml`, the active plan, and `docs/plan.md`.

Hosted CI status has not been observed in this stage. Final `verify` still owns branch-ready evidence.

## Review Resolution Summary

Review-resolution is closed at `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/review-resolution.md`.

- Accepted/closed findings: 2
- Rejected findings: 0
- Deferred findings: 0
- Partially accepted findings: 0
- Needs decision: 0

`F-PROP-EDITOR-SOURCE-COMPANION-001` was closed by proposal-review R3 after the proposal lifecycle sections were synchronized. `F-CODE-EDITOR-SOURCE-COMPANION-M3-001` was closed by code-review M3 R2 after `explain-change.md` stopped routing readers back to M1 and accurately described the M3/final-closeout state.

## Alternatives Rejected

- Keep hardcoded Chinese + English default: rejected because it overfits bilingual Chinese/English workflows and fails for non-Chinese, non-English source text.
- Source-language only by default: rejected because the editor skill also serves translation workflows and the accepted direction asked for one companion language.
- Keep exhaustive learning-note and output-template rules: rejected because they consumed too much prompt weight and made behavior harder to maintain.
- Move all learning guidance to a separate reference file: rejected for this slice because learning notes are default behavior and the compact in-body rules are small enough.
- Add runtime validators, tools, scripts, preference storage, or live model CI: rejected as out of scope for a prompt-contract optimization.
- Create a canonical architecture artifact or ADR: rejected after architecture review approved the no-runtime-impact rationale.

## Scope Control

This change preserves these non-goals:

- No weakening of fidelity, restraint, meaning preservation, integrity checks, or unsupported-certainty rules.
- No removal of learning notes.
- No shift toward teaching as the primary deliverable.
- No live model CI, scripts, tool integrations, validator changes, or preference storage.
- No unrelated skill optimization.
- No guarantee of expert quality for every possible source language beyond bounded eval evidence.
- No branch-ready, PR-ready, CI-final, or final verification claim in this artifact.

## Risks And Follow-Ups

- The final proof remains prompt-contract and fixture evidence, not live model output. This is consistent with the repository's deterministic validation model, but final verify should still check artifact-code-test coherence.
- Broad language intake is best-effort. The prompt and evidence avoid claiming equal expert translation quality across all languages.
- The English-source fallback uses Chinese when no clearly non-English instruction language exists. A future proposal could add project-level or user-level companion-language configuration.
- Existing unrelated validator warning remains: grandfathered skills without eval fixtures. It is non-blocking and outside this change.

## Current Handoff

Final explain-change closeout is complete. The next stage is `verify`.

This artifact does not claim final verification, branch readiness, PR readiness, hosted CI success, or final lifecycle completion.
