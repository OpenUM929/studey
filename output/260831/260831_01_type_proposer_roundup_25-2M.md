# 회람문: type-proposer 호출 — 2025-2중간 전 과목 유형분석

**날짜**: 260831  
**발신**: Claude Code (Main Loop, 단독 운영)  
**수신**: type-proposer (Opus 서브에이전트)

---

## 1. 대상 문서 경로

각 과목 corpus 유닛 (총 6개):
- `corpus/EX-korean-20252M/` (국어2)
- `corpus/EX-math2-20252M/` (수학2)
- `corpus/EX-english-20252M/` (영어2)
- `corpus/EX-science-20252M/` (통합과학2)
- `corpus/EX-social-20252M/` (통합사회2)
- `corpus/EX-history-20252M/` (한국사2)

**REFINE 상태**: ✅ 모두 완료 (transcript.md · meta.yml · verify_log.tsv 존재)  
**PROPOSE 상태**: ❌ 미실행

---

## 2. 참고 정본 (읽기 전용)

- `analysis/catalog/_README.md` — 유형 카탈로그 형식 규격
- `analysis/catalog/COMMON_TYPES.md` — 기존 공통 유형
- `analysis/catalog/TYPE_MASTER.md` — 분석 축(A×B×C×D×E)
- `analysis/catalog/DIFFICULTY_RUBRIC.md` — Tier/DF 판정 기준
- `analysis/catalog/CODE_REGISTRY.md` — ID 명명 정책 (접두어: KO/M2/EN/SC/SS/HI)
- `analysis/curriculum_2022.md` — 교육과정 범위 가드
- `analysis/FORECAST_GUIDE.md` — 예측 소비자 요구사항
- 기존 카탈로그 (각 과목별):
  - `analysis/catalog/korean.md` (KO-nn)
  - `analysis/catalog/math2.md` (SM2-01~33)
  - `analysis/catalog/english.md` (EN-nn)
  - `analysis/catalog/science.md` (SC-nn)
  - `analysis/catalog/social.md` (SS-nn)
  - `analysis/catalog/history.md` (F-01~08)

---

## 3. 이번 라운드 작업 (R1)

**범위**: 2025-2중간 전 과목 (6개) × 1회차

**작업 분할** (서브에이전트 단독 수행):

**⚠️ 정정(260831)**: 회람문의 접두어 `KO/M2/EN/SC/SS/HI`는 CODE_REGISTRY §1 정본과 불일치.
정본 접두어 사용:
- 국어: `K`
- 수학2: `SM2`
- 영어: `T` 또는 `W`
- 통합과학: `GB`·`GT`·`MC`·`ER`·`CH`·`BI`·`UN` (단원별)
- 통합사회: `F`(사회 스코프)
- 한국사: `F`(역사 스코프)

**type-proposer는 정본을 우선하므로 위 정본 접두어를 적용하고 산출물 파일명에는 subject code(KO/SM2/etc) 사용.**

| 슬라이스 | 과목 | 대상 | 산출물 |
|---------|------|------|--------|
| 1 | 국어(K) | EX-korean-20252M | 260831_01_type_analysis_KO.md + 260831_01_catalog_update_KO.md |
| 2 | 수학2(SM2) | EX-math2-20252M | 260831_01_type_analysis_SM2.md + 260831_01_catalog_update_SM2.md |
| 3 | 영어(T/W) | EX-english-20252M | 260831_01_type_analysis_EN.md + 260831_01_catalog_update_EN.md |
| 4 | 통합과학(GB·GT·MC·ER·CH·BI·UN) | EX-science-20252M | 260831_01_type_analysis_SC.md + 260831_01_catalog_update_SC.md |
| 5 | 통합사회(F:사회) | EX-social-20252M | 260831_01_type_analysis_SS.md + 260831_01_catalog_update_SS.md |
| 6 | 한국사(F:역사) | EX-history-20252M | 260831_01_type_analysis_HI.md + 260831_01_catalog_update_HI.md |

---

## 4. 판정 요청 (3-tier review 진행 조건)

### 판정 가능 질문형:

1. **완성도**: 각 과목의 integrity check(예상/실제 문항 수 대조), per-item 할당, 통합이 각각 완료되었나?
   - [ ] 완료 (모든 슬라이스 6개 과목 산출물 생성)
   - [ ] ▲ 부분실패 (차단 조건 명시)

2. **카탈로그 연속성**: 기존 유형(KO-nn 등)의 빈도·별표 업데이트와 신규 유형 초안이 _README.md 형식에 정확히 부합하나?
   - [ ] 준거 (형식 완전히 일치)
   - [ ] 경고 (형식 편차, 지정)

3. **범위 가드**: curriculum_2022.md 기준으로 2025년 2학기 범위 내 항목만 포함되었나? (교육과정 밖 항목은 🚧 마킹됨)
   - [ ] 확인 (마킹 완료)
   - [ ] ▲ 범위 이탈 발견 (항목 지정)

4. **증거 인용**: 모든 분석 주장이 item no. + page(pNN) + 기존 유형 ID로 추적 가능한가?
   - [ ] 추적가능 (전 항목)
   - [ ] ▲ 미인용 발견 (범위 지정)

---

## 5. 제약 및 절차

**Write Surface** (REV_GUIDE §5):
- ✅ 허용: `output/260831/` 하위 proposal 문서 (2개/과목 × 6 = 12개)
- ✅ 허용: `corpus/*/verify_log.tsv` append (분석 단계 기록)
- ❌ 금지: 카탈로그 직접 수정 (analysis/catalog/*.md) — 판정 승인 후 Main Loop가 반영
- ❌ 금지: EXTRACTION_LOG/HARVEST_LOG 직접 수정 — append-only 관계자만

**슬라이스 체크포인트**:
- 각 과목(슬라이스) 완료 직후 WIP 파일에 행 기록 필수
- WIP: `analysis/wip/type-proposer_260831_25-2M.md`
- 형식: CLAUDE.md §서브에이전트 공통 실행 규격 ② 참조

**컨텍스트 한계** (원칙 ⑤):
- 남은 컨텍스트 60% 이하 → 새 슬라이스 금지, 현재 슬라이스 정리 후 중단
- HOLD 시: WIP에 복구 명령 기록

---

## 6. 회신 위치 및 형식

**위치**: `output/260831/` 디렉토리

**산출물 목록** (회신 시 첫 문장):
```
Pipeline : [1 refine]──▶[2 propose]──▶[3 review]──▶[4 arbiter]──▶[5 apply]
                           ▲ done
Stage    : proposed 6 subjects (KO/SM2/EN/SC/SS/HI) — 100% items assigned, N new drafts, M update diffs
Team     : mode=solo; actor=type-proposer(Opus); independence=independent-context
Next     : main loop starts review (output/260831/*_analysis.md + *_catalog_update.md)
```

**반환 값**:
- 예상/실제 문항 수 대조 결과 (과목별)
- per-item 할당 커버리지(%)
- 신규 유형 초안 수
- 기존 유형 업데이트 diff 수
- 공통유형 후보 수
- 차단된 항목(BLOCKED) 및 사유
- 개방형 질문/의논사항

---

## 7. 참고사항

**2025-2중간 범위** (사용자 확정):
- 교육과정: 2022 개정 기준, 각 과목의 2학년 1학기 단원 기준
- **기출 범위**: 확정됨 (각 카탈로그 헤더 참조)
- **예측 소비자**: 후속 forecast-writer가 이 분석 결과로 등급(A~E) 산정

**ID 부여 규칙**:
- 기존 유형 재사용 → 기존 ID 유지 (예: KO-01)
- 신규 유형 → CODE_REGISTRY 접두어 + 일련번호 (예: KO-09, KO-10)
- 다중 과목 신설 아님 (각 과목 독립 ID)
- 신규 ID 제안 시 CODE_REGISTRY에 **미등록 정책**이 있으면 **decision request** (rule 4)

---

## 8. 실행 권한

**executor**: type-proposer (이 메시지 수신자)  
**근거**: `.claude/agents/type-proposer.md` — Opus 모델 + 독립 분석 권한

**Main Loop 역할**:
- 이 회람 발신 후 서브에이전트 호출
- 산출물 수신 및 WIP 확인
- 3-tier review loop 진행
- 판정(rev-arbiter) 기반 카탈로그 반영

---

**회람 발신 완료** / **Main Loop 승인 대기 중**

---

*이 문서는 type-proposer가 붙여넣기로 바로 작업 착수할 수 있도록 자기완결 형식으로 작성됨.*
*REV_GUIDE §6-b 회람문 규격 준수.*
