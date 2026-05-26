# Skill Quality Standard Test Spec

## Status

active

## Related spec and plan

- Spec: `specs/skill-quality-standard.md`
- Plan: `docs/plans/2026-05-25-skill-quality-standard.md`
- Architecture/ADRs: not applicable; plan-review approved no separate architecture artifact for this slice
- Amendment note: `specs/skill-quality-standard.md` is approved after manual owner review of the design-philosophy amendment. This active test-spec update is the approved proof surface for that amendment.
- Reviews:
  - `docs/changes/2026-05-25-rigorloop-governed-skill-quality/reviews/spec-review-r2.md`
  - `docs/changes/2026-05-25-rigorloop-governed-skill-quality/reviews/plan-review-r1.md`
  - `docs/changes/2026-05-25-rigorloop-governed-skill-quality/reviews/test-spec-approval-r1.md`

## Testing strategy

Use deterministic local tests only. The proof surface is a mix of unit tests for parser and validator helpers, integration tests for command behavior against temporary fixture repositories, smoke tests on the real repository, contract checks for docs and CI wiring, migration checks for omitted runtime-specific metadata and grandfathering, and manual review for subjective prompt quality and design-philosophy heuristics.

No test may call a live model or require network access. The first-slice README sync helper is report-only; a `--fix` mode is not required or tested in this slice. Reserved platform words are limited to `anthropic` and `claude` for first-slice validation; additional reserved words require a later accepted spec or review-resolution decision.

Expected commands after implementation:

```bash
python -m unittest discover tests
python tests/validate_skills.py
python tests/check_readme_sync.py
```

`python tests/check_readme_sync.py` may return warning-only status for staged README drift if the implementation documents that behavior. It must still report missing, extra, or mismatched entries clearly.

## Requirement coverage map

| Requirement ID | Covered by | Level | Notes |
| --- | --- | --- | --- |
| R1 | T1, T2 | unit, smoke | Skill path and missing `SKILL.md` validation. |
| R2 | T2 | unit | Lowercase hyphenated names, length, and first-slice reserved words `anthropic` and `claude`. |
| R3 | T2 | unit | Invalid YAML frontmatter fails. |
| R4 | T2 | unit | Required `name` and `description`. |
| R5 | T2, T8 | unit, migration | Missing `effort` passes; invalid present value fails; current skills omit it. |
| R6 | T8 | migration | Governance and contributor docs no longer require `argument-hint`, `effort`, or `allowed-tools`. |
| R7 | T2 | unit | Non-empty `allowed-tools` requires an accepted tool-using skill spec. |
| R8 | T2, T10 | unit, manual | Non-Latin metadata warning plus manual English-facing review. |
| R9 | T10 | manual | Review checklist verifies description explains what and when. |
| R10 | T10 | manual | Trigger-forward description quality stays reviewer-facing. |
| R11 | T2 | unit | Missing `$ARGUMENTS` fails. |
| R12 | T2 | unit | Missing `## Output Format` fails. |
| R13 | T3, T4 | integration | New and materially changed skills require three scenario categories. |
| R14 | T3 | integration | Scenarios must include concrete prompt or situation and expected behavior. |
| R15 | T3, T7 | integration, contract | Eval checks parse static fixtures; CI has no live model step. |
| R16 | T4 | integration | Grandfathering baseline schema, sortedness, stale entries, and new-skill behavior. |
| R17 | T5, T10 | integration, manual | Material skill change classification is tested for known changed surfaces and reviewed when uncertain. |
| R18 | T5 | integration | Name, description, output format, `$ARGUMENTS`, frontmatter, workflow, safety, and referenced-file changes are material. |
| R19 | T5 | integration | Editorial-only changes may avoid eval fixtures. |
| R20 | T5, T10 | integration, manual | Unclear cases are surfaced for review rather than silently treated as editorial. |
| R21 | T3, T10 | integration, manual | High-risk eval fixtures and safety notes. |
| R22 | T3, T10 | integration, manual | No detailed high-risk shared schema required in first slice. |
| R23 | T10 | manual | Mission-fit checklist for engineering and non-engineering productivity skills. |
| R24 | T2 | unit | Soft warning for `SKILL.md` length over the local warning threshold. |
| R25 | T2, T5 | unit, integration | New/materially changed skills over 500 lines fail without accepted exception. |
| R26 | T10 | manual | Review checks progressive disclosure for near-limit skills. |
| R27 | T10 | manual | Review checks table of contents for long reference files. |
| R28 | T6 | integration | README sync covers skill table, command list, and install instructions. |
| R29 | T6, T7 | integration, contract | README sync is a separate helper and CI step. |
| R30 | T2, T3, T6, T10 | unit, integration, manual | Blocking checks are objective; subjective checks are manual. |
| R31 | T10 | manual | Reviewer heuristics are not brittle CI gates. |
| R32 | T2, T3, T6 | unit, integration | Validation output or tests distinguish compatibility, Skillsmith policy, and reviewer heuristic classes. |
| R33 | T7 | contract | CI remains deterministic and has no live model execution. |
| R34 | T10 | manual | Manual model smoke evidence only for high-risk, behavior-heavy, or model-specific claims. |
| R35 | T1, T7, T11 | smoke, contract | Existing skills validate and installer remains usable. |
| R36 | T12 | manual | Reviewer checks one clear primary job or accepted broader boundary. |
| R37 | T12 | manual | Reviewer checks whether branches, effort scaling, fallbacks, or scenario accumulation are justified. |
| R38 | T12 | manual | Reviewer checks whether known failure modes are structurally designed out when practical. |
| R39 | T8, T12 | migration, manual | Optional metadata remains non-authoritative; behavior lives in the Markdown body. |
| R40 | T10, T12 | manual | Reviewer checks third-person function-first descriptions and distinguishing output shape where relevant. |
| R41 | T12 | manual | Reviewer checks whether durable directives replace unnecessary narrow rules. |
| R42 | T12 | manual | Reviewer checks verification or consistency steps for silent-drift risks. |
| R43 | T12 | manual | Reviewer checks vocabulary consistency across workflow instructions and output templates. |
| R44 | T12 | manual | Reviewer checks output contracts name concrete dimensions for required reasons, assessments, checks, or refusals. |
| R45 | T12 | manual | Reviewer checks known tradeoffs are recorded when accepted requirements deliberately choose them. |
| R46 | T12 | manual | Reviewer checks remaining prompt concerns are behavioral rather than cosmetic before requesting more wording changes. |
| R47 | T12 | manual | Design-philosophy heuristics are review evidence, notes, or checklist findings, not brittle CI gates. |

## Example coverage map

| Example | Covered by | Notes |
| --- | --- | --- |
| E1 | T3, T6 | New skill fixture requires frontmatter/body evidence, README sync, and three eval scenarios. |
| E2 | T5 | Editorial typo fixture avoids eval requirement. |
| E3 | T5 | Description change fixture is material and requires eval evidence. |
| E4 | T3, T10 | High-risk fixture and manual checklist require safety evidence. |
| E5 | T2, T8 | Runtime-specific metadata is omitted by default; non-empty tool permissions fail. |

## Edge case coverage

| Edge case | Covered by | Notes |
| --- | --- | --- |
| EC1 | T5 | Trigger-changing description typo is material. |
| EC2 | T5 | Added reference file is material. |
| EC3 | T5, T10 | High-risk safety wording is material unless reviewer records narrower rationale. |
| EC4 | T2, T8 | Missing `argument-hint`, `effort`, and `allowed-tools` passes. |
| EC5 | T2 | `effort: ultra` fails. |
| EC6 | T6 | README extra skill reports drift. |
| EC7 | T6 | README missing skill reports drift. |
| EC8 | T2, T5 | New/materially changed over-500-line skill fails without exception. |
| EC9 | T3 | Eval fixture missing indirect-trigger category reports the missing category. |
| EC10 | T10 | Model-specific claim requires manual model smoke evidence. |
| EC11 | T4 | Stale grandfathering baseline entry fails unless paired with same-change removal evidence. |
| EC12 | T4 | New unlisted skill without `cases.yaml` fails before merge. |

## Test cases

### T1. Current repository validation smoke

- Covers: R1, R35, AC5, AC10
- Level: smoke
- Fixture/setup: current repository state after implementation.
- Steps:
  - Run `python tests/validate_skills.py`.
- Expected result: command exits 0, reports the number of skills checked, and reports all current skills passing.
- Failure proves: the first slice broke existing skill validation or repository layout.
- Automation location: `tests/validate_skills.py`

### T2. Per-skill validator fixtures

- Covers: R1-R12, R24, R25, R30, R32, E5, EC4, EC5, EC8
- Level: unit
- Fixture/setup: temporary skill directories or fixture files covering valid skill, missing `SKILL.md`, invalid YAML, missing required fields, invalid name, reserved name, non-empty `allowed-tools`, missing `$ARGUMENTS`, missing `## Output Format`, missing optional metadata, invalid `effort`, non-Latin metadata, 300-line warning, and 500-line ceiling.
- Steps:
  - Run validator helper tests against each fixture.
  - Assert expected errors and warnings by rule category.
- Expected result: objective compatibility and Skillsmith-policy failures are errors; non-Latin metadata and 300-line length are warnings; missing `argument-hint`, `effort`, and `allowed-tools` is neither an error nor a warning; invalid present `effort` is an error.
- Failure proves: per-skill validation does not match the approved compatibility and policy contract.
- Automation location: `tests/test_validate_skills.py` via `python -m unittest discover tests`

### T3. Eval fixture schema and category validation

- Covers: R13-R15, R21, R22, R30-R32, E1, E4, EC9
- Level: integration
- Fixture/setup: temporary `tests/evals/skills/<skill-name>/cases.yaml` fixtures for complete normal/indirect/edge coverage, missing category, abstract expected behavior, malformed YAML, and high-risk safety or misuse coverage.
- Steps:
  - Run eval fixture validation against each fixture.
  - Assert missing or malformed scenario output identifies the skill and category.
  - Assert high-risk fixtures require lightweight safety evidence but not a shared domain schema.
- Expected result: valid static fixtures pass; missing categories and malformed scenarios fail or warn according to staged enforcement; no live model call is attempted.
- Failure proves: eval fixtures are not reviewable or validation depends on runtime model behavior.
- Automation location: `tests/test_validate_skills.py` or `tests/test_eval_fixtures.py` via `python -m unittest discover tests`

### T4. Grandfathering baseline validation

- Covers: R16, AC11-AC14, EC11, EC12
- Level: integration
- Fixture/setup: temporary skills tree plus `tests/evals/skills/grandfathered-skills.yaml` variants for sorted valid baseline, unsorted baseline, path-valued entry, stale entry, grandfathered skill without `cases.yaml`, and unlisted new skill without `cases.yaml`.
- Steps:
  - Run grandfathering validation.
  - Assert baseline schema fields, sorted bare names, and existing directory checks.
  - Assert grandfathered skills may lack eval fixtures only while unchanged.
  - Assert unlisted new skills require `cases.yaml`.
- Expected result: baseline artifact is the only grandfathering source; stale or malformed entries fail; unlisted new skills without eval fixtures fail.
- Failure proves: grandfathering is nondeterministic or tied to branch, README, or commit inference.
- Automation location: `tests/test_validate_skills.py` or `tests/test_eval_fixtures.py` via `python -m unittest discover tests`

### T5. Material-change classification fixtures

- Covers: R17-R20, R25, EC1, EC2, EC3
- Level: integration
- Fixture/setup: paired before/after temporary skill trees for editorial typo, description trigger change, output format change, `$ARGUMENTS` handling change, execution-affecting frontmatter change, workflow-step change, safety-rule change, added reference file, and high-risk safety wording change.
- Steps:
  - Run materiality helper or change-classification test against each pair.
  - Assert known material surfaces require eval fixtures.
  - Assert editorial-only fixture does not require eval fixtures.
  - Assert ambiguous cases are surfaced for reviewer classification.
- Expected result: material changes are not silently treated as editorial; editorial-only changes avoid unnecessary eval work.
- Failure proves: eval gating cannot be applied safely to new and materially changed skills.
- Automation location: `tests/test_material_changes.py` via `python -m unittest discover tests`

### T6. README synchronization helper

- Covers: R28, R29, R30, R32, E1, EC6, EC7, AC8
- Level: integration
- Fixture/setup: temporary README variants with complete sync, missing skill table row, extra skill table row, missing slash command, extra slash command, stale install URL, and current Skillsmith install URL.
- Steps:
  - Run `python tests/check_readme_sync.py` against fixture inputs or helper functions.
  - Run `python tests/check_readme_sync.py` against the real README after implementation.
- Expected result: helper reports missing, extra, or mismatched README entries across table, command list, and install instructions. First-slice helper is report-only; no `--fix` mode is required.
- Failure proves: README drift is not detectable or is incorrectly coupled to per-skill validation.
- Automation location: `tests/check_readme_sync.py` and `tests/test_check_readme_sync.py`

### T7. CI deterministic contract

- Covers: R15, R29, R33, R35, AC9
- Level: integration
- Fixture/setup: `.github/workflows/validate.yml` after implementation.
- Steps:
  - Inspect workflow steps.
  - Assert CI runs `python tests/validate_skills.py`.
  - Assert CI runs `python tests/check_readme_sync.py` once the helper exists.
  - Assert workflow contains no live model, provider API, secret-dependent, or network test step beyond checkout, Python setup, and dependency installation.
- Expected result: CI gates deterministic local checks only.
- Failure proves: the first slice introduced nondeterministic CI or omitted a required check.
- Automation location: `tests/test_ci_contract.py` via `python -m unittest discover tests`

### T8. Runtime-specific metadata migration checks

- Covers: R5, R6, AC3, AC4, E5
- Level: integration
- Fixture/setup: repository docs after M1 and validator after M2.
- Steps:
  - Search `CONSTITUTION.md`, `AGENTS.md`, `CONTRIBUTING.md`, README, and `.github/pull_request_template.md` for statements that require `argument-hint`, `effort`, `effort: high`, or `allowed-tools: ""`.
  - Run validator fixtures with absent runtime-specific metadata, invalid present `effort`, and non-empty `allowed-tools`.
- Expected result: docs tell contributors to omit optional frontmatter by default; validation permits absence, rejects invalid present `effort`, and rejects non-empty tool permissions without an accepted tool-using spec.
- Failure proves: governance or validation still contradicts portability-first metadata omission.
- Automation location: `tests/test_governance_docs.py` and `tests/test_validate_skills.py` via `python -m unittest discover tests`

### T9. Contributor and PR evidence contract

- Covers: R6, R21, R23, R34, AC4, AC7
- Level: integration
- Fixture/setup: `CONTRIBUTING.md`, `AGENTS.md`, `CLAUDE.md`, README, and `.github/pull_request_template.md` after M1.
- Steps:
  - Inspect docs for material-change classification, eval scenario expectations, high-risk safety notes, manual model smoke triggers, validation command output, and links to `specs/skill-quality-standard.md`.
- Expected result: contributor-facing docs summarize the approved standard without duplicating it as a second canonical standard.
- Failure proves: reviewers and contributors do not have visible evidence expectations.
- Automation location: `tests/test_governance_docs.py` via `python -m unittest discover tests`

### T10. Manual quality and safety review checklist

- Covers: R8-R10, R17-R23, R26, R27, R31, R34, R40, EC3, EC10
- Level: manual
- Fixture/setup: PR or change-local evidence for any new or materially changed skill.
- Steps:
  - Confirm `description` explains what the skill does and when to use it.
  - Confirm trigger quality, mission fit, concision, progressive disclosure, and safety adequacy are reviewed without brittle CI gating.
  - For high-risk or behavior-heavy changes, confirm scope boundaries, refusal or escalation behavior, safety notes, and manual model smoke evidence where required.
  - For model-specific claims, confirm the PR records model, prompt, and result summary.
- Expected result: subjective quality is visible to reviewers and not hidden in automated pass/fail checks.
- Failure proves: the review process cannot assess prompt quality and safety beyond structure.
- Automation location: manual checklist in `.github/pull_request_template.md` or `CONTRIBUTING.md`

### T11. Existing skill installability smoke

- Covers: R35
- Level: smoke
- Fixture/setup: repository after implementation.
- Steps:
  - Run `bash install.sh --target "$(mktemp -d)"`.
  - Inspect the target directory for installed skill command files or skill directories expected by the installer.
- Expected result: installer completes successfully and existing skills remain installable.
- Failure proves: the first slice broke the install surface while changing validation or docs.
- Automation location: manual/local smoke command; may become `tests/test_install_smoke.py` only if the plan is revised to add installer automation.

### T12. Manual skill design philosophy review checklist

- Covers: R36-R47
- Level: manual
- Fixture/setup: PR or change-local evidence for any new or materially changed skill, including the skill prompt, eval scenarios, review notes, and accepted proposal/spec tradeoffs.
- Steps:
  - Confirm the skill has one clear primary job, or that the accepted proposal/spec justifies a broader boundary.
  - Confirm branches, input-type detection, effort scaling, fallbacks, or scenario accumulation are absent unless accepted requirements require them.
  - Confirm known failure modes are handled structurally where practical, rather than only through repeated warnings.
  - Confirm behavior-defining instructions live in the Markdown body and do not depend on optional frontmatter.
  - Confirm the description uses third-person descriptive language, states the function before trigger situations, and names distinguishing output shape when it affects selection.
  - Confirm the prompt uses a small set of durable directives where they cover the same behavior as many narrow rules.
  - Confirm quality-critical workflows include a verification or consistency-check step when output can silently drift.
  - Confirm workflow instructions and output templates use consistent vocabulary.
  - Confirm output sections, reasons, assessments, checks, and refusals name concrete dimensions instead of vague instructions.
  - Confirm known tradeoffs, including fixed output verbosity for trivial input, are recorded when accepted requirements choose them.
  - Confirm reviewers stop at behavioral eval evidence once remaining prompt concerns are cosmetic.
  - Confirm design-philosophy concerns are captured as review notes or checklist findings, not hard-coded as brittle CI gates.
- Expected result: reviewer-visible evidence shows how the skill follows or intentionally departs from the design philosophy, with tradeoffs recorded when requirements override generic best practice.
- Failure proves: skill design philosophy cannot be reviewed consistently without turning subjective heuristics into brittle automation.
- Automation location: manual checklist in `.github/pull_request_template.md`, `CONTRIBUTING.md`, or change-local review notes after the amendment is approved.

## Fixtures and data

- `tests/evals/skills/grandfathered-skills.yaml`: real baseline artifact for current repository smoke and migration tests.
- `tests/fixtures/skills/` or temporary directories created by unit tests: valid and invalid `SKILL.md` files.
- `tests/fixtures/evals/` or temporary files: valid and invalid `cases.yaml` examples.
- `tests/fixtures/readme/` or inline temporary README strings: synchronized and drifted README examples.
- All fixture prompts, expected outputs, and high-risk examples must be fictional or sanitized.

## Mocking/stubbing policy

Use temporary directories and monkeypatchable parser inputs instead of modifying real `skills/` during tests. Mock or inject repository roots where needed so tests do not depend on the developer's current branch state. Do not mock YAML parsing, filesystem existence checks, or command exit behavior for validator and README helper contract tests.

No live model, network provider, secret, external service, or real user data may be used.

## Migration or compatibility tests

- T4 proves grandfathering uses the checked-in baseline artifact rather than commit, branch, README, or future implementation state.
- T8 proves `argument-hint`, `effort`, and `allowed-tools` are omitted by default in docs and validation.
- T7 proves CI stays deterministic.
- T11 proves existing skills remain installable.
- README sync `--fix` mode is intentionally not part of the first-slice compatibility contract.
- Reserved platform word enforcement is intentionally limited to `anthropic` and `claude` in this first slice.

## Observability verification

- `tests/validate_skills.py` output must report the number of skills checked and distinguish warnings from errors.
- Eval fixture validation output must identify the skill and missing or malformed scenario category.
- README sync output must identify missing, extra, or mismatched README entries.
- PR or change evidence must include validation command output or explain why a check could not be run.

## Security/privacy verification

- Fixture tests must reject or flag obvious secrets only if the implementation includes a deterministic secret pattern; otherwise privacy is manually checked through T10.
- Eval fixture review must confirm examples use fictional or sanitized inputs.
- High-risk skill review must confirm the skill does not present itself as a substitute for licensed professionals, emergency services, official advice, or authorized security review.
- CI and validation tests must confirm no provider secret or live model step is required.

## Performance checks

- Smoke validation must complete fast enough for ordinary pre-PR use on the current 10-skill repository.
- No hard time threshold is required in the first slice; reviewers should investigate if `python tests/validate_skills.py` or `python tests/check_readme_sync.py` becomes noticeably slow for local use.
- Eval fixture checks must parse static files only.

## Manual QA checklist

- For any new or materially changed skill, confirm the three eval scenario categories are meaningful, concrete, and tied to expected observable behavior.
- For high-risk skills, confirm scope boundaries, refusal or escalation behavior, safety notes, and one safety or misuse scenario.
- For model-specific claims, confirm manual smoke evidence records model, prompt, and result summary.
- Confirm docs link to `specs/skill-quality-standard.md` rather than creating a second canonical standard.
- Confirm warnings introduced for grandfathering, README drift, or length thresholds are actionable rather than noisy.
- For new or materially changed skills, confirm design-philosophy tradeoffs are recorded when requirements intentionally override generic best practice.
- Confirm vocabulary does not drift between workflow steps and output templates.
- Confirm reviewers move to eval evidence once prompt wording concerns become cosmetic.

## What not to test and why

- Do not test live model output in CI; R15 and R33 explicitly prohibit live model dependency in this first slice.
- Do not require a README `--fix` mode; the first-slice contract is drift reporting.
- Do not enforce detailed medical, legal, financial, or security schemas; R22 defers shared high-risk schemas.
- Do not hard-block subjective trigger quality, concision, mission fit, or safety adequacy through brittle CI; these are reviewer heuristics.
- Do not hard-block design-philosophy heuristics such as simplicity, branch avoidance, body-owned behavior, vocabulary precision, fixed output shape, or tradeoff handling through brittle CI.
- Do not test `.claude-plugin` or plugin metadata validation; the accepted proposal and spec exclude it.
- Do not backfill eval fixtures for all grandfathered existing skills in this slice unless a skill is materially changed.

## Uncovered gaps

None blocking. The source spec is approved after manual owner review, and this test spec records approved proof coverage for the design-philosophy amendment.

The two approved-spec open questions are settled for this first test spec as follows: README sync reports drift and does not need `--fix`; reserved platform words are `anthropic` and `claude` only.

## Next artifacts

1. Implementation planning or governance-doc updates only if downstream implementation of R36-R47 is explicitly requested.
2. Code review, explain-change, verify, and PR handoff after any approved downstream implementation.

## Follow-on artifacts

None yet.

## Readiness

Active approved proof surface for the design-philosophy amendment.
