# 문제 데이터 표준안 (QUIZ_STANDARD)

> `output/`에 있는 마크다운 문제지를 웹 뷰어(`web/`)가 읽을 수 있는
> 중간 데이터(JSON)로 정제하기 위한 **입력 형식 규격**과 **데이터 스키마**를 정의한다.
> 기존 Claude 생성 흐름(본문 + 말미 답안표)을 그대로 표준 입력으로 삼는다.

## 1. 입력 MD 규격 (표준 입력)

파일은 다음 순서의 블록으로 구성된다. 세트 수준 메타는 YAML frontmatter로
시작할 수 있으며(아래 "세트 프론트매터"), 파서는 `subject_code` 등의 값을
본문 추론보다 **우선**한다(ruling 07 CB1).

```
---
set_id: SET-260822-math2-40     # 없으면 파일명(확장자 제외)이 set_id 가 된다
subject_code: math2             # DATA_STANDARD §5.8 의 7코드 — 본문 추론보다 우선
unit: I. 도형의 방정식
scope_confirmed: false          # 원칙 7 — 부재 시 false 로 해석(fail-safe)
intended_use: practice|exam
---

# <제목>                       <- H1 제목 (과목·회차·문항수 등)
> <메타 설명>                  <- blockquote 메타 (생성 근거, 난이도 등)
> ...

## 선택형                      <- 객관식(5지선다) 섹션
**1.** <줄기> [유형ID · Tier · DF목록 · 함정E코드]
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

### 유형 태그 표준형 (ruling 07 A1 / ruling 12 CB1 — amended)

본문 태그는 **네 슬롯**을 가질 수 있다:

```
[ID · Tier · DF1·DF2·… · E1~E9]        예) [SM2-18 · T3 · DF1·DF2·DF4 · E5]
[ID · Tier · DF… (+보조ID)]            보조 예) [SM2-13 · T4 · DF1·DF2·DF5·DF8 (+SM2-11)]
[ID · Tier]                            최소형 (DF·함정 슬롯 생략 가능)
```

- 슬롯 구분자는 중점 `·`, 슬롯 순서는 주유형 → Tier → DF목록 → 함정 E코드.
- 함정 코드 `E1~E9`는 `TYPE_MASTER.md`의 등록 함정 계열이다.
- 답안표 셀은 괄호 없이 `SM2-13·T4 (보조 SM2-11)` 형태를 허용한다.
- **포용 규칙**: 파서가 알지 못하는 `·` 구분 토큰은 버리지 않고 `tagExtra`에
  그대로 보존한다(원칙 3 — 정보 삭제 금지). 검증 RE는 ruling 07 판정서 참조.

### 합칠 키
- 본문의 `**N.**` 번호 ↔ 답안표의 `| N |` 행
- 두 곳의 `N`(문항 번호)으로 본문·정답·해설·유형ID를 병합한다.

### 문제 유형 판별
- 블록 내에 `①`~`⑤` 보기 줄이 있으면 `choice`(객관식)
- 없으면 `essay`(서답형/단답형)

### 섹션 상태 (ruling 07 CB2)
- 섹션 전환은 제목 키워드(`선택형`/`서답형`·`서술형`·`단답형`/`정답`·`해설`)로
  판별하며, 단원 헤더(`## I-2 …`) 같은 다른 헤딩은 질문 구역을 리셋하지 않는다.
  후행 보조 섹션(채점 기준·요약)도 상태를 바꾸지 않는다.

### 과목 판별
- frontmatter `subject_code` 최우선(DATA_STANDARD §5.8의 7코드 —
  math1·math2·science·social·history·english·korean).
- 없으면 제목/헤더에서 위 7코드로 추론(예: `공통수학2`/`도형의 방정식` → math2),
  못 하면 `unknown`. 레거시 `math` 값은 사용하지 않는다.

## 2. 중간 데이터 스키마 (web/data.js)

변환기는 아래 구조의 JS 변수로 출력한다(`window.QUIZ_DATA`).

```js
window.QUIZ_DATA = {
  "generatedAt": "2026-07-15T...",
  "sources": [                          // 처리된 md 파일 목록
    { "file": "output/260714/공통영어1_모의문제_25.md",
      "title": "공통영어1 모의 문제 — 25문항",
      "subject": "english",
      "scopeConfirmed": false,          // frontmatter 부재/false → false (원칙 7)
      "setId": "SET-..." }
  ],
  "problems": [
    {
      "id": "SET-...#1",             // setId + 번호
      "sourceKey": "260714",         // output 하위 폴더명(회차키)
      "setId": "SET-...",            // frontmatter set_id 또는 sourceKey
      "scopeConfirmed": false,
      "subject": "english",
      "number": 1,
      "qtype": "choice",             // "choice" | "essay"
      "stem": "다음 글의 주제로 가장 적절한 것은?",
      "passage": "For most of human history ...",  // 지문/조건(없으면 "")
      "options": ["① ...","② ...","③ ...","④ ...","⑤ ..."],
      "answer": "②",                 // 객관식: 번호 / 서답형: 모범답안 텍스트
      "typeId": "T-01",
      "tier": "T2",
      "df": ["DF1","DF3"],           // DF 슬롯 (없으면 [])
      "traps": [],                   // 함정 E코드 슬롯 (없으면 [])
      "auxTypes": [],                // 보조 유형 (+ID / (보조 ID)) (없으면 [])
      "tagExtra": [],                // 미분류 잔존 토큰 — 절대 삭제하지 않는다
      "explanation": "멀티태스킹의 숨은 비용 ..."
    }
  ]
}
```

> 예시의 `T-01`·`W-01` 등 ID는 `analysis/catalog/CODE_REGISTRY.md` §1에
> 등록된 접두어다(영어 T/W 계열). 난이도 코드 `T2`와의 구분법은 같은 문서 §2.

## 3. 변환·로드 흐름

### A. 브라우저에서 직접 (권장, Python 불필요)
1. `web/index.html` 더블클릭으로 열기
2. `output/<회차>/*.md` 를 **드래그앤드롭** 하거나 `📂 MD 불러오기` 버튼으로 선택
   → `web/parser.js` 가 md를 브라우저 안에서 파싱 → 바로 1페이지/1문제 렌더
3. 불러온 md는 `localStorage`에 자동 저장되어, 다음에 열 때 **자동 복원**됨
   (별도 변환 단계 없이 "파일 올리고 바로 풀기")

### B. 사전 변환 (배치/정적 배포용, 선택)
- `python tools/md2quiz.py` → `web/data.js` 생성. 이 경우 A의 드래그앱 없이
  `data.js` 샘플이 기본 로드됨(저장된 md가 있으면 그쪽 우선).

> `data.js`로 임베드하거나 `parser.js`로 직접 파싱하는 이유: `file://`에서
> `fetch(json)`이 CORS로 차단되는 브라우저 환경에서도 더블클릭만으로 동작하게 하기 위함.

## 4. 뷰어 기능 범위

- 1페이지 = 1문제 (풀스크린 카드)
- 이전/다음 + ←/→ 키 + 진행률 바
- 클릭 시 정답 + 해설 + 유형ID·Tier 공개
- 셔플 / 과목·유형 필터
- 오답노트·진도를 `localStorage`에 저장(이어풀기)
- **4상태 채점**(ruling 07 CB3): O(맞음)/△(애매)/X(틀림)//(백지) —
  코드는 DATA_STANDARD §4.1 enum(correct/unsure/wrong/blank)
- **🧾 채점 TSV 내보내기**: ATTEMPT_LOG §5.1과 동일 12열, UTF-8 BOM,
  `mark_code`는 enum 단어 — `tools/import_grading.py`로 직행 검증 가능

## 5. 객관식 자동 판정 / 서답형 입력·diff

- **객관식**: 보기를 고르면 정답(초록)·오답(빨강) 즉시 표시되고,
  맞음/틀림이 **자동으로** 오답노트에 기록된다(별도 버튼 불필요).
- **서답형**: 답을 직접 입력할 `<textarea>` 가 있음(입력 내용 `localStorage` 저장).
  `비교 / 정답 보기` 클릭 시 **모범답안을 기준**으로 렌더되며,
  사용자 답과 **다른 토큰을 빨강**으로 하이라이트한다.
  - diff 기준: 구두점(`. ,` 등)·공백·대소문자는 정답 판단에서 **무시**(LCS 토큰 정렬).
  - 한글은 음절 단위, 영어는 단어 단위 토큰.
  - ⚠️ diff는 "모범 표현과 얼마나 달리 썼나"를 보여주는 **참고용**(의미 채점 아님,
    유의어·어순 차이도 빨강으로 잡힘). 최종 판단은 사용자가 네 채점 버튼
    (`맞았어요 / 애매해요 / 틀렸어요 / 백지`)으로 한다.

## 6. 단일 HTML 내보내기(공유)

`📤 공유 HTML` 버튼으로 **현재 문제 세트를 단일 `.html` 파일로 다운로드**한다.
받는 사람은 그 파일을 더블클릭만으로 푼다(서버·md·Python 불필요).

- 내부 동작: 현재 `DATA`를 JSON으로 인라인(`<` → `\u003c` 이스케이프)하고
  `window.QUIZ_EMBEDDED = true` 플래그와 함께 `<head>` 에 주입.
  기존 데이터 태그는 제거하므로 외부 의존성 0개의 자급형 파일이 된다.
- 받는 사람 브라우저에서는 `QUZ_EMBEDDED` 감지 시 인라인 데이터를 그대로 사용하며,
  본인의 맞음/틀림 체크는 **자신의 `localStorage` 에만** 저장(공유본에 영향 없음).
- 단, 공유 파일에서도 `📂 MD 불러오기`로 다른 md를 올려 교체할 수는 있다.

### 빌드 워크플로우(개발자)
- 소스: `web/index.template.html`(구조) + `web/{style.css, parser.js, app.js, data.js}`
- `python tools/build_web.py` → `web/index.html` 에 인라인화(외부 참조 0).
- 문제 갱신: `python tools/md2quiz.py` → `python tools/build_web.py`.
- `index.html` 이 자체가 자급형이라 그대로 열거나 공유 가능.

