---
actor: type-extractor
task: EX-korean-20252M refine (Cycle-0 S1, HWP 고사원안 전사)
target: corpus/EX-korean-20252M
status: done
updated: 2026-08-27
---

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | 사전 확인(원본 존재·도구 확인) | done | - | 원본 `2025_2학기_중간_1학년_공통국어2_고사원안.hwp` 114,688 bytes 존재, answer_key `2학기 중간고사 정답 - 1학년.pdf` 확인, hwp2md.py 확인 |
| 2 | S2 hwp2md 변환 | done | extracted/2025-2학기/중간/공통국어2.txt (76,440 bytes) + corpus/_images/EX-korean-20252M/bindata/BIN0001.jpg (939 bytes) | `python tools/hwp2md.py ... --bindata` 실행: exit 0, `bindata=1 imgrefs=1` 고유 1건 일치, 추출 725라인 |
| 3 | S3 transcript.md 전사(표지·선택형 1~29·서술형 1~3) | done | corpus/EX-korean-20252M/transcript.md (83,536 bytes, 793라인, 표지+전문축자 32블록) | 선택형 29건 연속·서술형 3블록·지문 전문 축자, [[BIN0001.jpg]] 1/1 해소, [unreadable] 0건 |
| 4 | S4 meta.yml 작성(13 keys, null 포함 14행) | done | corpus/EX-korean-20252M/meta.yml (14 keys, confidence high) | id=EX-korean-20252M, exam_code=2025-2M, pages=null, items=32(29+3), answer_key 1건 |
| 5 | S5 verify_log.tsv 작성(TAB 8컬럼, BOM) | done | corpus/EX-korean-20252M/verify_log.tsv (header+11 rows, 3,591 bytes) | transcribe 11 rows, unreadable 0, a=1 b=0 m=1 (a+b==m), 8컬럼 TAB 검증 통과 |

NEXT: 완료(status done) — type-proposer가 corpus/EX-korean-20252M/transcript.md 참조 가능. 원장(HARVEST_LOG/INDEX) 미수정 확인.
