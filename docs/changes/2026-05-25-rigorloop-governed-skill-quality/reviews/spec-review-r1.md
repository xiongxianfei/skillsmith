# Spec Review: Skill Quality Standard R1

## Result

- Skill: spec-review
- Review status: changes-requested
- Material findings: F-SPEC-001
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-05-25-rigorloop-governed-skill-quality/reviews/spec-review-r1.md`
- Review log: `docs/changes/2026-05-25-rigorloop-governed-skill-quality/review-log.md`
- Review resolution: `docs/changes/2026-05-25-rigorloop-governed-skill-quality/review-resolution.md`
- Open blockers: F-SPEC-001
- Immediate next stage: spec revision

## Findings

### Finding ID: F-SPEC-001

- Severity: blocking
- Location: `specs/skill-quality-standard.md`, R16 and Open questions
- Evidence: R16 says existing skills are grandfathered "at the accepted proposal commit", while Open questions asks what exact accepted proposal commit should be recorded. This branch has not committed the proposal yet, so test-spec and implementation cannot determine which skills are grandfathered without guessing.
- Required outcome: The spec must define an observable grandfathering baseline that is available before implementation planning.
- Safe resolution path: Replace the unresolved commit dependency with a deterministic baseline such as "all skill directories present in the first implementation commit before validator changes" plus a generated baseline file, or require a specific baseline artifact path to list grandfathered skill names. The test spec can then verify against that artifact instead of an unavailable commit hash.

## Review Dimensions

- requirement clarity: block. R16 is not implementable because its baseline is unresolved.
- normative language: pass. Requirements use clear MUST/SHOULD/MAY language.
- completeness: concern. The spec covers the proposal scope, but the grandfathering baseline is incomplete.
- testability: block. Tests cannot distinguish grandfathered from new skills without a deterministic baseline.
- examples: pass. Examples cover new skills, editorial changes, material trigger changes, high-risk changes, and optional `effort`.
- compatibility: pass. The spec explicitly updates `CONSTITUTION.md` and keeps `.claude-plugin` out of scope.
- observability: pass. Validation output, README sync output, eval fixture output, and PR evidence are covered.
- security/privacy: pass. Sensitive examples, high-risk safety notes, and pure-prompt tool boundaries are covered.
- non-goals: pass. Non-goals align with the accepted proposal.
- acceptance criteria: concern. Acceptance criteria need the same grandfathering baseline clarity as R16.

## Eventual test-spec readiness

blocked until F-SPEC-001 is resolved.

## Stop condition

Spec revision is required before `specs/skill-quality-standard.test.md` can be written without guessing.
