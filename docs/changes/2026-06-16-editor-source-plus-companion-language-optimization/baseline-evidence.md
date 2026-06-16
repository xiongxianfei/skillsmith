# Baseline Evidence: Editor Source Plus Companion Language Optimization

## Status

baseline captured before prompt edit

## Capture point

- Date: 2026-06-16
- Branch: `docs/editor-source-companion-lifecycle`
- Commit before M1 changes: `fb8e1f8`
- Prompt file inspected: `skills/editor/SKILL.md`
- Prompt line count before optimization: 188 lines
- Eval fixture line count before M1 replacement: 224 lines
- Live model calls: none

This baseline is prompt-contract evidence, not live model output. The repository uses deterministic skill validation and reviewer-visible eval fixtures rather than live model CI.

## Current prompt contract evidence

| Baseline item | Current evidence | Effect relative to approved spec |
| --- | --- | --- |
| Description advertises hardcoded default | `skills/editor/SKILL.md:8` says the skill "defaults to Chinese + English final output". | Conflicts with source-language plus one companion-language default and trigger-focused description requirements. |
| Workflow default is hardcoded | `skills/editor/SKILL.md:52` says "Default visible target set is Chinese + English for non-empty source input." | Conflicts with R13-R16, which require polished source language plus one companion language. |
| Hidden cross-check exists | `skills/editor/SKILL.md:57` asks single-target requests to internally render Chinese + English as a fidelity cross-check. | Conflicts with R27 and R60, which remove hidden Chinese + English rendering requirements. |
| Target-only suppresses notes | `skills/editor/SKILL.md:59` treats `only the translation` and equivalent output-only phrasing as learning-note suppression. | Conflicts with R35-R36 for target-only requests that do not explicitly suppress notes. |
| Template gallery is broad | `skills/editor/SKILL.md:109`, `134`, `146`, `163`, and `178` introduce separate templates for default, explicit target, non-Chinese/non-English source, no-substantive-lesson, and integrity cases. | Supports the proposal's concern that templates and fallback cases have grown heavy; M2 should replace this with one base template plus modification rules. |
| Russian source defaults to Chinese + English | Existing eval text before M1 said Russian source edit returns visible target blocks defaulting to Chinese and English. | Conflicts with R14 and E2, which require Russian source to default to polished Russian plus English companion output. |

## Baseline behavior by required scenario class

| Scenario class | Current prompt behavior | Required post-change behavior |
| --- | --- | --- |
| Chinese source, no explicit target | Chinese + English output. This happens to match the visible language pair, but only because of the old hardcoded default rather than source + English companion resolution. | Polished Chinese source-language block plus English companion block and concise learning notes. |
| Russian source, no explicit target | Edited Russian source may appear first for editing requests, followed by target blocks defaulting to Chinese and English. | Polished Russian source-language block plus English companion block; no default Chinese block. |
| Spanish source, no explicit target | Same pattern as other non-Chinese/non-English source text: edited source first, then Chinese + English targets. | Polished Spanish source-language block plus English companion block, with best-effort quality caveat preserved by prompt contract. |
| English source, English instruction | Chinese + English final output; no duplicate English target because Chinese + English is hardcoded. | Polished English source-language block plus Chinese fallback companion because no non-English instruction language is available. |
| English source, Chinese instruction | Chinese + English final output; response framing follows instruction language, but companion selection is not expressed as instruction-language fallback. | Polished English source-language block plus Chinese companion output with Chinese framing. |
| Mixed-language directive words | No deterministic first-clear-non-English directive rule is present. | Determine instruction language from directive words; use first clearly identifiable non-English directive language for English-source companion fallback, otherwise Chinese. |
| Explicit single target | Current prompt allows explicit target-language output and may display only the requested target. | If not target-only, return polished source-language output plus the requested target-language block. |
| Explicit multiple targets | Current prompt says to repeat target-language blocks once per visible target language. | Preserve this behavior, but include the polished source-language block unless target-only and avoid unrelated language blocks. |
| Explicit target equals source | Current prompt only says not to duplicate when the edited source is already the Chinese or English target version. | Generalize no-duplicate behavior to any explicit target equal to the source language. |
| Target-only without note suppression | Current prompt treats output-only/only-translation phrasing as suppressing learning notes. | Omit source-language deliverable block but keep learning notes unless note suppression is explicit. |
| Target-only with no notes | Current prompt suppresses notes. | Preserve note suppression and omit source-language deliverable block. |
| Compact learning notes | Current prompt has strong learning-note rules and no fixed numeric cap. | Preserve default learning notes but simplify the rule set and make notes usually no more than three unless warranted. |
| Trivial correction | Current prompt uses exactly one fallback note for trivial-only cases. | Preserve one concise fallback note unless notes are suppressed. |
| Long source with many lessons | Current prompt permits uncapped substantive notes. | Keep notes concise, usually no more than three, but allow more when genuinely distinct and useful, grouped by theme. |
| Integrity issue | Current prompt refuses misleading transformations and provides accurate alternatives. | Preserve integrity priority; for explicit target and no-notes conflicts, use requested target language where possible and omit notes. |

## Baseline prompt-size evidence

```text
188 skills/editor/SKILL.md
224 tests/evals/skills/editor/cases.yaml
```

M2 must keep the optimized prompt under 500 lines and should make it shorter than this 188-line baseline or justify any increase in implementation evidence.

## Baseline conclusion

The current prompt already preserves many important editor qualities: fidelity with restraint, learning notes by default, response-language framing, explicit target handling, and integrity refusal behavior.

The baseline fails the accepted source-language plus companion-language contract because the prompt still hardcodes Chinese + English as the default visible target set, carries hidden Chinese + English cross-check rendering, and treats target-only output as learning-note suppression.

M1 replaces the reviewer-visible eval fixture with the approved scenario classes so M2 has a concrete proof target before the production prompt changes.
