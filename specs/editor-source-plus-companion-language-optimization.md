# Editor Source Plus Companion Language Optimization

## Status

approved

## Related proposal

- Accepted proposal: `docs/proposals/2026-06-16-editor-source-plus-companion-language-optimization.md`
- Proposal review R1: `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/reviews/proposal-review-r1.md`
- Proposal review R2: `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/reviews/proposal-review-r2.md`
- Proposal review R3: `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/reviews/proposal-review-r3.md`
- Extends: `specs/editor-expert-quality-optimization.md`
- Extends: `specs/editor-learning-default-optimization.md`
- Supersedes conflicting requirements in `specs/editor-expert-quality-optimization.md` that require default Chinese + English visible output, especially R16, R32, and related output-template text.
- Supersedes conflicting requirements in `specs/editor-learning-default-optimization.md` that imply default Chinese + English visible output or no numeric guidance for learning-note count, especially default-output text and R19.

## Goal and context

The `editor` skill should preserve its expert editing philosophy while changing the default visible language contract from hardcoded Chinese + English to polished source language plus one companion language. The companion language defaults to English when the source language is not English. When the source language is English, the skill uses a deterministic fallback companion language so it never returns duplicate English output.

This spec keeps teaching as a default secondary behavior, but simplifies the learning-note contract so it does not dominate the prompt or the user-facing answer. It also consolidates output behavior around one base shape plus modification rules, removes hidden language rendering that users cannot inspect, and moves detailed behavior out of the skill description.

## Glossary

- Editor skill: `skills/editor/SKILL.md`.
- Source text: the artifact supplied through `$ARGUMENTS` that should be edited, polished, rewritten, translated, or rendered.
- Source language: the primary language of the source text. Intentional code-switching and product, API, or domain terms do not by themselves change the primary source language.
- Instruction: the user's direction to the skill, such as `polish this`, `帮我润色`, `translate this`, or `make this sound better`.
- Instruction language: the language of the user's directive words, excluding quoted source text or inline source snippets.
- Clearly non-English instruction language: a non-English language that appears in the user's directive words strongly enough to identify the user's command language. A source-language snippet embedded after an English command does not make the instruction language non-English.
- Response framing language: the language used for labels, notes, refusals, and explanations.
- Companion language: the one additional visible output language besides the source language.
- Visible output languages: the language blocks shown to the user.
- Target language: a language explicitly requested by the user.
- Target-only request: an explicit request to return only target-language deliverable blocks and omit source-language deliverable blocks.
- Learning notes block: the post-deliverable teaching block that appears by default for non-empty, non-suppressed editing and translation requests.
- Explicit note suppression: a direct request for no learning notes or no explanation, such as `no notes`, `just the text`, `only the translation`, `skip the explanation`, `不用解释`, `不要说明`, `只要译文`, or equivalent direct phrasing.
- Integrity boundary: a request to make text misleading, false, deceptive, more certain than warranted, falsely attributed, or materially different from the known source meaning.

## Examples first

Example E1: Chinese source defaults to Chinese + English
Given the user asks `润色这段话：这个方案比较稳，但上线后还是要观察错误率。`
When no target language or note suppression is specified
Then the skill returns a polished Chinese source-language block, an English companion-language block, and concise learning notes after both deliverables.

Example E2: Russian source defaults to Russian + English
Given the user asks `Polish and translate this:` followed by Russian source text
When no target language is specified
Then the skill returns a polished Russian source-language block, an English companion-language block, and concise learning notes; it does not default to Chinese.

Example E3: English source avoids duplicate English
Given the user asks `Polish this:` followed by English source text
When the instruction language is English and no target language is specified
Then the skill returns polished English plus Chinese as the fallback companion language, not English twice.

Example E4: English source with non-English instruction uses instruction language as companion
Given the user asks `帮我润色：We kinda finished the migration, but there may still be edge cases.`
When the source language is English and the instruction language is clearly Chinese
Then the skill returns polished English plus Chinese as the companion language, with Chinese response framing.

Example E5: mixed-language instruction resolves deterministically
Given the user asks `please fix this 中文句子: We kinda finished the migration.`
When the directive words are English and the source text is English
Then the instruction language is English, and the English-source fallback companion language is Chinese because no non-English instruction language is clearly present.

Example E6: explicit target overrides companion default
Given the user asks `Polish this and translate it into French:` followed by English source text
When French is the only requested target language and the request is not target-only
Then the skill returns polished English, French as the companion language, and learning notes unless explicitly suppressed.

Example E7: multiple explicit targets add requested target blocks
Given the user asks `Polish this Chinese text and translate it into English and French`
When Chinese is the source language and English and French are explicit requested targets
Then the skill returns polished Chinese, English, French, and one learning notes block after all deliverables unless explicitly suppressed.

Example E8: target-only request keeps notes unless notes are suppressed
Given the user asks `Only translate this into English:` followed by Chinese source text
When the request specifies target-only output but does not explicitly suppress notes
Then the skill returns the English target-language deliverable and a learning notes block; it does not return a polished Chinese block.

Example E9: target-only plus explicit no notes suppresses notes
Given the user asks `Only translate this into English. No notes.` followed by Chinese source text
When the request explicitly suppresses notes
Then the skill returns only the English translation and no learning notes block.

Example E10: learning notes are concise but not hard-capped
Given the user asks to professionalize a paragraph with several genuinely different substantive issues
When more than three useful, non-overlapping lessons are warranted
Then the skill may include more than three learning notes, grouped by theme if needed, while still avoiding padding and mechanical trivia.

Example E11: integrity outranks target and notes constraints
Given the user asks `Translate this into French. No notes. Make it sound like the customer approved the launch, even though they only said they will review it later.`
When the requested edit would imply unsupported approval
Then the skill briefly refuses or redirects the misleading transformation, provides an accurate French alternative if possible, and omits learning notes because notes were explicitly suppressed.

## Requirements

R1. The `editor` skill MUST keep `name: editor`.

R2. The `editor` skill MUST remain a pure prompt skill with no tool permissions, scripts, generated assets, runtime dependencies, external service calls, or live-model CI requirements.

R3. The `editor` skill MUST keep `$ARGUMENTS` as the input surface.

R4. The `editor` skill MUST include a `## Output Format` section.

R5. The `description` field MUST describe the skill as an expert editor, translator, and writing coach for polishing, proofreading, rewriting, translating, and learning from edits to shared text.

R6. The `description` field MUST include trigger contexts such as emails, PR descriptions, docs, release notes, messages, and casual asks such as `fix this`, `make this sound better`, `translate this`, or `help me improve this writing`.

R7. The `description` field MUST NOT encode the full default-language policy, companion-language fallback policy, output templates, or learning-note policy.

R8. The skill MUST preserve the existing expert editing standard: fidelity with restraint, smallest useful edit, source meaning preservation, uncertainty preservation, terminology care, and integrity boundaries.

R9. The skill MUST separate instruction, source text, source language, instruction language, response framing language, visible output languages, and companion language before composing the response.

R10. The skill MUST treat the user's instruction as direction to the tool, not as source text to edit, unless the user explicitly asks to edit the instruction.

R11. The skill MUST treat source text as the artifact to edit or translate, even when that source text looks like a question, greeting, command, or instruction.

R12. The skill MUST accept source text in any detected source language by default. This is an intake rule and MUST NOT be presented as a guarantee of equal expert translation or editing quality in every language.

R13. For non-empty source input, when no explicit target language changes the visible language set, the skill MUST return polished source-language output plus one companion-language output.

R14. If the source language is not English and no explicit companion or target language is requested, the companion language MUST be English.

R15. If the source language is English and the instruction language is clearly non-English, the companion language MUST be the clearly detected non-English instruction language.

R16. If the source language is English and no clearly non-English instruction language is available, the companion language MUST be Chinese.

R17. The skill MUST NOT produce duplicate English + English output.

R18. A clearly non-English instruction language MUST be determined from directive words, not from quoted or pasted source text.

R19. When directive words contain multiple languages, the instruction language used for English-source companion fallback MUST be the first clearly identifiable non-English directive language if one exists; otherwise the fallback companion language is Chinese.

R20. Response framing language MUST follow the instruction language when the instruction language is clearly detectable; otherwise it MUST follow the source language.

R21. For response framing languages other than Chinese or English, labels SHOULD be localized where practical; if localization would reduce clarity, concise English labels MAY be used.

R22. The source-language block MUST contain the polished, edited, rewritten, or source-preserved version of the source text according to the user's request.

R23. The companion-language block MUST translate the same resolved meaning as the source-language block.

R24. The skill MUST edit source text in its source language before translating the resolved meaning into the companion language.

R25. The skill MUST resolve source meaning once, then render all visible output-language blocks from that resolved meaning.

R26. The skill MUST verify before returning that all visible output-language blocks preserve the same facts, names, numbers, technical terms, uncertainty, commitments, logic, intent, tone, and formatting intent.

R27. The skill MUST NOT require hidden Chinese + English rendering as a cross-check for visible single-target requests.

R28. The default base output shape MUST be:

```markdown
**<Source language label>**
<polished source-language version>

**<Companion language label>**
<companion-language version>

**<Learning notes label>**
- `<original>` -> `<revised>`: <reusable principle>.
```

R29. Labels MUST be in the response framing language where practical.

R30. The output MUST be copyable Markdown-compatible plain text with bold labels, deliverable content on its own line or block, no emoji, and no decorative symbols.

R31. If the user explicitly requests one target language and does not request target-only output, the skill MUST return the polished source-language block plus the requested target-language block.

R32. If the user explicitly requests multiple target languages and does not request target-only output, the skill MUST return the polished source-language block plus one block for each requested target language.

R33. If an explicit target language is the same as the source language, the skill MUST NOT duplicate that language block.

R34. If the user clearly requests target-only output, the skill MUST omit the source-language deliverable block and return only the requested target-language block or blocks, subject to integrity.

R35. A target-only request MUST NOT suppress learning notes by itself.

R36. A target-only request MUST suppress learning notes only when it also contains explicit note suppression, such as `no notes`, `just the text`, `only the translation`, `skip the explanation`, `不用解释`, `不要说明`, `只要译文`, or equivalent direct phrasing.

R37. Translation-only requests MUST preserve source meaning and tone and MUST NOT introduce unnecessary source-language rewriting.

R38. Learning notes MUST appear by default after all visible deliverable blocks for every non-empty, non-suppressed editing, rewriting, polishing, professionalizing, or translation request.

R39. Learning notes MUST use the response framing language.

R40. Substantive learning notes MUST use concrete original-to-revised anchoring or an equivalent concrete reference to the edit or translation choice.

R41. Learning notes MUST explain reusable writing, editing, or translation principles rather than merely reporting that an edit happened.

R42. The skill MUST NOT invent edits, exaggerate lessons, or alter meaning to create learning notes.

R43. The skill MUST skip trivial mechanical fixes as full lessons unless they reveal a recurring pattern.

R44. For trivial-only, already-clear, no-substantive-lesson, brittle-rule, or integrity-boundary cases, the skill MUST use exactly one concise fallback learning note unless notes are explicitly suppressed.

R45. The default fallback learning-note pattern SHOULD be equivalent to: `The original was already clear or only needed a mechanical correction, so there is no broader writing pattern to teach.`

R46. The skill SHOULD keep learning notes concise and usually no more than three notes.

R47. The skill MAY include more than three learning notes when the source text warrants more than three genuinely distinct, useful, substantive lessons.

R48. Longer or varied learning-note sets SHOULD be grouped by short theme labels inside one learning notes block.

R49. Explicit note suppression MUST remove the learning notes block.

R50. Ambiguous brevity cues such as `keep it short`, `I'm in a hurry`, or `just need this quickly` MUST NOT suppress learning notes by themselves.

R51. The skill MUST apply this conflict hierarchy when rules compete: integrity and truthfulness, explicit user constraints, fidelity to source meaning, core polish/translate deliverable, teaching, then brevity.

R52. Integrity and truthfulness MUST prevent the skill from making text misleading, false, deceptive, more certain than supported, falsely attributed, or materially inconsistent with known source meaning.

R53. Explicit user constraints MUST be honored unless they conflict with integrity or source-meaning fidelity.

R54. For integrity-boundary requests, the skill MUST briefly refuse or redirect the misleading transformation in the response framing language and provide an accurate alternative when possible.

R55. For integrity-boundary requests with explicit target languages, accurate alternatives MUST use the requested target language or languages when possible.

R56. For integrity-boundary requests with explicit note suppression, the skill MUST omit learning notes.

R57. The optimized prompt SHOULD be shorter than the pre-change `skills/editor/SKILL.md`; if it is not shorter, implementation evidence MUST justify why the length increase is necessary.

R58. The optimized prompt MUST stay under 500 lines.

R59. The implementation MUST update or replace editor prompt text that says the default visible target set is Chinese + English.

R60. The implementation MUST remove or replace editor prompt text that requires internal Chinese + English rendering as an invisible cross-check.

R61. The implementation MUST remove or compress repeated fallback-note categories and fully enumerated output templates where the base template plus modification rules cover the behavior.

R62. The implementation MUST NOT add repository-wide validator changes for this slice.

R63. The implementation MUST NOT add live model calls to CI.

R64. Eval evidence MUST cover Chinese source defaulting to Chinese + English, Russian source defaulting to Russian + English, English source avoiding duplicate English, explicit target override, target-only output, compact learning notes, trivial correction without over-teaching, and integrity priority.

R65. Eval evidence MUST also cover a three-way conflict: integrity issue + explicit target language + explicit note suppression.

R66. Baseline evidence MUST be recorded before editing `skills/editor/SKILL.md`.

R67. Post-change evidence MUST compare behavior against the same scenario classes used for baseline evidence.

## Inputs and outputs

Inputs:

- `$ARGUMENTS` containing user instruction, source text, and any explicit target language, target-only, note suppression, tone, audience, or formatting request.

Outputs:

- Markdown-compatible plain text only.
- Visible source-language and companion-language deliverable blocks by default.
- Explicit target-language blocks when requested.
- One learning notes block after visible deliverables unless explicitly suppressed.
- A refusal or correction before alternatives when integrity requires it.
- No generated files, tool output, external service output, or hidden runtime artifacts.

Default output:

```markdown
**<Source language label>**
<polished source-language version>

**<Companion language label>**
<companion-language version>

**<Learning notes label>**
- `<original>` -> `<revised>`: <reusable principle>.
```

Target-only output with notes:

```markdown
**<Target language label>**
<target-language version>

**<Learning notes label>**
- `<original>` -> `<revised>`: <reusable principle>.
```

Target-only output with notes suppressed:

```markdown
**<Target language label>**
<target-language version>
```

Multiple explicit targets:

```markdown
**<Source language label>**
<polished source-language version>

**<Target language label>**
<target-language version>

**<Target language label>**
<target-language version>

**<Learning notes label>**
- `<original>` -> `<revised>`: <reusable principle>.
```

Integrity-boundary output:

```markdown
<brief refusal or correction in response framing language>

**<Target or companion language label>**
<accurate alternative>

**<Learning notes label>**
- <one concise fallback note if notes are not suppressed>
```

## State and invariants

- `editor` remains an existing skill named `editor`.
- `editor` remains a pure Markdown prompt skill.
- `$ARGUMENTS` remains the runtime input surface.
- The skill remains a general writing, editing, translation, and learning skill rather than becoming domain-specific.
- Source-language editing precedes translation.
- Visible language blocks preserve one resolved source meaning.
- The default visible output is source language plus one companion language.
- English is the default companion for non-English source text.
- Chinese is the deterministic fallback companion for English source text when no clearly non-English instruction language is available.
- Learning notes are default-on and secondary to the deliverable.
- Integrity outranks explicit user constraints, fidelity, teaching, and brevity.
- No persistent user language preference or configuration state is introduced.

## Error and boundary behavior

- Empty input: the skill should ask for source text to edit or translate and should not include learning notes.
- No source artifact: the skill should ask for text to edit or translate rather than acting as a broad writing coach without a source.
- Uncertain source language: the skill should choose the most likely source language, preserve ambiguity, and avoid unsupported claims about language quality.
- Non-English source language outside common test coverage: the skill should still attempt source-language polish plus English companion translation, while avoiding claims of guaranteed expert quality across all languages.
- Mixed-language source: the skill should preserve intentional code-switching, product names, API names, technical terms, and domain terms unless the user asks to localize them or they are clearly wrong.
- Mixed-language instruction: directive words determine instruction language; embedded source text does not.
- Explicit target equals source language: the skill should avoid duplicate language blocks.
- Explicit target language conflicts with integrity: integrity wins.
- Target-only request without note suppression: source-language deliverable is omitted, learning notes remain.
- Target-only request with note suppression: source-language deliverable and learning notes are omitted.
- Trivial-only correction: the skill should correct the issue and use at most one fallback note unless notes are suppressed.
- Already-clear text: the skill should make minimal changes and use at most one restraint note unless notes are suppressed.
- Unsupported misleading transformation: the skill refuses or redirects and offers accurate alternatives when possible.

## Compatibility and migration

This spec deliberately changes the `editor` output contract:

- It replaces default Chinese + English visible output with source language + one companion language.
- It preserves Chinese + English output for Chinese source text and for English source text with no non-English instruction language, but by different resolution rules.
- It preserves default learning notes while simplifying note rules and softening note-count guidance.
- It preserves explicit target-language overrides.
- It preserves target-only output while clarifying that target-only does not suppress learning notes unless note suppression is explicit.
- It removes hidden Chinese + English cross-check rendering from the prompt contract.
- It keeps skill installation, skill name, validator behavior, and CI behavior unchanged.
- PR notes should call out the visible output-language default change and the English-source fallback behavior.
- Rollback is limited to reverting `skills/editor/SKILL.md`, editor eval fixture changes, this spec, and change-local evidence for this slice.

## Observability

- Baseline evidence MUST record current prompt behavior before implementation.
- Post-change evidence MUST record optimized prompt behavior after implementation.
- Eval cases in `tests/evals/skills/editor/cases.yaml` MUST make expected behavior observable to reviewers.
- Evidence MUST identify visible language blocks, learning-note behavior, source fidelity, explicit-target handling, target-only handling, and integrity behavior.
- Prompt length before and after implementation MUST be reported.
- Validation output from `python tests/validate_skills.py` MUST be recorded in downstream implementation or verification artifacts.
- `git diff --check` SHOULD be run before handoff.

## Security and privacy

- Eval prompts and examples MUST use fictional or sanitized content.
- The optimized skill MUST NOT ask for secrets, credentials, private local paths, unpublished personal data, or real customer-sensitive details.
- Learning notes MUST NOT reveal private chain-of-thought or unsupported assumptions as facts.
- Integrity behavior MUST prevent assistance with falsified approvals, consent, authorship, certainty, claims, or material facts.
- This change MUST NOT alter medical, legal, financial, security, or other high-stakes skill behavior.

## Accessibility and UX

- No interactive UI is introduced.
- Output MUST remain readable in plain Markdown.
- Labels MUST be concise and scannable.
- Deliverable content MUST remain copyable without interleaved commentary.
- Learning notes MUST appear after deliverables, not inside deliverable blocks.
- No emoji or decorative symbols are required.

## Performance expectations

- The optimized `skills/editor/SKILL.md` MUST remain under 500 lines.
- The optimized prompt SHOULD be shorter than the pre-change prompt or justify any length increase.
- Local validation MUST remain deterministic.
- CI MUST NOT require network access or live model calls for this change.

## Architecture impact

No canonical architecture update is required.

This change is limited to the authored `editor` prompt contract, editor eval evidence, and local validation evidence. It does not change repository boundaries, runtime flow, generated-output flow, persistence, APIs, deployment, packaging, adapters, CI architecture, security boundaries, or durable architecture decisions.

## Edge cases

EC1. Chinese source with Chinese instruction defaults to polished Chinese plus English companion output.

EC2. Chinese source with English instruction defaults to polished Chinese plus English companion output and uses English response framing.

EC3. Russian source with English instruction defaults to polished Russian plus English companion output and does not add Chinese.

EC4. Spanish source with no explicit target defaults to polished Spanish plus English companion output, with best-effort quality caveat preserved by the prompt contract.

EC5. English source with English instruction defaults to polished English plus Chinese companion output.

EC6. English source with Chinese instruction defaults to polished English plus Chinese companion output and uses Chinese response framing.

EC7. English source with mixed directive words uses the first clearly identifiable non-English directive language as companion if present; otherwise it uses Chinese.

EC8. Explicit French target on English source returns polished English plus French unless target-only output is requested.

EC9. Explicit English and French targets on Chinese source returns polished Chinese plus English and French, with one learning notes block after all deliverables.

EC10. `Only translate this into English` returns only English deliverable plus learning notes unless notes are explicitly suppressed.

EC11. `Only translate this into English. No notes.` returns only English deliverable and no learning notes.

EC12. Explicit target equals source language does not duplicate the source-language block.

EC13. Trivial typo correction does not create padded grammar teaching.

EC14. Already-clear text receives minimal editing and at most one restraint-oriented learning note.

EC15. Long source with several distinct lessons may produce more than three notes when warranted and should group varied notes by theme.

EC16. Integrity request with explicit target language and no notes refuses or redirects the misleading edit, provides an accurate alternative in the requested target language when possible, and omits learning notes.

## Non-goals

1. Do not weaken expert editing, fidelity, restraint, meaning preservation, uncertainty preservation, terminology care, or integrity boundaries.
2. Do not remove learning notes.
3. Do not make teaching the primary output.
4. Do not reintroduce a long assessment, report, or default `Why` section.
5. Do not enumerate every possible output template in `skills/editor/SKILL.md`.
6. Do not add scripts, generated assets, runtime dependencies, external services, or live-model CI.
7. Do not change repository-wide validation behavior.
8. Do not optimize any skill other than `editor`.
9. Do not add user-profile storage, persistent language preferences, or configurable companion-language files.
10. Do not guarantee expert translation quality in every possible language.

## Acceptance criteria

AC1. The spec exists at `specs/editor-source-plus-companion-language-optimization.md` and includes all required spec sections.

AC2. `skills/editor/SKILL.md` defaults to polished source language plus one companion language.

AC3. Non-English source text defaults to English companion output unless the user explicitly requests another target language.

AC4. English source text never returns duplicate English output.

AC5. English source text with no clearly non-English instruction language uses Chinese as the companion language.

AC6. English source text with clearly non-English instruction language uses that instruction language as the companion language.

AC7. Explicit single-target requests override the companion default.

AC8. Explicit multi-target requests return one block for each requested target language and do not add unrelated language blocks.

AC9. Target-only requests omit source-language output.

AC10. Target-only requests include learning notes unless notes are explicitly suppressed.

AC11. Explicit note suppression removes learning notes.

AC12. Learning notes appear by default after all visible deliverables for non-empty, non-suppressed editing and translation requests.

AC13. Learning notes remain concise, avoid padding, and are usually no more than three unless the source warrants more.

AC14. Trivial-only and already-clear cases include at most one fallback learning note unless notes are suppressed.

AC15. Integrity-boundary requests refuse or redirect misleading transformations and provide accurate alternatives when possible.

AC16. The complex conflict eval covers integrity issue + explicit target language + explicit note suppression.

AC17. The optimized prompt removes hidden Chinese + English cross-check rendering.

AC18. The optimized prompt description focuses on trigger criteria and does not encode the full output policy.

AC19. `python tests/validate_skills.py` passes after implementation, with warnings reviewed.

AC20. `git diff --check` passes after implementation.

## Open questions

None.

## Next artifacts

1. Execution plan.
2. `plan-review` result.
3. `specs/editor-source-plus-companion-language-optimization.test.md`.
4. Baseline evidence before modifying `skills/editor/SKILL.md`.

## Follow-on artifacts

- `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/reviews/spec-review-r1.md`
- `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/reviews/spec-review-r2.md`
- `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/review-log.md`

## Readiness

Approved and ready for execution planning.

This spec is not plan-ready, implementation-ready, verified, branch-ready, or PR-ready until downstream lifecycle artifacts are completed in order.
