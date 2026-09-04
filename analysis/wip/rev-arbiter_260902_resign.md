---
actor: rev-arbiter
task: 260902_resign — 260831_19 패킷 판정 (Q5·Q6·Q7, 자 DIFFICULTY_RUBRIC.md 재서명 개시 여부)
target: output/260831/rev/260831_08_arbiter_ruling_resign.md
status: in-progress
updated: 260902
---

| no | 범위 | state | 산출물 | 비고 |
|---|---|---|---|---|
| 1 | 동결 7건 해시 재검증 + 회신 부재 확인 | done | (검증만) | drift=0. 7/7 일치. 회신 파일 미생성 확인 |
| 2 | 측정기 재실행 (exit·GATE 0/1/2/3·분포) | done | scratchpad/arb_measure_out.txt (102행) | exit=0 확인. GATE0 planted=7 undetected=0 / GATE1 undetected=0 coverage=10/26 / GATE2 dup=1 warn / GATE3 mismatches=0 / sum-axis 8/22 uncovered=14 |
| 3 | BF1 검출력 = 수정 제거 시험 (사본, 원본 무접촉) | done | scratchpad/arb_mutate.py | no-JOIN=1(line-broken) / no-SPACEFIX=1(space-in-number) / no-ANNOT=1(annotation-quote) / no-MARK-lookahead=2(legend-equals,legend-per). 마스킹 반례 재현: SPACEFIX 그리디 + no-JOIN => undetected=0 |

| 4 | 재생성기 독립 검증 + stale 계수 대조 | done | scratchpad/arb_stale.py · arb_stale2.py | 재생성기 stale=31행/17행 exit=1. 판정자 독립 리터럴 판정: 파생값 38건/17행 + 도구정체성 2건/1행(L235) + 오탐 11건. 행집합 불일치 발견 -- 재생성기는 L184 포함/L235 누락, 판정07은 L235 포함/L184 누락 |
| 5 | 서명블록 지문 재현 + hold-out 추적 | done | (검증만) | L10-64+L120-132 = 68행, LF조인+말미LF = a204f3412cf900b5 (판정07 값 재현). hold-out 91.3% 출처 = 판정 260831_04 L174(2024->2025 231/253). 현행 모집단 재계산 = 255/277 = 92.1% -> 이동 |
| 6 | two-key 사슬·FU6 근거 확인 | done | (검증만) | REV_LOG L124에 두 열쇠 기재. 해시 사슬 f60455..->c68366..->23d6b8.. 확인. 요청측 WIP mtime 14:38:05 > 패킷 14:29:20 -> 동결표에 있었으면 drift=1 이었음 |

NEXT: 슬라이스 7 -- 판정문 작성(output/260831/rev/260831_08_arbiter_ruling_resign.md) 후 _index.md·REV_LOG 행 추가
