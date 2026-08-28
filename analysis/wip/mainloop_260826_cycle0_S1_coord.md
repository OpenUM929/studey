---
actor: main-loop
task: cycle0_S1_coordination
target: S1 REFINE 26 corpus units (P0 완료 후 웨이브 기동)
status: in-progress
updated: 260826
---

## P0 이행 ([OC 지시] 260826_03)
- P0-1 done — CODE_REGISTRY §3 `info` 행 + DATA_STANDARD §5.8 `info` 행 + §6 선행 판단 기록
- P0-2 done — CODE_REGISTRY §6 결정 블록에 math1 연장 확정(EX-math1-20242M/F, 선례 20241M/F)
- P0-3 done — PRD §3 S1 게이트 PDF(22→7)·HWP(24→25), type-extractor.md 24→25
- P0-4 done — corpus/SUP-M2-2026 → SUP-math2-2026 rename(불변식 PASS, meta id 일치).
  원인: 같은 PRD L448 구경로 지시가 A1 개명 결정을 따라가지 못함(부분 갱신 → 원칙 10 실증).
  보완: DATA_STANDARD §1.3·corpus/_README 불변식+검증 명령 명문화, 양쪽 이력 기록.

## G6 baseline (S1 착수 시점 sha256 앞16)
HARVEST_LOG 842427fbf2c3d658 · EXTRACTION_LOG d7ce74e4f2ec84c0 ·
ATTEMPT_LOG c130c71adccdb558 · MASTERY d637117febfac18d · WEAK_LEDGER ffae9938e32910ed

## 유닛 슬라이스 (26)
| no | ID | state | 산출물 | 비고 |
|----|----|-------|--------|------|
| 1 | EX-info-20252F | done | 25/25문항 · m=1 해소 · unreadable 0 | 시행일 불일치는 내 스모크 오류(중간 파일 실은 것) — 에이전트 판정 옳음 |
| 2 | EX-korean-20242M | done | 28/28(24+4) · m=1 해소 · unreadable 0 | 공급자 오류 3회 후 4차 성공 · EQED 0건 확인 |
| 3 | EX-math2-20252F | done | 23/23 · m=5 해소 · unreadable 0 | **EQED 수식 180건 유실 발견→레코드 직독 복원** · 배점 합계 100.0 자체검증 |
| 4~26 | 나머지 23건 | pending | 후속 웨이브 | ★대형 8건 단독 인스턴스 · PDF(EX-science-20242M) 마지막 배치 |

NEXT: wave2 기동(중형 HWP: math1-20242M/F, english-20242F, social-20242F, history-20242F 등) →
전 유닛 완료 후 S1 종합보고(G5 전체 카운트·G6 후후 대조표 포함).
신규 도구 결함 D4 후보: hwp2md.py EQED 수식 무흔적 유실(math2 실측 180건) — type-extractor.md
고지 목록 반영 여부는 CC 판정 사항, 현재는 에이전트 프롬프트 경고+레코드 직독 우회로 운용.
