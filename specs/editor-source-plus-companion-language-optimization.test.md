# Editor Source Plus Companion Language Optimization Test Spec

## Status

active

## Related spec and plan

- Spec: `specs/editor-source-plus-companion-language-optimization.md`
- Plan: `docs/plans/2026-06-16-editor-source-plus-companion-language-optimization.md`
- Architecture/ADRs: no canonical architecture or ADR artifact required; `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/reviews/architecture-review-r1.md` approved the no-impact architecture rationale.

## Testing strategy

Unit strategy: use existing Python unit tests for validator and README sync behavior. No new validator logic is planned, so unit coverage should remain unchanged unless implementation discovers a necessary validator update, which would require upstream scope review.

Integration strategy: use `python tests/validate_skills.py` to validate the edited `skills/editor/SKILL.md` and `tests/evals/skills/editor/cases.yaml` together. Use `python tests/check_readme_sync.py` to catch README frontmatter/table drift.

End-to-end strategy: no live model end-to-end tests are added. Behavioral proof is reviewer-visible eval evidence plus baseline/post-change scenario notes because this repository stores portable prompts and deterministic fixtures, not a live model harness.

Smoke strategy: run `python tests/validate_skills.py`, `python -m unittest discover tests`, `python tests/check_readme_sync.py`, `git diff --check`, and `wc -l skills/editor/SKILL.md` before handoff.

Manual strategy: reviewers inspect the editor prompt, eval fixture expected behaviors, baseline evidence, and post-change evidence for source-language defaults, companion-language resolution, learning-note behavior, integrity boundaries, prompt length, and removal of hidden cross-check rendering.

Contract strategy: verify that the skill remains a pure prompt skill with `name: editor`, English description, `$ARGUMENTS`, and `## Output Format`, and that no runtime, tool, installer, validator, CI, or architecture boundary changes are introduced.

Migration strategy: verify README wording and PR notes call out the visible default-output change from hardcoded Chinese + English to source language + companion language, while preserving existing Chinese + English behavior for Chinese sources and English-source fallback cases.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1 | T1 | contract | Confirms `name: editor` remains unchanged. |
| R2 | T1, T12 | contract | Confirms pure prompt boundary and no new runtime, tool, dependency, service, or CI live-model behavior. |
| R3 | T1 | contract | Confirms `$ARGUMENTS` remains in the body. |
| R4 | T1 | contract | Confirms `## Output Format` remains in the body. |
| R5 | T2 | manual | Description must identify expert editor, translator, and writing coach role. |
| R6 | T2 | manual | Description must include trigger contexts and casual asks. |
| R7 | T2 | manual | Description must not encode detailed execution policy. |
| R8 | T8, T9 | manual | Reviewer checks fidelity with restraint and integrity boundaries in prompt and evidence. |
| R9 | T9 | manual | Prompt must separate instruction, source, languages, framing, visible outputs, and companion language before composing. |
| R10 | T9 | manual | Prompt must treat instruction as tool direction, not source text. |
| R11 | T9 | manual | Prompt must treat source text as the edit/translation artifact even when it looks like an instruction. |
| R12 | T3, T10 | manual | Eval scenarios cover broad intake for non-English source text without quality overclaiming. |
| R13 | T3, T10 | manual | Eval scenarios cover default source-language plus one companion output. |
| R14 | T3, T10 | manual | Chinese, Russian, and Spanish cases cover English companion default for non-English sources. |
| R15 | T4, T10 | manual | English source with clearly non-English instruction uses instruction language as companion. |
| R16 | T4, T10 | manual | English source with no clear non-English instruction uses Chinese fallback. |
| R17 | T4, T10 | manual | English-source evals require no duplicate English + English output. |
| R18 | T4, T10 | manual | Mixed-language evals distinguish directive words from pasted source text. |
| R19 | T4, T10 | manual | Mixed directive words use first clearly identifiable non-English directive language, otherwise Chinese. |
| R20 | T4, T7, T10 | manual | Response framing follows clearly detectable instruction language. |
| R21 | T4, T10 | manual | Non-Chinese/non-English label localization is checked manually where practical. |
| R22 | T3, T5, T6, T10 | manual | Source-language block contains polished or preserved source text as requested. |
| R23 | T3, T5, T6, T10 | manual | Companion and target blocks translate the same resolved meaning. |
| R24 | T3, T9, T10 | manual | Prompt and evidence show edit-source-first, then translate. |
| R25 | T3, T5, T9, T10 | manual | Prompt and evidence show one resolved meaning rendered into visible blocks. |
| R26 | T3, T5, T8, T10 | manual | Evidence checks facts, uncertainty, tone, terms, logic, and formatting intent across visible blocks. |
| R27 | T9 | manual | Prompt inspection verifies no hidden Chinese + English cross-check requirement remains. |
| R28 | T3, T7, T9 | manual | Prompt inspection verifies base output shape. |
| R29 | T4, T7, T10 | manual | Labels use response framing language where practical. |
| R30 | T9, T10 | manual | Output format stays copyable Markdown-compatible plain text without emoji/decorative symbols. |
| R31 | T5, T10 | manual | Single explicit target returns polished source plus requested target unless target-only. |
| R32 | T5, T10 | manual | Multiple explicit targets return source plus each requested target. |
| R33 | T5, T10 | manual | Explicit target equal to source does not duplicate the language block. |
| R34 | T6, T10 | manual | Target-only omits the source-language deliverable block. |
| R35 | T6, T10 | manual | Target-only does not suppress notes by itself. |
| R36 | T6, T10 | manual | Target-only suppresses notes only with explicit note suppression. |
| R37 | T6, T10 | manual | Translation-only preserves meaning and tone without unnecessary source rewrite. |
| R38 | T7, T10 | manual | Learning notes appear by default after deliverables for non-suppressed requests. |
| R39 | T4, T7, T10 | manual | Learning notes use response framing language. |
| R40 | T7, T10 | manual | Substantive notes use concrete original-to-revised anchoring or equivalent reference. |
| R41 | T7, T10 | manual | Notes teach reusable principles rather than reporting edits. |
| R42 | T7, T10 | manual | Notes do not invent edits or alter meaning to create lessons. |
| R43 | T7, T10 | manual | Trivial mechanical fixes are skipped as full lessons unless recurring. |
| R44 | T7, T10 | manual | Trivial, already-clear, brittle-rule, and integrity-boundary cases use exactly one fallback note unless suppressed. |
| R45 | T7, T10 | manual | Fallback note pattern is equivalent to the approved concise pattern. |
| R46 | T7, T10 | manual | Notes remain concise and usually no more than three. |
| R47 | T7, T10 | manual | Long-source eval permits more than three genuinely useful notes. |
| R48 | T7, T10 | manual | Longer note sets are grouped by theme. |
| R49 | T6, T8, T10 | manual | Explicit note suppression removes learning notes block. |
| R50 | T7, T10 | manual | Ambiguous brevity cues do not suppress notes by themselves. |
| R51 | T8, T9 | manual | Prompt includes and evidence exercises the conflict hierarchy. |
| R52 | T8, T10 | manual | Integrity prevents misleading, false, deceptive, unsupported, or inconsistent edits. |
| R53 | T5, T6, T8, T10 | manual | Explicit constraints are honored unless they conflict with integrity or fidelity. |
| R54 | T8, T10 | manual | Integrity-boundary requests briefly refuse or redirect and offer accurate alternatives where possible. |
| R55 | T8, T10 | manual | Integrity alternatives use requested target languages where possible. |
| R56 | T8, T10 | manual | Integrity-boundary requests with note suppression omit learning notes. |
| R57 | T11 | manual | Post-change evidence compares prompt length and justifies any increase. |
| R58 | T11 | smoke | `wc -l skills/editor/SKILL.md` verifies the prompt stays under 500 lines. |
| R59 | T9 | manual | Prompt inspection verifies old Chinese + English default text is updated or replaced. |
| R60 | T9 | manual | Prompt inspection verifies hidden Chinese + English cross-check text is removed or replaced. |
| R61 | T9 | manual | Prompt inspection verifies fallback-note and template proliferation is compressed. |
| R62 | T12 | contract | Diff review confirms no repository-wide validator changes for this slice. |
| R63 | T12 | contract | Diff review confirms no live model calls are added to CI. |
| R64 | T10 | manual | Eval fixture covers required scenario classes. |
| R65 | T8, T10 | manual | Eval fixture covers integrity issue + explicit target + note suppression. |
| R66 | T11 | manual | Baseline evidence exists before prompt edit. |
| R67 | T11 | manual | Post-change evidence compares the same scenario classes used for baseline. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 | T3, T10 | Chinese source defaults to polished Chinese plus English and notes. |
| E2 | T3, T10 | Russian source defaults to polished Russian plus English and does not add Chinese. |
| E3 | T4, T10 | English source with English instruction avoids duplicate English and uses Chinese fallback. |
| E4 | T4, T10 | English source with Chinese instruction uses Chinese companion and framing. |
| E5 | T4, T10 | Mixed-language instruction resolves from directive words deterministically. |
| E6 | T5, T10 | Explicit French target overrides default companion. |
| E7 | T5, T10 | Explicit English and French targets add both target blocks. |
| E8 | T6, T10 | Target-only English translation keeps notes unless suppressed. |
| E9 | T6, T10 | Target-only plus explicit no-notes returns only the translation. |
| E10 | T7, T10 | Learning notes are concise but not hard-capped when many distinct lessons exist. |
| E11 | T8, T10 | Integrity outranks target-language and no-notes constraints. |

## Edge case coverage

| Edge case | Covered by | Notes |
| --- | --- | --- |
| EC1 | T3, T10 | Chinese instruction and Chinese source default. |
| EC2 | T3, T10 | English instruction and Chinese source with English framing. |
| EC3 | T3, T10 | Russian source with English instruction defaults to Russian + English. |
| EC4 | T3, T10 | Spanish source with best-effort quality caveat. |
| EC5 | T4, T10 | English source and English instruction uses Chinese fallback. |
| EC6 | T4, T10 | English source and Chinese instruction uses Chinese companion/framing. |
| EC7 | T4, T10 | Mixed directive words use first clear non-English directive language or Chinese fallback. |
| EC8 | T5, T10 | Explicit French target on English source. |
| EC9 | T5, T10 | Explicit English and French targets on Chinese source. |
| EC10 | T6, T10 | Target-only keeps notes unless notes are suppressed. |
| EC11 | T6, T10 | Target-only plus no notes suppresses notes. |
| EC12 | T5, T10 | Target equal to source does not duplicate a block. |
| EC13 | T7, T10 | Trivial typo does not create padded grammar teaching. |
| EC14 | T7, T10 | Already-clear text receives minimal editing and one fallback note at most. |
| EC15 | T7, T10 | Long source may exceed three notes when warranted and grouped. |
| EC16 | T8, T10 | Integrity conflict with explicit target and no-notes. |

## Test cases

### T1. Skill contract stays portable and addressable

- Covers: R1, R2, R3, R4
- Level: smoke
- Fixture/setup: edited `skills/editor/SKILL.md`
- Steps: run `python tests/validate_skills.py`; inspect `skills/editor/SKILL.md` frontmatter and body.
- Expected result: skill name remains `editor`, description is valid English, body includes `$ARGUMENTS`, body includes `## Output Format`, and the skill remains a Markdown prompt without tool permissions or runtime dependencies.
- Failure proves: the implementation broke the repository's skill contract or portability rules.
- Automation location: `python tests/validate_skills.py`; manual inspection of `skills/editor/SKILL.md`

### T2. Description is trigger-focused, not policy-heavy

- Covers: R5, R6, R7
- Level: manual
- Fixture/setup: edited `skills/editor/SKILL.md`
- Steps: inspect YAML `description`.
- Expected result: description identifies the skill as an expert editor, translator, and writing coach for polishing, proofreading, rewriting, translating, and learning from edits; includes contexts such as emails, PR descriptions, docs, release notes, messages, and casual edit/translate/improve requests; does not include the full default-language, fallback, output-template, or learning-note policy.
- Failure proves: skill selection metadata is too vague or overloaded with execution behavior.
- Automation location: manual review; `python tests/validate_skills.py` checks basic frontmatter validity only.

### T3. Non-English source defaults to source language plus English

- Covers: R12, R13, R14, R22, R23, R24, R25, R26, E1, E2, EC1, EC2, EC3, EC4
- Level: manual
- Fixture/setup: `tests/evals/skills/editor/cases.yaml`, `baseline-evidence.md`, and `post-change-evidence.md`
- Steps: add reviewer-visible eval cases for Chinese, Russian, and Spanish source text with no explicit target; record baseline and post-change expected behavior for visible language blocks, source fidelity, uncertainty preservation, and learning notes.
- Expected result: Chinese source returns polished Chinese + English; Russian source returns polished Russian + English and does not add Chinese; Spanish source returns polished Spanish + English while preserving the best-effort caveat; visible blocks preserve the same meaning and tone.
- Failure proves: the core default-language contract is missing, overfitted to Chinese, or not evidenced.
- Automation location: `tests/evals/skills/editor/cases.yaml` checked structurally by `python tests/validate_skills.py`; behavioral evidence is reviewer-visible manual evidence.

### T4. English source fallback and instruction-language resolution are deterministic

- Covers: R15, R16, R17, R18, R19, R20, R21, R29, R39, E3, E4, E5, EC5, EC6, EC7
- Level: manual
- Fixture/setup: `tests/evals/skills/editor/cases.yaml`, baseline and post-change evidence
- Steps: add cases for English source with English instruction, English source with Chinese instruction, English source with mixed directive words, and quoted/pasted non-English source text that should not determine instruction language.
- Expected result: English source with no clearly non-English instruction uses Chinese fallback, never duplicate English; clearly Chinese instruction uses Chinese companion/framing; mixed directive words follow the first clearly identifiable non-English directive language if present, otherwise Chinese; labels and notes follow response framing language where practical.
- Failure proves: companion fallback or response-framing behavior is guessy or inconsistent.
- Automation location: eval fixture plus manual evidence; `python tests/validate_skills.py` for fixture structure.

### T5. Explicit target-language requests override defaults without unrelated blocks

- Covers: R31, R32, R33, R53, E6, E7, EC8, EC9, EC12
- Level: manual
- Fixture/setup: `tests/evals/skills/editor/cases.yaml`, post-change evidence
- Steps: add cases for explicit French target, explicit English + French targets on Chinese source, and explicit target equal to source language.
- Expected result: single target returns polished source plus the requested target; multi-target returns source plus each requested target; target equal to source does not duplicate a block; no unrelated language blocks are added.
- Failure proves: explicit user constraints do not override companion defaults or output blocks are duplicated.
- Automation location: eval fixture plus manual evidence.

### T6. Target-only and note suppression behavior is explicit

- Covers: R34, R35, R36, R37, R49, R53, E8, E9, EC10, EC11
- Level: manual
- Fixture/setup: `tests/evals/skills/editor/cases.yaml`, post-change evidence
- Steps: add cases for `Only translate this into English`, `Only translate this into English. No notes.`, and equivalent Chinese suppression phrases such as `只要译文` or `不用解释`.
- Expected result: target-only omits source-language deliverable blocks; target-only alone keeps learning notes; explicit note suppression removes learning notes; translation-only preserves source meaning and tone without unnecessary source-language rewriting.
- Failure proves: target-only output and learning-note suppression rules are conflated.
- Automation location: eval fixture plus manual evidence.

### T7. Learning notes remain default, compact, anchored, and non-padded

- Covers: R38, R40, R41, R42, R43, R44, R45, R46, R47, R48, R50, E10, EC13, EC14, EC15
- Level: manual
- Fixture/setup: `tests/evals/skills/editor/cases.yaml`, post-change evidence
- Steps: add cases for substantive professionalization, ambiguous brevity cue, trivial typo, already-clear text, brittle-rule risk, and long source with more than three genuinely distinct issues.
- Expected result: notes appear after deliverables by default, use response framing language, anchor substantive edits with concrete original-to-revised references or equivalents, teach reusable principles, avoid invented lessons, use exactly one fallback note for trivial/already-clear/brittle cases unless suppressed, stay concise, and may exceed three only when distinct useful lessons warrant it and are grouped by theme.
- Failure proves: learning behavior is either removed, over-teaching, hard-capped incorrectly, or causing meaning drift.
- Automation location: eval fixture plus manual evidence.

### T8. Integrity hierarchy overrides misleading transformation requests

- Covers: R8, R26, R49, R51, R52, R53, R54, R55, R56, R65, E11, EC16
- Level: manual
- Fixture/setup: `tests/evals/skills/editor/cases.yaml`, post-change evidence
- Steps: add an integrity-boundary case with explicit target language and explicit note suppression, plus the existing simpler misleading-approval case if retained.
- Expected result: the skill briefly refuses or redirects the misleading transformation, does not imply unsupported approval, provides an accurate alternative in requested target language or languages where possible, and omits learning notes when note suppression is explicit.
- Failure proves: the prompt lets polish, translation, explicit targets, or teaching override integrity and truthfulness.
- Automation location: eval fixture plus manual evidence.

### T9. Prompt text implements the compact output contract

- Covers: R8, R9, R10, R11, R24, R25, R27, R28, R30, R51, R59, R60, R61
- Level: manual
- Fixture/setup: edited `skills/editor/SKILL.md`
- Steps: inspect prompt sections for priority order, language/default rules, workflow, output format, modification rules, and removed/replaced legacy text.
- Expected result: prompt separates instruction and source, resolves meaning once, edits source before translation, verifies only visible output blocks, includes the conflict hierarchy, uses one base template plus modification rules, removes or replaces Chinese + English default text, removes hidden Chinese + English cross-check rendering, and compresses fallback-note/template proliferation.
- Failure proves: implementation did not actually change the prompt contract or left conflicting legacy instructions.
- Automation location: manual prompt review; `git diff --check` for formatting hygiene.

### T10. Editor eval fixture captures all required behavioral scenarios

- Covers: R12-R56, R64, R65, all examples, all edge cases
- Level: integration
- Fixture/setup: `tests/evals/skills/editor/cases.yaml`
- Steps: update the YAML fixture with stable scenario IDs and categories; run `python tests/validate_skills.py`.
- Expected result: fixture remains valid `version: 1`, keeps required categories, includes prompts or situations and expected behavior for all required scenario classes, and is structurally accepted by the validator.
- Failure proves: reviewer-visible eval evidence is missing, malformed, or too narrow for the changed output contract.
- Automation location: `python tests/validate_skills.py`; manual review of scenario coverage.

### T11. Baseline and post-change evidence prove the behavior changed intentionally

- Covers: R57, R58, R66, R67
- Level: manual
- Fixture/setup: `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/baseline-evidence.md`, `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/post-change-evidence.md`
- Steps: before prompt edits, record current prompt behavior and line count; after prompt edits, record behavior against the same scenario classes and run `wc -l skills/editor/SKILL.md`.
- Expected result: baseline exists before `skills/editor/SKILL.md` changes; post-change evidence compares the same scenario classes; prompt remains under 500 lines; prompt is shorter than baseline or evidence justifies any increase.
- Failure proves: implementation lacks before/after proof or violates prompt-length requirements.
- Automation location: manual evidence files plus `wc -l skills/editor/SKILL.md`.

### T12. Repository boundaries and deterministic validation stay unchanged

- Covers: R2, R62, R63
- Level: manual
- Fixture/setup: final implementation diff and validation output
- Steps: inspect the diff for changes outside scoped prompt/eval/README/evidence/plan artifacts; inspect CI/workflow files if touched; run local validation commands.
- Expected result: no repository-wide validator changes are added; no live model calls or networked CI requirements are added; runtime, installer, persistence, API, deployment, packaging, and architecture boundaries remain unchanged.
- Failure proves: implementation expanded beyond the approved prompt/test/documentation slice.
- Automation location: diff review, `python tests/validate_skills.py`, `python -m unittest discover tests`, `git diff --check`.

### T13. README and migration notes reflect the new public contract

- Covers: compatibility and migration claims, observability claims
- Level: manual
- Fixture/setup: `README.md`, post-change evidence, PR notes when created
- Steps: inspect README editor row/section and run `python tests/check_readme_sync.py`.
- Expected result: README no longer describes editor as hardcoded Chinese/English output after the prompt changes; public wording describes source-language plus companion-language behavior without overloading details; PR notes later call out the default-output change and English-source fallback.
- Failure proves: public documentation or migration communication is stale.
- Automation location: `python tests/check_readme_sync.py`; manual README and PR-note review.

### T14. Security and privacy boundaries remain intact

- Covers: security/privacy requirements and high-stakes non-impact claims
- Level: manual
- Fixture/setup: eval prompts, prompt text, implementation diff
- Steps: inspect eval prompts and examples for fictional or sanitized content; inspect prompt text for secret/private-path requirements or unsupported chain-of-thought exposure; inspect diff for unrelated high-stakes skill changes.
- Expected result: examples and evals are sanitized, the skill does not ask for secrets or private paths, learning notes do not expose private reasoning, integrity behavior blocks falsified claims, and no unrelated high-stakes skill behavior is changed.
- Failure proves: the test data or prompt introduces privacy, safety, or scope risk.
- Automation location: manual review.

## Fixtures and data

- Primary prompt fixture: `skills/editor/SKILL.md`
- Eval fixture: `tests/evals/skills/editor/cases.yaml`
- Baseline evidence: `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/baseline-evidence.md`
- Post-change evidence: `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/post-change-evidence.md`
- README mirror surface: `README.md`
- Required eval data classes:
  - Chinese source defaulting to Chinese + English.
  - Russian source defaulting to Russian + English.
  - Spanish source defaulting to Spanish + English with best-effort quality caveat.
  - English source with English instruction falling back to Chinese.
  - English source with Chinese instruction using Chinese companion and framing.
  - Mixed-language directive handling.
  - Explicit single target.
  - Explicit multiple targets.
  - Explicit target equal to source.
  - Target-only with notes.
  - Target-only with explicit note suppression.
  - Substantive learning notes.
  - Ambiguous brevity cue.
  - Trivial correction.
  - Already-clear or restraint case.
  - Long source with more than three warranted lessons.
  - Integrity issue with explicit target and explicit note suppression.

## Mocking/stubbing policy

No mocks or stubs are needed. This repository does not use a live model harness for skill prompt behavior. Behavioral proof is recorded through deterministic fixtures and reviewer-visible evidence.

## Migration or compatibility tests

- Run `python tests/validate_skills.py` to preserve skill file compatibility and eval fixture schema.
- Run `python tests/check_readme_sync.py` to preserve README synchronization checks.
- Manually verify README and later PR notes describe the visible output-language default change and English-source fallback.
- Manually verify the implementation does not change skill name, installer behavior, validator behavior, CI behavior, runtime dependencies, or architecture boundaries.

## Observability verification

- Baseline evidence must identify current visible language blocks, learning-note behavior, explicit-target handling, target-only behavior, integrity behavior, hidden cross-check prompt text, and prompt line count.
- Post-change evidence must identify the same scenario classes and compare behavior after implementation.
- Validation output from `python tests/validate_skills.py` and `git diff --check` must be reported in downstream implementation and verification artifacts.
- Prompt length must be reported before and after implementation.

No logs, metrics, traces, or audit events are introduced by this change.

## Security/privacy verification

- Confirm eval prompts and evidence use fictional or sanitized examples.
- Confirm the optimized prompt does not request secrets, credentials, private local paths, unpublished personal data, or real customer-sensitive details.
- Confirm learning notes do not reveal private chain-of-thought or unsupported assumptions as facts.
- Confirm integrity cases block falsified approvals, consent, authorship, certainty, claims, or material facts.
- Confirm no unrelated medical, legal, financial, security, or other high-stakes skill files are changed.

## Performance checks

- Run `wc -l skills/editor/SKILL.md`.
- Confirm the prompt remains under 500 lines.
- Confirm the prompt is shorter than the pre-change line count or post-change evidence justifies any increase.
- Confirm validation remains deterministic and does not require network access or live model calls.

## Manual QA checklist

- Inspect `skills/editor/SKILL.md` for old default Chinese + English language that conflicts with the new contract.
- Inspect `skills/editor/SKILL.md` for hidden Chinese + English cross-check rendering requirements.
- Inspect `tests/evals/skills/editor/cases.yaml` for all required scenario classes and valid YAML structure.
- Inspect baseline evidence timestamp/order to ensure it was recorded before prompt edits.
- Inspect post-change evidence for the same scenario classes used in baseline.
- Inspect README for stale Chinese/English-only editor wording after prompt implementation.
- Inspect final diff for unrelated skill, validator, installer, CI, or architecture changes.

## What not to test and why

- Do not add live model CI or networked prompt tests; the approved spec forbids live model calls in CI for this slice.
- Do not test every possible source language; the spec accepts broad intake but bounds evidence to representative languages and best-effort caveats.
- Do not add validator behavior tests unless the implementation unexpectedly changes validation logic; validator changes are out of scope.
- Do not add installer, packaging, API, persistence, or deployment tests; this change does not alter those boundaries.
- Do not rely on snapshots alone; expected behavior must identify language blocks, note behavior, fidelity, explicit target handling, target-only handling, and integrity behavior.

## Uncovered gaps

None. All requirements are covered by deterministic validation, manual prompt review, eval fixture evidence, baseline/post-change evidence, or explicit migration checks.

## Next artifacts

1. Implement M1 from the execution plan: update eval fixture and record baseline evidence before editing `skills/editor/SKILL.md`.
2. Implement M2 from the execution plan: revise `skills/editor/SKILL.md` and README if mirrored behavior changes.
3. Implement M3 from the execution plan: record post-change evidence, run validation, and update plan handoff state.
4. Hand off to code-review after implementation evidence is complete.

## Follow-on artifacts

- 2026-06-16: Owner approved this test spec for implementation use.

## Readiness

This test spec is approved and active as the proof-planning surface for implementation.

Implementation may begin with M1 only: eval fixture updates and baseline evidence. Production prompt edits remain gated until baseline evidence has been recorded.
