# Skillsmith project map

## Scope and ownership

This is an orientation map of the repository after simplifying design to C4. It describes existing realization and evidence limits; [the design index](../design/architecture/README.md) owns navigation to engineering definitions and [the workflow guide](workflows.md) owns contributor procedures.

| Area | Responsibility |
| --- | --- |
| `skills/*/SKILL.md` | Portable product prompts; the README table enumerates the catalog |
| `tests/validate_skills.py` | The single automated skill-format and metadata check |
| `install.sh` | Clone and copy product skills into the chosen destination |
| `.github/` | CI, issue intake and PR template |
| `VISION.md` | Canonical project purpose and scope |
| `AGENTS.md` | Concise agent guidance and shared engineering principles |
| `docs/workflows.md` | Contributor workflow, authoring examples and bug guidance |
| `design/architecture/` | C4 specifications, models, views and generated diagrams |
| `docs/skill-quality-standard.md` | Shared authoring, safety and review guidance |
| Ignored `.agents/skills/` | Locally installed maintainer skills |

## Product and maintenance flows

A user invokes an installed skill. The host assistant reads its Markdown prompt and supplies slash-command text through `$ARGUMENTS`; the prompt governs behavior and output. Product skills have no application server, background worker or database dependency.

The Bash installer uses Git to clone the catalog into a temporary directory, copies skill directories into `~/.claude/skills` or the `--target` destination, replaces existing corresponding directories and removes the temporary clone. It does not generate prompt behavior.

Maintainers use `c4-architecture` for design and Git/PR review for delivery. Architecture specifications keep behavior, constraints and decisions together. RigorLoop is no longer required; historical evidence is accessible through the architecture index’s fixed Git links. Private working notes remain outside the repository.

## Validation and CI

`python tests/validate_skills.py` uses PyYAML to check skill-file format and metadata. It is the only file under `tests/` and the only test command in `.github/workflows/validate.yml`. Errors fail validation; warnings require review.

README synchronization is checked manually. Previous unit tests and scenario files are preserved in Git history, not maintained as an active suite. Passing the validator does not demonstrate model behavior or safety; review the actual prompt and evidence behind any behavioral claims.

## External boundaries and limits

Product installation requires Bash, Git and GitHub access. Validation requires Python and PyYAML. Host assistants execute prompts according to their capabilities; no external API runtime is introduced by this migration. Architecture rendering additionally uses D2 through the package helper; no Node maintenance runtime is required.

Shared architecture is documented in [portable skills](../design/architecture/portable-skills.md); the [workflow guide](workflows.md) explains contribution and review. Catalog-specific design coverage is partial, as listed in the design index. Historical sources and review hashes retain their old meaning; they are not evidence of current release or hosted CI status.
