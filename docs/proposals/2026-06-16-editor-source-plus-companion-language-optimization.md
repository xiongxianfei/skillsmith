# Proposal: Source-language plus companion-language optimization of the `editor` skill

## Status

accepted

## Problem

The `editor` skill's core editing philosophy is strong: fidelity with restraint, meaning preservation, and resolving meaning once before rendering target-language versions should remain the center of the skill.

The main issue is not the editing philosophy. The issue is weight distribution and default-language behavior.

The current direction has accumulated too much support logic around learning notes, fallback note cases, and output templates. Learning is important, but the learning-note rules now risk consuming as much prompt budget as the core editing mission. Similarly, fully spelling out every output permutation makes the skill heavier than necessary and increases the chance that the model spends attention assembling templates rather than editing well.

There is also a default-language mismatch. The prior default of always producing Chinese + English is useful for a bilingual workflow, but it is less general than the new desired behavior:

```text
source language + one additional language
```

That default better matches the skill's role as an editor and translator: first polish the text in its original language, then provide one companion translation. It also avoids treating Chinese + English as a hardcoded universal pair when the source text is neither Chinese nor English.

This proposal therefore optimizes `editor` around four priorities:

1. keep the editing philosophy;
2. change the default visible language contract to source language + one companion language;
3. keep learning as a default secondary feature, but drastically simplify it;
4. reduce prompt weight by deduplicating rules and replacing many templates with one base template plus modification rules.

External skill guidance is directionally consistent with this change: Anthropic's skill docs describe skill metadata as the discovery surface, recommend descriptions that explain what the skill does and when to use it, and emphasize concise skill bodies plus progressive disclosure when details are large or conditional. See [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) and [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).

## Goals

1. Preserve the core `editor` philosophy: fidelity with restraint, smallest useful edit, no meaning drift, no unsupported certainty, and resolving meaning once before rendering visible versions.
2. Change the default visible output contract to polished source language + one companion language.
3. Make English the default companion language when the source language is not English.
4. Avoid duplicate English + English output when the source language is English by defining a deterministic companion-language fallback.
5. Keep learning as a default secondary behavior, but reduce the learning-note specification to a compact rule set: default-on, suppressible, anchored `original` -> `revised` format, one fallback note pattern, no over-editing to create lessons, and a default cap of three notes.
6. Replace many output templates with one base template and a few modification rules.
7. Drop hidden cross-check work that asks the model to internally render languages the user cannot inspect.
8. Deduplicate repeated constraints between `Non-negotiables`, `Workflow`, and `Output Format`.
9. Sharpen the `description` so it focuses on skill selection triggers rather than implementation details.
10. Add a conflict-resolution hierarchy so competing rules are resolved predictably.

## Non-goals

1. Do not weaken fidelity, restraint, or meaning preservation.
2. Do not remove learning notes entirely.
3. Do not make teaching the first target. The first target remains polish and translate.
4. Do not reintroduce a long assessment or stage report.
5. Do not generate every possible template permutation in `SKILL.md`.
6. Do not add scripts, tools, or live-model CI.
7. Do not optimize every Skillsmith skill in this slice.
8. Do not solve user-profile or long-term language-preference storage in this proposal.
9. Do not guarantee expert translation quality in every possible language. The source-language intake may be broad, but acceptance evidence should stay bounded.

## Vision fit

fits the current vision

This proposal keeps `editor` as a reusable, reviewable, portable Markdown skill. It improves the skill by reducing prompt overhead while preserving expert-quality editing and making default language behavior more general.

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
|---|---|---|
| Generate a proposal | in scope | Entire artifact |
| Follow best practices | in scope | Problem, Context, Recommended Direction, Testing and Verification Strategy |
| Default to source language + one additional language | in scope | Goals, Default Language Contract |
| Additional language defaults to English | in scope | Goals, Default Language Contract |
| Preserve strong editing philosophy | in scope | Goals, Recommended Direction |
| Optimize token footprint | in scope | Problem, Goals, Risks and Mitigations |
| Reduce learning-note weight | in scope | Goals, Learning Notes Simplification |
| Reduce template proliferation | in scope | Goals, Output Contract |
| Drop invisible cross-check overhead | in scope | Goals, Recommended Direction |
| Deduplicate repeated rules | in scope | Goals, Recommended Direction |
| Sharpen description | in scope | Goals, Description Strategy |
| Add conflict-resolution hierarchy | in scope | Goals, Conflict Resolution Hierarchy |
| Keep teaching as important default behavior | in scope | Goals, Learning Notes Simplification |

## Scope budget

| Work item | Treatment | Reason |
|---|---|---|
| Default language contract change | core to this proposal | This is the main requested behavior change. |
| Source-language polished output | core to this proposal | The first target is to polish the text. |
| One companion-language output | core to this proposal | The first target also includes translation. |
| English as default companion language | core to this proposal | Explicit user preference. |
| English-source fallback companion rule | core to this proposal | Needed to avoid duplicate English output. |
| Learning-note simplification | core to this proposal | Teaching remains important, but current rule weight is too high. |
| Template consolidation | core to this proposal | Reduces prompt bloat and assembly ambiguity. |
| Remove hidden bilingual cross-check | core to this proposal | Invisible work is unverifiable overhead. |
| Description cleanup | core to this proposal | Description should aid triggering, not encode output policy. |
| Conflict hierarchy | core to this proposal | Prevents competing rules from being resolved ad hoc. |
| Repository-wide validator changes | out of scope | This is a skill behavior and prompt optimization. |
| Live model CI | out of scope | Keep validation deterministic and lightweight. |
| User preference storage | deferable follow-up | Useful later, but not needed for this prompt-level default. |

## Context

The current `editor` skill is built on two accepted directions:

- `docs/proposals/2026-05-26-editor-expert-quality-optimization.md` established expert editing around fidelity with restraint, language-role separation, source-language editing before rendering, default Chinese + English output, and bilingual cross-checking.
- `docs/proposals/2026-06-16-editor-learning-default-optimization.md` changed teaching from opt-in to default-on, while preserving the deliverable-first contract and suppressible learning notes.

The current `skills/editor/SKILL.md` reflects those directions. Its description says it defaults to Chinese + English final output with structured learning notes. Its workflow defaults visible targets to Chinese + English, asks for internal Chinese + English rendering as a fidelity cross-check for single-target requests, and contains multiple learning-note fallback patterns plus multiple fully written output templates.

This proposal keeps the expert editing and default teaching intent, but changes the default visible language contract and reduces support-rule weight.

External skill-authoring guidance also supports putting selection criteria in metadata and execution details in the body. The better first move for this change is not adding progressive disclosure files; it is simplifying the main skill because the default behavior itself should be compact enough to load every time the skill triggers.

## Default Language Contract

### Definitions

| Term | Meaning |
|---|---|
| Source language | The primary language of the text being edited. |
| Instruction language | The language of the user's command, such as `polish this` or `帮我润色`. |
| Response framing language | The language used for labels, notes, refusals, and explanations. |
| Companion language | The one additional visible output language besides the source language. |
| Visible output languages | The final languages shown to the user. |

### Default rule

The optimized `editor` skill should default to:

```text
source language + companion language
```

The source-language version is the polished, edited, or rewritten version of the original text. The companion-language version is a translation of the same resolved meaning.

### Companion-language resolution

The companion language should be resolved in this order:

1. If the user explicitly requests an additional target language, use that language.
2. Otherwise, if the source language is not English, use English as the companion language.
3. Otherwise, if the source language is English and the instruction language is clearly non-English, use the instruction language as the companion language.
4. Otherwise, if the source language is English and no non-English instruction language is available, use the project-local fallback companion language.

Proposal-level fallback:

```text
Chinese
```

English cannot be the additional language when the source is already English. A deterministic fallback prevents duplicate output. Chinese is the least disruptive fallback because the existing editor direction has already used Chinese + English as a default pair.

The downstream spec may later rename this to a configurable `default_companion_language`, but this proposal should not introduce preference storage or configuration files.

## Learning Notes Simplification

Learning remains default, but the rule set should be much lighter.

Keep only these learning-note rules in the main `SKILL.md`:

1. Include learning notes by default unless explicitly suppressed.
2. Place learning notes after the deliverable.
3. Use the response framing language for notes.
4. Anchor substantive notes as `` `original` -> `revised`: reusable principle. ``
5. Explain the principle, not just the edit.
6. Skip trivial mechanical fixes unless there is a recurring pattern.
7. Use one short fallback note when there is no substantive lesson.
8. Do not invent edits to create lessons.
9. Cap notes at three by default.

Remove or compress:

- multiple fallback-note categories;
- separate fallback templates;
- long lists of allowed and disallowed note types;
- repeated statements of "do not pad";
- repeated statements of "notes are after the deliverable";
- multiple versions of nearly identical templates.

Default fallback note pattern:

```text
The original was already clear or only needed a mechanical correction, so there is no broader writing pattern to teach.
```

The skill can adapt that sentence to the response framing language.

## Output Contract

Use one base template:

```markdown
**<Source language label>**
<polished source-language version>

**<Companion language label>**
<companion-language version>

**<Learning notes label>**
- `<original>` -> `<revised>`: <reusable principle>.
```

Instead of enumerating every template, use these modification rules:

1. Explicit suppression: if the user asks for no notes, drop the learning-notes block.
2. Explicit target language: if the user explicitly requests a target language, use that as the companion language unless the user requests target-only output.
3. Target-only request: if the user says "only translate to X" or equivalent, return only the requested target-language output unless the skill's local policy requires source preservation.
4. Non-edit translation request: if the user asks only to translate, preserve meaning and tone; do not add unnecessary source-language rewriting.
5. Integrity issue: prepend a one-line refusal or correction, then provide an accurate alternative if possible.
6. Already-clear text: keep the edit minimal and include at most one learning note.
7. Trivial correction: avoid a padded learning block; use either no note if suppressed or one short fallback note if not suppressed.
8. Long source: group learning notes by theme if needed, still capped.

This keeps the output contract testable without requiring six or seven fully written templates.

## Conflict Resolution Hierarchy

When rules compete, apply this hierarchy:

1. Integrity and truthfulness: do not make the text misleading, false, more certain than supported, or falsely attributed.
2. Explicit user constraints: honor explicit target languages, "no notes," "only translate," tone, audience, and format requests unless they conflict with integrity.
3. Fidelity to source meaning: preserve facts, names, numbers, technical terms, uncertainty, commitments, logic, and intent.
4. Core deliverable: polish and translate according to the source + companion-language contract.
5. Teaching: include learning notes by default, but do not let teaching cause over-editing, bloat, or meaning drift.
6. Brevity: prefer the smallest output that satisfies the higher-priority rules.

This hierarchy is important because the skill otherwise has competing defaults: be concise, teach by default, respect target languages, preserve source meaning, and refuse misleading edits.

## Description Strategy

The description should focus on when to trigger, not detailed output rules.

Suggested direction:

```yaml
description: >
  Expert editor, translator, and writing coach for polishing, proofreading,
  rewriting, translating, and learning from edits to shared text. Use for emails,
  PR descriptions, docs, release notes, messages, and asks like "fix this",
  "make this sound better", "translate this", or "help me improve this writing".
```

The full default-language policy and learning-note policy should stay in the body. Those details are execution behavior, not trigger criteria.

## Options Considered

### Option 1: Keep hardcoded Chinese + English default

This preserves the current bilingual workflow, but it is over-fitted. It does not generalize well when the source language is neither Chinese nor English, and it treats English source text as a special case without a clear companion-language rule.

Disposition: rejected.

### Option 2: Source language only by default

This is concise and avoids duplicate language output, but it weakens the translation role. The user explicitly wants polish and translate as the first target.

Disposition: rejected.

### Option 3: Source language + one companion language

This preserves the source edit, adds translation, and generalizes better. English remains the default companion language for non-English sources.

Disposition: recommended.

### Option 4: Keep all current learning-note and template detail

This maximizes explicitness but overweights support behavior relative to editing. It also increases context cost and makes the prompt harder to maintain.

Disposition: rejected.

### Option 5: Move all learning rules to a reference file

This could reduce `SKILL.md` length, but it may be unnecessary for this slice. Since teaching is default, the model needs the core learning-note rules every time. A compact in-body rule set is better than hiding required behavior in a reference file.

Disposition: rejected for now.

## Recommended Direction

Adopt Option 3: source language + one companion language, combined with prompt simplification.

The revised `editor` skill should be organized roughly as:

```markdown
# Editor

## Core standard
Fidelity with restraint.

## Priority order
Integrity > explicit user constraints > source fidelity > polish/translate deliverable > teaching > brevity.

## Language defaults
Return the polished source language plus one companion language.
Use English as companion unless the source is English; then use instruction language if non-English, otherwise Chinese.

## Workflow
1. Identify instruction, source language, response framing language, and companion language.
2. Check integrity and user constraints.
3. Edit the source in its own language with fidelity and restraint.
4. Translate the resolved meaning into the companion language.
5. Verify visible versions preserve the same meaning and tone.
6. Add concise learning notes unless suppressed.

## Output Format
Use the base template plus modification rules.
```

The revised skill should remove:

- hidden internal Chinese + English cross-checks;
- repeated language-verification rules;
- repeated non-negotiables that duplicate workflow steps;
- most fallback-note variants;
- fully enumerated output templates for every case.

## Expected Behavior Changes

1. A Chinese source text defaults to polished Chinese + English translation.
2. A Russian source text defaults to polished Russian + English translation.
3. A Spanish source text defaults to polished Spanish + English translation, subject to model capability and no guarantee of equal expert quality across all languages.
4. An English source text does not return English twice. It returns polished English + the resolved fallback companion language.
5. Explicit target-language requests override the default companion language.
6. "Only translate to English" or equivalent can suppress source-language output if the user clearly asks for target-only output.
7. Learning notes still appear by default, but the rule set is compact and notes are capped.
8. The skill no longer asks the model to perform hidden language renderings that are not visible to the user.
9. The description becomes easier to scan and more trigger-focused.

## Architecture Impact

No runtime architecture changes are expected.

Expected touched areas include:

```text
docs/proposals/2026-06-16-editor-source-plus-companion-language-optimization.md
specs/editor-source-plus-companion-language-optimization.md
docs/plans/2026-06-16-editor-source-plus-companion-language-optimization.md
specs/editor-source-plus-companion-language-optimization.test.md
tests/evals/skills/editor/cases.yaml
skills/editor/SKILL.md
editor-workflow.mmd
docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/
```

No scripts, tools, generated artifacts, or live model CI are expected. No repository-wide validator changes are expected.

## Testing and Verification Strategy

Before editing `skills/editor/SKILL.md`, run representative prompts against the current skill and record:

- current output languages;
- whether English source duplicates English output;
- whether learning notes dominate the answer;
- whether visible output includes unnecessary templates;
- whether hidden-cross-check language exists in the prompt;
- whether prompt length is reduced after revision.

Required eval scenarios:

| Scenario | Expected behavior |
|---|---|
| Chinese source defaults to Chinese + English | Produces polished Chinese source-language output, English companion-language output, cautious uncertainty preservation, concise learning notes unless suppressed, and no extra language blocks. |
| Russian source defaults to Russian + English | Produces polished Russian source-language output, English companion-language output, preserved meaning and cautious tone, no Chinese default, and concise learning notes unless suppressed. |
| English source avoids duplicate English | Produces polished English output, no duplicate English companion block, configured fallback companion language, preserved uncertainty, and concise learning notes unless suppressed. |
| Explicit target overrides companion default | Produces polished source-language output, uses the requested target such as French instead of default English, preserves details such as 24-hour monitoring, and does not add unrelated language blocks. |
| Target-only request | Produces only the requested target translation, omits source-language output, omits learning notes when requested, and preserves cautious uncertainty. |
| Learning notes remain default but compact | Produces source-language plus companion-language output, includes concise learning notes by default, anchors substantive notes with concrete `original` -> `revised` references, and avoids a long report. |
| Trivial correction does not over-teach | Corrects the typo, produces source-language plus companion-language output, avoids padded grammar lessons, and includes at most one short fallback learning note unless suppressed. |
| Integrity outranks user instruction | Does not imply approval or unsupported facts, briefly refuses or redirects the misleading transformation, offers an accurate alternative, and does not let polish, translation, or teaching override integrity. |

Minimum validation:

```bash
python tests/validate_skills.py
python -m unittest discover tests
git diff --check
```

Run only if present in the branch:

```bash
python tests/check_readme_sync.py
```

No live model calls should be added to CI.

## Rollout and Rollback

Rollout:

1. Accept this proposal after proposal review.
2. Write `specs/editor-source-plus-companion-language-optimization.md`.
3. Run `spec-review`.
4. Write an execution plan.
5. Run `plan-review`.
6. Write `specs/editor-source-plus-companion-language-optimization.test.md`.
7. Capture baseline behavior before editing.
8. Edit `skills/editor/SKILL.md`.
9. Update `editor-workflow.mmd` if it remains part of the change.
10. Add or update `tests/evals/skills/editor/cases.yaml`.
11. Run validation.
12. Send through code review and verification.

Rollback is straightforward:

```text
revert skills/editor/SKILL.md
revert editor-workflow.mmd if changed
revert tests/evals/skills/editor/cases.yaml changes
```

No installer, runtime, tool, or CI changes should be affected.

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| English-source output has no meaningful default companion language. | Use deterministic fallback: instruction language if non-English, otherwise Chinese. |
| Source-language intake overclaims quality for all languages. | Treat broad source intake as best-effort; acceptance tests cover representative languages only. |
| Learning notes still dominate the prompt. | Reduce learning-note rules to default-on, suppressible, anchoring, one fallback, cap, and no over-editing. |
| Template simplification causes inconsistent output. | Use one base template plus a small modification-rule list and eval it directly. |
| Removing hidden cross-check weakens fidelity. | Replace it with visible-version verification: all returned versions preserve meaning and tone. |
| Description becomes too vague after removing behavior details. | Keep concrete trigger phrases and contexts in the description. |
| Explicit target-language requests conflict with source + companion default. | Conflict hierarchy puts explicit user constraints above defaults. |
| Teaching conflicts with brevity. | Teaching outranks brevity but remains capped and subordinate to fidelity. |
| Integrity issue is polished instead of refused. | Integrity is the top priority in the conflict hierarchy. |
| Prompt grows instead of shrinking. | Add a concision gate: revised `SKILL.md` should be shorter, or any increase should be justified. |

## Open Questions

None blocking before proposal review.

The downstream spec should settle two details:

1. Fallback companion language for English source text. Proposal-level recommendation: use instruction language if non-English; otherwise Chinese.
2. Whether target-only requests suppress source-language output. Proposal-level recommendation: yes, when the user clearly says "only translate to X" or equivalent.

## Decision Log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-06-16 | Default to source language + one companion language | Better matches polish-and-translate behavior than hardcoded Chinese + English | Always Chinese + English; source only |
| 2026-06-16 | Use English as default companion for non-English sources | User explicitly requested English as default additional language | Infer companion language from model guess |
| 2026-06-16 | Use deterministic fallback for English source | Prevents duplicate English output | Output English twice; omit companion language silently |
| 2026-06-16 | Keep learning default but simplify rules | Teaching remains important, but should not dominate prompt budget | Remove learning; keep exhaustive learning rules |
| 2026-06-16 | Replace many templates with one base template plus modification rules | Reduces token footprint and maintenance burden | Enumerate every output shape |
| 2026-06-16 | Drop hidden cross-check rendering | Invisible work is unverifiable overhead | Internally render unseen language versions |
| 2026-06-16 | Add conflict hierarchy | Resolves competing defaults predictably | Let workflow order imply priority |
| 2026-06-16 | Move behavior details out of description | Description should support skill triggering | Encode full output contract in description |

## Next Artifacts

1. `specs/editor-source-plus-companion-language-optimization.md`.
2. `spec-review` result.
3. Execution plan.
4. `plan-review` result.
5. `specs/editor-source-plus-companion-language-optimization.test.md`.
6. Baseline evidence before modifying `skills/editor/SKILL.md`.

## Follow-on Artifacts

- `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/reviews/proposal-review-r1.md`
- `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/reviews/proposal-review-r2.md`
- `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/review-log.md`
- `docs/changes/2026-06-16-editor-source-plus-companion-language-optimization/review-resolution.md`

A later proposal may add project-level or user-level companion-language configuration. This slice should use deterministic prompt-level defaults only.

## Readiness

Accepted and ready for spec authoring.

This proposal is not spec-complete, implementation-ready, verified, branch-ready, or PR-ready. Downstream lifecycle artifacts still need to be completed in order.
