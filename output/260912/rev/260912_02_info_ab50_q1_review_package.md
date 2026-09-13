---
title: Q1 통합 패치 후보 검토 묶음
author: 메인 루프 (Codex/OMX)
grade: proposal
state: ready-for-review-with-open-evidence
repair_execution: blocked
release: blocked
---

## 작업과 권한
07의 BF1 완결성 승인을 소비하여 08 실패 전파와 09 원천/계층 검증을 통합했다. 정본 도구3개·루브릭·제품은 변경하지 않았다. 명세 재작성/부분 후보별 감사 라운드는 추가하지 않았다. 이 묶음은 운영 반영 승인이나 문항 감사가 아니다.

## 정확한 후보
`260912_01_info_ab50_q1_integrated.patch`와 `260912_01_info_ab50_q1_integrated_candidate.py`.
기준 대상은 tools/regen_rubric_values.py이며 snapshot/dispositions JSON을 별도 입력으로 요구한다. 원천 집합과 bytes/hash, 메타 exam_code와 ID, 적격성 명시 입력을 확인하고 계층 기대 집합을 원천에서 유도한다. 고정4를 집합 대조로 대체하고 합계/Tier/outside를 검사한다. 실패·경고는1, 실행불가·입력/출력 스키마 실패는2로 중단한다. 부분/미확정 적격성을 성공으로 만들지 않는다. 출력에 성공 문자열만 붙이거나 중복 ALL/Tier/계층을 넣어도 통과시키지 않는다.
운영 주의: 기존 무인자 호출과 CLI가 달라진다. **기존 assurance 호출은 아직 이 계약을 공급하지 않는다.** 후보를 단독 적용하면 상위 게이트는 blocked가 된다. 승인된 입력의 소유·동결·공급 방식과 호출부 변경까지 확정하기 전 적용 금지다.

## 실제 시험 증거
명령: `python output/260912/rev/260912_01_info_ab50_q1_integration_test.py`
실행 결과는 같은 디렉터리 `260912_01_info_ab50_q1_integration_result.json`, 측정기 전체 출력은 `260912_01_info_ab50_measure_raw.txt`.
- 통합 경계 시험15건 실패0. 기존 gate0 11개 planted/undetected0. gate0 함수 자체는 변경하지 않았다.
- 실제 원천60유닛/120파일 바이트 대조. source expected/observed/duplicates/missing/extra 목록은 JSON에 기록.
- 메타 기준6계층을 **진단용** derive에 제공하여 기존 gate0를 시험했다. 모든 원천이 정식 통계 적격이라는 판정은 아니다.
- 실제 측정기 exit1/WARN40. 통합 후보는 그 출력을 그대로 보존하고 실패1로 중단했다. 경고0이나 전수 폐쇄를 주장하지 않는다.
- 선택형 per-item 출력1148행은 측정기 두 번 실행의 바이트 일치로 보존을 확인했다. 이는 A/B50 문항 검증 수나 원천 인쇄 ID 커버리지가 아니다.
- 승인된 계약 없이 실제 후보 CLI 실행은 exit2. 성공 문자열이 있으나 파싱 불가한 출력도2. 보호3개 원본 해시 불변.
작성자 시험이지 독립 감사가 아니다. 테스트가 요구하는 입력 형식과 정본 승인 여부는 별개다.

## 완료하지 못한 근거/정책 경계
1. 원천의 인쇄 문항ID 전수와 적격성 dispositions에 대한 승인된 입력이 없다. source bytes 일치나 기존 측정기의 EXCL을 감사권한자의 적격성 판정으로 바꿔 적지 않았다. 실제 부분·합계축 미확인이 남아 있다.
2. 06 contract_exit 정책 사용자 키와 감사키는 07 완결성 승인에 포함되지 않는다. 이번 계속 지시를 모든 경고 면제/정식 적격성 승인으로 확대하지 않았다.
3. 기존 gate0는 통과했지만 정본 A/B/C축 최신 값의 갱신, 호출부 계약 공급, CLI 전역 정상 실행은 완료하지 않았다. 현재 fail-closed를 유지하는 증거만 있다.
4. Q3 정보 구조 난이도 기준 서명 및 A/B 문항 전수 독립 재검증·최종 배포 판정은 별도 잔여다.

## 요청 판정
- [ ] Q1 통합 후보의 실패 전파·집합/합계 검출 구현을 approve/revise-required/reject로 판정한다. 반영 가능한 범위를 정확히 구분한다.
- [ ] Q2 contract_exit 변경의 운영 타당성 및 필요한 사용자 키를 판정한다. 존재하지 않는 사용자 승인이나 적격성 표를 만들어 넣지 않는다.
- [ ] 명령 호출부·원천 적격성/인쇄ID 증거가 없는 상태에서 다음 작성자가 수행할 수 있는 최소 보완 범위를 지정한다. 현행 자를 바꾸거나 배포를 승인하지 않는다.
검토자는 후보를 직접 고치지 않는다. 승인 범위를 넘어 전체 통과로 표시하지 않는다.

## 세션
Session: NEW-INDEPENDENT — 이 작성 세션은 후보 작성자이므로 독립 판정을 겸하지 않는다. 새 판정 역할 완료 후 RETURN-AUTHOR로 본 작성 세션에 회신한다. 본 작성 세션 식별자: 01a0903f-4294-7412-b42b-f5f8b15b98f9 (환경에서 관측된 복귀 식별자이며 권한 증명 아님). 복구 불가 시 NEW-CONTINUATION으로 동일 작성 책임을 승계한다.
복귀 WIP: analysis/wip/solve-back-verifier_260910_info_ab50_newsession.md.