# Pitch

Skillsmith is a reusable prompt-skill library for people who use AI assistants to write, translate, learn, communicate, and make everyday decisions with more care.

The project exists to turn repeatable high-value prompting into portable skill files: small, inspectable instructions that can be installed as Codex or Claude Code slash commands, copied into other AI tools, and improved through ordinary review.

# What makes this different

Most prompt collections optimize for quantity, novelty, or one-off examples. Skillsmith optimizes for reusable judgment: each skill states when to invoke it, what input it expects, how it should reason, and what output shape a user can rely on.

That tradeoff means the project prefers fewer, more durable skills over a large catalog of loose prompts. A skill is worth adding when it captures a recurring workflow clearly enough that another person can use it without knowing the author's private context.

# Who it is for

Skillsmith is for engineers, multilingual workers, learners, and self-directed professionals who already use AI tools and want sharper repeatable workflows instead of ad hoc prompting.

It is also for maintainers who want skills to be easy to review: plain Markdown, explicit metadata, validation checks, and descriptions that help AI agents invoke the right skill from casual user intent.

# Who it is not for

This project is not for people looking for a general chatbot, a private knowledge base, or an automated agent platform. It is not for teams that need hidden proprietary prompt logic or skills that only work inside one vendor's runtime.

It is also not a substitute for licensed professionals, emergency services, or official advice. Skills can structure thinking and communication, but they do not make high-stakes decisions on the user's behalf.

# What it commits to

Every accepted skill is plain enough to inspect, copy, and adapt.

Every accepted skill has English metadata, a pushy invocation description, an argument hint, a `$ARGUMENTS` placeholder, and a clear output format.

Every accepted skill names a real user workflow and avoids being a vague personality preset.

The repository keeps validation simple enough that contributors can run it locally before opening a pull request.

The project favors practical usefulness over platform lock-in: installation can target supported assistant runtimes, but the skill body remains readable Markdown.

# What it refuses to be

Skillsmith refuses to become a grab bag of clever prompts without reviewable structure.

It refuses to hide important behavior in tooling, scripts, or private context when that behavior belongs in the skill prompt.

It refuses to add skills that pretend to replace professional judgment in medical, legal, financial, security, or other high-stakes contexts.

It refuses to make repository mechanics, installer details, or a specific AI vendor the main identity of the project.

# What would prove this wrong

The vision is failing if users cannot tell when to use a skill from its description.

It is failing if new skills pass validation but produce vague, inconsistent, or unactionable outputs.

It is failing if the catalog grows faster than maintainers can review quality and safety.

It is failing if skills become so tied to one assistant runtime that they stop being understandable as portable Markdown prompts.

# Open questions

Should the catalog stay centered on writing, translation, learning, and personal productivity, or should it explicitly include engineering workflow skills as first-class user-facing skills?

How strict should the project be about high-stakes advisory skills that include safety flags but still operate in sensitive domains?
