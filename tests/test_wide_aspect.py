"""Regression tests for 21:9 subject-filling camera normalization."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PLUGIN_ROOT))

import nodes


UNSAFE_UPRIGHT_SHOTS = {
    "坐姿半身",
    "三分之二身",
    "全身构图",
    "带环境全身",
    "环境人像",
    "局部特写",
    "动态全身",
}


def _all_random_requests() -> dict[str, str]:
    return {
        field_name: nodes.RANDOM_CHOICE
        for field_name in nodes.FIELD_ORDER
    }


class WideAspectCameraTests(unittest.TestCase):
    def resolve(self, seed: int, **overrides: str) -> dict[str, str]:
        requested = _all_random_requests()
        requested.update(overrides)
        return nodes.resolve_fields(
            nodes.PRESET_OPTIONS[0],
            nodes.RANDOM_SCOPES[2],
            seed,
            requested,
        )

    def assert_upright_21_9_is_subject_filling(
        self, fields: dict[str, str]
    ) -> None:
        self.assertEqual(fields["画面比例"], nodes.WIDE_ASPECT)
        self.assertNotIn(fields["基础姿态"], nodes.LYING_POSES)
        self.assertTrue(nodes._wide_aspect_compatible(fields))
        self.assertNotIn(fields["景别"], UNSAFE_UPRIGHT_SHOTS)
        self.assertIn(
            fields["景别"], {"面部特写", "头肩近景", "胸部以上"}
        )
        prompt = nodes.compose_prompt_text(fields, "详细")
        self.assertIn("主体以近距离横向展开的紧凑构图", prompt)
        self.assertNotIn("画面中仅此一人", prompt)

    def test_locked_21_9_normalizes_reported_dynamic_full_body_standing(self):
        fields = self.resolve(
            1,
            **{
                "画面比例": nodes.WIDE_ASPECT,
                "基础姿态": "门框间站立",
                "景别": "动态全身",
            },
        )
        self.assert_upright_21_9_is_subject_filling(fields)

    def test_locked_21_9_normalizes_reported_dynamic_full_body_walking(self):
        fields = self.resolve(
            2,
            **{
                "画面比例": nodes.WIDE_ASPECT,
                "基础姿态": "行走中停步",
                "景别": "动态全身",
            },
        )
        self.assert_upright_21_9_is_subject_filling(fields)

    def test_locked_21_9_normalizes_inherited_full_body_preset_camera(self):
        requested = {
            field_name: nodes.FOLLOW_PRESET
            for field_name in nodes.FIELD_ORDER
        }
        requested.update({
            "画面比例": nodes.WIDE_ASPECT,
            "基础姿态": "自然站立",
        })
        fields = nodes.resolve_fields(
            "夜间室内轻奢硬闪时尚写真",
            nodes.RANDOM_SCOPES[0],
            3,
            requested,
        )
        self.assert_upright_21_9_is_subject_filling(fields)

    def test_all_upright_poses_cannot_leak_full_body_camera_at_21_9(self):
        upright_poses = [
            option for option in nodes.FIELD_OPTIONS["基础姿态"]
            if option not in nodes.LYING_POSES
        ]
        for index, pose in enumerate(upright_poses):
            with self.subTest(pose=pose):
                fields = self.resolve(
                    index,
                    **{
                        "画面比例": nodes.WIDE_ASPECT,
                        "基础姿态": pose,
                        "景别": "动态全身",
                    },
                )
                self.assert_upright_21_9_is_subject_filling(fields)

    def test_lying_pose_can_keep_a_full_body_wide_camera(self):
        fields = self.resolve(
            4,
            **{
                "画面比例": nodes.WIDE_ASPECT,
                "基础姿态": "侧躺撑头",
                "景别": "动态全身",
            },
        )
        self.assertEqual(fields["画面比例"], nodes.WIDE_ASPECT)
        self.assertTrue(nodes._wide_aspect_compatible(fields))
        self.assertEqual(fields["景别"], "动态全身")

    def test_non_21_9_keeps_explicit_dynamic_full_body(self):
        fields = self.resolve(
            5,
            **{
                "画面比例": "16:9横构图",
                "基础姿态": "行走中停步",
                "景别": "动态全身",
            },
        )
        self.assertEqual(fields["景别"], "动态全身")
        self.assertNotIn(
            "主体横向占据画面主要宽度",
            nodes.compose_prompt_text(fields, "标准"),
        )

    def test_random_landscape_21_9_is_normalized_and_deterministic(self):
        requested = _all_random_requests()
        requested["画面比例"] = nodes.LANDSCAPE_RANDOM
        found = False
        for seed in range(1_000):
            first = nodes.resolve_fields(
                nodes.PRESET_OPTIONS[0], nodes.RANDOM_SCOPES[2], seed, requested
            )
            second = nodes.resolve_fields(
                nodes.PRESET_OPTIONS[0], nodes.RANDOM_SCOPES[2], seed, requested
            )
            self.assertEqual(first, second)
            if first["画面比例"] == nodes.WIDE_ASPECT:
                found = True
                if first["基础姿态"] not in nodes.LYING_POSES:
                    self.assert_upright_21_9_is_subject_filling(first)
        self.assertTrue(found, "Expected at least one 21:9 random-landscape seed")


if __name__ == "__main__":
    unittest.main()
