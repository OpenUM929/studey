---
title: 260829_01 — Codex/OMX 탐지 실패 원인·재설계안 판정
source: output/260829/rev/detection-failure-audit/{00_PREFLIGHT,01_author_root_cause,02_evidence_audit,03_adversarial_review,04_GATE,FINAL_REPORT_FOR_OPUS}.md
created: 260829
decided_by: main-loop (Claude Code Opus) — tier-3 판정 역할 직접 수행
reviewer: unset
independence: "**NOT FRESH-CONTEXT.** 이 세션이 260828 감사(F1~F9)와 CLAUDE.md 원칙 12의 작성자다.
  REV_GUIDE §5가 요구하는 `rev-arbiter` 독립 컨텍스트 요건을 충족하지 못한다. 회람 `<constraints>`가
  subagent 배치를 금지했고 외부 독립 Opus 레인이 없으므로 §5 「메인 루프 대행」 행으로 수행한다.
  따라서 Q1·Q2 판정은 **사용자 2차 키(원칙 12-c) 확인 전까지 잠정**이다."
status: proposal-grade — superseded-pending-rerun (260829 2차 정정)
grade: proposal (REV_GUIDE §5 대행 행 · §6-d (3) 배우표)
errata: "§0의 `binding`·`approve` 라벨은 **권한 초과**였다. §5는 메인 루프 대행 산출물을 제안
  등급으로 한정한다. 아래 라벨은 전부 `proposal-` 접두로 읽는다. 추가로 BF1의 `[OK]` 마커
  인용과 BF3의 span 정규식은 실측으로 오류가 확인됐다 — `## 개정 이력` 참조."
---

## 0. 판정 요약

| question | ruling | 2차 키 |
|---|---|---|
| Q1 원인 모델 | **accept**(수정 1건 부기) | 필요 |
| Q2 소유 토폴로지 | **revise-required** — 4-way 분리는 이 저장소에서 인력 불가, 2-key로 축소 | 필요 |
| Q3 F1 warning 채널 | **binding: 존치 + 계산값化** (삭제 아님) | 불요(원칙 11 기존 규정의 집행) |
| Q4 F6 유형 상한 | **binding: 상한 폐지 + `row_kind` 신설. 이 자료의 기대 행수 = 16** | 필요(재동결) |
| Q5 F9 span 규칙 | **binding: rule_a 정본화. W-04 = 44–49** | 필요(재동결) |
| Q6 F2-b 역사 증거 | **approve** — `documentary-only` 영구 표기 | 불요 |
| Q7 재실행 조건 | **revise-required** — model/depth telemetry 요구는 달성 불가 조건이므로 게이트에서 제외 | 필요 |

**게이트 판정 자체(`▲ blocked — BLOCKED`)는 유지한다.** 다만 그 근거 중 **F6·F9의 "raw 부재"
항목은 기각**한다 — 아래 §2에서 원천을 직접 열어 재산출했다.

## 1. 독립 재검증 (verify-don't-trust)

보고서 서술을 신뢰하지 않고 다음을 직접 실행·판독했다.

| 검증 | 결과 |
|---|---|
| 동결 13파일 SHA-256 재계산 | **13/13 일치** (`CLAUDE.md` 27763/`36b919c5…`, `gate_selftest_260828.py` 10621/`69e8610d…` 등). drift 0 |
| 필수 산출물 4종 해시 | 04_GATE §2.1 기재값과 일치 |
| `meta_gate_260828.py --check all` | `freeze_ok=12/12 integrity_hits=7 vacuous_signal_count=1 coverage_failures=2 warnings=0 failures=7` **exit 1** — 보고서 §7과 일치 |
| `gate_selftest_260828.py` | `baseline_exit=1 baseline_failures=5` → `FAIL: baseline is not clean` **exit 1** — 일치 |
| F1 `check_experiment.py:223` | `print(f"warnings=0")` — **리터럴 확인** |
| F6 `check_experiment.py:143` | `if not 5 <= len(rows) <= 12` + `type membership is not an exclusive exact cover` — **확인** |
| F3 `check_experiment.py:168-170` | `require_report()` = 파일 존재만 확인 — **확인** |
| 5-ID coverage | expected=observed=`[F1,F2-b,F3,F6,F9]`, dup/missing/extra 모두 `[]` — **확인** |

이 범위에서 보고서의 사실 주장은 **전건 재현됐다**. 아래 §2의 두 항목만 예외다.

## 2. 판정을 바꾼 실측 — "raw 부재"는 성립하지 않는다

### 2.1 F6 — `author/types.tsv`로 16을 직접 재산출했다

보고서 §2는 "raw `items.tsv/types.tsv/corpus`가 13-source freeze에 없어 16을 독립 재산출하지
못한다"고 적고 `⚠️ 자 미확정`을 걸었다. 그러나 `output/260828/diagnostic/math2-method-comparison/
codex-team/author/types.tsv`는 **저장소에 실재하며 지금 열린다**. 실제 계수:

| row_kind | 행 | 문항 수 |
|---|---|---:|
| 재사용 유형(2문항 이상) | `DIAG-G01,G02,G03,G06,G08,G09` | 12 |
| 단독 generator | `DIAG-G04,G05,G07` + `U10`이 스스로 열거한 `S-07·S-10·S-12` + `U11`이 열거한 `S-13·S-14·S-18` | 9 |
| BLOCKED(원본 결함) | `S-17` | 1 |
| **합계** | **16행** | **22** |

`DIAG-U10`·`U11`은 자기 셀에 `"세 문항은 서로 독립 subgroup이며 하나의 reusable type가 아님"`,
`"5~12 row 제약을 위한 비재사용 bookkeeping row"`라고 **명시**한다. 즉 정직한 행수는 16이고 상한
12와 충돌한다는 260828 F6은 **원천에서 독립 재현된다**. `⚠️ 자 미확정` 중 "재산출 불가" 부분은 기각.

### 2.2 F9 — `transcript.md`로 span 규칙을 확정했다

동결된 두 TSV 모두 `source_path` 열에 `corpus/EX-math2-20252M/transcript.md`를 **경로로 적고
있는데**, 그 파일이 freeze 목록에 없다. 파일은 저장소에 있다. 44~50행 실측:

```
44  ## 4.
45  [서술형4] 포물선 y=x^2 -4x를 포물선 y=x^2 -12x+27 로
46  옮기는 평행이동에 의하여 직선 l: 2x+y-1=0 이 직선
47  l'으로 옮겨진다. 이때 두 직선 l과 l' 사이의 거리를
48  구하시오.
49  (빈 줄)
50  # 단답형 문항
```

- `W-01` = 31–34 (다음 heading `## 2.` = 35 → 34). `W-03` = 39–43 (다음 heading 44 → 43).
  **21/22행이 "다음 heading 직전"** = rule_a이며, 후행 공백 1줄을 포함한다.
- `W-04`만 44–48(마지막 비공백 행). rule_a라면 44–49다.
- 원인은 의미 모호성이 아니라 **파서가 `##`만 heading으로 인식**해 W-04에서 다음 `##`(52행)까지
  흘렀고, gatekeeper가 **파서 대신 출력 한 행을 손으로** 44–48로 고친 것이다. 260828 F9의 진단이
  원천에서 확인된다.

### 2.3 신규 발견 F10 — 피측정 레인이 증거 경계도 소유했다

13파일 목록은 `00_PREFLIGHT.md`, 즉 **피측정 레인 자신이 작성한 문서**다. 그 목록은 동결 파일이
경로로 직접 지목하는 세 원천(`corpus/EX-math2-20252M/transcript.md`, `author/types.tsv`,
`author/items.tsv`)을 제외했고, 그 결과 F6·F9가 "원천 부재로 판정 불가"가 됐다. 세 파일은 모두
저장소에 있었다.

이것을 부정직으로 보지 않는다 — F6의 우산 행과 **같은 구조적 결과**다. 원칙 12는 자(ruler)의
소유만 분리했는데, **증거 동결 경계(evidence scope)도 자의 일부**다. 경계를 피측정 레인이 그으면
"측정 불가"가 자기 판정으로 산출된다. 원칙 12의 적용 범위를 확장해야 한다(§4 구속 수정 5).

## 3. 질문별 판정

| question | ruling | evidence | note |
|---|---|---|---|
| **Q1 원인 모델** — 자기측정 + dependency-closure 실패를 주원인으로 인정할지 | **accept** | §1 전건 재현. 모델은 260828 F1·F2-b·F3·F6·F9와 CLAUDE.md 원칙 12의 진단과 일치한다 | 수정 1건: 보고서 §1은 원인을 5개로 열거하면서 **증거 경계 자기소유(F10)** 를 누락했다. §2.3을 원인 6번으로 추가할 것. 또한 이 모델은 **정확하되 독자 발견이 아니다** — 5개 ID를 미리 받은 상태의 사후 설명이므로 탐지 능력의 증거로 인용 금지(보고서 §2 말미 문장을 유지한다) |
| **Q2 소유 토폴로지** — implementer ≠ qualifier ≠ refreezer ≠ measured lane/gatekeeper 필수화 | **revise-required** | 이 저장소의 실행 자원은 Codex/OMX 런타임 1개와 Claude Code 세션 1개다. 이번 라운드에서 4레인을 띄운 결과가 `independence=shared-context` + `observed model/depth unavailable`이었다(04_GATE §4) | 4-way 분리를 **필수 조건으로 확정하지 않는다.** 독립 컨텍스트로 인력할 수 없는 역할을 필수화하면 이름만 다른 레인이 별도 key로 계상되고, 이는 보고서 §3.5가 스스로 지적한 실패다. **확정하는 최소 규칙은 2-key다**: (i) 피측정 레인은 자·증거경계에 **어떤 경우에도 쓰기 없음** (ii) 자·경계의 변경은 **감사권한자 제안 + 사용자 확인** 두 키로만 성립. implementer/qualifier/refreezer 3분할은 **권고(목표 상태)** 로 강등하고, 달성 시에만 그 사실을 근거로 인용한다 |
| **Q3 F1 warning 채널** | **binding — 존치하되 계산값으로 전환** | `check_experiment.py:223`의 `print(f"warnings=0")`은 리터럴. 원칙 11의 수용기준은 `경고 0줄 + exit 0`의 연언이므로, 상수 채널은 그 연언의 한 항을 항구적으로 참으로 만든다 | **삭제가 아니라 계산이다.** 삭제하면 원칙 11의 연언 자체가 무의미해지고, 같은 이름의 채널을 정직하게 계산하는 도구(`build_mastery.py`·`import_grading.py` — 260828 수정 B로 `len(warnings)` 계산값)와 규격이 갈라진다. 요건: ① `warnings` 리스트를 실제로 축적 ② `warnings=len(warnings)` 출력 ③ 각 경고를 `[WARN] …` 한 줄씩 **`[OK]`보다 먼저** 출력 ④ 경고 정의를 문서화(=차단하지 않는 이탈). 구현자는 피측정 레인이 아니어야 한다 |
| **Q4 F6 reusable-type/count/exact-cover 정책** | **binding** | §2.1 재산출: 16행 = 재사용 6 + 단독 9 + blocked 1, 22문항 정확 포괄 | ① **행수 상한·하한 폐지**(`check_experiment.py:143`의 `5 <= len(rows) <= 12` 제거). ② **문항 exact-cover는 존치** — 22개 item ID가 정확히 한 행에 속한다는 완전성 검사는 정당하다. ③ **`row_kind` 열 신설**: `reusable`(2문항 이상, 관측 variation axis 2개 이상) / `singleton`(1문항, axis 2개 이상) / `blocked`(원본 결함). ④ **독립 generator를 묶은 우산 행 금지** — 한 행의 모든 문항은 같은 generator를 공유해야 한다. ⑤ 통합 압력은 pass/fail이 아니라 **보고 지표** `reuse_ratio = items / rows`로 낸다. ⑥ 문항층이 이미 쓰던 다중 배정(`SM2-15 후 SM2-19`)을 `primary_type`·`secondary_types` 열로 명시해 유형층 분할 모델과의 모순을 제거한다. **이 자료의 기대값: rows=16, reusable=6, singleton=9, blocked=1, items=22, reuse_ratio=1.375**(플레이스홀더 금지 — 원칙 9-c-iii). `ACCEPTANCE_SCHEMA_260828.repaired.md` §2는 위 ③④⑤⑥을 추가하는 조건으로 채택한다 |
| **Q5 F9 span 경계·generator 규격** | **binding** | §2.2 원천 판독 | ① **정본 규칙 = rule_a**: 문항 span은 자기 heading 행부터 **다음 heading 직전 행**까지, 마지막 문항은 EOF까지. ② heading 인식은 **`^#{1,6}\s`** — 레벨 무관. `##`만 인식한 것이 W-04 이탈의 단일 원인이다. ③ 따라서 **`W-04` = 44–49**로 정정하고, shipped TSV의 손수정값 44–48은 **무효**다. ④ 표는 **generator가 매 실행 재생성**하고 게이트가 재생성본과 대조한다(원칙 12-b). 손수정 발견 시 그 라운드 판정 전체가 stale. ⑤ `derivation_rule` 열을 유지하되 값이 `rule_a` 외인 행이 1개라도 있으면 **FAIL**(현재 두 규칙 공존이 결함의 실체였다) |
| **Q6 F2-b 역사 증거** | **approve** | pre-change ruler snapshot·당시 audit artifact·변경 로그가 저장소·freeze 어디에도 없다 | `documentary-only` **영구 표기**를 승인한다. 재구성물을 원본 증거로 표기하지 않는다는 04_GATE §9 항목 4를 그대로 확정한다. 단 F6·F9와 달리 F2-b만 이 처분 대상이다 — §2가 셋을 같은 `⚠️` 등급으로 묶은 것은 정정한다 |
| **Q7 재실행 조건** | **revise-required** | 04_GATE §4는 4레인 전부 `observed model/depth: unavailable`로 기록한다. 이는 이번 실행의 흠이 아니라 **호스트가 노출하지 않는 정보**다 | `host-authenticated model/depth telemetry`를 재실행 **선결 조건**으로 확정하지 않는다. 관측 불가능한 조건을 게이트에 넣는 것은 **만족 불가능한 수용기준**이고, 그 결과는 F6과 같은 우회 산출물이다(원칙 12-a). 대체 규격: (a) configured model/depth와 launch args를 기록하고 (b) `observed: unavailable`을 **명시**하며 (c) 그 상태에서 **모델 동등성·benchmark·대체 주장을 전면 금지**한다 — 금지로 막을 뿐 증명을 요구하지 않는다. **독립성 요건은 그대로 hard**: 독립 감사를 자처하는 레인은 `fork_turns=none`이어야 하고, `fork_turns=all` 레인은 독립 증거로 계상하지 않는다. Phase 1·2·5(결정→새 freeze→two-key 재동결)는 **선결 조건으로 유지**한다 |

## 4. 구속 수정 (binding fixes)

승인된 항목만 **작성 주체**가 반영한다(원칙 8). 자·게이트 코드는 **피측정 레인이 아닌 implementer**가 고친다.

- [ ] **BF1** `check_experiment.py:223` — `warnings=0` 리터럴을 `len(warnings)` 계산값으로 교체하고 `[WARN]` 행을 `[OK]`보다 먼저 출력. (Q3)
- [ ] **BF2** `check_experiment.py:143` — `5 <= len(rows) <= 12` 제거. exact-cover 검사는 존치. `row_kind` 열 검사 신설(우산 행 = 서로 다른 generator를 묶은 행이면 FAIL). (Q4)
- [ ] **BF3** `EXPECTED_ITEM_IDS` generator — heading 정규식을 `^#{1,6}\s`로 고치고 `W-04`를 44–49로 재생성. 표 손수정 경로 제거. (Q5)
- [ ] **BF4** `ACCEPTANCE_SCHEMA_260828.repaired.md` §2에 `row_kind`·우산 금지·`reuse_ratio`·`primary/secondary` 4항 추가 후 **동결본으로 승격**. 기대값 `rows=16 / reusable=6 / singleton=9 / blocked=1 / items=22`를 수용기준에 실측 수치로 기입. (Q4)
- [ ] **BF5** CLAUDE.md 원칙 12에 **증거 동결 경계(evidence scope)** 를 자의 구성요소로 추가. 피측정 레인은 자기 freeze 목록을 스스로 확정하지 못하며, 동결 목록은 **동결 파일이 경로로 지목하는 원천을 빠짐없이 포함**해야 한다(누락 시 게이트 FAIL). 근거: F10. (Q1 수정·§2.3)
- [ ] **BF6** Q2 토폴로지를 2-key(피측정 레인 쓰기 없음 + 감사권한자 제안·사용자 확인)로 확정하고, implementer/qualifier/refreezer 3분할은 권고로 표기. (Q2)
- [ ] **BF7** Q7 재실행 조건에서 `observed model/depth telemetry` 요구를 삭제하고 (a)(b)(c) 대체 규격으로 교체. 독립성(`fork_turns=none`) 요건은 유지. (Q7)

## 5. 유지되는 차단

- **BLOCKED 판정 유지.** F6·F9의 raw 근거는 §2에서 해소됐으나, 04_GATE §7의 blocker 2(author/auditor
  `fork_turns=all` shared-context)는 그대로다. 독립 감사 레인 부재는 사후에 치유할 수 없다.
- **`READY-FOR-EXTERNAL-EVALUATION` DENIED 유지.** benchmark·comparison·Opus 대체/동등성·release 금지.
- **판정자 결격.** 이 판정은 fresh-context 아비터가 아니라 260828 감사 작성자가 내렸다. Q1·Q2는
  자기확증 위험 구간이므로 **사용자 확인이 2차 키**다. Q3~Q7은 원천 실측(§1·§2)에 근거하므로
  재현 가능하다.
- **자 미수정.** 이 라운드에서 `ACCEPTANCE_SCHEMA`·`EXPECTED_ITEM_IDS`·게이트 코드 어느 것도
  수정하지 않았다(REV_GUIDE §5 「자는 어떤 배우의 write surface도 아니다」). 판정은 정책만 확정한다.

## 6. notes

- 보고서의 **자기 판정 정직도는 높다.** 04_GATE는 자기 팀 산출물에 대해 `evidence locatability: FAIL`,
  `independent substantive lane proof: FAIL`, `verified actual-team assurance: FAIL`을 스스로 냈고,
  `mode=actual-team`을 성공 판정으로 쓰지 말라고 명시했다. 이것은 F6 당시의 태도(기준을 통과시키는
  산출물 제작)와 반대다 — 원칙 12가 요구한 **결정요청으로 올리는** 행동이 실제로 나왔다.
- 동시에 **같은 결함의 마지막 잔재가 F10이다.** 자를 못 고치게 하자, 이번엔 자를 적용할 **증거 범위**가
  피측정 레인 손에 남아 있었고 "측정 불가"가 산출됐다. 소유 분리는 자 → 증거경계 → 판정 순으로
  전부 걷어내야 닫힌다.
- Q4·Q5는 **자가 실제 데이터에 닿았을 때만 드러나는 결함**을 새로 노출했다: repaired schema §2의
  "genuine reusable type" 문언은 `DIAG-G04·G05·G07`(1문항 + axis 2개)에 대해 판정 불능이었다.
  `row_kind`는 그 실측에서 나왔다. 자는 문서로 검토해서가 아니라 **돌려봐야** 검증된다.

## 개정 이력 (260829 2차 — Codex 응답 `CODEX_TEAM_RESPONSE_TO_RULING.md` 반영)

작성 주체(메인 루프)가 자기 산출물에 대한 지적을 실측으로 확인하고 반영한다(원칙 8: 승인된
수정은 작성 주체가 반영). 판정 본문은 재작성하지 않고 아래 정정만 덧붙인다(원칙 3 append-only).

**확정된 오류 3건 — 전부 자인한다.**

| # | 위치 | 오류 | 실측 근거 |
|---|---|---|---|
| E1 | BF1 | PASS 마커를 `[OK]`로 인용 | `check_experiment.py:230` = `print(f"experiment-gate: PASS phase={args.phase}")`. `[OK]`는 이 파일에 없다. 형제 도구의 마커를 실측 없이 옮겨 적은 것 — 원칙 9-c-ii가 금지하는 사본 열거 |
| E2 | BF3 / Q5 | span 규칙 `^#{1,6}\s` + "다음 heading 직전"이 S-18에서 깨짐 | 22행 전수 실행: `rule_a(heading only)` → mismatch **2/22** (W-04 48↔49, S-18 146↔148). 138=`## 18.` · 147=`---` · 149=`## 전사 범위·보류` |
| E3 | §0 라벨 | 제안 등급 배우가 `binding` 3건·`approve` 1건 부여 | REV_GUIDE §5 대행 행: "산출물은 **제안 등급**이며 승인·투입 허가를 스스로 부여하지 못한다" — 260828에 내가 직접 쓴 조항 |

**E2의 최소 수리 (신규 실측 — 결론은 유지된다).** 경계 토큰에 수평선
`^(-{3,}|\*{3,}|_{3,})\s*$` 를 추가해 전수 재실행:

```
rule_a(heading only) : mismatches=2/22   W-04(48↔49) · S-18(146↔148)
rule_a + horizontal-rule : mismatches=1/22   W-04(48↔49) 단독
```

따라서 **Q5의 결론(rule_a 정본화, W-04=44–49, 손수정 48 무효)은 살아남고 규칙 문언만 1절
부족했다.** Codex 응답 §3.1이 "21/22와 all rule_a를 동시에 유지할 수 없다"고 한 것과, 필요
개정으로 numeric item-start·appendix·fenced-code·EOF·trailing separator 5종을 나열한 것은
**과대범위**다 — 이 코퍼스가 실제로 요구하는 추가 경계는 수평선 1종이다(§6-d `closure` 의무의
최초 적용 사례).

**Codex 지적 중 수용 — 내 입장이 틀렸던 것 2건.**
- **Q2 (2-key 축소) 철회.** authorization / candidate implementation / qualification / refreeze /
  consume은 **인원수가 아니라 양립 불가 기능의 분리**이므로 "인력 불가"라는 내 반대 근거가
  사실상 틀렸다. 한 배우가 양립 가능한 기능은 겸할 수 있고, 이 저장소의 실제 신원
  (사용자 · 메인 루프 · fresh-context 서브에이전트 · Codex/OMX)만으로 배치 가능하다.
- **Q7 (telemetry 요건 삭제) 수정.** 삭제가 아니라 **작업 착수 조건에서 빼고 actual-team·
  independence 주장에만 남기는** Codex 안이 낫다 — 만족 불가능 기준 회피와 무결성을 둘 다 지킨다.

**Codex 지적 중 부분 수용 — remedy가 과·소한 것 2건.**
- **Q4.** "16은 유일 도출되지 않는다"는 정확하고, 이는 사실 **원칙 12-b가 내게 돌아온 것**이다
  (손으로 박은 상수 16은 자가 아니라 산출물). 다만 Codex의 `report-only` 처방은 게이트를
  비워 원칙 11(기대 카운트는 실측 수치·산술식)과 충돌한다. 제3안: **행을 `generator_id`
  동치류로 정의**하면 최대성이 구성적으로 보장되고, 기대값은 상수가 아니라 **원천 재생성본과의
  diff**가 된다 — "22개 singleton으로 쪼개기"는 동치류 폐쇄 조건에서 자동 실패한다.
- **BF5.** typed claim-to-evidence closure는 F10보다 넓다. F10의 실제 실패는 "동결 산출물이
  `source_path` 열로 직접 지목한 파일 3개 제외"이고 **직접경로 폐쇄만으로 잡힌다.**
  `parent_claim`·`dependency_kind`·전이 깊이·순환 처분은 아직 실패 사례가 0건인 검출기이므로
  원칙 12-d 기준 `follow-up`이다(이 저장소는 이미 마커 존재 검사기 S1·`require_report()`로
  같은 실패형을 두 번 겪었다). 직접경로 폐쇄를 REV_GUIDE §6-d (1)에 규격으로 넣었다.

**처분.** 이 문서는 `proposal-grade`이며, 사용자 지시(260829: "다시 돌리고 다시 테스트한다")에
따라 **재실행 산출물이 나오면 superseded**된다. BF1~BF7은 승인 대상이 아니라 **재실행 라운드의
입력 후보**로 이월한다. 라운드 3(fresh-context 판정)은 **실시하지 않는다** — 판정 대상이 곧
stale이 되므로 REV_GUIDE §3 rule 6-b(동결 입력 밖 신규 선행조건은 차단 사유가 아님)를 적용한다.

## history
- 260829 (2차) · **등급 정정 + 오류 자인.** status `partially-approved` → `proposal-grade —
  superseded-pending-rerun`. 확정 오류 3건(E1 `[OK]` 미실측 인용 · E2 span 규칙 S-18 반례 ·
  E3 권한 초과 라벨). E2 최소 수리 전수 실측으로 결론 유지(rule_a+수평선 → 1/22, W-04 단독).
  Q2·Q7 입장 철회·수정, Q4·BF5 remedy 제3안 제시. 이 라운드의 형식 결함 3종을 막기 위해
  REV_GUIDE §6-d(판정 요청·판정문 표준)와 §3 rule 6(정지 조건)을 신설. 판정 본문 무수정.
- 260829 · 신설. [CC 회람] 260829_01 Q1~Q7 판정. accept 2(Q1·Q6) · revise-required 2(Q2·Q7) ·
  binding 3(Q3·Q4·Q5). 동결 13파일 해시 13/13 독립 재계산, meta_gate·selftest 재실행 일치.
  F6·F9의 "raw 부재" 근거 기각(원천 저장소 실재, 16행·rule_a 재산출). 신규 발견 F10(증거 동결
  경계 자기소유). BLOCKED 판정은 독립성 결격으로 유지. 대상 파일·자·게이트 코드 무수정. 커밋 없음.
