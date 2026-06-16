# Post-Change Evidence: Editor Source Plus Companion Language Optimization

## Status

post-change evidence captured for M3

## Capture point

- Date: 2026-06-16
- Branch: `docs/editor-source-companion-lifecycle`
- Prompt file inspected: `skills/editor/SKILL.md`
- Prompt line count after optimization and line-break normalization: 117 lines
- Baseline prompt line count: 188 lines
- Eval fixture line count: 274 lines
- Live model calls: none

This evidence is prompt-contract and fixture evidence, not live model output. The repository uses deterministic skill validation and reviewer-visible eval fixtures rather than live model CI.

## Prompt contract evidence

| Requirement area | Post-change evidence | Result |
| --- | --- | --- |
| Trigger-focused description | `skills/editor/SKILL.md` describes an expert editor, translator, and writing coach with trigger examples, without embedding output-policy details. | Satisfies R5-R7 and AC18. |
| Source + companion default | The workflow says default visible output is polished source language plus one companion language, with English as companion for non-English sources and Chinese fallback for English sources without a clearly non-English instruction language. | Satisfies R13-R17 and AC2-AC6. |
| Mixed-language instruction handling | The workflow determines instruction language from directive words and uses the first clearly identifiable non-English directive language for English-source fallback. | Satisfies R18-R20 and mixed-language edge cases. |
| Explicit target handling | Modification rules cover single target, multiple targets, target equal to source, and target-only output. | Satisfies R31-R37 and AC7-AC10. |
| Learning notes | Learning notes are default-on, suppressible, response-framed, concrete when substantive, compact, and not hard-capped when more than three distinct lessons are warranted. | Satisfies R38-R50 and AC11-AC14. |
| Integrity hierarchy | The priority order puts integrity first, and integrity requests are refused or redirected with accurate alternatives where possible. | Satisfies R51-R56 and AC15-AC16. |
| Hidden cross-check removal | Stale-text search found no `internally render` or hidden Chinese + English cross-check language in `skills/editor/SKILL.md` or `README.md`. | Satisfies R27, R60, and AC17. |
| Prompt weight | Prompt is 117 lines after normalization, shorter than the 188-line baseline and under the 500-line maximum. | Satisfies R57-R58. |
| README mirror | README editor table and detail section describe source-language plus companion-language output. | Satisfies migration and public-doc alignment requirements. |

## Scenario class comparison

| Scenario class | Baseline behavior | Post-change prompt and fixture behavior |
| --- | --- | --- |
| Chinese source, no explicit target | Hardcoded Chinese + English happened to produce the desired visible pair. | Source-language resolution returns polished Chinese plus English companion output with learning notes. Covered by `editor-source-plus-english-chinese-source`. |
| Chinese source with English instruction | Hardcoded Chinese + English output with English response framing. | Returns polished Chinese plus English companion output and English-framed notes. Covered by `editor-source-plus-english-chinese-source-english-instruction`. |
| Russian source, no explicit target | Baseline prompt defaulted visible target blocks to Chinese + English. | Returns polished Russian plus English companion output and does not default to Chinese. Covered by `editor-source-plus-english-russian-source`. |
| Spanish source, no explicit target | Baseline pattern would add Chinese + English target blocks. | Returns polished Spanish plus English companion output while preserving best-effort intake caveat. Covered by `editor-source-plus-english-spanish-source`. |
| English source, English instruction | Baseline hardcoded Chinese + English, not source + fallback semantics. | Returns polished English plus Chinese fallback companion, with no duplicate English. Covered by `editor-english-source-fallback-companion`. |
| English source, Chinese instruction | Baseline did not express instruction-language fallback as the companion rule. | Returns polished English plus Chinese companion with Chinese response framing. Covered by `editor-english-source-chinese-instruction-fallback`. |
| Mixed directive words | Baseline lacked deterministic first-clear-non-English directive handling. | Uses directive words, not source snippets, to resolve instruction language and companion fallback. Covered by `editor-mixed-directive-uses-clear-non-english` and `editor-mixed-source-does-not-set-instruction-language`. |
| Explicit single target | Baseline could return target-only output even when source + target was required for non-target-only requests. | Non-target-only explicit target returns polished source plus requested target. Covered by `editor-explicit-target-overrides-default`. |
| Explicit multiple targets | Baseline repeated target blocks but remained anchored to Chinese + English defaults. | Returns polished source plus each requested target and no unrelated language blocks. Covered by `editor-explicit-multi-targets`. |
| Explicit target equals source | Baseline no-duplicate behavior was limited to Chinese or English target/source cases. | Avoids duplicate language blocks for any explicit target equal to source. Covered by `editor-explicit-target-equals-source`. |
| Target-only without note suppression | Baseline treated output-only/only-translation phrasing as note suppression. | Omits source-language deliverable but keeps learning notes unless suppression is explicit. Covered by `editor-target-only-keeps-notes`. |
| Target-only with note suppression | Baseline suppressed notes. | Preserves suppression and returns only the requested target-language deliverable. Covered by `editor-target-only-no-notes` and `editor-chinese-output-only-suppression`. |
| Compact learning notes | Baseline had strong notes but heavier fallback/template rules. | Notes remain default-on, compact, anchored, and secondary to the deliverables. Covered by `editor-compact-learning-notes`. |
| Ambiguous brevity | Baseline preserved notes for ambiguous brevity cues. | Preserves concise learning notes for ambiguous brevity cues. Covered by `editor-ambiguous-brevity-keeps-notes`. |
| Trivial correction | Baseline used one fallback note. | Keeps at most one concise fallback note and avoids padded grammar lessons. Covered by `editor-trivial-correction-no-overteach`. |
| Already-clear/restraint | Baseline used minimal changes and restraint notes. | Keeps minimal edits and at most one restraint note. Covered by `editor-already-clear-restraint`. |
| Long source with many lessons | Baseline allowed uncapped notes. | Allows more than three notes only when genuinely distinct and useful, grouped by theme. Covered by `editor-long-source-more-than-three-notes`. |
| Integrity issue | Baseline refused misleading approval claims. | Preserves integrity-first refusal/redirect behavior. Covered by `editor-integrity-priority`. |
| Integrity + explicit target + no notes | Baseline did not have a dedicated three-way conflict eval. | Refuses or redirects, uses French accurate alternative where possible, and omits notes. Covered by `editor-integrity-explicit-target-no-notes`. |
| No source artifact | Baseline asked for text and omitted notes. | Preserves no-source boundary. Covered by `editor-boundary-no-source`. |

## Validation evidence

The final M3 validation set is recorded in the active plan and `change.yaml`:

- `python tests/validate_skills.py`
- `python -m unittest discover tests`
- `python tests/check_readme_sync.py`
- `git diff --check`
- `wc -l skills/editor/SKILL.md`
- stale hardcoded Chinese + English default / hidden cross-check search

The known validator warning about unrelated grandfathered skills without eval fixtures remains non-blocking and unrelated to this editor change.

## Conclusion

The optimized prompt and eval fixture now align with the accepted source-language plus companion-language contract. The final prompt is shorter than baseline, hidden cross-check rendering has been removed, README wording is synchronized, and reviewer-visible evidence covers the same scenario classes recorded in baseline.
