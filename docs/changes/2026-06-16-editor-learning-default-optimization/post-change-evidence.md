# Post-change Evidence: Editor Learning Default Optimization

## Status

captured after M2 prompt implementation and before M3 code review

## Evidence source

- Skill prompt inspected: `skills/editor/SKILL.md`
- Baseline evidence: `docs/changes/2026-06-16-editor-learning-default-optimization/baseline-evidence.md`
- Eval fixture: `tests/evals/skills/editor/cases.yaml`
- Current prompt contract: expert editor and translator with default Chinese + English output, explicit target-language overrides, and default `Learning notes` unless explicitly suppressed.
- Evidence method: static prompt-contract inspection against the approved eval scenarios. No live model call was used, consistent with the test spec's deterministic/manual evidence strategy.

## Post-change prompt behavior summary

The updated `editor` prompt preserves the expert editor foundation from the baseline:

- it edits with fidelity and restraint;
- it separates instruction, source, and target language roles;
- it defaults visible output to Chinese + English;
- it honors explicit target-language requests;
- it refuses misleading or materially unsupported transformations;
- it keeps deliverables copyable and before commentary.

The prompt now adds default teaching value:

- `Learning notes` are included by default after the deliverable for every non-empty, non-suppressed editing or translation request;
- English response framing labels the block `Learning notes`;
- Chinese response framing labels the block `学习要点`;
- explicit output-only or no-explanation requests suppress the block;
- ambiguous brevity cues keep focused notes;
- substantive notes require concrete anchoring or an equivalent reference to the edit or translation choice;
- trivial, already-strong, brittle-rule, no-substantive-lesson, and integrity-boundary cases use exactly one concise fallback note;
- notes are not limited by a fixed numeric cap, are not padded, stay scannable, and must not justify meaning drift or unsupported certainty.

## Prompt-contract evidence

| Current prompt location | Post-change behavior |
| --- | --- |
| `skills/editor/SKILL.md:3-10` | Description identifies an expert editor and translator that supports learning from edits to shared text, without standalone writing-coach identity. |
| `skills/editor/SKILL.md:35-39` | Preserves restraint and integrity, makes concise `Learning notes` default, and asks for source text instead of coaching without an artifact. |
| `skills/editor/SKILL.md:51-57` | Keeps default Chinese + English output and explicit target-language overrides. |
| `skills/editor/SKILL.md:58-63` | Defines explicit-only suppression, ambiguous brevity fallback, substantive lessons, fallback notes, and no-padding/no-extra-edit rules. |
| `skills/editor/SKILL.md:71-75` | Keeps no default assessment or `Why` section while making `Learning notes` default for non-empty, non-suppressed requests. |
| `skills/editor/SKILL.md:79-83` | Defines exact `Learning notes` and `学习要点` labels. |
| `skills/editor/SKILL.md:87-107` | Requires post-deliverable, response-language-only, anchored, reusable, uncapped, scannable, non-padded, non-generic learning notes and concrete fallback notes. |
| `skills/editor/SKILL.md:109-174` | Defines default, longer-note grouping, explicit target-language, non-Chinese/English source edit, no-substantive-lesson, and explicit suppression templates. |
| `skills/editor/SKILL.md:176-188` | Preserves integrity-boundary refusal ordering and adds a concise concrete integrity note unless explicitly suppressed. |

## Scenario comparison

| Scenario | Baseline behavior | Post-change behavior from current prompt | Learning value after change | Bloat, over-editing, and fidelity check |
| --- | --- | --- | --- | --- |
| `editor-learning-default-polish` | Chinese and English deliverables only; no default teaching. | Chinese and English deliverables are followed by `Learning notes` with anchored substantive notes. | Added: teaches a reusable editing principle from a concrete edit. | Capped at three by default; deliverables stay first; fidelity rules remain in force. |
| `editor-learning-principle-not-report` | Preserves uncertainty but does not teach the principle unless asked. | Notes must preserve uncertainty and must not justify unsupported certainty or drift. | Added: can teach why cautious wording should remain cautious. | The prompt explicitly bars unsupported certainty and generic self-commentary. |
| `editor-learning-explicit-english-target` | English-only output; no notes by default. | Explicit target-language output remains English-only, then adds `Learning notes` unless suppressed. | Added: teaches a translation choice while respecting target override. | The default Chinese + English set is not reintroduced when an explicit target is clear. |
| `editor-learning-no-notes-override` | Omits notes because notes are opt-in. | Omits notes because `no notes` is explicit suppression. | Correctly absent by user request. | Suppression is direct and narrow; deliverable behavior remains intact. |
| `editor-learning-ambiguous-brevity` | Omits notes because notes are opt-in. | `keep it short` does not suppress notes; notes stay focused and scannable. | Added: preserves default teaching under ambiguous brevity. | The prompt avoids padding and uses structured notes rather than a report. |
| `editor-learning-response-language-notes` | Chinese framing for requested notes, but not default and label was `说明`. | Chinese instruction uses `学习要点` and notes in Chinese response framing only. | Added: default teaching with the learning-oriented Chinese label. | No bilingual note duplication by default. |
| `editor-learning-english-instruction-chinese-source` | English framing and Chinese source-role handling, but no default notes. | English framing uses `Learning notes`; Chinese source is edited as Chinese before target rendering. | Added: teaches in English response framing while preserving source-language editing. | Role separation remains explicit in workflow. |
| `editor-learning-skip-trivial` | Corrects typo and omits notes. | Corrects typo and includes exactly one concise fallback note for trivial-only correction unless suppressed. | Added: teaches restraint by saying there is no broader pattern. | Prevents grammar lectures and multi-note padding. |
| `editor-learning-restraint` | Minimal or no edits; no notes. | Minimal or no edits and at most one restraint-oriented fallback note unless suppressed. | Added: restraint itself becomes the lesson. | Explicitly forbids extra edits or padded notes to create teachable material. |
| `editor-learning-brittle-rule` | Notes only if asked; brittle-rule handling not explicit. | Notes must qualify context-dependent rules or use a concrete fallback note. | Added: teaches with epistemic restraint rather than absolute rules. | Prevents misleading lessons such as universal active-voice rules. |
| `editor-learning-dim-lighting-fidelity` | Preserves meaning and omits notes. | Any note must preserve ambiguity and cannot justify unsupported specificity. | Added: can teach fidelity to source uncertainty. | Fidelity remains primary and teaching is subordinate. |
| `editor-learning-chinese-output-only` | Omits notes because notes are opt-in; likely honors `只要译文`. | Omits notes because `只要译文` is explicit output-only suppression. | Correctly absent by user request. | Chinese suppression is explicitly anchored in the prompt. |
| `editor-learning-chinese-no-explanation` | Omits notes because notes are opt-in; likely honors `不用解释`. | Omits notes because `不用解释` is explicit no-explanation suppression. | Correctly absent by user request. | Chinese no-explanation suppression is explicitly anchored. |
| `editor-learning-pr-description` | Indirect edit request receives deliverables only. | Indirect edit requests receive deliverables plus concise notes unless suppressed. | Added: teaches from professionalizing PR text without changing the workflow. | Prompt keeps deliverables copyable and before notes. |
| `editor-learning-integrity-boundary` | Refuses misleading approval rewrite and offers accurate alternatives; no default note. | Refuses misleading transformation, offers accurate alternatives, and includes one concrete integrity note unless suppressed. | Added: explains why review intent cannot become approval. | Teaching cannot weaken the refusal or imply unsupported approval. |
| `editor-learning-boundary-no-source` | No explicit standalone coaching boundary. | Missing-source and source-free coaching requests ask for source text and omit notes. | Correctly absent because there is no deliverable to teach from. | Prevents trigger-scope drift into standalone coaching. |
| `editor-learning-russian-source-edit` | Includes edited Russian source plus Chinese and English targets; no default notes. | Preserves edited source block plus target blocks, then adds one notes block after all deliverables. | Added: teaches from source edit or translation choices. | Does not duplicate notes per language and keeps source role intact. |
| `editor-learning-russian-translation-only` | Translation-only request does not add an optimized Russian source block; no notes. | Preserves translation-only behavior and adds notes after target deliverables unless suppressed. | Added: teaches translation choices without adding an edited source block. | Existing source-intake and target-output contract remains bounded. |

## Required behavior evidence by test-spec group

| Test-spec group | Evidence |
| --- | --- |
| T1 structure and pure prompt | `name: editor`, `$ARGUMENTS`, and `## Output Format` remain present; no optional tool/runtime frontmatter was added. |
| T2 description and old-rule replacement | Description says expert editor and translator, mentions learning from edits to shared text, and does not advertise broad coaching; obsolete notes-on-request wording was replaced. |
| T4 default substantive learning | Default templates include Chinese and English deliverables followed by `Learning notes`; note rules require anchoring and reusable principles. |
| T5 explicit target-language learning | Explicit single-target template includes the requested target deliverable followed by `Learning notes`. |
| T6 explicit suppression | Suppression examples include `no notes`, `just the text`, `only the translation`, `skip the explanation`, `不用解释`, `不要说明`, and `只要译文`. |
| T7 ambiguous brevity | `keep it short`, `I'm in a hurry`, and `just need this quickly` are explicitly not suppression triggers. |
| T8 mixed-language framing | Labels are response-language controlled; English uses `Learning notes`, Chinese uses `学习要点`, and notes are not duplicated bilingually. |
| T9 trivial-only fallback | Trivial edits avoid grammar lectures and get exactly one concise fallback note unless suppressed. |
| T10 already-good restraint | Already-strong text keeps minimal changes and at most one restraint-oriented fallback note. |
| T11 brittle-rule teaching | Context-dependent principles must be qualified or replaced with a concrete fallback note. |
| T12 integrity boundary | Integrity refusals preserve truth and use one concrete integrity note unless explicitly suppressed. |
| T13 source-free boundary | Missing-source and standalone coaching requests ask for text and do not include `Learning notes`. |
| T14 before/after comparison | This file compares the same scenario classes against `baseline-evidence.md`. |
| T15 compatibility | Default Chinese + English output, explicit target overrides, no default assessment, no default `Why`, and pure prompt boundaries remain. |
| T16 repository validation | See M3 validation notes in the active plan and change metadata. |

## Before/after comparison summary

| Dimension | Baseline | Post-change evidence | Result |
| --- | --- | --- | --- |
| Learning value | Absent by default; present only when requested. | Present by default through a post-deliverable `Learning notes` block. | Improved for normal non-suppressed requests. |
| Bloat risk | Low because notes were absent. | Controlled by deliverable-first ordering, one bullet per useful substantive lesson, theme labels for longer note sets, no-padding rules, and fallback notes. | Acceptable under the approved contract. |
| Over-editing risk | Low-to-moderate due to existing restraint language. | Explicitly controlled by no-extra-edit and no-padding rules, plus trivial/already-good fallback behavior. | Not increased by prompt contract. |
| Fidelity | Strong existing fidelity and restraint language. | Preserved and extended so notes cannot justify drift, unsupported certainty, false approval, or false attribution. | Preserved. |
| Suppression | Notes absent by default. | Notes default-on; suppression is explicit-only with multilingual anchors. | Behavior changes as intended. |
| Response language | Labels and requested notes followed response language. | `Learning notes` / `学习要点` follow response language, with no bilingual duplication by default. | Preserved and sharpened. |
| Trigger scope | Editor/translator prompt without broad coaching identity. | Description and prompt ask for source text instead of handling standalone coaching. | Preserved. |

## Residual risk

This evidence proves the updated prompt contract and its reviewer-visible scenario coverage. It does not prove every downstream model will always follow the prompt perfectly. That residual risk is expected by the approved test strategy, which relies on deterministic validation plus reviewer-readable evidence rather than live model CI.

## Conclusion

The post-change prompt contract adds default learning value where the baseline had none, while preserving the expert editor contract, target-language behavior, suppression override, response-language framing, and integrity boundaries. The new behavior is bounded by explicit no-padding, no-extra-edit, scannable-format, fallback-note, and fidelity rules.
