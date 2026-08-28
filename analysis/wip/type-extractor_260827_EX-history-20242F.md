---
actor: type-extractor
task: EX-history-20242F refine (Cycle-0 S1, HWP 고사원안 전사)
target: corpus/EX-history-20242F
status: done
updated: 2026-08-27
---

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | 사전 확인(EXTRACTION_LOG 중복·원본 존재·도구 확인) | done | - | EXTRACTION_LOG #51 미착수 확인, 원본 1,696,256 bytes 존재, hwp2md.py 확인 |
| 2 | S2 hwp2md 변환 | done | extracted/2024-2학기/기말/한국사.txt (24,286 bytes) + corpus/_images/EX-history-20242F/bindata (9건) | `python tools/hwp2md.py ... --bindata` 실행: exit 0, [FAIL] 0줄, `bindata=9 imgrefs=9` 고유 9 일치 |
| 3 | S3 transcript.md 전사(표지·선택형 1~21) | done | corpus/EX-history-20242F/transcript.md (450 lines, 41,415 bytes, 26문항 21+5) | 9 imgrefs 전건 해소, EQED 0건, [unreadable] 0건 |
| 4 | S4 meta.yml 작성(13 keys) | done | corpus/EX-history-20242F/meta.yml (13 keys, confidence high) | id=EX-history-20242F, exam_code=2024-2F, pages=7, items=26, answer_key 2건 |
| 5 | S5 verify_log.tsv 작성(TAB 8컬럼) | done | corpus/EX-history-20242F/verify_log.tsv (header+9 rows, 4,105 bytes) | transcribe 9 rows, unreadable 0, a=9 b=0 m=9 (a+b==m), 8컬럼 TAB 검증 통과 |

NEXT: 완료(status done) — type-proposer가 corpus/EX-history-20242F/transcript.md 참조 가능. 원장 미수정 확인.
