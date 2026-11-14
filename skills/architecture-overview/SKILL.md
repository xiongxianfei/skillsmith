---
name: architecture-overview
description: Explain or propose the architecture of software, AI skills and other structured projects through a Mermaid graph and matching responsibility tables. Use to map contexts, components, responsibilities and relationships in an architecture overview. Formal C4 views and D2 packages belong to c4-architecture.
---

# Architecture overview

Make the project's meaningful responsibilities and relationships understandable. Describe existing implementation from evidence or propose a design from requirements; distinguish implemented, instructed, proposed and unknown behavior. A skill instruction is evidence of intended behavior, not demonstrated model compliance.

## Find the structure

- Inspect the intended outcome, requirements, available implementation and existing architecture decisions. Read repository conventions first. Preserve accepted decisions; surface conflicts with code or requirements rather than silently overriding them.
- Identify the smallest useful set of contexts from coherent language, models and rules. A folder, workflow step or diagram box does not establish a bounded context. Use one candidate context when that is all the evidence supports, and label uncertain boundaries instead of inventing more contexts.
- Group components into meaningful numbered responsibilities. Explain whether the groups are capability groups, execution stages or technical layers; do not imply deployment tiers or execution order without evidence. Do not force four layers or generic intake/workflow/output boxes.
- Identify relationships that explain how the outcome is achieved. Separate supporting files and resources from core responsibilities, and place external capabilities outside the context boundary. Mark optional capabilities and continuations explicitly. Do not invent services, protocols, tools or integrations.

## Output contract

Default to a page titled `<Subject> — Architecture Overview`, with these three parts in order:

1. **One Mermaid architecture graph.** Use context boundaries containing numbered responsibility groups and short component names, arranged in compact rows where useful. Prefer containment for grouping; draw only meaningful relationships. Use `and` instead of `&` in labels. State arrow semantics once (for example, information flows from producer to consumer, or a component points to one it uses) and keep direction and concise relationship labels consistent. Distinguish optional relationships; invisible layout links carry no architectural meaning.
2. **One layer table:** `# | Layer | Responsibility | Components`. Add `Context` when multiple contexts require disambiguation. The Layer column names the chosen responsibility groups; explain their kind rather than implying every group is a technical layer.
3. **One contexts–components table:** `Context | Component | Layer | Responsibility`. Include one row per core component with its matching numbered group. Keep supporting resources and conditional external capabilities outside this mapping and describe them briefly alongside it.

Use exactly matching names and numbering across graph and tables. Explain responsibilities and their contribution, not just labels. Allow brief assumptions, boundaries, rationale and source links; keep operational rules and schemas in their owning artifacts.

Choose structure from the subject. Purchase guidance can have a primary decision framework and optional candidate comparison within one shared decision model. A local CSV inventory project can group import and validation, reorder calculation, and export without inventing network services. Sparse requirements justify a proposed structure and explicit unknowns, not claims that components already exist.

## Ownership and delivery

Update the owning architecture artifact and affected references when editing existing documentation. Preserve existing files and unrelated changes; do not create a competing design tree. For new documentation, follow the project's location convention; if absent, use `design/<subject>/README.md`. Honor chat-only requests without saving files.

Architecture work does not itself authorize changes to product or skill behavior. Distinguish explanations from requested implementation and record consequential policy changes in the owning artifact. Formal C4/D2 requests belong to the existing `c4-architecture` capability when available; do not label this overview as a formal C4 model or generate a D2 package by default.

## Review

Check that the graph and both tables cover the same core components and groups, context boundaries follow shared rules, arrows match their stated meaning, and resources and external capabilities are visibly distinct. Check source links and implementation-status claims against inspected evidence.

Render generated diagrams when suitable tooling is available and inspect labels, boundaries, connections and legibility. If rendering is unavailable, report that it was skipped. Report actual validation separately from architectural judgments; a valid diagram is not proof of behavioral correctness, host compatibility or independent approval.
