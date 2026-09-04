---
actor: type-extractor
task: EX-social-20261M_refine
target: corpus/EX-social-20261M/ (transcript.md, meta.yml, verify_log.tsv) + corpus/_images/EX-social-20261M/
status: done
updated: 260904
---

## 슬라이스 표

| no | 범위 | state | 산출물 | 비고 |
|---|---|---|---|---|
| 0 | 렌더 (전 8쪽) | done | corpus/_images/EX-social-20261M/p01~p08.png (dpi=160) | PyMuPDF, 원본 sha256[:16]=792f24802cd81057 bytes=3729153 확인 일치 |
| 1 | p01(표지)+p02(1~4번) | done | 판독 완료 | 표지 인쇄 선언 확보. 각 페이지가 좌우 2열(=2개 실제 쪽)로 스캔됨, 회전방향 페이지마다 다름(짝수 홀수 불규칙) 확인 후 개별 회전 처리 |
| 2 | p03(5,7번)~p08(단답형1,2) | done | 판독 완료 | **중대 발견**: 문항 2,4,5,7,10,12,14,22,24가 쪽 하단에서 본문/선택지가 절단됨. 문항 6,8,16,18,21,23은 전 8쪽 어디에도 존재하지 않음(고배율 재확인 포함 3회 대조). 단답형3 도 전 8쪽에 없음. 단답형1 분류표, 단답형2 후반부도 절단. 완화 없이 unreadable 행으로 기록 예정(허용오차 차0) |
| 3 | transcript.md/meta.yml/verify_log.tsv 작성 | done | corpus/EX-social-20261M/{transcript.md,meta.yml,verify_log.tsv} | 문항별 완결/부분판독/미발견 3분류로 기록, unreadable 행 18건(transcribe 9행 포함 총 27행) |
| 4 | 정제 게이트(PRD §3 S2) 실행 | done | (return값에 기록) | pages=8 unit_files=3 typeid_hits=0 present=3 empty=0 — 전건 기대치 일치 |

NEXT: (없음 — 유닛 완료) type-proposer가 corpus/EX-social-20261M/transcript.md를 열어 S3 분류 진입. 단, 인쇄 선언(27문항) 대 전사 확인(20문항, 그중 완결 9)의 차 0 불일치가 실재하므로 메인 루프가 이 사실을 S3 발주 회람문에 명시해야 한다.
