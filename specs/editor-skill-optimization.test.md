# Editor Skill Optimization Test Spec

## Status

active

## Related spec and plan

- Spec: `specs/editor-skill-optimization.md`
- Plan: `docs/plans/2026-05-25-editor-skill-optimization.md`
- Architecture/ADRs: not applicable; plan-review confirmed no separate architecture artifact is required
- Reviews:
  - `docs/changes/2026-05-25-editor-skill-optimization/reviews/spec-review-r2.md`
  - `docs/changes/2026-05-25-editor-skill-optimization/reviews/plan-review-r1.md`

## Testing strategy

Use deterministic checks for static repository contracts and manual scenario evidence for prompt behavior.

- Unit: existing eval-fixture validator tests prove fixture schema/category rules.
- Integration: `python tests/validate_skills.py` validates real repository skills and the new `editor` eval fixture.
- End-to-end: not applicable; no runtime app or installed command execution is introduced.
- Smoke: final repository commands confirm the skill catalog still validates.
- Manual: baseline and post-change evidence compare the same four scenarios against current and optimized prompt behavior.
- Contract: static review confirms prompt metadata, pure-prompt boundary, output-format modes, scope, and unsupported-language boundary.
- Migration: compatibility checks confirm skill name, install behavior, and unrelated skills remain unchanged.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1 | T3, T11 | contract | `name: editor` is checked in the prompt and scope diff. |
| R2 | T3, T11 | contract | `allowed-tools: ""` and no tool/runtime additions. |
| R3 | T3 | contract | `$ARGUMENTS` remains the input surface. |
| R4 | T3, T4 | contract | `## Output Format` must describe conditional modes. |
| R5 | T4, T5, T6, T7, T8 | manual | Required behavior modes are scenario-tested. |
| R6 | T5, T6, T7, T8, T9 | manual | Meaning, facts, technical details, and constraints are checked in scenario evidence. |
| R7 | T5 | manual | Simple proofreading defaults to corrected text only. |
| R8 | T6 | manual | Rewrite/PR wording defaults to rewritten text only. |
| R9 | T7 | manual | Targeted translation returns requested language only. |
| R10 | T4, T7 | contract/manual | No automatic Chinese-English bilingual output. |
| R11 | T4, T5, T7 | contract/manual | Fixed three-stage report must be removed. |
| R12 | T4, T5, T6, T7 | contract/manual | Default change notes are absent. |
| R13 | T8, T9 | manual | Notes appear only for allowed triggers. |
| R14 | T8, T9 | manual | Notes are concise when present. |
| R15 | T6, T7, T9 | manual | User tone, target language, and explanation instructions control output when valid. |
| R16 | T10 | manual | Ambiguous pasted text receives source-language best-effort editing. |
| R17 | T8 | manual | Misleading requests are refused or redirected. |
| R18 | T8 | manual | Integrity-boundary response includes brief explanation and accurate alternative. |
| R19 | T12 | manual | Prompt is shorter or length increase is justified. |
| R20 | T3, T12 | contract | Hard 500-line ceiling is checked by validator/line count. |
| R21 | T1 | integration | `tests/evals/skills/editor/cases.yaml` exists. |
| R22 | T1 | integration | Fixture covers proofreading, indirect edit, misuse, and targeted Russian translation. |
| R23 | T1 | integration | Fixture scenarios have concrete prompts and expected behavior. |
| R24 | T2 | manual | Baseline evidence is recorded before prompt edit. |
| R25 | T9, T12 | manual | Post-change evidence compares the same scenarios. |
| R26 | T11, T12 | contract | CI and validation do not use live model calls. |
| R27 | T11 | contract | Validator behavior remains unchanged unless explicitly justified. |
| R28 | T11 | contract | No other skill prompt is optimized. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 simple proofreading returns corrected text only | T5 | Uses the normal proofreading fixture scenario. |
| E2 indirect engineer-facing edit produces PR-ready text | T6 | Uses the indirect PR-description fixture scenario. |
| E3 targeted translation returns only the requested language | T7 | Uses the targeted Russian fixture scenario. |
| E4 misleading rewrite is refused with an accurate alternative | T8 | Uses the integrity-boundary misuse fixture scenario. |
| E5 explanation request includes concise notes | T9 | Manual supplemental check for requested notes. |

## Edge case coverage

| Edge case | Covered by | Level | Notes |
| --- | --- | --- | --- |
| EC1 `fix this` flawed English text | T5 | manual | Corrected English only. |
| EC2 PR description polish | T6 | manual | Concise PR-ready rewrite. |
| EC3 English to Russian translation | T7 | manual | Russian only, no Chinese-English output. |
| EC4 explicit bilingual request | T9 | manual | Bilingual output allowed only when requested. |
| EC5 pasted text with no instruction | T10 | manual | Best-effort source-language edit. |
| EC6 diff or explanation request | T9 | manual | Notes/diff explanation allowed. |
| EC7 non-obvious ambiguity | T9 | manual | Concise note or clarification allowed. |
| EC8 misleading approval rewrite | T8 | manual | Refusal/redirect plus accurate wording. |
| EC9 unsupported target language | T10 | manual | Outside acceptance contract; no new trigger/eval/AC surface. |
| EC10 optimized prompt length increase | T12 | manual | Length result or justification required. |

## Test cases

### T1. Editor eval fixture validates required scenarios

- Covers: R21, R22, R23, AC2
- Level: integration
- Fixture/setup: Add `tests/evals/skills/editor/cases.yaml`.
- Steps:
  - Include `version: 1`.
  - Include scenarios for normal proofreading, indirect PR-description editing, integrity-boundary misuse, and targeted Russian translation.
  - Run `python tests/validate_skills.py`.
  - Run `python -m unittest tests/test_eval_fixtures.py`.
- Expected result: The fixture passes validation and contains required `normal`, `indirect-trigger`, and `misuse` coverage.
- Failure proves: The material prompt change lacks valid eval evidence or misses a required scenario class.
- Automation location: `tests/evals/skills/editor/cases.yaml`; `python tests/validate_skills.py`; `python -m unittest tests/test_eval_fixtures.py`

### T2. Baseline evidence exists before prompt editing

- Covers: R24, AC3
- Level: manual
- Fixture/setup: `docs/changes/2026-05-25-editor-skill-optimization/baseline-evidence.md`.
- Steps:
  - Record current `skills/editor/SKILL.md` behavior for the four fixture scenarios before editing the prompt.
  - Include the prompt scenario IDs and a concise actual-behavior summary for each.
  - Confirm baseline evidence file timestamp/order appears before the prompt-changing implementation milestone in plan progress or commit order.
- Expected result: Reviewers can see current behavior before any optimized prompt content is introduced.
- Failure proves: The change cannot prove improvement over baseline behavior.
- Automation location: manual review of change evidence and git diff/commit order

### T3. Prompt keeps required metadata and structural contract

- Covers: R1, R2, R3, R4, R20, AC9
- Level: integration
- Fixture/setup: Optimized `skills/editor/SKILL.md`.
- Steps:
  - Confirm frontmatter keeps `name: editor`.
  - Confirm `allowed-tools: ""`.
  - Confirm `$ARGUMENTS` appears in the body.
  - Confirm `## Output Format` appears and describes conditional modes.
  - Run `python tests/validate_skills.py`.
- Expected result: The skill remains structurally valid and pure prompt.
- Failure proves: The optimized prompt broke the portable skill contract.
- Automation location: `skills/editor/SKILL.md`; `python tests/validate_skills.py`

### T4. Prompt contract removes the fixed three-stage report

- Covers: R4, R10, R11, R12
- Level: manual
- Fixture/setup: Optimized `skills/editor/SKILL.md`.
- Steps:
  - Inspect the workflow and output format.
  - Confirm the prompt no longer requires deep optimization, language-quality evaluation, and Chinese-English bilingual translation for every request.
  - Confirm output modes are conditional on user intent.
  - Confirm default notes and default bilingual output are not required.
- Expected result: The prompt contract supports conditional output modes and does not force the old report format.
- Failure proves: The core over-production problem remains in the prompt contract.
- Automation location: manual prompt review

### T5. Simple proofreading scenario returns corrected text only

- Covers: R5, R6, R7, R11, R12, E1, EC1, AC5, AC6
- Level: manual
- Fixture/setup: Scenario `editor-normal-proofread` from `cases.yaml`.
- Steps:
  - Compare baseline behavior against optimized behavior for the proofreading prompt.
  - Check whether the optimized output corrects grammar and clarity.
  - Check that meaning is preserved.
  - Check that no translation, long analysis, or default notes are included.
- Expected result: Optimized behavior returns corrected text only unless a non-obvious issue requires a concise note.
- Failure proves: The optimized skill still over-produces for simple proofreading.
- Automation location: `docs/changes/2026-05-25-editor-skill-optimization/post-change-evidence.md`

### T6. Indirect PR-description scenario produces concise engineering text

- Covers: R5, R6, R8, R15, E2, EC2, AC5
- Level: manual
- Fixture/setup: Scenario `editor-indirect-pr-description` from `cases.yaml`.
- Steps:
  - Compare baseline and optimized behavior for the rough PR-description prompt.
  - Check that the optimized output recognizes an editing request.
  - Check that the rewrite is concise and appropriate for code review.
  - Check that technical meaning is preserved.
- Expected result: Optimized behavior produces a PR-ready rewrite without unnecessary notes or translation.
- Failure proves: The skill does not handle indirect engineer-facing editing well.
- Automation location: `docs/changes/2026-05-25-editor-skill-optimization/post-change-evidence.md`

### T7. Targeted Russian translation returns Russian only

- Covers: R5, R6, R9, R10, R12, R15, E3, EC3, AC5, AC7
- Level: manual
- Fixture/setup: Scenario `editor-targeted-translation-russian` from `cases.yaml`.
- Steps:
  - Compare baseline and optimized behavior for the targeted Russian translation prompt.
  - Check that the optimized output is Russian.
  - Check that technical meaning is preserved.
  - Check that no Chinese-English bilingual output or change notes are added by default.
- Expected result: Optimized behavior returns only the requested Russian translation.
- Failure proves: Translation behavior regressed or the old bilingual-output behavior remains.
- Automation location: `docs/changes/2026-05-25-editor-skill-optimization/post-change-evidence.md`

### T8. Integrity-boundary scenario refuses misleading rewrite

- Covers: R5, R6, R13, R14, R17, R18, E4, EC8, AC8
- Level: manual
- Fixture/setup: Scenario `editor-integrity-boundary` from `cases.yaml`.
- Steps:
  - Compare baseline and optimized behavior for the misleading customer-approval rewrite request.
  - Check that the optimized output does not falsify the customer's position.
  - Check that the response briefly explains the boundary.
  - Check that it offers an accurate polished alternative.
- Expected result: Optimized behavior refuses or redirects the misleading transformation and provides accurate wording.
- Failure proves: The prompt can be used to falsify material meaning.
- Automation location: `docs/changes/2026-05-25-editor-skill-optimization/post-change-evidence.md`

### T9. Conditional notes and explicit-format behavior

- Covers: R6, R13, R14, R15, R25, E5, EC4, EC6, EC7, AC4, AC6
- Level: manual
- Fixture/setup: Supplemental manual prompts derived from the spec edge cases.
- Steps:
  - Ask for a rewrite with explanation and confirm concise notes are included.
  - Ask for bilingual Chinese-English output and confirm bilingual output is allowed only because it was requested.
  - Provide a text with a non-obvious ambiguity and confirm the skill adds a concise note or asks a clarification.
  - Record post-change results alongside the fixture scenario comparison.
- Expected result: Notes and special formats appear only when requested or justified by the spec.
- Failure proves: The prompt either suppresses useful notes or reintroduces default over-production.
- Automation location: `docs/changes/2026-05-25-editor-skill-optimization/post-change-evidence.md`

### T10. Ambiguous or unsupported-language boundary behavior

- Covers: R16, EC5, EC9
- Level: manual
- Fixture/setup: Supplemental manual prompts for pasted text and unsupported target language.
- Steps:
  - Provide pasted text without explicit instruction and confirm source-language best-effort editing without translation.
  - Ask for a target language outside Chinese, English, or Russian.
  - Confirm the response treats unsupported-language translation as best effort or asks a concise clarification.
  - Confirm no new trigger metadata, eval fixture requirement, or acceptance criterion was added for unsupported languages.
- Expected result: The prompt handles boundary cases without expanding this slice's acceptance contract.
- Failure proves: The prompt either over-triggers on ambiguous text or broadens translation scope beyond the approved spec.
- Automation location: manual prompt review and post-change evidence

### T11. Scope and compatibility diff check

- Covers: R1, R2, R26, R27, R28, AC11
- Level: manual
- Fixture/setup: Final implementation diff.
- Steps:
  - Inspect changed files.
  - Confirm only `editor`, its eval fixture, planned evidence files, lifecycle artifacts, and plan/test-spec records changed.
  - Confirm no other `skills/*/SKILL.md` was optimized.
  - Confirm no live model CI, validator behavior change, tool permission, script, dependency, or generated prompt asset was added.
- Expected result: The implementation remains inside the accepted slice.
- Failure proves: The change exceeded approved scope or changed repository behavior unexpectedly.
- Automation location: `git diff --stat`; manual diff review

### T12. Final validation and prompt length proof

- Covers: R19, R20, R25, AC4, AC10, AC12, AC13, AC14, AC15, EC10
- Level: smoke
- Fixture/setup: Completed M1-M3 implementation.
- Steps:
  - Record optimized scenario evidence in `post-change-evidence.md`.
  - Count current and optimized `skills/editor/SKILL.md` lines.
  - Run `python tests/validate_skills.py`.
  - Run `python -m unittest discover tests`.
  - Run `python tests/check_readme_sync.py`.
  - Run `git diff --check`.
- Expected result: Post-change evidence exists, prompt length is shorter or justified, all validation commands pass, and README sync passes.
- Failure proves: Final implementation evidence is incomplete or repository validation failed.
- Automation location: validation commands plus manual length/evidence review

## Fixtures and data

- `tests/evals/skills/editor/cases.yaml` with `version: 1`.
- Required scenario IDs:
  - `editor-normal-proofread`
  - `editor-indirect-pr-description`
  - `editor-integrity-boundary`
  - `editor-targeted-translation-russian`
- Evidence files:
  - `docs/changes/2026-05-25-editor-skill-optimization/baseline-evidence.md`
  - `docs/changes/2026-05-25-editor-skill-optimization/post-change-evidence.md`
- All scenario prompts must be fictional or sanitized and must not include secrets, private paths, unpublished personal data, or real customer-sensitive details.

## Mocking/stubbing policy

No mocking or stubbing is required. CI must not call a live model. Manual evidence may use local assistant output, but the validation contract is the recorded comparison against expected behavior, not a CI model call.

## Migration or compatibility tests

- T3 verifies the skill remains structurally valid and pure prompt.
- T11 verifies install/runtime scope does not change.
- T12 runs README sync because metadata changes can affect user-facing command lists or tables.
- No old-data migration applies.

## Observability verification

- T1 makes expected behavior observable through `cases.yaml`.
- T2 records baseline behavior before prompt edits.
- T5-T10 record post-change behavior.
- T12 records validation command output and prompt length result.
- No logs, metrics, traces, or audit events are introduced.

## Security/privacy verification

- T8 verifies integrity-boundary behavior.
- T11 verifies no tools, external services, or live model CI are added.
- Fixture review verifies sanitized test data.

## Performance checks

- T12 records line-count evidence for `skills/editor/SKILL.md`.
- Static validation commands must remain deterministic.
- No runtime performance benchmark applies.

## Manual QA checklist

- Baseline evidence exists before `skills/editor/SKILL.md` changes.
- `cases.yaml` includes all four required scenario IDs.
- Simple proofreading returns corrected text only.
- PR-description polishing returns concise engineering-review wording.
- Russian translation returns Russian only.
- Misleading rewrite is refused or redirected with accurate wording.
- Notes appear only when requested or justified.
- No unrelated skill prompt is changed.
- Prompt length is shorter or length increase is justified.
- Required validation commands pass.

## What not to test and why

- Do not test live model behavior in CI; the approved spec forbids live model CI.
- Do not test unsupported target languages as acceptance behavior; EC9 keeps them outside this slice's acceptance contract.
- Do not test high-risk skill safety schemas; high-risk skills are out of scope.
- Do not test installer migration; install behavior and command names are unchanged.
- Do not add snapshot-only tests for prompt behavior; reviewer-readable scenario evidence is more useful for this prompt-only change.

## Uncovered gaps

None.

## Next artifacts

1. Implement M1 from `docs/plans/2026-05-25-editor-skill-optimization.md`.
2. Code review after each implemented milestone according to the plan.

## Follow-on artifacts

- `docs/changes/2026-05-25-editor-skill-optimization/reviews/test-spec-approval-r1.md`

## Readiness

Active proof surface for implementation M1.
