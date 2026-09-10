---
actor: type-extractor
task: EX-history-20261F_refine
target: corpus/EX-history-20261F/
status: done
updated: 2026-09-09
---

| no | 범위 | state | 산출물 | 비고 |
|---|---|---|---|---|
| 1 | dpi160 전 8쪽 렌더 | done | corpus/_images/EX-history-20261F/p01~p08.png | rect 1033.4x729.6, 1 embed/page, 확인 완료 |
| 2 | 회전 실측 + native/ 생성 | done | corpus/_images/EX-history-20261F/native/p01~p08.png | 홀수=-90/짝수=+90 (전 8쪽 육안 대조), 4299x3035 jpeg, 실효dpi=300, 분할 불요(좌우2열 1장) |
| 3 | 표지·인쇄 선언 전사 | done | corpus/EX-history-20261F/transcript.md | 총(7)쪽, 선택형(24)문항, 서답형(6)문항. variant=student(필기 다수 관측) |
| 4 | 문항 1~13 전사 (p02-p04) | done | corpus/EX-history-20261F/transcript.md | 배점 합 1~13 확인 |
| 5 | 문항 14~24 전사 (p05-p07) | done | corpus/EX-history-20261F/transcript.md | Q16 그래프, Q18 지도, Q21 사진 확대 판독 완료 |
| 6 | 서답형 1~6 전사 (p08) + meta/verify_log 작성 | done | corpus/EX-history-20261F/{meta.yml,verify_log.tsv} | 429로 회신 유실 후 규격⑤ 1회 재개 — transcript.md(이미 작성됨)를 읽어 meta.yml·verify_log.tsv만 신규 작성, 전사 재작업 없음 |
| 7 | 게이트 실행 | done | (회신 원문 첨부) | 최초 실행 시 G2-a FAIL(declared 24/extracted 25, sum 83.5) — 원인은 Q3 항목 설명 각주에 배점 "[3.5점]"을 본문과 중복 기재한 전사자 실수(섹션3 함정#1과 동일 유형). 각주 수정 후 재실행 전건 PASS |

NEXT: 없음 (유닛 완료). 이후 단계는 type-proposer의 S3 분류.
