# DATA_STANDARD — 데이터·문서 표준 정본 v1

> 이 저장소의 모든 데이터 파일과 문서가 따르는 형식 표준이다. 웹 연동·도구 파싱을 전제로 한다.
> 문제지(문항 본문) 입력 규격은 [`QUIZ_STANDARD.md`](QUIZ_STANDARD.md)가 담당하고, 검토서 절차는
> [`../analysis/REV_GUIDE.md`](../analysis/REV_GUIDE.md)가 담당한다 — 본 문서는 그 위의 전역 층이다.
> 개정 규칙: 변경은 사용자 승인 후 `## 이력`에 날짜와 함께 추가한다(원칙 8 준용).

## 0. 2층 원칙 (최우선)

| 층 | 형식 | 언어 규칙 | 소속 파일 |
|----|------|-----------|-----------|
| **기계 소비 원장** | TSV(탭 구분, UTF-8 **BOM 필수**) | 컬럼명 = 영어 snake_case. **셀 값 = ASCII 전용**(enum 코드·ID·수치) | ATTEMPT_LOG · MASTERY · WEAK_LEDGER · index · HARVEST_LOG · SHARE_LOG |
| **사람 큐레이션 문서** | Markdown | 한국어 라벨·서술 자유 | 카탈로그 · 지침 · CLAUDE.md · 검토서(rev/) |

- 한글 표시명은 §4의 LABEL_MAP에서만 코드와 대응한다. 코드·라벨의 임의 1:N 대응 금지.
- **원장 셀에 한글·심볼을 넣지 않는다** — 표시는 출력 시점에 LABEL_MAP으로 붙인다.
  사람 서술이 필요하면 코드화(예: 오답 사유 → `fail_code` §4.1-A)하고, 코드가 없으면
  코드를 먼저 등록한다. `note`는 자유 서술란이 아니라 **산출 경로·처리 표시용 ASCII 열**이다.
  원장을 MD로 사본하는 이중화도 금지.
- 도구(import_grading 등)는 스키마 위반 행을 **거부**한다 — 표준은 사람 기억이 아니라 코드로 집행된다.

## 1. 전역 규약

### 1.1 날짜

| 맥락 | 형식 | 예 |
|------|------|-----|
| 파일명·폴더명·로그 행 | `YYMMDD` | 260825 |
| 데이터 값(frontmatter, TSV date 컬럼) | ISO 8601 `YYYY-MM-DD` | 2026-08-25 |

### 1.2 인코딩

UTF-8. BOM은 TSV에만 붙인다(Windows Excel 호환). 셀 안 개행 금지 — 서술 나열은 `;` 구분.

### 1.3 ID 레지스트리

| ID | 패턴(regex) | 예 | 비고 |
|----|-------------|-----|------|
| 유형ID | `^[A-Z]{1,3}\d?-\d{2}$` | `SM2-14` | 접두어 등록제: `SM`=공통수학1, `SM2`=공통수학2. 타과목 카탈로그 정식화 시 여기에 등록 |
| 세트ID | `^SET-\d{6}-[a-z0-9]+-\d+$` | `SET-260822-math2-40` | YYMMDD-과목코드(§5.8)-문항수 |
| 코퍼스ID | `^[A-Z]{2,4}-[a-z0-9]{2,8}-\d{4}([12][MF]\|P\d{2})?$` | `EX-math2-20262M` | 자료성격(EX=기출, PA=수행평가, NY=내신기출집, SUP=부교재, CU=교육과정)-subject_code-연도+학기구분. **v2(260825)**: middle=subject_code 소문자 통일(세트ID와 조인), 회차 꼬리 허용 |
| 코퍼스 문항ID | `<코퍼스ID>-Q\d+` | `SUP-math2-2026-Q07` | |
| 회차코드 | `^20\d{2}-[12](M\|F\|P\d{2})$` | `2026-1M` | 시험 식별자 ASCII 표준. M=중간, F=기말, Pnn=n차수 수행평가 — LABEL_MAP §4.6 |
| 약점ID | `^WK-\d{2}$` | `WK-01` | 순차 부여, 재사용 금지 |
| 학생ID | `^S\d{2}$` | `S01` | |
| 함정코드 E | `^E\d{1,2}$` | `E5` | 정의: `analysis/catalog/TYPE_MASTER.md` |
| 난이도코드 DF | `^DF[1-9]$` | `DF5` | 정의: `analysis/catalog/DIFFICULTY_RUBRIC.md` |

> **디렉터리 불변식(260826)**: 코퍼스 유닛의 **폴더명은 코퍼스ID와 문자 단위로 일치**한다.
> 검증(PowerShell, 출력 0행이어야 통과 — `_images`는 예약 디렉터리이므로 제외):
> `Get-ChildItem corpus -Directory | Where-Object { $_.Name -ne '_images' -and $_.Name -notmatch '^[A-Z]{2,4}-[a-z0-9]{2,8}-\d{4}([12][MF]|P\d{2})?$' }`
> — 발단: 260825 골격 생성 시 같은 PRD 본문에 구경로 지시(`corpus/SUP-M2-2026/`)가 남아 실행돼
> 폴더만 v1 명칭으로 생성됨(meta.yml·원장은 v2). 부분 갱신 사고 → CLAUDE.md 원칙 10 실증 사례.

### 1.4 enum 운용 원칙

저장값은 ASCII 코드, 화면 출력만 LABEL_MAP의 심볼·한글이다. 신규 enum은 이 문서에 코드표를 먼저 추가한 뒤 쓴다.

### 1.5 정답지류(회차 공용 자료)의 취급 — v1.7 (A12 명문화)

> 대상: 한 회차에 여러 과목의 정답을 함께 수록한 정답지·채점 기준지
> (예: `2025_1학기_1학년_중간` 폴더의 통합본 정답 파일, raw/정답/*.png 스캔).

- **코퍼스ID를 발급하지 않는다** — §1.3 코퍼스ID 패턴은 subject_code가 성립하는 자료 전용이므로
  회차 공용 자료는 패턴 전제가 불충족된다.
- 추적처: 소속 회차 유닛의 `note`(HARVEST_LOG) + 동일 회차 개별 자료 meta.yml의 `answer_key`(§5.7).
- `extracted/INDEX.md`에는 발견 사실로 등재하되 코퍼스ID 칸은 `-`를 유지한다.
- 물리 위치는 발견 당시 위치를 유지한다(`raw/정답/*.png` 선례 — 분석 문서 인용 경로 보호).

## 2. 문서 클래스 분류표

| 클래스 | 위치·파일명 | 헤더 규약 | 형식 |
|--------|------------|-----------|------|
| 문제지 세트 | `output/<YYMMDD>/<YYMMDD>_<NN>_<subject>_<영문snake>.md`(H1에 한국어 제목, set_id는 frontmatter) | YAML frontmatter(§5.8) + H1 | MD |
| 계획서 | `output/<YYMMDD>/<YYMMDD>_<NN>_<영문snake>.md` — 구 `plan_*` 접두 폐지(260825), 기존 plan_* 파일은 레거시 유지 | YAML frontmatter(title·created·author·status·related) | MD |
| 검토서 | 정본·시스템 대상=`analysis/rev/`, 회차 산출물 대상=`output/<YYMMDD>/rev/` — 파일명 `YYMMDD_NN_<영문snake>.md`. 홈 판별은 [DOC_LOCATION](../analysis/DOC_LOCATION.md) §2 | YAML(REV_GUIDE §2) | MD |
| 제안서 | `output/<YYMMDD>/<YYMMDD>_<NN>_<영문snake>.md` — `*_type_analysis.md`·`*_catalog_update.md`(type-proposer 산출, REV_GUIDE §3-b). 승인 전까지 정본 미반영 | H1(제안 상태 포함: draft·in-review·approved·applied) | MD |
| 예측 보고서 | `analysis/forecast/<YYMMDD>_<회차코드>-<subject_code>.md` | H1(+사후 채점 append) | MD |
| 오답분석 | `analysis/student/<YYMMDD>_<subject_code>_<영문snake>.md` — 내용 규격은 student/_README(A15) | YAML(title·created·author·source·status) + 필수 섹션 | MD |
| rev 진입점 | 각 rev 홈의 `HISTORY.md` | H1 + 목록표 | MD |
| 학생 원장 | `student/<학생ID>/*.tsv` | 1행 = 컬럼 헤더 | TSV |
| 코퍼스 메타 | `corpus/<코퍼스ID>/meta.yml` | YAML(§5.7) | YAML |
| 리포트 | `student/<학생ID>/reports/<YYMMDD>_report.html` | — (생성물) | HTML 단일파일 |

> 파일명 통일 근거: 사용자 지시 "모든 문서는 YYMMDD_NN 명칭"(260825) → PRD output/260825/260825_01 §5.2 전 클래스 통합표.

## 3. TSV 원장 공통 규칙

1. 1행은 반드시 컬럼 헤더. 빈 값은 `-`.
2. append-only 원장(ATTEMPT_LOG · HARVEST_LOG · SHARE_LOG)은 과거 행 수정 금지 — 정정은 새 행 + `note`에 `fix:` 접두어.
3. 상태기계 원장(WEAK_LEDGER)은 최신 상태를 행으로 유지하되, 전이마다 새 행을 추가하고 완료 행을 남긴다(추적 가능).
4. 목록값 컬럼(aux_types, evidence_types 등)은 `,` 구분. 셀 안 탭·개행 금지.

## 4. enum 코드표

### 4.1 mark (채점 표기)

| 코드 | 표시 | 의미 | 진단 |
|------|------|------|------|
| `correct` | O | 정답 | — |
| `unsure` | △ | 불확신 정답 | 같은 유형 2회 누적 시 약점 승격 |
| `wrong` | X | 오답 | 개념·절차 결손 → 개념 사다리 처방 |
| `blank` | / | 백지·미완주 | 완주력 결손 → 제한시간 완주 처방 |

### 4.1-A fail_code (오답 귀인 — 함정 축)

`ATTEMPT_LOG` 11열. **값은 §1.3 함정코드 E**(`^E\d{1,2}$`, 정의 정본
`analysis/catalog/TYPE_MASTER.md`) 또는 미판정을 뜻하는 `-`.

| 항목 | 규정 |
|------|------|
| 의미 | 학생이 **실제로 빠진 함정**. 문항이 보유한 함정(`traps[]`)이 아니라 **귀인 결과**다 |
| 채우는 주체 | **교사(채점자)**. 도구·웹·AI는 채우지 않는다 |
| 채우는 시점 | 채점 시. `import_grading.py` 투입 **전**에 확정한다 |
| 미판정 표기 | `-` (빈칸·공백 금지) |
| 적용 조건 | `mark_code = wrong` 일 때만 의미를 갖는다. correct·unsure·blank 행은 `-` |
| 소비처 | `import_grading.py`의 `wrong_axes` 집계 → WEAK_LEDGER 신규 축 **제안**. 제안일 뿐 승격은 교사 판정(§5) |

**후보 제시 규칙(자동 채움과 구별).** 웹 뷰어는 `wrong` 표기 시 그 문항의 `traps[]`를
**선택지로 제시**할 수 있고, 교사가 고른 값만 이 열에 실린다. 교사가 고르지 않으면 `-`다.
`traps[]`를 그대로 복사해 넣는 자동 채움은 **금지** — 문항이 품은 함정과 학생이 빠진
함정은 다르며, 원칙 6(자료 등급)의 "확정과 추정을 섞지 않는다"에 걸린다.

> **왜 명문화하는가**(260826): 이 규정이 없던 동안 웹 export는 전 행을 `-`로 내보냈고,
> 그 결과 `wrong_axes`가 영구 공집합이 되어 **취약 축 자동 제안 기능 전체가 무동작**이었다.
> 값 패턴(§1.3)만 있고 *누가 언제 채우는가*가 어디에도 없었던 것이 원인이다.

### 4.2 mastery_status (유형 숙련도)

| 코드 | 표시 | 판정 기준 |
|------|------|-----------|
| `mastered` | 🟢 숙달 | 최근 3시도 연속 correct, 그중 최소 1개 T3 이상 |
| `unstable` | 🟡 불안정 | correct 존재하나 unsure/wrong 혼재 |
| `weak` | 🔴 취약 | 최근 3시도 중 wrong≥2 또는 blank≥1 |
| `unmeasured` | ⬜ 미측정 | 시도 0회 |

### 4.3 weak_state (약점 상태)

`found`(발견) → `prescribing`(처방중) → `retesting`(재시험) → `resolved`(해소) / 해소 후 동일 축 wrong 재출현 시 `relapsed`(재발, Tier +1 재처방).

### 4.4 catalog_status (카탈로그 유형 상태)

| 코드 | 표시 |
|------|------|
| `verified` | 검증 |
| `verified_aux` | 검증(부교재) |
| `demo` | 시연 |
| `deprecated` | 폐기 |

### 4.5 rev_status (검토서) — 예외

`대기 / 회신 / 반영 / 기각` 한글 값을 그대로 쓴다. REV_GUIDE §3이 한글 값을 정본으로 못박았으므로,
전환은 REV_GUIDE 개정 승인과 함께만 한다(§7 참조).

### 4.6 exam_term (회차 코드 표시)

| 코드 | 표시 | 비고 |
|------|------|------|
| `M` | 중간고사 | |
| `F` | 기말고사 | |
| `Pnn` | n차수 수행평가 | nn=2자리 일련 |

형식 `<YYYY>-<학기 1|2><코드>` (예: `2026-1M`, `2026-1P02`). 근거: PRD output/260825/260825_01 §3.2.

## 5. 스키마 v1

### 5.1 ATTEMPT_LOG.tsv (단일 채점 원장, append-only)

```
date	set_id	qnum	main_type	aux_types	tier	df	mark_code	student_answer	correct_answer	fail_code	note
2026-08-22	SET-260822-math2-40	13	SM2-14	-	T3	DF5	wrong	2	3	E5	-
2026-08-22	SET-260822-math2-40	16	SM2-13	SM2-11	T4	DF1,DF8	blank	-	18	-	web-export
```

#### 열 규격 (12열 고정, 순서 불변)

| # | 열 | 값 규격 | 예 | 비고 |
|---|----|---------|-----|------|
| 1 | `date` | `^\d{4}-\d{2}-\d{2}$` | `2026-08-22` | 채점일(응시일 아님) |
| 2 | `set_id` | §1.3 세트ID | `SET-260822-math2-40` | 세트 조인 키. 세트 frontmatter `set_id`에서 옴 |
| 3 | `qnum` | 정수 | `13` | 세트 내 문항번호 |
| 4 | `main_type` | §1.3 유형ID | `SM2-14` | `catalog/index.tsv` 등록분만 |
| 5 | `aux_types` | 유형ID 콤마결합 \| `-` | `SM2-11` | 없으면 `-` |
| 6 | `tier` | `^T[1-4]$` | `T3` | |
| 7 | `df` | `^DF[1-9](,DF[1-9])*$` \| `-` | `DF1,DF8` | §1.3 |
| 8 | `mark_code` | §4.1 enum | `wrong` | 화면의 O·△·X·/ 는 LABEL_MAP 출력일 뿐 |
| 9 | `student_answer` | ASCII \| `-` | `2` | 아래 **ASCII 전용 규칙** |
| 10 | `correct_answer` | ASCII \| `-` | `18` | 〃 |
| 11 | `fail_code` | §4.1-A 함정코드 \| `-` | `E5` | 미판정은 `-` |
| 12 | `note` | ASCII \| `-` | `web-export` | 자유 서술 금지 — 산출 경로·처리 표시용 |

#### ASCII 전용 규칙 (§1.4 "저장값은 ASCII 코드"의 원장 적용)

**12열 전부 ASCII만 저장한다. 한글·심볼(O·△·X·🟢 등)·개행·탭 금지 — 예외 열 없다.**
사람이 읽는 한글 표시는 LABEL_MAP(§4.6)을 거쳐 **출력 시점에** 붙인다.

- ASCII로 표현되지 않는 **서술형 답안·모범답은 원장에 싣지 않는다.** `student_answer`·
  `correct_answer`를 `-`로 두고, 답안 원문은 `student/<학생ID>/` 답안 파일에 보관해
  `(set_id, qnum)`으로 조인한다. 원장은 **집계용**이지 답안 보관소가 아니다.
  (수학 서답형은 `18`·`x=1` 같은 수식이라 대개 그대로 ASCII로 들어간다.)
- `note`에 오답 사유를 한글로 적지 않는다. 사유는 `fail_code`(§4.1-A)로 코드화하고,
  해당하는 함정코드가 없으면 `TYPE_MASTER.md`에 코드를 먼저 등록한 뒤 쓴다(§1.4).
- 강제 지점: `tools/import_grading.py`가 12열 전부 비-ASCII를 거부한다(§6).

### 5.2 MASTERY.tsv (재생성물 — 손편집 금지)

```
type_id	unit	importance	attempts	o_count	amb_count	wrong_count	blank_count	last3	status_code
SM2-14	I-3 원의방정식	★★★	5	2	1	1	1	oaw	weak
SM2-25	I-4 도형의이동	★★	0	0	0	0	0	-	unmeasured
```

`last3`: 최근 3시도의 mark_code 첫 글자(o/a/w/b), 최근 것이 왼쪽, 부족분은 `-`. `importance`는 카탈로그 복사값.

### 5.3 WEAK_LEDGER.tsv (약점 상태기계)

```
wk_id	axis	evidence_types	evidence_codes	found_date	state	prescription	resolve_condition	resolved_date	note
WK-01	E5 경계 조건(등호 포함·배제 판단)	SM2-03,SM2-14,SM2-18,SM2-25,SM2-28	SM-11,E5	2026-07-21	found	-	동일 축 T3 2연속 correct	-	1학기 중간 9번(SM-11) 오답 기원; 모의40 해설 3·13·26·34번 반복 지목
```

`state`는 §4.3 코드. 처방 생성 시 `prescribing` 행 추가, `prescription`에 세트ID 기입.

### 5.4 index.tsv (유형 인덱스 — 조인의 근원)

```
type_id	subject_code	unit_major	unit_minor	importance	status_code
SM2-14	math2	I.도형의방정식	3.원의방정식	★★★	verified_aux
```

`tools/build_catalog_index.py`가 `analysis/catalog/*.md`에서 재생성. 카탈로그 갱신 시 재실행.

### 5.5 HARVEST_LOG.tsv (코퍼스 수확 이력, append-only)

```
date	corpus_id	new_types	freq_update	weakness_evidence	remaining	note
2026-08-25	SUP-math2-2026	SM2-01~SM2-33	-	WK-01(E5) 보강	93문항 전사본 유실; 별도 세션 재판독	소급 등록(구 EXTRACTION_LOG #37) — ID v2 명명 적용(SUP-M2-2026→SUP-math2-2026)
```

### 5.6 SHARE_LOG.tsv (학부모 공유 이력, append-only)

```
date	target	link_or_file	contents_summary	feedback
2026-08-30	SET-260822-math2-40	reports/260830_report.html	40문항 결과·약점 1건·처방 계획	-
```

### 5.7 corpus meta.yml

```yaml
id: SUP-math2-2026          # §1.3 패턴(v2)
title: "스무년 고1-2.pdf (단원별 문항연습 #1~#4)"
grade: 2                   # 1=기출·수행 > 2=부교재·내신집 > 3=교육과정·타교 (CLAUDE.md 원칙 6)
exam_code: "2026-1M"       # 회차코드(§4.6). 회차 없는 자료(부교재 등)는 null
variant: master            # master=고사원안 | student=학생 응시본 — 별도 코퍼스ID로 분리 등록
pages: 18
items: 93
render_dpi: 160            # 판독 이미지(corpus/_images/<id>/pNN.png) 렌더 파라미터 → 재생성 보장
render_tool: "PyMuPDF"
transcribed_at: null       # ISO 8601. null = 미전사
method: "PyMuPDF PNG(dpi130+) + LLM 판독"
confidence: medium         # high|medium|low
answer_key: null           # 동일 단위 내 정답지 파일명(answers.*). 없으면 null
catalog_ref: "analysis/catalog/math2.md"
```

Writer: `type-extractor`, at transcription completion (its procedure already determines
grade / exam_code). The main loop assigns the corpus ID and folder before extraction runs.

### 5.7-A verify_log.tsv (단계별 검증 원장, append-only — 260825 신설)

> 근거 사료 **3중 축**: 원본(origin_data/) → 판독 이미지(corpus/_images/) → 본 원장(판단의 사유·근거 인용).
> 어떤 주장이든 이 축으로 소급 검증 가능해야 한다. 유닛 구조 안내는 [corpus/_README.md](../corpus/_README.md).

| 컬럼 | 의미 |
|------|------|
| date | ISO 8601 |
| step | `transcribe`(전사) · `classify`(유형 배정) · `merge`(유형 통합) · `grade`(등급·회차 판정) · `promote`(공통유형 승격) |
| target | 대상 — 문항번호·유형ID 등 |
| decision | 판정 결과. 판독 실패는 반드시 `unreadable` 행으로 남긴다 |
| evidence | 근거 위치 — `p07+하단좌측` 형식(페이지 = corpus/_images/<ID>/pNN.png 대응) |
| reason | 사유 — 왜 그렇게 판단했나(한 문장 이상). 생략 금지 |
| confidence | high · medium · low |
| actor | judging party — `type-extractor` · `type-proposer` · `item-writer` · `rev-writer` · `rev-auditor` · `rev-arbiter` · `forecast-writer` · `forecast-reviewer` · `forecast-auditor` · `forecast-arbiter` · `main-loop` · `teacher` |

### 5.8 문제지 세트 프론트매터 + 과목 코드

```yaml
---
set_id: SET-260822-math2-40
student: S01
subject_code: math2
term: 2026-2
unit: I. 도형의 방정식
scope_confirmed: false     # false이면 뷰어·리포트에 ⚠️ 범위 미확정 배지 (원칙 7)
intended_use: practice     # practice=연습용(tier-1 경량 검토) | exam=실전 투입(3단계 루프+arbiter 허가 필요, REV_GUIDE §3-b)
---
```

| subject_code | 표시 |
|--------------|------|
| math1 | 공통수학1 |
| math2 | 공통수학2 |
| science | 통합과학 |
| social | 통합사회 |
| history | 한국사 |
| english | 영어 |
| korean | 국어 |
| info | 정보 |

`scope_confirmed`가 없는 구(舊) 문제지는 false로 간주한다.

## 6. 강제 장치

- import_grading류 도구는 §4 enum·§1.3 ID 패턴·§5 컬럼 집합을 검증하고 위반 행을 거부한다.
- **ASCII 전용 강제**(260826): `import_grading.py`가 12열 전부에 비-ASCII 문자를 검출하면
  그 행을 거부한다(원자적 정책이므로 한 행이라도 걸리면 전량 미반영). §0·§1.4·§5.1의
  "저장값은 ASCII"가 사람 기억이 아니라 코드로 집행되는 지점이다.
- 웹 뷰어는 frontmatter `scope_confirmed:false`를 배지로 노출한다(원칙 7의 데이터 강제).
- MASTERY·index는 재생성 파일이므로 손편집을 감지하면 경고한다(체크섬 또는 생성 태각 비교).

## 7. 예외·미결

| 항목 | 상태 |
|------|------|
| REV_LOG.md(MD 표) | REV_GUIDE §4가 한글 MD 형식을 정본으로 지정 — TSV 전환은 REV_GUIDE 개정 승인과 함께만 검토 |
| docs/QUIZ_STANDARD.md 개정 | **해소(260825)** — 판정 07·12 반영: 네 슬롯 태그 표준형(ID·Tier·DF·함정E)+보조/포용 규칙, §5.8 과목 매핑 참조, 스키마 df[]·traps[]·auxTypes[]·tagExtra[]+세트 프론트매터 계약, 예시 ID는 등록 접두어(T/W) 유지+상호참조 |

## 이력
- 260826 **v1.8** — [OC 지시] 260826_03 P0 반영(사용자 승인): §5.8 subject_code에 `info`
  (정보) 추가(CODE_REGISTRY §3과 쌍 — 온보딩 #2·#3의 S1 착수 전 선행 등록, 나머지 6항목은 S4).
  §1.3에 **코퍼스 디렉터리 불변식**(폴더명==코퍼스ID + 검증 명령) 명문화 — 260825 골격 생성 시
  같은 PRD 본문의 구경로 지시(`SUP-M2-2026`)가 갱신 없이 실행돼 폴더만 v1로 남은 부분 갱신 사고의
  재발 방지. §5.5 예시 행을 실물 원장(v2 개명 후)과 정합하게 교체.
- 260826 **v1.4** — 사용자 판정 2건 반영(검토서 [260826_01] Q1·Q2). **Q1 ASCII 전용 표준화**: §0 2층 원칙의 '원장에 사람 서술은 note로 흡수' 문구가 §1.4('저장값은 ASCII 코드')와 충돌해 §5.1이 한글 예시를 싣고 있던 것을 정리 — 원장 12열 전부 ASCII 전용(예외 열 없음), §5.1 열 규격표 신설, ASCII 미표현 서술형 답안은 원장에서 `-`(원문은 student/<학생ID>/에서 (set_id,qnum) 조인), §6에 `import_grading.py` 비-ASCII 거부 강제 등재. **Q2 fail_code 명문화**: §4.1-A 신설 — 값 패턴(§1.3)만 있고 *누가 언제 채우는가*가 없어 웹이 전 행 `-`를 내보냈고 `wrong_axes`가 영구 공집합이 되어 취약 축 자동 제안이 무동작이었다. 의미·주체(교사)·시점·wrong 행 한정·소비처와 후보 제시 규칙(자동 채움 금지)을 규정.
- 260825 v1 신설 — 사용자 결정(판단 원장 TSV 통일 / mark ASCII 코드+표시 매핑 / QUIZ_STANDARD와 분리 신설) 반영. 작성: 메인 루프.
- 260825 정합 수선 — 검토서 재번호(02→06, 타 세션 선등록 충돌)와 DOC_LOCATION §2(rev 이원화) 반영: §2 검토서 행을 위치 표준 참조로 교체, §7 번호 갱신.
- 260825 **v1.1** — PRD 260825_01 A1·A2 반영(사용자 일괄 지시 "표준화 마무리"로 실행): §1.3 코퍼스ID 패턴 v2(EX·PA·NY 등재·subject_code 통일) + 회차코드 등록, §4.6 exam_term LABEL_MAP 신설,
  §5.7 meta.yml에 exam_code·variant·answer_key 필드, §2 파일명 YYMMDD_NN 통일(계획서 plan_* 폐지·문제지 패턴 변경)+예측·오답분석 클래스 추가.
- 260825 **v1.2** — 검증 사료 체계 신설(사용자 지시: 분석 이미지 관리 + 단계별 사유·근거 기록): §2에 transcript·판독 이미지(_images)·verify_log 클래스 등록,
  §5.7 meta.yml에 render_dpi·render_tool 필드, **§5.7-A verify_log.tsv 스키마** 신설. corpus/_README.md가 유닛 해부도 담당.
- 260825 **v1.3** — three-tier review protocol (user decision): meta.yml writer fixed to
  `type-extractor` (§5.7); §5.7-A actor enum extended (`rev-auditor`, `rev-arbiter`,
  `rev-writer`). Protocol spec lives in `analysis/REV_GUIDE.md`. New content is English-first
  per language policy; legacy Korean text migrates gradually (PRD backlog).
- 260825 **v1.4** — role re-partition + authoring gate (user decisions): §2 proposal class
  (`*_type_analysis`·`*_catalog_update`, status draft→in-review→approved→applied);
  §5.8 set frontmatter `intended_use: practice|exam`; actor enum + `type-proposer`·`item-writer`.
  Pipeline spec: REV_GUIDE §3-b.
- 260825 **v1.5** — filename romanization (user policy: no Korean in guide/deliverable NAMES):
  16 canonical files renamed — REV_GUIDE · FORECAST_GUIDE · DOC_LOCATION · TYPE_MASTER ·
  DIFFICULTY_RUBRIC · COMMON_TYPES · AUTHORING_GUIDE · subject catalogs aligned to subject_code
  (math1·math2·science·social·history·english·korean·english_passage_level) · PROMPT_math2.
  Historical records (`output/**`, `analysis/rev/**`, append-only logs) keep old names as
  snapshots. Content-level Korean (subject names in prose, quoted exam text) stays allowed.
- 260825 **v1.6** — forecast pipeline + two-layer persona (user decisions): dedicated
  forecast chain (`forecast-writer` · `forecast-reviewer` · `forecast-auditor` ·
  `forecast-arbiter`) added to actor enum; differential governance by scope certainty;
  persona standard = fixed layer (Sangsang High subject teacher & expert item writer)
  + variable layer line `Target cohort: grade 1 (2026)` across all judgment-side agents.
  Procedure spec: FORECAST_GUIDE §0; mappings: REV_GUIDE §3-b.
- 260825 **v1.7** — A12 명문화(user decision "§1.3 명문화"): §1.5 신설 — 정답지류(회차 공용
  자료)는 코퍼스ID 미발급, HARVEST_LOG note+meta.yml answer_key로 추적, INDEX 등재 시 ID `-`,
  발견 당시 물리 위치 유지 원칙.
