# Skill quality standard

Skillsmith keeps one automated check: `python tests/validate_skills.py`. It validates skill-file structure and metadata. CI runs this command only; there is no unit-test suite, eval-fixture requirement, grandfathering baseline or separate README checker.

## Automated format checks

Every immediate directory under `skills/` must contain `SKILL.md`. The validator checks:

- Parseable YAML frontmatter containing `name` and `description`.
- A name matching its directory, using lowercase letters, numbers and single hyphens, at most 64 characters; reserved names `anthropic` and `claude` are rejected.
- `$ARGUMENTS` in the body and a `## Output Format` section.
- Valid `effort` values when present: `low`, `medium`, `high`, `xhigh`, `max`.
- No non-empty `allowed-tools` declaration under the current portable-prompt contract.
- A maximum of 500 lines. More than 300 lines produces a warning.

CJK or Cyrillic characters in the description produce an English-metadata warning. This heuristic does not prove that a description is English or that its triggers are useful. Errors fail the command; warnings require review. Format validation does not demonstrate model behavior, safety or learning effectiveness.

## Authoring and compatibility

Each skill should have one clear primary job and a useful outcome in a known context. State the skill's identity first in an English description, then its direct and indirect triggering situations. Use explicit invocation guidance where useful. Put behavior in the Markdown body; metadata must not carry hidden behavioral guarantees.

Required frontmatter fields are `name` and `description`. Omit optional fields such as `argument-hint`, `effort` and `allowed-tools` unless an accepted design explains a concrete compatibility need. A design that changes tool permissions must also update the current validator deliberately; metadata alone grants no exception.

Preserve readable Markdown, Codex slash-command input, Claude Code compatibility and copy-paste use in other assistants. Vendor-specific guidance must not make the prompt unusable elsewhere. Keep skill names, output formats and installation paths stable; describe breaking changes and migration steps in the PR.

Prefer a small number of clear directives over accumulated branches. Use consistent terms between workflow and output instructions. Make outputs observable and copyable, separate deliverables from commentary, and avoid decorative Output Format headers. Include a consistency check where meaning, intent, safety or format can silently drift. Honor deliberate tradeoffs rather than repeatedly polishing cosmetic wording.

Keep prompts under 300 lines when practical. Move supporting detail into skill-local references instead of expanding the core prompt; keep references shallow and give long references a table of contents. An exception to the enforced 500-line limit needs an explicit policy and validator change.

## Safety and privacy

Skills must not require secrets, credentials, private local paths or unpublished personal data. Use fictional or sanitized sensitive examples.

Medical, legal, financial, security and other high-stakes skills must state scope, refusal or escalation boundaries and must not present themselves as substitutes for licensed professionals, emergency services or official advice. Explain relevant safety limits in the PR. Reduced automated testing does not remove these prompt requirements.

Do not fabricate facts, user history, tool access, corpus verification, approvals or model results. Preserve source meaning and uncertainty where the skill transforms supplied material. Ordinary skill execution remains a portable prompt; the [shared architecture](../design/architecture/portable-skills.md) owns runtime boundaries.

## Review and evidence

Reviewers check purpose, trigger intent, input/output contracts, safety, clarity and appropriate scope. Describe substantive behavior changes and their expected result in the PR; use a representative example when it makes the change assessable. Editorial corrections do not need an artificial scenario pack. No fixed scenario count, YAML fixture schema or mandatory model-run gate is required.

When making an empirical quality or model-specific claim, provide actual evidence and its limitations. Expected examples are not observed model runs. Format-check success must never be presented as proof of behavioral quality. Report what was checked and what remains unknown.

Maintain the README skill table, slash commands and enumerated installation examples manually when the catalog changes. The [contributor guide](workflows.md) owns change preparation, validation and PR review.

## Historical evidence

Earlier scenario declarations and test implementations remain in [Git history](https://github.com/xiongxianfei/skillsmith/tree/0abafec052bcdf9952f462fa0a872a207b5cb83c/tests). They preserve useful examples and provenance but do not impose the retired fixture or test-suite requirements. Current C4 specifications link relevant historical scenarios directly.
