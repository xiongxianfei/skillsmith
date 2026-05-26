# Spec Review R3: Editor Expert Quality Optimization

## Result

- Skill: spec-review
- Review status: changes-requested
- Material findings: `F-SPEC-EDITOR-EXPERT-003`
- Recording status: recorded
- Recording blocker: none
- Review record: `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/spec-review-r3.md`
- Review log: `docs/changes/2026-05-26-editor-expert-quality-optimization/review-log.md`
- Review resolution: `docs/changes/2026-05-26-editor-expert-quality-optimization/review-resolution.md`
- Open blockers: `F-SPEC-EDITOR-EXPERT-003`
- Immediate next stage: spec revision

## Findings

## Finding F-SPEC-EDITOR-EXPERT-003

- Finding ID: F-SPEC-EDITOR-EXPERT-003
- Severity: major
- Location: `specs/editor-expert-quality-optimization.md`, requirements `R33` and `R37`; `Inputs and outputs` templates; acceptance criteria `AC11`, `AC12`, and `AC16`
- Evidence: `R33` requires explicit target-language requests, including target-language-only requests, to be honored unless they conflict with integrity or meaning preservation. `R37` requires integrity-boundary alternatives in the requested target languages. But the required note-bearing template, non-Chinese/non-English source-edit template, and integrity-boundary template still hardcode Chinese and English output. `AC11` says explicit single-target output displays only the requested target language, while `AC12` and `AC16` still point to templates that would display Chinese and English. This leaves cases such as "English only, explain" or an English-only integrity refusal underspecified or contradictory.
- Required outcome: The spec must define target-language-aware output templates for note-bearing output, non-Chinese/non-English source-edit output, and integrity-boundary output so explicit target-language overrides compose cleanly with notes, source edits, and refusals.
- Safe resolution path: Replace the hardcoded Chinese/English note-bearing and integrity templates with target-language templates, while stating that the default target-language set is Chinese + English. For non-Chinese/non-English source edits, keep the edited source-language block first, then repeat the target-language label/content pattern for each visible target language. Update `AC12` and `AC16` so they reference target-language-aware templates rather than fixed Chinese/English templates.
- needs-decision rationale: none

## Review Dimensions

| Review dimension | Verdict |
| --- | --- |
| requirement clarity | concern |
| normative language | pass |
| completeness | concern |
| testability | concern |
| examples | pass |
| compatibility | pass |
| observability | pass |
| security/privacy | pass |
| non-goals | pass |
| acceptance criteria | concern |

## Review Notes

The spec is directionally aligned with the approved R5 proposal: Chinese + English is the default target set, explicit target-language overrides are honored, notes are explicit-request only, and integrity remains an explicit gate. The remaining issue is template composition. Downstream tests and implementation need one unambiguous output contract for combinations of explicit target override plus notes, source-language edit blocks, or integrity refusal.

## Eventual test-spec readiness

conditionally-ready

The spec has stable requirement IDs, examples, edge cases, and acceptance criteria, but test-spec authoring should wait until `F-SPEC-EDITOR-EXPERT-003` is resolved because output-template tests would otherwise require guessing.

## Stop condition

Resolve `F-SPEC-EDITOR-EXPERT-003` and run renewed spec review before architecture-review, planning, or test-spec authoring.
