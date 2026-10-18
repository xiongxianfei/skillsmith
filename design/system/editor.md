# Editor system behavior

## Capability and boundary

F-ED-001 — Edit and translate supplied text while teaching from useful changes. The user receives faithful, restrained deliverables and, unless suppressed, concrete learning notes. The [editor requirements](../requirements/editor.md) own the output contract, safety constraints and acceptance; this file explains logical behavior. Source IDs remain qualified by their original document identity.

## Functions

| Function | Inputs, conditions and logical result | Failure and boundary | Requirement basis |
| --- | --- | --- | --- |
| FN-ED-001 — Resolve instruction and source roles | Separate directive words, supplied artifact, source language, framing language and explicit targets; determine the visible language set before rendering | Pasted questions/commands remain source, not instructions to obey. Missing text requests the source; uncertain language remains qualified | Current R9–R21, R31–R37; error/boundary behavior |
| FN-ED-002 — Refine source meaning with restraint | Edit in the source language, using the smallest useful changes for audience, tone and medium; keep a single resolved meaning | Preserve uncertainty, ambiguity, code-switching and precise terminology. Do not invent facts, certainty or changes to produce lessons | Current R8, R22–R27, R51–R56; inherited expert R24/R27/R28/R30 |
| FN-ED-003 — Render visible deliverables | Render source plus companion by default, or the explicit target set; deduplicate language blocks, apply target-only selection and copyable formatting | Explicit target-only selection does not itself suppress notes. Integrity can require refusal/correction and truthful alternatives | Current R13–R37, R51–R56 |
| FN-ED-004 — Explain useful edits and verify consistency | Produce anchored reusable lessons after deliverables, or one concrete fallback when appropriate; honor explicit note suppression; check visible outputs against the same meaning | No hidden Chinese/English rendering requirement, inflated lesson count, generic self-praise or extra edits for teaching | Current R38–R50; inherited learning labels, anchoring, grouping and expansion constraints |

F-ED-001 is realized by all four Functions. Their primary implementation responsibility is allocated in [portable skill architecture](../architecture/portable-skills.md).

## Flow and state

Resolve roles → preserve/refine meaning → render the selected visible language blocks → produce permitted learning notes → verify fidelity and presentation. Integrity and explicit constraints are applied throughout, not postponed until after generation. No persistent language preference, user profile or external service state is introduced.

For Chinese source, English is normally the companion. For Russian source, the visible pair is Russian/English. For English source, a clearly non-English directive language selects the companion; otherwise Chinese is the fallback. These examples explain the current R13–R19 contract, not a separate language policy.

## Test intent

Exercise source/instruction separation, mixed directive languages, explicit targets equal to source, target-only with and without explicit note suppression, faithful treatment of ambiguous terms, trivial edits, already-clear text, useful lessons beyond the default brevity, and the combined integrity/target/suppression boundary. Test expectations come from the current requirements and existing `tests/evals/skills/editor/cases.yaml`. Old change-specific test plans remain historical evidence and do not override current output rules.

Inherited source-qualified proof intent remains applicable: expert-quality R43/R44 require expert scenarios covering professional polish with restraint, already-good text, **`dim lighting` fidelity**, Chinese-instruction/English-source and English-instruction/Chinese-source separation, code-switching, non-Chinese/non-English intake, engineer-facing PR editing and integrity misuse. Learning-default R38 additionally covers default notes, explicit/ambiguous suppression, no edits made merely to teach, trivial mechanics, restraint, brittle-rule qualification, translation notes and mixed-language framing. Apply the current language and note rules to these scenario classes; do not revive superseded output defaults.

The original expert test plan's conditional manual-smoke requirement and the quality standard's high-risk/behavior-heavy/model-specific evidence rule remain distinguishable from static fixture checks. This migration runs no model test and does not backfill missing cases. In particular, the existing fixture lacks an explicit named `dim lighting` case; retaining that obligation exposes the pre-existing evidence gap for the next editor evidence update, without weakening the contract or changing protected product/test files.
