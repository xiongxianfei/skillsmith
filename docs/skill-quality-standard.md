# Skill quality standard

Skillsmith keeps one automated check: `python tests/validate_skills.py`. It checks required files and metadata. CI runs this command only; there is no unit-test suite, eval-fixture requirement, grandfathering baseline or separate README checker.

## Required checks

Every immediate directory under `skills/` must contain a readable `SKILL.md`. The validator checks:

- YAML frontmatter at the start of the file, enclosed by standalone `---` lines and parseable as a mapping.
- `name` and `description` values that are non-empty strings; whitespace-only values fail.

Missing files, malformed frontmatter or invalid required fields fail the command. An empty or unreadable skill catalog also fails. A minimal file with these two fields passes without a prescribed body structure. The validator does not enforce `$ARGUMENTS`, headings, naming patterns, directory/name matching, language, line limits or optional metadata values, and emits no style warnings.

Passing this check does not demonstrate host compatibility, model behavior, safety or learning effectiveness. Check compatibility with the intended host separately when relevant.

## Authoring and compatibility

Each skill should have one clear primary job and a useful outcome in a known context. State the skill's identity first in the description, then its direct and indirect triggering situations. Choose language appropriate to the intended users and host. Use explicit invocation guidance where useful. Put behavior in the Markdown body; metadata must not carry hidden behavioral guarantees.

Required frontmatter fields are `name` and `description`. Include optional fields only when useful and supported by the intended host; their values are not checked here. Review changes affecting tool permissions explicitly; metadata alone does not authorize actions.

Keep Markdown readable and review input handling for the intended hosts and copy-paste use. `$ARGUMENTS` is optional when useful for a host's input substitution. Choose headings and output instructions to fit the skill; no `## Output Format` heading is required. Vendor-specific guidance should preserve portable use. Keep existing skill names, output contracts and installation paths stable; describe breaking changes and migration steps in the PR.

Prefer a small number of clear directives over accumulated branches. Use consistent terms between workflow and output instructions. Make outputs observable and copyable, and separate deliverables from commentary. Include a consistency check where meaning, intent, safety or format can silently drift. Honor deliberate tradeoffs rather than repeatedly polishing cosmetic wording.

Keep prompts concise. Move supporting detail into skill-local references when that improves usability; keep references shallow and make long references easy to navigate. There is no enforced line limit.

## Safety and privacy

Skills must not require secrets, credentials, private local paths or unpublished personal data. Use fictional or sanitized sensitive examples.

Medical, legal, financial, security and other high-stakes skills must state scope, refusal or escalation boundaries and must not present themselves as substitutes for licensed professionals, emergency services or official advice. Explain relevant safety limits in the PR. Reduced automated testing does not remove these prompt requirements.

Do not fabricate facts, user history, tool access, corpus verification, approvals or model results. Preserve source meaning and uncertainty where the skill transforms supplied material. Ordinary skill execution remains a portable prompt; the [shared architecture](../design/architecture/portable-skills.md) owns runtime boundaries.

## Review and evidence

Reviewers check purpose, trigger intent, input/output contracts, safety, clarity and appropriate scope. Describe substantive behavior changes and their expected result in the PR; use a representative example when it makes the change assessable. Editorial corrections do not need an artificial scenario pack. No fixed scenario count, YAML fixture schema or mandatory model-run gate is required.

When making an empirical quality or model-specific claim, provide actual evidence and its limitations. Expected examples are not observed model runs. Required-metadata validation must never be presented as proof of behavioral quality. Report what was checked and what remains unknown.

Maintain the README skill table, slash commands and enumerated installation examples manually when the catalog changes. The [contributor guide](workflows.md) owns change preparation, validation and PR review.

## Historical evidence

Earlier scenario declarations and test implementations remain in [Git history](https://github.com/xiongxianfei/skillsmith/tree/0abafec052bcdf9952f462fa0a872a207b5cb83c/tests). They preserve useful examples and provenance but do not impose the retired fixture or test-suite requirements. Current C4 specifications link relevant historical scenarios directly.
