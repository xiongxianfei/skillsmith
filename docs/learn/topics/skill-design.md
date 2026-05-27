# Skill Design Lessons

Curated lessons for designing portable prompt skills. These lessons are guidance, not policy; authoritative behavior still belongs in accepted proposals, specs, architecture docs, plans, skill files, and review records.

## 2026-05-26: Design Skills As Behavior Contracts

- Source session: `docs/learn/sessions/2026-05-26-editor-skill-design.md`
- Primary classification: `durable-lesson`
- Secondary routes: none
- Lesson: A good skill should define observable behavior, not rely on persona alone. Use a concise identity, concrete non-negotiables, ordered workflow, output contract, and eval examples so the model has an executable shape to follow.

## 2026-05-26: Separate Input Roles Before Acting

- Source session: `docs/learn/sessions/2026-05-26-editor-skill-design.md`
- Primary classification: `durable-lesson`
- Secondary routes: none
- Lesson: When a user message can contain instructions, source material, and output-target requests, split those roles before acting. This prevents the skill from confusing what the user is asking with the artifact being edited or rendered.

## 2026-05-26: Treat Output Shape As Part Of The Skill

- Source session: `docs/learn/sessions/2026-05-26-editor-skill-design.md`
- Primary classification: `durable-lesson`
- Secondary routes: none
- Lesson: Output format is behavior. Define the smallest useful default response, state when optional sections appear, and avoid duplicated deliverables. This keeps a skill from drifting into report generation when the user asked for a usable result.

## 2026-05-26: Use Examples As Design Pressure Tests

- Source session: `docs/learn/sessions/2026-05-26-editor-skill-design.md`
- Primary classification: `durable-lesson`
- Secondary routes: possible future eval-design topic
- Lesson: Examples and eval fixtures should test the design before and after prompt edits. Include normal cases, inverse cases, edge cases, indirect triggers, and misuse cases so the prompt is tested against the places it is most likely to break.

## 2026-05-26: Keep Verification In The Method

- Source session: `docs/learn/sessions/2026-05-26-editor-skill-design.md`
- Primary classification: `durable-lesson`
- Secondary routes: none
- Lesson: A skill can use internal verification steps even when the visible output is compact. Keep cross-checks, meaning resolution, or consistency checks in the method, then display only what the request needs.

## 2026-05-26: Prefer Crisp Conditions

- Source session: `docs/learn/sessions/2026-05-26-editor-skill-design.md`
- Primary classification: `durable-lesson`
- Secondary routes: none
- Lesson: Conditions based on explicit user requests or detected source properties are easier to specify, review, and test than soft judgment branches. Prefer "only when asked" over vague triggers such as "when useful" unless the softer judgment is essential and testable.

## 2026-05-26: Name Integrity Boundaries

- Source session: `docs/learn/sessions/2026-05-26-editor-skill-design.md`
- Primary classification: `durable-lesson`
- Secondary routes: none
- Lesson: If a skill could be asked to transform content deceptively, make the refusal boundary explicit. Ordinary fidelity checks catch accidental drift; they do not reliably catch user-requested deception.

## 2026-05-26: Keep Prompt Skills Portable And Scoped

- Source session: `docs/learn/sessions/2026-05-26-editor-skill-design.md`
- Primary classification: `durable-lesson`
- Secondary routes: none
- Lesson: Keep behavior in the Markdown skill unless accepted requirements prove infrastructure is needed. Avoid adding tools, runtime dependencies, live-model CI, validator changes, or unrelated skill edits as part of a focused prompt optimization.

## 2026-05-26: Use Workflow Design To Clarify Complex Skills

- Source session: `docs/learn/sessions/2026-05-26-editor-skill-design.md`
- Primary classification: `durable-lesson`
- Secondary routes: possible future architecture-design topic
- Lesson: For skills with ordered roles, gates, cross-checks, and output assembly, draw the workflow before finalizing prose. A focused workflow diagram can make the skill easier to understand, expose stale branches, and map the design to implementation and eval coverage.
