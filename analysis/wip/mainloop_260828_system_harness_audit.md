---
actor: main-loop
task: system_harness_audit
target: "CLAUDE.md · AGENTS.md · REV_GUIDE §5 · .claude/agents/*.md(11) · tools/*.py(9) · analysis/wip/*(24)"
status: done
updated: 260828
---

# WIP — 하네스 구조 감사 (메인 루프)

규격 ②는 서브에이전트에만 걸려 있어 메인 루프는 체크포인트 의무가 없었다. 이번 세션이
compact를 한 번 겪었고 복구된 것은 호스트 요약이지 체크포인트가 아니었으므로, 감사 S5·P-F의
자기적용으로 이 파일을 만든다. 배타 소유 = main-loop.

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | 배우 정의 11종 인벤토리 (tools:/model: 결합) | done | — | 원칙 ④ 위반 0건 — 260826 A1 3종은 이미 수정 반영됨 |
| 2 | 게이트 도구 9종 exit-path 스캔 | done | — | fail-open 2건 발견 (build_mastery · import_grading) |
| 3 | 계약 검사기 성격 판정 | done | — | 마커 존재 검사기 = codex-team `require_report()`와 동일 결함 유형 |
| 4 | 원칙 10 구현률 측정 | done | — | 8개 정본 중 1개(REV_GUIDE §5)만 구현 |
| 5 | WIP 원장 24건 규격 검사 | done | — | 이탈 3건 (status 열거값 1 · NEXT 누락 2) |
| 6 | 오탐 기각 (슬라이스·고아경로·도구부여) | done | — | 감사서 S6에 기록 |
| 7 | 수정 A — 계약 검사기 구조 검사 4종 추가 | done | tools/check_assurance_contract.py | PASS(0) → 26 failures로 이빨 실증 |
| 8 | 수정 B — fail-closed 전환 2종 | done | tools/build_mastery.py · import_grading.py | warnings를 [OK]보다 먼저 출력 + exit 1 |
| 9 | 수정 C — 연속성 규칙 11개 정의 전파 | done | .claude/agents/*.md | 26 → 3 failures |
| 10 | 수정 D — 메인 루프 WIP에 NEXT 보정 | done | analysis/wip/mainloop_260826_cycle0_S0.md | codex-omx 소유 2건은 미수정(배타 소유) |
| 11 | 감사서 작성 | done | analysis/rev/260828_02_system_harness_audit.md | S1~S6 · 수정 A~D · 승인요청 P-A~P-F |
| 12 | P-C — 동반 갱신 목록 8개 정본 신설 | done | CLAUDE.md · AGENTS.md · FORECAST_GUIDE · DOC_LOCATION · TYPE_CATALOG · CODE_REGISTRY · catalog/_README · DATA_STANDARD | 의존처는 grep 실측 |
| 13 | 계약 검사기 5번째 검사(동반갱신 목록 존재) 추가 | done | tools/check_assurance_contract.py | REV_GUIDE §5 blockquote 형식도 통과하도록 부분문자열 검사 |
| 14 | 최종 게이트 재실행 · 회귀 확인 | done | — | 잔여 3건 = codex-omx WIP 2파일. 회귀 0건 (catalog·mastery 모두 exit 0) |
| 15 | P-D — REV_GUIDE §5 대행 배우 행 + 발동조건 2요건 | done | analysis/REV_GUIDE.md §5 | 3단계 루프 우회 방지 위해 제안 등급 한정 명시 |
| 16 | P-G — CLAUDE.md ② 적용 대상에 메인 루프 추가 | done | CLAUDE.md | `mainloop_<YYMMDD>_<task>.md` 명명 규정 |
| 17 | P-E — 원장 기입 (_index 2행 · REV_LOG 2행) | done | analysis/rev/_index.md · analysis/REV_LOG.md | reviewer=main-loop. REV_LOG에 시스템 층 절 신설(종전 절은 전부 output/ 기준) |
| 18 | 자/산출물 소유 분리 정본화 (사용자 지적) | done | CLAUDE.md 원칙 12 · AGENTS.md 비협상규칙 · REV_GUIDE §5 · 감사서 §G | F6·F9를 실행 레인 과제로 인계하려 한 처분 철회. 게이트 3종 재실행 회귀 0건 |

## 차단 조건
- `analysis/wip/codex-omx_260827_cycle0_s1_restart.md`(status='complete') 및
  `..._s2_staged_dispatch.md`(status·NEXT 없음)는 **배타 소유자가 아니라 수정 불가**(원칙 8).
  계약 게이트는 이 2파일 때문에 exit 1을 유지한다 — 의도된 fail-closed 상태다.
- P-D(REV_GUIDE §5 배우 행 신설)·P-E(_index·REV_LOG 기입)는 사용자 승인 대기.

## 검증 명령
```
python tools/check_assurance_contract.py     # 기대: 3 failure(s), exit 1, 전부 codex-omx WIP
python tools/build_catalog_index.py --check  # 기대: [OK] ... (131 rows), exit 0
python tools/build_mastery.py --check        # 기대: [OK] ... (131 rows) + warnings=0, exit 0
```

NEXT: (완료 — 슬라이스 1~17 전건 done. P-A·P-B는 사용자 소관이라 이 WIP의 재개 대상이 아니다)
