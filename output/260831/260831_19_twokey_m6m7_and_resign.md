---
doc: 260831_19 — 측정기 파서 결함 M6·M7 수리 + 자 재서명 two-key 상신
author: 메인 루프 (실행 레인)
grade: proposal — 실행 레인이므로 판정 등급 없음 (REV_GUIDE §5 마지막 행)
date: 260903
thread: 260831 (자·측정기 계열). 선행 판정 `260831_07`(파서) · `260831_08`(재서명)
state: 승인 대기 — two-key(사용자 + `rev-arbiter`)
user_key: **turned** — 사용자 260903 "모두 마무리하고 알려줘"(직전 턴에서 이 2건이 two-key 대상임을
  명시해 보고한 뒤 받은 지시). 남은 것은 `rev-arbiter` 열쇠 하나다.
---

# 0. 왜 라이브 편집이 아니라 상신인가

판정 `260831_07` **BF4**: 「앞으로 자 수정은 **패치 제안으로 상신**하고 승인 후 반영한다.」
`REV_GUIDE` §5 two-key 대상 목록에 `tools/measure_score_bands.py`·`tools/regen_rubric_values.py`·
`analysis/catalog/DIFFICULTY_RUBRIC.md` 3종이 명시돼 있다.

**이 라운드에서 세 파일 모두 한 바이트도 고치지 않았다.** 패치는 샌드박스에만 있다.

| 파일 | 상태 |
|---|---|
| `tools/measure_score_bands.py` | **무접촉** 20662 B / `23d6b87be9714ed6` |
| `tools/regen_rubric_values.py` | **무접촉** 21129 B / `259bbfdfc3a6520e` |
| `analysis/catalog/DIFFICULTY_RUBRIC.md` | **무접촉** 20294 B / `62674856f148e9ce` |

패치 생성기는 `scratchpad/sb/mkpatch.py`이며 **손편집이 아니라 앵커 치환**이다(원칙 12-b).
원본이 CRLF(394행 / lone LF 0)이므로 앵커 대조는 LF 정규화본에서 하고 되쓸 때 CRLF로 복원한다.

> **선행 자기정정.** 직전 턴에 이 두 유닛의 원인을 사용자에게 보고하면서 **둘 다 틀리게 말했다.**
> `EX-english-20251M`을 「서답형이 선택형 사이에 끼어 마지막 구간 전환 뒤 1건 흡수」라고 했으나
> 실제 흡수 지점은 `[ 서답형3(단답) ]`(L253)이 아니라 **L145의 맨숫자 `10`** 이고,
> `EX-korean-20241M`은 「`MARK` 정규식이 못 본다」까지만 맞고 그 원인이 소수점 자리의 쉼표라는
> 것을 이 라운드에서야 실측했다. 아래 §1은 전부 이번 라운드 실행 출력이다.

---

# 1. `<frozen_inputs>`

| path | bytes | sha256 | role |
|---|---|---|---|
| `tools/measure_score_bands.py` | 20662 | `23d6b87be9714ed6f6b24ccb6bbb8008957cdf0eba9f5cf997afbed6eee1a243` | ruler |
| `tools/regen_rubric_values.py` | 21129 | `259bbfdfc3a6520efd7c2cf21c0d90ca1b24101e23db0d347300d9794a0ba975` | ruler |
| `analysis/catalog/DIFFICULTY_RUBRIC.md` | 20294 | `62674856f148e9ce4b2519044d7c410f9f9824823a5d8e8e9c458701bb27df21` | ruler |
| `corpus/EX-english-20251M/transcript.md` | 45525 | `67e7fc3da0ee0443b7f0680d744f3458be2dd4481aea5cfacef753451ca78cd8` | source |
| `corpus/EX-korean-20241M/transcript.md` | 67253 | `b7ae7b4af7c8c5080d613cd60c77d1e8056facd2d0aa44a50ca2141b66c6d665` | source |
| `output/260831/rev/260831_07_arbiter_ruling_parser.md` | 33420 | `a278415bb28384f4604a5e83a36a032dc7047658eab868611605dbc0d96626fa` | evidence |
| `output/260831/rev/260831_08_arbiter_ruling_resign.md` | 28832 | `f1e50d682b34444cb5f2a0fe7ecf593135f108d6cb74ea9b1e0f1832d651697d` | evidence |
| `output/260831/260831_18_twokey_tool_patch.md` | 7275 | `17bf5503042d07a14f1014b5454f10f6f6b34fda6ebb5393175d863d616b3196` | evidence |
| `scratchpad/sb/patched.py` | 21969 | `0cf91284e2c1f7b1be4d94a09d641996614d65fa88fdf8444b9f9daa3958fe24` | output (제안 패치) |
| `scratchpad/sb/mkpatch.py` | 4490 | `5bcabd7c800d2cf5cf5ace201ffb5a02873f4be8414d328557aa877d1333da4a` | output (생성기) |
| `scratchpad/sb/prove.py` | 1638 | `a0a16d90330345371646b6cd1e82fa2736e5239a0b9d4e4ac49507ae872e6ce9` | output (검출력 증명기) |

**`<excluded>`** — 본문이 경로로 지목하지만 동결 표에 넣지 않은 것과 그 사유:

- `corpus/EX-*/transcript.md` 나머지 49건 — 폐쇄 시험의 **모집단**이지 이 판정의 입력이 아니다.
  개별 해시 대신 폐쇄 결과(§3 U2)로 대표한다. 모집단 카운트는 §3에 측정 경계와 함께 적었다.
- `analysis/REV_GUIDE.md` — 규격 참조원이며 이 라운드에서 개정 대상이 아니다.

측정 시점: 이 패킷을 닫기 직전. 패킷 자신은 모집단에 들지 않는다(§6-b (f-1)).

---

# 2. 결함 2건 — 원인과 증거

## M6 — `EX-english-20251M` (선언 23 / 추출 22)

HWP 추출이 문항 번호 `10.`에서 **마침표를 떼어내 번호만 한 줄에 남겼다.**

```
$ sed -n '150,155p' corpus/EX-english-20251M/transcript.md | od -c
   i n s u l a t i n g \n <...한글...> ? \n [ 3 . 3 \n 점 \n ] \n S o m e ...
$ awk 'NR==145' corpus/EX-english-20251M/transcript.md
10
```

`TO_SEL = ^\s*(?:#{1,4}\s*선택형|\*{0,2}\d+\s*\.\s*\S)` 은 **마침표를 요구**하므로 L145에서
발화하지 않는다. 직전 L130 `[ 서답형2(서술) ]` 이 상태를 `sod`로 넘긴 뒤 되돌아오지 않아,
문항 10의 배점이 서답형 구간에 흡수된다.

`JOIN`은 정상 작동한다 — 상태 재현 출력에서 L152가 `[3.3점` 으로 합쳐진 것을 확인했다:

```
L130  SEL=False SOD=True  MARK=['5']    [ 서답형2(서술) ] ...
L152  SEL=False SOD=False MARK=['3.3']  [3.3점
```

즉 **표식 추출이 아니라 구간 귀속의 결함**이다. 표식 총수는 이미 맞고 있었다.

## M7 — `EX-korean-20241M` (선언 24 / 추출 23)

원본 시험지 오타다 — 소수점 자리에 **쉼표**가 찍혔다.

```
$ grep -n '[0-9],[0-9]\s*점' corpus/EX-korean-20241M/transcript.md
149:7. (가)와 (나)의 관점으로 <보기>를 설명한 것으로 가장 적절한 것 은?(2,8점)
```

`MARK = [\[(]\s*([0-9]+(?:\.[0-9]+)?)\s*점(?!\s*(?:=|당))` 은 `(2` 다음에 `점`을 요구하므로
`,8점` 에서 끊겨 **표식 자체를 못 본다**.

**이것이 `2.8`이라는 근거는 두 축이 독립으로 일치한다:**

| 축 | 값 |
|---|---|
| 문항 수 | 현행 23 + 1 = **24** = 인쇄 선언 `선택형( 24 )문항` |
| 선택형 총점 | 현행 57.2 + 2.8 = **60.0** = 이 학교 선택형 총점 관행(`VALIDATE`에 `F(60)` 다수) |

한 축만 맞으면 우연일 수 있으나, 개수와 총점이 **동시에** 정수 착지하는 값은 2.8뿐이다.

## 귀속 판단

두 건 다 **고치면 인쇄 선언에 정확히 착지**한다 → 판정 `260831_07`의 기준으로 **파서 결함
(M계열)**이며 전사 결함이 아니다. `260831_04` F3의 `type-extractor` 일괄 귀속에서 이 2건을
분리해 줄 것을 요청한다(U3). **M5(`EX-science-20242F` 요약행 78.8/21.2 vs 열거 80.0/20.0)는
그대로 전사 결함으로 남는다** — 이 패킷의 대상이 아니다.

---

# 3. 제안 패치 — 3줄

```diff
+ COMMAFIX= re.compile(r'([\[(][^\S\n]*[0-9])[^\S\n]*,[^\S\n]*([0-9][^\S\n]*점)')

- TO_SEL  = re.compile(r'^\s*(?:#{1,4}\s*선택형|\*{0,2}\d+\s*\.\s*\S)')
+ TO_SEL  = re.compile(r'^\s*(?:#{1,4}\s*선택형|\*{0,2}\d+\s*\.\s*\S|\d{1,2}\s*$)')

-     return JOIN.sub(r'[\1점', SPACEFIX.sub(r'[\1.\2점', t))
+     return JOIN.sub(r'[\1점', SPACEFIX.sub(r'[\1.\2점', COMMAFIX.sub(r'\1.\2', t)))
```

`COMMAFIX`가 좁은 이유: 여는 괄호 바로 뒤 **한 자리** 숫자 + 쉼표 + **한 자리** 숫자 + `점`.
천단위 구분(`1,234`)은 쉼표 뒤가 세 자리라 걸리지 않고, `[^\S\n]`이라 줄바꿈을 넘지 않는다
(BF2가 `SPACEFIX`에서 겪은 「수리가 다른 수리의 검출기를 가리는」 사고 방지).

## 위험면적 실측 — `\d{1,2}\s*$` 가 과잉 발화하는가

```
$ grep -rh '^[[:space:]]*[0-9]\{1,2\}[[:space:]]*$' corpus/EX-*/transcript.md | wc -l
7
```

전 코퍼스 51유닛에 **맨숫자 줄은 7개뿐**이고, 그중 4유닛에 분포한다
(`EX-korean-20251M` 3 · `EX-science-20252F` 2 · `EX-korean-20241F` 1 · `EX-english-20251M` 1).

---

# 4. `<units>` — 판정 요청

## U1 — M6·M7을 파서 결함으로 인정하고 위 3줄 패치를 승인하는가

- `verdict enum`: `approve | revise-required | reject | insufficient-evidence`
- `evidence`: §2 원문 인용 + 아래 재현
- `reproduce:` `python scratchpad/sb/patched.py > /dev/null 2>&1 ; echo "exit=$?"` → 기대 `exit=0`
- `measured`: yes — §2·§3의 모든 리터럴은 이번 라운드 명령 출력이다

## U2 — 폐쇄: 패치가 대상 2유닛 **밖**을 움직이지 않는가

`--per-item` 의 유닛별 `(n, 선택형 총점)`을 base와 patched에서 대조했다.

```
base units=40  patched units=42
only in patched: ['EX-english-20251M', 'EX-korean-20241M']
only in base   : []
공통 40 중 이동 0
```

**`k/N` = 0/40** — 공통 40유닛 중 개수도 총점도 바뀐 유닛이 **0건**이다.
40 → 42는 `EXCL = set(mism) - set(sumonly)`(measure_score_bands.py L252)가 GATE 3 불일치
유닛을 집계에서 빼기 때문이며, 수리로 불일치가 사라지면서 두 유닛이 **모집단에 복귀**한다.

- `reproduce:` `python scratchpad/sb/base.py --per-item` 과 `python scratchpad/sb/patched.py --per-item`
  의 `mean unit price` 행 대조
- `measured`: yes

## U3 — 검출력: 심어둔 fixture가 실제로 발화하는가 (원칙 12-d)

수리를 하나씩 **되돌려** fixture가 발화하는지 확인했다. 수리 전후 모두 통과하는 fixture는
검출기가 아니라 장식이다.

```
$ python scratchpad/sb/prove.py
M7 COMMAFIX 무력화          exit=1  발화=2
      [FAIL] fixture comma-decimal  got=[] want=['2.8']
      planted=9 undetected=1
M6 맨숫자 대안 제거             exit=1  발화=3
      [FAIL] fixture bare-number      TO_SEL=False want=True
      [FAIL] fixture bare-number-pad  TO_SEL=False want=True
      planted-state=6 undetected=2
---
knockout=2  undetected=0
prove_exit=0
```

fixture는 거짓 양성 방지 자리를 함께 둔다 — `comma-thousands`(`(1,234점=합계)` → `[]`),
`prose-number`(`약 10 명이 참여했다` → False), `three-digit`(`2024` → False),
`sod-header`(`[ 서답형1(서술) ] 쓰시오` → False).

M6는 상태 전이 규칙이라 `extract_marks()` 경로 밖이므로 **GATE 0s**를 신설해 `TO_SEL`을
직접 건다. 이 신설 자체가 자의 개정이므로 U1과 함께 판정 대상이다.

- `reproduce:` `python scratchpad/sb/prove.py ; echo "exit=$?"` → 기대 `exit=0`
- `measured`: yes

## U4 — 자 재서명(two-key)을 지금 개시하는가

수리 후 자 값을 **샌드박스 재생성기**로 미리 산출했다(`regen_preview.py` = 정본 regen의
`TOOL` 한 줄만 patched로 바꾼 사본, 정본 무접촉).

| 항목 | 현행 자 본문 | 수리 전 실측 | **수리 후 실측** |
|---|---|---|---|
| 전수 폐쇄 | 488/510 = 95.7% | 895/935 = 95.7% | **940/982 = 95.7%** |
| 계층 최저 | — | 89.6% (M-2025) | **89.7% (M-2025)** |
| 연도 hold-out 최저 | 92.1% | 92.0% | **92.0%** |
| 유닛 | 22유닛 | 50 · 선택형 42 | **50 · 선택형 42** |
| T1/T2/T3/T4 100환산 | 24/32/… | 5/34/39/22 | **5/33/39/23** |

**요지: 밴드 임계값은 움직이지 않는다.** `r ∈ [0.80, 1.20]` 의 폐쇄율이 모집단이 510 → 982로
**1.9배가 되는 동안 95.7%로 동일**하다. 재서명은 자의 판단 기준을 바꾸는 것이 아니라
**인용 수치를 현행 모집단에 맞추는 것**이다.

- `reproduce:` `python scratchpad/sb/regen_preview.py` (정본은 `python tools/regen_rubric_values.py`)
- `measured`: yes
- 현행 정본 게이트 상태(파이프 없이 실측):
  `python tools/regen_rubric_values.py > /dev/null 2>&1 ; echo "exit=$?"` → `exit=1`
  `stale=57 lines=28 residual=18` · `python tools/check_assurance_contract.py` → `3 failure(s)`, `exit=1`

## U5 — 반영 방법: 자 본문을 무엇이 고치는가

원칙 12-b는 「자는 손이 아니라 코드가 만든다」인데 `regen_rubric_values.py`는 **읽기 전용**이라
값을 써 주지 않는다. 제안: 재생성기 출력의 `:행번호 [역할] 현재 -> 기대` 28행을 입력으로
`tools/textpatch.py patch` 를 돌려 기계적으로 반영하고, 반영 후 `regen` 재실행이
`stale=0 lines=0 residual=0`을 내는 것을 수용기준으로 삼는다.

- `verdict enum`: `approve | revise-required | reject`
- 대안(판정자가 선택 가능): (a) 위 제안 (b) `regen`에 `--write` 추가 — 단 이는 재생성기 자체의
  개정이므로 별도 two-key가 필요하다 (c) 반영 주체를 사용자로 한정
- `measured`: yes (`stale=57 lines=28 residual=18` 은 이번 라운드 출력)

---

# 5. `<actor_grade>`

| 배우 | 등급 | 근거 |
|---|---|---|
| 메인 루프(이 문서 작성) | **proposal** — `binding` 불가 | REV_GUIDE §5 마지막 행: 대행 산출물은 제안 등급. 자기 승인 금지 |
| `rev-arbiter` | **binding** | fresh context · 동일 저장소 · tier-3. §6-d (3) 배우표 |
| 사용자 | **binding** (two-key 나머지 한쪽) | 260903 지시로 **이미 행사됨** |

---

# 6. `<open_units>` / `<out_of_scope>`

**`<open_units>`** (이 라운드 시작 시점): U1 · U2 · U3 · U4 · U5.
선행 `260831_17`의 Q1~Q4는 판정 `260831_07`·`260831_08`로 닫혔다.

**`<out_of_scope>`** — 이번 라운드에서 판정하지 않는다:

- **M5** (`EX-science-20242F` 요약행 78.8/21.2 vs 열거 80.0/20.0) — 전사 결함으로 확정돼 있고
  소관은 `type-extractor`다. 이 패킷은 파서 결함 2건만 다룬다.
- **GATE 3b sum-axis uncovered 34건** — 경고이지 불일치가 아니며(`mismatches=0`), 별건이다.
- **F4로 새로 들어온 24유닛의 카탈로그 반영(`분석완료` 표시)** — 사용자가 요청한 범위 밖이다.
- **커밋** — HEAD `941af21` 고정. 이 라운드에서 커밋하지 않는다.

---

# 7. `<constraints>`

- **write surface**: 판정자는 `*_ruling.md` + `REV_LOG` + 자기 WIP. 자 3종 직접 편집 금지.
- **무커밋**: HEAD `941af21`.
- **원장은 append-only**: `analysis/REV_LOG.md`(5열) · `output/260831/rev/_index.md`(8열).
  행 추가는 `tools/textpatch.py append_row` 로만 한다(손편집 금지 — 260902 CRLF 3회 재발).
- **자 무접촉 검증 의무**: 판정 전후로 아래 세 해시가 불변임을 확인할 수 있어야 한다 —
  `23d6b87be9714ed6` · `259bbfdfc3a6520e` · `62674856f148e9ce`.

# 8. `<reply>`

`output/260831/rev/260831_09_arbiter_ruling_m6m7_resign.md`
형식: REV_GUIDE §6-d (2) 고정 절 + §0 7열 요약표(`unit | verdict | grade | evidence |
measured | closure | note`).
