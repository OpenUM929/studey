# Type-Proposer 수정 요청 (N1: CP-SM2-1 재구조화)

**발신**: Claude Code (Main Loop)  
**수신**: type-proposer  
**대상**: output/260831/260831_01_type_analysis_SM2.md — CP-SM2-1 기각 판정 재검토

**실행 시점**: 2026-08-31 15:10+ (type-extractor 완료 후)

---

## 배경

### Rev-Auditor 발견 (N1)

**Tier-1 판정**:
```
CP-SM2-1 (정확 이분 60:40 후보) → 기각
근거: 영어 70:30, 한국사 40:60 반례
```

**Rev-Auditor 재측정** (corpus 직접 측정):
```
전 과목 선택:서답 비율:
- 수학2:  60:40 ✓
- 국어:   60:40 ✓
- 과학:   60:40 ✓
- 사회:   60:40 ✓
- 영어:   70:30 (예외)
- 한국사: 40:60 (예외)

결과:
- (강) 총점 정확도: 6/6 = 100.0 ✓
- (중) 60:40 패턴: 4/6
- (약) 예외: EN 70:30, HI 40:60

결론: 기각이 과도 → 재구조화 필요
```

**문제**:
- Tier-1이 proposal에서만 소싱 (proposal 내 EN 분석)
- corpus 직접 측정하지 않음
- 결과: 2/6 예외를 6/6 오류로 판정

---

## 수정 항목

**파일**: `output/260831/260831_01_type_analysis_SM2.md`

**대상 섹션**: CP-SM2-1 (정확 이분 후보)

**현재 표기** (예상):
```
## 공통 패턴 CP-SM2-1: 정확 이분 (선택 60 : 서답 40)
- 상태: 기각 (60:40 정확성 불성립)
- 근거: 영어 70:30, 한국사 40:60 반례
```

**수정 표기**:
```
## 공통 패턴 CP-SM2-1: 점수 배분 구조 (선택 vs 서답)
- 상태: 검증 (partial pattern)
- 강도 분석:
  - (강) 총점 정확도: 6/6 과목 = 100.0 (완벽 동기)
  - (중) 60:40 정확 이분: 4/6 과목 (수학2·국어·과학·사회)
  - (약) 예외 패턴: 2/6 (영어 70:30, 한국사 40:60)
- 해석: 기본 설계 60:40 + 과목별 조정 (영어 강화, 한국사 서답 강화)
```

---

## 수정 근거

**Rev-Auditor 독립 측정**:
- corpus 직접 읽음 (proposal 재인용 아님)
- 모든 과목 배점 재계산
- 패턴 분류: 강/중/약 3단계

**신뢰도**:
- Corpus 일차자료 직접 측정
- tier-1의 제한적 소싱(proposal만) 보완

---

## Write Surface

- ✅ 수정: `output/260831/260831_01_type_analysis_SM2.md` (CP-SM2-1 섹션)
- ❌ 금지: catalog_update_SM2.md 수정 (arbiter 승인 후 apply)

---

## 체크포인트

**WIP 파일**: `analysis/wip/type-proposer_260831_fix_N1.md`

```markdown
---
actor: type-proposer
task: N1_CP-SM2-1_재구조화
target: output/260831/260831_01_type_analysis_SM2.md
status: done
updated: 260831 15:XX
---

| 슬라이스 | 대상 | 수정 | 상태 | 비고 |
|---------|------|------|------|------|
| 1 | SM2 | CP-SM2-1: 기각→재구조화 (4/6 중도) | done | rev-auditor N1 승인 |

NEXT: none (CP-SM2-1 재구조화 완료)
```

---

## 다음 단계

수정 완료 후:
1. **rev-writer**: 오류 정정 + tier-1 재검토 호출
2. 수렴 선언

---

**수정 권한**: checkpoint 기록 후 즉시 반영

