---
title: "Cycle 0 S2 역량 실험 — Codex assurance team 산출물 선행 감사 (Opus 독립 재검증)"
source: output/260828/diagnostic/math2-method-comparison/codex-team/
source_location: "output/260828/diagnostic/math2-method-comparison/codex-team/{author,audit,critique}/ + 코디네이터 파일"
created: 2026-08-28
author: Claude Code Opus (메인 세션 · 선행 감사)
status: pending
reviewer: unset
---

# Review 01 — Codex assurance team S2 산출물 선행 감사

> ⚠️ 이 문서는 정식 tier-1 라운드가 **아니다**. Codex/OMX 쪽 quota 소진으로 실행되지 못한
> auditor·critic 재검증 구간을 사용자 요청에 따라 Opus가 **선행 대행**한 결과다.
> `_index.md`·`REV_LOG.md`에는 행을 추가하지 않았다(원장 기입은 사용자 판정 사항 — Q5).
> 대상 파일은 하나도 수정하지 않았다(원칙 8).

<document>

## 감사 시점 실측 상태 (모두 재계산)

| artifact | bytes | SHA-256 (앞 12) |
|---|---:|---|
| `author/items.tsv` | 15794 | `484cde845373` |
| `author/types.tsv` | 8598 | `0db58644f823` |
| `author/AUTHOR_REPORT_260828.md` | 16068 | `291c490d4c49` |

audit·critique가 판정 근거로 인용한 해시는 `8316ef0a…` / `acc5b56a…` / `28e1f840…` 이다.
**세 개 모두 현재 파일과 불일치** → 두 리뷰 산출물은 이미 존재하지 않는 v1을 판정한 것이다.

## 게이트 실행 로그 (직접 실행)

```text
$ python output/260828/diagnostic/math2-method-comparison/codex-team/check_experiment.py --phase author
manifest_ok=17/17
duplicate=[] missing=[] extra=[]
type_membership_gate: duplicate=[] missing=[] extra=[]
warnings=0
failures=0
experiment-gate: PASS phase=author
REAL exit=0

$ ... --phase final
warnings=0
failures=4
FAIL: missing final artifact: GATE_REPORT_260828.md
FAIL: missing final artifact: SOL_OPUS_COMPARISON_REPORT_260828.md
FAIL: missing final artifact: 260828_CC_RELAY_SOL_OPUS_COMPARISON.md
FAIL: missing final artifact: LANE_RUNTIME_EVIDENCE_260828.tsv
experiment-gate: FAIL
REAL exit=1
```

## 문자 무결성 실측 (리터럴 `?` 개수)

```text
0  author/items.tsv          0  author/types.tsv
0  author/AUTHOR_REPORT_260828.md
3  TEAM_PREFLIGHT_260828.md          <- 코디네이터 소유
5  ACCEPTANCE_SCHEMA_260828.md       <- 코디네이터 소유 · 동결 manifest 포함
```

</document>

<context>

Cycle 0 S2는 Codex/OMX(gpt-5.6-sol) 4레인(gatekeeper/author/evidence-auditor/adversarial-critic)이
`.claude/agents/type-proposer.md` 역할을 대행할 수 있는지 측정한 역량 실험이다. 대상은
`corpus/EX-math2-20252M`(2025-2학기 중간, 공통수학2, 서술형 4 + 단답형 18 = 22문항).
전 문항 `pNN.png` 부재·`answer_key: null`이라 formal proposer readiness는 설계상 BLOCKED이고,
실험이 측정하는 것은 그 제약 아래에서의 **진단 분석 품질**이다.

파이프라인 진행 상태는 사용자가 전달한 Stage 헤더보다 **한 단계 앞서 있다.** 헤더는
"author가 이제 수정한다"로 되어 있으나, `AUTHOR_REPORT`는 이미 `revision 1`이고 세 산출물의
해시가 모두 리뷰 시점과 다르다. 즉 **author 수정 라운드는 완료됐고, 미실행 구간은
auditor·critic 재검증 이후**다. 이 문서가 그 구간을 대행한다.

</context>

<findings>

## A. author 산출물 — 22문항 전량 독립 재풀이 결과

정본을 보기 전에 transcript만으로 직접 풀고, 그 뒤 `math2.md` 정의와 대조했다.

| ID | 독립 재풀이 결과 | author 배정 | 판정 |
|---|---|---|---|
| W-01 | 기울기 −2, `2x+y−9=0` | SM2-08 | 일치 |
| W-02 | 중심 (6,5) r=5 | SM2-15 | 일치 |
| W-03 | `(x−5)²+(y−1)²=5` | SM2-31 | 일치 |
| W-04 | 이동 (+4,−5), l′ `2x+y−4=0`, 거리 `3√5/5` | SM2-27 + SM2-11 | 일치 |
| S-01 | (0,−1) | SM2-03 | 일치 |
| S-02 | a=4, b=−4, ab=−16 | SM2-08 | 일치 |
| S-03 | a=5 | SM2-26 | 일치 |
| S-04 | 내분점 (−2,−1), k=−2 | SM2-03 + SM2-08 | 일치 |
| S-05 | 교점 `x=2(k−1)/(k+2)`, `y=2(4−k)/(k+2)` → **1<k<4** | ID-free 결정요청 | 일치 (exact match 없음 타당) |
| S-06 | r=5, 현 `4√6` | SM2-15 → SM2-19 | 일치 |
| S-07 | d=3√2, 높이 [2√2,4√2], 넓이차 **8√3** | SM2-25 + SM2-11 | 일치 |
| S-08 | 외심 (3,−1) | SM2-01 | 일치 |
| S-09 | 수직이등분선 `y=x−5`, x=**√17** | SM2-01 + SM2-09 | 일치 |
| S-10 | A′(3,4), B′(6,−4), 최소 **√73** | SM2-33 | 일치 |
| S-11 | a=4, a=−2 → 중심거리 **6** | SM2-12 | 일치 |
| S-12 | 상한 AB=**5**, P=(−2/3,0) | ID-free 결정요청 | 일치 |
| S-13 | 다발 고정점 (−1/2,1/2), 최대 **3√2/2** | SM2-10 + SM2-11 | 일치 |
| S-14 | `0≤m≤24/7`, m=0 접선 1점 + m=1,2,3 각 2점 = **7** | SM2-18 primary + SM2-25 보조 | 일치 |
| S-15 | 변환 중심 (3,−2)/(−7,−2)/(3,0)/(3,−2)/(1,0) → ㄱ·ㄹ | SM2-31 | 일치 |
| S-16 | tan(θ/2)=1/√2, P=(2√2,2), y절편 **6** | SM2-12 + SM2-21 | 일치 |
| S-17 | `f` 정의 0건 (transcript:136, verify_log:8) | BLOCKED / Tier BLOCKED | 일치 |
| S-18 | Q=(3/2)P, PQ=OP/2 구조 — 단일 invariant 미확정 | ID-free 결정요청, SM2-13 불주장 | 일치 |

**결과: 21/21 배정 전부 정확. 오배정 0건.** S-14 → SM2-18 primary 재분류(critic 지적)도
`math2.md:266-272`("d<r/d=r/d>r … 매개변수 범위·정수 조건")와 정확히 맞다. S-17 미보충,
S-18 SM2-13 불주장, S-05/S-12 ID 미발급도 모두 옳은 보수 판단이다.

이 부분에 대한 내 판정은 **PASS**다. 이견 없음.

## B. 세 레인이 모두 놓친 것 (신규 발견)

### F1 — `warnings=0`은 하드코딩 상수다 (critical, 게이트 무효화)

`check_experiment.py:223` 은 `print(f"warnings=0")` 이다. 조건도 변수도 없다.
증거: `--phase final` 실행에서 **`failures=4` · `experiment-gate: FAIL` 인데도 `warnings=0`** 이 찍힌다.

exit code는 정상 동작하므로 fail-open은 아니다. 그러나 CLAUDE.md **원칙 11**은 게이트 수용기준을
"명령 + 기대 출력 문자열 + **경고 0줄** + 기대 카운트"로 적으라고 요구한다. 여기서 "경고 0줄"은
정보량이 0이다 — 어떤 상태에서도 참이다. 즉 이 실험의 수용기준 중 한 축이 **장식**이며,
`warnings=0 + failures=0` 이라는 이중 신호는 실제로는 단일 신호다.

세 레인 전부 이 줄을 증거로 인용했다(author §15, audit §13.1, critic §11). audit C-02는 checker의
불충분성을 지적했지만 근거가 "blank만 검사한다"였고, **`warnings`가 상수라는 사실은 누구도 보지 못했다.**
이는 260826 판정 BF3(`build_catalog_index.py --check`의 `[WARN]` + exit 0)와 **동일 결함 계열의 재발**이다.

### F2 — 동결된 ACCEPTANCE_SCHEMA 자체가 문자 훼손 상태다 (high)

gatekeeper는 "checker에 문자 무결성 규칙을 추가했다"(TEAM_PREFLIGHT:34)고 선언했지만,
그 규칙을 **자기 소유 파일에는 적용하지 않았다.**

```text
ACCEPTANCE_SCHEMA_260828.md:8  "Consolidation into 5?12 reusable types"        <- 5–12 (en-dash 소실)
ACCEPTANCE_SCHEMA_260828.md:9  "source-axis-labelled importance (`?? 1?`; …)"  <- ★★ 기출 1회 계열이 전멸
ACCEPTANCE_SCHEMA_260828.md:1  "Exact acceptance schema ? Math2 …"
TEAM_PREFLIGHT_260828.md:1,5   동일 계열 2건
```

특히 `:9`는 **중요도 표기 형식을 지정하는 수용기준 문장**이다. author가 만족시켜야 할 정확한
문자열이 파괴되어 있으므로, author는 요구 형식을 **추측해서** 맞춘 셈이다(결과적으로는
`기출축 ★(2025-2M 1회) / 부교재축 …`로 잘 맞췄다).

audit은 C-01의 근거로 `ACCEPTANCE_SCHEMA_260828.md:3-5,16`을 인용하면서 **자기가 인용한 그 파일이
:9에서 같은 병으로 훼손된 것을 보지 못했다.**

**더 나쁜 점 (260828 정정 — 최초 작성 시 "manifest에 해시 동결됨"이라 적은 것은 오류다):**
`ACCEPTANCE_SCHEMA_260828.md`와 `EXPECTED_ITEM_IDS_260828.tsv`는 `AUTHOR_INPUT_MANIFEST_260828.tsv`
17행 **어디에도 없다**(corpus 3 + bindata 3 + 카탈로그 6 + curriculum + FORECAST_GUIDE +
type-proposer.md + ASSURANCE_GUIDE + AGENTS.md). `check_experiment.py`도 없다.

즉 이 실험은 **읽기 전용 정본 17개는 해시로 동결하면서, 정작 판정의 자를 이루는 세 파일
(수용기준·기대 식별자·게이트 코드)은 동결하지 않았다.** 그리고 세 파일 모두 gatekeeper 소유다.

게이트가 **심사 대상 레인은 검사하고 자기가 만든 자는 면제**하는 비대칭 구조다.

### F2-b — 측정 후에 자를 고쳤고, 그 결과를 재측정하지 않았다 (high, 신규)

`TEAM_PREFLIGHT_260828.md`의 「Post-audit preflight correction」은 coordinator가
`EXPECTED_ITEM_IDS_260828.tsv`의 W-04 범위를 `44-51` → `44-48`로 **audit 이후에** 고쳤다고 자인한다.
현재 파일도 `44 48`이다.

그런데 audit §7·N-01·§11-3은 바로 그 항목을 **author의 FAIL**로 판정했다 — "frozen expected end=51인데
author는 44-48". 순서를 복원하면:

1. author가 `44-48`로 씀 → 2. audit이 자(`44-51`)와 다르다며 FAIL 3건 중 1건으로 계상 →
3. gatekeeper가 **자를 author 값으로 고침** → 4. audit은 재실행되지 않음.

결과: audit의 W-04 FAIL은 지금 **반증 불가능한 상태**로 남아 있다. 인용한 증거(`expected row 5=44-51`)가
더 이상 존재하지 않기 때문이다. author가 처음부터 옳았고 자가 틀렸다는 사실이 어느 문서에도 기록되지 않았다.

또한 이 수정은 gatekeeper 자신의 `<boundary>`("Write only the exclusive gate report and
external-evaluation package fields assigned by the leader")를 벗어난다. `check_experiment.py` 수정
(TEAM_PREFLIGHT:34 자인)도 같다.

### F3 — 문자 무결성 검사가 보고서 본문에는 걸려 있지 않다 (medium)

`require_report()`(`:168-188`)는 마커 문자열 존재만 본다. `?`·U+FFFD·제어문자 검사는
`items.tsv`·`types.tsv`의 **행 필드에만** 걸려 있다(`:107-126`, `:150-159`).
따라서 TEAM_PREFLIGHT:34의 "The deterministic checker now rejects ASCII `?` …"는
**코드가 실제로 하는 일보다 넓게 서술된 주장**이다. 현재 `AUTHOR_REPORT`는 깨끗해서 실피해는 없다.

### F4 — `?` 전면 금지 규칙은 과광범위한 fail-closed 함정이다 (low, 잠재)

`:110`은 `"?" in row` 로 10개 열 전부를 검사한다. 정당한 물음표(한국어 의문문, 수식 주석)도
전량 FAIL이다. mojibake는 보통 **한글 인접 `?`** 또는 **연속 `?`** 로 나타나므로, 그 패턴이나
읽기 시점 인코딩 검증으로 좁히는 편이 낫다. 지금 형태로 동결하면 이후 author는 물음표를 쓸 수 없다.

### F5 — audit·critique는 stale인데 그 표시가 어디에도 없다 (medium, 절차)

두 문서의 헤더 판정은 각각 `REVISE`·`BLOCKED`이고, 인용 해시는 전부 v1이다.
critic §7의 그룹별 판정표(DIAG-G03~G09 멤버십)는 **현재 `types.tsv`에 존재하지 않는 구조**를
판정하고 있다(revision 1이 9군 → 12행 U10/U11/G12 구조로 재편). 디렉터리를 파일 순서로 읽으면
PASS 게이트 옆에 BLOCKED 판정이 나란히 있고, 어느 쪽이 현행인지 문서만으로는 판별 불가다.

### F6 — 5~12 exact-cover 제약 자체가 결함인데 아무도 그렇게 부르지 않았다 (high, 설계)

author는 22문항의 정직한 primary generator를 **최소 16개**로 식별했다
(SM2-08/15/31/27/03/26/25/01/33/12/10/18 + S-05·S-12·S-18 결정요청 + S-17 BLOCKED).
16 > 12이므로 **exact-cover ≤12 파티션은 의미를 보존한 채로는 수학적으로 불가능**하다.

author의 대응은 `DIAG-U10`·`DIAG-U11`이라는 우산 행을 만들고, 그 행의 필드에 스스로
"세 문항은 서로 독립 subgroup이며 하나의 reusable type가 아님"이라고 적는 것이었다.
정직한 라벨링이지만, **결과물은 게이트를 통과시키기 위한 빈 행**이다.

원칙 9-c-iii·11의 정신에 맞는 처분은 우회가 아니라 **수용기준을 결정요청으로 올리는 것**이었다:
(a) 상한을 16 이상으로 올리거나 (b) exact-cover를 버리고 primary/secondary 다중배정을 허용
(정본 카탈로그 형식 자체가 다중배정 모델이고, author의 `items.tsv`도 이미 `SM2-03 + SM2-08` 식으로
다중배정하고 있다 — 즉 item 레벨과 type 레벨의 모델이 서로 모순이다).
audit은 "5~12 PASS"로 형식만 봤고, critic은 개별 통합군을 때렸을 뿐 **제약 자체를 겨냥하지 않았다.**

### F7 — 두 리뷰 레인 모두 배점 축을 한 번도 쓰지 않았다 (medium, 리뷰 깊이)

transcript는 단답형 18문항의 **정확한 배점**을 제공한다(`:20`, 3.0~3.7점, 합 60.0 실측 일치).
`DIFFICULTY_RUBRIC.md`의 Tier는 배점 밴드로 정의된다(T1 3.0~3.2 / T2 3.2~3.5).
즉 이 실험에는 **Tier 판정용 객관 앵커가 원문에 이미 있다.**

- author: 22행 중 **20행의 `tier_basis`가 배점을 인용**한다. S-04는 "T2 경계 가능성은 감사 대상",
  S-05는 "배점 3.1점은 T1 신호지만 DF1·DF8 기준에서는 T2 경계"라고 **긴장을 스스로 노출**했다.
- audit·critique: `배점` 언급 **0회**(grep 실측).

결과로 두 가지가 생겼다.

1. audit N-03("S-04 T1은 구조상 T2 경계")은 **author가 이미 자기 필드에 적어 둔 문장의 재진술**이다.
   신규 발견이 아니므로 audit의 발견 수율이 그만큼 부풀려져 있다. 그리고 배점 3.1은 T1 밴드이므로
   author의 T1 유지가 오히려 근거가 강하다.
2. critic #9는 DF8만으로 S-05 Tier를 밀었고 revision 1이 T1 → T2로 올렸다. 배점 3.1은 T1 밴드다.
   **결론이 틀렸다고 단정하지는 않는다**(DF8은 실제 상향 요인이고 3단계 구조도 사실이다).
   문제는 **원문에 있는 반대 증거를 어느 레인도 저울에 올린 기록이 없다**는 점이다.
   author 스스로 제시한 반증이 리뷰 과정에서 응답 없이 사라졌다.

### F8 — revision 1에 "미반영 지적과 그 사유" 구획이 없다 (low, 절차)

`AUTHOR_REPORT §3`은 반영 항목만 나열한다. audit N-02(bindata)·N-03(S-04 Tier)은 표에 없고,
본문 다른 곳에서 처분되지도 않았다. REV_GUIDE는 owner가 **반영하지 않은 지적에도 흔적을**
남기도록 요구한다. 실제로 N-03은 배점 근거로 기각하는 것이 옳았으므로, 기각 사유를 적었다면
F7의 문제까지 같이 해소됐을 사안이다.

## C. 성능 비교 — Codex 팀 vs. 내가 했을 때

사용자가 요청한 비교. 축별로 실측 근거만 쓴다.

| 축 | Codex assurance team | Opus(이 세션) | 평가 |
|---|---|---|---|
| **수학 내용 정확도** | 21/21 배정 정확, 오류 0 | 독립 재풀이 21/21 동일 | **동급.** 차이 없음 |
| **critic의 독립 재계산** | S-05 `1<k<4`, S-07 `8√3`, S-12 `5`·P=(−2/3,0), S-14 `7`, S-15 ㄱ·ㄹ | 전부 동일 검증 | **동급.** critic 5/5 정확 |
| **권한 경계 보수성** | S-17 미보충, 답 미주장, ID 미발급, canonical 미수정 — 전부 준수 | 동일 판단 | **동급.** 이 부분은 매우 잘했다 |
| **자기 산출물 결함 검출** | audit·critic이 v1의 문자 훼손·S-14 오분류·과도 통합을 잡아냄 | 동일하게 잡았을 것 | **동급.** 레인 분리가 실제로 작동했다 |
| **자기 도구 결함 검출** | `?` 미검사만 발견 | `warnings=0` 상수(F1) 추가 발견 | **Opus 우위.** 게이트 신호 자체의 유효성을 의심하지 않았다 |
| **자기 상류 문서 검사** | 코디네이터 파일 훼손 0건 발견 | F2 발견(동결 수용기준 훼손) | **Opus 우위.** "심사자는 심사받지 않는다"는 사각지대 |
| **수용기준 자체에 대한 도전** | 제약 안에서 우회(U10/U11) | F6으로 제약 결함 판정 | **Opus 우위.** 가장 큰 격차 |
| **원문 신호 활용** | author는 배점 20/22 인용(우수), 리뷰 2레인은 0회 | 배점을 Tier 검증의 1차 축으로 사용 | **혼합.** author는 동급 이상, 리뷰 레인은 열위 |
| **파이프라인 상태 정합** | Stage 헤더가 실제 상태보다 1단계 뒤 | 해시 대조로 즉시 발견 | **Opus 우위.** stale 판정 미표시(F5) |
| **문서 산출 밀도** | 매우 높음(구조·표·근거 인용 철저) | 동급 | **동급** |

**요약.** 문항 단위 실무(풀이·배정·Tier·경계 준수)에서 Codex 팀은 **Opus와 실질적으로 동급**이다.
21문항 오배정 0, critic 독립 재계산 5/5 정확은 자력으로 낸 결과이고 과장이 없다.

격차는 **한 층 위, 메타 층에서만** 났다. 세 레인 모두 자기 파이프라인이 정한 규칙과 도구를
**주어진 전제로 받아들였고**, 그 안에서만 서로를 감사했다. 그래서

- 게이트가 출력하는 숫자가 진짜인지 (F1)
- 자기들이 동결한 기준 문서가 온전한지 (F2)
- 만족시키려는 수용기준이 애초에 만족 가능한지 (F6)
- 원문이 이미 주는 객관 앵커를 쓰고 있는지 (F7)

이 네 가지를 아무도 묻지 않았다. adversarial-critic조차 **author를 향해서만 적대적이었지
실험 설계를 향해서는 적대적이지 않았다.** 이것이 이번 실험에서 관측된 유일한 실질적 성능 차이다.

역량 실험의 결론으로 읽으면: **Codex 팀은 `type-proposer`의 분석 실무를 대행할 수 있다.
단, 자기 자신의 게이트·기준·설계를 감사하는 역할까지 같은 팀에 맡기면 그 층은 비어 있게 된다.**

</findings>

<questions>

1. audit·critique를 v1 판정으로 **동결 보존**하고 재검증분을 새 파일로 받을 것인가,
   아니면 두 문서에 `SUPERSEDED — v1 판정` 머리표를 붙일 것인가? (원칙 3상 내용 수정은 불가)
2. F6(5~12 exact-cover 불가능)을 **수용기준 개정**으로 처리할 것인가, 현행 U10/U11 우회를
   "제약 하 최선"으로 승인할 것인가?
3. F7의 S-05 Tier는 배점 3.1 근거로 **T1 환원**인가, DF8 근거로 **T2 유지**인가?
4. F1·F3·F4의 `check_experiment.py` 수정 주체는 gatekeeper(Codex)인가 이 세션인가?
   원칙 8상 나는 내가 쓰지 않은 파일을 고치지 않는다.
5. 이 문서를 **정식 tier-1 라운드로 승격**해 `_index.md`·`REV_LOG.md`에 행을 남길 것인가,
   아니면 **선행 참고 자료**로만 둘 것인가?

</questions>

<proposed_fixes>

- [ ] **P1** `check_experiment.py:223`의 `print(f"warnings=0")`을 실제 경고 집계로 교체하거나,
      경고 채널이 없다면 그 줄을 삭제한다. 동시에 이 실험의 수용기준 문구에서 `warnings=0`을
      제거한다(정보량 0인 조건을 게이트에 남기지 않는다 — 원칙 11).
- [ ] **P2** `ACCEPTANCE_SCHEMA_260828.md:1,8,9`와 `TEAM_PREFLIGHT_260828.md:1,5`의 훼손 문자를
      UTF-8로 복구한다. 복구 전까지 `:9`의 중요도 형식 요구는 **⚠️미확정**으로 라벨링한다.
- [ ] **P2-b** `ACCEPTANCE_SCHEMA`·`EXPECTED_ITEM_IDS`·`check_experiment.py` 세 파일을
      **manifest에 편입해 해시 동결**한다. 판정의 자가 동결되지 않으면 어떤 게이트 결과도 재현 불가다.
- [ ] **P2-c** audit의 W-04 FAIL(§7·N-01·§11-3)에 대해 **자가 틀렸고 author가 옳았다**는 사실을
      기록한다. 자 변경 후 재측정 없이 FAIL 판정만 남아 있는 현 상태를 해소한다.
- [ ] **P3** 문자 무결성 검사를 코디네이터 소유 md(`TEAM_PREFLIGHT`·`ACCEPTANCE_SCHEMA`)와
      `require_report()` 대상 보고서에도 적용한다. 게이트의 검사 범위와 TEAM_PREFLIGHT:34의
      서술을 일치시킨다(원칙 10 동반 갱신).
- [ ] **P4** `?` 검사를 `한글 인접 ?` 또는 `?{2,}` 패턴으로 좁혀 정당한 물음표를 허용한다.
- [ ] **P5** `audit/`·`critique/`에 현행성 표시를 추가한다(신규 파일 또는 머리표).
      기존 판정 본문은 원칙 3에 따라 보존한다.
- [ ] **P6** 수용기준 §2의 "5~12 reusable types + exact cover"를 개정한다.
      권고: **상한 제거 또는 16 이상 상향**, 그리고 exact-cover 대신 `primary 1 + secondary N`
      다중배정 허용. 근거: item 레벨은 이미 다중배정 모델이고 type 레벨만 파티션을 강요해
      두 모델이 모순이다.
- [ ] **P7** S-05 Tier를 **배점 3.1 근거로 T1 환원**하고, DF8 긴장은 `tier_basis`에만 남긴다.
      (Q3에서 T2 유지로 결정되면 대신 배점 반대증거를 `tier_basis`에 명시적으로 기각 기록한다.)
- [ ] **P8** `AUTHOR_REPORT §3`에 **미반영 지적과 기각 사유** 구획을 신설하고 audit N-02·N-03을
      기재한다. N-03은 "배점 3.1 = T1 밴드"를 사유로 기각이 타당하다.
- [ ] **P9** 향후 assurance 실험의 preflight에 **메타 감사 레인**(게이트 코드·수용기준·설계
      가정을 대상으로 하는 adversarial 레인)을 추가한다. 근거: 이번 실험에서 F1·F2·F6·F7이
      전부 이 레인 부재로 누락됐다.
- [ ] **P10** 자(ruler) 변경에 **two-key 규칙**을 건다 — `check_experiment.py`·`ACCEPTANCE_SCHEMA`·
      `EXPECTED_ITEM_IDS` 수정은 gatekeeper 단독으로 성립하지 않고, 감사권한자의 재동결
      (`RULER_FREEZE_260828.tsv` 갱신 행)이 있어야 유효하다. 근거: F2-b는 단독 권한이었기에 가능했다.
- [ ] **P11** **측정-후-자변경 시 재측정 강제** 규칙을 preflight에 명문화한다. 자가 바뀌면 그 자로
      내려진 모든 판정은 자동으로 stale이며, 재실행 전까지 인용 금지. 검출은
      `meta_gate_260828.py --check staleness`가 담당한다.
- [ ] **P12** 판정문(`audit/`·`critique/`)에 **대상 산출물 해시 기재를 필수 필드로** 승격한다.
      현재는 본문 산문에만 있어 stale 판정이 자동 검출되지 않는다(§D 실측 2건 FAIL).
- [ ] **P13** (R1) `EXPECTED_ITEM_IDS_260828.tsv`를 손작성 표에서 **생성물**로 전환한다.
      `gen_expected_ids_260828.py`를 codex-team으로 이식하고, 게이트가 매 실행 재생성·대조하게 한다.
      동시에 F9(규칙 2종 혼재)를 해소한다 — W-04를 `44-49`로 되돌려 rule_a로 통일하는 것을 권고.
- [ ] **P14** (R3·R4) `check_experiment.py`에 `--selftest`를 신설해 심은 결함 11종을 매번 증명하게 하고,
      `TEAM_PREFLIGHT_260828.md:34`의 능력 주장 산문을 **그 실행 출력으로 대체**한다.
      현행 실측: detected=8 / **undetected=3**(report 본문·자·수용기준). undetected 3종을 0으로 만드는 것이
      P1·P3의 수용기준이 된다 — `[OK]` 문자열이 아니라 `undetected=0`이 게이트다(원칙 11).
- [ ] **P15** (R2) `codex-team/` 16파일을 버전관리에 넣는다. 실측: 비교 기준인 `opus/…EVALUATION_260828.md`는
      tracked인데 심판받는 쪽과 자 전부가 untracked이고 `check_experiment.py`는 커밋 이력이 0이다.
      단계별 커밋이 있으면 `RULER_FREEZE_260828.tsv`는 불필요해진다. **커밋은 사용자 승인 사항이라 미실행.**

</proposed_fixes>

<output_format>

| question | verdict | evidence | proposal |
|---|---|---|---|
| Q1 | | | |
| Q2 | | | |
| Q3 | | | |
| Q4 | | | |
| Q5 | | | |

| fix | approve/reject | owner | note |
|---|---|---|---|
| P1 … P9 | | | |

</output_format>

## D. 2차 안전 울타리 — 감사권한자 소유 메타 게이트 (260828 구축)

### D-1. 구축한 것 (원칙 8 준수 — codex-team 파일은 읽기만 했다)

| 파일 | 소유 | 역할 |
|---|---|---|
| `output/260828/rev/RULER_FREEZE_260828.tsv` | 감사권한자(이 세션) | 자 7종 + 레인 산출물 5종, 총 **12개 파일의 SHA-256·바이트 동결**. gatekeeper의 manifest가 덮지 않는 영역을 독립 당사자가 덮는다. |
| `output/260828/rev/meta_gate_260828.py` | 감사권한자(이 세션) | 1차 게이트가 **면제한 대상**(= gatekeeper 자신의 자)을 측정하는 5개 검사. |

핵심 설계 차이 — **1차 게이트는 author를 재고, 2차 게이트는 자를 잰다.**

### D-2. 실행 로그 (원칙 11 수용기준: 명령 + 기대 출력 + 경고 0줄 + 실측 카운트)

```
$ python output/260828/rev/meta_gate_260828.py --check all
--- freeze ---      freeze_ok=12/12
--- integrity ---   integrity_files_scanned=16 integrity_hits=7
--- signal ---      vacuous_signal_count=1
--- coverage ---    coverage_checks=2 coverage_failures=2
--- staleness ---   staleness_author_artifacts=3 staleness_verdict_docs=2
checks_run=5   warnings=0   failures=7
meta-gate: FAIL
exit=1
```

failures 7건 = F1(1) + F2(2) + F3/설계면제(2) + F5(2). **전부 gatekeeper 소유 파일에서만 나왔다.**
author revision 1은 `?` 0건 — 즉 이 울타리는 author를 다시 때리는 도구가 아니다.

`warnings=0`은 여기서 **리스트 길이 계산 결과**다(`len(warnings)`). F1과 같은 글자를 출력하지만
의미가 반대다 — 이것이 P1이 요구하는 수정의 동작 예시다.

### D-3. 오탐·미탐 실측 (heuristic 정직성)

`?` 검사는 전면 금지(F4의 함정)가 아니라 **문맥 규칙**이다: 백틱 스팬이 오직 `?`로만 이루어지면
그 문자를 인용하는 것으로 보아 허용, 단어문자 뒤 + 공백/줄끝 앞이면 정상 종결 물음표로 허용.

| 파일 | 리터럴 `?` | 훼손으로 판정 | 판정 |
|---|---|---|---|
| `ACCEPTANCE_SCHEMA_260828.md` | 5 | 5 | 전부 훼손 (L1 em-dash, L8 en-dash, L9 중요도 표기 3자) |
| `TEAM_PREFLIGHT_260828.md` | 3 | 2 | L34의 `` `?` `` 는 정상 인용으로 허용 |
| `audit/EVIDENCE_AUDIT_260828.md` | 8 | 0 | 전부 `` `?` `` 인용 — 정상 허용 |
| `critique/ADVERSARIAL_CRITIQUE_260828.md` | 3 | 0 | 동상 |
| `author/*.tsv`, `AUTHOR_REPORT` | 0 | 0 | revision 1에서 수리 완료 확인 |

**오탐 0건 / 16파일.** 초판에서 미탐 1건(`` `?? 1?` `` 의 마지막 물음표가 "단어문자 뒤 + 백틱 앞"
조건에 걸려 정상 종결로 오인)이 있어 닫는 백틱을 허용 문맥에서 제외했고, 재실행에서 5/5로 잡혔다.

### D-4. 이 울타리가 **못 막는 것** (한계 명시)

1. **자기 면제** — `meta_gate_260828.py`는 자기 자신과 `rev/`를 스캔하지 않는다. 이번에 발견한
   결함(측정자가 측정 대상에서 빠지는 것)과 **동일한 구조**를 이 도구도 갖는다. 이것은 2차
   울타리로 해소할 수 없고, 3차(사람 또는 별도 tier-3)가 필요한 이유다.
2. **차단력 없음** — 이 게이트는 exit 1을 낼 뿐, Codex 파이프라인의 진행을 물리적으로 막지 못한다.
   preflight가 이 명령을 **stop 조건으로 인용해야** 비로소 울타리가 된다(P10·P11).
3. **자를 검증하지 못함** — 자가 훼손됐다는 것은 잡지만, 자의 *내용이 옳은지*(예: 5~12 제약이
   타당한지, F6)는 기계가 판단할 수 없다. 이 축은 메타 감사 레인(P9)이 사람 판단으로 맡는다.

### D-5. 감사권한자가 쓸 수 있는 울타리 수단 — 전체 목록

| # | 수단 | 무엇을 막나 | 현재 상태 | 필요 권한 |
|---|---|---|---|---|
| 1 | **독립 해시 동결** (`RULER_FREEZE`) | 측정 후 자 변경(F2-b) — 사후 검출 | ✅ 적용 | 감사권한자 단독 가능 |
| 2 | **메타 게이트** (자를 재는 게이트) | 게이트 자기면제(F1·F2·F3) | ✅ 적용 | 감사권한자 단독 가능 |
| 3 | **판정 현행성 바인딩** (판정문에 대상 해시 필수) | stale 판정 인용(F5) | ◐ 검사만 구현, 필드 승격은 P12 | 규격 개정 필요 |
| 4 | **two-key 자 변경** (gatekeeper + 감사권한자 재동결) | 자 변경을 단독으로 못 하게 — **사전 차단** | ✗ P10 | preflight 개정 필요 |
| 5 | **측정-후-자변경 시 재측정 강제** | 자 변경으로 지적이 소멸하는 경로(F2-b) | ✗ P11 | preflight 개정 필요 |
| 6 | **메타 감사 레인** (게이트·수용기준·설계가정 대상 adversarial) | 설계 결함(F6)·리뷰 깊이(F7) | ✗ P9 | 팀 구성 개정 필요 |
| 7 | **교차 모델 감사** (Opus가 gatekeeper 산출물을 감사) | 동일 모델 4레인의 공통 맹점 | ◐ 이번 감사가 그 1회 실증 | 사용자 승인 |
| 8 | **사용자 직보 경로** (감사 결과가 gatekeeper를 경유하지 않음) | 감사 대상이 감사 결재선에 앉는 구조 | ✅ 이 문서가 그것 | 이미 확보 |

**사전 차단력이 있는 것은 4·5·6뿐**이고, 셋 다 preflight/팀 구성 개정을 요구한다 —
즉 감사권한자 단독으로 세울 수 있는 울타리는 **사후 검출**까지가 한계다.
1·2·8은 지금 세웠고, 3·4·5·6은 승인이 필요하다(P9~P12).

## E. 원천 처방 참조 구현 — R1·R3 (260828 구축)

§D의 2종은 **사후 검출**이다. 아래 2종은 실패 모드 자체를 없애는 쪽이며, 채택은 gatekeeper 몫이므로
**참조 구현**으로만 제출한다(원칙 8: codex-team 파일 무수정).

### E-1. R1 — 자를 생성물로 (`gen_expected_ids_260828.py`)

`transcript.md` 하나에서 22개 item_id·행범위를 결정론적으로 재생성하고 현행 자와 대조한다.

```
$ python output/260828/rev/gen_expected_ids_260828.py
transcript_lines=152
derived_items=22 shipped_items=22
rule_a_diff_count=1      # 다음 경계 직전까지
rule_b_diff_count=20     # 마지막 비공백 행까지
warnings=0  failures=2
FAIL: NO SINGLE RULE REPRODUCES THE SHIPPED RULER -> the ruler is hand-authored, not generated
FAIL: diff(rule_a) W-04: rule_a=44-49 shipped=44-48
exit=1
```

**신규 발견 F9 (medium) — 현행 자는 두 규칙이 섞여 있다.**
22개 중 21개는 rule_a(다음 헤딩·수평선 직전까지)로 정확히 재현되고, **W-04 단 하나만** rule_b
(마지막 비공백 행)로 적혀 있다. gatekeeper는 파서 버그를 **파서가 아니라 출력에서** 고쳤고
(`TEAM_PREFLIGHT:33`), 그 결과 같은 파일 안에 서로 다른 두 규칙이 공존한다 — 원칙 9-a가
"같은 상황에 두 정책이 공존하면 그 자체가 결함"이라 한 형태와 동일하다.
rule_b를 전체에 적용하면 20건이 어긋나므로 **W-04를 44-49로 되돌리는 것이 규칙 일관성 해법**이며,
어느 쪽을 택하든 자는 손이 아니라 코드가 만들어야 한다. 재생성 결과는
`EXPECTED_ITEM_IDS_260828.regenerated.tsv`(rev/ 안, 원본 무수정).

### E-2. R3 — 게이트 자가시험 (`gate_selftest_260828.py`)

codex-team 트리를 샌드박스로 복사해 알려진 결함 11종을 심고, 1차 게이트가 결함마다 **새 실패를
내는지** 차등 비교한다. 검출기가 자기 검출력을 실증한 적이 없으면 검증되지 않은 검출기다.

```
$ python output/260828/rev/gate_selftest_260828.py
source_files=16
baseline_exit=0 baseline_failures=0 baseline_warnings=0
fixtures=11 detected=8 undetected=3
warnings_values_observed=[0]
source_unchanged=True drifted=[]
selftest: FAIL   exit=1
```

| 픽스처 | 판정 | 증명 대상 |
|---|---|---|
| items_mojibake / control_char / blank_field | DETECTED | author TSV 무결성·공란 검사 살아 있음 |
| s17_tier / s17_assignment | DETECTED | S-17 BLOCKED 규칙 살아 있음 |
| duplicate_id / missing_id / types_undercount | DETECTED | ID·exact cover 검사 살아 있음 |
| **report_mojibake** | **UNDETECTED (exit 0)** | **F3 기계 확증** — 보고서 본문에 훼손 7자를 넣어도 PASS |
| **ruler_edit** | **UNDETECTED (exit 0)** | **F2-b 근본원인 기계 확증** — 자의 W-04를 `999`로 바꿔도 PASS |
| **schema_ruler_edit** | **UNDETECTED (exit 0)** | 수용기준 md를 통째로 훼손해도 PASS |

**F1도 기계 확증됐다:** baseline + 결함 11종, 총 12회 실행에서 `warnings=` 관측값 집합이
`[0]` 하나다. 결함이 8건 검출된 실행에서도 경고는 0이었다 — 코드를 읽지 않고도 그 채널이
공허함이 증명된다.

**중요 — author 재평가:** baseline이 `exit=0 failures=0`이다. 즉 **author revision 1은 강화된
게이트를 이미 통과한다.** 사용자가 붙여넣은 Stage 헤더의 "의도대로 FAIL(3)"은 수정 전 산출물
기준이며, 현행 산출물에는 적용되지 않는다. §A(22문항 전량 재풀이)와 합치면 author 레인에 남은
쟁점은 S-05 Tier(Q3)뿐이다.

**무손상 증거:** `source_unchanged=True drifted=[]`, 실행 후 `meta_gate --check freeze` →
`freeze_ok=12/12`. 모든 변형은 샌드박스에서만 일어났다(원칙 9-b).

### E-3. 그래서 더 강한 울타리인가 — 축별로 다르다

| 축 | §D (사후 검출) | §E (원천) | 실제로 더 강한가 |
|---|---|---|---|
| 게이트 공허·죽은 검사 | 사람이 코드 정독 | **자가시험이 매 실행 증명** | **예 — 질적으로 다르다.** 읽는 사람 없이도 유지되고, 게이트가 길어져도 확장된다 |
| 자 변경 | 해시 대조로 사후 검출 | 재생성으로 조작 무효화 | **예 — 단, gatekeeper 채택 후에만.** 지금은 참조 구현이라 검출력만 있다 |
| 판정 stale | 해시 대조 | 버전관리(R2) | **R2 미실행** — 커밋은 사용자 승인 사항이라 보류 |
| 기준 타당성(F6) | 사람이 발견 | 불가 | **아니오 — 변함없이 사용자 자리** |

정리하면 **F1·F3 축은 확실히 더 강해졌고**(정독 → 기계 증명), **F2-b 축은 아직 아니다**
(검출은 되지만 무효화는 채택 후). F6 축은 어떤 도구로도 강해지지 않는다.

## F. 유형 분석 측 수정안 — F6·Q2·Q3 (260828 구축)

§B의 발견 중 **분석 산출물에 걸리는 것은 F6 하나**다(나머지 8건은 gatekeeper 소유 인프라).
아래는 그 하나와 S-05 Tier(Q3)에 대한 수정안이며, **원본 무수정·제안본만** 제출한다(원칙 8).

### F-1. 무엇이 실제로 잘못됐나 — 유형 통합 층만

`types.tsv` 13행 중 3행이 유형이 아니다. `DIAG-U10`(S-07,S-10,S-12)과 `DIAG-U11`(S-13,S-14,S-18)은
자기 `type_disposition`에 **"세 문항은 서로 독립 subgroup이며 하나의 reusable type가 아님"** 이라고
적혀 있다. 즉 22문항 중 **16문항만 유형화됐고 6문항은 회계용 빈칸에 담겼다.**
배정 층(22/22 정확)·중요도 축 병기·카탈로그 전량 HOLD는 모두 정상이다.

### F-2. 제안 산출물 3종

| 파일 | 내용 |
|---|---|
| `types.proposed.tsv` | **16행.** G01~G09·BLOCKED-G12는 원문 그대로 보존(원칙 3), `DIAG-U10`·`DIAG-U11`을 해체해 `DIAG-G20`~`DIAG-G25` 6행으로 분리. 각 행에 실제 variation axis 2개·함정·중요도 축·카탈로그 disposition을 채웠다. |
| `ITEMS_CELL_FIXES_260828.tsv` | S-05 `tier` T2→**T1**(IF-01) + `tier_basis` 동반 갱신(IF-02). 배점 3.1은 T1 대역이고, critic #9는 DF8만으로 상향했으며 author가 이미 제시한 배점 반증을 기록상 저울질하지 않았다. DF8 긴장은 삭제하지 않고 "T1 상단"으로 보존한다. |
| `ACCEPTANCE_SCHEMA_260828.repaired.md` | 훼손 문자 5개 복원 + §2 개정(행수 밴드 폐지, exact cover는 유지, **회계용 우산 행 금지**) + **escalation duty 신설**(기준이 만족 불가능하면 우회 대신 decision request). |

새 group_id는 `G20`부터 시작한다 — 기존 `BLOCKED-G12`를 개명하지 않으면서(원칙 3)
`DIAG-G12`와의 번호 충돌도 만들지 않기 위해서다(원칙 9-a).

### F-3. 샌드박스 검증 (원본 무손상)

```
=== A. 현행 게이트(5..12 제약 그대로) + 제안 types.tsv ===
[current-gate] exit=1
   FAIL: type group count outside 5..12: 16
=== B. 동반 갱신(check_experiment.py:143 상한 제거) 후 ===
[amended-gate] exit=0
   experiment-gate: PASS phase=author
proposed_type_rows=16 members=22 unique=22
source_unchanged=True
```

**원칙 10 실증:** 수용기준 §2만 고치고 게이트 코드를 그대로 두면 **개정 기준을 만족하는 파일이
게이트에서 FAIL한다.** 두 파일은 반드시 같은 작업에서 함께 고쳐야 하며, 이 동반 갱신 목록은
`ACCEPTANCE_SCHEMA_260828.repaired.md` 말미에 명시했다.

### F-4. 적용 주체

author 레인이 quota 소진으로 정지 상태이므로, 승인 시 적용 주체는 **사용자 또는 재가동된 author
레인**이다(원칙 8: 승인된 항목만 작성 주체가 원본에 반영). 이 세션은 어느 원본도 수정하지 않았다.

## G. 재시작 팀 인계 — 자(ruler)와 산출물의 소유 분리 (260828 추가)

§E-3은 F6 축을 "변함없이 사용자 자리"로 판정했다. 그런데 재시작 인계를 정리하면서 F6·F9를
**재시작 팀의 입력 과제**로 넘기려 한 순간이 있었다 — 사용자 지적으로 철회한다. 그 처분은
F2-b(자를 실행 레인이 단독으로 고칠 수 있었다)를 구조 그대로 재생산한다.

| 발견 | 성격 | 소유 | 재시작 팀에 주는 형태 |
|---|---|---|---|
| F6 (수용기준 §2 5~12 exact-cover) | **자** — 채점 기준 | 사용자 / `rev-arbiter` | 개정 확정 후 **동결본을 제약으로 지급**. 팀은 소비만 |
| F9 (`EXPECTED_ITEM_IDS` 규칙 2종 혼재) | **자** — 측정 눈금 | 생성기 코드 + 감사측 동결 | 생성기(`gen_expected_ids_260828.py`)를 이식해 **매 실행 재생성**. 표 손수정 금지 |
| F1 (`warnings=` 상수) · F3 (보고서 본문 미검사) | **자** — 검출력 | 감사측 | `--selftest`로 `undetected=0` 실증 후 게이트 채택. 자기 게이트 자기 판단 개정 금지 |
| F2-b (자 단독 변경 권한) | **자** — 권한 구조 | 사용자 | two-key 재동결 규칙(P10)을 preflight에 선탑재 |
| F7 (배점 축 미사용) · F8 (미반영 지적 구획 부재) | **산출물·절차** | 실행 레인 | 그대로 팀 과제로 인계 |
| Q3 (S-05 Tier) | **산출물** | 실행 레인 (배점 근거 기록 의무) | 그대로 팀 과제로 인계 |

따라서 `ACCEPTANCE_SCHEMA_260828.repaired.md`는 **팀에 넘길 과제가 아니라 사용자·arbiter가
판정할 제안**이다. 판정 전에는 자가 없으므로 재시작 팀은 §2 관련 작업을 시작할 수 없다
(⚠️ 자 미확정). `gen_expected_ids_260828.py`·`gate_selftest_260828.py`는 참조 구현이며,
팀이 채택하더라도 **동결·재동결 권한은 감사측에 남는다**.

이 구조를 CLAUDE.md **원칙 12**(피측정자는 자기 자를 소유하지 않는다)와 AGENTS.md
`Non-negotiable repository rules`에 정본화했다 — 실행 주체를 교체해도 재발하는 종류의 결함이므로
Codex 재시작만으로는 해소되지 않는다.

## history

- 260828 · 최초 작성. Codex quota 소진으로 미실행된 auditor·critic 재검증 구간을 Opus가 선행 대행.
  22문항 전량 독립 재풀이 + 게이트 직접 실행 + 해시 재계산 기반. 대상 파일 무수정, 원장 무기입.
- 260828 · F2 사실오류 정정(manifest 동결 주장 철회) + F2-b 신설 + P2-b·P2-c 신설.
- 260828 · §D 신설. 2차 안전 울타리 2종 구축(`RULER_FREEZE_260828.tsv`, `meta_gate_260828.py`),
  실행 결과 failures=7(전량 gatekeeper 소유 파일). P10·P11·P12 신설.
  codex-team 파일은 여전히 **1건도 수정하지 않았다** — 신규 파일은 모두 `output/260828/rev/` 안.
- 260828 · §E 신설. 원천 처방 참조 구현 2종(`gen_expected_ids_260828.py`, `gate_selftest_260828.py`)
  + 재생성 산출물 1종. F1·F3를 기계 확증했고 **F9 신규 발견**(자에 규칙 2종 혼재).
  author revision 1이 강화 게이트를 통과함을 baseline으로 확인(exit 0, failures 0).
  P13·P14·P15 신설. R2(커밋)는 사용자 승인 사항이라 미실행. 무손상: `freeze_ok=12/12`.
- 260828 · §F 신설. 유형 분석 측 수정안 3종 제출(`types.proposed.tsv` 16행,
  `ITEMS_CELL_FIXES_260828.tsv`, `ACCEPTANCE_SCHEMA_260828.repaired.md`).
  샌드박스 검증: 현행 게이트 FAIL(16>12) → 동반 갱신 후 PASS, exact cover 22/22 unique.
  `source_unchanged=True`. 적용은 승인 후 author 또는 사용자가 수행.
- 260828 · §G 신설. 재시작 인계 시 F6·F9를 실행 레인 과제로 넘기려 한 처분을 사용자 지적으로 철회.
  자/산출물 소유 분리를 CLAUDE.md 원칙 12·AGENTS.md 비협상 규칙으로 정본화. codex-team 파일 무수정.
