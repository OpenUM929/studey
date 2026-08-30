---
title: 260829_01 판정 후 Codex 전문팀 재검토 배치 manifest
created: 260829
author: Codex/OMX main-loop
status: dispatch-only
---

# 1. 용도와 비권한 고지

이 문서는 사용자 요청에 따른 Q1~Q7 판정 자문을 위해 각 레인이 읽을 수 있는 입력과 배타 출력을
고정하는 **dispatch manifest**다. 수용기준·기대값·증거 동결 경계를 승인하는 ruler/refreeze가 아니며,
Codex/OMX의 사용자 2차 키 대행이나 Opus 판정 승인이 아니다. 입력 완전성은 주장하지 않는다.

# 2. 입력 manifest (16파일)

| path | bytes | sha256 |
|---|---:|---|
| `output/260829/rev/detection-failure-audit/260829_01_detection_failure_ruling.md` | 16469 | `171bc0882a845bd6654e4e555a74f96a4a3bced3eccab76ee3002612d047fbd8` |
| `output/260829/rev/detection-failure-audit/FINAL_REPORT_FOR_OPUS.md` | 19610 | `5b2c553b323f33a9ddaf064d2dceb8c3f0383249f5d13918d757974fe9e06f07` |
| `output/260829/rev/detection-failure-audit/04_GATE.md` | 17477 | `fd27ab2b7f4fd373a3554ec2e88e9ebaf64b9de82aca4fbeab73b89f71eb3be8` |
| `output/260829/rev/detection-failure-audit/00_PREFLIGHT.md` | 6445 | `81c50b0b7aa5db71fa9adbfa65c5317e19e412489266abb314bbd1b9730f1676` |
| `CLAUDE.md` | 27763 | `36b919c541c093fb70745b557a079f1380ca85748c8014adb3e2b919698c3ef9` |
| `analysis/REV_GUIDE.md` | 30908 | `b0109e323eabffb5ee275ff49d69100005bf95cbfd8c77ac4c8e1e33a8299e28` |
| `output/260828/diagnostic/math2-method-comparison/codex-team/check_experiment.py` | 8437 | `325807caff872b5a52f33603eb7ec976d66ce34f80c2c0cb9f3432043ac2eb5f` |
| `output/260828/rev/meta_gate_260828.py` | 10001 | `88ed208b1419cc9451dedc5a765abc378913f02a5fe9c8c1799ca19c888d5bb1` |
| `output/260828/rev/gate_selftest_260828.py` | 10621 | `69e8610df06223f70e7df3a4fabe137575968082a22d2f9f7b55f020a6ba96a9` |
| `output/260828/diagnostic/math2-method-comparison/codex-team/author/types.tsv` | 8598 | `0db58644f823bb874dc797bc16ea5c432144a60b405822641072a80a5c6da359` |
| `output/260828/diagnostic/math2-method-comparison/codex-team/author/items.tsv` | 15794 | `484cde845373a7a4ab68398ca185c74d0e8f3c76bfdc18f3b5bdf72de2957e07` |
| `corpus/EX-math2-20252M/transcript.md` | 8336 | `9e2ed478c120c790327eec4e68404bbfbf6e50028f099934b22803d3671744be` |
| `output/260828/rev/ACCEPTANCE_SCHEMA_260828.repaired.md` | 3377 | `2a5d8bda46bcb270784560b47d43944886219a08063e9965e6c0105433dd225b` |
| `.codex/agents/assessment-evidence-auditor-sol.toml` | 2178 | `4797c5b68c5f279f17d9c8516c42f3187549eadef5e2cafbb88879e9a1debb85` |
| `.codex/agents/assessment-adversarial-critic-sol.toml` | 2027 | `f87ae6fbf6ba187d70af8fba252fc96bbf7fa788485c2b01cc9b1c12b9b91cf7` |
| `.codex/agents/assessment-gatekeeper-sol.toml` | 2359 | `d86863fa2601eaf506ef5a09b9a4b084b157dfb91809a031c7f84f8d148e7ed6` |

레인은 위 파일이 `source_path` 등으로 직접 지목하는 원천이 추가로 필요하면 읽을 수 있으나, 그 경로와
이유를 보고서에 기록해야 한다. 이 확장은 evidence completeness 또는 refreeze를 의미하지 않는다.

# 3. 공통 산출 스키마와 금지

- 각 쟁점: `ruling item`, `direct evidence`, `analysis`, `severity`, `disposition`, `unknown/limit`.
- Q1~Q7과 BF1~BF7의 expected/observed/missing 목록을 명시한다. 행수 합계만으로 coverage를 주장하지 않는다.
- configured model/depth와 `observed: unavailable`을 분리한다. 동등성·benchmark·대체 주장을 하지 않는다.
- 사용자 2차 키를 추정하거나 대행하지 않는다. 자·게이트·generator·정본·원장·기존 판정문을 수정하지 않는다.
- `fork_turns=none`은 context inheritance 차단 설정으로만 기록하고 host-authenticated independence 증명으로
  과장하지 않는다.
- stop: source/hash drift, 배타 출력 충돌, ruler 변경 필요, 필수 쟁점 누락이 생기면 `BLOCKED`로 반환한다.

# 4. 순차 게이트

1. pilot `06_EVIDENCE_REVIEW.md`: Q3~Q5·F10 직접 재현과 스키마 모순 확인.
2. pilot의 파일·해시·coverage·경고 확인 후 `07_GOVERNANCE_CRITIQUE.md` 배치.
3. 두 보고서 검증 후 `08_RULING_RESPONSE_GATE.md` 배치.
4. main-loop는 gate가 허용한 범위만 `CODEX_TEAM_RESPONSE_TO_RULING.md`에 통합한다.

