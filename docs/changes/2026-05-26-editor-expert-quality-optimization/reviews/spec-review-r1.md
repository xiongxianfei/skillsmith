# Spec Review R1: Editor Expert Quality Optimization

## Result

- Skill: spec-review
- Review status: changes-requested
- Material findings: `F-SPEC-EDITOR-EXPERT-001`, `F-SPEC-EDITOR-EXPERT-002`
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/spec-review-r1.md`
- Review log: `docs/changes/2026-05-26-editor-expert-quality-optimization/review-log.md`
- Review resolution: `docs/changes/2026-05-26-editor-expert-quality-optimization/review-resolution.md`
- Open blockers: two material spec findings
- Immediate next stage: isolated stop; revise spec or disposition findings

## Findings

## Finding F-SPEC-EDITOR-EXPERT-001

- Finding ID: F-SPEC-EDITOR-EXPERT-001
- Severity: major
- Location: `specs/editor-expert-quality-optimization.md`, R9-R12, Inputs and outputs, Error and boundary behavior
- Evidence: The spec requires detecting the source language before composing the response and using that language for response framing. It defines source language as the detected primary language of the source text, but `$ARGUMENTS` contains both instructions and source text. Common prompts can mix languages, such as Chinese instruction plus English source (`帮我润色: The rollout is complete`) or English instruction plus Chinese source (`Polish this: 这个 PR...`). The spec does not say whether response framing follows the instruction language, the source-text language, or a precedence rule when they differ.
- Required outcome: The spec must define a deterministic response-framing rule for mixed-language instructions and source text.
- Safe resolution path: Add requirements and edge cases that distinguish instruction language from source-text language. A safe default is: when the user's instruction language is clearly Chinese or English, response framing follows the instruction language; otherwise response framing follows the source-text language. Russian framing can remain bounded as already described. Add examples for Chinese instruction with English source and English instruction with Chinese source.
- needs-decision rationale: none

## Finding F-SPEC-EDITOR-EXPERT-002

- Finding ID: F-SPEC-EDITOR-EXPERT-002
- Severity: major
- Location: `specs/editor-expert-quality-optimization.md`, R13-R19, R34-R36, Inputs and outputs
- Evidence: The spec removes the previous fixed three-stage report and says output should include Chinese and English final versions, avoid duplicate source-language sections, and keep labels concise. However, it does not define a concrete default output shape for simple edits or note-bearing responses. Implementation could choose many incompatible formats, such as one unlabeled bilingual block, `中文`/`English` labels, source-language localized labels, or headings plus bullets. Tests would need to infer unstated label and section expectations.
- Required outcome: The spec must define a concrete observable default output shape while preserving the proposal's de-duplication and source-language-aware framing rules.
- Safe resolution path: Add an `Output format contract` subsection under Inputs and outputs with explicit default templates. For simple edits, define two labeled blocks: Chinese final version and English final version, with labels localized to the response framing language where required. For note-bearing responses, define the order: brief source-language note or refusal first when needed, then Chinese and English final versions. Specify that labels are concise, content appears on its own line, no assessment/why section appears by default, and no duplicate optimized-text section appears for Chinese or English source edits.
- needs-decision rationale: none

## Review Dimensions

| Review dimension | Verdict | Notes |
|---|---|---|
| requirement clarity | concern | Core expert-quality and bilingual-output requirements are clear, but mixed-language framing and output shape need clarification. |
| normative language | pass | Requirements use stable IDs and mostly testable MUST/SHOULD language. |
| completeness | concern | Normal, boundary, migration, and rollback behavior are covered; mixed-language input and concrete output shape are incomplete. |
| testability | concern | Most requirements are testable, but output-format tests would require guessing exact structure. |
| examples | concern | Good examples exist, but mixed instruction/source language examples are missing. |
| compatibility | pass | Supersession, breaking output-format change, migration guidance, and rollback are covered. |
| observability | pass | Eval fixtures, baseline evidence, post-change evidence, validation, model smoke, and line count are specified. |
| security/privacy | pass | Sanitized eval prompts, no secrets, no private files, and integrity boundaries are covered. |
| non-goals | pass | Scope exclusions are clear. |
| acceptance criteria | concern | Acceptance criteria need additions for mixed-language framing and concrete output-shape behavior after the spec is revised. |

## Eventual test-spec readiness

conditionally-ready

The proposed scenario classes are strong enough for test-spec once the two output-contract clarifications are made. Without those edits, test-spec authors would need to invent mixed-language precedence and output template expectations.

## Stop condition

Do not proceed to architecture, plan, or test-spec until `F-SPEC-EDITOR-EXPERT-001` and `F-SPEC-EDITOR-EXPERT-002` are resolved or explicitly dispositioned.
