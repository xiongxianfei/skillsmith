# Explain Change: Editor Expert Quality Optimization

## Status

complete

## Summary

This change replaces the `editor` skill's fixed three-stage report with an expert editing and translation workflow. The new prompt edits source text with fidelity and restraint, separates instruction/source/target language roles, defaults visible output to Chinese + English, honors explicit target-language requests, adds notes only when requested, and refuses misleading transformations.

The change is intentionally prompt-only. It does not add runtime tools, generated prompt assets, live-model CI, installer behavior, or repository-wide validator changes.

## Problem

The prior `editor` prompt always returned optimized text, a `Why` explanation, a quality assessment, and Chinese/English output. That was predictable, but it made simple edits look like report generation and increased the risk of unnecessary transformation. It also lacked explicit language-role separation, which made mixed inputs such as Chinese instructions with English source text harder to specify and test.

The accepted proposal reframed the skill around expert editorial judgment: preserve meaning first, improve only what helps, route response framing by instruction language, edit source text in the source language, and use bilingual rendering as a fidelity check.

## Decision Trail

| Decision point | Outcome |
|---|---|
| Proposal option selected | Option 3: expert persona plus concrete guardrails and evals. Persona-only prompting was rejected as too weak; the fixed three-stage report was rejected as too verbose. |
| Proposal scope | Optimize only `editor`; supersede the 2026-05-25 editor path; keep pure-prompt boundaries. |
| Key requirements | R1-R6 keep identity and discovery valid; R7-R30 define expert editing, fidelity, restraint, role separation, source-language editing, ambiguity, terminology, and integrity; R31-R38 define modes, target override, non-CN/EN handling, and cross-checking; R39-R42 define copyable concise output and line-count limit; R43-R49 define eval/evidence, validation, and scope controls. |
| Architecture decision | No new component. Runtime behavior remains in `skills/editor/SKILL.md`; eval evidence remains in `tests/evals/skills/editor/cases.yaml`; change evidence remains under `docs/changes/2026-05-26-editor-expert-quality-optimization/`. |
| Plan sequencing | M1 eval fixture and baseline evidence before prompt edits; M2 prompt and README implementation; M3 post-change evidence and lifecycle validation. |
| Review outcome | M1 clean; M2 required one template fix and then closed; M3 required one lifecycle text fix and then closed. |

## Diff Rationale By Area

| File | Change | Reason | Source artifact | Test/evidence |
|---|---|---|---|---|
| `skills/editor/SKILL.md` | Replaced the fixed three-stage prompt with expert editing standard, non-negotiables, role-separation workflow, target-language handling, cross-checking, and concise output templates. | Implements the approved editor behavior contract and removes default assessment/`Why` report output. | Spec R1-R42; architecture sections 4-8; plan M2. | `python tests/validate_skills.py`; `wc -l` = 126; M2 code reviews. |
| `tests/evals/skills/editor/cases.yaml` | Replaced stale fixed-report scenarios with 13 expert-quality scenarios. | Makes the new behavior reviewable, including mixed-language directions, fidelity drift, explicit target override, code-switching, non-CN/EN source handling, notes gating, ambiguity, and integrity misuse. | Spec R43-R44; test spec T13. | `python tests/validate_skills.py`; `python -m unittest tests/test_eval_fixtures.py`; baseline/post-change evidence. |
| `README.md` | Updated the `editor` table row and detail section from 3-phase bilingual report to expert editing/translation with default CN+EN and explicit target overrides. | README mirrored the old public output contract and needed to match the new skill behavior. | Spec compatibility section; plan M2. | `python tests/check_readme_sync.py`. |
| `docs/proposals/2026-05-25-editor-skill-optimization.md` | Marked superseded. | Prevents the old fixed three-stage proposal from remaining an active competing contract. | Accepted 2026-05-26 proposal supersession section. | Code-review lifecycle checks. |
| `specs/editor-skill-optimization.md` | Marked superseded. | Prevents stale requirements from driving downstream review or implementation. | Accepted 2026-05-26 proposal/spec. | Code-review lifecycle checks. |
| `docs/plans/2026-05-25-editor-skill-optimization.md` | Marked superseded. | Keeps the active workflow on the 2026-05-26 expert-quality plan. | Plan supersession decision. | `docs/plan.md` active index. |
| `docs/changes/2026-05-25-editor-skill-optimization/review-log.md` | Redirected the old review path to the superseding change. | Avoids continuing unresolved work on the old editor path. | Proposal supersession section. | Review-log inspection. |
| `docs/proposals/2026-05-26-editor-expert-quality-optimization.md` | Added the accepted expert-quality proposal with language-role model and target override contract. | Establishes the decision basis before spec and implementation. | Proposal lifecycle. | Proposal reviews R1-R5. |
| `specs/editor-expert-quality-optimization.md` | Added the normative behavior contract for the new editor skill. | Defines observable requirements for prompt behavior, output templates, compatibility, safety, validation, and evidence. | Spec lifecycle. | Spec reviews R1-R4. |
| `docs/architecture/system/architecture.md` and diagrams | Added architecture package and workflow design. | Documents that the change remains prompt-only and records the language-role/cross-check workflow. | Architecture lifecycle. | Architecture reviews R1-R2. |
| `docs/plans/2026-05-26-editor-expert-quality-optimization.md` | Added and maintained the active milestone plan. | Sequenced baseline evidence before prompt edits and tracked M1-M3 review/closeout state. | Plan lifecycle. | Plan review R1; code reviews M1-M3. |
| `specs/editor-expert-quality-optimization.test.md` | Added test specification mapping requirements to deterministic and manual proof. | Defines how eval fixtures, baseline/post-change evidence, and validation commands prove the prompt-only change. | Test-spec lifecycle. | Test-spec approval R1. |
| `docs/changes/2026-05-26-editor-expert-quality-optimization/baseline-evidence.md` | Recorded baseline behavior before prompt edits. | Proves the old prompt behavior and the gaps the change is meant to fix. | Spec R45; test spec T15; plan M1. | Code-review M1. |
| `docs/changes/2026-05-26-editor-expert-quality-optimization/post-change-evidence.md` | Recorded post-change static evidence against the same scenario surface. | Provides reviewer-visible evidence that the optimized prompt addresses the baseline gaps without live-model CI. | Spec R46; test spec T16; plan M3. | Code-review M3. |
| `docs/changes/2026-05-26-editor-expert-quality-optimization/change.yaml`, `review-log.md`, `review-resolution.md`, review records | Added lifecycle metadata, review records, and finding dispositions. | Keeps proposal/spec/architecture/plan/test/implementation/review state auditable. | Workflow and review skills. | Code reviews R1/R2 for M1-M3. |
| `docs/plan.md` | Updated active plan index to point to the new expert-quality workflow and later final closeout. | Prevents the old editor plan from appearing active and routes the next stage correctly. | Plan and code-review handoff rules. | Code-review M3 R2. |
| `editor_language_role_separation_workflow.svg` | Added/kept the user-provided reference workflow asset. | Captures the reference design that informed the architecture workflow. | Architecture source artifact. | Architecture review. |

## Tests Added Or Changed

| Test/proof ID | Level | What it proves | Why this level fits |
|---|---|---|---|
| T1 | integration | `editor` remains a valid pure Markdown skill with `name: editor`, `$ARGUMENTS`, and `## Output Format`. | Repository validation can prove skill-file structure deterministically. |
| T2-T3 | manual contract | Prompt advertises expert behavior and includes role-separation workflow. | Prompt behavior is a Markdown contract, so static inspection is the useful proof. |
| T4-T12 | manual/eval fixture | Default bilingual output, restraint, explicit target override, fidelity, mixed-language role separation, non-CN/EN behavior, notes gating, and integrity refusal. | These are prompt-behavior scenarios, captured in reviewer-readable eval fixtures and evidence rather than live CI. |
| T13 | integration | Eval fixture contains the required scenario classes. | Fixture shape is deterministically validated by existing tests. |
| T14 | smoke | Full local validation, README sync, diff hygiene, prompt line count, and scope control. | Confirms the repository remains valid without runtime or validator changes. |
| T15 | manual | Baseline evidence existed before prompt edits. | Ordering is workflow evidence, not executable behavior. |
| T16 | manual | Post-change evidence compares against the same scenario classes as baseline. | The skill has no runtime integration; reviewer-visible evidence is the approved proof layer. |

No new validator logic was added. That was deliberate: the approved scope said repository-wide validator changes were out of scope unless the existing eval-fixture path could not represent the change.

## Validation Evidence Available Before Final Verify

The following local commands have passed during implementation and code review:

- `python tests/validate_skills.py`
  - Passed with the existing non-blocking grandfathered-evals warning for unrelated skills: `communicator`, `doctor`, `email-drafter`, `fitness-coach`, `journaling`, `language-tutor`, `nvc`, `oscp-coach`, `study-planner`.
- `python -m unittest tests/test_eval_fixtures.py`
  - Passed during M1, 9 tests OK.
- `python -m unittest discover tests`
  - Passed during M2/M3 and review reruns, 31 tests OK.
- `python tests/check_readme_sync.py`
  - Passed after README changes.
- `git diff --check`
  - Passed after implementation and review metadata updates.
- `wc -l skills/editor/SKILL.md`
  - Returned 126 lines after the final prompt update, below the 500-line requirement.

No hosted CI result is claimed here. Final verification remains a downstream stage.

## Review Resolution Summary

Review-resolution artifact: `docs/changes/2026-05-26-editor-expert-quality-optimization/review-resolution.md`.

Material findings disposition:

- Proposal findings: 3 total, all closed by proposal review R4/R5.
- Spec findings: 3 total, all closed by spec review R2/R4.
- Architecture findings: 1 total, closed by architecture review R2.
- Code-review findings: 2 total, both closed by rerun reviews.

The two code-review findings were:

- `F-CODE-EDITOR-M2-001`: note-bearing and integrity templates needed explicit target-language block repetition. Closed by code-review M2 R2.
- `F-CODE-EDITOR-M3-001`: active plan readiness/outcome text still referenced the completed M2 rerun. Closed by code-review M3 R2.

`review-resolution.md` is closed and records no open `needs-decision` items.

## Alternatives Rejected

- Keep the fixed three-stage editor: rejected because it preserved the report-generator behavior that caused overproduction.
- Add only a stronger expert persona: rejected because weaker models may treat "expert" as permission to rewrite more heavily.
- Split `editor` into separate proofreading, rewriting, and translation skills: deferred because it would redesign the catalog rather than optimize the existing skill.
- Add live model CI: rejected by scope and spec; prompt behavior is covered by eval fixtures and manual evidence instead.
- Add repository-wide validator changes: rejected because the existing eval-fixture path represented the behavior adequately.
- Restore assessment/default `Why` sections: rejected because those are the core default-output bloat this change removes.

## Scope Control

Preserved non-goals:

- No prompt optimization for skills other than `editor`.
- No changes to high-risk skill behavior such as `doctor` or `oscp-coach`.
- No runtime tools, scripts, generated prompt assets, external services, or installer changes.
- No live-model CI and no network-dependent validation.
- No repository-wide validator architecture changes.
- No claim that all source languages receive equal expert editing quality; all-language support is an intake rule.

The old 2026-05-25 editor path was marked superseded rather than continued in parallel.

## Risks And Follow-Ups

- Weak models may still fuse instruction/source roles on mixed-language inputs. Mitigation: eval scenarios and post-change evidence cover both Chinese-instruction/English-source and English-instruction/Chinese-source cases.
- Default Chinese + English output may be more output than trivial requests need. Mitigation: explicit target-language-only requests are honored and default assessment/`Why` sections are removed.
- Single-target visible output has weaker visible cross-checking. Mitigation: the prompt instructs internal Chinese + English rendering where practical before displaying only the requested target.
- No live weakest-model smoke was run. This is recorded in `post-change-evidence.md`; final verification should carry that limitation forward rather than implying model-level proof.
- Final verify and PR handoff remain pending. This artifact does not claim branch readiness, PR readiness, hosted CI success, or final verification.

## Current Handoff

All implementation milestones M1-M3 are closed and all material review findings are closed. This explanation completes the durable rationale step and is ready for the next lifecycle stage: `verify`.
