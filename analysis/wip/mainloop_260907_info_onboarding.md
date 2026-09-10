---
actor: main-loop
task: 정보 과목 온보딩 + Python 학습지 2종 정제·분류·출제
target: SUP-info-2026-01, SUP-info-2026-02, analysis/catalog/info.md
status: active
updated: 2026-09-08
---

# WIP — mainloop_260907_info_onboarding

PRD: `output/260907/260907_01_info_onboarding_prd.md`

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| S0 | PRD + WIP 개설 | done | PRD 65행 · 이 파일 | 사용자 확정 D1~D3 반영 |
| S1 | 명명 정책 선행 등록 | done | DATA_STANDARD v1.10(§1.3 v3 패턴) · corpus/_README · CODE_REGISTRY 이력 | 게이트: 신규 2ID MATCH, 기존 4ID MATCH 유지, 오형식 2건 거부 |
| S2 | 폴더·파일 개명 + 해시 검증 | done | origin_data/SUP-info-2026-0N/pNN.png · corpus/_images/... · output/260907/_rename_map.json | 17행 매핑, 전건 sha256 불변, 디렉터리 불변식 위반 0 |
| S3 | 1차 정제(전사) 15p | done | corpus/SUP-info-2026-0N/{transcript,meta.yml,verify_log.tsv} + HARVEST_LOG 2행 | items 01=24 / 02=31. HARVEST 68->70행 |
| S4 | 정보 온보딩 8항목 | done | CODE_REGISTRY §1·§3 · DATA_STANDARD §5.8 · catalog/info.md · curriculum_2022 정보 절 · build_catalog_index · md2quiz · index.tsv | **260908 8/8 완료(일괄)**. 게이트 `--check` [OK] 157행, WARN/FAIL 0줄 |
| S5 | 1차 분류(기출 EX-info-20252M 25문항) | done | info.md IN-01~IN-18 | 25/25 전건 배정, 문항->유형 원장 포함 |
| S6 | 1차 분류(학습지) + 개념↔실습 매핑 | done | info.md IN-19~IN-26 + per-item 원장 | 24/24 · 31/31 전건. 중복 8건은 기존 항목에 누적(신설 안 함) |
| S7 | 신규 문제 생성 | done | output/260908/260908_04_info_midterm_26.md + .novelty.tsv | 26유형 각 1문항, 100점. 자기 검산 26/26 FAIL 0 |
| S8 | 맹목 풀이 | blocked | — | `solve-back-verifier`가 이 세션 cwd에 서브에이전트로 미등록. **자기 검산은 이 게이트를 대신하지 못한다** |
| S9 | 단순변형 감사 | partial | 세트 「검증 이력」 + .novelty.tsv 26행 | 기출 25문항 원문 대조로 동형 4건 적발·재설계. 단 **작성자 자기 감사**이며 `item-quality-auditor` 독립 감사 미실시 |

## S2 개명 매핑 (요약 — 전체는 `output/260907/_rename_map.json`)

| 구 | 신 |
|---|---|
| `origin_data/Python_2학기_1학년_개념/` | `origin_data/SUP-info-2026-01/` |
| `origin_data/Python_2학기_1학년_실습_문제/` | `origin_data/SUP-info-2026-02/` |
| `4fce8096-...-497c.pdf-00NN.png` (10개) | `p01.png` ~ `p10.png` |
| `1f06def2-...-2fc2.pdf-000N.png` (5개) | `p01.png` ~ `p05.png` |
| `Python_2학기_1학년_개념.zip` | `SUP-info-2026-01.zip` |
| `Python_2학기_1학년_실습_문제.zip` | `SUP-info-2026-02.zip` |

## 260908 재개 기록 — S4 완료

중단 지시 뒤 재개. NEXT에 적힌 수용기준을 그대로 집행했다.

### 온보딩 8항목 (CODE_REGISTRY §6) — 전부 완료

| # | 대상 | 실제 변경 |
|---|------|----------|
| 1 | CODE_REGISTRY §1 | 접두어 등록 행 추가 — `IN` / catalog/info.md / 정보 / 1~26 / 동결 |
| 2 | CODE_REGISTRY §3 | 260826 선행분. "S4 온보딩 예정" 단서를 지워 info 행을 실현 |
| 3 | DATA_STANDARD §5.8 | 260826 선행분(변경 없음) |
| 4 | catalog/info.md | 260907 신설분 + 배너 교체 + `영역/단원` 26행 정규화 |
| 5 | curriculum_2022.md | **정보 절 신설**(107행~). 성취기준은 `blocked` 유지 |
| 6 | build_catalog_index.py | `SUBJECT_FILES["info.md"]="info"`, `EXPECTED["IN"]=26`, 독스트링 7→8 |
| 7 | md2quiz.py | `SUBJECT_MAP`에 `정보|파이썬|Python` → `info` (과학·사회·한국사 **뒤**에 배치) |
| 8 | index.tsv | 재생성 131 → **157행**(+26) |

### 게이트 실측

```
python tools/build_catalog_index.py --check
[OK] index.tsv matches regeneration (157 rows)
exit=0
```
`[WARN]`·`[FAIL]` 0줄. 260908 이전의 `unregistered catalog: info.md` FAIL은 해소됐다.

### 이번에 내린 판단 (근거 병기)

- **`영역/단원` 표기 정규화**: 기존 값 `관측 — 파이썬 기초 · 연산자`는 인덱서 `parse_units`가
  첫 공백에서 끊어 `unit_major="관측"`을 만든다(전 26행이 같은 major). 조인키로 못 쓴다.
  과학 카탈로그 선례(`생명시스템 > 유전자와 단백질`)에 맞춰 `대영역 > 소단원 [관측]`으로 바꿨다.
  `parse_units`가 `[`이후를 잘라내므로 `[관측]` 표식은 인덱스를 오염시키지 않는다(실측 확인).
- **성취기준은 채우지 않았다**: 웹 검색으로 교육부 고시/NCIC 원문을 확보하지 못했고 2차 자료
  (나무위키·연구보고서)뿐이었다. §6 단서대로 `blocked`. 검색으로 본 5개 영역 골격은
  curriculum_2022 정보 절에 **"근거로 쓰지 않는다"는 단서와 함께** 참고 기록만 남겼다.
- **md2quiz 패턴 순서**: `정보`는 "정보통신"(통합과학)·"정보화 사회"(통합사회)에 걸린다.
  과학·사회·한국사 패턴이 먼저 소비하도록 그 뒤에 넣었다(코드 주석에 이유 기재).

### 미해소 발견 (수정하지 않고 기록만 — 원칙 8 검토·수정 분리)

- **선행분**: `tools/build_corpus_unit.py:68` `RE_ID`가 DATA_STANDARD §1.3보다 좁아
  `SUP-math2-2026`·`SUP-info-2026-01`을 모두 거부한다. 260907 패턴 개정 이전부터의 불일치.
- **신규 관측**: `tools/build_catalog_index.py` 쓰기 모드의 요약 출력이
  `for subj, *_ in rows`로 **행의 0번(type_id)** 을 과목으로 착각한다. 그래서 이번 실행이
  `BI-01: 1 types`처럼 유형ID별로 찍혔다(과목별 합계가 아님). 게이트 판정에는 영향이 없는
  **표시 전용 결함**이라 이번 작업 범위(온보딩)에서 손대지 않았다. 실측 증거 = 위 실행 출력.

### 남은 요구사항

| 요구 | 상태 |
|---|---|
| 1·2 폴더/파일명 표준화 | 완료 |
| 3 매핑 | 전/후 완료 · **개념↔실습 독립 문서 미작성** |
| 4 유형정리 갱신 | **완료 — 정본 등록까지 성립(260908)** |
| 5 유형별 신규 문제 생성 | 미착수(S7) |
| 6 단순변형 감사 | 미착수(S9) |

NEXT: 요구사항 3 잔여(개념↔실습 매핑 문서) → S7 신규 문제 생성 → S8 맹목 풀이 → S9 단순변형 감사.
S7 문항은 전부 `scope_confirmed: false`이며 근거 페이지(`SUP-info-2026-0N pNN`)를 문항마다 인용한다.

---

## 260908 재개 기록 2 — 요구사항 3 잔여 · S7 완료

### 산출물

| 요구 | 산출물 | 실측 |
|---|---|---|
| 3 개념↔실습 매핑 | `output/260908/260908_03_info_concept_practice_map.md` | 지면 성격 12행 · 개념 C1~C9 · 실습 P1~P13(합 55 = 24+31 검증) · 정방향/역방향 전건 매핑 · 갭 분석 7-a~7-d |
| 5 유형별 신규 문제 | `output/260908/260908_04_info_midterm_26.md` | 26문항(선택형 18 = 70.0점 + 서답형 8 = 30점). IN-01~IN-26 각 1문항, 유형 내 중복 0 |
| 5 신규성 원장 | `output/260908/260908_04_info_midterm_26.novelty.tsv` | 8열 26행, BOM+LF, 본문 문항ID와 1:1 일치(스크립트 대조), FAIL 0 |
| — 정본 등록 | `output/_index.md` | 26행 추가, 상태 전건 `검토필요` + 머리말에 분모 구분 문단 |
| — 과목 표 | `analysis/TYPE_CATALOG.md` | info.md 행 추가(info.md 동반 갱신 목록에 있었으나 누락돼 있던 것) |

### 이번에 실측한 것 (추측 아님)

- **난이도 자**: 기출 선택형 18문항 배점 합이 정확히 70.0 → 평균단가 3.889.
  이 단가로 기출 최저 3.2 = `r` 0.823(T1), 최고 4.4 = `r` 1.131(T4)이 되어 DIFFICULTY_RUBRIC §1
  밴드에 들어맞음을 확인한 뒤 세트 배점을 환산했다.
- **solve-back**: 26문항 전건을 파이썬으로 실행. 정답뿐 아니라 **오답지 값까지** 계산해
  모든 오답이 실제 오류 경로에서 나오도록 했다. FAIL 0.
- **N축 대조**: `corpus/EX-info-20252M/transcript.md`의 25문항 원문을 **선지까지 열어** 대조했다.
  초안 4건이 동형으로 걸려 재설계했다 — 10번(기출 7과 발문·정답 구조가 사실상 동일),
  12번(기출 6과 동형), 18번(학습지 실습 1과 소재·해법 중복), 20번(학습지 Quiz 4와 풀이 골격 동일).
  **추측이 아니라 원문을 나란히 놓고 내린 판정**이다.
- 대조에서 얻은 부수 사실: 기출 선택 9가 `or`를, 선택 12가 요소 순회 `for i in a`를,
  선택 6이 NC·SA 설명을 선지로 쓴다. `260908_03` §7의 "학습지 기준 갭" 판정은 그대로 유효하지만
  **기출 근거는 그만큼 더 넓다**.

### 레인 실측 (없는 레인을 실행한 것처럼 적지 않는다)

이 세션의 cwd는 Nconnect 저장소이고, study 저장소의 `.claude/agents/` 정의는 이 세션에
서브에이전트 타입으로 등록돼 있지 않다. 따라서:

| 단계 | 지침상 담당 | 실제 수행 |
|---|---|---|
| S7 생성 | `item-writer` | **메인 루프가 역할 정의를 읽고 직접 수행**(필독 정본 6종 전부 로드) |
| S8 맹목 풀이 | `solve-back-verifier` | **미실시** — 무엇으로도 대체하지 않았다 |
| S9 신규성 감사 | `item-quality-auditor` | **작성자 자기 감사만** — 독립 감사가 아니다 |

`item-writer` 정의의 "Planned, unavailable, or failed lanes must be marked, never reported as
executed"를 그대로 적용한 기록이다. 원칙 12(피측정자는 자기 자를 소유하지 않는다)에 따라,
자기 검산 결과를 게이트 통과로 승격하지 않았다.

### 미해소 발견 추가

- `tools/build_catalog_index.py` 쓰기 모드 요약 출력이 `for subj, *_ in rows`로 행의 0번(type_id)을
  과목으로 착각해 `BI-01: 1 types`처럼 찍힌다. 게이트 판정에는 영향이 없는 표시 전용 결함이라
  이번 작업 범위 밖으로 두고 기록만 한다(원칙 8 검토·수정 분리).
- `output/_index.md` 머리말이 "65/65 배포가능"으로 시작하는데 정보 26제는 그 분모 밖이다.
  분모 혼동을 막으려고 머리말에 명시 문단을 추가했다(원칙 11-a).

NEXT: S8 독립 맹목 풀이와 S9 독립 품질감사. 둘 다 이 저장소 밖의 배우(외부 Claude Code 등)가
필요하므로, 그 레인이 열리기 전까지 세트 상태는 `검토필요`에 머문다.
착수 명령: `output/260908/260908_04_info_midterm_26.md`를 **정답표를 가린 채** 전건 풀게 하고
26문항 답을 대조한다. 통과한 뒤에야 `output/_index.md` 상태를 `배포가능`으로 올린다.

---

## 260908 중단 기록 (사용자 지시)

세션명 "정보 문제 만들다가 데이터 문제로 정지_다른 작업으로 인해 작업 대기_260907"로 중단.
**정본은 부분 갱신 상태로 멈춰 있으며, 그 사실을 은폐하지 않도록 아래에 실측을 남긴다.**

### 지금 저장소의 실제 상태 (실행 결과)

```
python tools/build_catalog_index.py --check
[OK] index.tsv matches regeneration (131 rows)
[WARN] consistency issues:
  - unregistered catalog: info.md holds 26 type blocks but is not in SUBJECT_FILES
[FAIL] 1 consistency issue(s) - gate not passed
```

이 FAIL은 **의도된 것**이다. 게이트가 부분 온보딩을 정확히 잡아냈다.
(참고: 이 도구는 `[FAIL]`을 찍고도 exit 0을 반환한다 — CLAUDE.md 원칙 11 BF3의 알려진 fail-open.
 판정은 exit code가 아니라 출력 문자열로 한다.)

### CODE_REGISTRY §6 온보딩 8항목 현황

| # | 대상 | 상태 |
|---|------|------|
| 1 | CODE_REGISTRY §1 접두어 `IN` 등록 행 | **미완** |
| 2 | CODE_REGISTRY §3 subject_code 매핑 | 완료(260826 선행 등록) |
| 3 | DATA_STANDARD §5.8 subject_code enum | 완료(260826 선행 등록) |
| 4 | `analysis/catalog/info.md` 신설 | **완료(260907)** — 26유형 |
| 5 | `analysis/curriculum_2022.md` 정보 절 | **미완** — 성취기준 조회 불가로 `blocked` 예상 |
| 6 | `tools/build_catalog_index.py` SUBJECT_FILES·EXPECTED | **미완** — 위 FAIL의 원인 |
| 7 | `tools/md2quiz.py` SUBJECT_MAP | **미완** |
| 8 | `analysis/catalog/index.tsv` 재생성 | **미완** — 현재 131행(info 미포함) |

### 남은 요구사항 (사용자 6개 중)

| 요구 | 상태 |
|---|---|
| 1 폴더명 표준화 | 완료 |
| 2 파일명 표준화 | 완료 |
| 3 변경 전/후 + 개념<->실습 매핑 | **부분** — 전/후 매핑 완료(`output/260907/_rename_map.json`), 개념<->실습 매핑표는 info.md per-item 원장으로 대체 가능하나 **독립 문서 미작성** |
| 4 유형정리 문서에 실습 유형 추가 | 완료(단, 정본 등록은 #6·#8 전까지 미성립) |
| 5 유형별 신규 문제 생성 | **미착수** |
| 6 단순변형 감사 | **미착수** |

### 미해소 발견 (재개 시 판단 필요)

- `tools/build_corpus_unit.py:68` `RE_ID = ^(?:EX|SUP|NY)-[a-z0-9_]+-\d{5}[MF]$` 가
  DATA_STANDARD §1.3보다 좁아 `SUP-math2-2026`·`SUP-info-2026-01`을 모두 거부한다.
  **260907 패턴 개정 이전부터 있던 불일치**이므로 이번 작업에서 고치지 않았다. 확인 필요.
- `EX-info-20252F`(기말) 미분류. info.md에 `scope: partial`로 명시돼 있다.

~~NEXT (S4 시절 — 260908 S4 완료로 **폐기**. 유효한 재개 지점은 `analysis/wip/RESUME.md`)~~: 재개 시 S4 잔여 온보딩 #1·#5·#6·#7·#8을 **한 작업으로 묶어** 처리한다(부분 갱신 금지,
CODE_REGISTRY §6). 수용기준은 `python tools/build_catalog_index.py --check` 출력에
`[WARN]`·`[FAIL]` 0줄 + `[OK] index.tsv matches regeneration` + 행 수가 131 -> 157(131+26)로
증가하는 것. 그 게이트를 통과한 뒤에야 S7(신규 문제 생성)에 들어간다.
