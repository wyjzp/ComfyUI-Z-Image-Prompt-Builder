"""Regression tests for expanded iris-color and heterochromia options."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PLUGIN_ROOT))

import nodes


NEW_IRIS_LABELS = {
    "榛褐色",
    "金棕色",
    "蜂蜜金色",
    "橄榄绿色",
    "海蓝色",
    "冰蓝色",
    "青灰色",
    "银灰色",
    "紫灰色",
    "深紫色",
    "玫瑰粉色",
    "异色瞳（左右不同色）",
    "异色瞳（左蓝右棕）",
    "异色瞳（左绿右琥珀）",
    "异色瞳（左灰右蓝）",
}


class IrisColorTests(unittest.TestCase):
    def test_existing_and_new_iris_options_are_public(self):
        options = set(nodes.FIELD_OPTIONS["瞳色"])
        self.assertTrue({"深棕色", "黑褐色", "蓝色", "绿色"}.issubset(options))
        self.assertTrue(NEW_IRIS_LABELS.issubset(options))

    def test_heterochromia_renders_at_all_prompt_densities(self):
        requested = {field: nodes.FOLLOW_PRESET for field in nodes.FIELD_ORDER}
        requested["瞳色"] = "异色瞳（左蓝右棕）"
        fields = nodes.resolve_fields(
            nodes.PRESET_OPTIONS[0], nodes.RANDOM_SCOPES[0], 42, requested
        )
        self.assertEqual(fields["瞳色"], "异色瞳（左蓝右棕）")
        self.assertIn("左眼", nodes.compose_prompt_text(fields, "详细"))
        self.assertIn("异色瞳", nodes.compose_prompt_text(fields, "标准"))
        self.assertIn("左蓝右棕异色瞳", nodes.compose_prompt_text(fields, "精简"))

    def test_profile_random_pool_can_select_new_iris_colors(self):
        for preset in nodes.PRESET_OPTIONS:
            if preset == nodes.CUSTOM_PRESET:
                continue
            pool = nodes.PROFILE_POOLS[preset]["瞳色"]
            self.assertTrue(set(pool).intersection(NEW_IRIS_LABELS))

    def test_iris_resolution_remains_deterministic(self):
        requested = {field: nodes.RANDOM_CHOICE for field in nodes.FIELD_ORDER}
        first = nodes.resolve_fields(
            nodes.PRESET_OPTIONS[0], nodes.RANDOM_SCOPES[2], 123, requested
        )
        second = nodes.resolve_fields(
            nodes.PRESET_OPTIONS[0], nodes.RANDOM_SCOPES[2], 123, requested
        )
        self.assertEqual(first["瞳色"], second["瞳色"])


if __name__ == "__main__":
    unittest.main()
