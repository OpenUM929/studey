---
actor: type-extractor
task: EX-social-20242F refine (Cycle-0 S1, HWP 고사원안 전사)
target: corpus/EX-social-20242F
status: done
updated: 2026-08-27
---

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | 사전 확인(중복·원본 존재·도구 확인·EXTRACTION_LOG 미등재 확인) | done | - | 원본 hwp 존재(~3.6MB), 변환 도구 hwp2md.py 확인, 중복 없음 |
| 2 | S2 hwp2md 변환 | done | extracted/2024-2학기/기말/통합사회.txt(28362B) + corpus/_images/EX-social-20242F/bindata(16개) | exit 0, bindata=16 imgrefs=16, a+b==m 16/16, [FAIL] 0건 |
| 3 | S3 transcript.md 전사([[BIN]] 전건 해소 포함) | done | corpus/EX-social-20242F/transcript.md(305 lines, 18954 chars, 16개 BIN 인라인 판독) | 선택형 20 + 단답형 4 =24문항 축자, 결번·중복 0, 변환 문자 전량 보존, 그림 의존성 명시 |
| 4 | S4 meta.yml + S5 verify_log.tsv | done | corpus/EX-social-20242F/meta.yml(14 keys) · verify_log.tsv(header+9 rows, TAB 8컬럼, actor=type-extractor) | §5.7 14키, §5.7-A 8컬럼 검증 통과, unreadable 0건, confidence=high |

NEXT: 완료(status=done) — 다음 주체: type-proposer가 corpus/EX-social-20242F/transcript.md 열어 유형 제안서로 진행.
