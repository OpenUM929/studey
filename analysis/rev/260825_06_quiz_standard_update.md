---
title: "QUIZ_STANDARD 개정 승인 요청 — 태그 표준형·과목 매핑·스키마(df·aux_types·세트 메타)·예시 ID의 DATA_STANDARD v1 정합화"
source: docs/QUIZ_STANDARD.md
source_location: "17행(§1 태그 표기) · 40~41·79행(예시 ID) · 52~54행(§1 과목 판별) · 60~85행(§2 중간 데이터 스키마)"
created: 2026-08-25
author: main-loop
status: approved
reviewer: 사용자
---

# 검토서 06 — QUIZ_STANDARD 개정 승인 요청 (DATA_STANDARD v1 신설로 뒤처진 기존 정본, 총 4건)

<document>

아래 인용은 **260825 작성 시점 원본 그대로**다. 검토 대상(QUIZ_STANDARD)과 개정 근거(DATA_STANDARD),
실물 근거(모의40)를 모두 발췌했으므로 이 문서 하나만으로 회신 가능하다.

### D1. docs/QUIZ_STANDARD.md §1 입력 규격 코드블록 (11~42행 전문)

```
# <제목>                       <- H1 제목 (과목·회차·문항수 등)
> <메타 설명>                  <- blockquote 메타 (생성 근거, 난이도 등)
> ...

## 선택형                      <- 객관식(5지선다) 섹션
**1.** <줄기> [유형ID·Tier]
<지문(생략 가능)>
① <보기1>
② <보기2>
③ <보기3>
④ <보기4>
⑤ <보기5>

---
**2.** ...
...

## 서답형                      <- 단답·서술형 섹션 (보기 없음)
**21.** [지문/조건] <줄기>
> <보기/조건 블록>

---
**22.** ...

---
# 정답 · 해설 · 유형           <- 답안표 (본문과 분리, 권위적 정답원)
| 문항 | 정답 | 유형ID·Tier | 해설(핵심) / 함정 |
|---|---|---|---|
| 1 | ② | T-01·T2 | <해설> |
| 21 | <모범답안> | W-01·T3 | <해설> |
```

### D2. docs/QUIZ_STANDARD.md §1 과목 판별 절 (52~54행 전문)

```
### 과목 판별
- 제목/헤더에 `영어` → `english`, `통합과학`/`과학` → `science`
- 그 외는 파일명/제목에서 추론, 못 하면 `unknown`
```

### D3. docs/QUIZ_STANDARD.md §2 중간 데이터 스키마 코드블록 전부 (58~85행)

```js
window.QUIZ_DATA = {
  "generatedAt": "2026-07-15T...",
  "sources": [                          // 처리된 md 파일 목록
    { "file": "output/260714/공통영어1_모의문제_25.md",
      "title": "공통영어1 모의 문제 — 25문항",
      "subject": "english" }
  ],
  "problems": [
    {
      "id": "260714#1",              // sourceKey + 번호
      "sourceKey": "260714",         // output 하위 폴더명(회차키)
      "subject": "english",
      "number": 1,
      "qtype": "choice",             // "choice" | "essay"
      "stem": "다음 글의 주제로 가장 적절한 것은?",
      "passage": "For most of human history ...",  // 지문/조건(없으면 "")
      "options": ["① ...","② ...","③ ...","④ ...","⑤ ..."],
      "answer": "②",                 // 객관식: 번호 / 서답형: 모범답안 텍스트
      "typeId": "T-01",
      "tier": "T2",
      "explanation": "멀티태스킹의 숨은 비용 ..."
    }
  ]
}
```

보강 사실: QUIZ_STANDARD.md 전체(140행)에 `df`, `aux`, `set_id`, `scope_confirmed`,
frontmatter라는 문자열은 **한 건도 없다**(grep 실시, 0매치).

### D4. docs/DATA_STANDARD.md 대조 조항 (개정 방향의 근거, v1 = 260825 신설)

§1.3 ID 레지스트리 중 유형ID·세트ID·DF 행(36~37·43행):

```
| 유형ID | `^[A-Z]{1,3}\d?-\d{2}$` | `SM2-14` | 접두어 등록제: `SM`=공통수학1, `SM2`=공통수학2. 타과목 카탈로그 정식화 시 여기에 등록 |
| 세트ID | `^SET-\d{6}-[a-z0-9]+-\d+$` | `SET-260822-math2-40` | YYMMDD-과목코드(§5.8)-문항수 |
| 난이도코드 DF | `^DF[1-9]$` | `DF5` | 정의: `analysis/catalog/난이도_루브릭.md` |
```

§5.1 ATTEMPT_LOG.tsv 헤더 + 샘플행(111~114행, 탭 구분 원본 그대로):

```
date	set_id	qnum	main_type	aux_types	tier	df	mark_code	student_answer	correct_answer	fail_code	note
2026-08-22	SET-260822-math2-40	13	SM2-14	-	T3	DF5	wrong	2	3	E5	등호 누락
2026-08-22	SET-260822-math2-40	16	SM2-13	SM2-11	T4	DF1,DF8	blank	-	18	-	미착수
```

§5.8 문제지 세트 프론트매터 + 과목 코드(176~197행):

```yaml
---
set_id: SET-260822-math2-40
student: S01
subject_code: math2
term: 2026-2
unit: I. 도형의 방정식
scope_confirmed: false     # false이면 뷰어·리포트에 ⚠️ 범위 미확정 배지 (원칙 7)
---
```

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
```

> "`scope_confirmed`가 없는 구(舊) 문제지는 false로 간주한다."(197행)

§6 강제 장치 중(201~203행): "- 웹 뷰어는 frontmatter `scope_confirmed:false`를 배지로 노출한다(원칙 7의 데이터 강제)."

§7 예외·미결 표(207~210행 전문):

```
| 항목 | 상태 |
|------|------|
| REV_LOG.md(MD 표) | REV_지침 §4가 한글 MD 형식을 정본으로 지정 — TSV 전환은 REV_지침 개정 승인과 함께만 검토 |
| docs/QUIZ_STANDARD.md 개정 | 태그 표준형·과목 매핑·스키마 필드(df·aux_types)·프론트매터 계약 — 검토서 `260825_02`로 승인 요청 중 |
```

> ▲ 정정 주석(260825 재번호) — 위 인용의 「검토서 `260825_02`」는 작성 당시 예고 번호다. 당일 순번 충돌
> (동일 세션군 카탈로그 검토서 02~05 선착 등록, 사용자 판정: 선착순 유지·후발 재번호)으로 본 검토서는
> **260825_06**으로 확정됐다. 원문은 원칙 3에 따라 그대로 보존한다.

Q4 관련 추가 인용 — DATA_STANDARD §0 2층 원칙(12~13행):

```
| **기계 소비 원장** | TSV(탭 구분, UTF-8 **BOM 필수**) | 컬럼명 = 영어 snake_case. enum 값 = ASCII 코드 | ATTEMPT_LOG · MASTERY · WEAK_LEDGER · index · HARVEST_LOG · SHARE_LOG |
| **사람 큐레이션 문서** | Markdown | 한국어 라벨·서술 자유 | 카탈로그 · 지침 · CLAUDE.md · 검토서(rev/) |
```

REV_지침 §4(80~84행 요지): REV_LOG 규격은 MD 표 `| 날짜 | 검토서 | 요약(한 줄) | 상태 | 반영처 |`이며
"- 행 삭제 금지. 상태 변화는 새 행으로 남긴다(추적 가능)." / "회차 폴더 단위로 구분 주석(`## output/YYMMDD`)을 넣어도 된다."

### D5. 실물 문제지 output/260822/공통수학2_도형의방정식_모의40.md (직접 확인분)

본문 태그는 전 행이 **공백형 + DF 목록**이다:

```
모의40 30행: [SM2-01 · T1 · DF1]
모의40 38행: [SM2-02 · T2 · DF1·DF5]
모의40 46행: [SM2-03 · T3 · DF1·DF2·DF4]
```

답안표 헤더(429행)와 첫 데이터 행 col1~3(431행), 보조유형 표기 행 col1~3(446행):

```
| 문항 | 정답 | 유형ID·Tier | 해설(핵심) / 함정 |
|---|---|---|---|
| 1 | **10** | SM2-01·T1 | …해설 이하 생략… |
| 16 | **(1)** x = 1, x − y + 5 = 0 / **(2)** 18 | SM2-13·T4 (보조 SM2-11) | …해설 이하 생략… |
```

즉 답안표 col3은 **대괄호 없는** `SM2-XX·TN` 무괴호 형식이고, 보조유형은 자연어 `(보조 SM2-11)`로만 기록됐다.
또한 모의40의 1행은 H1(`# 공통수학2 「도형의 방정식」 예상 문제 40제 …`)으로 바로 시작한다 — **frontmatter가 없다**(Q5 근거).

</document>

<context>
상산고(전북 전주, 자사고) 1학년 지필평가 출제 시스템이다. 웹 뷰어(web/)는 서버 없는 단일 HTML(file:// 드래그앤드롭)로
output/*.md를 직접 파싱하며, docs/QUIZ_STANDARD.md가 그 입력 규격의 기존 정본이다(본 검토서 작성 주체 아님).
260825 사용자 결정으로 docs/DATA_STANDARD.md v1(전역 데이터 표준 — enum 코드표·ID 레지스트리·frontmatter 계약)이
신설돼, QUIZ_STANDARD가 정의하는 계약이 새 표준층과 실물 문제지 양쪽에서 파생됐다.
같은 날 작성된 검토서 260825_01에서 파서 결함 9건(TAG_RE 불일치 F1~F3, DF 파싱 부재 F4, 보조유형 미수용 F5,
과목 매핑 누락 F6 등)이 이미 보고돼 있으며, 그 교정과 QUIZ_STANDARD 개정은 같은 표준형을 향한다.
지배 규범: CLAUDE.md 원칙 7(범위 미확정)·원칙 8(검토·수정 분리 — 본 검토서는 QUIZ_STANDARD를 절대 수정하지 않는다).
</context>

<findings>

등급 기준(260825_01 준용): **치명**=기능 전멸 / **주요**=기능 결손·규범 구조 충돌 / **경미**=데이터 정합성 미비.
검증 방법: 두 정본 파일의 직접 행단위 대조 + PowerShell regex 검산(ID 레지스트리 패턴) + grep 문자열 부재 확인.
아래 4건은 모두 파일 대조로 확정한 사실이며 짐작을 포함하지 않는다.

#### QS-1 【주요】 §1 태그 표기가 밀착형 `[유형ID·Tier]`만 정의 — 공백·DF·보조유형을 수용하지 못한다

QUIZ_STANDARD 17행(D1)은 본문 태그를 `[유형ID·Tier]` 한 형태로만 정의한다: (a) `·` 앞뒤 공백 없음,
(b) DF 목록 슬롯 없음, (c) 보조유형 슬롯 없음. 반면 실물 문제지는 전 문항이 공백형+DF 목록이다(모의40 30·38·46행, D5).
답안표 셀은 대괄호 없는 `SM2-01·T1`(무괴호)이고 보조유형은 자연어 `(보조 SM2-11)`로만 나온다(446행).
DATA_STANDARD §1.3은 DF를 enum 코드(`^DF[1-9]$`)로, §5.1 ATTEMPT_LOG는 `df`·`aux_types`를 원장 컬럼으로
각각 정식 계약하고 있는데(D4), QUIZ_STANDARD에는 그 어디에도 `df`·`aux` 문자열이 없다(grep 0매치).
검토서 260825_01의 F1(TAG_RE 공백 미허용→미매치)·F4(DF 파싱 경로 부재)·F5(보조유형 수용 불가)는
"파서가 이 규격을 충실히 따라 만들었기 때문에 실패했다"는 점을 실증했으므로, 본 결함은 그 교정의 규격 측 근원이다.

#### QS-2 【주요】 §1 과목 판별 목록이 불완전 — 통합사회·한국사 누락, math1/math2 구분 불가

QUIZ_STANDARD 52~54행(D2)의 명시 매핑은 `영어 → english`, `통합과학/과학 → science`뿐이고
나머지는 "파일명/제목에서 추론, 못 하면 unknown"으로 위임한다. DATA_STANDARD §5.8 SUBJECT_CODES는
7종(math1/math2/science/social/history/english/korean)을 정의해 통합사회(social)·한국사(history)와
공통수학1(math1)/공통수학2(math2)의 구분을 이미 계약했다(D4). 파서 구현(parser.js SUBJECT_MAP, 260825_01 D1)이
`수학 → math`·`국어 → korean`을 임의로 추가해 오히려 규격과 구현이 양방향으로 어긋나 있다.
파급: `/수학/` 하나로는 math1·math2를 못 가르므로 세트ID 패턴 `SET-YYMMDD-과목코드-N`(§1.3, 과목코드=§5.8 참조)의
생성 자체가 불안정해지고, 통합사회·한국사 문제지는 전부 `unknown`으로 떨어진다.

#### QS-3 【주요】 §2 중간 데이터 스키마에 df·aux_types 필드가 없고, 세트 단위 메타 계약이 없다

스키마(D3)의 문항 객체 필드는 `id, sourceKey, subject, number, qtype, stem, passage, options, answer,
typeId, tier, explanation` 12개뿐이다 — **DF 코드와 보조유형을 담을 필드가 없어**, 태그에 기록된
DF 정보는 규격상 저장소 자체가 없다(QS-1과 표리일치). 또한 `sources[]`는 file/title/subject만으로
세트 단위 메타(set_id·subject_code·unit·scope_confirmed) 계약이 없다. 그런데 DATA_STANDARD은
(i) §5.1 ATTEMPT_LOG가 매 시도마다 `set_id`·`aux_types`·`tier`·`df` 컬럼을 요구하고,
(ii) §5.8이 frontmatter 계약을, (iii) §6 강제 장치가 "웹 뷰어는 frontmatter scope_confirmed:false를
배지로 노출"을 각각 못박았다(D4). QUIZ_STANDARD §1의 입력 블록 순서는 H1에서 시작해 frontmatter 단계 자체가
없으므로(12행), 이 규격만 읽고 만든 변환기·뷰어는 DATA_STANDARD의 강제 장치를 구현할 방법이 없다.
양 정본의 계약이 연결되지 않는 것이 본 결함의 핵심이다.

#### QS-4 【경미】 예시 답안표·스키마의 유형ID가 `T-01`/`W-01` — ID 레지스트리 등록제와 불일치

QUIZ_STANDARD 40~41행의 예시 행 `T-01·T2`, `W-01·T3`과 79행의 `"typeId": "T-01"`은 가공 접두어다.
regex 검산 결과 `[regex]::IsMatch('T-01','^[A-Z]{1,3}\d?-\d{2}$')` = True, 동일 조건 `'W-01'` = True —
즉 **§1.3 패턴 자체는 통과하므로 문제는 패턴이 아니라 등록제다**: 현재 등록된 접두어는 SM(공통수학1)·SM2(공통수학2)뿐이고
카탈로그 정본도 그 체계뿐이며, T-/W- 뒤에는 어떤 카탈로그도 없다(DATA_STANDARD §1.3 "타과목 카탈로그 정식화 시
여기에 등록"). 예시는 후속 생성기(md2quiz.py, 향후 item-writer)가 그대로 모방하는 학습 표본이므로,
비등록 접두어 양산과 Tier 코드(T1~T4)와의 시각적 혼동(T-01 vs T2)을 막으려면 실재 ID(SM/SM2 체계)로 교체가 필요하다.

</findings>

<questions>

- Q4 【열림 — 판정 요청】 analysis/REV_LOG(MD 표)의 TSV 전환 여부.
  현황: REV_지침 §4가 한글 MD 표를 정본으로 지정했고, DATA_STANDARD §7에 "TSV 전환은 REV_지침 개정 승인과
  함께만 검토"로 예외 등록돼 있다(D4). DATA_STANDARD §0은 검토서(rev/)류를 사람 큐레이션 문서(Markdown,
  한글 서술 자유) 층에 둔다.
  - 안 a) 현행 유지 — REV_LOG는 사람이 읽는 추적 문서 성격이 강하고(한글 요약 열), §0 사람 문서 층 해석과
    양립한다. §7 예외 등록 상태로 즉시 조치 불요.
  - 안 b) TSV 전환 — 기계 집계(미결 검토서 목록 자동 추출 등)가 가능해지지만, REV_지침 §4 개정이 선행돼야 하고
    (원칙 8 — 본 검토서 범위 밖 별도 건), append-only 행의 마이그레이션 방법(전량 이관 vs MD 아카이브 보존 후
    신규부터 TSV)과 `## output/YYMMDD` 구분 주석의 재현 방법(폴더 컬럼 신설 등)을 함께 정해야 한다.
  판단 포인트: REV_LOG를 도구가 읽어 집계할 필요가 있는가 — 현재까지는 사람 조회뿐이면 전환 이익이 작다.

- Q5 【열림 — 판정 요청】 구(舊) 문제지(frontmatter 무소유)의 `scope_confirmed` 기본값 처리 적절성.
  DATA_STANDARD §5.8은 "없는 구(舊) 문제지는 false로 간주한다"(197행)로 정했으며(D4), 실측상 모의40은
  frontmatter가 없다(D5). 검산: false 기본값이면 ⚠️ 범위 미확정 배지가 노출되는데, 모의40은 스스로 머리말에서
  ⚠️범위 미확정을 선언하고 있어(모의40 4행) 배지 내용이 파일의 실제 상태와 **일치**한다. 반대안(true 간주·내용 추론)은
  미확인 범위를 조용히 확정으로 통과시켜 원칙 7(확인 전까지 경고 표시)을 우회할 수 있다. false 기본값은
  안전측(fail-safe) 방향이라 유지가 타당하다고 판단하나, 최종 판정을 요청한다.

</questions>

<proposed_fixes>

아래 수정은 **docs/QUIZ_STANDARD.md 원본에 대한 것**이며, 원칙 8에 따라 본 검토서 작성 주체는 수정하지 않는다.
승인 시 item-writer 또는 사용자가 반영한다.

- [ ] QUIZ_STANDARD §1: 태그 표준형 섹션 신설 — 공백 허용 `[주유형ID · Tier · DF목록 (+보조)]` 표준형 정의,
      무괴호 답안표 셀(`SM2-XX·TN (+보조 SM2-YY)`) 병기, 17행 밀착형 예시 교체 (QS-1)
- [ ] QUIZ_STANDARD §1 과목 판별: DATA_STANDARD §5.8 SUBJECT_CODES 참조로 교체 — 통합사회(social)·한국사(history)
      추가, math1/math2 구분 규칙 명시, `unknown` 잔존 조건 정의 (QS-2)
- [ ] QUIZ_STANDARD §2: 스키마에 df·aux_types 필드 추가 + 세트 메타 계약 절 신설 — frontmatter
      (set_id/subject_code/unit/scope_confirmed, DATA_STANDARD §5.8 참조)를 §1 입력 블록 순서에 편입하고
      sources[]에 반영 (QS-3)
- [ ] QUIZ_STANDARD 예시 답안표·스키마의 유형ID를 SM/SM2 체계 실재 ID로 교체 — `T-01`/`W-01` 폐기,
      ID 레지스트리(§1.3) 정합 (QS-4)
- [ ] (선택, Q4 연동 — **본 검토서 범위 밖 별도 건**) REV_지침 §4 및 analysis/REV_LOG의 TSV 전환.
      REV_지침 개정을 수반하므로 본 검토서에서는 기술만 하고 별도 건으로 진행함

</proposed_fixes>

<output_format>

회신은 아래 표 한 개로 못박는다.

| 질문 | 판정 | 근거 | 제안 |
|------|------|------|------|
| (예: Q4) | 정당/기각/보류 | … | … |

Q4·Q5의 판정과 `<proposed_fixes>` 체크박스 5건(마지막 1건은 범위 밖 별도 건)의 승인 여부만 회신하면 된다.
findings(QS-1~4)에 대한 이견이 있으면 같은 표에 추가 행으로 적어라.

</output_format>

## 이력
- 260825 작성 — 기존 정본 docs/QUIZ_STANDARD.md(타 주체 작성)를 DATA_STANDARD v1(260825 신설) 및
  실물 문제지(output/260822 모의40)와 행단위 대조해 규격 결함 4건(QS-1~3 주요, QS-4 경미)을 패키징.
  원칙 8에 따라 원본 미수정, 개정 체크박스 5건 승인 요청 + 열린 판정 요청 2건(Q4·Q5). 상태: 대기.
- 260825 재번호 — 당일 순번 충돌(동일 세션군 카탈로그 검토서 02~05 선등록, 사용자 판정: 선착순 유지·후발
  재번호)으로 `260825_02_quiz_standard_update.md` → **`260825_06_quiz_standard_update.md`** 확정. 같은 날
  확립된 [`문서위치_표준.md`](../../analysis/문서위치_표준.md) §2(검토서 이원화)에 따라 `output/260825/rev/` →
  `analysis/rev/` 로 이동. 발견·제안 내용은 무변경 — H1 번호, 위 ▲정정 주석, 본 행만 추가. 상태: 대기.
