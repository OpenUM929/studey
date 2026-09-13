---
title: 정보 A/B50 수리 명세 상태계약 완결성 판정
created: 2026-09-11
author: Codex/OMX (별도 컨텍스트 직접 판정)
responsibility: 수리 명세 상태계약 판정; 문항 맹목 풀이 아님
observed_model: gpt-6-astra
observed_reasoning_depth: medium
model_evidence: host-generated turn_context
grade: binding (명세 완결성 한정)
verdict: revise-required
repair_execution: blocked
release: blocked
---

# §0 판정 요약표

| unit | verdict | grade | evidence | measured | closure | note |
|---|---|---|---|---|---|---|
| Q2 상태계약의 구현 착수 가능성 | revise-required | binding (완결성 한정) | 수리 명세 §2·§5·다음 단계; 선행 판정 §2 Q2·Q4; 아래 재현 명령 | yes | 상태 차원 4/4 확인; 실행 계약 완성은 명세 자체가 미확정으로 명시. 새 규칙의 모집단 폐쇄 판정은 하지 않음 | 분리 방향을 기각하지 않는다. 적용 단계·분모·상태별 종료 코드가 없는 현 문서는 구현 계약이 아니다 |

**결론:** 수리 명세의 방향은 기존 판정과 양립하지만, 상태계약 승인과 코드 반영으로 넘어갈 만큼 구체화되지 않았다. 기존 차단을 해제하지 않는다. 수정 요구는 아래 BF1 한 건으로 한정한다. 새로운 난이도·분모·경고 면제 기준을 이 판정에서 만들지 않는다.

# §1 독립 재검증

## 실행·입력 경계

- 현재 호스트 세션: `01a09096-47a0-7122-91e1-67e7d3fb4850`.
- 현재 turn: `01a09096-5354-7303-8557-97be9e5030e7`.
- 호스트 JSONL: `C:/Users/Park/.codex/sessions/2026/09/11/rollout-2026-09-11T22-09-23-01a09096-47a0-7122-91e1-67e7d3fb4850.jsonl`.
- `CODEX_THREAD_ID`로 파일을 좁히고 `type=turn_context`의 `model=gpt-6-astra`, `effort=medium`을 직접 확인했다. 환경값·설정 파일만으로 모델을 인증하지 않았다.
- 이 컨텍스트는 수리 명세를 작성하지 않았다. 사용자 인계문과 이번에 읽은 명세·선행 판정을 입력으로 삼았다. 팀·서브에이전트 발주 없이 순차 직접 수행했다. 파일 접근 격리나 서버 내부 라우팅 attestation을 주장하지 않는다.
- 책임 지침: `.claude/agents/rev-arbiter.md`; 실제 실행자는 Claude Code Opus가 아닌 Codex/OMX다. 모델 정책은 `docs/ASTRA_EXECUTION_POLICY.md`를 적용했다.
- 허용 읽기: 위 지침, `CLAUDE.md`, `docs/DATA_STANDARD.md`, `analysis/REV_GUIDE.md`, 수리 명세, 선행 판정의 상태계약·권한 절, 원천 inventory 바이트, `analysis/REV_LOG.md` 말미와 `tools/textpatch.py` 원장 처리 규격.
- 금지 작업: 원천·기준·코드·문항·타인 WIP 수정, 문항 정답/해설 독립검증 주장, 배포. A/B 문항 본문·답지는 이번에 읽지 않았다.
- 인계문은 정식 §6-b/§6-d 패킷의 모든 필드를 갖추지 않았다. 이번에는 지목된 명세의 Q2 완결성만 판정한다. 패치 승인·자의 재동결·새 상태 규칙의 승인은 범위 밖이다.

## 바이트 동결 대조

| path | bytes | SHA256 |
|---|---:|---|
| output/260911/rev/260911_04_info_ab50_repair_spec.md | 15649 | 8ee9a46ecbd57ae9826bdf1c8f1b7a93939fa4ce500645421b0e86d309b64249 |
| output/260911/rev/260911_03_info_ab50_ruler_ruling.md | 68935 | ff129cc5ce45487671ba1f2626237950dccb3f2d57828729906c5dcb66edb8b1 |
| analysis/catalog/DIFFICULTY_RUBRIC.md | 20921 | 07dab5d38c8da48a22ca01d2f4c2b75d71fdd421a6da5ad3fcdd1a3b81b1ad99 |
| tools/measure_score_bands.py | 21969 | 0cf91284e2c1f7b1be4d94a09d641996614d65fa88fdf8444b9f9daa3958fe24 |
| tools/regen_rubric_values.py | 21594 | 599fbdef489fa1475dfba5dad76c3cd7eb0b133150359902c1b0590aa9ae11d1 |

原 inventory는 **60유닛**, 해시 대상은 transcript/meta **120파일**이다. 60파일이라고 혼동하지 않는다. 원천 디렉터리 집합과 명세 집합을 직접 대조했고 duplicates/missing/extra는 각각 빈 목록, 120파일의 bytes·SHA256 불일치도 빈 목록이었다. 이는 바이트 보존 확인이며 원천 내용의 정확성·문항 전수검증·통계 적격성 승인이 아니다. 보호 기준 세 파일의 현재 해시는 선행 판정 표와 일치했다.

재현 명령(PowerShell에서 Python 실행; 읽기 전용):

```powershell
@'
from pathlib import Path
from hashlib import sha256
import json
p=Path('output/260911/rev/260911_04_info_ab50_repair_spec.md')
rows=[[c.strip() for c in l.strip('|').split('|')] for l in p.read_text(encoding='utf-8').splitlines() if l.startswith('| EX-')]
expected=[r[0] for r in rows]
observed=sorted(x.name for x in Path('corpus').glob('EX-*') if x.is_dir())
bad=[]
for uid,tb,th,mb,mh in rows:
    for name,size,h in [('transcript.md',tb,th),('meta.yml',mb,mh)]:
        f=Path('corpus')/uid/name
        if not f.exists():
            bad.append(str(f)); continue
        b=f.read_bytes()
        if len(b)!=int(size) or sha256(b).hexdigest()!=h: bad.append(str(f))
print(json.dumps(dict(expected=expected,observed=observed,duplicates=sorted({u for u in expected if expected.count(u)>1}),missing=sorted(set(expected)-set(observed)),extra=sorted(set(observed)-set(expected)),files_checked=len(rows)*2,mismatches=bad)))
'@ | python -
Get-Content -Encoding UTF8 output/260911/rev/260911_04_info_ab50_repair_spec.md | Select-Object -First 50
Get-Content -Encoding UTF8 output/260911/rev/260911_03_info_ab50_ruler_ruling.md | Select-Object -Skip 541 -First 60
```

이번 읽기·해시 대조 명령 exit 0. 해시 대조 경고 0. 기존 measure/regen/assurance 게이트는 이번에 실행하지 않았고 그 성공을 주장하지 않는다. 선행 판정의 실패 수치는 새로운 실행값으로 인용하지 않는다.

# §2 unit별 판정

## Q2: revise-required — 계약 작성과 계약 판정을 분리한다

명세 §2는 원천 검사·통계 적격성·역사 면제·배포 적격성을 분리한다. 그러나 표 뒤에서 적용 단계·분모·상태별 종료 코드를 독립 판정에서 확정하도록 남겼다. §5 첫 항목도 이를 미완료로 명시한다. 따라서 현 문서는 후보 방향이지 판정 가능한 구체 계약이 아니다.

기존 판정 §2 Q2는 전역 미통과 유지 또는 별도 명시 계약의 선택을 요구하며, Q4는 기대 출력의 변경에 두 키를 요구한다. 판정자가 지금 새 처리표를 직접 작성하고 같은 응답에서 독립 승인하면 작성·감사 분리를 위반한다. 그렇다고 전역 경고를 그대로 두면서 새로운 성공을 주장할 수도 없다.

- [ ] **BF1 — 명세 소유자가 상태계약을 완성한다.** §2에서 미확정이라고 적은 적용 단계·유닛/분모·상태별 종료 코드·잔여 FAIL 표시·재검증 조건을 명시한다. 기존 규약 유지 부분과 변경 요청 부분을 구분하고, 변경 요청은 사용자 선택 및 별도 독립 판정 대상으로 표시한다. 원천 검사 실패, 부분 통계 사용, 역사적 부분 활용 허용, 배포 가능 여부를 하나의 PASS로 합치지 않는다. 본 판정은 어떤 경고의 면제도 승인하지 않는다.

이 요구는 새 검출기를 추가하는 것이 아니라 이미 명세와 선행 판정이 요구한 계약을 채우는 것이다. 알려진 사례는 명세 §2의 부분 자료/선언 불일치와 별도 중복 후보·합계축 미확인이다. 아직 제시되지 않은 새 규칙을 반박하거나 전수 통과를 인증하지 않았으므로 최소 수리·폐쇄 성과도 주장하지 않는다. 계약 작성 후에는 새 규칙의 전체 모집단 적용 결과와 잔여 목록이 필요하며, 이번 120파일 해시 대조로 대체할 수 없다.

# §3 follow-up (비차단)

Q1 구현 diff·fixture 검증, Q3 정보 구조 기반 난이도 기준, 문항 파일럿/전수 재검증은 기존 미결이며 이번에 새 차단 조건으로 늘리지 않는다. 명세 작성 승인과 구체 자 변경 승인은 구별한다. 배포 요청 자체를 다시 승인받으라고 요구하지 않는다.

# §4 open units (남은 집합)

| unit | 상태 | 다음 행위 |
|---|---|---|
| Q2 상태계약 | revise-required | 소유자가 BF1을 반영한 구체 계약 작성 → 변경되는 정책의 사용자 키 확인 → 별도 Astra 판정 |
| Q1 구현 | blocked 유지 | Q2 계약 확정 후 최소 diff·회귀 증거의 독립 승인 |
| Q3 난이도 기준 | 미결 유지 | 기존 별도 기준 결정 절차 수행 |
| A/B50 배포 | blocked 유지 | 위 기준 및 문항별 독립검증·최종 승인 후 배포 |

판정 단계는 여기서 종료한다. 이 판정 컨텍스트가 명세를 직접 고치고 자기 승인하지 않는다. 보호 기준·코드·문항 수정 승인 파일은 없다.

## history

- 2026-09-11: Codex/OMX, 호스트 확인 gpt-6-astra/medium, 별도 컨텍스트에서 Q2 완결성 한정 판정. 원천 60유닛/120파일 해시 대조 완료. BF1 한 건, 기준 반영·배포 blocked 유지.
