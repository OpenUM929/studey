---
actor: main-loop
task: detection_failure_audit
target: "Opus findings F1/F2-b/F3/F6/F9 and Codex/OMX detection/ownership controls"
status: done
updated: 260829
---

# WIP — Codex 탐지 실패 전문 감사팀

배타 소유 = main-loop(Codex/OMX coordinator). 이 WIP은 복구용이며 보고서 근거로 인용하지 않는다.

## 목표와 경계

- 목표: Codex/OMX가 F1·F2-b·F3·F6·F9를 사전에 탐지하지 못한 구조적 이유를 독립 레인으로
  재검증하고, 재발 방지 방법을 Opus가 후속 검토할 수 있는 문서로 남긴다.
- 이번 라운드는 **감사·설계 제안만** 한다. 정본, 원장, 수용기준, 기대값 표, 게이트 코드를 수정하지 않는다.
- 특히 F6·F9와 F1·F3의 게이트 검출력은 자(ruler) 영역이다. 팀은 결함과 대안을 보고하지만
  자의 선택·개정·승인·재동결을 하지 않는다.

## 슬라이스와 상태

| no | 범위 | state | 소유/산출물 | 중지 조건 |
|---:|---|---|---|---|
| 1 | 사전점검·동결·staffing matrix | done | main-loop / `output/260829/rev/detection-failure-audit/00_PREFLIGHT.md` | 입력 해시·배타 경로·검증 형식 누락 시 BLOCKED |
| 2 | 대표 파일럿: 5개 발견의 1차 원인 분석 | done | assessment-author-sol / `01_author_root_cause.md` | 5/5 ID, frozen hash 13/13, 배타 출력 통과; observed model/depth telemetry unavailable |
| 3 | 독립 증거 감사 | blocked | assessment-evidence-auditor-sol / `02_evidence_audit.md` | F1/F3 PASS; F2-b/F6/F9 raw 재현 BLOCKED; runtime telemetry 없음 |
| 4 | 차단상태 적대적 재발 검토 | done | assessment-adversarial-critic-sol / `03_adversarial_review.md` | clean-context; dependency-closure failure와 통제 우회 6종 확인 |
| 5 | 통합 게이트·최종 보고서 | done | assessment-gatekeeper-sol + main-loop / `04_GATE.md`, `FINAL_REPORT_FOR_OPUS.md` | 최종 verdict `▲ blocked — BLOCKED`; Opus review relay만 허용 |

## 배타 쓰기

- main-loop: 이 WIP, `00_PREFLIGHT.md`, `04_GATE.md`, `FINAL_REPORT_FOR_OPUS.md`
- assessment-author-sol: `01_author_root_cause.md`만
- assessment-evidence-auditor-sol: `02_evidence_audit.md`만
- assessment-adversarial-critic-sol: `03_adversarial_review.md`만
- 공유 원장·정본·자 파일: 전 레인 쓰기 금지

## 현재 증거

- 사용자 승인 범위: Opus 실측 F1·F2-b·F3·F6·F9를 대상으로 전문 감사팀 구성 및 문서화.
- 입력 파일 13개와 SHA-256은 `00_PREFLIGHT.md`에 동결.
- 단위 ID: `F1`, `F2-b`, `F3`, `F6`, `F9` (5개).
- 현재 정본 계약 게이트는 다른 소유자의 WIP 2파일 때문에 3 failure(s), exit 1을 유지한다.
- author native runtime identity는 `/root/detection_author_pilot`; 실제 model/depth telemetry는 surface가
  노출하지 않았다. 따라서 품질 감사는 계속하되 `actual-team` 실행능력 증명과 외부 비교 readiness는
  `▲ blocked`로 유지한다. 설정 TOML을 실행 증거로 승격하지 않는다.
- evidence audit은 C-01(runtime telemetry), C-02(raw evidence), C-03(gate 개정자와 qualifier 분리)을
  critical로 판정했다. author와 auditor는 `fork_turns=all`로 시작되어 independent-context 증거도 없고
  `shared-context`로 재분류한다.
- critic은 `/root/detection_blocked_critic`, `fork_turns=none`, exclusive output 1파일로 실행되었으나
  model/depth telemetry는 여전히 unavailable이다. critic 존재는 기존 BLOCKED를 치유하지 않는다.
- gatekeeper는 `/root/detection_gatekeeper`, `fork_turns=none`; required artifact 4/4와 frozen input
  13/13 hash 일치, 5-ID exact coverage를 확인하고 `BLOCKED` 판정했다.
- 최종 보고서: `output/260829/rev/detection-failure-audit/FINAL_REPORT_FOR_OPUS.md`, 19610 bytes,
  SHA-256 `5b2c553b323f33a9ddaf064d2dceb8c3f0383249f5d13918d757974fe9e06f07`.

## 다음 검증 명령

```powershell
python tools/check_assurance_contract.py
python tools/build_catalog_index.py --check
python tools/build_mastery.py --check
```

NEXT: 외부 Claude Code Opus `rev-arbiter` 단일 세션의 회신 파일 `output/260829/rev/detection-failure-audit/260829_01_detection_failure_ruling.md`가 생성될 때까지 HOLD. 회신을 읽고 7개 질문의 ruling·근거·binding fixes가 완전한지 검증하기 전에는 ruler 수정, 새 파일럿, benchmark/comparison/release를 시작하지 않는다.
