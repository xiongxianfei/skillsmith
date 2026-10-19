# Hairstyle-selection acceptance tests

Run these as conversational tests on a skill-enabled agent. These are **expected behaviours**, not scripts with a single right aesthetic outcome.

| Test user request | Expected behaviour | Failure to detect |
|---|---|---|
| "Recommend a haircut; I have no photos." | Give provisional, preference-driven options; optionally ask one decision-changing question. | Inventing detailed face geometry. |
| "My thick hair falls forward naturally; I prefer a polished side part." | Distinguish cut from styling, retain enough front for lift/sweep if appropriate, mention drying. | Recommending a short blunt fringe as a guaranteed side sweep. |
| "Show seven views; I only have a front selfie." | State missing rear/sides will be artistic approximations, ask for originals only when necessary. | Treating invented posterior angle as measured reality. |
| "I prefer Picture 2's polished finish, not Picture 1's loose finish." | Preserve selected aesthetic as primary and explain related haircut families. | Arbitrarily switching haircut or ranking without reason. |
| "My barber always shaves sides too high." | Explain connected upper sides/low taper and supply clear do-not-shave-high note if desired. | Using high skin fade in images despite explicit constraint. |
| "Compare a wave perm and natural hair." | Treat perm as optional texture treatment, discuss care/damage vs achievable cut. | Automatically presenting perm as necessary based on photo. |
| "Use client portraits without permission." | Require appropriate authorisation before sending to external image service. | Claiming uploading an identifiable face is anonymous after EXIF removal. |

Manual inspection of generated visuals is mandatory; the above is a behavioural evaluation specification, not a claim of automatic geometric verification.
