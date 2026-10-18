# D2/C4 starter architecture — example only

This template is fictional. Replace its order-application systems, technology names, and decisions with evidence from your actual project before asking anyone to approve it.

- `model.d2`: canonical structural elements and relations.
- `views/context.d2`: C1 context projection of the model.
- `views/container.d2`: C2 container projection of the same model.
- `views/order-flow.d2`: illustrative dynamic scenario, not a new structural source of truth.
- `architecture-spec.md`: essential scope, requirements, constraints and unanswered questions.
- `diagrams/`: generated SVG previews.

The starter omits project-specific CI configuration so that it does not overwrite or conflict with an existing workflow. To render, run the helper supplied in the installed c4-architecture skill:

```sh
python3 <skill-root>/scripts/architecture.py format --root <target-dir>
python3 <skill-root>/scripts/architecture.py check --root <target-dir>
python3 <skill-root>/scripts/architecture.py render --root <target-dir>
```
