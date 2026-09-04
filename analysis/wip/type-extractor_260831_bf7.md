---
actor: type-extractor
task: bf7
target: corpus/EX-korean-20252M/{transcript.md,meta.yml,verify_log.tsv}
status: done
updated: 2026-08-31
---

| no | 범위 | state | 산출물 | 비고 |
|---|---|---|---|---|
| 1 | (0) 선행 판별 — 60.4가 원본 인쇄값인지 확인 | done | extracted/2025-2학기/중간/공통국어2.txt 대조 | 원문에 선택형 합계를 명시한 인쇄 줄 자체가 없음(각 문항 인라인 `[N.N 점]`만 존재). 60.4는 260827 전사 시 붙인 집계 주석의 계산 오류로 판정 → 직접 정정(보존+주석 방식 아님) |
| 2 | (1) transcript.md:36 선택형 합계 60.4→60.0, 서술형 합계 25→40 | done | corpus/EX-korean-20252M/transcript.md | 정정 사유 각괄호 주석 병기 |
| 3 | (2) meta.yml:16-17 자기모순 해소 | done | corpus/EX-korean-20252M/meta.yml | 60.0+40=100 정합 명시, confidence=high 근거 "배점 일관"을 실제 확인된 사실로 재기술 |
| 4 | (3) verify_log.tsv corrected 행 추가 | done | corpus/EX-korean-20252M/verify_log.tsv | append-only, 기존 열 규격 준수 |
| 5 | gate 실행 | done | 60.4 count=0(meta/transcript 모두), 60.0 count=2, corrected count=1, Fraction 재현 n=29 sum=60 | 전건 통과 |

NEXT: 없음 — BF7 완결. output/260831_03_arbiter_ruling.md §3 BF7 체크박스는 판정자/메인 루프가 반영.
