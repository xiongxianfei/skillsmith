# Proposal: RigorLoop-Governed Skill Quality System for Skillsmith

## Status

accepted

## Problem

Skillsmith already has a useful catalog of reusable AI prompt skills and a fast structural validator. The current workflow catches important shape errors, such as missing frontmatter, missing `$ARGUMENTS`, and missing `## Output Format`, but it does not yet give contributors a durable way to show why a skill belongs, what quality standard it follows, or what scenarios prove that a skill change is reviewable.

The repository now has standing governance artifacts: `VISION.md`, `CONSTITUTION.md`, `docs/workflows.md`, and `docs/project-map.md`. Those artifacts establish the project identity and workflow baseline, but they do not yet define a contributor-facing skill-quality standard or an evaluation convention for new and materially changed skills.

Without that next layer, Skillsmith risks accepting prompts that pass structural validation but still have weak trigger behavior, vague output contracts, poor safety handling, or no realistic examples for reviewers.

The first slice also needs to stay proportional. The current working tree has ten skills and a small maintenance surface, so the quality system should prove its value by reducing review ambiguity and repetitive engineering work, not by making every contribution pass through unnecessary ceremony.

## Goals

1. Establish a RigorLoop-compatible quality path for skill additions and material revisions.
2. Define a Skillsmith skill-quality standard that turns current governance and skill-authoring expectations into contributor-facing review criteria.
3. Introduce evaluation-driven skill development with at least three representative scenarios for each new or materially changed skill.
4. Keep Skillsmith portable across models while preserving Codex slash-command and Claude Code skill usage.
5. Extend fast deterministic validation for objective structural checks while leaving subjective quality judgments visible to reviewers.
6. Keep repository identity and contributor documentation aligned around Skillsmith.
7. Connect skill quality to the project mission: a skill should help users, especially engineers and self-directed professionals, complete repeatable work with less prompting, less ambiguity, or better review evidence.

## Non-goals

1. Do not rewrite every existing skill in the first implementation slice.
2. Do not require live model calls in CI as the first version of evaluation.
3. Do not turn pure prompt skills into tool-using skills.
4. Do not replace human review with automated validation.
5. Do not reintroduce `.claude-plugin` or plugin metadata checks; plugin distribution is outside the current repository boundary.

## Vision fit

fits the current vision

The proposal strengthens Skillsmith's commitment to reusable judgment, reviewable prompts, portable Markdown skills, and concrete validation. It also supports the vision's refusal to become a grab bag of clever prompts without reviewable structure.

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
|---|---|---|
| Use RigorLoop for Skillsmith development | in scope | Goals, Recommended Direction, Next Artifacts |
| Create and save a proposal | in scope | Status, all proposal sections |
| Follow best practices for skill authoring | in scope | Context, Recommended Direction, Testing and Verification Strategy |
| Apply the proposal to Skillsmith | in scope | Problem, Vision fit, Architecture Impact |
| Avoid jumping straight to implementation | in scope | Status, Readiness, Next Artifacts |
| Resolve old ai-skills naming drift | already satisfied by current branch; no longer core scope | Context, Scope budget |
| Bootstrap vision and constitution | already satisfied by current branch; no longer core scope | Context, Scope budget |
| Keep plugin metadata valid | rejected option | Non-goals, Scope budget |
| Right-size the process for the current repo size | in scope | Problem, Scope budget, Recommended Direction, Risks and Mitigations |
| Connect the standard to engineering efficiency | in scope | Goals, Vision fit, Recommended Direction |

## Scope budget

| Work item | Treatment | Reason |
|---|---|---|
| `VISION.md`, `CONSTITUTION.md`, `docs/workflows.md`, and `docs/project-map.md` bootstrap | same-slice dependency | These standing artifacts are expected in the working branch review packet. If the review target lacks them, they remain same-slice bootstrap dependencies. |
| One canonical skill-quality standard at `specs/skill-quality-standard.md` | core to this proposal | A single authoritative standard reduces drift while still giving contributors readable criteria. |
| `docs/skill-quality-standard.md` | out of scope | Avoid a parallel docs/specs standard in the first slice; contributor docs should link to or summarize the canonical standard instead. |
| Evaluation fixtures for skills | core to this proposal | Realistic scenarios make skill behavior reviewable beyond structural checks. |
| Validator extension | core to this proposal | Objective rules should be caught locally and in CI. |
| `CONSTITUTION.md` compatibility-rule update | core to this proposal | The first slice changes `effort` from required to optional, so the higher-ranked governance rule must be updated before spec relies on that policy. |
| README, CONTRIBUTING, AGENTS, CLAUDE, and PR template updates | core to this proposal | Contributor-facing docs need to reflect the new quality path. |
| Rename from ai-skills to Skillsmith | same-slice dependency | Expected in the working branch review packet. If the review target still uses old naming, naming cleanup remains a same-slice dependency. |
| Rewrite all existing skills to the new standard | separate implementation slice | Useful, but too broad for the first quality-system change. |
| Live model evaluation in CI | deferable follow-up | Valuable later, but it adds cost, nondeterminism, secrets, provider dependency, and model drift. |
| Domain-specific safety standards for medical, security, legal, and financial skills | core minimal gate; detailed schema deferred | High-risk domains need minimum safety review now, but detailed shared schemas should wait until repeated patterns justify them. |
| `.claude-plugin` or plugin metadata validation | out of scope | The project intentionally removed `.claude-plugin`; current validation should not require it. |

## Context

Skillsmith's current project map identifies the repository as a plain Markdown prompt-skill library. Skill behavior lives in `skills/<skill-name>/SKILL.md`, validation lives in `tests/validate_skills.py`, installation lives in `install.sh`, and CI runs the validator through `.github/workflows/validate.yml`.

The constitution defines the source-of-truth order and says non-trivial skill additions, output-contract changes, validation changes, installer changes, and compatibility changes need written requirements before implementation. It also preserves the pure-prompt boundary: skills use `allowed-tools: ""` unless a later accepted change revises that direction.

The workflow guide defines the standard lifecycle and local artifact locations. This proposal is the decision artifact before a skill-quality spec, test spec, implementation plan, and validator changes.

The working branch for this proposal is expected to contain the standing governance artifacts and Skillsmith naming cleanup. Proposal acceptance depends on those branch-local artifacts being present in the review evidence set; otherwise, the naming and plugin-validation cleanup remain same-slice dependencies.

The current working tree contains ten skill files, and the local README table lists those ten skills. If the public default branch shows fewer skills, that is repository-state drift outside this proposal's current evidence set; the proposed README synchronization check is meant to catch that class of drift during future changes.

The current official Claude Code skills documentation lists `effort` as an optional frontmatter field that can override session effort while a skill is active. That makes `effort` a valid compatibility surface, but not a reason to require every portable Skillsmith skill to declare `effort: high`.

## Options Considered

### Option 1: Keep the current lightweight validator only

This preserves today’s simple contribution path, but it leaves most skill-quality decisions to ad hoc reviewer judgment. It does not create evaluation-driven development or a durable standard for trigger quality, output clarity, or safety review.

Disposition: rejected.

### Option 2: Adopt the full quality system and rewrite every skill immediately

This would improve consistency quickly, but it combines standards, documentation, validation, eval design, safety review, and ten skill rewrites into one oversized review unit.

Disposition: rejected for the first implementation slice.

### Option 3: Add governance-backed quality gates for new and materially changed skills first

This adds a contributor-facing quality standard, evaluation fixture convention, validator improvements, and review documentation without requiring an immediate rewrite of all existing skills.

Disposition: recommended.

### Option 4: Make live model evaluations mandatory in CI

This measures real model behavior more directly, but it introduces cost, nondeterminism, provider dependency, secrets management, and model-version drift. Static fixtures and manual model evidence are a better first step.

Disposition: deferred follow-up.

## Recommended Direction

Adopt Option 3: add governance-backed quality gates for new and materially changed skills first, with a deliberately small first slice.

The first implementation slice should introduce a small durable quality system:

1. Add one canonical standard at `specs/skill-quality-standard.md` with contributor-facing criteria for skill purpose, trigger quality, metadata, `$ARGUMENTS`, output format, concision, progressive disclosure, examples, eval scenarios, mission fit, and high-risk domain expectations.
2. Add an eval fixture convention such as `tests/evals/skills/<skill-name>/cases.yaml`.
3. Require at least three scenarios for each new or materially changed skill: normal intended use, vague or indirect trigger, and edge/safety/failure case.
4. Extend `tests/validate_skills.py` for objective checks such as lowercase hyphenated names, required `allowed-tools: ""`, README skill-table sync, and presence or grandfathering of eval fixtures.
5. Treat `effort` as optional. The validator may check allowed values when the field is present, but should not require `effort`, should not require `effort: high`, and should not let effort-specific behavior become part of the portable skill contract.
6. Update `CONSTITUTION.md` so the compatibility rule no longer lists `effort` as required. It should define `effort` as optional frontmatter whose allowed values may be validated when present.
7. Update `CONTRIBUTING.md`, `.github/pull_request_template.md`, `AGENTS.md`, and `CLAUDE.md` so contributors and agents know what evidence to provide.
8. Keep existing skills grandfathered initially unless they are materially changed.

The standard should include a mission-fit criterion without over-narrowing the catalog: for engineering-facing skills, reviewers should ask whether the skill measurably reduces a repetitive engineering task, clarifies review evidence, or improves execution quality. For non-engineering productivity skills, reviewers should ask the same kind of efficiency question in that domain rather than accepting vague usefulness.

For high-risk domains, the first slice requires a lightweight safety gate, not a full domain-specific safety schema. New or materially changed medical, security, legal, financial, or similarly high-impact skills should include scope boundaries, escalation or refusal behavior, at least one safety or misuse eval case, and reviewer-visible safety notes. Detailed domain-specific schemas are deferred until repeated patterns justify them.

The spec should also encode these calibration decisions:

1. A material skill change is any change that could alter what the skill does, when it triggers, or what it returns. That includes changes to `name`, `description`, output format, `$ARGUMENTS` handling, execution-affecting frontmatter, workflow steps, safety rules, or referenced files. Editorial changes are typo, grammar, formatting, link, or wording cleanups that leave trigger behavior, output contract, workflow steps, and safety behavior unchanged. Unclear cases should be treated as material.
2. Immediate blocking checks should be objective and already satisfied by existing skills: valid YAML frontmatter, parseable `SKILL.md`, lowercase hyphenated names no longer than 64 characters, non-empty descriptions within the local length limit, `$ARGUMENTS`, and `## Output Format`.
3. Grandfathering checks should begin as warnings and promote only when their trigger is clear. Eval fixtures should block new and materially changed skills first. README sync should warn first and become blocking once the sync mechanism is reliable. Length thresholds should warn before they block. Description-quality heuristics should stay reviewer-facing unless they become mechanically unambiguous.
4. README synchronization should live in a separate helper, such as `tests/check_readme_sync.py`, invoked by CI alongside `tests/validate_skills.py`. It should cover the skill table, slash-command list, and install instructions. It may later gain a `--fix` mode that regenerates the table from skill frontmatter.
5. `SKILL.md` length guidance should use progressive disclosure. Around 300 lines should prompt a soft warning. Around 500 lines should be treated as the ceiling for new skills after grandfathering. The preferred remedy is one-level-deep reference files, with a table of contents for any reference file over roughly 100 lines.
6. Existing skills under `skills/*` as of 2026-05-25 are grandfathered for eval-fixture enforcement until materially changed. The spec should replace the date with the accepted proposal commit once known.
7. Validator and review rules should distinguish compatibility rules, Skillsmith policy, and reviewer heuristics:

   | Class | Examples | Enforcement |
   |---|---|---|
   | Compatibility rule | valid YAML, valid name syntax, non-empty description | blocking |
   | Skillsmith policy | `$ARGUMENTS`, `## Output Format`, `allowed-tools: ""` for pure-prompt skills | blocking after grandfathering rules |
   | Reviewer heuristic | trigger quality, concision quality, mission fit, safety adequacy | surfaced in eval/review, not brittle CI |

## Expected Behavior Changes

After implementation, contributors should not add or materially revise a skill by only copying a prompt into `skills/<name>/SKILL.md`.

New and materially changed skills should include reviewable evaluation scenarios.

Reviewers should be able to distinguish structural validity, trigger quality, output-contract quality, portability, and safety quality.

CI should continue to block objective structural failures. Subjective quality issues should be surfaced through fixtures, documentation, and review checklists rather than hidden in brittle automated judgments.

## Architecture Impact

This change affects repository workflow, docs, test fixtures, and validation. It does not change runtime execution of individual skills.

Expected touched areas:

```text
specs/skill-quality-standard.md
specs/skill-quality-standard.test.md
tests/validate_skills.py
tests/evals/skills/
CONSTITUTION.md
CONTRIBUTING.md
AGENTS.md
CLAUDE.md
README.md
.github/pull_request_template.md
docs/proposals/
```

No skill needs tool permissions as part of this proposal. The pure-prompt convention remains the default.

`specs/skill-quality-standard.md` should be authoritative for the quality standard. `specs/skill-quality-standard.test.md` should map the standard to validation and eval checks without restating the full standard. README, CONTRIBUTING, AGENTS, and CLAUDE should summarize and link rather than duplicate the rules.

## Testing and Verification Strategy

Use layered evidence:

1. Run the current validator:

   ```bash
   python tests/validate_skills.py
   ```

2. Add focused validator tests or fixtures for invalid names, missing `$ARGUMENTS`, missing `## Output Format`, missing or non-grandfathered eval fixtures, stale README skill table entries, non-English metadata, and optional `effort` values when present.

3. Review eval scenarios for changed skills: normal intended use, indirect trigger, and edge/safety/failure behavior. For skills likely to over-trigger or be misused, the edge case may be a non-trigger or misuse case.

4. For high-risk or behavior-heavy skill changes, include at least one manual model smoke summary in the PR or change artifact, including model, prompt, and result summary.

5. Require cross-model evidence only when a PR claims model-specific behavior, changes a high-risk skill, or changes behavior-heavy prompt logic. Static eval fixtures remain the baseline evidence for ordinary new or materially changed skills.

6. Check documentation consistency across README, CONTRIBUTING, AGENTS, CLAUDE, PR template, README install instructions, command lists, and the skill-quality standard.

## Rollout and Rollback

Roll out in stages:

1. Accept this proposal after review.
2. Write the canonical skill-quality spec and a focused test spec that maps checks without duplicating the standard.
3. Add the quality standard and eval fixture convention.
4. Extend validator checks with grandfathering for existing skills where needed.
5. Update contributor and agent docs.

Rollback is straightforward: reduce or revert validator gating while keeping eval fixtures and quality docs as reviewer guidance. Existing skills should remain installable throughout the rollout.

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| The process becomes too heavy for small prompt edits. | Apply the full path to new skills and material behavior changes; allow small editorial fixes to use normal PR review. |
| Eval fixtures become paperwork. | Require concrete user prompts and expected behavior, not abstract checklist prose. |
| Validator false positives block useful changes. | Keep subjective checks as reviewer guidance; automate only objective checks. |
| Existing skills fail new standards immediately. | Grandfather existing skills and apply gates when they are materially changed. |
| Pushy descriptions over-trigger skills. | Include both indirect-trigger and non-trigger or misuse scenarios in eval review where relevant. |
| High-risk skills need deeper safety review. | Start with lightweight per-skill safety notes and safety edge cases; extract a shared schema later only after repeated patterns are clear. |
| Quality rules drift from project identity. | Check future changes against `VISION.md`, `CONSTITUTION.md`, and `docs/project-map.md`. |
| Governance overhead outweighs skill quality gains. | Keep the first slice to one canonical standard, eval fixtures, validator checks, and contributor docs; defer broad backfills and live model CI. |

## Open Questions

None blocking before spec authoring.

The spec should still settle exact warning-to-error promotion timing for grandfathered skills and whether the README sync helper should ship with a `--fix` mode in the first implementation slice.

## Decision Log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-05-25 | Recommend governance-backed quality gates for new and materially changed skills first | Improves reviewability without forcing a broad rewrite or nondeterministic CI | Lightweight validator only; full immediate rewrite; mandatory live model CI |
| 2026-05-25 | Right-size the first slice to one canonical standard plus eval and validator changes | Reduces documentation drift and contributor overhead for the current repo size | Parallel docs/specs/test-standard triad as coequal sources |
| 2026-05-25 | Keep `effort` optional rather than required | Current Claude Code docs support it as optional, but requiring one constant value adds little information and weakens portability | Require `effort: high`; remove `effort` immediately |
| 2026-05-25 | Use behavioral surface to classify material changes | Trigger, output, workflow, safety, and execution-affecting edits are the review surfaces that need eval evidence | Classify by diff size |
| 2026-05-25 | Keep README sync as a separate helper | README sync is a cross-artifact consistency check, not per-skill structural validation | Fold README parsing into the skill validator |
| 2026-05-25 | Accept proposal after required review revisions | Required evidence wording and high-risk-scope revisions were incorporated | Send directly to spec with ambiguous evidence wording and high-risk scope |
| 2026-05-25 | Include `CONSTITUTION.md` compatibility update in the first slice | Optional `effort` conflicts with the current higher-ranked constitution unless the governance rule changes too | Let the spec rely on optional `effort` while leaving the constitution unchanged |

## Next Artifacts

1. `specs/skill-quality-standard.md`.
2. `specs/skill-quality-standard.test.md`.
3. Architecture note only if the spec introduces complex fixture formats, validator restructuring, or generated outputs that need long-lived design decisions.
4. Implementation plan after spec, review, and test-spec are settled.

## Follow-on Artifacts

Proposal review completed in user review on 2026-05-25. Required revisions were incorporated into this accepted proposal.

## Readiness

Accepted and ready for `spec` and `test-spec` authoring.

This proposal is not implementation-ready or PR-ready. Specification and test specification are the next required artifacts before implementation planning.
