# Code Review: M1 Governance and Contributor Guidance Alignment R1

## Review status

clean-with-notes

## Review inputs

- Diff/review surface:
  - `CONSTITUTION.md`
  - `AGENTS.md`
  - `CLAUDE.md`
  - `CONTRIBUTING.md`
  - `README.md`
  - `.github/pull_request_template.md`
  - `docs/changes/2026-05-25-rigorloop-governed-skill-quality/change.yaml`
  - `docs/changes/2026-05-25-rigorloop-governed-skill-quality/explain-change.md`
  - `docs/plans/2026-05-25-skill-quality-standard.md`
  - `docs/plan.md`
- Governing artifacts:
  - `specs/skill-quality-standard.md`
  - `specs/skill-quality-standard.test.md`
  - `docs/plans/2026-05-25-skill-quality-standard.md`
- Validation evidence:
  - `python tests/validate_skills.py`: passed, 10 skills checked
  - `rg -n "effort: high|required.*effort|Required frontmatter fields.*effort|\.claude-plugin|ai-skills" AGENTS.md CLAUDE.md CONTRIBUTING.md README.md CONSTITUTION.md .github || true`: no matches
  - `git diff --check`: passed
  - `python -m unittest discover tests`: inspected but not applicable for M1 because no test modules exist yet

## Diff summary

M1 updates governance and contributor guidance so `effort` is optional rather than required, removes plugin metadata references from agent-facing structure guidance, and adds contributor/reviewer expectations for eval evidence, material-versus-editorial classification, high-risk safety notes, and selective manual model smoke evidence. It also adds the required change-local `change.yaml` and `explain-change.md` surfaces and moves the active plan state to M1 review handoff.

## Findings

No blocking or required-change findings.

## Checklist coverage

- Spec alignment: pass. `CONSTITUTION.md` now says required frontmatter is `name`, `description`, `argument-hint`, and `allowed-tools`, while `effort` is optional and non-portable-behavior cannot rely on it, satisfying R5, R6, AC3, and AC4.
- Test coverage: pass for M1. T8 and T9 are covered by direct documentation inspection and stale-text search. Automated unit tests are not yet applicable because M1 is docs/governance-only and the repository has no test modules yet.
- Edge cases: pass for M1. High-risk and model-specific evidence expectations are present in `CONTRIBUTING.md` and `.github/pull_request_template.md`, covering the M1-relevant parts of R21, R34, T9, and T10.
- Error handling: pass. No runtime error paths are changed by M1.
- Architecture boundaries: pass. M1 changes governance and contributor docs only; it does not add dependencies, runtime services, generated assets, or data flow.
- Compatibility: pass. Guidance preserves pure-prompt `allowed-tools: ""`, cross-model portability, and optional runtime-specific `effort`.
- Security/privacy: pass. High-risk skill evidence now requires safety notes, boundaries, refusal or escalation behavior, and safety or misuse eval coverage.
- Derived artifact currency: pass for M1. `docs/plan.md`, the concrete plan, `change.yaml`, and `explain-change.md` reflect the M1 implementation and validation state.
- Unrelated changes: pass for the reviewed M1 surface. The broader working tree contains earlier lifecycle/bootstrap changes, but the M1-reviewed changes are aligned with the approved milestone.
- Validation evidence: pass. The recorded commands are relevant to M1 and current local execution confirms validator, stale-text, and diff-check evidence.

## No-finding rationale

The M1 contract was to align governance and contributor-facing docs before validator implementation. The diff removes the required-`effort` policy from all M1-owned guidance surfaces, replaces it with optional accepted-value language, adds eval-first and high-risk evidence expectations, and keeps subjective quality in review-facing checklists rather than automated gates. The targeted validation directly proves no stale required-effort, `.claude-plugin`, or `ai-skills` matches remain in the M1-owned guidance surfaces.

## Residual risks

- README sync helper, validator extensions, eval fixture enforcement, and CI wiring remain future milestones M2-M5.
- `python -m unittest discover tests` is not yet useful until test modules are introduced in later milestones.

## Milestone handoff

- Reviewed milestone: M1. Governance and contributor guidance alignment
- Review status: clean-with-notes
- Milestone state after review: closed
- Required review-resolution: no
- Remaining in-scope implementation milestones: M2, M3, M4, M5
- Next stage: `implement M2`
- Final closeout readiness: not ready; M2-M5 and downstream review, rationale, verification, and PR handoff gates remain.
