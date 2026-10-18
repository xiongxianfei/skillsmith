# Skill Quality Standard requirements

Canonical contributor quality standard, relocated without changing its authoring, safety or evaluation obligations. IDs R/AC/EC/E retain their source-local identity under `skill-quality-standard`. The [source dispositions](https://github.com/xiongxianfei/skillsmith/blob/230c4de32289abc8a883bab86ba744e9f4009d32/docs/changes/2026-10-18-rigorloop-v2-adoption/source-disposition.md) preserve exact sources, historical delivery conditions and supersession. One-time rollout instructions are historical evidence, not new product changes.

## Goal and context

Skillsmith skills are portable Markdown prompt assets. This spec defines the observable quality contract for adding or materially changing a skill so reviewers can evaluate purpose, trigger behavior, output quality, safety behavior, and evidence without relying on ad hoc judgment.

The standard applies to new skills and materially changed skills first. Existing skills listed in `tests/evals/skills/grandfathered-skills.yaml` are grandfathered for eval-fixture enforcement until materially changed.

## Design Philosophy

Skillsmith skills should be small, portable prompt contracts that do one job through one verified path.

When a skill behavior can be expressed as one uniform workflow, prefer that over broad scenario coverage, input-type detection, effort-scaling branches, or fallback branches. Simpler skill structure should remove failure modes rather than patch them with louder instructions.

Skill bodies should define behavior. Frontmatter should help selection, but the skill must remain correct from `name`, `description`, `$ARGUMENTS`, and the Markdown body alone. Optional metadata may make a runtime more convenient, but skill correctness must not depend on it.

Descriptions are the highest-leverage metadata line. They should use third-person descriptive language, state what the skill does first, name any distinguishing output shape, then name concrete trigger situations and common user phrasing. Spending description tokens is acceptable when it improves reliable selection.

The strongest skill rules should be few and deep. Prefer a small number of durable directives that imply boundary behavior. For example, preserving source meaning can also define an integrity boundary by preventing misleading transformations.

Quality should be verified, not merely asserted. A quality-critical workflow should include an explicit check or review step when the skill output could silently drift from the source, user intent, safety boundary, or requested format.

Conciseness should come from essential instructions and honest execution. Avoid adding branches only to shorten trivial cases when the accepted skill design requires a fixed output contract. When fixed output creates a known cost, record that tradeoff instead of hiding it.

Every reference in a skill prompt should resolve to one thing. Terminology should not drift between workflow instructions and output templates, because ambiguous references can produce inconsistent behavior across runs.

Output contracts should be stable and specific. Required reasons, assessments, or sections should name the actual dimensions to check rather than saying only "explain" or "assess quality."

Structured outputs should optimize for reuse, not decoration. Prefer concise bold labels, copyable content on its own line under each label, clear separation between deliverables and commentary, and no emoji or decorative symbols unless an accepted skill spec explicitly needs them.

When a prompt reaches diminishing returns from wording review, freeze the good-enough contract and move to eval evidence. Further refinements should be driven by observed behavior, not endless polishing.

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

Example E5: optional metadata is omitted by default
Given a skill omits `argument-hint`, `effort`, and `allowed-tools`
When validation runs
Then the omission is allowed and preferred.
Given a skill includes non-empty `allowed-tools`
When validation runs
Then validation fails unless a later accepted tool-using skill spec authorizes tool permissions.

## Requirements

<a id="r1"></a>

R1. Each skill MUST live at `skills/<skill-name>/SKILL.md`.

<a id="r2"></a>

R2. Each skill name MUST use lowercase letters, numbers, and hyphens only, MUST NOT exceed 64 characters, and MUST NOT use reserved platform words when the validator can identify them.

<a id="r3"></a>

R3. Each `SKILL.md` MUST have parseable YAML frontmatter.

<a id="r4"></a>

R4. Each `SKILL.md` frontmatter MUST include `name` and `description`.

<a id="r5"></a>

R5. `effort` MUST NOT be required, and Skillsmith skills SHOULD omit it unless a later accepted compatibility reason requires it.

<a id="r6"></a>

R6. `CONSTITUTION.md`, `AGENTS.md`, `docs/workflows.md`, and validator expectations MUST NOT instruct contributors to add `argument-hint`, `effort`, or `allowed-tools` by default.

<a id="r7"></a>

R7. Skills SHOULD omit `allowed-tools`; if `allowed-tools` is present and non-empty, validation MUST fail unless an accepted proposal and spec explicitly allow tool use.

<a id="r8"></a>

R8. `description` MUST be English-facing metadata suitable for assistant UI and invocation.

<a id="r9"></a>

R9. `description` MUST explain both what the skill does and when to use it.

<a id="r10"></a>

R10. Skill descriptions SHOULD state what the skill does first, then name the triggering situations clearly enough for reliable selection.

<a id="r11"></a>

R11. Each skill body MUST include `$ARGUMENTS`.

<a id="r12"></a>

R12. Each skill body MUST include a `## Output Format` section.

<a id="r13"></a>

R13. A new or materially changed skill MUST include at least three eval scenarios: normal intended use, vague or indirect trigger, and edge, safety, failure, non-trigger, or misuse behavior.

<a id="r14"></a>

R14. Eval scenarios MUST contain concrete user prompts or situations and expected observable behavior.

<a id="r15"></a>

R15. Eval scenarios MUST NOT require live model calls in CI.

<a id="r16"></a>

R16. The repository MUST define grandfathered skills through the checked-in artifact `tests/evals/skills/grandfathered-skills.yaml`. The artifact MUST exist before implementation planning begins. It MUST list the exact skill directory names under `skills/` that are exempt from the initial eval-fixture requirement until materially changed. The artifact, not a commit hash, branch name, README table, or future implementation commit, is the source of truth for grandfathering. Each entry MUST match an existing `skills/<skill-name>/` directory at the time the baseline artifact is created. The validator MUST fail if the artifact contains a skill that no longer exists, unless the corresponding skill removal is part of the same change. A skill listed in the baseline artifact MAY lack `tests/evals/skills/<skill-name>/cases.yaml` only while it remains editorially unchanged. If a grandfathered skill receives a material change, it MUST satisfy the same eval-fixture requirements as a new skill before merge. A skill not listed in the baseline artifact MUST provide `tests/evals/skills/<skill-name>/cases.yaml` before merge. Material-change detection MUST follow this specification's material-change definition. When materiality is unclear, reviewers MUST treat the change as material.

<a id="r17"></a>

R17. A material skill change MUST include any change that could alter what the skill does, when it triggers, or what it returns.

<a id="r18"></a>

R18. Changes to `name`, `description`, output format, `$ARGUMENTS` handling, execution-affecting frontmatter, workflow steps, safety rules, or referenced files MUST be treated as material unless the reviewer records a narrower rationale.

<a id="r19"></a>

R19. Editorial skill changes MAY proceed without new eval fixtures when they leave trigger behavior, output contract, workflow steps, referenced files, and safety behavior unchanged.

<a id="r20"></a>

R20. Unclear material-versus-editorial cases MUST be treated as material.

<a id="r21"></a>

R21. High-risk new or materially changed skills MUST include scope boundaries, escalation or refusal behavior, reviewer-visible safety notes, and at least one safety or misuse eval case.

<a id="r22"></a>

R22. Detailed shared schemas for high-risk domains MUST NOT be required in the first implementation slice.

<a id="r23"></a>

R23. A skill quality review MUST include a mission-fit check: engineering-facing skills are evaluated for reduction of repetitive engineering work, clarification of review evidence, or improvement of execution quality; non-engineering productivity skills are evaluated for the same kind of efficiency gain in their domain.

<a id="r24"></a>

R24. `SKILL.md` files SHOULD stay under 300 lines when practical.

<a id="r25"></a>

R25. New or materially changed `SKILL.md` files MUST NOT exceed 500 lines unless an accepted exception explains why progressive disclosure is not suitable.

<a id="r26"></a>

R26. Skills approaching the length ceiling SHOULD move detail into one-level-deep reference files.

<a id="r27"></a>

R27. Reference files over roughly 100 lines SHOULD include a table of contents.

<a id="r28"></a>

R28. README synchronization MUST cover the skill table, slash-command list, and install instructions.

<a id="r29"></a>

R29. README synchronization MUST be checked separately from per-skill structural validation.

<a id="r30"></a>

R30. Blocking automated checks MUST be objective and mechanically verifiable.

<a id="r31"></a>

R31. Reviewer heuristics such as trigger quality, concision quality, mission fit, and safety adequacy MUST be surfaced through eval evidence or review checklists rather than brittle CI gates.

<a id="r32"></a>

R32. Validation MUST distinguish compatibility rules, Skillsmith policy, and reviewer heuristics.

<a id="r33"></a>

R33. CI MUST run deterministic checks only; live model execution MUST NOT be required in CI for this first slice.

<a id="r34"></a>

R34. Manual model smoke evidence MUST be required only when a change is high-risk, behavior-heavy, or claims model-specific behavior.

<a id="r35"></a>

R35. The first implementation slice MUST keep existing skills installable.

<a id="r36"></a>

R36. New or materially changed skills SHOULD have one clear primary job unless the accepted proposal and spec justify a broader skill boundary.

<a id="r37"></a>

R37. New or materially changed skills SHOULD avoid input-type detection, effort-scaling branches, fallback branches, or scenario accumulation unless the accepted behavior requires them.

<a id="r38"></a>

R38. New or materially changed skills SHOULD design known failure modes out of the workflow when a structural rule can make the failure impossible or unlikely.

<a id="r39"></a>

R39. New or materially changed skills SHOULD put behavioral guarantees in the Markdown body rather than relying on optional frontmatter.

<a id="r40"></a>

R40. New or materially changed skill descriptions SHOULD use third-person descriptive language, state the skill function before trigger situations, and include distinguishing output shape when output shape affects selection.

<a id="r41"></a>

R41. New or materially changed skills SHOULD prefer a small number of durable directives over many narrow rules when those directives cover the same boundary behavior.

<a id="r42"></a>

R42. New or materially changed skills SHOULD include a verification or consistency-check step when output quality can silently drift from source meaning, user intent, safety boundaries, or requested format.

<a id="r43"></a>

R43. New or materially changed skills SHOULD use consistent vocabulary between workflow instructions and output templates.

<a id="r44"></a>

R44. New or materially changed skills SHOULD make output contracts specific enough for reviewers to observe, including concrete dimensions for reasons, assessments, checks, or refusals when those sections are required.

<a id="r45"></a>

R45. Reviewers SHOULD treat known tradeoffs, such as fixed output verbosity for trivial input, as acceptable when the accepted requirements deliberately choose that behavior and the tradeoff is recorded.

<a id="r46"></a>

R46. Reviewers SHOULD stop requesting prompt wording refinements once remaining concerns are cosmetic and the next useful evidence is behavioral eval output.

<a id="r47"></a>

R47. Reviewer heuristics for skill design philosophy, including simplicity, branch avoidance, body-owned behavior, vocabulary precision, fixed output contracts, and known tradeoffs, MUST be surfaced through eval evidence, review notes, or checklist findings rather than brittle CI gates.

<a id="r48"></a>

R48. New or materially changed structured output contracts SHOULD use concise bold labels, put copyable content on its own line below each label, visually separate deliverables from supporting commentary where useful, and avoid emoji or decorative symbols unless an accepted skill spec explicitly requires them.

## Inputs and outputs

Inputs:

- `skills/*/SKILL.md`
- `tests/evals/skills/<skill-name>/cases.yaml` or an equivalent accepted eval fixture path
- `tests/evals/skills/grandfathered-skills.yaml`
- README skill table, slash-command list, and install instructions
- `CONSTITUTION.md`, `AGENTS.md`, `docs/workflows.md`, and `.github/pull_request_template.md`
- `tests/validate_skills.py`
- a README sync helper, expected as `tests/check_readme_sync.py` unless changed by spec review

Outputs:

- contributor-visible skill-quality standard at `docs/skill-quality-standard.md`
- validation failures for blocking structural and policy violations
- validation warnings for grandfathered or staged checks
- reviewer-visible eval and safety evidence for subjective quality
- updated governance and contributor documentation

## State and invariants

- The canonical skill-quality standard is this spec once approved.
- [the original quality proof map](https://github.com/xiongxianfei/skillsmith/blob/e3ab8b3f4c07d4f96a97ec69d8f73b3a92e17aa1/specs/skill-quality-standard.test.md) maps this spec to validation and eval checks without restating the full standard.
- `tests/evals/skills/grandfathered-skills.yaml` is the only source of truth for grandfathered skill names.
- Existing skills listed in the grandfathering baseline remain grandfathered for eval-fixture enforcement until materially changed.
- Skills remain pure prompt assets unless a later accepted proposal and spec change that boundary.
- `argument-hint`, `effort`, and `allowed-tools` are omitted from current skill frontmatter.
- CI remains deterministic and does not depend on live model calls.
- Skill design philosophy is reviewer guidance unless a requirement states a mechanically verifiable rule.

## Error and boundary behavior

- Invalid YAML frontmatter is a blocking validation error.
- Missing `name`, `description`, `$ARGUMENTS`, or `## Output Format` is a blocking validation error after this standard is implemented.
- Missing `argument-hint`, `effort`, and `allowed-tools` is not an error or warning.
- Invalid `effort` values are validation errors when the field is present, but current skills should omit the field.
- Missing eval fixtures are warnings for grandfathered skills and blocking errors for new or materially changed skills once the material-change detection path exists.
- Stale entries in `tests/evals/skills/grandfathered-skills.yaml` are validation errors unless the corresponding skill deletion is part of the same change.
- README sync drift starts as a warning and becomes blocking once the sync helper is reliable and documented.
- Description quality failures are review findings unless the failure is mechanically checkable.
- Skill design philosophy failures are review findings unless the failure is mechanically checkable.
- If the validator cannot determine whether a change is new, material, or grandfathered, it must not silently pass the change as editorial; it must surface the uncertainty for review.

## Security and privacy

- Eval fixtures and examples MUST use fictional or sanitized inputs.
- Eval fixtures MUST NOT contain secrets, credentials, private local paths, or unpublished personal data.
- High-risk skills MUST include reviewer-visible safety notes and at least one safety or misuse eval scenario.
- Medical, legal, financial, security, or similarly high-impact skills MUST NOT present themselves as substitutes for licensed professionals, emergency services, official advice, or authorized security review.
- Skills SHOULD omit `allowed-tools`; non-empty tool permissions require a later accepted proposal and spec.

## Accessibility and UX

No interactive UI is introduced.

Contributor-facing docs and validation errors SHOULD use direct, actionable language that identifies the file, failing rule, and expected fix.

## Performance expectations

- Local validation SHOULD complete quickly enough for ordinary pre-PR use on the current repository size.
- Validation MUST remain deterministic.
- CI MUST NOT require network access beyond normal dependency installation and repository checkout for this first slice.
- Eval fixture checks MUST parse static files only.

## Edge cases

<a id="ec1"></a>

EC1. A description typo changes trigger meaning. Treat the change as material if trigger behavior could change.

<a id="ec2"></a>

EC2. A skill adds a reference file without changing `SKILL.md` instructions. Treat the change as material because referenced files can alter behavior.

<a id="ec3"></a>

EC3. A high-risk skill adds a minor safety wording change. Treat the change as material unless a reviewer records why behavior is unchanged.

<a id="ec4"></a>

EC4. A skill omits `argument-hint`, `effort`, and `allowed-tools`. Validation passes because these fields are omitted by default.

<a id="ec5"></a>

EC5. A skill includes `effort: ultra`. Validation fails when allowed values do not include `ultra`.

<a id="ec6"></a>

EC6. README lists a skill that no longer exists. README sync reports drift.

<a id="ec7"></a>

EC7. README omits a skill that exists under `skills/`. README sync reports drift.

<a id="ec8"></a>

EC8. A skill exceeds 500 lines but has no exception. New or materially changed skill validation fails after grandfathering rules are active.

<a id="ec9"></a>

EC9. An eval fixture has three scenarios but none covers indirect trigger behavior. Eval fixture validation reports the missing category.

<a id="ec10"></a>

EC10. A contributor claims a skill works better on a specific model. Manual model smoke evidence is required for that claim.

<a id="ec11"></a>

EC11. The grandfathering baseline lists `old-skill`, but `skills/old-skill/` does not exist. Validation fails unless the same change removes that skill and its baseline entry.

<a id="ec12"></a>

EC12. A new skill is not listed in the grandfathering baseline and has no `cases.yaml`. Validation fails before merge.

## Non-goals

- Do not rewrite all existing skills in the first implementation slice.
- Do not require live model CI.
- Do not introduce tool-using skills.
- Do not add `.claude-plugin` validation.
- Do not make subjective prompt quality a brittle CI gate.
- Do not make design-philosophy heuristics a brittle CI gate.
- Do not create a second canonical skill-quality standard under `docs/`.

## Acceptance criteria

These criteria retain their original IDs. Creation, baseline and first-slice timing conditions describe the original delivery; continuing behavior and evidence obligations remain applicable to future material changes. Moving this contract does not renew prior acceptance.

<a id="ac1"></a>

AC1. `docs/skill-quality-standard.md` exists and contains testable or reviewer-observable requirements for skill metadata, body structure, design philosophy, eval fixtures, high-risk safety gates, README sync, runtime-specific metadata omission, and grandfathering.

<a id="ac2"></a>

AC2. [the original quality proof map](https://github.com/xiongxianfei/skillsmith/blob/e3ab8b3f4c07d4f96a97ec69d8f73b3a92e17aa1/specs/skill-quality-standard.test.md) maps each requirement in this spec to validation, fixture review, manual review, or non-applicable coverage.

<a id="ac3"></a>

AC3. `CONSTITUTION.md` is updated so `argument-hint`, `effort`, and `allowed-tools` are omitted by default.

<a id="ac4"></a>

AC4. Contributor and agent docs no longer describe `argument-hint`, `effort`, or `allowed-tools` as required fields.

<a id="ac5"></a>

AC5. Deterministic validation checks continue to pass for the existing repository after grandfathering is applied.

<a id="ac6"></a>

AC6. New or materially changed skills require the three eval scenario categories.

<a id="ac7"></a>

AC7. High-risk new or materially changed skills require lightweight safety evidence.

<a id="ac8"></a>

AC8. README sync covers the skill table, slash-command list, and install instructions.

<a id="ac9"></a>

AC9. CI does not require live model calls.

<a id="ac10"></a>

AC10. `python tests/validate_skills.py` passes after the first implementation slice.

<a id="ac11"></a>

AC11. `tests/evals/skills/grandfathered-skills.yaml` exists before implementation planning.

<a id="ac12"></a>

AC12. The grandfathering artifact lists only existing `skills/<skill-name>/` directories.

<a id="ac13"></a>

AC13. The grandfathering artifact lists skill names lexicographically and contains no paths.

<a id="ac14"></a>

AC14. Validation or a test helper can distinguish listed grandfathered skills without eval fixtures, listed grandfathered skills with material changes that require eval fixtures, unlisted new skills that require eval fixtures, and stale baseline entries that fail validation unless removed with the same skill deletion.

## Open questions

- Should README sync include a `--fix` mode in the first implementation slice or only report drift?
- Which reserved platform words beyond `anthropic` and `claude` should the validator reject?

## Resolved Decision: Grandfathering Baseline

Grandfathering is not tied to an accepted proposal commit. The deterministic baseline is the checked-in artifact `tests/evals/skills/grandfathered-skills.yaml`. Test spec and implementation planning MUST use that file as the source of truth.

## Compatibility and migration

- The implementation MUST update `CONSTITUTION.md` so optional frontmatter is omitted by default.
- The implementation MUST use `tests/evals/skills/grandfathered-skills.yaml`, not a commit hash, branch name, README table, or future implementation commit, to determine grandfathered skills.
- The implementation MUST update `AGENTS.md`, `docs/workflows.md`, README, and PR template guidance to align with this standard.
- Existing skills are grandfathered for eval fixtures but not for core parseability and required structural fields already enforced by the validator.
- The implementation MUST NOT reintroduce `.claude-plugin` or plugin metadata validation.
- Rollback may reduce validator gating while preserving eval fixtures and the quality standard as reviewer guidance.

## Observability

- Local validation output MUST report the number of skills checked.
- Validation output MUST distinguish warnings from errors.
- README sync output MUST identify missing, extra, or mismatched README entries.
- Eval fixture validation output MUST identify the skill and scenario category that is missing or malformed.
- PRs for new or materially changed skills MUST include validation command output or an explicit explanation when a check could not be run.
- Reviews for new or materially changed skills SHOULD record any material design-philosophy tradeoffs that affect output length, trigger breadth, workflow branching, safety boundaries, or eval interpretation.
