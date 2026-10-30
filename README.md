# Skillsmith

[![Validate Skills](https://github.com/xiongxianfei/Skillsmith/actions/workflows/validate.yml/badge.svg)](https://github.com/xiongxianfei/Skillsmith/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<!-- vision:start -->
Skillsmith brings together a library of practice skills and a shared platform for making good skills. It turns good practices into useful, reusable AI skills and continually improves how those skills are made.

The platform helps contributors build better practice skills. Real use of those skills supplies feedback and evidence that improve both the skills and the platform. Skillsmith favors demonstrated improvements over catalog size or speculative platform features.

It is for people applying useful practices with AI assistants, and practitioners, skill authors, and maintainers who want to share and improve how they work.

See [VISION.md](VISION.md) for goals, non-goals, and falsifiability.
<!-- vision:end -->

Portable Markdown skills for applying good practices, with examples across writing, translation, learning, and productivity.

## Skills

| Skill | Claude Command | Description |
|-------|---------------|-------------|
| [purchase-comparison](skills/purchase-comparison/SKILL.md) | `/purchase-comparison` | Product comparisons using Must/Avoid filters, weighted preferences, visible raw facts and Excel purchase trackers |
| [trip-expense-tracker](skills/trip-expense-tracker/SKILL.md) | `/trip-expense-tracker` | Multi-currency trip expense workbooks with separate cash and card costs, exchange fees, reimbursements and configurable base-currency summaries |
| [city-view-model](skills/city-view-model/SKILL.md) | `/city-view-model` | Structured city profiles using Place, Taste, Culture, Space, Time and Scenarios, with linked Excel tables, priority scores, checklists and visual layouts |
| [hairstyle-selection](skills/hairstyle-selection/SKILL.md) | `/hairstyle-selection` | Hairstyle consultation using visible hair and face observations, fair haircut comparisons, optional controlled previews and clear barber handoffs |
| [eyeglasses-selection](skills/eyeglasses-selection/SKILL.md) | `/eyeglasses-selection` | Everyday prescription frame selection, shape and fit comparisons, illustrative try-ons, and optician handoff with prescription safety boundaries |
| [c4-architecture](skills/c4-architecture/SKILL.md) | `/c4-architecture` | Public D2/C4 architecture skill for AI-generated, Git-reviewed system context, container and dynamic views; includes example models and validation helpers |
| [travel-planner](skills/travel-planner/SKILL.md) | `/travel-planner` | Constraint-aware travel planning: cross-platform flight and hotel comparisons, MCDA scoring, transport, experiences, approval gates and predeparture audits |
| [city-attraction-research](skills/city-attraction-research/SKILL.md) | `/city-attraction-research` | Evidence-grounded attraction rankings, comprehensive checklists, optional native pin maps, and Google My Maps CSV/GeoJSON exports |
| [local-food-and-dining-research](skills/local-food-and-dining-research/SKILL.md) | `/local-food-and-dining-research` | Ranked foods and drinks, dish-specific venue matches, optional native venue maps, and Google My Maps venue CSV exports |
| [city-itinerary-builder](skills/city-itinerary-builder/SKILL.md) | `/city-itinerary-builder` | Turn city attractions, foods, arrival arrangements and preferences into feasible daily itineraries, route data, timelines, printable guides and navigation checklists |
| [travel-storytelling-guide](skills/travel-storytelling-guide/SKILL.md) | `/travel-storytelling-guide` | Sourced attraction and food stories for pre-trip reading and on-location commentary; shared evidence, explicit uncertainty and optional reusable scripts |
| [editor](skills/editor/SKILL.md) | `/editor` | Faithful writing and speech editing/translation with source-language plus companion-language output and personalized linguistic learning notes; explicit target-language and no-notes overrides |
| [vocabulary-mastery](skills/vocabulary-mastery/SKILL.md) | `/vocabulary-mastery` | English-only skill instructions generating two complete, separate ten-domain vocabulary references (English first, Simplified Chinese second), each with learning connections and recall questions |
| [restaurant-menu-advisor](skills/restaurant-menu-advisor/SKILL.md) | `/restaurant-menu-advisor` | Restaurant menu advisor for choosing what to order from supplied menu photos, pasted menus, or readable dish evidence, with allergy-aware boundaries and illustrative visual briefs |
| [flashcard-generator](skills/flashcard-generator/SKILL.md) | `/flashcard-generator` | Source-grounded spaced-repetition flashcard generator for Anki cards, cloze deletions, memory prompts, durable recall practice, and retention cards |
| [quiz-generator](skills/quiz-generator/SKILL.md) | `/quiz-generator` | Source-grounded diagnostic quiz generator for quizzes, comprehension checks, MCQs, short-answer items, answer keys, rationales, feedback, and rubrics |
| [communicator](skills/communicator/SKILL.md) | `/communicator` | Draft formal Russian messages from Chinese input, with Chinese translation and cultural strategy notes |
| [doctor](skills/doctor/SKILL.md) | `/doctor` | Medical consultation — symptoms, medications, lab reports, health advice, with referral guidance and safety flags |
| [fitness-coach](skills/fitness-coach/SKILL.md) | `/fitness-coach` | Personal fitness coach — training plans, exercise technique, nutrition, and recovery advice |
| [nvc](skills/nvc/SKILL.md) | `/nvc` | Nonviolent Communication coach — rewrites harsh or blaming messages into NVC framework (observation, feeling, need, request) |
| [email-drafter](skills/email-drafter/SKILL.md) | `/email-drafter` | Draft professional English emails with Chinese translation and writing strategy notes — support tickets, business, academic, complaints, follow-ups |
| [journaling](skills/journaling/SKILL.md) | `/journaling` | Guided daily reflection coach — turns your day into structured reflection, deep-dive prompts, an optional journal draft, and a clear intention for tomorrow |
| [study-planner](skills/study-planner/SKILL.md) | `/study-planner` | Learning plan designer — turns any learning goal into a phased roadmap with weekly tasks, milestones, and curated resource recommendations |
| [language-tutor](skills/language-tutor/SKILL.md) | `/language-tutor` | Language learning tutor for any language — sentence correction, grammar, vocabulary, writing feedback, and conversation practice with targeted exercises |
| [oscp-coach](skills/oscp-coach/SKILL.md) | `/oscp-coach` | OSCP exam preparation coach — Socratic methodology guidance, 3-tier hint system, enumeration framework, and OSCP-allowed toolset enforcement |

---

## Installation

### Claude Code

#### Install all skills (recommended)

```bash
curl -sSL https://raw.githubusercontent.com/xiongxianfei/Skillsmith/main/install.sh | bash
```

This clones the repo into a temp directory, copies all skill folders into `~/.claude/skills/`, and cleans up automatically. Run the same command again to update.

Restart Claude Code after installing — skills are available immediately as `/editor`, `/vocabulary-mastery`, `/restaurant-menu-advisor`, `/flashcard-generator`, `/quiz-generator`, `/communicator`, `/doctor`, `/fitness-coach`, `/nvc`, `/email-drafter`, `/journaling`, `/study-planner`, `/language-tutor`, and `/oscp-coach` and `/travel-planner`, plus `/c4-architecture`, `/hairstyle-selection`, and `/eyeglasses-selection`.

#### Install a specific skill only

```bash
git clone https://github.com/xiongxianfei/Skillsmith
cp -r Skillsmith/skills/editor ~/.claude/skills/editor
cp -r Skillsmith/skills/vocabulary-mastery ~/.claude/skills/vocabulary-mastery
cp -r Skillsmith/skills/c4-architecture ~/.claude/skills/c4-architecture
cp -r Skillsmith/skills/travel-planner ~/.claude/skills/travel-planner
cp -r Skillsmith/skills/hairstyle-selection ~/.claude/skills/hairstyle-selection
cp -r Skillsmith/skills/eyeglasses-selection ~/.claude/skills/eyeglasses-selection
```

Install any individual skill by copying its **entire** directory. The examples above show how to install individual skills, including `hairstyle-selection` and `eyeglasses-selection`.

#### Project-level install — shared with your team

Run inside your project root:

```bash
curl -sSL https://raw.githubusercontent.com/xiongxianfei/Skillsmith/main/install.sh | bash -s -- --target .claude/skills
```

Or manually copy the folders you want into `.claude/skills/` and commit them so teammates get the skills automatically.

#### Try it for one session (no install)

```bash
git clone https://github.com/xiongxianfei/Skillsmith
claude --plugin-dir ./Skillsmith
```

Skills are available as `/Skillsmith:editor`, `/Skillsmith:vocabulary-mastery`, `/Skillsmith:restaurant-menu-advisor`, `/Skillsmith:flashcard-generator`, `/Skillsmith:quiz-generator`, `/Skillsmith:communicator`, `/Skillsmith:c4-architecture`, `/Skillsmith:hairstyle-selection`, and `/Skillsmith:eyeglasses-selection` for this session only.

### Other AI models (ChatGPT, Gemini, etc.)

Skills are portable **directory packages** following [Agent Skills](https://agentskills.io/specification). With an Agent Skills-compatible host, install the complete `skills/<skill-name>/` folder so `SKILL.md` can load bundled references, scripts, schemas, and assets. For agents supporting a conventional local skills directory, choose that agent's documented installation path.

For a text-only chat without directory access, copying `SKILL.md` can provide limited guidance, but it is **not** a supported full-function replacement when the skill requires local references, resources, or scripts.

---

## Usage

### Claude Code

Invoke by slash command, passing your text as the argument:

```
/editor  Please polish this text for me.
/editor  Correct this paragraph and explain the two most useful linguistic patterns.
/vocabulary-mastery  record — complete English reference, then a separate complete Simplified Chinese reference, each with ten linguistic dimensions.
/restaurant-menu-advisor  Here's the menu. What should I order if I want something filling under $25?
/flashcard-generator  Turn this onboarding note into Anki-ready flashcards.
/quiz-generator  Make a 10-question diagnostic quiz from this chapter.
/communicator  我想告诉房东暖气坏了，请帮我写一条俄语消息。
/c4-architecture  Create C1/C2 D2 views from our software requirements for a Git design review.
/travel-planner  Plan a long weekend with protected work commitments; compare complete itineraries, check travel documents, and create a realistic sightseeing plan.
/hairstyle-selection  Compare short and medium hairstyles from authorised portraits and prepare a barber brief.
/eyeglasses-selection  Compare everyday frame styles and explain which choices need in-person fitting.
```

Or just describe what you want in natural language — Claude auto-invokes the right skill based on context.

#### Learning artifact examples

Use `/vocabulary-mastery` for two full, independent references to one English lexical item: English first, Simplified Chinese second. The skill file itself uses English-only instructions:

```text
/vocabulary-mastery  record
Context: I need to record meetings and keep a record of project decisions.
Prefer British English pronunciation.
```

This produces two complete ten-dimensional entries rather than alternating languages within each section. Both contain a word overview, linguistic analysis, knowledge connections, and three recall questions with answers. The Chinese version includes the same English example sentences with Chinese translations. Use `/flashcard-generator` separately for Anki cards, TSV export, or spaced-repetition decks.

Use `/flashcard-generator` when the goal is durable recall and spaced repetition:

```text
/flashcard-generator  Turn this onboarding note into 20 Anki-ready flashcards.
Audience: new backend engineers.
Prefer basic, cloze, contrast, and failure-mode cards.
Export: Markdown table plus TSV.

<paste source material>
```

Use `/quiz-generator` when the goal is assessment, diagnosis, or feedback:

```text
/quiz-generator  Create a 10-question diagnostic quiz from this design doc.
Audience: senior engineers joining the project.
Include MCQs and short-answer questions.
Include answer key, rationales, and remediation feedback.

<paste source material>
```

For requests that need both, keep the two outputs separate:

```text
Create flashcards and a diagnostic quiz from this chapter.
Extract shared learning objectives once.
Keep flashcards and quiz outputs separate.
Return separate JSON payloads for each.

<paste source material>
```

Best practices for both learning skills:

- Provide source material instead of asking for unsupported facts.
- State the audience, purpose, desired count, difficulty, and export format.
- Ask external or related facts to be marked as inferred.
- Request fewer items when the source is short or narrow.
- Prefer separate flashcard and quiz sections instead of a merged study-artifact format.

### Other models

Install the complete skill directory in a compatible host. Where a host does not support directory access, a copied `SKILL.md` may be incomplete, especially for `c4-architecture` and skills with references or executable helpers.

---

## Skill Details

### `hairstyle-selection` — Hairstyle and Haircut Advisor

Uses authorised photographs or descriptions to evaluate visible facial proportions and natural hair behaviour; compares distinct haircut families, offers controlled illustrative previews on request, and prepares a practical multi-angle barber handoff. Separates cutting geometry from styling and validates outcomes in person.

### `eyeglasses-selection` — Prescription Eyewear Frame Advisor

Compares frame shapes, construction, materials and everyday style while keeping appearance distinct from actual fit and prescription requirements. Supports consented illustrative try-ons and optician-ready fitting questions; never substitutes AI imagery for a verified prescription or dispensing assessment.

### `travel-planner` — Constraint-Aware Trip Planning

Plans multi-day travel using feasibility screening, comparable flight and hotel evidence, constrained MCDA/weighted scoring, arrival and recovery planning, local connectivity/ground transfers and geographically clustered activities. Prevents unverified prices or pending legal/safety checks from becoming purchase recommendations. Booking and payment always require available authorized tools and explicit traveler approval. The bundled Moscow–Samarkand example is fictional and illustrates how to handle missing reliability evidence and pending hard gates.


### `editor` — Expert Text Editing & Translation

Edits writing or accessible speech in its own language with fidelity and restraint, then returns polished source-language output plus one companion language and selective, personalized linguistic learning notes by default. Notes label real changes with relevant domains, explain transferable patterns, and avoid unsupported pronunciation or intonation claims without audio. Explicit target-language and no-notes requests still override the defaults.

Best for: emails, PR descriptions, documentation, release notes, messages, academic writing, and professional business communication.

### `vocabulary-mastery` — Bilingual Linguistic Vocabulary Reference

Accepts a single English word or fixed expression and produces two separate, complete references: an English version followed by an independently readable Simplified Chinese version. Each version covers all ten linguistic dimensions: phonetics, phonology, morphology, lexicon, syntax, semantics, pragmatics, discourse, information structure, and prosody. The skill instructions and templates themselves remain entirely in English.

Each version includes the same sense map, reliably labelled pronunciation, linguistic explanations, natural example contexts, cross-domain connections, and three recall prompts with aligned answers. The Chinese reference retains the English examples alongside their Chinese translations. It differentiates reference pronunciation from learner audio and does not invent linguistic facts to fill headings.

Best for: deep study of an English word, bilingual lexical reference notes, homographs, polysemy, collocations, grammatical frames, and pronunciation-versus-word-class contrasts.

### `restaurant-menu-advisor` — Restaurant Menu Advisor

Compares supplied restaurant-menu evidence against taste, budget, appetite, dietary restrictions, allergies, and sharing context, then returns a small grounded shortlist, one leading recommendation, staff-confirmation questions when needed, and a copyable illustrative visual brief.

Best for: choosing from unfamiliar menus, deciding quickly at a restaurant, comparing a few dishes, handling allergy uncertainty conservatively, and previewing a likely dish appearance without treating generated images as restaurant photos.

### `flashcard-generator` — Flashcard Generator

Turns source material into spaced-repetition-ready flashcards with learning objectives, a compact knowledge map, atomic prompts, explanations, tags, and canonical JSON.

Best for: Anki cards, cloze deletions, memory prompts, durable recall practice, and retention cards from notes, documents, code, papers, courses, or project material.

Use it when you want learners to remember important ideas over time. For best results, ask for atomic cards, contrast cards for easily confused concepts, cloze cards only when the surrounding context is strong, and an export format such as Markdown, JSON, CSV, TSV, or Anki-oriented text.

### `quiz-generator` — Quiz Generator

Turns source material into diagnostic quizzes with a blueprint, learning objectives, questions, answer keys, rationales, feedback, rubrics where useful, and canonical JSON.

Best for: comprehension checks, MCQs, short-answer questions, diagnostic assessment, misconception checks, and transfer-oriented learning questions.

Use it when you want to assess understanding or diagnose gaps. For best results, ask for a quiz blueprint, cognitive levels such as recall/comprehension/application/diagnosis, one best answer for MCQs unless multiple-select is intended, and rationales or feedback for each answer.

### `communicator` — Formal Russian Communication Assistant

Takes your Chinese description of what you want to say and produces:

1. **Russian message** — Ready to send, culturally appropriate, using formal "Вы" register with proper greetings and closings.
2. **Chinese translation** — Exact translation of the Russian message.
3. **沟通建议** — Cultural strategy notes explaining the phrasing choices.

Default recipient is an elderly Russian landlady (Татьяна). Mention a different recipient/context in your input to adapt the tone.

Best for: landlord communication, formal letters, official correspondence with Russian contacts.

---

## Contributing

Start with the [contribution guide](docs/workflows.md) to define a change, edit, validate and open a PR. It includes a minimal skill example and bug-reporting guidance.

- [Skill quality standard](docs/skill-quality-standard.md): metadata, practical design guidance, safety, portability and review expectations.
- [Architecture guide](design/architecture/README.md): intended behavior, constraints and design decisions, maintained with `c4-architecture`.
- [Agent instructions](AGENTS.md): repository ownership, structure and engineering principles.

## License

MIT
