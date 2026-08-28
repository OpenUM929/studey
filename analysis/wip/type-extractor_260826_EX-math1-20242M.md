---
actor: type-extractor
task: EX-math1-20242M
target: origin_data\2024_2학기_1학년_중간\2024_2학기_중간_1학년_수학_고사원안.hwp → corpus\EX-math1-20242M
status: done
updated: 2026-08-26
---

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | S2 변환(hwp2md) | done | extracted\2024-2학기\중간\수학.txt + bindata | exit0·[FAIL]0·bindata=1 imgrefs=1 — 단, EQED 수식 전량 무흔적 삭제 확인(결함 경고대로) |
| 2 | S3 전사 전반(문항 1~10) | done | corpus\EX-math1-20242M\transcript.md | EQED 복원: pyhwp ViewText(distdoc) 레코드 직접 파싱, 161 marker=160 script+빈 개체 1 |
| 3 | S3 전사 후반(나머지) | done | corpus\EX-math1-20242M\transcript.md | 22문항(18+4) ±0, 결번·중복 없음, 분절 수식 3건 ⌈⌉ 표기 |
| 4 | S4+S5 meta.yml·verify_log.tsv | done | corpus\EX-math1-20242M\meta.yml 외 | 13키·TAB 헤더, unreadable 0건(빈 수식 개체는 판독불가 아닌 '내용 없음' 실증) |

NEXT: 완료 — status done. type-proposer가 corpus/EX-math1-20242M/transcript.md 개시
