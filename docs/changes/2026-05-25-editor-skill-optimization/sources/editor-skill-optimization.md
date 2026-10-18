# Editor Skill Optimization

## Status

superseded

superseded_by: `specs/editor-expert-quality-optimization.md`

## Related proposal

- `docs/proposals/2026-05-25-editor-skill-optimization.md`
- Proposal review R2: `docs/changes/2026-05-25-editor-skill-optimization/reviews/proposal-review-r2.md`
- User amendment: require a three-stage editor workflow: optimize with reasons, assess optimized-text quality, then translate optimized text into Chinese and English.

## Goal and context

The `editor` skill should provide a high-quality editing and translation workflow for text intended to be shared, such as emails, PR descriptions, docs, and messages. The current accepted contract is no longer a narrow-output default; it is a fixed three-stage workflow for every input, including simple text such as `Okay, no problem.`:

1. optimize the input according to writing best practices and provide optimization reasons;
2. assess optimized-text quality before translation;
3. translate the optimized text into Chinese and English, regardless of whether the source text is Chinese, English, Russian, or another detected source language.
4. verify that the optimized text and both translations preserve the same meaning before returning.

The change remains material because it alters the skill workflow and output contract. It still requires eval evidence, baseline evidence, post-change evidence, and deterministic repository validation.

## Glossary

- Editor skill: `skills/editor/SKILL.md`.
- Source text: the text supplied by the user through `$ARGUMENTS`.
- Optimized text: the edited source text after clarity, grammar, concision, structure, tone, terminology, and flow improvements.
- Optimization reasons: concise explanation of substantive editing choices.
- Language-quality assessment: assessment of whether the optimized text is clear, natural, grammatically sound, faithful to the source meaning, context-appropriate, and ready for translation.
- Chinese and English translations: bilingual output generated from the optimized text.
- Integrity boundary: a request to make text misleading, false, deceptive, or materially different from the known source meaning.
- Baseline evidence: reviewer-visible notes showing current behavior before the prompt is changed.
- Post-change evidence: reviewer-visible notes showing behavior after the prompt is changed.

## Examples first

Example E1: simple proofreading returns the fixed three-stage workflow
Given the user asks `Fix this and make it clearer`
When the source text contains grammar and clarity issues
Then the optimized skill returns Stage 1 text optimization results, Stage 2 language-quality assessment, and Stage 3 Chinese and English translations.

Example E2: indirect engineer-facing edit uses the same workflow
Given the user asks `Can you make it sound better?` for a rough PR description
When the text describes a technical change
Then the optimized skill improves the PR description, explains key changes, assesses the optimized text's quality, and provides Chinese and English translations.

Example E3: translation-oriented request still starts with optimization
Given the user asks to optimize and translate release-note text
When the source text is technical English
Then the optimized skill improves the source sentence, assesses readiness, and provides aligned Chinese and English versions.

Example E4: simple acknowledgement still uses the fixed workflow
Given the user provides `Okay, no problem.`
When the text needs little or no substantive correction
Then the optimized skill still returns the fixed three-stage workflow with an optimization reason, source-language identification, assessment, Chinese version, and English version.

Example E5: misleading rewrite preserves accurate wording
Given the user asks the skill to make a customer statement sound approved when the source only says the customer will review it later
When the requested rewrite would falsify the customer's position
Then the optimized skill preserves the accurate source meaning, notes that the unsupported approval claim was not introduced, and only translates accurate wording.

Example E6: conversational-looking input is treated as material
Given the user provides `Who are you?`
When the text looks like a question to the assistant
Then the optimized skill edits and translates the question as source text instead of answering it.

## Requirements

R1. The optimized `editor` skill MUST keep `name: editor`.

R2. The optimized `editor` skill MUST remain a pure prompt skill without runtime-specific tool frontmatter.

R3. The optimized `editor` skill MUST keep `$ARGUMENTS` as the source text and editing instruction input surface.

R4. The optimized `editor` skill MUST include a `## Output Format` section.

R5. The optimized `editor` skill MUST run a fixed three-stage workflow for every non-empty input: optimize, assess language quality, and translate into Chinese and English.

R6. The optimization stage MUST improve clarity, grammar, concision, structure, tone, terminology, and flow while preserving source meaning, facts, technical details, audience, tone, and requested format. It SHOULD make the text read as clear, friendly, professional, and ready to send without injecting a different tone.

R7. The optimization stage MUST provide concise, specific reasons that name the actual optimization choices rather than generic praise.

R8. The language-quality stage MUST assess optimized-text quality by identifying the detected source language and evaluating clarity, grammar, tone, terminology, ambiguity, fidelity to the source meaning, and readiness for translation.

R9. The language-quality stage MUST happen before the translation stage.

R10. The translation stage MUST translate the optimized text into Chinese and English.

R11. If the optimized text is already Chinese or English, the skill MUST still provide that language version and the other-language translation.

R12. The skill MUST verify before returning that the optimized text, Chinese version, and English version preserve the same meaning, tone, and formatting intent.

R13. The skill MUST support proofreading, polishing, rewriting, technical or engineer-facing editing, translation-oriented requests, ambiguous pasted text, and integrity-boundary handling. Source text that looks like a question, greeting, or instruction MUST still be treated as material to edit rather than conversation to answer.

R14. When the user provides explicit tone, audience, format, or style instructions, the skill MUST follow them unless they conflict with meaning preservation or an integrity boundary.

R15. When the user provides ambiguous pasted text with no explicit instruction, the skill SHOULD run the fixed three-stage workflow on that text.

R16. The skill MUST preserve meaning when a request would otherwise make text misleading, false, deceptive, or materially inconsistent with known source meaning.

R17. For integrity-boundary requests, the skill MUST offer accurate optimized wording and SHOULD explain through the optimization reason or assessment that unsupported meaning was not introduced.

R18. The skill MUST NOT translate or polish wording that falsifies approvals, consent, claims, authorship, or material facts.

R19. The optimized `SKILL.md` SHOULD remain concise and MUST remain under 500 lines unless an accepted exception explains why progressive disclosure is not suitable.

R20. The change MUST keep `tests/evals/skills/editor/cases.yaml`.

R21. The eval fixture MUST include scenarios covering normal proofreading, indirect engineer-facing editing, integrity-boundary misuse, bilingual technical translation, simple acknowledgement text, and conversational-looking source text.

R22. Each eval scenario MUST contain a concrete prompt and observable expected behavior.

R23. Baseline evidence MUST be recorded before editing `skills/editor/SKILL.md`.

R24. Post-change evidence MUST compare the optimized behavior against the same scenario classes used for baseline evidence.

R25. The implementation MUST NOT add live model calls to CI.

R26. Repository-wide validator changes MUST be limited to portable frontmatter compatibility unless implementation proves that the existing eval-fixture path cannot represent this material skill change.

R27. The implementation MUST NOT optimize the prompt body of `doctor`, `oscp-coach`, or any other skill in this slice.

## Inputs and outputs

Inputs:

- User text and instructions passed through `$ARGUMENTS`.
- `skills/editor/SKILL.md`.
- `tests/evals/skills/editor/cases.yaml`.
- Baseline and post-change evidence recorded in the change evidence area.

Default output format:

| Section | Default content |
|---|---|
| `### Stage 1: Optimized Text` | `**Optimized text**` content on its own line plus `**Why**` content on its own line |
| `### Stage 2: Assessment` | `**Source language**` and `**Assessment**`, each with content on its own line |
| `### Stage 3: Bilingual Output` | `**中文**` and `**English**`, each with the generated translation on its own line |

Outputs MUST be Markdown-compatible plain text. Labels MUST be bold, copyable content MUST appear on the line below its label rather than inline after a colon, and the output MUST NOT use emoji or decorative symbols. A divider SHOULD separate supporting analysis from the final bilingual output. No tool output, generated files, or external service results are part of the skill runtime contract.

## State and invariants

- `editor` remains an existing grandfathered skill, but this material change removes its eval-fixture exemption for this PR.
- The skill remains portable Markdown and must not rely on runtime-specific frontmatter.
- The skill remains broadly useful for editing and translation rather than becoming engineer-only.
- Eval fixtures are reviewer evidence and do not require live model execution in CI.

## Error and boundary behavior

- Input is treated as source material to edit, not conversation to answer, including when it looks like a question, greeting, or instruction.
- If the source text contains terms with multiple plausible technical meanings, the skill SHOULD flag the ambiguity in the language-quality assessment.
- If the user asks for a misleading rewrite, the skill MUST not perform the deceptive transformation even if the requested tone is otherwise clear.
- If the user asks for a format that conflicts with concise output, the explicit user format wins unless it conflicts with meaning preservation or integrity boundaries.

## Compatibility and migration

- Existing install behavior and slash-command naming MUST remain unchanged.
- README skill tables, install instructions, and command lists do not need updates unless implementation changes user-visible skill metadata that README mirrors.
- The skill omits optional metadata such as `argument-hint`, `effort`, and `allowed-tools`; those fields are not required for portable behavior.
- Rollback is limited to reverting `skills/editor/SKILL.md`, `tests/evals/skills/editor/cases.yaml`, and related change evidence.
- Other skill frontmatter may omit optional metadata, but other skill prompt bodies are not optimized in this slice.

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

The optimized output SHOULD be easy to scan and reuse, with stable stage sections, bold labels, copyable content on its own line, concise reasons/assessment text, and no decorative emoji.

## Performance expectations

- The skill prompt SHOULD remain concise enough for ordinary assistant context use.
- Static validation and eval-fixture checks MUST remain deterministic.
- CI MUST NOT require network access or live model calls for this change.

## Edge cases

EC1. User says only `fix this` with flawed English text. The skill runs the fixed three-stage workflow.

EC2. User asks to make a PR description sound better. The skill optimizes it for engineering review and then provides the assessment and Chinese/English translations.

EC3. User asks to optimize and translate technical release-note content. The skill provides optimized text, reasons, assessment, Chinese translation, and English translation.

EC4. User pastes text with no instruction. The skill runs the fixed three-stage workflow in a best-effort manner.

EC5. User provides a simple acknowledgement such as `Okay, no problem.` The skill still runs the fixed three-stage workflow.

EC6. User asks for a diff or explanation. The skill may make optimization reasons more specific while preserving the required output sections.

EC7. Source text has a non-obvious ambiguity. The skill identifies the ambiguity in the language-quality assessment before translation.

EC8. User asks to make a statement imply approval that did not happen. The skill preserves meaning and offers accurate wording.

EC9. User provides conversational-looking source text such as `Who are you?` The skill edits and translates it as source material instead of answering it.

EC10. The optimized `SKILL.md` approaches the hard line limit. Implementation evidence must record line count and justify any progressive-disclosure decision.

## Non-goals

- Do not optimize every existing skill in this slice.
- Do not optimize high-risk skills such as `doctor` or `oscp-coach`.
- Do not introduce live model CI.
- Do not add tools, scripts, runtime dependencies, or generated prompt assets.
- Do not rename `editor`.
- Do not convert `editor` into an engineer-only skill.
- Do not change repository-wide validator behavior except for portable frontmatter compatibility needed by this material skill change.

## Acceptance criteria

AC1. `specs/editor-skill-optimization.md` exists and defines the optimized `editor` output contract.

AC2. `tests/evals/skills/editor/cases.yaml` exists and includes scenarios for proofreading, indirect PR-description editing, integrity-boundary misuse, bilingual technical translation, simple acknowledgement text, and conversational-looking source text.

AC3. Baseline evidence is recorded before `skills/editor/SKILL.md` is edited.

AC4. Post-change evidence compares optimized behavior against the baseline scenario classes.

AC5. Normal editing and translation requests use the fixed three-stage workflow.

AC6. Optimization reasons are included by default.

AC7. Language-quality assessment is included before translation.

AC8. Chinese and English translations are included by default.

AC9. Integrity-boundary requests preserve accurate wording and do not introduce unsupported meaning.

AC10. `skills/editor/SKILL.md` remains pure prompt with `$ARGUMENTS` and `## Output Format`, and without optional frontmatter.

AC11. No other skill prompt is optimized in this slice.

AC12. `python tests/validate_skills.py` passes.

AC13. `python -m unittest discover tests` passes.

AC14. `git diff --check` passes.

AC15. `python tests/check_readme_sync.py` is run if the helper exists in the branch.

## Open questions

None.

## Readiness

Ready for implementation/review only when the plan, test spec, evidence, and skill prompt all reflect the amended fixed three-stage workflow.
