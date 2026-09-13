---
title: 정보 A/B50 배포 선행 기준 수리 결정요청
created: 2026-09-11
requested_by: main-loop
author: 메인 루프 (Codex/OMX)
grade: proposal
state: blocked
---

## 범위 및 현재 권한
대상은 정보 A/1–A/25, B/1–B/25의 배포 선행 기준이다. 이 요청서는 문항의 독립 감사나 배포 승인이 아니다. SET-260908-info-26의 기대 출력/판정을 A/B50에 적용하지 않는다.
사용자는 같은 대화에서 배포까지 진행 및 이후 「수행」을 지시했다. 진행 권한의 근거이지, 아래 미결정 기준의 구체적 선택이나 두 번째 열쇠를 대신하지 않는다.
현행 Astra 단독 운영하 별도의 깨끗한 컨텍스트에서 판단해야 한다. 요청 측 실행 모델의 호스트 증빙은 미노출이다. 독립 판정자는 아직 실행되지 않았다. 팀/외부 세션 발주 없음, 측정 가능한 잔여 dispatch 예산 없음. 이 문서는 발주 명령이 아닌 준비된 결정요청이다.

## document / 근거
품질 보고서의 최신 부록에 과거 실행 명령·전체 출력이 저장되어 있다. 이번에는 재생성기 derive()의 `if len(strata) != 4`를 직접 확인했다. 기존 측정에는 F/M × 2024/2025/2026의 6계층이 있어 비교 이전에 중단한다. 4를 6으로 바꾸는 임의 수리는 금지한다.
기존 실행: measure_score_bands exit1/WARN40; regen_rubric_values exit1; check_assurance_contract exit1/10 failures. 이는 저장된 실행 결과이며 이 요청서 작성 중 재실행했다고 주장하지 않는다.
카탈로그·인덱스의 최신 해시 차이는 개행만의 차이임을 git 저장본과 정규화 내용으로 확인했다. 추가 내용 변경이라는 의심은 철회했으나, 이전 카탈로그 보강에 따른 N/V 재측정 필요는 남는다.

## rounds
독립 tier-1/tier-2 수리 검토 및 이번 기준 수리 판정은 없음. 품질 보고서의 메인 루프 기록은 proposal이며 해당 독립 절차를 대체하지 않는다. 기존 260911_01 판정은 별도 26문항 세트이고, 이번 기준 수리를 승인하지 않았다. 기존 Cycle1 F2-2는 partial 유닛 FAIL 유지/면제 기록이며 전역 자 게이트 PASS가 아니다.

## open_questions
1. 모집단에 2026 자료가 추가된 현상에 대해, 현행 자의 모집단 계약을 유지할 것인가 또는 원본에서 파생되는 계층 집합으로 재서명할 것인가? 승인하는 경우 정확한 대상 모집단, 허용 파일, 누락/중복/추가 계층 검출 및 연도 합=ALL 검증을 명시하라. 고정 숫자만 교체하거나 유닛을 임의 제외하는 수정은 요청하지 않는다.
2. EX-social-20261M partial에 대한 기존 F2-2 면제와 전역 measure 게이트 요구의 관계는 무엇인가? 관측하지 못한 배점 생성 및 FAIL→PASS 위장은 금지한다. 적용 범위와 명시적 미통과 처리를 결정하라.
3. 정보 서답형 Tier 및 T4 추가 사고력 조건의 미서명을 어떤 별도 판정으로 해소해야 하는가? 기존 최고 수준+필수적인 추가 사고력이라는 사용자 조건을 낮추지 않는다. 이번 수리 판정과 문항별 난이도 승인을 분리하라.
4. 승인 가능한 수리가 있다면 two-key 반영 절차와 재측정해야 할 기존 판정 범위를 명시하라. 다른 소유자의 WIP 상태를 추정하여 바꾸는 작업은 포함하지 않는다.

## output_format / 승인 전 검증
| question | ruling (approve / revise-required / reject / blocked) | 직접 확인한 evidence | 허용 변경 및 note |
각 수정은 명령·기대 출력·경고 수·기대 카운트, 회귀/결함 주입 검증 및 원본 기반 기대값 생성 방식을 명시한다. 기존 §5-a의 exit0, undetected=0, stale=0 lines=0 residual=0, 지적0/WARN0을 무단 완화하지 않는다. 기대값은 승인자가 정하며 요청자가 현재 실패에 맞춰 채우지 않는다.
회신 경로: output/260911/rev/260911_03_info_ab50_ruler_ruling.md (아직 없음).
판정자는 실제 모델/깊이·독립 실행 증거·읽은 입력·해시를 기록한다. 모델 미확인이면 인증된 Astra 판정으로 표시하지 않는다. 허용 쓰기는 자신의 회신뿐이며 제품/자/타인 WIP/공유 원장은 수정하지 않는다. no-commit.

## stop / resume
판정 전 기준 수정·N/V 확정·배포는 blocked. 회신을 읽고 허용 범위 및 사용자 키를 확인한 뒤에만 소유자 수정과 bytes+sha256(16) 재동결을 진행한다. 다음은 기준 검사 3종, A/1–A/5 파일럿, A/B50 전수 및 수정 후 독립 검증, 최종 승인, 승인분 문제지/답지/정본/인덱스 동기화다.

## 입력 동결 (작성 시 실측)
| path | bytes | SHA256 |
|---|---:|---|
| analysis/catalog/DIFFICULTY_RUBRIC.md | 20921 | 07dab5d38c8da48a22ca01d2f4c2b75d71fdd421a6da5ad3fcdd1a3b81b1ad99 |
| tools/measure_score_bands.py | 21969 | 0cf91284e2c1f7b1be4d94a09d641996614d65fa88fdf8444b9f9daa3958fe24 |
| tools/regen_rubric_values.py | 21594 | 599fbdef489fa1475dfba5dad76c3cd7eb0b133150359902c1b0590aa9ae11d1 |
| tools/check_assurance_contract.py | 11648 | 45ed11661961ce1d7d46f5874db0d9b1b05ec724d577844bdf410228459c6802 |
| output/260910/rev/260910_14_item_quality_audit.md | 50910 | bea97c7de546a707c55dcaa6d5621569e1d6fa516a1d99f9467ab0143002ab05 |
| output/260911/rev/260911_01_info_v1_criterion_ruling.md | 32195 | 61eb47788b53b2c5134e5723678a52ee8fb96dbed909967f5ae8aa9bb74a5fb3 |
| output/260903/rev/260903_06_arbiter_ruling_cycle1_f.md | 14321 | 6992e0faecda6fcf08609eac44b65c2de984686771f6f527125efedd4a61936b |
| docs/ASTRA_EXECUTION_POLICY.md | 2901 | 760b9dc375712f27d93aaf36b58b521f47603800669bbc3e7b8274c5b1ee5082 |
| analysis/REV_GUIDE.md | 48947 | 371f3963c239d6463320c5cdde5a14f8b811493d33ed403c7e4413a88bca5ffb |
