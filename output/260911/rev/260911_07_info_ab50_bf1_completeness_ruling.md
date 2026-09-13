---
title: 정보 A/B50 BF1 보완안 명세 완결성 판정
created: 2026-09-11
author: Codex/OMX (별도 컨텍스트 직접 판정)
responsibility: BF1 명세 완결성 한정
observed_model: gpt-6-astra
observed_reasoning_depth: medium
model_evidence: host-generated turn_context
independence: 새 컨텍스트; 보완안 작성에 참여하지 않음
grade: binding (명세 완결성 한정)
verdict: approve
repair_execution: blocked
release: blocked
---

# §0 판정 요약표

| unit | verdict | grade | evidence | measured | closure | note |
|---|---|---|---|---|---|---|
| BF1 보완안의 명세 완결성 | approve | binding (명세 완결성 한정) | output/260911/rev/260911_06_info_ab50_state_contract_spec.md:16-57; 선행 05 §2 BF1; 아래 재현 명령 | yes | 선행 BF1의 적용 단계·분모·종료 코드·잔여·재검증 조건 5/5 명시 확인. 새 규칙의 전 모집단 적용/폐쇄는 미실행이며 승인 범위 밖 | Q1 패치 후보 준비 가능. 정책 적용·코드 반영·배포 승인 아님 |

보완안은 선행 BF1이 요구한 구체 계약을 제시했다. **명세 완결성 BF1을 닫는다.** 변경 요청의 정당성·운영 적합성, 실제 구현의 검출력과 전수 폐쇄를 승인한 것은 아니다. 추가 binding fix는 없다.

# §1 독립 재검증

## 실행·입력 경계

- 호스트 thread: `01a090a2-73b2-7800-8f82-91ddfcc7a9d4`.
- 호스트 증거: `C:/Users/Park/.codex/sessions/2026/09/11/rollout-2026-09-11T22-22-40-01a090a2-73b2-7800-8f82-91ddfcc7a9d4.jsonl`의 `type=turn_context`, timestamp `2026-09-11T13:22:43.995Z`, model `gpt-6-astra`, effort `medium`을 직접 읽었다. 요청 모델·설정만으로 인증하지 않았다. 서버 라우팅 attestation은 주장하지 않는다.
- 이 컨텍스트는 보완안을 작성하지 않았다. 사용자 인계문을 시작 입력으로 받고 이번에 선행 판정과 명세를 읽었다. 과거 작성/판정 세션의 재사용이 아니다. 맹목 문항 풀이가 아닌 명세 검토다.
- 책임 지침 `.claude/agents/rev-arbiter.md`를 읽되 실제 실행자는 Codex/OMX다. 현재 모델 운영은 `docs/ASTRA_EXECUTION_POLICY.md`를 적용한다. 팀/서브에이전트 발주 없음.
- 허용 입력: 아래 해시 목록의 문서, 원천 inventory 바이트, 현재 호스트의 turn_context. 규약은 관련 절, 03은 Q1–Q4 관련 절, 원장은 말미, 도구는 관련 구현을 읽었다. 해시만 읽은 보호 파일을 전문 검토했다고 주장하지 않는다.
- 금지: 보완안·선행 판정·원천·코드·기준·문항·타인 WIP 수정. A/B 문제/답지는 읽지 않았고 문항 검증을 하지 않았다.
- 쓰기: 본 판정문, 이번 전용 WIP, REV_LOG 한 행만. 기존 사용자 변경은 보존한다.
- 인계문은 정식 패킷의 모든 필드를 갖추지 않았다. 명시된 다음 단계와 06 §5의 첫 요청인 **명세 완결성**만 처리하며 두 번째 요청의 사용자/감사키와 Q1/Q3/배포를 판정하지 않는다.

## 입력 바이트 측정

| path | bytes | SHA256 |
|---|---:|---|
| output/260911/rev/260911_06_info_ab50_state_contract_spec.md | 8389 | 93f75d1a4c0fc6af7df62dbf7e4b3799a62fa5e8ed74b0cb9cc6d87caf7aca22 |
| output/260911/rev/260911_05_info_ab50_state_contract_ruling.md | 9008 | e390779e99dbf6b066a03f03a5b073af851ba7e382808ebd5f3c797adb214d95 |
| output/260911/rev/260911_04_info_ab50_repair_spec.md | 15649 | 8ee9a46ecbd57ae9826bdf1c8f1b7a93939fa4ce500645421b0e86d309b64249 |
| output/260911/rev/260911_03_info_ab50_ruler_ruling.md | 68935 | ff129cc5ce45487671ba1f2626237950dccb3f2d57828729906c5dcb66edb8b1 |
| analysis/catalog/DIFFICULTY_RUBRIC.md | 20921 | 07dab5d38c8da48a22ca01d2f4c2b75d71fdd421a6da5ad3fcdd1a3b81b1ad99 |
| tools/measure_score_bands.py | 21969 | 0cf91284e2c1f7b1be4d94a09d641996614d65fa88fdf8444b9f9daa3958fe24 |
| tools/regen_rubric_values.py | 21594 | 599fbdef489fa1475dfba5dad76c3cd7eb0b133150359902c1b0590aa9ae11d1 |
| docs/ASTRA_EXECUTION_POLICY.md | 2901 | 760b9dc375712f27d93aaf36b58b521f47603800669bbc3e7b8274c5b1ee5082 |
| .claude/agents/rev-arbiter.md | 9239 | c7168c5eca9c56d6150044ca8b0f5a28526d6930048da74e8a059068b4eeb283 |
| CLAUDE.md | 45832 | b8adc4e7c7e56f1e57027eb66d3920f8ef202a0c61411b9838d60e1d34465928 |
| docs/DATA_STANDARD.md | 27062 | 315c621ba02466561088e1e6d1276218311569218d52caa39e1e9faad2ee35b5 |
| analysis/REV_GUIDE.md | 48947 | 371f3963c239d6463320c5cdde5a14f8b811493d33ed403c7e4413a88bca5ffb |
| tools/textpatch.py | 12170 | eaa4e9b8ff67b87f07a214c37aa5cddf8f027756e977ddf93828e71bacf1cb48 |
| analysis/REV_LOG.md | 245159 | 9baf3caf64ffaa9e7eecee13595214d196188f838c8d6f395f7404c9b581e349 |
| analysis/wip/rev-arbiter_260911_info_ab50_state_contract.md | 1415 | 372afc51bb069d0b53b83acc6369146249c0fb0296cf5de6230f6929a0927e6f |

원천 비교: 스냅숏 기대 유닛과 현재 EX 디렉터리를 양방향 대조하고 transcript/meta 바이트를 각각 확인했다. 결과 60유닛/120파일 일치, 보호 파일 3/3은 선행 05 해시와 일치했다. **원천 내용·문항 ID 완전성 승인이 아니다.** 문항 기준 expected/observed 대조는 후속 구현/문항 감사에서 별도로 수행해야 한다.

실행 출력:
```json
{
  "expected": [
    "EX-english-20241F",
    "EX-english-20241M",
    "EX-english-20242F",
    "EX-english-20242M",
    "EX-english-20251F",
    "EX-english-20251M",
    "EX-english-20252F",
    "EX-english-20252M",
    "EX-english-20261F",
    "EX-english-20261M",
    "EX-history-20241F",
    "EX-history-20241M",
    "EX-history-20242F",
    "EX-history-20242M",
    "EX-history-20251F",
    "EX-history-20251M",
    "EX-history-20252F",
    "EX-history-20252M",
    "EX-history-20261F",
    "EX-history-20261M",
    "EX-info-20252F",
    "EX-info-20252M",
    "EX-korean-20241F",
    "EX-korean-20241M",
    "EX-korean-20242F",
    "EX-korean-20242M",
    "EX-korean-20251F",
    "EX-korean-20251M",
    "EX-korean-20252F",
    "EX-korean-20252M",
    "EX-math1-20241F",
    "EX-math1-20241M",
    "EX-math1-20242F",
    "EX-math1-20242M",
    "EX-math1-20251F",
    "EX-math1-20251M",
    "EX-math1-20261F",
    "EX-math1-20261M",
    "EX-math2-20252F",
    "EX-math2-20252M",
    "EX-science-20241F",
    "EX-science-20241M",
    "EX-science-20242F",
    "EX-science-20242M",
    "EX-science-20251F",
    "EX-science-20251M",
    "EX-science-20252F",
    "EX-science-20252M",
    "EX-science-20261F",
    "EX-science-20261M",
    "EX-social-20241F",
    "EX-social-20241M",
    "EX-social-20242F",
    "EX-social-20242M",
    "EX-social-20251F",
    "EX-social-20251M",
    "EX-social-20252F",
    "EX-social-20252M",
    "EX-social-20261F",
    "EX-social-20261M"
  ],
  "observed": [
    "EX-english-20241F",
    "EX-english-20241M",
    "EX-english-20242F",
    "EX-english-20242M",
    "EX-english-20251F",
    "EX-english-20251M",
    "EX-english-20252F",
    "EX-english-20252M",
    "EX-english-20261F",
    "EX-english-20261M",
    "EX-history-20241F",
    "EX-history-20241M",
    "EX-history-20242F",
    "EX-history-20242M",
    "EX-history-20251F",
    "EX-history-20251M",
    "EX-history-20252F",
    "EX-history-20252M",
    "EX-history-20261F",
    "EX-history-20261M",
    "EX-info-20252F",
    "EX-info-20252M",
    "EX-korean-20241F",
    "EX-korean-20241M",
    "EX-korean-20242F",
    "EX-korean-20242M",
    "EX-korean-20251F",
    "EX-korean-20251M",
    "EX-korean-20252F",
    "EX-korean-20252M",
    "EX-math1-20241F",
    "EX-math1-20241M",
    "EX-math1-20242F",
    "EX-math1-20242M",
    "EX-math1-20251F",
    "EX-math1-20251M",
    "EX-math1-20261F",
    "EX-math1-20261M",
    "EX-math2-20252F",
    "EX-math2-20252M",
    "EX-science-20241F",
    "EX-science-20241M",
    "EX-science-20242F",
    "EX-science-20242M",
    "EX-science-20251F",
    "EX-science-20251M",
    "EX-science-20252F",
    "EX-science-20252M",
    "EX-science-20261F",
    "EX-science-20261M",
    "EX-social-20241F",
    "EX-social-20241M",
    "EX-social-20242F",
    "EX-social-20242M",
    "EX-social-20251F",
    "EX-social-20251M",
    "EX-social-20252F",
    "EX-social-20252M",
    "EX-social-20261F",
    "EX-social-20261M"
  ],
  "duplicates": [],
  "missing": [],
  "extra": [],
  "files_checked": 120,
  "mismatches": [],
  "protected_matches": [
    "analysis/catalog/DIFFICULTY_RUBRIC.md",
    "tools/measure_score_bands.py",
    "tools/regen_rubric_values.py"
  ]
}
```

재현 명령(읽기 전용; PowerShell):
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
  if not f.exists(): bad.append(str(f)); continue
  b=f.read_bytes()
  if len(b)!=int(size) or sha256(b).hexdigest()!=h: bad.append(str(f))
r=dict(expected=expected,observed=observed,duplicates=sorted({u for u in expected if expected.count(u)>1}),missing=sorted(set(expected)-set(observed)),extra=sorted(set(observed)-set(expected)),files_checked=len(rows)*2,mismatches=bad)
print(json.dumps(r))
assert not(r['duplicates'] or r['missing'] or r['extra'] or bad)
'@ | python -
rg -n '^##|contract_exit|원천 FAIL|두 키|미실행' output/260911/rev/260911_06_info_ab50_state_contract_spec.md
rg -n 'duplicate|warning|WARN|sys.exit|return 1|return 0' tools/measure_score_bands.py
```

원천/보호 바이트 검사는 exit 0, `BYTE_CHECK: PASS; warnings=0`. 명세/소스 조회도 exit 0. 최초 git status는 전역 ignore 경로 읽기 권한 경고를 냈으며 게이트 성공 증거로 사용하지 않는다. measure/regen/assurance 본 실행, 회귀 테스트·lint·typecheck는 미실행(제품 수정 없는 명세 판정). 과거 게이트 결과를 신규 성공으로 인용하지 않는다.

# §2 unit별 판정

## BF1 — approve (완결성 한정)

| 선행 요구 | 이번 보완안 근거 | 판정 이유 |
|---|---|---|
| 적용 단계 | 06 §2 | 입력 동결부터 배포까지 구별하고 각 단계 산출 의미를 명시했다. |
| 분모 | 06 §2 | 인쇄/추출 ID, 선택형/서답형, 관측/전체 및 A/B 집합을 구분한다. 확인 불가를 가상 0으로 채우지 않는다. |
| 종료 코드 | 06 §3 | 현행 하위 종료 코드를 보존하고 후보 contract_exit 0/1/2 및 합성 우선순위를 명시했다. 미실행을 성공 처리하지 않는다. |
| 잔여 FAIL | 06 §3–4 | 부분 자료·미확정·경고·역사적 허용을 전역 성공으로 합치지 않으며 잔여 목록과 근거를 요구한다. |
| 재검증 조건 | 06 §4–5 | 원천/파서 변경 후 전 모집단 검사, fixture와 정확한 diff, 기준 변경 후 stale·독립 재검증을 남겼다. |

06 §3의 현행 중복 warning-only 서술은 측정기 228–229행 및 374–376행과 부합한다. `contract_exit`는 **향후 변경 요청**으로 분리돼 있어 현행 도구가 이미 구현했다는 허위 주장이 아니다. 06 §1·§5는 전역 실패 유지와 두 키를 명시하므로 본 판정자가 새 계약을 작성해 자기 승인할 필요가 없어졌다.

이번에는 새로운 규칙·임계값을 제안/반박하거나 모집단 적격성을 승인하지 않는다. 따라서 바이트 일치를 새 규칙의 폐쇄 결과로 사용하지 않는다. **06의 모든 정책/구현 선택이 타당하다는 포괄 승인으로 확대하면 이 판정 범위를 벗어난다.**

# §3 follow-up (비차단)

추가 명세 재작성 요구 없음. 기존 Q1 단계에서 하위 경고/실패 전파, 정상/결함 fixture, 정확한 패치 및 전수 잔여를 검사한다. 근거 미확정과 실행 불가 상태가 구현에서 섞이지 않는지도 해당 fixture로 확인한다. 이는 새 BF가 아니라 이미 06 §3–4에 명시된 후속 검증이다.

# §4 open units (남은 집합)

| unit | 상태 | 다음 행위 |
|---|---|---|
| BF1 명세 완결성 | closed — approve | 동일 보완안을 다시 작성할 필요 없음 |
| Q2 정책 적용 | blocked | 06의 contract_exit 추가/전파에 대한 사용자 키 및 별도 감사키 확인; 완결성 승인과 구별 |
| Q1 구현 | blocked (반영) | 명세 소유자가 최소 diff·fixture 후보 준비 → 독립 패치 판정 → 두 키 범위만 반영/재동결 |
| Q3 난이도 기준 | 미결 유지 | 원천/경계 사례와 별도 기준 서명 |
| A/B50 배포 | ▲ blocked | 원본 ID 기준 전수 독립 검증·수정 후 재검증·최종 배포 판정 |

이 판정 컨텍스트는 후속 패치의 작성자가 되지 않는다. 배포 요청 자체의 재승인은 요구하지 않는다. 신규 정책의 사용자 키를 기존 배포 요청에서 추정하지 않는다.

## history

- 2026-09-11: Codex/OMX, 호스트 확인 gpt-6-astra/medium. 별도 컨텍스트에서 BF1 명세 완결성 approve. 원천 60유닛/120파일·보호 파일 3종 바이트 대조 완료. 정책 적용·코드 반영·문항 검증·배포 승인 없음.

