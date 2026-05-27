# Learn Session: Editor Skill Design

## Frame

- Trigger: explicit maintainer `$learn` request after multiple proposal, spec, architecture, implementation, review, and verification rounds for `2026-05-26-editor-expert-quality-optimization`.
- Trigger type: maintainer request and workflow retrospective.
- Scope: reusable lessons about designing a good portable prompt skill, using the optimized `editor` skill as the evidence base.
- Evidence in scope:
  - `docs/changes/2026-05-26-editor-expert-quality-optimization/explain-change.md`
  - `docs/changes/2026-05-26-editor-expert-quality-optimization/review-resolution.md`
  - `specs/editor-expert-quality-optimization.md`
  - `specs/editor-expert-quality-optimization.test.md`
  - `skills/editor/SKILL.md`
  - `tests/evals/skills/editor/cases.yaml`
  - `docs/changes/2026-05-26-editor-expert-quality-optimization/post-change-evidence.md`
  - `docs/architecture/system/architecture.md`
  - `docs/architecture/system/diagrams/editor-workflow.mmd`
  - `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/architecture-review-r2.md`
- Explicit exclusions: no PR readiness claim, no hosted CI claim, no new workflow policy, no changes to the `editor` skill, and no topic-file update without contributor confirmation.
- Prior learnings reviewed:
  - `docs/learn/sessions/2026-05-25-spec-review-next-stage-routing.md`
- Session record path: `docs/learn/sessions/2026-05-26-editor-skill-design.md`

## Observe

O1. A good skill needs a concrete behavior contract, not just a stronger persona.

Evidence:

- `explain-change.md` records that persona-only prompting was rejected as too weak, and the selected direction was expert persona plus concrete guardrails and evals.
- `specs/editor-expert-quality-optimization.md` defines expert editing through requirements for fidelity, restraint, professional polish, terminology care, integrity, minimality, and verification.
- `skills/editor/SKILL.md` encodes the behavior as an expert editing standard, non-negotiables, workflow steps, and output templates instead of relying only on "act as an expert."

O2. Role separation is a core skill-design move when user input contains multiple jobs.

Evidence:

- `specs/editor-expert-quality-optimization.md` defines instruction, source, target, response language, and target language set as separate concepts.
- `skills/editor/SKILL.md` starts the workflow by separating instruction, source, and target before editing.
- `tests/evals/skills/editor/cases.yaml` includes both `editor-expert-chinese-instruction-english-source` and `editor-expert-english-instruction-chinese-source`, showing that mixed-language behavior was tested in both directions after proposal review found the inverse case missing.

O3. Output shape is part of skill behavior and should be intentionally small.

Evidence:

- `specs/editor-expert-quality-optimization.md` replaced the old fixed three-stage report with concise target-language output, no default assessment, no default `Why`, notes only when explicitly requested, and no duplicate source-language block for Chinese or English source edits.
- `skills/editor/SKILL.md` implements those output rules directly under `## Output Format`.
- `post-change-evidence.md` records that removing default assessment, default `Why`, and default notes was part of addressing the baseline report-generator gap.

O4. Good examples and eval fixtures pressure-test the design before and after prompt edits.

Evidence:

- `explain-change.md` records the plan sequencing as M1 eval fixture and baseline evidence before prompt edits, M2 prompt and README implementation, then M3 post-change evidence.
- `specs/editor-expert-quality-optimization.test.md` maps requirements to test cases T1-T16 and explicitly covers role separation, output size, notes gating, target override, non-Chinese/non-English source behavior, and integrity refusal.
- `tests/evals/skills/editor/cases.yaml` contains 13 scenarios that encode normal, edge, indirect-trigger, and misuse cases instead of only happy-path examples.

O5. Verification should be part of the method, while visible output should remain proportional to the request.

Evidence:

- `specs/editor-expert-quality-optimization.md` requires resolving source meaning once, rendering requested target-language versions from that meaning, and cross-checking visible versions; for single-target requests it recommends internal Chinese and English rendering where practical.
- `skills/editor/SKILL.md` keeps that verification step in the workflow while honoring explicit target-language-only requests in visible output.
- `post-change-evidence.md` records the same distinction: default bilingual output, explicit target override, and internal cross-checking where practical.

O6. Crisp conditions are more reliable than soft judgment branches in a portable skill.

Evidence:

- The design moved notes from "when needed" to "only when explicitly asked," and `skills/editor/SKILL.md` now uses that crisp condition.
- `specs/editor-expert-quality-optimization.test.md` includes T11 for notes-only-when-asked and ambiguity-without-notes, proving the condition is testable.
- `review-resolution.md` records a later template-composition finding where note-bearing and integrity-boundary templates needed explicit target-language repetition, showing that even output-template edge cases need concrete wording.

O7. Integrity boundaries deserve explicit prompt treatment because verification alone does not catch requested deception.

Evidence:

- `specs/editor-expert-quality-optimization.md` requires refusing misleading, false, deceptive, unsupported, or falsely attributed transformations and offering accurate target-language alternatives.
- `skills/editor/SKILL.md` checks integrity before editing and includes an integrity-boundary output template.
- `tests/evals/skills/editor/cases.yaml` includes `editor-expert-integrity-boundary` as a misuse scenario, not merely a normal editing case.

O8. Good skill changes stay portable and scoped unless evidence proves infrastructure must change.

Evidence:

- `explain-change.md` says the change was intentionally prompt-only, with no runtime tools, generated prompt assets, live-model CI, installer behavior, or repository-wide validator changes.
- `specs/editor-expert-quality-optimization.md` requires no live model calls in CI, no repository-wide validator changes unless forced, and no unrelated skill optimization.
- `skills/editor/SKILL.md` remains a portable Markdown prompt with `$ARGUMENTS` and `## Output Format`.

O9. Workflow design can make a prompt skill clearer by externalizing the handling sequence before it becomes prose.

Evidence:

- The maintainer explicitly observed that the workflow design made the editor skill clearer, easier to understand, and materially helped the editor skill design.
- `docs/architecture/system/architecture.md` names "make the editor handling workflow explicit enough for implementation and eval design" as an architecture goal.
- `docs/architecture/system/diagrams/editor-workflow.mmd` lays out the role split, response-language resolution, integrity gate, source-language edit, meaning resolution, target rendering, cross-check loop, and final assembly in one reviewable flow.
- `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/architecture-review-r2.md` approved the workflow as aligned with the R4 spec and noted that runtime flow covers role separation, source-language editing, target rendering, cross-check drift repair, source-language block conditions, and integrity refusals.

## Classify

| Observation | Proposed classification | Final classification | Secondary routes | Confirmed by | Rationale |
|---|---|---|---|---|---|
| O1 | durable-lesson | durable-lesson | `docs/learn/topics/skill-design.md` | maintainer request: "Please write a topic in accordance with best practices." | The evidence shows a reusable pattern across proposal, spec, implementation, and review, and topic routing was confirmed. |
| O2 | durable-lesson | durable-lesson | `docs/learn/topics/skill-design.md` | maintainer request: "Please write a topic in accordance with best practices." | Role separation was central to the editor design and review fixes, and the maintainer confirmed topic publication. |
| O3 | durable-lesson | durable-lesson | `docs/learn/topics/skill-design.md` | maintainer request: "Please write a topic in accordance with best practices." | Output minimality was repeatedly specified and validated, and the maintainer confirmed topic publication. |
| O4 | durable-lesson | durable-lesson | `docs/learn/topics/skill-design.md`; possible future eval-design topic | maintainer request: "Please write a topic in accordance with best practices." | The eval-first pattern is supported by the plan and evidence, and the maintainer confirmed topic publication. |
| O5 | durable-lesson | durable-lesson | `docs/learn/topics/skill-design.md` | maintainer request: "Please write a topic in accordance with best practices." | The method/display distinction is reusable for prompt skills, and the maintainer confirmed topic publication. |
| O6 | durable-lesson | durable-lesson | `docs/learn/topics/skill-design.md` | maintainer request: "Please write a topic in accordance with best practices." | The move from soft to crisp conditions is supported by spec, tests, and review, and the maintainer confirmed topic publication. |
| O7 | durable-lesson | durable-lesson | `docs/learn/topics/skill-design.md` | maintainer request: "Please write a topic in accordance with best practices." | Integrity-boundary handling is reusable for editing skills, and the maintainer confirmed topic publication. |
| O8 | durable-lesson | durable-lesson | `docs/learn/topics/skill-design.md` | maintainer request: "Please write a topic in accordance with best practices." | Prompt-only scoping is supported by the accepted artifacts, and the maintainer confirmed topic publication. |
| O9 | durable-lesson | durable-lesson | `docs/learn/topics/skill-design.md`; possible future architecture-design topic | maintainer request: "Please write a topic in accordance with best practices." | The workflow diagram improved clarity and mapped the skill contract to implementation and eval design, and the maintainer confirmed topic publication. |

## Route

- Added curated topic entries to `docs/learn/topics/skill-design.md`.
- Contributor confirmation for final durable-lesson classification was supplied by the maintainer request to write the topic.
- No authoritative artifact, ADR, proposal, spec, workflow, skill, or active plan was updated.

## Promoted Skill-Design Lessons

These were promoted to `docs/learn/topics/skill-design.md` after contributor confirmation:

- Define the skill as observable behavior, not as persona alone.
- Separate input roles before acting when the user message may contain instructions, source material, and output-target requests.
- Treat output shape as part of the contract; default to the smallest useful response.
- Use examples and eval fixtures as design pressure tests, including inverse and misuse cases.
- Keep verification in the method even when visible output is smaller than the internal reasoning path.
- Prefer crisp, request-driven conditions over soft model-judgment branches.
- Name integrity boundaries explicitly when the user may request a misleading transformation.
- Keep prompt skills portable and scoped unless accepted requirements prove infrastructure changes are needed.
- Use workflow design as a skill-design tool when behavior has ordered roles, gates, cross-checks, and output assembly; the diagram can make the prompt easier to reason about before it becomes final prose.

## Follow-ups

- Topic promotion completed in `docs/learn/topics/skill-design.md`.
- No follow-up issue, ADR, proposal, or skill edit was created from this learn session.

## Validation

- `git diff --check` passed.
- `python tests/validate_skills.py` passed with the existing non-blocking grandfathered-evals warning for unrelated skills: `communicator`, `doctor`, `email-drafter`, `fitness-coach`, `journaling`, `language-tutor`, `nvc`, `oscp-coach`, `study-planner`.
