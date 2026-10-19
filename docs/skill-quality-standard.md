# Skill quality standard

Skillsmith keeps one automated check: `python tests/validate_skills.py`. It checks required files and Agent Skills metadata. CI runs this command only; there is no required unit-test suite, eval-fixture gate, grandfathering baseline or separate README checker.

## Required checks

Every immediate directory under `skills/` must contain a readable `SKILL.md`. The validator checks:

- YAML frontmatter at the start of the file, enclosed by standalone `---` lines and parseable as a mapping.
- `name` and `description` values that are non-empty strings; whitespace-only values fail.
- `name` has 1–64 lowercase letters/numbers/hyphens, no leading/trailing or consecutive hyphens, and matches the skill directory.
- `description` is at most 1024 characters; optional `compatibility` is a non-empty string of at most 500 characters when present; optional `metadata` is a string-to-string map.

Missing files, malformed frontmatter or invalid required fields fail the command. An empty or unreadable skill catalog also fails. A minimal file with these two fields passes without a prescribed body structure. The validator does not enforce `$ARGUMENTS`, headings, language, line limits or output quality, and emits no style warnings.

Passing this check does not demonstrate host compatibility, model behavior, safety or learning effectiveness. Check compatibility with the intended host separately when relevant.

## Authoring and compatibility

Each skill should have one clear primary job and a useful outcome in a known context. State the skill's identity first in the description, then its direct and indirect triggering situations. Choose language appropriate to the intended users and host. Use explicit invocation guidance where useful. Put behavior in the Markdown body; metadata must not carry hidden behavioral guarantees.

Required frontmatter fields are `name` and `description`. Include optional fields only when useful and supported by the intended host; the validator checks `compatibility` and `metadata` shapes where present. Review changes affecting tool permissions explicitly; metadata alone does not authorize actions.

Keep Markdown readable and review input handling for the intended hosts and copy-paste use. `$ARGUMENTS` is optional when useful for a host's input substitution. Choose headings and output instructions to fit the skill; no `## Output Format` heading is required. Vendor-specific guidance should preserve portable use. Keep existing skill names, output contracts and installation paths stable; describe breaking changes and migration steps in the PR.

Prefer a small number of clear directives over accumulated branches. Use consistent terms between workflow and output instructions. Make outputs observable and copyable, and separate deliverables from commentary. Include a consistency check where meaning, intent, safety or format can silently drift. Honor deliberate tradeoffs rather than repeatedly polishing cosmetic wording.

Define observable behavior beyond a role or persona: what input to use, which steps matter, what to return, and how to handle uncertainty. Separate instructions, source material and output targets before acting. For example, a Chinese request to edit an English paragraph does not make Chinese the source language; also consider the inverse case when checking the design.

Treat output shape as part of the contract. Choose the smallest useful default that meets the skill's purpose, state when optional sections appear, and keep verification in the method even when the visible output is brief. A complete reference may need substantial output; concision must not silently remove promised content. Prefer explicit conditions when they capture the intended behavior, such as adding practice only when requested. When judgment is necessary, explain the relevant factors and give contrasting examples instead of leaving “when useful” undefined.

For complex skills, sketch the sequence of input handling, decisions, checks and output assembly before finalizing instructions. A focused workflow view can reveal missing branches or contradictory conditions; use the [architecture guide](../design/architecture/README.md#maintaining-a-design) when a maintained design is needed. Simple skills need no diagram.

Keep prompts concise. Move supporting detail into skill-local references when that improves usability; keep references shallow and make long references easy to navigate. There is no enforced line limit.

## Full-directory skill design

The **skill directory** is the portable unit. `SKILL.md` owns universal workflow instructions, triggers, invariants, safety boundaries, and concise output requirements. Additional resources are optional and justified by actual tasks:

- `references/` is for focused, specialized knowledge needed conditionally. In `SKILL.md`, name the exact file and the situation in which it must be read; avoid instructions such as “read references when useful.” Keep references shallow and prevent conflicting sources of truth.
- `scripts/` is for repeatable, deterministic work such as linting, format conversion, schema validation, and D2 rendering. Document dependencies and arguments, handle errors, avoid unrequested destructive operations, and never claim successful execution without evidence. Execution requires a host with the relevant capabilities and permissions.
- `assets/` is for static templates, output examples, diagrams and lookup tables; do not put essential behavioral rules only in assets. Custom directories such as `schemas/` or `evals/` are allowed.

Do not create these folders as scaffolding by default. Prefer a compact `SKILL.md` when the skill is simple. For longer tasks, load supplementary resources only as needed (progressive disclosure). Validate actual model behavior separately from syntax; use realistic cases and explicit limitations rather than claiming quality from metadata checks alone. The official format is [Agent Skills](https://agentskills.io/specification).

## Safety and privacy

Skills must not require secrets, credentials, private local paths or unpublished personal data. Use fictional or sanitized sensitive examples.

Medical, legal, financial, security and other high-stakes skills must state scope, refusal or escalation boundaries and must not present themselves as substitutes for licensed professionals, emergency services or official advice. Explain relevant safety limits in the PR. Reduced automated testing does not remove these prompt requirements.

Do not fabricate facts, user history, tool access, corpus verification, approvals or model results. Preserve source meaning and uncertainty where the skill transforms supplied material. Ordinary skill behavior remains readable Markdown, but full functionality may depend on bundled resources and explicitly documented local scripts executed by a capable host. No hidden external services are implied; the [shared architecture](../design/architecture/portable-skills.md) owns the boundary.

Where a transformation could be used deceptively, state the integrity boundary and an accurate alternative. A consistency check can catch accidental meaning drift but does not resolve a request to fabricate approval or remove a material qualification.

## Review and evidence

Reviewers check purpose, trigger intent, input/output contracts, safety, clarity and appropriate scope. Describe substantive behavior changes and their expected result in the PR; use a representative example when it makes the change assessable. Editorial corrections do not need an artificial scenario pack. No fixed scenario count, YAML fixture schema or mandatory model-run gate is required.

Choose examples that challenge the changed behavior: ordinary use, inverse inputs, missing information, indirect triggers, requests that should not activate the skill, and misuse where relevant. State observable expected results so reviewers can reason through the cases before and after the edit. These are design checks until actual outputs have been examined; they need not become a separate fixture suite.

When making an empirical quality or model-specific claim, provide actual evidence and its limitations. Expected examples are not observed model runs. Required-metadata validation must never be presented as proof of behavioral quality. Report what was checked and what remains unknown.

Maintain the README skill table manually when the catalog changes, and update usage or installation examples when affected. The [contributor guide](workflows.md) owns change preparation, validation, PR review and documentation maintenance.
