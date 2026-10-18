# Bilingual vocabulary mastery: comprehensive ten-domain reference

## Status and rationale

Design proposal for a new skill, 2026-10-18. User-selected mode: comprehensive linguistic reference (all ten domains, English plus Simplified Chinese). Existing `editor`, `language-tutor`, and `flashcard-generator` remain separate and unchanged.

## Trigger intent and accepted input

- Name: `vocabulary-mastery`; slash command: `/vocabulary-mastery`.
- Accept one English headword (or a fixed multiword lexical expression) from `$ARGUMENTS`, optionally accompanied by an example sentence, target sense, learner goals, or British/American variety.
- Trigger for requests for deep bilingual lexical/linguistic analysis, including indirect requests for a word's pronunciation, structure, meanings, grammar, and real usage as a complete learning reference.
- Do not hijack generic proofreading, sentence correction, conversation tutoring, quiz-only tasks, or flashcard export.
- With missing target, ask for the word; with multiple unrelated targets, request one term to analyze to avoid incomplete entries.

## Output contract

One portable Markdown reference, English + Simplified Chinese, with:
1. **Word Overview / 词汇概览**: headword, POS, short sense map, pronunciation marked by variety if reliable, and sense selected from any supplied context.
2. **Ten numbered linguistic sections**, always in this fixed order and with English and Chinese explanations and natural, bilingual example or concrete illustration when supportable:
   1. Phonetics / 语音学
   2. Phonology / 音系学
   3. Morphology / 形态学
   4. Lexicon / 词汇
   5. Syntax / 句法学
   6. Semantics / 语义学
   7. Pragmatics / 语用学
   8. Discourse / 语篇
   9. Information Structure / 信息结构
   10. Prosody / 韵律
3. **Knowledge Connections / 知识关联**: compact cross-domain synthesis with a high-value contrast or usage link.
4. **Recall Prompts / 回忆练习**: exactly three short questions testing different aspects (e.g., meaning-to-form, collocation/syntax, and pronunciation/context), with short answer key.
5. **Accuracy Notes / 准确性说明** only when needed for uncertainty, variety variation, or absent evidence.

Each domain is mandatory. For dimensions with no special or word-specific feature, explicitly describe the limitation (English and Chinese) and optionally illustrate a general sentence-level phenomenon. Never invent unusual linguistic features just to fill a section.

## Analysis and evidence boundaries

- Distinguish *a word's reference pronunciation* from *how the learner actually pronounced it*. IPA is labelled BrE or AmE; no observation of learner audio without real audio, no claims of generating/playing sound without tools.
- Phonetics covers speech segments and articulation; phonology covers system-level syllables/stress/contrasts; prosody covers phrase-level stress, rhythm, intonation. Distinguish information focus from intonation and syntax from meaning.
- Use genuine morphological structure; do not infer roots or etymologies by slicing spelling (`record` is not automatically `re-` + `cord`). Give inflection and related forms that are real.
- For polysemy or homographs (e.g., `record`, `bank`, `lead`), map common senses and part-of-speech differences; prioritize a user-provided context. Avoid treating unrelated senses as identical.
- Use natural, original example sentences with faithful Chinese translations. Never label generated examples as corpus quotations, or fabricate source, frequency, etymology, citation, historical status, or dialect authority.
- Note pragmatic or discourse behaviours only when genuinely associated with the word or provide an accurately labelled context-level illustration; generic cultural stereotypes are disallowed.
- Explain that coverage does not prove mastery. Recall prompts are complementary, not automatic flashcard exports or spaced-scheduling guarantees.
- Maintain portable Markdown with only required YAML fields and `$ARGUMENTS`, `## Output Format`; no tools, dependencies, secrets, or persistent profile.

## Compatibility and tradeoffs

- The chosen comprehensive profile can be long for common words; that verbosity is an intentional user-selected tradeoff. Do not switch to adaptive/quick mode implicitly.
- No changes to existing skill contracts, install.sh, or CI validator. Adding a new skills directory integrates with the current installer.
- Update README skill table, command enumeration, dedicated `cp` example, usage, and skill details.
- Keep `SKILL.md` under 300 lines when feasible. Store worked examples in change-local documentation for reviewers, not as mandatory runtime prompt content.

## Verification and evals

- Add `tests/evals/skills/vocabulary-mastery/cases.yaml` with normal, indirect-trigger, and edge/failure/non-trigger cases covering all ten bilingual sections, polysemy, weak-dimension honesty, pronunciation confidence, grammatical frames, and skill routing.
- Include a bilingual worked example for `record` and a boundary example for `apple`.
- Verify `python -m unittest discover tests`, `python tests/validate_skills.py`, and `python tests/check_readme_sync.py`.
- Static evals document observable expectations, **not** live-model pass rates; document any skipped live-model testing.
