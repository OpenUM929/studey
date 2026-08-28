---
title: "3층 아키텍처 구축 계획"
created: 2026-08-25
author: main-loop
status: 완료(P0–P4 전 단계 반영 · 260825 Group P/wrap — 운영 사이클은 별도 착수)
related_rev: "analysis/rev/260825_01_tag_pipeline_mismatch.md" (260825 위치 표준에 따라 analysis/rev/로 이전됨)
---

# 계획서 — 3층 아키텍처 구축 (원문 코퍼스 · 학생 응답 · 학부모 공유)

> **작성**: 2026-08-25, 메인 루프 (사용자 요청에 따른 신설 건설 계획)
> **상태**: 승인 대기 — Phase별 착수 승인은 §7 체크박스로 받는다
> **전제 검토서**: [`analysis/rev/260825_01_tag_pipeline_mismatch.md`](../../analysis/rev/260825_01_tag_pipeline_mismatch.md) (결함 9건, 체크박스 5건 대기)
> **데이터 표준**: [`../../docs/DATA_STANDARD.md`](../../docs/DATA_STANDARD.md) v1 — enum·ID·날짜·원장 스키마의 정본. 본 문서 §4는 요약이며 충돌 시 표준이 우선한다
> **지배 규범**: CLAUDE.md 원칙 3(append-only)·6(자료등급)·7(범위 미확정)·8(검토·수정 분리)

---

## 0. 이 문서의 성격과 경계

- 이 문서는 **새로 만드는 것**(디렉터리·파일·도구)만 정의한다.
- **기존 파일의 변경**(web/parser.js, web/app.js, 모의40 본문 등)은 전부 검토서 260825_01의
  체크박스 승인 대상이며, 여기서 중복 기술하지 않는다. 원칙 8 준수.
- 웹 UI·도구 스크립트는 **정본이 아니다**. 정본은 언제나 마크다운/TSV 파일이고,
  웹·도구는 그것을 읽고 쓰는 입력기·뷰어일 뿐이다. 웹이 정본으로 둔갑하려는 순간이
  원칙 3·8이 무너지는 지점이다(구조로 막는다: §6).

## 1. 배경 — 왜 이 3개 층이 필요한가

현재 파이프라인은 "원본 → 유형 카탈로그(요약)"만 영속화되고, 그 사이와 아래의 세 층이 비어 있다.

| 층 | 갭 | 실제로 일어난 일 |
|----|-----|------------------|
| ① 원문 코퍼스 | PDF/이미지 판독 전사본의 영속 보관소 없음 | 부교재 93문항 전사본이 세션 스크래치패드에서 **유실**. 카탈로그 요약(SM2-01~33)만 생존 |
| ② 학생 응답 | 채점→약점→처방→해소 판정의 원장 없음 | `analysis/student/` 6건은 일회성 분석 문서. 웹 채점 결과는 localStorage에 갇혀 리셋 한 번에 전소(검토서 F8) |
| ③ 공유 | 학부모 정기 공유 산출물과 발행 이력 없음 | 매 회차 수동 보고, 추적 불가 |

또한 위 데이터 흐름의 외래키인 **유형 태그 배관이 끊겨 있다**(검토서 F1~F9: 실데이터 문항 0개 파싱 포함).
본 계획의 Phase 2에서 함께 수선한다.

## 2. 확정 결정사항 (260825 사용자)

| # | 결정 | 내용 |
|---|------|------|
| D1 | X와 / 분리 추적 | X=오답(개념·절차 결손), /=백지·미완주(완주력 결손) — 서로 다른 처방 라인 |
| D2 | △ = 불확신 정답 | 약점이 아니라 관찰 대상. 같은 유형 △ 2회 누적 시 약점 '발견'으로 승격 |
| D3 | 단일 원장 | 채점 사실의 유일한 저장소는 `ATTEMPT_LOG.tsv`. 회차별 요약 MD는 도구 생성물 — 손으로 이중 기록 금지 |
| D4 | MASTERY 재생성물 | 집계 테이블은 도구가 ATTEMPT_LOG에서 재생성. 손으로 고치지 않는다 |
| D5 | 웹=입력기+뷰 | localStorage는 임시 버퍼. 버려도 아무것도 잃지 않아야 한다 |
| D6 | 모의40 미풀 | 첫 ATTEMPT_LOG는 빈 원장. 단 WEAK_LEDGER는 1학기 자산으로 WK-01(E5) 시딩 |
| D7 | 전사본 복구 분리 | 부교재 93문항 재판독은 별도 세션. HARVEST_LOG에 미수확 잔여로만 기록 |
| D8 | 판단 원장 TSV 통일 | WEAK_LEDGER 포함 전 원장을 TSV로. 사람 서술은 `note` 컬럼으로 흡수 |
| D9 | mark ASCII 코드 | 저장=`correct/unsure/wrong/blank`, 화면 출력만 O/△/X// 매핑 (DATA_STANDARD §4.1) |
| D10 | 표준 정본 분리 | `docs/DATA_STANDARD.md` 신설(전역 층), QUIZ_STANDARD는 문제지 입력 규격 전용 |

## 3. 디렉터리 설계 (신설 전체)

```
docs/DATA_STANDARD.md                # 데이터·문서 표준 정본 v1 (260825 신설)

corpus/                              # ① 원문 코퍼스 (git 추적, 정본)
  README.md                          #   ID 규칙·등급 규칙
  HARVEST_LOG.tsv                    #   수확 이력 (append-only)
  SUP-M2-2026/                       #   스무년 고1-2.pdf
    meta.yml · source.md · figures/

analysis/catalog/index.tsv           # 유형 인덱스 (카탈로그에서 기계 생성)

student/S01/                         # ② 학생 응답 층 (S01 = 학생 1명 가정)
  profile.md                         #   목표선·기준 회차
  ATTEMPT_LOG.tsv                    #   문항 시도 원장 (append-only, UTF-8 BOM)
  MASTERY.tsv                        #   유형별 숙련도 (재생성물)
  WEAK_LEDGER.tsv                    #   약점 상태기계 (WK-01 E5 시딩)
  reports/                           #   build_report.py 산출물

share/
  SHARE_LOG.tsv                      # ③ 공유 이력 (append-only)

tools/
  build_catalog_index.py · build_mastery.py · import_grading.py · build_report.py
```

## 4. 스키마 요약 (정본: DATA_STANDARD v1 §5)

아래는 발췌 요약이다. 컬럼 정의·enum 코드·ID 패턴의 **정본은 DATA_STANDARD**이며,
여기 예시와 충돌하면 표준을 따른다.

### 4.1 유형 태그 표준형 (문제지·답안표 공통)

```
[주유형 · Tier · DF코드목록 (+보조유형)*]

예시: [SM2-13 · T4 · DF1·DF8 · +SM2-11]
```

- **공백 허용**을 표준으로 하고, 무공백 밀착형도 파서가 양방향 수용(기존 40문항 무손실).
- 답안표 col3는 동일 정보의 무괴호형(`SM2-13·T4`) 허용 — 파서가 두 형식 모두 읽는다.
- 화면 노출 3모드: **실전=숨김**(풀이 중 접근법 새어나감 방지) / **복습=표시** / **분석=표시+필터**.

### 4.2 ATTEMPT_LOG.tsv — 단일 원장 (D3, append-only)

UTF-8 BOM 필수. 탭 구분. 1행 = 1문항 1시도. `mark_code`는 D9 ASCII 코드.

```
date	set_id	qnum	main_type	aux_types	tier	df	mark_code	student_answer	correct_answer	fail_code	note
2026-08-22	SET-260822-math2-40	13	SM2-14	-	T3	DF5	wrong	2	3	E5	등호 누락
2026-08-22	SET-260822-math2-40	16	SM2-13	SM2-11	T4	DF1,DF8	blank	-	18	-	미착수
```

과거 행 수정 금지 — 정정은 새 행 + `note`에 `fix:` 접두어.

### 4.3 MASTERY.tsv — 유형별 숙련도 (D4, 재생성물)

`tools/build_mastery.py`가 ATTEMPT_LOG × index.tsv에서 재생성. 손편집 금지.

```
type_id	unit	importance	attempts	o_count	amb_count	wrong_count	blank_count	last3	status_code
SM2-14	I-3 원의방정식	★★★	5	2	1	1	1	oaw	weak
SM2-25	I-4 도형의이동	★★	0	0	0	0	0	-	unmeasured
```

판정 기준(mastered/unstable/weak/unmeasured)의 정본은 DATA_STANDARD §4.2.
⬜ 미측정 칸이 "안 틀렸다"와 "안 냈다"를 구분 — 원칙 7의 사각지대를 학생 단위로 구현.

### 4.4 WEAK_LEDGER.tsv — 약점 상태기계 (D8)

```
wk_id	axis	evidence_types	evidence_codes	found_date	state	prescription	resolve_condition	resolved_date	note
WK-01	E5 경계 조건(등호 포함·배제 판단)	SM2-03,SM2-14,SM2-18,SM2-25,SM2-28	SM-11,E5	2026-07-21	found	-	동일 축 T3 2연속 correct	-	1학기 중간 9번(SM-11) 오답 기원; 모의40 해설 3·13·26·34번 반복 지목
```

상태 전이(DATA_STANDARD §4.3):

```
found ──처방 생성──▶ prescribing ──세트 채점──▶ retesting ──조건 충족──▶ resolved
                        ▲                                        │동일 축 wrong 재출현
                        └────────── relapsed(Tier +1 재처방) ◀───┘
```

분기 규칙(D1·D2):

| 표기 | 라인 | 처방 | 해소 조건 기본값 |
|------|------|------|------------------|
| wrong(X) | 개념 보강 | 동일 축 T2→T3→T4 사다리 세트 | 동일 축 T3 **2연속 correct** |
| blank(/) | 완주 훈련 | 제한시간 내 동일 Tier T4 단독 완주 | 제한시간 내 완주 **2회** |
| unsure(△) | (약점 아님) | 관찰만 | 같은 유형 △ 2회 누적 → found 승격 |

WK-01 시딩 근거: `analysis/catalog/수학.md:218-231`(1학기 중간 9번 SM-11 오답) +
모의40 해설 4곳 반복 언급. 발견일 소급 2026-07-21(오답분석일), 상태 found(처방 미생성), 최상단 배치.

### 4.5 index.tsv — 유형 인덱스 (조인의 근원)

```
type_id	subject_code	unit_major	unit_minor	importance	status_code
SM2-14	math2	I.도형의방정식	3.원의방정식	★★★	verified_aux
```

`tools/build_catalog_index.py`가 `analysis/catalog/*.md`의 유형 블록에서 재생성. 카탈로그 갱신 시 재실행.
문제지·채점·약점 어느 문서든 유형ID만 있으면 이 표로 조인된다.

### 4.6 corpus/ — 원문 코퍼스

- 문항 ID: `<코퍼스ID>-Q<번호>` (예: `SUP-M2-2026-Q07`). 카탈로그 유형의 `출처` 필드에서 역참조.
- meta.yml 서식: DATA_STANDARD §5.7 참조(SUP-M2-2026 샘플 포함).
- HARVEST_LOG.tsv 첫 행: DATA_STANDARD §5.5 참조 — "미수확 잔여" 칸이 같은 자료를 다시 볼 가치의 판단 근거.

### 4.7 문제지 세트 프론트매터

output 세트 md 머리말(DATA_STANDARD §5.8):

```yaml
---
set_id: SET-260822-math2-40
student: S01
subject_code: math2
term: 2026-2
unit: I. 도형의 방정식
scope_confirmed: false     # false → 뷰어·리포트에 ⚠️ 범위 미확정 배지 (원칙 7)
---
```

H1은 그대로 유지 — 기존 파서 호환. 구(舊) 문제지처럼 frontmatter가 없으면 `scope_confirmed=false` 간주.

## 5. 도구 명세 (tools/) — 전부 표준라이브러리만, 강제 UTF-8

| 도구 | 입력 → 출력 | 핵심 규칙 |
|------|-------------|-----------|
| build_catalog_index.py | catalog/*.md → index.tsv | 멱등 재생성. 카탈로그 변경 시 재실행 |
| import_grading.py | 채점 TSV(웹 export 또는 손작성) → ATTEMPT_LOG append + MASTERY 재생성 | DATA_STANDARD §6 검증 수행(set_id·유형ID·enum 위반 행 거부). BOM 보존. **WEAK_LEDGER는 직접 고치지 않고 갱신 제안만 출력** (상태기계 판정은 사람 확인) |
| build_mastery.py | ATTEMPT_LOG + index.tsv → MASTERY.tsv | import_grading에서 호출, 단독 실행도 가능 |
| build_report.py | S01 원장들 + index.tsv → reports/<YYMMDD>_report.html + SHARE_LOG.tsv append | 외부참조 0 단일 HTML. 모든 수치는 원장에서 도출 — 손입런치 없음 |

## 6. 웹 변경 범위

- **기존 파일 수선**(parser.js·app.js): 검토서 260825_01 체크박스 범위 그대로. 여기서 반복하지 않는다.
- **신규 기능**:
  1. 드래그&드롭이 `.tsv`도 수용 — FileReader 방식이라 file:// 환경의 fetch 제한을 피한다.
     ATTEMPT_LOG·MASTERY·WEAK_LEDGER·index.tsv를 끌어놓으면 「이력 / 유형 현황 / 약점」 탭에서 렌더.
  2. 탭 4종: 풀기(현행) / 이력(ATTEMPT_LOG) / 유형 현황(MASTERY×index 조인, 단원별 커버리지) / 약점(WEAK_LEDGER).
  3. 「채점 원장 내보내기」 — mark_code 기반 TSV 다운로드(BOM 포함, set_id는 프론트매터에서).
     학생이 자기 기기에서 풀고 파일 하나를 돌려주면 당신의 작업은 commit뿐이 된다.
- **경계 선언**: localStorage는 임시 버퍼(초기화 안내문에 명시). 내보내기 전 분실해도 손해 0.
- 표시 계층에서만 O/△/X// 심볼 사용(D9) — 저장·내보내기는 항상 코드.

### 데이터 흐름 전체도

```
문제지 MD ──[태그]──┐
채점(O△X//) ───────┴─▶ ATTEMPT_LOG.tsv ──build_mastery──▶ MASTERY.tsv
index.tsv ─────────────────┘                    │
                          import_grading 제안 → (사람 판정) → WEAK_LEDGER.tsv
                                                          │
                                     build_report → reports/*.html → SHARE_LOG.tsv
```

## 7. 실행 Phase와 착수 승인

| Phase | 내용 | 완료 조건 | 승인 |
|-------|------|-----------|------|
| P0 | DATA_STANDARD v1 신설 + 본 계획서 표준화 소급 수정 + QUIZ_STANDARD 개정 검토서(260825_06) 작성 | (260825 실행됨) | - [x] 소급 승인(260825 "순차 진행" 질의 응답) |
| P1 | corpus 골격(README·HARVEST_LOG.tsv·SUP-M2-2026/meta.yml) + index.tsv 33행 + S01 템플릿 4종(profile·ATTEMPT_LOG 빈원장·MASTERY 빈원장·WEAK_LEDGER.tsv WK-01 시딩) + share/SHARE_LOG.tsv | 파일 존재·**DATA_STANDARD v1 준수**, 빈 원장에서 mastery dry-run 통과 | - [x] 260825 Group O3 실행 — index.tsv는 `build_catalog_index.py`가 전 과목 131행 생성(math2 부분집합=33행 일치). corpus README는 G6 `_README.md`로 충족 |
| P2 | 검토서 체크박스 반영(parser.js F1~F6·F9, app.js 4상태+내보내기, 모의40 16번 +SM2-11) — **검토서 체크박스 승인 선행** | node 재실행 problems=40·typeId 40/40, 4상태 마킹·TSV export 동작 확인 | - [x] 260825 Group P 실행 — 판정 `07`·`12` 승인 후 규정 순서(CB2→CB1+12-CB1→CB3)로 반영. node 수용기준 **40/40/40/함정6/보조1** 통과(python 미러 동일). 브라우저 클릭 레벨 확인은 첫 실사용 시 확정 |
| P3 | tools 4종 | 가짜 채점 5행 end-to-end dry run → MASTERY 재생성·리포트 HTML 생성 확인 | - [x] 260825 Group O4 실행 — build_catalog_index(P1로 전진)+import_grading(원자적 검증·위반행 전체 거부 exit2)+build_mastery(--check)+build_report. dry run 임시 디렉터리 통과(SM2-13 o+a→unstable 등), S01 정본 원장은 빈 상태 유지(D6) |
| P4 | CLAUDE.md 작업 흐름 표에 신규 경로 행 추가(기존 행 보존) + 모의40 머리말 프론트매터 삽입 | 파서가 메타블록 인식(scope_confirmed 배지 노출) 확인 | - [x] 완료 — CLAUDE.md 행 추가 + 260825 Group P-wrap에서 모의40 frontmatter 삽입(`SET-260822-math2-40`, scope_confirmed=false)·data.js 재생성으로 배지 노출 확인(QS-3 해소 후 실행) |

P2의 반영 주체는 원칙 8에 따라 item-writer 또는 사용자다(검토서 작성자 아님).

## 8. 보류 항목

| 항목 | 사유 | 재평가 시점 |
|------|------|-------------|
| 학생×과목×단원 히트맵 대시보드 | 학부모 리포트와 내용 90% 중복. 원장 2회차분 미달 | 실데이터 2회차 이후 |
| 부교재 93문항 전사본 복구 | 작업량 큼 — 결정 D7 | 별도 세션 |
| 서버·DB·계정 | 단일 HTML+파일 교환으로 충분. 원칙 3·8은 git diff를 전제 | 영구 불요 |

## 9. 리스크와 방어

| 리스크 | 방어 |
|--------|------|
| TSV 손편집 오류(탭 누락·유형ID 오탈자) | 웹 채점→내보내기 경로 권장. import_grading이 DATA_STANDARD 검증 |
| 인코딩(CP949 콘솔 vs UTF-8 파일) | 모든 도구 UTF-8 강제, TSV는 BOM |
| localStorage 분실 | 내보내기 버튼 + 초기화 안내문 개선(F8 반영) |
| 원장 이중화 유혹 | D3 단일 원장 원칙 — 회차 요약은 생성물만 |
| 범위 추정의 확정화 | scope_confirmed:false 배지 유지(원칙 7) |
| 표준과 문서의 재차 불일치 | 스키마·enum의 단일 정본 = DATA_STANDARD. 개정은 승인 후 이력 남김 |

## 10. 열린 질문

- **Q3** (검토서 01과 동일) 태그 표준형 보강 범위 — 안 a) 16번만 +SM2-11 / 안 b) 40문항 전체 표준형 재작성. P2 착수 전 판정 필요.
- **Q4** (검토서 02에서 판정 요청) REV_LOG(MD 표)의 TSV 전환 여부 — REV_지침 §4 개정을 수반하므로 별도 승인.

## 이력
- 260825 작성 — 메인 루프. 사용자 결정 D1~D7 반영. 관련 검토서 260825_01(F1~F9)과 상호 참조 설정.
- 260825 표준화 소급 — 파일명 `plan_3layer_architecture.md`로 변경, frontmatter 추가,
  D8~D10 반영(TSV 통일·mark_code·DATA_STANDARD 위임). §4를 요약층으로 격하하고 정본을 DATA_STANDARD로 위임.
- 260825 동기화 — 검토서 02→06 재번호(타 세션 선등록 충돌, 선착순 규칙) 및 문서위치_표준 §2에 따른 rev 홈 이전(`analysis/rev/`)을 헤더 링크·P0 참조에 반영.
- 260825 **A11 소화** — Group O3에서 P1 착수(사용자 승인 "순차 진행"): 본 계획서가 만드는
  모든 ID는 CODE_REGISTRY §5 부여 규칙 + 선점 확인을 우선 적용한다. P1 산출물은 기등록
  계열(SM2 유형ID·WK-01·S01·SET·코퍼스ID v2)만 사용 — 신규 접두어 없음을 확인했다.
