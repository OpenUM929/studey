---
title: "태그 파이프라인 불일치(TAG_RE↔본문 태그·답안표 셀) 및 웹 뷰어 채점 상태·영속화 결함"
source: web/parser.js
source_location: "parser.js:7-18,91-98,143-148 / app.js:4-10,201-208,256-282,327-333 / 모의40 본문태그·답안표16번"
created: 2026-08-25
author: main-loop
status: approved
reviewer: 사용자
---

# 검토서 01 — 태그 배관 불일치와 웹 뷰어 상태·영속화 결함 (위탁 8건 + 재현 중 신규 1건)

<document>

아래 인용은 **260825 작성 시점의 원본 그대로**다(수정 전 스냅숏이 아니라 현행 원본).
승인된 수정이 반영되면 이후 문서와 달라지므로, 그 시점에는 새 검토서가 새 인용을 가져야 한다.

### D1. web/parser.js 7~18행 전문 (TAG_RE · SUBJECT_MAP)

```js
// web/parser.js 7~18행 — 원본 그대로
  var OPTION_RE = /^\s*([①②③④⑤])\s*(.*)$/m;
  var PROB_RE = /^\s*\*\*(\d+)\.\*\*\s*(.*)$/m;
  var TAG_RE = /\[([A-Za-z0-9\-]+)·?(T\d)\s*\]/;
  var H1_RE = /^\s*#\s+(.*)$/m;
  var ANSWER_H_RE = /^\s*#\s*정답/m;

  var SUBJECT_MAP = [
    [/통합과학|과학/, "science"],
    [/영어/, "english"],
    [/수학/, "math"],
    [/국어/, "korean"]
  ];
```

파서가 최종 만드는 문항 객체 필드(parser.js:149-162)는
`id, sourceKey, subject, number, qtype, stem, passage, options, answer, typeId, tier, explanation` 이다.
**DF 코드를 담는 필드는 존재하지 않고**, 파일 전체(181행 전수 판독)에 `DF` 문자열 자체가 없다.

### D2. web/app.js 발췌

```js
// app.js 4~10행 — localStorage 키 (유일한 영속 계층)
  var LS = {
    status: "quiz_status_v1",
    choice: "quiz_choice_v1",
    revealed: "quiz_revealed_v1",
    md: "quiz_md_v1",
    answer: "quiz_answer_v1"
  };

// app.js 114행 — 유형 필터 드롭다운은 typeId에서만 생성
      if (p.typeId) types[p.typeId] = true;

// app.js 201~208행 — 객관식 자동채점 (2값뿐)
        var ch = choice[p.id];
        if (ch) {
          status[p.id] = (ch === cNum) ? "correct" : "wrong";
          save(LS.status, status);
        }
        if (!ch) { el.autoStatus.textContent = "보기를 선택하면 자동 채점됩니다"; ... }
        else if (ch === cNum) { el.autoStatus.textContent = "✅ 정답"; ... }
        else { el.autoStatus.textContent = "❌ 오답 (정답 " + cNum + ")"; ... }

// app.js 256~263행 — 수동 mark() (val은 호출처에서 "correct"/"wrong"만 넘어옴)
  function mark(val) {
    var p = state.list[state.idx];
    if (!p) return;
    if (status[p.id] === val) { delete status[p.id]; }
    else { status[p.id] = val; }
    save(LS.status, status);
    render();
  }

// app.js 266~282행(요지) — 단일 HTML 내보내기: DATA(문제지)만 직렬화, 결과(status/choice/revealed/answers) 미포함
  function exportStandalone() {
    ...
    var json = JSON.stringify(DATA).replace(/</g, "\\u003c");   // ← 268행. 학생 데이터 미포함
    ...
  }

// app.js 327~333행 — 초기화 시 학생 데이터 4스토어 일괄 소멸
  el.resetBtn.addEventListener("click", function () {
    if (confirm("맞음/틀림 기록과 공개 상태를 초기화할까요?")) {
      status = {}; choice = {}; revealed = {}; answers = {};
      save(LS.status, status); save(LS.choice, choice); save(LS.revealed, revealed); save(LS.answer, answers);
      render();
    }
  });
```

버튼은 2개뿐이다 (app.js:336-337):
`el.correctBtn → mark("correct")`, `el.wrongMarkBtn → mark("wrong")`.

### D3. output/260822/공통수학2_도형의방정식_모의40.md 발췌

본문 태그는 전 문항에서 **별도 줄**(스텝 줄이 아님)에, `·` 앞뒤에 **공백이 있는 형식**으로 기록돼 있다:

```
모의40 30행:  [SM2-01 · T1 · DF1]
모의40 46행:  [SM2-03 · T3 · DF1·DF2·DF4]
모의40 165행(16번 본문 태그): [SM2-13 · T4 · DF1·DF2·DF5·DF8]
```

답안표 헤더행(429행):

```
| 문항 | 정답 | 유형ID·Tier | 해설(핵심) / 함정 |
```

> 주: 위탁 발췌 지침에는 헤더가 「해설(검증) / 판정」으로 적혀 있었으나, 원본 429행은 위와 같다.
> 인용은 원본을 따른다.

16번 행 col1~3(446행, 해설부 생략):

```
| 16 | **(1)** x = 1, x − y + 5 = 0 / **(2)** 18 | SM2-13·T4 (보조 SM2-11) | …해설 이하 생략… |
```

즉 답안표 셀(col3)은 **대괄호 없는** `SM2-13·T4` 형식이며, 보조유형은 자연어 `(보조 SM2-11)`로만 기록됐다.

</document>

<context>
상산고(전북 전주, 자사고) 1학년 지필평가 출제 시스템이다. 유형 카탈로그(SM2-01~33,
analysis/catalog/공통수학2.md)가 정본이고, 웹 뷰어(web/)는 서버 없는 단일 HTML(file:// 드래그&드롭)로
문제집 md를 브라우저에서 직접 파싱한다. 채점 표기는 사용자 확정 4상태 O/△/X/(빗금)를 쓴다
(X=오답, /=백지·미완주 — 분리 추적용). 지배 규범은 원칙 3(append-only)·7(범위 미확정)·8(검토·수정 분리)이다.
이번 검토는 문제집 내용이 아니라 카탈로그↔문제지↔웹을 잇는 태그 배관과 학생 데이터 영속화 결함에 관한 것이다.
</context>

<findings>

등급 기준: **치명**=기능 전멸·배관 단절 / **주요**=기능 결손·규범 구조 충돌 / **경미**=데이터 정합성 미비.

검증 방법 요약: F1~F3은 PowerShell .NET regex(`[regex]::IsMatch`) 독립 재현 + node v24.14.1로
parser.js 실실행(실제 모의40 파일 입력). 콘솔이 U+00B7(·)을 화면에 `?`로 표시했으나
선행 codepoint 검증(`[int][char]'·'` = **183**)으로 패턴·입력 문자열 모두 정상 수송됨을 확인했으므로
True/False 판정은 유효하다.

#### F1 【치명】 TAG_RE가 본문 태그(공백 포함형)를 못 읽는다 — 위탁 결함

parser.js:9 `var TAG_RE = /\[([A-Za-z0-9\-]+)·?(T\d)\s*\]/;` 는
(a) ID와 `·` 사이 공백을 허용하지 않고(ID 문자클래스 바로 뒤 `·?`),
(b) Tier 뒤 `\s*\]` 밖에 못 건너뛰어 후미 `· DFn` 그룹도 허용하지 않는다. 두 원인은 **각각 독립적으로** 매치를 죽인다.
모의40의 본문 태그는 전 문항이 공백+후미 DF 그룹 형식이다(tagLines=40 계수, D3 참조).

```
[재현 — .NET regex]
IsMatch('[SM2-01 · T1 · DF1]', '\[([A-Za-z0-9\-]+)·?(T\d)\s*\]') = False   ← F1 (미션 지정 명령 그대로)
IsMatch('[SM2-01·T1]',         '\[([A-Za-z0-9\-]+)·?(T\d)\s*\]') = True    ← 대조군: RE 자체는 유효, 조건만 과밀
IsMatch('[SM2-01·T1 · DF1]',   '\[([A-Za-z0-9\-]+)·?(T\d)\s*\]') = False   ← 후미 그룹(원인 b)만으로도 실패
```

교정 후보 RE(공백 허용 + DF 목록 캡처)로는 양쪽 표본이 모두 잡힌다:

```
\[([A-Za-z0-9\-]+)\s*·\s*(T\d)(?:\s*·\s*(DF\d+(?:·DF\d+)*))?\s*\]
'[SM2-01 · T1 · DF1]'          → True, id=SM2-01 tier=T1 df=DF1
'[SM2-03 · T3 · DF1·DF2·DF4]'  → True, id=SM2-03 tier=T3 df=DF1·DF2·DF4
```

#### F2 【치명】 같은 TAG_RE가 답안표 셀(무괴호)도 못 읽는다 — 위탁 결함

TAG_RE는 리터럴 `[`를 요구하는데 답안표 col3은 `SM2-13·T4`처럼 괄호가 없다(D3, 446행 표본).
parseAnswerTable(parser.js:91-92 `var tm = TAG_RE.exec(typeTier);`)이므로 표 행 40건 전부 미매치.

```
[재현 — .NET regex]
IsMatch('SM2-13·T4', '\[([A-Za-z0-9\-]+)·?(T\d)\s*\]') = False   ← F2 (미션 지정 명령과 동일 조건)
무괴호 셀 대응 교정 후보: ^\s*([A-Za-z0-9\-]+)\s*·\s*(T\d)
  'SM2-13·T4 (보조 SM2-11)' → id=SM2-13 tier=T4 (앞 2그룹만 캡처)
```

#### F3 【치명】 두 경로 전멸 → typeId·tier 전부 공란, 유형 필터 기능 상실 — 위탁 결함

답안표 경로(F2)가 비면 convertText의 폴백(parser.js:145-148, `TAG_RE.exec(stem)`)이 실행되는데,
(i) 코퍼스의 태그는 전부 **별도 줄**이라 스텝 문자열에 아예 없고(모의40·part2에서 tagOnStemLine=0 계수),
(ii) 설령 스텝 줄에 있어도 공백형은 F1로 미매치다. 합성 대조로 격리 확인:

```
[재현 — node v24.14.1, parser.js 실실행]
A(태그 별도 줄·공백형):   problems=1 typeId=[] tier=[]
B(무공백 태그가 스텝 줄 끝): problems=1 typeId=[SM2-01] tier=[T1]  ← RE가 정상이면 폴백은 작동함
                          → 즉 폴백 로직의 결함이 아니라 "코퍼스 형식≠RE" 불일치가 원인
```

typeId가 전부 공란이면 app.js:114(`if (p.typeId) types[p.typeId] = true;`)에 걸리는 항목이 없어
유형 필터 드롭다운은 "유형: 전체" 1개만 남는다. ※ 현재 버전에서는 F9 때문에 문항 자체가 0개라
이 상태가 관측되지 않으며(아래 F9), F9 선행 수정 후 표면화되는 2차 결함이다.

#### F4 【주요】 DF 코드는 파싱 경로 자체가 없다 — 위탁 결함

본문 태그는 `DF1·DF5` 등 DF 코드를 담고 있으나(D3), parser.js에는 DF를 다루는 정규식·필드가 없다
(D1 말단 근거). DF의 정의는 카탈로그 정본 `analysis/catalog/난이도_루브릭.md` 28~36행(D F1~DF9 표)에 존재하므로,
태그에 기록된 난이도 메타데이터가 뷰어 도달 전에 폐기된다. F1의 교정 후보 RE가 df 그룹을 캡처함을 이미 보였다.

#### F5 【경미】 보조유형은 16번 단 1건, 본문 태그에는 없고 답안표 자연어로만 존재 — 위탁 결함

모의40 전체에서 '보조' 등장은 1회(446행, 16번 col3 `(보조 SM2-11)`), 본문 태그(165행)에는 SM2-11이 없다.
분할본 `_part2_직선.md`도 동일(보조 1회, 106행).

```
[계수 — PowerShell regex Matches]
모의40:       tagLines=40  tableRows=40  auxCount=1  auxLines=[446]  tagOnStemLine=0
_part2_직선:  tagLines=10  tableRows=10  auxCount=1  auxLines=[106]
```

#### F6 【주요】 SUBJECT_MAP에 통합사회·한국사 없음, 공통수학1/2 구분 불가 — 위탁 결함

parser.js:13-18(D1)의 매핑은 통합과학·영어·수학·국어뿐이다.
detectSubject(parser.js:20-25)는 미매치 시 `"unknown"`을 반환하고(app.js:13에서 라벨 "기타"),
`/수학/` 하나로 공통수학1과 공통수학2를 구분하지 못해 둘 다 `"math"`가 된다.

#### F7 【주요】 채점 상태가 correct/wrong 2종뿐 — △(불확신)/​/(백지) 표현 불가 — 위탁 결함

자동채점은 2값 할당(app.js:203), 수동 mark()는 호출처가 "correct"/"wrong"만 넘기고(app.js:336-337),
오답노트 필터도 `status[p.id] !== "wrong"` 2값 전제다(app.js:131). 사용자 확정 4상태 O/△/X// 중
△와 /(빗금)은 저장·표시·집계 어느 경로로도 표현할 수 없다.

#### F8 【주요】 결과 영속성이 localStorage 전용 — exportStandalone은 결과 미포함, reset 시 전소 — 위탁 결함

영속 계층은 LS 5키뿐이다(app.js:4-10). exportStandalone은 `JSON.stringify(DATA)`로 문제지만
임베드하고(app.js:268), status/choice/revealed/answers는 제외된다(:266-282). resetBtn은
4스토어를 일괄 클리어한다(:327-333). 따라서 학생 채점 원장은 파일 이동·백업이 불가능하고
버튼 한 번으로 전소된다. CLAUDE.md 원칙 3(append-only 누적)과 구조적으로 충돌한다.

#### F9 【치명·신규】 실데이터에서는 문항이 0개로 파싱된다 — 섹션 리셋 버그 (위탁 8건 외, 재현 중 확인)

F3 재현을 위해 parser.js를 모의40 실파일에 실행하니 `problems=0`이 나왔다(typeId 이전에 문항 수집 자체 실패).
원인: splitSections의 일반 헤딩 처리(parser.js:115-118) —

```js
if (/^\s*#{1,2}\s/m.test(ln) && cur !== null && cur !== "answer") {
  if (cur === "select" || cur === "essay") cur = null;   // ← 단원 ## 헤딩마다 수집 중단
  continue;
}
```

모의40은 `## 서답형`(16행) 직후 단원 헤딩 `## I-1 평면좌표 (1~6번)`(18행) 등 4개가 나오므로,
이후 본문 전체가 수집되지 않는다.

```
[재현 — node v24.14.1]
실데이터(모의40) parseAll:            problems=0  typeId_filled=0  tier_filled=0
합성 C(섹션 헤더 뒤 단원 ## 헤딩 1개): problems=0                      ← 격리 재현
합성 A(단원 헤딩 없음):               problems=1                      ← 헤딩이 없으면 정상
[파급 확인]
tools/md2quiz.py:173-176 — parser.js와 동일 리셋 로직(grep 확인) → 정적 변환 파이프라인도 동일 결함
```

결과적으로 현재 웹 뷰어에 모의40을 올리면 문항 0개(드롭힌트만 노출, app.js:382)이고,
F1~F3의 "40문항 typeId 공란"은 이 버그 수정 후에 비로소 관측되는 하류 결함이다.

</findings>

<questions>

- Q1 【사용자 결정 완료(260825) — 회신 불요】 모의40 풀이 여부: **아직 안 풀었다**.
  → 첫 ATTEMPT_LOG는 빈 원장으로 시작한다. (기록 목적 명기)
- Q2 【사용자 결정 완료(260825) — 회신 불요】 부교재 전사본 93문항 복구(PDF 18쪽 재판독):
  **별도 세션 분리**. (기록 목적 명기)
- Q3 【열림 — 판정 요청】 태그 표준형 보강 범위:
  - 안 a) 16번 본문 태그에만 보조유형 `+SM2-11` 보강(답안표와의 최소 정합)
  - 안 b) 40문항 전체를 표준형 `[주유형·Tier·DF목록(+보조)]`으로 재작성
  판단 포인트: 안 b가 F1·F4 교정(RE 표준화)과 가장 정합이지만 문제집 원본 대규모 변경이므로
  원칙 8상 승인이 필요하다. 함께 판정 바란다.

</questions>

<proposed_fixes>

- [ ] parser.js: TAG_RE 공백 허용형으로 교정 + 무괴호 답안표 셀 대응 RE 추가 + `(보조 SM2-XX)` 추출 + DF 코드 추출 + SUBJECT_MAP에 통합사회·한국사 추가 및 공통수학1/2 구분 + 프론트매터 메타블록(set_id/subject/unit/scope_confirmed) 파싱 우선 적용
- [ ] parser.js(F9 신규분): splitSections의 일반 `#{1,2}` 헤딩 처리에서 섹션(cur)을 리셋하지 않도록 수정 — tools/md2quiz.py:173-176 동일 로직 동반 교정 포함
- [ ] app.js: 채점 4상태(O/△/X//) 확장 — 서답형 버튼 4종, 객관식은 정답 선택 시 △ 옵션 제공 / localStorage는 임시버퍼임을 UI 명시 / 「채점 원장 내보내기」 버튼(TSV 다운로드, BOM 포함) 신설
- [ ] output/260822/공통수학2_도형의방정식_모의40.md 및 _part2_직선.md: 16번 본문 태그에 보조유형 +SM2-11 보강 (답안표와 정합)
- [ ] (선택, Q3 연동) 모의40 전체 태그 표준형 재작성 — 승인 시에만

</proposed_fixes>

<output_format>

회신은 아래 표 한 개로 못박는다.

| 질문 | 판정 | 근거 | 제안 |
|------|------|------|------|
| (예: Q3) | 정당/기각/보류 | … | … |

Q1·Q2는 사용자 결정 완료(260825)라 판정 불요다. Q3와 `<proposed_fixes>` 체크박스 5건의
승인 여부만 회신하면 된다. F9는 위탁 목록 외 신규 확인분이므로, 이견 있으면 같은 표에 적어라.

</output_format>

## 이력
- 260825 작성 — 메인 루프 위탁 결함 8건(F1~F8)을 .NET regex + node 실실행으로 독립 재현하여 패키징.
  재현 과정에서 신규 결함 F9(섹션 리셋 → 실데이터 문항 0개, parser.js:115-118 · md2quiz.py:173-176 동일 로직)를
  추가 확인, 총 9건으로 성립. 상태: 대기.
