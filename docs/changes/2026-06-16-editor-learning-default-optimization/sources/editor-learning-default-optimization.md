# Editor Learning Default Optimization

## Status

approved

## Related proposal

- Accepted proposal: `docs/proposals/2026-06-16-editor-learning-default-optimization.md`
- Proposal review R1: `docs/changes/2026-06-16-editor-learning-default-optimization/reviews/proposal-review-r1.md`
- Proposal review R2: `docs/changes/2026-06-16-editor-learning-default-optimization/reviews/proposal-review-r2.md`
- Extends: `specs/editor-expert-quality-optimization.md`
- Supersedes conflicting requirements in `specs/editor-expert-quality-optimization.md` that make supporting notes opt-in only, especially R23 and AC12.

## Goal and context

The `editor` skill should keep its expert editor and translator contract while making teaching a default secondary behavior. The primary deliverable remains polished and translated text. After that deliverable, the skill should include a structured `Learning notes` block by default so the user can learn from substantive edits.

This spec changes only the notes/default-teaching portion of the current editor contract. It preserves the existing language-role model, default Chinese and English visible output, explicit target-language overrides, fidelity with restraint, integrity boundaries, copyable deliverables, and pure-prompt boundary.

## Glossary

- Editor skill: `skills/editor/SKILL.md`.
- Source text: the artifact supplied through `$ARGUMENTS` that should be edited, polished, rewritten, translated, or rendered.
- Instruction language: the detected language the user uses to address the skill.
- Response language: the language used for labels, learning notes, refusals, and other non-deliverable response framing.
- Target language set: the visible output language set; defaults to Chinese and English and honors explicit user target-language requests.
- Learning notes block: the post-deliverable teaching block that appears by default for normal polish, rewrite, and translation requests. Its English label is `Learning notes`; its Chinese label is `学习要点`; other response languages use a localized equivalent where practical, otherwise `Learning notes`.
- Learning note: one bullet or short paragraph in the learning notes block, anchored to a concrete edit or translation choice and teaching a reusable principle.
- Substantive lesson: a non-trivial writing, editing, or translation principle that the user can reuse in future writing.
- Trivial edit: a typo, punctuation, capitalization, or mechanical correction that does not reveal a reusable pattern.
- Explicit suppression: a direct user request for output-only delivery or no explanation, such as `no notes`, `just the text`, `only the translation`, `skip the explanation`, `不用解释`, `不要说明`, or `只要译文`.
- Ambiguous brevity cue: an indirect request such as `keep it short`, `I'm in a hurry`, or `just need this quickly` that may mean concise output but does not explicitly ask to remove notes.

## Examples first

Example E1: default polish includes learning notes
Given the user asks `Polish this:` followed by `We are committed to delivering excellent solutions for users and we will try to make the migration easy.`
When no explicit suppression phrase is present
Then the skill returns Chinese and English final versions first, followed by a `Learning notes` block that teaches at least one substantive lesson from the edit.

Example E2: explicit English target still includes learning notes
Given the user asks `Translate this into English:` followed by `这个方案比较稳，但上线后还是要观察错误率。`
When English is the explicit visible target language
Then the skill returns the English deliverable first, followed by a `Learning notes` block unless the user explicitly suppresses notes.

Example E3: explicit suppression removes learning notes
Given the user asks `Just polish this. No notes.` followed by source text
When the request directly suppresses explanation
Then the skill returns the requested deliverable and does not include a `Learning notes` block.

Example E4: ambiguous brevity does not suppress learning notes
Given the user asks `Keep it short and polish this:` followed by source text
When the request does not explicitly ask to remove notes
Then the skill returns the deliverable first and still includes a focused `Learning notes` block.

Example E5: already-good text teaches restraint without padding
Given the user asks `Polish this:` followed by `The rollout is complete. We will monitor error rates for 24 hours and follow up if we see regressions.`
When the source is already clear and accurate
Then the skill makes minimal or no wording changes, preserves `24 hours`, and includes at most one learning note about restraint rather than inventing extra edits or padded notes.

Example E6: trivial typo does not create a lesson quota
Given the user asks `Polish this:` followed by `We shiped the docs yesterday.`
When the only useful edit is a typo correction
Then the skill corrects the typo, produces the requested deliverable first, and includes a `Learning notes` block with exactly one concise fallback note, such as `Only the typo was corrected; there was no broader writing pattern to teach.`

Example E7: already-strong text teaches restraint without padding
Given the user asks `Polish this:` followed by `The rollout is complete. We will monitor error rates for 24 hours and follow up if we see regressions.`
When the source is already clear and accurate
Then the skill makes minimal or no wording changes, preserves `24 hours`, and includes a `Learning notes` block with at most one restraint note, such as `The original was already clear, so I preserved the structure and made only minimal changes.`

Example E8: integrity boundary preserves truth
Given the user asks to rewrite `The customer said they will review the launch plan next week.` so it sounds like customer approval
When the source does not support approval
Then the skill refuses the misleading transformation, offers accurate alternatives in the visible target languages, and may include one learning note explaining that review intent cannot be represented as approval.

## Requirements

R1. The `editor` skill MUST keep the expert-quality editing requirements from `specs/editor-expert-quality-optimization.md` unless a requirement in this spec explicitly supersedes them.

R2. The `editor` skill MUST remain a pure prompt skill with no new tools, scripts, generated assets, runtime dependencies, or live-model CI requirements.

R3. The `editor` skill description MUST identify the skill as an expert professional editor and translator, not as a standalone writing coach.

R4. The `editor` skill description MUST mention learning from edits to shared text as part of the skill behavior.

R5. The `editor` skill description MUST NOT include standalone coaching triggers that do not require source text, such as a broad `help me improve my writing` mode.

R6. For every non-empty, non-suppressed editing or translation request, the skill MUST include a learning notes block after the polished or translated deliverable. The block MUST contain either one or more substantive learning notes, or exactly one concise fallback note for trivial-only, already-strong, no-substantive-lesson, brittle-rule, or integrity-boundary cases. The block MUST NOT be empty and MUST NOT be padded.

R7. The learning notes block MUST appear after all visible target-language deliverables.

R8. The learning notes block MUST NOT be interleaved with the polished or translated deliverable.

R9. The English response-language label for the learning notes block MUST be `Learning notes`.

R10. The Chinese response-language label for the learning notes block MUST be `学习要点`.

R11. For other response languages, the learning notes label SHOULD be localized where practical; if localization would reduce clarity, the label MUST be `Learning notes`.

R12. Each substantive learning note MUST use concrete original-to-revised anchoring or an equivalent concrete reference to the edit or translation choice.

R12a. Fallback learning notes for restraint, typo-only, no-substantive-lesson, brittle-rule, or integrity-boundary cases are exempt from original-to-revised anchoring only when there is no substantive edit or no safe reusable principle to teach. Those fallback notes MUST still reference the concrete source condition, edit category, or integrity issue. Generic self-commentary such as `I improved the text`, `This is better`, `I made it more professional`, or `Good writing is clear` MUST NOT satisfy this requirement.

R13. Each learning note MUST teach a reusable writing, editing, or translation principle rather than merely reporting that a change was made.

R14. Learning notes MUST be written in the response language and MUST NOT be duplicated bilingually by default.

R15. Learning notes MUST preserve and support source meaning, facts, names, numbers, technical details, uncertainty, logic, intent, commitments, voice, requested tone, and integrity boundaries.

R16. Learning notes MUST NOT justify meaning drift, unsupported certainty, false approval, false attribution, or any transformation that conflicts with the source.

R17. The skill MUST NOT create extra edits for the purpose of producing learning notes.

R18. The skill MUST include one learning note per substantive lesson, not one note per mechanical edit.

R19. The skill MUST NOT impose a fixed numeric cap on the learning notes block.

R20. The skill MUST include the substantive lessons that are genuinely useful for the user's source text.

R21. The skill MUST treat the number of learning notes as an outcome of actual substantive edits or translation choices, not as a quota, and MUST NOT pad the learning notes block.

R22. The skill MUST keep the learning notes block scannable by using one bullet per substantive lesson and, when the useful note set becomes longer or varied, grouping notes under short theme labels inside the same learning notes block.

R23. The skill MUST NOT explain ordinary typos, punctuation, capitalization, or mechanical corrections as full grammar lessons unless they reveal a recurring pattern. For a trivial-only correction, the skill MUST still render the default learning notes block unless the user explicitly suppresses notes. In that case, the block MUST contain exactly one concise fallback note, such as `Only the typo was corrected; there was no broader writing pattern to teach.`

R24. If the source text is already strong and needs little change, the skill MUST make minimal or no changes and MUST include at most one fallback learning note about restraint or preservation unless the user explicitly suppresses notes.

R25. The skill MUST NOT teach brittle, oversimplified, or misleading rules. If no safe generalizable principle should be taught, the skill MUST still render the default learning notes block unless explicitly suppressed. In that case, the block MUST contain exactly one concise fallback note that references the concrete condition, such as `No safe general rule is worth teaching here; the choice depends on context.`

R26. The skill MUST suppress the learning notes block when the user explicitly asks for output-only delivery or no explanation.

R27. Explicit suppression MUST include direct phrases such as `no notes`, `just the text`, `only the translation`, `skip the explanation`, `不用解释`, `不要说明`, `只要译文`, and equivalent direct phrasing in the user's language.

R28. The skill MUST NOT infer suppression from ambiguous brevity cues such as `keep it short`, `I'm in a hurry`, or `just need this quickly`.

R29. When suppression intent is ambiguous, the skill MUST show focused learning notes by default.

R30. When the user explicitly asks to learn more, the skill MAY expand the learning notes beyond the default brevity, but the expanded explanation MUST remain anchored to concrete edits or translation choices.

R31. Explicit target-language requests MUST continue to override the visible target-language set; the learning notes block MUST still appear after the requested visible deliverables unless explicitly suppressed.

R32. Integrity-boundary refusals MUST continue to use the response language and visible target-language alternatives required by `specs/editor-expert-quality-optimization.md`; any learning note included with a refusal MUST be concise and truth-preserving.

R33. The default output template for Chinese and English visible output MUST be:

```markdown
**<Chinese label in response language>**
<final Chinese version>

**<English label in response language>**
<final English version>

**<Learning notes label in response language>**
- `<original>` -> `<revised>`: <generalizable principle>.
```

R34. For explicit single-target output, the output template MUST be:

```markdown
**<target language label in response language>**
<final target-language version>

**<Learning notes label in response language>**
- `<original>` -> `<revised>`: <generalizable principle>.
```

R35. When explicit suppression is present, the output template MUST omit the learning notes block and retain the applicable visible target-language deliverable template.

R35a. For no-substantive-lesson cases, the default Chinese and English output template MUST be:

```markdown
**<Chinese label in response language>**
<final Chinese version>

**<English label in response language>**
<final English version>

**<Learning notes label in response language>**
- <one concise fallback note referencing the concrete source condition or edit category>
```

R35b. For longer or varied learning-note sets, the output template SHOULD keep one learning notes block and group bullets by short theme labels:

```markdown
**<Learning notes label in response language>**
**<theme label>**
- `<original>` -> `<revised>`: <generalizable principle>.
- `<original>` -> `<revised>`: <generalizable principle>.

**<theme label>**
- `<original>` -> `<revised>`: <generalizable principle>.
```

R36. The implementation MUST update or replace any existing editor prompt text that says notes appear only when explicitly requested.

R37. Eval evidence MUST include baseline behavior showing current learning value from the same prompts before this change and post-change behavior showing default learning value without unacceptable bloat, over-editing, or fidelity drift.

R38. Eval evidence MUST cover default learning notes, explicit suppression, ambiguous suppression fallback, no over-editing to teach, trivial mechanical fixes, already-good text restraint, brittle-rule qualification, translation learning notes, mixed-language response framing, and integrity boundaries.

## Inputs and outputs

Inputs:

- `$ARGUMENTS` containing the user's instruction, source text, and any explicit target-language, tone, formatting, learning, or suppression request.

Outputs:

- Markdown-compatible plain text.
- Visible target-language deliverables first.
- A learning notes block after the visible deliverables by default.
- No generated files, tool outputs, external service results, or hidden runtime artifacts.

### Default Learning notes block contract

For every non-empty editing, polishing, rewriting, professionalizing, or translation request, the skill MUST render a `Learning notes` block by default after the deliverable unless the user explicitly suppresses notes.

The `Learning notes` block MUST NOT be empty.

For ordinary substantive edits or translation choices, the block SHOULD contain one note per substantive lesson and MUST NOT be constrained by a fixed numeric maximum.

For trivial-only corrections, already-strong text, no-substantive-lesson cases, brittle-rule cases, or cases where a tempting rule would be misleading, the block MUST contain exactly one concise fallback note.

The fallback note MUST be concrete and non-padded. It MUST reference the source condition, edit category, or integrity issue.

Allowed fallback examples:

- `Only the typo was corrected; there was no broader writing pattern to teach.`
- `The original was already clear, so I preserved the structure and made only minimal changes.`
- `No safe general rule is worth teaching here; the choice depends on context.`
- `I preserved the ambiguity because the source does not support a more specific claim.`
- `Approval cannot be implied from a promise to review; the alternative keeps the claim accurate.`

The skill MUST NOT invent edits, exaggerate lessons, or produce padded explanations merely to populate the `Learning notes` block.

The normal path that removes the `Learning notes` block is explicit suppression, such as `no notes`, `just the text`, `only the translation`, `skip the explanation`, `不用解释`, `不要说明`, or `只要译文`.

For empty input or clarification-only responses where no deliverable is produced, the skill MAY omit the `Learning notes` block.

Default visible output:

- Chinese final version.
- English final version.
- Learning notes block.

Explicit target-language output:

- Requested visible target-language version or versions.
- Learning notes block unless explicitly suppressed.

Explicitly suppressed output:

- Requested visible deliverable only.
- No learning notes block.

## State and invariants

- The skill has no persistent runtime state.
- Deliverable-first ordering is invariant unless an integrity refusal must precede accurate alternatives under the existing editor integrity-boundary contract.
- Teaching is subordinate to fidelity, restraint, and integrity.
- The learning notes block is default-on for normal non-empty editing and translation requests.
- Explicit suppression is honored.
- Ambiguous suppression intent keeps focused learning notes.
- The learning notes block has no fixed numeric cap.
- The note count follows actual useful substantive lessons and is not a quota.
- Longer or varied learning-note sets stay scannable through short theme labels inside the same block.
- Response-language framing applies to learning notes.
- Visible target-language behavior from `specs/editor-expert-quality-optimization.md` remains in force except where this spec explicitly changes notes behavior.

## Error and boundary behavior

- Empty or missing source text: the skill should ask for source text or state that it needs text to edit or translate; it should not produce a learning notes block without a source artifact.
- Standalone writing-coaching request without source text: the skill should not act as a broad writing coach; it should ask for text to edit or translate.
- Explicit no-notes request: the skill must omit learning notes.
- Ambiguous brevity request: the skill must keep focused learning notes.
- Misleading transformation request: the skill must refuse or redirect accurately under the existing integrity-boundary contract; teaching must not weaken the refusal.
- Already-good source: the skill must not invent unnecessary edits or padded notes; unless explicitly suppressed, it must render the learning notes block with at most one restraint-oriented fallback note.
- Trivial-only correction: the skill must avoid long grammar lessons and padded teaching notes; unless explicitly suppressed, it must render the learning notes block with exactly one concise fallback note identifying the correction as trivial.
- Unsupported target-language request: existing target-language and integrity behavior remains governed by `specs/editor-expert-quality-optimization.md`.

## Compatibility and migration

This spec is a deliberate output-contract change for `editor`.

- It supersedes the current notes-on-request default in `specs/editor-expert-quality-optimization.md`.
- It preserves default Chinese and English visible output unless the user explicitly requests another target-language set.
- It preserves explicit target-language-only output while adding learning notes after the requested target deliverable unless explicitly suppressed.
- It preserves no default assessment section and no default `Why` section.
- It preserves copyable deliverable blocks before commentary.
- PR notes should call out that users now receive structured learning notes by default and can suppress them with explicit output-only or no-explanation phrasing.
- Rollback is to restore the prior notes-on-request behavior in `skills/editor/SKILL.md`, eval fixtures, and any change-local evidence for this slice.

## Observability

No runtime telemetry is required.

Observable proof is through:

- Baseline evidence recording current learning value from representative prompts.
- Post-change eval evidence showing the learning notes block appears by default.
- Eval cases showing suppression removes the block.
- Eval cases showing ambiguous brevity cues keep focused notes.
- Eval cases showing fidelity, restraint, and no-padding behavior.
- Local validation commands recorded in downstream implementation and verification artifacts.

## Security and privacy

- The skill must not request secrets, credentials, private paths, or unpublished personal data.
- Examples and evals should use fictional or sanitized text.
- Learning notes must not reveal hidden reasoning, private chain-of-thought, or unstated assumptions as facts.
- Learning notes must not encourage deceptive, misleading, false, or high-stakes advisory behavior.
- Integrity-boundary behavior from the existing editor spec remains mandatory.

## Accessibility and UX

- Output must remain readable as plain Markdown.
- Labels must be clear and concise.
- Deliverables must remain copyable without interleaved teaching commentary.
- The learning notes block must be focused and scannable.
- No decorative emoji or nonfunctional formatting is required.
- The skill should avoid dense report-style sections.

## Performance expectations

- The prompt remains a pure Markdown skill and must not add runtime calls or external dependencies.
- The learning notes block should be complete enough to cover the actual useful lessons without a fixed numeric maximum, while remaining scannable through one bullet per lesson and short theme labels for longer or varied note sets.
- No live model calls may be added to CI for this slice.

## Edge cases

EC1. User asks `Only translate this into English` without saying no notes. The skill displays English output and a learning notes block because target-language-only is not the same as no-notes suppression.

EC2. User asks `Only output the translation`. The skill treats this as explicit output-only suppression and omits learning notes.

EC3. User asks `Keep it short`. The skill keeps the learning notes concise but does not suppress them.

EC4. User asks in Chinese `只要译文`. The skill omits learning notes.

EC5. User asks in Chinese `不用解释`. The skill omits learning notes.

EC6. User asks in Chinese to polish English source text. The skill uses Chinese response framing for labels and `学习要点`, while editing the English source as English and preserving meaning.

EC7. User asks in English to polish Chinese source text. The skill uses English response framing and `Learning notes`, while editing the Chinese source as Chinese and preserving meaning.

EC8. Source text has only a typo. The skill fixes it, does not create a multi-note teaching block, and unless explicitly suppressed, produces a `Learning notes` block with exactly one concise fallback note that identifies the correction as trivial and states that there is no broader writing pattern to teach.

EC9. Source text is already strong. The skill preserves the structure and details with minimal changes. Unless explicitly suppressed, it produces a `Learning notes` block with at most one restraint-oriented note. The skill must not create unnecessary edits to generate teachable material.

EC10. A possible lesson is oversimplified. The skill avoids teaching the brittle rule. Unless explicitly suppressed, it produces a `Learning notes` block with exactly one concise fallback note that references the concrete source condition or explains that the choice depends on context.

EC11. User asks for more explanation. The skill may provide a longer learning section, still anchored to concrete edits.

EC12. User asks for misleading approval language. The skill refuses the misleading transformation and may include one note about not implying approval from review intent.

## Non-goals

- Do not redesign the whole `editor` skill.
- Do not make `editor` a standalone writing-coach skill.
- Do not remove or weaken the expert-quality editing standard.
- Do not make teaching more important than the polished or translated deliverable.
- Do not explain every typo, punctuation fix, capitalization change, or mechanical correction.
- Do not produce bilingual learning notes by default.
- Do not add a long assessment, grading section, report section, or default `Why` section.
- Do not add tools, scripts, generated assets, external services, installer behavior, validator behavior, dependencies, or live model CI.
- Do not expand source-language guarantees beyond the current editor source-intake contract.

## Acceptance criteria

AC1. `docs/proposals/2026-06-16-editor-learning-default-optimization.md` is accepted before this spec is relied on downstream.

AC2. `skills/editor/SKILL.md` still keeps `name: editor`, `$ARGUMENTS`, and `## Output Format`.

AC3. `skills/editor/SKILL.md` remains a pure prompt skill without optional tool frontmatter, scripts, generated assets, or runtime dependencies.

AC4. The editor description identifies the skill as an editor and translator that supports learning from edits to shared text, without advertising standalone writing coaching.

AC5. Non-empty, non-suppressed editing and translation requests render a learning notes block after the deliverable. The block is never empty.

AC6. English response framing labels the teaching block `Learning notes`.

AC7. Chinese response framing labels the teaching block `学习要点`.

AC8. Explicit target-language requests still control visible target-language deliverables.

AC9. Explicit target-language requests still include a learning notes block unless explicit suppression is present.

AC10. Explicit suppression phrases remove the learning notes block.

AC11. Ambiguous brevity cues keep a focused learning notes block.

AC12. Substantive learning notes use original-to-revised anchoring or an equivalent concrete reference to the edit or translation choice. Fallback notes for restraint, typo-only, no-substantive-lesson, brittle-rule, or integrity-boundary cases reference the concrete source condition, edit category, or integrity issue and do not become generic self-commentary.

AC13. Learning notes teach reusable principles when a substantive lesson exists. When no substantive lesson exists, the fallback note accurately explains the concrete reason no broader lesson is being taught.

AC14. Learning notes qualify brittle rules or avoid teaching them.

AC15. Learning notes are not limited by a fixed numeric cap, are not padded, and remain scannable when the useful note set is longer or varied.

AC16. Already-good text is minimally edited and receives at most one restraint note.

AC17. Trivial-only fixes do not produce padded explanations or full grammar lessons, and they still render the default learning notes block with exactly one concise fallback note unless the user explicitly suppresses notes.

AC18. Integrity-boundary requests remain truth-preserving and do not use teaching notes to justify misleading output.

AC19. Baseline and post-change evidence compare learning value, bloat, over-editing, and fidelity on the same representative prompts.

AC20. Eval fixtures cover the scenarios listed in R38.

AC21. `python tests/validate_skills.py` passes before implementation handoff.

## Open questions

None.

## Next artifacts

1. `spec-review` result for this spec.
2. Architecture artifact or architecture-review routing decision.
3. Execution plan.
4. `plan-review` result.
5. `specs/editor-learning-default-optimization.test.md`.
6. Baseline evidence before modifying `skills/editor/SKILL.md`.

## Follow-on artifacts

None yet.

## Readiness

Ready for spec-review.
