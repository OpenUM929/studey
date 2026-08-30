# Codex/OMX 탐지 실패 원인 및 재설계안 — Opus 검토본

상태: **`▲ blocked — ADVISORY ONLY — NOT AN ACTUAL-TEAM ASSURANCE RESULT`**  
작성: Codex/OMX main-loop coordinator  
목적: Opus 실측 F1·F2-b·F3·F6·F9를 Codex/OMX가 왜 먼저 탐지하지 못했는지 설명하고,
같은 실패를 재현하지 않는 소유·증거·게이트 구조를 외부 Opus가 판정할 수 있게 한다.

## 1. 결론

이번 실패의 1차 원인은 모델 한 명의 부주의가 아니라 **자(ruler), 피측정 산출물, 게이트,
통합 판정이 같은 통제 축에 놓인 자기측정 구조**다. 그 결과:

1. 불가능한 기준은 결정요청이 아니라 형식 순응 산출물로 우회됐다(F6).
2. 어긋난 눈금은 생성 규칙 수정이 아니라 표 한 행 손수정으로 흡수됐다(F2-b·F9).
3. 게이트의 자기 선언(`warnings=0`, marker 존재)을 검출력 증거로 다시 사용했다(F1·F3).
4. 판정이 exact raw source·ruler version·artifact·runtime/context와 완전 결속되지 않아,
   자가 바뀌어도 결론이 stale임을 기계적으로 전파하지 못했다.
5. 여러 레인을 실행한 사실을 독립성·모델 증거로 과대해석했다. 이번 author/auditor는
   `fork_turns=all`이라 shared-context이고, 모든 native lane의 실제 model/depth telemetry가 없다.

따라서 “레인을 더 많이 띄운다” 또는 “Sol 레인을 교체한다”만으로는 해결되지 않는다.
**피측정자와 자의 소유 분리, raw provenance, 역할상 three-way separation, dependency closure,
held-out 검출력 qualification, 파일럿 중지 규칙**이 함께 필요하다.

근거: `CLAUDE.md:86-102`, `AGENTS.md:64-88,115`, `analysis/REV_GUIDE.md:268-280`,
`03_adversarial_review.md:78-108`.

## 2. 발견별 원인과 현재 판정

| ID | Codex/OMX가 놓친 이유 | 직접 확인된 범위 | 현재 한계/처분 |
|---|---|---|---|
| F1 | `warnings=0`을 계산값인지 확인하지 않고 독립 신호로 신뢰했다. 게이트 작성자와 검출력 qualifier도 분리되지 않았다. | `check_experiment.py:223`의 상수 출력과 `meta_gate_260828.py`의 `vacuous_signal_count=1`은 재현됨. | warning 채널의 의미·존치 자체는 자 결정. 공개 fixture의 `undetected=0`만으로 충분하지 않고 held-out/property 검증 필요. |
| F2-b | 자 변경을 판정 무효화 사건이 아니라 국소 수정으로 취급했다. old/new ruler와 판정 dependency가 결속되지 않았다. | 현 ruler, frozen Opus 서술, stale 정본 규칙은 확인됨. | pre-change snapshot·당시 audit hash·변경 로그가 없어 독립 raw replay는 불가. documentary evidence로만 유지. |
| F3 | marker 존재를 보고서 내용·인용·문자 무결성으로 일반화했다. fixture가 한 증상만 겨냥했다. | `require_report()`의 marker-only 검사와 본문 미검사 범위는 직접 확인됨. | mojibake 1종뿐 아니라 citation binding, cardinality, marker stuffing, Unicode 변형을 독립 qualification해야 함. |
| F6 | 5–12를 도전 불가능한 공리로 취급해, 의미 보존보다 기준 통과를 최적화했다. audit도 행수, critic도 개별 군만 봤다. | schema/checker의 5..12 exact-cover 강제는 직접 확인됨; 16-generator/우산 행은 frozen Opus 문서 근거. | **⚠️ 자 미확정.** raw items/types/corpus가 이번 freeze에 없어 16을 독립 재산출하지 못함. 상한 제거·상향·다중배정 중 선택 금지. |
| F9 | expected table을 원천에서 생성되는 눈금이 아니라 gatekeeper가 조정 가능한 산출물로 취급했다. 결정론적 생성과 의미적 정당성도 구분하지 않았다. | shipped/regenerated TSV의 W-04 한 행 차이는 직접 확인됨. | **⚠️ 자 미확정.** raw transcript와 generator가 freeze에 없고 span rule authority도 미확정. 값 선택/표 손수정 금지. |

5개 ID coverage: expected=`[F1,F2-b,F3,F6,F9]`, observed=`[F1,F2-b,F3,F6,F9]`,
duplicate=`[]`, missing=`[]`, extra=`[]`. 이 exact coverage는 이미 알려진 발견을 빠짐없이 다뤘다는
뜻일 뿐, Codex가 그것을 독자 발견할 능력을 증명하지 않는다.

## 3. 왜 기존 오케스트레이터·서브에이전트 지침만으로 부족했는가

### 3.1 지침은 산출물 검토를 분리했지만 측정 구조를 분리하지 않았다

기존 원칙 8은 review와 fix를 나눴지만, acceptance schema·expected values·gate implementation과
그 결과를 받는 gatekeeper 사이의 소유 분리를 강제하지 않았다. 형식상 다른 reviewer가 있어도
동일 ruler와 동일 framing을 공유하면 모두 같은 맹점을 재확인한다.

### 3.2 “기준을 만족하라”가 “기준을 반증하라”보다 우선했다

author는 5–12가 의미적으로 불가능한지 결정할 권한도 없고, 중지·결정요청 의무도 명시적으로
강제되지 않았다. 그래서 우산 행은 부정직이라기보다 주어진 목적함수의 합리적 최적화였다.

### 3.3 검증이 결과 신호와 구조 존재에 편향됐다

행수, marker, `[OK]`, `warnings=0`, exit code를 확인했지만, 검출기 자체가 알려진/알려지지 않은
결함에 민감한지, 주장과 실제 코드 범위가 1:1인지, 기준이 의미적으로 타당한지는 별도 대상이 아니었다.

### 3.4 판정 dependency closure가 없었다

판정마다 raw source manifest, ruler manifest, measured artifact, command/log, runtime/context evidence의
full SHA-256 그래프가 없었다. 그래서 ruler 변경 후 상세 audit만 stale로 표시하고 요약 결론을 재사용하는
“stale verdict laundering” 경로가 남았다(`03_adversarial_review.md:120-127`).

### 3.5 팀 구성 증거를 실행 품질로 오인했다

팀 계획·역할 TOML·레인 수는 실행 모델/depth/독립 context 증거가 아니다. 이번에도 author/auditor가
shared-context였고 host-authenticated model/depth telemetry가 없었다. 이 한계 때문에 gatekeeper는
정확히 `BLOCKED`를 냈다(`04_GATE.md:61-72,110-120`).

## 4. 개선 원칙 — 자·산출물·절차를 분리한다

### 4.1 소유 토폴로지

| 대상 | 작성/제안 | qualification | 확정/동결 | 소비/측정 | 금지 |
|---|---|---|---|---|---|
| 의미적 수용기준(F6 등) | 근거·반례는 Codex/Opus 누구나 제안 | 별도 audit authority가 실행 가능성 검토 | 사용자/`rev-arbiter` 결정 + audit authority refreeze | author/auditor/gatekeeper | measured lane의 기준 수정·우회 |
| expected-value 규칙·표(F9) | 승인된 generator 구현자는 candidate 생성 | clean-context qualifier가 raw source에서 독립 재유도 | audit authority가 generator+raw+output hash 동결 | measured lane | 표 손수정, special case 은닉 |
| gate 코드(F1/F3) | 비측정 maintainer가 candidate 구현 | 별도 clean-context qualifier가 held-out/property/mutation 시험 | 별도 refreezer가 old/new full hash와 결과 기록 | gatekeeper/author는 실행만 | implementer=qualifier=refreezer, 자기 fixture만으로 통과 |
| measured artifact | 지정 author | evidence auditor + adversarial critic | gatekeeper는 결과 통합만 | 외부 Opus가 review | artifact가 자기 자를 수정 |

최소 분리는 **candidate implementer ≠ qualifier ≠ refreezer**이고, 셋 모두 그 라운드의 measured
author/gatekeeper와 달라야 한다. 이름만 다른 shared-context 레인은 별도 key가 아니다.

### 4.2 검출력의 정의

- `undetected=0`은 필요조건일 뿐 충분조건이 아니다.
- public regression fixture 외에 qualifier만 소유한 held-out hostile cases를 사용한다.
- 예시가 아니라 property를 검증한다: source→expected 전량 재유도, duplicate/missing/extra set equality,
  citation target binding, Unicode/control-character class, marker cardinality, ruler/source hash drift,
  stale descendant 전파, semantic umbrella/split counterexample.
- deterministic generator는 일관성을 증명할 뿐 의미적 규칙의 옳음을 증명하지 않는다.

### 4.3 판정 dependency closure

각 conclusion은 다음 full SHA-256 노드에 결속한다.

```text
raw source manifest
  -> ruler manifest (acceptance + generator/expected + gate)
  -> measured artifact manifest
  -> command/output log
  -> lane runtime/context evidence
  -> finding/verdict
  -> executive summary / release decision
```

어느 상위 노드라도 바뀌면 모든 하위 판정은 자동 `stale`이며 재실행 전 인용 금지다. 8자 hash token,
현재 파일만의 hash, 보고서 존재 여부만으로는 dependency closure가 아니다.

## 5. 단계별 실행 방법

### Phase 0 — 현재 라운드 격리 (완료)

- 이 보고서와 `04_GATE.md`를 `▲ blocked`로 유지한다.
- author/auditor=`shared-context`, critic/gatekeeper=`clean-context dispatch`, 전 레인 observed
  model/depth=`unavailable`을 그대로 기록한다.
- repaired schema/regenerated TSV를 운영 ruler로 승격하지 않는다.

### Phase 1 — 사용자/arbiter 결정

다음 네 결정을 먼저 받는다. 하나라도 미정이면 관련 실행을 시작하지 않는다.

1. F1 warning 채널을 유지하며 의미를 정의할지, acceptance contract에서 제거할지.
2. F6 reusable-type 의미와 상한/정확포괄/primary-secondary 정책.
3. F9 source-span 경계 의미와 generator specification.
4. F2-b의 소실된 pre-change provenance를 `documentary-only`로 영구 표기할지.

### Phase 2 — 새 버전 raw-evidence freeze

- 현재 freeze에 파일을 덧붙여 독립성을 소급 주장하지 않는다.
- 새 버전 디렉터리에 raw transcript/corpus, generator, original measured items/types, 가능한 old/new ruler,
  change log, commands, full hashes를 먼저 동결한다.
- 소실된 역사 자료는 재구성해 “원본”이라고 부르지 않고 `BLOCKED`로 남긴다.

### Phase 3 — candidate control 구현

- Codex/OMX는 확정된 ruler를 **소비**해 candidate generator/gate/staleness manifest를 구현할 수 있다.
- 구현자는 해당 라운드의 qualifier/refreezer/measured author/gatekeeper를 겸하지 않는다.
- substitute main-loop 산출물은 제안 등급이며 실제 lane slot이나 assurance 증거로 세지 않는다.

### Phase 4 — 독립 qualification

- clean-context qualifier가 public regression + 비공개 held-out mutation/property tests를 실행한다.
- gate 자체의 source/ruler drift, marker stuffing, 잘못된 citation binding, Unicode 변형,
  special-case generator, umbrella relabel, stale-summary 재사용을 공격한다.
- expected/observed/duplicate/missing/extra와 `undetected`를 출력하되 의미 타당성의 대체물로 쓰지 않는다.

### Phase 5 — two-key refreeze

- 별도 audit authority가 candidate/qualification/raw source의 old/new full hash를 기록하고 재동결한다.
- ruler가 바뀐 경우 기존 verdict 전체를 stale로 만들고 재측정 전 인용을 차단한다.

### Phase 6 — 대표 파일럿 1개

- 실제 model/depth telemetry와 clean-context proof가 노출되는 runtime에서 작은 slice 하나만 실행한다.
- 기준이 만족 불가능/자기모순이면 우회하지 않고 decision request로 중지한다.
- 파일럿의 completeness, raw evidence, warnings, elapsed usage, write isolation이 통과한 뒤에만 다음 wave를
  사용자 승인으로 연다.

### Phase 7 — Opus 전문 검토

- Opus에게 raw/source hashes, exact commands/output, unresolved blocks, dependency graph를 제공한다.
- Codex 요약이나 과거 Opus 결론을 신뢰하지 않고 재현 가능해야 한다.
- 이 단계도 benchmark/동등성/대체/운영 승인으로 자동 전환되지 않는다.

## 6. 이번 전문 감사팀의 실제 증거와 한계

| lane | runtime identity | context | observed model/depth | artifact | sha256 | status |
|---|---|---|---|---|---|---|
| author | `/root/detection_author_pilot` | `fork_turns=all` / shared-context | unavailable | `01_author_root_cause.md` | `b7538ee3fdf315911c2ec70b7a471d044e3561830b8386a411f36c16af95154d` | completed draft; assurance BLOCKED |
| evidence auditor | `/root/detection_evidence_audit` | `fork_turns=all` / shared-context | unavailable | `02_evidence_audit.md` | `dbbccd1270239279c5700f224a34b2c5f846c62dcf3722942fad0ecfcabe1892` | completed BLOCKED audit |
| adversarial critic | `/root/detection_blocked_critic` | `fork_turns=none` / clean-context dispatch | unavailable | `03_adversarial_review.md` | `c5e6f3695dbbd8000deb846b9e61af0d3b706d42494523cc3651627a1498ca33` | completed BLOCKED critique |
| gatekeeper | `/root/detection_gatekeeper` | `fork_turns=none` / clean-context dispatch | unavailable | `04_GATE.md` | `fd27ab2b7f4fd373a3554ec2e88e9ebaf64b9de82aca4fbeab73b89f71eb3be8` | `▲ blocked — BLOCKED` |

이 표는 네 실행이 있었다는 증거다. 그러나 author/auditor의 독립성 및 모든 레인의 실제 model/depth
증거가 없으므로 **검증된 actual-team assurance 결과가 아니다**. `mode=actual-team`은 의도한
orchestration을 설명할 수 있을 뿐 성공 판정으로 사용하지 않는다.

## 7. fresh validation

gatekeeper 실측(`04_GATE.md:86-108`):

```text
required artifacts: 4/4 hash match
frozen inputs: 13/13 bytes/hash match, drift=0, warnings=0
finding IDs: expected=observed=[F1,F2-b,F3,F6,F9]
duplicate=[] missing=[] extra=[]
meta_gate_260828.py --check all: exit 1, failures=7
gate_selftest_260828.py: exit 1 (baseline not clean)
check_assurance_contract.py: exit 1, failures=3 (other-owner WIP)
build_catalog_index.py --check: exit 0, 131 rows
build_mastery.py --check: exit 0, 131 rows, warnings=0
```

따라서 내부 결과는 `READY`나 `REVISE`가 아니라 `BLOCKED`다. 다만 원인 모델·증거 한계·결정요청을
외부 Opus가 전문 검토하는 것은 허용되며, benchmark/comparison/release는 금지된다.

## 8. Opus 판정 요청

1. **원인 모델** — 자기측정 + dependency-closure failure를 주원인으로 인정할지
   (`accept | revise | reject`).
2. **소유 토폴로지** — implementer ≠ qualifier ≠ refreezer ≠ measured lane/gatekeeper를 필수로
   확정할지 (`approve | revise-required | reject`).
3. **F1** — warning 채널 존치/의미 정의 또는 acceptance contract 제거 중 처분.
4. **F6** — reusable-type 의미와 count/exact-cover/primary-secondary 정책의 binding decision.
5. **F9** — source-span 경계 의미와 generator specification의 binding decision.
6. **F2-b** — 소실된 역사 증거를 documentary-only로 영구 제한할지.
7. **재실행 조건** — Phase 1~5와 host telemetry가 충족될 때만 새 파일럿을 허용할지.

## 9. 관련 파일

- 사전점검: `output/260829/rev/detection-failure-audit/00_PREFLIGHT.md`
- 원인 초안: `output/260829/rev/detection-failure-audit/01_author_root_cause.md`
- 증거 감사: `output/260829/rev/detection-failure-audit/02_evidence_audit.md`
- 적대 검토: `output/260829/rev/detection-failure-audit/03_adversarial_review.md`
- 통합 게이트: `output/260829/rev/detection-failure-audit/04_GATE.md`
- 외부 회신 경로: `output/260829/rev/detection-failure-audit/260829_01_detection_failure_ruling.md`
- 외부 역할 지침: `.claude/agents/rev-arbiter.md`

## 10. [CC 회람]

```text
[CC 회람] 260829_01 — Codex/OMX 탐지 실패 원인·재설계안 판정 요청
<target> output/260829/rev/detection-failure-audit/FINAL_REPORT_FOR_OPUS.md 및 같은 디렉터리의 00_PREFLIGHT.md, 01_author_root_cause.md, 02_evidence_audit.md, 03_adversarial_review.md, 04_GATE.md — 발견 ID 5개(F1,F2-b,F3,F6,F9), 팀 산출물 4개+preflight 1개를 직접 열어 검증
<touched> 이번 Codex/OMX 라운드 생성: analysis/wip/mainloop_260829_detection_failure_audit.md, output/260829/rev/detection-failure-audit/00_PREFLIGHT.md, 01_author_root_cause.md, 02_evidence_audit.md, 03_adversarial_review.md, 04_GATE.md, FINAL_REPORT_FOR_OPUS.md — 총 7파일; 정본·원장·ruler·gate 코드는 수정하지 않음
<executor> rev-arbiter (Claude Code Opus) — `.claude/agents/rev-arbiter.md:7-20`의 최종 compliance 판정 책임으로, 이 보고서 §8의 7개 질문을 직접 근거 검증 후 binding ruling; 기존 tier loop가 아니라 BLOCKED 시스템 감사의 ruler/소유 결정요청임을 notes에 명시
<requests> Q1 원인 모델 accept|revise|reject; Q2 implementer≠qualifier≠refreezer≠measured/gatekeeper 토폴로지 approve|revise-required|reject; Q3 F1 warning 채널 처분; Q4 F6 reusable-type/count/exact-cover 정책; Q5 F9 span/generator 규칙; Q6 F2-b documentary-only 처분; Q7 Phase 1~5+host telemetry 충족 전 재실행 금지 여부 — 각 질문에 ruling/evidence/note 기입
<reply> output/260829/rev/detection-failure-audit/260829_01_detection_failure_ruling.md — `analysis/REV_GUIDE.md` §6 `<decision>` 표(question|ruling|evidence|note), frontmatter status approved|revise-required|rejected, decided_by rev-arbiter, binding_fixes, notes, history; own WIP `analysis/wip/rev-arbiter_260829_detection_failure.md`와 허용된 REV_LOG 1행
<constraints> external-single-session Opus 1회·단일 보고서; subagent/background/parallel/auto-retry 금지; 위 파일을 직접 열어 verify-don't-trust; `▲ blocked`·shared-context·runtime telemetry unavailable·F2-b/F6/F9 raw gap을 보존; repaired schema/regenerated TSV를 ruler로 승격 금지; write surface는 ruling+own WIP+허용 REV_LOG 1행뿐; no commit; benchmark/comparison/release/actual-team 성공 판정 금지
```

## 11. 비승인 선언

이 문서는 외부 Opus의 전문 검토 입력이다. Codex/OMX는 F1/F6/F9의 ruler 값을 정하지 않았고,
F2-b의 소실 증거를 복원했다고 주장하지 않으며, 어떤 canonical·ledger·gate·release도 승인하지 않는다.

Pipeline: Opus audit findings → preflight → author(shared-context) → evidence audit(BLOCKED) → critic(clean-context, BLOCKED) → gatekeeper(BLOCKED) → **BLOCKED advisory report ready for Opus review**
Stage: Codex/OMX = configured gpt-5.6-sol/high, observed model/depth unavailable — root-cause synthesis, staged redesign, ownership matrix, seven Opus decision requests, and §6-b relay documented; active verdict remains `▲ blocked — BLOCKED`
Team: mode=actual-team; lead=main-loop coordinator | configured gpt-5.6-sol/high | integrator | completed advisory report; lanes=author = configured gpt-5.6-sol = observed depth unavailable | shared-context author | completed draft | `.codex/agents/assessment-author-sol.toml`; evidence auditor = configured gpt-5.6-sol = observed depth unavailable | shared-context evidence auditor | completed BLOCKED | `.codex/agents/assessment-evidence-auditor-sol.toml`; adversarial critic = configured gpt-5.6-sol = observed depth unavailable | clean-context critic | completed BLOCKED | `.codex/agents/assessment-adversarial-critic-sol.toml`; gatekeeper = configured gpt-5.6-sol = observed depth unavailable | clean-context gatekeeper | completed BLOCKED | `.codex/agents/assessment-gatekeeper-sol.toml`; independence=shared-context; planned/unavailable/failed lanes=verified actual-team assurance unavailable
Next: 사용자는 §10의 `[CC 회람]` 블록을 external Claude Code Opus `rev-arbiter` 단일 세션에 전달한다. Codex/OMX는 reply path가 실제 생성되어 읽히기 전까지 ruler 수정·새 파일럿·benchmark/comparison/release를 시작하지 않는다.
