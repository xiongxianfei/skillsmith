# Contributing to Skillsmith

Use [OpenAI skill guidance](https://learn.chatgpt.com/docs/build-skills) and [Anthropic authoring guidance](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) for skill structure and authoring practices. Apply vendor-specific guidance to its intended host. [AGENTS.md](../AGENTS.md) covers repository conduct and ownership.

## 1. Define the change

Inspect the repository and affected skill first. For substantive behavior changes, describe the problem, intended outcome and representative input/expected-output examples in the issue or PR before implementation. For bugs, include the smallest reproduction. Distinguish observed behavior from untested expectations; small editorial changes need no formal design.

## 2. Edit

Start new branches from latest `main` using `feat/`, `fix/`, `docs/` or `improve/`; preserve unrelated work. Keep changes scoped and update the owning files and affected links.

Skills live at `skills/<skill-name>/SKILL.md`; the validator checks required files and Agent Skills metadata, including non-empty `name` and `description` and name/directory agreement. Update the README catalog when adding, removing or renaming skills.

Preserve safety boundaries and host compatibility obligations. Explain changes to tool permissions, dependencies and output contracts in the PR. Keep useful skill-specific designs under [architecture](../design/architecture/README.md#maintaining-a-design), using `c4-architecture` for design changes. Simple edits need no new design artifact.

## 3. Validate

Install PyYAML if needed, then run from the repository root:

```bash
python -m pip install pyyaml
python tests/validate_skills.py
```

CI runs the validator on pushes and PRs to `main`. It checks required files and metadata, not model quality, safety or host compatibility.

Run functional tests relevant to changed scripts. Existing suites can be run with:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python -m unittest discover -s skills/city-itinerary-builder/tests -p 'test_*.py' -v
python -m unittest discover -s skills/travel-planner/scripts -p 'test_*.py' -v
```

Check affected links and supporting resources. For validator changes, check representative valid and invalid inputs. For changed diagrams, follow the architecture guide's format, check, render and visual review steps. For prompt changes, assess representative requests; claim observed model behavior only when actual outputs support it. No fixed scenario count or live-model CI gate is required.

## 4. Review and deliver

All changes go through a PR to `main`. Describe the problem, resulting behavior, relevant safety or compatibility changes, and actual validation results. Report failures, warnings, skipped checks and unresolved questions. For breaking changes, explain migration; for bug fixes, explain the cause and verification.

Review depth should match risk. Successful checks do not establish human approval, and authors cannot claim independent approval. Commit, push, merge and release require applicable user authorization. Use squash merge and delete the branch after merging.

Use the **Bug Report** issue template for reproducible problems and **Skill Request** for new skills. Improve the affected skill or guidance directly; do not add parallel policy documents or archives for routine cleanup.
