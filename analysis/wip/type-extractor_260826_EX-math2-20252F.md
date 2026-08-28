---
actor: type-extractor
task: EX-math2-20252F refine (Cycle-0 S1, HWP 고사원안 전사)
target: corpus/EX-math2-20252F
status: done
updated: 2026-08-26
---

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | S2 hwp2md 변환 | done | extracted\2025-2학기\기말\공통수학2.txt + bindata | exit 0·[FAIL] 0·bindata=5 imgrefs=5 |
| 2 | S2-b 수식 복구(HWP 레코드 판독) | done | (스크래치패드 rebuilt2.txt) | hwp2md는 수식 전량 유실 → pyhwp 레코드에서 EQED 스크립트 180건 직접 판독·문단 재조립. 추측 복원 아님 — 원본 스크립트 해독 |
| 3 | S3-a 그림 5건 판독 | done | corpus\_images\EX-math2-20252F\bindata | a+b==m: 5+5==5 imgrefs 전건 해소, unreadable 0 |
| 4 | S3-b transcript.md 전사 | done | corpus\EX-math2-20252F\transcript.md | 23문항 verbatim + 사실 기록, 유형 판단 0 |
| 5 | S4+S5 meta.yml·verify_log.tsv | done | corpus\EX-math2-20252F\meta.yml, verify_log.tsv | §5.7 13키(high) · verify_log 9행(transcribed만, unreadable 0) |

비고: 12·13·17번 기호 범위는 정답지 값(−4·6·0<m<1/6)으로 확정 — verify_log 3~5행. 5·12번 슬롯 재부착 2건 — 6~7행. method 필드는 지시문 문자열에 "EQED 레코드 판독"을 추가한 실측 기술.

NEXT: 없음 — S1 refine 완료. 다음 주체 type-proposer
