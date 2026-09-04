# 3-tier Review 회람문 (2025-2중간 전과목 PROPOSE 결과)

**발신**: Claude Code (Main Loop)  
**수신**: rev-writer (Tier-1 reviewer)  
**대상**: 2025-2중간 전 과목(6개) 유형분석 산출물  
**회차**: Round 1

**실행 시점**: 2026-08-31 13:35+ (슬라이스 6 완료 직후)

---

## 1. 검토 대상 문서

### 산출물 경로 (10개, 슬라이스 1~5) + 6개(슬라이스 6, 13:30 예상)

**완료된 산출물** (현재 저장):
```
output/260831/260831_01_type_analysis_KO.md         (38.2 KB)
output/260831/260831_01_type_analysis_SM2.md        (40.0 KB)
output/260831/260831_01_type_analysis_EN.md         (30.7 KB)
output/260831/260831_01_type_analysis_SC.md         (36.8 KB)
output/260831/260831_01_type_analysis_SS.md         (35.4 KB)
output/260831/260831_01_catalog_update_KO.md        (32.3 KB)
output/260831/260831_01_catalog_update_SM2.md       (49.2 KB)
output/260831/260831_01_catalog_update_EN.md        (33.3 KB)
output/260831/260831_01_catalog_update_SC.md        (35.4 KB)
output/260831/260831_01_catalog_update_SS.md        (37.3 KB)
```

**슬라이스 6 예상 산출물** (13:30 완료):
```
output/260831/260831_01_type_analysis_HI.md         (예상 30~50 KB)
output/260831/260831_01_catalog_update_HI.md        (예상 30~50 KB)
```

**합계**: 12개 파일

---

## 2. 참고 정본 (읽기 전용)

- `analysis/catalog/history.md` — 기존 한국사 유형(F-01~08)
- `analysis/catalog/_README.md` — 유형 카탈로그 형식
- `analysis/curriculum_2022.md` — 교육과정 범위 가드 (⚠️ 2학기 절 부재)
- `docs/DATA_STANDARD.md` — 데이터 규격
- `analysis/REV_GUIDE.md` — 검토 절차

---

## 3. 이번 라운드 범위

**대상**: 2025-2중간 전 과목 × 1회차

| 과목 | 유형ID | 산출물 |
|------|--------|--------|
| 국어(K) | KO-01~... | type_analysis_KO + catalog_update_KO |
| 수학2(SM2) | SM2-01~33 | type_analysis_SM2 + catalog_update_SM2 |
| 영어(T/W) | T-01..., W-01... | type_analysis_EN + catalog_update_EN |
| 통합과학(SC) | GB/GT/MC/ER/CH/BI/UN... | type_analysis_SC + catalog_update_SC |
| 통합사회(SS) | F-역사(또는 다중 접두어) | type_analysis_SS + catalog_update_SS |
| 한국사(HI) | F-01~08 기존 + 신규 | type_analysis_HI + catalog_update_HI (슬라이스 6 예상) |

---

## 4. 검토 절차

### tier-1 (rev-writer, 본 라운드)

**작업**:
- 각 과목별 산출물 item-by-item 재검증
- 유형 ID 부여의 정확성 확인
- 카탈로그 형식(_README.md) 준거 확인
- 함정 요소·배점대·중요도 논거 확인
- 제시된 차단 조건(INT-1, INT-2, INT-5, DQ-*) 영향도 평가

**산출물**: 
- `output/260831/rev/260831_01_type_analysis_*_review_first.md` (과목당 1개)
- `output/260831/rev/_index.md` 행 추가 (체크리스트 기반)

**예상 소요**: 2~3시간 (6과목 × 20~30분)

### tier-2 (rev-auditor, Round 1 완료 후)

- tier-1 재검증 없이 원본에서 독립 검증
- tier-1 결과와 비교 (동의/불동의/신규 결함)
- 이의 기록

**≤5R**: 동일 이의 재현 시 차단 조건 재분류 또는 tier-3 상향

### tier-3 (rev-arbiter, 수렴 후)

- 최종 판정: approve / revise-required / reject
- DQ-* 결정요청 (INT-1/INT-2/INT-5, DQ-SC-1 등)에 대한 바인딩 룰

---

## 5. 차단 조건 명시 (INT-1, INT-2, INT-5, DQ-*)

### INT-1: 페이지 렌더 이미지 부재 (6과목 공통)

```
corpus/_images/EX-*/pNN.png : 0건
대체 인용: transcript.md L<행번호>
결과: 모든 산출물 = PROVISIONAL 등급
```

**영향**: 커버리지 100% 주장 불가능 → review에서 주석 추가 필수

**판정 필요**: DQ-KO-1/DQ-KO-2 (arbiter)

---

### INT-2: 통합과학 배점 인덱스 불일치

```
전사본 §1 서술형 배점 합: 22점
실제 verify_log 배점 합: 40점
```

**영향**: Tier/DF 판정 재계산 필요 여부 미확정

**대응**: type_analysis_SC 검증 시 배점 기준 확인

---

### INT-5: curriculum_2022.md 2학기 절 부재 (6과목 공통)

```
범위 가드 불가능 → ⚠️ 표시 필수
```

**영향**: 모든 산출물에 "범위 미확정" 주석

**판정 필요**: DQ-SC-2 (curriculum_2022.md 갱신 or 별도 범위 문서)

---

### DQ-SC-1: 통합과학 신규 ID 정책 공백

**신규 유형 8군 발견 → ID 부여 불가 상태**

**판정 필요**: CODE_REGISTRY 정책 명시 (A: 단원별 PREFIX 신설 / B: 신규 항목만 기록)

---

## 6. 판정 요청 (질문형)

### 질문 1: INT-1 해결 방법 선택

**현재 상황**: pNN 렌더 부재 → transcript L<n> 인용으로 대체

**선택지**:
- [ ] **A**: 현재대로 진행 (transcript L<n> 인용 유지, PROVISIONAL 유지)
- [ ] **B**: render_recovery 완료 대기 (전 과목 재분석, 기간 TBD)
- [ ] **C**: 부분 허용 (어느 과목부터 허용할 것인가?)

---

### 질문 2: INT-2 (통합과학 배점) 재검증

**선택지**:
- [ ] **A**: 검증 결과 일치 확인됨 → 진행 가능
- [ ] **B**: 배점 재확인 필요 → type-extractor 또는 사용자 확인 후 재분석

---

### 질문 3: INT-5 (범위 가드) 해결 방법

**선택지**:
- [ ] **A**: curriculum_2022.md 2학기 절 추가 (사용자 담당)
- [ ] **B**: 별도 범위 정본 작성 (`analysis/forecast/2025-2M_scope.md`)
- [ ] **C**: 현재 상태로 ⚠️ 표시 유지 후 추후 갱신

---

### 질문 4: DQ-SC-1 (통합과학 신규 ID)

**선택지**:
- [ ] **A**: CODE_REGISTRY 정책 추가 (단원별 PREFIX: GB/GT/MC/ER/CH/BI/UN 신설 또는 통합 SC 사용)
- [ ] **B**: 신규 유형만 별도 기록, 카탈로그는 기존 ID만 사용 (정책 미정)

---

## 7. 제약 및 write surface

**Write Surface** (REV_GUIDE §5):
- ✅ 허용: `output/260831/rev/` 하위 검토 보고서 작성
- ✅ 허용: `output/260831/rev/_index.md` 행 추가
- ✅ 허용: `analysis/REV_LOG.md` 행 추가
- ❌ 금지: 카탈로그·EXTRACTION_LOG·HARVEST_LOG 직접 수정
- ❌ 금지: 산출물 문서 자체 수정 (기술만 기록)

**체크포인트** (CLAUDE.md 공통 규격 ②):
- 각 슬라이스(과목) 완료 후 WIP 파일에 행 추가
- WIP: `analysis/wip/rev-writer_260831_3tier.md`
- 형식: 과목 | 범위 | 상태(done/blocked) | 산출물 경로 | 비고

---

## 8. 회신 위치 및 형식

**산출물 디렉토리**: `output/260831/rev/`

**1차 회신** (tier-1 완료):
```
Pipeline : [1 refine]──▶[2 propose]──▶[3 review]──▶[4 arbiter]──▶[5 apply]
                                           ▲ R1 tier-1
Stage    : reviewed 6 subjects — N issues found, M need arbiter decision, K ready for tier-2
Team     : actor=rev-writer; WIP=rev-writer_260831_3tier.md
Next     : tier-2 (rev-auditor) independent verification
```

**산출물 파일**:
```
output/260831/rev/260831_01_type_analysis_KO_review_first.md
output/260831/rev/260831_01_type_analysis_SM2_review_first.md
output/260831/rev/260831_01_type_analysis_EN_review_first.md
output/260831/rev/260831_01_type_analysis_SC_review_first.md
output/260831/rev/260831_01_type_analysis_SS_review_first.md
output/260831/rev/260831_01_type_analysis_HI_review_first.md (슬라이스 6 후)
```

---

## 9. 특별 지침

### CLAUDE.md 원칙 ① (정본 참조)

- 접두어 목록 → CODE_REGISTRY.md 정본 직접 읽기 (사본 금지)
- 카탈로그 형식 → `analysis/catalog/_README.md` 확인
- 규격 문구 → REV_GUIDE §2-b E 참조

### 원칙 ② (슬라이스 체크포인트)

- 과목별 검토 완료 직후 즉시 WIP 행 추가
- 지연 금지 (이전 slices 5에서 발생)

### 원칙 ④ (검수 피드백)

- 해당 유형의 「금지·주의」 항목 추천사항 기록
- 앞으로의 출제 오류 방지

---

## 10. 참고사항

**차단 조건 예상**:
- 모든 6개 과목이 INT-1(페이지 렌더) 동반 → PROVISIONAL 마킹
- 통합과학만 INT-2(배점) 확인 필요
- 6과목 모두 INT-5(범위 미확정) → ⚠️ 표시

**신규 유형 잠금 상태**:
- 통합과학 8군 ID 부여 불가 (DQ-SC-1 결정 대기)
- 기존 유형만 재사용 (검증 자료 확인 필수)

---

## 11. 체크리스트

**회람문 품질 확인** (REV_GUIDE §6-b):
- [ ] (a) 자기완결인가? ✓ (대상·범위·판정 형식·회신처 닫혀 있음)
- [ ] (b) 실측값인가? ✓ (파일 목록, 크기, 경로 재확인)
- [ ] (c) executor 근거가 있나? ✓ (rev-writer.md description)
- [ ] (d) 판정이 판정 가능한 질문형인가? ✓ (선지 A/B/C 명시)
- [ ] (e) 제약이 검증 가능한가? ✓ (수신자가 위반 점검 가능)

---

**회람문 발신 준비 완료**  
**13:30 슬라이스 6 완료 직후 즉시 발신 예정**
