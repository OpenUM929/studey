from __future__ import annotations

import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "check_novelty_ledger.py"
SPEC = importlib.util.spec_from_file_location("check_novelty_ledger", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class NoveltyLedgerTest(unittest.TestCase):
    def write_case(self, markdown: str, rows: list[dict[str, str]]) -> tuple[Path, Path, tempfile.TemporaryDirectory]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        set_path = root / "set.md"
        ledger_path = root / "set.novelty.tsv"
        set_path.write_text(markdown, encoding="utf-8")
        with ledger_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=MODULE.HEADER, delimiter="\t")
            writer.writeheader()
            writer.writerows(rows)
        return set_path, ledger_path, temp

    def write_raw_ledger(self, path: Path, lines: list[str]) -> None:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def base_rows(self) -> list[dict[str, str]]:
        return [
            {
                "item_id": "1",
                "type_id": "SM2-09",
                "invariant": "중점을 지나며 기준 직선에 수직",
                "non_numeric_axis_1": "조건 방향: 직선 찾기에서 꼭짓점 역추적으로 전환",
                "non_numeric_axis_2": "목표량: 방정식에서 사각형 넓이로 전환",
                "structural_difference": "수직이등분선을 먼저 구한 뒤 교점을 복원하고 넓이를 계산한다.",
                "nearest_prior": "catalog:SM2-09 representative; SET-260822-math2-40#9",
                "verdict": "PASS",
            },
            {
                "item_id": "2",
                "type_id": "SM2-16",
                "invariant": "중심의 축까지 거리가 반지름",
                "non_numeric_axis_1": "조건 방향: 원 결정에서 접점 자취 역산으로 전환",
                "non_numeric_axis_2": "경우 구조: 한 사분면 선택에서 두 경우 합산으로 전환",
                "structural_difference": "접하는 원을 직접 정하지 않고 접점의 자취와 경우 수를 결합한다.",
                "nearest_prior": "catalog:SM2-16 representative; SET-260829-math2-25#10",
                "verdict": "PASS",
            },
        ]

    def test_valid_exact_cover_passes(self) -> None:
        markdown = "**1.** 문제\n\n[SM2-09 · T2 · DF1]\n\n**2.** 문제\n\n[SM2-16 · T3 · DF2]\n"
        set_path, ledger_path, temp = self.write_case(markdown, self.base_rows())
        self.addCleanup(temp.cleanup)
        failures, warnings = MODULE.validate(set_path, ledger_path, 2)
        self.assertEqual([], failures)
        self.assertEqual([], warnings)

    def test_missing_id_fails(self) -> None:
        markdown = "**1.** 문제\n\n[SM2-09 · T2 · DF1]\n\n**2.** 문제\n\n[SM2-16 · T3 · DF2]\n"
        set_path, ledger_path, temp = self.write_case(markdown, self.base_rows()[:1])
        self.addCleanup(temp.cleanup)
        failures, _ = MODULE.validate(set_path, ledger_path, 2)
        self.assertTrue(any("missing_ledger_ids=['2']" in failure for failure in failures))

    def test_duplicate_id_fails(self) -> None:
        markdown = "**1.** 문제\n\n[SM2-09 · T2 · DF1]\n"
        rows = [self.base_rows()[0], self.base_rows()[0].copy()]
        set_path, ledger_path, temp = self.write_case(markdown, rows)
        self.addCleanup(temp.cleanup)
        failures, _ = MODULE.validate(set_path, ledger_path, 1)
        self.assertTrue(any("duplicate_ledger_ids=['1']" in failure for failure in failures))

    def test_numeric_only_axis_fails(self) -> None:
        markdown = "**1.** 문제\n\n[SM2-09 · T2 · DF1]\n"
        row = self.base_rows()[0]
        row["non_numeric_axis_1"] = "좌표 변경 2→3"
        set_path, ledger_path, temp = self.write_case(markdown, [row])
        self.addCleanup(temp.cleanup)
        failures, _ = MODULE.validate(set_path, ledger_path, 1)
        self.assertTrue(any("axis_1_numeric_or_cosmetic" in failure for failure in failures))

    def test_type_mismatch_fails(self) -> None:
        markdown = "**1.** 문제\n\n[SM2-09 · T2 · DF1]\n"
        row = self.base_rows()[0]
        row["type_id"] = "SM2-16"
        set_path, ledger_path, temp = self.write_case(markdown, [row])
        self.addCleanup(temp.cleanup)
        failures, _ = MODULE.validate(set_path, ledger_path, 1)
        self.assertTrue(any("type_mismatch" in failure for failure in failures))

    def test_extra_data_column_fails(self) -> None:
        markdown = "**1.** 문제\n\n[SM2-09 · T2 · DF1]\n"
        set_path, ledger_path, temp = self.write_case(markdown, [self.base_rows()[0]])
        self.addCleanup(temp.cleanup)
        lines = ledger_path.read_text(encoding="utf-8").splitlines()
        lines[1] += "\textra"
        self.write_raw_ledger(ledger_path, lines)
        failures, _ = MODULE.validate(set_path, ledger_path, 1)
        self.assertTrue(any("field_count=9 expected=8" in failure for failure in failures))

    def test_wrong_stem_ledger_fails(self) -> None:
        markdown = "**1.** 문제\n\n[SM2-09 · T2 · DF1]\n"
        set_path, ledger_path, temp = self.write_case(markdown, [self.base_rows()[0]])
        self.addCleanup(temp.cleanup)
        wrong_path = ledger_path.with_name("unrelated.novelty.tsv")
        ledger_path.replace(wrong_path)
        failures, _ = MODULE.validate(set_path, wrong_path, 1)
        self.assertTrue(any("ledger_path_mismatch" in failure for failure in failures))

    def test_auxiliary_type_does_not_replace_main_type(self) -> None:
        markdown = "**1.** 문제\n\n[SM2-09 · T3 · DF1·DF2 (+SM2-16)]\n"
        row = self.base_rows()[0]
        set_path, ledger_path, temp = self.write_case(markdown, [row])
        self.addCleanup(temp.cleanup)
        failures, warnings = MODULE.validate(set_path, ledger_path, 1)
        self.assertEqual([], failures)
        self.assertEqual([], warnings)


if __name__ == "__main__":
    unittest.main()
