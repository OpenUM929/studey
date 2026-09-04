# 3-Tier Review 준비 안내 (260831)

## 목표
- type-proposer 산출물(국어 슬라이스 1 + 2~6 진행 중) 검토
- INT-1(렌더 페이지 부재) 차단 상태 평가
- rev-arbiter 판정 전까지 검토 가능 여부 판단

---

## 산출물 위치

**완료된 산출물 (슬라이스 1 — 국어)**:
- `output/260831/260831_01_type_analysis_KO.md` (문항 32/32 PROVISIONAL)
- `output/260831/260831_01_catalog_update_KO.md` (신규 K-13~K-16, 갱신 8건)

**진행 중 산출물 (슬라이스 2~6)**:
- 예상: 12개 파일 (수학2·영어·통합과학·통합사회·한국사 × 2)
- 상태: type-proposer 백그라운드 실행 중 (agentId: a3d63f282895e1437)

---

## 검토 포인트 (rev-writer 예정 과제)

### 슬라이스 1(국어) — 검토 가능 여부 판단

1. **INT-1 영향도 평가**
   - 모든 32문항이 PROVISIONAL 등급
   - 페이지 인용 대체(transcript L<n>)의 추적가능성 확인
   - 임시로 검토 진행 가능? vs 판정 대기 필수?

2. **신규 유형 초안 검증** (INT-1 해소 후)
   - K-13~K-16의 `_README.md` 형식 정합
   - 변형 축·함정 요소·배점대 적절성
   - CODE_REGISTRY 접두어 정정 (KO → K) 적용됨? ✓

3. **기존 유형 업데이트** (INT-1 해소 후)
   - 빈도/별표 갱신 8건의 정당성
   - 기출 근거 인용 (transcript L<n>) 검증

4. **공통 패턴 후보** (INT-1 해소 후)
   - 국어 특화 4개 + 기존 C-nn 보강 5개 식별 타당성

### 슬라이스 2~6 — 같은 INT-1 문제 예상

- 모든 과목이 corpus/_images에 pNN.png 0건
- 모든 과목이 같은 차단 조건 마주할 것
- **판정 전략**: 한 번에 모든 과목의 INT-1을 arbiter에 올릴 것

---

## 회람 일정

**타임아웃 방어**:
- type-proposer 완료 → 즉시 rev-writer 호출 (대기 최소화)
- rev-writer 검토 동안 type-proposer 산출물 계속 모니터
- 슬라이스 2~6 완료 후 한 번에 arbiter 판정 요청

---

## 다음 단계

1. **type-proposer 완료 알림 대기** (자동)
2. **rev-writer 호출** (회람문 준비됨)
3. **3-tier loop** (rev-writer → rev-auditor → rev-arbiter)
4. **arbiter 판정** 후 카탈로그 반영

---

*이 브리핑은 rev-writer 호출 직전에 발송할 회람문의 배경 정보임.*
