# Vocabulary mastery: C4 architecture and implementation profile

Vocabulary-mastery turns **one English word or fixed lexical expression** into two complete linguistic references: English first, Simplified Chinese second. Both cover the same ten dimensions and the same three recall tasks. The central design problem is preserving lexical accuracy, coverage and bilingual parity across a deliberately long response.

**Status:** implementation-derived design for human architecture review; no human approval recorded. “Implemented” means the instruction is present in the prompt, not that a model has demonstrated it. The behavior and constraints below have not yet received human acceptance. This specification keeps them together; separate requirement and system-model documents are not required.

## Basis and scope

| Evidence | What it establishes | What it does not establish |
| --- | --- | --- |
| [Vocabulary prompt](../../../skills/vocabulary-mastery/SKILL.md) | Role and Scope; Workflow; Two-Version Output Contract; Linguistic Rules; Output Format | Deterministic execution, lexical correctness, learning effectiveness |
| [Historical vocabulary scenarios](https://github.com/xiongxianfei/skillsmith/blob/0abafec052bcdf9952f462fa0a872a207b5cb83c/tests/evals/skills/vocabulary-mastery/cases.yaml) | 16 archived expected scenarios covering ordinary use, boundaries and non-triggers | Successful model runs or exhaustive coverage |
| [October 18 requirements](https://github.com/xiongxianfei/skillsmith/blob/1d6ce5bee418b59fcfdd4a8cc98304a491e3e49a/docs/changes/2026-10-18-bilingual-vocabulary-mastery/requirements.md) | Original two-complete-version choice, English-only skill source, behavior and evidence constraints | Current C4 approval or successful model execution |
| [Reviewer examples](https://github.com/xiongxianfei/skillsmith/blob/1d6ce5bee418b59fcfdd4a8cc98304a491e3e49a/docs/changes/2026-10-18-bilingual-vocabulary-mastery/examples.md) | Full `record` bilingual illustration and `apple` boundary examples with pronunciation provenance | Live-model outputs or measured accuracy |
| [Shared quality requirements](../../../docs/skill-quality-standard.md) | Repository quality/evidence obligations | A complete accepted contract for this skill |
| [Portable-skill architecture](../portable-skills.md) | Existing pure-prompt, validation and review boundaries | Previously accepted vocabulary-specific Function allocation |
| [Design index](../README.md) | Existing coverage limits | Approval created by adding a link |
| [D2 model](model.d2) | Diagram identities and structural relationships | A new runtime or a second normative product contract |

This isolated design uses the current prompt and archived scenarios as source evidence. It neither edits the prompt nor adopts new product behavior. The contextual learner examples are fictional scenario inputs. Maintenance uses the C4 design and PR workflow, outside vocabulary invocation.

## C4 scope and ownership

C1 treats `vocabulary_package` as a **passive prompt distribution**. The learner interacts with an external assistant host; the package supplies instructions through installation or paste. C2 opens the package to one genuine file-store container, `vocabulary_package.prompt_files`, containing the authored Markdown. It is not an executing lexicography service.

| Stable diagram ID | C4 type / owner | Responsibility |
| --- | --- | --- |
| `learner` | Person outside package | Supplies target, context and preferences; reads reference and recall answers |
| `maintainer` | Person outside invocation | Authors and reviews instructions and scenario evidence using shared methods |
| `vocabulary_package` | Passive software distribution / Skillsmith | Distributes the vocabulary behavior contract as authored instructions |
| `vocabulary_package.prompt_files` | File-store container / Skillsmith-authored Markdown | `skills/vocabulary-mastery/SKILL.md`; installed copy or pasted content |
| `assistant_host` | External software system / host operator | Interprets the prompt and generates the response; actual host/model topology is unknown |

A filesystem store fits the [C4 container definition](https://c4model.com/diagrams/container). Treating a passive package as the system scope is an explicit modeling adaptation. No C3 components are invented for ten linguistic headings or English/Chinese rendering. These are logical concerns in one prompt, not separately implemented applications. Host UI, inference services, authentication and transport are not specified here. A deployment diagram is deferred until an actual host deployment is selected.

The architecture reuses the editor design's modeling convention, not its editing policy. Vocabulary-mastery always develops all ten linguistic dimensions; editor selects only useful domains for grounded learning notes. No new service, data-store technology or API decision requires an ADR in this documentation-only projection.

## Concrete information flow

The implementation instructs the host to perform this logical flow:

**Resolve one target → build a shared sense map and examples → complete English reference → complete Chinese reference → check each part and compare parity → return both.**

The following information structure explains that flow. It is not an implemented JSON schema, persistent record, exposed reasoning transcript or new tool call.

| Logical information | Contents | Used by |
| --- | --- | --- |
| Target context | Headword/expression, supplied sentence, requested sense, learner goal, BrE/AmE preference | Sense selection and examples |
| Shared lexical basis | Selected senses/word classes, qualified pronunciation, grammatical frames, original examples, uncertainty | Both complete references |
| Dimension coverage | Ten ordered observations; explicit absence/limits where distinctive properties are unsupported | English drafting and Chinese explanation |
| Learning connections | Two or three links across linguistic dimensions | Knowledge Connections in both parts |
| Recall alignment | Exactly three concepts, corresponding questions and matching answers | Retrieval sections in both parts |
| Parity criteria | Same senses, IPA, observations, examples, connections, retrieval concepts and caveats | Independent completeness and cross-part checks |

Only the sense map, consistent examples and output checks are explicitly named workflow steps. The remaining rows make their implied information dependencies visible; they do not assert actual materialized structures inside a model.

## Input and routing decisions

| Input condition | Current instructed behavior | Evidence / limitation |
| --- | --- | --- |
| No target | Ask for one English word or lexical expression; do not emit empty profiles | Workflow 1; `vocabulary-no-input` |
| Several unrelated targets | Ask which one to study | Workflow 1; `vocabulary-multiple-unrelated-targets` |
| One expression such as `look up` | Treat the expression as one lexical item; honor its supplied meaning | `vocabulary-separable-expression` |
| A sentence establishing a sense | Prioritize that context in both versions | `vocabulary-bank-context-sense-parity` |
| No narrowing context | Distinguish up to three well-supported major senses or word classes | Workflow 2; homographs remain separate |
| Explicit BrE/AmE preference | Account for the requested variety; label confident reference IPA and qualify uncertainty | Workflow 1 and Linguistic Rules; no verification service specified |
| User-created coinage | Identify the evidence limit; retain ten sections without inventing established lexical facts | `vocabulary-coinage-evidence-boundary`; complete recovery strategy is not specified |
| Line-by-line bilingual formatting request | Preserve the selected skill's fixed two-part format | `vocabulary-conventional-fixed-two-part-contract`; this is unlike editor's configurable language contract |
| Ordinary proofreading, conversation tutoring or Anki export | Favor `editor`, `language-tutor` or `flashcard-generator` respectively | Routing guidance, not an implemented inter-skill API or automatic dispatch guarantee |

A fixed lexical expression is not equivalent to several unrelated words. The prompt does not provide a complete recognition algorithm for malformed input, non-English targets, or ambiguous phrase boundaries. Those remain limits, not invented error branches.

## Ten-dimension content design

Every row appears in both references, numbered in this order. Explanations aim for one to three substantive sentences per domain, with more depth only for meaningful complexity. An honest absence of a distinctive word-level property is valid content; an omitted domain or fabricated phenomenon is not.

| # | Dimension | Content responsibility | Boundary to preserve |
| --- | --- | --- | --- |
| 1 | Phonetics | Reference segments and articulation | Does not assess how the learner actually spoke |
| 2 | Phonology | Syllables, lexical stress and system contrasts | Distinct from sentence focus/intonation |
| 3 | Morphology | Real inflections/derivations and spelling changes | Do not infer historical roots from spelling alone |
| 4 | Lexicon | Collocations, chunks and lexical relations | Do not invent conventional expressions or frequency evidence |
| 5 | Syntax | Word class, countability, complements and grammatical frames | Preserve sense-specific grammatical behavior |
| 6 | Semantics | Differentiated senses, contextual meanings and contrasts | Do not collapse homographs or Chinese glosses |
| 7 | Pragmatics | Social intention, register and context | A word need not have a special speech act |
| 8 | Discourse | Coherence/reference across sentences or turns | Distinct from isolated sentence grammar |
| 9 | Information Structure | Given/new information, topic and contextual focus | Specify the context making focus meaningful |
| 10 | Prosody | Sentence prominence, rhythm and intonation illustrations | Reference illustration is not observed learner production |

Knowledge Connections then provides two or three cross-domain links. For example, a reference can connect a selected word class with its grammatical frame and usage distinction. No dictionary, corpus, recording or pronunciation service is invoked by the prompt; claims of verification or playback are prohibited when unsupported.

## Two independently complete outputs

Each part contains:

1. Word Overview: headword, selected word classes/senses, qualified BrE/AmE pronunciation when known, context focus.
2. All ten numbered dimensions with substantive explanation and useful natural examples or honest limitations.
3. Two or three Knowledge Connections.
4. Exactly three Recall Prompts and three corresponding Answers.
5. Accuracy Notes when needed, carrying the same qualifications in both parts.

English is completed before Chinese. The Chinese part localizes its title, section names, labels, explanatory prose, questions and answers. English lexical objects remain intact where needed: headword, cited forms, frames and original sample sentences; IPA is preserved. Each retained English example receives a faithful Chinese rendering. Chinese explanations are full rather than abridged, and neither part relies on “see above.”

| Parity check | Expected relation | Example failure |
| --- | --- | --- |
| Sense identity | Same selected meaning and word class | Contextual riverbank switches to financial bank in Chinese |
| Pronunciation | Same qualified IPA and distinctions | One homograph is merged into another pronunciation |
| Examples | Same original English samples plus Chinese translations | Chinese replaces the sample with an unrelated sentence |
| Coverage | Ten domains and supporting sections independently present | Chinese becomes a summary or omits prosody |
| Retrieval | Same three concepts, aligned answers | Chinese asks different questions or drops answers |
| Qualifications | Same uncertainty in each part's Accuracy Notes when needed | Caveat appears only in English or as a shared global note |

These are model-directed checks, not an implemented automated comparison engine. No fixed part-length ratio or exact textual translation is required; parity is factual and instructional.

## Scenarios and quality evidence

| View / historical scenario | What the design demonstrates | Evidence status |
| --- | --- | --- |
| [C1 context](diagrams/context.svg) / [source](views/context.d2) | Passive instructions versus external execution | Repository-grounded boundary |
| [C2 container](diagrams/container.svg) / [source](views/container.d2) | One authored file store; no glossary database or learning engine | Repository-grounded boundary |
| [Complete reference](diagrams/complete-reference.svg) / [source](views/complete-reference.d2) | `record`: shared sense map, full EN/ZH outputs, parity check | Derived from `vocabulary-record-two-complete-references` and archived recall scenarios; not an execution log |
| [Target clarification](diagrams/target-clarification.svg) / [source](views/target-clarification.d2) | Multiple targets → choose one → contextual `bank` reference | Composed walkthrough from archived multiple-target and bank scenarios; follow-up exchange is illustrative |
| [Coinage boundary](diagrams/coinage-boundary.svg) / [source](views/coinage-boundary.d2) | `flinderation`: required structure with honest evidence limits | Archived coinage scenario plus shared recall/accuracy rules; exact limited-content output remains underspecified |

Additional archived scenarios address `lead` homographs, `unhappiness` morphology, `apple` weak word-level dimensions, `look up` syntax, indirect triggering, independently readable Chinese, text-only pronunciation boundaries and non-triggers. These are written expected behaviors, not proof of accuracy, effective retrieval practice or long-term retention.

D2 sequence self-messages represent prompt-directed logical activities inside the external host. They do not expose model internals, create separate components or guarantee a deterministic execution order.

## State, trust, deployment and constraints

- **Authored state:** English-only prompt instructions and templates in `SKILL.md`; historical scenario declarations are linked above. The generated Chinese reference is output, not a separately maintained Chinese prompt.
- **Invocation state:** target, sense map, examples, draft references and questions belong to the current host interaction. No Skillsmith learner profile, score history, spaced-repetition schedule or progress database is implemented.
- **External execution:** installation copies prompt files or users paste them. Host capabilities, context limits, latency, inference cost, availability, authentication and retention policies are unknown. No local-only processing or privacy guarantee follows from a Markdown skill.
- **Accuracy:** preserve uncertainty and label supported variety distinctions. Reference pronunciation is not an assessment of the learner's actual speech. The skill does not establish an audio-assessment workflow merely by warning against unsupported sound claims.
- **Trust:** user sentences and invented terms are evidence to interpret, not independent authority for established lexical facts. The prompt does not fully specify hostile embedded-instruction handling; no security enforcement claim is made.
- **Quality tradeoff:** two full references favor independent usability over brevity. The prompt requires this despite possible output-budget pressure; continuation/truncation handling has not been designed.
- **Non-functional boundary:** no measured accuracy, speed, cost, scale or learning-retention target is accepted here. D2 is documentation tooling only; product installation and invocation gain no dependency.

The shared development platform supports authoring, format validation, review and distribution outside the learner's request. Cross-skill lessons about evidence quality or bilingual consistency may improve that platform after assessment. This is not an implemented telemetry/training loop, and no platform service is drawn on the invocation path.

## Open design work

| ID | Gap / candidate refinement | Next owner |
| --- | --- | --- |
| VM-C4-01 | Review these observations and record the accepted behavior and constraints in this specification | Maintainer and human design reviewer |
| VM-C4-02 | Define support/confidence criteria for IPA, senses, morphology and regional claims; no source-verification mechanism exists here | Requirements and evaluation owners |
| VM-C4-03 | Define continuation behavior when two complete references exceed available output budget | Requirement owner before prompt change |
| VM-C4-04 | Specify malformed-input, ambiguous-expression and non-English-input handling and the limits of unsupported coinage profiles; missing-target behavior already asks for a target | Maintainer and human reviewer of this specification |
| VM-C4-05 | Make a practical parity assessment rubric and collect representative model outputs | Evaluation owner; preserve exact subject/model identity |
| VM-C4-06 | Explain fixed-format conflicts to users while preserving the chosen contract, or explicitly reconsider that contract | Requirement owner; no silent adaptive-format change |

These are proposals or unresolved decisions, not newly accepted requirements. Human architecture sign-off remains pending. Existing [quality criteria](../../../docs/skill-quality-standard.md) continue to apply; no catalog-wide completeness or successful learning claim is inferred from these views.
