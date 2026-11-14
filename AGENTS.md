# Skillsmith

A collection of AI skills. Each skill lives in `skills/<skill-name>/` with a required `SKILL.md` and optional supporting resources.

## Guidance and ownership

Use [OpenAI skill guidance](https://learn.chatgpt.com/docs/build-skills) and [Anthropic authoring guidance](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) for authoring. Apply host-specific guidance to the intended host.

- `README.md`: project description, skill catalog and usage.
- `skills/*/SKILL.md`: skill behavior; supporting resources belong in the skill directory.
- `tests/validate_skills.py`: required-file and metadata validation.
- [Architecture](design/README.md): skill mechanisms, constraints and design decisions; follow the design guide when changing designs.

## Working rules

- Inspect repository state first, preserve user changes, and keep edits scoped.
- Update the owning artifact and repair affected references. Record explicit policy changes there; implementation and historical reviews do not silently override accepted decisions.
- Before substantive behavior changes, write the intended outcome and acceptance examples in the issue or PR. Small editorial changes need no formal design.
- Preserve safety boundaries and actual compatibility obligations. High-risk skills must retain explicit scope and refusal or escalation boundaries; describe safety changes in the PR.
- Never invent facts, tool access, tests, model results, approvals or release status. Authors cannot claim independent approval of their own work.
- Keep secrets and private data out of skills and examples; use sanitized or fictional sensitive examples.
- Report validation commands, results, skipped checks and unresolved questions. Metadata checks do not demonstrate model quality or host compatibility.

## Engineering principles

- Keep essential meaning understandable and canonical knowledge in one place. Add context that helps decisions; load supporting resources only when needed.
- Prioritize useful reader outcomes and causal explanations over polish or memorization. State assumptions, mechanisms, boundaries and trade-offs.
- Choose the smallest sufficient change. Reuse established tools and guidance before inventing alternatives.
- Fix confirmed problem classes without speculative redesign. Remove obsolete internal implementations and migrate their uses while honoring external contracts.
- Think before acting, scale planning to risk, and clarify before irreversible or high-risk decisions.
- Test the core outcome first, then affected contracts and regressions as risk warrants. Do not skip essential verification.

## Validation and delivery

```bash
python tests/validate_skills.py
```

CI runs this required-file and metadata check on pushes and PRs to `main`; errors block merging. Install PyYAML if needed (`python -m pip install pyyaml`). Run focused functional tests for affected scripts; check representative valid and invalid inputs when changing the validator, and check affected links.

Start new branches from latest `main`, using `feat/`, `fix/`, `docs/` or `improve/`. All changes go through a PR to `main`; squash merge and delete the branch after merging. Update the README catalog when adding, removing or renaming skills.

Describe the problem, expected behavior, safety or compatibility changes, and actual validation results in the PR. Include reproduction and cause for bug fixes, and migration guidance for breaking changes. Commit, push, merge and release require applicable user authorization. Use the Bug Report and Skill Request issue templates as appropriate.

Existing functional suites:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
python -m unittest discover -s skills/city-itinerary-builder/tests -p 'test_*.py' -v
python -m unittest discover -s skills/travel-planner/scripts -p 'test_*.py' -v
```
