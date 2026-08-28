---
actor: type-extractor
task: EX-english-20242F
target: corpus/EX-english-20242F
status: done
updated: 2026-08-27
---

## 슬라이스 체크포인트

| no | 범위 | state | 산출물 | 비고 |
|---|---|---|---|---|
| 1 | S1 변환 + 사실 header + 선택형 1~10 | done | extracted/2024-2학기/기말/영어.txt 50820 bytes (bindata=1 imgrefs=1) + transcript.md 0~2블록 초안 | hwp2md.py OK 50820 bytes bindata=1 imgrefs=1 |
| 2 | 선택형 11~24 | done | transcript.md 3블록(선택형 11~24 전문) | 배점 2.6~3.5 14건 축자 |
| 3 | 서답형 1~5 + 사실 기록·meta·verify_log 마무리 | done | transcript.md 완료(29문항) + meta.yml(14keys) + verify_log.tsv(8 rows) | 배점 합계 100.0 산술 일치, a+b==m 1/1 해소, unreadable 0건, EQED 0건 |

NEXT: done — type-proposer가 corpus/EX-english-20242F/transcript.md 열람 가능
