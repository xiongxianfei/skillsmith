# Travel Planner — reusable AI skill and travel SOP

This package contains a vendor-neutral [Agent Skills](https://agentskills.io/specification)-style `travel-planner` skill, a human-facing SOP, starter templates, a deterministic evaluator and a worked Moscow–Samarkand example.

## Package map

```text
travel-planner/
  SKILL.md                         Agent-facing workflow and safety/approval rules
  SOP.md                           Human-facing SOP entry point (see references/sop.md)
  references/
    sop.md                         Detailed stage-by-stage procedure
    scoring.md                     Hard constraints, weights, normalization, uncertainty
    research-and-tools.md          Provider adapters, provenance and freshness
    quality-gates.md               G0–G6 approvals and QA
    data-contracts.md              Canonical record fields and states
  assets/
    trip-brief.yaml                Intake template
    flight-comparison.csv          Flight research matrix
    hotel-comparison.csv           Lodging matrix
    poi-checklist.csv              Must-visit shortlist
    itinerary.md                   Day-by-day itinerary template
    connectivity-and-transport.md  Network, payment and mobility plan
    booking-approval.md            Mandatory purchase authorization record
    predeparture-checklist.md      Final trip QA
    decision-log.md                Decisions and reversals
  scripts/
    evaluate_itineraries.py        Dependency-free deterministic WSM evaluator
    test_evaluate.py               Unit tests
    verify_package.py              Structural bundle QA
  examples/
    samarkand-case-study.md        Worked SOP example (not live quotes)
    samarkand-input.json           Illustrative evaluator input
    samarkand-evaluation.json      Generated evaluator output
```

## Use with an Agent Skills-compatible agent

1. Place the **whole `travel-planner` directory** in a skill/capability location recognized by your agent implementation (installation path differs by product).
2. Confirm the agent can read `SKILL.md` and the referenced files. The manifest uses standard YAML `name` and `description` fields.
3. Ask: “Use the travel-planner skill to prepare a 4-night trip, including hard constraints, cross-platform flight comparison, hotel and transport checks, day-by-day plan and approvals.”
4. Connect browsing/search, map, calendar or booking tools separately if available. **Installing SKILL.md does not grant tool access.**
5. An agent without current prices/availability must produce a clearly labeled research plan rather than claim a verified booking.

## Run the decision evaluator offline

From this directory:

```bash
python3 scripts/evaluate_itineraries.py --input examples/samarkand-input.json --output /tmp/samarkand-evaluation.json
python3 -m unittest discover -s scripts -p 'test_*.py' -v
python3 scripts/verify_package.py
```

The script never queries airlines or makes purchases. It checks structured hard-check statuses and computes known-score intervals for missing data. A final winner is generated **only** when all hard constraints have passed and all soft criteria are scored.

## Operational rules

- A quote is not a reservation. A reservation is not a paid, issued e-ticket.
- An airline safety approval threshold must be chosen and validated explicitly. Never silently relax it.
- Mixed airline itineraries may be two independent tickets.
- Do not buy tickets or authorize charges based merely on approval of a shortlist.
- Keep source URLs and timestamps, separate current from old data, and verify checkout terms.
- Do not publish personal passport or payment information in shared files.

## Sources for the format

- Agent Skills specification: https://agentskills.io/specification
- OpenAI Academy explanation: https://openai.com/academy/skills/

Version 1.0.0. The worked Moscow–Samarkand example is entirely fictional and contains no live flight availability or real traveler details.