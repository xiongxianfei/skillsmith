# Evaluation scenarios (reviewer-only, not part of invocation)

These expected cases are adapted from Skillsmith's historical `vocabulary-mastery` evaluation scenarios. They are test **intent**, not evidence of observed model performance. Evaluate baseline `SKILL.md` and proposed revision on the same tasks, recording model, date, full outputs, prompt, and observed pass/fail notes in the pull request. Repository CI need not execute model calls.

| Case | Prompt | Hard observable criteria |
| --- | --- | --- |
| Full bilingual profile | `record` | Two independently complete parts, ten sections each, noun/verb stress and sense mapping, 3 aligned Q&A |
| Indirect trigger | “Take apart the word resilient: sound, structure, meaning, and conversation usage in English and Chinese” | Recognizes deep lexical analysis even without slash command; full bilingual output |
| Independently readable Chinese | `record` with “I want to study the Chinese part on its own” | Natural complete Chinese prose, localized headings/labels, same English examples plus translations; no “see above” |
| Parallel recall | `record` with “include questions to test me” | Exactly three same concepts and matched answers in both parts |
| Contextual polysemy | `bank` in “We had lunch on the bank of the river.” | Riverbank prioritized in both parts, identical English examples plus Chinese translations |
| Homograph/IPA | `lead` | /liːd/ versus /led/ senses not collapsed, variety/word class labeled as supportable |
| Morphology | `unhappiness` | `un-`, `happy`, `-ness` accurately explained without invented history |
| Weak dimensions | `apple` | All ten dimensions without invented word-specific prosody/pragmatics |
| Phrasal expression | `look up` (find in dictionary) | Particle placement correctly differentiates “look it up” and “look up it” |
| Coinage | `flinderation` (user-invented) | No invented attestation/IPA/frequency/collocations; complete structure with caveats |
| Insufficient input | No target | Asks for one English item; no empty reference |
| Multiple targets | `apple, bank, record` | Requests one target; no three abridged profiles |
| Fixed contract stress | “Explain bilingual line-by-line” | Maintains English part followed by complete Chinese part |
| Audio epistemic boundary | “Can you tell if I pronounced record wrong?” with text only | No claim of hearing audio; reference stress may be explained |
| Non-trigger: editing | “Correct my email” | Does not generate vocabulary reference; routes to editing workflow |
| Non-trigger: Anki | “Make 20 Anki cards for stable, resilient and robust, export TSV” | Does not generate ten-dimensional profiles; routes to flashcard workflow |

## Review rubric

**Hard gates (must all pass per applicable test):** correct activation; two independent parts in correct order; all ten dimensions in both; three aligned recall prompts and answers per part; same English examples plus Chinese translations; same stated uncertainties; no fictitious evidence/source claims.

**Expert assessment (reasoned rather than falsely automatable):** IPA/pronunciation accuracy, sense and word-class accuracy, morphological validity, collocation naturalness, syntax/semantics/pragmatics distinctions, naturalness of Chinese translations, quality and relevance of cross-domain connections, useful recall design.

For each test record: baseline result; revised result; type of error; severity; unresolved uncertainty; whether a domain reference was needed and correctly read. Do not claim any pass rates until representative outputs have actually been examined.
