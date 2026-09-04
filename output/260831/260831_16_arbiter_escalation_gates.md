---
doc: 260831_16 — 게이트 3건 결정요청 (원칙 12-a 상신)
author: 메인 루프 (실행 레인 — 판정 등급 없음)
date: 260902
target_actor: rev-arbiter
predecessor: output/260831/rev/260831_05_arbiter_ruling_refreeze.md
format: analysis/REV_GUIDE.md §6-d (1)
---

# 0. 요지

판정 `260831_05` 반영(구속 6건) 및 U7 병합 라운드(슬라이스 1·2)를 완료하는 과정에서
**동결된 수용기준·게이트 자체의 결함 3건**을 발견했다. 셋 다 실행 레인의 소관이 아니므로
(CLAUDE.md 원칙 12-a) 우회하지 않고 그대로 올린다. 세 건 모두 **최소 수리를 구성해
전수 실행한 `closure`** 를 첨부한다(§6-d (2)).

# 1. `<frozen_inputs>`

| path | bytes | sha256(앞16) | role |
|---|---|---|---|
| `analysis/catalog/DIFFICULTY_RUBRIC.md` | 20058 | `3a1b609b46855485` | ruler |
| `tools/measure_score_bands.py` | 14731 | `f60455c6fc0d8ca9` | derived |
| `output/260831/rev/260831_05_arbiter_ruling_refreeze.md` | 38294 | `6c93e096b986e9f6` | source |
| `output/260831/260831_15_arbiter_refreeze_request.md` | 12932 | `2ba84f24aa2fde08` | evidence |
| `analysis/REV_GUIDE.md` | 42178 | `ecb54fd74c08f0c3` | ruler |
| `CLAUDE.md` | 36245 | `c5ce263fe3594c84` | ruler |

서명 블록 지문(판정 U5 §2 동결 명령, `260831_05:277-278`) 재실행 = **68행 / `a204f3412cf900b5`** — 불변.

`<excluded>` — 본문에 경로 문자열로 등장하나 동결하지 않는 것:

- `output/260831/260831_01_*.md` 12파일 — U7 슬라이스 2 산출물. **이 라운드의 판정 대상이 아니고**
  게이트 실측의 모집단으로만 인용한다(값은 아래 `reproduce:`로 재산출 가능).
- `analysis/wip/mainloop_260901_bfrf_apply.md` · `analysis/wip/mainloop_260902_escalation.md` —
  **live 문서**다. 판정 `260831_05` F-RF-1이 지적한 「살아 있는 WIP를 `frozen_inputs`에 넣은 결함」을
  반복하지 않기 위해 해시를 동결값으로 주장하지 않는다. 근거로 인용하지도 않는다(모든 근거는
  `reproduce:` 명령으로 재산출한다).

# 2. `<units>`

## E1 — U6 확정 수용기준의 종단 exit code가 반전돼 있다

**질문**: 판정 `260831_05` §2 U6가 동결한 게이트 명령의 **종단에 `| wc -l` 을 부가**해
`기대 출력 0 / exit 0`으로 재기술하는 개정을 승인하는가?

**사실**: 동결 명령의 마지막 단은 `grep`이고, GNU grep은 **무매칭 시 1을 반환**한다.
따라서 이 게이트는 현재 **exit 1 = 통과 / exit 0 = 실패**다. 판정문이 수용기준을
「기대 출력: 0줄 (`wc -l` = `0`)」로 적었으므로 **사람이 읽으면 오판하지 않는다.** 문제는
명령 블록을 그대로 CI·스크립트에 옮기는 경우로, 원칙 11의 fail-closed가 **정확히 뒤집혀**
fail-open이 된다.

**fixture (원칙 12-d)** — 샌드박스(`scratchpad/gatefix/`)에 실 27파일을 복제하고
동결 패턴 3종 중 첫 패턴을 담은 1줄을 별도 파일로 주입해 4셀 전수 실행:

| 상태 | 동결형(끝단 grep) | 제안형(`wc -l` 부가) |
|---|---|---|
| LIVE 0건 = **통과** | `exit=1` | `out=0 exit=0` |
| LIVE 1건 = **실패** | `exit=0` | `out=1 exit=0` |

**closure = 2/4** — exit code를 판정 신호로 읽을 때 동결형은 2셀 전부 오분류,
제안형은 2셀 전부 정분류. 실 `output/260831/`은 무접촉(샌드박스 복제본에서만 주입, 원칙 9-b).

**최소 수리 범위**: 허용목록 4파일·이력 표식 8종·`GATEQ` 리터럴 **전부 불변**. 종단 1파이프만 추가.
즉 「자를 넓히는」 변경이 아니다(U6이 금지한 방향과 무관).

**verdict enum**: `approve | revise-required | reject | insufficient-evidence`

**reproduce**:

```
SB=<scratchpad>/gatefix ; rm -rf $SB; mkdir -p $SB/output/260831
cp output/260831/260831_*.md $SB/output/260831/ ; cd $SB
ALLOW='_09_extractor_fix_request|_12_tier2_round2_briefing|_13_arbiter_decision_request|_14_K1_band_measurement'
HIST='정정 이력|철회|종전|오기|최초안|기각|이 자리에 있던|적었다'
GATEQ="grep -rn -e '선택(단답)형'"
grep -rn -e '선택(단답)형' -e '60\.4' -e '서답형 비중 50% 초과 회차는 제외' output/260831/260831_*.md \
  | grep -vE "$ALLOW" | grep -vF "$GATEQ" | grep -vE "$HIST" >/dev/null; echo "exit=$?"
```

## E2 — U7 진입 게이트 `grep -rc "축 보류"` = 0 은 만족 불가능하다

**질문**: 진입 게이트를 `grep -rn "열 축 보류" output/260831/260831_01_*.md | wc -l` = 0
**으로 정밀화**하는 개정을 승인하는가? (선지: A 정밀화 승인 / B 원문 유지 / C 게이트 폐기)

**사실 ①(경로 미한정)**: 동결 문구(`260831_05:357`)에는 경로 인자가 없어 **repo 전체 재귀**다.
**U6에서 이미 폐기 판정한 자기오염 구조와 동형** — 규정을 지킬수록(이력 보존·수용기준 인용)
게이트가 멀어진다. 이 패킷 한 편을 쓰는 동안 두 시점에서 실측했다:

| 시점 | 매칭 | 파일 | U7이 해소 가능한 건수 |
|---|---|---|---|
| 본 패킷 작성 **직전** | 34 | 11 | 0 |
| 본 패킷 작성 **직후** | 45 | 13 | 0 |
| 원장 기록(`_index` R4 행 · `REV_LOG` 행) **완료 후** | **47** | **14** | 0 |

13건이 늘어난 원인은 전부 **이 게이트를 논한 문서 자신**이다(본 패킷 8 + 본 라운드 WIP 3 +
원장 2). 판정문 `260831_05` 단독으로도 5건을 기여하고 있다. **게이트를 상신하는 행위 자체가
게이트를 더 멀어지게 한다** — 이보다 명확한 만족 불가능성의 실증은 없다.

**사실 ②(뜻이 둘)**: 판정 시점 5건은 서로 다른 두 뜻이었다.

| 위치 | 뜻 | U7 범위 |
|---|---|---|
| `type_analysis_SC.md:386` · `SM2.md:505` · `SS.md:347` | **열 축 보류** — BF-K1-4 축 분리로 공통수학2 행이 거짓 | 예 (3) |
| `type_analysis_SS.md:118` · `catalog_update_SS.md:473` | **내용 축 보류** — 통합사회 선택형 17번 자료가 그림 안에만 존재(INT-1) | 아니오 (2) |

내용 축 보류는 원본 그림 판독 문제로 `type-extractor` 계열 소관이며 U7이 해소할 수 없다.

**closure = 0/2** — 제안형을 전수 실행하면 잔여 **0건**(열 축 3건은 슬라이스 1에서 해소).
원문형을 전수 실행하면 잔여 **47건**이며, 그 중 U7이 해소 가능한 것은 **0건**이다
(`_01_*` 잔여 2건은 내용 축이라 범위 밖, 나머지 45건은 게이트를 인용한 메타 문서).

**reproduce**:

```
grep -rc "축 보류" . | grep -v ":0$"                                    # 원문형: 11파일 / 합 34
grep -rn "축 보류"      output/260831/260831_01_*.md | wc -l            # 2  (내용 축 잔여)
grep -rn "열 축 보류"   output/260831/260831_01_*.md | wc -l            # 0  (제안형 = 통과)
grep -ro "Tier 재도출 대기" output/260831/260831_01_*.md | wc -l        # 0
```

**주의**: 이 패킷 파일 자체가 원문형 카운트를 즉시 올린다 — 그것이 사실 ①의 실증이다.

## E3 — `REV_GUIDE` §6-b (f)에 **기입 순서** 조항을 추가

**질문**: §6-b (f)에 다음 한 문장을 추가하는 개정을 승인하는가?

> **기입할 값은 그 편집이 끝난 뒤 다시 측정한다.** 편집 전에 잰 값을 편집 후 문서에 옮겨 적으면
> 그것은 인용이 아니라 창작이다. 해시·바이트수·카운트는 **문서를 닫기 직전** 재측정한 값만 쓴다.
> 명령이 다르면 값도 다르다 — 동결된 값을 재확인할 때는 **동결 명령 그 자체**를 실행한다.

**사실**: (f)는 「증거를 그 자리에 달라」고만 요구하고 **언제 재는지**를 정하지 않았다. 그래서
증거를 붙인 값조차 stale일 수 있고, 260901에 실제로 그렇게 됐다.

**closure = 3/32** — 260901 `REV_LOG` 9행의 16-hex 리터럴 **32회(고유 19종)** 전수 대조.
오기 **3종**, 전부 동일 원인(편집 완료 전 기입):

| 오기 값 | 실제 | 원인 |
|---|---|---|
| `05f4f3d0d2952134` | `3a1b609b46855485` | 자 정정 **전** 해시를 정정 후 행에 기입 (바이트수는 20058로 동일해 눈에 안 띔) |
| `bd8dea2c8ed4b47b` (14337 B) | `f60455c6fc0d8ca9` (14731 B) | 측정기 편집 도중 기입 |
| `d1e6f5…` | `6c93e096b986e9f6` | 판정문 접두어를 **창작** — 「미확인」 라벨을 붙였으나 그럴듯한 문자열을 지어낸 것 자체가 결함 |

**fixture (원칙 12-d)** — 이 규칙이 잡아내는 알려진 실패 사례는 위 3건이며, 그 밖에 이번
라운드에서 1건이 더 재현됐다: 서명 블록 지문을 **동결 명령이 아닌 단일 `awk` 2범위**로 재측정해
`70행 / e4423614da073c51`을 얻었다. 동결 명령(`awk` 2회 + 각 `sed '$d'`)의 재실행값은
`68행 / a204f3412cf900b5`로 **불변**이다. type-proposer가 슬라이스 2에서 `sed -n '1,68p'`로
재측정해 「지문 불일치」를 보고한 것과 **동형의 오류**이며, 그 보고 역시 이 규칙이 막는다.

**reproduce**:

```
grep "260901" analysis/REV_LOG.md | grep -o '[0-9a-f]\{16\}' | sort | uniq -c   # 32회 / 19종
sha256sum analysis/catalog/DIFFICULTY_RUBRIC.md tools/measure_score_bands.py \
          output/260831/rev/260831_05_arbiter_ruling_refreeze.md | cut -c1-16
{ awk '/^# 1\. 배점/,/^# 2\. 난이도/' analysis/catalog/DIFFICULTY_RUBRIC.md | sed '$d'
  awk '/^### Tier 요약표/,/^# 4\./'  analysis/catalog/DIFFICULTY_RUBRIC.md | sed '$d'; } | sha256sum
```

# 3. `<actor_grade>`

| 배우 | 등급 | 쓸 수 있는 라벨 |
|---|---|---|
| `rev-arbiter` (fresh context, §5) | `binding` | approve · revise-required · reject |
| 메인 루프(본 문서 작성자) | **등급 없음** | 판정 불가 — 결정요청으로 올린다 |

본 문서는 실행 레인 산출물이므로 어떤 판정 라벨도 자칭하지 않는다.

# 4. `<open_units>`

라운드 개시 시점 미해결: **E1 · E2 · E3** (3건). 이전 라운드 잔여는 아래와 같이 이관 완료:
U5 refreeze 반영 done · U6 blocked 해제 done · U7 슬라이스 1·2 done · U8 조건 3건 반영 done.

# 5. `<out_of_scope>`

- **재론 금지 유지**: CP-SM2-1 `3/6` 승격 임계값 · X3 예외조항 철회 · X4 two-key 소관 ·
  `260831_04` §5 E1·E2·E3 · **BF-K1-5의 「기대 19건」**(U6에서 폐기, 재론 금지).
- **U6 확정 수용기준의 허용목록 4파일·이력 표식 8종·`GATEQ` 리터럴** — E1은 이 셋을 건드리지 않는다.
- **자(`DIFFICULTY_RUBRIC.md`) 서명 블록** — 본 라운드에서 개정 요청 없음. 지문 불변 확인만.
- 타 배우 소유 잔여(**판정 대상 아님, 상태 보고**): 전사 불일치 M2·M3·M5(`type-extractor`),
  1학기 원본 24건 정제 F4(`type-extractor`), WIP 형식 7건(F-RF-4, 각 WIP 작성자),
  `REV_LOG` L101/L103/L106 열 손상(F5/M4, 각 행 작성자),
  자 §2 표제 「7개 실측 특징」 vs 실제 DF1~DF9(보고됨, 범위 밖).

# 6. §6-b 6필드

- `<target>` — 본 문서 `output/260831/260831_16_arbiter_escalation_gates.md`
- `<touched>` — 이번 라운드 요청 측 생성/수정 **2건뿐**:
  ▸`output/260831/260831_16_arbiter_escalation_gates.md`(신규)
  ▸`analysis/wip/mainloop_260902_escalation.md`(신규).
  그 외 **0건** — 자·측정기·판정문·`_01_*` 무수정이며 §1 표의 `sha256` 재실행으로 확인 가능하다.
- `<executor>` — `rev-arbiter`. 근거: 정의 description이 「tier-3 FINAL DECISION authority,
  fresh context, same repository, binding ruling approve/revise-required/reject」이고,
  본 건은 **동결된 수용기준의 개정 가부**이므로 원칙 12-c의 two-key 중 감사권한자 키에 해당한다.
- `<requests>` — E1 · E2 · E3 각각 `approve | revise-required | reject | insufficient-evidence`
- `<reply>` — `output/260831/rev/260831_06_arbiter_ruling_gates.md`, 형식 `REV_GUIDE` §6-d (2)
  (고정 절 + `unit | verdict | grade | evidence | measured | closure | note` 7열)
- `<constraints>` — write surface는 `output/260831/rev/` + `output/260831/rev/_index.md` 행 추가 +
  `analysis/REV_LOG.md` 행 추가만. **커밋 금지.** 자·측정기·`_01_*` 산출물 **수정 금지**
  (개정이 필요하면 판정문에 구속 항목으로 적고 반영은 소유 레인이 한다 — 원칙 8).
  인용값을 신뢰하지 말고 `reproduce:` 명령을 직접 실행하라.

> 이 지시문의 값이 원문과 어긋나면 지시가 아니라 **실측을 따르고 그 사실을 회신하라**.
