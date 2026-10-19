"""Focused unit tests for the deterministic, offline flight decision evaluator."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("evaluate_itineraries", Path(__file__).with_name("evaluate_itineraries.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class EvaluateTests(unittest.TestCase):
    def base(self):
        return {
            "weights": {"schedule": 4, "cost": 6, "reliability": 2},
            "hard_requirements": ["travel_documents", "safety", "airport", "fare_checkout"],
            "candidates": [{
                "id": "a",
                "hard_checks": {"travel_documents": "pass", "safety": "pass", "airport": "pass", "fare_checkout": "pass"},
                "price": {"amount": 100, "status": "checkout_verified"},
                "scores": {"schedule": 7, "cost": 9, "reliability": 8}
            }]
        }

    def test_complete_candidate_can_win(self):
        report = mod.evaluate_plan(self.base())
        self.assertTrue(report["ranking_ready"])
        self.assertEqual(report["winner_id"], "a")
        self.assertAlmostEqual(report["candidates"][0]["score_0_to_10"], (4*7+6*9+2*8)/12, places=4)

    def test_missing_score_is_not_zero_or_neutral(self):
        plan = self.base()
        plan["candidates"][0]["scores"]["reliability"] = None
        result = mod.evaluate_plan(plan)["candidates"][0]
        self.assertIsNone(result["score_0_to_10"])
        self.assertEqual(result["missing_score_criteria"], ["reliability"])
        self.assertAlmostEqual(result["score_interval_0_to_10"][0], (4*7+6*9)/12, places=3)
        self.assertFalse(mod.evaluate_plan(plan)["ranking_ready"])

    def test_failed_safety_check_rejects(self):
        plan = self.base()
        plan["candidates"][0]["hard_checks"]["safety"] = "fail"
        result = mod.evaluate_plan(plan)
        self.assertEqual(result["candidates"][0]["eligibility"], "rejected")
        self.assertIsNone(result["winner_id"])

    def test_pending_document_check_blocks_selection(self):
        plan = self.base()
        plan["candidates"][0]["hard_checks"]["travel_documents"] = "pending"
        self.assertFalse(mod.evaluate_plan(plan)["ranking_ready"])

    def test_estimated_fare_cannot_pass_checkout_gate(self):
        plan = self.base()
        plan["candidates"][0]["price"]["status"] = "derived"
        with self.assertRaises(mod.EvaluationError):
            mod.evaluate_plan(plan)

    def test_missing_required_check_errors(self):
        plan = self.base()
        del plan["candidates"][0]["hard_checks"]["airport"]
        with self.assertRaises(mod.EvaluationError):
            mod.evaluate_plan(plan)

    def test_negative_weight_errors(self):
        plan = self.base()
        plan["weights"]["cost"] = -1
        with self.assertRaises(mod.EvaluationError):
            mod.evaluate_plan(plan)

    def test_out_of_range_score_errors(self):
        plan = self.base()
        plan["candidates"][0]["scores"]["comfort"] = 15
        with self.assertRaises(mod.EvaluationError):
            mod.evaluate_plan(plan)


if __name__ == "__main__":
    unittest.main()
