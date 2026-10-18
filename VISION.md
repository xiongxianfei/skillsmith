# Pitch

Skillsmith brings together a library of practice skills and a shared platform for making good skills. It turns good practices into useful, reusable AI skills and continually improves how those skills are made.

A good practice helps someone achieve a clear outcome in a known context. A practice skill makes it usable by an AI assistant: when to apply it, how to act, why the approach helps, and where its limits are. Editing, English vocabulary learning, and travel planning are examples of possible applications.

The shared platform provides methods, guidance, tools, and evaluation for developing skills. It helps contributors build better practice skills; experience from those skills improves the platform. The platform supports skill development while the skills remain portable and inspectable.

# What makes this different

Skillsmith connects practical use with a shared way to improve skills. Domain knowledge belongs in practice skills. Lessons that hold across skills refine the platform, so contributors can reuse what others have learned. Feedback from real use tests both the skills and the methods used to create them.

The project prefers fewer, well-supported skills over a large catalog of loose prompts, and demonstrated needs over speculative platform features. A practice is worth capturing when others can apply it and assess whether it helps. Calling it good is a claim to examine in context.

# Who it is for

Skillsmith is for people who want AI assistants to apply useful practices consistently, and practitioners who want to share and improve how they work.

It is also for skill authors and maintainers who want a shared, evidence-informed way to turn domain expertise into skills and improve their quality.

# Who it is not for

This project is not for people looking for a general chatbot, a private knowledge base, or autonomous agent execution. It is not for teams that need hidden proprietary prompt logic or skills that only work inside one vendor's runtime.

It is also not a substitute for licensed professionals, emergency services, or official advice. Skills can structure thinking and communication, but they do not make high-stakes decisions on the user's behalf.

# What it commits to

Every accepted skill is plain enough to inspect, copy, and adapt. It names a real user outcome, explains its practice and limits, and makes its expected input and output clear.

Skills improve through concrete examples, reported failures, user feedback, and evaluation. Revisions explain the problem they address and provide evidence appropriate to the claimed improvement. Passing a format check alone does not establish usefulness.

Shared guidance improves when experience across skills supports a reusable lesson. Domain-specific findings improve the relevant skill. The project refines, combines, or retires practices and platform guidance when evidence shows they are unclear, redundant, or no longer useful.

The platform makes good skill development understandable and practical for contributors.

The project favors practical usefulness over platform lock-in: installation can target supported assistant runtimes, but the skill body remains readable Markdown.

# What it refuses to be

Skillsmith refuses to become a grab bag of clever prompts without reviewable structure.

It refuses to hide important behavior in tooling, scripts, or private context when that behavior belongs in the skill prompt.

It refuses to add skills that pretend to replace professional judgment in medical, legal, financial, security, or other high-stakes contexts.

It refuses to grow platform machinery without a demonstrated benefit to practice skills, or make repository mechanics and a specific AI vendor the project identity.

# What would prove this wrong

The vision is failing if users cannot tell when to use a skill from its description.

It is failing if new skills pass validation but produce vague, inconsistent, or unactionable outputs.

It is failing if recurring failures and useful feedback do not improve skills, or if lessons that apply across skills never improve the platform.

It is failing if the platform adds effort without improving outcomes or making the next good skill easier to create.

It is failing if the catalog grows faster than maintainers can review quality and safety.

It is failing if skills become so tied to one assistant runtime that they stop being understandable as portable Markdown prompts.

# Open questions

How strict should the project be about high-stakes advisory skills that include safety flags but still operate in sensitive domains?
