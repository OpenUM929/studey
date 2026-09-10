---
actor: type-extractor
task: EX-english-20261M_refine
target: corpus/EX-english-20261M/ (transcript.md, meta.yml, verify_log.tsv) + corpus/_images/EX-english-20261M/
status: in-progress
updated: 2026-09-09
---

| no | 범위 | state | 산출물 | 비고 |
|---|---|---|---|---|
| 1 | 렌더(dpi160 전 10쪽) + 회전 실측 + native/ 생성 | done | corpus/_images/EX-english-20261M/p01~10.png, native/p01~10.png | 임베드 이미지 1개/쪽 확인(C-A1-2). 회전각: 물리 홀수쪽(1,3,5,7,9)=-90, 짝수쪽(2,4,6,8,10)=+90 (전 10쪽 육안 대조 확정, EX-social 계열과 동일 alternating 패턴, history-M의 고정 -90과는 다름). 실효 dpi=300(4299x3035 jpeg, round(4299*72/1033.4)) |
| 2 | 표지·인쇄 선언 전사 | done | (transcript.md 작성 대기, 본 슬라이스는 판독만) | 총(9)쪽, 선택형(22)문항, 서술형(6)문항. 물리p01=표지(-90), 인쇄쪽번호는 물리순서와 동일(역순 아님) — p02=1면 ... p10=9면 |
| 3 | 선택형 1~10 판독 | done | — | p02(1,2,3) p03(4,5) p04(6,7+서술형1 지문공유) p05(8,9,10) |
| 4 | 선택형 11~22 판독 | done | — | p06(11+서술형2,12,13) p07(14+서술형3,15) p08(16,17,18) p09(19+서술형4,20) p10(21,22) |
| 5 | 서술형1~6 판독 | done | — | 1@p04 2@p06 3@p07 4@p09 5,6@p10(독립문항, 지문無) |
| 6 | transcript.md/meta.yml/verify_log.tsv 작성 | done | corpus/EX-english-20261M/{transcript.md,meta.yml,verify_log.tsv} | 선택형 합 60.0 + 서술형 합 40.0 = 100.0 내부 정합 확인 |
| 7 | 게이트 실행(S2 펜스 블록) | pending | — | 다음 단계 |

NEXT: S2 게이트 명령(PRD §3 펜스 블록)을 U=EX-english-20261M 로 실행하고 출력을 회신에 원문 그대로 첨부.
