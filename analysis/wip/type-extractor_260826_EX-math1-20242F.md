---
actor: type-extractor
task: EX-math1-20242F 전사(REFINE S1)
target: origin_data\2024_2학기_1학년_기말\2024_2학기_기말_1학년_수학_고사원안.hwp → corpus\EX-math1-20242F
status: done
updated: 2026-08-26
---

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | S2 변환(hwp2md) | done | extracted\2024-2학기\기말\수학.txt + corpus\_images\EX-math1-20242F\bindata | exit 0, [FAIL] 0줄, `bindata=4 imgrefs=4` → m=4 (재실행 검증 2026-08-26 OK 5780 bytes) |
| 2 | S3 증거 추출(EQED 복원·그림 판독) | done | temp para_dump5.txt(슬라이스 증거) | EQED 117/117 배치·스크립트 페어링 확인, 정답지 PDF로 EQ1·7·9·13·21 교차검증 |
| 3 | S3 전사(22문항 축자) | done | corpus\EX-math1-20242F\transcript.md (22문항, 166 lines, 11172 bytes) | 결번 0·중복 0·선언 22문항 일치, imgrefs 4/4 해소 |
| 4 | S4+S5 meta.yml·verify_log.tsv | done | corpus\EX-math1-20242F\meta.yml (13키) + corpus\EX-math1-20242F\verify_log.tsv (11 data rows + header) | TAB 8열, actor=type-extractor, high confidence |

NEXT: — (완료) type-proposer가 corpus/EX-math1-20242F/transcript.md를 열어 유형 제안으로 진행.
