#!/usr/bin/env python3
"""Install or verify the repository-owned continuity block in global AGENTS.md."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
FRAGMENT = ROOT / "docs" / "GLOBAL_GUIDANCE_CONTINUITY.md"
START = "<!-- STUDY:GLOBAL-CONTINUITY:START -->"
END = "<!-- STUDY:GLOBAL-CONTINUITY:END -->"


def normalized(text: str) -> str:
    return text.replace("\r\n", "\n").rstrip() + "\n"


def render(current: str, fragment: str) -> str:
    current = normalized(current)
    fragment = normalized(fragment).strip()
    start_at = current.find(START)
    end_at = current.find(END)
    if (start_at == -1) != (end_at == -1):
        raise ValueError("global AGENTS.md has only one continuity marker")
    if start_at != -1:
        if end_at < start_at:
            raise ValueError("global AGENTS.md continuity markers are reversed")
        end_at += len(END)
        return normalized(current[:start_at] + fragment + current[end_at:])
    anchor = "\n## Setup\n"
    if anchor not in current:
        raise ValueError("global AGENTS.md is missing the expected '## Setup' anchor")
    return normalized(current.replace(anchor, f"\n\n{fragment}\n{anchor}", 1))


def digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--check", action="store_true")
    action.add_argument("--install", action="store_true")
    parser.add_argument(
        "--target",
        type=pathlib.Path,
        default=pathlib.Path.home() / ".codex" / "AGENTS.md",
    )
    args = parser.parse_args()

    fragment = FRAGMENT.read_text(encoding="utf-8")
    current = args.target.read_text(encoding="utf-8")
    expected = render(current, fragment)
    current_normalized = normalized(current)
    if args.check:
        if current_normalized != expected:
            print(f"global-guidance: OUT-OF-SYNC target={args.target}")
            return 1
        print(
            "global-guidance: PASS "
            f"target={args.target} sha256={digest(current_normalized)}"
        )
        return 0

    if current_normalized == expected:
        print(
            "global-guidance: UNCHANGED "
            f"target={args.target} sha256={digest(current_normalized)}"
        )
        return 0
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = args.target.with_name(f"{args.target.name}.{stamp}.bak")
    shutil.copy2(args.target, backup)
    args.target.write_text(expected, encoding="utf-8", newline="\n")
    print(
        "global-guidance: INSTALLED "
        f"target={args.target} backup={backup} sha256={digest(expected)}"
    )
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
