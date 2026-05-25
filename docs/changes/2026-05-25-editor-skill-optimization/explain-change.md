# Explain Change: Editor skill optimization

## Summary

This change optimizes the existing `editor` skill with a baseline-first process. The old prompt forced every request through deep text optimization, language-quality assessment, and Chinese-English bilingual translation. The new prompt keeps the skill portable and multilingual, but makes output conditional on the user's actual intent: simple edits return edited text, targeted translation returns the requested language, notes are conditional, and misleading rewrites hit an explicit integrity boundary.

The implementation also adds the required eval fixture and reviewer-visible baseline/post-change evidence for the material skill behavior change.

Current lifecycle state: all implementation milestones M1-M3 are closed after clean code review. Final verification has not been run yet.

## Problem

The proposal identified that `skills/editor/SKILL.md` was useful but over-prescriptive. A quick proofreading request, PR description polish, or targeted Russian translation could be routed into a long fixed report with bilingual Chinese-English output even when the user did not ask for analysis or translation.

The repository constitution requires materially changed skill prompts to include eval evidence and to prove current behavior before changing it. Because this work changes output contract, workflow, and safety behavior, it needed proposal, spec, plan, test spec, implementation evidence, and code review.

## Decision trail

| Decision point | Outcome | Why |
|---|---|---|
| Proposal option | Optimize `editor` alone with baseline-first evals | Low-risk skill, useful first proof of the quality process, avoids mixing high-risk safety work into the first slice. |
| Proposal review | Added targeted Russian translation scenario | Translation was in scope, so it needed direct eval coverage instead of relying on editing scenarios. |
| Spec review | Bounded unsupported target languages | Chinese, English, and Russian remain the accepted translation contract; other languages are best effort and outside this slice's acceptance surface. |
| Architecture | No architecture artifact required | No runtime components, data flow, persistence, dependencies, CI services, or installer behavior changed. |
| Plan | Three milestones | M1 evidence before edits, M2 prompt optimization, M3 post-change evidence and final implementation validation. |
| Test strategy | Deterministic checks plus manual prompt-contract evidence | Live model CI is out of scope; prompt behavior is recorded in reviewer-visible evidence. |

Key requirements satisfied:

- R1-R4: keep `editor`, pure prompt metadata, `$ARGUMENTS`, and conditional `## Output Format`.
- R5-R18: support proofreading, rewriting, targeted translation, conditional notes, ambiguous input, and integrity-boundary handling.
- R19-R20: keep the prompt concise and under 500 lines.
- R21-R25: add eval fixture, baseline evidence, and post-change evidence.
- R26-R28: no live model CI, no validator behavior change, no other skill optimization.

## Diff rationale by area

| File | Change | Reason | Source artifact | Test/evidence |
|---|---|---|---|---|
| `docs/proposals/2026-05-25-editor-skill-optimization.md` | Records accepted direction and four scenarios. | Establishes the low-risk editor-only scope and baseline-first approach. | Proposal review R2 | Review log; proposal-review records. |
| `specs/editor-skill-optimization.md` | Defines the observable output contract, safety boundary, acceptance criteria, and non-goals. | Converts the proposal into testable requirements for the prompt change. | Spec review R2 | Requirements R1-R28; AC1-AC15. |
| `specs/editor-skill-optimization.test.md` | Maps requirements to T1-T12 proof surfaces. | Makes prompt evidence, validation commands, line count, and scope checks reviewable. | Test-spec approval R1 | M1-M3 evidence and validation. |
| `docs/plans/2026-05-25-editor-skill-optimization.md` | Sequences M1-M3 and tracks lifecycle state. | Keeps implementation slices reviewable and prevents prompt edits before baseline evidence. | Plan review R1 | Code-review M1-M3. |
| `tests/evals/skills/editor/cases.yaml` | Adds four eval scenarios: proofreading, PR description, integrity misuse, Russian translation. | Required eval fixture for a material `editor` prompt change. | R21-R23, T1 | `python tests/validate_skills.py`; `python -m unittest tests/test_eval_fixtures.py`. |
| `docs/changes/2026-05-25-editor-skill-optimization/baseline-evidence.md` | Records current prompt-contract behavior before editing `SKILL.md`. | Proves the baseline over-production problem before optimization. | R24, T2 | M1 code review. |
| `skills/editor/SKILL.md` | Replaces the fixed three-stage Chinese-language workflow with concise conditional modes. | Satisfies the new output contract while keeping the skill portable and shorter. | R1-R20, AC5-AC11 | M2 code review; validator; line count 74. |
| `docs/changes/2026-05-25-editor-skill-optimization/post-change-evidence.md` | Compares optimized behavior against the same scenarios and supplemental edge cases. | Provides the post-change proof required before final implementation review. | R25, T5-T12 | M3 code review. |
| `docs/changes/2026-05-25-editor-skill-optimization/review-resolution.md` | Records accepted proposal/spec review finding resolutions. | Keeps material review finding dispositions durable without changing implementation scope. | Proposal-review R1; spec-review R1 | Proposal-review R2; spec-review R2. |
| `docs/changes/2026-05-25-editor-skill-optimization/reviews/*.md` | Records proposal, spec, plan, test-spec, and code-review outcomes. | Maintains lifecycle evidence and review handoff history. | Workflow requirements | Review log. |
| `docs/changes/2026-05-25-editor-skill-optimization/change.yaml`, `review-log.md`, `docs/plan.md` | Tracks active stage, validation evidence, and next handoff. | Keeps workflow state inspectable. | Active plan | Updated at each milestone/review. |

## Skill behavior rationale

The edited `skills/editor/SKILL.md` keeps the existing trigger metadata and command compatibility, but changes the body:

- `## Input` keeps `$ARGUMENTS` as the text plus user instruction surface.
- `## Workflow` tells the model to identify whether the request is proofreading, rewriting, translation, explanation, or ambiguous pasted text.
- Default output is narrow: corrected text for proofreading, rewritten text for PR/docs/release-note edits, requested target language for translation.
- `## Integrity Boundaries` prevents deceptive rewrites such as implying customer approval that did not happen.
- `## Translation Boundaries` keeps Chinese, English, and Russian as direct support and treats other languages as best effort outside the acceptance contract.
- `## Output Format` lists conditional sections instead of forcing every response into the old three-stage report.

This directly addresses AC5-AC8 while preserving AC9-AC11.

## Tests and proof

| Test/proof ID | Surface | What it proves |
|---|---|---|
| T1 | `tests/evals/skills/editor/cases.yaml` plus validator/unit tests | The material prompt change has valid scenarios for normal, indirect-trigger, misuse, and targeted translation coverage. |
| T2 | `baseline-evidence.md` | Baseline behavior was recorded before prompt edits. |
| T3-T4 | `skills/editor/SKILL.md` plus validator/manual review | Metadata, `$ARGUMENTS`, pure prompt boundary, and conditional output format are preserved. |
| T5-T8 | `post-change-evidence.md` | The four fixture scenarios compare baseline and optimized prompt behavior. |
| T9-T10 | `post-change-evidence.md` | Requested notes, bilingual output, ambiguity, ambiguous pasted text, and unsupported-language behavior are covered. |
| T11 | Diff review | No unrelated skills, live model CI, validator behavior, installer behavior, tools, dependencies, or generated assets changed. |
| T12 | Validation commands and line count | Final implementation evidence exists, validation passes, and prompt length is shorter. |

## Validation evidence before final verify

Validation recorded during implementation and code review:

- `python tests/validate_skills.py` passed. The remaining warning is for other grandfathered skills without eval fixtures; `editor` is no longer in that warning set.
- `python -m unittest tests/test_eval_fixtures.py` passed after M1.
- `python -m unittest discover tests` passed after M2/M3 and during review.
- `python tests/check_readme_sync.py` passed because the helper exists in this branch.
- `git diff --check` and milestone-specific `git diff --check HEAD~1..HEAD` checks passed.
- `wc -l skills/editor/SKILL.md` reported 74 lines, down from the 92-line baseline.

Hosted CI status is not claimed here.

## Review resolution summary

Material findings resolved before implementation:

- `F-PROP-EDITOR-001`: accepted; added direct targeted Russian translation coverage.
- `F-SPEC-EDITOR-001`: accepted; bounded unsupported-language behavior outside Chinese, English, and Russian.
- `F-SPEC-EDITOR-002`: accepted; corrected downstream artifact order so plan and plan-review came before test-spec.

See `docs/changes/2026-05-25-editor-skill-optimization/review-resolution.md`.

Implementation reviews:

- `code-review-m1-r1`: clean-with-notes; M1 closed.
- `code-review-m2-r1`: clean-with-notes; M2 closed.
- `code-review-m3-r1`: clean-with-notes; M3 closed.

No implementation code-review findings required review-resolution.

## Alternatives rejected

- Do nothing: rejected because the over-production behavior would remain.
- Rewrite from taste without baseline evidence: rejected because reviewers could not prove improvement.
- Optimize a high-risk skill at the same time: rejected to avoid mixing prompt concision with high-risk safety policy.
- Convert `editor` into engineer-only editing: rejected because the existing general editing and translation value should be preserved.
- Add live model CI: rejected by scope and test strategy; manual prompt-contract evidence is the approved proof surface.
- Change validator behavior: rejected as unnecessary because the existing eval-fixture path represented this material skill change.

## Scope control

Preserved non-goals:

- No other skill prompt was optimized.
- No `doctor`, `oscp-coach`, or other high-risk skill was changed.
- No runtime tool, script, dependency, generated prompt asset, installer behavior, or live model CI was added.
- Skill name and install compatibility remain unchanged.
- Translation remains in scope for Chinese, English, and Russian instead of being removed.

## Risks and follow-ups

Residual risk: prompt behavior evidence is contract-based rather than live model output. This is intentional and matches the approved test spec, but reviewers should treat it as prompt evidence, not hosted runtime proof.

Follow-up stage: `verify` should independently check artifact-code-test coherence, validation commands, lifecycle state, and PR readiness prerequisites. This explanation does not claim final verification, branch readiness, PR readiness, or hosted CI success.
