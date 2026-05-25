# Code Review: M3 Eval Fixture and Grandfathering Support R1

## Review status

changes-requested

## Review inputs

- Diff/review surface:
  - `tests/validate_skills.py`
  - `tests/test_eval_fixtures.py`
  - `CONTRIBUTING.md`
  - `docs/plans/2026-05-25-skill-quality-standard.md`
  - `docs/plan.md`
  - `docs/changes/2026-05-25-rigorloop-governed-skill-quality/change.yaml`
  - `docs/changes/2026-05-25-rigorloop-governed-skill-quality/explain-change.md`
- Governing artifacts:
  - `specs/skill-quality-standard.md`
  - `specs/skill-quality-standard.test.md`
  - `docs/plans/2026-05-25-skill-quality-standard.md`
- Validation evidence inspected:
  - `python -m unittest tests/test_eval_fixtures.py`: passed, 8 tests
  - `python -m unittest discover tests`: passed, 21 tests
  - `python tests/validate_skills.py`: passed, 10 skills checked, one expected grandfathering warning
  - `git diff --check`: passed
- Additional review probe:
  - direct temporary-fixture probe with a non-string grandfathered baseline entry reproduced a `TypeError`.

## Diff summary

M3 adds `validate_eval_fixtures`, `validate_grandfathering_baseline`, and `validate_cases_file` to `tests/validate_skills.py`, wires eval validation into the existing CLI, adds `tests/test_eval_fixtures.py`, documents the `cases.yaml` convention in `CONTRIBUTING.md`, and updates plan/change evidence to request M3 code review.

## Findings

### Finding F-CODE-M3-001

- Finding ID: F-CODE-M3-001
- Severity: major
- Location: `tests/validate_skills.py:102`
- Evidence: `validate_grandfathering_baseline` evaluates `entries != sorted(entries)` before proving every entry is a string. A malformed baseline with mixed entries such as `grandfathered_skills: [sample-skill, 1]` raises `TypeError: '<' not supported between instances of 'int' and 'str'` instead of returning validation errors. T4 requires malformed baseline entries to fail validation deterministically, and M3 explicitly owns baseline schema validation.
- Required outcome: Malformed `grandfathered_skills` entries must be reported as validation errors without crashing, including non-string entries.
- Safe resolution path: Add a focused regression test with a non-string baseline entry, validate entry types before sortedness comparison, and keep sortedness, bare-name, duplicate, and stale-entry checks intact.
- needs-decision rationale: none.

## Checklist coverage

- Spec alignment: concern. The implementation covers R13-R16 directionally, but F-CODE-M3-001 violates the deterministic malformed-baseline behavior expected by R16/T4.
- Test coverage: concern. `tests/test_eval_fixtures.py` covers grandfathered-without-cases, unlisted skill, stale entry, sorted/bare names, required categories, empty expected behavior, and high-risk safety evidence. It does not catch the non-string malformed-baseline crash.
- Edge cases: block. The malformed baseline entry path crashes instead of returning a validation error.
- Error handling: block. Invalid baseline data is an expected validator input and must not produce an unhandled `TypeError`.
- Architecture boundaries: pass. The change stays in the validator/test/contributor-doc surface approved for M3.
- Compatibility: pass with one concern already captured by F-CODE-M3-001. The real repo continues to pass with an expected grandfathering warning.
- Security/privacy: pass. No external calls, secrets, or live model behavior were introduced.
- Derived artifact currency: pass. The active plan, plan index, change metadata, and explain-change were updated for M3 handoff.
- Unrelated changes: pass for the M3 review surface. Broader dirty files belong to earlier accepted lifecycle slices.
- Validation evidence: pass for executed commands, but validation does not cover the malformed non-string baseline edge case.

## No-finding rationale

Not applicable; this review has one required-change finding.

## Residual risks

- Material-change classification remains reviewer-mediated for grandfathered existing skills, which matches the implementation note and current milestone scope.
- M4 README synchronization and M5 CI wiring remain open milestones.

## Milestone handoff

- Reviewed milestone: M3. Eval fixture and grandfathering support
- Review status: changes-requested
- Milestone state after review: resolution-needed
- Required review-resolution: yes
- Finding IDs: F-CODE-M3-001
- Remaining in-scope implementation milestones: M3, M4, M5
- Next stage: `review-resolution`
- Final closeout readiness: not ready; M3 requires review-resolution and re-review, and M4-M5 remain open.
