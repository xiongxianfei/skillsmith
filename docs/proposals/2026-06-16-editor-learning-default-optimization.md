# Proposal: Learning-default optimization of the `editor` skill

## Status

accepted

## Problem

The current `editor` skill is already framed as an expert professional editor and translator for polishing, proofreading, rewriting, and translating shared text. It defaults to Chinese and English final output, honors explicit target-language requests, and emphasizes fidelity with restraint: preserve meaning, facts, numbers, technical details, uncertainty, voice, intent, tone, and requested format.

However, the current output contract treats teaching as opt-in. The accepted editor contract says there should be no default assessment section, no default `Why` or change-explanation section, and notes should appear only when the user explicitly asks for explanation, notes, or changes.

That was a reasonable prior decision when the main goal was minimal deliverable output. The product direction has changed: the first target remains polishing and translation, but the second target is now also important: teaching the user how to improve. Because teaching is part of the skill's default value, explanatory notes should no longer be opt-in only.

The challenge is to add default teaching without turning the skill back into a verbose report generator. Generic explanations like "I improved clarity" do not teach. Over-explaining typos creates noise. A teaching incentive can also encourage over-editing so the model has more things to explain. This proposal therefore reverses the prior notes-on-request default, but replaces it with a restrained, per-change teaching format that preserves the skill's expert-quality standard.

## Goals

1. Keep the primary behavior of `editor` as polish and translate.
2. Make teaching the user a default secondary behavior, not an opt-in-only behavior.
3. Replace "notes only when explicitly asked" with a default teaching block that appears after the polished or translated deliverable, stays short, is anchored to concrete edits, teaches principles, and remains suppressible by explicit user instruction.
4. Preserve the existing expert editing standard: fidelity, restraint, factual accuracy, terminology care, minimal change when the source is already good, and integrity boundaries.
5. Avoid over-editing for the sake of teaching.
6. Teach generalizable writing and translation principles, not merely report what changed.
7. Keep explanations in the response framing language rather than duplicating them bilingually.
8. Preserve the current default visible output target of Chinese and English unless the user explicitly requests a different target-language set.
9. Keep the pure-prompt boundary: no new tools, scripts, generated artifacts, or live-model CI.
10. Add baseline-first eval evidence that proves the new teaching behavior improves learning value without increasing bloat or weakening fidelity.

## Non-goals

1. Do not optimize every Skillsmith skill in this slice.
2. Do not redesign the whole `editor` skill from scratch.
3. Do not remove the expert-quality editing standard.
4. Do not make teaching more important than producing the polished or translated deliverable.
5. Do not explain every typo, punctuation fix, or mechanical correction.
6. Do not produce bilingual teaching notes by default.
7. Do not add a long assessment, grading, or language-quality report section.
8. Do not add live model calls to CI.
9. Do not add tools, scripts, or external resources.
10. Do not expand unsupported-language guarantees beyond the current source-intake and target-output contract.

## Vision fit

fits the current vision

This proposal strengthens `editor` as a reusable, reviewable, portable Markdown skill. It turns the skill from a deliverable-only editor into an editor-tutor while keeping the first-order user value clear: produce polished and translated text first, then teach briefly.

## Initial intent preservation

| Initial user goal | Proposal treatment | Where recorded |
|---|---|---|
| Generate a proposal | in scope | Entire artifact |
| Follow best practices | in scope | Problem, Recommended Direction, Testing and Verification Strategy |
| First target is polish text and translate | in scope | Goals, Recommended Direction, Expected Behavior Changes |
| Second target is to teach the user | in scope | Goals, Teaching Standard, Recommended Direction |
| Teaching is important enough to be default behavior | in scope | Problem, Goals, Testing and Verification Strategy |
| Avoid simply bolting on verbose explanations | in scope | Non-goals, Risks and Mitigations, Teaching Standard |
| Preserve existing expert quality | in scope | Goals, Expert Quality Preservation |

## Scope budget

| Work item | Treatment | Reason |
|---|---|---|
| Reverse "notes only when asked" default | core to this proposal | This is the central behavior change. |
| Add default teaching block | core to this proposal | Teaching becomes default secondary value. |
| Keep deliverable-first output | core to this proposal | Polished and translated text remains the primary target. |
| Per-change teaching-note format | core to this proposal | Concrete notes prevent generic explanation bloat. |
| Teaching-note suppression override | core to this proposal | Users must be able to ask for "no notes" or "just the text." |
| Eval scenarios for learning value | core to this proposal | The change must be reviewable through real examples. |
| Baseline manual smoke evidence | core to this proposal | Needed to prove the new default is useful rather than noisy. |
| Rewrite all editor internals | out of scope | Only change what is needed to support default teaching. |
| Repository-wide validator changes | out of scope | This is a skill behavior change, not a validator feature. |
| Live model CI | out of scope | Too costly and nondeterministic for this slice. |
| High-risk skill changes | separate proposal | This is a low-risk editor optimization. |

## Context

The current `editor` skill already has a strong expert foundation. It separates instruction, source, and target language roles; resolves response language; defaults visible target output to Chinese and English; checks integrity before editing; edits source text with fidelity and restraint; and verifies that visible target versions preserve the same meaning.

The current output format keeps responses copyable and minimal. It uses bold labels, content blocks, and no decorative symbols. It also explicitly suppresses default assessment and change-explanation sections.

This proposal changes that prior output decision. The new default should not restore the old long report shape. Instead, it should add a compact teaching layer after the deliverable.

The governing spec that currently captures the old decision is `specs/editor-expert-quality-optimization.md`, especially the requirements that supporting notes appear only when the user explicitly asks for them. If this proposal is accepted, the downstream spec should supersede that portion while preserving the rest of the expert-quality contract unless explicitly changed.

## Teaching Standard

For this skill, teaching means helping the user learn a transferable writing or translation principle from the edit.

A good teaching note is anchored to a specific original-to-revised change, explains a reusable principle, stays concise, covers only substantive changes, avoids oversimplified grammar or style rules, uses the response framing language, and does not create extra edits just to create teaching opportunities.

Bad teaching-note patterns include generic statements such as "I improved clarity," preference-only claims such as "changed X to Y because Y is better," explanations of ordinary typo fixes, bilingual note duplication, and multiple notes for a text that needed only one small edit.

## Expert Quality Preservation

The default teaching behavior should remain subordinate to the existing expert-quality standard. The skill should preserve meaning, facts, names, numbers, technical details, uncertainty, logic, intent, commitments, voice, and requested tone. It should not make the source more certain than warranted, imply unsupported approval or completion, replace precise terms with flashier but less accurate wording, or rewrite an already strong text just to generate teaching material.

## Options Considered

### Option 1: Keep notes opt-in only

This preserves the current minimal-output behavior, but it does not satisfy the new product direction. Teaching would remain hidden behind explicit requests even though it is now part of the skill's default value.

Disposition: rejected.

### Option 2: Add a generic default explanation paragraph

This is easy to implement, but it would teach poorly. A paragraph like "I improved clarity, concision, and professionalism" is not anchored to specific edits and does not help the user improve the next draft.

Disposition: rejected.

### Option 3: Add default per-change teaching notes after the deliverable

This keeps the polished or translated text first, then teaches through a short list of concrete, reusable lessons. It directly supports the new priority while preserving copyability and restraint.

Disposition: recommended.

### Option 4: Interleave teaching notes with the polished text

This makes the teaching more visible, but it damages copyability and forces learning friction into the primary deliverable. The user's first target is still polish and translation, so the deliverable should come first.

Disposition: rejected.

### Option 5: Teach every edit exhaustively

This maximizes explanation, but it creates noise and incentivizes over-editing. It also conflicts with the expert-quality principle that a strong edit is the smallest set of changes that makes the text clear, accurate, natural, and ready to use.

Disposition: rejected.

## Recommended Direction

Adopt Option 3: default per-change teaching notes after the deliverable.

The revised behavior hierarchy should be:

1. Polish and translate the text.
2. Then teach the user from the most important substantive edits.
3. Keep teaching concise, concrete, suppressible, and subordinate to fidelity.

The skill must include a `Learning notes` block by default for normal polish, rewrite, and translation requests. The default output should become:

```markdown
**<Chinese label>**
<final Chinese version>

**<English label>**
<final English version>

**<Learning notes label>**
- `<original>` -> `<revised>`: <generalizable principle>.
- `<original>` -> `<revised>`: <generalizable principle>.
```

The exact labels should follow the existing response-language rules. Recommended labels are `Learning notes` in English and `学习要点` in Chinese, because they make the teaching purpose explicit and reinforce selectivity. For other response languages, localize where practical; otherwise use `Learning notes`.

Teaching notes should follow these rules:

1. Put polished and translated text before teaching.
2. Place notes after target-language versions, not interleaved with them.
3. Anchor each note to a concrete change using an original-to-revised form or equivalent.
4. Explain a reusable principle rather than merely reporting that a change happened.
5. Skip trivial edits such as ordinary typos, punctuation, capitalization, and mechanical grammar corrections unless they reveal a recurring pattern.
6. Include one note per substantive lesson without a fixed numeric cap. The number of notes should follow the actual useful lessons in the source text; never pad the block or invent lessons.
7. Do not invent extra edits to produce more teaching notes.
8. If the text is already strong and needs little change, include at most one brief note about restraint.
9. Use the response framing language for teaching notes rather than repeating them in every target language.
10. Avoid brittle rules; note common exceptions when a principle depends on context.
11. Omit the teaching block only when the user explicitly asks for output-only delivery or no explanation.
12. Expand explanation only when the user asks to learn more, while still anchoring it to concrete edits.

### Suppression rule

Suppression should be high-precision rather than clever. The skill should suppress learning notes for direct, unambiguous output-only requests, such as `no notes`, `just the text`, `only the translation`, `skip the explanation`, `不用解释`, `不要说明`, `只要译文`, or equivalent explicit phrasing in the user's language.

The skill should not infer suppression from indirect or ambiguous cues such as "keep it short," "I'm in a hurry," or "just need this quickly." Those cues may mean concise output, not no notes. When suppression intent is ambiguous, the skill should show focused learning notes because teaching is the default behavior. This default is acceptable because the notes are deliverable-first, anchored, scannable, and suppressible on explicit request.

The `description` field should mention the new default teaching behavior, but it should not introduce `writing coach` as a standalone third identity. Teaching is a byproduct of editing or translating a source artifact, not a separate coaching mode. A downstream spec should settle final wording, but the direction is:

```yaml
description: >
  Expert professional editor and translator for polishing, proofreading,
  rewriting, translating, and learning from edits to shared text. Use for
  emails, PR descriptions, docs, release notes, messages, and casual asks like
  "fix this", "make this sound better", "translate this", or "show me what to
  learn from these edits"; defaults to Chinese + English final output with
  structured learning notes, and honors explicit target-language or no-notes
  requests.
```

## Expected Behavior Changes

1. A normal polishing request returns Chinese and English final versions first, followed by structured learning notes.
2. A translation request returns the target-language deliverable first, then a `Learning notes` block by default unless explicitly suppressed.
3. Default teaching notes explain substantive choices, not every mechanical correction.
4. Users can use explicit output-only or no-explanation phrasing, such as "no notes," "just the text," or "only translate," to suppress teaching.
5. If the source text is already strong, the skill teaches restraint instead of inventing unnecessary edits.
6. The skill does not reintroduce a long assessment section, stage report, or generic explanation paragraph.
7. Teaching notes use the response framing language, not bilingual duplication.
8. Integrity-boundary behavior remains intact: the skill refuses misleading transformations and offers accurate alternatives.

## Architecture Impact

No runtime architecture changes are expected.

Expected touched areas include:

```text
docs/proposals/2026-06-16-editor-learning-default-optimization.md
specs/editor-learning-default-optimization.md
docs/plans/2026-06-16-editor-learning-default-optimization.md
specs/editor-learning-default-optimization.test.md
tests/evals/skills/editor/cases.yaml
skills/editor/SKILL.md
docs/changes/2026-06-16-editor-learning-default-optimization/
```

If an editor workflow diagram exists in the active branch, it should be updated with the same teaching-default logic. No new tools, scripts, executable resources, generated prompt assets, or repository-wide validator changes are expected.

## Testing and Verification Strategy

Before editing `skills/editor/SKILL.md`, capture representative baseline behavior against the current skill. The baseline should record both that the current default suppresses notes unless requested and what learning value the user receives today from the same eval texts. In the current contract that learning value should usually be none by design; the after-comparison should show that the new teaching block adds useful learning value rather than merely adding text.

Required eval scenarios should cover:

| Scenario | Expected coverage |
|---|---|
| Default polish plus translation plus teaching | Chinese and English final versions first, then learning notes by default. |
| Teaching note quality | Notes preserve uncertainty, teach a generalizable principle, and avoid generic "made it professional" claims. |
| Explicit no-notes override | Direct suppression phrases such as "no notes," "just the text," `不用解释`, and `只要译文` suppress the learning block while preserving the deliverable. |
| Ambiguous suppression fallback | Indirect cues such as "keep it short" do not suppress learning notes; the skill still shows focused, scannable notes. |
| Restraint for already-good text | Minimal or no changes; at most one note about preserving already-clear wording. |
| No over-editing to teach | Already-good text remains minimally edited and the note count matches the actual substantive changes instead of being padded. |
| Trivial mechanical fix | Corrects the typo without producing a padded grammar lesson. |
| Translation with useful teaching | Honors explicit target-language requests and explains a transferable translation choice when useful. |
| Integrity boundary | Refuses misleading transformations and may include one note explaining why approval cannot be implied from review intent. |
| Mixed-language response framing | Uses the instruction language for labels and learning notes without duplicating notes bilingually. |
| Brittle-rule teaching | A tempting but oversimplified lesson, such as "always use active voice," is either qualified with context and exceptions or not taught. |

Success criteria:

| Check | Expected result |
|---|---|
| Deliverable first | Polished or translated text appears before teaching. |
| Default teaching | A `Learning notes` block appears by default unless explicitly suppressed. |
| Suppression override | Explicit output-only or no-explanation requests remove the teaching block. |
| Ambiguity fallback | Ambiguous brevity cues keep the default focused learning notes. |
| Anchoring | Notes use original-to-revised or equivalent concrete anchoring. |
| Generalization | Notes explain reusable principles and qualify them when a rule has common exceptions. |
| Selectivity | Trivial edits are not over-explained. |
| Restraint | The skill does not over-edit to create teaching material. |
| Framing language | Notes use the response language, not bilingual duplication. |
| Fidelity | Teaching does not justify meaning drift. |
| Scannability | Teaching block has no fixed numeric cap, but remains structured and scannable. |

Minimum validation commands for the eventual implementation:

```bash
python tests/validate_skills.py
python -m unittest discover tests
git diff --check
```

Run this only if present in the branch:

```bash
python tests/check_readme_sync.py
```

Do not add live model calls to CI for this slice.

## Rollout and Rollback

Rollout should be limited to the `editor` skill, its durable behavior spec, its eval fixture, and any existing workflow diagram or change-local evidence that owns editor behavior. The change should proceed through proposal review before spec authoring and downstream lifecycle artifacts.

Rollback is straightforward: revert the `editor` skill prompt, eval fixture changes, workflow diagram changes if any, and change-local evidence for this slice. Because this proposal does not add tools, scripts, installer behavior, dependencies, or CI model calls, rollback should not affect other skills.

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Teaching notes make every response too long. | Use deliverable-first ordering, one bullet per substantive lesson, theme labels for longer note sets, and no-padding rules. |
| The skill over-edits to create lessons. | Add an explicit "do not invent edits to teach" rule and a restraint eval. |
| Notes become generic self-commentary. | Require concrete original-to-revised anchoring and a reusable principle. |
| Trivial fixes drown out useful lessons. | Skip typos and mechanical punctuation unless they reveal a recurring pattern. |
| Users who only want the deliverable feel friction. | Support explicit suppression such as "no notes," "just the text," "only translation," `不用解释`, and `只要译文`. |
| Weak models over-infer suppression from indirect cues. | Define suppression narrowly: explicit output-only or no-explanation phrasing only; ambiguous brevity cues still show concise notes. |
| The description expands trigger scope into standalone coaching. | Keep the identity as editor and translator that teaches through edits to shared text; do not advertise a separate writing-coach mode. |
| Notes conflict with bilingual output. | Keep notes in the response framing language only. |
| Teaching rules become oversimplified. | Require nuance where a rule has common exceptions. |
| Prompt grows too long. | Keep new teaching rules compact and remove obsolete notes-only-when-asked logic. |
| Fidelity weakens because teaching rewards changes. | Preserve the existing fidelity-with-restraint standard as the top editing rule. |
| The new behavior silently reverses a prior decision. | Record this proposal as an explicit supersession of the old notes-on-request default. |

## Open Questions

None blocking before spec.

Resolved proposal-level decisions:

1. Suppression detection should be high-precision on explicit phrasing and should not try to infer suppression from indirect cues.
2. Ambiguous suppression intent should default to showing focused learning notes.
3. The spec should use both a narrow semantic rule and multilingual anchor examples: suppress only on explicit output-only or no-explanation requests, illustrated by examples such as `no notes`, `just the text`, `only the translation`, `skip the explanation`, `不用解释`, `不要说明`, and `只要译文`.

Labels are settled as:

| Response language | Teaching label |
|---|---|
| English | `Learning notes` |
| Chinese | `学习要点` |
| Other | Localized where practical; otherwise `Learning notes` |

The note-count rule is settled as: one note per genuinely useful substantive lesson, no fixed numeric cap, no padding, and scannable formatting with short theme labels when the note set is longer or varied.

## Decision Log

| Date | Decision | Reason | Alternatives rejected |
|---|---|---|---|
| 2026-06-16 | Make polish and translation the first target | User explicitly identified this as the primary goal | Teaching-first output |
| 2026-06-16 | Make teaching the default second target | User identified teaching as important default value | Notes only when asked |
| 2026-06-16 | Put teaching after the deliverable | Keeps output copyable and respects the primary goal | Interleaved explanations |
| 2026-06-16 | Use per-change teaching notes | Concrete changes teach better than generic commentary | Generic explanation paragraph |
| 2026-06-16 | Teach principles, not just fixes | Learning value requires reusable guidance | "Changed X to Y because Y is better" |
| 2026-06-16 | Keep notes suppressible | Defaults should yield to explicit user intent | Always teach regardless of request |
| 2026-06-16 | Add no-over-editing guard | Teaching should not undermine fidelity and restraint | Reward more edits with more lessons |
| 2026-06-16 | Keep notes in response framing language | Notes are commentary to the user, not target-language deliverables | Bilingual teaching notes by default |
| 2026-06-16 | Suppress notes only on explicit output-only or no-explanation requests | Weak models are more reliable on crisp surface signals than implicit intent | Infer suppression from ambiguous brevity cues |
| 2026-06-16 | Show concise notes when suppression intent is ambiguous | Teaching is the default and unwanted short notes are a visible, recoverable cost | Suppress notes on ambiguity |
| 2026-06-16 | Use both semantic rule and multilingual anchor examples for suppression | The rule defines the narrow concept and examples calibrate weak-model behavior across common languages | Closed list only; broad semantic inference only |
| 2026-06-16 | Set the teaching label to `Learning notes` / `学习要点` | The labels foreground learning and selectivity | Generic `Notes`; literal `学习笔记` |
| 2026-06-16 | Remove the fixed note cap while preserving no-padding | Supports fuller learning notes when useful without turning the count into a quota | Fixed three-note cap; always produce three notes |

## Next Artifacts

1. `proposal-review` result for this proposal.
2. `specs/editor-learning-default-optimization.md`.
3. `spec-review` result.
4. Execution plan.
5. `plan-review` result.
6. `specs/editor-learning-default-optimization.test.md`.
7. Baseline evidence before modifying `skills/editor/SKILL.md`.

## Follow-on Artifacts

- Proposal review R1: `docs/changes/2026-06-16-editor-learning-default-optimization/reviews/proposal-review-r1.md`
- Proposal review R2: `docs/changes/2026-06-16-editor-learning-default-optimization/reviews/proposal-review-r2.md`

A later proposal may consider a dedicated `writing-coach` skill if teaching grows beyond concise per-change notes. For this slice, teaching should remain part of `editor`, not a separate skill.

## Readiness

Accepted for spec authoring after proposal-review R2. This proposal is not implementation-ready, verified, branch-ready, or PR-ready until downstream lifecycle artifacts are completed in order.
