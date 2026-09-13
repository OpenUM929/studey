---
author: 메인 루프
executor: Codex/OMX
grade: proposal
status: blocked
date: 2026-09-11
requested_model: gpt-6-astra
observed_model: unavailable
observed_reasoning_depth: unavailable
release: blocked
---
# 정보 A/B 50제 — 감사 현황 및 배포 승인 검수

## 결론: ▲ blocked — 배포 승인 불가
이 문서는 미완료 품질감사를 완료로 바꾸는 판정문이 아니다. 기존 증거와 현재 승인 게이트를 검수한 **현황 보고서**다. 제품·인덱스·공유 원장·자의 파일은 수정하지 않았다.

- 동결 문제 A25+B25 해시가 동일하다. 답을 개봉하기 전 저장한 자체 풀이50개와 답지 대조50/50, 해설·채점 대조50/50은 WIP의 이전 구간 결과를 이월한다. 이번 재개를 새 맹목 풀이로 표시하지 않는다.
- 교과서 실제 열람33/33 기록 및 파일별 해시는 WIP에 있다. 열람 완료는 제품 반영 완료가 아니다. 기출 시험 이미지는 미열람(전사만 확인). `_29.jpg` 쪽수 앞부분은 잘렸으므로 전체 파일명으로 인용했다.
- 이번 MD 내용 검사: 문제/답 ID 각50, 두 세트 각각 문제 본문과 답지 본문 전체가 통합본에 포함됨. 각25×4=100점, 채점기준 각25개. HTML/PDF 인쇄 검수는 미실행.
- 호스트가 실제 모델·깊이를 제공하지 않았다. 사용자 Astra 지정과 실행 증명은 다르므로 인증된 Astra 독립 검증 커버리지는 미확인이다. Opus 부재 자체를 차단 사유로 삼지 않는다.

## 재개 시 발견한 기준 변경 — 기존 카탈로그 결론 이월 금지
`analysis/catalog/info.md`는 종전 47631 bytes / SHA256 `be569576e45f8b92b913b50a89058596708eb1b709a75d730f8a97b71572e1f3`에서 현재 63937 bytes / `171b7d8a671f39a9fc6826feec7312059e97a6dc5dae0c02361cfe22a8080ca9`로 변경됐다. 재개 해시 불일치이므로 카탈로그 의존 결론의 현행 승인은 차단한다. 변경이 부당하다고 단정하거나 자를 되돌리지 않는다.
현재 `.claude/agents/item-quality-auditor.md` V1은 발화 / ▲ ruler-gap / FAIL 및 실제 오독 계산을 요구한다. 그 근거인 `output/260911/rev/260911_01_info_v1_criterion_ruling.md` 앞부분은 읽었지만, 그 문서는 기존26제 대상이지 A/B 승인문이 아니다. 문서의 binding 표기를 이번 실행이 인증하지도 않았다. two-key·재동결 이력과 변경 영향을 확인한 뒤 현행 자로 전건 재측정해야 한다.
난이도 자와 TYPE_MASTER는 종전 해시와 동일하다(아래 증거).

## 최고 난이도 목표
사용자 요구: **기존 최고 난이도 수준 + 필수적인 추가 사고력**. 코드 길이·계산량·알고리즘 명칭만으로 충족하지 않는다. 기존 WIP 구조 의견은 T2 성격32 / T3 후보18이며 정식 티어 판정이 아니다. 제공 코드의 유한 추적과 중간 상태 설명만으로 답할 수 있어 필수적인 추가 사고력은 50문항에서 입증되지 않았다. 머리말도 중상 목표·최고난도 인증 아님·Tier 미확정이라고 밝힌다. 따라서 거짓 T4 표기 결함이 아니라 사용자 추가 목표의 미충족이다.
개편할 최고 구간은 조건 역구성·반례·선택/설계·정당화 등의 요구 행동을 실제로 추가하고, 최단 유효 풀이에서도 그것이 필요한지 검증해야 한다. 감사자는 문제나 난이도 자를 수정하지 않는다.

## 전수 현황 50행
아래는 기존 WIP 구조 의견을 현재 동결 문제와 연결한 표다. **최근접 원본, 등록 축·함정 발화, 신규성, 범위, 태그의 종합 N/V 최종 판정은 전건 BLOCKED**이며 해당 전수 검사를 완료했다고 주장하지 않는다. 모든 정식 Tier·공식 시험범위는 미확정이고 학생 오답 기록도 없다. 미완료 행을 삭제하지 않았다. 답·해설 상세 중간값은 WIP §정답·해설 대조 50행에 있다.

| ID | 문제 근거 | 기존 잠정 구조 의견 | 최단 추론·의존 관계 | 답 대조 | N/V 최종 판정 |
|---|---|---|---|---|---|
| A/1 | output/260910/260910_01_info_composite_a_questions_review.md:L24 | T2 성격(정형 변형·순차 추적) | 잔액을 읽어 분기하고 갱신; 고정 상태표로 완결 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/2 | output/260910/260910_01_info_composite_a_questions_review.md:L48 | T2 성격(정형 변형·순차 추적) | 갱신된 앞 원소를 재사용; 누적합 한 규칙으로 완결 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/3 | output/260910/260910_01_info_composite_a_questions_review.md:L69 | T2 성격(정형 변형·순차 추적) | 첫 원소→나머지→회전→다시 회전; 입력 변화 추적 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/4 | output/260910/260910_01_info_composite_a_questions_review.md:L93 | T2 성격(정형 변형·순차 추적) | 행 조건→최대-최소 누적; 행별 독립 계산 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/5 | output/260910/260910_01_info_composite_a_questions_review.md:L116 | T2 성격(정형 변형·순차 추적) | 슬라이스→두 비교→분기; 주어진 조건 직접 대입 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/6 | output/260910/260910_01_info_composite_a_questions_review.md:L139 | T3 후보 성격(조건·상태 결합) | 다음 원소 포함 합으로 수용 여부; 종료 경계와 인덱스 동시 추적 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/7 | output/260910/260910_01_info_composite_a_questions_review.md:L163 | T3 후보 성격(조건·상태 결합) | 두 함수 관측 조건이나 후보1~9 전수 대입이 코드로 제공됨; 역산 발상 불필요 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/8 | output/260910/260910_01_info_composite_a_questions_review.md:L189 | T3 후보 성격(조건·상태 결합) | 행 합→대소·동점 인덱스→순위; 조건 결합 있으나 순위 규칙 제공 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/9 | output/260910/260910_01_info_composite_a_questions_review.md:L217 | T2 성격(정형 변형·순차 추적) | i<j 조합→차이 필터→개수; 정형 열거 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/10 | output/260910/260910_01_info_composite_a_questions_review.md:L241 | T3 후보 성격(조건·상태 결합) | 삭제 후 길이·현재 위치 재검사; 인덱스 갱신 분기와 실제 자료 상태 결합 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/11 | output/260910/260910_01_info_composite_a_questions_review.md:L268 | T2 성격(정형 변형·순차 추적) | 이전 행의 기준으로 판정 후 기준 변경; 상태표로 완결 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/12 | output/260910/260910_01_info_composite_a_questions_review.md:L293 | T2 성격(정형 변형·순차 추적) | old 보존→a 갱신→b 갱신; 순서 함정이나 정형 대입 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/13 | output/260910/260910_01_info_composite_a_questions_review.md:L319 | T2 성격(정형 변형·순차 추적) | 양끝 비교→슬라이스→다시 함수→합; 원본 길이 보존 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/14 | output/260910/260910_01_info_composite_a_questions_review.md:L343 | T2 성격(정형 변형·순차 추적) | 이동 누적→나머지→문자 선택; 동일 규칙 반복 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/15 | output/260910/260910_01_info_composite_a_questions_review.md:L367 | T2 성격(정형 변형·순차 추적) | 함수 순서에 따른 입력·분기 차이; 두 합성 직접 계산 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/16 | output/260910/260910_01_info_composite_a_questions_review.md:L391 | T2 성격(정형 변형·순차 추적) | 행별 대각 원소→첫 열 갱신; 행간 의존 없음 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/17 | output/260910/260910_01_info_composite_a_questions_review.md:L413 | T2 성격(정형 변형·순차 추적) | 이전·현재 값→2차원 주소→횟수; 직접 인덱싱 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/18 | output/260910/260910_01_info_composite_a_questions_review.md:L437 | T2 성격(정형 변형·순차 추적) | 몫 축소와 나머지 합→반환값 재호출; 제공된 자릿수 합 규칙 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/19 | output/260910/260910_01_info_composite_a_questions_review.md:L462 | T3 후보 성격(조건·상태 결합) | 양끝 교환→구간 축소→겹친 다음 구간; 갱신 자료 재사용 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/20 | output/260910/260910_01_info_composite_a_questions_review.md:L490 | T2 성격(정형 변형·순차 추적) | 같은 열 두 값 비교→차이 수집; 정형 필터 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/21 | output/260910/260910_01_info_composite_a_questions_review.md:L513 | T3 후보 성격(조건·상태 결합) | need 변화·중복 건너뜀·조기반환; 종료 경계 결합 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/22 | output/260910/260910_01_info_composite_a_questions_review.md:L539 | T3 후보 성격(조건·상태 결합) | 끝 원소 비교→삭제/추가→다음 비교대상 변경; 상태 의존 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/23 | output/260910/260910_01_info_composite_a_questions_review.md:L563 | T2 성격(정형 변형·순차 추적) | 누적 합과 최초 통과 회차 분리; 주어진 first==0 조건 추적 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/24 | output/260910/260910_01_info_composite_a_questions_review.md:L587 | T2 성격(정형 변형·순차 추적) | 길이 경계→양끝 비교→입력 축소; 직접 반복 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| A/25 | output/260910/260910_01_info_composite_a_questions_review.md:L611 | T2 성격(정형 변형·순차 추적) | 행 점수→최대 선택; 세 점수 모두6이라 최초 동점 보존으로 축약 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/1 | output/260910/260910_02_info_composite_b_questions_review.md:L24 | T3 후보 성격(조건·상태 결합) | 역방향 차분→정방향 누적 복원; 순서 민감하나 두 절차 모두 제공 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/2 | output/260910/260910_02_info_composite_b_questions_review.md:L48 | T2 성격(정형 변형·순차 추적) | 인덱스+이동량→나머지 주소→횟수; 정형 대입 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/3 | output/260910/260910_02_info_composite_b_questions_review.md:L71 | T2 성격(정형 변형·순차 추적) | 첫 조건 충족 return와 기본값0; 짧은 조기반환 추적 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/4 | output/260910/260910_02_info_composite_b_questions_review.md:L94 | T2 성격(정형 변형·순차 추적) | 열별 합→최대; 독립 열 누적 후 집계 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/5 | output/260910/260910_02_info_composite_b_questions_review.md:L117 | T2 성격(정형 변형·순차 추적) | 문자A 위치와 홀수 위치가 완전히 같음; 두 조건의 변별력 없음 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/6 | output/260910/260910_02_info_composite_b_questions_review.md:L140 | T2 성격(정형 변형·순차 추적) | 양끝 차이→포인터 동시 이동→종료; 두 회차 직접 계산 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/7 | output/260910/260910_02_info_composite_b_questions_review.md:L166 | T3 후보 성격(조건·상태 결합) | 전역 잔량→조기반환→승인목록; 실패가 이후 상태에 영향 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/8 | output/260910/260910_02_info_composite_b_questions_review.md:L195 | T3 후보 성격(조건·상태 결합) | 두 칸 슬라이스 재귀→복귀시 append; 호출·복귀 순서 추적 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/9 | output/260910/260910_02_info_composite_b_questions_review.md:L220 | T3 후보 성격(조건·상태 결합) | 패턴 상태p→문자 선택→다음 목표; 단락평가가 범위 초과 방지 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/10 | output/260910/260910_02_info_composite_b_questions_review.md:L246 | T2 성격(정형 변형·순차 추적) | <= 동점 탐색→종료 인덱스→삽입; 주어진 upper-bound 규칙 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/11 | output/260910/260910_02_info_composite_b_questions_review.md:L270 | T3 후보 성격(조건·상태 결합) | 현재 부하 비교→작업대 선택→다음 부하 변경; 피드백 분기 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/12 | output/260910/260910_02_info_composite_b_questions_review.md:L297 | T3 후보 성격(조건·상태 결합) | done 초기화→가용 칸 탐색→소모→다음 요청; 두 상태 결합 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/13 | output/260910/260910_02_info_composite_b_questions_review.md:L324 | T2 성격(정형 변형·순차 추적) | 구간합 모두8→엄격한 >로 최초 위치 보존; 최대 갱신 분기 미실행 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/14 | output/260910/260910_02_info_composite_b_questions_review.md:L350 | T2 성격(정형 변형·순차 추적) | 두 슬라이스 길이 비교→연결 순서; 짧은 두 함수 호출 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/15 | output/260910/260910_02_info_composite_b_questions_review.md:L374 | T3 후보 성격(조건·상태 결합) | 중간 위치→좌우 구간 축소→성공/실패; 알고리즘 선택은 이미 제공 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/16 | output/260910/260910_02_info_composite_b_questions_review.md:L405 | T3 후보 성격(조건·상태 결합) | 하위 집계→상위 누적; 점화식·순회 순서가 제공돼 설계/최적성 증명 불필요 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/17 | output/260910/260910_02_info_composite_b_questions_review.md:L427 | T2 성격(정형 변형·순차 추적) | 반전/유지→현재 상태로 기록; 주어진 두 if의 순서 추적 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/18 | output/260910/260910_02_info_composite_b_questions_review.md:L453 | T2 성격(정형 변형·순차 추적) | 현재 원소가 이동폭→다음 위치→종료; 정형 상태 추적 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/19 | output/260910/260910_02_info_composite_b_questions_review.md:L477 | T3 후보 성격(조건·상태 결합) | 부분 위치 반환→복귀시 +1 또는 -1 보존; 재귀 경계 결합 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/20 | output/260910/260910_02_info_composite_b_questions_review.md:L505 | T2 성격(정형 변형·순차 추적) | 행 내부 짝수 수→행 통과 여부; 집계 단위 구분 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/21 | output/260910/260910_02_info_composite_b_questions_review.md:L532 | T2 성격(정형 변형·순차 추적) | 자료/합계 칸 분리→검증→수정 위치 기록; 식과 수정법 제공 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/22 | output/260910/260910_02_info_composite_b_questions_review.md:L558 | T2 성격(정형 변형·순차 추적) | 최대값 선택→이동→첫 중복 삭제 반복; 방법 발상 불필요 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/23 | output/260910/260910_02_info_composite_b_questions_review.md:L582 | T2 성격(정형 변형·순차 추적) | 현재 연속 길이 초기화와 역대 최대 유지; 두 누적 변수 구분 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/24 | output/260910/260910_02_info_composite_b_questions_review.md:L609 | T3 후보 성격(조건·상태 결합) | 두 목록 비교→선택한 인덱스만 이동→한쪽 소진시 종료; 동점과 잔여 구분 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |
| B/25 | output/260910/260910_02_info_composite_b_questions_review.md:L639 | T3 후보 성격(조건·상태 결합) | 행 주소→방문 기록→합→다음 주소; 재방문 종료 조건 제공 | 일치(동결 WIP) | BLOCKED: 현행 자 재측정 |

## 배포 게이트
| gate | 결과 | 근거·남은 종료 조건 |
|---|---|---|
| G0 승인 | ▲ blocked | 검수 수행 요청은 감사 PASS 근거가 아니다. 품질 종료 조건 미충족. |
| G1 전수 | 부분 확인 / ▲ blocked | 원본 N50·동결 풀이 기록 M50. 모델 인증·최종 품질 검증은 미확인. |
| G2 신규성 | ▲ blocked | 원본·기존 세트 비교 자료는 읽었으나 50개 최근접 원본과 N/V 종합 판정 미완료. A2/B1, A25/B13 교차 노출 후보를 재측정. 수치변형 확정 아님. |
| G3 동반7면 | 부분 확인 / ▲ blocked | 기존 답·해설 대조와 이번 배점 수량 확인. 종전 A20/B22 IN-12, A23/B23 IN-26 태그 불일치 후보는 변경 카탈로그로 재측정 전 확정하지 않음. |
| G4 내용 | MD 일치 / 인쇄 미검수 | 문제/답 각25의 전체 본문 포함 검사 통과. 렌더링·잘림 검수 미실행. |
| G5 위치 | 검토용 상태 일치 | `_review.md`와 검토필요 표기 일치. 배포본 생성 안 함. |
| G6 등록 | ▲ blocked | 두 set_id:null. index에는 초안~revision4의 이력5묶음250행; 현행 revision4만 분리하면 고유50행. 이력 중복을 현행250문항으로 세지 않음. |
| G7 재생성 | 미검수 | 작성 코드·selfcheck·revision 실행 금지 유지. 배포 시 재생성/manifest가 상태를 되돌리지 않는지 별도 확인. |
| G8 잔여 | 배포 중단 | 보고서에 결함을 숨기고 학생 배포하지 않음. 제품 경고 삭제·상태 승격 없음. |

## 조치 목록
- [ ] 조정/판정 담당: 현행 카탈로그 two-key·재동결 이력과 적용 범위 확인. 구판 복원·자의 수정으로 통과시키지 않는다.
- [ ] 확인된 깨끗한 Astra 감사 컨텍스트: A/1~25, B/1~25의 최근접 원본·등록 축·같은 유형 함정의 실제 오독값·신규성·범위·태그를 전수 재측정. 답을 이미 읽은 현재 컨텍스트를 새 맹목 컨텍스트라 하지 않는다.
- [ ] 작성 컨텍스트: 최고 구간에 필수 사고력을 추가하고 티어 사다리를 명시. 변경 문항·답·해설은 다시 독립 검증. 감사자가 직접 고치고 통과시키지 않는다.
- [ ] 조정 담당: DATA_STANDARD에 따라 정식 ID 충돌 해소. 범위/학생 맞춤 표기는 사실대로 유지. 학생 기록 부재를 일반 practice의 자동 결함으로 과장하지 않되 맞춤 효과는 주장하지 않는다.
- [ ] 배포 담당: 위 게이트 해소 후 인쇄·잔여 경고 확인 및 정본/문제지/답지/인덱스/감사 이력 동시 갱신. 보고서 저장만으로 배포하지 않는다.

## 실제 읽기와 비교 분모의 한계
기존 구간 읽기·해시 원장은 WIP이다: 문제50, 답·해설50, 구 정보문제26, 기출/퀴즈/개념 전사3종, 교과서33이미지, 카탈로그·난이도·TYPE_MASTER·교육과정·답지 양식. 당시 inventory는 정보 MD9개(기존26제3복사본 + A/B6복사본), 고유 기존 세트1개. 이는 이전 구간의 실측이지 현재 전역 inventory 주장이 아니다. 신규성 최종 판정 전 재열거해야 한다.
이번 추가 열람: 요청 프롬프트, Astra 정책, 품질감사/배포 역할 정의, WIP, 대상6개 MD 전체(내용 비교), 현재 카탈로그 해시, 난이도/TYPE_MASTER 해시, REV_GUIDE 일부, CLAUDE/DATA_STANDARD 줄수, 기존 배포 사전점검13, index 대상행·섹션, 260911 V1 판정문 앞부분. 작성 코드·selfcheck·revision·novelty 결과는 읽거나 실행하지 않았다. 사전점검13의 과거 실행값은 이번 독립 검산 근거로 사용하지 않았다.
작성 대화와 분리해 시작한 맹목 기록을 보존하되 호스트 차원의 모델/격리 증명은 미노출. 답 개봉 이후는 비맹목 대조다.

## 명령·실측
PowerShell UTF-8 입출력 후 `python -`: hashlib.sha256, 정규식 제목 ID 추출, Counter/차집합, 본문 전체 문자열 포함, index 현행 revision4 구간 분리. 기존 게이트 수정 없음. 보조검사를 품질 자 대신 사용하지 않음.
처음 내용검사는 셸 인코딩 문제 ValueError로 exit1, UTF-8 설정 후 exit0. 보고서 최초 작성 시도는 index 이력250행을50행으로 단정한 assertion에서 exit1로 중단되어 파일 미생성. 이후 섹션을 확인해 현행50행과 역사250행을 구분했다. 아래 신선한 구조 검사의 warnings0은 **배포 경고0을 뜻하지 않는다**. 제품 코드 미변경; lint/build/전체 assurance gate는 미실행이며 통과 주장 없음.

```json
{
  "coverage": {
    "expected": [
      "A/1",
      "A/2",
      "A/3",
      "A/4",
      "A/5",
      "A/6",
      "A/7",
      "A/8",
      "A/9",
      "A/10",
      "A/11",
      "A/12",
      "A/13",
      "A/14",
      "A/15",
      "A/16",
      "A/17",
      "A/18",
      "A/19",
      "A/20",
      "A/21",
      "A/22",
      "A/23",
      "A/24",
      "A/25",
      "B/1",
      "B/2",
      "B/3",
      "B/4",
      "B/5",
      "B/6",
      "B/7",
      "B/8",
      "B/9",
      "B/10",
      "B/11",
      "B/12",
      "B/13",
      "B/14",
      "B/15",
      "B/16",
      "B/17",
      "B/18",
      "B/19",
      "B/20",
      "B/21",
      "B/22",
      "B/23",
      "B/24",
      "B/25"
    ],
    "observed": [
      "A/1",
      "A/2",
      "A/3",
      "A/4",
      "A/5",
      "A/6",
      "A/7",
      "A/8",
      "A/9",
      "A/10",
      "A/11",
      "A/12",
      "A/13",
      "A/14",
      "A/15",
      "A/16",
      "A/17",
      "A/18",
      "A/19",
      "A/20",
      "A/21",
      "A/22",
      "A/23",
      "A/24",
      "A/25",
      "B/1",
      "B/2",
      "B/3",
      "B/4",
      "B/5",
      "B/6",
      "B/7",
      "B/8",
      "B/9",
      "B/10",
      "B/11",
      "B/12",
      "B/13",
      "B/14",
      "B/15",
      "B/16",
      "B/17",
      "B/18",
      "B/19",
      "B/20",
      "B/21",
      "B/22",
      "B/23",
      "B/24",
      "B/25"
    ],
    "duplicate": [],
    "missing": [],
    "extra": []
  },
  "content_checks": [
    {
      "set": "A",
      "question_body_equal": true,
      "answer_body_equal": true,
      "question_count": 25,
      "answer_count": 25,
      "4point_items": 25,
      "rubrics": 25,
      "total": 100
    },
    {
      "set": "B",
      "question_body_equal": true,
      "answer_body_equal": true,
      "question_count": 25,
      "answer_count": 25,
      "4point_items": 25,
      "rubrics": 25,
      "total": 100
    }
  ],
  "files": [
    {
      "path": "output/260910/260910_01_info_composite_a_questions_review.md",
      "bytes": 19401,
      "sha256": "2017bcaea3eb7c49c65fcbc187596df1a79a5bfb9f2e7664ec2cd01c6c47a88d"
    },
    {
      "path": "output/260910/260910_01_info_composite_a_answers_review.md",
      "bytes": 31372,
      "sha256": "70fa9e18eeae4c313d44f742e94ee9a946b195c95b9e25272c015a138463f109"
    },
    {
      "path": "output/260910/260910_01_info_composite_a_review.md",
      "bytes": 49224,
      "sha256": "521c625c7971fb9f494a8763246303f497b6566aa1eaa40cdef370b5fa37dec7"
    },
    {
      "path": "output/260910/260910_02_info_composite_b_questions_review.md",
      "bytes": 20207,
      "sha256": "a4dea5692f3c1a116fb2771ea628f0afaeef01602864de2040e05bd9bb13ccd6"
    },
    {
      "path": "output/260910/260910_02_info_composite_b_answers_review.md",
      "bytes": 33805,
      "sha256": "dfa2387e3d5ffc9b124a3aa3cdd8bf218f6810bc822415fc610c3f0cae85a6bf"
    },
    {
      "path": "output/260910/260910_02_info_composite_b_review.md",
      "bytes": 52463,
      "sha256": "2f7bb0130508272508429796cc38b343086a9be9da1f4e31d3918efb04c55602"
    }
  ],
  "wip_sha256": "46b69ed547198413da620f629c4a39c3a134b074b1505cc8d15a0837035964d8",
  "blind_prefix_bytes": 26604,
  "blind_prefix_sha256": "59c8020eeafcedfde9529b75c6feef4f01ca123e2991b7785a3309abad2f4e36",
  "index_current_ids": [
    "A/1",
    "A/2",
    "A/3",
    "A/4",
    "A/5",
    "A/6",
    "A/7",
    "A/8",
    "A/9",
    "A/10",
    "A/11",
    "A/12",
    "A/13",
    "A/14",
    "A/15",
    "A/16",
    "A/17",
    "A/18",
    "A/19",
    "A/20",
    "A/21",
    "A/22",
    "A/23",
    "A/24",
    "A/25",
    "B/1",
    "B/2",
    "B/3",
    "B/4",
    "B/5",
    "B/6",
    "B/7",
    "B/8",
    "B/9",
    "B/10",
    "B/11",
    "B/12",
    "B/13",
    "B/14",
    "B/15",
    "B/16",
    "B/17",
    "B/18",
    "B/19",
    "B/20",
    "B/21",
    "B/22",
    "B/23",
    "B/24",
    "B/25"
  ],
  "structural_warnings": 0,
  "exit": 0,
  "release": "BLOCKED",
  "additional_hashes": [
    {
      "path": "analysis/catalog/info.md",
      "bytes": 63937,
      "sha256": "171b7d8a671f39a9fc6826feec7312059e97a6dc5dae0c02361cfe22a8080ca9"
    },
    {
      "path": "analysis/catalog/DIFFICULTY_RUBRIC.md",
      "bytes": 20921,
      "sha256": "07dab5d38c8da48a22ca01d2f4c2b75d71fdd421a6da5ad3fcdd1a3b81b1ad99"
    },
    {
      "path": "analysis/catalog/TYPE_MASTER.md",
      "bytes": 19399,
      "sha256": "ff45bdf8f6f46689ccd68a5caa645e5c7be54bca456684f0483bee82db24bea9"
    },
    {
      "path": "output/_index.md",
      "bytes": 174713,
      "sha256": "6d550bd60e16a9552c0085a40935c105217a3ad4c0fe24397329eec1ef04474d"
    }
  ]
}
```

Pipeline: 작성 → 맹목 풀이 기록 → **품질감사 ▲ blocked** → 수정·재검증 → 배포
Stage: Codex/OMX = 모델·깊이 호스트 미확인 — 기존 답 일치50/50·교과서33/33; 카탈로그 변경·품질 미완료로 배포 보류
Team: mode=solo; lead=메인 루프 | 모델 미확인 | 감사 | blocked; lanes=없음; independence=작성 대화와 분리해 시작한 기록·답 개봉 후 비맹목·호스트 격리 미확인; planned/unavailable/failed lanes=없음
Next: 현행 자 재동결 이력 확인 후50문항 N/V 재측정. 모델·품질·최고 사고력·ID·인쇄 게이트 충족 전 배포 승격 금지.


## 재개 검수 추가 기록 — 2026-09-11: 변경 이력 확인 및 기준 게이트 실패

실행자 Codex/OMX, author: 메인 루프, grade: proposal. 모델/깊이 호스트 증빙은 여전히 미노출. 기존 보고서 본문과 맹목 풀이 동결은 변경하지 않았다.

### 변경 이력 확인 결과
- 보고서의 제품 6개 및 additional_hashes 4개를 SHA256 전수 재대조: 10/10 일치. 기존 보고서와 WIP 자체 해시도 체크포인트와 일치. 이번 조회에서 추가 입력 변경은 발견하지 않았다.
- `analysis/REV_LOG.md:178`은 BF1·2·3·5·6① 반영, `:179`는 BF4·BF6②의 카탈로그 반영을 기록한다. 후자는 63,937 bytes, SHA256 접두 `171B7D8A671F39A9`로 현재 `analysis/catalog/info.md`와 일치한다. 따라서 **카탈로그 변경 이력이 없다는 가정으로 차단하지 않는다**. 다만 원장 자기 신고를 이 실행의 모델 인증이나 사용자 승인 원문으로 바꾸어 표시하지 않는다.
- `analysis/REV_GUIDE.md:308–320`의 정본 two-key 목록과 카탈로그 변경 추적을 구별한다. 목록을 임의로 확대하거나 수정하지 않았다.
- `output/260911/rev/260911_01_info_v1_criterion_ruling.md`의 대상은 **SET-260908-info-26**이다. 해당 문서의 수치·판정은 **A/B50 승인 또는 V1 전수 결과가 아니다**. V1의 현행 3치 절차는 `.claude/agents/item-quality-auditor.md:81–98`에 반영되어 있으나 A/B50은 별도로 재측정해야 한다.
- 해당 판정 §4는 정보 T4 레시피와 서답형 Tier 밴드 문제를 미해소로 남긴다. 이는 사용자 요구인 **기존 최고 수준 + 필수 추가 사고력**을 완화할 근거가 아니다. 기존 잠정 T2/T3 의견도 정식 Tier 인증이 아니다.

### 새로 실행한 기준 게이트 — 모두 통과 아님
| 명령 | 기대 | 실제 | 판정 |
|---|---|---|---|
| `python tools/measure_score_bands.py` | exit 0, 경고 0 | exit 1, `[WARN]` 40행, `[FAIL] GATE 3 mismatches=1 -- EX-social-20261M` | FAIL |
| `python tools/regen_rubric_values.py` | exit 0, `[GATE 0 PASS] undetected=0`, `stale=0 lines=0 residual=0` | exit 1, `계층 4행 없음` 및 F/M 2024–2026 여섯 계층 출력; 기대 문자열 없음 | FAIL |
| `python tools/check_assurance_contract.py` | exit 0, failures 0 | exit 1, `assurance-contract: 10 failure(s)` | FAIL |

규정 검사 10건은 타 WIP 메타데이터 7건과 ruler gate 3건이다. WIP 대상: `260910_astra_fallback_policy_proposal.md` 2건(status pending/NEXT 없음), `260910_info_astra_pilot_questions.md` 2건(status/NEXT 없음), `mainloop_260907_info_onboarding.md` 1건(status active), `RESUME.md` 2건(status/NEXT 없음). ruler gate는 regen exit 1, 검출력 증명 문자열 부재, stale 상태 확인 불가 3건이다. 검사 출력의 `[WARN]` 0은 실패 0을 뜻하지 않는다. 실행 래퍼의 exit 0도 내부 명령 exit 1을 덮지 않는다.

이 결과만으로 `EX-social-20261M`의 원인이 전사인지 파서인지 단정하지 않으며, A/B50의 정답 오류로도 단정하지 않는다. 기준 도구·타인 WIP·정본·인덱스는 이번 감사 write surface 밖이므로 고치지 않았다. 전체 lint/build 또는 인쇄 검수 통과도 주장하지 않는다.

### 현재 결정 및 정확한 NEXT
**배포 승인 ▲ blocked 유지.** 카탈로그 변경 추적 조회는 완료했으나 기준 게이트, A/B50 최근접 원본·N/V 전수표, 최고 사고력 요건, 정식 ID/인쇄 및 인증된 독립 단계가 남아 있다.
NEXT: 기준 소유 단계에서 위 세 명령의 실패를 해소하고 같은 명령으로 재확인한다. 자 변경이 필요하면 사용자 승인+감사권한자 판정 및 재동결을 선행한다. 이 감사는 기준을 고치거나 성공 조건을 축소하지 않는다. 그 뒤 고정된 현행 입력으로 A/1–A/5 N/V 파일럿부터 전수 재측정한다. 기존 답 50/50 동결은 보존하고 다시 맹목이라고 표시하지 않는다.


## ?? ?? ? 2026-09-11: ?? ?? ??? ???? ???

author: ?? ?? (Codex/OMX); grade: proposal; ??/?? ??? ???. ?? ?? ? ??? ?? ???? ??? Astra ?? ?????? ???. ?? ??, ?? ??, ? WIP ??, ? ?? ??? ???? ???.

### ??? ??? ??
1. `tools/regen_rubric_values.py:82?85`? `len(strata) != 4`?? ????. ?? ?? ??? F/M ? 2024/2025/2026 = 6???? ??? ?? ?? ????. ?? 4?6 ??? ???? ???. ???? ?? ??? ???? ?????????????? ???? ??? two-key ?? ????.
2. `corpus/EX-social-20261M/transcript.md:9?14`? scope: partial? ?? ?? 15/27? ????. `output/260903/rev/260903_06_arbiter_ruling_cycle1_f.md` F2-2? G2-a ??? FAIL? ???? ??? ????? ???. ??? ?? 24/15 ???? ? ?? ??? ????? ?? ??? ???? ? ??. ? ?? ??? Cycle-1 ?? ???? A/B50 ?? ?? ? ??? PASS? ???. ???? ??? ???? ?? ??? ???? ???.
3. ?? ?? 10? ? 7?? ?? ? WIP? status/NEXT ???? ??? 3?? ??? ??? ?? ??? ???. ? WIP? ?? ??? ??? ??? ???.
4. ?? ??? ???? ?? ????? ???? ???. ?? 26?? ??? ???? A/B50? ???? ???. ?? ??? ??? ?? ?? ?? + ?? ?? ???? ????.

### ????? ?? (???, ???? ??)
- [ ] ?? ???/?????: ?? 6?? ???? ???? ??? ??? ?? ?? ??? ????, ??? ?? ?? ??? ??? ????.
- [ ] ?? ???/?????: F2-2? ?? ?? ??? ?? ??/? ???? ?? ???? ????? ??? ?? ????. ?? FAIL???? ???? A/B ???? ???? ???.
- [ ] ? WIP ???: ??? ??? ? WIP? ?? ??? NEXT? ??? ?? ??? ????. ?? ??? ?? ????.

?? ???? ??? ??/??/??, ?? ??, ?? ????? ????? ? ???, ??? ? ??, ??? ??? ???? ??. ? ???? ? ??? ???? ? ??? ???? ????? ?? ?? ??? ????.

### ??? ?? ?? ? ?? ??
```json
{
  "input_checks": [
    {
      "path": "output/260910/260910_01_info_composite_a_questions_review.md",
      "match": true,
      "sha256": "2017bcaea3eb7c49c65fcbc187596df1a79a5bfb9f2e7664ec2cd01c6c47a88d",
      "bytes": 19401
    },
    {
      "path": "output/260910/260910_01_info_composite_a_answers_review.md",
      "match": true,
      "sha256": "70fa9e18eeae4c313d44f742e94ee9a946b195c95b9e25272c015a138463f109",
      "bytes": 31372
    },
    {
      "path": "output/260910/260910_01_info_composite_a_review.md",
      "match": true,
      "sha256": "521c625c7971fb9f494a8763246303f497b6566aa1eaa40cdef370b5fa37dec7",
      "bytes": 49224
    },
    {
      "path": "output/260910/260910_02_info_composite_b_questions_review.md",
      "match": true,
      "sha256": "a4dea5692f3c1a116fb2771ea628f0afaeef01602864de2040e05bd9bb13ccd6",
      "bytes": 20207
    },
    {
      "path": "output/260910/260910_02_info_composite_b_answers_review.md",
      "match": true,
      "sha256": "dfa2387e3d5ffc9b124a3aa3cdd8bf218f6810bc822415fc610c3f0cae85a6bf",
      "bytes": 33805
    },
    {
      "path": "output/260910/260910_02_info_composite_b_review.md",
      "match": true,
      "sha256": "2f7bb0130508272508429796cc38b343086a9be9da1f4e31d3918efb04c55602",
      "bytes": 52463
    },
    {
      "path": "analysis/catalog/info.md",
      "match": false,
      "sha256": "48db904b1e4c8cfc5256e93ecd036f4ea19466720adbc55ee89e4c40d0dc1c64",
      "bytes": 64517
    },
    {
      "path": "analysis/catalog/DIFFICULTY_RUBRIC.md",
      "match": true,
      "sha256": "07dab5d38c8da48a22ca01d2f4c2b75d71fdd421a6da5ad3fcdd1a3b81b1ad99",
      "bytes": 20921
    },
    {
      "path": "analysis/catalog/TYPE_MASTER.md",
      "match": true,
      "sha256": "ff45bdf8f6f46689ccd68a5caa645e5c7be54bca456684f0483bee82db24bea9",
      "bytes": 19399
    },
    {
      "path": "output/_index.md",
      "match": false,
      "sha256": "527b917b9ef897923593a7bc25d5cabfc38ef93363d86ae654879bf312076151",
      "bytes": 175118
    }
  ],
  "runs": [
    {
      "command": "python tools/measure_score_bands.py",
      "exit": 1,
      "warn_lines": 40,
      "output": "=== GATE 0 fixture: planted parser defects ===\r\nplanted=9 undetected=0\r\nplanted-state=6 undetected=0\r\n[GATE 0 PASS] undetected=0\r\n=== GATE 1 truth: reproduce tier-3 confirmed values ===\r\nEX-english-20252M    [body       ] got n=27  sum=70.0    want n=27  sum=70.0    OK\r\nEX-history-20252M    [body       ] got n=20  sum=40.0    want n=20  sum=40.0    OK\r\nEX-info-20252F       [body       ] got n=18  sum=70.0    want n=18  sum=70.0    OK\r\nEX-korean-20252M     [body       ] got n=29  sum=60.0    want n=29  sum=60.0    OK\r\nEX-math1-20242M      [body+math0 ] got n=0   sum=0.0     want n=0   sum=0.0     OK\r\nEX-math2-20252M      [body+math0 ] got n=0   sum=0.0     want n=0   sum=0.0     OK\r\nEX-science-20242F    [body       ] got n=24  sum=80.0    want n=24  sum=80.0    OK\r\nEX-science-20242M    [body       ] got n=24  sum=60.0    want n=24  sum=60.0    OK\r\nEX-science-20252M    [index      ] got n=23  sum=60.0    want n=23  sum=60.0    OK\r\nEX-social-20252M     [body       ] got n=20  sum=60.0    want n=20  sum=60.0    OK\r\nchecked=10 undetected=0 flagged=0 coverage=10/60\r\n[GATE 1 PASS] undetected=0\r\n\r\n=== GATE 2 dup: identical selective sequences ===\r\n[WARN] identical selective sequence (n=18): EX-info-20252F == EX-info-20252M\r\nduplicates=1 (warning only -- not excluded, see BF-K1-7a)\r\nGATE 2 false-positive rate to date: 1/1 -- EX-info-20252M vs EX-info-20252F are different exams that reuse one score-allocation table (ruling 260831_04 U3-a). Treat every firing as a candidate, never as a verdict.\r\n\r\n=== GATE 3 declared: printed declaration vs extraction ===\r\n[WARN] EX-social-20261M     declared n=24  extracted n=15 \r\nmismatches=1\r\n--- GATE 3b sum-axis coverage (BF3) ---\r\n[WARN] EX-english-20241F    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-english-20241M    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-english-20242F    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-english-20242M    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-english-20251F    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-english-20251M    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-english-20252F    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-english-20252M    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-history-20241F    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-history-20241M    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-history-20251F    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-history-20251M    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-history-20252F    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-history-20252M    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-history-20261F    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-history-20261M    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-korean-20241F     self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-korean-20241M     self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-korean-20242F     self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-korean-20242M     self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-korean-20251F     self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-korean-20251M     self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-korean-20252F     self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-korean-20252M     self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-science-20241F    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-science-20241M    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-science-20251F    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-science-20251M    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-science-20252F    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-science-20252M    self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-social-20241F     self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-social-20241M     self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-social-20251F     self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-social-20251M     self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-social-20252F     self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-social-20252M     self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-social-20261F     self-enumerated selective total not found -- sum axis UNCOVERED\r\n[WARN] EX-social-20261M     self-enumerated selective total not found -- sum axis UNCOVERED\r\nsum-axis coverage=12/50 uncovered=38 mismatches=0\r\n\r\nexcluded from aggregate: EX-social-20261M\r\n\r\n=== selective-score distribution ===\r\nunit                 T  mode      n  decl      sum       range      band  4.0+\r\nEX-english-20241F    F  body     24    24     70.0     2.5~3.5   10/24       0\r\nEX-english-20241M    M  body     26    26     70.0     2.3~3.4    6/26       0\r\nEX-english-20242F    F  body     24    24     70.0     2.5~3.5   11/24       0\r\nEX-english-20242M    M  body     24    24     70.0     2.5~3.5   10/24       0\r\nEX-english-20251F    F  body     26    26     70.0     2.1~3.6    8/26       0\r\nEX-english-20251M    M  body     23    23     70.0     2.2~3.6   16/23       0\r\nEX-english-20252F    F  body     28    28     70.0     2.1~2.8    0/28       0\r\nEX-english-20252M    M  body     27    27     70.0     2.2~3.3    4/27       0\r\nEX-english-20261F    F  body     23    23     80.0     3.1~4.2   23/23       1\r\nEX-english-20261M    M  body     22    22     60.0     2.1~3.7    6/22       0\r\nEX-history-20241F    F  body     21    21     80.0     3.4~4.2   21/21       6\r\nEX-history-20241M    M  body     25    25     60.0     2.2~2.8    0/25       0\r\nEX-history-20242F    F  body     21    21     80.0     3.5~4.2   21/21       3\r\nEX-history-20242M    M  body     24    24     60.0     2.3~2.7    0/24       0\r\nEX-history-20251F    F  body     24    24     80.0     3.1~3.5   24/24       0\r\nEX-history-20251M    M  body     25    25     60.0     2.2~2.6    0/25       0\r\nEX-history-20252F    F  body     23    23     80.0     3.2~3.7   23/23       0\r\nEX-history-20252M    M  body     20    20     40.0     1.8~2.2    0/20       0\r\nEX-history-20261F    F  body     24    24     80.0     3.0~3.6   24/24       0\r\nEX-history-20261M    M  body     25    25     60.0     2.2~2.5    0/25       0\r\nEX-info-20252F       F  body     18    18     70.0     3.2~4.4   15/18      10\r\nEX-info-20252M       M  body     18    18     70.0     3.2~4.4   15/18      10\r\nEX-korean-20241F     F  body     24    24     80.0     3.0~3.7   24/24       0\r\nEX-korean-20241M     M  body     24    24     60.0     2.2~2.8    0/24       0\r\nEX-korean-20242F     F  body     24    24     80.0     3.0~3.6   24/24       0\r\nEX-korean-20242M     M  body     24    24     60.0     2.2~2.8    0/24       0\r\nEX-korean-20251F     F  body     26    26     80.0     2.0~4.0   18/26       1\r\nEX-korean-20251M     M  body     24    24     60.0     1.7~3.3    7/24       0\r\nEX-korean-20252F     F  body     25    25     80.0     2.3~4.0   18/25       1\r\nEX-korean-20252M     M  body     29    29     60.0     1.2~2.8    0/29       0\r\nEX-math1-20241F      F  body+math0    0     0        - no selective         -     -\r\nEX-math1-20241M      M  body+math0    0     0        - no selective         -     -\r\nEX-math1-20242F      F  body+math0    0     0        - no selective         -     -\r\nEX-math1-20242M      M  body+math0    0     0        - no selective         -     -\r\nEX-math1-20251F      F  body+math0    0     0        - no selective         -     -\r\nEX-math1-20251M      M  body+math0    0     0        - no selective         -     -\r\nEX-math1-20261F      F  body+math0    0     0        - no selective         -     -\r\nEX-math1-20261M      M  body+math0    0     0        - no selective         -     -\r\nEX-math2-20252F      F  body+math0    0     0        - no selective         -     -\r\nEX-math2-20252M      M  body+math0    0     0        - no selective         -     -\r\nEX-science-20241F    F  body     24    24     80.0     3.0~3.6   24/24       0\r\nEX-science-20241M    M  body     24    24     60.0     2.2~2.8    0/24       0\r\nEX-science-20242F    F  body     24    24     80.0     3.0~3.6   24/24       0\r\nEX-science-20242M    M  body     24    24     60.0     2.2~2.8    0/24       0\r\nEX-science-20251F    F  body     24    24     80.0     3.0~3.9   24/24       0\r\nEX-science-20251M    M  body     24    24     60.0     2.3~2.7    0/24       0\r\nEX-science-20252F    F  body     24    24     80.0     3.0~3.6   24/24       0\r\nEX-science-20252M    M  index    23    23     60.0     2.2~3.2    2/23       0\r\nEX-science-20261F    F  body     24    24     90.0     3.4~4.0   24/24       7\r\nEX-science-20261M    M  body     24    24     90.0     3.4~4.0   24/24       7\r\nEX-social-20241F     F  body     20    20     80.0     3.3~4.4   13/20      12\r\nEX-social-20241M     M  body     24    24     60.0     2.3~2.8    0/24       0\r\nEX-social-20242F     F  body     20    20     80.0     3.6~4.4   17/20      12\r\nEX-social-20242M     M  body     24    24     60.0     2.0~2.9    0/24       0\r\nEX-social-20251F     F  body     20    20     80.0     3.5~4.5   16/20      14\r\nEX-social-20251M     M  body     20    20     60.0     2.6~3.3   12/20       0\r\nEX-social-20252F     F  body     22    22     80.0     3.1~4.2   22/22       6\r\nEX-social-20252M     M  body     20    20     60.0     2.7~3.3   13/20       0\r\nEX-social-20261F     F  body     24    24     90.0     3.5~4.1   24/24       6\r\nEX-social-20261M     M  body     15    24     55.3     3.5~4.0   15/15       2 EXCL\r\n\r\n=== axis test: midterm(M) vs final(F) ===\r\nT  units      n     band         pct   4.0+ sel_total_avg\r\nM     24    567      115       20.3%     17        62.5\r\nF     25    581      476       81.9%     79        78.8\r\n\r\nmean unit price:  M=2.65  F=3.39\r\n\r\n=== signed relative band  r in [0.80, 1.20] ===\r\nALL   n=1148  fit=1101 = 95.9%  residual=47\r\n\r\n--- per stratum ---\r\nF-2024   n=226  fit=226   100.0%\r\nF-2025   n=260  fit=245    94.2%\r\nF-2026   n=95   fit=94     98.9%\r\nM-2024   n=243  fit=242    99.6%\r\nM-2025   n=253  fit=227    89.7%\r\nM-2026   n=71   fit=67     94.4%\r\n\r\n--- per unit (residual > 0 only) ---\r\nEX-english-20241M    n=26   residual=1\r\nEX-english-20251F    n=26   residual=3\r\nEX-english-20251M    n=23   residual=2\r\nEX-english-20252M    n=27   residual=2\r\nEX-english-20261F    n=23   residual=1\r\nEX-english-20261M    n=22   residual=4\r\nEX-korean-20251F     n=26   residual=8\r\nEX-korean-20251M     n=24   residual=6\r\nEX-korean-20252F     n=25   residual=4\r\nEX-korean-20252M     n=29   residual=15\r\nEX-science-20252M    n=23   residual=1\r\n\r\n--- Tier conversion share ---\r\nT1  [0.800,0.867)   48    4.2%\r\nT2  [0.867,0.967)  365   31.8%\r\nT3  [0.967,1.067)  460   40.1%\r\nT4  [1.067,1.200]  228   19.9%\r\n--  outside band        47    4.1%\r\n\r\n[FAIL] GATE 3 mismatches=1 -- EX-social-20261M\r\n       band figures above are usable but the run is NOT a pass. Locate the\r\n       defect before naming an owner: a count/sum that lands exactly on the\r\n       printed declaration once a parse rule is corrected is a parser defect\r\n       (M2/M3, fixed 260902), not a transcription defect. M5 remains one --\r\n       EX-science-20242F summary 78.8/21.2 vs enumerated 80.0/20.0.\r\n"
    },
    {
      "command": "python tools/regen_rubric_values.py",
      "exit": 1,
      "warn_lines": 0,
      "output": "계층 4행 없음: [('F-2024', '226', '226', '100.0'), ('F-2025', '260', '245', '94.2'), ('F-2026', '95', '94', '98.9'), ('M-2024', '243', '242', '99.6'), ('M-2025', '253', '227', '89.7'), ('M-2026', '71', '67', '94.4')]\r\n"
    },
    {
      "command": "python tools/check_assurance_contract.py",
      "exit": 1,
      "warn_lines": 0,
      "output": "FAIL analysis/wip/260910_astra_fallback_policy_proposal.md: status 'pending' outside ['blocked', 'done', 'in-progress']\r\nFAIL analysis/wip/260910_astra_fallback_policy_proposal.md: no NEXT: line — cannot be resumed\r\nFAIL analysis/wip/260910_info_astra_pilot_questions.md: no status: field (CLAUDE.md 규격 ②)\r\nFAIL analysis/wip/260910_info_astra_pilot_questions.md: no NEXT: line — cannot be resumed\r\nFAIL analysis/wip/mainloop_260907_info_onboarding.md: status 'active' outside ['blocked', 'done', 'in-progress']\r\nFAIL analysis/wip/RESUME.md: no status: field (CLAUDE.md 규격 ②)\r\nFAIL analysis/wip/RESUME.md: no NEXT: line — cannot be resumed\r\nFAIL ruler gate: regen_rubric_values.py exit=1 (expected 0)\r\nFAIL ruler gate: detector did not prove its own detection power (원칙 12-d)\r\nFAIL ruler gate: ruler is stale -- ?\r\nassurance-contract: 10 failure(s)\r\n"
    }
  ]
}
```


### ?? ?? ?? ? ?? ?? ??
?? ??? ??? **10? ? 8? ??**?. ?? 10/10 ??? ?? ??? ???? ???. ?? 6?? ????? `analysis/catalog/info.md`? 64,517 bytes / `48db904b1e4c8cfc5256e93ecd036f4ea19466720adbc55ee89e4c40d0dc1c64`, `output/_index.md`? 175,118 bytes / `527b917b9ef897923593a7bc25d5cabfc38ef93363d86ae654879bf312076151`? ?? ??? ???. ?? ?? ??????? ? ??? ??? ?? ?? ??? ????. ?? ????? ??? ?? ???? ???? ?? ??? ??? ???.
NEXT ???? ??: ? ? ??? ?? ?? ?? ?? ??? ?? ??? ?? ????. ? ? ?? ??? two-key ??? ????, ??? ????? ?? N/V ??? ???? ???. ?? ? blocked.

## 2026-09-11 재개 정정: 두 입력의 변경은 개행뿐
- author: 메인 루프 (Codex/OMX); grade: proposal; 모델 호스트 미확인. 독립 감사 또는 배포 판정 아님.
- git 저장본과 현재 파일을 바이트 해시 및 CRLF→LF 정규화 내용으로 각각 대조했다. 정규화는 비교 메모리에서만 수행했으며 제품/기준 파일은 변경하지 않았다.
- analysis/catalog/info.md: commit 51b2702184e97e44d4a1d3bcfdcd17298670ffa4 저장본 63937 B/171b7d8a671f39a9 → 현재 64517 B/48db904b1e4c8cfc. 580행 전부 동일, 증가 580 B는 CRLF 개행에 대응한다.
- output/_index.md: commit aed832b79a07731855c51a001be6b65e3a0779a8 저장본 174713 B/6d550bd60e16a9552c0085a40935c105217a3ad4c0fe24397329eec1ef04474d → 현재 175118 B/527b917b9ef89792. 405행 전부 동일, 증가 405 B는 CRLF 개행에 대응한다.
- 검증: 두 파일 모두 NORMALIZED_EQUAL True, 내용 diff 없음, 명령 exit 0. 바이트 해시는 여전히 다르므로 기존 동결 해시와 일치했다고 기록하지 않는다. 다만 이번 두 해시 차이를 새로운 내용 변경/승인 누락으로 취급했던 추론은 철회한다. 이전 BF4/BF6 카탈로그 보강에 따른 N/V 재측정 필요는 별개로 유지한다.
- 이전 체크포인트 일부에 실제 물음표로 저장된 한글 손상이 있어 이 UTF-8 부록을 유효한 최신 요약으로 사용한다. 과거 기록은 삭제/치환하지 않는다.
- 남은 차단: 기준 재생성기의 4계층 조건과 실제 6계층 불일치에 대한 two-key 수리 판정, 전역 기준 실패, 정보 서답형 Tier/D5 미서명, 현행 기준하 A/B50 N/V 재측정 및 인증된 독립 감사/최종 판정. SET-260908-info-26 판정을 A/B50 승인으로 전용하지 않는다.
- NEXT: 기준 소유자의 6계층 수리·재동결 판정을 확보하여 허용 범위 확인 → measure_score_bands / regen_rubric_values / check_assurance_contract 순차 통과 → A/1–A/5 파일럿 → A/B50 전수 재검증·독립 판정 → 승인분 배포. 사용자 진행 요청은 배포 기준 면제가 아니다.