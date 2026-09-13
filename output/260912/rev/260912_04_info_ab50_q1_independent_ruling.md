---
title: 정보 A/B50 Q1 통합 후보 독립 판정
created: 2026-09-12
author: Codex/OMX
responsibility: 독립 판정 (rev-arbiter 책임, Claude Code 역할 신분 아님)
model: gpt-6-astra
model_evidence: 사용자 확인을 근거로 인정하라는 현재 대화의 명시 지시
observed_reasoning_depth: 미확인
host_model_verified: false
independence: 후보 작성에 참여하지 않은 별도 컨텍스트; 인계 후 허용된 후보와 선행 판정만 검토
grade: binding (이번 세 요청의 한정 판정)
verdict: revise-required
repair_execution: blocked
release: blocked
---

# §0 판정 요약표

| unit | verdict | grade | evidence | measured | closure | note |
|---|---|---|---|---|---|---|
| Q1 통합 후보 구현·반영 범위 | revise-required | binding | §1 재현 A/B; 후보 :99–107, :205–209, :467–599 | yes | 기존 15/15 및 gate0 11/11 재현; 추가 상태 결함 120/120, 출력 유닛 결함 180/180, 종료표시 결함 2/3. 각각 최소 수리 후 잔여 0/120, 0/180, 0/3 | 구속 보완 B1–B3. 현재 패치의 정본 반영 승인 아님 |
| Q2 contract_exit 운영 계약·사용자 키 | approve | binding (06 §3 계약 의미 한정) | 260911_06_info_ab50_state_contract_spec.md §1–5; §1-C; 03 §2 Q4 | yes | 3단계 0/1/2 합성 27/27 모순 없음. 실제 원천 적용 완료·적격성 폐쇄는 미승인 | 전역 FAIL 유지 계약은 타당. 사용자 정책키 및 정확한 구현 승인 미충족으로 적용 blocked |
| R3 최소 후속 범위 | approve | binding (후보 보완·증거 준비 한정) | 02 검토 묶음 잔여·요청; tools/check_assurance_contract.py:268–283; §2 R3 | yes | 요청 3/3 대응. 운영 계약 입력 없는 CLI exit2 재현; 원천 60/60·120파일 바이트 확인은 내용 완전성과 구별 | B1–B3와 호출부/입력 패키지를 한 후보로 보완. 보호 기준·제품 즉시 수정 0개 |

**종합: revise-required.** 판정 역할은 완료하되 Q1 반영·전체 배포는 ▲ blocked다. 과거 BF1 명세 완결성은 07에서 닫힌 상태를 유지하며 다시 판정하지 않는다. R3는 이 검토 묶음의 세 번째 요청을 구분한 표기이며 기존 **Q3 정보 난이도 기준**과 다른 항목이다.

# §1 독립 재검증

## 실행·권한 및 실제 입력 범위

- 본체 직접 실행, 서브에이전트·팀·자동 외부 재시도 없음. 실제 수행자는 Codex/OMX다.
- 사용자 최신 발언: “현재 Astra를 선택했다. 모델 확인은 내 확인을 근거로 인정하고, 이 세션에서 독립 판정을 계속해라.” 이에 따라 모델 선택의 사용자 확인을 이 판정의 근거로 사용했다. **호스트 모델/깊이 검증으로 표시하지 않는다.** 깊이는 미확인이다. 이 지시는 Q2 정책이나 제품 반영·배포의 사용자 키가 아니다.
- 이 컨텍스트는 01 후보·02 묶음·선행 명세를 작성하지 않았다. 인계 뒤 정책·입력·후보를 읽고 재실행했다. 기존 작성 과정 전체를 전달받은 작성 컨텍스트를 감사자로 재표시한 것이 아니다. 파일 접근 격리나 서버 내부 라우팅 증명은 주장하지 않는다. 문항 맹목 풀이도 아니다.
- 실제 읽기: 현재 대화의 AGENTS 지침, 아래 문서의 관련 규약·결정 절, 후보·패치·시험 전체, 원출력과 결과 JSON, 보호 파일(측정기는 실행 관련 코드·기계 실행, 루브릭은 바이트 및 후보 스캔), 호출부 관련 절, textpatch, REV_LOG 말미. 03의 긴 과거 실행 로그 전부를 새로 검증했다고 하지 않는다.
- 코퍼스는 스냅숏 60유닛의 transcript/meta를 바이트·메타 검사 및 기존 측정기 재실행으로만 읽었다. **이미지 전수, 인쇄 문항ID 전수, 적격성 판정, A/B 답·해설·문항 본문 품질감사는 하지 않았다.** 문서에 간접 링크된 과거 파일은 이 판정의 직접 검증 입력에서 제외한다.
- 쓰기: 본 판정문, 전용 WIP, REV_LOG 한 행. 시험은 임시 디렉터리 및 메모리. 원본 후보·원출력·선행 문서·자의 3파일·다른 작성자 WIP는 무수정. 기존 사용자 변경도 보존했다.
- 예산: 계정 잔여량과 모델 깊이의 측정 수단은 확인되지 않았다. 발주하지 않고 직접 한 후보만 검토했다. 검토 단위는 기존 15케이스/11검출 시험이며 추가 주입은 같은 후보의 누락된 경계 3종에 한정했다.

## A. 원본 시험의 독립 재실행

원 명령은 `python output/260912/rev/260912_01_info_ab50_q1_integration_test.py`다. 이것은 작성자 raw 파일을 재기록하므로 **시험 코드의 raw 출력 경로 한 곳만 임시 경로로 치환한 메모리 사본**을 실행했다. 시험 단언·후보 경로·원천·측정기 호출은 그대로다. 아래 A 재현 코드는 그 차이를 명시한다. 후보 stdout-wrapper 및 __main__을 제거하는 원래 시험 로더의 한계도 그대로이며 무인자 CLI는 실제 subprocess로 실행됐다.

결과: exit0, 15케이스 실패0, 기존 gate0 `planted=11 undetected=0`. 새 raw와 저장 raw가 같고, 결과 JSON 전체도 같았다. 측정기는 새로 두 번 실행했으며 **exit1 / WARN40 / per-item 1148행**이 재현됐다. 시험 harness 성공과 실제 원천 게이트 실패를 합치지 않는다. 1148행은 문항 인쇄ID 커버리지나 A/B 검증 수가 아니다.

```json
{
  "frozen": [
    {
      "path": "output\\260912\\rev\\260912_01_info_ab50_measure_raw.txt",
      "bytes": 76913,
      "sha256": "d5544cfbbc003bdfcebae8587833b2f841c32464993df237f3a4eca445db1859",
      "match": true
    },
    {
      "path": "output\\260912\\rev\\260912_01_info_ab50_q1_integrated.patch",
      "bytes": 8398,
      "sha256": "1cbed11e5c5841585736351b940f827d67c15f7c4f730a893b81e78eefd9b614",
      "match": true
    },
    {
      "path": "output\\260912\\rev\\260912_01_info_ab50_q1_integrated_candidate.py",
      "bytes": 27749,
      "sha256": "cdaf9e1d1670e3ffb21846554c39a5e65bc9b7e5e4da424225480d1e8f48b7fb",
      "match": true
    },
    {
      "path": "output\\260912\\rev\\260912_01_info_ab50_q1_integration_result.json",
      "bytes": 4801,
      "sha256": "e28cf9dd0aab19410b5ca46af083f6da9b2a1cdf52b6a6e0390921bbb34a9fd0",
      "match": true
    },
    {
      "path": "output\\260912\\rev\\260912_01_info_ab50_q1_integration_test.py",
      "bytes": 6192,
      "sha256": "d10efb5cf5a552dbaf13c5f00101b09c1ca1b8bfa7cf052e739d4aac36c43892",
      "match": true
    },
    {
      "path": "output\\260912\\rev\\260912_02_info_ab50_q1_review_package.md",
      "bytes": 4913,
      "sha256": "1399b0711166ed455d612197567680c631e96e0800cd2e84df3ba1031d8f6885",
      "match": true
    }
  ],
  "protected": {
    "tools\\measure_score_bands.py": {
      "bytes": 21969,
      "sha256": "0cf91284e2c1f7b1be4d94a09d641996614d65fa88fdf8444b9f9daa3958fe24"
    },
    "tools\\regen_rubric_values.py": {
      "bytes": 21594,
      "sha256": "599fbdef489fa1475dfba5dad76c3cd7eb0b133150359902c1b0590aa9ae11d1"
    },
    "analysis\\catalog\\DIFFICULTY_RUBRIC.md": {
      "bytes": 20921,
      "sha256": "07dab5d38c8da48a22ca01d2f4c2b75d71fdd421a6da5ad3fcdd1a3b81b1ad99"
    }
  },
  "replay": {
    "scope": "author diagnostic integration; NOT release or eligibility approval",
    "cases": [
      {
        "name": "missing_stratum",
        "rejected": true
      },
      {
        "name": "duplicate_stratum",
        "rejected": true
      },
      {
        "name": "same_count_replacement",
        "rejected": true
      },
      {
        "name": "expected_extra",
        "rejected": true
      },
      {
        "name": "empty_output",
        "rejected": true
      },
      {
        "name": "duplicate_ALL",
        "rejected": true
      },
      {
        "name": "duplicate_outside",
        "rejected": true
      },
      {
        "name": "missing_outside",
        "rejected": true
      },
      {
        "name": "duplicate_tier",
        "rejected": true
      },
      {
        "name": "all_sum_corruption",
        "rejected": true
      },
      {
        "name": "main_live_failure",
        "exit": 1
      },
      {
        "name": "main_empty",
        "exit": 2
      },
      {
        "name": "main_abort",
        "exit": 2
      },
      {
        "name": "main_exit2",
        "exit": 2
      },
      {
        "name": "main_malformed_success",
        "exit": 2
      }
    ],
    "failures": 0,
    "original_gate0_output": "  planted=11 undetected=0\n  [GATE 0 PASS] undetected=0\n",
    "live_child_exit": 1,
    "live_warnings": 40,
    "source_coverage": {
      "expected": [
        "EX-english-20241F",
        "EX-english-20241M",
        "EX-english-20242F",
        "EX-english-20242M",
        "EX-english-20251F",
        "EX-english-20251M",
        "EX-english-20252F",
        "EX-english-20252M",
        "EX-english-20261F",
        "EX-english-20261M",
        "EX-history-20241F",
        "EX-history-20241M",
        "EX-history-20242F",
        "EX-history-20242M",
        "EX-history-20251F",
        "EX-history-20251M",
        "EX-history-20252F",
        "EX-history-20252M",
        "EX-history-20261F",
        "EX-history-20261M",
        "EX-info-20252F",
        "EX-info-20252M",
        "EX-korean-20241F",
        "EX-korean-20241M",
        "EX-korean-20242F",
        "EX-korean-20242M",
        "EX-korean-20251F",
        "EX-korean-20251M",
        "EX-korean-20252F",
        "EX-korean-20252M",
        "EX-math1-20241F",
        "EX-math1-20241M",
        "EX-math1-20242F",
        "EX-math1-20242M",
        "EX-math1-20251F",
        "EX-math1-20251M",
        "EX-math1-20261F",
        "EX-math1-20261M",
        "EX-math2-20252F",
        "EX-math2-20252M",
        "EX-science-20241F",
        "EX-science-20241M",
        "EX-science-20242F",
        "EX-science-20242M",
        "EX-science-20251F",
        "EX-science-20251M",
        "EX-science-20252F",
        "EX-science-20252M",
        "EX-science-20261F",
        "EX-science-20261M",
        "EX-social-20241F",
        "EX-social-20241M",
        "EX-social-20242F",
        "EX-social-20242M",
        "EX-social-20251F",
        "EX-social-20251M",
        "EX-social-20252F",
        "EX-social-20252M",
        "EX-social-20261F",
        "EX-social-20261M"
      ],
      "observed": [
        "EX-english-20241F",
        "EX-english-20241M",
        "EX-english-20242F",
        "EX-english-20242M",
        "EX-english-20251F",
        "EX-english-20251M",
        "EX-english-20252F",
        "EX-english-20252M",
        "EX-english-20261F",
        "EX-english-20261M",
        "EX-history-20241F",
        "EX-history-20241M",
        "EX-history-20242F",
        "EX-history-20242M",
        "EX-history-20251F",
        "EX-history-20251M",
        "EX-history-20252F",
        "EX-history-20252M",
        "EX-history-20261F",
        "EX-history-20261M",
        "EX-info-20252F",
        "EX-info-20252M",
        "EX-korean-20241F",
        "EX-korean-20241M",
        "EX-korean-20242F",
        "EX-korean-20242M",
        "EX-korean-20251F",
        "EX-korean-20251M",
        "EX-korean-20252F",
        "EX-korean-20252M",
        "EX-math1-20241F",
        "EX-math1-20241M",
        "EX-math1-20242F",
        "EX-math1-20242M",
        "EX-math1-20251F",
        "EX-math1-20251M",
        "EX-math1-20261F",
        "EX-math1-20261M",
        "EX-math2-20252F",
        "EX-math2-20252M",
        "EX-science-20241F",
        "EX-science-20241M",
        "EX-science-20242F",
        "EX-science-20242M",
        "EX-science-20251F",
        "EX-science-20251M",
        "EX-science-20252F",
        "EX-science-20252M",
        "EX-science-20261F",
        "EX-science-20261M",
        "EX-social-20241F",
        "EX-social-20241M",
        "EX-social-20242F",
        "EX-social-20242M",
        "EX-social-20251F",
        "EX-social-20251M",
        "EX-social-20252F",
        "EX-social-20252M",
        "EX-social-20261F",
        "EX-social-20261M"
      ],
      "duplicates": [],
      "expected_duplicates": [],
      "missing": [],
      "extra": []
    },
    "diagnostic_strata": [
      "F-2024",
      "F-2025",
      "F-2026",
      "M-2024",
      "M-2025",
      "M-2026"
    ],
    "per_item_rows": 1148,
    "measurement_byte_equal": true,
    "protected_unchanged": true,
    "cli_without_contract": 2
  },
  "stored_result_equal": true,
  "raw_equal": true,
  "protected_unchanged": true
}
```

후보 patch는 현재 base→candidate의 unified diff와 텍스트상 정확히 같았다(개행 정규화 후 패치 내용 대조; 바이트 동결 검사는 별도로 수행). 기존 gate0 함수 AST는 동일했다.

## B. 추가 반례 및 최소 수리 — 운영 파일 무수정

시험 도메인은 위 원천 유닛 식별자 60개다. B1은 각 유닛에 partial/unresolved를 각각 한 번 주입한 120케이스, B2는 각 출력 유닛에 삭제/중복/동수대체를 한 번씩 주입한 180케이스, B3는 최종 상태 경로 3케이스다. 이들은 **합성 입력**이며 실제 60유닛의 통계 적격성을 정하지 않는다.

| 경계 | 현 후보 | 메모리 최소 수리 | 해석 |
|---|---|---|---|
| partial / unresolved | 120/120에서 exit2; 명세 기대는 exit1 | 상태를 입력/스키마 실패와 분리하고 원천 상태·coverage를 보존: 잔여0/120 | 차단 자체는 유지됐지만 상태 의미와 원인 목록이 틀렸다 |
| distribution 유닛 삭제·중복·동수대체 | 180/180 모두 derive가 수용 | 해당 섹션의 유닛ID를 동결 source와 양방향 대조: 미검출0/180; 무변조 정상 입력1/1 수용 | 기존 검사는 계층 집합만 대조하고 출력 유닛 행은 단순 행수로 센다 |
| 최종 stale / 로컬 fixture 실패 / 합성 clean | 실제 return1/2/0인데 표시0/0/0 | 단계 상태 이름 분리 + 최종 반환값을 단일 contract_exit로 출력: 불일치0/3 | clean은 최종 배선 확인용 mock이며 원천 또는 정본 성공 증거 아님 |

**최소 수리의 제한:** 각각의 결함을 닫는 좁은 메모리 실험이다. 통합 수정본·입력 증거·상위 호출부까지 완성하거나 승인한 것이 아니다. 특히 B2의 수리는 진단 분포 유닛의 누락을 닫는 실험일 뿐, eligible/비적용/집계 포함 집합이나 인쇄 문항ID의 전수 증거를 만들어 주지 않는다. 그 기존 잔여는 R3에 남긴다. B1에서 차단 후 실행하지 않은 downstream 단계를 PASS로 표시할 수 없으며, 실제 적용 시 필수 단계별 상태와 미실행 사유를 구분해야 한다.

```json
{
  "patch_matches": true,
  "gate0_ast_unchanged": true,
  "unit_domain": [
    "EX-english-20241F",
    "EX-english-20241M",
    "EX-english-20242F",
    "EX-english-20242M",
    "EX-english-20251F",
    "EX-english-20251M",
    "EX-english-20252F",
    "EX-english-20252M",
    "EX-english-20261F",
    "EX-english-20261M",
    "EX-history-20241F",
    "EX-history-20241M",
    "EX-history-20242F",
    "EX-history-20242M",
    "EX-history-20251F",
    "EX-history-20251M",
    "EX-history-20252F",
    "EX-history-20252M",
    "EX-history-20261F",
    "EX-history-20261M",
    "EX-info-20252F",
    "EX-info-20252M",
    "EX-korean-20241F",
    "EX-korean-20241M",
    "EX-korean-20242F",
    "EX-korean-20242M",
    "EX-korean-20251F",
    "EX-korean-20251M",
    "EX-korean-20252F",
    "EX-korean-20252M",
    "EX-math1-20241F",
    "EX-math1-20241M",
    "EX-math1-20242F",
    "EX-math1-20242M",
    "EX-math1-20251F",
    "EX-math1-20251M",
    "EX-math1-20261F",
    "EX-math1-20261M",
    "EX-math2-20252F",
    "EX-math2-20252M",
    "EX-science-20241F",
    "EX-science-20241M",
    "EX-science-20242F",
    "EX-science-20242M",
    "EX-science-20251F",
    "EX-science-20251M",
    "EX-science-20252F",
    "EX-science-20252M",
    "EX-science-20261F",
    "EX-science-20261M",
    "EX-social-20241F",
    "EX-social-20241M",
    "EX-social-20242F",
    "EX-social-20242M",
    "EX-social-20251F",
    "EX-social-20251M",
    "EX-social-20252F",
    "EX-social-20252M",
    "EX-social-20261F",
    "EX-social-20261M"
  ],
  "state_cases": [
    {
      "state": "partial",
      "expected_cases": 60,
      "original_exit_counts": {
        "2": 60
      },
      "minimal_exit_counts": {
        "1": 60
      },
      "minimal_residual": []
    },
    {
      "state": "unresolved",
      "expected_cases": 60,
      "original_exit_counts": {
        "2": 60
      },
      "minimal_exit_counts": {
        "1": 60
      },
      "minimal_residual": []
    }
  ],
  "distribution_cases": [
    {
      "kind": "delete",
      "expected_cases": 60,
      "original_undetected": 60,
      "affected_all_units": true,
      "minimal_undetected": []
    },
    {
      "kind": "duplicate",
      "expected_cases": 60,
      "original_undetected": 60,
      "affected_all_units": true,
      "minimal_undetected": []
    },
    {
      "kind": "same_count_replace",
      "expected_cases": 60,
      "original_undetected": 60,
      "affected_all_units": true,
      "minimal_undetected": []
    }
  ],
  "normal_control": true,
  "terminal_results": [
    {
      "case": "ruler_stale",
      "expected_exit": 1,
      "original": {
        "exit": 1,
        "markers": [
          "0"
        ],
        "agrees": false
      },
      "minimal": {
        "exit": 1,
        "markers": [
          "1"
        ],
        "agrees": true
      }
    },
    {
      "case": "local_fixture_failed",
      "expected_exit": 2,
      "original": {
        "exit": 2,
        "markers": [
          "0"
        ],
        "agrees": false
      },
      "minimal": {
        "exit": 2,
        "markers": [
          "2"
        ],
        "agrees": true
      }
    },
    {
      "case": "synthetic_clean",
      "expected_exit": 0,
      "original": {
        "exit": 0,
        "markers": [
          "0"
        ],
        "agrees": true
      },
      "minimal": {
        "exit": 0,
        "markers": [
          "0"
        ],
        "agrees": true
      }
    }
  ],
  "policy_combinations": 27,
  "policy_composition_mismatches": []
}
```

## C. Q2 정책 대조

| 계약 부분 | 근거와 결론 |
|---|---|
| 원천 관측과 적격성의 분리 | 06 §2는 인쇄/추출/관측/정식 통계를 구분하며 원천 미확인을 0이나 적격으로 바꾸지 않는다. 04 §2·03 Q2 경계와 일치 |
| 전역 종료 의미 | 06 §3의 0=해당 단계 완결, 1=판정 가능한 실패/미해결, 2=입력·실행·파싱 불가/검출력 실패는 원칙11의 fail-closed를 유지 |
| 합성 우선순위 | 0/1/2의 3단계 조합 27개 모두 2 우선, 다음1, 전부0일 때만0. 이는 추상 계약 검산이며 현 후보의 전역 실행 성공 증거 아님 |
| 역사 부분 활용 | 06 §3의 별도 historical-permission은 원천 FAIL이나 신규 배포 승인을 덮지 않음 |
| 적용 승인 | 06 §5 및 03 Q4의 사용자 키·정확한 diff 감사키·재동결 필요. 현재 모델 확인 지시를 정책키로 확대하지 않음 |
| 미완료 입력·호출부 | 현재 assurance는 무인자 regen 호출; 현 후보 무인자 exit2. 호출부와 계약 공급을 빼고 단독 설치하면 기존 동작과 호환되지 않음 |

새 상태정책을 작성해서 자기 승인한 것이 아니라 06의 기존 제안을 판정했다. 정책 의미에 대한 감사 판단은 approve이며 **현재 미완성 구현의 감사키가 아니다**. 실제 불완전 자료를 남긴 채 전역 PASS를 얻으려는 예외는 이 계약에 없고 이번에도 승인하지 않는다.

## D. 나머지 입력 바이트

아래 값은 이번 원장 append **전** 측정이다. 이전 판정에 적힌 과거 정책/규약 바이트를 현재값으로 복사하지 않았다. 01 동결6파일과 보호3파일은 §1-A의 전체 SHA256을 사용한다. 코퍼스별 해시는 04 snapshot 표를 기준으로 재대조했고 그 04 자체를 아래에 동결한다.

| path | bytes | SHA256 |
|---|---:|---|
| AGENTS.md | 28450 | e517756f2ceaa1cc9ff947465ad8666f2038796af53178da09dee07b7ef9694f |
| CLAUDE.md | 46198 | d01a29a7b00e3fcd226e6c1cee602dda693ed5a80d5bedb29995908581748841 |
| docs/DATA_STANDARD.md | 27062 | 315c621ba02466561088e1e6d1276218311569218d52caa39e1e9faad2ee35b5 |
| docs/ASTRA_EXECUTION_POLICY.md | 3267 | 40424dd0e82eb36204b61890be8a44cf9f0cd0d95300f217ac86c8366199833b |
| docs/SESSION_HANDOFF_GUIDE.md | 4468 | ca5abfb7ea550cb0e13379067a554b2a6ba0c61364e10f770b7cc5d145600312 |
| analysis/REV_GUIDE.md | 49313 | 62641c9f517bb4b4b2aa1b7ab489f46b2753e375c19d0ee0f40d6be25cdee1fe |
| .claude/agents/rev-arbiter.md | 9239 | c7168c5eca9c56d6150044ca8b0f5a28526d6930048da74e8a059068b4eeb283 |
| output/260911/rev/260911_03_info_ab50_ruler_ruling.md | 68935 | ff129cc5ce45487671ba1f2626237950dccb3f2d57828729906c5dcb66edb8b1 |
| output/260911/rev/260911_04_info_ab50_repair_spec.md | 15649 | 8ee9a46ecbd57ae9826bdf1c8f1b7a93939fa4ce500645421b0e86d309b64249 |
| output/260911/rev/260911_06_info_ab50_state_contract_spec.md | 8389 | 93f75d1a4c0fc6af7df62dbf7e4b3799a62fa5e8ed74b0cb9cc6d87caf7aca22 |
| output/260911/rev/260911_07_info_ab50_bf1_completeness_ruling.md | 13329 | 3d87d3bbb58e93c0c260c12083ce0e938711b3858c0a2bb3f6608170225c4265 |
| output/260912/rev/260912_03_info_ab50_q1_session_prompt.md | 5597 | f2827935a2bafba30077a892a9d1ec7c2d84c70d703d3b83da41f4ee0ca6e1a6 |
| tools/check_assurance_contract.py | 12243 | 85db02a7bd8b191a18bf0b88ec0b4d9ef3b69c1d08342823d9e50dfeb8d21223 |
| tools/textpatch.py | 12170 | eaa4e9b8ff67b87f07a214c37aa5cddf8f027756e977ddf93828e71bacf1cb48 |
| analysis/REV_LOG.md | 245518 | 09169fc0ba1ee13e30f1add77385785977e0b0832521b9c9077a87de10fd1644 |

## E. 재현 명령과 한계

저장소 루트에서 아래 **A, B, C 블록을 각각** PowerShell here-string으로 `python -`에 전달하면 된다. 또는 본 문서의 세 Python 블록을 추출해 순서대로 `python -`에 전달한다. A는 원본 출력 경로를 격리하고, B는 메모리 최소 수리만 수행한다. **원본 파일을 고치거나 임시 수리를 정본에 적용하는 명령이 아니다.**

A 기대: exit0; `stored_result_equal=true`, `raw_equal=true`, `protected_unchanged=true`; cases15/failures0; gate0 planted11/undetected0. 측정 원출력에는 WARN40이 있어야 현재 실패 재현과 같으며 이를 배포 수용치로 승인하지 않는다.

```python
import ast, contextlib, hashlib, io, json, re, sys, tempfile
from pathlib import Path
root=Path.cwd()
h=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
prompt=root/'output/260912/rev/260912_03_info_ab50_q1_session_prompt.md'
frozen=[]
for line in prompt.read_text(encoding='utf-8').splitlines():
 if line.startswith('| output'):
  name,size,digest=[v.strip() for v in line.strip('|').split('|')]
  p=root/name
  frozen.append(dict(path=name,bytes=p.stat().st_size,sha256=h(p),match=p.stat().st_size==int(size) and h(p)==digest))
assert all(x['match'] for x in frozen)
protected=[root/p for p in ['tools/measure_score_bands.py','tools/regen_rubric_values.py','analysis/catalog/DIFFICULTY_RUBRIC.md']]
before={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=h(p)) for p in protected}
test=root/'output/260912/rev/260912_01_info_ab50_q1_integration_test.py'
code=test.read_text(encoding='utf-8')
needle="(HERE/'260912_01_info_ab50_measure_raw.txt').write_text(live,encoding='utf-8')"
assert code.count(needle)==1
with tempfile.TemporaryDirectory(prefix='ab50-independent-') as tmp:
 code=code.replace(needle,"Path("+repr(str(Path(tmp)/'measure_raw.txt'))+").write_text(live,encoding='utf-8')")
 ns={'__file__':str(test),'__name__':'independent_replay'}
 capture=io.StringIO()
 with contextlib.redirect_stdout(capture):
  exec(compile(code,str(test)+'[isolated-output]','exec'),ns)
 result=json.loads(capture.getvalue())
 original=json.loads((test.parent/'260912_01_info_ab50_q1_integration_result.json').read_text(encoding='utf-8'))
 raw=Path(tmp)/'measure_raw.txt'
 print(json.dumps(dict(frozen=frozen,protected=before,replay=result,stored_result_equal=result==original,raw_equal=raw.read_bytes()==(test.parent/'260912_01_info_ab50_measure_raw.txt').read_bytes(),protected_unchanged=before=={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=h(p)) for p in protected}),ensure_ascii=True,indent=2))
```

B 기대: exit0; patch_matches/gate0_ast_unchanged=true; 상태120·분포180·종료3케이스에서 위 원 후보의 결함과 각 최소 수리 잔여0 재현. 원래 후보의 미검출을 숨기는 성공 테스트가 아니라 **결함 존재의 회귀 증거**다.

```python
import ast, contextlib, copy, io, json, re, sys, tempfile, difflib
from pathlib import Path
ROOT=Path.cwd(); folder=ROOT/'output/260912/rev'
p=folder/'260912_01_info_ab50_q1_integrated_candidate.py'
text=p.read_text(encoding='utf-8')
def load(code=text):
 tree=ast.parse(code)
 nodes=[n for n in tree.body if not isinstance(n,ast.If) and not (isinstance(n,ast.Assign) and any(isinstance(t,ast.Attribute) for t in n.targets))]
 ns={'__file__':str(p),'__name__':'independent_test'}
 exec(compile(ast.Module(body=nodes,type_ignores=[]),str(p),'exec'),ns)
 return ns
ns=load()
snapshot={}
for line in (ROOT/'output/260911/rev/260911_04_info_ab50_repair_spec.md').read_text(encoding='utf-8').splitlines():
 if line.startswith('| EX-'):
  u,tb,th,mb,mh=[x.strip() for x in line.strip('|').split('|')]
  snapshot[u]={'transcript.md':{'bytes':int(tb),'sha256':th},'meta.yml':{'bytes':int(mb),'sha256':mh}}
source,coverage=ns['frozen_source'](ROOT/'corpus',snapshot)
expected=sorted(set(source.values()))
raw=(folder/'260912_01_info_ab50_measure_raw.txt').read_text(encoding='utf-8')
# Verify patch/candidate textual correspondence and unchanged legacy gate0 AST.
base=(ROOT/'tools/regen_rubric_values.py').read_text(encoding='utf-8')
patch=''.join(difflib.unified_diff(base.splitlines(True),text.splitlines(True),fromfile='a/tools/regen_rubric_values.py',tofile='b/tools/regen_rubric_values.py'))
assert patch==(folder/'260912_01_info_ab50_q1_integrated.patch').read_text(encoding='utf-8')
gate=lambda code:ast.dump(next(n for n in ast.parse(code).body if isinstance(n,ast.FunctionDef) and n.name=='gate0'))
assert gate(base)==gate(text)
# F1: use real snapshot verification, synthetic per-unit state assignments.
state_old="source_expected = expected_strata(source, contract['dispositions'])"
state_new="""require_equal(list(source), list(contract['dispositions']))
        states = contract['dispositions']
        if not all(s in ('eligible','not-applicable','partial','unresolved') for s in states.values()):
            raise ValueError('unknown disposition')
        if any(s in ('partial','unresolved') for s in states.values()):
            print(json.dumps(dict(coverage=coverage, dispositions=states), sort_keys=True))
            print('contract_exit=1')
            return 1
        source_expected = expected_strata(source, states)"""
assert text.count(state_old)==1
repaired=load(text.replace(state_old,state_new))
def call(n,contract,output='',child=0):
 n['tool_output']=lambda:(output,child)
 with tempfile.TemporaryDirectory(prefix='ab50-contract-') as tmp:
  f=Path(tmp)/'contract.json'; f.write_text(json.dumps(contract),encoding='utf-8')
  previous=sys.argv[:]; sys.argv=['candidate','--source-contract',str(f)]
  cap=io.StringIO()
  try:
   with contextlib.redirect_stdout(cap): result=n['main']()
  except Exception as exc: result=type(exc).__name__
  finally: sys.argv=previous
 return result,cap.getvalue()
states={u:'eligible' for u in source}
c={'snapshot':snapshot,'dispositions':states}
state_results=[]
for status in ['partial','unresolved']:
 observed=[]; fixed=[]
 for uid in source:
  cc=copy.deepcopy(c); cc['dispositions'][uid]=status
  a,_=call(ns,cc); b,_=call(repaired,cc)
  observed.append(a); fixed.append(b)
 state_results.append(dict(state=status,units=list(source),original_exit_counts={str(x):observed.count(x) for x in set(observed)},minimal_exit_counts={str(x):fixed.count(x) for x in set(fixed)},minimal_residual=[u for u,x in zip(source,fixed) if x!=1]))
# F2: distribution unit IDs are disconnected from frozen-source identifiers.
m=re.search(r'=== selective-score distribution ===\n(.*?)\n\n',raw,re.S)
body=m.group(1); rows=body.splitlines(); assert len(rows[1:])==len(source)
def minimal_derive(out):
 part=re.search(r'=== selective-score distribution ===\n(.*?)\n\n',out,re.S)
 ids=[x.split()[0] for x in part.group(1).splitlines()[1:] if x.strip()]
 ns['require_equal'](list(source),ids)
 return ns['derive'](out,expected)
def accepted(fn,out):
 try: fn(out); return True
 except (ValueError,TypeError,KeyError,AttributeError,IndexError,ZeroDivisionError,SystemExit): return False
dist_results=[]
for kind in ['delete','duplicate','same_count_replace']:
 misses=[]; repaired_misses=[]
 for row in rows[1:]:
  uid=row.split()[0]
  replacement='' if kind=='delete' else row+'\n'+row if kind=='duplicate' else row.replace(uid,uid+'-synthetic',1)
  altered=body.replace(row,replacement,1)
  out=raw[:m.start(1)]+altered+raw[m.end(1):]
  if accepted(lambda t:ns['derive'](t,expected),out): misses.append(uid)
  if accepted(minimal_derive,out): repaired_misses.append(uid)
 dist_results.append(dict(kind=kind,expected=list(source),undetected=misses,minimal_undetected=repaired_misses))
assert accepted(minimal_derive,raw)
# F3: early contract_exit=0 survives a later nonzero terminal decision.
clean='\n'.join(l for l in raw.splitlines() if '[WARN]' not in l and '[FAIL]' not in l)+'\n[OK] GATE 1 undetected=0 / GATE 3 mismatches=0\n'
marker_old="print('measurement_exit=%d contract_exit=%d' % (code, contract_exit))"
marker_new="print('measurement_exit=%d stage_measurement_exit=%d' % (code, contract_exit))"
terminal_code=text.replace('def main():','def _main_impl():',1).replace(marker_old,marker_new)
terminal_code=terminal_code.replace("        print('contract_exit=2')","        print('stage_input_or_schema_exit=2')")
terminal_code += "\ndef main():\n    result = _main_impl()\n    print('contract_exit=%d' % result)\n    return result\n"
terminal=load(terminal_code)
final_results=[]
for label,want in [('ruler_stale',1),('local_fixture_failed',2),('synthetic_clean',0)]:
 results=[]
 for n in [load(),load(terminal_code)]:
  # Keep all real scans on ruler_stale. The other two isolate final-status wiring.
  if label=='local_fixture_failed': n['gate0']=lambda *args:1
  if label=='synthetic_clean':
   n['role_scan']=lambda *args:[]
   n['ident_scan']=lambda *args:[]
   n['moved_literals']=lambda *args:[]
   n['residue_scan']=lambda *args:([],[])
   n['git_baseline']=lambda *args:(None,None)
   n['gate0']=lambda *args:0
  exit_code,out=call(n,c,clean,0)
  markers=re.findall(r'(?<![A-Za-z_])contract_exit=(\d+)',out)
  results.append(dict(exit=exit_code,markers=markers,agrees=markers==[str(want)] and exit_code==want))
 final_results.append(dict(case=label,expected_exit=want,original=results[0],minimal=results[1]))
assert all(x['minimal']['agrees'] for x in final_results)
report=dict(patch_matches=True,gate0_ast_unchanged=True,state_results=state_results,distribution_results=dist_results,distribution_normal_control=True,terminal_results=final_results)
print(json.dumps(report,ensure_ascii=True))
```

C 기대: exit0; 조합27·composition_mismatches=[]; 입력 manifest와 코드 위치 출력. REV_LOG는 append 뒤 해시가 바뀌므로 §1-D와 비교할 때 이번 행을 제외한 측정 경계를 지킨다.

```python
from pathlib import Path
import hashlib, json, itertools, re
files=['AGENTS.md','CLAUDE.md','docs/DATA_STANDARD.md','docs/ASTRA_EXECUTION_POLICY.md','docs/SESSION_HANDOFF_GUIDE.md','analysis/REV_GUIDE.md','.claude/agents/rev-arbiter.md','output/260911/rev/260911_03_info_ab50_ruler_ruling.md','output/260911/rev/260911_04_info_ab50_repair_spec.md','output/260911/rev/260911_06_info_ab50_state_contract_spec.md','output/260911/rev/260911_07_info_ab50_bf1_completeness_ruling.md','output/260912/rev/260912_03_info_ab50_q1_session_prompt.md','tools/check_assurance_contract.py','tools/textpatch.py','analysis/REV_LOG.md']
manifest=[dict(path=f,bytes=len(Path(f).read_bytes()),sha256=hashlib.sha256(Path(f).read_bytes()).hexdigest()) for f in files]
def compose(xs):
 return 2 if 2 in xs else 1 if 1 in xs else 0
matrix=[dict(input=list(xs),result=compose(xs)) for xs in itertools.product([0,1,2],repeat=3)]
assert all(x['result']==max(x['input']) for x in matrix)
candidate=Path('output/260912/rev/260912_01_info_ab50_q1_integrated_candidate.py')
needles=['def frozen_source','def expected_strata','official population unresolved','def derive','v[\'units_all\']','def main','source_expected =','measurement_exit=%d contract_exit=%d','return 1 if']
locations={needle:[i for i,l in enumerate(candidate.read_text(encoding='utf-8').splitlines(),1) if needle in l] for needle in needles}
print(json.dumps(dict(manifest=manifest,policy_composition=matrix,composition_mismatches=[],locations=locations),ensure_ascii=True,indent=2))
```

도구 실행 결과: A/B/C 모두 exit0, harness stderr 경고0. 이는 실제 측정기 WARN40과 다른 층이다. `python tools/textpatch.py --self-test`는 exit0, `seeded=10 undetected=0`이었다. 이 자기시험은 mixed 줄바꿈 거부/명시 정규화 fixture에서 의도적으로 FAIL 진단과 WARN을 각각 출력하므로 “경고0 도구 실행”이라고 표기하지 않는다. 실원장 append는 정규화 허용 없이 실행한다.

전체 assurance·lint·typecheck·빌드는 이번 판정에서 실행하지 않았다. 제품 코드를 수정하지 않았으며 판정문 구조·증거 및 입력 무손상 검사만 수행한다. 전역 통과나 배포 검증을 대체하지 않는다.

# §2 unit별 판정

## Q1 — revise-required, 최소 구속 보완 3건

### B1 상태 의미와 실패 원인 보존

- [ ] 후보 :99–107, :476–481의 partial/unresolved를 일반 입력 예외에 합쳐 exit2로 반환하는 경로를 분리한다. 정상 형식·동결 검사를 통과한 partial/unresolved는 06 §3에 따라 exit1, 상태별 유닛 목록과 근거 누락을 보존한다. 입력 누락·해시 불일치·스키마 오류는 exit2로 유지한다.
- 범위는 상태 분기 및 출력 계약뿐이다. 미확인 원천을 eligible로 채우거나 WARN을 제거하는 수정은 금지한다. 입력 형식 오류와 원천 내용의 미확정을 혼동하지 않는다.
- 검출 fixture: §1-B의 전체60유닛×2상태. 상태별 원천 목록을 보존하고 미실행 단계가 성공으로 표시되지 않는지 확인한다. 메모리 수리의 전수 잔여0/120은 수리 가능성의 증거다.

### B2 출력 유닛ID와 원천 연결

- [ ] 후보 :205–209의 distribution 행수만 세는 경로에 유닛ID 양방향 대조·중복 검사를 결합한다. 진단 전체 집합과 실제 통계 포함/비적용/부분 집합은 명시적으로 나누며 계층·ALL 수치만 맞는다고 원천 출력 커버리지를 통과시키지 않는다.
- 검출 fixture: 원천 유닛60개 각각의 distribution 행 삭제/중복/동수대체, 총180개. 현재 후보는 모두 수용하며 최소 유닛ID 대조는 모두 차단한다. 정상 분포는 그대로 수용한다.
- 인쇄 문항ID 완전성은 별도 입력 근거가 필요하다. 이 수리로 원천 전사 품질·정식 적격성·A/B 문항 검증을 승인하지 않는다. 측정기가 실제로 보고하는 전 유닛과 집계 포함 집합을 같은 분모로 재해석하지 않는다.

### B3 최종 종료코드와 출력 일치

- [ ] 후보 :499의 하위 측정 결과에 붙은 `contract_exit=0`을 최종 상태처럼 출력하지 않는다. 하위 상태는 별도 이름으로 보존하고, 로컬 gate0 및 A/B/C 대조가 끝난 최종 반환값을 명확한 terminal contract_exit로 출력한다. 실패 경로도 같은 계약을 따른다.
- 검출 fixture: 실제 루브릭 stale 경로 return1/표시0, 로컬 fixture 실패 경로 return2/표시0, 합성 clean 경로 return0/표시0. 최소 수리 후 세 경로 모두 최종 표시와 반환값 일치.
- 성공 표시는 필수 검증보다 앞서 나와서는 안 된다. **현재 원천 WARN40을 삭제해 운영 성공을 만들라는 지시가 아니다.** clean 표본의 경고 필터링/mock은 결함 주입 배선 확인에만 썼다.

현재 후보를 그대로 적용할 수 있는 보호 정본 파일은 **0개**다. 위 요구는 작성자가 새 후보에서 고칠 범위이며 판정자가 후보를 직접 수정하지 않았다. 기존 15시험/11검출을 폐기하거나 기준을 낮추지 않는다.

## Q2 — approve (정책 의미만), 적용은 blocked

06 §3의 정확한 상태 의미와 전파를 정책 수준에서 수용한다. WARN·partial·unresolved를 남긴 채 전역0을 허용하지 않으므로 기존 원칙과 모순되지 않는다. 0은 그 단계의 완료이지 문항/배포 자동 승인이 아니다.

남은 사용자 결정은 **현재 동결 원천 범위에서 파생한 모집단/계층 재서명 및 06 §3 contract_exit 운영 적용**이다. 이번 사용자의 모델 확인은 이 결정과 다르다. 작성자는 완성된 후보·원천 입력 소유/승인 방식·호출부 diff를 묶어 정책키를 요청해야 하며, 부분 산출물마다 같은 배포 요청을 다시 묻지 않는다. 별도 경고 면제나 Q3 난이도 정책은 이 판정에 포함되지 않는다.

허용 쓰기: 작성자 자기 후보·시험·명세 보완 증거·자기 WIP. 금지 쓰기: 사용자키 및 정확한 수정 diff 독립 승인 전에 현행 보호 기준·실운영 호출부 적용, 가짜 승인 원장, 원천 적격성 자동 확정.

## R3 — approve (최소 보완 경로)

추가 명세 완결성 라운드를 만들지 않는다. 아래를 **한 수정 후보 묶음**으로 준비한다.

1. B1–B3 회귀 증거를 통합 후보 시험에 고정한다. 기존 성공/실패 재현 및 원본 무손상 검사를 유지한다.
2. source-contract의 소유자·동결 입력·승인 근거·공급 위치 및 기존 assurance 호출부의 정확한 diff를 후보로만 준비한다. 무인자 호출 실패를 PASS로 바꾸거나 상위 검사를 삭제하는 방법은 금지한다.
3. 04의 기대 원천 집합에서 출발해 전 유닛 상태·근거 상태를 관리한다. 현재 확인되지 않은 인쇄ID/적격성은 unresolved/blocked로 남긴다. 선언 수나 출력행 수만으로 expected 인쇄ID를 생성하지 않는다. 출처·해시·locator 및 expected/observed/duplicate/missing/extra를 갖춘 근거 없이는 완전성을 선언하지 않는다.
4. 인쇄ID 내용 검증이 필요해지면 그 단계의 허용 원천과 검토 범위를 분명히 별도로 배정한다. 본 세션은 60유닛의 바이트·메타·기존 측정기 범위만 검토했고 이미지를 열지 않았다.
5. 수정 후보와 호출부·입력 패키지를 한 번에 독립 재검증한다. 그 다음 사용자 정책키·정확한 패치 감사키가 모두 있는 부분만 소유자가 적용하고 재동결한다.

# §3 follow-up (비차단)

- 반복 import나 “계층 4행”이라는 남은 설명 문구는 이번 세 구속 보완과 무관한 정리 사항이다. 이를 이유로 별도 리팩터링 범위를 만들지 않는다.
- 정식 적격성·인쇄ID·합계축 근거 결손, 현재 WARN40, Q3 정보 난이도 기준, A/B 전수 독립 검증은 **기존 배포 차단 잔여**이지 이 절에서 새로 만든 Q1 구속 보완이 아니다.
- 추가 JSON 형식/인코딩/적격성 입력 다양성은 완성 호출부 시험에 포함하는 것이 바람직하다. 이 판정은 해당 영역을 전부 검증했다고 주장하지 않으며 별도 미재현 결함을 binding fix로 부풀리지 않는다.

# §4 open units (남은 집합)

| unit | 상태 | 재개 위치/완료 조건 |
|---|---|---|
| 과거 BF1 명세 완결성 | closed 유지 | 07 판정 소비; 재작성·재판정 안 함 |
| Q1 | revise-required | B1–B3와 호출부·입력 증거를 하나의 새 후보로 통합 → 기존15/11 및 새 경계 재검증 |
| Q2 | 정책 의미 approve, 적용 blocked | 사용자 정책키와 정확한 수정 구현 감사키 확보; 현재 모델 확인 지시로 대체 금지 |
| R3 | 후보 보완 범위 approve | source-contract·호출부·전유닛 상태/근거 준비; 미확인은 그대로 기록 |
| Q3 정보 난이도 | 미결 유지 | 별도 근거·서명 |
| A/B50 배포 | ▲ blocked | 원천/기준 및 문항 전수 독립 검증·최종 판정·산출물 동기화 |

## [Codex/OMX 지시]

```text
stage: Q1 후보 보완 — 이번 판정 Q1 revise-required / R3 approve에 따른 작성 책임의 재개
executor: Codex/OMX 작성 소유자. analysis/wip/solve-back-verifier_260910_info_ab50_newsession.md의 NEXT를 읽고 이번 판정을 반영한 자기 체크포인트에서 계속한다. 판정 세션이 수정까지 겸하지 않는다.
inputs: 본 판정문과 §1의 동결 입력. 후보·패치·시험·원출력·보호3파일 해시를 재확인한다. 현재 버전이 다르면 변경 출처 확인 전 적용을 멈춘다.
outputs: output/260912/rev/ 안의 충돌하지 않는 새 버전 후보·패치·시험·결과·검토 패키지, 자기 WIP. 기존 01/02/03 및 본 판정문은 덮어쓰지 않는다.
work: B1 상태 의미/목록 보존, B2 distribution 유닛ID 결합, B3 terminal contract_exit 수정. 호출부와 source-contract 공급 후보를 함께 준비한다. 진단 적격 상태를 정식 승인으로 바꾸지 않는다.
verification-now: 본 문서 §1-E의 A/B/C 재현. A의 cases15/failures0 및 gate0 planted11/undetected0 유지. B의 원후보 결함을 수정본에서 검출하는 회귀 단언으로 전환하고 상태120/분포180/종료3의 식별자 도메인과 중복·누락·추가를 출력한다. 최소 수리 실험을 완성 수정본 승인으로 대체하지 않는다.
gate-for-repaired-candidate: 기존15케이스 회귀 실패0, gate0 planted11 undetected0, 정상 분포 오탐0, 부분/미확정 상태 오분류0, 유닛 삭제/중복/동수대체 미검출0, 최종 코드/표시 불일치0. harness 예기치 않은 경고0. 실제 원천 WARN은 원문 보존하며 현재 WARN40을 통과 기대값으로 바꾸지 않는다.
operational-gate-after-both-keys: python tools/measure_score_bands.py ; python tools/regen_rubric_values.py ; python tools/check_assurance_contract.py 를 각각 독립 실행. 현행 REV_GUIDE §5-a의 exit0 / [GATE 0 PASS] undetected=0 / stale=0 lines=0 residual=0 / 지적행0 / WARN0 기준을 소비한다. CLI 변경이 필요하면 정확한 호출 변경도 두 키 범위와 함께 승인받는다. 무인자 계약을 몰래 생략하지 않는다.
constraints: 제품·보호 기준·실운영 호출부 즉시 반영 금지, 커밋·삭제 금지, 타인 WIP 수정 금지, 승인키 창작 금지. 새 후보 보완만 현재 허용됨.
stop: 후보 보완·시험·호출/입력 패키지가 갖춰지면 한 묶음으로 독립 판정. 승인되지 않은 상태에서 정본 반영·배포로 넘어가지 않는다.
report: 새 후보 경로·해시·기존/추가 시험 결과·잔여 상태 및 정확한 정책키 요청을 함께 보고한다. 동일 BF1 명세 재작성이나 부분 후보별 반복 승인을 요청하지 않는다.
```

Session: RETURN-AUTHOR — 기존 작성 세션 `01a0903f-4294-7412-b42b-f5f8b15b98f9`의 작성 책임으로 복귀한다. 식별자는 실행 프롬프트에 기록된 복귀 위치이며 호스트 세션 가용성·권한 증명은 아니다. 복구 불가 시 NEW-CONTINUATION으로 같은 작성 책임을 승계하고 지정 WIP NEXT에서 계속한다.

복귀 메시지: “output/260912/rev/260912_04_info_ab50_q1_independent_ruling.md를 읽고 해시·판정 범위를 확인하라. Q1은 revise-required이며 B1–B3와 호출부·source-contract를 한 후보로 보완하라. BF1 명세를 다시 만들지 말고 기존 작성 WIP NEXT에서 재개하라. 사용자 정책키·정확한 패치 승인 전 정본 반영·배포는 금지한다.”

## history

- 2026-09-12: 사용자 모델 선택 확인을 명시 근거로 삼아 Codex/OMX가 독립 판정 수행. Q1 revise-required(B1–B3), Q2 정책 의미 approve/적용 blocked, R3 최소 보완 범위 approve. 기존15/11 재현 및 새 경계303케이스와 개별 최소 수리 검증. 후보·보호 기준·제품 무수정. 전체 배포 미완료.

