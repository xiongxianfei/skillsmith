# Editor Skill Optimization

## Status

approved, amended by post-PR user direction on 2026-05-25

## Related proposal

- `docs/proposals/2026-05-25-editor-skill-optimization.md`
- Proposal review R2: `docs/changes/2026-05-25-editor-skill-optimization/reviews/proposal-review-r2.md`
- User amendment: require a three-stage editor workflow: optimize with reasons, review language quality, then translate optimized text into Chinese and English.

## Goal and context

The `editor` skill should provide a high-quality editing and translation workflow. The current accepted contract is no longer a narrow-output default; it is a deliberate three-stage workflow:

1. optimize the input according to writing best practices and provide optimization reasons;
2. review source-language quality before translation;
3. translate the optimized text into Chinese and English.

The change remains material because it alters the skill workflow and output contract. It still requires eval evidence, baseline evidence, post-change evidence, and deterministic repository validation.

## Glossary

- Editor skill: `skills/editor/SKILL.md`.
- Source text: the text supplied by the user through `$ARGUMENTS`.
- Optimized text: the edited source text after clarity, grammar, concision, structure, tone, terminology, and flow improvements.
- Optimization reasons: concise explanation of substantive editing choices.
- Language-quality assessment: assessment of whether the optimized text is clear, natural, grammatically sound, context-appropriate, and ready for translation.
- Chinese and English translations: bilingual output generated from the optimized text.
- Integrity boundary: a request to make text misleading, false, deceptive, or materially different from the known source meaning.
- Baseline evidence: reviewer-visible notes showing current behavior before the prompt is changed.
- Post-change evidence: reviewer-visible notes showing behavior after the prompt is changed.

## Examples first

Example E1: simple proofreading returns the full three-stage workflow
Given the user asks `Fix this and make it clearer`
When the source text contains grammar and clarity issues
Then the optimized skill returns optimized text, optimization reasons, language-quality assessment, and Chinese and English translations.

Example E2: indirect engineer-facing edit uses the same workflow
Given the user asks `Can you make it sound better?` for a rough PR description
When the text describes a technical change
Then the optimized skill improves the PR description, explains key changes, assesses source quality, and provides Chinese and English translations.

Example E3: translation-oriented request still starts with optimization
Given the user asks to optimize and translate release-note text
When the source text is technical English
Then the optimized skill improves the source sentence, assesses readiness, and provides aligned Chinese and English versions.

Example E4: misleading rewrite is refused with accurate wording
Given the user asks the skill to make a customer statement sound approved when the source only says the customer will review it later
When the requested rewrite would falsify the customer's position
Then the optimized skill briefly refuses the misleading transformation, offers accurate optimized wording, and only translates accurate wording.

## Requirements

R1. The optimized `editor` skill MUST keep `name: editor`.

R2. The optimized `editor` skill MUST remain a pure prompt skill without runtime-specific tool frontmatter.

R3. The optimized `editor` skill MUST keep `$ARGUMENTS` as the source text and editing instruction input surface.

R4. The optimized `editor` skill MUST include a `## Output Format` section.

R5. The optimized `editor` skill MUST run a three-stage workflow for normal editing and translation requests: optimize, assess language quality, and translate into Chinese and English.

R6. The optimization stage MUST improve clarity, grammar, concision, structure, tone, terminology, and flow while preserving source meaning, facts, technical details, audience, tone, and requested format.

R7. The optimization stage MUST provide concise reasons for substantive optimization choices.

R8. The language-quality stage MUST assess clarity, grammar, tone, terminology, ambiguity, fidelity, and readiness for translation.

R9. The language-quality stage MUST happen before the translation stage.

R10. The translation stage MUST translate the optimized text into Chinese and English.

R11. If the optimized text is already Chinese or English, the skill MUST still provide that language version and the other-language translation.

R12. The skill MUST keep Chinese and English translations aligned in technical meaning, tone, and formatting.

R13. The skill MUST support proofreading, polishing, rewriting, technical or engineer-facing editing, translation-oriented requests, ambiguous pasted text, and integrity-boundary handling.

R14. When the user provides explicit tone, audience, format, or style instructions, the skill MUST follow them unless they conflict with meaning preservation or an integrity boundary.

R15. When the user provides ambiguous pasted text with no explicit instruction, the skill SHOULD run the full three-stage workflow on that text.

R16. The skill MUST refuse or redirect requests that would make text misleading, false, deceptive, or materially inconsistent with known source meaning.

R17. For integrity-boundary requests, the skill MUST briefly explain the boundary and SHOULD offer accurate optimized wording.

R18. The skill MUST NOT translate or polish wording that falsifies approvals, consent, claims, authorship, or material facts.

R19. The optimized `SKILL.md` SHOULD remain concise and MUST remain under 500 lines unless an accepted exception explains why progressive disclosure is not suitable.

R20. The change MUST keep `tests/evals/skills/editor/cases.yaml`.

R21. The eval fixture MUST include scenarios covering normal proofreading, indirect engineer-facing editing, integrity-boundary misuse, and bilingual technical translation.

R22. Each eval scenario MUST contain a concrete prompt and observable expected behavior.

R23. Baseline evidence MUST be recorded before editing `skills/editor/SKILL.md`.

R24. Post-change evidence MUST compare the optimized behavior against the same scenario classes used for baseline evidence.

R25. The implementation MUST NOT add live model calls to CI.

R26. The implementation MUST NOT change repository-wide validator behavior unless implementation proves that the existing eval-fixture path cannot represent this material skill change.

R27. The implementation MUST NOT optimize `doctor`, `oscp-coach`, or any other skill in this slice.

## Inputs and outputs

Inputs:

- User text and instructions passed through `$ARGUMENTS`.
- `skills/editor/SKILL.md`.
- `tests/evals/skills/editor/cases.yaml`.
- Baseline and post-change evidence recorded in the change evidence area.

Default output format:

| Section | Default content |
|---|---|
| `### 1. Optimized Text` | Optimized source text |
| `### 2. Optimization Reasons` | Concise bullets explaining substantive changes |
| `### 3. Language Quality Assessment` | Brief quality and translation-readiness assessment |
| `### 4. Chinese Translation` | Chinese version of the optimized text |
| `### 5. English Translation` | English version of the optimized text |

Outputs MUST be Markdown-compatible plain text. No tool output, generated files, or external service results are part of the skill runtime contract.

## State and invariants

- `editor` remains an existing grandfathered skill, but this material change removes its eval-fixture exemption for this PR.
- The skill remains portable Markdown and must not rely on runtime-specific frontmatter.
- The skill remains broadly useful for editing and translation rather than becoming engineer-only.
- Eval fixtures are reviewer evidence and do not require live model execution in CI.

## Error and boundary behavior

- Empty or missing source text SHOULD produce a brief request for the text to edit or translate.
- If the source text contains terms with multiple plausible technical meanings, the skill SHOULD flag the ambiguity in the language-quality assessment.
- If the user asks for a misleading rewrite, the skill MUST not perform the deceptive transformation even if the requested tone is otherwise clear.
- If the user asks for a format that conflicts with concise output, the explicit user format wins unless it conflicts with meaning preservation or integrity boundaries.

## Compatibility and migration

- Existing install behavior and slash-command naming MUST remain unchanged.
- README skill tables, install instructions, and command lists do not need updates unless implementation changes user-visible skill metadata that README mirrors.
- The skill omits runtime-specific frontmatter such as `effort` and `allowed-tools`; no migration is required for those removed metadata fields.
- Rollback is limited to reverting `skills/editor/SKILL.md`, `tests/evals/skills/editor/cases.yaml`, and related change evidence.
- No migration is required for other skills.

## Observability

- `tests/evals/skills/editor/cases.yaml` MUST make expected behavior observable to reviewers.
- Baseline evidence MUST identify how the current skill behaves before prompt edits.
- Post-change evidence MUST identify how the optimized skill behaves after prompt edits.
- Validation output from `python tests/validate_skills.py` MUST show that the repository remains valid.
- Final implementation evidence MUST report the line count for `skills/editor/SKILL.md`.

## Security and privacy

- Eval prompts MUST use fictional or sanitized content.
- Eval prompts MUST NOT contain secrets, credentials, private local paths, unpublished personal data, or real customer-sensitive details.
- The optimized skill MUST not ask users for secrets or private local files.
- Integrity-boundary behavior MUST prevent the skill from helping falsify approvals, consent, claims, authorship, or material facts.

## Accessibility and UX

No interactive UI is introduced.

The optimized output SHOULD be easy to scan and reuse, with stable numbered sections and concise reasons/assessment text.

## Performance expectations

- The skill prompt SHOULD remain concise enough for ordinary assistant context use.
- Static validation and eval-fixture checks MUST remain deterministic.
- CI MUST NOT require network access or live model calls for this change.

## Edge cases

EC1. User says only `fix this` with flawed English text. The skill runs the full three-stage workflow.

EC2. User asks to make a PR description sound better. The skill optimizes it for engineering review and then provides the assessment and Chinese/English translations.

EC3. User asks to optimize and translate technical release-note content. The skill provides optimized text, reasons, assessment, Chinese translation, and English translation.

EC4. User pastes text with no instruction. The skill runs the full three-stage workflow in a best-effort manner.

EC5. User asks for a diff or explanation. The skill may make optimization reasons more specific while preserving the required output sections.

EC6. Source text has a non-obvious ambiguity. The skill identifies the ambiguity in the language-quality assessment before translation.

EC7. User asks to make a statement imply approval that did not happen. The skill refuses that misleading transformation and offers accurate wording.

EC8. The optimized `SKILL.md` approaches the hard line limit. Implementation evidence must record line count and justify any progressive-disclosure decision.

## Non-goals

- Do not optimize every existing skill in this slice.
- Do not optimize high-risk skills such as `doctor` or `oscp-coach`.
- Do not introduce live model CI.
- Do not add tools, scripts, runtime dependencies, or generated prompt assets.
- Do not rename `editor`.
- Do not convert `editor` into an engineer-only skill.
- Do not change repository-wide validator behavior unless needed to support this material skill change.

## Acceptance criteria

AC1. `specs/editor-skill-optimization.md` exists and defines the optimized `editor` output contract.

AC2. `tests/evals/skills/editor/cases.yaml` exists and includes scenarios for proofreading, indirect PR-description editing, integrity-boundary misuse, and bilingual technical translation.

AC3. Baseline evidence is recorded before `skills/editor/SKILL.md` is edited.

AC4. Post-change evidence compares optimized behavior against the baseline scenario classes.

AC5. Normal editing and translation requests use the full three-stage workflow.

AC6. Optimization reasons are included by default.

AC7. Language-quality assessment is included before translation.

AC8. Chinese and English translations are included by default.

AC9. Integrity-boundary requests are refused or redirected with accurate wording.

AC10. `skills/editor/SKILL.md` remains pure prompt with `$ARGUMENTS` and `## Output Format`, and without runtime-specific frontmatter.

AC11. No other skill prompt is optimized in this slice.

AC12. `python tests/validate_skills.py` passes.

AC13. `python -m unittest discover tests` passes.

AC14. `git diff --check` passes.

AC15. `python tests/check_readme_sync.py` is run if the helper exists in the branch.

## Open questions

None.

## Readiness

Ready for implementation/review only when the plan, test spec, evidence, and skill prompt all reflect the amended three-stage workflow.
