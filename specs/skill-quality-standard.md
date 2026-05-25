# Skill Quality Standard

## Status

approved

## Related proposal

- `docs/proposals/2026-05-25-rigorloop-governed-skill-quality.md`
- Proposal review R2: `docs/changes/2026-05-25-rigorloop-governed-skill-quality/reviews/proposal-review-r2.md`

## Goal and context

Skillsmith skills are portable Markdown prompt assets. This spec defines the observable quality contract for adding or materially changing a skill so reviewers can evaluate purpose, trigger behavior, output quality, safety behavior, and evidence without relying on ad hoc judgment.

The standard applies to new skills and materially changed skills first. Existing skills listed in `tests/evals/skills/grandfathered-skills.yaml` are grandfathered for eval-fixture enforcement until materially changed.

## Glossary

- Skill: a directory under `skills/<skill-name>/` containing `SKILL.md`.
- Skill frontmatter: YAML metadata at the top of `SKILL.md`.
- Skill body: Markdown prompt content after frontmatter.
- Material skill change: a change that could alter what a skill does, when it triggers, or what it returns.
- Editorial skill change: a typo, grammar, formatting, link, or wording cleanup that leaves trigger behavior, output contract, workflow steps, and safety behavior unchanged.
- Eval fixture: a static scenario file used as reviewer evidence for expected skill behavior.
- High-risk skill: a skill operating in medical, security, legal, financial, or similarly high-impact domains.
- Reviewer heuristic: a quality judgment surfaced to reviewers but not hard-blocked by brittle CI.

## Examples first

Example E1: new skill includes required quality evidence
Given a contributor adds `skills/code-reviewer/SKILL.md`
When the contributor opens the change for review
Then the skill has valid frontmatter, `$ARGUMENTS`, `## Output Format`, a README entry, and at least three eval scenarios covering normal use, indirect trigger, and edge or safety behavior.

Example E2: editorial typo fix avoids unnecessary eval work
Given a contributor fixes a spelling error in `skills/editor/SKILL.md`
When the change does not alter frontmatter, trigger meaning, workflow steps, output format, safety behavior, or referenced files
Then the change is treated as editorial and does not require new eval fixtures.

Example E3: material trigger change requires eval evidence
Given a contributor changes a skill `description`
When the changed description could alter when the skill is selected
Then the change is material and requires the three eval scenarios for that skill.

Example E4: high-risk skill includes safety evidence
Given a contributor materially changes a medical, security, legal, financial, or similarly high-impact skill
When the change is submitted for review
Then the evidence includes scope boundaries, escalation or refusal behavior, reviewer-visible safety notes, and at least one safety or misuse eval case.

Example E5: optional effort remains portable
Given a skill omits `effort`
When validation runs
Then the omission is allowed.
Given a skill includes `effort`
When validation runs
Then the value is checked against the allowed set and the skill still does not rely on `effort` for portable behavior.

## Requirements

R1. Each skill MUST live at `skills/<skill-name>/SKILL.md`.

R2. Each skill name MUST use lowercase letters, numbers, and hyphens only, MUST NOT exceed 64 characters, and MUST NOT use reserved platform words when the validator can identify them.

R3. Each `SKILL.md` MUST have parseable YAML frontmatter.

R4. Each `SKILL.md` frontmatter MUST include `name`, `description`, `argument-hint`, and `allowed-tools`.

R5. `effort` MUST be optional. When present, `effort` MUST use an allowed value defined by the skill-quality standard or validator, and Skillsmith skills MUST NOT rely on `effort` for portable behavior.

R6. `CONSTITUTION.md`, `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, and the validator expectations MUST treat `effort` as optional once this standard is implemented.

R7. For pure-prompt skills, `allowed-tools` MUST be the empty string unless an accepted proposal and spec explicitly allow tool use.

R8. `description` and `argument-hint` MUST be English-facing metadata suitable for assistant UI and invocation.

R9. `description` MUST explain both what the skill does and when to use it.

R10. Skill descriptions SHOULD be trigger-forward and include explicit "Use this skill whenever..." style phrasing unless a reviewer records why a less direct description is clearer.

R11. Each skill body MUST include `$ARGUMENTS`.

R12. Each skill body MUST include a `## Output Format` section.

R13. A new or materially changed skill MUST include at least three eval scenarios: normal intended use, vague or indirect trigger, and edge, safety, failure, non-trigger, or misuse behavior.

R14. Eval scenarios MUST contain concrete user prompts or situations and expected observable behavior.

R15. Eval scenarios MUST NOT require live model calls in CI.

R16. The repository MUST define grandfathered skills through the checked-in artifact `tests/evals/skills/grandfathered-skills.yaml`. The artifact MUST exist before implementation planning begins. It MUST list the exact skill directory names under `skills/` that are exempt from the initial eval-fixture requirement until materially changed. The artifact, not a commit hash, branch name, README table, or future implementation commit, is the source of truth for grandfathering. Each entry MUST match an existing `skills/<skill-name>/` directory at the time the baseline artifact is created. The validator MUST fail if the artifact contains a skill that no longer exists, unless the corresponding skill removal is part of the same change. A skill listed in the baseline artifact MAY lack `tests/evals/skills/<skill-name>/cases.yaml` only while it remains editorially unchanged. If a grandfathered skill receives a material change, it MUST satisfy the same eval-fixture requirements as a new skill before merge. A skill not listed in the baseline artifact MUST provide `tests/evals/skills/<skill-name>/cases.yaml` before merge. Material-change detection MUST follow this specification's material-change definition. When materiality is unclear, reviewers MUST treat the change as material.

R17. A material skill change MUST include any change that could alter what the skill does, when it triggers, or what it returns.

R18. Changes to `name`, `description`, output format, `$ARGUMENTS` handling, execution-affecting frontmatter, workflow steps, safety rules, or referenced files MUST be treated as material unless the reviewer records a narrower rationale.

R19. Editorial skill changes MAY proceed without new eval fixtures when they leave trigger behavior, output contract, workflow steps, referenced files, and safety behavior unchanged.

R20. Unclear material-versus-editorial cases MUST be treated as material.

R21. High-risk new or materially changed skills MUST include scope boundaries, escalation or refusal behavior, reviewer-visible safety notes, and at least one safety or misuse eval case.

R22. Detailed shared schemas for high-risk domains MUST NOT be required in the first implementation slice.

R23. A skill quality review MUST include a mission-fit check: engineering-facing skills are evaluated for reduction of repetitive engineering work, clarification of review evidence, or improvement of execution quality; non-engineering productivity skills are evaluated for the same kind of efficiency gain in their domain.

R24. `SKILL.md` files SHOULD stay under 300 lines when practical.

R25. New or materially changed `SKILL.md` files MUST NOT exceed 500 lines unless an accepted exception explains why progressive disclosure is not suitable.

R26. Skills approaching the length ceiling SHOULD move detail into one-level-deep reference files.

R27. Reference files over roughly 100 lines SHOULD include a table of contents.

R28. README synchronization MUST cover the skill table, slash-command list, and install instructions.

R29. README synchronization MUST be checked separately from per-skill structural validation.

R30. Blocking automated checks MUST be objective and mechanically verifiable.

R31. Reviewer heuristics such as trigger quality, concision quality, mission fit, and safety adequacy MUST be surfaced through eval evidence or review checklists rather than brittle CI gates.

R32. Validation MUST distinguish compatibility rules, Skillsmith policy, and reviewer heuristics.

R33. CI MUST run deterministic checks only; live model execution MUST NOT be required in CI for this first slice.

R34. Manual model smoke evidence MUST be required only when a change is high-risk, behavior-heavy, or claims model-specific behavior.

R35. The first implementation slice MUST keep existing skills installable.

## Inputs and outputs

Inputs:

- `skills/*/SKILL.md`
- `tests/evals/skills/<skill-name>/cases.yaml` or an equivalent accepted eval fixture path
- `tests/evals/skills/grandfathered-skills.yaml`
- README skill table, slash-command list, and install instructions
- `CONSTITUTION.md`, `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, and `.github/pull_request_template.md`
- `tests/validate_skills.py`
- a README sync helper, expected as `tests/check_readme_sync.py` unless changed by spec review

Outputs:

- contributor-visible skill-quality standard at `specs/skill-quality-standard.md`
- validation failures for blocking structural and policy violations
- validation warnings for grandfathered or staged checks
- reviewer-visible eval and safety evidence for subjective quality
- updated governance and contributor documentation

## State and invariants

- The canonical skill-quality standard is this spec once approved.
- `specs/skill-quality-standard.test.md` maps this spec to validation and eval checks without restating the full standard.
- `tests/evals/skills/grandfathered-skills.yaml` is the only source of truth for grandfathered skill names.
- Existing skills listed in the grandfathering baseline remain grandfathered for eval-fixture enforcement until materially changed.
- Skills remain pure prompt assets unless a later accepted proposal and spec change that boundary.
- `effort` remains optional even when present in current skills.
- CI remains deterministic and does not depend on live model calls.

## Error and boundary behavior

- Invalid YAML frontmatter is a blocking validation error.
- Missing `name`, `description`, `argument-hint`, `allowed-tools`, `$ARGUMENTS`, or `## Output Format` is a blocking validation error after this standard is implemented.
- Missing `effort` is not an error or warning by itself.
- Invalid `effort` values are validation errors when the field is present.
- Missing eval fixtures are warnings for grandfathered skills and blocking errors for new or materially changed skills once the material-change detection path exists.
- Stale entries in `tests/evals/skills/grandfathered-skills.yaml` are validation errors unless the corresponding skill deletion is part of the same change.
- README sync drift starts as a warning and becomes blocking once the sync helper is reliable and documented.
- Description quality failures are review findings unless the failure is mechanically checkable.
- If the validator cannot determine whether a change is new, material, or grandfathered, it must not silently pass the change as editorial; it must surface the uncertainty for review.

## Compatibility and migration

- The implementation MUST update `CONSTITUTION.md` so `effort` is optional, because the current constitution lists `effort` as required.
- The implementation MUST use `tests/evals/skills/grandfathered-skills.yaml`, not a commit hash, branch name, README table, or future implementation commit, to determine grandfathered skills.
- The implementation MUST update `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, README, and PR template guidance to align with this standard.
- Existing skills are grandfathered for eval fixtures but not for core parseability and required structural fields already enforced by the validator.
- The implementation MUST NOT reintroduce `.claude-plugin` or plugin metadata validation.
- Rollback may reduce validator gating while preserving eval fixtures and the quality standard as reviewer guidance.

## Observability

- Local validation output MUST report the number of skills checked.
- Validation output MUST distinguish warnings from errors.
- README sync output MUST identify missing, extra, or mismatched README entries.
- Eval fixture validation output MUST identify the skill and scenario category that is missing or malformed.
- PRs for new or materially changed skills MUST include validation command output or an explicit explanation when a check could not be run.

## Security and privacy

- Eval fixtures and examples MUST use fictional or sanitized inputs.
- Eval fixtures MUST NOT contain secrets, credentials, private local paths, or unpublished personal data.
- High-risk skills MUST include reviewer-visible safety notes and at least one safety or misuse eval scenario.
- Medical, legal, financial, security, or similarly high-impact skills MUST NOT present themselves as substitutes for licensed professionals, emergency services, official advice, or authorized security review.
- Skills MUST keep `allowed-tools: ""` unless a later accepted proposal and spec authorize tool use.

## Accessibility and UX

No interactive UI is introduced.

Contributor-facing docs and validation errors SHOULD use direct, actionable language that identifies the file, failing rule, and expected fix.

## Performance expectations

- Local validation SHOULD complete quickly enough for ordinary pre-PR use on the current repository size.
- Validation MUST remain deterministic.
- CI MUST NOT require network access beyond normal dependency installation and repository checkout for this first slice.
- Eval fixture checks MUST parse static files only.

## Edge cases

EC1. A description typo changes trigger meaning. Treat the change as material if trigger behavior could change.

EC2. A skill adds a reference file without changing `SKILL.md` instructions. Treat the change as material because referenced files can alter behavior.

EC3. A high-risk skill adds a minor safety wording change. Treat the change as material unless a reviewer records why behavior is unchanged.

EC4. A skill omits `effort`. Validation passes because `effort` is optional.

EC5. A skill includes `effort: ultra`. Validation fails when allowed values do not include `ultra`.

EC6. README lists a skill that no longer exists. README sync reports drift.

EC7. README omits a skill that exists under `skills/`. README sync reports drift.

EC8. A skill exceeds 500 lines but has no exception. New or materially changed skill validation fails after grandfathering rules are active.

EC9. An eval fixture has three scenarios but none covers indirect trigger behavior. Eval fixture validation reports the missing category.

EC10. A contributor claims a skill works better on a specific model. Manual model smoke evidence is required for that claim.

EC11. The grandfathering baseline lists `old-skill`, but `skills/old-skill/` does not exist. Validation fails unless the same change removes that skill and its baseline entry.

EC12. A new skill is not listed in the grandfathering baseline and has no `cases.yaml`. Validation fails before merge.

## Non-goals

- Do not rewrite all existing skills in the first implementation slice.
- Do not require live model CI.
- Do not introduce tool-using skills.
- Do not add `.claude-plugin` validation.
- Do not make subjective prompt quality a brittle CI gate.
- Do not create a second canonical skill-quality standard under `docs/`.

## Acceptance criteria

AC1. `specs/skill-quality-standard.md` exists and contains testable requirements for skill metadata, body structure, eval fixtures, high-risk safety gates, README sync, `effort`, and grandfathering.

AC2. `specs/skill-quality-standard.test.md` maps each requirement in this spec to validation, fixture review, manual review, or non-applicable coverage.

AC3. `CONSTITUTION.md` is updated so `effort` is optional and validated only when present.

AC4. Contributor and agent docs no longer describe `effort` as a required field.

AC5. Deterministic validation checks continue to pass for the existing repository after grandfathering is applied.

AC6. New or materially changed skills require the three eval scenario categories.

AC7. High-risk new or materially changed skills require lightweight safety evidence.

AC8. README sync covers the skill table, slash-command list, and install instructions.

AC9. CI does not require live model calls.

AC10. `python tests/validate_skills.py` passes after the first implementation slice.

AC11. `tests/evals/skills/grandfathered-skills.yaml` exists before implementation planning.

AC12. The grandfathering artifact lists only existing `skills/<skill-name>/` directories.

AC13. The grandfathering artifact lists skill names lexicographically and contains no paths.

AC14. Validation or a test helper can distinguish listed grandfathered skills without eval fixtures, listed grandfathered skills with material changes that require eval fixtures, unlisted new skills that require eval fixtures, and stale baseline entries that fail validation unless removed with the same skill deletion.

## Open questions

- Should README sync include a `--fix` mode in the first implementation slice or only report drift?
- Which reserved platform words beyond `anthropic` and `claude` should the validator reject?

## Resolved Decision: Grandfathering Baseline

Grandfathering is not tied to an accepted proposal commit. The deterministic baseline is the checked-in artifact `tests/evals/skills/grandfathered-skills.yaml`. Test spec and implementation planning MUST use that file as the source of truth.

## Next artifacts

1. Implementation plan for the first slice.
2. Plan review.
3. `specs/skill-quality-standard.test.md` after plan review.
4. Architecture note only if planning or review identifies a long-lived design decision that needs separate architecture assessment.

## Follow-on artifacts

None yet.

## Readiness

Approved by spec-review R2 and ready for planning.
