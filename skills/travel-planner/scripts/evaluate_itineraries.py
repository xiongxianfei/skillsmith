#!/usr/bin/env python3
"""Evaluate structured trip options with hard-check gates and a Weighted Sum Model.

This script performs no network calls, price checks, legal checks, bookings or payments.
It only applies reproducible arithmetic to evidence and status values supplied by
an agent or person. A point-score winner is withheld for unresolved hard gates or
missing scored criteria.

Usage:
    python3 scripts/evaluate_itineraries.py --input examples/samarkand-input.json \
        --output examples/samarkand-evaluation.json
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any, Dict, List

VALID_CHECKS = {"pass", "fail", "pending"}
VALID_PRICE_STATUSES = {"checkout_verified", "advertised", "derived", "unknown"}


class EvaluationError(ValueError):
    """Invalid plan or ambiguous data schema."""


def _number(value: Any, label: str, minimum: float, maximum: float | None = None) -> float:
    if isinstance(value, bool) or not isinstance(value, (float, int)) or not math.isfinite(value):
        raise EvaluationError(f"{label} must be a finite numeric value")
    if value < minimum or (maximum is not None and value > maximum):
        raise EvaluationError(f"{label} must be in [{minimum}, {maximum if maximum is not None else 'infinity'}]")
    return float(value)


def _hard_status(data: Any, label: str) -> str:
    status = data.get("status") if isinstance(data, dict) else data
    if status not in VALID_CHECKS:
        raise EvaluationError(f"{label} must contain status: pass | fail | pending")
    return status


def evaluate_plan(plan: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(plan, dict):
        raise EvaluationError("plan must be a JSON object")

    raw_weights = plan.get("weights")
    if not isinstance(raw_weights, dict) or not raw_weights:
        raise EvaluationError("weights must be a nonempty object")
    weights = {str(k): _number(v, f"weights.{k}", 0) for k, v in raw_weights.items()}
    if sum(weights.values()) <= 0:
        raise EvaluationError("sum of weights must be positive")
    total_weight = sum(weights.values())

    required = plan.get("hard_requirements")
    if not isinstance(required, list) or not required or not all(isinstance(r, str) and r for r in required):
        raise EvaluationError("hard_requirements must be a nonempty list of string IDs")
    if len(required) != len(set(required)):
        raise EvaluationError("hard_requirements contains duplicates")
    if "safety" not in required or "travel_documents" not in required:
        raise EvaluationError("hard_requirements must include safety and travel_documents")

    candidates = plan.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        raise EvaluationError("candidates must be a nonempty list")

    results: List[Dict[str, Any]] = []
    ids = set()
    for pos, candidate in enumerate(candidates):
        if not isinstance(candidate, dict):
            raise EvaluationError(f"candidate {pos} must be an object")
        cid = candidate.get("id")
        if not isinstance(cid, str) or not cid.strip() or cid in ids:
            raise EvaluationError(f"candidate {pos} must have a unique nonempty ID")
        ids.add(cid)

        checks = candidate.get("hard_checks")
        if not isinstance(checks, dict):
            raise EvaluationError(f"{cid}.hard_checks must be an object")
        absent = [r for r in required if r not in checks]
        if absent:
            raise EvaluationError(f"{cid}: missing required hard checks: {', '.join(absent)}")
        status_map = {r: _hard_status(checks[r], f"{cid}.hard_checks.{r}") for r in required}

        price = candidate.get("price")
        if price is not None:
            if not isinstance(price, dict):
                raise EvaluationError(f"{cid}.price must be an object or null")
            price_status = price.get("status", "unknown")
            if price_status not in VALID_PRICE_STATUSES:
                raise EvaluationError(f"{cid}.price.status is invalid")
            amount = price.get("amount")
            if amount is not None:
                _number(amount, f"{cid}.price.amount", 0)
            if status_map.get("fare_checkout") == "pass" and price_status != "checkout_verified":
                raise EvaluationError(f"{cid}: fare_checkout cannot pass unless price.status=checkout_verified")

        raw_scores = candidate.get("scores")
        if not isinstance(raw_scores, dict):
            raise EvaluationError(f"{cid}.scores must be an object")
        extra = set(raw_scores) - set(weights)
        if extra:
            raise EvaluationError(f"{cid}: scores contain criteria not in weights: {', '.join(sorted(extra))}")
        scores: Dict[str, float | None] = {}
        for criterion in weights:
            value = raw_scores.get(criterion)
            scores[criterion] = None if value is None else _number(value, f"{cid}.scores.{criterion}", 0, 10)

        failing = [k for k, v in status_map.items() if v == "fail"]
        waiting = [k for k, v in status_map.items() if v == "pending"]
        eligibility = "rejected" if failing else ("pending" if waiting else "eligible")

        known = [key for key, val in scores.items() if val is not None and weights[key] > 0]
        unknown = [key for key, val in scores.items() if val is None and weights[key] > 0]
        known_sum = sum(weights[key] * float(scores[key]) for key in known)
        missing_weight = sum(weights[key] for key in unknown)
        complete = (missing_weight == 0)
        exact = known_sum / total_weight if complete else None

        results.append({
            "id": cid,
            "label": candidate.get("label", cid),
            "eligibility": eligibility,
            "failed_checks": failing,
            "pending_checks": waiting,
            "missing_score_criteria": unknown,
            "evidence_completeness_pct": round(100 * (total_weight - missing_weight) / total_weight, 2),
            "score_0_to_10": round(exact, 4) if exact is not None else None,
            "score_interval_0_to_10": [round(known_sum / total_weight, 4), round((known_sum + 10 * missing_weight) / total_weight, 4)],
            "price": price,
            "notes": candidate.get("notes", ""),
        })

    # A global winner is withheld if any non-rejected competitor has pending gate(s)
    # or missing scored criteria. Rejected candidates cannot be selected.
    contenders = [x for x in results if x["eligibility"] != "rejected"]
    ready = bool(contenders) and all(x["eligibility"] == "eligible" and x["score_0_to_10"] is not None for x in contenders)
    if ready:
        ranking = sorted(contenders, key=lambda x: (-x["score_0_to_10"], x["id"]))
        winner = ranking[0]["id"]
        gap = (ranking[0]["score_0_to_10"] - ranking[1]["score_0_to_10"]) if len(ranking) > 1 else None
        comment = "All non-rejected contenders have passed hard checks and have complete scores."
        if gap is not None and gap < 0.2:
            comment += " Winner's margin is narrow (<0.2 points); sensitivity testing strongly advised."
    else:
        ranking = []
        winner = None
        comment = "No final winner: at least one non-rejected contender has pending constraints or missing scored evidence, or all candidates are rejected."

    return {
        "method": "constrained weighted-sum model (WSM)",
        "not_a_booking": True,
        "source_data_is_not_live_verified_by_script": True,
        "weights_total": total_weight,
        "required_hard_checks": required,
        "candidates": results,
        "ranking_ready": ready,
        "winner_id": winner,
        "ranking_ids": [r["id"] for r in ranking],
        "note": comment,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Trip candidate JSON input")
    parser.add_argument("--output", help="Destination JSON evaluation file; stdout if omitted")
    args = parser.parse_args()
    try:
        with open(args.input, "r", encoding="utf-8") as handle:
            plan = json.load(handle)
        report = evaluate_plan(plan)
    except (OSError, json.JSONDecodeError, EvaluationError) as exc:
        parser.error(str(exc))
        return 2
    payload = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        Path(args.output).write_text(payload, encoding="utf-8")
        print(f"Saved evaluation: {args.output}\n{report['note']}")
    else:
        print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())