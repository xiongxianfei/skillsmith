# Bilingual vocabulary mastery: comprehensive ten-domain reference

## Status and rationale

Revision of the 2026-10-18 requirements for PR #35. The user selected **Option A: two complete, separate output versions**. The reusable skill file itself must be written **entirely in English**. Existing `editor`, `language-tutor`, and `flashcard-generator` remain unchanged.

## Trigger intent and accepted input

- Name: `vocabulary-mastery`; slash command: `/vocabulary-mastery`.
- Accept one English headword or fixed lexical expression from `$ARGUMENTS`, optionally with a usage sentence, target sense, learner goals, or BrE/AmE preference.
- Trigger for a comprehensive lexical/linguistic reference request, including indirect requests about the word's sounds, structure, meanings, syntax, and communicative use.
- Do not hijack ordinary proofreading, writing correction, conversation tutoring, quiz-only tasks, or flashcard export.
- If the target is missing, ask for the word. For several unrelated targets, request one word rather than create incomplete multiword profiles.

## Instruction-language constraint

- **Every line of `skills/vocabulary-mastery/SKILL.md` must be English-only**, including frontmatter, directions, headings, labels, comments, templates, and placeholder descriptions.
- The instruction file must contain no Chinese characters. Chinese-language output is controlled by clear English instructions and English-language placeholder labels.
- Chinese example text, Chinese headings, and Chinese translations belong in **generated output** and reviewer-facing examples, not the English-only skill source.

## Fixed output contract

For any accepted lexical target, produce **two complete standalone references** in sequence, never an interleaved bilingual reference or parallel-column table:

1. **Part 1: English Reference**: complete English-only explanatory prose, heading labels, examples, recall questions, and answer key.
2. **Part 2: Simplified Chinese Reference**: a complete, independently readable Simplified Chinese explanation with naturally translated Chinese heading labels, recall questions and answers. Original English headword, quoted target forms, IPA and original example sentences may appear as linguistic evidence, with faithful Chinese interpretation/translation beside each English example.

**Each part must independently include:**
- Word Overview: headword, part of speech, up to three major senses, reliably variety-labelled IPA, context focus.
- **Ten** numbered dimensions, always in this order: Phonetics, Phonology, Morphology, Lexicon, Syntax, Semantics, Pragmatics, Discourse, Information Structure, Prosody.
- For every dimension, substantive explanation and an original, natural usage illustration when supportable. If no distinctive word-level phenomenon exists, explicitly say so within **that version** and optionally show a correctly labelled general illustration.
- Knowledge Connections: two or three supported cross-domain connections.
- Exactly three recall questions and a corresponding three-answer key.
- Accuracy Notes only when uncertainty, pronunciation evidence, or variety caveats require them.

The Chinese part must not reference the English part ("as above"/"see Part 1") or omit sections as a shortcut. Match sense selection, part-of-speech distinctions, IPA and accent labels, morphological forms, grammatical frames, semantic nuances, examples, focus contrasts, uncertainty, and question/answer content **across both versions**. Preserve English example sentences in the Chinese part and add faithful Chinese translations. Both versions should be similarly informative, even though their wording need not be literal translations.

## Linguistic evidence and boundary rules

- Phonetics describes sound segments/articulation; phonology describes syllables, lexical stress and sound-system contrasts; prosody describes phrase-level rhythm, intonation, prominence. Separate lexical stress from sentence-level focus.
- Reference pronunciation is not learner-performance evidence. Label confident IPA BrE or AmE; never infer an actual user's pronunciation from text or claim to have heard audio that is not available.
- Morphology must use real inflection and derivation, not inferred etymologies or fabricated roots. Lexicon covers collocations and lexical relations; syntax covers grammatical frames; semantics covers distinct senses.
- Pragmatics needs communicative context; discourse needs cross-sentence/turn linkage; information structure concerns given/new and focus. Distinctive phenomena must not be invented simply because all ten headings are mandatory.
- All examples are original unless a real cited source is available. Do not claim corpus verification, frequency ranking, invented idioms, historical claims, accent superiority, or universal regional usage.
- Ensure English examples are accurately translated into Chinese without collapsing important sense differences.
- A comprehensive two-part article is intentionally long for familiar words; the user explicitly selected this tradeoff. Do not silently switch to quick/adaptive or mixed-language single-entry format.

## Architecture and compatibility

- Portable Markdown skill; only required YAML fields, `$ARGUMENTS`, and `## Output Format`; no new tools or runtime dependencies.
- `/editor` remains for prose editing, `/language-tutor` for interactive practice, and `/flashcard-generator` for card or TSV export.
- No installer changes; the existing installer copies all skill directories.
- Update the README skill table, user-facing usage examples and skill details to describe two separate output versions.
- A deterministic unit test guards the English-only skill source and two complete ten-dimension templates.

## Verification and evals

- Static fixtures under `tests/evals/skills/vocabulary-mastery/cases.yaml` include normal, indirect, edge, missing-input, sense selection, homograph, morphology, separable particle, coinage, non-trigger, and two-version parity cases.
- `docs/changes/2026-10-18-bilingual-vocabulary-mastery/examples.md` demonstrates a **full English record profile followed by a full Chinese record profile**, plus honest weak-dimension handling for `apple`.
- Run `python -m unittest discover tests`, `python tests/validate_skills.py`, and `python tests/check_readme_sync.py`; use CI where local checkout is inaccessible.
- Static fixtures and deterministic tests are **not** evidence that a language model reliably produces accurate, equivalent bilingual explanations. Live-model testing must be reported separately.
