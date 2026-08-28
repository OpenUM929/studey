---
title: "origin_data 실데이터 시나리오 테스트 · 마이그레이션 이행 대장"
created: 2026-08-25
author: main-loop
status: 반영
related: "260825_01_artifact_management_prd.md"(§2 시나리오 검증·§9 승인 항목) · "../../docs/DATA_STANDARD.md" · "../../corpus/HARVEST_LOG.tsv"
---

# 대장 02 — origin_data 실데이터 검증 및 마이그레이션 이행

> PRD [`260825_01`](260825_01_artifact_management_prd.md) §2의 가상 시나리오를 **실제 보유 자료 55건 전수**로 재검증하고,
> 사용자 승인(260825 "문제 없으면 작업")에 따라 A6·A7·A8을 실행한 기록이다. 원장의 단일 참조점은
> [`../../corpus/HARVEST_LOG.tsv`](../../corpus/HARVEST_LOG.tsv)이며, 본 문서는 그 근거·판정을 서술한다.

## 1. 실측 결과 — 설계 판정

전수 조사(origin_data 42건 + test 8건 + raw 5건 = **55건**)를 신규 코드체계에 매핑한 결과:

| 판정 | 내용 |
|------|------|
| ✓ 매핑 성립 | 55건 전부 자료성격(EX/NY/SUP)×subject_code×회차코드로 ID 발급 가능 — 미등류 유형 0 |
| ✓ 이동 충돌 0 | 19건 이동 dry-run에서 MISSING/COLLISION 0건, 실행 후 빈 폴더(26_1_1·test) 소멸 확인 |
| ⚠ 발견 D1 | `raw/` PNG는 수행평가가 아니라 **2026 1학기 공식 정답지 스캔 4건**(중간·기말 × 선택형·단답형). `extracted/INDEX.md`의 "2026 공식 정답지 없음"은 오류 — `analysis/student/종합진단_리포트_v2.md`의 `raw/정답/` 인용이 정확했음. PRD §9-A5의 "수행평가 추정" 가설 기각 |
| ⚠ 발견 D2 | data.zip은 git 미추적(`.gitignore` origin_data/) → 삭제 시 복구 불가. **A8 방식 변경: 삭제 → `_archive/` 격리** |
| ⚠ 발견 D3 | 2024·2025 레거시 폴더는 PRD §8 "레거시 유지" 원칙에 따라 물리 이동 없이 ID만 소급 부여 |

**판정: 결함 3건 모두 운용 파라미터 조정으로 흡수 — 설계 유효, 작업 진행 확정.**

## 2. 코퍼스ID 전수 배부 (소급)

### 2.1 이동한 자료 (물리 위치 변경 — 19건)

| 코퍼스ID | 원위치 | 현위치 | variant | 구 파일# |
|----------|--------|--------|---------|----------|
| EX-math1-20261M / -20261F | origin_data/26_1_1/1학년1학기_공통수학1_{중간,기말}.pdf | origin_data/EX-math1-20261M/F/ | student | #26·27 |
| EX-english-20261M / -20261F | 〃 공통영어1 | origin_data/EX-english-20261M/F/ | student | #28·29 |
| EX-science-20261M / -20261F | 〃 통합과학1 | origin_data/EX-science-20261M/F/ | student | #30·31 |
| EX-social-20261M / -20261F | 〃 통합사회1 | origin_data/EX-social-20261M/F/ | student | #32·33 |
| EX-history-20261M / -20261F | 〃 한국사1 | origin_data/EX-history-20261M/F/ | student | #34·35 |
| NY-math1-2021 | test/2021_1_중간_{문제,답}_상산고등학교.{pdf,txt} | origin_data/NY-math1-2021/ | master | #38 |
| NY-math1-2022 | test/2022_… | origin_data/NY-math1-2022/ | master | #39 |
| — (data.zip) | origin_data/data.zip | origin_data/_archive/data.zip | — | #36·48 |

### 2.2 제자리 소급 등록 (레거시 유지 — 24 유닛 + 특기 사항)

- `EX-{korean,math1,english,science,social,history}-2024{1M,1F}` ×12 ← `origin_data/2024_1학기_1학년_{중간,기말}/`
- `EX-{…}-2025{1M,1F}` ×12 ← `origin_data/2025_1학기_1학년_{중간,기말}/`
- 회차 공용 정답지 6건(2024 선택형+서답형 ×2세트, 2025 통합본 ×2): subject_code 미등록으로 **코퍼스ID 보류** — 소속 회차 유닛의 note로 추적(HARVEST_LOG 동반 기재)
- 2025 중간 통합과학 스캔 중복 PDF(#17): 중복 유지, note 기재
- `raw/정답/*.png` ×4(D1): **raw/ 현위치 유지** — `종합진단_리포트_v2.md`가 해당 경로를 근거로 인용 중이므로 이동 시 stale 참조 발생. 2026-1M/F 정답지 스캔으로서 INDEX.md 등재는 신규 승인 항목(A12)으로 요청

## 3. 생성·변경 산출물 일람

| 산출물 | 조치 | 클래스 |
|--------|------|--------|
| corpus/HARVEST_LOG.tsv | **신설**(UTF-8 BOM) — 37 유닛 소급 등록 + SUP 1행 | LOG |
| origin_data/EX-*-20261M/F ×10 | 신설 폴더 + PDF 이동 | RAW |
| origin_data/NY-math1-202{1,2} ×2 | 〃 (구 test/ 추적 파일 — 이동으로 구 경로 D 스테이징, 신규 경로는 gitignore 영역 → A14) | RAW |
| origin_data/_archive/data.zip | 격리 이동 | RAW |
| analysis/EXTRACTION_LOG.md | 이동 기록 행 M1~M3 append + 이력 | LOG |
| extracted/INDEX.md | 대응표·매트릭스 현위치 갱신 + raw/정답 발견 반영 + 이력 | IDX |
| 260825_01 PRD | A6·A7·A8 체크박스 반영, A5 판정 갱신, Q1 해소, 이력 | PLAN |
| test/ · origin_data/26_1_1/ | 소멸(빈 폴더) | — |

## 4. 미해결 · 후속

> **O1 동기화(260825 후반)**: 아래 체크박스를 PRD 실행 실황과 일치시켰다. 완료 판정 근거는
> 각 항목이 가리키는 PRD 행이다. 원래 텍스트는 이력 보존 원칙에 따라 내용을 덧붙이는 방식만 사용.

- [x] **A14** `.gitignore` 처리 — NY-math1-* 추적 유지 완료(`origin_data/*` + `!origin_data/NY-math1-2021/`·`!…2022/` + SUP 예외, git check-ignore 검증 통과). 실행 기록: PRD 그룹 C A14.
- [x] raw/README.md 내용 정정 — **A13**으로 실행됨(실태 2026 정답지 스캔 4건 반영 재작성). PRD 그룹 B A13.
- [x] A1(DATA_STANDARD 패턴 v2 교체)·A2(파일명 개정)·A3(forecast 규격)·A4(CLAUDE.md 경로)·A9(extracted/README)·A15(ANL 규격) — 전부 승인·실행 완료(PRD 그룹 A~E).
- [x] **A10** student 6건 파일명 소급 표준화 — 초기 보류 결정 → Group K5 로마자화 스윕으로 실질 해소(PRD A10 흡수 종결 주석 참조).
- [x] **A12** 정답지류 회차 공용 자료 취급의 DATA_STANDARD §1.3 명문화 — 사용자 결정("§1.3 명문화")으로 Group O2 실행 완료(§1.5 신설·v1.7 이력).
- [x] **A11** P1 착수 시 신규 ID 규칙 우선 적용 선언 — Group O3의 P1 착수와 함께 소화(계획서 이력 행).
- 학생 분석 문서들(`analysis/student/*`)이 인용하던 `26_1_1` 경로는 역사적 기록으로 유지 — 현 위치는 HARVEST_LOG·본 대장으로 조인
- git commit 시 사용자 지시 필요(본 세션은 커밋하지 않음)

## 이력
- 260825 작성 — 메인루프. 실데이터 검증(D1~D3) → 사용자 승인 범위 내 A6·A7·A8 실행, HARVEST_LOG 신설.
