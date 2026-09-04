# 차단 조건 정리 (260831 PROPOSE 단계)

**대상**: 2025-2중간 전 과목 (6개) 유형분석  
**날짜**: 260831  
**상태**: 슬라이스 1~5 완료, 슬라이스 6 대기

---

## INT-1: 페이지 렌더 이미지 부재 (6과목 공통)

**심각도**: 🔴 **전건 영향** (모든 문항)

**발견**:
```bash
Get-ChildItem corpus/_images -Recurse -File -Filter "p*.png"
# 결과: 0건 (모든 과목 EX-*-20252M 단위)
```

**영향**:
- type-proposer 절대규칙 2: 「문항번호 + 페이지(pNN)」 인용 필수
- 절대규칙 3: pNN 창작 금지 (수동 생성 불가)
- **결과**: 모든 6개 과목 = PROVISIONAL 등급

**대체 전략** (현재):
- 증거 좌표: `transcript.md L<행번호>` 사용
- 페이지 정보 미제공
- 커버리지: 100% 주장 불가능

**해결 방법** (rev-arbiter 판정 필요):
- **Option A**: type-extractor의 render_recovery 완료 후 재분석
  - 선행 WIP: `analysis/wip/type-extractor_260828_EX-math2-20252M_render_recovery.md` (in-progress)
  - 예상 기간: TBD
  - 비용: 전 과목 재분석 필요

- **Option B**: arbiter의 인용형식 대체 판정 (현재)
  - transcript L<n> 인용 자체로 충분한가?
  - PROVISIONAL 등급 유지하고 3-tier review 진행하나?
  - 판정 필요: **DQ-KO-1, DQ-KO-2** (국어에서 발행, 6과목 공통)

---

## INT-2: 통합과학 배점 인덱스 불일치

**심각도**: 🟡 **범위 확인 필요**

**발견**:
- 전사본 §1 서술형 배점 인덱스: 합계 22점
- 실제 verify_log 배점 합계: 40점
- 불일치 → 전사 검증 필요

**영향**:
- Tier/DF 판정이 배점에 기반할 경우 재계산 필요
- type-proposer가 배점 기반 등급을 사용했는가?

**해결**:
- type-extractor의 verify_log가 정본인가?
- 원본 문항 실제 배점 재확인
- 범위 확정 후 필요시 type-proposer 부분 재분석

**담당**: type-extractor 또는 사용자 (원본 자료 확인)

---

## INT-5: curriculum_2022.md 2학기 절 부재 (6과목 공통)

**심각도**: 🟡 **범위 가드 불가능**

**발견**:
```
curriculum_2022.md:
- 1학기: 전 과목 절(§1~6) 존재 ✓
- 2학기: 절 부재 ✗
```

**영향**:
- 범위 가드 규칙(CLAUDE.md 원칙 2): "교과 범위 판단은 curriculum_2022.md와 대조한다"
- 2학기 범위를 대조할 수 없음
- 교육과정 밖 내용 vs 안 내용 판단 불가능

**결과**:
- 모든 6개 과목의 type-proposer 산출물에 ⚠️ 주석 추가
- "2025-2중간 범위 미확정" 표시 필수

**해결**:
- Option A: curriculum_2022.md 2학기 절 추가 (정본 갱신)
- Option B: 사용자/학교 진도표 기반 범위 확정 후 별도 가드 문서 작성
- **판정 필요**: **DQ-SC-2** (통합과학에서 발행, 6과목 공통)

---

## DQ-KO-1 / DQ-KO-2: 페이지 인용 형식 (국어 발행, 6과목 공통)

**결정 요청 대상**: rev-arbiter

**질문**:
1. **INT-1 해결**: pNN 렌더 부재 상황에서, transcript L<n> 인용만으로 충분한가?
   - A: 충분 → PROVISIONAL 해제, 3-tier review 진행
   - B: 부족 → render_recovery 완료 대기
   - C: 부분허용 → 어느 과목/어느 항목부터?

2. 해결 전까지 PROVISIONAL 등급 유지하고 review 진행하나?

**담당**: rev-arbiter (최종 판정)

**영향**: 모든 6개 과목

---

## DQ-SC-1: 통합과학 신규 ID 정책 공백

**심각도**: 🟠 **신규 유형 차단**

**발견**:
- CODE_REGISTRY §5-3: "신규 과목은 PREFIX 신설 절차를 따른다"
- CODE_REGISTRY §6-b: "온보딩 목록 참조"
- 충돌: 통합과학이 "신규"인가 기존인가?
- 단원별 PREFIX (GB/GT/MC/ER/CH/BI/UN) 사용하나, 통합 PREFIX (SC) 사용하나?

**결과**:
- 신규 유형 8군 발견 → ID 부여 불가능
- 기존 유형만 재사용 (ER-05)

**해결**:
- Option A: CODE_REGISTRY에 통합과학 단원별 정책 명시 → 선점 확인 후 ID 부여
- Option B: 신규 유형 후보만 기록, arbiter 판정 후 ID 부여

**판정 필요**: **DQ-SC-1** (선택지 A/B/C별 ID 후보 제시)

---

## DQ-SC-2: 범위 가드 불가능 (6과목 공통, INT-5 동반)

**결정 요청 대상**: rev-arbiter

**질문**:
1. curriculum_2022.md 2학기 절을 추가할 것인가?
   - 일정: ?
   - 책임: 사용자?

2. 아니면, 별도 범위 가드 정본을 만들 것인가?
   - `analysis/forecast/2025-2M_scope.md` (사용자 확정 범위)
   - 책임: 사용자?

3. 그 전까지 ⚠️ 범위 미확정 표시 유지?

**영향**: 모든 6과목

---

## DQ-SM2-1~4: 수학2 특화 (슬라이스 2)

*상세는 output/260831/260831_01_type_analysis_SM2.md 참조*

- DQ-SM2-1: 단답17 원본 정의식 부재 (f 함수 정의 명확화)
- DQ-SM2-2~4: 별표 축 전환 (부교재→기출 근거) 적용 방식

---

## DQ-EN-1~3: 영어 특화 (슬라이스 3)

*상세는 output/260831/260831_01_type_analysis_EN.md 참조*

- 신규 유형 T-13·W-05 타당성
- CP-SM2-1과의 충돌 (60:40 vs 영어 70:30)

---

## 차단 조건별 rev-arbiter 결정 요청

| ID | 심각도 | 대상 | 필요 판정 |
|----|--------|------|---------|
| INT-1 | 🔴 | 6과목 | 페이지 인용 형식 대체 승인 |
| INT-2 | 🟡 | 통합과학 | 배점 검증 후 재분석 필요 여부 |
| INT-5 | 🟡 | 6과목 | curriculum_2022.md 갱신 또는 별도 범위 정본 |
| DQ-KO-1/2 | 🔴 | 6과목 | A/B/C 선택 (INT-1 연동) |
| DQ-SC-1 | 🟠 | 통합과학 | 신규 ID 정책 (A/B 선택) |
| DQ-SC-2 | 🟡 | 6과목 | 범위 정본 확정 방식 |
| DQ-SM2-1~4 | 🟠 | 수학2 | 단답 정의·별표 축 적용 |
| DQ-EN-1~3 | 🟠 | 영어 | 신규 유형·교차 충돌 검증 |

---

## 3-tier Review 진행 가능 여부

**현재 판정**: ⏳ **차단 조건 있음 → 검토 가능하되, 최종 승인 전 결정요청 필수**

**rev-writer 진행 범위**:
- ✅ 슬라이스 1~5 + 6(완료 후) 산출물 item-by-item 재검증
- ✅ 차단 조건 명시 및 근거 확인
- ✅ DQ 선택지 B/C 추천사항 작성

**rev-arbiter 판정 필요 시점**: 
- rev-writer/auditor 3-tier loop 완료 후
- 최종 승인 전

---

*이 정리는 rev-writer 호출 시 제공됨.*
