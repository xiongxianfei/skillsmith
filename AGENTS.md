# Skillsmith

Reusable AI prompt skills for writing, translation, and productivity. Each skill is a `SKILL.md` file with YAML frontmatter and a portable Markdown prompt.

`CONSTITUTION.md` is the highest-level project governance. Follow it before README, contribution docs, code, or chat history when rules conflict.

## Build & Validate

```
python tests/validate_skills.py
```

CI runs this on every push/PR to main. All errors must be fixed before merge.

## Operating Rules

- Inspect the current repo state before editing.
- Keep changes scoped; do not refactor unrelated files.
- Preserve user changes and never revert work you did not make unless explicitly asked.
- Update the owning artifact: prompt behavior in `skills/*/SKILL.md`, validation behavior in `tests/validate_skills.py`, install behavior in `install.sh`, project identity in `VISION.md`, durable governance in `CONSTITUTION.md`.
- Report validation commands, warnings, skipped checks, and unresolved questions before handoff.

## Skill File Format

Every skill lives at `skills/<skill-name>/SKILL.md`. Required structure:

```yaml
---
name: <lowercase-hyphenated>
description: >
  English only. Describe what the skill does and when it applies.
---
```

Body must contain:
- `$ARGUMENTS` placeholder (so slash command input flows through)
- `## Output Format` section (enforced by CI)

## Key Rules

- Descriptions MUST be English — skill bodies can be any language
- Descriptions should state the skill identity first, then the triggering situations, including indirect/casual user phrasing
- Do not add optional frontmatter such as `argument-hint`, `effort`, or `allowed-tools` unless an accepted proposal/spec requires it
- New or materially changed skills need eval evidence as defined in `specs/skill-quality-standard.md`
- High-risk skills need reviewer-visible safety notes and at least one safety or misuse eval case
- No emojis in Output Format headers

## Workflow

- All changes via PR to `main` (branch protection enabled)
- Branch naming: `feat/`, `fix/`, `docs/`, `improve/`
- Squash merge, delete branch after merge
- IMPORTANT: Always branch from latest `main` — never stack PRs from the same base to avoid README conflicts
- When adding a new skill, also add it to the README skills table
- Non-trivial behavior changes need written requirements before implementation; see `CONSTITUTION.md`.

## Project Structure

```
skills/*/SKILL.md          ← the skills (10 currently)
tests/validate_skills.py   ← CI validator (errors block merge, warnings don't)
install.sh                 ← one-command installer (supports --target flag)
CONSTITUTION.md            ← durable governance and workflow rules
VISION.md                  ← project identity and scope
```

## Common Mistakes

- Forgetting `$ARGUMENTS` in the body → CI error
- Missing `## Output Format` → CI error
- Non-English description → CI warning (CJK/Cyrillic detected)
- Descriptions that omit either the skill's function or the situations where it applies → unreliable skill selection

## Core Engineering Principles

1. **Self-contained knowledge.** Make each substantive document understandable on its own: explain the problem, essential terms, prerequisites, mechanisms, examples, and boundaries. Link to deeper material without requiring readers to follow links to understand the core argument. Keep canonical definitions in one place; avoid needless duplication.

2. **Reader-centered quality.** Evaluate whether a reader can explain *what happens, how, why, and when*; apply the knowledge to a realistic problem; predict likely outcomes and failure modes; and recognize opportunities to improve results. Correctness and clear reasoning matter more than polished prose.

3. **Goal-oriented work.** Identify the intended reader outcome before substantial work. Choose the smallest sufficient change; prioritize important knowledge gaps and useful results. Avoid speculative infrastructure, redundant research, unnecessary documentation, and rituals that do not advance the goal. Do not skip essential verification to save effort.

4. **Reuse before invention.** Look for established theory, standards, sources, methods, libraries, and tools before building alternatives. Prefer suitable, proven approaches; weigh fitness, reliability, cost, maintenance, and lock-in. Create custom solutions only when a material requirement justifies them.

5. **Mechanisms before memorization.** Explain causal relationships, relevant variables, assumptions, boundary conditions, and trade-offs. Show how the mechanism informs decisions and practical action. Surface possible improvements and testable hypotheses, clearly separating proposed innovations from demonstrated results.

6. **Delete obsolete internal compatibility.** When replacing internal code, paths, workflows, or knowledge structures, migrate affected uses and remove superseded implementations. Do not add internal legacy shims, deprecated aliases, dual-write logic, or competing canonical documents. Assess *external* contracts separately and honor actual obligations. Preserve unique evidence, provenance, and historically useful knowledge; remove obsolete representations, not valuable facts.

7. **Fix the problem class.** For defects or inconsistencies, identify the underlying cause and check for related instances. Make the smallest coherent change that addresses the confirmed class; add proportionate checks or regression coverage where useful. Do not turn isolated issues into speculative redesigns.

8. **Think before acting.** Before substantive work, clarify the intended outcome, inspect relevant context, challenge important assumptions, and consider dependencies, risks, and the simplest sound approach. Scale planning to the task: small, reversible changes need no formal plan; consequential or hard-to-reverse changes deserve more analysis. Avoid analysis that does not improve the decision.

9. **Test the core first; validate by risk.** First verify the main outcome: for software, the changed behavior; for knowledge, whether a reader can use it to reason through a representative problem. Expand to affected dependencies, contracts, edge cases, or regressions when the likelihood and impact of failure justify it. Prefer focused checks over redundant tests or unrelated full suites; never omit essential verification merely to save time.