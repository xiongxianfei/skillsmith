---
name: c4-architecture
description: >-
  Designs, updates, and reviews software architecture with C4 views expressed in D2.
  Use for system context, container and component diagrams, architecture changes,
  runtime/deployment views, design reviews, or Git-maintained architecture documentation.
license: MIT
compatibility: Requires access to the whole skill directory. Python 3.9+ is needed for bundled helpers; D2 CLI 0.7+ is needed for actual diagram formatting, validation, and SVG rendering. Git is optional.
metadata:
  version: "1.0.0"
---

# C4 architecture with D2

Produce **reviewable software architecture**, not merely attractive diagrams. C4 describes levels of abstraction; D2 is the source format. A human must approve consequential decisions.

## Before editing

1. Identify the correct repository and read its contribution/architecture conventions. Existing project paths take precedence; in Skillsmith, architecture subjects live under `design/architecture/<subject>/`. In other repositories, `architecture/` may be appropriate. Never create a parallel design tree.
2. Read relevant requirements, source code, existing D2 sources, specifications, and decisions. Separate **implemented**, **proposed**, and **unknown** behavior; a diagram is not proof of implementation or approval.
3. For a new or changed C1/C2/C3 view, read [C4 conventions](references/c4-conventions.md). Identify the smallest set of views needed to answer the actual review or implementation questions.
4. If essential facts are missing, label assumptions and questions. Do not invent services, protocols, technologies, deployment details, quality targets, or approved decisions.

## Files and ownership

Use the project's established structure. Where a new package is needed, the bundled [starter template](assets/project-template/README.md) illustrates a D2 model, two structural views, a dynamic example, and a concise specification.

- `model.d2` owns stable element identifiers and shared structural relationships.
- `views/context.d2` shows C1 people, software systems, boundaries, and system-level relationships.
- `views/container.d2` shows C2 independently deployable/runnable applications, services, and data stores, plus their relationships.
- Optional component, dynamic/sequence, and deployment views address specific risks or scenarios. Dynamic views must agree semantically with the shared model even where D2 sequence syntax needs local participant aliases.
- `architecture-spec.md` owns scope, requirements, constraints, rationale, evidence, NFRs, and unresolved risks. Existing ADRs remain authoritative for accepted decisions.
- `diagrams/*.svg` are generated review artifacts, never manually edited source.

## Workflow

1. Identify the requested change, evidence, affected diagram levels, and decision points. Preserve unrelated files and existing stable IDs.
2. Update `model.d2` first for structural changes; update only affected views, specifications, and ADRs. Do not replace existing design intent with code-derived guesses.
3. Label directed relationships by purpose and known protocol. Avoid mixing internal components into a context view.
4. Before running a generator, verify its target. To create a new package without overwriting files:

   ```sh
   python3 <skill-root>/scripts/init_project.py --repo . --target architecture --dry-run
   python3 <skill-root>/scripts/init_project.py --repo . --target architecture
   ```

   Substitute `design/architecture/<subject>` for an existing project convention. The initializer only copies missing files; starter content is fictional and must be replaced before approval.
5. When D2 is available, format, check, and render the selected package:

   ```sh
   python3 <skill-root>/scripts/architecture.py format --root <architecture-dir>
   python3 <skill-root>/scripts/architecture.py check --root <architecture-dir>
   python3 <skill-root>/scripts/architecture.py render --root <architecture-dir>
   ```

   `check` runs D2 validation, formatting checks, and test renders; it does not establish architectural correctness. If D2 is missing, report that validation/rendering was **not run**.
6. Inspect rendered SVGs for legibility, boundaries, edge direction, labels, and missing/duplicated elements. Consult [review checklist](references/review-checklist.md) before review handoff.
7. Summarize changed sources and views, requirement traceability, assumptions, ADR impacts, risks, actual checks run, skipped checks, and decisions requiring human review.

## Safety and boundaries

- Prefer incremental edits with a comprehensible Git diff; never overwrite user files silently.
- Never expose secrets, personal data, private tokens, or detailed production endpoints without authorization.
- Do not claim architecture approval, a successful CLI run, or inspected visuals unless those events occurred.
- On disagreement between code, requirements, and accepted architecture, surface the conflict; do not silently choose a new source of truth.
- For architecture explanation only, use the conceptual guidance without creating files or requiring Python/D2.

## Output

Deliver the changed D2/specification files when file editing is requested, generated previews only when actually rendered, and a concise handoff showing **what changed, why, validation evidence, risks, and review decisions outstanding**.
