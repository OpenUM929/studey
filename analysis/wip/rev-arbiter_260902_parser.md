---
actor: rev-arbiter
task: 260831 R5 판정 — GATE 3 잔여 3건 근본원인 재배정 · 파서 수정 승인 · 자 재서명 개시 여부
target: output/260831/rev/260831_07_arbiter_ruling_parser.md
status: done
updated: 260902
---

| no | 범위 | state | 산출물 | 비고 |
|---|---|---|---|---|
| 1 | 동결입력 10건 해시 재측정 | done | (검증) | 10/10 일치. measurer CRLF 329 / lone LF 0 확인 |

| 2 | measure_score_bands.py 소스 정독 + MARK/JOIN/GATE0 수정부 식별 | done | (검증) | L26 MARK lookahead / L32 JOIN / L109-125 GATE0 |
| 3 | 현행 측정기 실행 (파이프 없이 exit 확인) | done | scratchpad/run_new.txt | exit=1 GATE0 PASS GATE1 PASS mism=1 ALL n=510 fit=488 95.7% |
| 4 | 수정 전 파서 복원 2변종 실행 | done | scratchpad/old_A.txt old_B.txt | old=462/440 95.2% mism=3, GATE1 앵커 10/10 OK 양쪽 |
| 5 | 전수 폐쇄 (27 transcript) MARK/JOIN 차분 + 대안 수리 | done | scratchpad/closure.py | MARK drop 2건/1파일, JOIN 9건/3파일, 분포 변경 2/26유닛 |
| 6 | GATE0 fixture 검출력 시험 (4변종 x 5 fixture) | done | scratchpad/closure2.py | line-broken fixture 검출력 0 — JOIN 삭제해도 pass. 최소수리 3/3 |
| 7 | Q4 M5 산술 + 자 stale 위치 + 원장 구조 | done | scratchpad/q4.py q4b.py | L17 라벨 78.8 및 L18 배수표(합 80.5) 둘 다 본문 80.0과 불합치 |

| 8 | EX-history-20242F 주석행 마크 추적 (제4결함 M6) | done | scratchpad/hist.py | L50 주석 재인용 오검출 + L144 [3 .8점 ] 미검출, 개수축 상쇄 21=21 |
| 9 | M6 최소수리 구성 + 전수 실행 | done | scratchpad/fix.py fix.txt | 1/26 변동 79.8->80.0, GATE1 10/10, T2 158->157 T3 193->194 |
| 10 | 판정문 작성 | done | output/260831/rev/260831_07_arbiter_ruling_parser.md | Q1 approve / Q2 revise / Q3 revise(보류) / Q4 approve, 구속 5건 |
| 11 | 원장 2행 추가 + 제약 자기점검 | done | analysis/REV_LOG.md · output/260831/rev/_index.md | 열수 5/8 정상, 커밋 없음(941af21), 자 무접촉 |

| 12 | 라운드 중 요청 측 정정 접수 → 자 stale 전수 재측정 | done | scratchpad/stale.py | 37건/17행(245행), 서명블록 내부 3행. 패킷 7 / 판정자 1차 10 / 요청측 12 전부 과소 |

NEXT: 완료 — 판정문 output/260831/rev/260831_07_arbiter_ruling_parser.md 발행, 구속 5건은 반영 주체 소관
