---
title: 세션 안내 개선 및 Q1 원천·계층 후보 진행
author: 메인 루프 (Codex/OMX)
grade: proposal
state: in-progress
release: blocked
---

## 지침 개선
사용자 요청에 따라 docs/SESSION_HANDOFF_GUIDE.md를 신설했다. STAY/NEW-INDEPENDENT/RETURN-AUTHOR/NEW-CONTINUATION/HOLD, 역할 종료와 과업 종료의 구별, 실행 프롬프트와 완료 후 복귀 메시지를 요구한다. AGENTS.md, CLAUDE.md, ASTRA_EXECUTION_POLICY, REV_GUIDE, README에 참조를 추가하고 check_assurance_contract TEXT_REQUIREMENTS 및 GLOBAL_GUIDANCE_CONTINUITY를 동기화했다.
검증: 실제 TEXT_REQUIREMENTS 초기화 후 전 필수 문자열 검사 missing0; AST 검사 통과; git diff --check 통과. textpatch self-test seeded10/undetected0(고의 결함의 FAIL/WARN 출력은 시험 증거). 전역 동기화 도구는 임시 대상 install/check 통과. 실제 홈 AGENTS는 OUT-OF-SYNC이며 저장소 밖 파일은 수정하지 않았다. 프로젝트 지침은 반영됐지만 전역 배포 완료는 아니다.
전체 assurance 명령 exit1/10 failures: 기존 타인 WIP7건과 ruler3건. 새 지침 문자열 실패 없음. 타인 WIP와 보호 기준은 변경하지 않았다.

## 다음 단계 실행 결과
`260911_09_info_ab50_q1_source_candidate.py`: 동결 원천 파일 집합/해시, 메타 회차와 ID 일치, 명시 통계 적격성 입력, 계층 양방향 집합, 정확 정수 합계·연도·Tier/outside 검증의 미적용 후보다. 운영 도구에 연결하거나 정본 기대값을 변경하지 않았다.
명령: `python output/260911/rev/260911_09_info_ab50_q1_source_fixture.py`
결과: 작성자 시험23건/실패0; 실제60유닛/120파일 일치; 원천 메타6계층 관측. 전체 집합 목록은 `260911_09_info_ab50_q1_source_result.json`에 기록했다. 정상 fixture가 최초에 비율 분모 변수 덮어쓰기를 검출했고 후보 수정 후 같은 시험을 재실행해 통과했다.
미확정 적격성을 넣으면 실패한다. 이 시험은 원천 적격성 승인, 문항 ID 완전성, 전체 Q1 통합 통과가 아니다. 경고를 없애거나 부분 자료를 전체 통과로 취급하지 않았다. 보호 기준3개는 기존 해시 그대로다.

## NEXT
현재 작성 세션 계속(STAY). 08 전파 후보와 09 원천/집합 후보를 통합하고 파싱·기존 fixture/개별 score/r/Tier 회귀를 준비한다. 실제 정식 적격성 disposition은 원천 근거 및 별도 권한 없이는 만들어 넣지 않는다. 전체 후보 준비 후에만 필요한 정책 두 키·독립 패치 판정을 요청한다. 지금 별도 세션을 요구하지 않는다.
Session: STAY — 현재 작성 책임의 후속 후보·시험이 남았다. 사용자에게 새 세션 이동을 요구하지 않음.