# S2 type-proposer relay — Cycle 0 / 2025-2학기 신규 11개 corpus

Created by: Codex/OMX main loop (Sol)  
Date: 2026-08-27  
Status: waiting for external Claude Code Opus response

This is the local copy of the user-copied relay printed in the conversation. It is a coordination artifact, not a proposal or an approval.

``text
[CC 회람] 260827_03 — 2025-2학기 11개 코퍼스 유형 제안
<target> 2025-2학기 신규 corpus 11개(총 ·3개 필수 산출물 33개·합계 373,834 bytes): corpus/EX-english-20252M/, corpus/EX-info-20252M/, corpus/EX-math2-20252M/, corpus/EX-science-20252M/, corpus/EX-social-20252M/, corpus/EX-history-20252M/, corpus/EX-korean-20252F/, corpus/EX-english-20252F/, corpus/EX-science-20252F/, corpus/EX-social-20252F/, corpus/EX-history-20252F/. 각 디렉터리의 transcript.md·meta.yml·verify_log.tsv 및 corpus/_images/<ID>/ 페이지를 읽고, analysis/catalog/_README.md·COMMON_TYPES.md·TYPE_MASTER.md·DIFFICULTY_RUBRIC.md·CODE_REGISTRY.md·analysis/curriculum_2022.md·해당 과목 catalog·analysis/FORECAST_GUIDE.md를 읽으십시오. 산출물은 output/260827/260827_03_<ID>_type_analysis.md 및 output/260827/260827_03_<ID>_catalog_update.md (각 ID당 2개, 총 22개)입니다.
<touched> 이번 라운드 Codex/OMX가 생성: output/260827/260827_03_type-proposer_relay.md, analysis/wip/codex-omx_260827_cycle0_s2_type_propose_relay.md. 이전 S1에서 수정: 11개 target corpus의 transcript.md·meta.yml·verify_log.tsv, analysis/EXTRACTION_LOG.md, analysis/wip/codex-omx_260827_cycle0_s1_restart.md. 카탈로그는 변경하지 않았습니다.
<executor> type-proposer (external Claude Code CLI / Opus; source instruction inspected: .claude/agents/type-proposer.md). 이 역할은 refined corpus를 근거로 문항별 유형 배정·통합·카탈로그 갱신 초안을 작성하는 전담 authoring owner입니다.
<requests> 1) 각 corpus의 transcript↔meta.yml↔verify_log 및 페이지 spot-check 결과를 ready | ready-with-flags | blocked 중 하나로 명시하십시오. 2) 준비된 corpus마다 문항별 배정·5~12개 유형 통합·축/함정/별 근거·공통패턴 비교·새 항목/기존 항목 diff를 담은 한국어 제안서 2개를 작성하고 complete | partial | blocked를 명시하십시오. 3) 전 corpus에 대해 type-proposer actor의 classify·merge·grade 행을 해당 verify_log.tsv에 append하고, 각 행에 evidence page를 남기십시오. 4) catalog ID 정책이 미결이면 ID를 임의 발급하지 말고 decision-request로 남기십시오.
<reply> reply artifact는 output/260827/260827_03_<ID>_type_analysis.md 및 output/260827/260827_03_<ID>_catalog_update.md 22개와 analysis/wip/type-proposer_260827_cycle0_2025S2.md입니다. 각 제안서는 analysis/REV_GUIDE.md §2-b C 및 .claude/agents/type-proposer.md의 두 문서 형식을 충족하고, WIP에는 슬라이스마다 진행 행과 마지막 NEXT를 남기십시오. 완료 후 생성 경로·문항 배정 수·새 초안 수·update diff 수·공통 패턴 수·open questions를 WIP 마지막 행에 요약하십시오.
<constraints> Write surface는 output/260827/의 본인 제안서 22개, 위 11개 corpus의 verify_log.tsv append, 본인 WIP 1개뿐입니다. canonical catalogs·HARVEST_LOG·EXTRACTION_LOG·transcript·meta·타인의 WIP는 read/cite only입니다. commit 금지, 기존 행 수정/삭제 금지, 미확인 값 추측 금지(⚠️미확인 표기), 모든 분석 주장은 문항번호+transcript line/page를 인용하고 image page를 spot-check하십시오. 문항 수 또는 전사가 불일치하면 고치지 말고 제안서 상단에 flag하십시오.
``

Measured preflight:

| Corpus ID | items from meta.yml | three required artifacts | combined bytes |
|---|---:|---:|---:|
| EX-english-20252M | 32 | 3/3 | 52,997 |
| EX-info-20252M | 25 | 3/3 | 9,780 |
| EX-math2-20252M | 22 | 3/3 | 9,115 |
| EX-science-20252M | 29 | 3/3 | 32,682 |
| EX-social-20252M | 25 | 3/3 | 26,615 |
| EX-history-20252M | 29 | 3/3 | 25,649 |
| EX-korean-20252F | 31 | 3/3 | 82,562 |
| EX-english-20252F | 33 | 3/3 | 54,987 |
| EX-science-20252F | 33 | 3/3 | 26,292 |
| EX-social-20252F | 27 | 3/3 | 26,262 |
| EX-history-20252F | 29 | 3/3 | 26,893 |
| **Total** | **315** | **33/33** | **373,834** |