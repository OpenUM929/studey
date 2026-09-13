# 정보 A/B50 실행 복구 문구 — 독립 절차 검토

**[REJECT]**

status: `▲ blocked`
author: Codex/OMX 절차 비평자
scope: 문항 내용 감사·기준 변경 승인·배포 승인이 아닌 절차 문구 검토

**Justification:** 적용 문구의 방향은 승인 뒤 무실행 종료를 막으면서 two-key·독립성·배포 승인을 보존하려는 것으로 타당하다. 그러나 그대로 반영하면 (1) Q3의 시간 질문을 정확한 기준 선택으로 소급 간주하는 실행 단계, (2) 판정이 허용 범위를 읽기·재현·결정 제출로 닫았는데도 별도 제안본 작성을 일반적으로 허용하는 문장, (3) 배우별 write surface를 특정하지 않은 `WIP/결정 기록` 쓰기 지시 때문에 실행자가 추측해야 한다. 또한 이 검토의 실제 호스트 메타는 `gpt-5.6-sol / high`로 노출되어 Astra 전용 검토 요건을 충족하지 않는다. 따라서 아래 지적은 비구속 절차 비평으로만 사용할 수 있고, 독립 Astra 감사 키나 승인으로 소비할 수 없다.

## Summary

- Clarity: **fail** — 일반 승인과 Q1/Q2/Q3의 정확한 선택을 구분하지 않아 계획 4단계의 소급 승인 해석을 허용한다.
- Verifiability: **partial** — 문서 diff·보호 자 해시 보존은 검증 가능하지만, “동의한 것이면”과 “별도 제안본”의 허용 조건은 결정적으로 판정할 체크가 없다.
- Completeness: **fail** — actor별 허용 write surface와 Q4의 현재 실행 범위 우선 조건이 빠졌다.
- Big Picture: **fail until repaired** — 무실행 재발 방지 목적은 맞지만, Q3/Q4의 binding 경계를 우회할 수 있다.
- Principle/Option Consistency: **fail** — Q4는 정확한 Q1/Q2/Q3 선택을 요구하고 현재 즉시 수정 가능한 제품·기준 파일을 0개로 닫는데, 계획 4단계와 제안본 문구가 이를 넓힌다.
- Alternatives Depth: **pass** — 지침 무수정, 최소 5문구 삽입, 과도한 시스템 개정의 대안 중 최소 삽입을 택한 근거는 충분하다.
- Risk/Verification Rigor: **fail** — 문구 해석 fixture와 실제 Astra 검토 증거가 없다.
- Deliberate Additions: **not required** — 합의형 deliberate 검토로 발주되지 않았다.

## 차단 지적과 최소 수정

1. **Q3 소급 승인 금지 — definite blocker.** 계획의 검증 단계 4 `Q3 사용자 답변 ... 을 기존 결정 범위의 승인으로 기록`은 판정 Q4의 “정확한 ... 별도 Q3 기준 선택” 및 “이번 수행으로 소급 충족되지 않는다”와 충돌한다. 인용된 답변에는 기준 원천·구조·필수 추가 사고력 선택이 없다.
   - 최소 수정: 단계 4를 다음처럼 바꾼다.  
     `Q3 답변은 완료시각 질의와 일반 진행 의사로만 기록한다. Q1/Q2/Q3의 정확한 선택으로 소급 간주하지 않으며, 현재 판정이 허용한 읽기·근거 정리·결정안 제출을 같은 턴에 시작한다. 제품·자 반영은 두 키 이후로 유지한다.`
   - 첫 문구에도 다음 한 문장을 붙인다.  
     `다만 판정이 정확한 선택값을 요구한 사안은 일반 동의·진행 촉구·시간 질문으로 충족한 것으로 보지 않는다.`

2. **판정이 닫은 허용 범위보다 제안본을 넓히지 말 것 — definite blocker.** `별도 제안본 준비까지 금지됐다고 확대하지 않는다`는 일반 문장은 Q4가 이 단계의 실행 가능 범위를 회신 읽기·해시 확인·읽기 전용 재현·사용자 결정 제출로 한정한 사실을 무시할 수 있다.
   - 최소 수정: 해당 두 문장을 다음처럼 치환한다.  
     `특정 판정이 제품 쓰기나 현재 실행 범위를 제한하면 그 제한을 그대로 지킨다. 판정 또는 현행 write surface가 명시적으로 허용한 제안 작업만 계속하며, 제안본은 승인 정본·독립 검증본·배포 승인으로 표시하지 않는다.`

3. **기록 write surface 한정 — definite gap.** `기존 WIP/결정 기록에 한 번 남기고`는 일반 실행자가 타인 WIP, 공유 원장 또는 판정 문서에 쓸 수 있는 것처럼 읽힌다. REV_GUIDE §5는 배우별 write surface와 동시 쓰기 금지를 고정한다.
   - 최소 수정: `그 범위만 자기 소유 WIP 또는 현재 단계에서 쓰기가 명시적으로 허용된 결정 기록에 한 번 남기고`로 바꾼다. 허용 기록이 없으면 새 기록을 만들지 말고 기존 승인 증거를 참조한다.

4. **독립 단계 문구 자체는 보존 가능 — no issue after model gate.** `깨끗한 Astra 컨텍스트를 사용할 수 있으면 사용`하고 불가 시 제한을 기록하며 감사 완료를 꾸미지 않는 문장은 Astra 정책과 일치한다. 다만 이번 검토는 실제 Sol 호스트이므로 이 문구에 대한 독립 Astra 승인으로 사용할 수 없다.

5. **나머지 두 문구는 통과 가능.** 인계·결정 보고서 재생산 금지와 근거 없는 완료시각 금지는 append-only 삭제를 지시하지 않고, 필수 게이트·실제 차단을 종료 조건으로 남겨 우회가 아니다. 단, 필수 재개 감사나 Q4 해시 게이트를 “변하지 않은 입력 재해시 금지”로 생략해서는 안 된다.

## 대표 실행 시뮬레이션

1. **보호 자와 무관한 명시적 내용 수정 승인:** 자기 write surface 안의 다음 안전한 작업을 같은 턴에 수행할 수 있다. 새 문구의 목적에 부합한다.
2. **Q3 답변 `맞어 ... 언제쯤`:** 일반 진행 촉구는 될 수 있으나 구조 기반 난이도 자·기준 자료·필수 추가 사고력의 정확한 선택은 아니다. 계획 현행 단계 4로는 실행자가 추측해야 한다.
3. **Q4 상태에서 별도 제안본 생성:** Q4가 현재 출력을 결정 항목 제출까지로 제한하므로, 판정 또는 write surface가 별도 허용하지 않은 제안 산출물은 만들 수 없다.
4. **깨끗한 Astra 컨텍스트 부재:** 독립 감사 완료를 주장하지 않고 `▲ blocked`와 실제 제한을 기록해야 한다. Sol 비평으로 대체할 수 없다.

## 실제 읽은 입력과 해시

| path | bytes | SHA256 |
|---|---:|---|
| `analysis/rev/260912_info_execution_repair_plan.md` | 5686 | `5548f95369717fa48449ecd7cf229b7833b93b0dac4c80d36237213d8892d244` |
| `docs/ITEM_DELIVERY_WORKFLOW.md` | 6321 | `36a7846309a253cf4c2a9543ea486617caa7c6fbd526e4ae81a260c448b18467` |
| `analysis/REV_GUIDE.md` | 49701 | `240dc9b34a59bc24111a06658a96c50468729510336e0ac2da41dd6b4a111fcb` |
| `docs/ASTRA_EXECUTION_POLICY.md` | 3267 | `40424dd0e82eb36204b61890be8a44cf9f0cd0d95300f217ac86c8366199833b` |
| `output/260911/rev/260911_03_info_ab50_ruler_ruling.md` | 68935 | `ff129cc5ce45487671ba1f2626237950dccb3f2d57828729906c5dcb66edb8b1` |

읽기 범위: 계획 전체, 대상 절차 전체, Astra 정책 전체, `REV_GUIDE.md` §5·§5-a, 기존 판정 Q3/Q4와 그 적용 지시. 제품 문제·답·해설·원천은 읽지 않았다.

## 호스트 실행 증거와 한계

- 실행 identity: native child task `/root/procedure_check`; 상위 런타임 세션 표기 `omx-1789196581976-gn8uis`.
- 호스트가 이 레인에 노출한 실제 메타: role `critic`, resolved model `gpt-5.6-sol`, reasoning effort `high`.
- 계획의 요청값 `gpt-6-astra = high` 및 계획에 적힌 `turn_context Astra/medium`은 이 레인의 실제 모델 증거가 아니다.
- 서비스 잔여 예산은 노출되지 않아 `insufficient`; fallback2의 독립 단일 유계 슬라이스로 종료했다.
- 확인 한계: 런타임 서명·provider-side model attestation은 제공되지 않았다. 이 때문에 Astra 독립 검토 완료를 주장하지 않는다.

Pipeline: 정보 문항 실행 복구 계획 → **독립 절차 검토 `▲ blocked`** → 리더 최소 문구 재작성 → 깨끗한 Astra 재검토 → 허용된 실제 작업 재개
Stage: procedure critic = gpt-5.6-sol — 5개 허용 입력 대조 완료; 우회 위험 3건을 특정했으나 Astra 전용 모델 게이트 불충족
Team: mode=solo; lead=procedure critic | gpt-5.6-sol | critic | completed-with-blocker; lanes=procedure-check = gpt-5.6-sol = high | independent procedure critic | `▲ blocked` | `C:/Users/Park/.codex/prompts/critic.md`; independence=independent context but disallowed model; planned/unavailable/failed lanes=clean Astra reviewer unavailable in this execution
Next: 리더가 위 3개 최소 수정을 계획/대상 문구에 반영하되 이를 승인으로 표시하지 않고, 실제 `gpt-6-astra` 깨끗한 컨텍스트 검토가 확보될 때만 독립 검토 게이트를 통과시킨다. 그 전에는 제품·자·판정·배포를 건드리지 않는다.
