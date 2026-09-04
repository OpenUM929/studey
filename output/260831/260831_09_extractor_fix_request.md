# Type-Extractor 수정 요청 (N2: KO 배점)

**발신**: Claude Code (Main Loop)  
**수신**: type-extractor  
**대상**: corpus/EX-korean-20252M/meta.yml 배점 정정

**실행 시점**: 2026-08-31 15:00+

---

## 배경

### Rev-Auditor 발견 (N2)

**문제**: 
```
meta.yml 기록: 배점 합 = 60.4
실제 29개 항목: 배점 합 = 60.0 (정확)
```

**영향**:
- meta.yml → transcript.md → type-proposer 제안 → tier-1 재계산 전파
- 결과: tier-1이 CP-SM2-1 판정에 60.4를 기준으로 사용
- Cascade: KO 오류 → 전 과목 패턴 판정 오류로 확산

---

## 수정 항목

**파일**: `corpus/EX-korean-20252M/meta.yml`

**변경 사항**:
```yaml
# 현재
exam_total_points: 60.4

# 수정
exam_total_points: 60.0
```

**근거**:
- 29개 항목 × 평균 2.069점 = 60.0 (합산 확인)
- transcript.md 기존 서술형 배점 인덱스 재확인

---

## 검증 방법

수정 후 다음 명령 실행:
```bash
# corpus/EX-korean-20252M/meta.yml 배점 재점검
Get-Content corpus/EX-korean-20252M/meta.yml | Select-String "exam_total_points"

# 수정됨 확인 → 60.0
```

---

## Write Surface

- ✅ 수정 대상: `corpus/EX-korean-20252M/meta.yml` (1개 행)
- ❌ 금지: transcript.md, verify_log.tsv 수정 (정제 재수행 불필요)

---

## 체크포인트

**WIP 파일**: `analysis/wip/type-extractor_260831_fix_N2.md`

```markdown
---
actor: type-extractor
task: N2_KO_배점정정
target: corpus/EX-korean-20252M/meta.yml
status: done
updated: 260831 15:XX
---

| 슬라이스 | 대상 | 수정 | 상태 | 비고 |
|---------|------|------|------|------|
| 1 | meta.yml | exam_total_points: 60.4→60.0 | done | rev-auditor N2 승인 |

NEXT: none (meta.yml 수정 완료)
```

---

## 다음 단계

수정 완료 후:
1. **type-proposer**: CP-SM2-1 재구조화 호출 (배점 정정 반영)
2. **rev-writer**: tier-1 재검토 호출

---

**수정 권한**: checkpoint 기록 후 즉시 반영

