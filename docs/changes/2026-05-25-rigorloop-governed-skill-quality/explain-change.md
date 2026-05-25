# Explain Change: Skill Quality Standard First Slice

## Status

ready for verify

## Summary

This change establishes the first Skillsmith skill-quality slice: project identity and governance are aligned around Skillsmith, skill validation is made deterministic and testable, eval fixture and grandfathering checks are added, README drift is reported by a separate helper, and CI now runs the deterministic local checks.

The implementation follows the accepted proposal direction: improve reviewability for new and materially changed skills without rewriting existing skills or adding live model CI.

## Problem

Skillsmith had structural validation for skill files, but it did not yet give contributors durable evidence for why a skill exists, how trigger/output/safety behavior should be reviewed, how grandfathered existing skills avoid immediate eval backfill, or how README and install instructions stay synchronized with the repository.

The repository also still had old `ai-skills` naming and required `effort: high` guidance in several surfaces, which conflicted with the accepted portability-first standard.

## Decision Trail

| Decision point | Outcome | Source |
|---|---|---|
| Vision/governance bootstrap | Added Skillsmith vision and constitution so later artifacts have a stable source of truth. | `VISION.md`, `CONSTITUTION.md` |
| Proposal | Accepted bounded RigorLoop bootstrap plus quality gates. | `docs/proposals/2026-05-25-rigorloop-governed-skill-quality.md` |
| Spec | Approved skill-quality requirements covering metadata, evals, grandfathering, README sync, optional `effort`, and CI. | `specs/skill-quality-standard.md` |
| Test spec | Owner-approved deterministic proof surface with no live model CI. | `specs/skill-quality-standard.test.md` |
| Architecture | No separate architecture artifact required because the change is repository validation/workflow, not runtime architecture. | `docs/plans/2026-05-25-skill-quality-standard.md` |
| Plan | Split work into M1 docs, M2 validator, M3 eval/grandfathering, M4 README sync, M5 CI/full-slice validation. | `docs/plans/2026-05-25-skill-quality-standard.md` |

## Diff Rationale By Area

| File/area | Change | Reason | Source artifact | Test/evidence |
|---|---|---|---|---|
| `VISION.md`, `docs/vision/strategic-positioning.md` | Added Skillsmith identity, audience, goals, non-goals, and positioning. | RigorLoop workflow needs durable project intent; proposal review also asked to connect quality work to the mission. | Proposal, plan M1 | `python tests/validate_skills.py` |
| `CONSTITUTION.md` | Added governance rules and compatibility rule that `effort` is optional and validated only when present. | Proposal revision explicitly required constitution compatibility alignment. | R5-R6, AC3 | M1 stale-text search |
| `AGENTS.md`, `CLAUDE.md`, `.github/pull_request_template.md`, `CONTRIBUTING.md` | Updated contributor and agent guidance for Skillsmith naming, optional `effort`, eval scenarios, high-risk notes, material-change classification, and validation commands. | Contributors need the approved standard visible without duplicating it as a second canonical source. | R6, R21-R23, R34, AC4, AC7 | M1 checks, T9 manual/doc coverage |
| `README.md`, `install.sh` | Aligned project naming and install URLs around Skillsmith. | Public docs and install surface must not point to stale `ai-skills` identity. | R28, R35, proposal identity cleanup | README sync helper, installer smoke |
| `tests/validate_skills.py` | Reworked validator around `ValidationResult`; added optional `effort`, name syntax/reserved-name, `allowed-tools`, length, eval fixture, and grandfathering checks; removed plugin metadata validation. | Objective validator checks should be mechanically testable; `.claude-plugin` validation was no longer in scope; existing skills are grandfathered through a checked-in artifact. | R1-R16, R24-R25, R30-R33, AC5-AC14 | `tests/test_validate_skills.py`, `tests/test_eval_fixtures.py` |
| `tests/evals/skills/grandfathered-skills.yaml` | Added deterministic baseline of existing skill directory names. | Spec-review resolved grandfathering away from future commit inference. | R16, AC11-AC14, F-SPEC-001 | Eval fixture tests and repo validation |
| `tests/check_readme_sync.py` | Added separate README sync helper for skill table, slash commands, and install instructions. | README sync is cross-artifact validation and must remain separate from per-skill validation. | R28-R29, AC8 | `tests/test_check_readme_sync.py` |
| `.github/workflows/validate.yml` | Added unit discovery and README sync helper to CI after skill validation dependency setup. | CI should run deterministic local checks and no live model/provider/secret-dependent work. | R30-R35, AC9-AC10 | `tests/test_ci_contract.py` |
| `tests/test_validate_skills.py` | Added per-skill validator unit coverage. | T2 requires direct proof for valid and invalid metadata/body cases. | T2, F-CODE-M2-001 | 13 validator tests |
| `tests/test_eval_fixtures.py` | Added eval fixture and grandfathering tests. | T3/T4 require direct proof for eval categories, high-risk safety evidence, stale baseline, and new-skill gating. | T3, T4, F-CODE-M3-001 | 9 eval/grandfathering tests |
| `tests/test_check_readme_sync.py` | Added README sync fixture tests. | T6 requires missing/extra table rows, missing/extra commands, stale URL, and current URL proof. | T6, EC6, EC7 | 7 README sync tests |
| `tests/test_ci_contract.py` | Added CI contract tests. | T7 requires proof CI runs deterministic checks and avoids live model/provider/secret-dependent steps. | T7, AC9 | 2 CI tests |
| `docs/changes/...`, `docs/plans/...`, `docs/plan.md`, `specs/...`, `docs/workflows.md`, `docs/project-map.md` | Added durable lifecycle artifacts, reviews, review resolutions, plan state, and repository map/workflow docs. | RigorLoop workflow requires traceable proposal/spec/test/plan/review/evidence artifacts for non-trivial changes. | Workflow, proposal, plan | Review log and validation notes |

## Tests Added Or Changed

| Test surface | What it proves | Test-spec coverage |
|---|---|---|
| `tests/test_validate_skills.py` | Per-skill validation returns deterministic errors/warnings for YAML, required fields, optional/present `effort`, names, body contracts, non-Latin metadata, and length limits. | T2, EC4, EC5, EC8 |
| `tests/test_eval_fixtures.py` | Grandfathered skills may lack eval fixtures, unlisted skills need fixtures, stale/malformed baselines fail, eval categories are present, high-risk fixtures need safety evidence. | T3, T4, EC9, EC11, EC12 |
| `tests/test_check_readme_sync.py` | README drift is detected for missing/extra skill rows, missing/extra slash commands, stale install URLs, and current Skillsmith URLs. | T6, EC6, EC7 |
| `tests/test_ci_contract.py` | GitHub Actions runs deterministic local checks and does not include live model/provider/secret-dependent run commands. | T7, AC9 |
| Installer smoke command | `install.sh` still installs all 10 skills into a target directory with `SKILL.md` files. | T11, R35 |

## Validation Evidence Before Final Verify

Latest available local evidence:

- `python -m unittest tests/test_ci_contract.py`: passed, 2 tests.
- `python -m unittest discover tests`: passed, 31 tests.
- `python tests/check_readme_sync.py`: passed.
- `python tests/validate_skills.py`: passed; 10 skills checked, with one expected grandfathering warning.
- `bash install.sh --target "$(mktemp -d)"`: passed; all 10 skills installed with `SKILL.md`.
- `git diff --check`: passed.
- `docs/changes/2026-05-25-rigorloop-governed-skill-quality/change.yaml` YAML parse check: passed.

Hosted CI status is not claimed here; that belongs to downstream verification/PR evidence.

## Review Resolution Summary

Material findings resolved:

| Finding | Disposition | Resolution |
|---|---|---|
| F-PROP-001 | accepted | Proposal updated to include `CONSTITUTION.md` compatibility-rule work for optional `effort`. |
| F-SPEC-001 | accepted | Spec replaced commit-derived grandfathering with `tests/evals/skills/grandfathered-skills.yaml`. |
| F-CODE-M2-001 | resolved | Added missing direct validator tests for T2 fixture cases. |
| F-CODE-M3-001 | resolved | Added non-string baseline regression test and validated entry types before sortedness checks. |

Review evidence:

- Review log: `docs/changes/2026-05-25-rigorloop-governed-skill-quality/review-log.md`
- Resolution log: `docs/changes/2026-05-25-rigorloop-governed-skill-quality/review-resolution.md`
- Latest code reviews: M4 and M5 both `clean-with-notes`; all implementation milestones are closed.

## Alternatives Rejected

| Alternative | Why rejected |
|---|---|
| Rewrite every existing skill immediately | Too broad for the first governance slice; existing skills are grandfathered instead. |
| Require live model evals in CI | Adds cost, nondeterminism, secrets, and model drift; static fixtures plus review evidence are the first slice. |
| Keep `effort: high` required | A constant required field carries little information and conflicts with portability; `effort` is optional and checked only when present. |
| Put README sync inside `validate_skills.py` | README sync is cross-artifact doc validation, not per-skill structural validation. |
| Make README drift blocking immediately | Spec says README drift starts as warning-only while the helper proves reliable. |
| Run installer smoke in CI | `install.sh` clones from GitHub; the first-slice CI contract avoids extra network beyond checkout/setup/dependency install. |
| Reintroduce `.claude-plugin` validation | The project removed that plugin surface and the accepted scope explicitly excludes it. |

## Scope Control

Preserved non-goals:

- Existing skills were not rewritten to backfill eval fixtures.
- CI does not call live models or provider APIs.
- Prompt skills remain pure prompt assets; no tool permissions were added.
- High-risk domains received lightweight safety evidence rules, not a full shared domain schema.
- README sync has no `--fix` mode in this slice.
- Final branch/PR readiness is not claimed by this artifact.

## Risks And Follow-Ups

- Grandfathered existing skills still lack eval fixtures until materially changed; reviewers must enforce material-change classification.
- README parsing is format-sensitive; if README structure changes often, stable generated markers or a future `--fix` mode may be worth a later proposal.
- Installer smoke uses the configured GitHub repository path, so final verification should consider whether local uncommitted installer behavior and remote install behavior are both relevant.
- Final `verify` still needs to check artifact-code-test coherence and current local validation before PR handoff.

## Current Handoff

The active plan is in final closeout:

- Current milestone: final closeout
- Current state: ready-for-explain-change
- Last reviewed milestone: M5, clean-with-notes
- Remaining implementation milestones: none
- Next stage after this artifact: `verify`

This explanation does not claim final verification, branch readiness, PR body readiness, or PR open readiness.
