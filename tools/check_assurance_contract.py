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

# --------------------------------------------------------------------------
# Structural checks (260828).  The substring table above proves a marker EXISTS
# somewhere; it cannot prove the rule REACHED the actor that must obey it.  The
# 260828 system audit measured `resume audit` present in AGENTS.md and absent
# from all 11 agent definitions while this file still printed PASS.  These
# checks close that class: they read the canon and the definitions and compare.
# --------------------------------------------------------------------------

AGENT_DIR = ROOT / ".claude/agents"
AGENT_FILES = sorted(AGENT_DIR.glob("*.md"))

if not AGENT_FILES:
    fail(".claude/agents/: no agent definitions found")

# 1. Continuity rule (CLAUDE.md 서브에이전트 공통 실행 규격 ⑤) must reach every actor.
CONTINUITY_MARKERS = ("HOLD — resource exhausted", "resume audit")
for path in AGENT_FILES:
    text = path.read_text(encoding="utf-8")
    for needle in CONTINUITY_MARKERS:
        if needle not in text:
            fail(f".claude/agents/{path.name}: missing continuity marker {needle!r}")

# 2. Tool-grant coupling (CLAUDE.md 원칙 ④ / REV_GUIDE §5).  An actor the write-surface
#    table tells to write must actually hold Write; one that appends to a shared ledger
#    (_index / REV_LOG) must also hold Edit.  Without this the actor shells around the
#    grant or silently disobeys.
rev_guide = (ROOT / "analysis/REV_GUIDE.md").read_text(encoding="utf-8")
section5 = rev_guide.split("## 5. Actors", 1)[-1].split("\n## 6.", 1)[0]
actor_rows = []
for line in section5.splitlines():
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) != 3 or cells[0] in ("Role", "------"):
        continue
    names = [n for n in cells[1].split("`") if (AGENT_DIR / f"{n}.md").exists()]
    if names:
        actor_rows.append((names[0], cells[2]))

if len(actor_rows) < 8:
    fail(f"REV_GUIDE §5: parsed only {len(actor_rows)} agent rows — table shape changed")

for actor, surface in actor_rows:
    tools_line = ""
    for line in (AGENT_DIR / f"{actor}.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("tools:"):
            tools_line = line
            break
    granted = {t.strip() for t in tools_line[len("tools:"):].split(",")}
    if "Write" not in granted:
        fail(f".claude/agents/{actor}.md: REV_GUIDE §5 assigns a write surface but tools: has no Write")
    if ("_index" in surface or "REV_LOG" in surface) and "Edit" not in granted:
        fail(f".claude/agents/{actor}.md: §5 surface includes a shared ledger but tools: has no Edit")

# 3. WIP checkpoint files must be resumable: declared actor, enum status, NEXT pointer.
WIP_STATUS = {"in-progress", "done", "blocked"}
for path in sorted((ROOT / "analysis/wip").glob("*.md")):
    if path.name.startswith("_"):
        continue
    lines = path.read_text(encoding="utf-8").splitlines()
    status = next((l.split(":", 1)[1].strip() for l in lines if l.startswith("status:")), None)
    if status is None:
        fail(f"analysis/wip/{path.name}: no status: field (CLAUDE.md 규격 ②)")
    elif status not in WIP_STATUS:
        fail(f"analysis/wip/{path.name}: status {status!r} outside {sorted(WIP_STATUS)}")
    if not any(l.startswith("NEXT:") for l in lines):
        fail(f"analysis/wip/{path.name}: no NEXT: line — cannot be resumed")

# 4. Fail-closed tools (CLAUDE.md 원칙 11).  A tool that can print [WARN] must have a
#    nonzero exit path; a warning channel with no failure channel is fail-open by design.
for path in sorted((ROOT / "tools").glob("*.py")):
    text = path.read_text(encoding="utf-8")
    if "[WARN]" in text and "[FAIL]" not in text:
        fail(f"tools/{path.name}: prints [WARN] but has no [FAIL] path (fail-open)")

# 5. Companion-update list (CLAUDE.md 원칙 10).  A canon document that other files must
#    follow has to name its own dependents, or an edit to it silently desynchronises them.
COMPANION_REQUIRED = [
    "CLAUDE.md",
    "AGENTS.md",
    "analysis/REV_GUIDE.md",
    "analysis/FORECAST_GUIDE.md",
    "analysis/DOC_LOCATION.md",
    "analysis/TYPE_CATALOG.md",
    "analysis/catalog/CODE_REGISTRY.md",
    "analysis/catalog/_README.md",
    "docs/DATA_STANDARD.md",
]
for relative in COMPANION_REQUIRED:
    path = ROOT / relative
    if not path.exists():
        fail(f"{relative}: canon document missing")
        continue
    if "동반 갱신 목록" not in path.read_text(encoding="utf-8"):
        fail(f"{relative}: no 동반 갱신 목록 section (CLAUDE.md 원칙 10)")

# 6. Ruler gate (CLAUDE.md 원칙 12 / REV_GUIDE §5-a; ruling 260831_08 BF-R3·Q7).  The ruler
#    cites values that only the measurer can produce.  Nothing ran that comparison on a
#    schedule, so a ruler could go stale between rounds and every verdict issued from it
#    would be stale too, silently.  This runs the gate.  A ruler change without a matching
#    tool run is exactly the failure this catches, so there is no opt-out flag: 원칙 11
#    forbids a warning channel with no failure channel.
RULER_SUBJECTS = [
    "analysis/catalog/DIFFICULTY_RUBRIC.md",
    "tools/measure_score_bands.py",
    "tools/regen_rubric_values.py",
]
for relative in RULER_SUBJECTS:
    if not (ROOT / relative).exists():
        fail(f"{relative}: two-key ruler subject missing (REV_GUIDE §5)")

rev_five = rev_guide.split("## 5. Actors", 1)[-1].split("\n## 6.", 1)[0]
for relative in RULER_SUBJECTS:
    if relative not in rev_five:
        fail(f"REV_GUIDE §5: two-key subject list does not name {relative}")

# The gate runs even when earlier checks failed: gating it behind `failures == 0` would let
# an unrelated pre-existing failure switch the ruler axis off silently (fail-open).
if all((ROOT / r).exists() for r in RULER_SUBJECTS):
    import subprocess

    proc = subprocess.run(
        [sys.executable, str(ROOT / "tools/regen_rubric_values.py")],
        capture_output=True,
        cwd=ROOT,
    )
    out = (proc.stdout + proc.stderr).decode("utf-8", "replace").replace("\r\n", "\n")
    if proc.returncode != 0:
        fail(f"ruler gate: regen_rubric_values.py exit={proc.returncode} (expected 0)")
    if "[GATE 0 PASS] undetected=0" not in out:
        fail("ruler gate: detector did not prove its own detection power (원칙 12-d)")
    if "stale=0 lines=0 residual=0" not in out:
        line = next((l for l in out.split("\n") if l.strip().startswith("stale=")), "?")
        fail(f"ruler gate: ruler is stale -- {line.strip()}")
    warn = [l for l in out.split("\n") if "[WARN]" in l]
    if warn:
        fail(f"ruler gate: {len(warn)} warning line(s), expected 0 -- {warn[0].strip()}")
    findings = [l for l in out.split("\n") if l.startswith("  :")]
    if findings:
        fail(f"ruler gate: {len(findings)} finding line(s), expected 0 -- {findings[0].strip()}")

if failures:
    print(f"assurance-contract: {failures} failure(s)")
    raise SystemExit(1)
print(f"assurance-contract: PASS (0 failures, {len(AGENT_FILES)} agents, "
      f"{len(actor_rows)} §5 rows checked)")
