# Code Review: M2 Per-Skill Validator Rule Updates R1

## Review status

changes-requested

## Review inputs

- Diff/review surface:
  - `tests/validate_skills.py`
  - `tests/test_validate_skills.py`
  - `docs/plans/2026-05-25-skill-quality-standard.md`
  - `docs/plan.md`
  - `docs/changes/2026-05-25-rigorloop-governed-skill-quality/change.yaml`
  - `docs/changes/2026-05-25-rigorloop-governed-skill-quality/explain-change.md`
- Governing artifacts:
  - `specs/skill-quality-standard.md`
  - `specs/skill-quality-standard.test.md`
  - `docs/plans/2026-05-25-skill-quality-standard.md`
- Validation evidence:
  - `python -m unittest tests/test_validate_skills.py`: passed, 9 tests
  - `python -m unittest discover tests`: passed, 9 tests
  - `python tests/validate_skills.py`: passed, 10 skills checked
  - `git diff --check`: passed

## Diff summary

M2 refactors `tests/validate_skills.py` to return per-skill `ValidationResult` objects, removes the old global result mutation, keeps CLI aggregation, and adds objective validation for required `allowed-tools`, optional/allowed `effort`, skill name syntax and reserved names, pure-prompt `allowed-tools: ""`, `$ARGUMENTS`, `## Output Format`, non-Latin metadata warnings, and 300/500 line thresholds. It also adds `tests/test_validate_skills.py` with 9 unit tests.

## Findings

### Finding ID: F-CODE-M2-001

- Severity: major
- Location: `tests/test_validate_skills.py`
- Evidence: The approved test spec T2 requires fixture coverage for "valid skill, missing `SKILL.md`, invalid YAML, missing required fields, invalid name, reserved name, non-empty `allowed-tools`, missing `$ARGUMENTS`, missing `## Output Format`, missing `effort`, invalid `effort`, non-Latin metadata, 300-line warning, and 500-line ceiling." The current test file covers valid skill without `effort`, invalid `effort`, non-empty `allowed-tools`, missing `allowed-tools`, invalid name, reserved name, missing body contracts, non-Latin metadata, and line thresholds, but it does not directly test missing `SKILL.md`, invalid YAML frontmatter, missing `name`, missing `description`, missing `argument-hint`, or name length greater than 64 characters.
- Required outcome: Add direct unit coverage for the missing T2 fixture cases or revise the approved test spec before claiming M2 test coverage is complete.
- Safe resolution path: Extend `tests/test_validate_skills.py` with focused tests for missing `SKILL.md`, invalid YAML, each required frontmatter field omitted, and a `name` value longer than 64 characters; rerun `python -m unittest tests/test_validate_skills.py`, `python -m unittest discover tests`, `python tests/validate_skills.py`, and `git diff --check`.

## Checklist coverage

- Spec alignment: pass with finding. The validator implementation covers R1-R12, R24-R25, and R30-R32 behavior, but test proof is incomplete for approved T2 fixture coverage.
- Test coverage: block. F-CODE-M2-001 identifies missing direct tests required by `specs/skill-quality-standard.test.md`.
- Edge cases: concern. EC4, EC5, and EC8 have direct tests; missing `SKILL.md`, invalid YAML, and long-name failure paths lack direct proof.
- Error handling: concern. The implementation has code paths for missing file and invalid YAML, but those paths are not directly tested.
- Architecture boundaries: pass. The change stays within the per-skill validator and unit tests; no runtime services, dependencies, or CI behavior are added.
- Compatibility: pass. Existing CLI output still reports skill count, warnings, errors, and passes current 10 skills.
- Security/privacy: pass. No secrets, external services, or live model calls are introduced.
- Derived artifact currency: pass. Plan and change metadata reflect M2 implementation and validation state.
- Unrelated changes: pass. The reviewed M2 surface is scoped to validator/test updates and lifecycle evidence.
- Validation evidence: concern. Commands pass, but passing tests do not cover all T2-required fixtures.

## Residual risks

None beyond F-CODE-M2-001.

## Milestone handoff

- Reviewed milestone: M2. Per-skill validator rule updates
- Review status: changes-requested
- Milestone state after review: resolution-needed
- Required review-resolution: yes
- Finding IDs: F-CODE-M2-001
- Remaining in-scope implementation milestones: M2, M3, M4, M5
- Next stage: `review-resolution M2`
- Final closeout readiness: not ready; M2 requires review-resolution and re-review, and M3-M5 remain open.
