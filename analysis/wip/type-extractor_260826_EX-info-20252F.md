---
actor: type-extractor
task: EX-info-20252F refine (Cycle-0 S1, HWP 고사원안 전사)
target: corpus/EX-info-20252F
status: done
updated: 2026-08-26
---

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | 사전 확인(중복·원본 존재·정의 문서 로드) | done | - | EXTRACTION_LOG #62 미착수 확인, 원본 65,536B |
| 2 | S2 hwp2md 변환 | done | extracted\2025-2학기\기말\정보.txt(7,542B) + corpus\_images\EX-info-20252F\bindata | exit 0, [FAIL] 0줄, bindata=1 imgrefs=1 (초회 실행은 dst 부모디렉터리 부재로 실패→디렉터리 생성 후 재실행 성공) |
| 3 | S3 transcript.md 전사 | done | corpus\EX-info-20252F\transcript.md | 25문항(18+7) 전사, imgrefs 1건 해소(a=1,b=0,m=1), EQED 0건 실측, 코드 줄바꿈 레코드 직독 복원, 시행일 불일치 기록(문서=12/15 2교시) |
| 4 | S4 meta.yml + S5 verify_log.tsv | done | corpus\EX-info-20252F\meta.yml(§5.7 14키) · verify_log.tsv(헤더+6행 8열) | 코드블록 원문 일치 자동검증 0누락, TSV 8열 전행 확인 |

NEXT: 없음 — EX-info-20252F refine 완료(status done). 다음 주체: type-proposer
