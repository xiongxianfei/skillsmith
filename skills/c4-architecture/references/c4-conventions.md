# C4 conventions for D2

Read this reference when creating or changing C4 structure. See https://c4model.com/diagrams and https://d2lang.com/tour/models/ for the underlying models.

## Abstraction and scope

| View | Show | Avoid |
| --- | --- | --- |
| C1 Context | People, the in-scope software system, external software systems, meaningful relations | Databases, classes, in-scope component internals |
| C2 Container | In-scope runnable apps/services, data stores, external dependencies and protocols | A container for every library or source file |
| C3 Component (selective) | Significant internal components of **one** container | Entire-codebase class maps |
| Dynamic | A specific scenario, ordered messages and meaningful failure paths | Pretending a message flow is a structural dependency model |
| Deployment | Software mapped to actual environments/instances/boundaries | Unconfirmed infrastructure details |

Always show the system boundary and use purposeful relationship labels (e.g. "Submits orders — HTTPS/JSON", not "Uses"). Identify technologies only when known. Include a short description for architecturally important elements.

## Shared D2 model

D2 0.7+ supports importing a model and selecting subsets with `suspend`/`unsuspend` globs. Keep stable identifiers and structural edges in `model.d2`. C1 and C2 should import this file rather than restating relationships. See `assets/project-template/model.d2` and its `views/` examples.

- Prefer simple stable IDs such as `order_platform.api`; preserve IDs on incremental edits.
- Distinguish person, software system, external system, container, data store, and optional component in names/descriptions or shape.
- Define a structural relationship once at the appropriate abstraction level. C1 can use system-level edges, C2 uses container-level edges; both can coexist in the model.
- A runtime sequence may restate participants/messages to preserve chronological order, but its actors and behavior must match the model and specification.
- Render only views that answer a concrete review question. C1 and C2 are a good default for most small applications.
- Keep diagram source in Git. Generated SVG is a preview, not a new source of truth.

## Review semantics

A successful D2 render checks syntax and layout, **not** requirements satisfaction, data protection, fault tolerance, performance, or correctness. Review critical failure scenarios and relevant quality constraints in prose or targeted diagrams. Record uncertainty rather than manufacturing a complete architecture from incomplete evidence.

## Updating a model

For an incoming request, compare the accepted specification with existing model and code. List elements/relationships that change, preserve unaffected IDs, update affected views, then check for inconsistencies across views, specs and ADRs. Report changes that require a new decision (for example a data-store choice or trust-boundary crossing).
