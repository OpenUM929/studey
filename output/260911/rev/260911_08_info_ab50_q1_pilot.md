---
title: Q1 하위 실패 전파 패치 후보 파일럿
author: 메인 루프 (Codex/OMX)
grade: proposal
state: partial
repair_execution: blocked
release: blocked
---

## 승인 소비 범위
07 판정의 BF1 완결성 approve를 확인했다. Q1 후보 준비만 허용하며 코드 반영 승인으로 확대하지 않았다. 이번은 실패 전파 1개 경계의 파일럿이다. Q1 전체 완료나 독립 감사가 아니다.

## 파일
같은 디렉터리의 `260911_08_info_ab50_q1_propagation.patch`는 tools/regen_rubric_values.py에 대한 미적용 unified diff다. `260911_08_info_ab50_q1_regen_candidate.py`는 그 결과 복제본이며 직접 운영 실행용이 아니다. `260911_08_info_ab50_q1_fixture.py`는 AST에서 후보 main만 추출해 하위 측정/derive 경계를 대체하는 시험이다. `260911_08_info_ab50_q1_fixture_result.json`은 실행 증거다.

## 변경 후보
하위 exit1/WARN/FAIL은 contract_exit1, 실행 불가/비정상 종료/검출력 실패/필수 성공 표식 누락은2로 중단한다. 원 출력과 원 종료 코드를 남긴다. 통과한 측정 출력만 기존 derive로 넘긴다. 파서·통계 산식·ALLOW·원천·루브릭은 변경하지 않았다.

## 검증
명령: `python output/260911/rev/260911_08_info_ab50_q1_fixture.py`
결과: exit0, fixture12개/실패0. 이것은 작성자 후보 시험이며 규범 게이트가 아니다. 정상 케이스는 derive 도달까지만 확인하며 전체 성공을 뜻하지 않는다. 정본 버전은 실패 입력에도 derive에 도달하거나 OSError를 그대로 내므로 후보의 방어 경계를 비교할 수 있었다. 정본 전체가 모든 실패를 최종 PASS로 처리한다는 주장은 아니다.
실측 측정기 출력: child_exit1, WARN40, 후보 contract_exit1. 경고와 실패를 숨기지 않고 보존했다. 원천 오류를 해결했거나 원천의 부분 사용을 승인했다는 뜻이 아니다.
보호 기준3개 해시는 이전 동결과 일치한다. 정본 반영·배포·독립 승인 없음.

## 잔여 / 다음 소유자 작업
1. Q1의 원천 manifest 재유도·해시 drift, 메타 기반 계층 집합 대조(고정4 대체), ID 전수/합계/Tier 불변식 후보와 fixture를 준비한다.
2. 이 파일럿은 파싱 실패를 contract_exit2로 정규화하는 후속 경계, 정상 전체 실행, 기존 gate0 fixture 통합까지 검증하지 않았다. 현재 후보의 derive에는 기존 고정4 제한이 그대로 남아 있다. 그러므로 이 diff만 적용해선 Q1을 해결하지 못한다.
3. 전체 후보가 준비되면 정책 사용자 키/독립 패치 판정 후 승인 범위만 반영·재동결한다. Q3와 문항 전수검증은 별도 잔여다. 이번 파일럿만 다시 독립 승인받는 단계를 추가하지 않는다.