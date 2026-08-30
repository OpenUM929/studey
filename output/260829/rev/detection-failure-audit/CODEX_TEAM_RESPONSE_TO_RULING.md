---
title: 260829_01 판정에 대한 Codex 전문 감사팀 의견
created: 260829
author: Codex/OMX main-loop
status: advisory-revise-before-user-key
source: 260829_01_detection_failure_ruling.md, 06_EVIDENCE_REVIEW.md, 07_GOVERNANCE_CRITIQUE.md, 08_RULING_RESPONSE_GATE.md
---

# 1. 결론

**팀의 공통 의견은 `REVISE-BEFORE-USER-KEY`다.**

Opus 판정은 핵심 원인 모델과 F10을 정확히 강화했다. 특히 F6의 16행과 F9의 W-04 44–49를
원천에서 다시 산출하고, 증거 범위도 자의 일부라는 점을 드러낸 것은 중요한 개선이다. 그러나 현재
판정문을 그대로 사용자 2차 키나 BF1~BF7 실행 근거로 쓰기에는 새로 확인된 모순이 남아 있다.

- Q1 일반 원인 모델과 Q6 `documentary-only` 방향은 **guard를 붙여 지지**한다.
- Q2~Q5, Q7과 BF1~BF7은 **문언·스키마·권한 transition을 먼저 개정**해야 한다.
- 따라서 지금은 blanket 승인, 사용자 키 요청, implementer 지정, ruler 수정, refreeze, 재실행을 하지 않는다.

이 결론은 외부 Opus/`rev-arbiter` 판정이 아니라 Codex/OMX의 advisory 의견이다. 팀 레인의 serving
model/depth와 host-authenticated independence는 관측할 수 없었으므로 actual-team assurance도 주장하지 않는다.

# 2. 판정에서 타당한 부분

## 2.1 F6·F9 raw 재현

- `author/types.tsv:2-13`을 의미 단위로 펼치면 재사용 6, 단독 9, blocked 1, 합계 16행과 22문항이
  재현된다. 기존 U10/U11은 스스로 독립 generator를 묶은 bookkeeping row라고 명시한다.
- `transcript.md:44-50`에 heading 44, 본문 끝 48, blank 49, 다음 section heading 50이 있으므로
  heading boundary 규칙을 적용한 W-04 44–49는 재현된다.

## 2.2 F10 방향

원 13파일 목록에는 transcript, `author/types.tsv`, `author/items.tsv`가 없었고, 포함된 expected table과
gate가 이 경로들을 직접 지목했다. 따라서 같은 assurance/control plane이 입력 경계를 정하고 “raw 부재”를
판정한 구조는 실제다. 증거 범위를 ruler 구성요소로 다뤄야 한다는 방향은 맞다.

## 2.3 Q7 telemetry 현실성

configured model/depth와 observed serving telemetry를 구분하고, 관측 불가능한 telemetry 자체를 일반
advisory 작업의 만족 불가능 조건으로 두지 말자는 취지는 타당하다. 다만 이것은 actual-team assurance
기준을 없애는 근거가 아니라 **advisory와 assurance 두 등급을 분리하는 근거**다.

# 3. 사용자 키 전에 반드시 고칠 쟁점

## 3.1 Q5/BF3 — W-04를 고친 규칙이 S-18에서 다시 깨진다 (critical)

판정의 `^#{1,6}\s` + “다음 heading 직전”을 22개 item에 그대로 적용하면:

```text
W-04 = 44-49
S-18 = 138-148
```

그러나 shipped와 regenerated TSV 모두 S-18을 138–146으로 기록한다. 실제 147행은 `---`, 148행은
blank, 149행은 appendix heading이다. 따라서 heading regex 한 줄만으로는 horizontal rule, appendix,
EOF, trailing separator 처리가 닫히지 않는다. Q5의 “21/22가 rule_a”, “마지막 문항은 EOF까지”,
“모든 derivation_rule=rule_a”를 동시에 유지할 수 없다.

**필요 개정:** numeric item-start, section/appendix/horizontal-rule/EOF/fenced-code 규칙, generator의 정확한
경로·해시, S-18 fixture와 전체 22행 diff를 먼저 확정한다.

## 3.2 Q4/BF2/BF4 — 16은 재현되지만 수용기준에서 유일하게 유도되지 않는다 (critical)

현재 자료를 정직하게 재분할하면 16은 맞다. 하지만 제안된 `row_kind`만으로는 같은 generator의 문항을
반드시 최대 통합해야 한다는 규칙이 없다. 같은 두 문항을 singleton 두 개로 나눠도 형식 조건을 통과할
수 있다. 상한을 없앤 뒤 `rows=16`을 pass/fail 기대값으로 넣으면 F6의 count optimization을 exact-count
형태로 다시 만든다.

또한 다음이 미정이다.

- semantic umbrella를 기계 판정할 structured `generator_id`와 generator equivalence/maximality.
- singleton 한 문항에서 “observed variation axes 2개”가 뜻하는 관측 단위.
- exact-cover가 **primary membership에만** 적용되고 secondary types는 비포괄 참조라는 규칙.
- `reuse_ratio=items/rows`에서 blocked item/row 포함 여부. 현재 22/16은 source defect도 지표에 포함한다.

**필요 개정:** 16은 당분간 current-data report로만 두고, 위 의미가 정형화되어 유일한 partition을
도출할 때만 acceptance expected로 승격한다.

## 3.3 Q3/BF1 — warning의 의미와 출력 계약이 서로 충돌한다 (high)

`check_experiment.py:223`의 literal `warnings=0`은 결함이고 계산값으로 바꿔야 한다. 그러나 현재 판정은
warning을 “차단하지 않는 이탈”로 정의하면서 예시 도구는 warning을 integrity defect로 처리해 exit 1을
낸다. 또한 `check_experiment.py`의 PASS marker는 `[OK]`가 아니라 `experiment-gate: PASS`이므로
“[WARN]을 [OK]보다 먼저”라는 BF1은 실제 출력 스키마와 맞지 않는다.

**필요 개정:** warning 정의·수집 지점, tool exit와 composite acceptance 의미, 실제 PASS marker, 출력
순서, warning fixture의 명령·기대 출력·기대 카운트를 먼저 확정한다.

## 3.4 Q2/BF6 — 2-key는 권한 승인이지 구현 검증이 아니다 (critical)

`감사권한자 제안 + 사용자 확인`은 의미·정책 변경을 승인하는 최소 키가 될 수 있다. 그러나 사용자 키가
gate 구현, fixture 적합성, mutation 검출력을 qualification한 것은 아니다. 인력 수를 네 명으로 고정할
필요는 없지만 다음 incompatible function은 분리되어야 한다.

1. semantic authorization — 감사 제안 + 사용자/정규 arbiter 키.
2. candidate implementation — 지정된 non-measured implementer.
3. qualification — implementer와 다른 context/identity가 frozen semantics와 hostile/property fixtures를 검증.
4. refreeze — implementer가 아닌 감사권한자가 old/new full hash와 stale descendants를 기록.
5. consume — 이후 measured lane/gatekeeper는 refrozen ruler를 실행만 함.

현재 `REV_GUIDE §5`에는 ruler/gate candidate implementer의 write surface가 없고, 판정문에도 actor와
§6-c 실행 order가 없다. 그러므로 BF1~BF3를 구현할 권한자는 아직 지정되지 않았다.

## 3.5 F10/BF5 — direct path closure는 필요조건일 뿐 충분조건이 아니다 (high)

“동결 파일이 경로로 지목하는 모든 원천”만으로는 historical path, output/reply path, optional evidence,
순환 참조를 구분하지 못한다. 반대로 문서에 경로 문자열이 없지만 material claim에 필요한 원천은 놓친다.

**필요 개정:** `parent_claim`, `dependency_kind`, `source|derived|ruler|evidence|output`,
`required|optional|blocked`, resolved path/full hash, transitive depth, cycle/missing disposition을 가진 typed
claim-to-evidence closure. CLAUDE 단독 수정이 아니라 AGENTS, REV_GUIDE, agent definitions,
`check_assurance_contract.py`의 동반 갱신·검증도 포함한다.

## 3.6 Q7/BF7 — advisory와 actual-team assurance를 분리해야 한다 (critical)

telemetry unavailable 상태에서도 로컬 advisory 분석은 가능하다. 그러나 그 상태를 actual-team,
independent review, runtime-specific capability, benchmark/comparison 증거로 계상할 수는 없다.
`fork_turns=none`은 dispatch 시 대화 상속을 끄는 설정일 뿐 filesystem 선열람 부재, fresh context,
serving model/depth, control-plane 독립성을 증명하지 않는다.

**필요 개정:**

- advisory: configured 값 + `observed: unavailable`을 명시하고 실행 가능.
- assurance/independence/runtime claim: host evidence가 없으면 FAIL/BLOCKED.

## 3.7 메인 루프 대행의 권한 라벨

판정문은 fresh-context 아비터가 아니라 `REV_GUIDE §5` 메인 루프 대행임을 정확히 고지했다. 같은 절은
대행 산출물을 **제안 등급**으로 제한한다. 따라서 현재 Q3~Q5의 `binding`, Q6의 `approve`, 문서의
`partially-approved`, BF1~BF7의 `구속 수정`은 권한상 proposal disposition으로 정규화해야 한다.
원천 재현은 evidence quality를 높이지만 binding authority를 만들지 않는다.

# 4. Q1~Q7에 대한 Codex 팀 의견

| unit | 팀 의견 | 현재 사용자 키 |
|---|---|---|
| Q1 | **guard부 지지** — 원인 모델+F10 방향은 맞음. “피측정 레인”을 measured assurance/control plane으로 정정하고 BF5와 분리 | 불가(as written) |
| Q2 | **개정 필요** — authorization 2-key와 implementation qualification 분리 | 불가 |
| Q3 | **개정 필요** — warning 의미·marker·exit·fixture 미정 | 불가 |
| Q4 | **개정 필요** — 16 비유일, generator/schema/metric 미정 | 불가 |
| Q5 | **개정 필요** — S-18 반례로 전체 span rule 미완성 | 불가 |
| Q6 | **guard부 지지** — F2-b documentary-only는 타당하나 descendant PASS/ruler authorization 금지 필요 | binding 키 불가 |
| Q7 | **개정 필요** — advisory와 assurance claim gate 분리 | 불가 |

BF1~BF7은 모두 **방향 일부는 타당하지만 implementation-ready가 아니므로 현재 승인하지 않는다.**

# 5. 구현자 선택에 대한 의견

지금 BF1~BF3 구현자를 고르면 안 된다. semantics, actor write surface, qualification/refreeze 순서가 닫히지
않았기 때문이다. 개정 판정 후에는 다음 구성이 가장 현실적이다.

- Codex/OMX를 **non-measured candidate implementer**로 지정할 수 있다.
- 그 경우 Codex/OMX는 같은 라운드의 measured author, qualifier, refreezer, gatekeeper로 계상하지 않는다.
- fresh-context external Opus/권한 레인이 candidate를 raw source와 frozen semantics에서 검증한다.
- 사용자 키와 별도 refreeze가 끝난 뒤에만 새 측정 라운드가 ruler를 소비한다.
- fresh qualification을 제공할 수 없으면 역할을 합치지 말고 `BLOCKED`를 유지한다.

즉 “Codex가 고치면 Codex를 못 쓴다”가 아니라, **그 수정·검증 라운드에서 Codex를 피측정 결과로
평가하지 않는다**는 의미다. 다음 독립 측정 라운드에서 refrozen ruler의 소비자로 복귀할 수 있다.

# 6. 팀 실행 증거와 한계

| lane | artifact | SHA-256 | status |
|---|---|---|---|
| evidence review | `06_EVIDENCE_REVIEW.md` | `09650d1c12b5377d9d0a215138d029642447dd1007e63bfd2e8abe5b603293b2` | shared-context advisory REVISE |
| governance critique | `07_GOVERNANCE_CRITIQUE.md` | `1b88103d63cb5f31317579aa8a3fd50ef8eae7f1d456c432374168d85bbd2411` | separate existing lineage, not host-authenticated; REVISE |
| response gate | `08_RULING_RESPONSE_GATE.md` | `cb466c48c9d265c2837755d3be72bb814634adc68b7a140e8abfa6807bf09c1c` | advisory `REVISE-BEFORE-USER-KEY` |

- dispatch manifest 16/16 bytes·SHA-256 일치.
- Q1~Q7 + BF1~BF7 normalized coverage 14/14; duplicate/missing/extra `[]/[]/[]`.
- pilot C1~C3/H1~H2 5/5 유지.
- serving model/depth 및 host-authenticated independence는 unavailable.
- 정본·원장·ruler·gate·generator·기존 판정문 수정 0, 커밋 0.

# 7. 외부 Opus 재검토 요청안

```text
[CC 회람] 260829_02 — 260829_01 탐지 실패 판정 개정 요청
<target> output/260829/rev/detection-failure-audit/CODEX_TEAM_RESPONSE_TO_RULING.md 및 같은 디렉터리의 06_EVIDENCE_REVIEW.md(18349 bytes, SHA-256 09650d1c12b5377d9d0a215138d029642447dd1007e63bfd2e8abe5b603293b2), 07_GOVERNANCE_CRITIQUE.md(24860 bytes, SHA-256 1b88103d63cb5f31317579aa8a3fd50ef8eae7f1d456c432374168d85bbd2411), 08_RULING_RESPONSE_GATE.md(21851 bytes, SHA-256 cb466c48c9d265c2837755d3be72bb814634adc68b7a140e8abfa6807bf09c1c), 원 판정문 260829_01_detection_failure_ruling.md(16469 bytes, SHA-256 171bc0882a845bd6654e4e555a74f96a4a3bced3eccab76ee3002612d047fbd8) — 대상 5파일, ruling unit 14개(Q1~Q7·BF1~BF7)
<touched> Codex 재검토 라운드 생성 6파일: analysis/wip/mainloop_260829_detection_failure_ruling_review.md, output/260829/rev/detection-failure-audit/05_RULING_REVIEW_PREFLIGHT.md, 06_EVIDENCE_REVIEW.md, 07_GOVERNANCE_CRITIQUE.md, 08_RULING_RESPONSE_GATE.md, CODEX_TEAM_RESPONSE_TO_RULING.md. 정본·REV_LOG·ruler·gate·generator·기존 판정문 무수정, 커밋 없음
<executor> rev-arbiter (external Claude Code Opus, fresh context) — `.claude/agents/rev-arbiter.md:23-38,40-64`에 따라 원천을 직접 재검증하고 Q1~Q7과 BF1~BF7의 revise-required 판정 및 실행 가능 acceptance를 확정; fresh context를 제공할 수 없으면 REV_GUIDE §5 main-loop substitute로 proposal-grade만 작성하고 binding/approve 라벨 금지
<requests> ① Q5 S-18 138-148 대 138-146 반례를 포함한 span 전체 규칙 재판정 ② Q4 exact 16을 report-only로 둘지 generator maximality로 유일화할지 결정 ③ Q3 warning semantics·PASS marker·fixture 확정 ④ Q2/BF6 authorization과 implementation qualification transition 분리 및 authorized implementer/write surface 결정 ⑤ BF5 typed claim-to-evidence closure와 동반 갱신 확정 ⑥ Q7 advisory/actual-team claim gate 분리 ⑦ 대행 판정의 binding/approve 라벨을 proposal-grade로 정정 — 각 unit에 approve|revise-required|reject, evidence, note, runnable gate를 기입
<reply> output/260829/rev/detection-failure-audit/260829_02_detection_failure_ruling_revised.md 작성 + analysis/wip/rev-arbiter_260829_detection_failure_revision.md checkpoint + 허용된 analysis/REV_LOG.md 1행; 판정이 단계를 풀 때만 REV_GUIDE §6-c 형식의 [OC 지시]를 함께 반환
<constraints> external-single-session 1회, pilot slice 1개, subagent/background/parallel/auto-retry 금지; 5 target 파일과 raw transcript/types/items/expected TSV/gate code를 직접 열어 verify-don't-trust; serving model/depth 또는 fresh context가 증명되지 않으면 그대로 고지; user key 추정 금지; existing ruling·Codex reports·ruler·gate·generator·canonical 수정 금지; write surface는 revised ruling+own WIP+REV_LOG 1행뿐; no commit; benchmark/comparison/release 금지; S-18·exact-16·warning·typed-closure 쟁점 중 하나라도 미결이면 revise-required 유지
```

# 8. 비승인 선언

이 문서는 current ruling을 승인하거나 사용자 2차 키를 대행하지 않는다. BF1~BF7 구현, ruler 선택·변경,
qualification/refreeze, external approval, actual-team assurance, benchmark/comparison, release를 허가하지 않는다.

Pipeline: detection-failure audit → Opus substitute ruling → evidence pilot → governance critique → **advisory response gate(REVISE-BEFORE-USER-KEY)** → fresh-context ruling revision
Stage: Codex/OMX = configured gpt-5.6-sol/high, observed unavailable — Q/BF 14/14과 pilot 5/5 검토; Q5 S-18·Q4 비유일 count/schema·Q2 qualification·Q7 claim gate가 active blocker
Team: mode=actual-team; lead=coordinator | configured gpt-5.6-sol/high | ruling-response integrator | completed advisory; lanes=evidence auditor = configured gpt-5.6-sol = observed unavailable | shared-context reviewer | completed REVISE | `.codex/agents/assessment-evidence-auditor-sol.toml`; adversarial critic = configured gpt-5.6-sol = observed unavailable | existing separate lineage critic | completed REVISE | `.codex/agents/assessment-adversarial-critic-sol.toml`; gatekeeper = configured gpt-5.6-sol = observed unavailable | advisory gatekeeper | completed REVISE | `.codex/agents/assessment-gatekeeper-sol.toml`; independence=not host-authenticated; planned/unavailable/failed lanes=verified actual-team assurance unavailable, external fresh-context arbiter not run
Next: current ruling에 사용자 키나 BF 실행을 붙이지 않는다. 위 [CC 회람]으로 fresh-context revision을 받아 14개 unit과 runnable gate를 재검증하며, 한 쟁점이라도 미결이면 HOLD/REVISE를 유지한다.

