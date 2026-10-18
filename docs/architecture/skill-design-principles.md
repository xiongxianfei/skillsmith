# Skillsmith Skill Engineering Principles

**Status:** Applied project design guidance, effective when this change is merged. These are **reviewer heuristics**, not a second validator or a replacement for the [Constitution](../../CONSTITUTION.md) or the approved [Skill Quality Standard](../../specs/skill-quality-standard.md). Where they conflict, the repository's established source-of-truth order governs.

**Scope:** New and materially changed skills. Do not rewrite grandfathered skills merely for stylistic uniformity. The goal is small, portable, auditable prompt contracts with predictable observable behavior—not to recreate an object-oriented framework inside a prompt.

## Engineering principles

| ID | Software analogy | Skillsmith rule | Evidence to review |
| --- | --- | --- | --- |
| **P1. One outcome, cohesive responsibility** | Single Responsibility, high cohesion | One skill should solve one recognisable user job. Keep only closely related steps needed for that outcome. Avoid tiny, fragmented micro-skills with no standalone value. | Can the reviewer explain its job and non-goals in one sentence? Does its trigger overlap a neighbor without a clear boundary? |
| **P2. Contract before prose** | Design by Contract, interface segregation | Define accepted input, intent, default output, ordering, omissions, and missing/ambiguous-input behavior before writing elaborate instructions. Outputs must be independently usable. | Can a reviewer check every required section from a sample? Is the error/absence behavior explicit? |
| **P3. One simple execution path** | KISS, YAGNI | Prefer one clear workflow and only justified exceptions. Do not add speculative modes, routers, multi-stage agents, or repeated conditional fallbacks to patch an unclear core task. | Is each branch required by an accepted input/output contract? Could a simpler invariant remove it? |
| **P4. DRY the knowledge, not necessary deliverables** | DRY, single source of truth | Establish one conceptual analysis and reuse its facts across outputs. Duplicate *visible* sections or local instructions when necessary for independent usability, portability, or fidelity. Do not make runtime correctness depend on undisclosed shared prompts. | Do related outputs contradict each other? Is duplication intentional, or are two instructions drifting apart? |
| **P5. Explicit boundaries and composition** | Low coupling, composition over inheritance | Distinct skills own distinct jobs; use clear handoffs through user-visible text or artifacts. A skill may recommend another skill but must not assume it can invoke it or share memory automatically. | Does it rely on another skill, unavailable tools, or a persistent profile without guaranteed access? |
| **P6. Ground claims in available evidence** | Data integrity, fail-safe defaults | Preserve user facts and scope. Separate observed evidence, reference knowledge, inference, and original examples; qualify unsupported claims instead of fabricating them. Safety and privacy requirements from the Constitution still apply. | What evidence supports every non-obvious claim? Can a no-evidence case fail gracefully without invented content? |
| **P7. Stable, portable interfaces** | Open/Closed, semantic compatibility | Keep plain Markdown with minimal YAML frontmatter, `$ARGUMENTS`, and a clear output contract. Extend behavior without silently breaking published names, installation, downstream formats, or prior overrides. Record changes and migration if breaking. | Could the skill run by copy-paste in another model? Which previous users or callers would notice the change? |
| **P8. Layered verification, honest claims** | Testing pyramid, acceptance tests | Use structural/unit checks for observable invariants, static eval scenarios for expected model behavior, and manual live-model checks where needed for quality. Never equate fixture presence or passing CI with proven model reliability. | Which commands ran? Which realistic positive, indirect, boundary and non-trigger cases are covered? What remains untested? |
| **P9. Clear ownership and economical maintenance** | Separation of concerns, change locality | Put prompt behavior in the owning `SKILL.md`, evals in `tests/evals/`, validator behavior in `tests/`, and public usage in README. Prefer small, reviewable diffs and references with one unambiguous target. | Can each change be located in the correct owner? Were related docs and fixtures updated without unrelated refactors? |

These principles adapt software ideas; they do not imply deterministic execution, inheritance, class hierarchies, or a runtime skill orchestrator.

## Design-review checklist

For a new or materially changed skill, record short answers in the PR description or change-local requirements:

1. **Job:** What single user outcome does the skill own, and what neighboring job does it explicitly not own? (P1, P5)
2. **Contract:** What inputs, default output, language/format rules, and incomplete-input paths are visible? (P2)
3. **Path:** What is the smallest uniform workflow that meets that contract? Which exceptions are justified? (P3)
4. **Shared facts:** Where is the single conceptual source for information repeated in multiple output sections? Is duplication intentional? (P4)
5. **Evidence:** What claims would be unsupported, and what exact qualified behavior replaces invention? (P6)
6. **Compatibility:** Are public command names, output sections, privacy/safety rules, and portability preserved? (P7)
7. **Proof:** What static checks, scenario expectations, and (if applicable) model smoke tests establish confidence? What remains unverified? (P8, P9)

A review finding may justify an exception: record the tradeoff and its rationale. **Do not turn subjective heuristics into blocking lint rules** unless a separately reviewed spec defines an objective, mechanically testable invariant.

## Applied example: vocabulary-mastery

**Responsibility:** Build one comprehensive English-word reference, not edit user prose or export Anki cards. `editor` owns corrections; `language-tutor` owns interactive tutoring; `flashcard-generator` owns card generation. Mentioning them is a boundary, **not** automatic orchestration (P1, P5).

**Accepted contract:** One lexical item (plus optional context). Output **two complete, independent versions**: English first, Simplified Chinese second. Each retains its own overview, all ten numbered linguistic domains, connections, three recall questions/answers, and relevant accuracy notes. The `SKILL.md` instructions and both templates remain English-only (P2, P7).

**One analysis, two renderings:** First resolve the senses, parts of speech, pronunciation confidence, genuine morphology, English examples, evidence limits, and three testable recall answers **once** as an internal plan. Then render the English reference and its Chinese counterpart from those same facts. Do not show a third planning section or store a phantom state file. Check corresponding facts and example meanings before delivering (P3, P4).

**Accepted verbosity:** The two published references and full output templates repeat structure intentionally because the user selected independently readable, comprehensive versions. This is a *good reason* to duplicate the visible contract, **not** a reason to duplicate inconsistent facts (P4).

**Honest boundaries:** For ordinary words like `apple`, a pragmatics or prosody section can state there is no distinctive word-specific property, while explaining an appropriately labelled sentence-level illustration. Text cannot establish the user's actual pronunciation or speech prosody; reference IPA must be variety-labelled where supported (P6).

**Verification:** Structural checks can confirm the prompt is English-only, both required ten-domain templates exist, and the parts appear in order. Static scenario fixtures document expected sense selection, bilingual parity, and evidence limits; a live language-model evaluation would still be required to demonstrate generation quality (P8).
