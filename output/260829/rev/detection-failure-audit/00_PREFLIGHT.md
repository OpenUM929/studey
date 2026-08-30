# Codex 탐지 실패 감사팀 — 사전점검 및 동결

상태: `PILOT READY`  
작성자/소유: Codex/OMX main-loop coordinator  
성격: 비운영·제안 등급. 외부 Claude Code Opus 역할의 승인·대체·동등성 주장이 아니다.

## 1. 사용자 승인 범위와 대표 파일럿

- 목표 책임: Codex/OMX가 Opus 실측 발견 `F1`, `F2-b`, `F3`, `F6`, `F9`를 왜 사전에
  탐지하지 못했는지 설명하고 재발 방지 구조를 제안한다.
- 단위 수: 발견 ID 5개. 파일 13개.
- 포함: 탐지 실패의 직접 원인, 구조적 원인, 발견 시점, 책임/소유 경계, 재발 시나리오,
  검출·예방·결정요청 통제, 단계별 적용 순서, 검증 가능한 증거.
- 제외: 수용기준 선택, EXPECTED_ITEM_IDS 값 결정, 게이트 코드 개정, 정본/원장 변경,
  외부 Opus 역할 판정, 기존 판정 재승인.
- 중지 조건: 자의 타당성/값/코드를 팀이 정해야 하는 지점, 입력 해시 변화, 배타 쓰기 충돌,
  필수 레인 부재, 또는 5개 발견 중 하나의 근거 부재.

이 범위는 사용자가 이 세션에서 제공한 Opus 실측 정보와
`output/260828/rev/260828_01_codex_s2_capability_audit.md`의 발견 식별자를 그대로 소비한다.
팀은 새 수용기준을 만들지 않는다. 최종 실질 평가는 사용자가 전달할 외부 Opus 검토에 남긴다.

## 2. 동결 입력

| path | bytes | sha256 |
|---|---:|---|
| `CLAUDE.md` | 27763 | `36b919c541c093fb70745b557a079f1380ca85748c8014adb3e2b919698c3ef9` |
| `AGENTS.md` | 18946 | `aee11ab55e20817bbb0f2dbb1720bb104f6ad83c0308044d892ba375598b1781` |
| `analysis/REV_GUIDE.md` | 30908 | `b0109e323eabffb5ee275ff49d69100005bf95cbfd8c77ac4c8e1e33a8299e28` |
| `docs/CODEX_TEAM_ASSURANCE_GUIDE.md` | 6152 | `f2fa57e4a038169942691dd995edaadc0266e786e079f699854b1cf16e6a7672` |
| `output/260828/rev/260828_01_codex_s2_capability_audit.md` | 40873 | `b6e40283216327b869c39c179b106ca4470a45526389aef591a76c5a6dbb052e` |
| `analysis/rev/260828_02_system_harness_audit.md` | 15536 | `27c8fac3202b33991d499db88b22518e6d13c4742ff3849d9cca7aa53a196149` |
| `output/260828/diagnostic/math2-method-comparison/codex-team/ACCEPTANCE_SCHEMA_260828.md` | 1530 | `b8edd69949470571e3006d6179f96350ffe58cfbb5beec208bae218817c46642` |
| `output/260828/rev/ACCEPTANCE_SCHEMA_260828.repaired.md` | 3377 | `2a5d8bda46bcb270784560b47d43944886219a08063e9965e6c0105433dd225b` |
| `output/260828/diagnostic/math2-method-comparison/codex-team/EXPECTED_ITEM_IDS_260828.tsv` | 1652 | `db0ff6e06641aba7f213b362b69317f2ce9c06f5cc66083319f12bdf7421cfe4` |
| `output/260828/rev/EXPECTED_ITEM_IDS_260828.regenerated.tsv` | 1613 | `48460b1c168a718a6589d7550abdb9f2449e65494d91249debd0c3cada26cb23` |
| `output/260828/diagnostic/math2-method-comparison/codex-team/check_experiment.py` | 8437 | `325807caff872b5a52f33603eb7ec976d66ce34f80c2c0cb9f3432043ac2eb5f` |
| `output/260828/rev/meta_gate_260828.py` | 10001 | `88ed208b1419cc9451dedc5a765abc378913f02a5fe9c8c1799ca19c888d5bb1` |
| `output/260828/rev/gate_selftest_260828.py` | 10621 | `69e8610df06223f70e7df3a4fabe137575968082a22d2f9f7b55f020a6ba96a9` |

`ACCEPTANCE_SCHEMA_260828.repaired.md`와 재생성 TSV는 승인된 자가 아니라 감사 제안/증거다.
현재 라운드는 둘을 운영 입력으로 승격하지 않는다.

## 3. Staffing matrix

| lane | 목적·persona | unit/count | 입력 경계 | 배타 출력 | lane = model = depth | 예상량 | 동시성 | 검증/stop | instruction |
|---|---|---:|---|---|---|---|---:|---|---|
| author pilot | 5개 발견의 인과 모델·개선 초안 | 5 | §2 전부; 기존 제안은 증거일 뿐 승인 아님 | `01_author_root_cause.md` | `assessment-author-sol = gpt-5.6-sol = high` (planned; 런타임 관측 전) | 1 report, 5 finding rows | 1 | 5 ID exact coverage, file:line evidence, ruler write 0; 실패 시 후속 배치 금지 | `.codex/agents/assessment-author-sol.toml` |
| evidence audit | 주장·해시·라인·명령 독립 검증 | 5 | source-first 후 author | `02_evidence_audit.md` | `assessment-evidence-auditor-sol = gpt-5.6-sol = high` (planned) | 1 report, material claims 전수 | 최대 2(critic와만) | source-first 기록, PASS/FAIL/BLOCKED, 수리 금지 | `.codex/agents/assessment-evidence-auditor-sol.toml` |
| adversarial review | 재발 경로·통제 우회·잘못된 소유 재현 공격 | 5 | source 독립 재계산 후 author/audit | `03_adversarial_review.md` | `assessment-adversarial-critic-sol = gpt-5.6-sol = high` (planned) | 1 report, ≥1 hostile scenario/finding | 최대 2(auditor와만) | severity+disposition, 자 수정 금지 | `.codex/agents/assessment-adversarial-critic-sol.toml` |
| gate/integration | 레인 증거·경계·일관성 통합 | 5 | 3개 레인 산출물 + frozen inputs | `04_GATE.md`, `FINAL_REPORT_FOR_OPUS.md` | `assessment-gatekeeper-sol = gpt-5.6-sol = high` (leader runtime) | 2 reports | 1 | artifact/runtime/coverage/boundary 하나라도 누락 시 BLOCKED | `.codex/agents/assessment-gatekeeper-sol.toml` |

최대 동시성은 2이며, author 파일럿 검증 후에만 auditor와 critic을 배치한다. 공유 append-only 파일은 없다.

## 4. 동결 보고 형식

각 substantive 레인은 다음을 포함한다.

1. 실제 runtime execution identity, 관측 model/depth, 역할 지침 경로, 배타 출력 경로.
2. `F1`, `F2-b`, `F3`, `F6`, `F9` 각각에 대해: 직접 증거, 탐지했어야 할 단계, 놓친 이유,
   개인 실수/도구 결함/프로세스 결함/소유 구조 중 원인 분류, 재발 조건, 권고 통제, 통제 소유자.
3. 사실 / 추론 / 미확정을 분리하고 file:line 또는 재현 명령을 기입한다.
4. 자 관련 권고는 `결정요청`으로만 기록한다. 자 파일이나 정본을 수정하지 않는다.
5. 자신의 결과를 승인하지 않고 다음 레인 또는 외부 Opus 검토에 넘긴다.

로컬 통합은 5개 ID의 누락/중복, 근거 위치, 배타 쓰기, 런타임 증거, 미해결 critical을 검사한다.
이 검사는 외부 Opus 승인이나 자의 타당성 판정이 아니다.

## 5. 파일럿 재개점

`assessment-author-sol` 한 레인만 실행한다. 파일 생성 후 입력 해시, 변경 파일 범위, 5개 ID,
근거 위치, 금지된 자/정본 쓰기 여부를 확인한다. 하나라도 실패하면 `BLOCKED`로 끝내고 다음 레인을
배치하지 않는다.
