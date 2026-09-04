# Tier-2 Round 2 회람문 (rev-writer 수정사항 독립 교차검증)

**발신**: Claude Code (Main Loop)  
**수신**: rev-auditor (Tier-2 independent reviewer)  
**대상**: rev-writer round 2 corrections (N1~N5) 검증  
**회차**: Round 2 — Tier-2 독립 cross-check

**실행 시점**: 2026-08-31 16:xx (tier-1 round 2 완료 직후)

---

## 1. 배경

### Tier-1 Round 2 실행 완료

rev-writer는 tier-2 round 1 발견사항 5건(N1~N5)을 반영했습니다:

| 항목 | 처리 대상 | 현재 상태 |
|------|---------|---------|
| **N1** | 국어 선택형 배점 | review_KO.md 수정 (60.4→60.0 코퍼스 재실측) |
| **N2** | CP-SM2-1 기각 | review_SM2.md 수정 (6과목 재실측, 4/6=60:40 확인) |
| **N3** | CP-HI-2 근거 오류 | review_HI.md 수정 (2.2점 문항 7개 재확인) |
| **N4** | HI 40:60 근거 | review_SM2.md 수정 (한국사 원문 직접 교체) |
| **N5** | KO DIFFICULTY_RUBRIC | review_KO.md 수정 (CLAUDE.md L14-16·L19 직접 재열람) |

**현재 상태**: _index.md 행 15~17 모두 reflect_state=fixed

---

## 2. 검증 범위 (독립 재실측)

### 작업 방식

**"rev-writer 보고서 먼저 읽지 않고, 각 지적 항목을 원본에서 독립 재계산"**

이후 rev-writer 결과와 비교 (동의/불동의/신규).

### 5개 항목 독립 검증

#### **N1: 국어 선택형 배점 (60.0 vs 60.4)**

**rev-writer 주장**:
```
코퍼스 원문 29개값 재합산 = 60.0 (정확)
```

**당신의 독립 검증**:
- corpus/EX-korean-20252M/transcript.md L36 배점값 직접 합산
- 29개 값 × 개별 점수 재계산
- 결론: 동의 / 불동의 / 신규 발견 (선택 1개)

---

#### **N2: CP-SM2-1 기각 재판정 (4/6 vs 0/6)**

**rev-writer 주장**:
```
6과목 전수 선택:서답 비율:
- 수학2: 60:40 ✓
- 국어: 60:40 ✓
- 과학: 60:40 ✓
- 사회: 60:40 ✓
- 영어: 70:30 (예외)
- 한국사: 40:60 (예외)

결론: 4/6 정확 이분 → 기각 과도, 재구조화 필요
```

**당신의 독립 검증**:
- 각 과목 corpus (KO·SM2·SC·SS·EN·HI)의 transcript.md 직접 측정
- 선택형 vs 서답형 배점 구분 및 비율 재계산
- 결론: 동의 / 불동의 / 신규 발견

---

#### **N3: CP-HI-2 2.2점 문항 개수 (7개 vs 4개)**

**rev-writer 주장**:
```
EX-history-20252M/transcript.md 재확인:
2.2점 문항 = 1·4·6·7·9·10·11 = 7개
```

**당신의 독립 검증**:
- corpus/EX-history-20252M/transcript.md 원문 직접 확인
- 2.2점 배점 문항 목록 재추출
- 결론: 동의 / 불동의 / 신규 발견

---

#### **N4: HI 40:60 근거 재확인**

**rev-writer 주장**:
```
tier-2가 지적한 "EX-history-20252M/transcript.md" 근거 교체
- 선택형 20문항 (1~20) = 40점
- 서답형 9문항 (21~29) = 60점
```

**당신의 독립 검증**:
- 한국사 transcript.md 원문에서 배점 재확인
- 선택/서답 구분 및 합계 재계산
- 결론: 동의 / 불동의 / 신규 발견

---

#### **N5: KO DIFFICULTY_RUBRIC 열람 확인**

**rev-writer 주장**:
```
DIFFICULTY_RUBRIC.md L14-16·L19·L152-154 직접 재열람 후 confirmed
```

**당신의 독립 검증**:
- analysis/DIFFICULTY_RUBRIC.md 해당 행 직접 확인
- 내용 및 인용 정확성 재점검
- 결론: 동의 / 불동의 / 신규 발견

---

## 3. 추가 검증 사항

### 새로운 발견 여부

N1~N5 외에 rev-writer round 2의 다른 수정사항에서 오류 발견 시:
- 항목명 명시
- 근거 코퍼스 구간 명시
- 기대값 vs 실측값 명시

---

## 4. 제약 및 절차

**Write Surface**:
- ✅ output/260831/rev/ 하위 tier-2 round 2 보고서 작성
- ✅ output/260831/rev/_index.md 행 추가 (reflect_state 갱신)
- ✅ analysis/REV_LOG.md 행 추가
- ❌ 원본 산출물·카탈로그 수정 금지

**슬라이스 체크포인트**:
- 각 N항목 검증 후 WIP 즉시 행 추가
- WIP: `analysis/wip/rev-auditor_260831_3tier.md`

**라운드 루프** (≤5R):
- 동일 이의 재현 시 escalate 표시
- 종결: tier-1 vs tier-2 round 2 동의, 또는 arbiter 상향

---

## 5. 회신 위치 및 형식

**산출물** (회신 첫 문장):
```
Pipeline : [1 refine]──▶[2 propose]──▶[3 review]──────▶[4 arbiter]
                                        ▲ R2 tier-2
Stage    : re-verified N1~N5 against originals — M agree, N disagree, K new findings
Team     : actor=rev-auditor; WIP=rev-auditor_260831_3tier.md; round=2
Next     : [if converged] arbiter ruling on DQ-SC-1/SS-2 + N1/N2 정정 승인
```

**회신 파일**:
```
output/260831/rev/260831_02_tier2_round2_findings.md
```

---

## 6. 체크리스트

- [ ] **N1** (KO 배점): 코퍼스 L36 재합산 완료
- [ ] **N2** (CP-SM2-1): 6과목 전수 비율 재실측 완료
- [ ] **N3** (CP-HI-2): 한국사 2.2점 문항 재확인 완료
- [ ] **N4** (HI 40:60): 선택/서답 배점 재확인 완료
- [ ] **N5** (KO DIFFICULTY_RUBRIC): 파일 L14-16·L19 재확인 완료

---

**회람문 준비 완료**  
**rev-auditor tier-2 round 2 호출 즉시 가능**

