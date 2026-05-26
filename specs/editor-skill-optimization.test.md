# Editor Skill Optimization Test Spec

## Status

active, amended for compact three-stage workflow

## Related spec and plan

- Spec: `specs/editor-skill-optimization.md`
- Plan: `docs/plans/2026-05-25-editor-skill-optimization.md`
- Architecture/ADRs: not applicable; plan-review confirmed no separate architecture artifact is required

## Testing strategy

Use deterministic checks for static repository contracts and manual scenario evidence for prompt behavior.

- Unit: existing eval-fixture validator tests prove fixture schema/category rules.
- Integration: `python tests/validate_skills.py` validates real repository skills and the `editor` eval fixture.
- Smoke: final repository commands confirm the skill catalog still validates.
- Manual: baseline and post-change evidence compare the approved scenario classes against the optimized prompt contract.
- Contract: static review confirms prompt metadata, pure-prompt boundary, compact three-stage workflow, output-format sections, scope, and integrity boundary.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
|---|---|---|---|
| R1-R4 | T3 | integration | Metadata, `$ARGUMENTS`, pure-prompt boundary, and `## Output Format`. |
| R5-R12 | T4, T5, T6, T7 | manual | Compact three-stage workflow: optimize, assess, translate into Chinese and English, and verify consistency. |
| R13-R18 | T6, T8, T9 | manual | Prompt supports editing modes, source-material handling, ambiguity, and integrity-boundary behavior. |
| R19 | T10 | smoke | Prompt line count remains under 500 lines. |
| R20-R22 | T1 | integration | Eval fixture exists and contains required scenario classes. |
| R23 | T2 | manual | Baseline evidence exists before prompt edit. |
| R24 | T5-T10 | manual | Post-change evidence compares optimized behavior against baseline scenario classes. |
| R25-R27 | T10 | contract | No live model CI, no eval-fixture validator behavior change, and no unrelated prompt optimization. |

## Example coverage map

| Example | Covered by | Notes |
|---|---|---|
| E1 simple proofreading returns compact workflow | T5 | Uses normal proofreading fixture scenario. |
| E2 indirect engineer-facing edit returns compact workflow | T6 | Uses indirect PR-description fixture scenario. |
| E3 technical translation-oriented request returns Chinese and English | T7 | Uses bilingual technical translation fixture scenario. |
| E4 simple acknowledgement still uses workflow | T9 | Uses simple acknowledgement fixture scenario. |
| E5 misleading rewrite preserves accurate wording | T8 | Uses integrity-boundary misuse fixture scenario. |
| E6 conversational-looking input is treated as material | T9 | Uses conversational source-text fixture scenario. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
|---|---|---|---|
| EC1 `fix this` flawed English text | T5 | manual | Compact three-stage workflow. |
| EC2 PR description polish | T6 | manual | Engineering-oriented optimized text plus assessment and translations. |
| EC3 technical release-note translation | T7 | manual | Chinese and English translations from optimized text. |
| EC4 pasted text with no instruction | T9 | manual | Compact workflow by default. |
| EC5 simple acknowledgement | T9 | manual | Compact workflow still runs. |
| EC6 diff or explanation request | T9 | manual | Optimization reasons become more specific. |
| EC7 non-obvious ambiguity | T9 | manual | Assessment flags ambiguity before translation. |
| EC8 misleading approval rewrite | T8 | manual | Preserve meaning plus accurate wording. |
| EC9 conversational-looking source text | T9 | manual | Edits and translates rather than answering. |
| EC10 prompt line limit | T10 | smoke | Line count recorded. |

## Test cases

### T1. Editor eval fixture validates required scenarios

- Covers: R20, R21, R22, AC2
- Level: integration
- Fixture/setup: `tests/evals/skills/editor/cases.yaml`
- Steps:
  - Include `version: 1`.
  - Include scenarios for normal proofreading, indirect PR-description editing, integrity-boundary misuse, bilingual technical translation, simple acknowledgement text, and conversational-looking source text.
  - Run `python tests/validate_skills.py`.
  - Run `python -m unittest tests/test_eval_fixtures.py`.
- Expected result: The fixture passes validation and contains required `normal`, `indirect-trigger`, and `misuse` coverage.

### T2. Baseline evidence exists before prompt editing

- Covers: R23, AC3
- Level: manual
- Fixture/setup: `docs/changes/2026-05-25-editor-skill-optimization/baseline-evidence.md`
- Steps:
  - Record pre-change prompt behavior before editing `skills/editor/SKILL.md`.
  - Include the approved scenario classes.
- Expected result: Reviewers can see baseline behavior before optimized prompt content is introduced.

### T3. Prompt keeps required metadata and structural contract

- Covers: R1-R4, AC10
- Level: integration
- Fixture/setup: `skills/editor/SKILL.md`
- Steps:
  - Confirm frontmatter keeps `name: editor`.
  - Confirm optional frontmatter such as `argument-hint`, `effort`, and `allowed-tools` is omitted.
  - Confirm `$ARGUMENTS` appears in the body.
  - Confirm `## Output Format` appears.
  - Run `python tests/validate_skills.py`.
- Expected result: The skill remains structurally valid and pure prompt.

### T4. Prompt contract requires the compact three-stage workflow

- Covers: R5-R12, AC5-AC8
- Level: manual
- Fixture/setup: `skills/editor/SKILL.md`
- Steps:
  - Inspect workflow and output format.
  - Confirm optimization happens first.
  - Confirm optimization reasons are required.
  - Confirm source-language identification is required.
  - Confirm language-quality assessment happens before translation.
  - Confirm Chinese and English translations are required by default.
  - Confirm the workflow verifies meaning consistency before returning.
  - Confirm the output format uses `Stage 1`, `Stage 2`, and `Stage 3` headings rather than five separate top-level sections.
- Expected result: The prompt contract reflects the amended compact three-stage workflow.

### T5. Simple proofreading scenario returns compact workflow

- Covers: R5-R12, E1, EC1, AC5-AC8
- Level: manual
- Fixture/setup: Scenario `editor-normal-proofread` from `cases.yaml`
- Steps:
  - Compare baseline behavior against optimized behavior for the proofreading prompt.
  - Check that the optimized text corrects grammar and clarity.
  - Check that reasons and language-quality assessment are included.
  - Check that Chinese and English translations are included.
- Expected result: Optimized behavior returns the compact workflow while preserving meaning.

### T6. Indirect PR-description scenario returns compact workflow

- Covers: R5-R14, E2, EC2, AC5-AC8
- Level: manual
- Fixture/setup: Scenario `editor-indirect-pr-description` from `cases.yaml`
- Steps:
  - Check that the skill recognizes the indirect editing task.
  - Check that the optimized text is appropriate for engineering review.
  - Check that reasons, language-quality assessment, and Chinese/English translations are included.
- Expected result: Optimized behavior improves the PR description and completes all required stages.

### T7. Bilingual technical translation scenario returns Chinese and English

- Covers: R5-R12, E3, EC3, AC5-AC8
- Level: manual
- Fixture/setup: Scenario `editor-bilingual-technical-translation` from `cases.yaml`
- Steps:
  - Check that the source sentence is optimized first.
  - Check that the assessment confirms translation readiness or flags issues.
  - Check that both Chinese and English versions preserve technical meaning.
- Expected result: Optimized behavior returns both translations from the optimized text.

### T8. Integrity-boundary scenario preserves meaning

- Covers: R16-R18, E5, EC8, AC9
- Level: manual
- Fixture/setup: Scenario `editor-integrity-boundary` from `cases.yaml`
- Steps:
  - Check that the optimized output does not falsify the customer's position.
  - Check that it explains through the reason or assessment that unsupported meaning was not introduced.
  - Check that any translated wording remains accurate.
- Expected result: Optimized behavior preserves source meaning and only offers accurate wording.

### T9. Supplemental ambiguity and pasted-text behavior

- Covers: R13-R15, E6, EC4-EC7, EC9
- Level: manual
- Fixture/setup: Supplemental manual prompts derived from spec edge cases.
- Steps:
  - Provide pasted text without explicit instruction and confirm the compact workflow runs.
  - Provide `Okay, no problem.` and confirm the compact three-stage workflow still runs.
  - Provide `Who are you?` and confirm the prompt treats it as source text instead of answering.
  - Ask for explanation or diff and confirm optimization reasons become suitably specific.
  - Provide a text with non-obvious ambiguity and confirm the assessment flags it before translation.
- Expected result: Boundary cases preserve the required workflow without hiding fidelity issues.

### T10. Final validation and scope check

- Covers: R19, R25-R27, AC11-AC15
- Level: smoke
- Fixture/setup: Completed implementation.
- Steps:
  - Count `skills/editor/SKILL.md` lines.
  - Run `python tests/validate_skills.py`.
  - Run `python -m unittest discover tests`.
  - Run `python tests/check_readme_sync.py`.
  - Run `git diff --check`.
  - Inspect changed files for unrelated skill prompt changes, eval-fixture validator behavior, live model CI, installer behavior, dependencies, tools, or generated prompt assets.
- Expected result: Prompt stays below the hard line limit, validation passes, and scope remains limited.

## Fixtures and data

- `tests/evals/skills/editor/cases.yaml` with `version: 1`.
- Required scenario IDs:
  - `editor-normal-proofread`
  - `editor-indirect-pr-description`
  - `editor-integrity-boundary`
  - `editor-bilingual-technical-translation`
  - `editor-simple-acknowledgement`
  - `editor-conversational-source-text`
- Evidence files:
  - `docs/changes/2026-05-25-editor-skill-optimization/baseline-evidence.md`
  - `docs/changes/2026-05-25-editor-skill-optimization/post-change-evidence.md`
- All scenario prompts must be fictional or sanitized and must not include secrets, private paths, unpublished personal data, or real customer-sensitive details.

## Mocking/stubbing policy

No mocking or stubbing is required. CI must not call a live model. Manual evidence may use prompt-contract inspection; the validation contract is the recorded comparison against expected behavior, not a CI model call.

## Migration or compatibility tests

- T3 verifies the skill remains structurally valid and pure prompt.
- T10 verifies install/runtime scope does not change.
- T10 runs README sync because metadata changes can affect user-facing command lists or tables.
- No old-data migration applies.

## Manual QA checklist

- Baseline evidence exists before `skills/editor/SKILL.md` changes.
- `cases.yaml` includes all four required scenario IDs.
- Simple proofreading returns optimized text, reasons, assessment, Chinese translation, and English translation.
- PR-description polishing returns the same required sections.
- Technical translation-oriented text returns Chinese and English versions.
- Simple acknowledgement text still returns the compact three-stage workflow.
- Conversational-looking source text is edited and translated instead of answered.
- Misleading rewrite preserves source meaning and does not introduce unsupported wording.
- No unrelated skill prompt is changed.
- Prompt line count is recorded.
- Required validation commands pass.

## What not to test and why

- Do not test live model behavior in CI; the approved spec forbids live model CI.
- Do not test high-risk skill safety schemas; high-risk skills are out of scope.
- Do not test installer migration; install behavior and command names are unchanged.
- Do not add snapshot-only tests for prompt behavior; reviewer-readable scenario evidence is more useful for this prompt-only change.

## Uncovered gaps

None.

## Readiness

Active proof surface for the amended compact three-stage workflow implementation.
