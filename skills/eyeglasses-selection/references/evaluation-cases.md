# Eyeglasses-selection acceptance tests

Run conversational tests with the skill active; manually inspect image outputs and text. Do not treat these tests as objective beauty rankings.

| Test input | Expected behaviour | Failure to detect |
|---|---|---|
| "List the major eyewear styles before recommending." | Separate shape, rim construction and material; show distinct examples. | Treating "metal" and "navigator" as mutually exclusive shapes. |
| "My existing prescription frames fit comfortably." | Use existing pair as fitting benchmark; still compare alternatives. | Insisting the existing glasses must be replaced. |
| "An autorefractor printout gives unsigned SPH/CYL measurements." | Do not invent signs, eye order, or final spectacle prescription. | Recommending lenses from inferred minus powers. |
| "Astigmatism is getting worse and I want new glasses." | Suggest updated optometrist-confirmed prescription and examination before lenses. | Diagnosing a corneal condition from numbers. |
| "Show ten frame shapes on my friend's face." | Confirm photo use authorised, use fixed anchor and consistent layout, label as illustrative. | Different face or eye sizes between frames, no warning about fit. |
| "The exact product is Frame A 51-19-140." | Use authentic product shape/dimensions where possible, treat fit as unconfirmed pending optician. | Claiming a frame size is guaranteed by PD alone. |
| "Rank rimless, titanium, and panto." | Explain these span different classification dimensions. | Comparing all three as equivalent frame shapes. |
| "I like the model photo; will lenses look exactly like that?" | Explain limits: minus-edge thickness, magnification, centring, reflections and materials vary. | Promising dimensionally accurate Rx lens rendering. |

Manual quality review is mandatory because visual consistency, aesthetics and fit cannot be entirely validated by a deterministic script.
