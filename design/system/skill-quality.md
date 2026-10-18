# Skill quality system behavior

## Capability and authority

F-QUALITY-001 — Author and assess portable, reviewable prompt skills. The [quality requirements](../requirements/skill-quality-standard.md) own structural, compatibility, safety and eval obligations. Existing validator behavior is observed separately from broader reviewer obligations; a written requirement does not prove an automated check implements it.

| Function | Inputs and behavior | Observable result and boundary | Requirement basis |
| --- | --- | --- | --- |
| FN-QUALITY-001 — Assess structure and static eval evidence | Inspect authored skills, required frontmatter/body structure and fixture declarations against the checked-in grandfathering baseline | Blocking objective errors and non-blocking warnings remain distinct; unclear material changes go to review rather than assumed editorial exemption | R1–R22, R24–R27, R30–R34 |
| FN-QUALITY-002 — Compare catalog documentation | Compare skill names and supported enumerations with README table, commands and install examples | Report synchronization drift separately from per-skill validation | R28–R29 |
| FN-QUALITY-003 — Review purpose, behavior and safety | Assess trigger intent, primary job, scope, faithful output, simplicity, safety, known tradeoffs and required model evidence | Produce reviewer findings or a scoped judgment; subjective quality remains a review concern, not a brittle regex gate | R23, R31, R34, R36–R48 |

All three Functions realize F-QUALITY-001. [Portable skill architecture](../architecture/portable-skills.md) allocates checks and review responsibility. Static validation consumes local files and creates no product runtime dependency; skill execution stays portable prompt use.

## Test intent

Exercise missing/invalid metadata, missing arguments/output sections, stale or absent grandfather entries, required fixture categories, high-risk safety evidence and README omissions. Compare changed prompt scope to reviewer materiality criteria; static passing does not prove model quality or fully automated materiality detection. Use the existing unit tests, eval fixtures and checks as their actual implemented coverage. Historical quality test planning remains available under its original change.
