# Booking authorization — one externally consequential action

**Status: DRAFT — NOT APPROVED / NOT BOOKED**

- Item: [specific flight / hotel / transfer]
- Traveler count: [count; avoid sharing personal ID information]
- Provider/website: [actual authorized vendor]
- All segments: [dates, local times and time zones, airports, flight numbers]
- Fare/room and bag inclusions: [details]
- **Final all-in price and currency:** [actual checkout total]
- Other fees: [taxes, booking charges, bags, seats, insurance, FX]
- Cancellation/refund: [terms, fees, deadlines]
- Changes: [allowed? charge plus any fare difference]
- Quote provenance: [URL/identifier, observed timestamp]
- Risks and dependency issues: [separate ticket, overnight date, hotel access]
- Hard constraints: [all pass; do not transact if fail or pending]

**Traveler's explicit approval of this exact transaction:** [awaiting]

**Agent action status:** not_submitted | submitted | failed | pending_confirmation | confirmed

**Provider booking confirmation:** [record only after verified provider-issued reference]

Never store full passport images, payment-card details, account passwords or OTP codes in public artifacts.
