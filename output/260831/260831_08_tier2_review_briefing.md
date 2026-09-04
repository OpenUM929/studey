# Tier-2 Review 회람문 (2025-2중간 전과목 PROPOSE+TIER-1 결과)

**발신**: Claude Code (Main Loop)  
**수신**: rev-auditor (Tier-2 independent reviewer)  
**대상**: 2025-2중간 전 과목(6개) 유형분석 + tier-1 검토 결과  
**회차**: Round 1 — Tier-2 초회

**실행 시점**: 2026-08-31 14:45+ (tier-1 완료 직후)

---

## 1. 검토 대상 문서

### 원본 산출물 (type-proposer 기출, 12개)

```
output/260831/260831_01_type_analysis_KO.md         (38.2 KB)
output/260831/260831_01_type_analysis_SM2.md        (40.0 KB)
output/260831/260831_01_type_analysis_EN.md         (30.7 KB)
output/260831/260831_01_type_analysis_SC.md         (36.8 KB)
output/260831/260831_01_type_analysis_SS.md         (35.4 KB)
output/260831/260831_01_type_analysis_HI.md         (정규 크기)

output/260831/260831_01_catalog_update_KO.md        (32.3 KB)
output/260831/260831_01_catalog_update_SM2.md       (49.2 KB)
output/260831/260831_01_catalog_update_EN.md        (33.3 KB)
output/260831/260831_01_catalog_update_SC.md        (35.4 KB)
output/260831/260831_01_catalog_update_SS.md        (37.3 KB)
output/260831/260831_01_catalog_update_HI.md        (정규 크기)
```

### Tier-1 검토 보고서 (6개)

```
output/260831/rev/260831_01_review_KO.md
output/260831/rev/260831_01_review_SM2.md
output/260831/rev/260831_01_review_EN.md
output/260831/rev/260831_01_review_SC.md
output/260831/rev/260831_01_review_SS.md
output/260831/rev/260831_01_review_HI.md
```

### 핸드오프 레지스터

```
output/260831/rev/_index.md (tier-1 결과 요약 + 판정 단위 재구성 제안)
analysis/REV_LOG.md (tier-1 행 추가됨)
```

### 차단 조건 정리

```
output/260831/260831_05_blocking_conditions_summary.md
```

---

## 2. Tier-1 발견사항 (독립 재검증 전 비독립 읽음)

### INT-1 (페이지 렌더 부재, 6과목 공통)
- **tier-1 판정**: 모든 6개 과목 corpus/_images에 pNN.png 0건 → PROVISIONAL 등급 타당
- **근거**: 직접 실측(Get-ChildItem corpus/_images -Recurse -Filter "p*.png")
- **결과**: 모든 산출물 PROVISIONAL 마킹 + transcript L<n> 인용 대체

### INT-2 (통합과학 배점 인덱스 불일치)
- **tier-1 판정**: 전사본 §1 합 22점 vs verify_log 합 40점 → 불일치 확인, 하위 산출물 전건 40 채택 재현
- **영향도**: 정합 확인 — 전파 결함 없음
- **status**: 배점 기준 검증 필요 (배점에 기반한 Tier/DF 판정 여부 확인)

### INT-5 (curriculum_2022.md 2학기 절 부재, 6과목 공통)
- **tier-1 판정**: ⚠️ 범위 가드 불가능 — 모든 산출물에 "범위 미확정" 주석 필수
- **근거**: curriculum_2022.md 1학기 절 ✓, 2학기 절 ✗ 직접 확인

### CP-SM2-1 (정확 이분 후보, 패턴 충돌)
- **tier-1 판정**: 기각 (영어 70:30, 한국사 40:60 반례로 60:40 정확성 불성립)
- **근거**: 영어와 한국사 산출물 정항 수 계산 재확인 (산술 정확)
- **결론**: 과목별 고정 비율 재정식화 필요 → arbiter 의뢰

### CP-HI-1 (합답 선지 5종 고정, 신규 함정)
- **tier-1 판정**: 전건 9/9 재현 확인 — 신규 함정 유형 등록 타당
- **근거**: 한국사 전 문항 선지 패턴 문자 검색

### DQ 판정 단위 재구성
- **tier-1 발견**: 회람문 Q4-Q7이 EN/SS/SC/HI를 하나로 묶었으나, 실제로는
  - **EN(T-13/W-05)**: CODE_REGISTRY §6(b) 260826 이미 승인된 사항 → 결정요청 불필요
  - **SS(F-08 확장)**: 같이 260826 기결 → 결정요청 불필요
  - **SC(신규 영역 접두어)**: 진정한 신규 정책 필요 → DQ-SC-1 타당
  - **SS의 D 접두어**: F 충돌과 별개 — 미등록 정책 → DQ-SS-2 타당
- **권고**: 판정 단위 재구성 후 arbiter 상신

---

## 3. Tier-2 독립 검증 범위

### 작업 방식 (REV_GUIDE §3-b tier-2 정의)

**"tier-1 재검증 없이 원본에서 독립 검증 후, tier-1 결과와 비교"**

1. **각 과목별** (KO/SM2/EN/SC/SS/HI):
   - type-proposer 원본 (type_analysis_*.md) 직접 읽기 (tier-1 보고서 보지 않음)
   - 차단 조건(INT-1/2/5) 독립 재현
   - item-by-item per-type 할당 spot-check (표본 10~20%)
   - 카탈로그 형식 준거 확인
   - 변형 축 유효성 확인

2. **tier-1 결과와 교차점검**:
   - 동의 / 불동의 / 신규 결함 기록
   - 이의 발생 시 ≤5R 루프 진입 (동일 이의 재현 → escalate)

3. **차단 조건 추가 검증**:
   - INT-1 재현: corpus/_images 직접 확인
   - INT-2 재현: 통합과학 배점 재계산
   - INT-5 재현: curriculum_2022.md 2학기 절 재확인
   - DQ-SC-1/DQ-SS-2 타당성 재검증

---

## 4. 판정 요청 (질문형)

### Q1: INT-1 (페이지 렌더 부재) 해결 선택

**Tier-1 판정**: 현재 PROVISIONAL 등급 + transcript L<n> 인용 타당

**당신의 독립 판정**:
- [ ] **A**: tier-1 판정 동의 → PROVISIONAL 유지, transcript 인용 허용, 3-tier 진행
- [ ] **B**: tier-1 판정 불동의 → 사유 명시 (새 대체 방안 제시 시 상세)
- [ ] **C**: 추가 정보 필요 → 어느 부분 재검증 필요한가?

---

### Q2: INT-2 (통합과학 배점) 타당성

**Tier-1 판정**: 불일치 확인(22↔40), 하위 산출물 전건 40 채택으로 일관성 있음

**당신의 독립 판정**:
- [ ] **A**: tier-1 판정 동의 → 배점 기반 Tier/DF 판정 전파 오류 없음 확인
- [ ] **B**: tier-1 판정 불동의 → 어디서 오류 발견했는가?
- [ ] **C**: 재검증 필요 → 특정 항목 명시

---

### Q3: INT-5 (curriculum_2022.md 2학기 절) 관할 판정

**Tier-1 판정**: ⚠️ 범위 미확정 표시 + 모든 산출물 주석 필수

**당신의 독립 판정**:
- [ ] **A**: tier-1 판정 동의 → ⚠️ 표시 유지, 3-tier 진행
- [ ] **B**: tier-1 판정 불동의 → 범위 정보가 다른 출처에 있는가?
- [ ] **C**: 범위 판정 권한 질문 → arbiter에 미룰 사항인가?

---

### Q4: CP-SM2-1 기각 타당성

**Tier-1 판정**: 기각 (영어 70:30, 한국사 40:60 반례)

**당신의 독립 판정**:
- [ ] **A**: 기각 동의 → 정확 이분은 성립하지 않음
- [ ] **B**: 보류 → 다른 해석 가능한가? (사유 명시)
- [ ] **C**: 재계산 필요 → 정항 수 재점검 후 결론

---

### Q5: CP-HI-1 전건 9/9 재현 타당성

**Tier-1 판정**: 전건 재현 확인, 신규 함정 유형 등록 타당

**당신의 독립 판정**:
- [ ] **A**: 재현 동의 → 한국사 전 문항 선지 패턴 일치
- [ ] **B**: 재현 불동의 → 어느 문항에서 패턴 다른가?
- [ ] **C**: 일반화 불가 → 표본 범위만 동의 가능

---

### Q6: DQ 판정 단위 재구성 타당성

**Tier-1 판정**: 
- EN/SS는 이미 260826 기결 → 결정요청 불필요
- SC는 진정한 신규 정책 필요 → DQ-SC-1 타당
- SS의 D 접두어는 별개 → DQ-SS-2 타당

**당신의 독립 판정**:
- [ ] **A**: 재구성 동의 → CODE_REGISTRY §6(b) 재확인, arbiter 상신 시 3개 DQ로 분리
- [ ] **B**: 재구성 불동의 → 원래 판정 단위가 맞다고 생각하는가?
- [ ] **C**: 추가 DQ 발견 → 새로운 결정요청 명시

---

## 5. 제약 및 절차

**Write Surface** (REV_GUIDE §5):
- ✅ 허용: `output/260831/rev/` 하위 2차 검토 보고서 작성
- ✅ 허용: `output/260831/rev/_index.md` 행 추가 (reflect_state 갱신)
- ✅ 허용: `analysis/REV_LOG.md` 행 추가
- ❌ 금지: 원본 산출물 수정, 카탈로그 직접 수정

**슬라이스 체크포인트**:
- 과목별 검증 완료 후 WIP 파일에 즉시 행 추가
- WIP: `analysis/wip/rev-auditor_260831_3tier.md`
- 형식: CLAUDE.md §서브에이전트 공통 규격 ②

**라운드 루프** (≤5R):
- 동일 이의 재현 시 즉시 escalate 표시
- 종결은 tier-1 vs tier-2 동의 또는 arbiter 상향

---

## 6. 회신 위치 및 형식

**위치**: `output/260831/rev/`

**산출물** (회신 시 첫 문장):
```
Pipeline : [1 refine]──▶[2 propose]──▶[3 review]──────▶[4 arbiter]
                                        ▲ R1 tier-2
Stage    : verified 6 subjects independently — N agree, M disagree, K new findings
Team     : actor=rev-auditor; WIP=rev-auditor_260831_3tier.md; rounds≤5
Next     : [if converged] arbiter final ruling on DQ-SC-1/SS-2 and CP-SM2-1 rejection
```

**회신 파일**:
```
output/260831/rev/260831_01_type_analysis_KO_review_second.md
output/260831/rev/260831_01_type_analysis_SM2_review_second.md
output/260831/rev/260831_01_type_analysis_EN_review_second.md
output/260831/rev/260831_01_type_analysis_SC_review_second.md
output/260831/rev/260831_01_type_analysis_SS_review_second.md
output/260831/rev/260831_01_type_analysis_HI_review_second.md
```

---

## 7. 특별 지침

### 원칙 ① (정본 참조)

- CODE_REGISTRY.md §6(b) 260826 결정 내용 직접 읽기 (사본 불신뢰)
- curriculum_2022.md 2학기 절 부재 직접 확인

### 원칙 ② (슬라이스 체크포인트)

- 과목별 완료 직후 **즉시** WIP 행 추가 (이전 tier-1도 준수)

### 원칙 ④ (검수 피드백)

- 차단 조건 재현 시마다 근거(명령 + 출력) 기록

---

## 8. 체크리스트 (회람문 품질 확인)

**REV_GUIDE §6-b 회람문 규격 준수**:
- [ ] (a) 자기완결인가? ✓ (대상·범위·판정 형식·회신처 닫혀 있음)
- [ ] (b) 실측값인가? ✓ (파일 목록, 크기, 경로 재확인)
- [ ] (c) executor 근거가 있나? ✓ (rev-auditor.md description)
- [ ] (d) 판정이 판정 가능한 질문형인가? ✓ (선지 A/B/C 명시)
- [ ] (e) 제약이 검증 가능한가? ✓ (auditor가 위반 점검 가능)

---

**회람문 발신 준비 완료**  
**rev-auditor 호출 즉시 가능**

---

## Tier-2 실행 예상 타임라인

| 시각 | 작업 | 소요 |
|------|------|------|
| 14:45 | rev-auditor 호출 | 즉시 |
| 14:45~16:15 | 6과목 독립 검증 (과목당 15분) | 90분 |
| 16:15 | tier-2 보고서 6개 완료 + _index 갱신 | 5분 |
| 16:20 | 수렴 판정 (동의/불동의 집계) | 5분 |
| 16:25 | arbiter 상향 또는 수렴 선언 | 즉시 |

**예상 전체 3-tier 완료**: 16:30~17:00

