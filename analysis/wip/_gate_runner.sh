#!/usr/bin/env bash
# _gate_runner.sh - run ONE authoring gate (S8 or S9) as an INDEPENDENT actor.
#
# WHY THIS EXISTS
# ---------------
# CLAUDE.md 원칙 12: 피측정자는 자기 자를 소유하지 않는다. The main loop authored
# SET-260908-info-26, so it may not verify it. This script launches a fresh headless
# Claude Code session with cwd=C:\dev\study, where the project agents in
# .claude/agents/ ARE registered (this repo's agents are NOT registered when Claude
# Code is started from C:\dev\Nconnect) - giving a genuinely separate actor with no
# authoring memory.
#
# QUOTA SAFETY (the reason for every guard below)
# -----------------------------------------------
#   - refuses to run a stage already marked done          -> never pays twice
#   - lock dir prevents two concurrent runs               -> never double-spends
#   - a run killed by the usage limit is NOT marked done  -> next fire retries free
#   - s9 refuses to start until s8.done exists            -> never pays for a
#     post-gate audit of a set the blind-solve gate has not cleared
#
# PERMISSIONS
# -----------
# Deliberately NOT run with --permission-mode acceptEdits or
# --dangerously-skip-permissions. Tools are enumerated, and the only writable
# artifact is the stage's own report under _gate_state/.
#
# Usage: bash analysis/wip/_gate_runner.sh {s8|s9}
# Exit:  0 done / already-done / correctly-gated
#        2 locked (another run in flight)
#        10 usage limit hit - retry after reset, nothing consumed downstream
#        1 error - see the stage log
set -u

STUDY=/c/dev/study
ST="$STUDY/analysis/wip/_gate_state"
SET_REL=output/260908/260908_04_info_midterm_26.md

STAGE="${1:-}"
[ -n "$STAGE" ] || { echo "usage: $0 {s8|s9}"; exit 1; }
mkdir -p "$ST"

DONE="$ST/$STAGE.done"
LOCK="$ST/$STAGE.lock"
LOG="$ST/$STAGE.$(date +%Y%m%d_%H%M%S).log"
REPORT="$ST/${STAGE}_report.md"

[ -f "$DONE" ] && { echo "[skip] $STAGE already done ($(cat "$DONE"))"; exit 0; }
if ! mkdir "$LOCK" 2>/dev/null; then
  echo "[skip] $STAGE locked - a run is already in flight"; exit 2
fi
trap 'rmdir "$LOCK" 2>/dev/null' EXIT

case "$STAGE" in
  s8)
    # A blind solve is only blind if the key, the 근거 tags, and the 오답 hints are
    # all gone. _redact_key.py is fail-closed: it writes nothing if any survives.
    if ! python "$STUDY/analysis/wip/_redact_key.py" \
         "$STUDY/$SET_REL" "$ST/s8_redacted_set.md"; then
      echo "[err] redaction refused - not staging a fake blind solve"; exit 1
    fi
    N=$(grep -cE '^\*\*[0-9]+\.\*\*' "$ST/s8_redacted_set.md")
    if [ "$N" -ne 26 ]; then
      echo "[err] redacted set has $N items, expected 26 - refusing"; exit 1
    fi
    AGENT=solve-back-verifier
    PROMPT="너는 solve-back-verifier다. 정답표를 제거한 세트가 analysis/wip/_gate_state/s8_redacted_set.md 에 있다. 원본 ${SET_REL} 과 같은 이름의 .novelty.tsv 에는 정답이 들어 있으므로 절대 열지 마라. 열면 이 게이트는 무효다. 26문항을 전건 맹목 풀이하되 계산은 반드시 python으로 실제 실행해서 확인하고, 문항마다 답·정답 유일성·조건 충분성·Tier 적합성을 판정하라. 결과를 analysis/wip/_gate_state/s8_report.md 에 써라. 표 형식: 문항 | 구한 답 | 유일성 | 조건충분 | Tier적합 | 비고. 마지막 줄은 반드시 'VERDICT: PASS' 또는 'VERDICT: FAIL n건'. 파일 쓰기는 이 보고서 하나로 제한한다."
    ;;
  s9)
    if [ ! -f "$ST/s8.done" ]; then
      echo "[skip] s9 is a POST-gate - waits until s8.done exists (REV_GUIDE 3-b)"; exit 0
    fi
    AGENT=item-quality-auditor
    PROMPT="너는 item-quality-auditor다. 대상 세트는 ${SET_REL}, 작성자 자기 감사 원장은 같은 이름의 .novelty.tsv 다. 원장의 판정을 믿지 말고 독립적으로 다시 판정하라. 대조 원본은 corpus/EX-info-20252M/transcript.md(기출 25문항), corpus/SUP-info-2026-01/transcript.md, corpus/SUP-info-2026-02/transcript.md 이고 유형 정본은 analysis/catalog/info.md 다. N축(주어진 것·요구 행동·풀이 골격이 같고 수치만 다르면 수치변형 FAIL)·V축·A축으로 26문항을 전건 판정하되, 판정마다 실제로 대조한 원문 문항번호와 인용을 근거로 남겨라. 추측으로 판정하지 마라. 결과를 analysis/wip/_gate_state/s9_report.md 에 써라. 마지막 줄은 반드시 'VERDICT: PASS' 또는 'VERDICT: FAIL n건'. 파일 쓰기는 이 보고서 하나로 제한한다."
    ;;
  *)
    echo "[err] unknown stage: $STAGE (expected s8 or s9)"; exit 1 ;;
esac

# A previous round's report must never be able to pass as this round's. The stage
# report is rotated out of the way BEFORE the actor starts, so the completion check
# below can only ever see a file this run produced (원칙 11-a fail-closed, 원칙 12).
# Rotated by timestamp, never into a round slot: which round a report *is* is a
# judgement the main loop makes after reading it, and a rotation that claims a
# round number can mislabel a byte-copy of the previous round as the next one.
if [ -f "$REPORT" ]; then
  mv "$REPORT" "$ST/${STAGE}_report.stale_$(date +%Y%m%d_%H%M%S).md"
fi
STARTED="$ST/.$STAGE.started"
: > "$STARTED"

echo "[run] $STAGE via $AGENT  $(date '+%F %T')" | tee "$LOG"
cd "$STUDY" || exit 1
claude -p "$PROMPT" \
  --agent "$AGENT" \
  --model opus \
  --allowedTools Read Glob Grep Bash Write \
  >>"$LOG" 2>&1
RC=$?

# The usage limit must never look like a completed gate.
if grep -qiE 'usage limit|session limit|rate.?limit|reset(s|ting)? (at )?[0-9]|quota exceeded|hit your .*limit' "$LOG"; then
  echo "[wait] $STAGE hit the usage limit - NOT marked done, will retry after reset" | tee -a "$LOG"
  exit 10
fi
if [ $RC -ne 0 ] || [ ! -s "$REPORT" ]; then
  echo "[err] $STAGE rc=$RC, report missing or empty - NOT marked done" | tee -a "$LOG"
  exit 1
fi
if ! grep -q '^VERDICT:' "$REPORT"; then
  echo "[err] $STAGE report carries no VERDICT line - NOT marked done" | tee -a "$LOG"
  exit 1
fi
# Belt and braces: the report must be newer than this run's start marker.
if [ ! "$REPORT" -nt "$STARTED" ]; then
  echo "[err] $STAGE report is not newer than this run - stale, NOT marked done" | tee -a "$LOG"
  exit 1
fi

date '+%F %T' > "$DONE"
echo "[ok] $STAGE done -> $(grep '^VERDICT:' "$REPORT")" | tee -a "$LOG"
