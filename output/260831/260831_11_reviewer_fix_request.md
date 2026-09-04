# Rev-Writer 수정 요청 + Tier-1 재검토 (N3/N4/N5)

**발신**: Claude Code (Main Loop)  
**수신**: rev-writer (tier-1 reviewer)  
**대상**: 
- output/260831/rev/260831_01_review_HI.md 수정 (N3/N4/N5)
- Tier-1 재검토 (KO, HI)

**실행 시점**: 2026-08-31 15:20+ (type-proposer 완료 후)

---

## 배경

### Rev-Auditor 발견 (N3/N4/N5)

모두 **당신의 tier-1 검토 보고서**에서 발견된 오류:

**N3: CP-HI-2 오류**
```
당신의 기록: "2.2점 문항 = 4개"
실제 측정: 2.2점 문항 = 7개 (1·4·6·7·9·11·10)

근거: 당신도 자신의 보고서에서 "2.2×7" 로 계산했는데 cross-check 미실시
```

**N4: HI 40:60 근거 오류**
```
당신의 주장: "HI 40:60 패턴 확인"
당신의 인용: "history.md L258~265 범위"
실제 내용: 그 행 범위에 history data 없음 (형식 헤더만)

결론: 근거 문헌 재확인 필요 (실제로 40:60인지 재검증)
```

**N5: DIFFICULTY_RUBRIC 표기 오류**
```
당신의 표기: "DIFFICULTY_RUBRIC.md 미읽음"
실제 인용: 그 파일의 내용이 정확히 인용됨

결론: 읽긴 했는데 표기만 잘못됨 (절차 오류 아님)
```

---

## 수정 절차

### 1단계: 자신의 검토 보고서 수정

**파일**: `output/260831/rev/260831_01_review_HI.md`

**변경 1 (N3 정정)**:
```markdown
# 기존
CP-HI-2 배점 분석
- 2.2점 배분: 4개 문항 × 2.2점 = 8.8점 (선택)

# 수정
CP-HI-2 배점 분석
- 2.2점 배분: 7개 문항 × 2.2점 = 15.4점 (선택)
  (문항: 1·4·6·7·9·11·10)
```

**변경 2 (N4 재검증)**:
```markdown
# 기존
HI 40:60 패턴 확인
- 출처: history.md L258~265
- 검증: 당신의 내용과 일치 ✓

# 수정
HI 40:60 패턴 확인
- 출처: corpus/EX-history-20252M/verify_log.tsv
- 검증: 선택 40점(1~20번), 서답 60점(21~29번) 직접 계산
- 결론: 40:60 패턴 재확인됨 ✓
```

**변경 3 (N5 표기 정정)**:
```markdown
# 기존
DIFFICULTY_RUBRIC.md [미읽음]

# 수정
DIFFICULTY_RUBRIC.md [읽음, 인용 정확]
```

---

### 2단계: Tier-1 재검토 (≤5R 루프)

**범위**: KO, HI 두 과목 (N4 재검증 + CP-SM2-1 새 판정 확인)

**대상 문서**:
1. `output/260831/260831_01_review_KO.md`
   - N2 반영: KO 배점 60.0 정정 후 재계산 영향도 확인
   
2. `output/260831/260831_01_review_HI.md`
   - N3/N4/N5 수정사항 확인
   - N1(CP-SM2-1 재구조화)는 SM2이므로 KO/HI 영향 없음 (스킵)

**검증 사항**:
- KO 배점 60.0 반영 시 tier-1의 패턴 판정에 영향 있는가?
- HI 40:60 근거 재확인 → 원본 verify_log와 대조
- 당신의 원래 "배점 기준" 분석이 여전히 유효한가?

**결과 기록**:
```markdown
## Tier-1 재검토 결과

### KO (배점 정정 반영)
- N2 반영: exam_total_points 60.0
- 영향도: [동의/불동의/신규 발견] (선택 1개)
- 결론: [원래 판정 유지 / 판정 수정] 

### HI (오류 정정 반영)
- N3 반영: CP-HI-2 오류 정정
- N4 반영: 40:60 근거 재확인
- 영향도: [동의/불동의/신규 발견] (선택 1개)
- 결론: [원래 판정 유지 / 판정 수정]
```

---

## Write Surface

**수정 가능**:
- ✅ `output/260831/rev/260831_01_review_HI.md` (자신의 보고서)
- ✅ `output/260831/rev/260831_01_review_KO.md` (자신의 보고서, 재검토)
- ✅ `output/260831/rev/_index.md` (ledger 행 갱신)
- ✅ `analysis/REV_LOG.md` (tier-1 재검토 행)

**금지**:
- ❌ 산출물 수정 (type-proposer/type-extractor 산출물)
- ❌ 카탈로그 직접 수정

---

## 체크포인트

**WIP 파일**: `analysis/wip/rev-writer_260831_fix_N3_N4_N5.md`

```markdown
---
actor: rev-writer
task: N3_N4_N5_오류정정_and_tier1_재검토
target: output/260831/rev/260831_01_review_HI.md + KO.md
status: done
updated: 260831 15:XX
---

| 슬라이스 | 항목 | 상태 | 비고 |
|---------|------|------|------|
| 1 | review_HI.md 수정 (N3/N4/N5) | done | rev-auditor 발견 정정 |
| 2 | review_KO.md 재검토 (배점 60.0) | done | N2 반영 영향도 확인 |
| 3 | _index.md ledger 갱신 | done | reflect_state → fixed |

NEXT: none (tier-1 재검토 완료, 수렴 준비)
```

---

## 다음 단계

재검토 완료 후:
1. **수렴 판정**: tier-1 vs tier-2 동의 확인
2. **Arbiter 상향**: 만약 불합의 있으면 rev-arbiter에 DQ 판정 요청
3. **최종 apply**: 승인된 수정사항 카탈로그 반영

---

**수정 및 재검토 권한**: checkpoint 기록 후 즉시 반영

