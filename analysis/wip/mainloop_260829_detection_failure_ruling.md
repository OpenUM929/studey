---
actor: main-loop
task: detection_failure_ruling
target: "output/260829/rev/detection-failure-audit/ 7파일 — [CC 회람] 260829_01 Q1~Q7 판정"
status: done
updated: 260829
---

# WIP — 260829_01 탐지 실패 감사 판정 (tier-3 대행)

메인 루프가 tier-3 판정 역할을 직접 수행한다(`rev-arbiter` 서브에이전트 미배치 — 회람
`<constraints>`가 subagent 금지). 라벨 도용 금지 규칙에 따라 WIP 파일명은 `mainloop_`이며,
판정문 frontmatter에 fresh-context 결격을 명시한다.

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | 회람 수신 · FINAL_REPORT + 04_GATE 정독 | done | — | Q1~Q7 · BLOCKED 판정 구조 파악 |
| 2 | 동결 13파일 해시 독립 재계산 | done | — | 13/13 일치 (CLAUDE.md 27763/36b919c5 … gate_selftest 10621/69e8610d) |
| 3 | meta_gate · gate_selftest 독립 재실행 | done | — | meta_gate failures=7 exit 1 · selftest baseline_failures=5 exit 1 — 보고서 §7과 일치 |
| 4 | F1 코드 실측 (`check_experiment.py:223`) | done | — | `print(f"warnings=0")` 리터럴 확인 |
| 5 | F6 코드 실측 (`check_experiment.py:143`) | done | — | `if not 5 <= len(rows) <= 12` + exact-cover 확인 |
| 6 | F6 원천 재산출 — `author/types.tsv` 직접 계수 | done | — | **12행 = 재사용 9 + 우산 2(독립 subgroup 6) + BLOCKED 1** → 정직 행수 16 = 재사용 6 + 단독 9 + blocked 1, 22문항 정확 포괄. 보고서의 "raw 부재로 16 재산출 불가"는 **반증됨** |
| 7 | F9 원천 재유도 — `corpus/EX-math2-20252M/transcript.md` 44~50행 판독 | done | — | 44=`## 4.` · 48=본문 끝 · 49=공백 · 50=`# 단답형 문항`. rule_a(다음 heading 직전)가 21/22의 실제 규칙이고 W-04만 이탈 → 원인은 `##`만 인식한 파서. **span 규칙 확정 가능** |
| 8 | F10 신규 발견 — 동결 경계 자기소유 | done | — | 13파일 목록은 `00_PREFLIGHT.md`(피측정 레인 자체 작성)이고, 동결 파일이 경로로 지목하는 `corpus/.../transcript.md`·`author/types.tsv`·`author/items.tsv`가 전부 저장소에 실재하는데 제외됨 |
| 9 | Q1~Q7 판정문 작성 | done | output/260829/rev/detection-failure-audit/260829_01_detection_failure_ruling.md | accept 2 · revise-required 2 · binding 3 |
| 10 | REV_LOG 1행 기입 | done | analysis/REV_LOG.md | 시스템 층 절 |

## 차단 조건
- 판정자가 fresh-context가 아니다 — 이 세션이 260828 감사(F1~F9)와 CLAUDE.md 원칙 12의 작성자다.
  Q1·Q2는 자기확증 위험이 있어 **사용자 2차 키**를 조건으로 단다(원칙 12-c).
- 자(ruler) 파일 자체는 이 라운드에서 수정하지 않았다(REV_GUIDE §5 신설 문단). 판정은 정책만
  확정하고 구현은 비피측정 implementer 몫으로 남긴다.

## 검증 명령
```
python -X utf8 output/260828/rev/meta_gate_260828.py --check all   # 기대: failures=7, exit 1
python -X utf8 output/260828/rev/gate_selftest_260828.py           # 기대: baseline not clean, exit 1
python tools/check_assurance_contract.py                           # 기대: 3 failure(s), exit 1 (codex-omx WIP)
python tools/build_catalog_index.py --check                        # 기대: [OK] (131 rows), exit 0
python tools/build_mastery.py --check                              # 기대: [OK] (131 rows) + warnings=0, exit 0
```

NEXT: (완료 — 슬라이스 1~10 전건 done. Q3~Q5 구현·재동결은 사용자 2차 키 확인 후 별도 라운드)
