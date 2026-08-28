---
title: "산출물 관리 표준화 PRD — 코드체계·정제 파이프라인·파일명 표준"
created: 2026-08-25
author: main-loop
status: 대기
related: "../../docs/DATA_STANDARD.md" · "plan_3layer_architecture.md"(하부 실행계획) · "../../analysis/문서위치_표준.md"
---

# PRD 01 — 산출물 관리 표준화: 코드체계 · 정제 파이프라인 · 파일명 표준

## 0. 이 문서의 성격과 경계

- 본 문서는 산출물 관리 전반의 **최상위 프레임**이다. [`plan_3layer_architecture.md`](plan_3layer_architecture.md)(corpus/student/share 3층)는
  본 PRD가 정의하는 코드체계를 따르는 **하부 실행계획**으로 참조하며, 서술 중복을 만들지 않는다.
- 스키마·enum의 단일 정본은 [`../../docs/DATA_STANDARD.md`](../../docs/DATA_STANDARD.md)다. 본 PRD의 신설 코드는
  그 §1.3 ID 레지스트리에 **등록하는 방식**으로 착수한다(승인 항목 A1). 충돌 시 DATA_STANDARD이 우선한다.
- 기존 문서(CLAUDE.md·README·지침)의 수선은 전부 §9 체크박스 승인 대상이며, 본 문서는 직접 수정하지 않는다(원칙 8).
- **파일명 지침(사용자 260825)**: 마크다운 문서는 전부 `YYMMDD_NN_<영문snake>.md`로 만든다. 본 문서부터 적용한다(§5).
- **달성 목표의 정의(260825 개정 — C1)**: "기존 결과물과 같은 결과"란 — **D클래스(결정론적 산물)는 완전 재현**,
  **G클래스(생성형 산물)는 형식 재현 + 품질 계약 준수**를 뜻한다(§6.1). LLM 생성 단계(카탈로그 판독·출제·분석 서술)에
  내용까지의 재현을 요구하지 않는다 — 원리적으로 비결정론이므로, 검증(solve-back·검토)으로 대체한다.

## 1. 목적·배경 — 갭과 사건

"현재 불일치 수선"만이 목적이 아니다. 목적은 **코드 등록제**로 미래의 모든 자료(신규 과목·회차·수행평가·새 형식)를
기존 규칙 변경 없이 흡수하는 것이다. 실태 조사로 확인된 갭:

| # | 갭 | 근거 |
|---|-----|------|
| G1 | CLAUDE.md가 `data/raw/`를 참조하나 실체는 `origin_data/`+`raw/` 병존, 역할 분담 모호 | CLAUDE.md 원칙 1 ↔ 실태 |
| G2 | `origin_data/` 폴더명 불균일: `2024_1학기_1학년_중간` / `26_1_1` / `data.zip` | 실태 |
| G3 | 루트 `test/`(2021·22 수학 내신기출집)가 4계층 어디에도 미귀속 | extracted/INDEX.md §1 |
| G4 | 수행평가(반영비율 **40%**, 최중축) 자료 0건 — 도착 시 배치·ID·차수 규칙 미완성 | extracted/README 우선순위 축 |
| G5 | 산출물 규격이 문서위치_표준 §3 / DATA_STANDARD §2 / forecast README 등에 분산, 단일 진입점 부재 | 각 문서 |
| G6 | **정제 파이프라인 부재** — 원본 파일명 비일관(HWP·PDF·스캔 이미지 혼재), 표준명 부여 규칙 없음 | 실태 |
| G7 | **파일명 미정의 클래스** — 학생분석 무날짜·`_v2` 접미(`종합진단_리포트_v2.md`), `_partN_` 임시물 무규칙 | analysis/student/, output/260822/ |

법제화할 사건 2건(병렬 세션):

1. **검토서 번호 충돌** — `_02_quiz_standard_update` 선등록 건과 충돌 → 사용자 판정 "선착순 유지·후발 재번호"로 02→06
   ([../../analysis/rev/HISTORY.md](../../analysis/rev/HISTORY.md)). 본 PRD는 이 규칙을 모든 순번 채번으로 일반화한다(§5.3).
2. **rev 홈 이원화** — 문서위치_표준 신설로 `output/…/rev/` → `analysis/rev/` 이전, 링크 수선이 뒤따름
   ([../../analysis/문서위치_표준.md](../../analysis/문서위치_표준.md) §5). "이동·개명은 반드시 로그에 남긴다"를 일반 규칙으로 격상한다(§5.6).

## 2. 시나리오 검증 — 신규 기출 도착 드라이런

> 설계가 실제로 성립하는지, 자료 도착부터 약점 처방까지 전 단계를 가상 자료로 추적해 검증했다.
> **대상 자료**: ① 「1학년1학기_공통수학2_중간.hwp」(고사원안) ② 「수학 중간 정답.pdf」(선택형+서답형 정답지) ③ 수행평가 2차수 스캔 PNG

### 2.1 S1 트레이스 — 기출 HWP+정답지

| 단 | 행위 | 출력물 | 상태코드 | 판정 |
|----|------|--------|----------|------|
| 0 도착 | `origin_data/_inbox/` 에 원본 보관(개명 금지) | 원본 그대로 | arrived | ✓ |
| 1 등록 | EXTRACTION_LOG 중복 확인 → 코퍼스ID 발급 → HARVEST_LOG append | `EX-math2-20262M` | arrived | **V1 발견** |
| 2 정제 | `corpus/EX-math2-20262M/` 골격 생성: meta.yml + source.txt(HWP→표보존) + answers.txt(정답지 변환) | 표준명 파일군 | normalized→extracted | **V2·V3·V4 발견** |
| 3 추출 | 스캔 필요 시 pages/pNN.png 렌더(dpi130+) | 페이지 렌더 | extracted | ✓ |
| 4 분석 | catalog/공통수학2.md 유형 갱신(SM2-xx) → index.tsv 재생성 | 카탈로그·인덱스 | analyzed | ✓ (도구 명세 기존) |
| 5 예측 | forecast 보고서 저장 | `260915_2026-2M-math2.md` | — | **V5 발견**(파일명 규격 충돌) |
| 6 출제 | output/<YYMMDD>/ 세트 생성 + solve-back 전수 검증 통과 후 공개 | `261009_01_math2_midterm30.md` + frontmatter set_id | — | ✓ (웹 파서는 폴더명=sourceKey, 파일명 미사용 — 무손상 확인) |
| 7 검토 | 회차 산출물이므로 `output/<YYMMDD>/rev/` | 검토서 | — | ✓ (문서위치_표준 §2) |
| 8 채점 | 웹 export TSV → import_grading 검증 → ATTEMPT_LOG append | student/S01/ATTEMPT_LOG.tsv | — | ⚠ **설계 존재** — 도구·원장 미구축(3층 P1~P3 대기) |
| 9 약점 | WEAK_LEDGER 상태 전이 + 오답분석 MD | `analysis/student/261010_math2_오답분석.md` | — | ⚠ **설계 존재** — 〃 + ANL 규격 미제정(A15) |
| 10 공유 | build_report → 단일 HTML + SHARE_LOG append | reports/261010_report.html | — | ⚠ **설계 존재** — 도구 미구축(3층 P3 대기) |

> ⚠ 판정 기준 개정(P3): 8~10단은 '설계 참조 가능'까지만 확인된 상태이지 동작 가능이 아니다.
> 초기판의 ✓ 표기는 설계 존재와 구축 완료를 구분하지 못한 과대 판정 — 원판은 이력으로 보존한다.

### 2.2 S2 트레이스 — 수행평가(차수 다발)

- 자료성격 **PA** 신설 필요(G4). 회차코드에 차수 `P02` 허용 → 코퍼스ID `PA-math2-20261P02`. §3 설계에 반영 완료.
- CLAUDE.md 원칙 6 자료등급에 수행평가 위치 미정 → **학교 출제 1차 자료로 grade=1**(기출과 동급)로 명문화(§3.1).

### 2.3 검증으로 발견된 결함과 해결 (본문 §3~§5 설계에 반영 완료)

| # | 결함 | 해결 |
|---|------|------|
| V1 | DATA_STANDARD §1.3 코퍼스ID regex `^[A-Z]{3}-…$`는 3자 고정인데 기존 EX(기출)·CU(교육과정)는 2자 — **본문과 자체 모순** | 패턴 v2로 교체: `^[A-Z]{2,4}-[a-z0-9]{2,8}-\d{4}([12][MF]\|P\d{2})?$` (A1) |
| V2 | 세그먼트2 대소문자 불일치 — 기존 예 `M2`(대문자) vs 세트ID·과목코드 `math2`(소문자), 조인키 불능 | middle을 subject_code(소문자)로 통일, 기존 `SUP-M2-2026`은 corpus 골격 미생성 상태라 개명 부담 0 (A1) |
| V3 | 회차 미포함 — 동일 과목·연도에 중간/기말 2건이면 ID 충돌 | 꼬리에 회차 확장: `20262M`(연도+학기+중간) 등 (§3.3) |
| V4 | 정답지·판본(고사원안 vs 학생 응시본) 구분 없음 | 정답지=동일 코퍼스 단위 내 `answers.*` 파일, meta.yml에 `exam_code`·`variant`·`answer_key` 필드 신설 (A1) |
| V5 | forecast 파일명 규격(`<YYMMDD>_<한글 회차>.md`)이 회차코드 체계와 불일치 | 코드화 개정: `<YYMMDD>_<회차코드>-<subject>.md` (A3) |

**판정: 결함 5건 모두 설계 수정으로 흡수 가능 — 정상. 계획 문서 작성을 진행한다.**

## 3. 전역 코드 레지스트리 (신설·수정)

> 스타일: **영문 니모닉**(사용자 확정). 기계층 저장값은 ASCII, 화면만 LABEL_MAP 한글(DATA_STANDARD §0 준수).

### 3.1 자료성격 코드 (코퍼스ID 접두어 — 등록제)

| 코드 | 의미 | grade | 현황 |
|------|------|-------|------|
| `EX` | 기출(중간·기말 고사원안/응시본) | 1 | DATA_STANDARD §1.3 기재 |
| `PA` | **수행평가** — 학교 출제 1차 자료로 grade=1 | 1 | **신설** (A1) |
| `NY` | 내신기출집(출판사) | 2 | **신설** — test/ 2021·22 물질용 (A6) |
| `SUP` | 부교재 | 2 | 기존 |
| `CU` | 교육과정·타교 참고자료 | 3 | 기존 |

- 새 성격의 자료 도착 시: 이 표에 행 추가(승인 후) → 이후 자료는 규칙 변경 없이 흡수된다. 미등록 성격으로 파일을 두는 것을 금지한다.

### 3.2 회차 코드 (시험 식별자의 ASCII 표준)

```
패턴: <YYYY>-<학기 1|2><구분 M|F|P[0-9]{2}>   예: 2026-2M(중간) · 2026-1F(기말) · 2026-1P02(수행 2차수)
LABEL_MAP: M=중간, F=기말, Pnn=n차수 수행평가 — 화면·사람 문서만 한글 병기
```
- 기존 비공식 식별자 `2026-1중간-수학`(EXTRACTION_LOG)은 로그 비고에 병기하고, 신규 행부터 회차코드를 쓴다.
- 수행평가는 회차가 아닌 **차수**로 관리하므로 P 뒤 2자리 일련을 허용한다(S2 반영).
- LABEL_MAP(M=중간·F=기말·Pnn=n차수)의 등록 장소는 DATA_STANDARD §4 enum 코드표다 — A1 범위에 포함(초판 누락분 보강).

### 3.3 코퍼스ID 패턴 v2 (V1~V3 반영 — A1 승인 대상)

```
^[A-Z]{2,4}-[a-z0-9]{2,8}-\d{4}([12][MF]|P\d{2})?$

EX-math2-20262M      2026년 2학기 중간 수학 기출
PA-science-20261P01  2026년 1학기 1차수 과학 수행평가
SUP-math2-2026       부교재(회차 없음 — 연도만)
NY-math1-2021        내신기출집
```
- middle = `subject_code`(DATA_STANDARD §5.8 표)와 **동일 문자열** → index.tsv·세트ID와 직접 조인.
- 기존 `SUP-M2-2026` → `SUP-math2-2026` 소급 개명. corpus 골격(meta.yml 등)은 여전히 미생성이나, **HARVEST_LOG.tsv는
  260825 생성되어 37유닛이 이미 v2 체계로 등록돼 있다** — 따라서 A1 미승인 기간에는 원장 데이터가 구 정본 regex 위반 상태로
  존재한다(정본↔운용 괴리. 해소는 §9 그룹 A).
- 문항ID는 기존대로 `<코퍼스ID>-Qnn`.

### 3.4 산출물(문서) 클래스 코드 — 색인표 §6의 키

SET(문제지)·REV(검토서)·PLAN(계획서)·FCST(예측)·ANL(오답분석)·RPT(리포트)·IDX(색인·대장)·LOG(누적 로그).
새 산출물 유형 발생 시 여기에 코드 등록 후 사용. 코드 없는 신규 md 생성 금지.

### 3.5 정제 상태 코드 (EXTRACTION_LOG 상태 열의 확장)

```
arrived(도착) → normalized(표준명·meta 완비) → extracted(텍스트/페이지 변환) → analyzed(카탈로그 반영)
```
- 기존 `미착수→추출완료→분석완료`와 대응. 도착 즉시 `arrived` 행을 남겨 "미처리 잔여"가 로그에 보이게 한다.
- 폐기는 상태 `deprecated` + `_archive/` 격리(삭제 금지).

### 3.6 접두어 등록제 재확인

QUIZ_STANDARD 예시의 `T-01`·`W-01`은 미등록 접두어다(검토서 [../../analysis/rev/260825_06_quiz_standard_update.md](../../analysis/rev/260825_06_quiz_standard_update.md) QS-4, 대기).
본 PRD는 등록제 원칙을 재확인하며, 개정 자체는 06번 검토서 승인 범위로 위임한다(중복 금지).

## 4. 정제 파이프라인 표준 (G6)

> 어떤 형식이 와도 같은 골격으로 흡수된다. 정제 깊이는 **페이지 단위 우선**(사용자 확정) — 문항 컷(`-Qnn.png`)은 출제·태깅에 필요해졌을 때 그때 만든다.

```
origin_data/_inbox/            도착 스테이징 (무엇이든 여기 둔다)
   │ ①EXTRACTION_LOG 중복확인 ②코퍼스ID 발급 ③HARVEST_LOG append
   ▼
origin_data/<코퍼스ID>/         원본 최종 보존 (읽기전용, 폴더명=코퍼스ID → corpus와 1:1)
   +
corpus/<코퍼스ID>/              작업 정제본
   ├── meta.yml                §5.7 확장 스키마(A1): id·title·grade·variant·exam_code·pages·items·transcribed_at·method·confidence·answer_key·catalog_ref
   ├── source.txt              HWP→텍스트(표보존) 또는 PDF 텍스트층 추출
   ├── pages/pNN.png           스캔·이미지 자료의 페이지 렌더 (PyMuPDF dpi130+, 회전 보정)
   └── answers.txt             정답지 변환 (있을 때; answer_key로 참조)
```

포맷별 처리 경로:

| 입력 형식 | 처리 | 산출 | 검증 |
|-----------|------|------|------|
| PDF (텍스트층 있음) | 텍스트 추출 | source.txt | 머리말 배점·문항수 대조 |
| PDF (스캔) | PyMuPDF 렌더 | pages/pNN.png | Read 판독, dpi130+ |
| HWP | 표보존 변환 | source.txt | 표 소실 시 _archive 격리(기존 선례) |
| 이미지(JPG/PNG) | 이름 정규화+필요시 병합 | pages/ | 〃 |
| TXT | 인코딩 UTF-8 통일 | source.txt | 개행·깨짐 확인 |

- **판본 구분**(V4): 같은 시험이라도 고사원안(`variant: master`)과 학생 응시본(`variant: student`)은 **별도 코퍼스ID**로 등록한다
  — 26_1_1이 학생본이었던 전례에서 배점·구조 판독 오류를 방지하는 장치.
- 정제 완료 시 EXTRACTION_LOG 상태 갱신 + INDEX.md(레거시) 또는 corpus 메타(신규)에 반영.

## 5. 파일명 표준 (G7 — 사용자 지침 반영)

### 5.1 설계 원칙

1. **마크다운 문서는 전부 `YYMMDD_NN_<영문snake>.md`** (사용자 지시 260825). 사람이 읽는 제목은 파일 안 H1·frontmatter title이 담당한다.
2. 데이터 파일(TSV·YAML·PNG·HTML)은 각 스키마의 고정명 또는 코드 조합형을 따른다(§5.6 예외).
3. 날짜는 YYMMDD(§1.1), 세그먼트 구분 `_`, 코드 내부 `-`, 공백·한글 파일명 금지(납품물 H1 한국어 제목은 허용).
4. 기계 소비 파일명은 ASCII 코드 조합, 사람 큐레이션 문서 제목은 한국어 — DATA_STANDARD 2층 원칙의 파일명 확장.

### 5.2 전 클래스 파일명 통합표 (단일 진입점)

| 클래스 | 패턴 | 예 | 근거 |
|--------|------|-----|------|
| 검토서 REV | `YYMMDD_NN_<snake>.md` | `260825_06_quiz_standard_update.md` | 기존 확립 유지 |
| 계획서 PLAN | `YYMMDD_NN_<snake>.md` (**plan_* 접두 폐지**, A2) | 본 문서 `260825_01_artifact_management_prd.md` | 사용자 지시 |
| 문제지 세트 SET | `output/<YYMMDD>/<YYMMDD>_NN_<subject>_<snake>.md` (A2) | `261009_01_math2_midterm30.md` | 〃 — H1에 한국어 제목, set_id는 frontmatter |
| 예측 FCST | `<YYMMDD>_<회차코드>-<subject>.md` (A3) | `260915_2026-2M-math2.md` | V5 해소 |
| 오답분석 ANL | `<YYMMDD>_<subject_code>_<영문snake>.md`(내용 규격 = analysis/student/_README) | `261010_math2_wrong_analysis.md` | G7 신설 · A15 제정 완료 |
| 리포트 RPT | `<YYMMDD>_report.html` | 기존대로 | DATA_STANDARD §2 |
| 누적 로그 LOG | 고정 대문자 스네이크 | `ATTEMPT_LOG.tsv` | DATA_STANDARD §5 |
| 코퍼스 정제본 | `<코퍼스ID>_…` / `pNN.png` | `EX-math2-20262M_source.txt` | §4 |
| 추출물(레거시) | `<과목약칭>.txt` | extracted/ 현행 유지 | extracted/README |
| 임시 조각 | `_partN_<이름>.md` — 선행 `_`=비납품 표시, 납품 시 본문 통합 후 소거 | `_part1_평면좌표.md` | G7 신설 규정 |

### 5.3 채번·충돌 규칙 (사건 1의 일반화)

- NN = **같은 폴더(홈)에서 같은 날짜에 만들어지는 순번**, 01부터, 홈별 독립 채번.
- 충돌 발생 시 **선착순 유지·후발 재번호**(사용자 판정 260825, HISTORY 기록 준용). 재번호 시 본문 무변경·이력 한 줄.
- 폴더가 다르면 번호가 겹쳐도 무관(output/260825/의 01과 analysis/rev/의 01은 독립 — 기존 규칙 준용).

### 5.4 버전 규칙

- `_v2` 류 버전 접미 **금지**. 개정은 append-only 정신으로 새 날짜 파일로 만들고 이전 파일은 유지 또는 `_archive/`.
- 소급 대상: `analysis/student/종합진단_리포트_v2.md` 등 6건 → A10.

### 5.5 이동·개명 로깅 (사건 2의 일반화)

- 모든 이동·개명은 담당 로그(REV_LOG·EXTRACTION_LOG·HARVEST_LOG)에 **새 행**으로 기록하고, 기존 행은 삭제하지 않으며
  링크 href만 갱신한다(문서위치_표준 §4 준용).

### 5.6 예외(고정명) 목록

`CLAUDE.md` · `README.md`/`INDEX.md`(폴더 진입점) · `HISTORY.md`(rev 진입점) · TSV 원장 6종 · `meta.yml` · `web/`·`tools/` 빌드 산출물.
이들은 클래스 코드 대신 고정명으로 식별되며, 색인표 §6에 등재된 것만 허용한다.

## 6. 산출물 색인표 — 단일 진입점 (G5)

> 어떤 문서를 만들 때: ①클래스 찾음 → ②위치·파일명 확인 → ③규격 정본으로 이동. 이 표가 유일한 들어갈 자리 판단기이며,
> 문서위치_표준·DATA_STANDARD §2와 충돌 시 원본 정본이 우선한다(본 표는 색인일 뿐).

| 클래스 | 위치 | 파일명(§5) | 규격 정본 |
|--------|------|------------|-----------|
| SET 문제지 | output/<YYMMDD>/ | §5.2 | QUIZ_STANDARD(+06 개정 대기) |
| PLAN 계획서 | output/<YYMMDD>/ | §5.2 | DATA_STANDARD §2 |
| REV 검토서 | output/<YYMMDD>/rev/ 또는 analysis/rev/ | §5.2 | REV_지침 |
| FCST 예측 | analysis/forecast/ | §5.2 | 시험예측_지침 §5 |
| ANL 오답분석 | analysis/student/ | §5.2 | **student/_README.md**(A15 제정) — 원장은 TSV, ANL은 서술층(§6.1) |
| RPT 리포트 | student/<학생ID>/reports/ | §5.2 | DATA_STANDARD §2 |
| IDX 대장 | extracted/INDEX.md 등 | 고정명 | 각 README |
| LOG 로그 | analysis/·student/·share/·corpus/ | 고정명 | DATA_STANDARD §5 |
| COR 정제 자료 | corpus/<코퍼스ID>/ | §4 | DATA_STANDARD §5.7(v2) |
| RAW 원본 | origin_data/<코퍼스ID>/ | 코퍼스ID | §4 |

### 6.1 재현성 등급 — D클래스와 G클래스 (P1·P2 해소)

LLM 생성 단계는 비결정론이므로 "같은 결과"의 의미를 이원화한다:

| 클래스 | 산물 | 재현 보장 범위 | 품질 계약 |
|--------|------|----------------|-----------|
| **D(결정론적)** | 폴더 구조·파일명·코퍼스ID 발급·TSV 원장 행·meta.yml·로그 행·INDEX 갱신 | 입력이 같으면 결과 **100% 동일** — 규칙·도구로 강제 | 스키마·enum 위반 거부(DATA_STANDARD §6), 파일명 패턴 검사(A15와 함께 도구화 검토) |
| **G(생성형)** | 카탈로그 유형 블록·문제 세트 본문·오답분석 서술·예측 보고서 본문 | **형식만 재현**(파일명·frontmatter·필수 섹션·태그 표준형) | 내용 품질 = solve-back 전수 검증(출제) + 검토서 절차(정본) |

- 판정 문장: *같은 자료를 넣으면 같은 자리에 같은 이름의 파일이 생긴다(D). 그 내용은 같은 형식을 지키되 같다는 보장은 없고,
  검증을 통과해야 납품된다(G).*
- [x] **C1** 이 이원 모델 **채택** — 기술적 필연(LLM 비결정론)상 유일한 정의 가능 형태라 확인 절차 없이 확정함(§9 그룹 0 참조).

## 7. 생애주기 × 담당 주체

| 단계 | 입력 → 출력 | 주체 | 상태(260825 실측) | 근거 |
|------|-------------|------|--------------------|------|
| 도착·등록 | 자료 → 코퍼스ID·로그 행 | type-extractor | 🟢 구축(HARVEST_LOG 38행 운용 중) | CLAUDE.md 작업흐름 |
| 정제·추출 | 원본 → corpus 골격 | type-extractor | 🟡 절차 확립(수동 — meta.yml 스키마는 A1 대기) | §4 |
| 유형 분석 | corpus → 카탈로그·index.tsv | type-extractor | 🟢 구축(카탈로그 7과목+공통수학2) | 〃 |
| 예측 | 카탈로그 → FCST | 메인루프 | 🟡 절차 확립(실적 0건 — 폴더만 신설) | 시험예측_지침 |
| 출제·검증 | 카탈로그 → SET + solve-back | item-writer → solve-back-verifier | 🟢 구축(모의40 등 실적) | 통과 전 비공개 |
| 검토 | 산출물·정본 → REV | rev-writer | 🟢 구축(rev 6건 운용) | REV_지침 |
| 채점·약점 | TSV → ATTEMPT_LOG·WEAK_LEDGER·ANL | import_grading + 사람 판정 | 🔴 **설계 only** — 3층 P1~P3 착수 전 + A15 | 3층 계획 D1~D9 |
| 공유 | 원장 → RPT + SHARE_LOG | build_report | 🔴 **설계 only** — 〃 | 〃 |

> 🟢=실적 있음 또는 운영 중 · 🟡=규칙은 확립, 실무는 수동 · 🔴=문서상 설계만 존재(현재 동작 불가).
> 파이프라인이 끝까지 작동하려면 🔴 2단 해소(3층 착수+A15)가 선행된다.

## 8. 디렉터리 목표 구조 (신규 부분만 — 3층 계획 §3과 합쳐짐)

```
origin_data/
  _inbox/                      도착 스테이징
  <코퍼스ID>/                   신규 원본 (예: EX-math2-20262M/)
  EX-*-20261M/F/ · NY-math1-*/  이전 완료(260825 — A7·A6)
  2024·2025 레거시 폴더         유지 확정(D3) — ID만 소급, HARVEST_LOG 참조
  _archive/data.zip            격리 완료(A8 변경 실행)
corpus/
  HARVEST_LOG.tsv              생성 완료(260825 — 37유닛)
  <코퍼스ID>/                   정제 골격(meta.yml 등) — 미생성(P1 착수 대상)
extracted/                     레거시 동결 (신규 유입 금지, INDEX.md로 참조 유지)
raw/                           현위치 유지(A5 판정 — 2026 정답지 스캔 4건) · README 정정은 A13
```

## 9. 승인 요청 (체크박스 — 승인된 항목만 작성 주체가 실행)

> 원칙 8에 따라 기존 문서 수정·파일 이동은 전부 아래 승인 후 실행한다.
> **종속성(P6)**: 그룹 0 → A 미승인 시 그룹 B·C의 신규 코드·파일명이 정본 위반 상태로 누적된다. 그룹 B 내에서는 A10을 A15 이후로.

### 그룹 0 — 본 개정의 전제
- [x] **C1** 재현성 D/G 이원 모델 **채택**(§6.1) — 기술적 필연(LLM 비결정론)에 따른 정의 확정으로 사용자 확인 없이 채택.
      다른 정의가 필요하면 이력에 남기고 §10을 다시 협의한다.

### 그룹 A — 정본 반영 (최우선 · 타 그룹의 전제)
- [x] **A1** DATA_STANDARD v1.1 개정: §1.3 코퍼스ID 패턴 v2(EX·PA·NY 등재·subject_code 통일) + 회차코드 등록, §4.6 LABEL_MAP 신설, §5.7 meta 필드(exam_code·variant·answer_key) — 260825 실행(사용자 일괄 지시 "표준화 마무리" 경유). HARVEST_LOG 37행과의 괴리 해소
- [ ] **A11** 3층 계획서 P1(corpus 골격+S01 템플릿+WK-01 시딩) 착수 시 §3.3 신규 ID 규칙 우선 적용 선언(계획서 이력 한 줄) — *P1 착수 시점에 실행*

### 그룹 B — 파일명·경로 수선
- [x] **A2** DATA_STANDARD §2 파일명 개정 — 계획서(`plan_*` 폐지)·문제지 세트 `YYMMDD_NN_*` 통일 + 예측·오답분석 클래스 추가 — 260825 실행. 기존 plan_3layer_architecture.md는 레거시 유지
- [x] **A3** forecast/README 파일명 규격 코드화: `<YYMMDD>_<회차코드>-<subject>.md` — 260825 실행
- [x] **A4** CLAUDE.md 원칙 1 경로 수선 — `data/raw/` → `origin_data/`·`corpus/` — 260825 실행
- [x] **A13** raw/README.md 재작성 — 실태(2026 정답지 스캔 4건)·코퍼스ID 보류 방침·신규 유입 금지 반영 — 260825 실행
- [x] **A9** extracted/README.md 오타(`수행평기`) 수정 + 레거시 동결 선언 + 도착 절차를 corpus 경로로 개정 — 260825 실행
- [x] **A10** analysis/student 6건 파일명 소급 표준화 — 초기 **보류 결정(260825)**: 외부 인용 15곳 초과(catalog·EXTRACTION_LOG·rev·PROMPT 문서)라 개명 비용 > 편익이라 판단.
      → 이후 Group K5(파일명 로마자화 정책, 260825 후반)에서 역방향 개명 git mv 6건+참조 스윕 +24건/10파일로 **실질 해소** — 본 항목은 K5에 흡수 종결(O1 동기화).

### 그룹 C — 시스템 구축 연동
- [x] **A14** `.gitignore` 예외 — NY-math1-* 추적 유지(`origin_data/*` + `!NY-*` 방식, git check-ignore 검증 통과) — 260825 실행

### 그룹 D — 신규 규격
- [x] **A15** ANL 내용 규격 제정 — [`analysis/student/_README.md`](../../analysis/student/_README.md)(위치는 Q4 판정: catalog/_README 선례 준용).
      파일명 하위 클래스 3종·필수 섹션 6블록·신뢰도 표기 의무·원장 우선 원칙 정의 — 260825 실행

### 그룹 E — 분류 체계 명칭 표준화 + 루트 안내서 (260825 사용자 지시로 신설·실행)
- [x] **F1** 유형·코드 명칭 전수 조사 → [`analysis/catalog/CODE_REGISTRY.md`](../../analysis/catalog/CODE_REGISTRY.md) 제정.
      접두어 등록표(SM·SM2·K·T/W·F·과학 7종), 코드 패밀리 네임스페이스(C-07↔C7 등 혼동 쌍 구분법),
      subject_code↔접두어 매핑, 신규 부여 규칙 5조
- [x] **F2** **F 접두어 이중 소속 충돌 판정**(치명): `F-nn`이 통합사회(1~7)·한국사(1~8)에 동시 존재.
      조인키 용도에서 단독 인용 금지 + 파일 스코프 병기(`한국사:F-03`) 강제. 기존 ID 동결(소급 개명 금지)
- [x] **F3** 항목 템플릿 이중 정본 수선: CLAUDE.md(구판·성취기준 있음) vs _README(확장판·성취기준 누락) 불일치 →
      병합판으로 양쪽 동기화 + 상태 enum에 `검증(부교재)` 공식 등록 + 수정 기준을 _README로 지정
- [x] **F4** 루트 `README.md` 신설(사용자 지시) — 폴더 지도·데이터 흐름·코드 한눈표·운영 규칙 요약·현 상태.
      tools/·web/(기존 미문서화) 포함
- [x] **F5** 루트 방치 자료 「스무년 고1-2.pdf」(7MB, 부교재 원본·git 추적 중) 발견 →
      `origin_data/SUP-math2-2026/` 이동 + .gitignore 예외(추적 유지) + EXTRACTION_LOG M4 행

### 그룹 G — 검증 사료 체계 + 공통유형 절차 + 발견성 (260825 사용자 지시 3건)
- [x] **G1** 분석 이미지 아카이브 — `corpus/_images/<코퍼스ID>/pNN.png` 신설(gitignore, meta.yml render_dpi·render_tool로 재생성 보장)
- [x] **G2** 단계별 검증 원장 — DATA_STANDARD **§5.7-A verify_log.tsv 스키마**(date|step|target|decision|evidence|reason|confidence|actor). 사유 생략 금지·[판독불가]=unreadable 행 의무·append-only
- [x] **G3** type-extractor 재작성 — 산출 저장처 영구화(`transcript.md`+`_images/`+`verify_log.tsv`; 스크래치패드 유실 문제 해소) + 「공통 패턴 후보」 보고 추가(내용 비종속 출제자 패턴만)
- [x] **G4** 공통유형 정의 확정·승격 절차 — 머리말 명문화(**출제자 패턴 계층** vs 과목유형=내용 결합 유형), 승격 조건(2과목↑ 또는 2회차↑ 반복), **이력 섹션 신설**(기존 부재)
- [x] **G5** CLAUDE.md 자료-도착 흐름 개정 — 산출물 동반 산출 + 공통 패턴 승격 분기 반영
- [x] **G6** 발견성(descriptions) 보강 — **corpus/_README 신설**(유닛 해부도·검증 3중 축), raw/README 역할 문구 추가, README에 corpus 해부도·나침반·흐름도 갱신.
      정본 28곳 머리 서술 감사 → 실결손은 raw/README 1곳뿐(4곳 오탐, 기존 블록인용으로 충분)

### Group H — three-tier review protocol + language policy (260825 user decisions)
- [x] **H1** Tier-2 agent `.claude/agents/rev-auditor.md` NEW — independent re-verify BEFORE reading t1 findings; cross-judgment (agree/disagree/missed defect); write surface = own `*_second.md` + `_index` rows + REV_LOG rows
- [x] **H2** Tier-3 agent `.claude/agents/rev-arbiter.md` NEW — runs in Claude Code (Opus) on the same repo; binding ruling approve / revise-required / reject; writes `*_ruling.md` + one REV_LOG row only
- [x] **H3** Handoff ledger `_index.md` standard form (REV_지침 §1) — append-only round rows, reflect_state `flagged→fixed→re-verified`, the single shared touchpoint between tiers; HISTORY.md stays static registry
- [x] **H4** Round protocol (REV_지침 §3 rewrite) — main-loop driven t1⇄t2 auto loop, max 5 rounds, duplicate-dispute escalation; closure ONLY via user declaration or arbiter approval; status enum pending/in-round/converged/submitted/approved/revise-required/rejected/closed
- [x] **H5** Per-target review criteria (§2-b) — problem sets vs refined corpus artifacts (transcription fidelity, coefficient immutability, item-count triple-match transcript↔meta.yml↔HARVEST_LOG, evidence-page existence)
- [x] **H6** Decision-request package spec (§6 `<rounds>`) · 문서위치_표준 §2 `_index.md` composition update
- [x] **H7** type-extractor amended — meta.yml as 4th deliverable (writer fixed), run-once-and-stop rule, approved fixes applied as verify_log `corrected` rows
- [x] **H8** Language policy adopted — new/updated md content English-first; Korean only in legacy text, proper nouns, existing filenames
- [ ] **H9** (backlog) Migrate legacy Korean canonicals to English (CLAUDE.md body, DATA_STANDARD prose, catalog headers…) — awaits user go-ahead

### Group J — role re-partition + authoring round loop (260825 user decisions)
- [x] **J1** `type-proposer.md` NEW (Claude Code Opus) — primary type analysis from refined
      corpus: per-item assignment, consolidation, variation axes, new-entry drafts
      (_README template + CODE_REGISTRY legality), common-pattern candidates; writes
      `output/<YYMMDD>/` proposals (`*_type_analysis` · `*_catalog_update`); never edits canonicals
- [x] **J2** `type-extractor.md` reduced to PURE transcription — classification/consolidation/
      difficulty/traps/common-patterns removed (bias separation); keeps verbatim transcript,
      factual records (cover citations, point values, answer forms, verb counts), meta.yml,
      verify_log transcribe/unreadable rows only
- [x] **J3** REV guide §2-b **C. Proposal documents criteria** added; B narrowed to refined artifacts
- [x] **J4** REV guide §3 diagram re-partitioned (refine→propose→review→rule→apply);
      §3-b pipeline mappings added — extraction-analysis chain AND authoring chain
- [x] **J5** Authoring round loop wired (user request "문제 생성도 이런 라운드로"):
      item-writer creates set with `intended_use` → solve-back-verifier MANDATORY pre-gate
      for every set → practice = single tier-1 pass / exam = full t1⇄t2 rounds → arbiter;
      release rule = arbiter approve + user confirmation
- [x] **J6** `item-writer.md` English conversion + intended_use + authoring-owner fix path;
      `solve-back-verifier.md` English conversion + pre-gate positioning (all 260824 criteria preserved)
- [x] **J7** CLAUDE.md workflow rows rewritten (arrival chain · creation · gate · review/release);
      README agents row ×7 + flow diagram proposer chain; DATA_STANDARD v1.4
      (proposal class, actor enum, §5.8 intended_use)

### Group K — filename romanization (260825 user policy: no Korean in guide/deliverable names)
- [x] **K1** 16 canonical files renamed (git mv ×14 tracked + os.rename ×2 untracked-new):
      REV_지침→REV_GUIDE, 시험예측_지침→FORECAST_GUIDE, 문서위치_표준→DOC_LOCATION,
      출제유형_마스터→TYPE_MASTER, 난이도_루브릭→DIFFICULTY_RUBRIC, 공통유형→COMMON_TYPES,
      생성_운영지침→AUTHORING_GUIDE, subject catalogs → subject_code-aligned
      (수학→math1, 공통수학2→math2, 통합과학→science, 통합사회→social, 한국사→history,
      영어→english, 국어→korean, 영어_지문수준→english_passage_level), PROMPT_공통수학2→PROMPT_math2
- [x] **K2** Reference sweep: 144 replacements across 24 living docs (CLAUDE.md · README ·
      DATA_STANDARD · TYPE_CATALOG · catalog canonicals · agents ×7 · forecast/extracted READMEs);
      composite listing line fixed manually; content-level Korean untouched by design
- [x] **K3** Historical preservation: output/** bodies, analysis/rev/** reports, append-only logs
      (EXTRACTION_LOG · REV_LOG · HARVEST_LOG rows) NOT rewritten — old names remain as snapshots
- [x] **K4** DATA_STANDARD history v1.5 recorded
- [x] **K5** (extension during verification) analysis/student legacy deliverables romanized too —
      사회_한국사_영어_오답분석→wrong_analysis_social_history_english · 수학_오답분석→wrong_analysis_math ·
      종합보고서→comprehensive_report · 종합진단_리포트_v2→comprehensive_diagnosis_report_v2 ·
      통합과학_오답분석→wrong_analysis_science · 학습코칭_직언_260721→coaching_notes_260721;
      second reference pass (+24 replacements incl. cross-links inside renamed files).
      Final audit: old-name refs in living docs = 0 · Hangul-named canonical files = 0 ·
      21 staged git renames · remaining "broken links" are two known regex false positives.

### Group L — progress-map reporting (260825 user request)
- [x] **L1** All 7 agent definitions gained a mandatory "Progress reporting" opener: canonical
      pipeline diagram with current stage `▲`, stage facts, results, next actor+handoff path;
      blocked runs report `▲ blocked + reason`. Canonical diagrams codified in REV_GUIDE §3 rule 5.

### Group M — forecast pipeline + two-layer persona (260825 user decisions)
- Decisions: dedicated 4-role forecast chain (NOT reuse of rev-*); differential review by
  scope certainty; process overhaul only (no actual report run); persona = fixed layer
  (Sangsang High subject teacher & expert item writer) + variable line `Target cohort:
  grade 1 (2026)`.
- [x] **M1** FORECAST_GUIDE full English rewrite — §0 pipeline & actors, differential
      governance table, term-code filename, downstream obligations wired into §5 template;
      Korean history rows preserved.
- [x] **M2** New agents `forecast-writer`(Opus) · `forecast-reviewer` · `forecast-auditor` ·
      `forecast-arbiter`(Opus) — two-layer persona + progress-map openers + forecast checklists.
- [x] **M3** Persona backfill ×5 (`type-proposer` · `rev-writer` · `rev-auditor` ·
      `rev-arbiter` · `item-writer`). Deliberately NOT backfilled: `type-extractor`
      (pure transcription) and `solve-back-verifier` (blind-solve anti-persona).
- [x] **M4** CLAUDE.md prediction row actor cell filled (was "—").
- [x] **M5** REV_GUIDE: third canonical diagram (forecast) in §3 rule 5 · §3-b Forecast
      mapping paragraph · §5 Actors table +4 rows.
- [x] **M6** README: forecast flow block + shortest-path entry.
- [x] **M7** DATA_STANDARD v1.6 — actor enum +4, history row.

### Group N — six pending reviews processed to decision-request stage (260825 user request)
- Scope: hygiene → ledger instantiation → t2 independent cross-check ×6 → decision
  packages ×6 → bookkeeping. t2 executed by main loop (explore subagents unavailable —
  infra outage; limitation recorded in every *_second.md).
- [x] **N0** HISTORY.md living-header links fixed (DOC_LOCATION·REV_GUIDE); history rows preserved.
- [x] **N1** `analysis/rev/_index.md` created (§1 standard form; 12 rows after t2).
- [x] **N2** Second opinions ×6 (`*_second.md`) — 01: 9/9 CONFIRMED · 02: 5C/2P/7 pass ·
      03: 4C/3P · 04: 5C/1P/4 pass · 05: 8C/1P · 06: 4/4 CONFIRMED. Evidence: regex
      re-runs, machine counts, PNG reads (26중간 p03 · 26기말 p07 · 수학 covers+p07),
      header verbatims. Honest PARTIALs where 2024/2025 table-layout txts blocked
      item-level re-pinning.
- [x] **N3** Decision packages ×6: 260825_07 tag · 08 science · 09 history ·
      10 english/social · 11 math/korean · 12 QUIZ_STANDARD (§6 format, English-first,
      numbered open questions incl. conditional-approval options).
- [x] **N4** Frontmatters 대기→submitted ×6 · HISTORY status column · REV_LOG +8 rows ·
      this block.
- Pending: arbiter rulings (packages relayed by user to Claude Code), then owner-applied
  fixes + principle-4 forbidden/caution entries.

### Group O — PRD residual sweep + 3-layer P1/P3 construction (260825 user approval "순차 진행")
- Scope: ledger sync → A12 codification → plan P1 (+A11) → tools ×4 + dry-run →
  CLAUDE.md row → records. User decisions: full-scope approval · A12 via DATA_STANDARD
  §1.3 codification · NO commits this session.
- [x] **O1** Migration-ledger §4 synced to PRD reality (A13·A14·A1–A4·A9·A15 marked done
      with evidence pointers; A10 annotated as absorbed by Group K5). PRD A10 row updated.
- [x] **O2 = A12** DATA_STANDARD **v1.7**: §1.5 added — round-shared answer keys get NO
      corpus ID (subject_code precondition unmet), tracked via HARVEST_LOG note +
      meta.yml answer_key, INDEX listed with ID `-`, physical location preserved.
- [x] **O3 = plan P1 + A11** — `tools/build_catalog_index.py` NEW (pulled forward so
      index.tsv is machine-made): `analysis/catalog/index.tsv` regenerated, **131 data
      rows**, per-prefix counts match CODE_REGISTRY §1 exactly (SM2=33 ✓, SM=18, K=12,
      T+W=16, science 7-prefix=37, social=7, history=8). F dual-ownership safe via
      subject_code scope column. math2 sheet fallback via 영역 Gn section headings
      (blocks omitting the field resolve correctly; SM2-14→I-2 verified).
      `corpus/SUP-M2-2026/meta.yml` per §5.7 (transcribed_at null, honest render_dpi null).
      `student/S01/`: profile.md · ATTEMPT_LOG.tsv (BOM, header-only) · MASTERY.tsv
      (regenerated: 131 unmeasured) · WEAK_LEDGER.tsv (WK-01 E5 seeding, state=found)
      · `share/SHARE_LOG.tsv`. A11 declaration line appended to plan history.
- [x] **O4 = plan P3** — `build_mastery.py`(deterministic status ladder documented in
      docstring) · `import_grading.py`(atomic validation: ANY violation aborts whole
      file exit=2; BOM preserved; WEAK proposals print-only incl. unsure×2 promotion
      and covered-axis relapse hints) · `build_report.py`(single-file HTML, zero
      external refs, SHARE_LOG append, --share-log override for isolated runs).
      Dry-run in %TEMP%: 5 valid rows end-to-end PASS (SM2-03 blank→weak, SM2-13
      o+a→unstable, last3 newest-left), invalid mark_code row → atomic ABORT exit=2,
      E5 wrongs correctly matched to open WK-01. S01 ledgers stay EMPTY (D6 모의40 미풀).
      §6 conformance: real MASTERY == regeneration (--check PASS both files).
      Known quirk recorded: single wrong → unstable (not weak) until 2-in-last3 —
      conservative ladder, teacher-reviewable.
- [x] **O5 = plan P4 partial** — CLAUDE.md 작업 흐름 표 「원장 운용」 row added.
      모의40 frontmatter insertion DEFERRED to post-P2 (parser lacks frontmatter
      support, QS-3 — early insertion risks parse breakage).
- [x] **O6** Plan §7 checkboxes P0/P1/P3 [x], P4 partial, P2 blocked-note; plan status
      frontmatter updated; migration ledger A11/A12 flipped; session report extended.
- Blocked (unchanged): **P2** awaits rev-arbiter ruling on packages `260825_07`+`12`.

### Group P — rulings applied (post-arbiter; see root `260825_group_p_application_report.md`)
- Pre-check: every load-bearing ruling claim re-executed against sources before editing
  (A1 RE 6-fail reproduction · QS-4 registry facts · B1 grid columns · H line citations ·
  arbiter write-surface scan) — all stood; nits recorded in the report §1.
- [x] **P0** CB2 F9 section-reset fix first (parser.js + md2quiz.py behaviour-identical).
- [x] **P1** CB1 amended RE + SUBJECT_MAP §5.8 + frontmatter priority, bundled with
      **12-CB1** QUIZ_STANDARD rewrite (four-slot standard + tolerance rule, §5.8 ref,
      schema df/traps/auxTypes/tagExtra + set-meta contract, CB4→registry cross-ref).
      Acceptance node harness PASS: 모의40 **40/40/40/함정6/보조1** (python mirror equal).
- [x] **P2** CB3 app.js four-state O/△/X// + 🧾 TSV export (§5.1 12 cols, BOM).
- [x] **P3** Catalogs: science P1–P15 (40 pairs) · history Q1/Q3+P4–P7+E-6 inventory
      (조광조·삼강행실도 번호 미확정 per fallback) · english/social relabel+W-01 condition+
      T-11→T-02+backlogs (P2 numbers withheld honestly) · math/korean Q1-extended+P6
      qualifier · CODE_REGISTRY 매체 예약 행.
- [x] **P4** Ledger sync: _index R3 ×6 (approved/fixed), report statuses approved ×6,
      HISTORY ×6, REV_LOG owner-apply trace section, DATA_STANDARD §7 QS row 해소.
- Deferred to next cycle: separated sel/sa band derivation (english), E-6 typing,
  korean 누락(K-01·K-10·매체), science untyped candidates.
- [x] **P-wrap** (same day): plan §7 P2/P4 봉합 · CB4 본문 보조 슬롯 삽입(+파서 괄호형
      aux 견고화 js/py) · 모의40 frontmatter 삽입·배지 확인 · md2quiz 비퀴즈 입력 스킵
      가드(data.js 오염 14→6 소스 해소). 상세: root `260825_group_p_application_report.md`
      §15–16 및 세션 보고서 같은 절.

### 실행 완료 (기록 보존)
- [x] **A5** raw/ 판정 — PNG 4건은 수행평가가 아닌 **2026 공식 정답지 스캔**(D1). 귀속 불필요 판명, 현위치 유지. INDEX 반영 완료
- [x] **A6** test/ → `origin_data/NY-math1-202{1,2}/` 이전 + HARVEST_LOG 소급 등록 — 260825 실행
- [x] **A7** origin_data/26_1_1 → EX-*-20261M/F 재편 + EXTRACTION_LOG 이동 행 M1~M3 append — 260825 실행
- [x] **A8** data.zip 처분 — git 미추적 확인(D2)로 `_archive/` 격리 방식 변경 실행

## 10. 수용 기준

1. **관리 재현(D클래스)**: 새 과목·회차·수행평가 자료가 도착해도 문서만으로 ID 발급→배치→등록이 끝난다(§2 시나리오 재실행).
   같은 자료를 다시 넣으면 같은 코퍼스ID·같은 경로·같은 파일명이 나온다.
2. **생성 계약(G클래스)**: 생성물은 파일명·frontmatter·필수 섹션·태그 표준형을 준수하고 solve-back(출제) 또는 검토서(정본)를
   통과한다 — 내용의 일치가 아니라 **계약 준수**로 판정한다(§6.1).
3. 기존 정본과 모순 0 — 본 PRD의 수정안은 전부 A항목 승인을 거쳐 반영된다.
4. 문서 내 상대 링크 전수 실존.
5. **문서 내부 모순 0(P5 재발 방지)** — 실행으로 낡아진 서술은 즉시 본문에서 고치고 이력에 남긴다. "미생성"·"예정"류 문장은
   실행 후 남으면 결함으로 간주한다.

## 11. 열린 질문

- **Q1** ~~raw PNG의 실체~~ **해소(260825 실측)** — `raw/정답/` PNG 4건 = 2026 공식 정답지 스캔. 수행평가 가설 기각,
  A5는 "귀속 불필요·현위치 유지"로 판정. INDEX.md의 기존 "공식 정답지 없음" 표기 오류도 정정함.
- **Q2** REV_LOG(MD 표) TSV 전환 — 기존 Q4(검토서 02/06)와 동일 건, REV_지침 개정 수반이므로 본 PRD에서 다루지 않는다.
- **Q3** 태그 표준형 보강 범위 — 기존 Q3(검토서 01·06 연동), QUIZ_STANDARD 개정 승인 시 함께 판정.
- **Q4** ~~ANL 규격의 위치~~ **해소(260825)** — `analysis/student/_README.md`로 제정(catalog/_README 선례 준용: 규격이 다스리는
  자료 바로 옆에 둔다). docs/ 집중안은 폐기.

## 이력
- 260825 작성 — 메인루프. 사용자 결정 반영: ①코드 등록제 확장성(니모닉) ②정제 파이프라인(페이지 단위 우선) ③마이그레이션 포함 ④파일명 YYMMDD_NN 전 문서 적용 ⑤신규 기출 도착 시나리오 사전 검증(§2 — 결함 V1~V5 발견·설계 반영). 관련: plan_3layer_architecture(하부), 검토서 260825_01~06(대기).
- 260825 실행 반영 — 사용자 승인("origin_data 실데이터로 최종 시나리오 테스트 후 작업")에 따라 A6·A7·A8 실행, A5 판정 갱신(D1: raw/정답=2026 정답지 스캔 4건), A13 신설.
  실측 대장: [`260825_02_origin_migration_ledger.md`](260825_02_origin_migration_ledger.md). 원장: corpus/HARVEST_LOG.tsv(37 유닛).
- 260825 개정(**1차 뼈대**) — 자체 고찰 결함 P1~P7 반영:
  ①재현성 정의 도입(§0 목표 문구 + §6.1 D/G 이원 모델, **C1 동의 요청**) ②S1 트레이스 8~10단 판정 수정(✓→설계 존재 격하)
  ③생애주기 상태 열 신설(🟢🟡🔴 — 🔴 2단 = 채점·약점/공유 미구축 명시) ④§8·§3.3 실행 후 잔여 서술 수선(P5)
  ⑤§9 종속성 그룹화(0/A/B/C/D)+A15 신설(ANL 내용 규격)+A14 흡수 ⑥§10 수용 기준 재작성(G클래스 계약 판정·내부 모순 금지)
  ⑦Q4 신설(ANL 규격 위치). LABEL_MAP 등록은 A1 범위로 흡수.
- 260825 **표준화 마무리 실행** — 사용자 일괄 지시("표준화를 마무리")로 잔여 항목 전부 집행:
  **A1**(DATA_STANDARD v1.1: 코퍼스ID v2·PA/NY·회차코드 §4.6·meta 필드·§2 파일명 통일) · **A2**(동 문서 §2) ·
  **A3**(forecast README 코드화) · **A4**(CLAUDE.md 원칙1 경로) · **A9**(extracted README 오타+동결 선언) ·
  **A13**(raw/README 재작성) · **A14**(.gitignore NY 예외 — check-ignore 검증 통과) · **A15**(ANL 규격 student/_README 신설).
  **C1 채택**(기술적 필연 명시), **A10 보류 결정**(외부 인용 15곳 초과 — 개명 비용>편익, 신규분 패턴 적용으로 대체),
  Q4 해소. 미완료는 **A11뿐**(3층 P1 착수 시점에 실행).
- 260825 **그룹 E 신설·실행** — 사용자 지시("유형·카테고리 명칭 표준화" + "루트에 뼈대 설명문")로:
  F1 CODE_REGISTRY 제정 · F2 F접두어 충돌 판정(사회·한국사 이중 소속, 스코프 인용 강제) ·
  F3 CLAUDE.md↔_README 템플릿 병합 정합 · F4 루트 README 신설 · F5 스무년 부교재 원본 귀속.
  확장성 검토 결론: 축 분해(내용/형식/난이도)와 append-only는 우수하나 ID 체계가 ad-hoc → F1~F2로 법제화.
- 260825 **그룹 G 실행** — 사용자 지시(①분석 이미지 체계적 관리 ②단계별 사유·판단 근거 기록 ③공통유형=출제자 패턴 계층 정의 확정
  + 발견성 지적 "description 없으면 AI가 못 찾는다"): **G1~G6**. 검증 사료 3중 축(원본→이미지→원장) 확립,
  type-extractor 산출 영구화, 공통유형 승격 절차 법제화, corpus/_README 신설.
- 260825 **Group H executed** — user architecture decisions: t1⇄t2 automated round loop
  (main-loop driven, ≤5 rounds) + tier-3 arbiter in Claude Code Opus (same repo) +
  handoff ledger `_index.md` + language policy (English-first). REV_지침 fully rewritten
  in English; rev-writer/type-extractor converted; rev-auditor·rev-arbiter created.
- 260825 **Group J executed** — user re-partition: 정제=opencode / 제안·판정=Claude Code Opus /
  검토 루프=opencode. type-proposer 신설, type-extractor 순수 전사 축소, 제안서 검토 기준(C),
  출제 파이프라인도 동일 라운드 구조에 편입(solve-back 사전 게이트 + practice/exam 분기 + 투입 허가 조건).
- 260825 **Group K executed** — 사용자 정책 강화(파일명 포함 한글 지양): 정전 16곳 영문 개명
  (과목 카탈로그는 subject_code 어휘 일치), 생존 문서 참조 144건 전파, 기록물은 스냅숏 보존.
