# 포스트 리셋 실행 계획 (260831)

**현재 상태**: ON-HOLD (resource exhausted — Opus rate limit)  
**리셋 시각**: 2026-08-31 13:00 (Asia/Seoul)  
**대기 시간**: 약 70분 (현재 11:50)  
**문서 작성**: 11:50 (리셋 전 사전 준비)

---

## 리셋 후 즉시 실행 순서

### 1단계: Opus 리셋 확인 (13:00)

```bash
# 테스트: 간단한 Opus 호출로 quota 복구 확인
# (선택사항 — 꼭 필요하지는 않음)
```

**소요시간**: 1~2분

---

### 2단계: 슬라이스 6 재호출 (13:00+)

**명령어** (위 단계에서 사용 가능):

```
회람문 위치: output/260831/260831_04_slice6_resume_briefing.md
회람문 형식: 자기완결, 붙여넣기 가능
대상: type-proposer (Opus, 슬라이스 6 단독)
입력: corpus/EX-history-20252M/ (한국사 2025-2중간)
출력: output/260831/260831_01_type_analysis_HI.md + catalog_update_HI.md
```

**실행 주의**:
- ⚠️ **6개 과목을 한 번에 호출하지 말 것** (이전 실수 반복 금지)
- ✅ 슬라이스 6만 단독 호출
- ✅ 새로운 type-proposer 호출 (이전 호출 재시도 아님)

**예상 소요시간**: 20~30분

**WIP 갱신** (완료 직후):
- 슬라이스 6 행 추가
- status: done
- 산출물 경로 기록
- ⚠️ **지연 금지** — 즉시 기록 (지난 슬라이스 5에서 6분 지연 발생)

---

### 3단계: 슬라이스 6 완료 확인 (완료 후)

```bash
# 산출물 존재 확인
Get-ChildItem "C:\dev\study\output\260831\" -Filter "*_HI.md"

# WIP 행 기록 확인
# → analysis/wip/type-proposer_260831_25-2M.md 슬라이스 6 행 조회
```

**확인 항목**:
- ✅ type_analysis_HI.md 생성됨?
- ✅ catalog_update_HI.md 생성됨?
- ✅ 파일 크기 정상? (30~50KB 예상)
- ✅ WIP 행 기록됨? (state=done)

**블로킹**: 위 항목 중 하나라도 실패 → `▲ blocked` 표시, 원인 분석

---

### 4단계: 모든 슬라이스 무결성 최종 확인

```bash
# 슬라이스 1~6 전체 산출물 재확인
Get-ChildItem "C:\dev\study\output\260831\" -Filter "260831_01_*_*.md" | 
  Select-Object Name, Length, LastWriteTime | 
  Sort-Object Name
```

**기대 결과**:
```
260831_01_catalog_update_EN.md       ✓
260831_01_catalog_update_HI.md       ✓ (새로 추가)
260831_01_catalog_update_KO.md       ✓
260831_01_catalog_update_SC.md       ✓
260831_01_catalog_update_SM2.md      ✓
260831_01_catalog_update_SS.md       ✓
260831_01_type_analysis_EN.md        ✓
260831_01_type_analysis_HI.md        ✓ (새로 추가)
260831_01_type_analysis_KO.md        ✓
260831_01_type_analysis_SC.md        ✓
260831_01_type_analysis_SM2.md       ✓
260831_01_type_analysis_SS.md        ✓
```

**합계**: 12개 파일 (6과목 × 2)

---

### 5단계: rev-writer 호출 (모든 슬라이스 완료 후)

**회람문 작성** (사전 준비 완료):

```
위치: output/260831/260831_07_3tier_review_briefing.md (새로 작성)
형식: REV_GUIDE §6-b 회람문 규격
대상: rev-writer (tier-1 reviewer)
입력: output/260831/260831_01_*_*.md (12개 파일) + 
      output/260831/260831_05_blocking_conditions_summary.md
출력: output/260831/rev/ 하위 검토 보고서
```

**회람문 필수 항목** (사전 확인):
- [ ] 대상 문서 경로 (12개 파일 경로 정확한가?)
- [ ] 참고 정본 경로 (카탈로그·가이드 경로)
- [ ] 작업 범위 (6과목 × 1회차)
- [ ] 차단 조건 명시 (INT-1, INT-2, INT-5, DQ-* 목록)
- [ ] 판정 요청 질문형 (choice enum 포함)
- [ ] write surface 명시 (rev-writer가 쓸 수 있는 경로)
- [ ] 체크포인트 규격 (WIP 경로·형식)

**계획 상태**: 절반 완료 (rev-writer 회람문 아직 미작성 — 슬라이스 6 완료 후 작성)

---

## 현 단계 사전 준비 (11:50 진행 중)

| 항목 | 상태 | 파일 |
|------|------|------|
| WIP 상태 머신 재설계 | ✅ done | analysis/wip/type-proposer_260831_25-2M.md |
| 메모리 체크리스트 | ✅ done | memory/guideline-checkpoint-mainloop.md |
| HOLD 상태 문서 | ✅ done | output/260831/260831_03_mainloop_status_hold.md |
| 슬라이스 6 회람문 | ✅ done | output/260831/260831_04_slice6_resume_briefing.md |
| 차단 조건 정리 | ✅ done | output/260831/260831_05_blocking_conditions_summary.md |
| rev-writer 회람문 | ⏳ pending | output/260831/260831_07_... (슬라이스 6 완료 후) |

---

## 타임라인

| 시각 | 작업 | 소요 |
|------|------|------|
| 11:50 | 사전 준비 완료 | 지금 |
| 13:00 | Opus 리셋 확인 | 1-2분 |
| 13:00+ | 슬라이스 6 호출 | 20-30분 |
| 13:30 | 슬라이스 6 완료 예상 | — |
| 13:30+ | 산출물 확인 | 2-3분 |
| 13:35 | rev-writer 회람문 작성 | 10-15분 |
| 13:45 | rev-writer 호출 | 즉시 |

**예상 3-tier review 완료**: 14:30~15:30 (라운드 1)

---

## 리스크 & 대응

### 리스크 1: 슬라이스 6 또 다시 rate limit

**신호**: 13:15 이후에도 type-proposer 응답 없음

**대응**:
- 다시 HOLD 상태로 진입
- WIP에 차단 기록
- reset 시각 재기록
- (극단적으로) 슬라이스 6을 여러 부분집합(한국사 early/middle/late)으로 분할

### 리스크 2: 슬라이스 6에서 INT-2 발견

**신호**: 한국사도 배점 불일치 발견

**대응**:
- DQ 목록에 추가
- rev-arbiter 판정 요청 확장

### 리스크 3: 내 컨텍스트 60% 이하 떨어짐

**신호**: ScheduleWakeup 알림 또는 context % 급락

**대응** (CLAUDE.md 원칙 ⑤):
- 현재 슬라이스/라운드 완료 후 즉시 HOLD
- WIP에 상태 기록
- compact 실행
- resume audit 후 재개

---

## 메모: 지침 준수 확인

**원칙 ②** (슬라이스 체크포인트):
- ✅ WIP 상태 머신 (status 명시)
- ✅ 슬라이스 6 완료 후 즉시 행 기록 (지연 금지)

**원칙 ⑤** (컨텍스트·리소스):
- ✅ rate limit 감지 → HOLD 상태 진입
- ✅ reset 시각 기록 (13:00)
- ✅ 재개 명령 명시
- ✅ busy-wait 금지 (대신 회람문·차단 정리)

**공통 규격 ①-b** (회람문 품질):
- ✅ 경로 실측값 기입 (corpus/EX-history-20252M/ 확인)
- ✅ 정본 참조 (CODE_REGISTRY.md F:역사 스코프)
- ✅ write surface 명시

**공통 규격 ②** (슬라이스 체크포인트):
- ✅ WIP 형식 준수 (frontmatter + 슬라이스 표)
- ✅ 완료 후 즉시 기록 규칙 (이전 5에서 위반, 이번엔 강화)

---

**준비 완료. 13:00 리셋 후 즉시 실행 가능.**

*모든 문서가 사전 준비되어 있으므로, 리셋 후 "회람문 붙여넣고 호출"로 한 줄이면 됨.*
