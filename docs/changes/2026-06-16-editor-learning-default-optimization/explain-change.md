# Explain Change: Editor Learning Default Optimization

## Status

closed for explain-change

## Summary

This change updates the `editor` skill so polishing and translation remain the primary deliverables, and a structured `Learning notes` block appears by default after those deliverables unless the user explicitly asks for output-only delivery or no explanation.

The work reverses the prior notes-on-request default while preserving the expert editor contract: fidelity, restraint, target-language overrides, response-language framing, copyable output, and integrity boundaries. It also adds reviewer-visible eval coverage, baseline evidence, post-change evidence, and lifecycle records for the full change.

## Problem

The previous `editor` prompt produced useful polished and translated text, but it deliberately suppressed notes unless the user explicitly requested explanation. That kept output minimal, but it did not support the new product direction: the user should learn from edits by default.

The risk was adding teaching in a way that created noise, generic commentary, or over-editing. The accepted direction was to keep deliverables first, add short concrete learning notes after the deliverables, make the notes suppressible by explicit output-only requests, and prevent the model from padding notes or inventing edits just to teach.

## Decision Trail

| Decision point | Outcome | Source |
| --- | --- | --- |
| Proposal direction | Adopt default per-change teaching notes after the deliverable; reject opt-in-only notes, generic explanation paragraphs, interleaved notes, and exhaustive teaching. | `docs/proposals/2026-06-16-editor-learning-default-optimization.md` |
| Trigger scope | Keep the skill identity as expert editor and translator; teaching is from edits to shared text, not standalone writing coaching. | Proposal review and spec R3-R5 |
| Suppression rule | Suppress only on explicit output-only/no-explanation phrasing; ambiguous brevity keeps concise notes. | Spec R26-R29 |
| Architecture | No separate architecture artifact; pure prompt, eval fixture, and evidence slice only. | Plan-review R1 and test spec |
| Implementation sequence | M1 eval/baseline first, M2 prompt/README implementation, M3 post-change evidence/validation. | `docs/plans/2026-06-16-editor-learning-default-optimization.md` |
| Review outcome | M1, M2, and M3 code reviews all closed `clean-with-notes` with no material findings. | `docs/changes/2026-06-16-editor-learning-default-optimization/review-log.md` |

Key requirements implemented:

- R1-R2: preserve expert editor quality and pure-prompt boundary.
- R3-R5: editor/translator identity, learning from edits, no standalone coaching trigger.
- R6-R14: default post-deliverable `Learning notes`, labels, anchoring, response-language-only notes.
- R15-R25: fidelity, no meaning drift, no extra edits, uncapped-but-scannable notes, trivial/already-good/brittle fallback handling.
- R26-R31: explicit suppression, ambiguous fallback, explicit target-language behavior.
- R32-R36: integrity-boundary behavior and removal of obsolete notes-on-request prompt text.
- R37-R38: baseline and post-change evidence over the required scenario classes.

## Diff Rationale By Area

| File | Change | Reason | Source artifact | Test/evidence |
| --- | --- | --- | --- | --- |
| `skills/editor/SKILL.md` | Replaced the old notes-on-request contract with default `Learning notes`; added explicit suppression examples, ambiguous brevity handling, anchoring, fallback notes, no-padding rules, scannable longer-note formatting, response-language labels, target-language templates, and integrity-boundary note behavior. | Implements the accepted learning-default contract while preserving the expert editor and translator behavior. | Spec R1-R36; proposal recommended direction. | M2 code review, amendment validation, `python tests/validate_skills.py`, prompt line count. |
| `README.md` | Updated the editor table row and detail section to mention structured learning notes by default and no-notes overrides. | README mirrors public skill behavior and would otherwise advertise the old output contract. | Plan M2 aligned-surface audit. | `python tests/check_readme_sync.py`; M2 code review. |
| `tests/evals/skills/editor/cases.yaml` | Updated editor eval scenarios from notes-on-request expectations to learning-default expectations. | The proof surface had to express the accepted behavior before prompt implementation. | Spec R38; test spec required scenario IDs. | M1 code review; `python tests/validate_skills.py`. |
| `docs/changes/2026-06-16-editor-learning-default-optimization/baseline-evidence.md` | Recorded the old prompt behavior before editing `skills/editor/SKILL.md`. | Required baseline-first evidence and showed baseline learning value was absent by design. | Spec R37; test spec T3. | M1 code review; direct no-prompt-diff check. |
| `docs/changes/2026-06-16-editor-learning-default-optimization/post-change-evidence.md` | Recorded post-change prompt-contract evidence for the same scenario classes and compared learning value, bloat, over-editing, fidelity, suppression, labels, target-language behavior, and integrity boundaries. | Required after-change evidence without live model CI. | Spec R37-R38; test spec T14. | M3 code review; direct scenario-ID coverage check. |
| `docs/plans/2026-06-16-editor-learning-default-optimization.md` | Tracked milestone state, validation, aligned-surface audits, review outcomes, and final closeout handoff. | The workflow requires milestone-aware state and reviewable validation history. | Plan skill and active plan. | M1-M3 code reviews. |
| `docs/changes/2026-06-16-editor-learning-default-optimization/change.yaml` | Recorded artifact paths, validation evidence, review records, current lifecycle state, and no open findings. | Keeps change metadata auditable. | Implement/code-review workflow. | YAML parse checks during implementation/review. |
| `docs/changes/2026-06-16-editor-learning-default-optimization/review-log.md` and `reviews/*` | Recorded proposal/spec/plan/test-spec/code-review outcomes, including clean M1-M3 code reviews. | Formal lifecycle reviews must be durable and indexed. | Code-review skill recording rules. | Review receipts and review log. |
| `docs/plan.md` | Updated the repository-level plan index as the milestone state advanced. | Keeps the active plan discoverable and current. | Plan update requirements. | M1-M3 reviews. |

## Tests Added Or Changed

| Test/evidence item | What it proves | Why this level is appropriate |
| --- | --- | --- |
| `tests/evals/skills/editor/cases.yaml` scenario IDs | Covers default learning notes, principle-not-report, explicit target language, explicit suppression, ambiguous brevity, mixed-language framing, trivial-only fallback, already-good restraint, brittle-rule handling, integrity boundary, Chinese suppression, no-source boundary, and non-English source/translation continuity. | The repository uses reviewer-readable eval fixtures for prompt behavior rather than live model CI. |
| `baseline-evidence.md` | Before the prompt edit, ordinary requests had no default learning value because notes were opt-in. | Required by R37/T3 to make the before/after learning claim reviewable. |
| `post-change-evidence.md` | After the prompt edit, the prompt contract provides default learning value while bounding bloat, over-editing, and fidelity risk. | Required by R37/T14 and allowed by the test spec's manual evidence strategy. |
| `python tests/validate_skills.py` | Validates skill structure and eval fixture schema. | Required repository validation for skills. |
| `python -m unittest discover tests` | Runs the repository unit suite. | Broad deterministic smoke for changed docs/test surfaces. |
| `python tests/check_readme_sync.py` | Confirms README remains synchronized with skill metadata expectations. | Required because README mirrors the changed public editor behavior. |
| `git diff --check` | Guards whitespace and patch hygiene. | Required milestone validation. |
| `wc -l skills/editor/SKILL.md` | Records prompt size after adding learning rules. | Prompt-size smoke for portability and bloat risk. |

## Validation Evidence Available Before Final Verify

Validation has passed during implementation and review. The known warning is non-blocking and unrelated to this editor change: grandfathered skills without eval fixtures.

| Command/check | Latest recorded result |
| --- | --- |
| `python tests/validate_skills.py` | Passed with existing unrelated grandfathered-evals warning. |
| `python -m unittest discover tests` | Passed, 31 tests OK. |
| `python tests/check_readme_sync.py` | Passed. |
| `git diff --check` / commit-range diff checks | Passed. |
| `wc -l skills/editor/SKILL.md` | 188 lines. |
| Code review M1 R1 | `clean-with-notes`, no material findings. |
| Code review M2 R1 | `clean-with-notes`, no material findings. |
| Code review M3 R1 | `clean-with-notes`, no material findings. |

No hosted CI result or final `verify` result is claimed here.

## Review Resolution Summary

No implementation code-review material findings were opened. No implementation `review-resolution.md` is required.

Earlier spec-review findings were resolved before implementation:

- `F-SPEC-EDITOR-LEARNING-001`: default `Learning notes` block must appear for non-empty, non-suppressed requests, with a concrete fallback note when there is no substantive lesson.
- `F-SPEC-EDITOR-LEARNING-002`: substantive notes require concrete anchoring; fallback notes must still reference the concrete source condition, edit category, or integrity issue.

The durable review index is `docs/changes/2026-06-16-editor-learning-default-optimization/review-log.md`.

## Alternatives Rejected

| Alternative | Why rejected |
| --- | --- |
| Keep notes opt-in only | Fails the new default teaching goal. |
| Add a generic explanation paragraph | Produces low learning value and encourages vague commentary. |
| Interleave notes with deliverables | Hurts copyability and makes teaching interfere with the primary output. |
| Teach every edit exhaustively | Creates noise and incentivizes over-editing. |
| Add live model CI or new tooling | Out of scope for a pure prompt change; nondeterministic and unnecessary for this slice. |
| Create a standalone writing-coach identity | Broadens trigger scope beyond source-text editing and conflicts with the accepted direction. |

## Scope Control

The change intentionally does not:

- redesign the whole `editor` skill;
- weaken fidelity, restraint, target-language overrides, or integrity boundaries;
- add a default assessment, grading report, stage report, or default `Why` section;
- duplicate learning notes bilingually by default;
- add tools, scripts, generated assets, external services, dependencies, installer behavior, validator behavior, runtime behavior, or live model CI;
- expand unsupported-language guarantees beyond the existing source-intake and target-output contract;
- modify unrelated skills.

## Risks And Follow-Ups

| Risk | Current mitigation |
| --- | --- |
| Weak models may still miss or overproduce learning notes. | Prompt now gives explicit examples, scannable formatting, fallback-note rules, and no-padding/no-extra-edit constraints; post-change evidence records this as residual model-following risk. |
| Users may sometimes not want notes. | Explicit suppression phrases in English and Chinese remove the block; ambiguous brevity keeps notes concise rather than hidden. |
| Teaching could justify meaning drift. | Prompt explicitly subordinates notes to fidelity and integrity and forbids unsupported certainty, false approval, or false attribution. |
| Prompt complexity could grow over time. | Prompt line count is recorded during validation; future changes should keep the learning-note format scannable and fallback rules focused. |

## Current Handoff

All implementation milestones are closed by code review. The active plan is in the final closeout sequence. This explanation artifact is closed and ready for the next lifecycle stage: `verify`.

This does not claim final verification, branch readiness, PR readiness, hosted CI success, or merge readiness.
