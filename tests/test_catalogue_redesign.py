import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import catalogue


class CatalogueRedesignTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = json.loads(catalogue.REDESIGN_FIXTURE.read_text())
        cls.contract = json.loads(catalogue.REDESIGN_CONTRACT.read_text())

    def test_failed_product_can_contain_valuable_transferable_practice(self):
        record = self.fixture
        catalogue.validate_assessment(record)
        product_value = record["project"]["judgements"]["current_product_value"]["estimate"]
        contribution = record["contributions"][0]
        self.assertEqual(product_value, 0)
        self.assertGreater(contribution["judgements"]["current_contribution_value"]["estimate"], product_value)
        self.assertEqual(record["project"]["inside_value_refs"], [contribution["id"]])

    def test_unknown_effort_and_forecasts_stay_unknown(self):
        catalogue.validate_assessment(self.fixture)
        self.assertEqual(self.fixture["effort"]["human"]["status"], "unknown")
        self.assertEqual(self.fixture["effort"]["ai"]["status"], "unknown")
        for aspect in ("future_product_value", "technical_feasibility", "delivery_feasibility"):
            self.assertEqual(self.fixture["project"]["judgements"][aspect]["status"], "unknown")

    def test_estimate_bounds_are_validated(self):
        record = copy.deepcopy(self.fixture)
        record["contributions"][0]["judgements"]["transferability"]["plausible_range"] = [9, 10]
        with self.assertRaisesRegex(ValueError, "within plausible_range"):
            catalogue.validate_assessment(record)

    def test_feasibility_range_requires_explicit_constraints_and_horizon(self):
        record = copy.deepcopy(self.fixture)
        record["project"]["judgements"]["technical_feasibility"] = {
            "status": "range",
            "probability_range": [0.2, 0.6],
            "rationale": "Hypothetical evidence-backed range.",
            "evidence_refs": ["independent-example"],
        }
        with self.assertRaisesRegex(ValueError, "constrained range or unknown"):
            catalogue.validate_assessment(record)

    def test_ordinal_aggregation_is_rejected(self):
        record = copy.deepcopy(self.fixture)
        record["overall_score"] = 4
        with self.assertRaisesRegex(ValueError, "forbidden aggregate"):
            catalogue.validate_assessment(record)

    def test_coverage_partition_rejects_overlap_and_gaps(self):
        wp1 = self.contract["x_wp1"]
        paths = [item["path"] for item in wp1["registry_pins"]]
        lanes = copy.deepcopy(wp1["lanes"])
        lanes[1]["paths"].append(lanes[0]["paths"][0])
        lanes[1]["paths"].sort()
        with self.assertRaisesRegex(ValueError, "overlap"):
            catalogue.validate_partition(lanes, paths)
        lanes = copy.deepcopy(wp1["lanes"])
        lanes[0]["paths"].pop()
        with self.assertRaisesRegex(ValueError, "exactly cover"):
            catalogue.validate_partition(lanes, paths)

    def test_contract_validates_pinned_registry_and_fixture(self):
        checked = catalogue.validate_redesign_contract()
        self.assertEqual(checked["pin_count"], 73)
        self.assertEqual([len(lane["paths"]) for lane in checked["lanes"]], [19, 18, 18, 18])

    def test_lane_handoff_requires_exact_paths_and_root_pins(self):
        checked = catalogue.validate_redesign_contract()
        lane = checked["lanes"][0]
        pins = {item["path"]: item["source_pin"] for item in self.contract["x_wp1"]["registry_pins"]}
        records = []
        for path in lane["paths"]:
            record = copy.deepcopy(self.fixture)
            record["path"] = path
            record["source_pin"] = pins[path]
            records.append(record)
        handoff = {"contract_version": 1, "lane": lane["key"], "root_source_revision": self.contract["x_wp1"]["root_source_revision"], "assessments": records}
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / (lane["key"] + ".json")
            output.write_text(json.dumps(handoff))
            catalogue.validate_redesign_handoff(output, lane["key"])
            handoff["assessments"][0]["source_pin"] = "0" * 40
            output.write_text(json.dumps(handoff))
            with self.assertRaisesRegex(ValueError, "source_pin differs"):
                catalogue.validate_redesign_handoff(output, lane["key"])

    def test_aspect_anchors_cover_each_integer_estimate_range(self):
        catalogue.validate_schema_shape(self.contract)
        anchors = self.contract["x_wp1"]["judgements"]
        for aspect in catalogue.VALUE_JUDGEMENTS:
            bands = [item["range"] for item in anchors[aspect]["anchors"]]
            self.assertEqual(bands[0][0], 0)
            self.assertEqual(bands[-1][1], 10)
            self.assertTrue(all(left[1] + 1 == right[0] for left, right in zip(bands, bands[1:])))


if __name__ == "__main__":
    unittest.main()
