---
title: 정보 A/B50 Q1 수정 통합 후보 — B1/B2/B3·호출부·입력 패키지
created: 2026-09-12
author: 메인 루프 (Codex/OMX)
grade: proposal
model: 미확인 (호스트 모델·깊이 증빙 미노출)
state: awaiting-independent-ruling
release: blocked
---

## 범위와 판정 소비
`260912_04_info_ab50_q1_independent_ruling.md` [Codex/OMX 지시]에 따른 작성 책임의 이어쓰기다.
기존 01/02/03/04, 보호 기준 3개, 실운영 호출부는 무수정이다. BF1 명세 완결성은 재작성하지 않았다.
독립 판정·정식 적격성 확인·A/B 문항 품질감사·배포 승인은 수행하지 않았다.
현재 세션의 모델은 판정문에 기록된 이전 세션의 사용자 모델 확인으로 소급 인증하지 않는다.

## 수정 내용
| 요구 | 후보 변경 | 작성자 시험 |
|---|---|---|
| B1 | 동결/형식 검사를 통과한 partial/unresolved만 SourceIncomplete로 분리하여 원천 단계 exit1. 상태별 ID·미확정 근거·원천 coverage 보존. 입력/해시/스키마 오류 exit2 | 60유닛 × 2상태 = 120건, 오분류0·목록 손실0 |
| B2 | derive의 필수 source_units 인자로 distribution ID를 양방향 대조. 중복·누락·동수대체 거부. diagnostic_units와 statistical_units를 분리 | 60 × 삭제/중복/동수대체 = 180건, 미검출0; 정상 분포 수용 |
| B3 | 측정 단계는 stage_measurement_exit, 최종 main 래퍼에서 단일 contract_exit 출력 | stale/fixture 실패/합성 clean의 1/2/0 모두 일치 |
| 호출부 | 기존 assurance argv에 --source-contract 및 고정 공급 경로만 추가. 모든 기존 검사 AST 동일 | 실제 후보 CLI 15건 + 격리한 실제 호출부 블록 3건, 실패0 |

main의 미실행 downstream은 `not-run`, exit=null, reason=source-incomplete로 출력한다.
그 반환1은 **원천 단계 실패**이며 미실행 단계를 통과 처리한 전역0이 아니다. 상위 assurance는
검출력/정본 대조 증거가 없는 경우 기존 검사를 그대로 실패시킨다. 현재 계약 입력은 60개 모두
unresolved이므로 원천 단계에서 멈춘다. 운영 배포가 가능한 계약을 꾸며내지 않았다.

## 후보 파일·동결
이 문서와 같은 디렉터리의 `260912_05_info_ab50_q1_` 접두사 파일:
- `repaired_candidate.py`: 수정 통합 재생성기.
- `repair_delta.patch`: 01 후보 대비 B1–B3 차이.
- `integrated.patch`: 현행 tools/regen_rubric_values.py 대비 전체 차이.
- `assurance_candidate.py`, `assurance.patch`: 호출부 사본과 현행 대비 정확한 차이.
- `source_contract.json`: snapshot/dispositions 입력 후보. 전 유닛 unresolved.
- `source_evidence.json`: 소유/승인/공급 위치, 120개 파일 bytes/hash/locator, 전 유닛 근거 상태.
- `build.py`: 입력 앵커·gate0 AST·120파일 해시를 확인하는 재생성기. 운영 파일에는 쓰지 않는다.
- `regression_test.py`, `baseline_result.json`, `regression_result.json`: 303건 도메인과 결과.
- `caller_test.py`, `caller_result.json`: 실제 CLI·호출부 경계 시험과 stdout/stderr.
- `verify.py`, `validation.json`: 통합 재실행 명령·출력·정적 검사·한계.
- `manifest.json`: 직접 소비 입력·후보·증거의 path/bytes/full SHA256/role. 원천120파일은 source_evidence.json에 개별 동결.

manifest 자체와 매번 갱신되는 validation.json, WIP/런타임 체크포인트는 자기참조 해시에서 제외한다.
manifest에 열거된 과거 파일의 간접 링크 전부를 검토 입력으로 확대하지 않는다. 과거 문항 본문,
이미지, 카탈로그 내용 품질, 타인 WIP는 이번 독립 코드 재판정 범위 밖이다.

## 재현과 결과
```powershell
python output/260912/rev/260912_05_info_ab50_q1_regression_test.py --baseline --no-save
python output/260912/rev/260912_05_info_ab50_q1_verify.py
```
- 원후보: 303건 중 알려진 결함302건 재현(상태120·유닛180·종료2), 정상 통제 수용. baseline harness exit0은 결함 재현 성공이지 후보 통과가 아니다.
- 수정본: 같은 303 ID 전수 대조, 실패0. expected/observed/duplicates/missing/extra는 결과 JSON 및 재실행 stdout에 출력한다.
- 기존 15케이스 실패0, 기존 gate0 planted11/undetected0 유지. 보호 파일·원후보·기존 시험·원출력·판정문 무손상 확인.
- 측정기 실제 exit1/WARN40, per-item1148행 재현. 두 측정 실행과 원출력 동일. 행수는 인쇄ID 완전성 증거가 아니다.
- CLI15/호출부3: 기대 종료·terminal 일치, stderr 경고0. 호출부는 **전체 assurance 실행이 아니라** 변경된 호출 블록을 그대로 실행하고 경로 두 곳만 후보로 연결한 시험이다.
- Python6파일 compile/AST·후보 trailing whitespace 검사, 전체 패치 정확성 통과. ruff/mypy/pytest 미설치, 의존성 추가 없음. 전체 assurance/build는 실행하지 않았다.
- textpatch self-test exit0, seeded10/undetected0. 의도된 mixed-EOL 거부 FAIL/WARN 출력이 있으므로 경고0 시험으로 합산하지 않는다.
- git diff --check exit0. 기존 작성 WIP의 LF→CRLF 경고는 별도 기록하며 예기치 않은 harness 경고로 숨기지 않는다.

기존 시험 코드는 메모리 사본에서 후보 경로·추가 source_units 인자·임시 raw 목적지만 변경했다.
기존 assertion은 보존했다. 성공 배선용 clean/mock은 단위시험에만 존재한다. 실제 WARN을 필터링한
출력을 운영 성공 근거로 쓰지 않는다. CLI 테스트의 eligible 입력 역시 명시적 합성 통제다.

## 원천 입력·공급 계약
| 항목 | 현재 후보 |
|---|---|
| 입력 공급자 | Codex/OMX 작성 소유자: 후보 작성만. 적격성 승인권 없음 |
| 동결 기준 | 260911_04_info_ab50_repair_spec.md 원천60유닛 표. 현재120파일 bytes/hash 일치 |
| 승인 주체 | 사용자 정책키 + 독립 판정의 정확한 구현/입력 감사키 |
| 공급 후보 | 현재는 rev/의 source_contract.json. 두 키 이후에만 analysis/info_ab50_source_contract.json으로 공급하는 안 |
| 현재 승인 값 | policy_key=null, exact_patch_audit_key=null; 운영 공급 파일 미설치 |
| 인쇄ID·수량·적격성 | 확인하지 않은 값은 null/unresolved/blocked. 분모·인쇄ID를 출력행 수에서 만들지 않음 |
| 상태 세분화 | sidecar 전유닛 목록에 source file/hash/locator와 missing_evidence 기록. 실제 내용 확인 전 partial/eligible 확정 금지 |

source_contract는 프로그램이 소비하는 두 필드(snapshot/dispositions), source_evidence는 승인·근거
인계용 sidecar다. 프로그램은 승인자의 신원을 자체 인증하지 않는다. 검토·두 키·공급 소유권이
승인 경계이며, 이 후보 파일의 존재 자체는 승인 증명이 아니다. 내용 검증은 이 코드 수리 범위 밖이다.
통계 집계 포함/비적용 집합과 전체 진단 출력 집합의 동일성을 주장하지 않는다. 실제 적격 입력이
없으므로 정식 통계 적용은 미완료다. 기존 관측 측정기의 집계 규칙을 이 후보에서 변경하지 않았다.

## 결정 요청 — 한 묶음
- [ ] Q1 B1–B3 및 호출부/입력 패키지를 독립 재검증하여 정확한 후보 diff에 approve/revise-required/reject를 판정한다. 원본303 경계·기존15/11을 소비하며 기준을 수정하지 않는다.
- [ ] 사용자 정책키 요청: 현재 동결 원천에서 근거 확인 후 도출되는 모집단/계층 재서명과 260911_06 §3 contract_exit 운영 적용, 위 고정 공급 위치 및 정확한 CLI 변경을 승인할지 결정한다. **미확정60개를 적격으로 승인하거나 WARN40을 면제하는 요청이 아니다.**
- [ ] 실제 입력 근거가 미완성이면 코드 후보 적합성과 운영 적용 가능성을 나누어 기록한다. 적용 가능한 파일·범위를 명시하고, 두 키와 입력 근거가 없는 부분은 blocked로 남긴다.

잔여: 정식 원천 적격성/인쇄ID/합계축, WARN40, Q3 정보 난이도, A/B 전수 독립 검증, 최종 판정 및 산출물 동기화.
정본 반영·재동결·배포는 아직 하지 않는다. 새 BF1 명세 라운드나 부분 후보별 반복 승인을 만들지 않는다.

## history
- 2026-09-12: Codex/OMX 작성 이어쓰기. 판정04의 B1–B3 수리·호출/입력 후보·작성자 회귀시험을 한 묶음으로 준비. 독립 판정 아님, 정본 무수정, 배포 blocked.
