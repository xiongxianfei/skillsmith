# Skillsmith

[![Validate Skills](https://github.com/xiongxianfei/Skillsmith/actions/workflows/validate.yml/badge.svg)](https://github.com/xiongxianfei/Skillsmith/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<!-- vision:start -->
Skillsmith is a reusable prompt-skill library for people who use AI assistants to write, translate, learn, communicate, and make everyday decisions with more care.

Unlike loose prompt collections that optimize for quantity, Skillsmith optimizes for reusable judgment: each skill states when to invoke it, what input it expects, how it should reason, and what output shape a user can rely on.

It is for engineers, multilingual workers, learners, and self-directed professionals who already use AI tools and want sharper repeatable workflows instead of ad hoc prompting.

See [VISION.md](VISION.md) for goals, non-goals, and falsifiability.
<!-- vision:end -->

A curated collection of AI prompts for writing, translation, and productivity — works with any model, installable as Claude Code skills.

## Skills

| Skill | Claude Command | Description |
|-------|---------------|-------------|
| [editor](skills/editor/SKILL.md) | `/editor` | Faithful writing and speech editing/translation with source-language plus companion-language output and personalized linguistic learning notes; explicit target-language and no-notes overrides |
| [vocabulary-mastery](skills/vocabulary-mastery/SKILL.md) | `/vocabulary-mastery` | Comprehensive English–Chinese vocabulary reference with all ten linguistic dimensions, bilingual examples, cross-domain connections, and three recall questions |
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

Restart Claude Code after installing — skills are available immediately as `/editor`, `/vocabulary-mastery`, `/restaurant-menu-advisor`, `/flashcard-generator`, `/quiz-generator`, `/communicator`, `/doctor`, `/fitness-coach`, `/nvc`, `/email-drafter`, `/journaling`, `/study-planner`, `/language-tutor`, and `/oscp-coach`.

#### Install a specific skill only

```bash
git clone https://github.com/xiongxianfei/Skillsmith
cp -r Skillsmith/skills/editor ~/.claude/skills/editor
cp -r Skillsmith/skills/vocabulary-mastery ~/.claude/skills/vocabulary-mastery
```

Use the first `cp` command for `editor` or the second for `vocabulary-mastery`; to install another skill, replace the name in the source and destination paths.

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

Skills are available as `/Skillsmith:editor`, `/Skillsmith:vocabulary-mastery`, `/Skillsmith:restaurant-menu-advisor`, `/Skillsmith:flashcard-generator`, `/Skillsmith:quiz-generator`, and `/Skillsmith:communicator` for this session only.

### Other AI models (ChatGPT, Gemini, etc.)

Each skill's prompt works with any model — just copy and paste:

1. Open `skills/<skill-name>/SKILL.md`
2. Copy everything **below** the `---` frontmatter block
3. Paste as the system prompt in your AI tool of choice

---

## Usage

### Claude Code

Invoke by slash command, passing your text as the argument:

```
/editor  Please polish this text for me.
/editor  Correct this paragraph and explain the two most useful linguistic patterns.
/vocabulary-mastery  record — full English–Chinese reference in all ten linguistic dimensions.
/restaurant-menu-advisor  Here's the menu. What should I order if I want something filling under $25?
/flashcard-generator  Turn this onboarding note into Anki-ready flashcards.
/quiz-generator  Make a 10-question diagnostic quiz from this chapter.
/communicator  我想告诉房东暖气坏了，请帮我写一条俄语消息。
```

Or just describe what you want in natural language — Claude auto-invokes the right skill based on context.

#### Learning artifact examples

Use `/vocabulary-mastery` to investigate one English lexical item across all ten linguistic domains, in English and Simplified Chinese:

```text
/vocabulary-mastery  record
Context: I need to record meetings and keep a record of project decisions.
Prefer British English pronunciation.
```

This produces a detailed bilingual lexical reference (sound, form, word family, collocations, grammar, meaning, pragmatics, discourse, information structure, and prosody) and three recall questions. Use `/flashcard-generator` separately when you want Anki cards, TSV export, or spaced-repetition decks.

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

Paste the prompt as the system prompt, then send your input as the first user message.

---

## Skill Details

### `editor` — Expert Text Editing & Translation

Edits writing or accessible speech in its own language with fidelity and restraint, then returns polished source-language output plus one companion language and selective, personalized linguistic learning notes by default. Notes label real changes with relevant domains, explain transferable patterns, and avoid unsupported pronunciation or intonation claims without audio. Explicit target-language and no-notes requests still override the defaults.

Best for: emails, PR descriptions, documentation, release notes, messages, academic writing, and professional business communication.

### `vocabulary-mastery` — Bilingual Linguistic Vocabulary Reference

Accepts a single English word or fixed expression and provides a complete English + Simplified Chinese entry with all ten linguistic dimensions: phonetics, phonology, morphology, lexicon, syntax, semantics, pragmatics, discourse, information structure, and prosody. Each dimension includes an evidence-based explanation and a natural example or an explicit statement when a word has no unusual feature in that dimension.

The output includes a sense map, pronunciation by variety where reliable, cross-domain connections, and three retrieval prompts with answers. It differentiates dictionary pronunciation from learner audio and does not invent linguistic facts to fill headings.

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

1. Fork the repo
2. Create a branch: `git checkout -b feat/your-skill-name`
3. Add your skill under `skills/<skill-name>/SKILL.md` following the [frontmatter schema](https://docs.anthropic.com/en/docs/claude-code/skills)
4. Follow the canonical quality standard in [specs/skill-quality-standard.md](specs/skill-quality-standard.md)
5. Open a PR — include what the skill does, when to use it, validation output, and eval evidence for new or materially changed skills

## License

MIT
