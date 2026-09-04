---
doc: 260831_17 결정요청 — GATE 3 잔여 3건의 근본 원인 재배정 및 자 재서명 요청
author: 메인 루프 (실행 레인 — 판정 등급 없음)
target_actor: rev-arbiter
date: 260902
round: 5
spec: analysis/REV_GUIDE.md §6-d (1)
---

# 0. 한 줄 요약

판정 `260831_04` F3이 **전사 결함 3건(M2·M3·M5, 소유 `type-extractor`)** 으로 배정한 GATE 3
mismatch 중 **2건은 전사 결함이 아니라 측정기 파서 결함**이었다. 파서를 고치자 두 유닛이
인쇄 선언값에 정확히 착지했고, 조용히 버려지던 **48문항이 모집단에 복귀**하면서 서명된 자
`DIFFICULTY_RUBRIC.md`의 수치가 전부 stale이 됐다. 자는 two-key이므로 상신한다.

# 1. `<frozen_inputs>`

측정 시점: **이 패킷 본문 작성 직전**(§6-b (f-1)). 패킷 자신은 아직 존재하지 않으므로 표에 없다.

| path | bytes | sha256(16) | role |
|---|---|---|---|
| `tools/measure_score_bands.py` | 17438 | `c6836602a55e0d0f` | derived (260902 수정본, 판정 대상) |
| `analysis/catalog/DIFFICULTY_RUBRIC.md` | 20058 | `3a1b609b46855485` | ruler (무수정 — 확인용) |
| `corpus/EX-science-20242F/transcript.md` | 39144 | `ef85df2dfbe6bf3c` | source (M5 대상) |
| `corpus/EX-science-20252F/transcript.md` | 25304 | `8cf3a26aafc7512a` | source (M3 대상) |
| `corpus/EX-social-20242M/transcript.md` | 45054 | `3e7fc678538e0ed0` | source (M2 대상) |
| `output/260831/rev/260831_05_arbiter_ruling_refreeze.md` | 38294 | `6c93e096b986e9f6` | evidence (U5 지문 동결) |
| `output/260831/rev/260831_06_arbiter_ruling_gates.md` | 32690 | `ad62f9b99a679054` | evidence (직전 판정) |
| `analysis/REV_GUIDE.md` | 43857 | `f361f43150927668` | evidence (§6-d 규격) |
| `analysis/wip/mainloop_260902_m2m3m5_rootcause.md` | 14093 | `bee419aa16681b88` | evidence (본 라운드 WIP) |

> **드리프트 자기신고 (260902 재측정)** — 이 패킷은 한 차례 발주됐으나 수신 측이 429(session limit)로 
> 즉사해 판정이 생산되지 않았다. 그 사이 **내 WIP에 §사고 절을 추가**해 위 행이 `10236 / c4bd370abd34ee2a`에서
> `14093 / bee419aa16681b88`로 바뀌었다. **표를 재측정해 갱신했고, 나머지 9건은 전건 불변이다**
> (`drift=1`, 유일 변경자 = 작성자 본인). 패킷 본문의 Q1~Q4 내용은 무수정이다.

`<excluded>`
- `output/260831/260831_*.md` 나머지 27건 · `output/260831/rev/*` 나머지 — 본 라운드가 **본문을
  읽지 않는다**. 경로 문자열로도 인용하지 않는다.
- `analysis/REV_LOG.md` · `output/260831/rev/_index.md` — **이 라운드가 행을 덧붙일 대상**이므로
  해시가 필연적으로 바뀐다. 동결 불가(§6-b (f-1) 자기참조 모집단).
- `analysis/wip/` 타 배우 WIP 6건 — 배타 소유, 본 라운드 무접촉.
- 판정 `260831_04` 원문 — F3의 귀속 문장만 인용하며, 그 인용은 아래 `reproduce:`로 재현 가능하다.

# 2. `<units>`

## Q1 — M2·M3의 소유 재배정은 타당한가?

**질문**: `EX-social-20242M`(선언 24 vs 추출 26)과 `EX-science-20252F`(선언 24 vs 추출 20)는
전사 결함인가, 측정기 파서 결함인가? 판정 `260831_04` F3의 `owner: type-extractor` 귀속을
**M5 단독으로 축소**하는 정정을 승인하는가?

`verdict enum`: `승인(파서 결함으로 재배정)` | `기각(전사 결함 유지)` | `부분승인(unit별 분리)`

**근거**
- M2: 지도 범례 2건이 배점으로 오인됐다. `transcript.md:34` = `(1점=소규모 단위)`,
  `:121` = `(1점당 10만명)` — 「점」의 **dot** 뜻. 2건 제외 시 `26-2=24` = 인쇄 선언 24.
- M3: 배점 표식이 HWP 추출에서 3줄로 쪼개져(`[3.2` / `점` / `]`) 행 단위 정규식이 못 봤다.
  L82·L95·L180·L206 4건. 복원 시 개수 `20+4=24` = 선언 24, 배점 `66.3+13.7=80.0`
  = `100 - 단답형 9문항 20.0`. **개수와 배점 두 축이 동시에 착지**한다.

`reproduce:` (스크립트를 `/tmp/q1.py`로 저장 후 `python /tmp/q1.py`)

```python
import re
MARK_OLD = re.compile(r'[\[(]\s*([0-9]+(?:\.[0-9]+)?)\s*점')
MARK_NEW = re.compile(r'[\[(]\s*([0-9]+(?:\.[0-9]+)?)\s*점(?!\s*(?:=|당))')
JOIN     = re.compile(r'\[\s*([0-9]+(?:\.[0-9]+)?)\s*\n\s*점')
for u, decl in [('EX-social-20242M', 24), ('EX-science-20252F', 24)]:
    t = open('corpus/%s/transcript.md' % u, encoding='utf-8').read()
    old = len(MARK_OLD.findall(t))
    new = len(MARK_NEW.findall(JOIN.sub(r'[\1점', t)))
    print(u, 'old=%d new=%d declared=%d' % (old, new, decl))
# 기대: EX-social-20242M old=26 new=24 declared=24
#       EX-science-20252F old=20 new=24 declared=24
```

## Q2 — 측정기 수정 2건 + fixture 1건을 승인하는가?

**질문**: `tools/measure_score_bands.py`의 (a) `MARK` 부정 lookahead `(?!\s*(?:=|당))`
(b) `JOIN` 줄바꿈 결합 전처리 (c) `GATE 0` fixture 5종 — 이 셋을 승인하는가?
특히 **실행 레인이 자기 측정기를 고쳐 실패 게이트를 3→1로 줄인 것**이 원칙 12가 금지하는
자기 자 손질에 해당하는가?

`verdict enum`: `승인` | `수정요구` | `기각(원복 후 타 배우 이관)`

**자기신고**: 나는 측정기 소유자이고, 실패하던 게이트를 그 측정기를 고쳐 완화했다. 형태만 보면
F9와 같은 자리에 있다. 판정자가 검증할 반증 3가지를 남긴다.

1. 두 수정 모두 **선언값에 정확히 착지**한다 — 눈금을 맞춘 것이 아니라 도착한 것이다.
2. **GATE 1 앵커 10건 전건 무변화**(tier-3 fresh context 확정값). 특히 줄바꿈 표식을 4건 가진
   `EX-history-20252M`은 그 4건이 전부 **서답형 구간**이라 `sel`이 `n=20 sum=40.0`으로 불변이다.
3. 게이트는 여전히 **fail-closed(exit 1)** 이다. 통과가 목적이었다면 M5도 함께 사라졌을 것이다.

```
reproduce:
python tools/measure_score_bands.py > /dev/null 2>&1 ; echo "exit=$?"
# 기대: exit=1
python tools/measure_score_bands.py 2>&1 | grep -E "GATE 0 PASS|GATE 1 PASS|mismatches=|excluded from"
# 기대 4줄:
#   [GATE 0 PASS] undetected=0
#   [GATE 1 PASS] undetected=0
#   mismatches=1
#   excluded from aggregate: none
```

## Q3 — 자 `DIFFICULTY_RUBRIC.md` 재서명(two-key)을 개시하는가?

**질문**: 파서 수정으로 모집단이 **462 → 510문항(20 → 22유닛)** 이 되어 서명 블록 내부
(`:21`)를 포함한 수치가 stale이다. 재서명 라운드를 여는가? 연다면 **누가 값을 만드는가**?

`verdict enum`: `개시(메인 루프가 재생성, 판정자+사용자 two-key로 확정)` |
`개시(타 배우가 재생성)` | `보류(M5 해소 후 일괄)` | `기각`

| 항목 | 서명값 | 260902 실측 | 위치 |
|---|---|---|---|
| 전수 폐쇄 | 440/462 = 95.2% | **488/510 = 95.7%** | `:21` **서명 블록 안** |
| 범위 라벨 | 20유닛 462문항 | **22유닛 510문항** | `:22` `:166` `:169` `:223` `:237` `:240` |
| F-2025 | n=116 fit=112 96.6% | **n=140 fit=136 97.1%** | §6 |
| M-2024 | n=96 fit=96 100.0% | **n=120 fit=120 100.0%** | §6 |
| T1/T2/T3/T4 | 23 5.0% / 142 30.7% / 175 37.9% / 100 21.6% | **24 4.7% / 158 31.0% / 193 37.8% / 113 22.2%** | §6 `:169` |
| 밴드 밖 | 22 4.8% | **22 4.3%** | §6 |
| 측정기 해시 인용 | `f60455c6fc0d8ca9`(14731 B) | **`c6836602a55e0d0f`(17438 B)** | 자 이력 · REV_LOG |

**나는 자를 건드리지 않았다** — 파일 `3a1b609b46855485` / 20058 B 불변,
서명 블록 지문 **68행 / `a204f3412cf900b5`** 불변(U5 동결 명령 원문으로 재측정).

```
reproduce:
python -c "import hashlib;b=open('analysis/catalog/DIFFICULTY_RUBRIC.md','rb').read();print(len(b),hashlib.sha256(b).hexdigest()[:16])"
# 기대: 20058 3a1b609b46855485

{ awk '/^# 1\. 배점/,/^# 2\. 난이도/' analysis/catalog/DIFFICULTY_RUBRIC.md | sed '$d'; \
  awk '/^### Tier 요약표/,/^# 4\./'   analysis/catalog/DIFFICULTY_RUBRIC.md | sed '$d'; } > /tmp/fp17.txt
wc -l < /tmp/fp17.txt ; sha256sum /tmp/fp17.txt | cut -c1-16
# 기대: 68 / a204f3412cf900b5

python tools/measure_score_bands.py 2>&1 | grep -E "^ALL|^T[1-4]|outside band"
# 기대: ALL   n=510  fit=488 = 95.7%  residual=22
```

## Q4 — M5 실행 지시를 지금 내보내는가?

**질문**: M5(`corpus/EX-science-20242F/transcript.md:17`의 요약 `78.8/21.2` → `80.0/20.0`)는
전사 결함으로 확정된 유일 건이다. `type-extractor` 실행 지시(§6-c `[OC 지시]`)를 이 판정과
함께 내보내는가, 아니면 Q3 재서명 확정 후로 미루는가?

`verdict enum`: `즉시 발행` | `Q3 이후로 보류` | `수정요구`

`reproduce:` (스크립트를 `/tmp/q4.py`로 저장 후 `python /tmp/q4.py`)

```python
from fractions import Fraction as F
sel = "3.5+3.4+3.0+3.2+3.6+3.3+3.0+3.3+3.2+3.4+3.5+3.6+3.4+3.2+3.0+3.3+3.5+3.6+3.0+3.2+3.4+3.5+3.3+3.6"
sod = "3+2+2+3+2+3+2+3"
for name, s in (('sel', sel), ('sod', sod)):
    v = [F(x) for x in s.split('+')]
    print(name, len(v), float(sum(v)))
# 기대: sel 24 80.0 / sod 8 20.0
# 두 값은 transcript.md:17이 같은 줄에 나열한 개별 배점이다. 표지 인쇄 100점과 합치하고,
# 같은 줄의 요약 선언 78.8/21.2와는 불합치한다.
```

# 3. `<actor_grade>`

- 요청 측(본 문서 작성자) = **메인 루프 / 실행 레인 — 판정 등급 없음**. 자기 산출물이므로 등급 부여 불가.
- 수신 측 `rev-arbiter` = **fresh context, 동일 저장소** → `binding`(§6-d (3)).
- Q3의 자 확정은 `binding` 판정만으로 성립하지 않는다 — **사용자 키가 두 번째 열쇠**(원칙 12-c).

# 4. `<open_units>`

라운드 시작 시점(260902, `260831_06` 반영 완료 직후) open 집합 = **공집합**.
본 라운드가 **Q1~Q4 4건을 새로 연다**. 단조 축소 대상은 이 4건이다.

# 5. `<out_of_scope>`

- **재론 금지 확정분** — CP-SM2-1 `3/6` 임계값 · X3 예외조항 철회 · X4 two-key 소관 ·
  `260831_04` §5 E1·E2·E3 · BF-K1-5 「기대 19건」 · U6 허용목록 4파일 · 이력 표식 8종 ·
  `GATEQ` 리터럴 · `260831_06` §2의 E1·E2 확정 문안.
- **타 배우 소유 잔여**(본 라운드 판정 대상 아님): F4(1학기 원본 24건 정제) ·
  내용 축 보류 2건(INT-1) · WIP 형식 6건(`codex-omx` 3 · `type-proposer` 3) ·
  `REV_LOG` L101/L103/L106 열 손상.
- **GATE 2 오탐**(`EX-info-20252F` == `EX-info-20252M`) — `260831_04` U3-a로 이미 판정됨, 경고 전용 유지.

# 6. §6-b 6필드

- `<target>` — `tools/measure_score_bands.py`(수정본) · `analysis/catalog/DIFFICULTY_RUBRIC.md`(stale 판정 대상)
- `<touched>` — 이 라운드에 내가 만들거나 고친 것: `tools/measure_score_bands.py`(수정) ·
  `analysis/wip/mainloop_260902_m2m3m5_rootcause.md`(신규) ·
  `analysis/wip/mainloop_260831_fullscan.md`(내 소유, `NEXT:` 1줄 추가) ·
  본 문서(신규). **자·코퍼스·타 배우 문서 무접촉.**
- `<executor>` — `rev-arbiter`. 근거: 정의상 tier-3 최종 판정 권한이며 fresh context로 동일
  저장소를 직접 열어 주장 대신 실측으로 검증한다. 본 건은 **실행 레인이 자기 측정기를 고친**
  사안이라 같은 레인의 자기 승인이 구조적으로 불가능하다.
- `<requests>` — Q1 · Q2 · Q3 · Q4 (§2)
- `<reply>` — `output/260831/rev/260831_07_arbiter_ruling_parser.md`, §6-d (2) 고정 절 + 7열 표
- `<constraints>` — write surface: 위 회신 경로 1개 + `output/260831/rev/_index.md` ·
  `analysis/REV_LOG.md` 행 추가 + 자기 WIP. **커밋 금지.**
  **자 `DIFFICULTY_RUBRIC.md` 직접 수정 금지**(two-key — 판정은 개시 여부만 정한다).
  원장은 append-only, 시뮬 행 금지, 표식 ASCII.
  카운트·해시는 **회신을 닫기 직전 재측정**하고 자기참조 모집단에는 측정 경계를 병기한다(§6-b (f-1)).

# 7. 지시와 원문이 어긋나면 실측을 따르라

본 문서의 수치는 전부 작성 직전 실측이지만, 직전 라운드에서만 내 카운트 4건이 판정자에게
반증됐다(`260831_06`). 인용과 원문이 어긋나면 **원문과 재실행 결과가 이긴다.**
