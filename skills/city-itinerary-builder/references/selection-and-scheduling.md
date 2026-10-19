# Selection and scheduling policy

1. **Hard constraints first.** Record arrival, departure, fixed reservations, hotel access, booked commitments and rest windows before adding optional attractions. Do not schedule anything overlapping those blocks.
2. **Independent baseline ranking.** Respect the upstream attraction and food rankings without altering them. Personal restrictions or the marginal value of adding another museum affect *selection*, not the research score.
3. **Use capacity conservatively.** Consider visit duration, verified transfer time, queuing, season/daylight, energy, recovery, and meal capacity. A food tasting might fit inside a market stop; do not schedule two compulsory full lunches to maximize checklist coverage.
4. **Group geographically.** Use place and route evidence, not similarity in labels. If true route time is unavailable, label the leg unresolved and allow sufficient unsourced planning slack, without giving a numeric travel-time claim.
5. **Verify timing.** For each fixed activity check the relevant date, local opening/service window and reservation state. Distinguish explicitly verified, provisional and unknown. Published regular opening hours are not themselves an available reservation.
6. **Optimize without hiding alternatives.** Select a diverse subset of worthwhile experiences that is feasible under user preferences. Record omitted options for substitutions after closure or fatigue.
7. **Escalate a conflict.** If confirmed bookings or mandatory travel commitments conflict, return a conflict report instead of a polished but impossible schedule.

## Example acceptance cases

- A traveler reaches Samarkand at 14:00. The builder must not assign a 09:00 attraction to that arrival day merely because its upstream score was highest.
- Siyob Bazaar appears as both a sightseeing stop and a food experience. The builder must not create two travel stops unless the traveler intentionally plans separate visits.
- A transit provider quotes a 25-minute transfer, but adjacent blocks have a 15-minute gap. The plan fails feasibility checks; reroute or reschedule.
- Without any routing provider, report the transfer as unresolved, not as a straight-line five-minute walk.
