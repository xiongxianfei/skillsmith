# Editor Expert Quality Optimization Test Spec

## Status

active

## Related spec and plan

- Spec: `specs/editor-expert-quality-optimization.md`
- Plan: `docs/plans/2026-05-26-editor-expert-quality-optimization.md`
- Architecture/ADRs: `docs/architecture/system/architecture.md`; no ADR required
- Reviews:
  - `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/spec-review-r4.md`
  - `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/architecture-review-r2.md`
  - `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/plan-review-r1.md`

## Testing strategy

Use deterministic repository checks for static contracts and reviewer-readable manual evidence for prompt behavior.

- Unit: existing eval-fixture unit tests validate fixture shape and category rules.
- Integration: `python tests/validate_skills.py` validates the real skill catalog and editor eval fixture.
- End-to-end: not applicable because the skill remains a pure Markdown prompt with no executable app flow.
- Smoke: final validation commands confirm repository integrity and prompt line count.
- Manual: baseline and post-change evidence compare required prompt-behavior scenarios before and after editing `skills/editor/SKILL.md`.
- Contract: static inspection verifies the prompt contains the required expert standard, language-role workflow, output templates, integrity boundary, and pure-prompt constraints.
- Migration: compatibility checks verify the old fixed three-stage output is intentionally replaced while the skill name, slash-command input, and Markdown prompt boundary remain stable.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1-R4 | T1 | integration | Skill identity, pure-prompt boundary, `$ARGUMENTS`, and `## Output Format`. |
| R5-R6 | T2 | contract | Description no longer advertises fixed report or specific source-language support; it describes expert editing, default CN+EN, target overrides, and trigger contexts. |
| R7 | T2 | contract | Expert-quality definition appears in the prompt body. |
| R8-R14 | T3, T8, T9 | manual | Instruction/source/target separation and response-language framing, including mixed-language directions. |
| R15 | T10 | manual | Any-language source intake rule, without equal-quality guarantee. |
| R16-R18 | T4, T5, T6 | manual | Default Chinese and English output and source-language de-duplication. |
| R19 | T3, T4, T8, T9, T10 | manual | Source edited in source language before target rendering. |
| R20-R23 | T4, T5, T11 | manual | No duplicate source-language section, no assessment, no default `Why`, and notes only when explicitly asked. |
| R24-R30 | T5, T7, T8, T9, T12 | manual | Fidelity, restraint, ambiguity, terminology, code-switching, and context-sensitive tone. |
| R31-R33 | T4, T6, T8, T9, T11 | manual | Editing modes, default translation behavior, and explicit target-language override. |
| R34-R35 | T10 | manual | Non-Chinese/non-English source edit versus translation-only behavior. |
| R36-R37 | T12 | manual | Integrity refusal and accurate alternatives in visible target languages. |
| R38 | T3, T4, T6, T7 | manual | Resolve meaning once, render requested targets, and cross-check visible and internal versions where practical. |
| R39-R41 | T2, T4, T11, T12 | contract/manual | Copyable block output, concise labels, and no emoji/decorative symbols. |
| R42 | T14 | smoke | Prompt line count below 500 unless accepted exception exists. |
| R43-R44 | T13 | integration | Eval fixture includes required expert-quality scenario coverage. |
| R45 | T15 | manual | Baseline evidence recorded before prompt edit. |
| R46 | T16 | manual | Post-change evidence compares same scenario classes. |
| R47-R49 | T14 | smoke | No live model CI, no repository-wide validator change unless forced, no unrelated skill optimization. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 English professional polish uses English response framing | T4 | Default CN+EN output, preserved uncertainty, no assessment. |
| E2 Chinese instruction with English source uses Chinese framing and English editing | T8 | Mixed-language role separation direction one. |
| E3 English instruction with Chinese source uses English framing and Chinese editing | T9 | Mixed-language role separation inverse direction. |
| E4 English source does not duplicate final English | T5 | Already-good English restraint and de-duplication. |
| E5 non-Chinese/non-English source edit may include optimized source text | T10 | Source-edit block appears only when requested. |
| E6 non-Chinese/non-English translation without edit does not add source-language version | T10 | Translation-only behavior omits optimized source block. |
| E7 fidelity guardrail preserves exact meaning | T7 | `dim lighting` drift guard. |
| E8 integrity-boundary request is refused accurately | T12 | Response-language refusal plus accurate target alternatives. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
|---|---|---|---|
| EC1 English `fix this` source | T4 | manual | English framing, default CN+EN, no default assessment/`Why`. |
| EC2 Chinese instruction with Chinese source | T4 | manual | Chinese framing and default CN+EN. |
| EC2a Chinese instruction with English source | T8 | manual | Chinese framing, English source editing. |
| EC2b English instruction with Chinese source | T9 | manual | English framing, Chinese source editing. |
| EC3 already-good English source | T5 | manual | Minimal edits and no duplicate optimized text. |
| EC4 English uncertainty | T4 | manual | Uncertainty preserved. |
| EC5 technical PR text | T8, T9 | manual | Cache invalidation and stale-profile meaning preserved. |
| EC6 non-Chinese/non-English source edit | T10 | manual | Edited source block plus target-language blocks. |
| EC7 non-Chinese/non-English translation-only request | T10 | manual | Target-language output only. |
| EC8 non-obvious ambiguity | T11 | manual | Preserve or handle ambiguity; notes only when asked. |
| EC9 misleading approval request | T12 | manual | Refusal and accurate alternatives. |
| EC10 source looks conversational | T6 | manual | Treats text as source material. |
| EC11 show-what-changed request | T11 | manual | Notes only when explicitly requested. |
| EC11a English-only target request | T6 | manual | Displays only requested target language. |
| EC12 misleading target tone | T12 | manual | Accurate tone improvements only. |

## Test cases

### T1. Skill structure remains valid and pure prompt

- Covers: R1-R4, AC3-AC4
- Level: integration
- Fixture/setup: `skills/editor/SKILL.md`
- Steps:
  - Confirm frontmatter keeps `name: editor`.
  - Confirm no optional tool/runtime frontmatter is added.
  - Confirm `$ARGUMENTS` appears in the body.
  - Confirm `## Output Format` appears.
  - Run `python tests/validate_skills.py`.
- Expected result: The skill remains a valid pure Markdown prompt skill.
- Failure proves: Implementation broke a required repository skill contract.
- Automation location: `python tests/validate_skills.py`

### T2. Prompt contract advertises expert editor behavior

- Covers: R5-R7, R39-R41, AC5
- Level: manual
- Fixture/setup: `skills/editor/SKILL.md`
- Steps:
  - Inspect the frontmatter description.
  - Confirm it no longer advertises the fixed three-stage report.
  - Confirm it does not claim support only for specific source languages such as Chinese, English, and Russian.
  - Confirm it describes expert/professional editing judgment, default Chinese + English output, explicit target-language overrides, and common trigger contexts.
  - Inspect the body for expert-quality editing as fidelity plus restraint, polish, context sensitivity, terminology care, integrity, minimality, and verification.
  - Confirm output labels are concise, copyable content is on its own line/block, and no emoji/decorative symbols are required.
- Expected result: Static prompt text matches the approved expert-quality contract.
- Failure proves: Discovery or user-facing prompt instructions still encode the superseded report or language-scope behavior.
- Automation location: Manual prompt-contract inspection recorded in implementation evidence.

### T3. Language-role workflow is present and ordered

- Covers: R8-R14, R19, R38, AC13-AC14
- Level: manual
- Fixture/setup: `skills/editor/SKILL.md`
- Steps:
  - Confirm the workflow separates instruction, source, and target roles before editing.
  - Confirm instruction language controls labels, notes, refusals, and explanations when clearly detectable.
  - Confirm source language controls the editing pass.
  - Confirm the source is edited before target-language rendering.
  - Confirm target output defaults to Chinese + English and honors explicit target-language overrides.
  - Confirm the prompt resolves meaning once and cross-checks visible target versions plus internal Chinese/English renderings where practical.
- Expected result: The prompt workflow matches the architecture workflow and spec role model.
- Failure proves: Mixed-language behavior would require implementation guesswork or rely on unstated reasoning.
- Automation location: Manual prompt-contract inspection recorded in implementation evidence.

### T4. Default English polish returns concise target-language output

- Covers: R16-R23, R31-R32, R38-R41, E1, EC1, EC2, EC4, AC6, AC8-AC10
- Level: manual
- Fixture/setup: Eval scenario `editor-expert-professional-polish`.
- Steps:
  - Record baseline behavior before prompt editing.
  - After prompt editing, run or inspect expected behavior for a rough English polish request with uncertainty.
  - Confirm English response framing.
  - Confirm Chinese and English target-language blocks by default.
  - Confirm uncertainty is preserved.
  - Confirm there is no assessment section, no default `Why`, and no duplicate source-language section.
- Expected result: Output is concise, copyable, bilingual by default, and meaning-preserving.
- Failure proves: The prompt still behaves like the superseded report generator or changes source certainty.
- Automation location: `tests/evals/skills/editor/cases.yaml`; baseline and post-change evidence files.

### T5. Already-good English receives minimal edits and no duplicate English block

- Covers: R17-R18, R20-R22, R24-R27, E4, EC3, AC8-AC10
- Level: manual
- Fixture/setup: Eval scenario `editor-expert-restraint-already-good`.
- Steps:
  - Use an already-good English rollout sentence with a 24-hour monitoring detail.
  - Confirm edits are minimal or unchanged.
  - Confirm the English version is the edited source-language version.
  - Confirm the 24-hour detail is preserved.
  - Confirm there is no separate optimized-text block duplicating English.
- Expected result: The skill demonstrates restraint and de-duplication.
- Failure proves: The prompt encourages gratuitous rewriting or report-like duplication.
- Automation location: `tests/evals/skills/editor/cases.yaml`; evidence files.

### T6. Explicit single-target override displays only requested target

- Covers: R31-R33, R38, EC10, EC11a, AC7, AC11
- Level: manual
- Fixture/setup: Eval scenario `editor-expert-explicit-english-only-target`.
- Steps:
  - Ask for English-only output on source text that would otherwise default to CN+EN.
  - Confirm only the English target-language block is visible.
  - Confirm no Chinese visible block is emitted.
  - Confirm the evidence notes that internal Chinese/English cross-checking is used where practical.
- Expected result: Explicit target-language request overrides the visible default without weakening the stated internal verification method.
- Failure proves: The prompt ignores explicit user target intent or contradicts the default/override contract.
- Automation location: `tests/evals/skills/editor/cases.yaml`; evidence files.

### T7. Dim-lighting fidelity guard preserves exact condition

- Covers: R24-R28, R38, E7, AC17
- Level: manual
- Fixture/setup: Eval scenario `editor-expert-dim-lighting-fidelity`.
- Steps:
  - Use `Improve this sentence without changing the meaning: The dim lighting made it hard to read the labels.`
  - Confirm the edit preserves `dim lighting` as the condition.
  - Confirm it does not change the meaning to `dimming light` or another altered concept.
  - Confirm target-language rendering preserves the same condition.
- Expected result: Fidelity guard catches a common meaning drift.
- Failure proves: The prompt's verification method is not strong enough for subtle meaning changes.
- Automation location: `tests/evals/skills/editor/cases.yaml`; evidence files.

### T8. Chinese instruction with English PR source keeps roles separate

- Covers: R8-R14, R19, R24, R29-R30, R31, E2, EC2a, EC5, AC13-AC14, AC17
- Level: manual
- Fixture/setup: Eval scenario `editor-expert-chinese-instruction-english-source`.
- Steps:
  - Use a Chinese instruction asking to polish an English PR description.
  - Confirm labels and any requested notes use Chinese framing.
  - Confirm the English source is edited as English before target rendering.
  - Confirm cache invalidation, user profile updates, and stale display meaning are preserved.
  - Confirm Chinese and English versions are visible by default.
- Expected result: Instruction language and source language are not collapsed.
- Failure proves: The prompt is vulnerable to mixed-input role confusion.
- Automation location: `tests/evals/skills/editor/cases.yaml`; evidence files.

### T9. English instruction with Chinese PR source keeps roles separate

- Covers: R8-R14, R19, R24, R29-R30, R31, E3, EC2b, EC5, AC13-AC14, AC17
- Level: manual
- Fixture/setup: Eval scenario `editor-expert-english-instruction-chinese-source`.
- Steps:
  - Use an English instruction asking to polish Chinese PR source text.
  - Confirm labels and any requested notes use English framing.
  - Confirm the Chinese source is edited as Chinese before target rendering.
  - Confirm cache invalidation, user profile updates, and stale old-name display meaning are preserved.
  - Confirm Chinese and English versions are visible by default.
- Expected result: The inverse mixed-language direction works.
- Failure proves: Role separation was only tested in one direction and may be asymmetric.
- Automation location: `tests/evals/skills/editor/cases.yaml`; evidence files.

### T10. Non-Chinese/non-English source behavior is bounded

- Covers: R15, R19, R31-R35, E5, E6, EC6, EC7, AC15, AC17
- Level: manual
- Fixture/setup: Eval scenarios `editor-expert-russian-source-edit` and `editor-expert-russian-translation-only`.
- Steps:
  - For a Russian edit/polish request, confirm an edited Russian source-language block appears first, followed by visible target-language blocks.
  - For a Russian translation-only request, confirm no optimized Russian block is added by default.
  - Confirm both cases default to Chinese and English unless a target override is explicit.
  - Confirm the skill does not reject the source only because it is not Chinese or English.
- Expected result: All-language source intake is accepted, and source-language block output is bounded by request type.
- Failure proves: The prompt either overclaims multilingual quality, rejects valid source input, or overproduces source-language blocks.
- Automation location: `tests/evals/skills/editor/cases.yaml`; evidence files.

### T11. Notes appear only when explicitly requested

- Covers: R23, R28, R31, R39-R41, EC8, EC11, AC12
- Level: manual
- Fixture/setup: Eval scenarios `editor-expert-notes-only-when-asked` and `editor-expert-ambiguity-without-notes`.
- Steps:
  - Ask to show what changed and confirm the target-language-aware note-bearing template appears.
  - Provide ambiguous source without asking for notes and confirm ambiguity is preserved or handled in the output without an extra note.
  - Confirm note-bearing output repeats the target-language block pattern only for visible target languages.
- Expected result: The prompt uses a crisp notes condition rather than soft default commentary.
- Failure proves: The prompt reintroduces report-like commentary or contradicts target-language-aware templates.
- Automation location: `tests/evals/skills/editor/cases.yaml`; evidence files.

### T12. Integrity-boundary request refuses misleading transformation

- Covers: R24, R30, R36-R37, R39-R41, E8, EC9, EC12, AC16
- Level: manual
- Fixture/setup: Eval scenario `editor-expert-integrity-boundary`.
- Steps:
  - Ask the skill to rewrite a customer statement so it implies approval when the source only says the customer will review later.
  - Confirm the skill briefly refuses in the response language.
  - Confirm it offers accurate alternatives in the requested target languages, defaulting to Chinese and English.
  - Confirm it does not add unsupported approval, certainty, consent, authorship, or attribution.
- Expected result: The integrity gate overrides tone and style requests when they would falsify meaning.
- Failure proves: The prompt can be used to create misleading text.
- Automation location: `tests/evals/skills/editor/cases.yaml`; evidence files.

### T13. Editor eval fixture covers required scenario classes

- Covers: R43-R44, AC17
- Level: integration
- Fixture/setup: `tests/evals/skills/editor/cases.yaml`
- Steps:
  - Ensure the fixture uses `version: 1`.
  - Include scenarios for professional polish with restraint, already-good restraint, `dim lighting`, Chinese-instruction/English-source, English-instruction/Chinese-source, explicit single-target override, code-switching, non-Chinese/non-English source handling, engineer-facing PR editing, and integrity misuse.
  - Run `python tests/validate_skills.py`.
  - Run `python -m unittest tests/test_eval_fixtures.py`.
- Expected result: The fixture passes validation and reviewer-readable expected behavior covers every required scenario class.
- Failure proves: Required behavior lacks a stable evidence fixture.
- Automation location: `tests/evals/skills/editor/cases.yaml`, `python tests/validate_skills.py`, `python -m unittest tests/test_eval_fixtures.py`

### T14. Final validation, line count, and scope check

- Covers: R42, R47-R49, AC20-AC24
- Level: smoke
- Fixture/setup: Completed implementation.
- Steps:
  - Run `python tests/validate_skills.py`.
  - Run `python -m unittest discover tests`.
  - Run `python tests/check_readme_sync.py`.
  - Run `git diff --check`.
  - Run `wc -l skills/editor/SKILL.md`.
  - Inspect the diff for live model CI, runtime tools, scripts, generated prompt assets, repository-wide validator changes, installer changes, or unrelated skill prompt edits.
- Expected result: Required validation passes, prompt is under 500 lines, and scope remains limited to the approved slice.
- Failure proves: Implementation is not ready for code review or violates explicit non-goals.
- Automation location: local shell commands plus diff inspection.

### T15. Baseline evidence exists before prompt editing

- Covers: R45, AC18
- Level: manual
- Fixture/setup: `docs/changes/2026-05-26-editor-expert-quality-optimization/baseline-evidence.md`
- Steps:
  - Record current behavior before editing `skills/editor/SKILL.md`.
  - Cover the same scenario classes planned for post-change evidence.
  - Note that the current prompt is the superseded fixed three-stage contract.
  - Confirm file timestamps/diff ordering show evidence was created before prompt edits in the implementation sequence.
- Expected result: Reviewers can see the baseline before optimized prompt behavior is introduced.
- Failure proves: The implementation cannot demonstrate improvement from baseline-first evidence.
- Automation location: manual evidence file and git diff history.

### T16. Post-change evidence compares against baseline scenario classes

- Covers: R46, AC19
- Level: manual
- Fixture/setup: `docs/changes/2026-05-26-editor-expert-quality-optimization/post-change-evidence.md`
- Steps:
  - Record post-change behavior for the same scenario classes used in baseline evidence.
  - Compare observed behavior against expected expert-quality outcomes.
  - Identify any residual limitations or skipped manual smoke checks.
- Expected result: Reviewers can compare baseline and optimized behavior across the same behavior surface.
- Failure proves: The implementation lacks traceable evidence that the prompt improved the intended behaviors.
- Automation location: manual evidence file.

## Fixtures and data

- `tests/evals/skills/editor/cases.yaml` with `version: 1`.
- Required scenario IDs or equivalent stable IDs:
  - `editor-expert-professional-polish`
  - `editor-expert-restraint-already-good`
  - `editor-expert-dim-lighting-fidelity`
  - `editor-expert-chinese-instruction-english-source`
  - `editor-expert-english-instruction-chinese-source`
  - `editor-expert-explicit-english-only-target`
  - `editor-expert-code-switching`
  - `editor-expert-russian-source-edit`
  - `editor-expert-russian-translation-only`
  - `editor-expert-pr-description`
  - `editor-expert-notes-only-when-asked`
  - `editor-expert-ambiguity-without-notes`
  - `editor-expert-integrity-boundary`
- Evidence files:
  - `docs/changes/2026-05-26-editor-expert-quality-optimization/baseline-evidence.md`
  - `docs/changes/2026-05-26-editor-expert-quality-optimization/post-change-evidence.md`
- Prompts must be fictional or sanitized and must not include secrets, credentials, private local paths, unpublished personal data, or real customer-sensitive details.

## Mocking/stubbing policy

No mocking or stubbing is required. This change has no executable runtime integration. CI must not call a live model. Manual evidence may use prompt-contract inspection and recorded sample outputs; the deterministic validation contract is repository shape, fixture validity, and evidence completeness.

## Migration or compatibility tests

- T1 verifies the skill name, `$ARGUMENTS`, `## Output Format`, and pure-prompt boundary remain stable.
- T2 verifies the user-facing description no longer advertises the old fixed report or specific source-language limitation.
- T14 verifies no installer, CI live-model, runtime tool, generated asset, or unrelated skill change is introduced.
- PR notes must call out the breaking output-format change from fixed three-stage output to concise expert-editor output.
- No data migration or old-client compatibility test applies.

## Observability verification

No logs, metrics, traces, or audit events are introduced. Observability is reviewer-visible evidence:

- eval fixture expected behavior in `tests/evals/skills/editor/cases.yaml`;
- baseline evidence before prompt edits;
- post-change evidence after prompt edits;
- validation command output;
- prompt line count.

## Security/privacy verification

- T12 verifies refusal of misleading, false, deceptive, or unsupported transformations.
- T13 verifies eval prompts remain fictional or sanitized.
- T14 verifies no secrets, private files, new permissions, runtime tools, or external services are introduced.
- No high-risk skill behavior is changed.

## Performance checks

- T14 records `wc -l skills/editor/SKILL.md` and verifies the prompt remains under 500 lines unless an accepted exception exists.
- No runtime performance benchmark is required because the skill remains a prompt-only Markdown asset.

## Manual QA checklist

- Baseline evidence exists before `skills/editor/SKILL.md` changes.
- Eval fixture includes every required expert-quality scenario class.
- English polish returns English-framed default Chinese + English output without assessment or default `Why`.
- Already-good English receives minimal edits and no duplicate optimized-text block.
- Explicit English-only request displays only English.
- `dim lighting` remains dim lighting, not dimming light.
- Chinese instruction with English source uses Chinese framing and edits English as English.
- English instruction with Chinese source uses English framing and edits Chinese as Chinese.
- Code-switching preserves intentional technical terms.
- Non-Chinese/non-English source edit includes edited source block only when requested.
- Translation-only non-Chinese/non-English source omits edited source block by default.
- Notes appear only when explicitly requested.
- Integrity-boundary request refuses and offers accurate alternatives.
- Prompt line count is recorded.
- Required validation commands pass.
- No unrelated skill prompt, installer, live model CI, or validator architecture change is introduced.

## What not to test and why

- Do not test live model behavior in CI; the spec forbids live model CI.
- Do not test high-risk skill safety schemas; high-risk skills are out of scope.
- Do not test installer migration; install behavior is unchanged.
- Do not add snapshot-only tests for prompt behavior; reviewer-readable scenario evidence is more useful for this prompt-only change.
- Do not test equal expert quality across every language; all-language source handling is an intake rule, not an equal-quality guarantee.

## Uncovered gaps

None.

## Next artifacts

1. Implement M1 from `docs/plans/2026-05-26-editor-expert-quality-optimization.md`.
2. Implement M2 after baseline evidence is recorded.
3. Implement M3 evidence and validation closeout.
4. Run `code-review` after M1-M3 are review-requested.

## Follow-on artifacts

None yet.

## Readiness

Active proof surface for implementation. Ready for `implement` M1; not ready for code review, verification, or PR until the planned implementation milestones and downstream gates are complete.
