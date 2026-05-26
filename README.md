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
| [editor](skills/editor/SKILL.md) | `/editor` | Expert text editing and translation with Chinese/English output by default and explicit target-language overrides |
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

Restart Claude Code after installing — skills are available immediately as `/editor`, `/communicator`, `/doctor`, `/fitness-coach`, `/nvc`, `/email-drafter`, `/journaling`, `/study-planner`, `/language-tutor`, and `/oscp-coach`.

#### Install a specific skill only

```bash
git clone https://github.com/xiongxianfei/Skillsmith
cp -r Skillsmith/skills/editor ~/.claude/skills/editor
```

Replace `editor` with the skill name you want.

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

Skills are available as `/Skillsmith:editor` and `/Skillsmith:communicator` for this session only.

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
/communicator  我想告诉房东暖气坏了，请帮我写一条俄语消息。
```

Or just describe what you want in natural language — Claude auto-invokes the right skill based on context.

### Other models

Paste the prompt as the system prompt, then send your input as the first user message.

---

## Skill Details

### `editor` — Expert Text Editing & Translation

Edits source text in its own language with fidelity and restraint, then returns Chinese and English final versions by default. Explicit target-language requests override the visible default.

Best for: emails, PR descriptions, documentation, release notes, messages, academic writing, and professional business communication.

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
