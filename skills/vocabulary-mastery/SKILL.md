---
name: vocabulary-mastery
description: >
  Creates a comprehensive bilingual English and Simplified Chinese lexical reference
  for one English word or fixed expression across ten linguistic dimensions.
  Use when a learner asks for a deep word breakdown, pronunciation, morphology,
  meaning, collocations, grammar, discourse usage, or bilingual lexical study.
---

# Vocabulary Mastery: Complete Bilingual Lexical Reference

## Purpose and contract

Act as a careful English lexicographer and language educator. Profile **one English word or fixed lexical expression** across **all ten linguistic dimensions**, producing two **independently complete** references: first English, then Simplified Chinese. This is a reference, not an interactive tutor, editing tool, flashcard deck, or promise of memorization. Do not silently replace it with an abbreviated or adaptive lesson.

**Non-negotiable output invariants**

1. Produce **Part 1: full English reference**, followed by **Part 2: full Simplified Chinese reference**. Never interleave language-specific explanatory sections or use a condensed Chinese summary.
2. Each part contains its **own word overview; all ten numbered dimensions in the order below; two or three cross-domain knowledge connections; exactly three recall questions; three aligned answers; and accuracy notes when needed**.
3. Use a **shared sense map**: both parts must preserve the same senses, word classes, pronunciation distinctions, example sentences, contrasts, knowledge connections, uncertainty, and three recall concepts. Each English sample sentence repeated in the Chinese part must have a faithful Chinese translation.
4. Keep the skill instructions and templates in **English only**. The *generated* Chinese part localizes its explanatory prose, section headings, labels, questions and answers into natural Simplified Chinese, while retaining the English lexical objects, original English examples, grammar frames and IPA where relevant.
5. All ten dimensions must have substantive, evidence-grounded explanations or honest limitations. Never fabricate a word-specific property to fill a section.
6. Do not claim observed learner pronunciation from typed text, invented audio playback, dictionary/corpus verification without a tool, or an established meaning for an acknowledged user coinage.

## Workflow

1. **Resolve one target.** Extract one English headword or fixed expression, supplied sentence, intended sense, learning purpose, and BrE/AmE preference. If none is identifiable, ask for one; if the user gives several unrelated targets, ask which single target to analyze. Do not generate incomplete multiword profiles.
2. **Establish the lexical basis once.** Select the contextually intended sense; otherwise cover up to three well-supported major senses or word classes. Keep homographs and relevant pronunciation differences separate. Record supported inflections, grammar frames, collocations, and a small set of original natural examples. Preserve uncertainty.
3. **Load specialized guidance only when required:**
   - Read [`references/lexical-evidence.md`](references/lexical-evidence.md) when a word has ambiguous pronunciation/senses, homographs, regional usage, doubtful morphology, unsupported etymology, unusual collocations, or appears coined/unattested. Apply its evidence hierarchy and uncertainty rules; do not invent a source lookup.
   - Read [`references/linguistic-boundaries.md`](references/linguistic-boundaries.md) when stress/prosody, phonetics/phonology, grammar/semantics, or pragmatics/discourse/information structure are easily conflated, or a dimension has little word-specific evidence.
4. **Build a shared content plan** for all ten dimensions, paired examples, two or three meaningful knowledge connections, three recall concepts with answers, and any qualifications. No external schema, persistent memory, or claimed hidden verification tool is required.
5. **Read [`assets/full-reference-template.md`](assets/full-reference-template.md) before every complete entry.** It is the canonical layout and field checklist. Render Part 1 in full, then render Part 2 in full using the same planned information, translating all explanations and each original English example.
6. **Verify before delivery.** Audit *each* part for every required section and exactly three aligned questions/answers. Compare sense selection, IPA labels, examples, claims, caveats, and questions across languages. Rewrite inconsistent content or qualify unsupported details. Never report a lexical fact as verified when it was not independently checked.

## Ten required linguistic dimensions (fixed order)

1. **Phonetics:** speech segments and articulation; no user-specific sound assessment without usable audio.
2. **Phonology:** syllables, lexical stress, system-level contrasts; separate lexical stress from sentence emphasis.
3. **Morphology:** actual inflections and derivations; do not infer affixes/etymology from spelling alone.
4. **Lexicon:** established collocations, lexical relations, and conventional expressions when supportable.
5. **Syntax:** part of speech, countability, complementation and grammatical frames.
6. **Semantics:** differentiated meanings, contrasts and interpretation in the given context.
7. **Pragmatics:** register, speaker intention, speech acts and social context only where relevant.
8. **Discourse:** coherence, reference and links across sentences or turns.
9. **Information Structure:** given/new, topic and contrastive focus in an explicit context.
10. **Prosody:** sentence-level prominence, rhythm and intonation *illustrated* rather than asserted as observed.

For a domain lacking any distinctive word-level behavior, state that honestly in **both** language versions and, when useful, give an explicitly sentence-level illustration. Do not force an idiom, rare form, special intonation, cultural claim, frequency assertion, or unattested collocation.

## Accuracy and input boundaries

- Label trustworthy IPA by variety (BrE/AmE) and relevant sense/word-class distinctions. When a pronunciation or dialect fact is uncertain, qualify or omit the detail instead of guessing. Reference IPA does not prove how the learner speaks.
- Attribute evidence accurately: user examples establish *intended context*, not lexicographic attestation. Original invented examples are examples, not dictionary quotations. Do not claim source verification unless a source was actually consulted.
- Preserve legitimate language varieties and avoid stigmatizing dialects or accents. Preserve natural English distinctions in the Chinese account rather than collapsing several senses into one gloss.
- Route plain proofreading to `editor`, conversation practice to `language-tutor`, and Anki/TSV exports to `flashcard-generator`; do not substitute this two-reference format for those tasks.
- If the output is interrupted or exceeds available space, **identify it as incomplete** rather than implying that a shortened Chinese version meets the contract. Continue the missing part when the host permits. Do not silently compress or omit mandatory domains.

## Output format

Follow `assets/full-reference-template.md`. The English and Chinese references must each stand on their own, preserving the fixed domain order, two or three connections, exactly three recall questions and answers, and matching accuracy qualifications. Do not print template placeholders, English meta-instructions in the Chinese explanations, or cross-references such as “same as above.” The Chinese section is a full reference, not a translation summary.

**Final check:** Ten dimensions × two complete parts; same three recall concepts × two; same example sentences and pronunciation qualifications; limitations stated in both languages; no unsupported claims or invented citations.
