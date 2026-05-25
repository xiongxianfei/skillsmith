# Code Review: M4 README Synchronization Helper R1

## Review status

clean-with-notes

## Review inputs

- Diff/review surface:
  - `tests/check_readme_sync.py`
  - `tests/test_check_readme_sync.py`
  - `CONTRIBUTING.md`
  - `docs/plans/2026-05-25-skill-quality-standard.md`
  - `docs/plan.md`
  - `docs/changes/2026-05-25-rigorloop-governed-skill-quality/change.yaml`
  - `docs/changes/2026-05-25-rigorloop-governed-skill-quality/explain-change.md`
- Governing artifacts:
  - `specs/skill-quality-standard.md`
  - `specs/skill-quality-standard.test.md`
  - `docs/plans/2026-05-25-skill-quality-standard.md`
- Validation evidence:
  - `python -m unittest tests/test_check_readme_sync.py`: passed, 7 tests
  - `python -m unittest discover tests`: passed, 29 tests
  - `python tests/check_readme_sync.py`: passed
  - `python tests/validate_skills.py`: passed, 10 skills checked, one expected grandfathering warning
  - `git diff --check`: passed
  - `change.yaml` parse check: passed

## Diff summary

M4 adds a standalone `tests/check_readme_sync.py` helper that reports README drift separately from per-skill validation. It checks skill table entries, slash-command mentions, and install instructions. The helper is report-only for README drift in this first slice and exits non-zero only for execution errors such as missing required files. M4 also adds `tests/test_check_readme_sync.py` fixture coverage and documents the local helper command in `CONTRIBUTING.md`.

## Findings

No blocking or required-change findings.

## Checklist coverage

- Spec alignment: pass. R28 and AC8 require README sync for table, command list, and install instructions; R29 requires a separate helper rather than mixing this into `validate_skills.py`.
- Test coverage: pass. T6 fixture coverage includes complete sync, missing and extra table rows, missing and extra slash commands, stale install URL, and current Skillsmith install URL.
- Edge cases: pass. EC6 and EC7 are directly covered through extra and missing README table entries.
- Error handling: pass. Missing `skills/` or `README.md` are errors, while first-slice README drift is warning-only as specified.
- Architecture boundaries: pass. The helper is standalone and does not couple README parsing into per-skill structural validation.
- Compatibility: pass. The real README sync check passes, and `python tests/validate_skills.py` still passes current skills with only the expected grandfathering warning.
- Security/privacy: pass. The helper performs local file parsing only and adds no network or secret-dependent behavior.
- Derived artifact currency: pass. Plan, plan index, change metadata, and explain-change evidence reflect the M4 handoff state.
- Unrelated changes: pass for the M4 review surface. Broader dirty files belong to earlier accepted lifecycle slices.
- Validation evidence: pass. The targeted and broad local validation commands passed.

## No-finding rationale

The implementation matches the approved M4 boundary: it detects README drift across the required surfaces, keeps README sync separate from per-skill validation, does not add a `--fix` mode, and leaves CI wiring to M5. The tests directly prove the named T6 fixture cases, and the helper passes against the real README.

## Residual risks

- README parsing remains format-sensitive; the plan already records this risk and keeps the helper warning-only in the first slice.
- CI wiring remains open for M5.

## Milestone handoff

- Reviewed milestone: M4. README synchronization helper
- Review status: clean-with-notes
- Milestone state after review: closed
- Required review-resolution: no
- Finding IDs: none
- Remaining in-scope implementation milestones: M5
- Next stage: `implement M5`
- Final closeout readiness: not ready; M5 and downstream rationale, verification, and PR handoff gates remain.
