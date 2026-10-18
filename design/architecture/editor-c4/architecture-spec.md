# Editor C4 architecture and implementation profile

This is an implementation-grounded design for reviewing the editor's boundaries and behavior. The editor delivers faithful editing/translation with grounded learning notes. It is distributed as one Markdown prompt interpreted by an external assistant host. The C4 views expose that real boundary; the decision tables below explain the prompt's logical policies without inventing services.

**Status:** authored for human architecture review; no human approval recorded. “Implemented” below means instructions exist in the prompt, not that a model has demonstrated compliance. Proposed corrections remain separate and do not change the prompt.

## Scope, evidence and authority

| Subject | Owning artifact | Treatment here |
| --- | --- | --- |
| Prior editor contract | [Historical requirements](https://github.com/xiongxianfei/skillsmith/blob/93c9bf750ceea7585c06fd93fcceecac5f7e8d26/design/requirements/editor.md) | Source-qualified R/AC/EC IDs retain provenance; this layout change does not alter behavior |
| Linguistic-learning requirement draft | [October 14 requirements](https://github.com/xiongxianfei/skillsmith/blob/1d6ce5bee418b59fcfdd4a8cc98304a491e3e49a/docs/changes/2026-10-14-editor-linguistic-learning-notes/requirements.md) | Proposed scope for speech evidence, selective linguistic teaching and requested practice; this records provenance, not new acceptance |
| Prior logical decomposition | [Historical system design](https://github.com/xiongxianfei/skillsmith/blob/93c9bf750ceea7585c06fd93fcceecac5f7e8d26/design/system/editor.md) | FN-ED-001–004 remain trace labels for the behavior documented below |
| Module and Interface allocation | [Portable-skill architecture](../portable-skills.md) | All editor Functions remain MOD-PROMPT through IF-PROMPT; MOD-QUALITY and MOD-REVIEW are maintenance responsibilities |
| Current implementation | [Editor SKILL.md](../../../skills/editor/SKILL.md) | Core Standard; Workflow; Learning Notes; Output Format |
| Expected examples | [Editor eval scenarios](../../../tests/evals/skills/editor/cases.yaml) | Scenario declarations, not execution logs |
| Diagram entities and relationships | [model.d2](model.d2) | Single source for C4 identity; C1/C2 filter it, sequences reuse its participants |

The user requested C4 after asking for concrete design from implementation. This bounded work preserves current prompt behavior. This specification now holds the current design context, behavior and open decisions together. Speech and richer linguistic teaching extend the historical contract; they remain observations requiring human review, not silently approved amendments.

## C4 interpretation and boundaries

C1 models `editor_package` as a **passive software distribution**, not an independently executing product. The writer uses `assistant_host`, an external software system; the maintainer authors the package. The package supplies instructions by installation or paste, not through a running API. This is an explicit adaptation for a prompt-only product.

C2 opens that package to show its one genuine data container, `editor_package.prompt_files`: the Markdown file store. A filesystem store is a C4 container; a workflow step is not. The externally owned assistant stays opaque. Its UI, model service, authentication, network transport and storage topology are not established by this repository. The diagram neither collapses a known distributed host into one container nor invents host internals.

| Stable diagram ID | Type and ownership | Responsibility / existing model relationship |
| --- | --- | --- |
| `writer` | Person, outside package | Supplies source, instructions and preferences; receives output |
| `maintainer` | Person, outside invocation | Authors/reviews instructions and evidence using shared development methods |
| `editor_package` | Passive software system scope, Skillsmith-owned instructions | Distribution boundary for editor behavior |
| `editor_package.prompt_files` | File-store container, Skillsmith-authored Markdown | Realizes editor's part of MOD-PROMPT; no mutable learner data |
| `assistant_host` | External software system, host operator | Interprets IF-PROMPT and generates output; capabilities and execution depend on selected host |

C3 is omitted: one prompt file does not establish independently implemented editor components. Self-messages in sequence views describe logical instructions inside the host, not callable functions, hidden reasoning transcripts, or an enforced program pipeline. A deployment diagram is omitted because no specific host/deployment has been selected. No impactful runtime choice is introduced, so no new ADR is needed for a service/database decision.

This mapping follows the [C4 container definition](https://c4model.com/diagrams/container) and [D2 model/view selection](https://d2lang.com/tour/models/). [D2 sequences](https://d2lang.com/tour/sequence-diagrams/) supply ordered scenario views. The package boundary is an interpretation of this repository, not a claim that C4 defines a special prompt-runtime abstraction.

## Request interpretation: FN-ED-001

The following is a documentation model of the decisions required by the prompt. There is no parser, stored request object or new schema in the implementation.

| Decision | Derived from | Result and boundary |
| --- | --- | --- |
| Task and source | `$ARGUMENTS`, available content | Editing, polishing, translation or transcript correction; quoted commands remain source |
| Evidence modality | Readable text, transcript, accessible audio | Missing usable material leads to a request for source and no learning notes |
| Source language | Source material, respecting code-switching | Primary source language; broad intake is not equal-quality assurance |
| Instruction language | Directive words, excluding source snippets | Used for framing and English-source companion selection |
| Framing language | Clear instruction language, else source | Labels, explanations and refusals; mixed/uncertain framing remains model-dependent |
| Visible language set | Explicit targets and target-only constraint, else defaults | Deduplicated deliverables as below |
| Notes and practice | Explicit suppression and exercise request | Notes default on; exercise only if requested and notes remain enabled |
| Communication context | Stated audience, purpose, register, observed samples | Guides restrained edits and explanations; no inferred proficiency or unseen history |

### Language and notes decisions

Apply explicit requested targets first. With no targets, non-English source gets English; English source gets the first clearly identifiable non-English directive language, otherwise Chinese. Include polished source unless target-only; deduplicate any target equal to source. Framing is resolved separately from deliverable languages.

| Request example | Deliverable blocks | Learning block |
| --- | --- | --- |
| Chinese source, English instruction, no target | Chinese + English | English notes |
| English source, Chinese instruction, no target | English + Chinese | Chinese notes |
| English source and instruction, no target | English + Chinese | English notes |
| English source, “translate into French” | English + French | On unless suppressed |
| Chinese source, “only translate into English” | English | On |
| Chinese source, “only translate into English; no notes” | English | Omitted |
| “Only the translation” with a stated target | Target only | Omitted by explicit suppression rule |
| Target language equals source | One source/target block | On unless suppressed |

“Keep it short” alone does not suppress notes. “Only translate into English” versus “only the translation” deliberately produces different note behavior in the current prompt. This is a wording-sensitive contract requiring evaluation, not a robust parser established by the table. Unsupported or irreconcilable directives have no fully specified conflict-resolution algorithm beyond the priority order.

## Editing and rendering: FN-ED-002 and FN-ED-003

The priority order is integrity/truthfulness, explicit constraints, source fidelity, deliverables, teaching, then brevity. Explicit constraints cannot authorize false approval, invented facts, false attribution or unsupported certainty.

The current instructed sequence is: check integrity; edit/preserve in the source language; resolve meaning once; render visible blocks from that meaning; compare their facts, names, numbers, terminology, uncertainty, commitments, logic, intent, tone and formatting intent; then add permitted notes. Hidden extra-language renderings are prohibited.

| Case | Current instruction | Unspecified detail |
| --- | --- | --- |
| Already clear source | Preserve or make minimal useful changes | No formal edit-cost measure |
| Awkward or incorrect language | Improve clarity, accuracy, naturalness or readiness while preserving meaning | No explicit diagnosis taxonomy, candidate-generation or ranking algorithm |
| Ambiguous meaning | Preserve ambiguity/uncertainty rather than invent facts | No complete criterion for asking a clarification question |
| Technical text | Preserve names, APIs and intentional code-switching | No external terminology verification service |
| Misleading request | Brief refusal/correction in framing language; accurate alternative when possible | No separate refusal service; source plus target policy under all refusal cases is not fully explicit |

A useful design refinement is a conceptual **change-evidence record**: source span, revised span, reason, necessary correction versus optional style choice, fidelity constraint, and lesson eligibility. This is **proposed**, not an implemented data structure. It could make edit selection and lesson grounding reviewable without creating hidden runtime state.

## Teaching from evidence: FN-ED-004

The prompt selects useful observable changes or grounded translation choices by communication impact, repeated patterns in available samples, then explicit learner goals. Overlapping changes are grouped. Usually one to three lessons are chosen; substantial material can justify more distinct lessons.

Each substantive lesson contains an original-to-revised anchor (or translation choice), one or two relevant domain tags, why the choice helps, and a reusable pattern/contrast; add a short example only when useful. Corrections and style preferences are distinguished. Notes follow every deliverable, in the framing language. A requested exercise appears inside the same notes block after explanations, only when notes are enabled.

| Evidence | Supported linguistic explanation | Excluded claim |
| --- | --- | --- |
| Text or transcript | Morphology, lexicon, syntax, semantics, pragmatics, discourse, information structure | Actual pronunciation, intonation or rhythm |
| Clear accessible audio | Supported observations from the above plus phonetics, phonology and prosody | Invented sound observations, uncertain transcription treated as learner error, accent stigma |
| Stated goals and multiple available samples | Contextual personalization and supported recurring patterns | Persistent tracking, assumed native language, unseen history or proficiency |

The ten linguistic domains are a selective taxonomy, not mandatory output headings. The prompt forbids manufacturing edits or lessons. For nonsuppressed trivial/no-lesson cases, Learning Notes requires exactly one fallback. That also satisfies the broader “at most one” limit in Output Format. The differing specificity may benefit from clearer wording, but it is not a contradictory contract or evidence that zero notes is permitted by the complete prompt.

## Concrete scenario views

| Rendered view | Source / walkthrough basis | Decision exposed |
| --- | --- | --- |
| [C1 context](diagrams/context.svg) | [D2 source](views/context.d2); R2/R3 and IF-PROMPT | Who supplies instructions versus who executes |
| [C2 container](diagrams/container.svg) | [D2 source](views/container.d2); existing prompt file | The passive file-store boundary and external host |
| [Edit and learn](diagrams/edit-and-learn.svg) | [D2 source](views/edit-and-learn.d2); `editor-linguistic-personalized-goal-and-exercise` | English update, Chinese companion, grounded syntax note, requested exercise |
| [Integrity with no notes](diagrams/integrity-no-notes.svg) | [D2 source](views/integrity-no-notes.d2); `editor-integrity-explicit-target-no-notes`, R51–R56 | Refuse false customer approval while honoring note suppression |
| [Transcript boundary](diagrams/transcript-boundary.svg) | [D2 source](views/transcript-boundary.d2); `editor-linguistic-transcript-no-acoustics` | Text correction can proceed; sound-level claims lack evidence |

The first scenario's concrete source is “The issue was fixed yesterday, we will release next week.” A faithful correction could connect the independent clauses with a semicolon. The lesson can explain clause connection, and the exercise can ask the learner to repair a comparable comma splice. This is an illustrative expected result, not an observed model response. The sequence maps to existing Function identities while showing newer implementation detail explicitly.

## Acceptance scenarios and retained proof intent

The target-only example previously documented in the standalone editor view remains applicable: Chinese source with “Only translate this into English. No notes.” yields only an English deliverable, with neither Chinese output nor learning notes. A simultaneous request to invent customer approval still requires refusal or a truthful alternative while respecting note suppression. These are expected behaviors, not executed test results.

Retain coverage for source/instruction separation, mixed directive languages, source-equal targets, target-only with and without suppression, ambiguous terms, code-switching, non-Chinese/non-English input, already-clear text, restrained professional/PR editing, grounded lessons and integrity misuse. Learning checks include ambiguous suppression, trivial mechanics, expanded useful notes, qualified language rules and no unnecessary edits made for teaching. Historical proof intent includes the named `dim lighting` fidelity case; its fixture gap remains open below. The shared quality standard determines when actual model smoke evidence is required.

## Decision rationale and provenance

Fidelity and restraint define editing quality: an expert persona alone can encourage unnecessary transformation. Separating instructions, source and target languages prevents mixed-input role confusion. Deliverables come first so they stay copyable; learning notes follow and use concrete changes to teach reusable principles. Explicit suppression keeps that default controllable, while ambiguous brevity requests retain concise notes. Teaching must never reward unnecessary edits.

Source-plus-companion output replaced a fixed Chinese/English pair to preserve the user's source language while adding useful translation. Deterministic companion selection avoids duplicate English output. One base output shape with explicit overrides reduces competing templates, and fidelity checks compare the visible versions without requiring hidden extra-language renderings.

The original [expert-editing](https://github.com/xiongxianfei/skillsmith/blob/00224740db8a8e18e10579d8b38377ef0c1b04cf/docs/proposals/2026-05-26-editor-expert-quality-optimization.md#decision-log), [learning-default](https://github.com/xiongxianfei/skillsmith/blob/00224740db8a8e18e10579d8b38377ef0c1b04cf/docs/proposals/2026-06-16-editor-learning-default-optimization.md#decision-log) and [language-policy](https://github.com/xiongxianfei/skillsmith/blob/00224740db8a8e18e10579d8b38377ef0c1b04cf/docs/proposals/2026-06-16-editor-source-plus-companion-language-optimization.md#decision-log) decision logs preserve the alternatives and their reasons. Their superseded output defaults are history; the behavior tables in this specification describe the current prompt. Original review/model-run limitations remain in the historical plans and do not establish compliance with today's prompt.

## Shared platform participation

The platform supports the maintainer through authoring methods, fixture structure, deterministic validation, independent assessment and distribution. It is not called as a service during editing. Existing MOD-QUALITY/IF-STATIC and MOD-REVIEW/IF-SKILL-REVIEW remain outside the invocation path. The repository uses the C4 design and PR workflow; no maintenance coordinator is required at runtime.

Editor-specific outcomes can suggest reusable improvements, such as evidence requirements for feedback. That feedback-to-platform process is a proposed project direction from the vision, not an implemented telemetry or automatic training connection. No speculative feedback server is drawn.

## State, deployment, trust and quality constraints

- **Authored state:** prompt instructions and static expected scenarios live in repository files. Installation copies prompt assets; it does not execute editing or rewrite prompt behavior.
- **Invocation state:** source, preferences, outputs and observed examples belong to the host conversation. The skill creates no persistent learner profile; host retention and provider processing remain unknown and must not be described as local-only/private by this design.
- **Trust:** source text may contain apparent commands and private information. Keep source/instruction roles separate; user-selected host handling applies. The prompt does not grant tool permissions or initiate a repository-defined external service call.
- **Integrity:** no fabricated approval, facts, attribution, audio access or successful evaluation. A model following the prompt is an expectation requiring evidence, not a security enforcement mechanism.
- **Compatibility:** portable Markdown and `$ARGUMENTS` remain unchanged. Audio capability is conditional on the host. D2 is design tooling only, not an installation/invocation dependency.
- **NFR boundary:** no latency, cost, availability, scale, multilingual accuracy or learning-retention target has been accepted here. These depend on task and host; no unmeasured SLO is invented.

## Open decisions and evidence gaps

| ID | Finding / proposed work | Responsible next owner |
| --- | --- | --- |
| ED-C4-01 | Review observed speech and linguistic teaching against the historical contract and record accepted behavior here | Maintainer and human design reviewer |
| ED-C4-02 | Specify editing diagnosis, ambiguity handling and selection among candidate edits | This specification and human review before prompt change |
| ED-C4-03 | Consider consolidating fallback wording for readability; exactly one already satisfies at most one | Prompt/documentation owner; preserve existing behavior |
| ED-C4-04 | Define a final whole-response check covering notes/exercise; current sequence checks deliverables before adding notes | This specification with human review |
| ED-C4-05 | Named `dim lighting` fidelity fixture remains missing; static scenarios are not model-run evidence | Evaluation owner; preserve existing proof intent |
| ED-C4-06 | Record actual host/model and representative results before claiming behavioral quality | Evaluation owner |

No item above is marked implemented or accepted by producing these diagrams. The C4 model is a review aid; human architecture sign-off remains pending.
