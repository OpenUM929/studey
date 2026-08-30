---
actor: main-loop
task: ruling_standardization
target: "analysis/REV_GUIDE.md §3 rule 6 · §6-d 신설 · .claude/agents/rev-arbiter.md · 260829_01 등급 정정"
status: done
updated: 260829
---

# WIP — 판정 요청·판정문 표준화 + 정지 규칙 (사용자 지시 3건)

사용자 지시: ① 라운드 3 배우는 메인 루프가 판단하고, 판정 요청 프롬프트·출력 방식을 표준
규격으로 제약할 것 ② 실험은 재실행·재시험하므로 현 산출물을 확정 입력으로 승격하지 말 것
③ 종료 조건을 REV_GUIDE에 추가할 것.

근거 실측(이 라운드에서 확정, 스크래치패드 `span_check.py`):
- `rule_a(heading only)` → mismatch 2/22 (W-04 48↔49, S-18 146↔148) — 260829_01 BF3 오류 확정
- `rule_a + horizontal-rule` → mismatch 1/22 (W-04 단독) — 최소 수리 폐쇄 확인
- `check_experiment.py:230` PASS marker = `experiment-gate: PASS` (`[OK]` 아님) — BF1 인용 오류 확정
- REV_GUIDE §5 대행 행 = "산출물은 제안 등급" — 260829_01의 binding/approve 라벨 권한 초과 확정

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | Codex 응답 5파일 SHA-256 독립 재계산 | done | — | 5/5 일치 (CODEX_TEAM_RESPONSE 2dd71e39…, 06 09650d1c…, 07 1b88103d…, 08 cb466c48…, 260829_01 171bc088…) |
| 2 | S-18 반례 검증 + 최소 수리 폐쇄 22행 전수 | done | — | 위 실측. 코덱스 지적 확정 / 코덱스 remedy는 과대범위 |
| 3 | PASS marker 실측 | done | — | `:230` `experiment-gate: PASS` |
| 4 | 권한 등급 근거 확인 (REV_GUIDE §5) | done | — | 대행 = 제안 등급 |
| 5 | 라운드 3 배우 판단 | done | — | **round 3 미실시** — 재실행으로 대상이 stale. `rev-arbiter`는 재실행 산출물에 배치 |
| 6 | §3 rule 6 정지 규칙 신설 | done | analysis/REV_GUIDE.md | open-unit 단조 축소 · 신규 선행조건 차단 금지 · 수렴 3요건 |
| 7 | §6-d 판정 요청·판정문 표준 규격 신설 | done | analysis/REV_GUIDE.md | 요청 패킷 6필드 + 판정문 7열 + 3대 강제(실측·폐쇄·등급유도) |
| 8 | 원칙 10 동반 갱신 — rev-arbiter 정의에 §6-d 반영 | done | .claude/agents/rev-arbiter.md | 정본만 고치면 아무도 안 지킨다 |
| 9 | 260829_01 등급 정정 + history 추가 | done | output/260829/rev/detection-failure-audit/260829_01_… | status → proposal-grade, BF1·BF3 오류 자인 |
| 10 | REV_LOG 1행 · 게이트 재실행 | done | analysis/REV_LOG.md | 회귀 확인 |

## 차단 조건
- 자(ruler: `ACCEPTANCE_SCHEMA`·`EXPECTED_ITEM_IDS`·게이트 코드) 무수정 유지 — 원칙 12.
- Codex 소유 문서(06·07·08·CODEX_TEAM_RESPONSE) 무수정 — 원칙 8.
- 260829_01은 내가 작성 주체이므로 등급 정정·history 추가만 하고 판정 본문은 재작성하지 않는다
  (원칙 3 append-only).

## 검증 명령
```
python tools/check_assurance_contract.py     # 기대: 3 failure(s), exit 1 (codex-omx WIP 2건 잔류)
python tools/build_catalog_index.py --check  # 기대: [OK] ... (131 rows), exit 0
python tools/build_mastery.py --check        # 기대: [OK] ... (131 rows) + warnings=0, exit 0
```

NEXT: (완료 — 슬라이스 1~10 전건 done. 다음 라운드는 재실행 산출물에 §6-d 규격으로 개시)
