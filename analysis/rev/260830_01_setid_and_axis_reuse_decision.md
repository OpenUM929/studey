---
document: 260830_01_setid_and_axis_reuse_decision
author: 메인 세션 (main loop, Claude Code Opus)
reviewer: unset
grade: 제안 (decision request)
date: 260830
target: docs/DATA_STANDARD.md §1.3 · analysis/catalog/CODE_REGISTRY.md §5 · analysis/catalog/math2.md
decision_authority: 사용자 또는 rev-arbiter
---

# 결정요청 — 세트ID 정책 부재 · 세트 간 변형축 재사용 기준 부재

> **왜 실행 레인이 고치지 않고 올리는가.** 두 사안 모두 **자(ruler)** 다 —
> 수용기준·명명정책의 개정이다. CLAUDE.md 원칙 12-a에 따라 실행 레인(메인 루프)은
> 확정된 기준을 소비만 하고, 만족 불가능하거나 부재한 기준은 **우회하지 않고 올린다.**
> 특히 U1은 **내가 만든 산출물이 통과하도록 정책을 신설하는 형태**가 되므로
> (260828 감사 F6과 동일한 구조), 내가 쓰면 그 순간 자가 아니라 산출물이 된다.

## frozen_inputs (직접경로 폐쇄 — 본문에 등장하는 모든 경로를 여기 싣는다)

| # | 경로 | 역할 |
|---|------|------|
| 1 | `docs/DATA_STANDARD.md` | §1.3 세트ID 정규식의 정본 |
| 2 | `tools/import_grading.py` | `RE_SET` — 같은 정규식의 실행 구현 |
| 3 | `analysis/catalog/CODE_REGISTRY.md` | 비가역 식별자 등록부(원칙 9-a의 정본) |
| 4 | `analysis/catalog/math2.md` | SM2-01~33 유형 카탈로그 — U2의 `변형 축` 출처 |
| 5 | `output/260822/공통수학2_도형의방정식_모의40.md` | 세트 A (`SET-260822-math2-40`) |
| 6 | `output/260829/260829_02_math2_comprehensive_25.md` | 세트 B (`SET-260829-math2-25`) |
| 7 | `output/260830/260830_01_math2_graded_new_forms_32.md` | 세트 C (`SET-260830-math2-32`) |
| 8 | `output/260830/260830_02_math2_unused_axes_32.md` | 세트 D — **문제의 세트** (`SET-260830-math2-32u`) |
| 9 | `output/260830/parts/W1_I2.md` | 세트 E(미완성, Codex/OMX 레인 소유) — 유일하게 frontmatter를 가진 part |
| 10 | `output/260830/rev/260830_01_item_quality_audit.md` | 260830 품질감사 — U2의 D-2 최초 제기처 |
| 11 | `analysis/REV_GUIDE.md` | §5 배우표 · §6-d 패킷 규격 |
| 12 | `CLAUDE.md` | 원칙 9-a · 9-c · 12 |

excluded: 없음.

---

## units

### U1 — 세트ID: 정책이 없고, 형식이 충돌을 표현하지 못한다

**판정 요청 (선지 enum):** 세트ID 명명 정책을 어느 형태로 확정하는가?
`(a) 접미어 허용` / `(b) 일련번호 치환` / `(c) 하루 1세트 강제` / `(d) 기타`

**측정 결과 (이번 라운드 실측).**

`docs/DATA_STANDARD.md` §1.3의 세트ID 정규식 `^SET-\d{6}-[a-z0-9]+-\d+$`
(의미: `YYMMDD-과목코드-문항수`)에 현존 세트ID 5건을 실제로 넣어 본 결과:

```
intended_use sets: 5
PASS SET-260822-math2-40 | practice | output\260822\공통수학2_도형의방정식_모의40.md
PASS SET-260829-math2-25 | exam     | output\260829\260829_02_math2_comprehensive_25.md
PASS SET-260830-math2-32 | practice | output\260830\260830_01_math2_graded_new_forms_32.md
FAIL SET-260830-math2-32u| practice | output\260830\260830_02_math2_unused_axes_32.md
PASS SET-260830-math2-40 | practice | output\260830\parts\W1_I2.md
```

**결함은 3층이다.**

- **(가) 무효 ID 1건.** `SET-260830-math2-32u`는 끝자리 `u` 때문에 §1.3을 통과하지 못한다.
  같은 정규식이 `tools/import_grading.py`의 `RE_SET`으로 구현돼 있으므로, 이 세트의 채점
  결과는 **원장 반입 시 전량 거부**된다. 작성자는 나(메인 루프)이며, 원칙 9-c-i("ID를 예시로
  적기 전에 §1.3 정규식에 실제로 넣어 본다")를 **지키지 않은 것이 직접 원인**이다.
- **(나) 형식이 충돌을 표현할 수 없다.** `YYMMDD-과목코드-문항수` 세 성분만으로는
  **같은 날·같은 과목·같은 문항수** 세트 2개를 구별할 수단이 없다. 260830이 정확히 그
  상황이었고(32문항 세트 2개), 그래서 접미어 `u`가 즉흥적으로 붙었다. 즉 (가)는 개인의
  부주의이기 이전에 **형식의 표현력 부족**이다.
- **(다) 등록부에 세트ID 항목이 아예 없다.** `analysis/catalog/CODE_REGISTRY.md` 전문에서
  `SET-` 문자열 검색 결과 **0건**. §1은 유형ID 접두어, §3은 subject_code, §5-7은
  "코퍼스ID·유형ID·접두어·subject_code"를 비가역 식별자로 열거하는데 **세트ID가 빠져 있다.**
  그러나 세트ID는 `docs/DATA_STANDARD.md` 원장 열규격에서 `ATTEMPT_LOG`의 조인키이고,
  그 원장은 append-only다 — **정의상 비가역 식별자인데 등록부 밖에 있다.**
  원칙 9-a가 막으려던 바로 그 구멍이다.

**reproduce:**
```
python -c "import re,glob;R=re.compile(r'^SET-\d{6}-[a-z0-9]+-\d+$');
[print(('PASS' if R.match(m.group(1)) else 'FAIL'),m.group(1),f)
 for f in glob.glob('output/**/*.md',recursive=True)
 for t in [open(f,encoding='utf-8').read(1200)]
 for m in [re.search(r'^set_id:\s*(\S+)',t,re.M)] if m and 'intended_use:' in t]"
grep -c "SET-" analysis/catalog/CODE_REGISTRY.md      # 기대: 0
grep -rn "math2-32u" --include=*.md --include=*.py .  # 기대: 자기 frontmatter 1행뿐
```

**선지.**

| 선지 | 내용 | 장점 | 대가 |
|---|---|---|---|
| **(a)** | §1.3을 `^SET-\d{6}-[a-z0-9]+-\d+([a-z])?$` 로 확장해 소문자 1자 접미어를 **정식 허용** | 기존 4개 ID 무손상, 32u가 그대로 유효해짐 | 정규식·`RE_SET`·웹 파서 3곳 동시 개정 필요. **내 산출물을 구제하는 방향의 개정**이라 원칙 12 관점에서 가장 위험한 선지 |
| **(b)** | 마지막 성분의 의미를 **문항수 → 그날의 세트 일련번호**로 재정의(`SET-260830-math2-01`, `-02`) | 정규식 무변경, 충돌 원리적 해소 | 기존 4개 ID의 의미가 소급 변경됨(숫자는 그대로여도 해석이 달라짐). 운영원칙 ① 저촉 여부 판단 필요 |
| **(c)** | 형식 유지 + **같은 날 같은 과목 세트를 1개로 제한**(초과분은 다음 날짜로) | 무개정 | 실제 작업 리듬과 충돌. 날짜를 허위 기재하게 만드는 압력 |
| **(d)** | 기타 — 판정자 제시 | | |

**어느 선지든 함께 확정해야 할 것.**
1. `SET-260830-math2-32u`의 처리 — 개명인가 유효화인가. **지금은 어떤 원장도 이 ID를
   참조하지 않으므로**(실측 1건 = 자기 frontmatter) 개명이 가능한 마지막 시점이다.
   원장 행이 하나라도 생기면 운영원칙 ①로 영구 동결된다.
2. `CODE_REGISTRY`에 **세트ID 절 신설** 여부 — §5-7의 비가역 식별자 열거에 세트ID를
   추가할 것인가. (원칙 9-c-ii에 따라 열거를 사본으로 늘리지 말고 원본 표를 참조하는
   형태를 권한다.)

**메인 루프 의견(구속력 없음):** (b). 정규식과 도구 코드를 건드리지 않고, 충돌을 원리적으로
없애며, 무엇보다 **내 산출물을 통과시키기 위한 개정이 아니다.** 다만 기존 4개 ID의 의미
소급 변경이 운영원칙 ①에 걸리는지는 내가 판단할 사안이 아니다.

---

### U2 — 세트 간 변형축 재사용 기준이 없다

**판정 요청 (선지 enum):** 세트를 새로 만들 때 기존 전 세트가 사용한 변형 축을 배제하는
규칙을 신설하는가? `(a) 강제 배제 + 대조표 의무` / `(b) 권고만` / `(c) 신설하지 않음` / `(d) 기타`

**측정 결과.**

`output/260830/rev/260830_01_item_quality_audit.md` §6 D-2로 최초 제기됐고,
**같은 날 같은 결함이 두 번 더 재현됐다.**

- 1차 발생: 세트 B·C 작성 시 세트 A를 대조하지 않아 수치변형 4건(F1~F4).
- 2차 발생: 그 F1~F4를 고치려고 만든 **교체 문항 2건이 세트 D와 새로 중복**됐다
  (세트 C의 C8 ↔ 세트 D의 C7 · 세트 C의 D1 ↔ 세트 D의 D2). 2차 교체로 해소.

즉 **결함을 고치는 작업 자체가 같은 종류의 결함을 다시 만들었다.** 이는 작성자의 주의력
문제가 아니라 **대조 의무가 규정에 없어서 매번 개인 판단에 맡겨지기 때문**이다.
`analysis/catalog/math2.md`의 각 유형은 `변형 축`을 명시하지만, 그 축이
**세트 간에 소진되는 자원인지 재사용 가능한지**를 정한 문장이 카탈로그에도
`analysis/REV_GUIDE.md`에도 `CLAUDE.md`에도 없다.

**구조적 사실:** 129문항이 33유형을 공유하면 유형당 평균 3.9문항이다. 기준이 없으면
중복은 확률이 아니라 **필연**이다.

**reproduce:** `output/260830/rev/260830_01_item_quality_audit.md` §2 N-2·N-3 표, 그리고
세트 C·D의 `← 260830 2차 교체` 주석 2건.

**선지.**

| 선지 | 내용 | 대가 |
|---|---|---|
| **(a)** | 신규 세트는 기존 전 세트의 `(유형ID, 사용한 변형 축)` 목록을 먼저 추출하고, **미사용 축에서만** 출제. 세트에 대조표 첨부를 의무화하고 `item-quality-auditor` N2가 이를 검사 | 축이 소진된 유형은 결국 출제 불가 — 실측상 SM2-24는 이미 8회로 소진 임박. **카탈로그의 축을 늘리려면 부교재 재판독이 필요**한데 원본이 저장소에 없다(별건 차단 조건) |
| **(b)** | 권고로만 두고 감사에서 지적 | 오늘 두 번 실패한 방식 그대로 |
| **(c)** | 신설하지 않음 — 반복 훈련 목적의 practice 세트에서는 축 재사용을 정상으로 본다 | exam 세트에는 부적절. practice/exam 구분 필요 |
| **(d)** | 기타 | |

**메인 루프 의견(구속력 없음):** (a)를 `intended_use: exam`에만 강제하고 practice에는
대조표만 의무화. 다만 (a)의 대가로 적힌 "축 소진" 문제는 실재하므로, 이 결정은
**부교재 재판독(세트 A의 N축 `▲ blocked` 해소)과 묶어서** 판단하는 편이 합리적이다.

---

## actor_grade

- 작성 주체: 메인 세션(main loop). `analysis/REV_GUIDE.md` §5 마지막 행의 **대행이 아니다** —
  이 문서는 검토서가 아니라 **실행 레인이 올리는 결정요청**이다. tier 라벨을 쓰지 않는다.
- 등급: `제안`. 이 문서는 어떤 것도 승인하지 못하며, 개정 권한은 사용자와 `rev-arbiter`에 있다.
- 이해충돌 고지: **U1의 무효 ID와 U2의 중복 문항은 모두 내가 만든 것이다.** 따라서 내가
  제시한 "메인 루프 의견"은 자기 산출물의 처리에 관한 이해당사자 의견이다.

## open_units

- `SET-260830-math2-32u`는 판정 전까지 **무효 ID 상태로 유지**한다. 임의 개명하지 않는다.
- 세트 A·B·C·D 4종은 전부 `gate_status: not-verified` (260830 시점 3종 게이트 진행 중).
- 세트 E(`output/260830/parts/`)는 **Codex/OMX 레인 배타 소유**로 이 문서의 판정 대상이 아니다.

## out_of_scope

- 부교재 원본 재판독 여부(세트 A의 N축 차단 해소) — 별건.
- `tools/check_assurance_contract.py`의 금지 표현 불가 문제 — 별건(260828 감사 잔여).
- 세트 E의 내용·품질 — 소유 레인의 판정 대상.

## history

- 260830 신설. U1은 이번 세션의 세트ID 전수 정규식 검사에서 발견, U2는 260830 품질감사
  D-2의 재제출(같은 날 2회 재현으로 근거 보강).
