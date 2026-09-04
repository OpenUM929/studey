---
actor: rev-arbiter
task: K1_band_signature
target: output/260831/rev/260831_04_arbiter_ruling_K1.md
status: done
updated: 2026-09-01
---

| no | 범위 | state | 산출물 | 비고 |
|---|---|---|---|---|
| 1 | 요청 패킷 정독 · WIP 개설 | done | - | §6-d 필드 5종 확인 |
| 2 | resume audit(해시 4건 재산출 전건 일치) · 260831_03 §1-2/§2 DQ-X1 원문 대조 · measure_score_bands.py 정독 · 도구 1회 실행 | done | - | GATE1 PASS undetected=0 / dup=1 / mism=2 재현. VALIDATE 6행 = 내 판정문 §1-2 표와 일치. **도구가 §3 정규화 지표(0.80~1.20)를 산출하지 않음** — 패킷 인용값 미실측 의혹 |
| 3 | DIFFICULTY_RUBRIC §1~§3 정독 · 유닛별 단가-적합률 표 독립 산출 · GATE2 오탐 검증(info M/F 원본 해시 상이 확인) · 정규화 지표 재산출 · A/B/C 폐쇄 + 연도 hold-out 예측 시험 | done | - | **M1은 코퍼스 결함 아님 = GATE2 오탐**(원본 hwp 해시 c59de5.. vs 7a1ca5.. 상이, 본문 문항 상이). info-M 복원시 M 4.0+ 0→10건. A 유닛내 0~83.3% 교차, C 70계열 내 0/41.7/83.3% 분열. hold-out: B고정 95.2% > A 79.9% > C 77.6% |
| 4 | Tier 사다리 환산(끝점보존 사상) · §6-A 대조 · U4 전수 grep(26파일) | done | - | 환산컷 0.800/0.8667/0.9667/1.0667/1.200, 분포 5.2/32.3/39.8/22.7 vs §6-A 10/30/40/20. **U4 전제 반증: live 잔여 9건(표 행 6건)** — 패킷 reproduce가 단일 파일로 한정돼 8건 은폐 |
| 5 | 판정문 작성 · _index.md 행 추가 · REV_LOG 행 추가 | done | output/260831/rev/260831_04_arbiter_ruling_K1.md | verdict=revise-required(U1·U2 approve+값 서명 / U3-a·U4 reject / U3-b follow-up). 구속 7건. _index 10필드·REV_LOG 7필드 일치 확인, 본문 파이프 0 |

NEXT: 없음 — 완료. 자 반영(BF-K1-1~3)은 two-key 별도 라운드, 판정자 write surface 아님
