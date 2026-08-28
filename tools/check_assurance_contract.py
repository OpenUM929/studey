#!/usr/bin/env python3
"""Static regression checks for the assessment assurance workflow.

This intentionally checks policy invariants, not a team's claimed result.  It
keeps a future edit from silently restoring the shortcuts that caused the
2026-08 comparison failure.
"""
from __future__ import annotations

import pathlib
import sys
import tomllib

ROOT = pathlib.Path(__file__).resolve().parents[1]

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

TEXT_REQUIREMENTS = {
    "AGENTS.md": [
        "runtime identity",
        "row count alone",
        "expected item identifiers",
        "one main session and one pilot slice",
        "actual-team",
        "HOLD — resource exhausted",
        "resume audit",
        "never busy-wait",
    ],
    "CLAUDE.md": [
        "HOLD — resource exhausted",
        "resume audit",
        "remaining context is 60% or less",
    ],
    "docs/CODEX_TEAM_ASSURANCE_GUIDE.md": [
        "runtime identity",
        "expected item identifiers",
        "No row-count-only",
        "one main session",
        "blocked",
        "resource-exhaustion checkpoint",
        "resume audit",
    ],
    "docs/OPUS_ASSURANCE_TEAM.md": [
        "runtime evidence",
        "expected item identifiers",
        "No row-count-only",
        "independent context",
    ],
    "docs/GLOBAL_GUIDANCE_CONTINUITY.md": [
        "STUDY:GLOBAL-CONTINUITY:START",
        "remaining model context is 60% or less",
        "HOLD — resource exhausted",
        "resume audit",
        "busy-wait",
    ],
    "tools/sync_global_continuity_guidance.py": [
        "GLOBAL-CONTINUITY:START",
        "--check",
        "--install",
        "sha256",
    ],
    ".claude/agents/type-proposer.md": [
        "expected item identifiers",
        "duplicate",
        "BLOCKED",
        "HARVEST_LOG",
        "EXTRACTION_LOG",
    ],
}

ROLE_FILES = [
    ".codex/agents/assessment-author-sol.toml",
    ".codex/agents/assessment-evidence-auditor-sol.toml",
    ".codex/agents/assessment-adversarial-critic-sol.toml",
    ".codex/agents/assessment-gatekeeper-sol.toml",
]


def fail(message: str) -> None:
    print(f"FAIL {message}")
    global failures
    failures += 1


failures = 0
for relative, needles in TEXT_REQUIREMENTS.items():
    path = ROOT / relative
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"{relative}: unreadable: {exc}")
        continue
    for needle in needles:
        if needle not in text:
            fail(f"{relative}: missing policy marker {needle!r}")

for relative in ROLE_FILES:
    path = ROOT / relative
    try:
        with path.open("rb") as handle:
            role = tomllib.load(handle)
    except (OSError, tomllib.TOMLDecodeError) as exc:
        fail(f"{relative}: invalid TOML: {exc}")
        continue
    if role.get("model") != "gpt-5.6-sol":
        fail(f"{relative}: model must be gpt-5.6-sol")
    if role.get("model_reasoning_effort") != "high":
        fail(f"{relative}: must use runtime-supported high effort, not an inferred depth")
    instructions = role.get("developer_instructions", "")
    for needle in (
        "exclusive",
        "runtime",
        "expected item identifiers",
        "HOLD — resource exhausted",
        "resume audit",
    ):
        if needle not in instructions:
            fail(f"{relative}: missing role safeguard {needle!r}")

if failures:
    print(f"assurance-contract: {failures} failure(s)")
    raise SystemExit(1)
print("assurance-contract: PASS (0 failures)")
