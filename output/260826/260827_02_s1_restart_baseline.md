---
title: "Cycle-0 S1 재개 기준선 및 지침·도구 비교 검증"
created: 2026-08-27
author: Codex/OMX
status: evidence-baseline
governing_prd: output/260826/260826_01_operations_cycle_prd.md
scope: 2024·2025 2학기 신규 기출 26개 코퍼스 대상
---

# Cycle-0 S1 재개 기준선 및 지침·도구 비교 검증

## 1. 판정 범위

이 문서는 중단된 S1을 안전하게 재개하기 위한 **현황·도구·지침 기준선**이다.
카탈로그·HARVEST_LOG·EXTRACTION_LOG 상태를 바꾸지 않으며, 유형 판단이나 Opus 판정을 대체하지 않는다.

## 2. 데이터 완성도 (2026-08-27 실측)

| 지표 | 값 | 판정 |
|---|---:|---|
| PRD 대상 코퍼스 | 26 | 기준 모수 |
| `transcript.md`·`meta.yml`·`verify_log.tsv`를 모두 가진 코퍼스 | 15/26 (57.7%) | 부분 완료 |
| 세 파일 중 하나 이상이 없는 코퍼스 | 11/26 (42.3%) | S1 미완료 |
| HWP 원본 | 25 | 기계 변환 완료 |
| PDF 시험지 원본 | 1 | 기존 코퍼스 단위 완성 |
| 보존된 HWP bindata 파일 | 204 | 전사 전 사실 값 |

미완료 코퍼스는 `EX-math2-20252M`, `EX-english-20252M`, `EX-info-20252M`,
`EX-science-20252M`, `EX-social-20252M`, `EX-history-20252M`,
`EX-korean-20252F`, `EX-english-20252F`, `EX-science-20252F`,
`EX-social-20252F`, `EX-history-20252F`이다. 이 11개는 추출 텍스트와 bindata만 있으며,
축자 전사·meta·verify_log·문항/이미지 수율 판정 전에는 S1 완료로 간주하지 않는다.

## 3. 도구 성능 비교 (동일 원본, 임시 경로 실행)

대상: `origin_data/2025_2학기_1학년_중간/2025_2학기_중간_1학년_통합과학2_고사원안.hwp` (8,952,320B).

| 도구 | 결과 | 측정값 | 의미 |
|---|---|---|---|
| Git HEAD의 기존 `tools/hwp2md.py` | exit 1 | `FileNotFoundError: hwp5html` | PATH만 탐색해 이 환경에서 변환 불가 |
| 현행 `tools/hwp2md.py` | exit 0 | 텍스트 23,443B, `bindata=18 imgrefs=22` | 사용자 site-packages 스크립트 경로 탐색 성공, 매립 이미지 보존·마커 계수 제공 |

따라서 이 환경에서의 변환 가용성은 **실패(0/1) → 성공(1/1)** 으로 개선됐다. 다만 `imgrefs=22`와
`bindata=18`은 같은 파일의 복수 참조일 수 있으므로 오류로 단정하지 않는다. 전사에서 마커 22개 각각을
설명하거나 `[unreadable]`과 `verify_log.tsv` 행으로 처리해야만 S1 게이트가 통과한다.

## 4. 지침 개선 검증

현재 `AGENTS.md`는 다음을 명시한다.

- 팀 구성 전 역할 지침·페르소나·정본 입력·쓰기 경계·게이트를 확인하는 사전 점검
- 팀 배치의 명시적 `lane = model` 표기: 정확도 중심 작업은 Sol, 좁은 읽기 전용 조사는 Luna
- 외부 Claude Code Opus 역할의 운영 권한을 유지하는 분리 규칙
- Sol 결과를 Opus와 동일 입력·동일 스키마로 섀도우 비교하는 대체 가능성 평가 절차

이 개선은 지침의 **추적 가능성**을 높이는 것이며, 아직 Sol과 Opus의 동형 과업 3건 비교 결과는 없다.
따라서 어떤 Opus 역할도 “대체 가능”으로 판정하지 않는다.

## 5. 다음 순서와 차단선

1. 미완료 11개를 코퍼스 단위로 축자 전사하고 HWP 수율(문항수 ±1, 이미지 마커 전건)을 검증한다.
2. 26개 전체 S1의 필수 파일·수율·대장 정합성을 재검증한다.
3. 그 뒤에만 외부 Claude Code Opus의 `type-proposer`용 `[CC 회람]` 패키지를 만든다.

S2 제안, 카탈로그 변경, 신규 ID 부여, HARVEST_LOG 반영은 이 기준선 문서의 범위 밖이며 Opus 회신 전까지 수행하지 않는다.
