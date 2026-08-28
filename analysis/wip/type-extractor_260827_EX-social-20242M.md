---
actor: type-extractor
task: EX-social-20242M refine (Cycle-0 S1, HWP 고사원안 전사)
target: corpus/EX-social-20242M
status: done
updated: 2026-08-27
---

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | 사전 확인(중복·원본 존재·도구 확인·EXTRACTION_LOG 미등재 확인) | done | - | 원본 3,648,000B 존재, 변환 도구 hwp2md.py 확인, 중복 없음 |
| 2 | S2 hwp2md 변환 | done | extracted/2024-2학기/중간/통합사회.txt(30,876B) + corpus/_images/EX-social-20242M/bindata(16개) | exit 0, [FAIL] 0건, bindata=16 imgrefs=16, a+b==m 16/16 |
| 3 | S3 transcript.md 전사([[BIN]] 전건 해소 포함) | done | corpus/EX-social-20242M/transcript.md(377 lines, 22,177 chars, 16개 BIN 판독 병기) | 선택형 24 + 서답형 4 =28문항 축자, 결번·중복 0, 변환 문자 전량 보존, 그림 의존성 명시 |
| 4 | S4 meta.yml + S5 verify_log.tsv | done | corpus/EX-social-20242M/meta.yml(14 keys) · verify_log.tsv(header+9 rows, TAB 8컬럼, actor=type-extractor) | §5.7 14키, §5.7-A 8컬럼 검증 통과, unreadable 0건, confidence=high |

NEXT: 완료(status=done) — 다음 주체: type-proposer가 corpus/EX-social-20242M/transcript.md 열어 유형 제안서로 진행.
