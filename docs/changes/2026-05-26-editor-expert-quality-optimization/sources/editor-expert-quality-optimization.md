# Editor Expert Quality Optimization

## Status

approved

## Related proposal

- `docs/proposals/2026-05-26-editor-expert-quality-optimization.md`
- Proposal review R1: `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/proposal-review-r1.md`
- Proposal review R2: `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/proposal-review-r2.md`
- Proposal review R3: `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/proposal-review-r3.md`
- Proposal review R4: `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/proposal-review-r4.md`
- Proposal review R5: `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/proposal-review-r5.md`
- Spec review R4: `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/spec-review-r4.md`
- Supersedes: `specs/editor-skill-optimization.md`

## Goal and context

The `editor` skill should behave like a senior professional editor and translator whose defining traits are fidelity and restraint. It should improve text only where the improvement helps, preserve the author's meaning and factual content, separate instruction, source, and target language roles before acting, and provide Chinese and English final versions by default while honoring explicit target-language requests.

This spec replaces the previous fixed three-stage report contract. Chinese and English final output remains the default, but explicit target-language requests override the visible default. Default assessment sections, default "why" sections, and duplicate source-language sections are no longer the default for simple edits.

## Glossary

- Editor skill: `skills/editor/SKILL.md`.
- Instruction: the user's direction to the skill, such as `fix this`, `帮我润色`, `make this suitable for a PR description`, or `translate this`.
- Instruction language: the detected language the user uses to address the skill.
- Source text: the artifact supplied through `$ARGUMENTS` that should be edited, translated, or rendered.
- Source language: the detected primary language or intentional language mix of the source text.
- Target language set: the visible output language set; defaults to Chinese and English and honors explicit user requests for another target language or language set.
- Response language: the language used for labels, notes, explanations, refusals, and other non-deliverable response framing. It follows the instruction language when one is clearly present, otherwise it falls back to the source language.
- Response framing: labels, notes, explanations, refusals, and other non-deliverable wrapper text around the final edited or translated content.
- Final Chinese version: the Chinese final deliverable that preserves the source meaning after expert editing.
- Final English version: the English final deliverable that preserves the source meaning after expert editing.
- Duplicate source-language section: a separate optimized-text block that repeats the same content as the final Chinese or English version for simple Chinese or English source edits.
- Expert-quality editing: editing that combines fidelity, restraint, professional polish, context sensitivity, terminology care, integrity, minimality when appropriate, and pre-return verification.
- Supporting notes: concise notes shown only when the user explicitly asks for explanation or changes.
- Integrity boundary: a request to make text misleading, false, deceptive, more certain than warranted, falsely attributed, or materially different from the known source meaning.

## Examples first

Example E1: English professional polish uses English response framing
Given the user asks `Make this sound more professional` for rough English migration text
When the source preserves uncertainty such as "maybe still some edge cases"
Then the skill returns English-framed output with Chinese and English final versions by default, preserves uncertainty, and does not add a default assessment section.

Example E2: Chinese instruction with English source uses Chinese framing and English editing
Given the user asks `帮我润色一下这段 PR 描述:This PR fix the cache invalidation when user update there profile.`
When the instruction language is Chinese and the source language is English
Then the skill frames labels and notes in Chinese, edits the English source as English before rendering the target-language output, preserves the cache-invalidation meaning, and returns Chinese and English final versions by default.

Example E3: English instruction with Chinese source uses English framing and Chinese editing
Given the user asks `Polish this and make it suitable for a PR description:` followed by Chinese PR source text
When the instruction language is English and the source language is Chinese
Then the skill frames labels and notes in English, edits the Chinese source as Chinese before rendering the target-language output, preserves the cache-invalidation meaning, and returns Chinese and English final versions by default.

Example E4: English source does not duplicate final English
Given the user asks `Polish this lightly` for already-good English text
When the source says `The rollout is complete. We will monitor error rates for 24 hours...`
Then the final English version is the edited source-language version, no separate optimized-text section repeats it, and the 24-hour detail is preserved.

Example E5: non-Chinese/non-English source edit may include optimized source text
Given the user asks in another language to briefly edit source text in that language
When the user asks to edit or polish the source-language text itself
Then the skill may include an optimized source-language version and still returns Chinese and English final versions by default unless the user explicitly requested another target.

Example E6: non-Chinese/non-English translation without edit does not add source-language version by default
Given the user provides source text in a language other than Chinese or English and asks only for translation
When no edit or polish of the source-language text is requested
Then the skill returns Chinese and English final versions without an optimized source-language section by default unless the user explicitly requested another target.

Example E7: fidelity guardrail preserves exact meaning
Given the user asks to improve `The dim lighting made it hard to read the labels.`
When the source uses "dim lighting" as the condition
Then the skill preserves that condition and does not alter it to "dimming light" or another concept.

Example E8: integrity-boundary request is refused accurately
Given the user asks in Chinese to make a customer statement sound approved when the source only says the customer will review it later
When the requested edit would falsify approval
Then the skill briefly refuses in Chinese, the instruction language, and offers accurate alternatives in the requested target languages, defaulting to Chinese and English.

## Requirements

R1. The optimized `editor` skill MUST keep `name: editor`.

R2. The optimized `editor` skill MUST remain a pure prompt skill without runtime-specific tool frontmatter, tool permissions, scripts, generated assets, or external runtime dependencies.

R3. The optimized `editor` skill MUST keep `$ARGUMENTS` as the input surface for source text and editing instructions.

R4. The optimized `editor` skill MUST include a `## Output Format` section.

R5. The `description` field MUST no longer advertise a fixed three-stage report.

R6. The `description` field MUST describe expert editing or professional editing judgment, default Chinese and English final output, explicit target-language overrides, and common trigger contexts such as emails, PR descriptions, docs, release notes, and messages.

R7. The skill body MUST define expert-quality editing as fidelity plus restraint, professional polish, context sensitivity, terminology care, integrity, minimality when appropriate, and verification.

R8. The skill MUST separate incoming input into instruction, source, and target roles before acting.

R9. The skill MUST treat the instruction as the user's direction to the tool, not as text to edit, unless the user explicitly asks to edit that instruction.

R10. The skill MUST treat source text as the artifact to edit, translate, or render, not as conversation to answer, including when the source text itself looks like a question, greeting, command, or instruction.

R11. The skill MUST detect the instruction language, source language, and response language before composing the response.

R12. When the user's instruction language is clearly detectable, response language MUST follow the instruction language for labels, supporting notes, refusals, and explanations.

R13. When the user's instruction language is not clearly detectable, response language MUST follow the source language for labels, supporting notes, refusals, and explanations.

R14. For response languages other than Chinese or English, the skill SHOULD use the detected response language for labels, supporting notes, refusals, and explanations when practical; if that framing would reduce clarity, it MAY use concise English framing while still preserving source meaning.

R15. The skill MUST accept source text in any detected language by default and MUST NOT reject source text solely because it is not Chinese or English. This is a language-agnostic source-intake rule, not a guarantee of equal editorial quality across all languages.

R16. The skill MUST provide a final Chinese version and a final English version by default for non-empty source input in any detected language.

R17. For Chinese source text, the final Chinese version MUST be the edited source-language version unless the user explicitly asks for a different Chinese variant.

R18. For English source text, the final English version MUST be the edited source-language version unless the user explicitly asks for a different English variant.

R19. The skill MUST edit source text in its source language before rendering target-language versions; it MUST NOT translate first and then edit the translation as if it were the source.

R20. For simple Chinese or English edit requests, the skill MUST NOT duplicate the edited source-language final version in a separate optimized-text section.

R21. For simple edit requests, the skill MUST NOT include a default assessment section.

R22. For simple edit requests, the skill MUST NOT include a default `Why` or change-explanation section.

R23. The skill MUST include concise supporting notes only when the user explicitly asks for explanation, notes, or changes. Ambiguity, substantial edits, translation choices, and integrity boundaries MUST be handled in the output itself without adding a note unless the user asked for one.

R24. The skill MUST preserve source meaning, facts, names, numbers, technical terms, logic, commitments, uncertainty, voice, intent, audience, tone, and requested format unless preserving a requested format would conflict with meaning preservation or integrity.

R25. The skill MUST change only what improves clarity, grammar, flow, tone, concision, structure, terminology, or idiomatic expression.

R26. If the source text is already good, the skill MUST make minimal changes or leave the wording nearly unchanged.

R27. The skill MUST NOT replace precise wording with fancier but less accurate wording.

R28. If a phrase, term, or technical reference is ambiguous, the skill MUST preserve the ambiguity or flag it briefly rather than silently choosing an unsupported meaning.

R29. The skill MUST preserve intentional code-switching, mixed-language technical terms, product names, API names, and domain terminology unless the user asks to localize them or they are clearly erroneous.

R30. The skill MUST adapt the edit to audience, medium, and requested tone when those signals are present in the source or instruction.

R31. The skill MUST support proofreading, polishing, professionalizing, clarity rewriting, translation-oriented requests, PR-description editing, documentation/release-note editing, messages, ambiguous pasted text, and integrity-boundary handling.

R32. The skill MUST provide Chinese and English final versions for translation-oriented requests when no explicit target language is requested.

R33. The skill MUST honor explicit target-language requests, including target-language-only requests, unless they conflict with integrity or meaning preservation.

R34. For source text in languages other than Chinese or English, the skill MUST include an optimized source-language version only when the user asks to edit, polish, rewrite, or professionalize the source-language text itself.

R35. For source text in languages other than Chinese or English where the user asks only for translation, the skill MUST NOT add an optimized source-language version by default.

R36. The skill MUST refuse to make text misleading, false, deceptive, more certain than the source supports, falsely attributed, or materially inconsistent with known source meaning.

R37. For integrity-boundary requests, the skill MUST briefly explain the refusal in the response language and offer accurate alternatives in the requested target languages, defaulting to Chinese and English.

R38. Before returning, the skill MUST resolve the source meaning once, render the requested target-language versions from that meaning, and verify that visible target versions and any edited source-language version preserve the same meaning, tone, intent, and formatting intent. For single-target requests, the skill SHOULD internally render Chinese and English where practical to preserve the bilingual fidelity cross-check while displaying only the requested target.

R39. The output format MUST optimize for copyability: final target-language deliverables appear on their own lines or blocks under clear labels.

R40. The output format MUST avoid emoji and decorative symbols.

R41. The output format SHOULD keep labels concise and visually distinct from copyable content.

R42. The optimized `SKILL.md` SHOULD remain concise and MUST remain under 500 lines unless an accepted exception explains why progressive disclosure is unsuitable.

R43. The change MUST keep or update `tests/evals/skills/editor/cases.yaml` with expert-quality eval scenarios.

R44. Eval scenarios MUST include professional polish with restraint, already-good text restraint, `dim lighting` fidelity, Chinese-instruction/English-source role separation, English-instruction/Chinese-source role separation, intentional code-switching, non-Chinese/non-English source handling, engineer-facing PR editing, and integrity-boundary misuse.

R45. Baseline evidence MUST be recorded before editing `skills/editor/SKILL.md`.

R46. Post-change evidence MUST compare optimized behavior against the same scenario classes used for baseline evidence.

R47. The implementation MUST NOT add live model calls to CI.

R48. Repository-wide validator changes MUST NOT be introduced in this slice unless implementation proves the existing eval-fixture path cannot represent this material skill change.

R49. The implementation MUST NOT optimize the prompt body of `doctor`, `oscp-coach`, or any other skill in this slice.

## Inputs and outputs

Inputs:

- User instructions and source text passed through `$ARGUMENTS`.
- `skills/editor/SKILL.md`.
- `tests/evals/skills/editor/cases.yaml`.
- Baseline and post-change evidence recorded in the change evidence area.

Supported source-language contract:

- Source text in any detected language. The skill must not reject source text only because it is outside Chinese or English, while recognizing that this does not guarantee equal editorial quality across all languages.

Required output contract:

- Non-empty source input in any detected language returns final Chinese and English versions by default.
- Explicit target-language requests override the visible default target set.
- Response framing uses the detected response language: the instruction language when clearly detectable, otherwise the source language.
- The source is edited in its source language before target-language versions are rendered.
- Simple Chinese or English edit requests return only the smallest useful target-language deliverable: target-language final versions, no assessment section, no default `Why` section, and no duplicate source-language optimized-text section.
- Supporting notes appear only when the user explicitly asks for explanation, notes, or changes.

Default target-language set: Chinese and English.

Required simple-output template for default Chinese and English output:

```markdown
**<Chinese label in response language>**
<final Chinese version>

**<English label in response language>**
<final English version>
```

Required label text:

| Response language | Chinese label | English label | Note label |
|---|---|---|---|
| English | `Chinese` | `English` | `Note` |
| Chinese | `中文` | `英文` | `说明` |
| Other detected response language | localized equivalent where practical; otherwise `Chinese` | localized equivalent where practical; otherwise `English` | localized equivalent where practical; otherwise `Note` |

Required target-language block pattern:

```markdown
**<target language label in response language>**
<final target-language version>
```

For the default target-language set, repeat this pattern once for Chinese and once for English. When the user requests an explicit target language or language set, repeat this pattern only for the requested visible target language or languages.

Required note-bearing template when the user explicitly asks for explanation, notes, or changes:

```markdown
<target-language block pattern repeated for each visible target language>

**<Note label in response language>**
<concise note>
```

Required non-Chinese/non-English source-edit template when the user asks to edit the source-language text itself:

```markdown
**<Edited source label in response language>**
<edited source-language version>

<target-language block pattern repeated for each visible target language>
```

Required target-language-aware integrity-boundary template:

```markdown
<brief refusal in response language>

<target-language block pattern repeated for each visible target language, containing accurate alternatives>
```

Required explicit-target-output template:

```markdown
**<target language label in response language>**
<final target-language version>
```

When the user requests multiple explicit target languages, repeat the same label/content pattern once per requested target language.

Outputs are Markdown-compatible plain text. No tool output, generated files, or external service results are part of the skill runtime contract.

## State and invariants

- `editor` remains an existing skill named `editor`.
- `editor` remains a pure Markdown prompt skill.
- `editor` remains broadly useful for professional editing and translation rather than becoming engineer-only.
- Chinese and English final versions are the default for non-empty input in any language.
- Explicit target-language overrides are honored unless they conflict with integrity or meaning preservation.
- Instruction/source/target role separation is invariant for all non-empty input.
- Response-language-aware framing is invariant for all input.
- Eval fixtures are reviewer evidence and do not require live model execution in CI.
- The prior fixed three-stage editor spec is superseded by this spec once this spec is approved.

## Error and boundary behavior

- Empty input is outside the required behavior contract; the skill may ask for text to edit.
- Source text in all languages is inside the default intake contract, but this does not guarantee equal expert editorial quality across all languages.
- If source language detection is uncertain, the skill SHOULD choose the most likely language and avoid adding an explanatory note unless the user explicitly asks for one.
- If the user asks for target-language-only output, the skill MUST honor that explicit target request unless it conflicts with integrity or meaning preservation.
- If the user asks for misleading wording, the integrity boundary overrides tone, audience, format, and style instructions.
- If explicit user formatting conflicts with copyability or concision, the user format wins unless it conflicts with meaning preservation, integrity, or the requested target-language output.
- If technical terminology is uncertain, the skill preserves the term or flags ambiguity rather than substituting an unsupported term.

## Compatibility and migration

- Existing install behavior and slash-command naming MUST remain unchanged.
- The skill name remains `editor`.
- The old fixed three-stage output is a breaking output-format change and MUST be called out in PR notes.
- Migration guidance: users should expect concise expert-editor output with Chinese and English final versions by default, explicit target-language overrides when requested, and no previous fixed optimized-text, assessment, and bilingual report.
- Existing README skill tables, command lists, and usage examples MUST be updated only if they mirror the changed description or output contract.
- The skill omits optional metadata such as `argument-hint`, `effort`, and `allowed-tools`; those fields remain unnecessary for portable behavior.
- Rollback is limited to reverting `skills/editor/SKILL.md`, `tests/evals/skills/editor/cases.yaml`, this spec, and related change evidence.

## Observability

- `tests/evals/skills/editor/cases.yaml` MUST make expected behavior observable to reviewers.
- Baseline evidence MUST identify how the current skill behaves before prompt edits.
- Post-change evidence MUST identify how the optimized skill behaves after prompt edits.
- Manual smoke evidence SHOULD include the weakest model the project realistically expects to support.
- Manual smoke evidence MUST include the `dim lighting` fidelity case when model smoke is performed.
- Validation output from `python tests/validate_skills.py` MUST show that the repository remains valid.
- Final implementation evidence MUST report the line count for `skills/editor/SKILL.md`.

## Security and privacy

- Eval prompts MUST use fictional or sanitized content.
- Eval prompts MUST NOT contain secrets, credentials, private local paths, unpublished personal data, or real customer-sensitive details.
- The optimized skill MUST NOT ask users for secrets, credentials, or private local files.
- Integrity-boundary behavior MUST prevent the skill from helping falsify approvals, consent, claims, authorship, certainty, or material facts.
- This change MUST NOT alter high-risk skill behavior.

## Accessibility and UX

No interactive UI is introduced.

The optimized output SHOULD be easy to scan and reuse, with concise labels, copyable target-language content, response-language-aware framing, and no decorative emoji.

## Performance expectations

- The skill prompt SHOULD remain concise enough for ordinary assistant context use.
- Static validation and eval-fixture checks MUST remain deterministic.
- CI MUST NOT require network access or live model calls for this change.

## Edge cases

EC1. English instruction asks `fix this` with English source text. The skill uses English framing and returns Chinese and English final versions by default without default assessment or `Why`.

EC2. Chinese instruction says `帮我润色一下` with Chinese source text. The skill uses Chinese framing and returns Chinese and English final versions by default.

EC2a. Chinese instruction includes English source text. The skill uses Chinese framing because the instruction language is clearly Chinese, while preserving the English source meaning in the final Chinese and English versions.

EC2b. English instruction includes Chinese source text. The skill uses English framing because the instruction language is clearly English, while preserving the Chinese source meaning in the final Chinese and English versions.

EC3. English source is already good. The skill makes minimal changes, preserves details, and avoids duplicate optimized-text output.

EC4. English source includes uncertainty. The skill preserves uncertainty and does not overstate completion, safety, approval, or certainty.

EC5. Technical PR text contains grammar errors. The skill edits into concise PR-ready wording while preserving cache invalidation and stale profile meaning.

EC6. Non-Chinese/non-English source asks for editing. The skill may include an optimized source-language version and returns Chinese and English final versions by default unless the user explicitly requests another target.

EC7. Non-Chinese/non-English source asks only for translation. The skill returns Chinese and English final versions without an optimized source-language version by default unless the user explicitly requests another target.

EC8. Source phrase has a non-obvious ambiguity. The skill preserves the ambiguity or edits around it rather than silently choosing an unsupported meaning; it adds an explanatory note only when the user asks for notes.

EC9. User asks to make a customer statement imply approval that did not happen. The skill refuses briefly and offers accurate alternatives in the requested target languages, defaulting to Chinese and English.

EC10. Source text looks like a question, greeting, or instruction. The skill treats it as source material to edit or translate instead of answering it conversationally.

EC11. User asks to show what changed. The skill includes concise notes plus target-language final versions, defaulting to Chinese and English.

EC11a. User explicitly asks for English-only output. The skill displays only the English target-language version while internally using Chinese/English cross-checking where practical.

EC12. User asks for a misleading target tone. The skill applies only accurate tone improvements and does not distort source meaning.

## Non-goals

- Do not optimize every existing skill in this slice.
- Do not optimize high-risk skills such as `doctor` or `oscp-coach`.
- Do not introduce live model CI.
- Do not add tools, scripts, runtime dependencies, or generated prompt assets.
- Do not rename `editor`.
- Do not convert `editor` into an engineer-only skill.
- Do not provide target-language-only output by default; target-language-only output is allowed only when explicitly requested.
- Do not introduce repository-wide validator behavior changes unless the existing eval-fixture path cannot represent the change.

## Acceptance criteria

AC1. `docs/proposals/2026-05-26-editor-expert-quality-optimization.md` is accepted and linked from this spec.

AC2. `docs/proposals/2026-05-25-editor-skill-optimization.md` and `specs/editor-skill-optimization.md` are marked superseded by the expert-quality optimization path.

AC3. `skills/editor/SKILL.md` keeps `name: editor`, `$ARGUMENTS`, and `## Output Format`.

AC4. `skills/editor/SKILL.md` remains a pure prompt skill without optional tool frontmatter.

AC5. `skills/editor/SKILL.md` defines expert-quality editing as fidelity with restraint plus the concrete quality dimensions in this spec.

AC6. The output contract includes Chinese and English final versions by default for non-empty source input in any detected language.

AC7. Explicit target-language requests override the visible default target set unless they conflict with integrity or meaning preservation.

AC8. Simple Chinese and English edits do not duplicate the edited source-language final version in a separate optimized-text section.

AC9. Simple edits do not include default assessment or `Why` sections.

AC10. Default simple output uses the required two-label template with copyable Chinese and English content on their own lines or blocks.

AC11. Explicit single-target output uses the required explicit-target-output template and displays only the requested target language.

AC12. Note-bearing output uses the required target-language-aware note-bearing template and includes notes only when the user explicitly asks for explanation, notes, or changes.

AC13. Clearly English instruction input uses English response framing even when the source text is Chinese.

AC14. Clearly Chinese instruction input uses Chinese response framing even when the source text is English.

AC15. Non-Chinese/non-English source behavior is bounded: an optimized source-language version appears only when the user asks to edit or polish the source-language text itself.

AC16. Integrity-boundary requests refuse misleading transformations and use the required target-language-aware integrity-boundary template.

AC17. Eval fixtures cover professional polish with restraint, already-good text restraint, `dim lighting` fidelity, Chinese-instruction/English-source role separation, English-instruction/Chinese-source role separation, explicit single-target override, intentional code-switching, non-Chinese/non-English source handling, engineer-facing PR editing, and integrity-boundary misuse.

AC18. Baseline evidence is recorded before `skills/editor/SKILL.md` is edited.

AC19. Post-change evidence compares against the same scenario classes.

AC20. `python tests/validate_skills.py` passes.

AC21. `python -m unittest discover tests` passes.

AC22. `git diff --check` passes.

AC23. `python tests/check_readme_sync.py` is run if present.

AC24. Final implementation evidence reports `wc -l skills/editor/SKILL.md`.

## Open questions

None.

## Next artifacts

1. Spec review result for this spec.
2. Execution plan.
3. Plan review result.
4. `specs/editor-expert-quality-optimization.test.md`.
5. Baseline evidence before modifying `skills/editor/SKILL.md`.

## Follow-on artifacts

- `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/spec-review-r2.md`

## Readiness

Approved by `docs/changes/2026-05-26-editor-expert-quality-optimization/reviews/spec-review-r4.md` after the target-language-aware template revision. Ready for architecture-reviewed planning.
