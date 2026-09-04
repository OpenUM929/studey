---
actor: type-proposer
task: bf_apply (260831_03 판정 구속수정 BF1·BF3·BF4·BF5 반영)
target: output/260831/260831_01_{type_analysis,catalog_update}_{KO,EN,SC,SM2,SS,HI}.md
status: done
updated: 2026-08-31
---

# 슬라이스

| no | 범위 | state | 산출물 | 비고 |
|---|---|---|---|---|
| 0 | 판정문 전문 통독 + 지시문 인용행 원문 대조 | done | — | EN:352-360 · HI:269/275/276/277/278 전건 일치 |
| 1 | §6 재현명령 자체 실행 + math2 배점 출처 확인 + 병합ID 선점조사 | done | — | N=119 fit19(16.0%) max3.3 ge4.0=0 / MR-a 80/99 / MR-b 119/119 / old 67/119 **전건 일치**. math2 18/18은 인라인마커(16건)가 아니라 `transcript.md:20` 계수선언 18값에서 유도됨(8·16번 인라인 마커 부재, 53.2 = 60.0−3.2−3.6 검증) → 출처 병기 필요. 병합ID `DQ-RUBRIC-1` 미선점 확인(CODE_REGISTRY §1·§3·§5에 DQ 네임스페이스 부재) |

| 2 | BF1 반영 (type_analysis_EN.md §4-D) | done | type_analysis_EN.md:347-397 | 열머리 단일축 재정의 + 6과목 실측표 + 3층표(강 6/6 · 중 3/6 · 예외 3/6) + 승격금지·k/N병기 의무 명시. 게이트: 표 행 내 구 토큰 **0건**, 잔여 3건은 전부 「정정 이력」 인용(원칙 3 이력 보존) → 절 「지시문과의 불일치」에 보고 |

| 3 | BF3+BF4 반영 (catalog_update_HI.md) | done | HI.md:269-317 | 3-C 표에서 RUBRIC 3행 제거(잔여 6행 유지·메인루프 소관) → 신설 3-C-2(two-key 소관) + 3-C-3(병합 포인터). §1척도표 제안 🚫철회 + MR-a/MR-b 대조표. C-07 행(L275) 무수정 확인 |
| 4 | BF5-1 병합 유닛 정본 작성 + 5개소 포인터 | done | SM2.md §DQ-RUBRIC-1 / KO·EN·SC·SS·HI 포인터 | 병합ID **`DQ-RUBRIC-1`**. SS:312 밴드→T4 유도문 제거(판정 §1-6 실증사례) |

| 5 | BF5-3 Tier 표식 (문서 배너 + 절 머리) | done | 11개 문서 | 방식: **① 문서 최상단 배너 1건 + ② Tier 값이 실제로 등장하는 절 머리 마커**. 절 마커 34건(오탐 3건 제거 후). Tier 토큰 0인 catalog_update_SC는 대상 제외 |
| 6 | 병합에 따른 stale 참조 정정 | done | 8개소 | DQ-SM2-1/KO-2/EN-1/SC-3 → `DQ-RUBRIC-1` |

| 7 | 전체 게이트 재실행 + write surface 검증 | done | — | 판정문 §6 전건 재현(BF7 반영 코퍼스 기준에서도 동일). 구조 게이트 전건 통과. `analysis/catalog/` changed=0 (자 무편집 확인). corpus/·rev/·REV_LOG 변경분은 **병렬 배우(type-extractor BF7 · rev-writer BF2) 소관**이며 내 작업 아님 |

NEXT: (없음 — BF1·BF3·BF4·BF5 반영 완료. 잔여 open = X1(K1 사용자 키 대기, 내 소관 아님))
