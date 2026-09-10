---
actor: type-extractor
task: EX-history-20261M_refine
target: corpus/EX-history-20261M
status: done
updated: 2026-09-09
---

# WIP — type-extractor EX-history-20261M (Cycle-1 wave-1)

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | dpi160 렌더(전 8쪽, G1 분모) | done | corpus/_images/EX-history-20261M/p01~p08.png | PyMuPDF dpi=160, 원본 rotation=0 메타 그대로(미보정) |
| 2 | 회전 실측 + native/ 생성 | done | corpus/_images/EX-history-20261M/native/p01~p08.png (3035x4299, rotate(-90) 고정) | 임베드 이미지 전건 1개(4299x3035 jpeg), 실효dpi=round(4299*72/1033.4)=300. 전 8쪽 육안 대조: -90 고정(EX-social과 달리 홀짝 교대 아님). 2단 인쇄이나 분할 불요(단일 이미지로 legible). PDF스캔순서 역순=인쇄순서: p01=인쇄7면(서술형1-5,표지제외 마지막)/p02=6면(24-25)/p03=5면(19-23)/p04=4면(14-18)/p05=3면(10-13)/p06=2면(5-9)/p07=1면(1-4,'선택형 문항' 헤더)/p08=표지 |
| 3 | 표지·인쇄 선언 전사 | done | (본 WIP에 기록, transcript.md 작성 시 반영 예정) | 표지(p08): "2026학년도 1학기 (1)학년 (한국사1)과 중간고사 문제지" / "총(7)쪽, 선택형(25)문항, 서답형(5)문항" / 고사반영비율 중간30%·기말30%·수행40% / 유의사항 1~5 |
| 4 | 문항 전반부 전사 (선택형 1~13, 인쇄1~3면) | done | corpus/EX-history-20261M/transcript.md | native/p07(1~4)·p06(5~9)·p05(10~13) 축자 완료, 도표 문항(1,4,5,9) 이미지 서술 포함 |
| 5 | 문항 후반부 전사 (선택형 14~25, 인쇄4~6면) | done | transcript.md | native/p04(14~18)·p03(19~23)·p02(24~25) 축자 완료, 조직도(15)·표(18) 서술 포함 |
| 6 | 서답형(서술형1~5, 인쇄7면) + meta/verify_log 마감 | done | transcript.md, meta.yml, verify_log.tsv | native/p01 서술형1~5 축자 완료(빈칸만, 학생 답안 손글씨 제외). meta.yml 9키 + 참고주석, verify_log 11행(TSV) 작성. 배점 합계 60.0+40.0=100.0 내부 정합 확인 |
| 7 | 게이트 7축 실행 | done | (메인 루프 규격⑤ 독립 실행, ⑥(d) 회람) | 메인 루프가 PRD §3 펜스 블록을 문면 그대로 `U=EX-history-20261M`으로 독립 실행: `pages=8` `unit_files=3` `typeid_hits=0` `present=3 empty=0` `[GATE 0 PASS] undetected=0` `[FAIL] GATE 3 mismatches=2 -- EX-history-20261F EX-social-20261M`(본 유닛 ID는 그 줄에 없음 → G2-a PASS, FA3 판정 방법 적용 — EX-history-20261F는 타 에이전트 작업 중 유닛, EX-social-20261M은 gate-exempt 유닛) `item_heads=30 declared_items=30` `stderr 0줄`. 7축 전건 통과 |

NEXT: 없음 — 전 슬라이스 완료(status: done). corpus/EX-history-20261M/{transcript.md,meta.yml,verify_log.tsv} + corpus/_images/EX-history-20261M/{p01~p08.png, native/p01~p08.png} 산출 확정
