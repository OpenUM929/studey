# 260829_01 판정 기술 재검토 — evidence review pilot

상태: `ADVISORY REVIEW — REVISE BEFORE USER KEY`  
대상: `Q3`, `Q4`, `Q5`, `F10` 4개 단위  
대상 판정문: `output/260829/rev/detection-failure-audit/260829_01_detection_failure_ruling.md`

## 1. 실행 정체성·컨텍스트·입력 검증

- runtime identity: `/root/detection_evidence_audit`.
- configured model/depth: `.codex/agents/assessment-evidence-auditor-sol.toml:1-4`의 `gpt-5.6-sol / high`.
- observed model/depth: **unavailable**. 설정값을 런타임 관측으로 승격하지 않는다.
- context status: **shared-context**. 기존 agent lineage를 이어받았으므로 독립성을 주장하지 않는다.
- 역할 지침: `.codex/agents/assessment-evidence-auditor-sol.toml`.
- 배타 출력: `output/260829/rev/detection-failure-audit/06_EVIDENCE_REVIEW.md` 한 파일.
- 금지 경계: 판정문, 정본, 원장, WIP, ruler, gate, generator, 기존 보고서를 수정하지 않았고 사용자 2차 키를 추정하지 않았다.

실제 순서: 역할 지침과 `05_RULING_REVIEW_PREFLIGHT.md`를 먼저 읽고, manifest 16파일의 bytes/SHA-256을 재계산한 뒤 원천·코드·기존 보고서를 판독했다. 그 후 대상 판정문의 Q3~Q5·F10/BF1~BF5를 열어 대조했다.

manifest hash 결과: expected `16`, observed `16`, missing `[]`, byte mismatch `[]`, hash mismatch `[]`, drift `0`.

## 2. 추가 직접 원천

05 preflight가 허용한 “manifest 파일이 직접 지목한 원천”으로 아래 4개를 추가 판독했다. 이는 입력 완전성이나 refreeze를 뜻하지 않는다.

| path | bytes | sha256 | 직접 참조·이유 |
|---|---:|---|---|
| `output/260828/diagnostic/math2-method-comparison/codex-team/EXPECTED_ITEM_IDS_260828.tsv` | 1652 | `db0ff6e06641aba7f213b362b69317f2ce9c06f5cc66083319f12bdf7421cfe4` | `00_PREFLIGHT.md` frozen table이 직접 지목; Q5 shipped span 대조 |
| `output/260828/rev/EXPECTED_ITEM_IDS_260828.regenerated.tsv` | 1613 | `48460b1c168a718a6589d7550abdb9f2449e65494d91249debd0c3cada26cb23` | `00_PREFLIGHT.md` frozen table이 직접 지목; Q5 regenerated span 대조 |
| `tools/build_mastery.py` | 5761 | `b20e865a510aeabf6ff34e3716b1e20631a98fbf2ddfa95ace4fed0ec75e4d66` | 판정 Q3가 정직한 warning 구현 예로 직접 지목 |
| `tools/import_grading.py` | 12463 | `df17a50b8e37ed3a424dfb25c7c20f114d63e680b100c3492b65df08b7e6464c` | 판정 Q3가 정직한 warning 구현 예로 직접 지목 |

generator 구현 파일은 판정/BF3에 경로가 특정되지 않았고 16-file manifest에도 없으므로 읽지 않았다. 따라서 Q5의 **현재 generator 구현 적합성**은 검증 범위 밖이다.

## 3. 쟁점 ID exact coverage

expected=`[Q3,Q4,Q5,F10]`  
observed=`[Q3,Q4,Q5,F10]`  
duplicate=`[]` · missing=`[]` · extra=`[]` · count=`4`  
warnings list=`[]` · warnings=`0`

| ruling item | direct file:line evidence | recomputation / analysis | severity | disposition | unknown / limit |
|---|---|---|---|---|---|
| **Q3** warning 채널 | `check_experiment.py:223`; `CLAUDE.md:78-85`; `build_mastery.py:113-132`; `import_grading.py:242-254`; ruling `:104,114` | 상수 `warnings=0` 제거와 계산값 전환 방향은 타당하다. 그러나 “삭제하면 원칙 11 연언이 무의미”는 성립하지 않는다. 원칙 11은 **경고 0줄**을 요구할 뿐 반드시 `warnings=` 카운터를 요구하지 않는다. 더구나 판정은 warning을 “차단하지 않는 이탈”로 정의하지만 인용한 두 도구는 warning을 integrity defect로 보고 exit 1/fail-closed 처리한다. `check_experiment.py`에는 `[OK]` 줄도 없어 BF1의 “[WARN]을 [OK]보다 먼저”가 현재 출력 스키마와 맞지 않는다. | high | **revise-before-user-key** | warning이 tool-exit 비차단인지, composite acceptance 차단인지, failure와 어떤 차이가 있는지 미정. PASS marker를 `[OK]`로 신설할지 `experiment-gate: PASS`를 기준으로 삼을지도 미정. |
| **Q4** reusable/count/exact-cover | `types.tsv:1-13`; `items.tsv` 다중배정 8행; `check_experiment.py:137-165`; repaired schema `:12-17`; ruling `:48-63,105,115,117` | 원본 12행을 의미대로 펼치면 `reusable=6`(12 items), 기존 singleton 3 + U10/U11의 독립 item 6 = `singleton=9`, `blocked=1`, 총 `rows=16/items=22`; `22/16=1.375`는 산술상 맞다. 그러나 새 규칙은 16을 **유일하게 강제하지 않는다**. 같은 generator의 2문항을 두 singleton으로 쪼개도 row_kind/count 조건을 만족하며, maximal consolidation 규칙이 없다. 상·하한 폐지 뒤 exact `rows=16`을 pass/fail 기대값으로 넣으면 count 압력을 더 강하게 재도입한다. singleton 한 문항에서 “관측 variation axes 2개”가 무엇을 뜻하는지도 불명확하다. exact-cover는 primary membership에만 적용해야 primary/secondary 다중배정과 양립한다. | critical | **revise-before-user-key** | `generator_id`의 정형 정의·출처, maximality/동치 규칙, singleton axis의 관측 단위, blocked 포함 여부를 포함한 reuse_ratio 분모·분자, primary exact-cover와 secondary reference의 스키마 위치가 미정. |
| **Q5** span/generator | transcript `:29-55,138-152`; shipped/regenerated TSV; ruling `:65-85,106,116` | `^#{1,6}\s`를 **경계**로 적용하면 W-04는 44–49가 맞다. 그러나 같은 규칙으로 S-18은 다음 heading 149 직전인 138–148이 된다. shipped와 regenerated TSV는 모두 S-18을 138–146으로 적어 horizontal rule `---`(147)과 blank(148)를 제외한다. 따라서 판정의 “21/22가 다음 heading 직전”, “마지막 문항은 EOF”, “모든 derivation_rule=rule_a”는 서로 및 실제 TSV와 모순이다. 자체 재계산은 regenerated와 W-04 외에 **S-18도 diff**를 냈다. heading regex는 경계만 정의하고 item-start heading 식별도 정의하지 않는다. | critical | **revise-before-user-key** | horizontal rule/section appendix/EOF 처리, item heading 식별(`## N.`과 section 상태), fenced code·선행 공백·ATX 변형의 범위, generator path/hash와 fixture가 미정. W-04 44–49만 단독 확정해도 전체 rule은 닫히지 않는다. |
| **F10** evidence-scope ownership | `00_PREFLIGHT.md:23-45`; included expected TSV의 transcript path; `check_experiment.py:208-211`의 author items/types 직접 경로; ruling `:87-96,118,139-141` | 원래 13-file freeze에는 transcript/items/types가 없었고, 포함된 자와 gate가 세 원천을 직접 참조했다. F6/F9 raw 재현이 그 경계 때문에 차단된 것은 재현된다. 다만 `00_PREFLIGHT` 작성자는 개별 author lane이 아니라 main-loop coordinator이므로 “피측정 레인”은 **피측정 assurance team/조정 축**으로 정확히 써야 한다. BF5의 “직접 참조 원천 전부 포함”은 필요조건이지만 충분조건이 아니다. 산문 예시·역사 경로·출력 경로·순환 참조를 구분하는 typed dependency와 claim→evidence closure가 필요하다. | high | **accept-with-clarification** | closure의 재귀 깊이, dependency kind, missing/optional 처리, cycle, source-of-truth와 derived artifact 구분, scope 후보 작성자와 qualifier/refreezer가 미정. |

## 4. 독립 재계산 세부

### 4.1 Q3 — warning 의미가 아직 닫히지 않았다

1. 현 gate는 warning collection 없이 `print(f"warnings=0")`만 출력한다(`check_experiment.py:191-230`). 계산값 전환 필요성은 직접 재현된다.
2. `CLAUDE.md:78-85`는 acceptance evidence로 “경고 0줄 + exit 0”을 요구한다. 이것은 **warning counter 존치**를 논리적으로 강제하지 않는다. `[WARN]` 줄이 0개인지 별도 검사해도 같은 연언을 구성할 수 있다.
3. `build_mastery.py:114-131`은 warning을 “integrity defect — not advisory”로 정의하고 warning이 있으면 exit 1이다. 이는 Q3의 “차단하지 않는 이탈” 정의와 반대다.
4. `import_grading.py:242`는 `[OK] appended ...`를 warning보다 먼저 출력한다. `:246-254`의 주석은 regenerated marker에 대해서만 warning-first다. 따라서 판정의 “같은 이름의 채널을 정직하게 계산하는 도구”와 BF1의 전역 `[WARN] before [OK]` 모범으로는 불완전하다.
5. `check_experiment.py`는 `[OK]`가 아니라 `experiment-gate: PASS`를 출력한다. BF1은 ordering target을 실제 marker에 맞추거나 출력 schema 변경을 별도 명시해야 한다.

기술적으로 가능한 일관된 의미는 둘 중 하나지만, 이 레인은 선택하지 않는다.

- warning은 tool-level 비차단이지만 composite acceptance에서는 warning 0이 아니면 차단; 또는
- warning은 곧 integrity failure이며 exit 1, failure와의 차이는 진단 분류에만 존재.

어느 쪽이든 warning 생성 조건, exit semantics, PASS marker, expected count를 BF1의 수용기준으로 고정해야 한다.

### 4.2 Q4 — 16은 재현되지만 규칙에서 유일하게 유도되지 않는다

fresh TSV parse:

```text
physical rows=12
reusable rows=6, reusable member items=12
existing singleton rows=3
U10/U11 independent members=6
blocked rows/items=1
expanded rows=6+3+6+1=16
items=12+3+6+1=22
22/16=1.375
```

이 계산은 ruling §2.1과 일치한다. 그러나 **재산출 가능**과 **수용기준으로 유일**은 다르다.

- `row_kind=reusable`은 “2문항 이상”이라는 필요조건만 주며 동일 generator 문항을 반드시 한 행으로 최대 통합하라는 규칙이 없다.
- gate가 “같은 generator”를 검사하려면 prose `type_disposition`이 아니라 정형 `generator_id`와 각 item의 primary generator 근거가 필요하다. `row_kind`만 추가해서는 U10/U11 같은 semantic umbrella를 결정론적으로 검출하지 못한다.
- 한 item에 variation이 실제로 두 번 **관측**된 것인지, 한 item에서 조절 가능한 feature axis 두 개를 추론한 것인지 구분이 없다. singleton에 “observed axis ≥2”를 요구하려면 비교 원천과 관측 단위를 명시해야 한다.
- current `items.tsv`에는 `primary + secondary` 배정이 8행 있다. exact-cover는 `member_item_ids`의 **primary row membership**에만 적용하고 `secondary_types`는 비포괄 참조로 분리한다고 써야 중복 판정과 충돌하지 않는다.
- `reuse_ratio=items/rows`가 blocked item까지 포함한 `22/16`이면 이름과 달리 source defect도 reuse 성과를 높인다. 최소한 `all_items/all_rows`, `nonblocked_items/nonblocked_rows`, `items_in_reusable_rows/nonblocked_items` 중 무엇인지 이름·식을 고정해야 한다.

따라서 Q4의 의미 재설계 방향은 타당하지만 BF2/BF4는 아직 실행 가능한 exact schema가 아니다.

### 4.3 Q5 — S-18 반례

heading regex `^#{1,6}\s`와 “다음 heading 직전”을 그대로 구현해 22개 item heading을 재계산했다.

```text
derived item headings=22
W-04 derived=44-49; shipped=44-48; regenerated=44-49
S-18 derived=138-148; shipped=138-146; regenerated=138-146
```

S-18 뒤 실제 행은 `146 blank`, `147 ---`, `148 blank`, `149 ## 전사 범위·보류`다. 판정 Q5가 정의한 heading-only rule은 147~148을 span에 포함한다. 반면 양쪽 TSV는 horizontal rule 직전의 blank 146까지만 포함한다. 그러므로 최소 하나가 필요하다.

- horizontal rule을 item boundary로 정의한다.
- section/appendix boundary를 heading과 별도로 정의한다.
- trailing separator normalization을 generator 규격으로 정의한다.

또한 item **start**는 단순 모든 heading이 아니라 section 내부의 numeric item heading이어야 한다. BF3가 regex 한 줄만 고치면 W-04는 고쳐져도 S-18과 future appendix/fence edge case는 닫히지 않는다.

### 4.4 F10 — dependency closure는 typed closure여야 한다

원 13-file manifest에서 세 raw path는 모두 absent였고, included source가 직접 지목했다.

```text
transcript manifest_present=False; expected TSV direct_ref=True
author/types.tsv manifest_present=False; check_experiment direct_ref=True
author/items.tsv manifest_present=False; check_experiment direct_ref=True
```

F10의 구조적 진단은 지지된다. 다만 “경로 문자열을 찾으면 전부 freeze”는 다음 오탐/폭증을 만든다.

- historical evidence path와 active input path 혼합;
- output/reply path를 source dependency로 오인;
- 문서 간 순환 참조;
- optional/absent rendered evidence를 필수 file hash로 오인;
- 직접 언급되지 않았지만 material claim에 실제로 필요한 원천 누락.

BF5에는 최소 `dependency_kind`, `required|optional|blocked`, `source|derived|ruler|evidence`, `parent_claim`, `resolved path/hash`, cycle 처리, closure warnings/failures가 필요하다. 또한 `CLAUDE.md:254-260`의 동반 갱신 목록상 CLAUDE 단독 수정은 불충분하며 `AGENTS.md`, `REV_GUIDE §5`, agent definitions, `check_assurance_contract.py`의 동반 점검을 BF5에 포함해야 한다.

## 5. BF1~BF5 스키마 충분성

| binding fix | Q/F 연결 | 판정 | 부족한 최소 필드/검증 |
|---|---|---|---|
| **BF1** | Q3 | **revise** | warning definition, collection sites, exit semantics, PASS marker, `[WARN]` ordering target, fixture가 warning을 실제 발생시키고 count/exit/order를 검증하는 명령·기대 출력 |
| **BF2** | Q4 | **revise** | structured `generator_id`, row_kind legality, primary exact-cover 대상 열, secondary 비포괄 열, singleton axis evidence source, umbrella semantic check owner, count를 acceptance가 아닌 report로 둘지 명시 |
| **BF3** | Q5 | **revise** | generator exact path/hash, numeric item-start rule, category/appendix/horizontal-rule/EOF boundary, S-18 fixture, fenced/indented heading scope, 22-row expected diff와 stale trigger |
| **BF4** | Q4 | **revise** | exact 16의 uniqueness/maximality 근거가 없으므로 pass/fail expected count로 승격 금지 또는 정형 generator partition을 별도 freeze; reuse_ratio 식·blocked 처리; repaired proposal의 stale ownership header 제거 여부는 ruler 변경 절차에서 별도 처리 |
| **BF5** | F10 | **revise** | typed claim-to-evidence dependency closure, transitive/cycle 규칙, optional/missing disposition, scope 후보 작성자와 qualifier/refreezer 분리, CLAUDE companion updates와 deterministic closure gate |

BF1~BF5 어느 것도 이 레인이 수정하지 않았다. 특히 BF4의 repaired schema 승격과 BF3의 expected 값 변경은 사용자 key/refreeze 전 운영 자로 취급할 수 없다.

## 6. 재현 명령과 검증 출력

```powershell
# manifest 16
Get-Item -LiteralPath <each path>
Get-FileHash -Algorithm SHA256 -LiteralPath <each path>
# expected=16 observed=16 missing=[] byte_mismatch=[] hash_mismatch=[]

# Q4 parse: csv.DictReader(types.tsv/items.tsv, delimiter='\t')
# physical_rows=12 reusable_rows=6 reusable_items=12
# expanded_singletons=9 blocked=1 expanded_rows=16 items=22 reuse_ratio=1.375
# primary+secondary item rows=8

# Q5 parse: heading boundaries by ^#{1,6}\s and item starts by ^##\s+\d+\.\s*$
# derived_count=22
# shipped diffs=[W-04 (44-49 vs 44-48), S-18 (138-148 vs 138-146)]
# regenerated diffs=[S-18 (138-148 vs 138-146)]

# F10 closure spot-check
# transcript absent/direct_ref=True; types absent/direct_ref=True; items absent/direct_ref=True
```

output validation: target IDs `4/4`; duplicate/missing/extra 모두 `[]`; replacement character count `0`; literal mojibake question-mark count `0`; warnings=`0`.

## 7. 결론과 다음 게이트 권고

### Critical

- **C1 Q5 rule contradiction:** heading-only rule_a는 S-18을 138–148로 만들지만 shipped/regenerated 모두 138–146이다. Q5/BF3는 전체 22행 규칙을 아직 닫지 못했다.
- **C2 Q4 exact-count reintroduction:** count band를 폐지하면서 근거가 유일하지 않은 exact rows=16을 acceptance expected로 넣어 동일한 count-optimization 압력을 재도입한다.
- **C3 Q4 schema mismatch:** row_kind만으로 same-generator umbrella를 기계 판정할 수 없고, singleton observed-axis와 primary exact-cover/secondary membership 의미가 미정이다.

### High

- **H1 Q3 warning contradiction:** “nonblocking deviation”과 인용 도구의 fail-closed warning semantics가 충돌하고 check_experiment에는 ordering 대상 `[OK]`가 없다.
- **H2 F10 closure insufficiency:** finding은 재현되지만 BF5의 untyped direct-reference closure와 CLAUDE-only 수정은 dependency closure 및 동반 갱신 게이트로 불충분하다.

### Pilot disposition

Q3=`revise-before-user-key`; Q4=`revise-before-user-key`; Q5=`revise-before-user-key`; F10=`accept-with-clarification`.

다음 governance critique는 이 보고서의 C1~C3/H1~H2를 입력으로 삼을 수 있다. 다만 이 pilot은 shared-context이고 ruler 선택권이 없으므로 Q3~Q5의 binding 값을 승인하거나 사용자 key를 대행하지 않는다.

## 8. 비승인 선언

이 문서는 기술 재검토 제안이다. 판정문·ruler·gate·generator·정본·원장·release를 수정하거나 승인하지 않는다. 외부 Claude Code Opus 판정 또는 사용자 2차 키를 대체하지 않는다.

Pipeline: ruling dispatch manifest → **evidence re-review pilot 완료(REVISE)** → governance critique → ruling-response gate → main-loop integration
Stage: assessment evidence auditor = configured gpt-5.6-sol/high, observed unavailable — 16/16 hash 일치, Q3/Q4/Q5/F10 4/4 exact coverage; Q5 S-18 규칙 반례와 Q4 count/schema 모순이 active blocker
Team: mode=actual-team; lead=gatekeeper | gpt-5.6-sol | coordinator | running; lanes=evidence review = configured gpt-5.6-sol = high | evidence auditor | completed shared-context pilot | `.codex/agents/assessment-evidence-auditor-sol.toml` | exclusive output `output/260829/rev/detection-failure-audit/06_EVIDENCE_REVIEW.md`; independence=shared-context; planned/unavailable/failed lanes=observed model/depth unavailable, governance critique pending leader pilot inspection
Next: leader가 이 파일의 hash·exclusive-write·4-ID coverage·warnings를 검증한다. 검증 통과 후에만 governance critique를 배치하며, critic은 C1~C3/H1~H2가 user-key 전 수정 필요인지 판정한다.
