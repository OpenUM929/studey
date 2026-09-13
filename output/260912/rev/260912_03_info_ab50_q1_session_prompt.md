# 새 독립 Astra 판정 세션 실행 프롬프트

C:\dev\study에서 실행한다. 이 프롬프트는 입력 후보에 대한 독립 검토 요청이지 그 후보를 승인하라는 지시가 아니다.

<target> output/260912/rev/260912_02_info_ab50_q1_review_package.md 및 그 문서가 지목한 01 패치·후보·시험·결과·원출력. 선행 입력은 output/260911/rev/260911_03_info_ab50_ruler_ruling.md, 260911_04_info_ab50_repair_spec.md, 260911_06_info_ab50_state_contract_spec.md, 260911_07_info_ab50_bf1_completeness_ruling.md. 모두 같은 output/260911/rev 아래에 있다. 지침은 AGENTS.md, CLAUDE.md, docs/DATA_STANDARD.md, docs/ASTRA_EXECUTION_POLICY.md, docs/SESSION_HANDOFF_GUIDE.md, analysis/REV_GUIDE.md 및 .claude/agents/rev-arbiter.md를 읽는다.
<touched> 작성자는 output/260912/rev/01 후보 묶음과 02 검토 묶음, 본 프롬프트 및 자기 WIP만 이번 후보 작업에서 작성했다. 보호 기준·문항은 변경하지 않았다. 바이트 manifest는 아래 표를 참조하고 재측정한다.
<executor> 본체 직접 Codex/OMX, gpt-6-astra를 호스트 증거로 확인. 책임은 .claude/agents/rev-arbiter.md의 독립 판정; 작성에 참여하지 않은 새 컨텍스트가 필요하다. 실제 모델/깊이를 기록한다. 모델 미확인 시 독립 Astra 승인이라고 표시하지 않는다. 서브에이전트/자동 재시도 없음.
<requests> 정확히 02의 세 요청을 판정한다: (1) Q1 구현의 검출력과 반영 허용 범위 (2) Q2 contract_exit 운영 계약/사용자 키 (3) 호출부와 원천 적격성/인쇄ID 증거가 미완성일 때의 최소 후속 범위. 각 요청은 approve/revise-required/reject/blocked, 근거, 허용/금지 쓰기, 잔여를 기록한다. BF1 완결성은 07에서 닫혔으므로 새로 반복 판정하지 않는다. 원천 바이트 일치를 정식 적격성이나 A/B 문항 감사로 확대하지 않는다.
<reply> output/260912/rev/260912_04_info_ab50_q1_independent_ruling.md. REV_GUIDE 판정 표와 [Codex/OMX 지시]에 승인 범위·구체 후속·재검증 명령을 적는다. 파일이 이미 있으면 덮어쓰지 말고 확인 후 충돌을 보고한다. 원장 기록은 규약에 따라 textpatch를 사용하며 자기 판정/WIP 외 기존 산출물은 수정하지 않는다.
<constraints> 검토 범위는 통합 후보1개와 시험15케이스/기존 gate0 11개이다(01 integration_result의 cases 길이와 original_gate0_output에서 재확인). 코퍼스는 04 snapshot의60유닛/120파일 바이트+메타 확인에 한정하며 내용 판정이 더 필요하면 최소 범위를 명시한다. 허용 입력: 위 파일, 기준3개, 측정기 재실행에 필요한 현재 corpus transcript/meta, 해당 근거 규약. 금지 입력/작업: A/B 답·해설·문항 본문을 통한 별도 품질감사, 제품·기준·후보·타인 WIP 수정, 배포·커밋·삭제. 시험은 작성자 코드이므로 실행 전 쓰기 경계를 읽는다. 검증 명령: python output/260912/rev/260912_01_info_ab50_q1_integration_test.py. 이 명령은 raw 출력 파일을 재기록하므로 원본 증거 보존이 필요하면 읽은 뒤 임시 복제본에서 출력 경로를 격리해 실행하고 차이를 명시한다. 실패 상태를 숨기지 않는다. 실제 원천 exit1/WARN40은 기존 실행 인용이며 직접 다시 측정하면 새 값으로 구분한다.

## 예산·중단·복귀
현재 작성 세션은 새 세션의 남은 예산을 측정할 수 없어 자동 발주하지 않았다. 수신 세션은 작업 시작 전 자기 자원 경계를 확인한다. 한 후보 묶음만 검토하고 범위를 확대하지 않는다. 컨텍스트/쿼터 한계 또는 승인 입력 부재 시 완료 증거·정확한 NEXT를 저장하며 추정 승인하지 않는다. 새 정책/정식 적격성 작성자가 되어 자기 승인하지 않는다.
판정 파일 저장·구조검사·원장 기록 후 이 독립 역할을 종료한다. 전체 배포 완료라고 표시하지 않는다.
Session: RETURN-AUTHOR — 기존 작성 세션 01a0903f-4294-7412-b42b-f5f8b15b98f9로 복귀. 복구 불가 시 NEW-CONTINUATION으로 작성 책임을 승계하고 아래 WIP에서 재개한다. 이 식별자는 복귀 위치이며 권한 증거 아님.
복귀 메시지: “output/260912/rev/260912_04_info_ab50_q1_independent_ruling.md를 읽고 해시·승인 범위를 확인한 뒤 analysis/wip/solve-back-verifier_260910_info_ab50_newsession.md의 NEXT부터 승인된 후속 작업을 진행하라. 완료 후보를 다시 작성하지 말고, 미승인 기준 변경·배포는 하지 마라.”
## 동결 입력(이 프롬프트 자신 제외)
| path | bytes | SHA256 |
|---|---:|---|
| output\260912\rev\260912_01_info_ab50_measure_raw.txt | 76913 | d5544cfbbc003bdfcebae8587833b2f841c32464993df237f3a4eca445db1859 |
| output\260912\rev\260912_01_info_ab50_q1_integrated.patch | 8398 | 1cbed11e5c5841585736351b940f827d67c15f7c4f730a893b81e78eefd9b614 |
| output\260912\rev\260912_01_info_ab50_q1_integrated_candidate.py | 27749 | cdaf9e1d1670e3ffb21846554c39a5e65bc9b7e5e4da424225480d1e8f48b7fb |
| output\260912\rev\260912_01_info_ab50_q1_integration_result.json | 4801 | e28cf9dd0aab19410b5ca46af083f6da9b2a1cdf52b6a6e0390921bbb34a9fd0 |
| output\260912\rev\260912_01_info_ab50_q1_integration_test.py | 6192 | d10efb5cf5a552dbaf13c5f00101b09c1ca1b8bfa7cf052e739d4aac36c43892 |
| output\260912\rev\260912_02_info_ab50_q1_review_package.md | 4913 | 1399b0711166ed455d612197567680c631e96e0800cd2e84df3ba1031d8f6885 |
