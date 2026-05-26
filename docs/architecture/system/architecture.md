# Skillsmith System Architecture

## Status

approved

## Scope

This package records the architecture relevant to the `editor` skill expert-quality optimization. It creates the canonical architecture surface for this repository because no prior canonical package existed.

Related artifacts:

- Spec: `../../../specs/editor-expert-quality-optimization.md`
- Proposal: `../../../docs/proposals/2026-05-26-editor-expert-quality-optimization.md`
- Spec review: `../../../docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/spec-review-r4.md`
- Reference sketch: `../../../editor_language_role_separation_workflow.svg`

## 1. Introduction and Goals

Skillsmith is a portable Markdown skill library. The editor optimization keeps that boundary intact: behavior lives in `skills/editor/SKILL.md`, validation remains local and deterministic, and eval fixtures document expected behavior without adding runtime services.

Architecture goals for this change:

- Make the editor handling workflow explicit enough for implementation and eval design.
- Preserve pure-prompt execution: no tools, scripts, generated prompt assets, external services, or runtime adapters.
- Route instruction, source, and target language roles separately before editing.
- Default to Chinese and English final versions while honoring explicit target-language overrides.
- Use bilingual rendering as a fidelity cross-check where practical, even when the visible target is overridden to one language.

## 2. Architecture Constraints

- Skill files remain plain Markdown with YAML frontmatter.
- `editor` keeps `name: editor`, `$ARGUMENTS`, and `## Output Format`.
- The skill description stays English and trigger-forward.
- Output defaults to a Chinese and English pair for non-empty source input and honors explicit target-language requests.
- Source text is accepted in any detected language by default, without claiming equal editorial quality across every language.
- CI must not call live models or require network access.
- No high-risk skill behavior changes are in this slice.

## 3. System Scope and Context

System context: [system-context.mmd](diagrams/system-context.mmd)

Container view: [container-view.mmd](diagrams/container-view.mmd)

Workflow design: [editor-workflow.mmd](diagrams/editor-workflow.mmd)

The repository remains the system boundary. Contributors and agents update Markdown skills, specs, eval fixtures, and review evidence. AI assistant runtimes consume the portable skill prompt, but no runtime-specific adapter is introduced by this change.

## 4. Solution Strategy

The editor skill workflow is designed as a prompt-level pipeline:

1. Split the input into instruction, source, and target roles.
2. Use the instruction language for response framing when present; otherwise use source-language framing.
3. Edit the source in its own language before rendering target output.
4. Treat target output as default Chinese + English unless the user explicitly requests a different target language set.
5. Resolve meaning once and render the target languages from that resolved meaning.
6. Cross-check rendered versions against the edited source meaning and against each other when multiple renderings exist; where practical, render both Chinese and English internally to preserve the fidelity check even when visible output is overridden.
7. Emit the target-language output template, adding an edited source-language block only for non-Chinese/non-English source edit requests and notes only when explicitly requested.

The reference SVG provided by the user is used for the role-separation and cross-check structure. Its old display-gating branch is not carried forward; target handling is a default-with-override rule rather than a broad conditional report shape.

## 5. Building Block View

The architecture has four relevant building blocks:

- `skills/editor/SKILL.md`: owns the runtime prompt contract and the workflow instructions.
- `tests/evals/skills/editor/cases.yaml`: owns reviewer-visible eval scenarios for role separation, restraint, fidelity, mixed-language handling, code-switching, non-Chinese/non-English intake, and integrity boundaries.
- `specs/editor-expert-quality-optimization.md`: owns the normative behavior contract.
- `docs/changes/2026-05-26-editor-expert-quality-optimization/`: owns lifecycle review and evidence records.

No new executable component is introduced.

## 6. Runtime View

The runtime flow is prompt-only:

1. The user invokes `editor` with `$ARGUMENTS`.
2. The skill prompt interprets `$ARGUMENTS` as user instruction plus source artifact.
3. The prompt separates instruction, source, and target roles.
4. The source is edited in source language with fidelity and restraint.
5. Target-language versions are rendered from the same resolved meaning, defaulting to Chinese and English.
6. The prompt cross-checks rendered versions, any edited source-language text, and internal Chinese/English renderings where practical.
7. The assistant returns Markdown-compatible output using the required template.

Boundary and failure paths:

- Empty input may ask for text to edit.
- Misleading transformation requests return a response-language refusal plus accurate alternatives in the requested target languages.
- Ambiguity should be preserved or fixed in the output; explanatory notes are shown only when the user explicitly asks for notes.
- Non-Chinese/non-English source-language edits may include an edited source-language block only when the user asked for source-language editing.

## 7. Deployment View

Not applicable beyond repository file layout. The skill remains a Markdown prompt consumed by supported assistant runtimes through existing installation paths. No deployment, packaging, installer, or runtime adapter change is introduced.

## 8. Cross-cutting Concepts

- Fidelity: preserve meaning, facts, names, numbers, terms, logic, uncertainty, commitments, intent, tone, and formatting intent.
- Restraint: change only what improves the text; already-good text receives minimal changes.
- Role separation: instruction language governs framing; source language governs editing; target defaults to Chinese + English and honors explicit overrides.
- Bilingual verification: Chinese and English versions are rendered from one resolved meaning and checked against each other before output where practical, even when only one target language is displayed.
- Copyability: labels are concise, deliverables appear on their own lines or blocks, and output avoids emoji or decorative symbols.
- Privacy and security: examples and evals use fictional or sanitized text; the skill asks for no secrets or private files.

## 9. Architecture Decisions

No ADR is required. The change does not alter system boundaries, packaging, validation architecture, cache strategy, release architecture, or runtime adapters. The durable workflow decision is already captured in the approved spec and this architecture package.

## 10. Quality Requirements

| Quality | Mechanism |
|---|---|
| Portability | Plain Markdown skill with no tools or runtime dependencies. |
| Testability | Eval fixture scenarios and baseline/post-change evidence map to spec requirements. |
| Maintainability | Workflow is documented as a focused diagram and normative spec requirements. |
| Usability | Output templates prioritize copyable target-language deliverables, defaulting to Chinese and English. |
| Safety/integrity | Misleading edits are refused and redirected to accurate alternatives. |
| Performance | No new runtime components; prompt remains under the spec line-count limit unless an exception is accepted. |

## 11. Risks and Technical Debt

- The workflow requires the model to separate instruction and source roles under mixed-language input; weak models may still fuse them. Mitigation: evals include both mixed-language directions.
- Default bilingual output can feel verbose for trivial edits. Mitigation: explicit target-language override is honored, with no assessment, no default `Why`, and no duplicate source-language block.
- Single-target output weakens the visible cross-check. Mitigation: render both Chinese and English internally where practical before displaying only the requested target language.
- All-language intake can be misread as equal-quality multilingual editing. Mitigation: spec and architecture describe it as an intake rule, not a quality guarantee.

## 12. Glossary

- Instruction: the user's direction to the skill.
- Source: the artifact to edit, translate, or render.
- Target: the visible output language set; defaults to Chinese and English unless the user explicitly requests otherwise.
- Response framing: labels, notes, refusals, and explanations around deliverable text.
- Bilingual cross-check: verification that Chinese and English renderings preserve the same resolved source meaning, used where practical even when visible output is overridden.
