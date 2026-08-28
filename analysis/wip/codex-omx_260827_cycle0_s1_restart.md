---
actor: Codex/OMX
task: cycle0_S1_restart_and_evidence_baseline
target: 2025-2학기 미완료 코퍼스 11개
status: complete
updated: 2026-08-27
---

| no | 범위 | state | 산출물 | 비고 |
|---|---|---|---|---|
| 1 | 이전 실행 인벤토리·PRD·Opus 판정 재검증 | done | 현 세션 증거 | 26 대상 중 corpus 단위 15개 완성·11개 미완료 확인. PRD S1 착수 조건 C1은 기존 PRD v2와 도구 정의에 반영되어 있음. |
| 2 | 2025-2학기 미완료 HWP 11개 기계 변환·매립 이미지 보존 | done | extracted/2025-2학기/, corpus/_images/ | 변환 11/11 exit 0. imgrefs/bindata: math2M 3/3, englishM 3/3, infoM 1/1, scienceM 22/18, socialM 10/20, historyM 16/16, koreanF 2/2, englishF 2/2, scienceF 30/30, socialF 11/11, historyF 7/7. 불일치·복수참조 여부는 다음 품질 검증에서 판정한다. |
| 3 | 완성 15개+신규 11개 S1 품질 기준선 검증 | done | output/260826/260827_02_s1_restart_baseline.md | 26개 중 완성 15개(57.7%)·미완료 11개(42.3%), HWP 25개 기계 변환 완료, bindata 204개를 실측했다. HEAD 변환기 exit 1 대비 현행 exit 0을 동일 원본으로 재현했다. |
| 4 | 누락 11개 축자 전사와 corpus unit 완성 | done | corpus/EX-*/ | EX-english-20252M(32), EX-info-20252M(25), EX-math2-20252M(22), EX-science-20252M(29), EX-social-20252M(25), EX-history-20252M(29), EX-korean-20252F(31), EX-english-20252F(33), EX-science-20252F(33), EX-social-20252F(27), EX-history-20252F(29) 전사·meta·verify_log 완료. 수식이 있는 통합과학 중간/기말은 EQED 원문 레코드(각 81/75건)를 별도 부록으로 보존했다. 이미지 고유 참조/bindata 불일치는 통합사회 중간 10/20, 통합과학 기말 30/30(원문 마커 35회)로 기록했으며 내용 판단은 하지 않았다. EXTRACTION_LOG #53~#59 및 #61·#63~#65를 `추출완료`로 전이했고, 기존 완료 corpus가 있던 #52·#60·#62는 산출물 3종을 재검증하여 상태를 동기화했다. 원장·카탈로그는 S2/Opus 제안·판정 전 수정하지 않는다. |

NEXT: S1 gate 산출물(26/26 corpus unit·각 meta.yml·verify_log.tsv)과 카탈로그 index check를 검증한 뒤, S2 외부 Claude Code Opus `type-proposer` 회람 패키지를 생성한다.

