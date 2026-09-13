---
title: 정보 A/B50 Q1 수정 후보 독립 재판정
created: 2026-09-12
author: Codex/OMX
responsibility: 독립 재판정; rev-arbiter 책임 수행, Claude Code 역할 신분 아님
model: gpt-6-astra
reasoning_depth: medium
model_evidence: 현재 대화에서 사용자가 medium 및 gpt-6-astra 실행을 확인
host_model_verified: false
independence: 작성에 참여하지 않은 별도 컨텍스트; 인계 후 허용 입력 검토와 직접 재실행
grade: binding
verdict: approve
approval_scope: B1-B3 수정 코드와 호출부·입력 패키지의 후보 적합성에 한정
operational_application: blocked
release: blocked
---

# §0 판정 요약표

| unit | verdict | grade | evidence | measured | closure | note |
|---|---|---|---|---|---|---|
| Q1 수정 후보 B1–B3 | approve | binding | §1-A/B/C 재실행; repaired_candidate.py:101–114, 211–218, 475–536, 629–638 | yes | 원후보 결함 302/303 → 수정본 잔여 0/303; 상태 0/120, 분포 0/180, 종료 0/3; 기존 0/15·gate0 미검출 0/11 | B1–B3 closed. 정확한 후보 diff의 감사키만 성립; 정본 즉시 적용 불가 |
| Q2 정책키·운영 적용 | insufficient-evidence | binding | source_evidence.json:policy_key; 260911_06 §3; 260912_04 §2 Q2; §1-A/C | yes | 입력 상태 unresolved 60/60; policy_key=null; 운영 공급 파일 없음. 운영 폐쇄 미성립 | 기존 정책 의미 approve 유지. 모델·깊이 확인은 정책키가 아니다 |
| R3 호출부·입력 준비 | approve | binding | §1-A/C; assurance.patch; source_contract.json·source_evidence.json | yes | CLI 15/15·호출부 3/3 기대 일치; 원천 파일 120/120·유닛 60/60 hash/ID/locator 일치; 차집합·중복 0 | 후보 준비 완료에 한정. 인쇄ID·적격성·정식 통계 입력 승인은 미완료 |

**결론: 수정 후보 재판정 approve, 신규 구속 수정 0건. 전체 운영 적용·배포는 ▲ blocked.**
이 판정은 코드의 모든 가능한 입력이나 A/B 문항 품질에 대한 무제한 승인이 아니다.
닫는 대상은 원판정04의 B1–B3와 R3의 후보 준비 요구다. 원천 적격성·정식 모집단·Q2 사용자키·Q3·문항 검증 잔여를 닫지 않는다.
과거 BF1 명세 완결성은 선행07의 closed를 유지하며 새 명세 라운드를 요구하지 않는다.

# §1 독립 재검증

## 실행·권한·입력 경계

- 실제 수행자: Codex/OMX, 현재 독립 세션 본체 직접 실행. 팀/서브에이전트 발주·외부 모델 호출 없음.
- 모델 및 깊이는 사용자의 “medium”, Astra 실행 여부 질문에 대한 “맞어”를 근거로 기록한다. 실행 프롬프트07이 허용한 사용자 확인이며 **호스트 attestation이나 서버 라우팅 검증으로 표시하지 않는다**.
- 이 세션은 수정 후보를 작성하지 않았다. 시작 입력은 인계와 독립 실행 프롬프트이며, 인계 후 작성자 결론을 허용 입력으로 읽었다. 본 작업은 코드 재판정이지 답·해설이 차단된 문항 맹목 풀이가 아니다. 파일 접근 격리는 주장하지 않는다.
- 책임 규약: docs/ASTRA_EXECUTION_POLICY.md, docs/SESSION_HANDOFF_GUIDE.md, analysis/REV_GUIDE.md §5·§6-d 및 .claude/agents/rev-arbiter.md.
- 직접 읽은 범위는 아래 표의 마지막 열로 구분한다. 규약 전문 전체를 새로 감사했다고 하지 않는다. 과거 원판정의 긴 실행 로그·간접 링크된 문항은 이번 검토의 새 증거로 삼지 않는다.
- 원천 60유닛 transcript/meta는 바이트 동결·exam_code 메타 및 기존 측정기 기계 실행으로만 소비했다. 이미지·인쇄ID·정답·적격성 내용은 판정하지 않았다. manifest에 포함된 과학 문항 파일은 hash만 대조했으며 그 내용을 읽거나 평가하지 않았다.
- 쓰기: 본 판정문, 전용 WIP analysis/wip/rev-arbiter_260912_info_ab50_q1_repaired.md, REV_LOG 한 행. 지정 verify.py가 허용된 validation.json을 갱신했다. 동결 결과 JSON·후보·원판정·보호 기준·제품·작성자 WIP는 무수정이다.
- 잔여 사용량 수치 미노출. 수치를 추정하거나 발주하지 않았고 직접 이 1묶음만 수행했다. 현재 자원 고갈 경고는 없었다.
- 사전 Git 조회의 사용자 전역 ignore 접근 거부 경고는 시험 결과와 별도로 보존한다. 최종 표적 diff 검사에서는 exit0·stdout/stderr 빈 출력이었다.
- 자체 추가 검증 출력의 첫 시도는 Windows cp1252가 한글 결과 JSON을 출력하지 못해 UnicodeEncodeError/exit1이었다. 후보 실패가 아닌 보고 출력 경로 문제로, ensure_ascii=True로 출력만 바꾼 동일 검증을 1회 재실행해 exit0을 얻었다. 이것을 새 판정 라운드나 원시험 실패 은폐로 처리하지 않는다.

## A. 입력 동결·출처 대조

manifest 직접 파일 **45개 전부** bytes/SHA256 일치. manifest 자체는 8954 B / 1e7c9a44c017b6ecc158689e504563b0bfa96f19495b9568c18c5eccb12ff3f3.
원천04의 표에서 기대 집합과 파일 해시를 새로 파싱하고, 현재 EX 디렉터리/contract/sidecar를 양방향 대조했다.
원천 **60유닛/120파일** 각각의 bytes/SHA256 및 sidecar의 원천 경로·snapshot locator가 일치했다.
printed_id_coverage의 expected/observed/duplicates/missing/extra는 전 유닛 null이며 status=blocked이다.
이 null은 빈 성공 집합이 아니다. 인쇄 문항 기준 검증 완료 수를 60이나 1148로 만들어 쓰지 않는다.

| path | bytes | SHA256 | 실제 읽기·검사 |
|---|---:|---|---|
| .claude/agents/rev-arbiter.md | 9239 | c7168c5eca9c56d6150044ca8b0f5a28526d6930048da74e8a059068b4eeb283 | 관련 규약·결정·구현 절 읽기 |
| AGENTS.md | 28450 | e517756f2ceaa1cc9ff947465ad8666f2038796af53178da09dee07b7ef9694f | 관련 규약·결정·구현 절 읽기 |
| analysis/catalog/DIFFICULTY_RUBRIC.md | 20921 | 07dab5d38c8da48a22ca01d2f4c2b75d71fdd421a6da5ad3fcdd1a3b81b1ad99 | 바이트 동결만; 내용 판정 제외 |
| analysis/REV_GUIDE.md | 49313 | 62641c9f517bb4b4b2aa1b7ab489f46b2753e375c19d0ee0f40d6be25cdee1fe | 관련 규약·결정·구현 절 읽기 |
| CLAUDE.md | 46198 | d01a29a7b00e3fcd226e6c1cee602dda693ed5a80d5bedb29995908581748841 | 관련 규약·결정·구현 절 읽기 |
| docs/ASTRA_EXECUTION_POLICY.md | 3267 | 40424dd0e82eb36204b61890be8a44cf9f0cd0d95300f217ac86c8366199833b | 관련 규약·결정·구현 절 읽기 |
| docs/DATA_STANDARD.md | 27062 | 315c621ba02466561088e1e6d1276218311569218d52caa39e1e9faad2ee35b5 | 관련 규약·결정·구현 절 읽기 |
| docs/SESSION_HANDOFF_GUIDE.md | 4468 | ca5abfb7ea550cb0e13379067a554b2a6ba0c61364e10f770b7cc5d145600312 | 관련 규약·결정·구현 절 읽기 |
| output/260911/rev/260911_03_info_ab50_ruler_ruling.md | 68935 | ff129cc5ce45487671ba1f2626237950dccb3f2d57828729906c5dcb66edb8b1 | 관련 규약·결정·구현 절 읽기 |
| output/260911/rev/260911_04_info_ab50_repair_spec.md | 15649 | 8ee9a46ecbd57ae9826bdf1c8f1b7a93939fa4ce500645421b0e86d309b64249 | 관련 규약·결정·구현 절 읽기 |
| output/260911/rev/260911_05_info_ab50_state_contract_ruling.md | 9008 | e390779e99dbf6b066a03f03a5b073af851ba7e382808ebd5f3c797adb214d95 | 관련 규약·결정·구현 절 읽기 |
| output/260911/rev/260911_06_info_ab50_state_contract_spec.md | 8389 | 93f75d1a4c0fc6af7df62dbf7e4b3799a62fa5e8ed74b0cb9cc6d87caf7aca22 | 관련 규약·결정·구현 절 읽기 |
| output/260911/rev/260911_07_info_ab50_bf1_completeness_ruling.md | 13329 | 3d87d3bbb58e93c0c260c12083ce0e938711b3858c0a2bb3f6608170225c4265 | 관련 규약·결정·구현 절 읽기 |
| output/260912/rev/260912_01_info_ab50_measure_raw.txt | 76913 | d5544cfbbc003bdfcebae8587833b2f841c32464993df237f3a4eca445db1859 | 기계 읽기·재실행 대조 |
| output/260912/rev/260912_01_info_ab50_q1_integrated.patch | 8398 | 1cbed11e5c5841585736351b940f827d67c15f7c4f730a893b81e78eefd9b614 | diff 대조 |
| output/260912/rev/260912_01_info_ab50_q1_integrated_candidate.py | 27749 | cdaf9e1d1670e3ffb21846554c39a5e65bc9b7e5e4da424225480d1e8f48b7fb | 코드/AST·기계 실행 또는 정적검사 |
| output/260912/rev/260912_01_info_ab50_q1_integration_result.json | 4801 | e28cf9dd0aab19410b5ca46af083f6da9b2a1cdf52b6a6e0390921bbb34a9fd0 | 기계 읽기·재실행 대조 |
| output/260912/rev/260912_01_info_ab50_q1_integration_test.py | 6192 | d10efb5cf5a552dbaf13c5f00101b09c1ca1b8bfa7cf052e739d4aac36c43892 | 코드/AST·기계 실행 또는 정적검사 |
| output/260912/rev/260912_01_science_blind_pilot.md | 3909 | 061528dd01fa1c8a7aed2abeb30076dbe383071c864d4c72c1ffd13b02e0df85 | 바이트 동결만; 내용 판정 제외 |
| output/260912/rev/260912_01_science_question_baseline_cd097a46.md | 21271 | cd097a46b0b8da5ba724a0824d0fd07cd1473eb5f4cf6e508ee15d2f404ef17e | 바이트 동결만; 내용 판정 제외 |
| output/260912/rev/260912_02_info_ab50_q1_review_package.md | 4913 | 1399b0711166ed455d612197567680c631e96e0800cd2e84df3ba1031d8f6885 | 바이트 동결만; 내용 판정 제외 |
| output/260912/rev/260912_02_science_blind_middle.md | 2891 | 8e76627e95c293c721f7e2bd1ccfd3af4e25edb9f0f3b6b80f2e74c8f62828df | 바이트 동결만; 내용 판정 제외 |
| output/260912/rev/260912_03_info_ab50_q1_session_prompt.md | 5597 | f2827935a2bafba30077a892a9d1ec7c2d84c70d703d3b83da41f4ee0ca6e1a6 | 바이트 동결만; 내용 판정 제외 |
| output/260912/rev/260912_03_science_carry_forward.json | 1230 | 400a734ef3e07da88c85f7366d3a1a584fae9c49290ca665f14be0a8be196f2a | 바이트 동결만; 내용 판정 제외 |
| output/260912/rev/260912_04_info_ab50_q1_independent_ruling.md | 44870 | 1ec05434a586f4c372d6409a79de62408f0ff9c3f77e7bbadadf471cc5410c56 | 관련 규약·결정·구현 절 읽기 |
| output/260912/rev/260912_05_info_ab50_q1_assurance.patch | 437 | ff0a66ea9d904c3664383f0740df349daea388451475cffc3763f91ae3b93338 | diff 대조 |
| output/260912/rev/260912_05_info_ab50_q1_assurance_candidate.py | 12036 | 2868482fa6fbb5c6094a7e112c988f5ddf493a59c30a78289e66c6f26f65471a | 코드/AST·기계 실행 또는 정적검사 |
| output/260912/rev/260912_05_info_ab50_q1_baseline_result.json | 82245 | 140ee466d43cb46b70b57de05df2cdc664902765807a91795dec05256c6b04ec | 기계 읽기·재실행 대조 |
| output/260912/rev/260912_05_info_ab50_q1_build.py | 8547 | 9ac7f74234b36077d71a8a5ddbd3e23a5e179e1f70ec8911a44824899b154511 | 코드/AST·기계 실행 또는 정적검사 |
| output/260912/rev/260912_05_info_ab50_q1_caller_result.json | 100211 | 7b751f3f41ce6a892fa70f6ccf00d9fe2997183929eb5acefaa325c0fed8d670 | 기계 읽기·재실행 대조 |
| output/260912/rev/260912_05_info_ab50_q1_caller_test.py | 7128 | 40fad8d685b5bc7acaa60b997e1003430017a14d75dbc37199d7d0d897d1c4b9 | 코드/AST·기계 실행 또는 정적검사 |
| output/260912/rev/260912_05_info_ab50_q1_integrated.patch | 11007 | e57e1069b76c6deefffa07081b008aee1db183d0031560aba77eefc4224ddda9 | diff 대조 |
| output/260912/rev/260912_05_info_ab50_q1_regression_result.json | 73239 | c2eedf01306bb6b4b505d6c6213cbf1835b7356b4c532c624c10fe6974566750 | 기계 읽기·재실행 대조 |
| output/260912/rev/260912_05_info_ab50_q1_regression_test.py | 8574 | 951e24af62749fca897be1a3c1d6c61c380854bff180fdb61acb221a693bcef1 | 코드/AST·기계 실행 또는 정적검사 |
| output/260912/rev/260912_05_info_ab50_q1_repair_delta.patch | 6366 | e1ee4855ea10434a9575c55b3017a90fe1e5ecf0b3bea0e52e1854936f228d90 | diff 대조 |
| output/260912/rev/260912_05_info_ab50_q1_repaired_candidate.py | 29916 | 12a2f410ec7fcff3b604480dd96c23248e90962a620c1e3bc4350c8e0fd3a4ae | 코드/AST·기계 실행 또는 정적검사 |
| output/260912/rev/260912_05_info_ab50_q1_source_contract.json | 21025 | b32854a557571d3e30faff826550a535b78c9b2fb4de489e50ee4a6a361d1e56 | 기계 읽기·재실행 대조 |
| output/260912/rev/260912_05_info_ab50_q1_source_evidence.json | 78792 | e804333b3b3bd85e2cb1f39ed151aa8ee042eb017c2e45e140eb6733d02fe551 | 기계 읽기·재실행 대조 |
| output/260912/rev/260912_05_info_ab50_q1_verify.py | 2604 | 0fd0ca6545c0fbbb26c656d33370de0463c28a12e977b07ca650dd1b6d26adc2 | 코드/AST·기계 실행 또는 정적검사 |
| output/260912/rev/260912_06_info_ab50_q1_repaired_review_package.md | 8558 | 30e9aa6d5341e52f16c2996022ac0f29e4a785ad8f8f9e889363bbd33f14feea | 관련 규약·결정·구현 절 읽기 |
| output/260912/rev/260912_07_info_ab50_q1_repaired_session_prompt.md | 4021 | 162e367b8ee82a0388561b60db33e195e5f5a01f6ad207bd5c4eaf5d8c8565c9 | 관련 규약·결정·구현 절 읽기 |
| tools/check_assurance_contract.py | 12243 | 85db02a7bd8b191a18bf0b88ec0b4d9ef3b69c1d08342823d9e50dfeb8d21223 | 관련 규약·결정·구현 절 읽기 |
| tools/measure_score_bands.py | 21969 | 0cf91284e2c1f7b1be4d94a09d641996614d65fa88fdf8444b9f9daa3958fe24 | 관련 규약·결정·구현 절 읽기 |
| tools/regen_rubric_values.py | 21594 | 599fbdef489fa1475dfba5dad76c3cd7eb0b133150359902c1b0590aa9ae11d1 | 코드/AST·기계 실행 또는 정적검사 |
| tools/textpatch.py | 12170 | eaa4e9b8ff67b87f07a214c37aa5cddf8f027756e977ddf93828e71bacf1cb48 | 관련 규약·결정·구현 절 읽기 |

원천 파일별 해시는 동결된 source_evidence.json과 아래 재현 A에서 직접 대조한다. 본 판정은 동일 120행을 별도 기준으로 수기 복제하지 않는다.
원천 유닛 식별자 실측(동일 집합에 대한 directories/sidecar/dispositions 각각의 출력):
```json
{
  "directories": {
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
    "missing": [],
    "extra": []
  },
  "sidecar": {
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
    "missing": [],
    "extra": []
  },
  "dispositions": {
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
    "missing": [],
    "extra": []
  }
}
```

재현 A — cwd=C:\dev\study, stdout은 JSON; 실패 시 assert/exit 비0, 성공 시 mismatch 0. 파일 쓰기 없음:
```python
import collections, hashlib, json
from pathlib import Path
P = Path("output/260912/rev")
prefix = "260912_05_info_ab50_q1_"
def stamp(path):
    b = path.read_bytes()
    return dict(bytes=len(b), sha256=hashlib.sha256(b).hexdigest())
manifest = json.loads((P / (prefix + "manifest.json")).read_text(encoding="utf-8"))
for row in manifest["files"]:
    assert stamp(Path(row["path"])) == {k: row[k] for k in ("bytes", "sha256")}, row["path"]
spec = Path("output/260911/rev/260911_04_info_ab50_repair_spec.md")
snapshot, locators = {}, {}
for number, line in enumerate(spec.read_text(encoding="utf-8").splitlines(), 1):
    if line.startswith("| EX-"):
        uid, tb, th, mb, mh = [x.strip() for x in line.strip("|").split("|")]
        assert uid not in snapshot
        snapshot[uid] = {"transcript.md": dict(bytes=int(tb), sha256=th),
                         "meta.yml": dict(bytes=int(mb), sha256=mh)}
        locators[uid] = "line " + str(number)
contract = json.loads((P / (prefix + "source_contract.json")).read_text(encoding="utf-8"))
sidecar = json.loads((P / (prefix + "source_evidence.json")).read_text(encoding="utf-8"))
assert contract["snapshot"] == snapshot
expected = sorted(snapshot)
for label, values in [("directories", [p.name for p in Path("corpus").glob("EX-*") if p.is_dir()]),
                      ("dispositions", list(contract["dispositions"])), ("sidecar", list(sidecar["units"]))]:
    duplicates = sorted(k for k, n in collections.Counter(values).items() if n > 1)
    result = dict(expected=expected, observed=sorted(values), duplicates=duplicates,
                  missing=sorted(set(expected)-set(values)), extra=sorted(set(values)-set(expected)))
    assert not any(result[k] for k in ("duplicates", "missing", "extra"))
    print(json.dumps({label: result}))
for uid, files in snapshot.items():
    item = sidecar["units"][uid]
    assert item["disposition"] == contract["dispositions"][uid] == "unresolved"
    assert item["printed_id_coverage"] == dict(expected=None, observed=None, duplicates=None, missing=None, extra=None, status="blocked")
    for name, expected_file in files.items():
        path = Path("corpus") / uid / name
        ref = item["source_files"][name]
        assert stamp(path) == expected_file == {k: ref[k] for k in ("bytes", "sha256")}
        assert Path(ref["path"]) == path and ref["snapshot_locator"] == locators[uid]
print(json.dumps(dict(manifest_files=len(manifest["files"]), source_units=len(snapshot),
                      source_files=sum(map(len, snapshot.values())), mismatches=0,
                      policy_key=sidecar["policy_key"], supply_exists=Path(sidecar["proposed_supply_path"]).exists())))
```

## B. 지정 시험 직접 재실행

```powershell
python output/260912/rev/260912_05_info_ab50_q1_verify.py
python output/260912/rev/260912_05_info_ab50_q1_regression_test.py --baseline --no-save
```

첫 명령 exit0:
```json
{"commands": 2, "exit": 0, "static_files": 6, "exact_patches": true, "unexpected_harness_warnings": 0, "manifest_checked": true}
```

실제 하위 2명령은 regression_test.py --no-save와 caller_test.py --no-save이고 각각 exit0, stderr 빈 문자열.
수정 303건 실패0·정상 통제 true·기존 15건, CLI15/호출부3 실패0이다.
원후보 명령은 exit0이며 **303건 중 302건 결함 재현**이 기대 결과다. baseline exit0을 후보 정상으로 읽지 않는다.
상태120·분포180·종료2에서 원결함이 재현되고 정상 clean 종료1건은 정상 통제다.

수정 회귀 ID는 원천04에서 재유도한 60유닛에 상태 2종·분포 변이 3종 및 종료 3경로를 붙인 집합이다.
기대/관측 각303, 중복/기대중복/누락/추가 모두 빈 집합. 행 수만으로 통과시키지 않고 아래 전수 목록으로 대조했다.
baseline도 동일 ID 집합을 실행했다.
```json
{
  "expected": [
    "distribution/delete/EX-english-20241F",
    "distribution/delete/EX-english-20241M",
    "distribution/delete/EX-english-20242F",
    "distribution/delete/EX-english-20242M",
    "distribution/delete/EX-english-20251F",
    "distribution/delete/EX-english-20251M",
    "distribution/delete/EX-english-20252F",
    "distribution/delete/EX-english-20252M",
    "distribution/delete/EX-english-20261F",
    "distribution/delete/EX-english-20261M",
    "distribution/delete/EX-history-20241F",
    "distribution/delete/EX-history-20241M",
    "distribution/delete/EX-history-20242F",
    "distribution/delete/EX-history-20242M",
    "distribution/delete/EX-history-20251F",
    "distribution/delete/EX-history-20251M",
    "distribution/delete/EX-history-20252F",
    "distribution/delete/EX-history-20252M",
    "distribution/delete/EX-history-20261F",
    "distribution/delete/EX-history-20261M",
    "distribution/delete/EX-info-20252F",
    "distribution/delete/EX-info-20252M",
    "distribution/delete/EX-korean-20241F",
    "distribution/delete/EX-korean-20241M",
    "distribution/delete/EX-korean-20242F",
    "distribution/delete/EX-korean-20242M",
    "distribution/delete/EX-korean-20251F",
    "distribution/delete/EX-korean-20251M",
    "distribution/delete/EX-korean-20252F",
    "distribution/delete/EX-korean-20252M",
    "distribution/delete/EX-math1-20241F",
    "distribution/delete/EX-math1-20241M",
    "distribution/delete/EX-math1-20242F",
    "distribution/delete/EX-math1-20242M",
    "distribution/delete/EX-math1-20251F",
    "distribution/delete/EX-math1-20251M",
    "distribution/delete/EX-math1-20261F",
    "distribution/delete/EX-math1-20261M",
    "distribution/delete/EX-math2-20252F",
    "distribution/delete/EX-math2-20252M",
    "distribution/delete/EX-science-20241F",
    "distribution/delete/EX-science-20241M",
    "distribution/delete/EX-science-20242F",
    "distribution/delete/EX-science-20242M",
    "distribution/delete/EX-science-20251F",
    "distribution/delete/EX-science-20251M",
    "distribution/delete/EX-science-20252F",
    "distribution/delete/EX-science-20252M",
    "distribution/delete/EX-science-20261F",
    "distribution/delete/EX-science-20261M",
    "distribution/delete/EX-social-20241F",
    "distribution/delete/EX-social-20241M",
    "distribution/delete/EX-social-20242F",
    "distribution/delete/EX-social-20242M",
    "distribution/delete/EX-social-20251F",
    "distribution/delete/EX-social-20251M",
    "distribution/delete/EX-social-20252F",
    "distribution/delete/EX-social-20252M",
    "distribution/delete/EX-social-20261F",
    "distribution/delete/EX-social-20261M",
    "distribution/duplicate/EX-english-20241F",
    "distribution/duplicate/EX-english-20241M",
    "distribution/duplicate/EX-english-20242F",
    "distribution/duplicate/EX-english-20242M",
    "distribution/duplicate/EX-english-20251F",
    "distribution/duplicate/EX-english-20251M",
    "distribution/duplicate/EX-english-20252F",
    "distribution/duplicate/EX-english-20252M",
    "distribution/duplicate/EX-english-20261F",
    "distribution/duplicate/EX-english-20261M",
    "distribution/duplicate/EX-history-20241F",
    "distribution/duplicate/EX-history-20241M",
    "distribution/duplicate/EX-history-20242F",
    "distribution/duplicate/EX-history-20242M",
    "distribution/duplicate/EX-history-20251F",
    "distribution/duplicate/EX-history-20251M",
    "distribution/duplicate/EX-history-20252F",
    "distribution/duplicate/EX-history-20252M",
    "distribution/duplicate/EX-history-20261F",
    "distribution/duplicate/EX-history-20261M",
    "distribution/duplicate/EX-info-20252F",
    "distribution/duplicate/EX-info-20252M",
    "distribution/duplicate/EX-korean-20241F",
    "distribution/duplicate/EX-korean-20241M",
    "distribution/duplicate/EX-korean-20242F",
    "distribution/duplicate/EX-korean-20242M",
    "distribution/duplicate/EX-korean-20251F",
    "distribution/duplicate/EX-korean-20251M",
    "distribution/duplicate/EX-korean-20252F",
    "distribution/duplicate/EX-korean-20252M",
    "distribution/duplicate/EX-math1-20241F",
    "distribution/duplicate/EX-math1-20241M",
    "distribution/duplicate/EX-math1-20242F",
    "distribution/duplicate/EX-math1-20242M",
    "distribution/duplicate/EX-math1-20251F",
    "distribution/duplicate/EX-math1-20251M",
    "distribution/duplicate/EX-math1-20261F",
    "distribution/duplicate/EX-math1-20261M",
    "distribution/duplicate/EX-math2-20252F",
    "distribution/duplicate/EX-math2-20252M",
    "distribution/duplicate/EX-science-20241F",
    "distribution/duplicate/EX-science-20241M",
    "distribution/duplicate/EX-science-20242F",
    "distribution/duplicate/EX-science-20242M",
    "distribution/duplicate/EX-science-20251F",
    "distribution/duplicate/EX-science-20251M",
    "distribution/duplicate/EX-science-20252F",
    "distribution/duplicate/EX-science-20252M",
    "distribution/duplicate/EX-science-20261F",
    "distribution/duplicate/EX-science-20261M",
    "distribution/duplicate/EX-social-20241F",
    "distribution/duplicate/EX-social-20241M",
    "distribution/duplicate/EX-social-20242F",
    "distribution/duplicate/EX-social-20242M",
    "distribution/duplicate/EX-social-20251F",
    "distribution/duplicate/EX-social-20251M",
    "distribution/duplicate/EX-social-20252F",
    "distribution/duplicate/EX-social-20252M",
    "distribution/duplicate/EX-social-20261F",
    "distribution/duplicate/EX-social-20261M",
    "distribution/same_count_replace/EX-english-20241F",
    "distribution/same_count_replace/EX-english-20241M",
    "distribution/same_count_replace/EX-english-20242F",
    "distribution/same_count_replace/EX-english-20242M",
    "distribution/same_count_replace/EX-english-20251F",
    "distribution/same_count_replace/EX-english-20251M",
    "distribution/same_count_replace/EX-english-20252F",
    "distribution/same_count_replace/EX-english-20252M",
    "distribution/same_count_replace/EX-english-20261F",
    "distribution/same_count_replace/EX-english-20261M",
    "distribution/same_count_replace/EX-history-20241F",
    "distribution/same_count_replace/EX-history-20241M",
    "distribution/same_count_replace/EX-history-20242F",
    "distribution/same_count_replace/EX-history-20242M",
    "distribution/same_count_replace/EX-history-20251F",
    "distribution/same_count_replace/EX-history-20251M",
    "distribution/same_count_replace/EX-history-20252F",
    "distribution/same_count_replace/EX-history-20252M",
    "distribution/same_count_replace/EX-history-20261F",
    "distribution/same_count_replace/EX-history-20261M",
    "distribution/same_count_replace/EX-info-20252F",
    "distribution/same_count_replace/EX-info-20252M",
    "distribution/same_count_replace/EX-korean-20241F",
    "distribution/same_count_replace/EX-korean-20241M",
    "distribution/same_count_replace/EX-korean-20242F",
    "distribution/same_count_replace/EX-korean-20242M",
    "distribution/same_count_replace/EX-korean-20251F",
    "distribution/same_count_replace/EX-korean-20251M",
    "distribution/same_count_replace/EX-korean-20252F",
    "distribution/same_count_replace/EX-korean-20252M",
    "distribution/same_count_replace/EX-math1-20241F",
    "distribution/same_count_replace/EX-math1-20241M",
    "distribution/same_count_replace/EX-math1-20242F",
    "distribution/same_count_replace/EX-math1-20242M",
    "distribution/same_count_replace/EX-math1-20251F",
    "distribution/same_count_replace/EX-math1-20251M",
    "distribution/same_count_replace/EX-math1-20261F",
    "distribution/same_count_replace/EX-math1-20261M",
    "distribution/same_count_replace/EX-math2-20252F",
    "distribution/same_count_replace/EX-math2-20252M",
    "distribution/same_count_replace/EX-science-20241F",
    "distribution/same_count_replace/EX-science-20241M",
    "distribution/same_count_replace/EX-science-20242F",
    "distribution/same_count_replace/EX-science-20242M",
    "distribution/same_count_replace/EX-science-20251F",
    "distribution/same_count_replace/EX-science-20251M",
    "distribution/same_count_replace/EX-science-20252F",
    "distribution/same_count_replace/EX-science-20252M",
    "distribution/same_count_replace/EX-science-20261F",
    "distribution/same_count_replace/EX-science-20261M",
    "distribution/same_count_replace/EX-social-20241F",
    "distribution/same_count_replace/EX-social-20241M",
    "distribution/same_count_replace/EX-social-20242F",
    "distribution/same_count_replace/EX-social-20242M",
    "distribution/same_count_replace/EX-social-20251F",
    "distribution/same_count_replace/EX-social-20251M",
    "distribution/same_count_replace/EX-social-20252F",
    "distribution/same_count_replace/EX-social-20252M",
    "distribution/same_count_replace/EX-social-20261F",
    "distribution/same_count_replace/EX-social-20261M",
    "state/partial/EX-english-20241F",
    "state/partial/EX-english-20241M",
    "state/partial/EX-english-20242F",
    "state/partial/EX-english-20242M",
    "state/partial/EX-english-20251F",
    "state/partial/EX-english-20251M",
    "state/partial/EX-english-20252F",
    "state/partial/EX-english-20252M",
    "state/partial/EX-english-20261F",
    "state/partial/EX-english-20261M",
    "state/partial/EX-history-20241F",
    "state/partial/EX-history-20241M",
    "state/partial/EX-history-20242F",
    "state/partial/EX-history-20242M",
    "state/partial/EX-history-20251F",
    "state/partial/EX-history-20251M",
    "state/partial/EX-history-20252F",
    "state/partial/EX-history-20252M",
    "state/partial/EX-history-20261F",
    "state/partial/EX-history-20261M",
    "state/partial/EX-info-20252F",
    "state/partial/EX-info-20252M",
    "state/partial/EX-korean-20241F",
    "state/partial/EX-korean-20241M",
    "state/partial/EX-korean-20242F",
    "state/partial/EX-korean-20242M",
    "state/partial/EX-korean-20251F",
    "state/partial/EX-korean-20251M",
    "state/partial/EX-korean-20252F",
    "state/partial/EX-korean-20252M",
    "state/partial/EX-math1-20241F",
    "state/partial/EX-math1-20241M",
    "state/partial/EX-math1-20242F",
    "state/partial/EX-math1-20242M",
    "state/partial/EX-math1-20251F",
    "state/partial/EX-math1-20251M",
    "state/partial/EX-math1-20261F",
    "state/partial/EX-math1-20261M",
    "state/partial/EX-math2-20252F",
    "state/partial/EX-math2-20252M",
    "state/partial/EX-science-20241F",
    "state/partial/EX-science-20241M",
    "state/partial/EX-science-20242F",
    "state/partial/EX-science-20242M",
    "state/partial/EX-science-20251F",
    "state/partial/EX-science-20251M",
    "state/partial/EX-science-20252F",
    "state/partial/EX-science-20252M",
    "state/partial/EX-science-20261F",
    "state/partial/EX-science-20261M",
    "state/partial/EX-social-20241F",
    "state/partial/EX-social-20241M",
    "state/partial/EX-social-20242F",
    "state/partial/EX-social-20242M",
    "state/partial/EX-social-20251F",
    "state/partial/EX-social-20251M",
    "state/partial/EX-social-20252F",
    "state/partial/EX-social-20252M",
    "state/partial/EX-social-20261F",
    "state/partial/EX-social-20261M",
    "state/unresolved/EX-english-20241F",
    "state/unresolved/EX-english-20241M",
    "state/unresolved/EX-english-20242F",
    "state/unresolved/EX-english-20242M",
    "state/unresolved/EX-english-20251F",
    "state/unresolved/EX-english-20251M",
    "state/unresolved/EX-english-20252F",
    "state/unresolved/EX-english-20252M",
    "state/unresolved/EX-english-20261F",
    "state/unresolved/EX-english-20261M",
    "state/unresolved/EX-history-20241F",
    "state/unresolved/EX-history-20241M",
    "state/unresolved/EX-history-20242F",
    "state/unresolved/EX-history-20242M",
    "state/unresolved/EX-history-20251F",
    "state/unresolved/EX-history-20251M",
    "state/unresolved/EX-history-20252F",
    "state/unresolved/EX-history-20252M",
    "state/unresolved/EX-history-20261F",
    "state/unresolved/EX-history-20261M",
    "state/unresolved/EX-info-20252F",
    "state/unresolved/EX-info-20252M",
    "state/unresolved/EX-korean-20241F",
    "state/unresolved/EX-korean-20241M",
    "state/unresolved/EX-korean-20242F",
    "state/unresolved/EX-korean-20242M",
    "state/unresolved/EX-korean-20251F",
    "state/unresolved/EX-korean-20251M",
    "state/unresolved/EX-korean-20252F",
    "state/unresolved/EX-korean-20252M",
    "state/unresolved/EX-math1-20241F",
    "state/unresolved/EX-math1-20241M",
    "state/unresolved/EX-math1-20242F",
    "state/unresolved/EX-math1-20242M",
    "state/unresolved/EX-math1-20251F",
    "state/unresolved/EX-math1-20251M",
    "state/unresolved/EX-math1-20261F",
    "state/unresolved/EX-math1-20261M",
    "state/unresolved/EX-math2-20252F",
    "state/unresolved/EX-math2-20252M",
    "state/unresolved/EX-science-20241F",
    "state/unresolved/EX-science-20241M",
    "state/unresolved/EX-science-20242F",
    "state/unresolved/EX-science-20242M",
    "state/unresolved/EX-science-20251F",
    "state/unresolved/EX-science-20251M",
    "state/unresolved/EX-science-20252F",
    "state/unresolved/EX-science-20252M",
    "state/unresolved/EX-science-20261F",
    "state/unresolved/EX-science-20261M",
    "state/unresolved/EX-social-20241F",
    "state/unresolved/EX-social-20241M",
    "state/unresolved/EX-social-20242F",
    "state/unresolved/EX-social-20242M",
    "state/unresolved/EX-social-20251F",
    "state/unresolved/EX-social-20251M",
    "state/unresolved/EX-social-20252F",
    "state/unresolved/EX-social-20252M",
    "state/unresolved/EX-social-20261F",
    "state/unresolved/EX-social-20261M",
    "terminal/local_fixture_failed",
    "terminal/ruler_stale",
    "terminal/synthetic_clean"
  ],
  "observed": [
    "distribution/delete/EX-english-20241F",
    "distribution/delete/EX-english-20241M",
    "distribution/delete/EX-english-20242F",
    "distribution/delete/EX-english-20242M",
    "distribution/delete/EX-english-20251F",
    "distribution/delete/EX-english-20251M",
    "distribution/delete/EX-english-20252F",
    "distribution/delete/EX-english-20252M",
    "distribution/delete/EX-english-20261F",
    "distribution/delete/EX-english-20261M",
    "distribution/delete/EX-history-20241F",
    "distribution/delete/EX-history-20241M",
    "distribution/delete/EX-history-20242F",
    "distribution/delete/EX-history-20242M",
    "distribution/delete/EX-history-20251F",
    "distribution/delete/EX-history-20251M",
    "distribution/delete/EX-history-20252F",
    "distribution/delete/EX-history-20252M",
    "distribution/delete/EX-history-20261F",
    "distribution/delete/EX-history-20261M",
    "distribution/delete/EX-info-20252F",
    "distribution/delete/EX-info-20252M",
    "distribution/delete/EX-korean-20241F",
    "distribution/delete/EX-korean-20241M",
    "distribution/delete/EX-korean-20242F",
    "distribution/delete/EX-korean-20242M",
    "distribution/delete/EX-korean-20251F",
    "distribution/delete/EX-korean-20251M",
    "distribution/delete/EX-korean-20252F",
    "distribution/delete/EX-korean-20252M",
    "distribution/delete/EX-math1-20241F",
    "distribution/delete/EX-math1-20241M",
    "distribution/delete/EX-math1-20242F",
    "distribution/delete/EX-math1-20242M",
    "distribution/delete/EX-math1-20251F",
    "distribution/delete/EX-math1-20251M",
    "distribution/delete/EX-math1-20261F",
    "distribution/delete/EX-math1-20261M",
    "distribution/delete/EX-math2-20252F",
    "distribution/delete/EX-math2-20252M",
    "distribution/delete/EX-science-20241F",
    "distribution/delete/EX-science-20241M",
    "distribution/delete/EX-science-20242F",
    "distribution/delete/EX-science-20242M",
    "distribution/delete/EX-science-20251F",
    "distribution/delete/EX-science-20251M",
    "distribution/delete/EX-science-20252F",
    "distribution/delete/EX-science-20252M",
    "distribution/delete/EX-science-20261F",
    "distribution/delete/EX-science-20261M",
    "distribution/delete/EX-social-20241F",
    "distribution/delete/EX-social-20241M",
    "distribution/delete/EX-social-20242F",
    "distribution/delete/EX-social-20242M",
    "distribution/delete/EX-social-20251F",
    "distribution/delete/EX-social-20251M",
    "distribution/delete/EX-social-20252F",
    "distribution/delete/EX-social-20252M",
    "distribution/delete/EX-social-20261F",
    "distribution/delete/EX-social-20261M",
    "distribution/duplicate/EX-english-20241F",
    "distribution/duplicate/EX-english-20241M",
    "distribution/duplicate/EX-english-20242F",
    "distribution/duplicate/EX-english-20242M",
    "distribution/duplicate/EX-english-20251F",
    "distribution/duplicate/EX-english-20251M",
    "distribution/duplicate/EX-english-20252F",
    "distribution/duplicate/EX-english-20252M",
    "distribution/duplicate/EX-english-20261F",
    "distribution/duplicate/EX-english-20261M",
    "distribution/duplicate/EX-history-20241F",
    "distribution/duplicate/EX-history-20241M",
    "distribution/duplicate/EX-history-20242F",
    "distribution/duplicate/EX-history-20242M",
    "distribution/duplicate/EX-history-20251F",
    "distribution/duplicate/EX-history-20251M",
    "distribution/duplicate/EX-history-20252F",
    "distribution/duplicate/EX-history-20252M",
    "distribution/duplicate/EX-history-20261F",
    "distribution/duplicate/EX-history-20261M",
    "distribution/duplicate/EX-info-20252F",
    "distribution/duplicate/EX-info-20252M",
    "distribution/duplicate/EX-korean-20241F",
    "distribution/duplicate/EX-korean-20241M",
    "distribution/duplicate/EX-korean-20242F",
    "distribution/duplicate/EX-korean-20242M",
    "distribution/duplicate/EX-korean-20251F",
    "distribution/duplicate/EX-korean-20251M",
    "distribution/duplicate/EX-korean-20252F",
    "distribution/duplicate/EX-korean-20252M",
    "distribution/duplicate/EX-math1-20241F",
    "distribution/duplicate/EX-math1-20241M",
    "distribution/duplicate/EX-math1-20242F",
    "distribution/duplicate/EX-math1-20242M",
    "distribution/duplicate/EX-math1-20251F",
    "distribution/duplicate/EX-math1-20251M",
    "distribution/duplicate/EX-math1-20261F",
    "distribution/duplicate/EX-math1-20261M",
    "distribution/duplicate/EX-math2-20252F",
    "distribution/duplicate/EX-math2-20252M",
    "distribution/duplicate/EX-science-20241F",
    "distribution/duplicate/EX-science-20241M",
    "distribution/duplicate/EX-science-20242F",
    "distribution/duplicate/EX-science-20242M",
    "distribution/duplicate/EX-science-20251F",
    "distribution/duplicate/EX-science-20251M",
    "distribution/duplicate/EX-science-20252F",
    "distribution/duplicate/EX-science-20252M",
    "distribution/duplicate/EX-science-20261F",
    "distribution/duplicate/EX-science-20261M",
    "distribution/duplicate/EX-social-20241F",
    "distribution/duplicate/EX-social-20241M",
    "distribution/duplicate/EX-social-20242F",
    "distribution/duplicate/EX-social-20242M",
    "distribution/duplicate/EX-social-20251F",
    "distribution/duplicate/EX-social-20251M",
    "distribution/duplicate/EX-social-20252F",
    "distribution/duplicate/EX-social-20252M",
    "distribution/duplicate/EX-social-20261F",
    "distribution/duplicate/EX-social-20261M",
    "distribution/same_count_replace/EX-english-20241F",
    "distribution/same_count_replace/EX-english-20241M",
    "distribution/same_count_replace/EX-english-20242F",
    "distribution/same_count_replace/EX-english-20242M",
    "distribution/same_count_replace/EX-english-20251F",
    "distribution/same_count_replace/EX-english-20251M",
    "distribution/same_count_replace/EX-english-20252F",
    "distribution/same_count_replace/EX-english-20252M",
    "distribution/same_count_replace/EX-english-20261F",
    "distribution/same_count_replace/EX-english-20261M",
    "distribution/same_count_replace/EX-history-20241F",
    "distribution/same_count_replace/EX-history-20241M",
    "distribution/same_count_replace/EX-history-20242F",
    "distribution/same_count_replace/EX-history-20242M",
    "distribution/same_count_replace/EX-history-20251F",
    "distribution/same_count_replace/EX-history-20251M",
    "distribution/same_count_replace/EX-history-20252F",
    "distribution/same_count_replace/EX-history-20252M",
    "distribution/same_count_replace/EX-history-20261F",
    "distribution/same_count_replace/EX-history-20261M",
    "distribution/same_count_replace/EX-info-20252F",
    "distribution/same_count_replace/EX-info-20252M",
    "distribution/same_count_replace/EX-korean-20241F",
    "distribution/same_count_replace/EX-korean-20241M",
    "distribution/same_count_replace/EX-korean-20242F",
    "distribution/same_count_replace/EX-korean-20242M",
    "distribution/same_count_replace/EX-korean-20251F",
    "distribution/same_count_replace/EX-korean-20251M",
    "distribution/same_count_replace/EX-korean-20252F",
    "distribution/same_count_replace/EX-korean-20252M",
    "distribution/same_count_replace/EX-math1-20241F",
    "distribution/same_count_replace/EX-math1-20241M",
    "distribution/same_count_replace/EX-math1-20242F",
    "distribution/same_count_replace/EX-math1-20242M",
    "distribution/same_count_replace/EX-math1-20251F",
    "distribution/same_count_replace/EX-math1-20251M",
    "distribution/same_count_replace/EX-math1-20261F",
    "distribution/same_count_replace/EX-math1-20261M",
    "distribution/same_count_replace/EX-math2-20252F",
    "distribution/same_count_replace/EX-math2-20252M",
    "distribution/same_count_replace/EX-science-20241F",
    "distribution/same_count_replace/EX-science-20241M",
    "distribution/same_count_replace/EX-science-20242F",
    "distribution/same_count_replace/EX-science-20242M",
    "distribution/same_count_replace/EX-science-20251F",
    "distribution/same_count_replace/EX-science-20251M",
    "distribution/same_count_replace/EX-science-20252F",
    "distribution/same_count_replace/EX-science-20252M",
    "distribution/same_count_replace/EX-science-20261F",
    "distribution/same_count_replace/EX-science-20261M",
    "distribution/same_count_replace/EX-social-20241F",
    "distribution/same_count_replace/EX-social-20241M",
    "distribution/same_count_replace/EX-social-20242F",
    "distribution/same_count_replace/EX-social-20242M",
    "distribution/same_count_replace/EX-social-20251F",
    "distribution/same_count_replace/EX-social-20251M",
    "distribution/same_count_replace/EX-social-20252F",
    "distribution/same_count_replace/EX-social-20252M",
    "distribution/same_count_replace/EX-social-20261F",
    "distribution/same_count_replace/EX-social-20261M",
    "state/partial/EX-english-20241F",
    "state/partial/EX-english-20241M",
    "state/partial/EX-english-20242F",
    "state/partial/EX-english-20242M",
    "state/partial/EX-english-20251F",
    "state/partial/EX-english-20251M",
    "state/partial/EX-english-20252F",
    "state/partial/EX-english-20252M",
    "state/partial/EX-english-20261F",
    "state/partial/EX-english-20261M",
    "state/partial/EX-history-20241F",
    "state/partial/EX-history-20241M",
    "state/partial/EX-history-20242F",
    "state/partial/EX-history-20242M",
    "state/partial/EX-history-20251F",
    "state/partial/EX-history-20251M",
    "state/partial/EX-history-20252F",
    "state/partial/EX-history-20252M",
    "state/partial/EX-history-20261F",
    "state/partial/EX-history-20261M",
    "state/partial/EX-info-20252F",
    "state/partial/EX-info-20252M",
    "state/partial/EX-korean-20241F",
    "state/partial/EX-korean-20241M",
    "state/partial/EX-korean-20242F",
    "state/partial/EX-korean-20242M",
    "state/partial/EX-korean-20251F",
    "state/partial/EX-korean-20251M",
    "state/partial/EX-korean-20252F",
    "state/partial/EX-korean-20252M",
    "state/partial/EX-math1-20241F",
    "state/partial/EX-math1-20241M",
    "state/partial/EX-math1-20242F",
    "state/partial/EX-math1-20242M",
    "state/partial/EX-math1-20251F",
    "state/partial/EX-math1-20251M",
    "state/partial/EX-math1-20261F",
    "state/partial/EX-math1-20261M",
    "state/partial/EX-math2-20252F",
    "state/partial/EX-math2-20252M",
    "state/partial/EX-science-20241F",
    "state/partial/EX-science-20241M",
    "state/partial/EX-science-20242F",
    "state/partial/EX-science-20242M",
    "state/partial/EX-science-20251F",
    "state/partial/EX-science-20251M",
    "state/partial/EX-science-20252F",
    "state/partial/EX-science-20252M",
    "state/partial/EX-science-20261F",
    "state/partial/EX-science-20261M",
    "state/partial/EX-social-20241F",
    "state/partial/EX-social-20241M",
    "state/partial/EX-social-20242F",
    "state/partial/EX-social-20242M",
    "state/partial/EX-social-20251F",
    "state/partial/EX-social-20251M",
    "state/partial/EX-social-20252F",
    "state/partial/EX-social-20252M",
    "state/partial/EX-social-20261F",
    "state/partial/EX-social-20261M",
    "state/unresolved/EX-english-20241F",
    "state/unresolved/EX-english-20241M",
    "state/unresolved/EX-english-20242F",
    "state/unresolved/EX-english-20242M",
    "state/unresolved/EX-english-20251F",
    "state/unresolved/EX-english-20251M",
    "state/unresolved/EX-english-20252F",
    "state/unresolved/EX-english-20252M",
    "state/unresolved/EX-english-20261F",
    "state/unresolved/EX-english-20261M",
    "state/unresolved/EX-history-20241F",
    "state/unresolved/EX-history-20241M",
    "state/unresolved/EX-history-20242F",
    "state/unresolved/EX-history-20242M",
    "state/unresolved/EX-history-20251F",
    "state/unresolved/EX-history-20251M",
    "state/unresolved/EX-history-20252F",
    "state/unresolved/EX-history-20252M",
    "state/unresolved/EX-history-20261F",
    "state/unresolved/EX-history-20261M",
    "state/unresolved/EX-info-20252F",
    "state/unresolved/EX-info-20252M",
    "state/unresolved/EX-korean-20241F",
    "state/unresolved/EX-korean-20241M",
    "state/unresolved/EX-korean-20242F",
    "state/unresolved/EX-korean-20242M",
    "state/unresolved/EX-korean-20251F",
    "state/unresolved/EX-korean-20251M",
    "state/unresolved/EX-korean-20252F",
    "state/unresolved/EX-korean-20252M",
    "state/unresolved/EX-math1-20241F",
    "state/unresolved/EX-math1-20241M",
    "state/unresolved/EX-math1-20242F",
    "state/unresolved/EX-math1-20242M",
    "state/unresolved/EX-math1-20251F",
    "state/unresolved/EX-math1-20251M",
    "state/unresolved/EX-math1-20261F",
    "state/unresolved/EX-math1-20261M",
    "state/unresolved/EX-math2-20252F",
    "state/unresolved/EX-math2-20252M",
    "state/unresolved/EX-science-20241F",
    "state/unresolved/EX-science-20241M",
    "state/unresolved/EX-science-20242F",
    "state/unresolved/EX-science-20242M",
    "state/unresolved/EX-science-20251F",
    "state/unresolved/EX-science-20251M",
    "state/unresolved/EX-science-20252F",
    "state/unresolved/EX-science-20252M",
    "state/unresolved/EX-science-20261F",
    "state/unresolved/EX-science-20261M",
    "state/unresolved/EX-social-20241F",
    "state/unresolved/EX-social-20241M",
    "state/unresolved/EX-social-20242F",
    "state/unresolved/EX-social-20242M",
    "state/unresolved/EX-social-20251F",
    "state/unresolved/EX-social-20251M",
    "state/unresolved/EX-social-20252F",
    "state/unresolved/EX-social-20252M",
    "state/unresolved/EX-social-20261F",
    "state/unresolved/EX-social-20261M",
    "terminal/local_fixture_failed",
    "terminal/ruler_stale",
    "terminal/synthetic_clean"
  ],
  "duplicates": [],
  "expected_duplicates": [],
  "missing": [],
  "extra": []
}
```

## C. 결과 재계산·독립 경계 확인

작성자 결과를 그대로 승격하지 않았다. 시험 코드·assertion·후보 diff를 읽고 실제 재실행했으며,
추가 메모리 실행의 result 전체가 동결 regression_result.json과 같은지 대조했다.
기존 시험의 변경은 사전에 명시된 후보 경로·source_units 인자·임시 raw 경로뿐이다. 기존 assertion은 유지된다.

- 기존15 케이스 실패0, gate0 planted=11 undetected=0 및 정상 오탐0.
- 측정기 실제 exit1·WARN40·per-item1148행, 두 측정 실행의 stdout/stderr와 동결 raw가 동일.
  **1148은 기계 출력행 수이며 인쇄ID 전수 커버리지가 아니다.**
- B3의 stale/fixture-fail/synthetic-clean은 최종 1/2/0 단일 마커와 일치한다.
  clean의 WARN 제거와 scanner mock은 배선 통제에만 쓰였으며 운영 성공 근거가 아니다.
- 실제 CLI 15건 및 격리한 실제 호출 블록 3건을 다시 실행했다. 호출부 기존 검사는 subprocess argv를 제외하고 AST 동일하다.
  전체 assurance 실행이 아니라 격리 호출 블록 시험임을 유지한다.
- 추가 확인은 혼합4상태·partial 이전 hash drift·정상 분포 순서 변경·분포 절 누락의 4건.
  상태별15개씩 혼합해도 eligible15와 diagnostic60을 분리하고 downstream4단계를 not-run/null로 보존한다.
- checks/role_scan/ident_scan/moved_literals/residue_scan/gate0/holdout 7함수는 현행·원후보·수정후보 간 AST 동일.
  gate0 및 기존 승인된 스캔 규칙을 수정하여 통과시키지 않았다.
- 두 전체 패치 및 원후보 대비 repair_delta.patch가 각각 정확히 대응한다.
  Python6파일 compile/AST·trailing-whitespace 검사 통과. ruff/mypy/pytest 미설치를 직접 확인했으며 의존성 추가 없음.
- textpatch self-test exit0, seeded10/undetected0. 의도된 mixed-EOL FAIL/WARN은 이 도구 검출력 시험의 출력이며 경고0으로 보고하지 않는다.
- validation.json 이번 재실행: 28109 B / 3835d24d80ffdd52d42f65859d9d36ed35cb97775a014e62c927563465a355a4.
  파일의 scope 문자열은 작성자 harness 원문을 보존한다. 독립 실행 사실은 본 판정의 실행 기록으로 입증한다.

독립 실행의 요약 및 상세(실제로 출력된 값; 원천 내용 적격성 판정 없음):
```json
{
  "regression_result_equal_frozen": true,
  "legacy": {
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
  "terminal_cases": [
    {
      "id": "terminal/ruler_stale",
      "actual": 1,
      "markers": [
        "1"
      ],
      "passed": true
    },
    {
      "id": "terminal/local_fixture_failed",
      "actual": 2,
      "markers": [
        "2"
      ],
      "passed": true
    },
    {
      "id": "terminal/synthetic_clean",
      "actual": 0,
      "markers": [
        "0"
      ],
      "passed": true
    }
  ],
  "probes": [
    {
      "id": "mixed-four-states",
      "exit": 1,
      "state_counts": {
        "eligible": 15,
        "not-applicable": 15,
        "partial": 15,
        "unresolved": 15
      },
      "terminal": "contract_exit=1",
      "downstream": {
        "derivation": {
          "exit": null,
          "reason": "source-incomplete",
          "status": "not-run"
        },
        "gate0": {
          "exit": null,
          "reason": "source-incomplete",
          "status": "not-run"
        },
        "measurement": {
          "exit": null,
          "reason": "source-incomplete",
          "status": "not-run"
        },
        "ruler-comparison": {
          "exit": null,
          "reason": "source-incomplete",
          "status": "not-run"
        }
      }
    },
    {
      "id": "drift-before-partial",
      "exit": 2,
      "output": "[BLOCKED] source contract: source drift: EX-english-20241F/meta.yml\ncontract_exit=2\n"
    },
    {
      "id": "reordered-distribution",
      "accepted": true,
      "count": 60
    },
    {
      "id": "missing-distribution",
      "rejected": true,
      "reason": "missing/duplicate measurement section: ^=== selective-score distribution ==="
    }
  ],
  "unchanged_functions": [
    "checks",
    "role_scan",
    "ident_scan",
    "moved_literals",
    "residue_scan",
    "gate0",
    "holdout"
  ],
  "exact_delta": true,
  "cli_coverage": {
    "expected": [
      "extra_field",
      "hash_drift",
      "invalid_utf8",
      "malformed",
      "missing_contract",
      "missing_unit",
      "mixed_partial",
      "no_arguments",
      "null",
      "root_array",
      "snapshot_array",
      "state_array",
      "synthetic_eligible_live_measurement",
      "unknown_state",
      "unresolved_real_snapshot"
    ],
    "observed": [
      "extra_field",
      "hash_drift",
      "invalid_utf8",
      "malformed",
      "missing_contract",
      "missing_unit",
      "mixed_partial",
      "no_arguments",
      "null",
      "root_array",
      "snapshot_array",
      "state_array",
      "synthetic_eligible_live_measurement",
      "unknown_state",
      "unresolved_real_snapshot"
    ],
    "duplicates": [],
    "expected_duplicates": [],
    "missing": [],
    "extra": []
  },
  "caller_coverage": {
    "expected": [
      "absent",
      "measurement_warn",
      "unresolved"
    ],
    "observed": [
      "absent",
      "measurement_warn",
      "unresolved"
    ],
    "duplicates": [],
    "expected_duplicates": [],
    "missing": [],
    "extra": []
  },
  "cli": [
    {
      "id": "no_arguments",
      "exit": 2,
      "terminal": "contract_exit=2",
      "warn": 0,
      "stderr": ""
    },
    {
      "id": "missing_contract",
      "exit": 2,
      "terminal": "contract_exit=2",
      "warn": 0,
      "stderr": ""
    },
    {
      "id": "unresolved_real_snapshot",
      "exit": 1,
      "terminal": "contract_exit=1",
      "warn": 0,
      "stderr": ""
    },
    {
      "id": "malformed",
      "exit": 2,
      "terminal": "contract_exit=2",
      "warn": 0,
      "stderr": ""
    },
    {
      "id": "invalid_utf8",
      "exit": 2,
      "terminal": "contract_exit=2",
      "warn": 0,
      "stderr": ""
    },
    {
      "id": "root_array",
      "exit": 2,
      "terminal": "contract_exit=2",
      "warn": 0,
      "stderr": ""
    },
    {
      "id": "null",
      "exit": 2,
      "terminal": "contract_exit=2",
      "warn": 0,
      "stderr": ""
    },
    {
      "id": "hash_drift",
      "exit": 2,
      "terminal": "contract_exit=2",
      "warn": 0,
      "stderr": ""
    },
    {
      "id": "missing_unit",
      "exit": 2,
      "terminal": "contract_exit=2",
      "warn": 0,
      "stderr": ""
    },
    {
      "id": "unknown_state",
      "exit": 2,
      "terminal": "contract_exit=2",
      "warn": 0,
      "stderr": ""
    },
    {
      "id": "state_array",
      "exit": 2,
      "terminal": "contract_exit=2",
      "warn": 0,
      "stderr": ""
    },
    {
      "id": "snapshot_array",
      "exit": 2,
      "terminal": "contract_exit=2",
      "warn": 0,
      "stderr": ""
    },
    {
      "id": "extra_field",
      "exit": 2,
      "terminal": "contract_exit=2",
      "warn": 0,
      "stderr": ""
    },
    {
      "id": "mixed_partial",
      "exit": 1,
      "terminal": "contract_exit=1",
      "warn": 0,
      "stderr": ""
    },
    {
      "id": "synthetic_eligible_live_measurement",
      "exit": 1,
      "terminal": "contract_exit=1",
      "warn": 40,
      "stderr": ""
    }
  ],
  "caller": [
    {
      "id": "unresolved",
      "exit": 1,
      "failures": [
        "ruler gate: regen_rubric_values.py exit=1 (expected 0)",
        "ruler gate: detector did not prove its own detection power (원칙 12-d)",
        "ruler gate: ruler is stale -- ?"
      ]
    },
    {
      "id": "absent",
      "exit": 2,
      "failures": [
        "ruler gate: regen_rubric_values.py exit=2 (expected 0)",
        "ruler gate: detector did not prove its own detection power (원칙 12-d)",
        "ruler gate: ruler is stale -- ?"
      ]
    },
    {
      "id": "measurement_warn",
      "exit": 1,
      "failures": [
        "ruler gate: regen_rubric_values.py exit=1 (expected 0)",
        "ruler gate: ruler is stale -- ?",
        "ruler gate: 40 warning line(s), expected 0 -- [WARN] identical selective sequence (n=18): EX-info-20252F == EX-info-20252M"
      ]
    }
  ],
  "validation": {
    "bytes": 28109,
    "sha256": "3835d24d80ffdd52d42f65859d9d36ed35cb97775a014e62c927563465a355a4"
  },
  "unexpected_warnings": 0
}
```

재현 C — 아래 코드를 PowerShell here-string으로 python 표준입력에 전달한다.
동결 결과 파일은 --no-save로 유지하며 임시파일만 사용한다. 성공 기대: exit0, unexpected_warnings=0,
case_coverage의 세 차집합·중복 모두 빈 목록, legacy.failures=0, exact_delta=true,
CLI15/호출부3 모두 기대 코드·마커 일치. 출력의 legacy.live_warnings=40은 보존된 실패 증거다.
```python
import ast,collections,contextlib,copy,difflib,hashlib,io,json,pathlib,re,sys
P=pathlib.Path('output/260912/rev').resolve(); pre='260912_05_info_ab50_q1_'
def stamp(p):
 b=p.read_bytes(); return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def cov(a,b):
 return dict(expected=sorted(a),observed=sorted(b),duplicates=sorted(k for k,n in collections.Counter(b).items() if n>1),expected_duplicates=sorted(k for k,n in collections.Counter(a).items() if n>1),missing=sorted(set(a)-set(b)),extra=sorted(set(b)-set(a)))
p=P/(pre+'regression_test.py')
g={'__file__':str(p),'__name__':'independent_replay'}; old=sys.argv[:]; sys.argv=[str(p),'--no-save']
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(p.read_text(encoding='utf-8'),str(p),'exec'),g)
sys.argv=old
actual=g['result']; frozen=json.loads((P/(pre+'regression_result.json')).read_text(encoding='utf-8'))
assert actual==frozen
units=g['source']; e=[f'state/{s}/{u}' for s in ('partial','unresolved') for u in units]+[f'distribution/{s}/{u}' for s in ('delete','duplicate','same_count_replace') for u in units]+['terminal/ruler_stale','terminal/local_fixture_failed','terminal/synthetic_clean']
coverage=cov(e,[c['id'] for c in actual['cases']])
assert not any(coverage[k] for k in ('duplicates','expected_duplicates','missing','extra'))
probes=[]
mod=g['load'](P/(pre+'repaired_candidate.py'))
data=copy.deepcopy(g['contract']); ordered=sorted(units)
for i,u in enumerate(ordered): data['dispositions'][u]=('eligible','not-applicable','partial','unresolved')[i%4]
code,out=g['call'](mod,data)
report=json.loads(out.splitlines()[0])
assert code==1 and report['dispositions']==data['dispositions']
assert report['diagnostic_units']==ordered
assert report['statistical_units']==sorted(u for u in ordered if data['dispositions'][u]=='eligible')
assert all(v==dict(status='not-run',reason='source-incomplete',exit=None) for v in report['downstream'].values())
assert out.splitlines()[-1]=='contract_exit=1'
probes.append(dict(id='mixed-four-states',exit=code,state_counts={k:len(v) for k,v in report['state_units'].items()},terminal=out.splitlines()[-1],downstream=report['downstream']))
data['snapshot'][ordered[0]]['meta.yml']['sha256']='0'*64
code,out=g['call'](mod,data); assert code==2 and out.splitlines()[-1]=='contract_exit=2'
probes.append(dict(id='drift-before-partial',exit=code,output=out))
raw=g['raw']; m=re.search(r'=== selective-score distribution ===\n(.*?)\n\n',raw,re.S)
lines=m.group(1).splitlines(); reverse=raw[:m.start(1)]+'\n'.join([lines[0]]+lines[1:][::-1])+raw[m.end(1):]
v=mod['derive'](reverse,g['expected'],ordered)
assert v['distribution_coverage']==cov(ordered,ordered)
probes.append(dict(id='reordered-distribution',accepted=True,count=v['units_all']))
missing=raw[:m.start()]+raw[m.end():]
try: mod['derive'](missing,g['expected'],ordered)
except ValueError as exc: probes.append(dict(id='missing-distribution',rejected=True,reason=str(exc)))
else: raise AssertionError('missing distribution accepted')
# Body-level AST identity proves unchanged approved scanner/detector semantics.
names=['checks','role_scan','ident_scan','moved_literals','residue_scan','gate0','holdout']
trees=[ast.parse(p.read_text(encoding='utf-8')) for p in (pathlib.Path('tools/regen_rubric_values.py'),P/'260912_01_info_ab50_q1_integrated_candidate.py',P/(pre+'repaired_candidate.py'))]
for name in names:
 vals=[ast.dump(next(n for n in t.body if isinstance(n,ast.FunctionDef) and n.name==name)) for t in trees]
 assert len(set(vals))==1,name
base=(P/'260912_01_info_ab50_q1_integrated_candidate.py').read_text(encoding='utf-8'); candidate=(P/(pre+'repaired_candidate.py')).read_text(encoding='utf-8')
delta=''.join(difflib.unified_diff(base.splitlines(True),candidate.splitlines(True),fromfile='a/output/260912/rev/260912_01_info_ab50_q1_integrated_candidate.py',tofile='b/output/260912/rev/'+pre+'repaired_candidate.py'))
assert delta==(P/(pre+'repair_delta.patch')).read_text(encoding='utf-8')
# Re-run real CLI/caller cases and preserve fresh details in memory, not frozen files.
p=P/(pre+'caller_test.py'); cg={'__file__':str(p),'__name__':'independent_caller'}; sys.argv=[str(p),'--no-save']
with contextlib.redirect_stdout(io.StringIO()): exec(compile(p.read_text(encoding='utf-8'),str(p),'exec'),cg)
sys.argv=old
cr=cg['result']
cli_expected=['no_arguments','missing_contract','unresolved_real_snapshot','malformed','invalid_utf8','root_array','null','hash_drift','missing_unit','unknown_state','state_array','snapshot_array','extra_field','mixed_partial','synthetic_eligible_live_measurement']
cli_cov=cov(cli_expected,[x['id'] for x in cr['cli_cases']])
caller_cov=cov(['unresolved','absent','measurement_warn'],[x['id'] for x in cr['caller_cases']])
for z in (cli_cov,caller_cov):
 assert not any(z[k] for k in ('duplicates','expected_duplicates','missing','extra'))
print(json.dumps(dict(regression_result_equal_frozen=True,case_coverage=coverage,legacy=actual['legacy'],terminal_cases=[x for x in actual['cases'] if x['id'].startswith('terminal/')],probes=probes,unchanged_functions=names,exact_delta=True,cli_coverage=cli_cov,caller_coverage=caller_cov,cli=[dict(id=x['id'],exit=x['exit'],terminal=x['stdout'].splitlines()[-1],warn=x['stdout'].count('[WARN]'),stderr=x['stderr']) for x in cr['cli_cases']],caller=[dict(id=x['id'],exit=x['exit'],failures=x['failures']) for x in cr['caller_cases']],validation=stamp(P/(pre+'validation.json')),unexpected_warnings=0),ensure_ascii=True))
```

# §2 unit별 판정

## Q1 — approve: B1–B3 수정 closure

**B1**: SourceIncomplete를 입력/스키마 오류와 구분한다. 정상 동결 입력의 partial/unresolved는 상태별 유닛·근거 누락·coverage를 보존하고 원천 단계 exit1을 반환한다.
downstream measurement/derivation/gate0/ruler-comparison은 not-run, exit=null, reason=source-incomplete이며 PASS가 아니다.
hash drift·스키마 실패는 exit2다. 120/120 상태 회귀와 혼합 상태·drift 우선순위 확인으로 원판정 요구가 닫혔다.
이 원천 단계의 terminal1을 전역 필수단계 완료로 해석하지 않는다. 06 §3의 전역 합성 규칙은 유지하며,
실제 상위 호출부가 누락된 detector/stale 증거를 추가 실패로 남긴다.

**B2**: derive의 필수 source_units와 distribution 식별자를 양방향·중복 대조한다.
삭제/중복/동수대체 180/180 차단, 정상 및 순서 변경 통제 수용. diagnostic_units와 statistical_units는 별도 출력이다.
이 결합은 진단 유닛ID에 대한 것일 뿐, 해당 ID의 원문 문항·선택형 보유·EXCL·정식 적격 집합이 모두 같은 집합이라는 승인이 아니다.
측정기 집계 규칙은 그대로이며, 실제 적격 입력의 포함/비적용 근거와 원천 수량축은 여전히 별도 폐쇄가 필요하다.

**B3**: 하위 표시는 stage_measurement_exit로 분리하고 main에서 terminal contract_exit를 한 번 출력한다.
원판정 3경로 및 실제 CLI15경로에서 최종 값과 프로세스 종료값 일치. 원 WARN을 삭제하거나 로컬 gate0 실패를 정상화하지 않는다.

**정확한 감사 승인 대상(후보 diff 한정):**
| 후보 | bytes | SHA256 | 대응 운영 대상·한계 |
|---|---:|---|---|
| 260912_05_info_ab50_q1_repaired_candidate.py | 29916 | 12a2f410ec7fcff3b604480dd96c23248e90962a620c1e3bc4350c8e0fd3a4ae | tools/regen_rubric_values.py; integrated.patch의 정확한 변경만 |
| 260912_05_info_ab50_q1_integrated.patch | 11007 | e57e1069b76c6deefffa07081b008aee1db183d0031560aba77eefc4224ddda9 | 현재 21594 B 원본에 대한 최소 통합 diff; 임의 ALLOW/수치/밴드 변경 불가 |
| 260912_05_info_ab50_q1_assurance_candidate.py | 12036 | 2868482fa6fbb5c6094a7e112c988f5ddf493a59c30a78289e66c6f26f65471a | tools/check_assurance_contract.py; argv 두 인자 추가만 |
| 260912_05_info_ab50_q1_assurance.patch | 437 | ff0a66ea9d904c3664383f0740df349daea388451475cffc3763f91ae3b93338 | --source-contract 및 고정 공급 위치; 기존 검사 제거 불가 |

후보 파일은 모두 output/260912/rev/ 아래다. 위 승인은 **정확한 diff에 대한 감사키**이며 사용자 정책키를 대신하지 않는다.
지금 즉시 반영하도록 승인된 제품/보호 기준 파일은 **0개**다.
사용자 정책키 확보 후에도 원천 입력·재동결·stale 처리·기존 게이트를 생략할 수 없다.
새로운 코드나 변경된 바이트는 이 감사키의 범위에 포함되지 않는다.

## Q2 — insufficient-evidence: 사용자 정책키·운영 적용 미충족

선행04가 승인한 06 §3의 정책 의미는 유지한다. 재판정 요청은 그 정책키 자체를 제공하지 않았다.
sidecar policy_key=null이고, 현재 사용자 확인은 실행 모델·깊이에 관한 것뿐이다.

남은 결정은 **동결 원천에서 근거 확인 후 파생되는 모집단/계층 재서명, 06 §3 contract_exit 운영 적용,
정확한 호출부 diff 및 analysis/info_ab50_source_contract.json 고정 공급 방식**이다.
실제 원천 60개는 unresolved이며 운영 적격성 감사키도 이 판정으로 생성되지 않는다.
후보에 적힌 exact_patch_audit_key=null은 작성 시점 기록으로 보존한다. 이번 코드 감사키는 본 판정의 Q1이고,
작성자는 과거 sidecar를 덮어쓰지 말고 후속 인계에서 코드 감사키와 입력 적격성 미완료를 분리해야 한다.

## R3 — approve: 호출부·입력 후보 준비 완료

호출부는 source-contract 인자와 고정 공급 경로만 더하며 기존 실패 검사들을 유지한다.
실제 unresolved 입력, 누락 입력, 측정 WARN 경로에서 상위 fail 목록이 남는다. 무인자 오류를 숨기지 않았다.

입력 공급자는 후보 작성 소유자이며 승인권자와 구분되어 있다. source_contract는 snapshot/dispositions,
sidecar는 소유·승인·파일 hash/locator·상태 결손 기록을 맡는다.
60개 모두 내용이 미확정임을 null/unresolved/blocked로 표시한 것은 R3의 **준비 요구 충족**이지 원천 승인 자체가 아니다.
프로그램이 승인권자의 신원을 암호학적으로 인증한다고 주장하지 않는다.
공급 파일 미설치 상태를 보존하며, 지금 확인되지 않은 인쇄ID를 임의로 채워서는 안 된다.

# §3 follow-up (비차단)

- 추가 일반 JSON/인코딩/모든 예외 종류나 임의의 미래 출력 형식에 대한 완전성을 주장하지 않는다.
  이번에 측정된 B1–B3 closure를 넘어 새 검출기·새 명세·새 차단 라운드를 요구하지 않는다.
- 기존 중복 import/계층4행 설명 문구 정리는 이번 구속 변경이 아니다.
- 정식 원천 적격성·인쇄ID·합계축·WARN40·Q3·문항 전수 검증은 **기존 운영/배포 차단 항목**이다.
  비차단 follow-up이라는 절 제목으로 그 잔여를 면제하지 않는다.
- 전체 assurance/build는 실행하지 않았다. 호출부3건 통과를 전체 assurance 통과라고 보고하지 않는다.
  코드 감사키 이후 실제 적용 시 기존 §5-a와 정확한 승인 CLI 계약을 소비해야 한다.

# §4 open units (남은 집합)

| unit | 현재 상태 | 다음 소유자·완료 조건 |
|---|---|---|
| BF1 명세 완결성 | closed 유지 | 재작성하지 않음 |
| Q1 B1–B3 코드 후보 | closed / approve | 작성자가 본 판정과 후보 hash를 소비; 수정 없이 정책키 단계로 |
| R3 호출·입력 후보 준비 | closed / approve | 미확정 내용은 유지; 후보 준비 반복 불필요 |
| Q2 사용자 정책키 | ▲ blocked | 정확한 범위의 사용자 결정 기록 필요 |
| 실제 원천 적격성·인쇄ID·합계축 | ▲ blocked | 60개 상태 근거 확인; expected/observed 문항ID 및 포함/비적용 근거 별도 검증 |
| 기준 운영 적용·재동결 | ▲ blocked | 두 키·정확 diff·입력 권한을 확인한 소유자 반영 후 감사권한자 재동결 및 새 게이트 |
| Q3 정보 난이도 | 미결 유지 | 이번 범위 밖; 별도 근거·서명 |
| A/B50 전수 검증·배포 | ▲ blocked | 원천/기준 및 문항 전수 독립검증·최종판정·정본/문제지/답지/인덱스 동기화 |

## [Codex/OMX 지시]

```text
stage: Q1 수정 독립 재판정 완료 → 작성 책임 복귀 → Q2 정책키/원천 입력 잔여. 전체 배포 미완료.
executor: Codex/OMX 작성 소유자. analysis/wip/solve-back-verifier_260910_info_ab50_newsession.md NEXT를 읽고 본 판정으로 상태를 갱신한다. 판정자는 후보를 수정하지 않는다.
inputs: output/260912/rev/260912_08_info_ab50_q1_repaired_ruling.md; output/260912/rev/260912_05_info_ab50_q1_manifest.json 및 직접 입력. 본 판정 §1-A의 bytes/SHA256을 재측정한다. 60유닛/120파일과 후보 diff 불일치 시 중단한다.
approved: Q1의 정확한 repaired_candidate/integrated.patch와 assurance_candidate/assurance.patch에 대한 코드 감사키; R3 후보 준비만. B1-B3 신규 수정 0건.
work-now: 본 회신과 hash를 읽고 WIP NEXT를 Q2 사용자 정책키·실제 입력 근거 단계로 갱신한다. 이미 통과한 후보를 재작성하거나 BF1을 다시 열지 않는다. 정확한 모집단/계층 재서명·06 §3 운영 계약·고정 공급 방식에 대한 사용자 결정은 모델 확인과 분리해서 기존 한 묶음으로 제시한다.
allowed-outputs-now: 작성자 자신의 WIP 및 후속 인계 기록. 기존 manifest·후보·결과·판정08은 덮어쓰지 않는다.
prohibited-now: 보호 기준·실운영 호출부·공급 파일 설치, 원천 적격성 임의 확정, WARN 면제, 커밋·삭제·타인 WIP 수정. 현재 즉시 제품 반영 0개.
gate-before-application: §1-A 동결 전수 대조 mismatch0, python output/260912/rev/260912_05_info_ab50_q1_verify.py → exit0, commands2/static_files6/exact_patches=true/unexpected_harness_warnings0/manifest_checked=true; 수정303 실패0, 기존15 실패0, gate0 planted11/undetected0, CLI15/호출부3 실패0. 실제 WARN40은 미통과 증거로 별도 보존한다.
after-both-keys: 정확한 승인 범위만 소유자 반영. 구→신 bytes/sha256 사슬, 감사권한자 재동결, 해당 자에 의존한 과거 판정 stale 처리, 원천 재생성·새 검증을 이어서 수행한다. 지금 미승인 정책·원천 적격성을 본 코드 승인으로 대체하지 않는다.
operational-gate: analysis/REV_GUIDE.md §5-a 및 선행03 §2 Q4의 명령·기대출력·WARN0·지적행0·카운트를 소비한다. source-contract CLI를 적용할 때는 승인된 정확한 인자/공급 경로로 실행하며 기존 무인자 계약을 슬쩍 생략하지 않는다. 현재 원천 미완성으로 이 게이트 성공은 아직 주장 불가.
stop: 정책키·입력 권한 미충족에서 정본 반영/재동결/배포로 넘어가지 않는다. 이미 측정한 B1-B3에 새 명세 라운드를 만들지 않는다.
report: 본 판정 경로·후보 hash·코드 승인 범위·기존 잔여 및 Session 목적지를 함께 보고한다.
```

Session: RETURN-AUTHOR — 작성 책임의 소유 WIP는 analysis/wip/solve-back-verifier_260910_info_ab50_newsession.md.
이전 인계의 작성 세션 식별자 01a0903f-4294-7412-b42b-f5f8b15b98f9는 현 가용성 미확인이다.
가능하면 해당 작성 세션으로 복귀하고, 복구 불가하면 NEW-CONTINUATION으로 같은 작성 책임을 승계한다.
새 작성 세션에서 해시·독점 소유권·충돌 쓰기를 확인하고 NEXT부터 이어가며 독립 감사로 재표시하지 않는다.

복귀 메시지:
“output/260912/rev/260912_08_info_ab50_q1_repaired_ruling.md를 읽고 hash·승인 범위를 확인하라.
Q1 B1–B3와 R3 후보 준비는 approve이며 새 구속 수정은 없다.
WIP NEXT에서 Q2 정책키와 실제 입력 근거 잔여를 이어가라. 모델 확인은 정책키가 아니며 정본 반영·배포는 아직 금지다.”

## history

- 2026-09-12: Codex/OMX gpt-6-astra/medium(사용자 확인)이 별도 컨텍스트에서 수정 후보를 직접 재검증.
  B1–B3와 호출·입력 후보 준비 approve, 신규 구속 수정0. Q2 정책키·원천 적격성·운영 적용·배포 blocked 유지.
  후보·보호 기준·제품 무수정. 이 독립 판정 역할만 완료하며 전체 과업 완료로 표시하지 않는다.

