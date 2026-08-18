"""Regression tests for the baseline iris-color option set."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PLUGIN_ROOT))

import nodes


BASE_IRIS_LABELS = {
    "深棕色", "黑褐色", "浅棕色", "琥珀色", "灰色", "蓝色", "绿色",
}
REMOVED_IRIS_LABELS = {
    "榛褐色", "金棕色", "蜂蜜金色", "橄榄绿色", "海蓝色", "冰蓝色",
    "青灰色", "银灰色", "紫灰色", "深紫色", "玫瑰粉色",
    "异色瞳（左右不同色）", "异色瞳（左蓝右棕）",
    "异色瞳（左绿右琥珀）", "异色瞳（左灰右蓝）",
}


class IrisColorTests(unittest.TestCase):
    def test_only_baseline_iris_options_are_public(self):
        options = set(nodes.FIELD_OPTIONS["瞳色"])
        self.assertEqual(options, BASE_IRIS_LABELS)
        self.assertFalse(options.intersection(REMOVED_IRIS_LABELS))

    def test_baseline_iris_color_resolves_and_renders(self):
        requested = {field: nodes.FOLLOW_PRESET for field in nodes.FIELD_ORDER}
        requested["瞳色"] = "琥珀色"
        fields = nodes.resolve_fields(
            nodes.PRESET_OPTIONS[0], nodes.RANDOM_SCOPES[0], 42, requested
        )
        self.assertEqual(fields["瞳色"], "琥珀色")
        self.assertIn("琥珀色", nodes.compose_prompt_text(fields, "详细"))

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
