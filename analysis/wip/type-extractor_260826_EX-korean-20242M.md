---
actor: type-extractor
task: EX-korean-20242M 전사(REFINE S1)
target: corpus/EX-korean-20242M
status: done
updated: 2026-08-26
---

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | 사전 확인(EXTRACTION_LOG #40 중복검사·원본·도구 존재) | done | - | 중복 없음(#40 미착수) |
| 2 | S2 HWP 변환(hwp2md.py → extracted txt + bindata) | done | extracted/2024-2학기/중간/국어.txt | exit 0, [FAIL] 0줄, `bindata=1 imgrefs=1` → m=1 |
| 3 | S3 transcript.md 전사(전문 읽기 → verbatim 전사 + 마커 해소) | done | corpus/EX-korean-20242M/transcript.md | 41 세그먼트 분절(프로그래밍 분할, 원문 문자 무변경). BIN0001 해소 1/1(학교 로고 그래픽 묘사), unreadable 0. 선택형 1~24 결번·중복 0, 서답형 4블록 |
| 4 | S4 meta.yml(13키) | done | corpus/EX-korean-20242M/meta.yml | items=28(선택형24+서답형4), confidence=medium(행갈림 평탄화) |
| 5 | S5 verify_log.tsv | done | corpus/EX-korean-20242M/verify_log.tsv | transcribe 13행, unreadable 0행, 8열 TAB 검증 통과 |
| 6 | S6 WIP 종료 | done | 본 파일 | status=done |

NEXT: 없음 — EX-korean-20242M 전사 완료. 다음 주체: type-proposer (Claude Code)
