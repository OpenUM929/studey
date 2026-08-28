---
title: "CRLF 개행으로 인한 프론트매터·선택지 파싱 전면 실패 및 채점 TSV 내보내기 TypeError (Group P 반영분 사후 검증)"
source: web/parser.js
source_location: "parser.js:169(convertText 행분할) → 40행(parseFrontmatter)·63행(LEADING_OPTION_RE) / app.js:281(exportTsv flat) / 대상 데이터 output/260822/…모의40.md · output/260714/공통영어1_모의25.md"
created: 2026-08-26
author: Claude Code (rev-arbiter class, 사용자 직접 지시로 검증+수정 겸행)
status: closed
reviewer: 사용자 (수정 권한 부여 — "확인하고 작업하고 수정 내역과 근거를 남겨줘")
---

# 검토서 01 — CRLF 파싱 실패 2건 + TSV 내보내기 TypeError 1건 (모두 수정 완료)

<document>

검증 대상은 `260825_group_p_application_report.md`(판정 07~12 반영 보고서)가
**"수용기준 통과"로 선언한 코드 트랙**이다. 보고서의 해당 주장 3개를 그대로 인용한다.

> §2.2 CB1 — "YAML frontmatter priority: `subject_code` overrides inference;
> `scope_confirmed` absent ⇒ false (fail-safe, §5.8); setId/unit/intended_use captured."

> §2.4 CB3 — "New 🧾 export builds ATTEMPT_LOG §5.1's 12 columns
> (`set_id,qnum,main_type,aux_types,tier,df,mark_code,…`), UTF-8 **with BOM**,
> ready for `tools/import_grading.py`."

> §2.5 수용기준 — "`problems=40 typeId=40 tier=40 traps=6 aux=1 extra=0` /
> python mirror convert_file(): identical counts."

수정 전 원본 코드 3곳:

```js
// web/parser.js 169행 — 수정 전
    var rawLines = text.split("\n");

// web/parser.js 40행 (parseFrontmatter 내부, m 플래그 없음)
      var m = /^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$/.exec(rawLines[i]);

// web/parser.js 63행 (m 플래그 없음)
  var LEADING_OPTION_RE = /^\s*([①②③④⑤])\s*(.*)$/;

// web/app.js 281행 — 수정 전
      function flat(v) { return (v && v.length) ? String(v).join(",") : "-"; }
```

</document>

<context>

이 저장소는 Windows(win32)에서 운용되며 `output/` 산출물 `.md`는 **전부 CRLF**다
(`file` 판정: `with CRLF line terminators`). 웹 뷰어(`web/`)는 문항 세트를 읽어 화면에
띄우고 채점 결과를 `ATTEMPT_LOG.tsv`로 내보내는 입력기이며, 정본 원장은 TSV다
(CLAUDE.md 원장 운용 행). `tools/md2quiz.py`는 같은 파싱을 파이썬으로 미러링한
구현으로, 판정 07은 두 구현이 **동작 동일(behaviour-identical)** 할 것을 요구했다.
Group P의 수용기준은 모의40 한 파일에 대한 **문항 단위 카운트 5개**(문항수·typeId·
tier·함정·보조)만 비교했고, 이 5개는 실제로 두 구현이 일치한다 — 결함은 그 5개가
건드리지 않는 **세트 메타·선택지·내보내기** 층에 숨어 있었다.

</context>

<findings>

### F1. CRLF 때문에 프론트매터가 **전량** 파싱 실패 (JS 단독, 파이썬은 정상)

JS `.` 는 줄 종결자(`\n \r    `)를 매치하지 않는다. 40행 정규식은 `m` 플래그가
없어 `$`가 **문자열 끝에서만** 매치된다. 따라서 `"set_id: SET-260822-math2-40\r"` 에서
`(.*)`가 `\r` 앞까지만 먹고 `$`가 실패 → **매치 없음**. 모든 키가 같은 이유로 실패한다.

```
$ node  (parser.js 35–44행 원본 그대로 복사 실행)
fm = {}                     ← null이 아니라 "키가 하나도 안 담긴 빈 객체"

with CR   : null
without CR: ["set_id","SET-260822-math2-40"]
"." matches \r ?  false
```

`fm`이 빈 객체라 169~178행의 세 갈래가 전부 폴백으로 떨어졌다:

| 필드 | 코드 | 수정 전 실측 | 정상값 |
|------|------|-------------|--------|
| `setId` | `fm.set_id ? … : sourceKey` | `"m"` (sourceKey) | `"SET-260822-math2-40"` |
| `subject` | `fm.subject_code ? … : detectSubject(title)` | `"math2"` — **제목 추론이 우연히 적중** | `"math2"` |
| `scopeConfirmed` | `!!(fm && fm.scope_confirmed === "true")` | `false` — **우연히 일치**(파일도 false) | `false` |

`subject`·`scopeConfirmed`가 맞은 것은 **우연**이다. 프론트매터에 `scope_confirmed: true`인
세트가 오면 무조건 `false`로 읽히고(범위 확정 세트가 미확정으로 표시됨), `subject_code`가
제목 추론과 어긋나는 세트는 과목이 틀리게 잡힌다. 즉 §2.2의 "frontmatter priority" 기능은
**한 번도 작동한 적이 없다**.

`setId`는 우연조차 없었다. 내보낸 TSV의 `set_id` 열에 `"m"`(브라우저에선 data.js 키)이
찍히므로 DATA_STANDARD §5.1 샘플(`SET-260822-math2-40`)과 어긋나고, `import_grading.py`가
세트를 식별할 수 없다.

**파이썬 미러는 정상이다** — `splitlines()`가 `\r`를 제거하기 때문:
`py setId : 'SET-260822-math2-40'`. 판정 07이 요구한 "동작 동일"이 실제로는 깨져 있었고,
수용기준이 문항 카운트만 비교했기 때문에 드러나지 않았다.

### F2. 같은 원인으로 **5지선다 선택지 파싱이 전 과목 실패** (F1보다 파급 큼)

63행 `LEADING_OPTION_RE`도 `m` 플래그가 없어 동일하게 깨진다. 모의40은
**수학=서답형 100%**(CLAUDE.md 페르소나 규정)라 선택지가 없어 이 결함이 가려졌다.
5지선다 과목 파일로 A/B 대조하면 즉시 드러난다:

```
$ node  (같은 parser.js, 입력 텍스트만 CRLF/LF 차이)
AS-IS (CRLF)    problems=25 withOptions=0  qtype={"essay":25}
LF-normalized   problems=25 withOptions=14 qtype={"choice":14,"essay":11}
```

`output/260714/공통영어1_모의25.md`에는 `①`이 **31회** 나오는데 선택지가 하나도 잡히지
않았고, 14개 선택형 문항이 전부 `essay`로 분류됐다. 웹 뷰어에서 **선택지 없는 빈 문항**으로
렌더링되고 선택형 자동채점(O/X)도 동작하지 않는다는 뜻이다. 통합과학·영어·국어·한국사·
통합사회 — 5지선다를 쓰는 **모든 과목**이 영향권이다.

### F3. `exportTsv`의 `flat()` TypeError — CB3 내보내기가 첫 행에서 즉사

`String(v)`는 문자열을 반환하고 문자열에는 `.join`이 없다.

```
$ node -e "flat(['DF1','DF2'])"
THROWS: String(...).join is not a function
$ 모의40 df 비어있지 않은 문항: 40 / 40
```

`df`가 비어있지 않은 문항이 **40/40**이므로 채점 1건만 있어도 🧾 버튼은 예외로 죽고
파일이 생성되지 않는다. §2.4의 "ready for `tools/import_grading.py`"는 **실행된 적 없는
주장**이다. 이 결함이 통과한 이유도 F1·F2와 같다 — 수용기준(파서 카운트 5개)이 CB3를
전혀 실행하지 않는다.

### F4. 보고서 §5.1 서술의 오해 소지 (사실은 참, 수정 불요)

"HEAD 3 E-slot tags → working tree 6"은 문자 그대로 참이지만, HEAD에도 함정 6건이 모두
있고 3건이 구표기 `DF4(E5)`일 뿐이다(신규 태그 3건 추가가 아니라 **표기 이관**).
`git diff` 확인: `-[SM2-18 · T3 · DF1·DF2·DF4(E5)]` → `+[… · DF4 · E5]`.
또한 `모의40.md` mtime은 **2026-08-24 11:24**로 260825 세션 이전 — Group P가 이 파일에
쓰지 않았다는 §5.1 주장은 사실이며, 수용기준이 **자기가 만들지 않은 입력**에 대해 실행됐다는
점(순환논증 아님)도 확인된다. 판정서 mtime 08-26 09:00 전후 < 카탈로그 반영 10:19 순서도 정합.

### F5. 재검증한 Group P 주장 — 지적 없음

§6 체크리스트 8항목 전부와 §1 RV-3·RV-4를 재실행해 **전부 성립**함을 확인했다:
`_index.md` 18행·`state: approved`, `status: submitted` 0건, HISTORY `approved(판정 반영)` ×6,
REV_LOG owner-apply 6행, `build_catalog_index.py --check`·`build_mastery.py --check` 둘 다 exit 0(131행),
답안표 40행·보조 1건@L446, CODE_REGISTRY L20 `T`/`W`→english.md·§2 L38 `T-01` vs `T2` 판별 규칙
(⇒ 판정 12의 QS-4 파기가 옳음), 카탈로그 스팟 grep 전건 존재, `git log -1` = `5e0b04d`.
보고서가 스스로 신고한 미결(영어 밴드 분리 실패·한국사 P6 번호 미피닝)도 카탈로그에
**실제로 미결로 기록**돼 있다 — 슬쩍 채워넣지 않았다.

</findings>

<questions>

1. `docs/DATA_STANDARD.md` §5.1의 "`mark_code` 외 컬럼에 한글·심볼 저장 금지" 문장은
   **같은 절의 예시 행과 모순**된다(예시 `note` 열에 `등호 누락`·`미착수`, 바로 다음 문장은
   `correct_answer`에 한글 모범답 요지 허용). 현행 `exportTsv`는 `student_answer`·
   `correct_answer`에 한글을 그대로 싣는다. **금지 문구를 `main_type`~`mark_code` 등
   코드 열 한정으로 좁히는 개정**이 맞는가? (정본 문서라 본 검토서에서 수정하지 않음)
2. `exportTsv`의 `fail_code` 열은 항상 `"-"`로 하드코딩돼 있다. §5.1 예시는 `E5`(함정코드)를
   싣고 파서는 이제 `traps[]`를 보유한다. 오답 시 **어느 함정에 빠졌는지는 교사 판정**이므로
   빈값이 맞다고 보아 수정하지 않았다 — 이 해석이 맞는가, 아니면 `traps[]` 후보를
   기본 채움해야 하는가?
3. 판정 07의 **수용기준 자체**가 CB1 파서 카운트만 검사해 CB2·CB3와 세트 메타·선택지를
   전혀 덮지 못했다. 향후 코드 판정에는 **변경세트별 실행 검증 1건 이상**을 수용기준에
   의무화할 것인가? (F1~F3 세 건 모두 같은 구멍으로 통과했다)

</questions>

<proposed_fixes>

사용자 직접 지시("확인하고 작업하고")로 수정 권한을 받아 **아래 2건은 이미 반영**했다.
원칙 8(검토·수정 분리)의 예외 근거는 **사용자 승인**이며, 그 사실을 여기 명시해 둔다.

- [x] **CB-F1/F2** `web/parser.js:169` — 행 분할을 CRLF 정규화로 교체.
      한 줄로 F1·F2를 동시에 해소하며 파이썬 `splitlines()` 동작과 일치시킨다.
      ```js
      // CRLF 정규화 — 파이썬 splitlines() 동작과 일치시킨다. \r가 남으면 m 플래그 없는
      // 행 단위 정규식(프론트매터 40행·LEADING_OPTION_RE 63행)의 (.*)$ 가 전부 실패한다.
      var rawLines = text.split(/\r?\n/);
      ```
- [x] **CB-F3** `web/app.js:281` — `flat()`을 배열 인지형으로 교체.
      §5.1 계약(`df=DF1,DF8` / 빈 값 `-`)을 그대로 만족한다.
      ```js
      // 배열은 콤마 결합, 빈 값은 "-" (§5.1 df=DF1,DF8 / aux_types=- 형식)
      function flat(v) { return Array.isArray(v) ? (v.length ? v.join(",") : "-") : (v || "-"); }
      ```
- [x] `python tools/build_web.py` 재실행 — 두 수정이 번들에 반영됨
      (`web/index.html` 121,887 bytes, 외부 참조 0).
- [x] **Q1 해소(260826, 사용자 판정 "한글 심볼 미사용 표준을 지켜라")** — `DATA_STANDARD`
      §0·§5.1·§6 개정: 원장 12열 **전부 ASCII 전용**(예외 열 없음), §5.1 열 규격표 신설,
      예시 행의 한글 제거, ASCII 미표현 서술형 답안은 `-`로 두고 원문은 `student/<학생ID>/`에서
      `(set_id,qnum)` 조인. `import_grading.py`에 비-ASCII 거부 검증 추가(죽은 문구 → 강제).
- [x] **Q2 해소(260826, 사용자 판정 "AI가 인지·작동 못 하면 명확히 하라")** — 판정 결과
      **인지 불가**였다(값 패턴만 §1.3에 있고 *누가 언제 채우는가*가 부재). `DATA_STANDARD`
      **§4.1-A 신설**: 의미·주체(교사)·시점·적용조건(wrong 행 한정)·소비처 명문화 +
      후보 제시 규칙(자동 채움 금지). 웹에 함정 선택 UI 추가로 **실제 채울 경로**를 만들었다.
- [x] **Q3 해소(260826, 사용자 판정 "라운드로 대체 가능한지 검토 후 아니면 의무화")** —
      검토 결과 **대체 불가**. `REV_GUIDE` §2-b에 코드 대상 기준이 아예 없어 3단계 전원이
      정적 검토만 했고(t2 자기기록 "Live node run NOT repeated"), 라운드 반복은 이 구멍을
      메우지 못한다. **§2-b D(System code) 신설 + §3 Round rule 4-a(수용기준 규격) 의무화.**

### 반영 후 검증 (전부 재실행 통과)

```
판정 07 수용기준 — 회귀 없음
  모의40 : 40 40 40 6 1 extra=0        ← 판정서 요구치와 동일
  선택지  : 0 {"essay":40}              ← 수학 서답형 100%라 정상

수정으로 복구된 값
  모의40 setId   : "m" → "SET-260822-math2-40"
  영어25 선택지  : 0 {"essay":25} → 14 {"choice":14,"essay":11}

JS ⇄ 파이썬 동작 동일 (판정 07 요구조건) — 두 파일 전 필드 일치
  모의40 : 40 40 40 6 1 / options 0  / setId 'SET-260822-math2-40'  (양쪽 동일)
  영어25 : 25 25 25 0 0 / options 14 / setId 'e'(해당 파일 프론트매터 없음, 양쪽 동일)

TSV 내보내기 — app.js exportTsv 본문을 DOM 스텁으로 실제 실행
  BOM=true · 전 행 12열 · df 콤마결합 · aux_types 빈값 "-"
  2026-08-26 | SET-260822-math2-40 | 16 | SM2-13 | SM2-11 | T4 | DF1,DF2,DF5,DF8 | blank
  4상태(correct/unsure/wrong/blank) 전부 왕복 확인

번들·원장 무결성
  web/index.html : Array.isArray 1건 · text.split(/\r?\n/) 1건 · 구코드 String(v).join 0건 · 외부참조 0
  build_catalog_index.py --check → exit 0 (131행)
  build_mastery.py --check       → exit 0 (131행)
  git log -1 → 5e0b04d (커밋 없음, 작업트리 유지)
```

</proposed_fixes>

<output_format>

| 질문 | 판정 | 근거 | 조치 |
|------|------|------|------|
| Q1 §5.1 한글 금지 문구 모순 | | | |
| Q2 fail_code 하드코딩 "-" | | | |
| Q3 코드 판정 수용기준 강화 | | | |

</output_format>

## history
- 260826(2차): 사용자 판정으로 미결 Q1~Q3 전부 해소. Q1=ASCII 전용 강제화(문서+검증기),
  Q2=fail_code §4.1-A 신설 및 웹 귀인 UI 신설(취약 축 제안 기능 복구 — 수정 전 `wrong_axes`
  영구 공집합이던 것이 `[E5] wrong in ['SM2-18'] … WK-01` 로 실제 출력됨), Q3=REV_GUIDE
  §2-b D + §3 rule 4-a 의무화. 신설 D 기준을 이번 변경 자체에 적용해 3층·미러 대조 검증.
- 260826: 신설. `260825_group_p_application_report.md` §6 체크리스트 8항목 + §1 RV-3·RV-4
  독립 재실행(전건 성립) 중 보고서가 검사하지 않은 층에서 결함 3건(F1 프론트매터 전량 실패·
  F2 선택지 전 과목 실패·F3 TSV 내보내기 TypeError) 발견. 사용자 지시로 F1~F3 수정·번들
  재빌드·재검증까지 완료, 정본 문서(DATA_STANDARD·REV_GUIDE) 개정 사안 3건은 미결로 이월.
