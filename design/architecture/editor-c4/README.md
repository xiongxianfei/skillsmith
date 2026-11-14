# Editor: C4 design from the implementation

Start with the [architecture specification](architecture-spec.md) for exact request decisions, language policy, edit/lesson behavior, trust boundaries and unresolved design questions. This is an implementation projection prepared for human review, not a claim of complete requirements alignment or executed model quality.

The editor is a passive Markdown package. Its one C2 container is a file store; the assistant host executes externally. Editing, translation and teaching are logical policies within the host.

## Context

![Editor C1 context: people, passive prompt package and external assistant host](diagrams/context.svg)

## Container

![Editor C2: authored prompt file store and external host](diagrams/container.svg)

## Editing and learning

![Scenario: formal English update with grounded lesson and requested exercise](diagrams/edit-and-learn.svg)

## Boundary scenarios

- [Misleading translation request with no notes](diagrams/integrity-no-notes.svg)
- [Transcript editing without audio evidence](diagrams/transcript-boundary.svg)

## Sources and reproduction

[model.d2](model.d2) owns diagram entities and structural relationships. C1/C2 views import and filter the model. Dynamic views reuse its participants for ordered interactions. Generated SVGs are previews and are never edited manually. The [shared architecture](../portable-skills.md) defines common responsibility boundaries.

Use Python 3.9+ and D2 0.7.0+ on PATH (rendered with D2 0.9.0 and ELK). From the repository root:

```bash
python3 design/architecture/editor-c4/scripts/architecture.py format
python3 design/architecture/editor-c4/scripts/architecture.py check
python3 design/architecture/editor-c4/scripts/architecture.py render
python tests/validate_skills.py
```

The helper checks required views, model imports, syntax, formatting and rendering. Semantic fidelity and layout require inspection; passing checks does not establish architecture approval. D2 is not a product or CI dependency.
