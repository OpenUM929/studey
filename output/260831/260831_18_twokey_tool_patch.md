---
doc: 260831_18 — 측정기 패치 two-key 상신 (BF1·BF2·BF3)
author: 메인 루프 (실행 레인)
grade: proposal — 실행 레인이므로 판정 등급 없음
date: 260902
ruling: output/260831/rev/260831_07_arbiter_ruling_parser.md (33420 B / a278415bb28384f4)
state: 승인 대기 — two-key(사용자 + rev-arbiter)
---

# 0. 왜 라이브 편집이 아니라 상신인가

판정 `260831_07` **BF4**: 「앞으로 자 수정은 **패치 제안으로 상신**하고 승인 후 반영한다 —
이번처럼 라이브 편집 후 사후 상신하지 않는다.」 그리고 **BF1·BF2의 owner는 `측정기 소유자 + two-key`**다.

따라서 이 라운드에서 **`tools/measure_score_bands.py`는 한 바이트도 고치지 않았다.**

| 파일 | 상태 |
|---|---|
| `tools/measure_score_bands.py` | **무접촉** 17438 B / `c6836602a55e0d0f` |
| `analysis/catalog/DIFFICULTY_RUBRIC.md` | **무접촉** 20058 B / `3a1b609b46855485` |
| 코퍼스 4건(EX-science-20242F·20252F, EX-social-20242M, EX-history-20242F) | **무접촉** (동결값 일치) |

패치는 샌드박스에만 있다 — `scratchpad/bf/measure_patched.py` (20662 B, CRLF 394 / lone LF 0,
원본 개행 규약 보존). 생성기는 `scratchpad/bf/apply_bf.py`이며 **손편집이 아니라 앵커 치환**이다
(원칙 12-b — 자는 코드가 만든다).

# 1. 패치 3건

## BF1 — GATE 0 를 `measure()` 와 같은 파이프라인으로 평가

종전 fixture는 `MARK.findall(JOIN.sub(...))`를 **멀티라인 원문에 통째로** 적용했다.
`MARK` 안의 `\s*`가 개행을 넘기 때문에, `JOIN`을 지워도 `line-broken` fixture가 통과했다.
즉 **JOIN의 검출기는 아무것도 검출하지 못하고 있었다**(판정문 Q2-b, 재현 완료).

공유 경로 3개를 신설하고 `measure()`와 GATE 0가 **둘 다** 그것을 쓴다.

```python
def prep(t):
    return JOIN.sub(r'[\1점', SPACEFIX.sub(r'[\1.\2점', t))

def line_marks(l):
    return [] if ANNOT.match(l) else MARK.findall(l)

def extract_marks(text):
    out = []
    for l in prep(text).split('\n'):
        out += line_marks(l)
    return out
```

소스 주석의 거짓 문구(「Both 260902 parser defects are planted here」)도 함께 정정한다(FU5).

## BF2 — M6 수리 (`EX-history-20242F`)

두 결함이 **개수축에서 정확히 상쇄**돼 GATE 3이 침묵했다: `> [판독]` 주석행이 본문 표식을
재인용해 +1, `[3 .8점 ]`(숫자 내부 공백)이 −1.

```python
SPACEFIX= re.compile(r'\[[^\S\n]*([0-9]+)[^\S\n]*\.[^\S\n]*([0-9]+)[^\S\n]*점')
ANNOT   = re.compile(r'^\s*>')
```

GATE 0 fixture 2종 추가 — `annotation-quote`, `space-in-number`.

## BF3 — GATE 3 합계축 커버리지

**판정문의 설명보다 나쁘다.** 판정문은 L426이 「첫 60행 창 밖」이라 했으나, 실측하면
`DECL_SUM`은 **창을 무제한으로 넓혀도 이 파일에서 0건 매칭**이다 — `선택형 합계`라는 문자열
자체가 없고 전사본은 `선택형 80.0점(3.5+3.7+...)`으로 적었다.

```
DECL_SUM.findall(전문)  ->  []
'선택형 합계' in 전문    ->  False
```

**창만 넓히는 수리는 fail-open이다.** 패턴도 함께 넓히고, 별도 커버리지 축으로 노출한다.

```python
DECL_ANY = re.compile(r'선택형(?:\s*합계)?\s*([0-9]+(?:\.[0-9]+)?)\s*점')
```

# 2. 수용기준 실측 (파이프 없이 exit 확인)

```
python scratchpad/bf/measure_patched.py     ->  exit=1   (M5 잔존, fail-closed 유지)
```

| 기준 | 요구 | 실측 | 판정 |
|---|---|---|---|
| BF1 GATE 0 | `undetected=0` + 경고 0줄 | `planted=7 undetected=0` / `[GATE 0 PASS]` | PASS |
| BF1 JOIN 제거 사본 | `undetected >= 1` | **`undetected=1`**, 울린 fixture `line-broken` | PASS |
| BF2 대상 유닛 | `n=21 decl=21 sum=80.0` | `EX-history-20242F F body 21 21 **80.0**` | PASS |
| BF2 GATE 1 앵커 | `undetected=0` (10/10) | `[GATE 1 PASS] undetected=0` | PASS |
| BF2 전수 변동 | 26유닛 중 1건뿐 | diff **1행**(79.8 -> 80.0), 그 외 25유닛 무변동 | PASS |
| BF2 GATE 3 | `mismatches=1` 유지 | `mismatches=1` (M5 단독) | PASS |
| BF3 커버리지 | 카운트 출력 + 미대조 `[WARN]` | `sum-axis coverage=8/22 uncovered=14 mismatches=1` | PASS |

## 검출력 실증 (원칙 12-d — 수정 4종을 각각 지우고 GATE 0 관찰)

| 지운 수정 | `undetected` | 울린 fixture |
|---|---|---|
| `JOIN` (M3 수리) | **1** | `line-broken` |
| `SPACEFIX` (M6-b 수리) | **1** | `space-in-number` |
| `ANNOT` (M6-a 수리) | **1** | `annotation-quote` |
| `MARK` 부정 lookahead (M2 수리) | **2** | `legend-equals`, `legend-per` |

네 수정 모두 자기 검출기를 갖는다. 종전에는 이 표에서 `JOIN` 칸이 **0**이었다.

# 3. 이 라운드의 신규 발견 — 「수리가 다른 수리의 검출기를 가린다」

BF2의 `SPACEFIX`를 처음에 `\s*`로 썼더니 **JOIN 제거 시에도 `undetected=0`** 이 나왔다.
`\s*`가 개행을 넘어 `[3.2\n점`을 스스로 이어붙여 **JOIN의 일을 대신했기** 때문이다.
결과적으로 BF1이 되살리려던 바로 그 검출기를 BF2가 다시 죽였다.

`[^\S\n]`(개행 아닌 공백)으로 한정해 해소했다. 일반화하면:

> **수리는 자기 범위 밖으로 새면 안 된다.** 다른 결함까지 우연히 덮는 수리는
> 그 결함의 검출기를 무력화하고, 원래 결함이 되돌아와도 게이트가 침묵한다.
> 새 수리를 넣을 때는 **기존 수정들을 하나씩 지워 보아 검출력이 유지되는지** 확인한다.

이 절차를 위 §2 검출력 표로 상시화할 것을 제안한다(비구속).

# 4. Q3(자 재서명)에 미치는 영향 — 판정자 예측과 일치

| 값 | 현행(BF2 전) | BF2 후 |
|---|---|---|
| `EX-history-20242F` 선택형 합 | 79.8 | **80.0** |
| T2 | 158 (31.0%) | **157 (30.8%)** |
| T3 | 193 (37.8%) | **194 (38.0%)** |
| T1 / T4 / ALL | 24 / 113 / `n=510 fit=488 95.7%` | 변동 없음 |

판정문 Q3의 「M6 수리만으로 `T2 158->157`, `T3 193->194`」 예측이 **정확히 재현**됐다.
Q3 보류 판단이 옳았다 — 지금 재서명했다면 이미 틀린 값을 서명할 뻔했다.
**BF5(M5) 해소 후 최종 재실행값으로 재서명해야 한다.**

# 5. 승인 요청 (체크박스 — 원칙 8)

- [ ] **A1** BF1 패치를 `tools/measure_score_bands.py`에 반영한다
- [ ] **A2** BF2 패치를 반영한다 (`SPACEFIX`는 `[^\S\n]` 한정형으로)
- [ ] **A3** BF3 패치를 반영한다 (패턴 확장 + 커버리지 축 노출)
- [ ] **A4** 반영 후 `analysis/REV_LOG.md`에 **BF4 재동결 행**을 남긴다
      (`f60455c6fc0d8ca9` 14731 B -> `c6836602a55e0d0f` 17438 B -> 반영본 해시)
- [ ] **A5** §3의 「수정 제거 검출력 표」를 매 측정기 변경 시 상시 절차로 채택한다 (비구속)

**두 열쇠**: 사용자 승인 + `rev-arbiter` 확인. 어느 한쪽만으로는 반영하지 않는다(원칙 12-c).
승인 전까지 새 수치(`T2 157` 등)는 **어떤 정본에도 인용하지 않는다**.

# 6. 이 문서가 건드리지 않은 것

`tools/` · `analysis/catalog/` · `corpus/` · `_01_*` 전부 무접촉. 커밋 없음(HEAD `941af21`).
BF5는 `type-extractor` 소관이므로 여기에 포함하지 않는다.
