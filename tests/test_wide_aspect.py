"""Regression tests for orientation-specific aspect randomization."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PLUGIN_ROOT))

import nodes


class DirectionalAspectRandomTests(unittest.TestCase):
    def resolve(self, option: str, seed: int) -> dict[str, str]:
        requested = {
            field: nodes.RANDOM_CHOICE for field in nodes.FIELD_ORDER
        }
        requested["画面比例"] = option
        return nodes.resolve_fields(
            nodes.PRESET_OPTIONS[0], nodes.RANDOM_SCOPES[2], seed, requested
        )

    def test_random_portrait_uses_only_portrait_aspects(self):
        for seed in range(200):
            fields = self.resolve(nodes.PORTRAIT_RANDOM, seed)
            self.assertIn(fields["画面比例"], nodes.PORTRAIT_ASPECTS)

    def test_random_landscape_uses_only_landscape_aspects(self):
        for seed in range(200):
            fields = self.resolve(nodes.LANDSCAPE_RANDOM, seed)
            self.assertIn(fields["画面比例"], nodes.LANDSCAPE_ASPECTS)

    def test_square_aspect_is_not_directional_random_candidate(self):
        seen_portrait = {
            self.resolve(nodes.PORTRAIT_RANDOM, seed)["画面比例"]
            for seed in range(200)
        }
        seen_landscape = {
            self.resolve(nodes.LANDSCAPE_RANDOM, seed)["画面比例"]
            for seed in range(200)
        }
        self.assertNotIn("1:1方形构图", seen_portrait)
        self.assertNotIn("1:1方形构图", seen_landscape)

    def test_directional_randomization_is_deterministic(self):
        for option in (nodes.PORTRAIT_RANDOM, nodes.LANDSCAPE_RANDOM):
            first = self.resolve(option, 123)
            second = self.resolve(option, 123)
            self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
