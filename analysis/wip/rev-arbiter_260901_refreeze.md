---
actor: rev-arbiter
task: 260901_refreeze (K1 자 재동결 · BF-K1-5 기대카운트 · 도구 변경 사후판정)
target: output/260831/rev/260831_05_arbiter_ruling_refreeze.md
status: done
updated: 260901
---

| no | 범위 | state | 산출물 | 비고 |
|---|---|---|---|---|
| 0 | frozen_inputs 해시 재측정 | done | (WIP) | 6건 중 5건 일치. `analysis/wip/mainloop_260901_k1_ruler_apply.md` 불일치: 패킷 8867/`086e14c3226f1fd5` vs 실측 11047/`777829e8a34d9ced` (요청 측이 동결 후 계속 추기). 요청문 자체 12932/`2ba84f24aa2fde08` 일치 |
| 1 | U5 자 반영본 대조 (§1·§1-1·§1-2·§1-3·§3·§4·§5·사용지침·이력) | done | (WIP) | 8개 점검항목 전건 반영 확인. reproduce grep = 13행(패킷 주장 일치). Tier 환산열 4x2 = 산술 독립 재현 일치. **결함 2건 적발**: (a) 이력 L216이 측정기 sha `3c3df110844269d6`(10089B) 인용 — 현재 `837d3ab62bde5dca`(11020B), 재현 불가 (b) §1 L21 `440/462=95.2%`를 현행 도구가 재산출 불가(`416/438=95.0%`, GATE3에 EX-science-20242F 추가 배제) |
| 2 | U6 게이트 카운트 실측 | done | (WIP) | 총계 **30**(요청문 포함) / **27**(제외) / live **0**. 패킷은 29/27로 적었으나 실측 30 — 요청문 L98·L99·L109 3행이 자기오염(패킷은 2행으로 계산). 자기오염이 패킷 작성 중에도 1건 증가한 실증 |
| 3 | U7 축 보류 표식 | done | (WIP) | `축 보류` 4파일 5건(catalog_update_SS 1 · type_analysis_SC 1 · SM2 1 · SS 2) 패킷 일치. `Tier 재도출 대기` 총 53건 = _01 파일 52 + 요청문 1 |
| 1 | U5 자 반영본 대조 (§1·§1-1·§1-2·§1-3·§3·§4·§5·사용지침·이력) | done | (WIP) | 8개 점검항목 전건 반영 확인. reproduce grep = 13행(패킷 주장 일치). Tier 환산열 4x2 = 산술 독립 재현 일치. 결함 2건 적발: (a) 이력 L216이 측정기 sha 3c3df110844269d6(10089B) 인용 - 현재 837d3ab62bde5dca(11020B), 재현 불가 (b) §1 L21 440/462=95.2%를 현행 도구가 재산출 불가(416/438=95.0%, GATE3에 EX-science-20242F 추가 배제) |
| 2 | U6 게이트 카운트 실측 | done | (WIP) | 총계 30(요청문 포함) / 27(제외) / live 0. 패킷은 29/27로 적었으나 실측 30 - 요청문 L98·L99·L109 3행이 자기오염(패킷은 2행으로 계산) |
| 3 | U7 축 보류 표식 | done | (WIP) | 축 보류 4파일 5건(catalog_update_SS 1 · type_analysis_SC 1 · SM2 1 · SS 2) 패킷 일치. Tier 재도출 대기 총 53건 = _01 파일 52 + 요청문 1 |
| 4 | U8 측정기 코드 감사 + 실행 | done | (WIP) | fail-closed 전환 확인(L216-227, 허용목록 신설 없음, exit 0->1). check_assurance_contract 7 FAIL(전부 타 배우 WIP 형식), measure_score_bands 행 소멸 확인. **반증**: 패킷의 "측정값 출력은 전량 유지" 는 거짓 - GATE3 자동배제가 EX-science-20242F(24문항, GATE1 앵커 검증분)를 추가 배제해 모집단 462->438, 서명값 95.2%->95.0% |
| 5 | U8 최소수리 폐쇄시험 | done | (WIP) | EXCL에서 앵커+문항수일치 유닛 제외 -> 462/440 = 95.2%, 계층 100.0/96.6/100.0/86.9 - 서명값과 축자 일치. 추가 결함: T4 구간이 반개구간 [1.067,1.200)이라 r=1.200 정확 4문항(english-20242F 1 · 20242M 3)이 전 Tier 밖. 닫힌구간이면 T4=100 = 판정 260831_04 §1-8 값 |
| 6 | U6 게이트 규칙 폐쇄시험 + fixture | done | (WIP) | 규칙 v2(경로허용 11 + 게이트명령 리터럴 3 + 이력표식 16) -> LIVE 0, 분류 30/30 = 100.0%. fixture(알려진 실패 9건 재현) 9/9 검출, undetected=0 |
| 7 | 판정문 작성 | done | output/260831/rev/260831_05_arbiter_ruling_refreeze.md (38294 B) | §6-d (2) 고정 절 + 7열 표. U5 refreeze-with-corrections · U6 선지 C · U7 open-new-round(병합) · U8 ratify-with-condition. 구속 6(BF-RF-1~6) · 비구속 6(F-RF-1~6) |
| 8 | REV_LOG 1행 append | done | analysis/REV_LOG.md 말미 | 5필드 = 헤더 일치 확인. 자·도구·산출물 무수정 확인(DIFFICULTY_RUBRIC 0e8ec7a8c44d87c0 · measure_score_bands 837d3ab62bde5dca 불변), 커밋 없음 |

NEXT: (없음 - 판정 종결). 반영 주체는 BF-RF-1~6 처리 후 재동결 지문 a204f3412cf900b5 불변 확인.
