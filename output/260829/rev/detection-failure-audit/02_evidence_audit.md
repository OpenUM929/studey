# Codex/OMX 탐지 실패 독립 증거 감사 — evidence-auditor lane

상태: `BLOCKED — ADVISORY EVIDENCE AUDIT, NOT APPROVED`  
대상 author: `output/260829/rev/detection-failure-audit/01_author_root_cause.md`  
대상 SHA-256: `b7538ee3fdf315911c2ec70b7a471d044e3561830b8386a411f36c16af95154d` (재계산 일치)

## 1. 실행 정체성·경계

- native execution identity: `/root/detection_evidence_audit` (협업 런타임이 노출한 canonical task identity).
- observed model/depth: **unavailable**. 역할 파일 `.codex/agents/assessment-evidence-auditor-sol.toml:1-4`에는 `gpt-5.6-sol / high`가 설정되어 있으나, 현재 child surface는 실제 실행 모델·depth telemetry를 별도로 노출하지 않는다. 설정값을 관측 증거로 승격하지 않는다.
- 역할 지침: `.codex/agents/assessment-evidence-auditor-sol.toml`.
- 배타 출력: `output/260829/rev/detection-failure-audit/02_evidence_audit.md` 한 파일.
- 금지 경계 준수: author 초안, 정본, 원장, WIP, 수용기준, expected-ID 표, gate code를 수정하지 않았고 child/external agent를 배치하지 않았다.
- assurance 영향: 관측 model/depth 부재는 `AGENTS.md:60,82`와 `docs/CODEX_TEAM_ASSURANCE_GUIDE.md:16`상 `actual-team` 실행 증거의 **명시적 blocker**다.

## 2. source-first 순서와 동결 검증

실제 읽기·검증 순서는 다음과 같다.

1. 역할 지침과 `00_PREFLIGHT.md`를 읽었다.
2. **author 초안을 열기 전에** preflight의 동결 파일 13개를 `Get-Item`과 `Get-FileHash -Algorithm SHA256`으로 재계산했다.
3. 13/13의 bytes와 SHA-256이 preflight와 정확히 일치한 뒤, 정본(`CLAUDE.md`, `AGENTS.md`, `REV_GUIDE`, assurance guide), Opus 감사 2종, 현행/제안 schema·expected 표, 현행 gate와 meta/self-test를 읽었다.
4. 현행 gate의 코드 경로를 정적 확인하고 meta gate/self-test를 비파괴 재실행했으며, 두 expected TSV를 ID·핵심 범위 기준으로 비교했다.
5. 그 후에만 author 파일의 SHA-256을 재계산하고 본문을 처음 읽었다.

동결 결과: **13/13 PASS**, missing `[]`, byte mismatch `[]`, hash mismatch `[]`.

source-first 결론은 다음과 같았다.

- F1·F3는 현행 gate source만으로 완전 재현된다.
- F2-b의 현재 W-04 `44-48`과 stale 무효화 규칙은 확인되지만, 변경 전 `44-51` raw snapshot과 audit 재실행 부재를 직접 재현할 버전 아티팩트는 동결 13종에 없다.
- F6의 `5..12 + exclusive exact cover` 강제는 확인되지만, 최소 16 generator와 U10/U11의 원본 type 산출물은 동결 13종에 없다.
- F9는 shipped W-04 `44-48` 대 regenerated `44-49`의 단일 핵심 범위 차이를 직접 확인했다. 다만 source transcript와 generator source가 동결 13종에 없어 21/22 rule-a와 수동 수정의 역사 전체는 raw 재유도할 수 없다.

## 3. 발견 ID exact coverage 및 finding별 판정

expected identifiers: `[F1, F2-b, F3, F6, F9]`  
observed author main-table identifiers: `[F1, F2-b, F3, F6, F9]`  
duplicate: `[]` · missing: `[]` · extra: `[]` · exact count: `5`

| ID | 판정 | 독립 재현 증거 | author 주장 판정 | 남은 증거 공백 |
|---|---|---|---|---|
| F1 | **PASS** | `check_experiment.py:223`은 실제로 `print(f"warnings=0")`; `meta_gate_260828.py:136-151` 정적 검사도 `vacuous_signal_count=1`을 재현했다. 현 실행은 `failures=7`이어도 meta gate의 계산된 warnings는 0이며, 구 gate의 warning 신호는 코드상 상수다. | 증상, 탐지 시점, 도구/검토/소유 분류, `undetected=0` 통제 방향 모두 근거와 합치한다. | 과거 clean baseline에서 11 fixture를 모두 실행한 결과는 현재 트리에서 재실행 불가(현재 baseline 자체가 5 failure). 다만 상수 결함 자체에는 영향 없음. |
| F2-b | **BLOCKED** | 현재 shipped expected의 W-04가 `44-48`인 것은 직접 확인했다. frozen Opus 감사 `260828_01...:162-179`는 `44-51 → 44-48`, audit 미재실행, stale 판정을 기록하며, 현 정본은 자 변경 시 전 판정 stale을 요구한다(`CLAUDE.md:98-99`; `REV_GUIDE.md:276-280`). | author는 frozen 감사의 역사 서술과 현재 소유 규칙을 충실히 옮겼다(**documentary PASS**). | 변경 전 expected snapshot, 당시 audit artifact/hash, 변경 행위 로그가 동결 입력에 없어 시간 순서를 독립 raw 재현할 수 없다. 이 부분을 완전 실측 PASS로 승격하면 안 된다. |
| F3 | **PASS** | `require_report()`(`check_experiment.py:168-188`)는 marker 존재만 검사한다. 문자/제어문자 검사는 item/type TSV 경로(`:91-126,137-159`)에만 있다. `meta_gate --check all`이 coverage failure를 재현했다. | 증상, 코드 범위, 과장된 capability claim, report mutation 필요성 모두 정확하다. | 현재 self-test는 dirty baseline 때문에 report fixture까지 진행하지 못했으므로 이번 라운드의 동적 증명은 BLOCKED이나 정적 코드 증명은 완전하다. |
| F6 | **BLOCKED** | 원 schema `:8`과 checker `:143-165`가 5..12 및 exclusive exact cover를 강제하는 것은 직접 확인했다. frozen Opus 감사 `:201-215`는 최소 16 generator와 U10/U11 우회 행을 구체적으로 기록한다. repaired schema는 상한 제거·우산 행 금지를 제안하지만 스스로 제안본임을 밝힌다(`repaired.md:3-5,12-17`). | author는 `⚠️ 자 미확정`, 선택 금지, decision request, repaired 문서의 proposal 지위를 정확히 유지했다(**documentary PASS**). | 16-generator 계산의 원본 `types.tsv/items.tsv`가 동결 13종에 없으므로 의미 보존 불가능성을 raw 행 단위로 재검산할 수 없다. |
| F9 | **BLOCKED** | 두 TSV 모두 22 unique ID를 가지며 핵심 범위 열은 W-04만 `44-48` 대 `44-49`로 다르다. frozen Opus 감사 `:440-461`은 rule-a diff 1, rule-b diff 20과 수동 출력 수정 경로를 기록한다. | author는 final W-04 값/규칙을 선택하지 않고 generator 재유도+감사 동결+two-key를 요구하여 경계를 지켰다(**documentary PASS**). | source transcript와 generator code가 동결 입력에 없으므로 21/22 규칙 일치와 수동 편집 역사를 이번 lane이 독립 재실행하지 못했다. regenerated TSV 자체는 승인된 눈금이 아니다. |

행수만으로 통과시키지 않았다. 각 PASS/BLOCKED는 코드 경로, 해시, ID 집합 또는 정확한 row diff에 결부했다.

## 4. material claim audit

### 4.1 PASS

1. **핵심 인과 모델** — 같은 소유 축이 measured artifact와 ruler와 gate 통합을 닫힌 회로로 만들었다는 설명은 `260828_01...:152-179,201-215,556-578` 및 `CLAUDE.md:86-102`와 합치한다.
2. **F1/F3 코드 인용** — author `:28,30,159-160`의 line range는 실제 함수 범위와 일치한다.
3. **F6/F9의 결정권 유보** — author `:31-32,83,172-173`은 repaired schema와 regenerated TSV를 운영 자로 승격하지 않고 `⚠️ 자 미확정`으로 남겼다.
4. **사실/추론/미확정 분리** — author `§6`은 관측 사실, 구조적 추론, 결정요청을 명시적으로 분리한다. 개인의 고의·심리를 단정하지 않는다.
5. **단계적 방법** — freeze → ruler qualification → representative pilot → source-first audit → critic → gate → external Opus의 순서는 `AGENTS.md:64-84`와 `docs/CODEX_TEAM_ASSURANCE_GUIDE.md:31-39`에 부합한다.
6. **외부 권한 비대체** — author `:3-6,193-195`는 advisory/no-approval을 일관되게 유지한다.
7. **source-first 역할 설명** — 시스템 감사 `analysis/rev/260828_02_system_harness_audit.md:119-149`의 실제 요지는 팬아웃 수보다 상대 산출물 후열람과 맹목 재유도 순서가 중요하다는 것이며 author `:57-65`는 이를 과도하게 뒤집지 않는다.

### 4.2 FAIL/BLOCKED

1. **BLOCKED — 실제 model/depth telemetry 없음.** author도 `:10-11,174`에서 인정한다. 따라서 author progress map `:199`의 `mode=actual-team`은 투명한 미관측 표시는 했지만, assurance 계약상 아직 검증 가능한 actual-team 증거가 아니다. 최종 팀/외부 비교 상태로 승격할 수 없다.
2. **BLOCKED — 역사적 raw evidence 3종 미동결.** F2-b pre-change ruler/audit hash, F6 원본 group rows, F9 source+generator가 없어 이 auditor는 해당 발견의 역사·의미 계산을 frozen audit 문서 밖에서 독립 재현하지 못했다. author가 Opus 감사의 내용을 정확히 인용했다는 것과 독립 실측 완료는 구별해야 한다.
3. **경계 위험 — F1/F3 통제의 구현자와 qualifier 분리가 완전히 이름 붙지 않았다.** author `:28,30`은 감사권한자를 통제 소유자로 쓰고 `:85-93`은 감사권한자가 gate/self-test를 동결한다고 한다. measured lane 수정 금지는 명확하지만, gate/self-test를 **누가 개정하고 누가 독립 qualification하는지**는 별도 두 주체로 고정되지 않았다. `:93`의 “감사측 내부 재검토”가 같은 lane의 자기 gate 자기 개정으로 해석되면 F2-b를 한 층 위에서 재현한다. 이는 운영 적용 전 critic이 hostile scenario로 공격해야 할 **미해결 boundary ambiguity**다.
4. **경계 위험 — repaired proposal 자체의 stale 문구.** author는 repaired schema를 승인본으로 승격하지 않았으므로 author의 처분은 PASS다. 그러나 frozen `ACCEPTANCE_SCHEMA_260828.repaired.md:4`에는 “승인 시 gatekeeper가 원본에 반영”이 남아 있어 현재 `CLAUDE.md:86-102`, `AGENTS.md:115`, `REV_GUIDE.md:276-280`의 ruler write 금지와 충돌한다. 이 파일 전체를 실행 지침으로 소비하면 안 되며, 인용 가능한 것은 proposal evidence뿐이다.
5. **재현 경고 — self-test 현재 실행은 과거 감사 로그와 상태가 다르다.** author는 참조 구현으로만 인용하여 거짓말은 하지 않았지만, 현재 `gate_selftest_260828.py`는 `baseline_exit=1 baseline_failures=5`에서 중지한다. `undetected=0`을 지금 달성했다고 읽힐 문구는 금지해야 한다.

## 5. 소유·경계 감사

| 대상 | author 처분 | 판정 |
|---|---|---|
| F6 acceptance criterion | 사용자/`rev-arbiter` 결정 전 시작 금지; author는 decision request만 | **PASS** |
| F9 expected value/rule | 값 선택 안 함; generator 재유도 후 감사 동결; 수동 표 수정 금지 | **PASS** |
| repaired schema | proposal/evidence로만 취급 | **PASS**, 단 proposal header `:4`는 stale conflict |
| regenerated TSV | 승인된 ruler로 승격하지 않음 | **PASS** |
| measured author의 ruler 수정 | 명시적 금지 | **PASS** |
| audit lane의 자기 gate/self-test 개정 | 명시적 허용은 없으나 개정자/qualifier 분리도 없음 | **BLOCKED — 역할 분리 필요** |
| gatekeeper 승인·외부 승인 | local conjunction gate만 수행, 외부 Opus 승인 문구 금지 | **PASS** |

결론적으로 author 권고는 measured lane에게 자 수정권을 돌려주지 않았고 repaired/regenerated 파일을 승인본으로 취급하지 않았다. 다만 **감사측 내부에서 gate code 작성자와 검출력 qualifier를 분리하지 않으면**, “감사측 소유”라는 표현이 자기 gate 자기 개정의 새 뒷문이 된다.

## 6. 재현 명령과 실측 출력

```powershell
# 13 frozen inputs
Get-Item -LiteralPath <path>
Get-FileHash -Algorithm SHA256 -LiteralPath <path>
# 결과: 13/13 bytes·sha256 exact match

python output/260828/rev/meta_gate_260828.py --check all
# freeze_ok=12/12
# integrity_hits=7; vacuous_signal_count=1; coverage_failures=2
# warnings=0; failures=7; meta-gate: FAIL; exit=1

python output/260828/rev/gate_selftest_260828.py
# source_files=16
# baseline_exit=1 baseline_failures=5 baseline_warnings=0
# FAIL: baseline is not clean; differential selftest needs a passing baseline
# exit=1

# author finding table deterministic parse
# expected=[F1,F2-b,F3,F6,F9]
# observed=[F1,F2-b,F3,F6,F9]
# duplicate=[] missing=[] extra=[] count=5

# author SHA-256
Get-FileHash output/260829/rev/detection-failure-audit/01_author_root_cause.md
# b7538ee3fdf315911c2ec70b7a471d044e3561830b8386a411f36c16af95154d
```

두 expected TSV의 item IDs는 각각 22개로 동일하고 중복이 없다. 핵심 source range 비교에서는 W-04만 shipped `44-48`, regenerated `44-49`로 다르다. 마지막 열의 schema가 `pilot_wave` 대 `derivation_rule`로 다르므로 파일 전체 행 동등성으로 비교하지 않고 ID·section·number·source_path·start/end 범위를 분리 비교했다.

## 7. findings 및 critic 전달 권고

### Critical

- **C-01 runtime assurance evidence missing:** author와 auditor 모두 actual model/depth telemetry가 없다. `actual-team` 보증 및 외부 비교는 `▲ blocked`다.
- **C-02 raw evidence incompleteness:** F2-b/F6/F9의 핵심 역사·의미 재현에 필요한 raw frozen artifacts가 없다. frozen Opus 감사에 대한 충실한 요약은 PASS지만, 이 팀의 독립 재검산 완료 주장은 BLOCKED다.
- **C-03 audit-ruler separation underspecified:** gate/self-test 개정자와 이를 동결·qualification하는 감사권한자가 명시적으로 분리되지 않으면 감사팀이 자기 자를 고치는 구조가 재발한다.

### Noncritical

- **N-01 repaired proposal stale header:** `repaired.md:4`는 최신 ruler ownership 규칙과 충돌하므로 final packet에서 승인 가능한 지침처럼 인용하면 안 된다.
- **N-02 current self-test baseline dirty:** 과거 `detected=8/undetected=3` 로그는 frozen 역사 증거이고 현재 재실행 결과가 아니다.

### 추천

**Adversarial review dispatch recommendation: BLOCKED.** 최소 stop condition은 (1) author/auditor observed model/depth의 별도 runtime evidence 확보 또는 actual-team claim 철회, (2) raw evidence 미동결을 최종 보고서에서 명시적 BLOCKED로 유지, (3) audit gate **개정자 ≠ qualifier/refreezer**의 two-key 역할을 preflight에 고정하는 것이다. 이 조건이 충족되지 않은 상태에서 critic을 실행하면 레인 수는 늘지만 실제 assurance hard gate는 통과하지 않는다.

## 8. 비승인 선언

이 문서는 Codex assurance team의 독립 증거 감사이며 제안 등급이다. author 초안을 수정·승인하지 않았고, 어떤 ruler 값·gate 변경·canonical 반영·release도 승인하지 않는다. 외부 Claude Code Opus 역할의 검토·판정·승인을 대체하지 않는다.

Pipeline: 감사 사전동결 → author pilot → **독립 evidence audit 완료(BLOCKED)** → adversarial critique → gatekeeper → 외부 Opus 검토
Stage: assessment evidence auditor = assigned configuration gpt-5.6-sol/high, observed model/depth telemetry unavailable — 13/13 frozen hash와 author hash 일치, ID 5/5 exact coverage, F1/F3 직접 재현; F2-b/F6/F9 raw 재현과 runtime evidence가 active blocker
Team: mode=actual-team; lead=gatekeeper | gpt-5.6-sol | coordinator | running; lanes=evidence auditor = assigned gpt-5.6-sol = high | independent evidence auditor | completed BLOCKED audit | `.codex/agents/assessment-evidence-auditor-sol.toml` | exclusive output `output/260829/rev/detection-failure-audit/02_evidence_audit.md`; independence=independent; planned/unavailable/failed lanes=author completed but observed model/depth unavailable, adversarial critic planned and dispatch BLOCKED; observed model/depth telemetry unavailable
Next: leader가 이 파일의 hash·exclusive-write·5-ID schema를 검증한 뒤 C-01~C-03 stop condition을 판정한다. 하나라도 해소되지 않으면 critic dispatch와 외부 비교를 중지하고 `▲ blocked`를 유지한다.
