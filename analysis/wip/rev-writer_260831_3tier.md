---
actor: rev-writer
task: 3tier_review_R1
target: output/260831/*_type_analysis_*.md, *_catalog_update_*.md (6 subjects)
status: in-progress
updated: 260831 (round 2)
---

# WIP — 3-tier Review Round 1 Tier-1 (2025-2중간 전과목)

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 0 | 공통 차단조건 실측(INT-1/INT-2/INT-5, CP-SM2-1, CP-HI-1, ID충돌) | done | (본 WIP 하단 근거) | corpus/_images 20252M 전 과목 bindata만 존재(png 0) 확인; science 배점 22↔40 재현; curriculum_2022 2학기 절 math2만 존재 확인; CP-HI-1 9/9 재현; DQ-SS-1/DQ-HI-1은 CODE_REGISTRY §2+§6(b)로 기존 해소 확인; DQ-EN ID건은 catalog_update_EN.md 자체가 "결정요청 불필요"로 이미 자답 |
| 1 | 국어(KO) type_analysis+catalog_update | done | output/260831/rev/260831_01_review_KO.md | 서술형 배점 40 재현(13+15+12) 확인, 문항수 32 일치 |
| 2 | 수학2(SM2) type_analysis+catalog_update | done | output/260831/rev/260831_01_review_SM2.md | DQ-SM2-1~3 근거 확인, 문항수 22 |
| 3 | 영어(EN) type_analysis+catalog_update | done | output/260831/rev/260831_01_review_EN.md | T-13/W-05 ID 자답 "불필요" 확인 — relay Q4-Q7 묶음 오분류 지적 |
| 4 | 통합과학(SC) type_analysis+catalog_update | done | output/260831/rev/260831_01_review_SC.md | INT-2 배점 22→40 재현, 선택60.0+서술40=100.0 확인 |
| 5 | 통합사회(SS) type_analysis+catalog_update | done | output/260831/rev/260831_01_review_SS.md | DQ-SS-1 CODE_REGISTRY §2/§6(b) 기결 확인 |
| 6 | 한국사(HI) type_analysis+catalog_update | done | output/260831/rev/260831_01_review_HI.md | CP-HI-1 9/9 재현, F-09~11 신규 템플릿 13필드 준수 확인, ★축 표기 준수 확인 |
| 7 | _index.md 6행 등재 | done | output/260831/rev/_index.md | — |
| 8 | REV_LOG.md 행 추가 | done | analysis/REV_LOG.md | — |

| 9 | 수신 회람문 사실검증(N3/N4/N5 재현) | done | (본 WIP 하단 근거) | tier-2 실보고서(`260831_01_type_analysis_all_review_second.md`)·소스(transcript.md·DIFFICULTY_RUBRIC.md) 직접 대조 — 회람문이 N3/N4/N5를 전부 review_HI.md 소관으로 오서술("2.2점 문항 4개"·"history.md L258~265"·"[미읽음]" 전부 원문 미확인/사실무근), 실제로는 N3=type_analysis_HI.md:385(type-proposer 소유)+F-HI-2 대조범위 누락, N4=review_SM2.md:80, N5=review_KO.md:46-49·75-78. 회람문 지시를 그대로 적용하지 않고 실제 소유·내용대로 정정 |
| 10 | review_KO.md Round 2 정정 | done | 260831_01_review_KO.md | N1(60.4→60.0, transcript.md:36 29개값 재합산 정수합600 검증)·N5(DIFFICULTY_RUBRIC.md L14-16·L19·L152-154 직접 재열람, confirmed→confirmed(재열람 후)) 반영, DQ-KO-1 결론 불변 확인 |
| 11 | review_SM2.md Round 2 정정 | done | 260831_01_review_SM2.md | N2(CP-SM2-1 기각→약화+2층분리, 6과목 전수 60:40/40:60 재실측)·N4(HI 40:60 증거경로를 `EX-history-20252M/transcript.md` 직접실측으로 교체) 반영 |
| 12 | review_HI.md Round 2 정정 | done | 260831_01_review_HI.md | N3 실측(transcript.md 문항 1·4·6·7·9·10·11 원문 `[2.2 점]` 태그 확인, 7개) — F-HI-2 총합·40:60 근거 무결 재확인, CP-HI-2 세부주장 미대조 누락 인정 및 type-proposer 앞 체크박스 신설 |
| 13 | _index.md round 2 등재 + REV_LOG 행 추가 | done | output/260831/rev/_index.md · analysis/REV_LOG.md | KO/SM2/HI 3행 reflect_state=fixed, header round:2 |

NEXT: tier-2(rev-auditor) round 2 독립 cross-check 대기. 라운드 상한 5회 중 2회 소진.

| 14 | tier-3(260831_03) BF2 반영 (owner-fix, 검토 아닌 반영) | done | 상세는 별도 WIP `analysis/wip/rev-writer_260831_bf2.md` 참조 | tier-3가 CP-SM2-1을 3/6으로 최종 종결(guardrail, 재론 금지) → 추가 검토 라운드 없이 owner-fix로 review_SM2.md·review_KO.md 3건 정정, _index.md·REV_LOG.md 흔적 행 추가 |

NEXT(갱신): 이 3-tier 라운드 자체는 tier-3 판정으로 종결(open={X1}, 사용자 키 K1 대기). 잔여 작업은
BF1·BF3·BF4·BF5(type-proposer)·BF6(메인 루프)·BF7(type-extractor) owner-fix 완료 확인뿐, 이 WIP의
후속 슬라이스는 없음.
