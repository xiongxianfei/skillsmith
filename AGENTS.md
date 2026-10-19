# Skillsmith

Turn good practices into reusable AI skills and continually improve them through use, feedback, and evaluation. Each skill is a portable directory package with a required `SKILL.md` and optional `references/`, `scripts/`, `assets/`, and other resources. Agents should read additional files only when the skill's instructions call for them.

Use the owning document for each concern:

| Concern | Owner |
| --- | --- |
| Project purpose and scope | [VISION.md](VISION.md) |
| Agent conduct and engineering principles | This file |
| Required skill metadata, safety, portability and review guidance | [Quality standard](docs/skill-quality-standard.md) |
| Contribution, validation and PR workflow | [Workflow guide](docs/workflows.md) |
| Intended behavior, constraints and design decisions | [C4 architecture](design/architecture/README.md) |

Resolve conflicting guidance explicitly in its owner. Observed implementation and historical reviews do not silently override accepted decisions; record explicit user policy changes in the affected owner.

## Build & Validate

```
python tests/validate_skills.py
```

CI runs this on every push/PR to main. All errors must be fixed before merge.

## Operating Rules

- Inspect the current repo state before editing.
- Keep changes scoped; do not refactor unrelated files.
- Preserve user changes and never revert work you did not make unless explicitly asked.
- Update the owning artifact: prompt behavior in `skills/*/SKILL.md`, validation behavior in `tests/validate_skills.py`, install behavior in `install.sh`, project identity in `VISION.md`; use the owners above for documentation and rules.
- Report validation commands, warnings, skipped checks, and unresolved questions before handoff.
- State assumptions when intent is incomplete; clarify before irreversible or high-risk decisions.
- Never invent tests, CI results, approvals, issue links, release status or external facts. Claim behavior works only with relevant evidence, or explicitly state what was not verified.
- Do not silently remove safety boundaries, validation checks or compatibility obligations. Authors cannot claim independent approval of their own work.

## Required Skill Metadata

Every skill lives at `skills/<skill-name>/SKILL.md`. Start the file with valid YAML frontmatter containing non-empty string values for `name` and `description`:

```yaml
---
name: your-skill-name
description: >
  Describe what the skill does and when it applies.
---
```

The body has no required placeholder or heading. Use `$ARGUMENTS` or `## Output Format` only when useful for the skill and its intended host. CI checks required files and metadata only; see the [quality standard](docs/skill-quality-standard.md#required-checks).

## Key Rules

- Descriptions should state the skill identity first, then the triggering situations, including indirect/casual user phrasing
- Keep always-needed behavior in `SKILL.md`; include focused, conditionally loaded references for specialized knowledge; add scripts only for repeatable executable operations.
- Include optional metadata only when useful and compatible with the intended host; the validator checks the format of the defined Agent Skills metadata fields
- Describe substantive skill changes and expected behavior in the PR; see `docs/skill-quality-standard.md`
- High-risk skills need explicit scope, refusal/escalation boundaries and reviewer-visible safety notes

## Workflow

Use [the workflow guide](docs/workflows.md) for scoped changes, validation and PR review. Use `c4-architecture` for design under [design/architecture/](design/architecture/README.md); keep behavior, constraints and decisions together in the relevant architecture specification.

- All changes via PR to `main` (branch protection enabled)
- Branch naming: `feat/`, `fix/`, `docs/`, `improve/`
- Squash merge, delete branch after merge
- IMPORTANT: Always branch from latest `main` — never stack PRs from the same base to avoid README conflicts
- When adding a new skill, also add it to the README skills table
- Non-trivial behavior changes need written intent and acceptance examples before implementation; see [the workflow guide](docs/workflows.md#1-define-the-change).

## Project Structure

```
skills/*/SKILL.md          ← entrypoint for portable skill directory packages
tests/validate_skills.py   ← required-file and metadata validator (errors block merge)
install.sh                 ← one-command installer (supports --target flag)
design/architecture/       ← C4 specifications, models, views and generated diagrams
docs/skill-quality-standard.md ← skill authoring, safety and review guidance
docs/workflows.md          ← contribution, validation and PR workflow
VISION.md                  ← project identity and scope
```

## Common Mistakes

- Missing or unreadable `SKILL.md` → CI error
- Missing, malformed or non-mapping YAML frontmatter → CI error
- Missing, blank or non-string `name` or `description` → CI error
- Invalid Agent Skills name, name/directory mismatch, or out-of-bounds metadata length → CI error
- Descriptions that omit either the skill's function or the situations where it applies → unreliable skill selection

## Core Engineering Principles

1. **Self-contained knowledge.** Make each substantive document understandable on its own: explain the problem, essential terms, prerequisites, mechanisms, examples, and boundaries. Link to deeper material without requiring readers to follow links to understand the core argument. Keep canonical definitions in one place; avoid needless duplication.

2. **Reader-centered quality.** Evaluate whether a reader can explain *what happens, how, why, and when*; apply the knowledge to a realistic problem; predict likely outcomes and failure modes; and recognize opportunities to improve results. Correctness and clear reasoning matter more than polished prose.

3. **Goal-oriented work.** Identify the intended reader outcome before substantial work. Choose the smallest sufficient change; prioritize important knowledge gaps and useful results. Avoid speculative infrastructure, redundant research, unnecessary documentation, and rituals that do not advance the goal. Do not skip essential verification to save effort.

4. **Reuse before invention.** Look for established theory, standards, sources, methods, libraries, and tools before building alternatives. Prefer suitable, proven approaches; weigh fitness, reliability, cost, maintenance, and lock-in. Create custom solutions only when a material requirement justifies them.

5. **Mechanisms before memorization.** Explain causal relationships, relevant variables, assumptions, boundary conditions, and trade-offs. Show how the mechanism informs decisions and practical action. Surface possible improvements and testable hypotheses, clearly separating proposed innovations from demonstrated results.

6. **Delete obsolete internal compatibility.** When replacing internal code, paths, workflows, or knowledge structures, migrate affected uses and remove superseded implementations. Do not add internal legacy shims, deprecated aliases, dual-write logic, or competing canonical documents. Assess *external* contracts separately and honor actual obligations. Move still-useful guidance into its owner and retain evidence needed for active claims. Documentation cleanup does not require historical provenance, archives or fixed-commit links.

7. **Fix the problem class.** For defects or inconsistencies, identify the underlying cause and check for related instances. Make the smallest coherent change that addresses the confirmed class; add proportionate checks or regression coverage where useful. Do not turn isolated issues into speculative redesigns.

8. **Think before acting.** Before substantive work, clarify the intended outcome, inspect relevant context, challenge important assumptions, and consider dependencies, risks, and the simplest sound approach. Scale planning to the task: small, reversible changes need no formal plan; consequential or hard-to-reverse changes deserve more analysis. Avoid analysis that does not improve the decision.

9. **Test the core first; validate by risk.** First verify the main outcome: for software, the changed behavior; for knowledge, whether a reader can use it to reason through a representative problem. Expand to affected dependencies, contracts, edge cases, or regressions when the likelihood and impact of failure justify it. Prefer focused checks over redundant tests or unrelated full suites; never omit essential verification merely to save time.
