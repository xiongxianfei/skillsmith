# Skillsmith project map

## Scope and ownership

This is an orientation map of the repository after simplifying design to C4. It describes existing realization and evidence limits; [the design index](../design/architecture/README.md) owns navigation to engineering definitions and [the workflow guide](workflows.md) owns contributor procedures.

| Area | Responsibility |
| --- | --- |
| `skills/*/SKILL.md` | Portable product prompts; the README table enumerates the catalog |
| `tests/validate_skills.py` | Structural/policy validation and static eval-fixture checks |
| `tests/test_*.py` | Automated validator and synchronization regression checks |
| `tests/evals/skills/` | Static expected-behavior scenarios and explicit grandfathering |
| `tests/check_readme_sync.py` | README catalog, command and installation synchronization |
| `install.sh` | Clone and copy product skills into the chosen destination |
| `.github/` | CI, issue intake and PR template |
| `CONSTITUTION.md`, `VISION.md` | Governance and product identity |
| `AGENTS.md` | Concise agent guidance and shared engineering principles |
| `docs/workflows.md` | Contributor workflow, authoring examples, eval fixtures and bug guidance |
| `design/architecture/` | C4 specifications, models, views and generated diagrams |
| `docs/skill-quality-standard.md` | Shared authoring, safety and evaluation obligations |
| `docs/plans/` | Stable delivery plans |
| `docs/changes/` | New records remain local and ignored; pre-existing tracked history is preserved |
| Ignored `.agents/skills/` | Locally installed maintainer skills |

## Product and maintenance flows

A user invokes an installed skill. The host assistant reads its Markdown prompt and supplies slash-command text through `$ARGUMENTS`; the prompt governs behavior and output. Product skills have no application server, background worker or database dependency.

The Bash installer uses Git to clone the catalog into a temporary directory, copies skill directories into `~/.claude/skills` or the `--target` destination, replaces existing corresponding directories and removes the temporary clone. It does not generate prompt behavior.

Maintainers use `c4-architecture` for design and Git/PR review for delivery. Architecture specifications keep behavior, constraints and decisions together. RigorLoop is no longer required; existing ignored local state and tracked historical evidence are retained.

## Validation and CI

`python tests/validate_skills.py` parses YAML with PyYAML, checks prompt structure and policy, and validates static eval fixtures. Errors fail validation; warnings are reported separately. `python -m unittest discover tests` runs regression tests, and `python tests/check_readme_sync.py` checks README synchronization. CI uses the repository workflow under `.github/workflows/validate.yml`; inspect it for the exact commands and environment.

Static eval fixtures express expected behavior; they do not demonstrate model execution. Nine grandfathered skills currently lack fixtures, a reported nonblocking warning. Material changes remove that exemption according to the quality standard. High-risk changes require safety evidence and appropriate model smoke evidence under the written standard.

## External boundaries and limits

Product installation requires Bash, Git and GitHub access. Validation requires Python and PyYAML. Host assistants execute prompts according to their capabilities; no external API runtime is introduced by this migration. Architecture rendering additionally uses D2 through the package helper; no Node maintenance runtime is required.

Shared architecture is documented in [portable skills](../design/architecture/portable-skills.md); the [workflow guide](workflows.md) explains contribution and review. Catalog-specific design coverage is partial, as listed in the design index. Historical sources and review hashes retain their old meaning; they are not evidence of current release or hosted CI status.
