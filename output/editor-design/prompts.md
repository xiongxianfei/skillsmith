# Editor summary image prompts

Generated with the built-in image-generation tool. These are explanatory summaries of skills/editor/SKILL.md; the source prompt and design documents remain authoritative. Amber proposed work in the second image is not implemented behavior. Images were visually inspected for readable labels and consistent flow.

Review clarification: the second image's fallback-note wording suggests a consistency issue. “Exactly one” satisfies “at most one”; the current prompt is compatible on this point. Any proposed edit is a wording clarification, not a behavioral correction. See the [editor specification](../../design/architecture/editor-c4/architecture-spec.md#teaching-from-evidence-fn-ed-004) for the precise interpretation. The prompts below record the original generation inputs unchanged.

## Image 1

Use case: infographic-diagram. Create one premium editorial technical infographic, landscape 16:10, high resolution ideally 2560px or more, polished clear vector-like artwork with precise typography. Subject: Skillsmith editor current implementation, reconstructed from its Markdown prompt. This is an explanatory summary, not a screenshot or UI mockup. Style: off-white background, deep navy typography, teal process cards, subtle blue accents, amber exception markers, generous whitespace, thin elegant connectors, small meaningful line icons, beautifully aligned grid. NO decorative filler, no gradients reducing contrast, no illegible tiny text. Aim for a professional engineering conference slide that is readable at a glance. Use the exact wording below; do not add invented claims.
Top eyebrow "SKILLSMITH / EDITOR"
Large title "From source to faithful output"
Subtitle "Current prompt behavior • editing, translation, and learning"
Main area: six numbered stages, in two rows of three, connected with a clear continuous serpentine arrow path 1→2→3→4→5→6. Each has bold title and two short lines:
1 "Interpret the request" / "Separate instructions from source" / "Identify task, audience, and constraints"
2 "Check usable evidence" / "Text, transcript, or accessible audio" / "Missing source → ask for material"
3 "Protect meaning" / "Check integrity; edit with restraint" / "Preserve facts, voice, and uncertainty"
4 "Render languages" / "Resolve meaning once" / "Produce only the selected language blocks"
5 "Check fidelity" / "Compare facts, terms, and commitments" / "Keep visible versions consistent"
6 "Teach from changes" / "Explain useful, grounded patterns" / "Honor no-notes and practice requests"
Under main flow: a thin highlighted strip headed "GOVERNING PRIORITY" with clearly spaced text "Truthfulness → User constraints → Fidelity → Deliverables → Teaching → Brevity".
Bottom left small callout with a microphone icon "Audio boundary" then "A transcript cannot prove pronunciation or intonation."
Bottom right small callout "Execution boundary" then "One portable Markdown prompt interpreted by the assistant host." then "No editor server or persistent learner profile."
Footer "Source: skills/editor/SKILL.md • Summary of instructions, not proof of model performance"
All text must be exact and clearly legible. Arrows must not cross text. No code listings, no extra platform modules, no fake evaluation scores.

## Image 2

Use case: infographic-diagram. Create one premium editorial technical infographic in landscape 16:10, high resolution ideally 2560px or more. Match an engineering design slide style: off-white background, deep navy typography, teal section headers, blue dividers, amber reserved exclusively for proposed improvements. Beautifully aligned grid, excellent whitespace, crisp vector-like small line icons, large legible text, no 3D, no decorative clutter. Subject: Skillsmith editor concrete output policies and teaching design, distinguished from proposed improvements. Exact content below; no invented rules.
Top eyebrow "SKILLSMITH / EDITOR"
Large title "Output decisions and learning design"
Subtitle "Current rules first. Proposed improvements clearly marked."
Two main panels, left about 53% width, right 47%.
LEFT PANEL header "01 / Choose deliverables"
A neat two-column decision table, headers "Request" and "Visible languages", exactly six rows:
"Non-English source; no target" | "Source + English"
"English source; non-English instruction" | "English + instruction language"
"English source; otherwise" | "English + Chinese"
"Explicit target languages" | "Source + requested targets"
"Target-only request" | "Requested targets only"
"Target matches source" | "One block; no duplicate"
Below table compact callout heading "Notes are a separate decision"
Three lines:
"Target-only ≠ no notes"
"“No notes” → omit learning block"
"“Keep it short” → concise notes remain"
RIGHT PANEL header "02 / Teach from evidence"
A vertical four-step mini flow with short numbered lines:
"Select useful changes"
"Group overlapping lessons"
"Explain why and when"
"Add practice only if requested"
Under it a distinctive outlined lesson card header "A substantive learning note"
Card lines:
"Original → Revised"
"1–2 relevant linguistic domains"
"Why it helps + reusable pattern"
"Optional example"
Below card two short lines:
"Usually 1–3 lessons; more only when justified."
"Personalize from available context, not assumed history."
BOTTOM full-width amber band separated visually from both current-policy panels, heading "PROPOSED DESIGN WORK — not implemented"
Three concise columns:
"Editing method" / "Make diagnosis and edit selection explicit"
"Rule consistency" / "Resolve “exactly one” vs “at most one” fallback note"
"Final checking" / "Check lessons as well as deliverables"
Footer "Source: skills/editor/SKILL.md • Current rules are prompt instructions, not executed test results"
Exact readable typography and logical spatial grouping are essential. Do not include automated learning claims, test pass badges, persistent profiles, or unsupported infrastructure.
