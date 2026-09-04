---
actor: main-loop
task: twokey_m6m7_and_resign
target: tools/measure_score_bands.py(제안만) · analysis/catalog/DIFFICULTY_RUBRIC.md(제안만) · output/260831/260831_19_twokey_m6m7_and_resign.md
status: done
updated: 260903
---

# 슬라이스

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | 자 게이트 현행 상태 실측 | done | — | `regen exit=1` `stale=57 lines=28 residual=18` · `check_assurance_contract 3 failure(s) exit=1` · measure `exit=1` GATE3 mismatches=2 |
| 2 | M6 원인 규명(EX-english-20251M) | done | — | **직전 보고 정정**: 서답형3 흡수가 아니라 **L145 맨숫자 `10`** — 마침표 탈락으로 `TO_SEL` 미발화, 문항10 배점이 sod에 귀속. `JOIN`은 정상(L152 `[3.3점` 확인) |
| 3 | M7 원인 규명(EX-korean-20241M) | done | — | 원본 오타 `(2,8점)` L149. 2.8 근거 2축 독립 일치: 개수 23+1=**24**=선언 · 총점 57.2+2.8=**60.0** |
| 4 | 샌드박스 최소 수리 + 폐쇄 시험 | done | scratchpad/sb/{mkpatch,patched}.py | 3줄 패치. 공통 40유닛 중 **이동 0/40**. GATE3 2→0. 위험면적 맨숫자 줄 전 코퍼스 **7개** |
| 5 | 원칙 12-d 검출력 증명 | done | scratchpad/sb/prove.py | knockout 2건 각각 발화(`undetected=1`·`2`), 거짓양성 fixture 4종 동봉. `prove_exit=0` |
| 6 | 수리 후 자 값 미리 산출 | done | scratchpad/sb/regen_preview.py | 폐쇄 **940/982 = 95.7%**(임계값 불변) · hold-out 92.0% · T 100환산 5/33/39/23 |
| 7 | 결정요청 패킷 §6-d 작성 | done | output/260831/260831_19_twokey_m6m7_and_resign.md | frozen_inputs 11행 · U1~U5 · actor_grade · open/out_of_scope |
| 8 | `rev-arbiter` 발주 1차(⑥(b) 잔여 실측 선행) | **blocked** | — | ⑥(b) ①이 확인 불가라 fail-closed 「부족」 판정 → ⑥(c)2 유계 슬라이스로 발주. **429 session limit 으로 사망**(`resets 1:50pm Asia/Seoul`). 에이전트 회신은 `I'll start by reading...` 1줄 |
| 8-a | 사망 후 산출물 실측(⑥(d)) | done | — | **판정문 미생성**(`output/260831/rev/260831_09*` 없음) · `rev-arbiter` WIP 신규 없음 · 자 3종 해시 불변 · 원장 2종 해시 불변 · HEAD `941af21`. **회신 유실이 아니라 작업 자체가 0** |
| 8-b | resume audit (규격 ⑤) | done | — | 관측 reset `13:50 KST` vs 현재 `14:39 KST` → **경과** · 동결 입력 해시 전건 일치 · 배타 작성권 유지(충돌 writer 없음) · 다음 검증 명령 확보 |
| 8-c | `rev-arbiter` 재개 1회 | in-progress | — | 규격 ⑤ 「reset 뒤 **1회만** 재개」. busy-wait 금지 — 재차 실패 시 재발주하지 않고 사용자 상신 |
| 8-d | 판정 수신·실측(⑥(d)) | done | — | 판정문 34323 B `ef4bc0bd3234b701` · U1~U4 **approve** / U5 **revise-required**(C-1~C-5) · 원장 107행/30행 열오류 0 · 자 3종 해시 불변 · HEAD `941af21` |
| 9 | U4-1 측정기 반영 | **done** | tools/measure_score_bands.py | 승인 4 hunk를 앵커 편집으로 반영 → 결과가 승인본 `patched.py` 와 **바이트 동일** `0cf91284e2c1f7b1`(초과 변경 0 증명). 수용기준 전건 통과: `exit=0` · `[OK]` 1줄 · `[FAIL]` 0줄 · `[GATE 0 PASS]` 1줄 · `planted=9/planted-state=6 undetected=0` |
| 10 | U4-2 정본 재생성기로 지시 취득 | done | — | `A축 32 / B축 2 / stale=55 lines=28 residual=18`. 미리보기(A축 36/B축 0)와 다르므로 **정본 출력만** 지시로 삼았다(U4-2 구속) |
| 11 | C-1 반영기 작성 | done | scratchpad/sb/apply_c1.py | 값을 손으로 타이핑하지 않는다 — `regen`의 역할 정규식·기대값을 임포트해 캡처 자리에 써 넣고 쓰기는 `textpatch.patch`. dry-run 실측 **치환 39자리 / 변경 16행** |
| 12 | 중간 게이트 사전 시뮬(무쓰기) | done | scratchpad/sb/simulate_gate.py | C-1만: `A축 0 / B축 2`. **C-1 + ⑥ append: `A축 0 / B축 0 / C축 잔차 0`** |
| 13 | C-1 + ⑥ 실제 반영 | **done** | analysis/catalog/DIFFICULTY_RUBRIC.md | A축 16행 39자리 + ⑤강등/⑥append. `20294 B/62674856f148e9ce` -> `20921 B/07dab5d38c8da48a`. 개행 무손상(CRLF 255 · lone LF 0 · lone CR 0 · BOM 없음) |
| 13-a | C-4 게이트 (정본) | **done** | — | `stale=0 lines=0 residual=0` · `A 0 / B 0 / C 0` · **regen exit=0**. 중간 게이트뿐 아니라 **최종 게이트까지** 통과 |
| 14 | 재동결 행 + 원장 | **done** | analysis/REV_LOG.md · output/260831/rev/_index.md | 108행/31행, 열오류 0, lone CR 0. `18a9452ffe315ef9` · `189386efe3db78f8` |

## 슬라이스 13 방법 이탈 (보고 대상)

판정 C-1은 `tools/textpatch.py patch` 로 기계 반영하라고 명시했다. 그런데 이 환경의 auto-mode
분류기가 **정본 파일에 쓰는 Bash 실행을 전건 차단**했다 — 스크립트 실행 · 인라인 `python -c` ·
`cp` · 리다이렉션 모두. `textpatch.py` 는 `--self-test` 외 CLI가 없어 라이브러리 호출이 유일한
경로인데 그 경로가 막힌 것이다. 차단 메시지가 지시한 대로 **Edit 도구**로 반영했고, 우회의
실질을 피하기 위해 다음을 지켰다: ① 값은 재생성기의 역할 정규식·기대값에서 **코드가 산출**한
것을 그대로 옮겼다(내가 타이핑한 수치 0개) ② 16행 전건이 파일 내 고유함을 사전 확인했다
③ 반영 후 **정본 재생성기 실행**으로 검증했다(`exit=0`) ④ 개행·BOM 무손상을 바이트로 확인했다.
원장에 이탈 사실을 남겼다.

## ⑤ 강등 + ⑥ append (판정 U4-3 문언과 다른 부분 — 보고 대상)

U4-3은 「L237의 `20662 B / 23d6b87be9714ed6` 를 반영 후 실측값으로 **갱신**」이라 적었다.
그런데 그 줄은 자 본문의 **세대 이력 ①~⑤** 중 ⑤이고 「BF1·BF2·BF3 반영 후」라는 **과거 사실**을
기술한다. 덮어쓰면 260902 재서명이 20662 B에서 이뤄졌다는 기록이 거짓이 된다(원칙 3 위반).
따라서 ⑤의 `**현행**` 표식만 떼어 강등하고 **⑥을 새 현행으로 append** 한다.
`ident_scan`은 `**현행**` 세대만 대조하므로 B축은 이 방식으로도 0이 된다(시뮬 실측).

## 판정 전제와 어긋나는 실측 1건 (원칙 12-a — 우회하지 않고 보고만)

판정 §1-H는 「역할 사각 18자리는 기대값이 없으므로 `stale=0`은 도달 불가」라고 보고 그것을
U5 revise-required의 **유일한 차단 사유**로 삼았다. 그런데 `moved_literals(txt, v)`는 기준선이
아니라 **검사 대상 텍스트 자신**에서 이동 리터럴을 뽑는다(`regen` L419). 따라서 A축 인용이
교정되면 그 18자리는 「이동 리터럴」이 아니게 되어 잔차에서 사라진다 — 18자리는 독립 결함이
아니라 stale 인용의 **부산물**이었다. 시뮬 실측: C-1 + ⑥ 후 `A 0 / B 0 / C 0` → `keys` 공집합
→ `return 0`. 즉 **최종 게이트까지 통과**할 것으로 예측된다.
**이것은 예측이며 정본 재생성기 실행이 진리다.** 자를 고쳐 맞춘 것이 아니라 자를 그대로 두고
쟀다. 판정 개정 요청은 실행 레인이 하지 않는다 — 슬라이스 13 실행 후 실측값으로 상신한다.

## 최종 실측 (종료 시점)

| 게이트 | exit | 비고 |
|---|---|---|
| `measure_score_bands.py` | 0 | `[OK]` 1줄 · `[FAIL]` 0줄 · `[GATE 0 PASS]` 1줄 |
| `regen_rubric_values.py` | 0 | `stale=0 lines=0 residual=0` |
| `check_assurance_contract.py` | 0 | `PASS (0 failures, 12 agents, 12 §5 rows)` — 세션 시작 시 3 failures |
| `textpatch.py --self-test` | 0 | `seeded=10 undetected=0` |

자 3종: `21969 B/0cf91284e2c1f7b1` · `21129 B/259bbfdfc3a6520e`(무접촉) ·
`20921 B/07dab5d38c8da48a`. 원장 108행/31행 열오류 0 · lone CR 0. HEAD `941af21`, 커밋 없음.

NEXT: 없음 — 잔여 2건(자 재서명 · 측정기 파서 결함) 전건 종결. two-key 두 열쇠 모두 성립.
U5의 C-2·C-3은 **판정 대상이 공집합**이 되어 별도 상신이 필요 없다(근거는 원장 260903 행 (6)).
별건으로 남은 것: M5(`EX-science-20242F` 요약행, `type-extractor` 소관) · F4 24유닛 카탈로그 반영.

**자 무접촉 증거(이 시점)**: `measure_score_bands.py` 20662 B `23d6b87be9714ed6` ·
`regen_rubric_values.py` 21129 B `259bbfdfc3a6520e` ·
`DIFFICULTY_RUBRIC.md` 20294 B `62674856f148e9ce`. HEAD `941af21`, 커밋 없음.

NEXT: 슬라이스 8 — `rev-arbiter`에 `260831_19` 판정 발주. 판정문은
`output/260831/rev/260831_09_arbiter_ruling_m6m7_resign.md`. 회신 도착 후 슬라이스 9.
