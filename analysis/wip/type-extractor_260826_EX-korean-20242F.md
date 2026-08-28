---
actor: type-extractor
task: EX-korean-20242F-refine
target: corpus/EX-korean-20242F
status: done
updated: 2026-08-26
---

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | 사전 확인(EXTRACTION_LOG 중복 없음, 소스 존재 130048B) | done | - | row46 미착수 확인 |
| 2 | hwp2md 변환 → extracted/2024-2학기/기말/국어.txt + bindata | done | extracted/2024-2학기/기말/국어.txt(75425B) | exit0·[FAIL]0·bindata=1 imgrefs=1 |
| 3 | transcript.md 전사([[BIN]] 해소 포함) | done | corpus/EX-korean-20242F/transcript.md(494행) | txt와 행 동일 492행+BIN주석2행·선택형24+단답형6=30 결번중복0·BIN0001=엠블럼묘사 해소(a=1,b=0) |

| 4 | meta.yml 13키 | done | corpus/EX-korean-20242F/meta.yml | items=30·answer_key 2건 |
| 5 | verify_log.tsv | done | corpus/EX-korean-20242F/verify_log.tsv | 배치행+BIN0001행, unreadable 0건 |

NEXT: WIP 종결(status=done) 후 3부 헤더 최종 보고
