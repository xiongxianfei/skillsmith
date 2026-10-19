---
name: hairstyle-selection
description: Evaluate haircut and hairstyle options from consented portraits or descriptions, compare short/medium/long styles, account for natural hair growth and glasses, generate controlled preview instructions, and prepare multi-angle barber briefs. Use when choosing a haircut, reviewing face-framing and hair texture, comparing hairstyle photos, or preparing references for a barber or stylist.
metadata:
  version: "1.0.0"
---

# Hairstyle Selection

## Goal and scope

Help a person select **realistic, personally preferred haircuts** and communicate the selected cut to a stylist. Separate (1) visible observations, (2) aesthetic hypotheses, (3) AI simulations, and (4) results validated by a real haircut. The client's preference overrides a generic face-shape rule. Do not claim one objectively most attractive haircut.

This skill covers haircut analysis, style shortlists, optional visual previews, styling advice, and barber handoff. It does **not** provide medical diagnosis of the scalp or hair loss, precise measurements from uncalibrated photos, or guaranteed reproduction of generated images.

## Use the minimum necessary inputs

1. Establish the requested outcome: general ideas, specific style comparison, personalised preview, or barber handoff. Reuse known answers; do not restart a questionnaire at every step.
2. Use photographs only when the subject authorised their use. If consent is unknown for a third-party identifiable portrait, confirm it before sending the image to an additional service. Minimise metadata and identifying background. Do not claim metadata removal anonymises a face.
3. Determine only the decision-changing constraints: current natural hair behaviour (air-dried vs styled), hair length range, desired impression, styling time, willingness for heat/chemical treatments, glasses/headwear, and barber skill. Ask at most the most consequential unanswered question at a time; proceed with clearly labelled assumptions when reasonable.
4. If images are supplied, assess usable views and possible lens distortion. Do not demand seven photos for a quick style shortlist. If no images exist, offer qualitative options and identify limits.

Read [photo standards](references/photo-standards.md) when planning or validating multi-angle photography.

## Reason from observations, not rigid typologies

- Record visible face outline, apparent proportions, forehead visibility, temples, jaw and cheek contours, head silhouette, existing cut, hair fall, apparent volume, cowlick/whorl and growth direction **with uncertainty**. Do not infer identity, ethnicity, underlying bone measurements, or medical conditions from appearance.
- Distinguish **hair density** from *apparent fullness*, and **natural growth** from deliberate styling. Do not diagnose thinning from a visible part or whorl.
- Describe evidence neutrally: `Visible: the fringe falls forward after air-drying`; `Possible implication: preserve front length if a swept style is desired`; `Unknown: whether it will hold without heat`.
- Separate cutting structure from finish: the same haircut can be styled as loose texture or a polished side part. Never equate scissor work with no use of clippers, or a low taper with a skin fade.

Read [cut structures and style families](references/style-and-cutting.md) when comparing candidate cuts or preparing a barber brief.

## Recommendation workflow

1. **Baseline:** State what currently works and what might improve; don't assume a dramatic makeover is better.
2. **Breadth:** For open exploration, compare about 5–7 genuinely different families (short, medium, long). Do not count near-synonyms (e.g., loose side part and side sweep) as unrelated hairstyles. Treat perm/wave treatments as styling or texture options, not automatically separate cuts.
3. **Fair comparison:** Use the same criteria for every candidate: facial balance, compatibility with natural growth, styling feasibility, glasses/temple clearance, upkeep, and alignment with stated aesthetic. Show strengths and drawbacks; use qualitative assessments rather than invented precision or beauty percentages.
4. **Shortlist:** Recommend roughly three distinct finalists, explain why each is viable and what could go wrong, and name a first choice **provisionally**. Do not silently change rankings when new evidence arrives: explain what changed.
5. **Reality check:** A chemical treatment is recommended only where ordinary cut/heat styling is unlikely to meet the desired texture and the user accepts its cost and care. Do not recommend excessive thinning purely from perceived bulk.
6. **Handoff:** If the user intends to visit a barber, deliver a compact instruction brief specifying fringe/top, upper-side connection, temple/ear, crown/whorl, nape, desired finish, and explicit avoidances. Hair lengths in centimetres are illustrative starting targets, never measurements extracted from pictures.

## Preview and barber-reference modes

Only generate or edit images when the user asks for visual outputs and a suitable tool is available. If none exists, provide a prompt and shooting plan rather than claiming pictures were generated.

- **Discovery:** One fixed frontal image, individual edits changing hairstyle only, and a labelled comparison sheet assembled after reviewing the images. Compare different cuts, not changing facial geometry or lighting.
- **Shortlist:** Add matched left/right oblique and profiles where useful. For a final barber package, use the seven-view convention in [photo standards](references/photo-standards.md). A synthetic view of an unseen side/back is illustrative, not measured evidence.
- **Image discipline:** Keep the person's face, colour, camera perspective, expression and clothing as fixed as tools permit. Use source images for each actual angle when available; do not flip anatomical left/right. Don't put fine technical labels inside a generated photo if accuracy is critical—annotate and verify separately.
- **Review:** Reject variants with changed identity, contradictory lengths/taper heights, wrong angle names, a high fade when low taper was requested, or impossible crown/part continuity.

Read [preview production and handoff](references/preview-and-handoff.md) for reusable prompts, deliverables, and quality checks.

## Expected response contract

Tailor the detail to the request. For a full selection task, give:

1. **Visible evidence and limits** (brief; note air-dried versus styled and perspective).
2. **Comparable options** (name, defining structure, reason it could suit, trade-off).
3. **Ranked finalists and rationale**, explicitly provisional until an actual cut is evaluated.
4. **Stylist-ready instructions** for the selected cut, with cutting structure distinct from finishing steps, if requested.
5. **Visual assets or preview plan** only when requested; identify AI-generated views as illustrative.
6. **Validation:** check immediately after cut, after washing/air-drying, after home styling, and after growth. Reassess before chemical treatment or another major cut.

## Stop/quality gate

Before finalising, verify: known user preferences reused; no overconfident geometry; no contradictory cut names; no precise photo-derived lengths; left/right views correct; sides match the desired fade/taper; user consent respected; no promise that a simulation is exact. If a key unknown prevents a decision, ask one focused question instead of presenting a long form.
