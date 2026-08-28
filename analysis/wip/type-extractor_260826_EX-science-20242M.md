---
actor: type-extractor
task: EX-science-20242M
target: origin_data\2024_2학기_1학년_중간\2024_2학기_중간_1학년_통합과학_고사원안.pdf → corpus\EX-science-20242M
status: done
updated: 2026-08-26
---

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | S2 렌더+텍스트 추출 (PDF 7쪽, dpi 160) | done | corpus\_images\EX-science-20242M\p01~p07.png + extracted\2024-2학기\중간\통합과학.txt | median 1441, threshold 576.4, low=[p01 cover 481, ratio 0.33] — 표지 특성으로 정상, 수식 유실 없음 |
| 2 | S3 전사 전반 (표지·선택형) | done | corpus\EX-science-20242M\transcript.md | 29문항 축자, 그림 묘사 포함, 배점 100점 집계 |
| 3 | S3 전사 후반 (서술형·사실기록) | done | corpus\EX-science-20242M\transcript.md | 결번·중복 없음, 서술형 5문항·사실기록 완료 |
| 4 | S4+S5 meta.yml·verify_log.tsv | done | corpus\EX-science-20242M\meta.yml + corpus\EX-science-20242M\verify_log.tsv | 13키 완비, TAB 헤더, G4 low=[p01 cover] 정상 기록 |

NEXT: 완료 — status done. type-proposer가 corpus/EX-science-20242M/transcript.md 개시
