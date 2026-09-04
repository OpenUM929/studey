---
doc: 260831_09 — 판정: 측정기 파서 결함 M6·M7 수리 승인 + 자 재서명 two-key
judge: rev-arbiter (Claude Code Opus, 동일 저장소)
date: 260903
target: `output/260831/260831_19_twokey_m6m7_and_resign.md` (결정요청 패킷, REV_GUIDE §6-d (1))
thread: 260831 자·측정기 계열. 선행 판정 `260831_07`(파서 귀속 기준) · `260831_08`(재서명·BF-R4)
independence: fresh context — 이 세션은 대상 패킷·자 3종·샌드박스 산출물을 이 라운드에 처음 읽었다.
  등급 `binding`은 REV_GUIDE §6-d (3) 배우표에서 유도된 값이며 판정자가 고른 값이 아니다.
write_surface: 이 판정문 + `analysis/REV_LOG.md` 1행 + `output/260831/rev/_index.md` 1행 + 자기 WIP
head: 941af21 (무커밋)
state: **확정** — U1·U2·U3·U4 approve / U5 revise-required(차단 수정 5건). 반영 주체는 메인 루프.
---

# §0 판정 요약표

| unit | verdict | grade | evidence | measured | closure | note |
|---|---|---|---|---|---|---|
| U1 M6·M7 파서 귀속 + 패치 승인 | **approve** | binding | `patched.py` exit=0 / `base.py` exit=1 · GATE3 mismatches 2→0 · 인쇄선언 2축 동시 착지(§1-B) | yes | COMMAFIX 매치 1/51 전사본(정확히 M7 1건) · TO_SEL 맨숫자 7줄/51 | 귀속을 `type-extractor`(전사)에서 **측정기 파서**로 정정. M5는 전사 결함 유지 |
| U2 폐쇄(대상 2유닛 밖 무이동) | **approve** | binding | 판정자가 `--per-item` base/patched를 직접 파싱·대조(§1-D) | yes | **k/N = 0/40 유닛 = 0/975 행** — 공통 40유닛의 문항별 score·r·tier·유닛평균 전량 불변, 잔여 없음 | 40→42는 GATE3 불일치 해소로 두 유닛이 모집단에 **복귀**한 것 |
| U3 검출력(원칙 12-d) | **approve** | binding | 판정자가 `prove.py` 직접 실행 exit=0 · knockout 2건 모두 발화(§1-E) | yes | **knockout 2/2 발화 · undetected=0** · 심은 fixture 15(표식축 9 + 상태축 6), 거짓양성 방지 자리 4 포함 | GATE 0s 신설 승인. `prove.py`의 `undetected`가 이진값인 점은 §3 N4 |
| U4 자 재서명 개시 | **approve** (순서 구속) | binding | 판정자가 `regen_preview` 충실도 diff 확인 후 직접 실행(§1-G) — `TOOL` 1줄만 상이 | yes | 밴드 임계값 불변: 폐쇄율 모집단 510→982(1.93배) 동안 **95.7% 동일**, 계층 최저 89.6→89.7, hold-out 최저 92.0→92.0 | 순서 구속: ①측정기 반영·`exit=0` 확인 → ②**정본** regen으로 지시 취득(미리보기 B축 2건은 인공물) |
| U5 반영 방법 | **revise-required** | binding | 판정자가 regen 종료조건 L461 · 지시행 36건 · 역할 사각 18자리를 직접 실측(§1-H) | yes | A축 지시 36/28행, 역할 사각 **18자리는 기대값이 없음** → 제안 수용기준 `stale=0 residual=0` **도달 불가** | 방법(textpatch)은 유지, 수용기준 교체 + 18자리 개별 판정 + `ALLOW` 별도 two-key. 차단 수정 5건 |

---

# §1 독립 재검증

패킷의 리터럴은 한 개도 옮겨 적지 않았다. 아래는 전부 **이 판정 세션에서 실행한 명령의 출력**이다.
파이프 뒤에서 exit code를 읽지 않았다(원칙 11-b). `$SB` = 패킷 §1이 지정한 샌드박스
`…/af319f01-a809-4feb-9753-894f91204270/scratchpad/sb`.

## A. 자 3종 무접촉 — 해시 불변

```
$ sha256sum tools/measure_score_bands.py tools/regen_rubric_values.py analysis/catalog/DIFFICULTY_RUBRIC.md
23d6b87be9714ed6f6b24ccb6bbb8008957cdf0eba9f5cf997afbed6eee1a243 *tools/measure_score_bands.py
259bbfdfc3a6520efd7c2cf21c0d90ca1b24101e23db0d347300d9794a0ba975 *tools/regen_rubric_values.py
62674856f148e9ce4b2519044d7c410f9f9824823a5d8e8e9c458701bb27df21 *analysis/catalog/DIFFICULTY_RUBRIC.md
$ wc -c (동일 3파일)
20662 / 21129 / 20294
```
패킷 §1 동결 표와 일치. HEAD `941af21` 유지, 무커밋. 종료 시 재확인은 §5.

**샌드박스 base가 정본과 동일한가** — 폐쇄 대조의 전제이므로 직접 확인했다.
```
$ diff <(tr -d '\r' < tools/measure_score_bands.py) <(tr -d '\r' < $SB/base.py)
(차이 0줄)   ;  sha256($SB/base.py) = 23d6b87b… 로 정본과 동일
```

**patched가 정말 「3줄」인가 — 아니다. 판정자 실측은 4 hunk · 24행이다.**
```
$ diff <(tr -d '\r' < $SB/base.py) <(tr -d '\r' < $SB/patched.py)
38a39        > COMMAFIX= re.compile(r'([\[(][^\S\n]*[0-9])[^\S\n]*,[^\S\n]*([0-9][^\S\n]*점)')
46c47        TO_SEL 에 대안 |\d{1,2}\s*$ 추가
86c87        normalize() 합성에 COMMAFIX.sub(r'\1.\2', t) 삽입
163a165,166  GATE 0 fixture 2행 추가 (comma-decimal / comma-thousands)
173a177,195  GATE 0s 신설 19행 (TO_SEL 상태전이 fixture 6종 + [ABORT] + sys.exit(1))
```
패킷 §3은 이를 「3줄 패치」로 부른다. 나머지 21행은 전부 fixture이고 패킷 §4 U3이 그 신설을
별도 판정 대상으로 명시했으므로 **은닉이 아니라 명명 부정확**이다. 승인 범위를 오해 없이 고정하기
위해 이 판정문은 승인 대상을 **위 4개 hunk 전체**로 정의한다(§3 N1).

## B. M6·M7이 파서 결함인가 — `260831_07` 귀속 기준 재적용

기준: 「파스 규칙을 고쳤을 때 **인쇄 선언에 정확히 착지**하면 파서 결함」.
판정자는 **개수축과 총점축이 독립으로 동시 착지**하는지를 직접 확인했다.

```
$ grep -nE "선택형[^0-9]{0,6}[0-9]+[^0-9]{0,6}문항" corpus/EX-korean-20241M/transcript.md
30:◑ 총( 11 )쪽, 선택형( 24 )문항, 서답형( 3 )문항
$ (동일 명령) corpus/EX-english-20251M/transcript.md
29:◑ 총( 10 )쪽, 선택형( 23 )문항, 서답형( 5 )문항
```

| 유닛 | 인쇄 선언 n | base n / 총점 | patched n / 총점 | 착지 |
|---|---|---|---|---|
| `EX-english-20251M` | 23 | 22 / 66.7 `EXCL` | **23 / 70.0** | 개수 ✓ · 총점 70.0 = 영어 전 유닛 공통 선택형 총점 ✓ |
| `EX-korean-20241M` | 24 | 23 / 57.2 `EXCL` | **24 / 60.0** | 개수 ✓ · 57.2+2.8 = **60.0** 정수 착지 ✓ |

(위 4개 수치는 판정자가 `base.py` / `patched.py` 의 `selective-score distribution` 절에서 직접 읽었다.)

두 축이 **독립으로 동시에** 선언값에 착지한다. 패킷은 M7에 대해서만 2축 논증을 폈으나
판정자 실측 결과 **M6도 66.7 → 70.0 으로 총점축이 함께 착지**한다 — 패킷이 제시한 것보다
강한 증거다. 따라서 `260831_07` 기준상 두 건은 명백히 **측정기 파서 결함**이다.

원인도 직접 확인했다. 두 건 모두 **전사는 원본을 정확히 옮겼다.**

```
$ grep -n '2,8' corpus/EX-korean-20241M/transcript.md
149:7. (가)와 (나)의 관점으로 <보기>를 설명한 것으로 가장 적절한 것 은?(2,8점)
```
→ M7: 원본 시험지의 소수점 오타 `(2,8점)`. `MARK` 정규식이 `[(]\s*숫자\s*점` 을 요구하므로
표식 자체를 못 본다. 전사 오류가 아니다.

```
$ sed -n '141,151p' corpus/EX-english-20251M/transcript.md
| (가) ______ [2 점 ] (나) ______ [3 점 ] |      <- 서답형 답안란
(빈 줄)
10                                              <- L145, 마침표 없는 맨 번호
다음 밑줄 친 … 에 해당하는 사례와 근거로 가장 적절한 것은?
```
→ M6: HWP 추출이 `10.` 의 마침표를 떼어냈고, 마침표를 요구하는 `TO_SEL` 이 발화하지 못해
문항 10의 배점이 직전 서답형 구간에 흡수된다. 이것도 전사 오류가 아니다.

## C. 지시받은 두 위험면적 — 직접 실측

### C-1 `TO_SEL` 의 `\d{1,2}\s*$` 과잉 발화 — 오탐 6/7이지만 전량 무해함을 실증

```
$ grep -rn --include=transcript.md -E '^[[:space:]]*[0-9]{1,2}[[:space:]]*$' corpus/
corpus/EX-english-20251M/transcript.md:145:10
corpus/EX-korean-20241F/transcript.md:98:1
corpus/EX-korean-20251M/transcript.md:60:1
corpus/EX-korean-20251M/transcript.md:62:2
corpus/EX-korean-20251M/transcript.md:64:3
corpus/EX-science-20252F/transcript.md:216:11
corpus/EX-science-20252F/transcript.md:218:12
```
전 코퍼스 **51개 transcript 중 7줄 / 4유닛**. 패킷의 「7」은 실측 재현됐다
(`corpus/*/transcript.md` = 51건; `EX-*` 만이면 50건 — 패킷의 「51유닛」은 전자 기준으로 정확).

**그러나 패킷은 이 7줄이 실제로 문항 번호인지 확인하지 않았다. 판정자가 7줄 전부의 문맥을 열었다:**

| 위치 | 내용 | 실체 | 판정 |
|---|---|---|---|
| `EX-english-20251M:145` | `10` | 문항 번호 10 (마침표 탈락) | **참 양성** — M6 대상 |
| `EX-korean-20241F:98` | `1` | `<보기>` 사전 표제어 `거치다 「동사」` 의 뜻풀이 번호 | 오탐 |
| `EX-korean-20251M:60,62,64` | `1`,`2`,`3` | `<보기>` 수필(한흑구 `<보리>`)의 문단 번호 | 오탐 3 |
| `EX-science-20252F:216,218` | `11`,`12` | 세트 머리 `[ 11 ~ 12 ]` 가 줄바꿈으로 분해된 조각 | 오탐 2 |

**정밀도 1/7 = 14.3%.** 「맨숫자 = 문항 번호」라는 명제로 보면 이 대안은 **틀렸다.**
그럼에도 **차단 사유가 되지 못하는 이유를 두 축으로 실증**했다.

1. **효과 폐쇄** — 오탐 6건은 전부 파서가 이미 `sel` 상태인 지점이라 상태 전이가 no-op이다.
   §1-D 폐쇄가 이를 전수로 증명한다: 공통 40유닛 **0/975행** 이동.
2. **fail-closed 그물이 실재한다** — 오탐이 장차 서답형 구간에서 발생하면 n이 선언값에서
   이탈하고 GATE 3 개수축이 즉시 발화한다. 그 커버리지를 판정자가 소스에서 직접 확인했다:
   `tools/measure_score_bands.py` L215가 `decl is None` 을 **불일치로 계상**하므로
   patched의 `GATE 3 mismatches=0` 은 「선언을 못 읽은 유닛 0 + 어긋난 유닛 0」을 뜻한다.
   오탐 3유닛 모두 선언이 실제로 파싱돼 있다:
   ```
   EX-korean-20241F   F body  n=24  decl=24  sum=80.0
   EX-korean-20251M   M body  n=24  decl=24  sum=60.0
   EX-science-20252F  F body  n=24  decl=24  sum=80.0
   ```
   즉 **선택형 42유닛 전부가 개수축 게이트에 덮여 있고, 침묵 실패 경로가 아니다.**

CLAUDE.md 원칙 12-d상 판정자가 규칙 축소를 **요구**하려면 그 축소가 잡아내는 **알려진 실패**를
지목해야 한다. 폐쇄가 0/975이므로 현 코퍼스에 그런 실패는 존재하지 않는다.
→ 차단이 아니라 **§3 N2**(최소 수리 후보안 포함)로 내린다.

### C-2 `COMMAFIX` 천단위·목록 쉼표 오탐 — 전 코퍼스 매치 1건, 정확히 M7

정규식을 코퍼스 전체에 판정자가 직접 돌렸다.
```
$ python <판정자 스크립트 j_comma.py>
corpus\EX-korean-20241M\transcript.md :: …가장 적절한 것 은?(2,8점)
COMMAFIX matches=1 in 1 units (population=51 transcripts)
probe '누적 (1,234점=합계)'  -> '누적 (1,234점=합계)'      (불변 — 천단위 미매치)
probe '[1,234 점]'          -> '[1,234 점]'             (불변)
probe '(가, 나) 2점'         -> '(가, 나) 2점'            (불변 — 목록 쉼표 미매치)
probe '(2,8점)'             -> '(2.8점)'                (의도된 수리)
probe '(3, 4점)'            -> '(3.4점)'                (이론적 오탐 — 코퍼스 0건)
```
**`k/N` = 매치 1건 / 51 transcript, 그 1건이 정확히 판정 대상이다.**
천단위는 쉼표 뒤가 세 자리라 미매치, 목록 쉼표는 여는 괄호 뒤가 숫자가 아니라 미매치.
유일한 이론적 오탐 `(3, 4점)` 은 코퍼스 실측 0건 → **§3 N3**(회귀 fixture)로 남긴다. 차단 아님.

## D. 폐쇄 — 판정자가 직접 계산한 k/N

패킷은 「공통 40 중 이동 0」이라고만 적었다. 판정자는 그 값을 옮겨 적지 않고
`--per-item` 출력의 **문항 단위 행 전량**(unit·idx·score·r·tier + 유닛별 `mean unit price` 행)을
직접 파싱해 대조했다.

```
$ python $SB/base.py    --per-item  > base.txt 2>&1 ; echo "exit=$?"      -> exit=1
$ python $SB/patched.py --per-item  > pat.txt  2>&1 ; echo "exit=$?"      -> exit=0
$ python <판정자 스크립트 j_close.py>
base units=40  patched units=42
only in patched: ['EX-english-20251M', 'EX-korean-20241M']
only in base   : []
common=40  moved=0
CLOSURE k/N = 0/40
base rows=975 patched rows=1024
```

산술이 닫힌다: `975 = 935 문항행 + 40 유닛평균행`, `1024 = 982 + 42`.
→ **폐쇄 k/N = 0/40 유닛 = 0/975 행. 잔여 목록: 없음(빈 리스트).**

비교면이 유닛 요약(n, 총점)이 아니라 **문항 단위 (score, r, tier)** 라는 점이 중요하다 —
유닛 총점은 같은데 내부 분포만 바뀌는 경우까지 이 대조가 배제한다.

40 → 42 는 `EXCL = set(mism) - set(sumonly)`(L252)가 GATE 3 불일치 유닛을 집계에서 빼기 때문이며,
수리로 불일치가 사라져 두 유닛이 **모집단에 복귀**한 것이다. 판정자도 base 분포표에서 두 유닛에
`EXCL` 표식이 붙어 있고 patched 에서 사라진 것을 확인했다.

## E. 검출력 — 판정자가 직접 knockout

`prove.py` 를 **먼저 읽어** 그것이 주장하는 일을 실제로 하는지 확인했다: `patched.py` 본문에서
수리 앵커를 문자열 치환으로 제거한 사본(`ko.py`)을 만들어 실행하고 `[FAIL] fixture` 발화를 센다.
앵커가 없으면 `!! 앵커 없음` 으로 실패 처리한다. 장식 fixture를 걸러내는 올바른 설계다.

```
$ python $SB/prove.py ; echo "exit=$?"
M7 COMMAFIX 무력화          exit=1  발화=2
      [FAIL] fixture comma-decimal  got=[] want=['2.8']
      planted=9 undetected=1
M6 맨숫자 대안 제거             exit=1  발화=3
      [FAIL] fixture bare-number      TO_SEL=False want=True
      [FAIL] fixture bare-number-pad  TO_SEL=False want=True
      planted-state=6 undetected=2
---
knockout=2  undetected=0
exit=0
```
무력화 사본은 **둘 다 exit=1 로 abort** 한다 — fail-closed(원칙 11). 정상 patched 실행에서는
```
=== GATE 0 fixture: planted parser defects ===
planted=9 undetected=0
planted-state=6 undetected=0
[GATE 0 PASS] undetected=0
```
거짓 양성 방지 자리도 patched 소스에서 실재를 확인했다 — `comma-thousands`(`누적 (1,234점=합계)` → `[]`),
`prose-number`(`약 10 명이 참여했다` → False), `three-digit`(`2024` → False),
`sod-header`(`[ 서답형1(서술) ] 쓰시오` → False). fixture가 **잡는 것과 안 잡는 것을 함께** 고정한다.
→ **검출력 closure: knockout 2/2 발화, undetected=0, 심은 fixture 15(표식축 9 + 상태축 6).**

## F. 정본·샌드박스 게이트 현황 (파이프 없이 실측)

```
$ python tools/measure_score_bands.py > /dev/null 2>&1 ; echo "exit=$?"   -> exit=1
$ python tools/regen_rubric_values.py > /dev/null 2>&1 ; echo "exit=$?"   -> exit=1
$ python $SB/base.py    > /dev/null 2>&1 ; echo "exit=$?"                 -> exit=1
$ python $SB/patched.py > /dev/null 2>&1 ; echo "exit=$?"                 -> exit=0
```
정본 측정기 말미: `[FAIL] GATE 3 mismatches=2 -- EX-english-20251M EX-korean-20241M`
patched 말미: `[OK] GATE 1 undetected=0 / GATE 3 mismatches=0 (GATE 2 warning-only per BF-K1-7a)`

## G. 재서명 값 — `regen_preview` 충실도 확인 후 직접 실행

먼저 미리보기가 정본 재생성기의 **충실한 사본**인지 확인했다.
```
$ diff <(tr -d '\r' < tools/regen_rubric_values.py) <(tr -d '\r' < $SB/regen_preview.py)
31c31
< TOOL = 'tools/measure_score_bands.py'
---
> TOOL = r'…\scratchpad\sb\patched.py'
```
**차이는 `TOOL` 한 줄뿐**이다 — 패킷의 설명대로다.

```
$ python $SB/regen_preview.py > … 2>&1 ; echo "exit=$?"      -> exit=1
== GATE 0: 검출기 자기 검출력 (원칙 12-d) ==
  planted=11 undetected=0        [GATE 0 PASS]
== 재생성된 정본 수치 (손으로 넣은 상수 0개) ==
  전수 폐쇄   940/982 = 95.7%  residual=42
  계층 최저   89.7% (M-2025)
  연도 hold-out   2024 n=469 fit=468 99.8% / 2025 n=513 fit=472 92.0% / 최저 fold = 92.0%
  유닛        전체 50 · 선택형 보유 42
  Tier 100환산  T1 5문 / T2 33문 / T3 39문 / T4 23문  (환산 합계 = 100)
```
수리 **전** 값은 판정자가 `base.py` 로 직접 잰 `895/935 = 95.7%`, 계층 최저 `89.6% (M-2025)` 다.

**핵심 확인: 자의 판단 임계값은 움직이지 않는다.** 유효 밴드 `r ∈ [0.80, 1.20]` 의 전수 폐쇄율이
모집단 510 → 982 (1.93배) 동안 **95.7% 로 동일**하고, 계층 최저는 89.6 → 89.7, 연도 hold-out
최저는 92.0 → 92.0 이다. 재서명은 **판단 기준의 변경이 아니라 인용 수치를 현행 모집단에
맞추는 작업**이라는 패킷의 요지는 실측으로 지지된다.

부수 변화 1건: 100문제 환산 사다리가 T2 34→33 · T4 22→23 으로 1문항씩 이동한다
(문항별 Tier 비중 base `4.6/32.1/37.6/21.4` → patched `4.7/31.8/37.5/21.8`).

## H. 자 본문 대조의 **실행 가능성** — U5의 결정적 실측

정본 재생성기 실행 결과:
```
$ python tools/regen_rubric_values.py > … 2>&1 ; echo "exit=$?"      -> exit=1
  stale=57 lines=28 residual=18
  A축(역할) 36건 / B축(정체성) 0건 / C축 잔차 61건 · 그중 역할 사각 18건
  역할 사각: L37/24 L38/24 L78/24 L79/22 L79/24 L79/32 L79/32 L121/24 L121/24
             L140/24 L140/32 L140/32 L140/32 L164/24 L185/40 L195/40 L201/32 L208/40
```

종료조건을 소스에서 직접 읽었다 — `tools/regen_rubric_values.py` L461:
```python
return 1 if (keys or a or b) else 0
```
즉 **exit 0 은 `stale=0` 을 요구**하고, `residual` 은 `hits` 의 부분집합이므로 `stale=0 ⇒ residual=0` 이다.

**그런데 28행 중 지시(`-> 기대`)가 붙은 것은 A축 36건뿐이다.** 판정자 실측:
```
$ grep -cE "^  :[0-9]+ +\[.*\] .* -> " <regen 출력>      -> 36
잔차(역할 사각) 소재 행: L37 L38 L78 L79 L121 L140 L164 L185 L195 L201 L208   (11행 · 18자리)
```
`[잔차]` 항목에는 **기대값이 없다** — 후보 역할만 괄호로 나열한다.
따라서 **A축 36건을 기계 반영해도 18자리가 그대로 남아 `stale=18`, exit=1 이다.**

그 18자리가 무엇인지 판정자가 자 본문을 직접 열어 확인했다:

| 자리 | 본문 | 실체 | 처리 |
|---|---|---|---|
| `L79/22` | `**깊이** (260822 신설)` | **날짜의 부분 문자열** | 갱신하면 문서 파손 → 허용목록 |
| `L79/32`×2, `L79/24`, `L140/32`×3, `L140/24`, `L201/32` | `→원상(SM2-32 #19)`, `반지름(SM2-24 #32)`, `(SM2-31·32 #23)`, `제작(#30·31·32)` | **유형ID·문항번호의 부분 문자열** | 갱신하면 문서 파손 → 허용목록 |
| `L37/24`, `L38/24`, `L121/24`×2 | `선택형 총점 60 · 24문항`, `60점/24문 환산 \| 80점/24문 환산` | 단가 공식의 **예시 분모**(최빈 문항수 24 — 수리 후에도 24) | 무변경 → 허용목록 |
| `L164/24` | `한 시험(≈24문항 + 서답형…)` | **근사 서술어** | 무변경 → 허용목록 |
| `L185/40`, `L208/40` | `10 / 30 / 40 / 20`, `T3 40%` | **목표 사다리**(실측 아님). `ALLOW` 에 같은 어구의 `(185,'20')`·`(208,'20')` 은 **이미 등재**돼 있는데 `40` 만 빠져 있다 | 허용목록 **누락 실증** |
| `L195/40` | `T3 상 \| 30% \| **43%** (40문항)` | 100환산 문항수 — **진짜 이동 대상**(§1-G의 재생성값은 39문) | 갱신 대상 |
| `L78/24` | 판정자가 이 라운드에 문맥 특정 못 함 | 미상 | 개별 판정 필요 |

즉 18자리는 **한 덩어리가 아니라 「허용목록 누락」과 「진짜 이동값」이 섞인 혼합**이며,
자동 지시가 없으므로 **자리마다 사람이 역할을 정해야** 한다.
그리고 `ALLOW` 확장은 자 소스 L36 주석이 스스로 밝히듯 **그 자체가 12-c two-key 대상**이다:
```python
# 이 목록을 늘리는 것 자체가 12-c two-key 대상이다(BF-R4).
```

---

# §2 unit별 판정

## U1 — M6·M7을 파서 결함으로 인정하고 패치를 승인하는가 → **approve** (binding)

**승인한다.** 근거는 §1-B: 두 유닛 모두 개수축과 총점축이 **독립으로 동시에** 인쇄 선언에 착지하며,
이것이 판정 `260831_07`이 정한 파서 결함 판별 기준 그 자체다. 원인도 파스 규칙에 있음을 원문 인용으로
확인했다 — M7은 원본 오타 `(2,8점)`를, M6은 HWP 추출이 남긴 마침표 없는 `10` 을 **전사가 정확히
옮긴 것**이다. 전사에 오류가 없으므로 `type-extractor` 귀속은 성립하지 않는다.

따라서 `260831_04` F3의 `type-extractor` 일괄 귀속에서 **이 2건을 분리 정정한다.**
**M5(`EX-science-20242F` 요약행 78.8/21.2 vs 열거 80.0/20.0)는 전사 결함으로 그대로 둔다** —
M5는 원본 요약행과 열거값이 서로 어긋나는 건이라 파스 규칙을 고쳐도 선언에 착지하지 않는다.

**승인 범위(오해 방지용 정의)**: 패킷이 「3줄」이라 부른 것의 실제는 **4 hunk · 24행**이다(§1-A 실측).
승인 대상은 그 전부 — `COMMAFIX` 정의 1행 · `TO_SEL` 대안 1개 · `normalize()` 합성 1행 ·
GATE 0 fixture 2행 · GATE 0s 신설 19행. **이 범위를 벗어난 변경은 이 판정으로 승인되지 않았다.**

**조건 없음.** C-1의 오탐 6건은 차단 사유가 아니다: 효과가 전수 폐쇄로 0이고(§1-D), 장차의 오탐은
GATE 3 개수축이 42/42 커버리지로 fail-closed 포착한다(§1-C-1). 원칙 12-d상 「잡아낼 알려진 실패」를
지목할 수 없는 요구는 차단이 아니라 follow-up이다.

## U2 — 폐쇄: 패치가 대상 2유닛 밖을 움직이지 않는가 → **approve** (binding)

**확인했다. `k/N` = 0/40 유닛 = 0/975 행, 잔여 없음** (판정자 자체 계산, §1-D).
패킷의 주장과 값이 일치하나, 이 판정문의 값은 패킷에서 옮긴 것이 아니라 판정자가 base/patched를
각각 실행해 문항 단위로 파싱·대조한 결과다. 모집단 경계: `--per-item` 이 출력하는 선택형 보유 유닛 전체.

## U3 — 검출력: 심어둔 fixture가 실제로 발화하는가 → **approve** (binding)

**발화한다. knockout 2/2, undetected=0** (판정자 직접 실행, §1-E).
`GATE 0s` 신설도 함께 승인한다 — `TO_SEL` 은 상태 전이 규칙이라 `extract_marks()` 경로 밖이고,
그 경로에 fixture가 없으면 M6 계열 재발을 아무도 잡지 못한다. 원칙 12-d가 요구하는 「알려진 실패」는
M6 자신(`EX-english-20251M` L145)이며 fixture `bare-number` 가 그것을 재현한다.
거짓 양성 방지 자리 4종이 함께 심겨 있어 「무조건 True를 돌려주는 검출기」로 통과하는 우회를 막는다.

## U4 — 자 재서명(two-key)을 지금 개시하는가 → **approve** (binding)

**개시한다.** 근거는 §1-G: 자의 **판단 임계값**(유효 밴드 `r ∈ [0.80, 1.20]`, Tier 경계)은
한 개도 움직이지 않고 폐쇄율이 95.7% 로 동일하다. 모집단이 510 → 982 로 1.93배가 되는 동안
같은 밴드가 같은 비율을 담는다는 것은 재서명이 **기준 변경이 아니라 인용 갱신**임을 뒷받침한다.
`regen_preview.py` 가 정본 재생성기와 `TOOL` 한 줄만 다른 충실한 사본임도 diff로 확인했다.

**다만 순서에 구속 조건을 건다.** 아래 순서를 어기면 결과는 stale이다.

1. **먼저** U1에서 승인한 4 hunk를 `tools/measure_score_bands.py` 에 반영한다.
   수용기준: `python tools/measure_score_bands.py > /dev/null 2>&1 ; echo "exit=$?"` → **`exit=0`**,
   그리고 표준출력에 `[OK] GATE 1 undetected=0 / GATE 3 mismatches=0` 1줄 · `[FAIL]` 0줄 ·
   `[GATE 0 PASS] undetected=0` 1줄. (원칙 11: `[OK]` 문자열만으로 끝내지 않는다.)
2. **그다음** 정본 `python tools/regen_rubric_values.py` 를 돌려 **정본 도구가 만든 지시 목록**을
   얻는다. `regen_preview.py` 의 출력을 그대로 쓰지 마라 — 미리보기의 `B축(정체성) 2건` 은
   **미리보기 자신의 파일명·바이트가 자 본문과 다르기 때문에 생긴 인공물**이며(정본 실행의
   B축은 0건이었다), 이를 지시로 받아들이면 자에 미리보기의 정체성을 새기게 된다.
3. 자 본문의 측정기 정체성 줄(`L237` `반영 후 20662 B / 23d6b87be9714ed6`)은 **반영 후 실측한
   바이트·해시**로 갱신한다. 샌드박스 `patched.py` 는 21969 B / `0cf91284e2c1f7b1` 이지만
   이는 샌드박스 사본의 값이므로 **정본 반영 후 다시 재어 쓴다**(원칙 9-c: 사본 열거 금지).
4. 재서명 완료 판정은 U5의 수정된 수용기준을 따른다.

**범위 밖 명시**: 자 3종은 현재 HEAD `941af21` 대비 작업 트리 상태다
(`analysis/catalog/DIFFICULTY_RUBRIC.md` 는 ` M`, 두 도구는 `??` 미추적 — §5 실측).
재서명은 작업 트리에서 진행하며 **커밋 여부는 이 판정의 대상이 아니다.**

## U5 — 반영 방법: 자 본문을 무엇이 고치는가 → **revise-required** (binding)

패킷 제안 (a)의 **방법은 옳고 수용기준은 도달 불가능하다.** 그대로 승인하면 실행 레인이
만족 불가능한 자 앞에 서게 되고, CLAUDE.md 원칙 12-a가 지목한 두 우회로(우산 산출물 F6 /
눈금 손질 F9)가 정확히 그 자리에서 열린다. 그래서 승인하지 않는다.

**대안 (b) `regen --write` 신설은 기각한다** — 재생성기 자체의 개정이라 별도 two-key가 필요할 뿐
아니라, §1-H가 보인 대로 **18자리는 기계가 기대값을 모른다**. 쓰기 기능을 붙여도 그 18자리는
못 쓴다. 기능만 늘고 문제는 그대로다.
**대안 (c) 사용자 한정도 기각한다** — 36건의 기계 반영까지 사람 손에 맡기는 것은 원칙 12-b
(「자는 손이 아니라 코드가 만든다」)의 후퇴다.

**채택: (a)를 두 갈래로 쪼갠 수정안.**

- [ ] **C-1** A축 36건은 `tools/textpatch.py patch` 로 기계 반영한다(손편집 금지, 원칙 12-b).
      입력은 U4-2에서 얻은 **정본** 재생성기 출력의 `:행번호 [역할] 현재 -> 기대` 행이다.
- [ ] **C-2** 역할 사각 18자리는 **자리마다 「갱신」인지 「허용목록」인지 판정**해 상신한다.
      §1-H 표가 판정자의 예비 분류다. 최소한 `L195/40`(→ 39) 은 갱신, `L79/22`·`L79/32`·
      `L140/32`·`L201/32` 계열은 날짜·유형ID 조각이라 허용목록이다.
- [ ] **C-3** `ALLOW` 확장은 **자를 재는 자의 개정이므로 별도 two-key** 다
      (자 소스 L36 주석이 스스로 그렇게 규정한다: 「이 목록을 늘리는 것 자체가 12-c two-key
      대상이다(BF-R4)」). C-2의 허용목록 항목은 사유와 함께 별도 상신하고, **이 판정으로
      선승인되지 않는다.**
- [ ] **C-4** 수용기준을 아래로 **교체한다**. 패킷의 `stale=0 lines=0 residual=0` 은
      C-3이 닫히기 전에는 도달 불가능하므로 그대로 쓰면 안 된다.
      - **중간 게이트(C-1 직후)**: `python tools/regen_rubric_values.py` 의 출력이
        **`A축(역할) 0건 / B축(정체성) 0건`** 일 것(지금은 A축 36 / B축 0 / stale=57 — §1-H 실측).
        exit code는 이 단계에서 여전히 1이므로 **exit 로 판정하지 않는다.**
        잔여 `stale`·`residual` 의 기대 카운트는 **판정자가 이번 라운드에 재지 않았으므로
        여기에 숫자를 적지 않는다**(원칙 9-c-iii — 미실측 수치는 게이트가 아니다).
        대신 실행 시 실측해 기록하고, **잔여 자리(행+리터럴)가 전부 C-2 판정 목록 안에 들어
        있는지**를 확인한다. 목록 밖 자리가 하나라도 있으면 `▲ blocked` 이고 C-2로 되돌아간다.
      - **최종 게이트(C-2·C-3 반영 후)**: `python tools/regen_rubric_values.py > /dev/null 2>&1 ;
        echo "exit=$?"` → **`exit=0`**, 그리고 출력에 `stale=0 lines=0 residual=0` 1줄 ·
        `[GATE 0 PASS] undetected=0` 1줄 · `[WARN]`/`[FAIL]` 0줄.
- [ ] **C-5** 허용목록으로 넘긴 자리마다 **왜 실측값이 아닌지**를 `ALLOW` 값 문자열에 적는다
      (현행 10건이 이미 그 형식이다). 사유 없는 등재는 곧 자 무력화이므로 금지한다.

**재라운드 범위는 U5로 한정한다.** U1·U2·U3·U4는 이 판정으로 확정됐고 재론 대상이 아니다.

---

# §3 follow-up (비차단 — 반영 주체는 메인 루프, 별건 처리 가능)

- **N1 패치 상신의 규모 표기** — 「3줄 패치」는 실측 4 hunk·24행이었다. 이후 자 패치 상신은
  `diff` 실측으로 **hunk 수·행 수**를 적는다(원칙 9-c-iii: 본문 수치는 실측값).
- **N2 `\d{1,2}\s*$` 정밀도 14.3%** — 현 코퍼스에서 무해하나 규칙이 「맨숫자=문항번호」로 일반화되지
  않는다. 최소 수리 **후보안**(채택 시 별도 two-key): 이 대안을 무조건 발화가 아니라 **`sod` 상태에서만
  발화하는 복구 규칙**으로 좁힌다 — M6은 `sod` 상태에 갇힌 건이라 참 양성은 보존되고, 오탐 6건은
  전부 이미 `sel` 상태 지점이라 소거될 것으로 예상된다. **판정자는 이 최소 수리를 전수 실행하지
  않았으므로 검증된 안이 아니라 후보안이다** — 채택하려면 별도 라운드에서 `k/N` 을 측정할 것.
  현행 안으로도 GATE 3 개수축(42/42)이 fail-closed 그물을 이루므로 긴급하지 않다.
- **N3 `COMMAFIX` 의 이론적 오탐 `(3, 4점)`** — 코퍼스 0건이나 회귀 fixture를 GATE 0에 추가해
  향후 등장 시 판단을 강제하는 편이 안전하다.
- **N4 `prove.py` 의 `undetected` 가 이진값** — `0 if ok else 1` 이라 미검출 **개수**를 세지 않는다.
  `tools/textpatch.py --self-test` 의 `seeded=7 undetected=0` 규격에 맞춰 실제 개수로 바꿀 것.

---

# §4 open units

패킷 `<open_units>` U1~U5는 **전부 판정했다.** 미판정으로 남긴 unit은 없다.
아래는 이 판정이 **의도적으로 열어 둔 것**이며, 별도 라운드의 대상이다.

| 열린 항목 | 상태 | 다음 행동 주체 |
|---|---|---|
| U5 차단 수정 C-1~C-5 | 재라운드 필요 | 메인 루프가 반영안을 다시 상신 → tier-3 재판정(범위는 U5로 한정) |
| `ALLOW` 확장 (C-3) | **이 판정으로 선승인되지 않음** | 자를 재는 자의 개정이므로 사유와 함께 별도 two-key 상신 |
| §3 N1~N4 follow-up | 비차단 | 메인 루프, 별건 처리 가능 |

**`<out_of_scope>` 승계 확인** — 패킷 §6이 범위 밖으로 둔 4건은 이 판정도 다루지 않았다:
M5(`EX-science-20242F`, 전사 결함 유지) · GATE 3b sum-axis uncovered 34건(경고이며 mismatches=0) ·
F4 신규 24유닛의 카탈로그 반영 · 커밋.

---

# §5 무접촉·무커밋 확인 (판정 종료 시 실측)

```
$ sha256sum tools/measure_score_bands.py tools/regen_rubric_values.py analysis/catalog/DIFFICULTY_RUBRIC.md
23d6b87be9714ed6f6b24ccb6bbb8008957cdf0eba9f5cf997afbed6eee1a243 *tools/measure_score_bands.py
259bbfdfc3a6520efd7c2cf21c0d90ca1b24101e23db0d347300d9794a0ba975 *tools/regen_rubric_values.py
62674856f148e9ce4b2519044d7c410f9f9824823a5d8e8e9c458701bb27df21 *analysis/catalog/DIFFICULTY_RUBRIC.md
$ wc -c  ->  20662 / 21129 / 20294
$ git log --oneline -1  ->  941af21
```
**판정 개시 시점 해시와 종료 시점 해시가 동일하다** — 자 3종은 이 라운드에 한 바이트도 바뀌지 않았다.
HEAD `941af21` 유지, 커밋 없음.

정직한 부기 하나: `git status --porcelain` 은 ` M analysis/catalog/DIFFICULTY_RUBRIC.md`,
`?? tools/measure_score_bands.py`, `?? tools/regen_rubric_values.py` 를 보고한다. 즉 세 파일은
HEAD 대비 이미 작업 트리 상태였다(선행 라운드의 반영분 미커밋 / 도구 2종은 HEAD에 미추적).
**판정자가 만든 차이가 아니다** — 위 해시가 패킷 §1 동결 표와 일치하는 것이 그 증거다.

**원장 기입** — 손편집하지 않고 `tools/textpatch.py append_row` 로만 붙였다(원칙 12-b).
도구 검출력을 먼저 증명했다: `python tools/textpatch.py --self-test` → `seeded=10 undetected=0`, `exit=0`.

```
analysis/REV_LOG.md          header_cols=5 row_cols=5   736e13e8097447e8 (178326 B) -> c6c8ee4d5f79ed4c (182883 B)
output/260831/rev/_index.md  header_cols=8 row_cols=8   ccee82ad872443e5 ( 36663 B) -> 565b02206e189139 ( 41338 B)
```
기입 후 전수 검증(판정자 실측):
`REV_LOG` 표 행 107건 전부 5열 · `_index` 30건 전부 8열 · 양쪽 lone CR 0 · BOM 없음 · 개행 LF 유지.

(부기: 1차 시도는 `append_row` 에 리스트를 넘겨 `PatchError` 전에 예외로 죽었는데, 도구가
**쓰기 전 검증**하는 구조라 두 원장이 바이트 단위로 무손상이었다 — 실패 후 해시가
`736e13e8` · `ccee82ad` 로 기준선과 동일함을 확인하고 재시도했다.)

## history

- 260903 rev-arbiter: 골격 생성(전 unit `insufficient-evidence` 초기값).
- 260903 rev-arbiter: U1·U2·U3 확정(모두 approve/binding). 독립 재검증 §1-A~F 기재.
  U1 승인 범위를 「3줄」이 아니라 실측 4 hunk·24행으로 명시했고, C-1 오탐 6/7을 새로 발견해
  차단이 아닌 §3 N2로 강등했다(근거: 폐쇄 0/975 + GATE 3 개수축 42/42 커버리지).
- 260903 rev-arbiter: U4 approve(순서 구속 4항) · U5 **revise-required**(차단 수정 C-1~C-5) 확정.
  U5의 근거는 `tools/regen_rubric_values.py` L461 종료조건과 「지시가 붙은 것은 A축 36건뿐,
  역할 사각 18자리는 기대값 없음」이라는 실측이다 — 패킷이 제안한 수용기준
  `stale=0 lines=0 residual=0` 은 `ALLOW` 확장(별도 two-key) 없이는 도달 불가능하므로,
  그대로 승인하면 원칙 12-a가 지목한 우회로(F6 우산 산출물 / F9 눈금 손질)를 여는 자가 된다.
  C-4 작성 중 판정자가 미실측 기대 카운트(`stale=18`)를 적었다가 원칙 9-c-iii에 따라 스스로
  삭제하고 「실행 시 실측 + 잔여 자리의 목록 포함 여부」로 교체했다.
- 260903 rev-arbiter: 판정 종료 시 자 3종 해시 재측정 — 개시 시점과 동일(§5). 무커밋 확인.
