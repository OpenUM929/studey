# 슬라이스 6 재개 회람문 (사전 작성)

**날짜**: 260831  
**발신**: Claude Code (Main Loop, 재개 명령)  
**수신**: type-proposer (Opus 서브에이전트) — 슬라이스 6 단독

**실행 시점**: 2026-08-31 13:00+ (Asia/Seoul, Opus rate limit 리셋 후)

---

## 1. 대상 문서 경로

**단독 과목 유닛** (이전 5개와 분리):
- `corpus/EX-history-20252M/` (한국사2)

**REFINE 상태**: ✅ 완료 (transcript.md · meta.yml · verify_log.tsv 존재)  
**PROPOSE 상태**: ❌ 미실행 (이전 rate limit 차단)

---

## 2. 참고 정본 (읽기 전용)

- `analysis/catalog/_README.md` — 유형 카탈로그 형식 규격
- `analysis/catalog/CODE_REGISTRY.md` — ID 명명 정책 (접두어: `F` 역사 스코프)
- `analysis/catalog/history.md` (기존 카탈로그 F-01~08)
- `analysis/curriculum_2022.md` — 교육과정 범위 가드
- ⚠️ **curriculum_2022.md 2학기 과목 절 부재**: 범위 가드 불가능 (INT-5, DQ-SC-2 참조)

---

## 3. 이번 슬라이스 작업 (R1-Slice6)

**범위**: 2025-2중간 한국사(F) × 1회차

**작업 분할** (서브에이전트 단독 수행):

| 슬라이스 | 과목 | 대상 | 산출물 |
|---------|------|------|--------|
| 6 | 한국사(F:역사) | EX-history-20252M | 260831_01_type_analysis_HI.md + 260831_01_catalog_update_HI.md |

---

## 4. 판정 요청 (3-tier review 진행 조건)

### 판정 가능 질문형:

1. **완성도**: 한국사 문항 수 integrity check(예상/실제 대조), per-item 할당 완료되었나?
   - [ ] 완료 (슬라이스 6 산출물 생성)
   - [ ] ▲ 부분실패 (차단 조건 명시)

2. **카탈로그 연속성**: 기존 유형(F-01~08)의 빈도·별표 업데이트와 신규 유형 초안이 _README.md 형식에 정확히 부합하나?
   - [ ] 준거 (형식 완전히 일치)
   - [ ] 경고 (형식 편차, 지정)

3. **범위 가드**: 2025년 2학기 범위 내 항목만 포함되었나?
   - [ ] 확인 (마킹 완료)
   - [ ] ⚠️ 범위 정보 부족 (curriculum_2022.md 2학기 절 부재 — INT-5 동반)

4. **증거 인용**: 모든 분석 주장이 item no. + page(pNN 또는 transcript L<n>) + 기존 유형 ID로 추적 가능한가?
   - [ ] 추적가능 (전 항목)
   - [ ] ⚠️ 페이지 렌더 부재 (INT-1, 6과목 공통 — 대체: transcript L<n>)

---

## 5. 제약 및 절차

**Write Surface** (REV_GUIDE §5):
- ✅ 허용: `output/260831/` 하위 proposal 문서 (2개)
- ✅ 허용: `corpus/EX-history-20252M/verify_log.tsv` append
- ❌ 금지: 카탈로그 직접 수정 (analysis/catalog/history.md)
- ❌ 금지: EXTRACTION_LOG/HARVEST_LOG 직접 수정

**슬라이스 체크포인트**:
- 완료 직후 WIP 파일에 **즉시** 행 기록 필수
- WIP: `analysis/wip/type-proposer_260831_25-2M.md`
- 형식: CLAUDE.md §서브에이전트 공통 실행 규격 ②
- ⚠️ 이전 슬라이스 5에서 WIP 갱신이 6분 지연됨 → 이번엔 완료 직후 즉시 기록

**컨텍스트 한계** (원칙 ⑤):
- 남은 컨텍스트 60% 이하 → 새 슬라이스 금지, 현재 정리 후 중단
- HOLD 시: WIP에 복구 명령 기록

---

## 6. 회신 위치 및 형식

**위치**: `output/260831/` 디렉토리

**산출물 목록** (회신 시 첫 문장):
```
Pipeline : [1 refine]──▶[2 propose]──▶[3 review]──▶[4 arbiter]──▶[5 apply]
                           ▲ resume S6
Stage    : proposed 1 subject (HI) — N items assigned, M new drafts, K update diffs
Team     : mode=solo; actor=type-proposer(Opus); independence=independent-context
Next     : main loop starts 3-tier review on all 6 subjects (output/260831/*_analysis.md)
```

**반환 값**:
- 예상/실제 문항 수 대조 결과
- per-item 할당 커버리지(%)
- 신규 유형 초안 수
- 기존 유형 업데이트 diff 수
- 차단된 항목 및 사유
- INT-1, INT-5 동반 표시

---

## 7. 참고사항

**중요**: 이전 5개 과목(KO/SM2/EN/SC/SS) 산출물과 동일한 차단 조건 예상

| 차단 ID | 영향도 | 설명 |
|---------|--------|------|
| INT-1 | 전건 | `corpus/_images/EX-history-20252M/` pNN.png 0건 → 페이지 인용 불가능 → PROVISIONAL 마킹 |
| INT-5 | 범위 가드 | curriculum_2022.md 2학기 절 부재 → 교육과정 범위 확인 불가능 → ⚠️ 주석 |

---

## 8. 실행 권한

**executor**: type-proposer (이 메시지 수신자)  
**근거**: `.claude/agents/type-proposer.md` — Opus 모델 + 슬라이스 분할 호출 허용

**Main Loop 역할**:
- 13:00 리셋 확인 후 이 회람 발신 (또는 새 회차로 전달)
- 산출물 수신 및 WIP 즉시 확인
- 모든 6개 과목 완료 후 3-tier review loop 진행

---

## 9. 주의사항

### 체크포인트 (CLAUDE.md 원칙 ②)

**완료 직후 필수**:
```markdown
| 6 | 한국사(F) | EX-history-20252M | done | output/260831/260831_01_type_analysis_HI.md, ... | notes |
```

⚠️ **지연 금지** — 이전 슬라이스 5가 6분 늦게 기록됨

### 차단 조건 충돌 (원칙 9-a)

INT-1과 INT-5가 모든 슬라이스에 동반되므로:
- 100% 커버리지 주장 금지
- PROVISIONAL 마킹 필수
- 차단 조건 명시 필수

---

**회람 사전 작성 완료** / **13:00 Asia/Seoul 리셋 후 발신 예정**

*이 문서는 type-proposer가 붙여넣기로 바로 작업 착수할 수 있도록 자기완결 형식으로 작성됨.*
*REV_GUIDE §6-b 회람문 규격 준수.*
