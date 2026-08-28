---
actor: type-extractor
task: EX-history-20242M
target: corpus/EX-history-20242M
status: done
updated: 2026-08-27
---

# WIP — type-extractor EX-history-20242M

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | 변환(hwp2md) + 이미지 수율 점검 | done | extracted/2024-2학기/중간/한국사.txt (27244 bytes, bindata=7 imgrefs=7, 고유 7) | `python tools/hwp2md.py ... --bindata corpus/_images/EX-history-20242M/bindata` 재실행 완료(260827), bindata 7건=BIN0001~0007 전량 보존 |
| 2 | 표지·header + 선택형 1~12 축자 전사 | done | corpus/EX-history-20242M/transcript.md (선택형 1~12 완료) | BIN0003/0005/0001/0002/0007 해소 반영 |
| 3 | 선택형 13~24 + 서술형 1~4 축자 전사 + 사실 기록 4축 | done | transcript.md (선택형 13~24, 서술형 1~4, 사실기록 5절 완료) | 전 문항 28문항 축자 완료, 배점 60+40=100 대조 |
| 4 | 이미지 마커 해소(a+b==m) + 배점·문항수 대조 | done | transcript.md 내 해소 블록(7/7) | bindata=7 고유=7 마커 8(중복1)·a=7 b=0 m=7 → a+b==m, 미해소 0 |
| 5 | meta.yml(13 keys) + verify_log.tsv(TAB) 작성 | done | corpus/EX-history-20242M/meta.yml, verify_log.tsv | 13키 완비, TSV TAB header + 8행 |

NEXT: 없음 — 전 슬라이스 완료, status done으로 전환 예정
