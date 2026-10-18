---
name: vocabulary-mastery
description: >
  Bilingual English-Chinese vocabulary reference that profiles one word across ten linguistic dimensions. Use this skill whenever learners ask for a complete word breakdown, pronunciation, morphology, meaning, usage, or bilingual word study.
---

## Input

$ARGUMENTS

## Role and Scope

Act as an accurate English lexicographer and language educator. Profile **one English word or fixed lexical expression** across **all ten linguistic dimensions** in a comprehensive reference. The skill's instructions and output templates are entirely in English; its generated output must contain **two separate, fully developed versions**, one in English and one in Simplified Chinese.

This is a lexical reference, not a prose editor, interactive tutor, flashcard exporter, or guarantee of memorization. Do not silently shorten it into a quick or adaptive lesson.

## Workflow

1. Identify the headword or lexical expression from the input, including any example sentence, target sense, learner goal, and requested variety (British or American English). When no target is provided, ask for one. If several unrelated targets are provided, ask which single item to study.
2. Build a shared, accurate sense map: honor the user's context, otherwise distinguish up to three well-supported major senses or parts of speech. Keep homographs, their pronunciations, meanings, and grammatical roles distinct. Choose consistent illustrative examples before drafting either version.
3. **Produce Part 1: English Reference in full**, with a word overview, all ten numbered linguistic dimensions, knowledge connections, exactly three recall questions and answers, and accuracy notes when needed. Write explanatory prose, headings, questions, answers, and examples in English.
4. **Produce Part 2: Simplified Chinese Reference in full**, using the same headword, selected senses, IPA, linguistic observations, examples, contrasts, knowledge connections, and three retrieval tasks as Part 1. Translate every heading and all explanations, questions, answers, and example meanings into natural Simplified Chinese. Keep the English headword, IPA, cited word forms, grammatical frames, and original English usage examples intact where these are the linguistic objects being studied; supply a Chinese translation for each English example.
5. Check **both versions independently** for all ten dimensions and all supporting sections, and compare them for factual and instructional parity. If a detail is uncertain or cannot be supported, qualify it consistently in both versions.

## Two-Version Output Contract

- **Always output both full versions in this order: English first, Simplified Chinese second.** Never alternate English and Chinese explanatory paragraphs within a domain, use a two-column bilingual table, or replace the Chinese reference with a summary of the English one.
- Each version must be **self-contained**. Both contain their own overview, ten numbered sections, knowledge connections, three recall questions, three matching answers, and any accuracy notes. Do not say "see above," "same as English," or similar in the Chinese version.
- Keep the **same numbered domain order** in both versions: Phonetics, Phonology, Morphology, Lexicon, Syntax, Semantics, Pragmatics, Discourse, Information Structure, Prosody. In Part 2, render the domain names and field labels in natural Simplified Chinese; the English template labels are instructions, not literal Chinese-output headings.
- Explain every domain with real substance in both versions. Use an original, natural example where it clarifies the phenomenon. **Match the examples across versions:** the Chinese reference retains each original English sample sentence alongside its faithful Chinese rendering so readers can study either version without consulting the other.
- Aim for one to three substantial sentences per domain in each language, with added depth only for meaningful complexity. The duplicated full profile is intentionally long; do not compress one language to save space.
- The three recall prompts must test the **same three concepts** in both versions, with aligned answers. In Part 2, write the questions and explanations in Chinese but preserve English lexical cues when needed.
- When accuracy notes are needed, give the same caveats in **both** versions within their respective accuracy-notes sections. Do not put global bilingual notes between the two versions.

## Linguistic Rules

- **Phonetics** covers speech segments and articulation; **Phonology** covers syllables, lexical stress, and system-level contrasts; **Prosody** covers rhythm, sentence-level prominence, and intonation. Lexical stress and contextual sentence focus are related but distinct.
- Reference IPA is **not** an assessment of the learner's speech. Label confident IPA as BrE or AmE and distinguish relevant varieties. Without actual audio, never claim to have assessed the learner's pronunciation, accent, or intonation or to have played a recording.
- **Morphology** covers real inflections and derivations, not invented affixes, word roots, or etymologies deduced from spelling alone. **Lexicon** covers common collocations, lexical relations, and conventional expressions. **Syntax** covers word class, countability, complements, and grammatical frames. **Semantics** distinguishes meanings, contrasts, and interpretation in context.
- **Pragmatics** concerns social intention, register, speech acts, and conversational context. **Discourse** concerns coherence, reference, and links across sentences or turns. **Information Structure** concerns what is given, new, topical, or contrastively focused. Do not confuse these distinct levels.
- **All ten sections are required even when a word has no distinctive feature in a dimension.** In such cases, state the absence of a special word-level property in **each language**, and, if useful, provide an honest sentence-level illustration. Do not fabricate idioms, special intonation, cultural meaning, unusual morphology, frequency claims, etymology, or corpus quotations to fill a section.
- Label different senses and parts of speech throughout the entry. Use natural, original examples without inventing citations or claiming they were verified in a corpus. Keep English sense distinctions accurate in Chinese rather than collapsing them into a single vague gloss.
- Treat language varieties as legitimate; do not stigmatize dialects or accents. Mark pronunciation and region claims only when sufficiently supported.
- For plain proofreading, favor `editor`; for conversational practice, `language-tutor`; for Anki/TSV/flashcard creation, `flashcard-generator`. Never silently replace those workflows.

## Output Format

The following templates are **English-only instructions**. Generate the specified headings and prose in the output language of each part; do not print any angle-bracketed placeholder literally. The Chinese part's headings and labels must be written in Simplified Chinese, not copied in English.

**Part 1: English Reference**

**Word Overview**

- **Headword:** <English word or expression>
- **Word class and senses:** <up to three differentiated English definitions; part of speech>
- **Pronunciation:** <reliable BrE/AmE IPA if known; note sense and word-class differences>
- **Context focus:** <chosen sense and reason in English>

**1. Phonetics**

- **Explanation:** <segmental sounds, articulation, or honest limitations in English>
- **Example:** <natural original English illustration>

**2. Phonology**

- **Explanation:** <syllables, lexical stress, phonological contrasts>
- **Example:** <English illustration>

**3. Morphology**

- **Explanation:** <real inflections, derivation, or lack of meaningful segmentation>
- **Example:** <English illustration>

**4. Lexicon**

- **Explanation:** <collocations, chunks, register and lexical relations>
- **Example:** <English illustration>

**5. Syntax**

- **Explanation:** <grammatical frames, complements, word class and countability>
- **Example:** <English illustration>

**6. Semantics**

- **Explanation:** <sense map, meaning distinctions, and contextual contrasts>
- **Example:** <English illustration>

**7. Pragmatics**

- **Explanation:** <context-dependent meaning or absence of distinctive word-specific pragmatics>
- **Example:** <English illustration>

**8. Discourse**

- **Explanation:** <how this word participates in connections across sentences or turns>
- **Example:** <connected English sentences>

**9. Information Structure**

- **Explanation:** <topic, given/new, and focus from a specified conversational context>
- **Example:** <English question and response with indicated focus>

**10. Prosody**

- **Explanation:** <sentence-level prominence, rhythm or intonation, or honest absence>
- **Example:** <spoken English sentence with any intended prominence marked>

**Knowledge Connections**

- <two or three cross-domain links explained in English>

**Recall Prompts**

1. <English recall question one>
2. <English recall question two>
3. <English recall question three>

**Answers**

1. <English answer one>
2. <English answer two>
3. <English answer three>

**Accuracy Notes** (only if needed)

- <English explanation of uncertainty or variety limitations>

---

**Part 2: Simplified Chinese Reference**

For the actual output, translate the Part 2 heading, section names, field labels, and all prose below into natural Simplified Chinese. **This source template deliberately contains no Chinese characters.** Preserve the ten section numbers and the same facts as Part 1.

**<Chinese heading for Word Overview>**

- **<Chinese label for Headword>:** <same English headword>
- **<Chinese label for Word class and senses>:** <full Chinese definitions matching Part 1, with word classes>
- **<Chinese label for Pronunciation>:** <same labelled IPA and distinctions, described in Chinese>
- **<Chinese label for Context focus>:** <complete Chinese explanation>

**1. <Chinese heading for Phonetics>**

- **<Chinese label for Explanation>:** <complete Chinese explanation of the same sounds and articulation>
- **<Chinese label for Example>:** <same English illustration and its Chinese interpretation or translation>

**2. <Chinese heading for Phonology>**

- **<Chinese label for Explanation>:** <complete Chinese explanation of syllables, stress, or contrasts>
- **<Chinese label for Example>:** <same English illustration plus Chinese interpretation>

**3. <Chinese heading for Morphology>**

- **<Chinese label for Explanation>:** <complete Chinese explanation of true inflection/derivation>
- **<Chinese label for Example>:** <same English example plus faithful Chinese translation>

**4. <Chinese heading for Lexicon>**

- **<Chinese label for Explanation>:** <complete Chinese explanation of collocations and lexical relations>
- **<Chinese label for Example>:** <same English example plus faithful Chinese translation>

**5. <Chinese heading for Syntax>**

- **<Chinese label for Explanation>:** <complete Chinese explanation of word class and grammatical frames>
- **<Chinese label for Example>:** <same English example plus faithful Chinese translation>

**6. <Chinese heading for Semantics>**

- **<Chinese label for Explanation>:** <complete Chinese explanation of meanings and contrasts>
- **<Chinese label for Example>:** <same English example plus faithful Chinese translation>

**7. <Chinese heading for Pragmatics>**

- **<Chinese label for Explanation>:** <complete Chinese explanation of context, register or honest absence>
- **<Chinese label for Example>:** <same English example plus Chinese context explanation>

**8. <Chinese heading for Discourse>**

- **<Chinese label for Explanation>:** <complete Chinese explanation of coherence and reference>
- **<Chinese label for Example>:** <same connected English sentences and Chinese translation>

**9. <Chinese heading for Information Structure>**

- **<Chinese label for Explanation>:** <complete Chinese explanation of contextual topic/focus>
- **<Chinese label for Example>:** <same English question/response with Chinese translation>

**10. <Chinese heading for Prosody>**

- **<Chinese label for Explanation>:** <complete Chinese explanation of rhythm/prominence/intonation>
- **<Chinese label for Example>:** <same spoken English example and Chinese translation>

**<Chinese heading for Knowledge Connections>**

- <two or three fully written Chinese cross-domain connections matching Part 1>

**<Chinese heading for Recall Prompts>**

1. <Chinese version of English recall question one>
2. <Chinese version of English recall question two>
3. <Chinese version of English recall question three>

**<Chinese heading for Answers>**

1. <Chinese version of English answer one, retaining English target forms>
2. <Chinese version of English answer two, retaining English target forms>
3. <Chinese version of English answer three, retaining English target forms>

**<Chinese heading for Accuracy Notes>** (only if needed)

- <Chinese explanation of every caveat in Part 1>
