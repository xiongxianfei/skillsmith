# Eyewear visual try-on production and deliverables

## Two-stage comparison

**Stage A — Explore types:** Compare about 8–10 distinct, brand-neutral shape/construction examples at one consistent frontal camera angle. Use a neutral clear-lens design. Keep the *same anchor face* and preferably the same hair, outfit, expression, lighting, crop and size. Use these as illustrations of style **not fit**.

**Stage B — Refine finalists:** Choose 2–3 shapes; compare real size ranges, different rim thicknesses/colours/materials as available. Only then add right and left ~45° oblique and an actual ~90° lateral view. If the user is choosing purchasable models, use actual frame photographs and dimensions where available; never claim a synthetic generic shape is a real product.

## Quality-control procedure

1. Create/choose an approved frontal source portrait without glasses (or an existing frame with a visually faithful removal, if possible). User permissions must cover identifiable-image processing.
2. Lock all non-frame properties: head geometry, eyes, ears, brows, nose bridge, jaw, hairstyle, expression, lighting, framing, clothing and background.
3. Generate one frame-style edit at a time; do **not** ask the model to independently remake the entire person's face for each frame.
4. Use approximately similar frame scale for fair shape comparison, except when exploring an intentionally oversized model; avoid changing apparent pupil position between variations.
5. Screen results for eye magnification changes, facial retouching, implausible nasal fit, warped rims, asymmetrical lens position, inconsistent lighting/reflections and style names not matching the actual geometry. Reject or flag flawed previews.
6. Build comparison grid after accepting individual outputs. Add style names/labels outside the generated portrait; don't depend on tiny lettering rendered by an image model.
7. State that AI try-ons do not predict actual dimensions, optical centring, comfort, edge thickness or corrected vision.

## Reusable prompts

### Style discovery

> Make a photorealistic eyeglass try-on by editing this **authorised original portrait**. Change ONLY the glasses to [clearly described frame family, rim, material and colour]. Use clear untinted lenses. Preserve the subject's facial geometry, eyes, eyebrows, nose, cheeks, hairstyle, expression, skin texture, background, camera angle and clothing. Do not widen/slim the face, change apparent eye size, add beauty filters or alter the haircut. Use a moderately sized plausible prescription frame and place it naturally. No caption or extra graphics. This preview is illustrative, not a calibrated fitting.

### Matching oblique/profile

> Edit the supplied authentic [subject-right / subject-left] [45° oblique / 90° lateral] view with the same glasses family selected from the frontal comparison. Preserve the actual pose and facial structure. Show coherent bridge, rims and temples with a physically plausible connection. Keep the frame design, lens height, rim thickness, colour and background consistent with the frontal image. Do not invent additional facial details where the source does not show them.

### Specific frame model, later stage

> Use the attached authentic product frame photo(s) and manufacturer dimensions [A, DBL, temple, where supplied] as references. Overlay or render the model on the approved anchor portrait without altering the subject's features. If exact perspective/geometry cannot be maintained, state that the result is an approximate style preview rather than dimensionally faithful.

## Evaluation matrix

For each candidate, record short justifications under five common criteria, not invented numeric scoring:

| Criterion | Question |
|---|---|
| Facial balance | Does the total width, lens height and corner shape complement the appearance? |
| Brow/eye relation | Do upper rims sit harmoniously relative to eyebrows and eyes? |
| Hairstyle versatility | Does the frame work with current and planned hairstyles? |
| Everyday use | Is it visually appropriate across intended situations and not unduly delicate? |
| Practical fit/optics | Any obvious reasons to check the physical frame or lens dimensions with the optician? |

Mark status `preview hypothesis` until the user tries real frames. Prefer direct front/side phone photos of *actual* tried-on models over the synthetic image once available.

## Final deliverable

- One shape taxonomy and explicit comparison criteria if the user asks broadly.
- Equal-framed frontal portrait grid and individual finalists on request.
- Clear provisional top 3 with advantages/risks and relation to comfortable existing pair.
- Optician shortlist: model name, authentic frame dimensions, material and possible concerns **only if known**, plus final Rx and fitting checks.
- Offer practical comparison photos from an in-person try-on, with the subject's permission, before finalising.
