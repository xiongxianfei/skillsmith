# Plan: Skill Quality Standard First Slice

## Status

- Status: draft
- Plan lifecycle state: active
- Terminal disposition: not-terminal

## Purpose / big picture

Implement the accepted Skill Quality Standard first slice without rewriting existing skills. The work updates governance and contributor docs, adds deterministic validation for objective rules, adds eval-fixture and grandfathering support, and keeps subjective prompt quality in review evidence instead of brittle CI.

## Source artifacts

- Proposal: `docs/proposals/2026-05-25-rigorloop-governed-skill-quality.md`
- Spec: `specs/skill-quality-standard.md`
- Architecture: not-required; spec-review did not require a separate architecture assessment
- Test spec: `specs/skill-quality-standard.test.md`
- Review evidence:
  - `docs/changes/2026-05-25-rigorloop-governed-skill-quality/reviews/proposal-review-r2.md`
  - `docs/changes/2026-05-25-rigorloop-governed-skill-quality/reviews/spec-review-r2.md`
  - `docs/changes/2026-05-25-rigorloop-governed-skill-quality/review-resolution.md`

## Context and orientation

Skillsmith is a Markdown prompt-skill repository. Skill behavior lives in `skills/<skill-name>/SKILL.md`; current validation lives in `tests/validate_skills.py`; repository guidance lives in `CONSTITUTION.md`, `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, and `README.md`; CI runs the validator through `.github/workflows/validate.yml`.

The current validator is per-skill and structural. The first slice must preserve that fast local path while adding separate cross-artifact checks for README synchronization and static eval-fixture coverage. Existing skills are grandfathered for eval fixtures through `tests/evals/skills/grandfathered-skills.yaml`.

## Non-goals

- Do not rewrite all existing skills.
- Do not add live model execution to CI.
- Do not add tool-using skill behavior.
- Do not reintroduce `.claude-plugin` or plugin metadata validation.
- Do not make subjective description quality a hard CI gate.
- Do not create a second canonical skill-quality standard under `docs/`.

## Requirements covered

- R1-R12: M2
- R13-R20: M3
- R21-R23: M1, M3
- R24-R27: M2, M3
- R28-R29: M4
- R30-R35: M1-M5
- AC1: already satisfied by `specs/skill-quality-standard.md`
- AC2: downstream `test-spec` gate before implementation
- AC3-AC4: M1
- AC5-AC7: M2, M3, M5
- AC8: M4
- AC9-AC10: M5
- AC11-AC13: baseline exists before planning; M3 keeps it validated
- AC14: M3

## Current Handoff Summary

- Current milestone: final closeout
- Current milestone state: branch-ready
- Last reviewed milestone: M5. CI and full-slice validation
- Review status: code-review M5 R1 clean-with-notes; M5 closed
- Remaining in-scope implementation milestones: none
- Next stage: pr
- Final closeout readiness: ready for PR handoff
- Reason final closeout is or is not ready: all implementation milestones are closed, explain-change is current, final verify passed, and PR handoff remains.

## Milestones

### M1. Governance and contributor guidance alignment

- Milestone state: closed
- Goal: Align governing and contributor-facing docs with the approved standard, especially optional `effort` and lightweight high-risk evidence.
- Requirements: R5, R6, R21-R23, R30-R35, AC3, AC4, AC7, AC9
- Files/components likely touched:
  - `CONSTITUTION.md`
  - `AGENTS.md`
  - `CLAUDE.md`
  - `CONTRIBUTING.md`
  - `.github/pull_request_template.md`
  - `README.md`
- Dependencies:
  - approved spec
  - plan-review before implementation
  - test spec before implementation
- Tests to add/update:
  - documented in `specs/skill-quality-standard.test.md`
  - local stale-text searches for required `effort: high`, `.claude-plugin`, and old naming
- Implementation steps:
  - update `CONSTITUTION.md` compatibility rules so `effort` is optional and validated only when present
  - update agent and contributor docs so `effort` is no longer required
  - add contributor expectations for eval scenarios, material-change classification, high-risk safety notes, and manual model smoke evidence triggers
  - ensure docs do not reintroduce plugin metadata requirements
- Validation commands:
  - `python tests/validate_skills.py`
  - `rg -n "effort: high|required.*effort|\\.claude-plugin|ai-skills" AGENTS.md CLAUDE.md CONTRIBUTING.md README.md CONSTITUTION.md .github || true`
- Expected observable result: docs describe the same optional-`effort`, pure-prompt, eval-first contribution rules as the approved spec.
- Commit message: `M1: align governance and contribution docs`
- Milestone closeout:
  - validation passed for M1 targeted checks
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone commit not created in this working tree handoff; changes are ready for code-review as an uncommitted working tree slice
- Risks:
  - duplicated guidance drifts from the spec
- Rollback/recovery:
  - revert doc edits for this milestone and keep the spec as the source of truth

### M2. Per-skill validator rule updates

- Milestone state: closed
- Goal: Update `tests/validate_skills.py` for objective per-skill rules in the approved standard while keeping subjective heuristics as warnings or review evidence.
- Requirements: R1-R12, R24-R27, R30-R33, R35, AC5, AC10
- Files/components likely touched:
  - `tests/validate_skills.py`
  - `tests/fixtures/` or equivalent validator fixtures if introduced by the test spec
- Dependencies:
  - M1 guidance alignment
  - test spec coverage for validator behavior
- Tests to add/update:
  - parseable YAML
  - required `name`, `description`, `argument-hint`, and `allowed-tools`
  - optional `effort` accepted when absent
  - invalid `effort` rejected when present
  - name syntax and reserved words
  - `$ARGUMENTS` and `## Output Format`
  - `allowed-tools: ""` for pure-prompt skills
  - length warning and ceiling behavior
- Implementation steps:
  - classify checks as compatibility rule, Skillsmith policy, or reviewer heuristic
  - make missing `effort` non-blocking and non-warning by itself
  - validate allowed `effort` values only when present
  - add objective skill-name, allowed-tools, and line-count checks
  - preserve current validator output shape with clear warnings and errors
- Validation commands:
  - `python tests/validate_skills.py`
  - targeted validator fixture command defined by the test spec
- Expected observable result: all current skills continue to pass deterministic validation after grandfathering and optional-effort handling.
- Commit message: `M2: update per-skill validator rules`
- Milestone closeout:
  - validation passed for M2 targeted checks
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - milestone commit not created in this working tree handoff; changes are ready for code-review as an uncommitted working tree slice
- Risks:
  - validator becomes too broad or blocks subjective quality judgments
- Rollback/recovery:
  - narrow the new checks to warnings or remove the last added check while preserving existing structural validation

### M3. Eval fixture and grandfathering support

- Milestone state: closed
- Goal: Add static eval-fixture validation and grandfathering behavior using the checked-in baseline artifact.
- Requirements: R13-R20, R21, R30-R35, AC5-AC7, AC11-AC14
- Files/components likely touched:
  - `tests/evals/skills/grandfathered-skills.yaml`
  - `tests/evals/skills/<skill-name>/cases.yaml` convention
  - `tests/validate_skills.py` or a focused eval validation helper if the test spec selects one
  - `CONTRIBUTING.md`
- Dependencies:
  - M2 validator structure
  - test spec decision on eval fixture schema and helper placement
- Tests to add/update:
  - grandfathered skill may lack `cases.yaml`
  - unlisted new skill requires `cases.yaml`
  - stale baseline entry fails
  - scenario categories cover normal, indirect trigger, and edge/safety/failure/non-trigger/misuse
  - high-risk material change evidence requires safety or misuse coverage
- Implementation steps:
  - parse `tests/evals/skills/grandfathered-skills.yaml`
  - validate version, source metadata, sorted bare skill names, and existing skill directories
  - define and validate minimal `cases.yaml` scenario categories
  - surface uncertainty when material-change detection cannot be mechanically determined
  - keep live model calls out of CI
- Validation commands:
  - `python tests/validate_skills.py`
  - targeted eval fixture validation command defined by the test spec
- Expected observable result: grandfathered skills can remain without eval fixtures until materially changed, while new or non-grandfathered skills require static eval evidence.
- Commit message: `M3: add eval fixture validation`
- Milestone closeout:
  - validation passed for M3 targeted checks
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - code-review R1 found F-CODE-M3-001; milestone requires review-resolution before closeout
  - F-CODE-M3-001 resolved pending code-review re-review
  - code-review R2 returned clean-with-notes and closed M3
  - milestone commit not created in this working tree handoff
- Risks:
  - material-change detection cannot be fully reliable from local file state alone
- Rollback/recovery:
  - require explicit reviewer classification for uncertain materiality and keep mechanical checks limited to new, unlisted skills

### M4. README synchronization helper

- Milestone state: closed
- Goal: Add a separate cross-artifact README sync check for the skill table, slash-command list, and install instructions.
- Requirements: R28-R29, R30-R33, AC8, AC10
- Files/components likely touched:
  - `tests/check_readme_sync.py`
  - `README.md`
  - `.github/workflows/validate.yml`
  - `CONTRIBUTING.md`
- Dependencies:
  - M2 parser helpers may be reused if practical without coupling the helper to per-skill validation
- Tests to add/update:
  - missing README skill entry
  - extra README skill entry
  - command list drift
  - install instruction drift for repository naming
- Implementation steps:
  - parse skill frontmatter from `skills/*/SKILL.md`
  - compare repository skill directories with README table and command list
  - check install instructions for current Skillsmith repository naming
  - invoke the helper from CI alongside `tests/validate_skills.py`
  - decide through the test spec whether first-slice README drift is warning-only or blocking
- Validation commands:
  - `python tests/check_readme_sync.py`
  - `python tests/validate_skills.py`
- Expected observable result: README drift is reported by a focused helper without mixing doc parsing into the per-skill validator.
- Commit message: `M4: add README sync check`
- Milestone closeout:
  - validation passed for M4 targeted checks
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - CI wiring intentionally left for M5, which owns deterministic workflow integration
  - code-review R1 returned clean-with-notes and closed M4
  - milestone commit not created in this working tree handoff; changes are ready for code-review as an uncommitted working tree slice
- Risks:
  - README format changes make the helper brittle
- Rollback/recovery:
  - keep helper warning-only until README markers or a generated table format are stable

### M5. CI and full-slice validation

- Milestone state: closed
- Goal: Wire deterministic checks together and prove the first slice keeps existing skills installable and validation fast.
- Requirements: R30-R35, AC5, AC9, AC10
- Files/components likely touched:
  - `.github/workflows/validate.yml`
  - `tests/validate_skills.py`
  - `tests/check_readme_sync.py`
  - `install.sh` if validation exposes installer doc drift
- Dependencies:
  - M1-M4 complete or intentionally deferred by review decision
- Tests to add/update:
  - CI runs validator
  - CI runs README sync helper when present
  - no CI step requires live model calls or network access beyond normal checkout/dependency setup
- Implementation steps:
  - update CI to run all deterministic local checks
  - run the full local validation set
  - record validation output in plan progress and change evidence
  - keep install path unchanged unless a failing check proves drift
- Validation commands:
  - `python tests/validate_skills.py`
  - `python tests/check_readme_sync.py`
  - any targeted test command required by `specs/skill-quality-standard.test.md`
- Expected observable result: the first slice has deterministic local and CI validation, and current skills remain installable.
- Commit message: `M5: wire skill quality checks into CI`
- Milestone closeout:
  - validation passed for M5 targeted checks
  - progress updated
  - decision log updated if needed
  - validation notes updated
  - installability smoke passed for 10 skills
  - code-review R1 returned clean-with-notes and closed M5
  - milestone commit not created in this working tree handoff; changes are ready for code-review as an uncommitted working tree slice
- Risks:
  - CI gating becomes stricter than the spec intends during grandfathering
- Rollback/recovery:
  - downgrade staged checks to warnings while preserving error checks for existing structural rules

## Validation plan

- `python tests/validate_skills.py`: default repository validation and existing skill pass check
- `python tests/check_readme_sync.py`: README skill table, command list, and install instruction drift once helper exists
- targeted validator fixture command from `specs/skill-quality-standard.test.md`: regression coverage for new validation rules
- `rg -n "effort: high|required.*effort|\\.claude-plugin|ai-skills" AGENTS.md CLAUDE.md CONTRIBUTING.md README.md CONSTITUTION.md .github || true`: stale governance and naming checks
- manual review of `tests/evals/skills/grandfathered-skills.yaml`: baseline sortedness and existing-directory coverage

## Risks and recovery

- Risk: first-slice validation blocks grandfathered skills unexpectedly.
  - Recovery: make the new eval and README checks warning-only where the spec allows staged enforcement.
- Risk: docs duplicate the spec and drift.
  - Recovery: keep docs concise and link to `specs/skill-quality-standard.md` for normative detail.
- Risk: material-change detection is not mechanically knowable in every CI context.
  - Recovery: require reviewer classification for uncertain changes and block only objectively new or unlisted skills mechanically.
- Risk: README sync parsing becomes brittle.
  - Recovery: introduce stable README markers or keep the helper warning-only until format stability is proven.

## Dependencies

- Plan review passed in `docs/changes/2026-05-25-rigorloop-governed-skill-quality/reviews/plan-review-r1.md`.
- `specs/skill-quality-standard.test.md` exists and is the active proof surface for implementation.
- Architecture assessment is not required unless plan-review or test-spec exposes a long-lived design decision.
- Code review is required after implementation because the change affects validator logic, CI, templates, and contributor policy.

## Progress

- 2026-05-25: Created plan from accepted proposal, approved spec, and spec-review R2.
- 2026-05-25: Ran current repository validation and grandfathering baseline sanity check for plan handoff evidence.
- 2026-05-25: Plan-review R1 approved the plan; created `specs/skill-quality-standard.test.md` as the active proof surface for implementation.
- 2026-05-25: Owner approved `specs/skill-quality-standard.test.md`; recorded approval in `docs/changes/2026-05-25-rigorloop-governed-skill-quality/reviews/test-spec-approval-r1.md`.
- 2026-05-25: Implemented M1 governance and contributor guidance alignment; M1 is ready for code-review.
- 2026-05-25: Code-review M1 R1 returned clean-with-notes and closed M1.
- 2026-05-25: Implemented M2 per-skill validator rule updates; M2 is ready for code-review.
- 2026-05-25: Code-review M2 R1 requested changes for F-CODE-M2-001; M2 moved to resolution-needed.
- 2026-05-25: Resolved F-CODE-M2-001 by adding the missing T2 unit tests; M2 returned to review-requested.
- 2026-05-25: Code-review M2 R2 returned clean-with-notes and closed M2.
- 2026-05-25: Implemented M3 eval fixture and grandfathering support; M3 is ready for code-review.
- 2026-05-25: Code-review M3 R1 requested changes for F-CODE-M3-001; M3 moved to resolution-needed.
- 2026-05-25: Resolved F-CODE-M3-001 by validating non-string grandfathering baseline entries before sortedness checks; M3 returned to review-requested.
- 2026-05-25: Code-review M3 R2 returned clean-with-notes and closed M3.
- 2026-05-25: Implemented M4 README synchronization helper; M4 is ready for code-review.
- 2026-05-25: Code-review M4 R1 returned clean-with-notes and closed M4.
- 2026-05-25: Implemented M5 CI and full-slice validation; M5 is ready for code-review.
- 2026-05-25: Code-review M5 R1 returned clean-with-notes and closed M5.
- 2026-05-25: Final verify passed and recorded branch-ready evidence.

## Decision log

| Date | Decision | Reason | Alternatives rejected |
| --- | --- | --- | --- |
| 2026-05-25 | Split work into docs, validator, eval, README sync, and CI milestones. | The spec touches multiple ownership areas, and separate milestones keep review focused. | One large implementation milestone. |
| 2026-05-25 | Treat architecture as not required for this slice unless a downstream review finds a design decision. | The accepted spec changes repository validation and workflow artifacts without adding runtime services, dependencies, data flow, or persistent architecture boundaries. | Creating architecture solely because it appears in the generic lifecycle. |
| 2026-05-25 | Keep README sync drift warning-only in M4. | The approved spec says README drift starts as a warning, and M5 owns CI wiring after the helper is proven reliable. | Making README drift blocking in the first helper slice. |
| 2026-05-25 | Keep installability proof as a local smoke command rather than a CI job. | The approved CI contract avoids extra network beyond checkout/setup; `install.sh` clones from GitHub and is better as local release evidence in this slice. | Running installer smoke in CI. |

## Surprises and discoveries

- M3 material-change detection cannot be fully inferred from the current local tree alone, so the validator mechanically blocks unlisted new skills without fixtures and keeps material-change classification as reviewer evidence for existing grandfathered skills.

## Validation notes

- 2026-05-25: `python tests/validate_skills.py` passed: 10 skills checked, all passed.
- 2026-05-25: Grandfathering baseline sanity check passed: 10 entries, lexicographically sorted, no missing `skills/<skill-name>/` directories.
- 2026-05-25: M1 proof-before-edit found stale required-effort guidance in `CONSTITUTION.md`, `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, and `.github/pull_request_template.md`.
- 2026-05-25: M1 targeted validation passed: `python tests/validate_skills.py` checked 10 skills and all passed.
- 2026-05-25: M1 stale-guidance check passed with no matches: `rg -n "effort: high|required.*effort|\.claude-plugin|ai-skills" AGENTS.md CLAUDE.md CONTRIBUTING.md README.md CONSTITUTION.md .github || true`.
- 2026-05-25: `python -m unittest discover tests` was inspected but skipped as not applicable for M1 because no test modules exist yet; command exits with "NO TESTS RAN".
- 2026-05-25: M2 proof-before-fix failed as expected: `python -m unittest tests/test_validate_skills.py` reported errors because the old validator returned `None` from `validate_skill`.
- 2026-05-25: M2 targeted tests passed: `python -m unittest tests/test_validate_skills.py` ran 9 tests and passed.
- 2026-05-25: M2 broad test discovery passed: `python -m unittest discover tests` ran 9 tests and passed.
- 2026-05-25: M2 repository validation passed: `python tests/validate_skills.py` checked 10 skills and all passed.
- 2026-05-25: M2 whitespace validation passed: `git diff --check`.
- 2026-05-25: F-CODE-M2-001 resolution validation passed: `python -m unittest tests/test_validate_skills.py` ran 13 tests and passed.
- 2026-05-25: F-CODE-M2-001 resolution broad discovery passed: `python -m unittest discover tests` ran 13 tests and passed.
- 2026-05-25: F-CODE-M2-001 resolution repository validation passed: `python tests/validate_skills.py` checked 10 skills and all passed.
- 2026-05-25: F-CODE-M2-001 resolution whitespace validation passed: `git diff --check`.
- 2026-05-25: M3 proof-before-fix failed as expected: `python -m unittest tests/test_eval_fixtures.py` reported missing `validate_eval_fixtures`.
- 2026-05-25: M3 targeted eval fixture tests passed: `python -m unittest tests/test_eval_fixtures.py` ran 8 tests and passed.
- 2026-05-25: M3 broad test discovery passed: `python -m unittest discover tests` ran 21 tests and passed.
- 2026-05-25: M3 repository validation passed: `python tests/validate_skills.py` checked 10 skills, passed, and reported one aggregate warning for grandfathered skills without eval fixtures.
- 2026-05-25: F-CODE-M3-001 proof-before-fix failed as expected: `python -m unittest tests/test_eval_fixtures.py` raised `TypeError` for a non-string `grandfathered_skills` entry.
- 2026-05-25: F-CODE-M3-001 resolution validation passed: `python -m unittest tests/test_eval_fixtures.py` ran 9 tests and passed.
- 2026-05-25: F-CODE-M3-001 resolution broad discovery passed: `python -m unittest discover tests` ran 22 tests and passed.
- 2026-05-25: F-CODE-M3-001 resolution repository validation passed: `python tests/validate_skills.py` checked 10 skills, passed, and reported one aggregate warning for grandfathered skills without eval fixtures.
- 2026-05-25: F-CODE-M3-001 resolution whitespace validation passed: `git diff --check`.
- 2026-05-25: M3 re-review validation passed: `python -m unittest tests/test_eval_fixtures.py` ran 9 tests and passed.
- 2026-05-25: M3 re-review broad discovery passed: `python -m unittest discover tests` ran 22 tests and passed.
- 2026-05-25: M3 re-review repository validation passed: `python tests/validate_skills.py` checked 10 skills, passed, and reported one aggregate warning for grandfathered skills without eval fixtures.
- 2026-05-25: M3 re-review whitespace validation passed: `git diff --check`.
- 2026-05-25: M4 proof-before-fix failed as expected: `python -m unittest tests/test_check_readme_sync.py` reported missing `check_readme_sync`.
- 2026-05-25: M4 targeted README sync tests passed: `python -m unittest tests/test_check_readme_sync.py` ran 7 tests and passed.
- 2026-05-25: M4 broad test discovery passed: `python -m unittest discover tests` ran 29 tests and passed.
- 2026-05-25: M4 real README sync passed: `python tests/check_readme_sync.py`.
- 2026-05-25: M4 repository validation passed: `python tests/validate_skills.py` checked 10 skills, passed, and reported one aggregate warning for grandfathered skills without eval fixtures.
- 2026-05-25: M4 whitespace validation passed: `git diff --check`.
- 2026-05-25: M4 review validation passed: `python -m unittest tests/test_check_readme_sync.py` ran 7 tests and passed.
- 2026-05-25: M4 review broad discovery passed: `python -m unittest discover tests` ran 29 tests and passed.
- 2026-05-25: M4 review real README sync passed: `python tests/check_readme_sync.py`.
- 2026-05-25: M4 review repository validation passed: `python tests/validate_skills.py` checked 10 skills, passed, and reported one aggregate warning for grandfathered skills without eval fixtures.
- 2026-05-25: M4 review whitespace validation passed: `git diff --check`.
- 2026-05-25: M5 proof-before-fix failed as expected: `python -m unittest tests/test_ci_contract.py` showed CI did not run `python -m unittest discover tests` or `python tests/check_readme_sync.py`.
- 2026-05-25: M5 CI contract tests passed: `python -m unittest tests/test_ci_contract.py` ran 2 tests and passed.
- 2026-05-25: M5 broad test discovery passed: `python -m unittest discover tests` ran 31 tests and passed.
- 2026-05-25: M5 README sync passed: `python tests/check_readme_sync.py`.
- 2026-05-25: M5 repository validation passed: `python tests/validate_skills.py` checked 10 skills, passed, and reported one aggregate warning for grandfathered skills without eval fixtures.
- 2026-05-25: M5 installability smoke passed: `bash install.sh --target "$(mktemp -d)"` installed all 10 skills and each target contained `SKILL.md`.
- 2026-05-25: M5 review CI contract tests passed: `python -m unittest tests/test_ci_contract.py` ran 2 tests and passed.
- 2026-05-25: M5 review broad discovery passed: `python -m unittest discover tests` ran 31 tests and passed.
- 2026-05-25: M5 review README sync passed: `python tests/check_readme_sync.py`.
- 2026-05-25: M5 review repository validation passed: `python tests/validate_skills.py` checked 10 skills, passed, and reported one aggregate warning for grandfathered skills without eval fixtures.
- 2026-05-25: M5 review installability smoke passed: `bash install.sh --target "$(mktemp -d)"` installed all 10 skills and each target contained `SKILL.md`.
- 2026-05-25: M5 review whitespace validation passed: `git diff --check`.
- 2026-05-25: Final verify passed: targeted unit tests, broad test discovery, README sync, skill validation, stale guidance search, YAML parse checks, installer smoke, and whitespace checks all passed.

## Outcome and retrospective

- Pending downstream implementation and review.

## Readiness

- See `Current Handoff Summary`.
- Branch-ready for `pr`; PR handoff remains.
