# Strategic Positioning

## Project category

Reusable AI prompt-skill library.

## Primary user

Engineers, multilingual workers, learners, and self-directed professionals who already use AI assistants and want repeatable workflows.

## Primary pain

Ad hoc prompting is hard to reuse, hard to review, and inconsistent across tools.

## Primary promise

Skillsmith turns recurring AI-assisted work into portable, inspectable skill files that improve the user's writing, communication, learning, and everyday productivity.

## Core mechanism

Each skill is a Markdown prompt with structured metadata, a pushy invocation description, a `$ARGUMENTS` placeholder, and a required output format. Validation keeps the catalog consistent enough for review.

## Alternatives

Loose prompt libraries, private system prompts, one-off chat examples, vendor-specific assistant configurations, and full agent platforms.

## Tradeoff

The project chooses a smaller catalog of durable, reviewable skills over a broad collection of clever but loosely specified prompts.

## Compatibility surfaces

Codex slash commands, Claude Code skills, copy-paste use in other AI tools, Markdown, YAML frontmatter, GitHub pull requests, local validation, and installer scripts.

These surfaces help adoption but are not the project identity.

## Refusals

The project will not become a general chatbot, agent platform, private knowledge base, vendor-specific prompt package, or unreviewed prompt dump.

It will not treat high-stakes skills as replacements for professional judgment.

## Falsifiability

The vision is wrong if users cannot infer when to invoke a skill from its description, if validated skills still produce inconsistent outputs, if review cannot keep up with catalog growth, or if the prompts stop being portable and understandable outside a single runtime.
