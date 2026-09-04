---
actor: 메인 루프
task: escalation — 상신 3건(게이트 exit 반전 · U7 진입 게이트 정밀화 · §6-b 기입 순서) 패킷화 및 판정 요청
target: output/260831/260831_16_arbiter_escalation_gates.md
status: done
updated: 260902
---

## 근거
`analysis/wip/mainloop_260901_bfrf_apply.md` §발견 8 · §발견 9 · §6-b (f) 순서 보강.
전건 **원칙 12-a** 이행 — 동결된 자·수용기준이므로 실행 레인이 고치지 않고 상신한다.

## 슬라이스

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | §6-d 규격 정독 (요청 패킷 6필드 + closure 의무) | done | — | REV_GUIDE:424-496 |
| 2 | E1 fixture — exit code 4셀 시험 (샌드박스) | done | 아래 §E1 | 반전 실증 2/2 |
| 3 | E2 실측 — 진입 게이트 현행값 | done | 아래 §E2 | repo 34매칭/11파일 |
| 4 | E3 실측 — 260901 해시 리터럴 모집단 | done | 아래 §E3 | REV_LOG 32건 중 오기 3종 |
| 5 | 동결 입력 해시 재측정 | done | 아래 §동결 | 지문 68행 불변 |
| 6 | 패킷 작성 | done | _16_ | §6-d (1) 6필드 |
| 7 | U6 게이트 무오염 확인(패킷 작성 후) | done | 잔여 0건 | 자기오염 없음 |
| 8 | 원장 2건 행 추가 | done | `_index.md` R4 · `REV_LOG` | `_index` state 줄 갱신 포함 |
| 9 | 마감 시점 재측정(E3 규칙 자기적용) | done | 아래 §마감 | 패킷 E2 표에 3시점 반영 |
| 10 | rev-arbiter 발주 + 회람문 출력 | done | — | 규격 ⑥(b) 통과 기록 |

## §마감 — 모든 기록 완료 후 재측정 (E3가 요청하는 규칙을 스스로 적용)

| 대상 | 값 |
|---|---|
| U6 동결 게이트 잔여 | **0줄** (패킷·원장 작성 후에도 무오염) |
| `축 보류` repo 전수 | 34 → 45 → **47 / 14파일** (3시점, E2 사실 ① 실증) |
| `_01_*` 한정 `축 보류` / `열 축 보류` / `Tier 재도출 대기` | **2 / 0 / 0** |
| 자 `DIFFICULTY_RUBRIC.md` | `3a1b609b46855485` (무수정) |
| 측정기 `measure_score_bands.py` | `f60455c6fc0d8ca9` (무수정) |
| 서명 블록 지문(동결 명령) | **68행 / `a204f3412cf900b5`** (불변) |
| 패킷 `260831_16_...md` | 12586 B / `5e1dfdfb8c579b12` |
| `_index.md` / `REV_LOG.md` | `b3c03af62b652f0a` / `7f34f6a53d783eba` |

## §E1 — 게이트 exit code 반전 fixture (샌드박스 실행, 실원장 무접촉)

샌드박스: `scratchpad/gatefix/output/260831/` (실 27파일 복제). 실 `output/260831/` 무수정.

| 상태 | 동결형(끝단 grep) | 제안형(`\| wc -l`) |
|---|---|---|
| LIVE 0건 (통과) | `exit=1` | `out=0 exit=0` |
| LIVE 1건 주입 (실패) | `exit=0` | `out=1 exit=0` |

주입 fixture: `이 회차의 선택(단답)형 비중은 60.4 이다.` (1줄, 샌드박스 전용)
→ **동결형은 exit code를 읽는 자동화에서 2/2 셀 모두 오판**. 제안형은 2/2 정분류.

## §E2 — U7 진입 게이트 현행 실측

동결 문구: `grep -rc "축 보류"` = 0 (경로 인자 없음 → repo 전체 재귀)

- repo 전체 매칭 **34건 / 11파일**. 그중 **27건**이 게이트를 논하는 WIP·판정문·패킷.
  (판정문 `260831_05` 자신이 5건 기여 — U6에서 폐기된 자기오염 구조와 동형)
- U7 대상 산출물 한정: `grep -rn "축 보류" output/260831/260831_01_*.md | wc -l` = **2**
- 제안형: `grep -rn "열 축 보류" output/260831/260831_01_*.md | wc -l` = **0**
- `grep -ro "Tier 재도출 대기" output/260831/260831_01_*.md | wc -l` = **0**

## §E3 — 260901 해시 리터럴 모집단

REV_LOG 260901 행 9개에 16-hex 리터럴 **32회 / 고유 19종**.
오기 3종 전부 **같은 원인** — 편집을 끝내기 전에 값을 기입:
`05f4f3d0d2952134`(자 정정 전) · `bd8dea2c8ed4b47b`(측정기 14337 B 주장) · `d1e6f5…`(판정문 접두어 창작).
이번 라운드 자체가 같은 함정을 1회 더 재현했다 — 지문을 단일 `awk` 2범위로 재측정해 `70행 /
e4423614da073c51`을 얻었으나, 동결 명령은 `awk` 2회 + 각 `sed '$d'`이며 재실행값은 `68행 /
a204f3412cf900b5`(불변). **다른 명령은 다른 값을 낸다** — type-proposer의 `sed -n '1,68p'` 오류와 동형.

## §동결 — 이 라운드 입력 해시 (기입 직전 실측)

| path | bytes | sha16 |
|---|---|---|
| analysis/catalog/DIFFICULTY_RUBRIC.md | 20058 | 3a1b609b46855485 |
| tools/measure_score_bands.py | 14731 | f60455c6fc0d8ca9 |
| output/260831/rev/260831_05_arbiter_ruling_refreeze.md | 38294 | 6c93e096b986e9f6 |
| output/260831/260831_15_arbiter_refreeze_request.md | 12932 | 2ba84f24aa2fde08 |
| analysis/REV_GUIDE.md | 42178 | ecb54fd74c08f0c3 |
| CLAUDE.md | 36245 | c5ce263fe3594c84 |

서명 블록 지문(U5 동결 명령 원문) = **68행 / `a204f3412cf900b5`** — 불변.

## §규격 ⑥(b) 발주 전 잔여 실측 (260902)

① 잔여 토큰 예산 **14,887,338 / 15,000,000** (호스트 계측치, 이 턴 실측)
② 이 세션이 겪은 rate limit: 429 1회, 기록 위치 `analysis/wip/mainloop_260901_k1_ruler_apply.md:104`
   (session limit, 관측 reset **1pm Asia/Seoul**). 현재 260902 — **날짜 경과로 reset 소진 완료**이며,
   reset 이후 Opus 레인이 실동작한 증거가 남아 있다(260902 `solve-back-verifier` 93제 완주,
   `REV_LOG` 260902 행).
③ 직전 동종 작업 실소요: `rev-arbiter` 판정 `260831_05` 1회 완주(38294 B 산출) ·
   같은 세션 `solve-back-verifier` 93문항 완주.
→ **통과**. 유계 3-unit 패킷이므로 슬라이스 분할 없이 1회 발주.

NEXT: **완료** — 판정 `260831_06` 수령(E1·E2·E3 전건 approve, 조건 3건). 반영은 `analysis/wip/mainloop_260902_gate_apply.md`로 이어진다.
