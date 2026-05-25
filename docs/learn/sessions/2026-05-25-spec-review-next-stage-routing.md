# Learn Session: Spec Review Next-Stage Routing

## Frame

- Trigger: explicit maintainer `$learn` request after spec-review output named "architecture assessment or `test-spec`" as the next repository stage.
- Trigger type: maintainer request and workflow-process observation.
- Scope: the `spec-review` R2 record for `2026-05-25-rigorloop-governed-skill-quality`, the local `spec-review` skill rules, and `docs/workflows.md`.
- Evidence in scope:
  - `docs/changes/2026-05-25-rigorloop-governed-skill-quality/reviews/spec-review-r2.md`
  - `.agents/skills/spec-review/SKILL.md`
  - `docs/workflows.md`
- Explicit exclusions: no implementation code review; no change to the `spec-review` skill itself in this session.
- Prior learnings reviewed: none found under `docs/learn/`.
- Session record path: `docs/learn/sessions/2026-05-25-spec-review-next-stage-routing.md`

## Observe

O1. The recorded R2 spec review incorrectly mixed immediate routing with eventual test planning.

Evidence:

- `spec-review-r2.md` originally said: "next repository stage is architecture assessment or `test-spec` when explicitly invoked."
- `.agents/skills/spec-review/SKILL.md` says not to name `test-spec` as the immediate next stage while `architecture` or `plan` still remains.
- The same skill requires reporting eventual `test-spec` readiness separately.

O2. The local workflow order makes `test-spec` downstream of plan, not an immediate post-spec-review stage.

Evidence:

- `docs/workflows.md` records the standard chain as `proposal -> proposal-review -> spec -> spec-review -> architecture -> architecture-review -> plan -> plan-review -> test-spec -> implement ...`.
- For this change, no blocking architecture finding was recorded, and the approved spec review did not require an architecture artifact before planning.

O3. The root cause was not the spec content; it was review-output routing.

Evidence:

- Spec-review R2 approved the spec and declared eventual test-spec readiness as ready.
- The incorrect phrase appeared only in the "Immediate next stage" field.

## Classify

| Observation | Proposed classification | Final classification | Secondary routes | Confirmed by | Rationale |
|---|---|---|---|---|---|
| O1 | artifact-update | artifact-update | update spec-review R2 record | maintainer request: "It should be plan" | A tracked review artifact contained a concrete routing error. |
| O2 | observation | observation | none | maintainer request | This explains the workflow order but does not by itself create new policy. |
| O3 | no-durable-lesson | no-durable-lesson | none | maintainer request | This is a single error explained by existing rules, not accumulated evidence of a recurring pattern. |

## Route

- Updated `docs/changes/2026-05-25-rigorloop-governed-skill-quality/reviews/spec-review-r2.md` so the immediate next stage is `plan` when explicitly invoked.
- No topic file was created. Existing workflow and skill rules already cover the best practice; this session records the mistake and correction.
- No new proposal, ADR, spec, or workflow change is required from this single event.

## Best Practices

- Keep "Immediate next stage" and "Eventual test-spec readiness" separate in spec-review output.
- Do not name `test-spec` as the immediate next stage while plan remains.
- If architecture is not triggered by the spec review, route the next repository stage to `plan`.
- If architecture is triggered, name `architecture` as the immediate next repository stage and keep test-spec readiness separate.
- Use `test-spec readiness: ready` only to say the approved spec is sufficiently testable later; it is not a routing substitute for plan.

## Follow-ups

None.

## Validation

- `python tests/validate_skills.py`
