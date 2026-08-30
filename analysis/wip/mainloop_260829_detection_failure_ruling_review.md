---
actor: main-loop
task: detection_failure_ruling_review
target: "260829_01 ruling Q1~Q7, BF1~BF7, and F10"
status: done
updated: 260829
---

# WIP — Opus 판정 후 Codex 전문팀 재검토

배타 소유 = main-loop(Codex/OMX coordinator). 이 WIP은 복구용이며 판정 근거로 인용하지 않는다.

## 목표와 경계

- 목표: 사용자가 반환한 `260829_01_detection_failure_ruling.md`의 사실 재현성, 거버넌스 일관성,
  BF1~BF7의 실행 가능성을 기존 전문 감사팀이 다시 검토하고 Codex/OMX의 의견을 문서화한다.
- 범위: Q1~Q7 7건, BF1~BF7 7건, 신규 F10 1건.
- 이번 라운드는 **읽기·자문·문서화만** 한다. 자, 게이트 코드, generator, 정본, 원장, 기존 판정문은
  수정하지 않는다. 사용자 2차 키나 Opus 승인으로 간주하지 않는다.
- `05_RULING_REVIEW_PREFLIGHT.md`의 입력 목록은 배치용 허용 입력 manifest일 뿐 ruler/evidence freeze가
  아니다. 목록의 완전성이나 판정 독립성을 Codex/OMX가 스스로 승인하지 않는다(F10 방지).

## Staffing matrix

| 순서 | unit/count | 목적 | 허용 입력 | 배타 출력 | lane = model = depth | 예상량 | 동시성 | 검증·중지 조건 | resume |
|---:|---|---|---|---|---|---|---:|---|---|
| 1 pilot | Q3~Q5·F10 4단위 | 원천·코드·수치와 binding fix의 기술적 충분성 검토 | dispatch manifest 16파일 및 그 안의 직접 경로 참조 | `06_EVIDENCE_REVIEW.md` | evidence-auditor = configured gpt-5.6-sol = high; observed unavailable | 1 report, 4 rows 이상 | 1 | 직접 재현 실패·source drift·ruler write 필요 시 BLOCKED | leader가 산출물·해시·경고 검사 후 unit 2 |
| 2 | Q1·Q2·Q6·Q7·BF5~BF7 7단위 | two-key, 독립성, stale 판정, 증거경계의 우회 가능성 공격 | pilot 산출물 + 동일 허용 입력 | `07_GOVERNANCE_CRITIQUE.md` | adversarial critic = configured gpt-5.6-sol = high; observed unavailable | 1 report, severity/disposition | 1 | 사용자 키 대행·ruler 변경·독립성 과장 시 BLOCKED | leader가 쟁점 집계 후 unit 3 |
| 3 | Q1~Q7·BF1~BF7 14단위 | 팀 의견의 결정론적 통합과 허용/금지 다음 단계 판정 | 앞선 두 산출물 + 동일 허용 입력 | `08_RULING_RESPONSE_GATE.md` | gatekeeper = configured gpt-5.6-sol = high; observed unavailable | 1 gate report | 1 | 필수 산출물/해시/쟁점 누락 시 BLOCKED | leader 최종 응답 문서 작성 |

최대 동시성은 1이다. 후속 단위가 선행 산출물에 의존하므로 staged dispatch를 순차 실행한다.

## 슬라이스 상태

| no | 범위 | state | 산출물/근거 |
|---:|---|---|---|
| 1 | 반환 파일·정본·역할 지침 intake | done | 판정문, WIP, REV_LOG 행, CLAUDE 원칙 11~12, REV_GUIDE §5~6-c |
| 2 | dispatch manifest·staffing matrix | done | `05_RULING_REVIEW_PREFLIGHT.md` + 본 문서 |
| 3 | evidence-auditor pilot | done — REVISE | `06_EVIDENCE_REVIEW.md`, SHA-256 `09650d1c12b5377d9d0a215138d029642447dd1007e63bfd2e8abe5b603293b2`; 16/16 manifest, 4/4 IDs, warnings=0 |
| 4 | adversarial governance critique | done — REVISE BEFORE USER KEY | `07_GOVERNANCE_CRITIQUE.md`, SHA-256 `1b88103d63cb5f31317579aa8a3fd50ef8eae7f1d456c432374168d85bbd2411`; 7/7 units, 5/5 pilot findings, warnings=0 |
| 5 | gatekeeper synthesis | done — REVISE-BEFORE-USER-KEY | `08_RULING_RESPONSE_GATE.md`, SHA-256 `cb466c48c9d265c2837755d3be72bb814634adc68b7a140e8abfa6807bf09c1c`; 14/14 units, warnings=0 |
| 6 | main-loop 의견 문서·fresh validation | done | `CODEX_TEAM_RESPONSE_TO_RULING.md`; Q1/Q6 guard부 지지, 나머지 revise, external revision relay 포함 |

## Fresh validation

- `CODEX_TEAM_RESPONSE_TO_RULING.md`: 16035 bytes, SHA-256
  `2dd71e3927cacaf1fb352713eaab1967e8c7da73bfbe4f2505a0e78afc6dc447`; replacement/NUL 0;
  Q1~Q7·BF1~BF7 전건 존재; progress-map 4줄 각 1회.
- `python tools/check_assurance_contract.py`: exit 1, 기존 타 소유 WIP 2파일의 3 failure(s) 그대로.
- `python tools/build_catalog_index.py --check`: exit 0, 131 rows.
- `python tools/build_mastery.py --check`: exit 0, 131 rows, warnings=0.
- `python -X utf8 output/260828/rev/meta_gate_260828.py --check all`: exit 1, 기존 failures=7.
- `python -X utf8 output/260828/rev/gate_selftest_260828.py`: exit 1, baseline failures=5로 clean baseline 아님.
- `git diff --check`: exit 0; 기존 `analysis/REV_LOG.md`, `analysis/wip/mainloop_260826_cycle0_S0.md`
  CRLF 경고만 있으며 이번 라운드 파일 오류는 없다.

## 배타 쓰기

- main-loop: 이 WIP, `05_RULING_REVIEW_PREFLIGHT.md`, `CODEX_TEAM_RESPONSE_TO_RULING.md`.
- evidence-auditor: `06_EVIDENCE_REVIEW.md`만.
- adversarial critic: `07_GOVERNANCE_CRITIQUE.md`만.
- gatekeeper: `08_RULING_RESPONSE_GATE.md`만.
- 공유 정본·원장·ruler·gate·generator·기존 판정/보고서: 전 레인 쓰기 금지.

NEXT: HOLD — current ruling에 사용자 키·BF 구현·ruler 변경·refreeze를 붙이지 않는다. fresh-context
external Opus `rev-arbiter`가 `CODEX_TEAM_RESPONSE_TO_RULING.md` §7 회람을 받아 revised ruling을 만들면,
그 reply의 14-unit coverage·runnable gates·actor/write-surface·해시를 검증한다. 미결 쟁점이 하나라도 있으면
REVISE/HOLD를 유지한다.
