---
actor: type-extractor
task: EX-english-20242M
target: corpus/EX-english-20242M
status: done
updated: 2026-08-27
---

## 슬라이스 체크포인트

| no | 범위 | state | 산출물 | 비고 |
|---|---|---|---|---|
| 1 | 표지·사실 header + 선택형 1~10 (BIN0001~0005 해소) | done | extracted/2024-2학기/중간/영어.txt 재검증(bindata=6 imgrefs=6) + transcript.md 0~2블록 초안 | hwp2md.py 재실행 OK 49325 bytes bindata=6 imgrefs=6 |
| 2 | 선택형 11~24 | done | transcript.md 3블록(선택형 11~24 전문) | 배점 2.6~3.5 14건 축자 |
| 3 | 서답형 1~6 + 사실 기록·meta·verify_log 마무리 | done | transcript.md 완료(30문항) + meta.yml(14keys) + verify_log.tsv(8 rows) | 배점 합계 100.0 산술 일치, a+b==m 6/6 해소, unreadable 0건, EQED 0건 |

NEXT: done — type-proposer가 corpus/EX-english-20242M/transcript.md 열람 가능
