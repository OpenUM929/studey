---
actor: type-extractor
task: EX-science-20242F
target: origin_data\2024_2학기_1학년_기말\2024_2학기_기말_1학년_통합과학_고사원안.hwp → corpus\EX-science-20242F
status: done
updated: 2026-08-27
---

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | S1 변환+검증 (HWP→TXT, bindata 22) | done | extracted\2024-2학기\기말\통합과학.txt + corpus\_images\EX-science-20242F\bindata\BIN* (22건) | `hwp2md.py --bindata` 실행: `bindata=22 imgrefs=22` 일치 확인, TXT 22622 bytes |
| 2 | S2 이미지 전건 확인 (22건 판독) | done | view_* PNG 렌더 확인 | BIN0001(표지 장식) ~ BIN0016 전건 시각 확인, 그림 묘사 준비 |
| 3 | S3 전사 전반 (표지·선택형 1~12) | done | corpus\EX-science-20242F\transcript.md | 사실헤더+선택형 1~12 축자 전사, EQED 유실부 [unreadable] 인라인 표기 |
| 4 | S3 전사 후반 (선택형 13~24·단답형 1~8) | done | corpus\EX-science-20242F\transcript.md | 24+8=32문항 전사 완료, 결번/중복 없음, 배점 집계 |
| 5 | S4+S5 meta.yml·verify_log.tsv | done | corpus\EX-science-20242F\meta.yml + corpus\EX-science-20242F\verify_log.tsv | 13키 완비, TAB 헤더, transcribe/unreadable 행 기록, a+b==m 검증 |

NEXT: 완료 — status done. type-proposer가 corpus/EX-science-20242F/transcript.md 개시
