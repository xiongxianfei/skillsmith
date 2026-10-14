# Editor: linguistics-aware learning notes

## Status

Proposed for this change (2026-10-14). Scope: improve the existing `editor` skill rather than introduce a competing language-tutor skill.

## Goal and accepted input

Enhance the default learning notes produced when a user asks to edit, proofread, polish, rewrite, or translate their **own writing or speech**. Accepted source material is written text, a speech transcript, or audio actually available to the assistant. A missing or unreadable source must prompt for usable input rather than invented analysis.

## Observable requirements

1. Preserve the existing editor's fidelity, refusal/integrity safeguards, source-language-plus-companion-language default, explicit target-language overrides, and explicit no-notes/target-only overrides.
2. Edit before teaching. Produce the corrected deliverable in the established language blocks, then up to three high-value learning notes by default; more only where genuinely distinct lessons warrant them. No mandatory exercise or new default top-level sections.
3. Select relevant domains rather than emit a ten-part checklist: phonetics, phonology, morphology, lexicon, syntax, semantics, pragmatics, discourse, information structure, and prosody. Each substantive note must cite a real source-to-revision change or evidence-backed translation decision, identify its relevant domain(s), explain why, and teach a transferable pattern; include a short example only when it clarifies the lesson.
4. Prioritize errors that affect meaning, communication, or recur in available samples. Adapt depth to explicit learner goals and demonstrated patterns without diagnosing ability or assuming a native language. Repeated-error claims require available history; no persistent learner storage is implied.
5. Distinguish factual/grammatical corrections from optional choices of register and style. Preserve intentional dialect, code-switching, jargon, disfluency, and author voice as appropriate.
6. Text/transcripts can support morphology, lexicon, syntax, semantics, pragmatics, discourse, and information structure. **Phonetics, phonology, and prosody require usable audio** for claims about a person's actual production. If audio is missing, inaccessible, or unclear, avoid unsupported pronunciation/intonation judgments; clearly distinguish uncertain transcription from learner mistakes.
7. Do not fabricate mistakes or lessons for clear text. Preserve the current one-note fallback when no substantive learning principle is evidenced. Obey explicit note suppression.
8. When the user explicitly wants practice, offer a brief, targeted exercise connected to an observed pattern; otherwise do not add practice to the default output.

## Examples and expected outcomes

- User: "Please fix: I want to refine editor skill. when it can give the learn notes from language lingusitics." Expected: faithful English revision, Chinese default companion, and one to three evidence-backed notes, e.g., `when` versus `so that` for purpose (syntax/semantics), and `learn notes` versus `learning notes` (morphology/lexicon).
- User: "Here is a transcript of my meeting. Analyse my pronunciation." Expected: no claim about the speaker's phonemes, stress, or intonation based solely on the transcript; optionally request audio for pronunciation analysis while still giving text-grounded edits.
- User: "Only translate this into French. No notes." Expected: only the requested translation, without learning notes or source-language output.
- User: "This sentence is correct; just check it." Expected: restraint and the existing concise fallback note, not invented linguistic diagnoses.

## Compatibility and safety boundaries

This is a **material** enhancement to `skills/editor/SKILL.md` with no runtime dependencies, no new tools, and no change to the install path or slash command (`/editor`). The sibling `language-tutor` remains a broader lesson/practice skill. The editor remains an editing/translation skill that teaches from the user's actual edits. Do not overgeneralize across languages, stigmatize accents or dialects, infer protected traits, or add unsupported linguistic judgments.

## Validation plan

- Extend `tests/evals/skills/editor/cases.yaml` with normal, indirect-trigger, text-only/audio-evidence boundary, personalisation, restraint, and suppression scenarios.
- Run `python tests/validate_skills.py`, `python tests/check_readme_sync.py`, and `python -m unittest discover tests`.
- Inspect the PR diff and GitHub Actions check status. Static eval fixtures define observable expectations; they are **not** evidence of live-model pass rates.
