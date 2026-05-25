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
  English only, under 250 chars. Must be "pushy" — include explicit
  "Use this skill whenever..." phrasing to prevent undertriggering.
argument-hint: <English, describes expected user input>
allowed-tools: ""
# Optional Claude Code tuning only; not required for portable behavior:
# effort: <low|medium|high|xhigh|max>
---
```

Body must contain:
- `$ARGUMENTS` placeholder (so slash command input flows through)
- `## Output Format` section (enforced by CI)

## Key Rules

- Descriptions MUST be English — skill bodies can be any language
- Descriptions should be trigger-phrase-forward and "pushy" per Anthropic's official guidance: tell Codex when to auto-invoke, including indirect/casual user phrasing
- `effort` is optional; if present, use an accepted value such as `low`, `medium`, `high`, `xhigh`, or `max`
- `allowed-tools: ""` for all skills (pure prompt, no tool use)
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
- Non-English description or argument-hint → CI warning (CJK/Cyrillic detected)
- Using passive descriptions ("Triggers when...") instead of pushy ("Use this skill whenever...") → skill won't auto-invoke reliably
