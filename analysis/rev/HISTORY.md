# analysis/rev/ — 정본·시스템 검토서 홈

> **이 홈은 `output/` 밖 대상**(카탈로그 `catalog/*`, 지침 `*_지침.md`, 표준 문서, 시스템 `web/`·`tools/`,
> 태그 배관 등)의 재검토에서 발견된 문제·의문을 프로젝트 밖 AI와 파일 하나로 주고받기 위한 검토서 모음이다.
> 회차 산출물(문제집) 검토서는 각 산출물 폴더의 `output/<YYMMDD>/rev/`에 둔다 — 구분 근거:
> [`DOC_LOCATION.md`](../DOC_LOCATION.md) §2.
> 규격 정본: [`../REV_GUIDE.md`](../REV_GUIDE.md) · 이력 총괄: [`../REV_LOG.md`](../REV_LOG.md)

## 절대 규칙 (요약)
1. **수정 불간섭** — 검토 주체는 자기가 작성하지 않은 문서(카탈로그, 지침, web/*.js 등)를 직접 수정하지 않는다.
2. 수정 제안은 각 검토서 `<proposed_fixes>` 섹션의 **체크박스 `- [ ]` 승인 요청**으로만 기록한다.
3. 승인된 항목만 작성 주체(item-writer 또는 사용자)가 원본에 반영하고, 반영 사실을 REV_LOG에 기록한다.

## 파일명 규칙
`YYMMDD_NN_NAME.md` — 작성일 / 당일 순번 NN(홈별 독립 채번호) / 영문 스네이크 이름

## 현재 검토서 목록

| 파일 | 제목 | 상태 | 발견 핵심 | 판정 |
|------|------|------|-----------|------|
| [260825_01_tag_pipeline_mismatch.md](260825_01_tag_pipeline_mismatch.md) | 태그 파이프라인 불일치 + 웹 뷰어 상태·영속화 결함 | **approved(판정 반영)** | TAG_RE 공백·답안표 무괴호 미매치 → typeId 배관 전멸 / 섹션 리셋으로 실데이터 문항 0개 파싱(F9 신규) / DF 파싱 부재 / 과목 매핑 누락 / 채점 2상태 / localStorage 한계 — 총 9건 | 결정요청 중 (decision 07~12) |
| [260825_02_catalog_science_factual_errors.md](260825_02_catalog_science_factual_errors.md) | 통합과학 카탈로그 사실 오류·누락 교정 요청 | **approved(판정 반영)** | 출제빈도 주장 156건 중 불일치 19(체계적 스왑 패턴 3종) + 머리말 배점 구조 전도("중간 2점대·기말 3점대"가 실측) + 지도표 26중간 GB 열 누락 + 26기말 역학 0건인데 "5/6회" 서술 — 체크박스 15건 | 결정요청 중 (decision 07~12) |
| [260825_03_catalog_korean_history_misattribution.md](260825_03_catalog_korean_history_misattribution.md) | 한국사 카탈로그 회차·시대 귀속 체계적 전도 | **approved(판정 반영)** | 24기말 내용을 "2025"로·24중간 문항을 "24기말"로 쓰는 전도 다수, **25기말=근대사 단독**이라는 핵심 사실 부재(E-6 신설 필요), 머리말 배점·서답 구조 전도 — 체크박스 7건 | 결정요청 중 (decision 07~12) |
| [260825_04_catalog_english_social_errors.md](260825_04_catalog_english_social_errors.md) | 영어·통합사회 머리말 구조 오류 및 귀속 불일치 | **approved(판정 반영)** | 문항 귀속은 대체로 정확(영어 80/81·통사 52/55), 오류는 머리말 요약치(서답형 개수·배점 하한·서술형 10점 고정 주장)와 **26을 '근거 시험' 병기한 원칙위반**(미분석 자료) 집중 — 체크박스 9건 | 결정요청 중 (decision 07~12) |
| [260825_05_catalog_math_korean_minor.md](260825_05_catalog_math_korean_minor.md) | 수학·국어 카탈로그 요약 수치·단정 표기 묶음 | **approved(판정 반영)** | 귀속·수치 인용은 매우 정확(수학 45/45·국어 36/36). 오류 9건뿐: 배점 상한(4.2→실측 5.0)·중간 문항구조(단답20+서술4)·"유일하게 틀린 문항" 단정(근거는 추정 후보)·국어 배점 1.7~4.0 등 — 체크박스 10건 | 결정요청 중 (decision 07~12) |
| [260825_06_quiz_standard_update.md](260825_06_quiz_standard_update.md) | QUIZ_STANDARD 개정 승인 요청 — DATA_STANDARD v1 정합화 | **approved(판정 반영)** | §1 태그 밀착형만 정의(공백·DF·보조유형 미수용) / 과목 판별 불완전(social·history 누락, math1/2 구분 불가) / §2 스키마 df·aux_types·세트 메타 계약 없음 / 예시 ID T-01·W-01 비등록 접두어 — 총 4건(주요 3·경미 1). 열린 판정 요청 Q4(REV_LOG TSV 전환)·Q5(scope_confirmed 기본값) 포함 | 결정요청 중 (decision 07~12) |

| [260826_01_crlf_frontmatter_and_tsv_export.md](260826_01_crlf_frontmatter_and_tsv_export.md) | CRLF 개행에 의한 프론트매터·선택지 파싱 전면 실패 + 채점 TSV 내보내기 TypeError | **closed(수정 반영)** | Group P 반영보고서 §6 체크리스트 8항목·RV-3·RV-4 재실행은 전건 성립. 그러나 보고서가 검사하지 않은 층에서 3건: **F1** CRLF로 `parseFrontmatter` 전량 실패(`fm={}`) → `setId`가 sourceKey로 폴백·`subject_code`/`scope_confirmed` 우선순위 기능 미작동(JS만, 파이썬 미러는 정상 ⇒ 판정 07 "동작 동일" 위반) / **F2** 같은 원인으로 `LEADING_OPTION_RE` 실패 → **5지선다 전 과목 선택지 0개 파싱**(영어25: `①` 31회인데 옵션 0, 14문항이 essay 오분류) / **F3** `exportTsv`의 `String(v).join` TypeError로 🧾 내보내기 첫 행 즉사(df 비어있지 않은 문항 40/40) | 사용자 지시로 F1~F3 수정·번들 재빌드·재검증 완료. **2차(260826): Q1~Q3도 사용자 판정으로 전부 해소** — ASCII 전용 강제화 · §4.1-A fail_code 신설+웹 귀인 UI(취약 축 제안 기능 복구) · REV_GUIDE §2-b D + §3 rule 4-a 의무화 |

## 검토서 읽을 때 주의
- 각 검토서의 `<document>` 인용은 **작성 시점 원본 그대로**다.
  승인 수정이 반영되면 현재 원본과 달라지므로 이후 검토는 새 스냅숏으로 한다.

## 회신 처리 흐름
회신 도착 → 해당 검토서에 회신 기록 + status 갱신 → 체크박스 승인 확인 →
승인 항목 반영(작성 주체 수행) → [`../REV_LOG.md`](../REV_LOG.md) 에 반영 기록 →
원칙 4에 따라 해당 유형 카탈로그 금지·주의에 피드백 기록

---
## 폴더 이력 (append-only)
- 260825 **홈 신설·이원화 확립** — 계기: 사용자 지적 "카탈로그 검토서가 output 회차 폴더에 저장됨".
  [`문서위치_표준.md`](../DOC_LOCATION.md) §2에 따라 output/ 밖 대상의 검토서는 본 홈으로 이동하기로 표준화하고,
  기존 `output/260825/rev/`에 섞여 있던 6건을 모두 이전했다:
  ① tag_pipeline(웹 시스템) ②~05 catalog_* (카탈로그 검산) ⑥ quiz_standard_update(docs/QUIZ_STANDARD).
  이전과 동시에 REV_LOG 링크 갱신 + REV_지침 §1 위치 규칙 개정 반영.
- 260825 이력 이관: 구 `output/260825/rev/HISTORY.md`의 폴더 이력 3건(tag_pipeline 신설, QUIZ_STANDARD 개정 요청,
  카탈로그 4건 추가)은 내용 보존해 위 목록·본 이력으로 흡수했다. 구 HISTORY는 소멸(내용 손실 없음).
  ※ 당시 `260825_02_quiz_standard_update.md`로 표기됐던 링크는 실물 파일명 `260825_06`으로 바로잡았다(번호 충돌 해소 — NN은 홈별 도착 순번).
- 260825 재번호 결정 기록 — **사용자 판정: 선착순 유지·후발 재번호.** quiz_standard_update는 동일 세션군 카탈로그
  검토서 02~05가 선행 등록됨에 따라 02→06으로 확정했다(위 ※ 주석의 근거). 검토서 본문 내용은 무변경.
