---
title: 정보 A/B50 배포 선행 기준 수리 독립 판정
created: 2026-09-11
author: Codex/OMX (새 컨텍스트 직접 판정)
responsibility: 기준 수리 판정 — 문항 맹목 풀이 아님
observed_model: gpt-6-astra
observed_reasoning_depth: medium
model_evidence: host-generated turn_context
grade: binding (판정 범위 한정; 사용자 키·반영 승인·배포 승인 아님)
verdict: revise-required
repair_execution: blocked
release: blocked
write_surface: output/260911/rev/260911_03_info_ab50_ruler_ruling.md
---

# §0 판정 요약표

| unit | verdict | grade | evidence | measured | closure | note |
|---|---|---|---|---|---|---|
| Q1 모집단·계층 계약 | revise-required | binding | §1-C/D 직접 실행; `tools/regen_rubric_values.py` derive; 루브릭 §1·§1-3 | yes | 원천 유닛 60/60; 계층 6/6 차집합·중복 0; 메모리 최소 수리 뒤에도 A축 33건 | 고정 4행 유지로 현재 모집단을 표현할 수 없다. 원본 파생 집합 재서명 방향 채택. 사용자 키 미충족으로 반영은 blocked |
| Q2 partial 면제의 효력 | approve | binding (경계 확인) | Cycle1 F 판정 §2 F2; 해당 meta·전사·verify_log; 측정기 재실행 | yes | 해당 유닛 1/1: 선언 선택형 24, 추출 15; FAIL 유지; 면제의 전역 PASS 전환 0건 승인 | 기존 면제는 해당 유닛 S3 부분 투입에 한정. 전역 기준 게이트는 여전히 blocked |
| Q3 정보 서답형 Tier·T4 | revise-required | binding | 루브릭 §1·§3·§4; 260911_01 §2 Q5·§4; A/B 문제지 머리말 | yes | A/B 식별자 50/50만 확인; 난이도·추가 사고력 전수 판정은 이번에 하지 않음 | 별도 정보 난이도 자 결정 필요. 미서명을 PASS·임의 T4·목표 하향으로 해소하지 않는다 |
| Q4 범위·two-key·stale | approve | binding (절차·금지 범위만) | `analysis/REV_GUIDE.md` §5·§5-a; `CLAUDE.md` 원칙 12; §1 재현 | yes | 수정 승인 파일 0개; 3개 명령 모두 미통과; 요청 동결 9/9 일치 | 수리 방향과 필요한 절차 확정. 두 키 완성·수리 완료·A/B50 배포는 승인하지 않음 |

**종합: revise-required / 기준 반영 및 A/B50 배포 ▲ blocked.** 새 기준 수치나 면제 정책에 대한 사용자 키는 없다. 사용자의 이번 수행 요청은 이 판정 절차와 회신 1개 작성의 권한이다. 요청서·기존 보고서의 승인 표현이나 과거 원장 자기 신고를 새로운 사용자 선택으로 대체하지 않는다.

# §1 독립 재검증

## A. 모델·컨텍스트·권한

- 실제 실행 표면: Codex/OMX 본체 직접. 팀·서브에이전트·외부 세션 발주 0.
- 호스트 세션: `01a0907a-7ccc-7e23-8c16-31dbfac8ac11`. 호스트의 현재 turn 기록은 `model=gpt-6-astra`, `effort=medium`이다. high/xhigh라고 상향 표시하지 않는다.
- 확인 경로: `C:\Users\Park\.codex\sessions\2026\09\11\rollout-2026-09-11T21-39-01-01a0907a-7ccc-7e23-8c16-31dbfac8ac11.jsonl`.
- `CODEX_THREAD_ID` 환경값으로 현재 파일을 좁힌 뒤, 그 파일의 호스트 생성 `session_meta`와 `turn_context`만 추출했다. 환경값 자체는 모델 증거가 아니다. 설정 파일, 에이전트 TOML, 요청 모델명은 실행 증거로 사용하지 않았다.
- 독립성 근거: 현재 호스트 기록의 새 CLI 세션·단일 turn_context, compacted 기록 0; 이 대화에는 작성 과정이나 선행 검토의 수행 이력이 없고 사용자로부터 이번 결정요청을 받았다. 기존 판정문은 이 판정 단계에서 읽은 입력이다. 그 자체가 이 작업을 맹목 풀이로 만들지는 않는다.
- 한계: 파일 접근 격리·이전 세션 전체와의 독립성을 암호학적으로 증명하는 호스트 attestation은 제공되지 않았다. 호스트 로그는 실행 메타데이터이지 서버 내부 라우팅의 별도 서명 증명은 아니다. 이를 넘어선 보장은 주장하지 않는다. 호스트 기록이 없거나 모델이 달랐다면 인증된 Astra 판정을 작성하지 않고 blocked 처리했을 것이다.
- `.claude/agents/rev-arbiter.md`는 판정 책임·절차 참고로만 적용했다. 실제 배우는 Claude Code Opus가 아니다. Astra 정책과 이번 사용자의 직접 수행·단일 파일 쓰기 제한을 우선했다. REV_LOG·WIP·OMX 상태 파일에 별도 기록하지 않는다.
- 허용 입력: 요청서·지침·동결 9파일 및 쟁점의 직접 원천·선행 판정·현재 문제지 식별자/메타. 금지 실행: 생성·revision·selfcheck를 이용한 제품 변경, 문항 맹목 풀이 발주, 기준/공유 원장/타인 WIP 수정. WIP 내용은 판정 증거로 삼지 않았다. assurance 도구가 WIP 메타를 읽고 출력한 실패는 **도구의 현재 실패 현상**만 증명한다.

호스트 기록의 원본 레코드 해시(개행 포함; 늘어나는 로그 전체를 불변 입력처럼 동결하지 않음):

```json
[
  {
    "type": "session_meta",
    "timestamp": "2026-09-11T12:39:05.236Z",
    "bytes": 52537,
    "sha256": "6d1207e135a90536bc0d2926232814a8137c2d153987b0fd37eea98929292189",
    "fields": {
      "id": "01a0907a-7ccc-7e23-8c16-31dbfac8ac11",
      "cwd": "C:\\dev\\study",
      "source": "cli",
      "originator": "codex-tui",
      "cli_version": "0.154.0",
      "model_provider": "openai"
    }
  },
  {
    "type": "turn_context",
    "timestamp": "2026-09-11T12:39:06.215Z",
    "bytes": 3516,
    "sha256": "c75f41c135dd99877e84e56d7f3acb1b2db0a70f1fca1b216d32817d72089897",
    "fields": {
      "turn_id": "01a0907a-8ab8-7bb0-9173-ddbf4ccd566e",
      "cwd": "C:\\dev\\study",
      "model": "gpt-6-astra",
      "effort": "medium"
    }
  }
]
```

재현: 해당 JSONL의 각 JSON에서 `type in {"session_meta","turn_context"}`만 선택해 payload의 id/turn_id/cwd/model/effort를 읽고, 원본 행 바이트에 SHA256을 적용한다. `session_meta`에는 model 필드가 없고 실제 모델 증거는 **turn_context**에 있다.

## B. 직접 읽은 입력·동결 대조

필수 지침 6개를 읽었다. 아래 요청 동결 9파일도 직접 읽었다. 스크립트는 전 소스를, 두 선행 판정과 품질 보고서는 본문을 읽되 그 보고서에 들어 있는 과거 실행값·맹목 풀이 성과는 이번 승인 근거로 이월하지 않았다.

| path | 현재 bytes | 현재 SHA256 | 요청 동결 대조 |
|---|---:|---|---|
| `analysis/catalog/DIFFICULTY_RUBRIC.md` | 20921 | `07dab5d38c8da48a22ca01d2f4c2b75d71fdd421a6da5ad3fcdd1a3b81b1ad99` | bytes·SHA256 모두 일치 |
| `tools/measure_score_bands.py` | 21969 | `0cf91284e2c1f7b1be4d94a09d641996614d65fa88fdf8444b9f9daa3958fe24` | bytes·SHA256 모두 일치 |
| `tools/regen_rubric_values.py` | 21594 | `599fbdef489fa1475dfba5dad76c3cd7eb0b133150359902c1b0590aa9ae11d1` | bytes·SHA256 모두 일치 |
| `tools/check_assurance_contract.py` | 11648 | `45ed11661961ce1d7d46f5874db0d9b1b05ec724d577844bdf410228459c6802` | bytes·SHA256 모두 일치 |
| `output/260910/rev/260910_14_item_quality_audit.md` | 50910 | `bea97c7de546a707c55dcaa6d5621569e1d6fa516a1d99f9467ab0143002ab05` | bytes·SHA256 모두 일치 |
| `output/260911/rev/260911_01_info_v1_criterion_ruling.md` | 32195 | `61eb47788b53b2c5134e5723678a52ee8fb96dbed909967f5ae8aa9bb74a5fb3` | bytes·SHA256 모두 일치 |
| `output/260903/rev/260903_06_arbiter_ruling_cycle1_f.md` | 14321 | `6992e0faecda6fcf08609eac44b65c2de984686771f6f527125efedd4a61936b` | bytes·SHA256 모두 일치 |
| `docs/ASTRA_EXECUTION_POLICY.md` | 2901 | `760b9dc375712f27d93aaf36b58b521f47603800669bbc3e7b8274c5b1ee5082` | bytes·SHA256 모두 일치 |
| `analysis/REV_GUIDE.md` | 48947 | `371f3963c239d6463320c5cdde5a14f8b811493d33ed403c7e4413a88bca5ffb` | bytes·SHA256 모두 일치 |

원시 바이트 기준 **일치 9 / 불일치 0**. CRLF→LF 정규화로 바이트 일치를 위장하지 않았다. 품질 보고서는 CRLF 394개와 단독 LF 120개가 혼재하지만 그 상태 그대로 동결과 일치한다. 나머지 8개는 CRLF이며 단독 LF 0이다. 이 라운드에서 동결 불일치가 없으므로 내용 차이/개행 차이로 분류할 불일치도 없다. 품질 보고서가 별도로 주장한 info.md·output/_index.md의 과거 개행 비교는 이번 9파일 동결 판정과 다른 사건이며 승인 근거로 쓰지 않았다.

추가 원천 읽기 범위:
- 측정기와 메모리 진단이 `corpus/EX-*/transcript.md` 60개를 실제 읽고 배점·선언을 파싱했다. 이는 60개 전사본의 **기계적 전수 읽기**이지 60개 원본 이미지의 육안 전수 판독을 뜻하지 않는다.
- partial 유닛은 meta 전체, 전사 머리말/문항 머리·관련 절, verify_log를 읽어 기존 면제 기록을 대조했다. 이번에 스캔 여백의 물리 원인을 새로 판정하지 않는다.
- K1 및 M6/M7 선행 판정은 모집단·재서명·잔차 처리 관련 절을 읽었다. 선행 판정의 모든 문항 계산을 재감사한 것은 아니다.
- 현재 A/B 문제지는 머리말·식별자를 직접 확인했다. 정답지·통합본을 이번에 독립 재풀이/승인하지 않았다.
- `analysis/REV_LOG.md`는 관련 과거 행을 조회했으며 자체 신고를 승인 증거로 대체하지 않았다.
- `.claude/agents/item-quality-auditor.md` V1/V2/V4/A 정의를 직접 확인했다. 이번 기준 수리와 문항 감사는 별개다.

추가 읽은 파일의 바이트 해시는 아래 별표에 전부 기록한다. 선행 문서 속 간접 경로(과거 샌드박스, WIP, 구 세트, 이미지 등)는 이번 판정의 직접 증거가 아니며 새로 검증했다고 주장하지 않는다. 문서 속 주장 전부를 승인하는 직접경로 폐쇄가 아니라 **네 기준 쟁점의 원천을 위 범위로 한정**했다.

## C. 요청된 세 명령 — 이번 실행의 전체 출력

저장소 루트 `C:\dev\study`에서 각각 실행했다. 아래 exit는 각 프로세스가 반환한 값이며 셸 후속 명령·grep의 exit가 아니다. 경고 수는 출력 줄 중 `[WARN]`을 포함한 줄 수다. 기존 실패 수를 기대값으로 복사하지 않았다.

| 명령 | exit | [WARN] 줄 | 현재 결과 |
|---|---:|---:|---|
| `python tools/measure_score_bands.py` | 1 | 40 | 미통과 |
| `python tools/regen_rubric_values.py` | 1 | 0 | 미통과 |
| `python tools/check_assurance_contract.py` | 1 | 0 | 미통과 |

### `python tools/measure_score_bands.py`

```text
=== GATE 0 fixture: planted parser defects ===
planted=9 undetected=0
planted-state=6 undetected=0
[GATE 0 PASS] undetected=0
=== GATE 1 truth: reproduce tier-3 confirmed values ===
EX-english-20252M    [body       ] got n=27  sum=70.0    want n=27  sum=70.0    OK
EX-history-20252M    [body       ] got n=20  sum=40.0    want n=20  sum=40.0    OK
EX-info-20252F       [body       ] got n=18  sum=70.0    want n=18  sum=70.0    OK
EX-korean-20252M     [body       ] got n=29  sum=60.0    want n=29  sum=60.0    OK
EX-math1-20242M      [body+math0 ] got n=0   sum=0.0     want n=0   sum=0.0     OK
EX-math2-20252M      [body+math0 ] got n=0   sum=0.0     want n=0   sum=0.0     OK
EX-science-20242F    [body       ] got n=24  sum=80.0    want n=24  sum=80.0    OK
EX-science-20242M    [body       ] got n=24  sum=60.0    want n=24  sum=60.0    OK
EX-science-20252M    [index      ] got n=23  sum=60.0    want n=23  sum=60.0    OK
EX-social-20252M     [body       ] got n=20  sum=60.0    want n=20  sum=60.0    OK
checked=10 undetected=0 flagged=0 coverage=10/60
[GATE 1 PASS] undetected=0

=== GATE 2 dup: identical selective sequences ===
[WARN] identical selective sequence (n=18): EX-info-20252F == EX-info-20252M
duplicates=1 (warning only -- not excluded, see BF-K1-7a)
GATE 2 false-positive rate to date: 1/1 -- EX-info-20252M vs EX-info-20252F are different exams that reuse one score-allocation table (ruling 260831_04 U3-a). Treat every firing as a candidate, never as a verdict.

=== GATE 3 declared: printed declaration vs extraction ===
[WARN] EX-social-20261M     declared n=24  extracted n=15 
mismatches=1
--- GATE 3b sum-axis coverage (BF3) ---
[WARN] EX-english-20241F    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-english-20241M    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-english-20242F    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-english-20242M    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-english-20251F    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-english-20251M    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-english-20252F    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-english-20252M    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-history-20241F    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-history-20241M    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-history-20251F    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-history-20251M    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-history-20252F    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-history-20252M    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-history-20261F    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-history-20261M    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-korean-20241F     self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-korean-20241M     self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-korean-20242F     self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-korean-20242M     self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-korean-20251F     self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-korean-20251M     self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-korean-20252F     self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-korean-20252M     self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-science-20241F    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-science-20241M    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-science-20251F    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-science-20251M    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-science-20252F    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-science-20252M    self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-social-20241F     self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-social-20241M     self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-social-20251F     self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-social-20251M     self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-social-20252F     self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-social-20252M     self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-social-20261F     self-enumerated selective total not found -- sum axis UNCOVERED
[WARN] EX-social-20261M     self-enumerated selective total not found -- sum axis UNCOVERED
sum-axis coverage=12/50 uncovered=38 mismatches=0

excluded from aggregate: EX-social-20261M

=== selective-score distribution ===
unit                 T  mode      n  decl      sum       range      band  4.0+
EX-english-20241F    F  body     24    24     70.0     2.5~3.5   10/24       0
EX-english-20241M    M  body     26    26     70.0     2.3~3.4    6/26       0
EX-english-20242F    F  body     24    24     70.0     2.5~3.5   11/24       0
EX-english-20242M    M  body     24    24     70.0     2.5~3.5   10/24       0
EX-english-20251F    F  body     26    26     70.0     2.1~3.6    8/26       0
EX-english-20251M    M  body     23    23     70.0     2.2~3.6   16/23       0
EX-english-20252F    F  body     28    28     70.0     2.1~2.8    0/28       0
EX-english-20252M    M  body     27    27     70.0     2.2~3.3    4/27       0
EX-english-20261F    F  body     23    23     80.0     3.1~4.2   23/23       1
EX-english-20261M    M  body     22    22     60.0     2.1~3.7    6/22       0
EX-history-20241F    F  body     21    21     80.0     3.4~4.2   21/21       6
EX-history-20241M    M  body     25    25     60.0     2.2~2.8    0/25       0
EX-history-20242F    F  body     21    21     80.0     3.5~4.2   21/21       3
EX-history-20242M    M  body     24    24     60.0     2.3~2.7    0/24       0
EX-history-20251F    F  body     24    24     80.0     3.1~3.5   24/24       0
EX-history-20251M    M  body     25    25     60.0     2.2~2.6    0/25       0
EX-history-20252F    F  body     23    23     80.0     3.2~3.7   23/23       0
EX-history-20252M    M  body     20    20     40.0     1.8~2.2    0/20       0
EX-history-20261F    F  body     24    24     80.0     3.0~3.6   24/24       0
EX-history-20261M    M  body     25    25     60.0     2.2~2.5    0/25       0
EX-info-20252F       F  body     18    18     70.0     3.2~4.4   15/18      10
EX-info-20252M       M  body     18    18     70.0     3.2~4.4   15/18      10
EX-korean-20241F     F  body     24    24     80.0     3.0~3.7   24/24       0
EX-korean-20241M     M  body     24    24     60.0     2.2~2.8    0/24       0
EX-korean-20242F     F  body     24    24     80.0     3.0~3.6   24/24       0
EX-korean-20242M     M  body     24    24     60.0     2.2~2.8    0/24       0
EX-korean-20251F     F  body     26    26     80.0     2.0~4.0   18/26       1
EX-korean-20251M     M  body     24    24     60.0     1.7~3.3    7/24       0
EX-korean-20252F     F  body     25    25     80.0     2.3~4.0   18/25       1
EX-korean-20252M     M  body     29    29     60.0     1.2~2.8    0/29       0
EX-math1-20241F      F  body+math0    0     0        - no selective         -     -
EX-math1-20241M      M  body+math0    0     0        - no selective         -     -
EX-math1-20242F      F  body+math0    0     0        - no selective         -     -
EX-math1-20242M      M  body+math0    0     0        - no selective         -     -
EX-math1-20251F      F  body+math0    0     0        - no selective         -     -
EX-math1-20251M      M  body+math0    0     0        - no selective         -     -
EX-math1-20261F      F  body+math0    0     0        - no selective         -     -
EX-math1-20261M      M  body+math0    0     0        - no selective         -     -
EX-math2-20252F      F  body+math0    0     0        - no selective         -     -
EX-math2-20252M      M  body+math0    0     0        - no selective         -     -
EX-science-20241F    F  body     24    24     80.0     3.0~3.6   24/24       0
EX-science-20241M    M  body     24    24     60.0     2.2~2.8    0/24       0
EX-science-20242F    F  body     24    24     80.0     3.0~3.6   24/24       0
EX-science-20242M    M  body     24    24     60.0     2.2~2.8    0/24       0
EX-science-20251F    F  body     24    24     80.0     3.0~3.9   24/24       0
EX-science-20251M    M  body     24    24     60.0     2.3~2.7    0/24       0
EX-science-20252F    F  body     24    24     80.0     3.0~3.6   24/24       0
EX-science-20252M    M  index    23    23     60.0     2.2~3.2    2/23       0
EX-science-20261F    F  body     24    24     90.0     3.4~4.0   24/24       7
EX-science-20261M    M  body     24    24     90.0     3.4~4.0   24/24       7
EX-social-20241F     F  body     20    20     80.0     3.3~4.4   13/20      12
EX-social-20241M     M  body     24    24     60.0     2.3~2.8    0/24       0
EX-social-20242F     F  body     20    20     80.0     3.6~4.4   17/20      12
EX-social-20242M     M  body     24    24     60.0     2.0~2.9    0/24       0
EX-social-20251F     F  body     20    20     80.0     3.5~4.5   16/20      14
EX-social-20251M     M  body     20    20     60.0     2.6~3.3   12/20       0
EX-social-20252F     F  body     22    22     80.0     3.1~4.2   22/22       6
EX-social-20252M     M  body     20    20     60.0     2.7~3.3   13/20       0
EX-social-20261F     F  body     24    24     90.0     3.5~4.1   24/24       6
EX-social-20261M     M  body     15    24     55.3     3.5~4.0   15/15       2 EXCL

=== axis test: midterm(M) vs final(F) ===
T  units      n     band         pct   4.0+ sel_total_avg
M     24    567      115       20.3%     17        62.5
F     25    581      476       81.9%     79        78.8

mean unit price:  M=2.65  F=3.39

=== signed relative band  r in [0.80, 1.20] ===
ALL   n=1148  fit=1101 = 95.9%  residual=47

--- per stratum ---
F-2024   n=226  fit=226   100.0%
F-2025   n=260  fit=245    94.2%
F-2026   n=95   fit=94     98.9%
M-2024   n=243  fit=242    99.6%
M-2025   n=253  fit=227    89.7%
M-2026   n=71   fit=67     94.4%

--- per unit (residual > 0 only) ---
EX-english-20241M    n=26   residual=1
EX-english-20251F    n=26   residual=3
EX-english-20251M    n=23   residual=2
EX-english-20252M    n=27   residual=2
EX-english-20261F    n=23   residual=1
EX-english-20261M    n=22   residual=4
EX-korean-20251F     n=26   residual=8
EX-korean-20251M     n=24   residual=6
EX-korean-20252F     n=25   residual=4
EX-korean-20252M     n=29   residual=15
EX-science-20252M    n=23   residual=1

--- Tier conversion share ---
T1  [0.800,0.867)   48    4.2%
T2  [0.867,0.967)  365   31.8%
T3  [0.967,1.067)  460   40.1%
T4  [1.067,1.200]  228   19.9%
--  outside band        47    4.1%

[FAIL] GATE 3 mismatches=1 -- EX-social-20261M
       band figures above are usable but the run is NOT a pass. Locate the
       defect before naming an owner: a count/sum that lands exactly on the
       printed declaration once a parse rule is corrected is a parser defect
       (M2/M3, fixed 260902), not a transcription defect. M5 remains one --
       EX-science-20242F summary 78.8/21.2 vs enumerated 80.0/20.0.
```

### `python tools/regen_rubric_values.py`

```text
\uacc4\uce35 4\ud589 \uc5c6\uc74c: [('F-2024', '226', '226', '100.0'), ('F-2025', '260', '245', '94.2'), ('F-2026', '95', '94', '98.9'), ('M-2024', '243', '242', '99.6'), ('M-2025', '253', '227', '89.7'), ('M-2026', '71', '67', '94.4')]
```

### `python tools/check_assurance_contract.py`

```text
FAIL analysis/wip/260910_astra_fallback_policy_proposal.md: status 'pending' outside ['blocked', 'done', 'in-progress']
FAIL analysis/wip/260910_astra_fallback_policy_proposal.md: no NEXT: line — cannot be resumed
FAIL analysis/wip/260910_info_astra_pilot_questions.md: no status: field (CLAUDE.md 규격 ②)
FAIL analysis/wip/260910_info_astra_pilot_questions.md: no NEXT: line — cannot be resumed
FAIL analysis/wip/mainloop_260907_info_onboarding.md: status 'active' outside ['blocked', 'done', 'in-progress']
FAIL analysis/wip/RESUME.md: no status: field (CLAUDE.md 규격 ②)
FAIL analysis/wip/RESUME.md: no NEXT: line — cannot be resumed
FAIL ruler gate: regen_rubric_values.py exit=1 (expected 0)
FAIL ruler gate: detector did not prove its own detection power (원칙 12-d)
FAIL ruler gate: ruler is stale -- ?
assurance-contract: 10 failure(s)
```


출력 보존 주의: regen stderr의 한글은 실행 환경에서 문자 그대로 `\\uacc4...`로 escape되어 나왔다. 위는 이를 임의로 치환하지 않은 도구 출력이다. 의미는 “계층 4행 없음”이다. 보고서 코드 펜스에서는 표시용 개행만 LF로 통일했다.

독립 해석:
1. measure의 경고 40 = 중복 후보 1 + partial 선언 불일치 1 + 합계축 uncovered 38. truth 앵커 10/60과 파서 fixture 9+6 통과는 전체 자료 검증 통과가 아니다.
2. regen은 derive의 고정 4계층 검사에서 끝나므로 공식 실행에서 자기 검출력·stale 수치가 **측정되지 않았다**. `check_assurance_contract`의 `stale -- ?`는 수치 0도 특정 stale 카운트도 아니다.
3. assurance 실패 10 = WIP 메타 검사에서 출력된 7 + ruler 게이트 3. 이 7을 면제하거나 소유자의 실제 NEXT를 추정해 고치지 않는다. WIP를 기준 판정 근거로 인용하지 않는다.
4. 경고 0인 두 실패 명령을 PASS로 오독하지 않는다. 모든 게이트는 기대 출력·카운트·exit·경고를 함께 만족해야 한다.

## D. 원천 모집단·최소 수리의 전수 실험

**실험은 메모리에서만 수행했다.** 기준 파일은 수정하지 않았으며 공식 수리 실행이나 새 정본이 아니다. 원본에서 읽은 현재 측정 결과를 유지하고, derive의 “4행인가” 검사만 **원천 ID에서 얻은 계층 집합과 정확히 같은가·중복 없는가·합이 같은가**로 바꾼 진단이다. 변경 전후 입력 바이트는 별표 해시로 고정한다.

원천 목록은 `corpus/EX-*/transcript.md` 직접 열거다. 기대 계층은 그 ID에서 과목·연도·학기·M/F를 파싱해 수학의 선택형 비적용을 구분하고 만들었다. 출력의 계층 목록을 기대 목록으로 복사하지 않았다. 이 현재 목록은 차후 승인된 source manifest와 재대조해야 하며 “디렉터리에 새 파일이 있으면 무조건 자동 승인”하는 계약이 아니다.

- 원천 유닛 60, 측정 행 60, 누락·추가·중복 각 0.
- 선택형 보유 50, 선택형 비적용 10, 현재 집계 포함 49, 제외 1(`EX-social-20261M`). **보유 50과 집계 49는 다르다.**
- 현재 선택형 집계 1148문항, 밴드 내 1101, 밖 47. 이 값은 **현행 실패 실행의 관측값**이지 서명된 새 기대값이 아니다.
- 기대/관측 계층:
```json
{
  "expected": [
    "F-2024",
    "F-2025",
    "F-2026",
    "M-2024",
    "M-2025",
    "M-2026"
  ],
  "observed": [
    [
      "F-2024",
      "226",
      "226",
      "100.0"
    ],
    [
      "F-2025",
      "260",
      "245",
      "94.2"
    ],
    [
      "F-2026",
      "95",
      "94",
      "98.9"
    ],
    [
      "M-2024",
      "243",
      "242",
      "99.6"
    ],
    [
      "M-2025",
      "253",
      "227",
      "89.7"
    ],
    [
      "M-2026",
      "71",
      "67",
      "94.4"
    ]
  ],
  "missing": [],
  "duplicates": [],
  "extra": []
}
```
- 계층·연도 합: 2024=469/468, 2025=513/472, 2026=166/161 (분모/밴드 내); 합 1148/1101로 ALL과 일치. 연도별 비율 99.8%, 92.0%, 97.0%; 최저 92.0%. 개별 계층 최저는 M-2025 89.7%. 원천·계층 차집합 잔여 **0/60 유닛, 0/6 계층**.
- 2024·2025 **두 학기 모두**만 진단적으로 분리하면 선택형 42유닛 982/940이다. 같은 연도의 **2학기만**이면 22유닛 510/488이다. 따라서 현 루브릭의 “2024·2025 2학기 42유닛 982문항”은 범위 라벨과 수치가 일치하지 않는다. 단순히 2026 두 계층만 추가하거나 4를 6으로 고쳐서는 이 라벨 결함이 닫히지 않는다.
- 위 과거 범위 분리는 비교용이다. 실패 유닛이나 2026 자료를 정본 집계에서 임의 제외하는 패치가 아니다.

### 메모리 최소 수리 결과와 남은 경계

고정 계층 검사만 대체한 derive는 6/6 계층을 받아들이고 연도 합을 검증했다. 기존 regen gate0도 `planted=11 undetected=0`, 반환 0. 그러나 현 루브릭과 대조하면 **A축 33, B축 0, C축 잔차 61, stale 자리 61/35행, 역할 사각 18**이 관측됐다. 이는 **메모리 진단 결과**이며 공식 regen의 출력으로 표시하지 않는다.

특히 derive의 `units_sel`은 `no selective`가 아닌 모든 행을 세므로 EXCL도 포함한다. 그 값 50을 “집계 유닛”으로 쓰면 실제 49와 어긋난다. 그러므로 관측 보유·적격 집계·제외를 별도 값으로 생성해야 한다. 자의 문면 역할을 정하지 않은 채 `42→50` 지시를 그대로 반영하는 것은 허용하지 않는다.

역할 사각 18개가 독립 결함 18개로 확정된 것도 아니다. `moved_literals(txt,v)`는 검사 대상 텍스트에서 이동 리터럴을 추출한다. A축 인용이 고쳐지면 잔차 모집단 자체가 달라질 수 있다. 역사적 예시·단원번호·독립 목표 분포까지 숫자를 치환하거나, 18개를 핑계로 ALLOW를 일괄 확장하지 않는다. 실제 반영 후 다시 측정해 남는 자리만 역할별로 판정해야 한다. 과거 원장 L144의 “잔차가 사라졌다”는 자기 신고를 이번 잔차 해소 증거로 쓰지 않았다.

또한 regen은 측정기 반환값을 `code`로 읽고 표시하지만 마지막 반환은 `keys or a or b`만 본다. measure의 exit 1·경고 40을 전파하는 조건이 없다. 현재는 4계층 검사 때문에 앞에서 막혀 있을 뿐이다. 계층 수리 후에도 **measure 실패를 regen의 통과로 세탁하지 못하게 하는 검증**이 필요하다. checker 구조6도 regen을 실행할 뿐 measure 결과를 별도로 검사하지 않는다. 따라서 §5-a의 두 명령을 각각 실행해야 한다.

### 결함 주입 — 정본 무변경

현재 6계층을 정상 입력으로 두고 메모리에서 다음 5개 변이만 만들었다. 새 검사와 기존 실제 실패의 연결: 고정 행 수가 실제 원천 6계층을 거부한 사건 및 행 수만 맞춰 누락을 숨길 수 있는 동일 종류의 실패다.

```json
{
  "clean": {
    "missing": [],
    "extra": [],
    "duplicates": [],
    "sum_ok": true
  },
  "missing": {
    "missing": [
      "F-2024"
    ],
    "extra": [],
    "duplicates": [],
    "sum_ok": false
  },
  "duplicate": {
    "missing": [],
    "extra": [],
    "duplicates": [
      "F-2024"
    ],
    "sum_ok": false
  },
  "extra": {
    "missing": [],
    "extra": [
      "F-2099"
    ],
    "duplicates": [],
    "sum_ok": false
  },
  "same-count-missing-plus-duplicate": {
    "missing": [
      "F-2024"
    ],
    "extra": [],
    "duplicates": [
      "F-2025"
    ],
    "sum_ok": false
  },
  "sum-fit-minus-one": {
    "missing": [],
    "extra": [],
    "duplicates": [],
    "sum_ok": false
  }
}
```

정상 1/1 수용, 결함 5/5 검출, 미검출 0. 누락+다른 계층 중복은 행 수가 6으로 같아도 검출된다. 이 실험은 유닛 원천 자체 삭제, 각 필드 파싱 오류, 경고 전파까지 다 덮는 배포용 회귀 suite가 아니다. 그 추가 요구는 §2 Q1의 실제 계약 수리 검증으로 구분한다.

### 재현 명령 (진단 전용, write 0)

아래는 이번에 실행한 메모리 실험이다. `audit`의 기준은 원천에서 파생된다. 기존 파일의 AST는 메모리에서만 다루며 `main()`을 새 정본인 것처럼 실행하지 않는다.

```powershell
@'
import ast, pathlib, io, contextlib, sys, re, json, hashlib
from collections import Counter
from fractions import Fraction
sys.dont_write_bytecode=True
ns={'__name__':'__ruler_diagnostic__'}
buf=io.StringIO()
with contextlib.redirect_stdout(buf):
 try: exec(compile(pathlib.Path('tools/measure_score_bands.py').read_text(encoding='utf-8'),'tools/measure_score_bands.py','exec'),ns)
 except SystemExit as e: measure_exit=e.code
rows=ns['rows']; strata=ns['strat']; out=buf.getvalue()
source_ids=[p.parent.name for p in sorted(pathlib.Path('corpus').glob('EX-*/transcript.md'))]
observed_ids=[r[0] for r in rows]
strata_expected=sorted(set(re.fullmatch(r'EX-[a-z0-9]+-(20[0-9]{2})[12]([MF])',uid).group(2)+'-'+re.fullmatch(r'EX-[a-z0-9]+-(20[0-9]{2})[12]([MF])',uid).group(1) for uid in source_ids if uid.split('-')[1] not in ('math1','math2')))
parsed=re.findall(r'^([FM]-\d{4})\s+n=(\d+)\s+fit=(\d+)\s+([\d.]+)%',out,re.M)
def audit(ss):
 names=[r[0] for r in ss]; counts=Counter(names)
 return dict(missing=sorted(set(strata_expected)-set(names)),extra=sorted(set(names)-set(strata_expected)),duplicates=sorted(k for k,v in counts.items() if v>1),sum_ok=(sum(int(r[1]) for r in ss),sum(int(r[2]) for r in ss))==(len(ns['rall']),ns['fit']))
tree=ast.parse(pathlib.Path('tools/regen_rubric_values.py').read_text(encoding='utf-8'))
allowed=[]
for n in tree.body:
 if isinstance(n,(ast.Import,ast.ImportFrom,ast.FunctionDef)): allowed.append(n)
 elif isinstance(n,ast.Assign) and all(isinstance(t,ast.Name) for t in n.targets): allowed.append(n)
g={'__name__':'__diagnostic__','__file__':'tools/regen_rubric_values.py'}
exec(compile(ast.Module(body=allowed,type_ignores=[]),'tools/regen_rubric_values.py','exec'),g)
# Memory-only minimal-repair experiment: exact source-derived set/multiplicity replaces fixed cardinality.
derive=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='derive')
for i,n in enumerate(derive.body):
 if isinstance(n,ast.If) and 'len(strata)' in ast.unparse(n.test):
  derive.body[i]=ast.parse("if audit(strata) != dict(missing=[],extra=[],duplicates=[],sum_ok=True):\n raise SystemExit('source-strata-contract-fail')").body[0]
g['audit']=audit
exec(compile(ast.fix_missing_locations(ast.Module(body=[derive],type_ignores=[])),'memory-only-minimal-repair','exec'),g)
v=g['derive'](out)
live={(str(len(pathlib.Path(p).read_bytes())),hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()[:16]) for p in ['tools/measure_score_bands.py','tools/regen_rubric_values.py']}
gb=io.StringIO()
with contextlib.redirect_stdout(gb): gate0=g['gate0'](v,live)
txt=pathlib.Path(g['RUBRIC']).read_text(encoding='utf-8')
a=g['role_scan'](txt,v); b=g['ident_scan'](txt,live); hits,allow=g['residue_scan'](txt,g['moved_literals'](txt,v))
keys=set((i,o) for i,o,_ in hits)|set((i,f) for i,_,f,_ in b)
case={'clean':parsed,'missing':parsed[1:],'duplicate':parsed+[parsed[0]],'extra':parsed+[('F-2099','1','1','100.0')],'same-count-missing-plus-duplicate':parsed[1:]+[parsed[1]],'sum-fit-minus-one':[(nm,n,str(int(f)-1) if j==0 else f,p) for j,(nm,n,f,p) in enumerate(parsed)]}
fixtures={k:audit(vv) for k,vv in case.items()}
pre2026=[(uid,rs) for uid,rs in ns['runits'] if uid.split('-')[2][:4] in ['2024','2025']]
sem2=[(uid,rs) for uid,rs in pre2026 if uid.split('-')[2][4]=='2']
def summary(rr):
 vs=[r for _,rs in rr for r in rs]
 return {'units':len(rr),'n':len(vs),'fit':sum(ns['R_LO']<=r<=ns['R_HI'] for r in vs)}
files=['AGENTS.md','CLAUDE.md','docs/DATA_STANDARD.md','.claude/agents/rev-arbiter.md','output/260911/rev/260911_02_info_ab50_ruler_decision.md','corpus/EX-social-20261M/meta.yml','corpus/EX-social-20261M/verify_log.tsv']+[str(p).replace('\\','/') for p in sorted(pathlib.Path('corpus').glob('EX-*/transcript.md'))]
hashes=[{'path':p,'bytes':len(bb),'sha256':hashlib.sha256(bb).hexdigest()} for p in files for bb in [pathlib.Path(p).read_bytes()]]
print(json.dumps({'unit_expected':source_ids,'unit_observed':observed_ids,'unit_missing':sorted(set(source_ids)-set(observed_ids)),'unit_extra':sorted(set(observed_ids)-set(source_ids)),'unit_duplicates':[k for k,vv in Counter(observed_ids).items() if vv>1],'strata_expected':strata_expected,'strata_observed':parsed,'closure':audit(parsed),'fixtures':fixtures,'measure_exit':measure_exit,'selected_units':len(ns['runits']),'nonselective_units':sum(not r[1] for r in rows),'excluded':sorted(ns['EXCL']),'pre2026':summary(pre2026),'pre2026_sem2':summary(sem2),'minimal_repair_derived':v,'minimal_repair_gate0_output':gb.getvalue(),'minimal_repair_gate0_return':gate0,'a_findings':a,'b_findings':b,'c_hits':hits,'stale':len(keys),'stale_lines':len(set(k[0] for k in keys)),'residual':sum(i not in set(z[0] for z in a) for i,_,_ in hits),'additional_hashes':hashes},ensure_ascii=True))
'@ | python -
```

실험 최초 출력은 Python cp1252가 한글 JSON을 인코딩하지 못해 exit 1이었다. `ensure_ascii=True`로 JSON 직렬화만 바꿔 재실행했고 최종 exit 0. 전사·기준·제품 바이트를 변환하지 않았다. 환경변수의 PowerShell Env: 열거도 duplicate-key 오류가 있어 Python os.environ 조회로 대체했다. Git 상태 조회는 전역 ignore 읽기 권한 경고 2줄을 냈다. 이것들은 제품 검증 PASS 근거가 아니며 숨기지 않는다.

# §2 unit별 판정

## Q1 — 원본 파생 모집단 계약으로 재서명: revise-required

**채택하는 수리 방향은 원본 파생 계층 집합의 재서명이다.** 현재 살아 있는 전체 모집단을 고정 4행으로 표현하는 안은 부적합하다. 다만 현재 실패한 6계층 결과를 그대로 정본 수치로 승인하지 않는다. **사용자 키 및 정확한 반영안이 아직 없어 기준 코드 수정은 blocked**다.

사용자가 명시해야 할 선택:
- [ ] 현재 동결된 EX 원천 60유닛(2024·2025의 1·2학기 및 2026의 확보된 1학기)을 검사 모집단으로 삼고, 그 원천에서 M/F×연도 계층을 파생하는 버전의 재서명을 승인하는가?
- [ ] 과거 범위를 보존하려면 이를 현재 전역 게이트 대신 쓰지 않고 **별도 역사 버전**으로 보존하는가? 2024·2025 전체학기 42 선택형 유닛/982문항과 2학기 한정 22/510을 혼동하지 않는 정확한 라벨을 선택해야 한다.
- [ ] 검사 모집단과 통계 적격 모집단을 분리할 때 partial·선택형 비적용·중복 후보의 처분을 어떤 계약으로 서명할 것인가? 현재 EXCL 1건을 정본에서 지우거나 전역 실패를 면제하는 승인은 본 문서에 없다(Q2).

이 판정이 허용하는 것은 위 방향의 **읽기 전용 명세·diff 준비**까지다. 반영 후보 범위는 REV_GUIDE §5의 해당 자 파일 중 원천 모집단/파생 계층/범위 라벨/인용 수치/하위 실패 전파에 필요한 최소 변경이다. 이것은 파일 전체 편집 허가가 아니다. 밴드 `[0.80,1.20]`, 기존 선택형 Tier 경계, 수학 비적용, 정보 서답형 기준을 이 수리에 섞어 바꾸지 않는다.

수리 명세의 필수 내용:
1. source manifest에는 유닛 ID·transcript/meta 해시·자료 범위·포함/비적용/부분의 근거를 적는다. 기대 유닛 집합을 실행 때 원천과 재대조한다. 승인 후 추가된 자료나 사라진 자료는 자동 수용하지 않고 manifest drift로 차단한다.
2. 계층은 정규화된 원천 메타에서 파생하고 expected/observed/duplicate/missing/extra **목록**을 출력한다. 숫자 6을 새 상수로 고정하는 방법도 거부한다. 동일 수의 계층 대체를 검출해야 한다.
3. 총 유닛/선택형 보유/집계 포함/미포함을 나눈다. 선택형 평균단가에 서답형을 섞지 않는다. 승인 없는 부분 유닛 재산입·자동 중복 제거는 금지한다.
4. 계층 합→연도 합→ALL의 분모·분자를 Fraction 또는 동등한 정확산술로 대조한다. 각 fit은 해당 n을 넘지 않고 outside 및 Tier 합도 맞아야 한다. 동일 밴드의 개별 score/r/Tier는 모집단 확장만으로 바뀌어서는 안 된다.
5. 원천 선언·합계축 미검증을 숨기지 않는다. 원천을 출력 복사값으로 “보충”하지 않는다. 이미 측정된 uncovered 38개가 known fixture다.
6. 계층 정상 입력 외에 누락, 중복, 추가, 같은 행 수의 대체, 합계 오류를 주입한다. 아울러 원천 유닛 1개 삭제/추가·중복, 선택형 비적용과 EXCL 혼동(50 대 49), measure의 현재 exit 1/경고 40을 하위 게이트가 PASS로 바꾸려는 경우를 실패로 검출한다. 실제 코드의 fixture와 knockout이 마련되기 전 이번 메모리 5/5만으로 구현 완료라 하지 않는다.
7. 현행 값·역사 예시·독립 목표 사다리를 구분한다. 역사 전체 숫자 치환과 ALLOW 일괄 확장은 불허한다. 개행만 바뀌어도 해시는 새로 재동결한다.

최종 값은 사용자 선택과 원천 자격 확정 후 재생성한다. 지금의 1148/1101, 49/50, 진단 stale 61 등은 **검증된 현상**이지 미래 성공 기대값이 아니다. 최종 경고 기대값은 0이며, 현재 경고 40을 허용 기대값으로 삼지 않는다.

## Q2 — 기존 면제의 경계만 approve; 전역 기준은 blocked

직접 읽은 Cycle1 F2-2는 “G2-a FAIL 그대로 + 별도 gate-exempt 기록”이다. 현재 meta `scope: partial`, 전사 머리의 동일 선언, verify_log의 `gate-exempt` 행이 그 범위를 뒷받침한다. 측정기에서도 declared 24 / extracted 15가 재현된다.

서로 다른 세 수치를 섞지 않는다:
- 시험 인쇄 선언: 선택형 24 + 서답 3 = 27.
- 기존 부분 분류 운용의 확인 문항: 20(완결 9+부분 11); 미발견 7을 미출제로 세지 않기 위한 분모다.
- 현재 선택형 배점 파싱: 15. **20을 선택형 배점 표본 수로 대신 넣을 수 없다.**

따라서 해당 유닛의 S3 부분 투입 면제는 유지할 수 있으나, 전역 measure exit0/WARN0, regen 검출력/stale0, assurance 실패0를 이미 만족했다는 뜻이 아니다. 다른 59유닛이나 A/B50에 면제 권한을 전파하지 않는다. 불명 배점 생성, 선언 24→15 축소, 유닛 삭제, 경고 필터링은 불허한다.

**현재 선택은 전역 미통과를 그대로 유지**하는 것이다. 그것이 partial 자료의 전사·유형 부분 활용까지 금지한다는 뜻은 아니다. 전역 검사와 통계의 적격성·면제 보고를 분리한 새로운 계약을 원한다면, 사용자는 그 적용 단계·유닛·분모·잔여 FAIL 표시·재검증 조건을 명시적으로 선택해야 하고 별도 two-key 판정이 필요하다. “수행”이나 이 Q2의 approve만으로 그런 계약이 선택됐다고 처리하지 않는다.

중복 후보 1개와 합계축 uncovered 38개도 별개다. partial 1건 처분으로 나머지 경고가 사라졌다고 보고하지 않는다. 기존 K1에서 배점열 동일은 시험 중복의 충분조건이 아니라고 판정한 사실은 확인했지만, 그 경고를 묵살해 전역 WARN0으로 간주하는 새 면제를 만들지 않는다.

## Q3 — 정보 난이도 자 별도 결정: revise-required

루브릭은 선택형 상대밴드만 서명했고 서답형은 명시적으로 미서명이다. T4 레시피에는 `DF1+DF2+DF5+(DF3 or DF7)`가 있으나 과목별 표에 정보 전용 발상 항목이 없다. 현 A/B 문제지는 서답·설명형 25개씩, 중상 목표·정식 Tier 미확정이라고 직접 적는다. 따라서 선택형 평균단가를 적용하거나 각 4점이라는 사실로 T4를 인증할 수 없다.

260911_01의 Q5와 open units도 정보 T4·서답형 밴드 결정을 남겨 두었다. 그 문서의 BF6 기대 “발화 ≥23 / FAIL 3”은 다른 SET-260908-info-26의 V1 사례다. 이번 50문항의 기대 출력이나 배포 승인으로 사용하지 않는다. 그 판정의 다른 수치·자기 모순 여부를 이번 기준 수리의 성공값으로 정정하려고 하지 않는다.

별도 결정에 필요한 내용:
- [ ] 정보 서답형을 **구조 기반으로 재는 기준** 및 자료 범위·경계 사례를 제시하고 사용자와 독립 판정자가 서명한다. 선택형 r 밴드에서 숫자만 전용하지 않는다. 기존 26제의 “서답형 Tier를 붙이지 않는 선택지”를 A/B50 최고 수준 요구 면제로 채택하지 않는다.
- [ ] 허용된 기출·학습지·교과서에서 비교할 **기존 최고 수준의 기준 문항과 최단 유효 풀이**를 동결한다. 출제/훈련 자료 등급과 범위 한계를 구별한다. 현재 A/B의 설계가 비교 기준을 역으로 정하게 하지 않는다.
- [ ] 사용자 조건 **“기존 최고 수준 + 필수적인 추가 사고력”**을 그대로 유지한다. 코드 길이·반복 횟수·배점·알고리즘 이름은 그 증거가 아니다. 선택/설계, 조건 역구성, 반례, 정당화 등의 요구가 실제 채점 조건에 있고, 최단 정당한 풀이에서도 제거할 수 없는지를 기준으로 명세한다. 어느 인지 요구를 정보의 DF5 및 자료/융합 축으로 인정할지 자료 근거와 함께 별도로 결정한다. 위 예시는 자동 통과 목록이 아니다.
- [ ] 긴 추적만으로 끝나는 경우, 추가 설명을 빼도 만점을 받는 경우, 제시 코드가 학생이 해야 할 설계를 이미 제공하는 경우를 음성 fixture로 삼는다. 최고 기준 충족의 양성 사례와 쉬운 지름길 반례를 함께 검증한다.
- [ ] 자가 확정된 뒤 각 문항의 최근접 원천, 필수 추가 사고, 최단 풀이/지름길 반증, 채점 기준을 기록하고 작성자와 분리된 Astra 컨텍스트에서 검증한다. 이번 세션은 이미 기존 해설이 인용된 문서를 읽었으므로 후속 맹목 풀이에 재사용하지 않는다.

이번에는 **정식 난이도 수치·T4 통과 문항 수를 서명하지 않는다**. 전수 50문항의 추가 사고력 충족/미충족을 기존 메인 루프 보고에서 복사해 독립 판정했다고 하지 않는다. 문항별 수리·재풀이 없이 자 결정만으로 배포가 열리지는 않는다.

## Q4 — 허용 변경·two-key·stale: 절차만 approve

### 현재 실행 가능한 범위
회신 읽기·해시 확인, 동결 source 확인, 읽기 전용 재현, 사용자 결정 항목 제출까지다. **본 판정에 의해 즉시 수정 가능한 제품·기준 파일은 0개**다. 타인 WIP, 카탈로그, 원장, check_assurance_contract의 실패 감추기·문자열 바꾸기도 허용하지 않는다.

### 두 키와 재동결 순서
1. **사용자 키**: Q1의 정확한 모집단/학기·연도 범위와 Q2의 전역 처리 계약, 별도 Q3 기준 선택을 명시한다. 어느 선택도 이번 “수행”으로 소급 충족되지 않는다.
2. **감사 키**: 그 선택에 대응하는 최소 diff·원천 해시·정상/결함 fixture·기대 출력·카운트를 독립 Astra 판정자가 승인한다. 본 판정의 revise-required를 패치 approve로 읽지 않는다. 새 부수 요건을 무한히 추가하지 말고 이번에 측정한 결함으로 범위를 닫는다.
3. **소유자 반영**: 승인 범위만 도구 기반으로 반영하고 승인 diff 밖 변화가 없는지 확인한다. 감사자가 자를 고쳐 자기 판정을 통과시키지 않는다.
4. **원천 재생성·검증**: 아래 명령을 개별 실행한다. 필요하다면 명시적 중간 미통과 결과를 기록하되 최종 성공 게이트를 완화하지 않는다.
5. **감사권한자의 재동결**: 원장에 구→신 bytes + sha256(16), 전체 SHA256, 두 키의 경로/범위, 원천 manifest, 실행 로그·검출력 결과를 append-only로 연결한다. 현행 세대 표시와 역사 세대를 구분하고 과거 행은 덮어쓰지 않는다. 이번 세션은 이 원장 행을 쓸 권한이 없다.
6. 기존 결과를 아래 범위로 stale 처리하고 새 기준에 의한 전수 검증을 마친 뒤만 다시 인용한다. 재동결만으로 새 판정이 생성되는 것은 아니다.

### 수정 후 검증 계약
| 명령 | 성공 기대 출력·exit·경고 | 기대 카운트/범위 |
|---|---|---|
| `python tools/measure_score_bands.py` | exit 0; `[GATE 0 PASS] undetected=0`; `[GATE 1 PASS] undetected=0`; 선언 불일치 0; 경고 0 | 현 기준 파서 fixture 9 + 상태 fixture 6; truth 앵커 10개가 실제로 모두 존재·대조되어야 함. 원천 유닛 및 적격 집합은 승인된 manifest로 재산출; 현재 inventory 60을 허가 없이 바꾸지 않음 |
| `python tools/regen_rubric_values.py` | exit 0; `[GATE 0 PASS] undetected=0`; `stale=0 lines=0 residual=0`; 지적 행 0·[WARN] 0 | 기존 fixture 11 + 승인 구현의 계층/원천/실패전파 fixture 전건 검출; 미검출 0. 계층/연도/ALL/Tier 총합 불일치 0. expected/observed ID와 계층 목록 동등·중복/누락/추가 0 |
| `python tools/check_assurance_contract.py` | exit 0; `assurance-contract: PASS (0 failures, 13 agents, 13 §5 rows checked)`; 경고 0 | 현재 직접 실측 agent 파일 13 및 §5 파싱 행 13. 이 파일 집합 변경 시 원천에서 다시 산출; 기존 실패10을 허용값으로 삼지 않음 |

첫 행의 exit0/WARN0은 현재 partial·다른 경고가 살아 있어 **지금 달성됐다고 주장할 수 없다**. Q2에 대한 별도 새 계약을 선택한다면 명령의 상태 모델·기대 출력 자체를 두 키로 다시 확정해야 한다. 현재 계약을 슬쩍 읽어 바꾸지 않는다.

회귀 검증은 승인 패치의 항목/원천 메타/출력 세 층을 모두 덮는다. 결함 주입은 복제본 또는 메모리에서만 하고 실자료·원장을 오염시키지 않는다. 정상도 오탐 0, 결함은 미검출 0이어야 하며 계층 수만 수용하도록 만든 코드의 knockout도 실패해야 한다. 변이 사례 및 per-item score/r/Tier 불변의 전수 결과를 별도 증거로 남긴다. 이번 5개 메모리 fixture를 새 구현의 실행 결과로 대체하지 않는다.

### stale 범위 확정
- REV_GUIDE §5 대상 자 중 하나라도 바뀌면 **그 자를 사용한 모든 판정**이 stale이다. FAIL 행만이 아니라 PASS 행도 포함한다. 저장된 파일을 삭제한다는 뜻이 아니라 현행 승인 근거로 인용 금지라는 뜻이다.
- 이 사안의 직접 대상: 상대배점/밴드/연도·계층 폐쇄/분포 수치, per-item Tier, 루브릭을 사용한 V2·V4/세트 사다리, 난이도를 포함한 종합 품질·배포 적격 판정. A/B50은 이 의존 범위를 **50개 ID 전건** 다시 검증해야 한다.
- 정보 자가 별도 확정되면 서답형 Tier 및 T4 적합성·추가 사고력 판정도 전건 새로 수행한다.
- 카탈로그 변경에 따른 N/V1 재측정은 별도 이미 남은 작업이며 이 수리로 면제되지 않는다. SET-260908-info-26에 적용된 기대 출력/수치를 A/B50에 복제하지 않는다.
- 독립적인 원천 전사 사실, 불변 문항의 산술 결과, partial 면제의 역사 기록은 삭제/거짓으로 만들지 않는다. 다만 의존성이 불명확한 기존 승인 문서는 보류하고 의존성 확인/재측정 전에는 사용하지 않는다. Q2의 기존 부분 투입 면제가 새 전역 자의 통과 판정으로 승격되지도 않는다.
- 저장소 전체 옛 판정 파일의 완전한 의존성 색인을 이번에 만들었다고 주장하지 않는다. 전역 적용 범위의 원칙은 위와 같이 확정하며, 반영 담당은 자 참조와 실제 측정 입력의 해시를 전수 추적해 재검증 목록을 만들어야 한다. 일부 문서만 골라 과거 승인을 살리는 것은 허용하지 않는다.

### [Codex/OMX 지시]

```text
[Codex/OMX 지시] 260911_03 — 기준 수리 판정 수신, 사용자 키 확정 전 반영 중지
stage: 정보 A/B50 배포 선행 기준 수리. overall revise-required / repair_execution blocked / release blocked.
executor: 메인 루프 (Codex/OMX). 조정·승인 소비 책임으로 수행하며, 독립 감사자나 Claude Code Opus로 표시하지 않는다.
inputs: 본 회신, 요청서 output/260911/rev/260911_02_info_ab50_ruler_decision.md, §1-B 동결 9파일 및 별표 원천 manifest. bytes/SHA256은 본 표와 다시 대조한다.
outputs: 현재 제품·기준·카탈로그·공유 원장·타인 WIP 쓰기 없음. 사용자에게 Q1/Q2/Q3의 정확한 미결 선택과 허용 diff 범위를 제시한다.
gate: 우선 입력 해시 불일치 0. 이후 사용자 키와 패치 감사 키가 모두 충족될 때만 §2 Q4의 세 명령/기대 출력/경고0/카운트 검증으로 넘어간다.
known defects: measure exit1/WARN40; regen 4계층에서 조기종료; assurance exit1/10 failures. 원천은 6계층이며 50 보유 대 49 집계가 다르다. 계층만 수리해도 전체 통과 아님. 상세는 §1-C/D.
constraints: 4→6 단순 치환, EX-social-20261M 제거/배점 생성/면제→PASS 전환, ALLOW 일괄 확대, SET-260908-info-26 판정 전용 금지. 사용자 키 미충족 상태에서 수리·재동결 완료 선언 금지. 무커밋·무삭제·무리셋.
report: 두 키와 반영 diff 및 검증이 확보되면 같은 증거 묶음에 구→신 해시 사슬·잔여 목록·stale 대상 재검증을 기록한다. 현재는 사용자 선택 확정 지점에서 중지한다.
NEXT: Q1 원천 모집단/범위와 Q2 전역 partial 처리에 대한 명시적 사용자 선택 확보. Q3 정보 난이도 자 결정은 별도 사안으로 유지. 그 뒤 승인된 기준 수리/재동결 → A/1–A/5 파일럿 → A/B50 전수 및 변경 후 깨끗한 Astra 독립검증 → 별도 최종 승인 → 승인분 배포 동기화.
이 지시문의 값이 원문과 어긋나면 지시가 아니라 실측을 따르고 그 사실을 회신한다.
```

# §3 follow-up (비차단)

- 품질 보고서의 물음표로 손상된 부록은 승인 근거로 사용하지 않았고, 그 파일을 고치지 않았다. 정정은 소유자 별도 작업이다.
- 기존 26제 판정의 내부 표현·기대값을 이번에 전면 재심하지 않는다. 이번 기준 수리/50제 승인과 분리한다.
- 도구가 출력한 WIP 메타 오류는 각 소유자가 실제 상태를 확인해 처리해야 한다. 현재 3번 명령의 미통과 원인이지만 이를 빌미로 본 기준 수리의 사용자 선택을 바꾸거나 타인 WIP를 추정 수정하지 않는다.
- 새 단계 착수/슬라이스 checkpoint는 원래 소유자가 자기 범위에서 수행한다. 이번 회신 작성자는 WIP·상태를 쓰지 않는 단일 파일 권한을 지켰다.

# §4 open units (남은 집합)

| unit | 상태 | 정확한 다음 행위·종료 조건 |
|---|---|---|
| Q1 | revise-required / 반영 blocked | 원본 파생 재서명 방향의 사용자 범위 선택 → 정확한 diff와 실패전파/집합 fixture 독립 승인 → 반영·재생성 |
| Q2 전역 처리 선택 | blocked | 기존 부분 투입 면제는 유지. 전역 미통과 유지 또는 별도 명시 계약의 two-key 결정. 임의 PASS 금지 |
| Q3 | revise-required | 정보 서답형·T4 자의 기준 원천/구조/필수 추가 사고력 결정. 이 회신은 문항별 통과를 부여하지 않음 |
| Q4 적용 | blocked | 두 키 확보 후 해시 사슬·세 게이트·stale 재검증. 절차 승인만으로 실행 승인 아님 |
| A/B50 배포 | blocked | 기준 수리 후 파일럿·전수 독립 검증·최종 승인·제품/문제지/답지/인덱스 동기화. 이번 단계 범위 밖 |

**NEXT: Q1/Q2의 명시적 사용자 선택 확정.** 다음 담당이 이미 승인된 산술식이나 기대 카운트가 있는 것처럼 작성하거나, 이 회신을 배포 승인으로 사용하면 안 된다.

## 별표 1 — 원천 식별자 전수 대조

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
  "extra": []
}
```

## 별표 2 — A/B 문제지 식별자 대조 (난이도 판정 아님)

문제지의 `^\*\*(\d+)\.\*\*` 머리를 추출하고 A/B 접두를 붙여, 요청의 A/1–A/25·B/1–B/25와 대조했다. 숫자 50만 비교하지 않았다. 답지 커버리지/정답/품질을 재검증한 것은 아니다.

```json
{
  "expected": [
    "A/1",
    "A/2",
    "A/3",
    "A/4",
    "A/5",
    "A/6",
    "A/7",
    "A/8",
    "A/9",
    "A/10",
    "A/11",
    "A/12",
    "A/13",
    "A/14",
    "A/15",
    "A/16",
    "A/17",
    "A/18",
    "A/19",
    "A/20",
    "A/21",
    "A/22",
    "A/23",
    "A/24",
    "A/25",
    "B/1",
    "B/2",
    "B/3",
    "B/4",
    "B/5",
    "B/6",
    "B/7",
    "B/8",
    "B/9",
    "B/10",
    "B/11",
    "B/12",
    "B/13",
    "B/14",
    "B/15",
    "B/16",
    "B/17",
    "B/18",
    "B/19",
    "B/20",
    "B/21",
    "B/22",
    "B/23",
    "B/24",
    "B/25"
  ],
  "observed": [
    "A/1",
    "A/2",
    "A/3",
    "A/4",
    "A/5",
    "A/6",
    "A/7",
    "A/8",
    "A/9",
    "A/10",
    "A/11",
    "A/12",
    "A/13",
    "A/14",
    "A/15",
    "A/16",
    "A/17",
    "A/18",
    "A/19",
    "A/20",
    "A/21",
    "A/22",
    "A/23",
    "A/24",
    "A/25",
    "B/1",
    "B/2",
    "B/3",
    "B/4",
    "B/5",
    "B/6",
    "B/7",
    "B/8",
    "B/9",
    "B/10",
    "B/11",
    "B/12",
    "B/13",
    "B/14",
    "B/15",
    "B/16",
    "B/17",
    "B/18",
    "B/19",
    "B/20",
    "B/21",
    "B/22",
    "B/23",
    "B/24",
    "B/25"
  ],
  "duplicates": [],
  "missing": [],
  "extra": []
}
```

## 별표 3 — 추가 읽기 입력 해시

| path | bytes | SHA256 |
|---|---:|---|
| `AGENTS.md` | 28084 | `5901a8628913257a51b2928db61c5f33a97e0d52a3c25fa0d155c158d63b401c` |
| `CLAUDE.md` | 45832 | `b8adc4e7c7e56f1e57027eb66d3920f8ef202a0c61411b9838d60e1d34465928` |
| `docs/DATA_STANDARD.md` | 27062 | `315c621ba02466561088e1e6d1276218311569218d52caa39e1e9faad2ee35b5` |
| `.claude/agents/rev-arbiter.md` | 9239 | `c7168c5eca9c56d6150044ca8b0f5a28526d6930048da74e8a059068b4eeb283` |
| `output/260911/rev/260911_02_info_ab50_ruler_decision.md` | 5864 | `1f25f1e8f468a26a733427008d7c0833f18646ff3d748eea7940383212acc188` |
| `corpus/EX-social-20261M/meta.yml` | 4948 | `e2de8f9f251950cf18584ef172a501a4be86670d0586548dab8add36cd97ced3` |
| `corpus/EX-social-20261M/verify_log.tsv` | 13599 | `a9ed4046e60693b7e320cda2c60ed7394ca37bef2e65ede0d75f11bdb9192b49` |
| `corpus/EX-english-20241F/transcript.md` | 46720 | `359c09da7842f5a0cdc716b42efc254c878d7b84e75fb409cb53933e1fd4c2ed` |
| `corpus/EX-english-20241M/transcript.md` | 46751 | `842b287b87837dc28220055cbf2d5f5eff9986fa176c7f9eb0394e8d67d6f279` |
| `corpus/EX-english-20242F/transcript.md` | 57638 | `38a96c6e5aa1d2272e41826dc4448ef0e922bfb492c459255018f6e9c507a5a9` |
| `corpus/EX-english-20242M/transcript.md` | 57734 | `c29d3ef592360b8695f2be9dc32e8d6d00e7e5626708487b7dbb7a87e6bb0b82` |
| `corpus/EX-english-20251F/transcript.md` | 55259 | `80042274dc869f5b37d535675ed231887e5e40e4e365a1a2d32b1f0f532a61d1` |
| `corpus/EX-english-20251M/transcript.md` | 45809 | `28fdfd0a65a7932652a238f073581ab56d55a93b6b9ccc75d171b4da5d25b2d2` |
| `corpus/EX-english-20252F/transcript.md` | 54395 | `c320a939ba431432189c1a50ef8a507f914be5267252badef9294677c9066df7` |
| `corpus/EX-english-20252M/transcript.md` | 51305 | `7c60c4fe031690bbcdd948970abf2c0bf654d72ba927ea3b2029a08502ee88f8` |
| `corpus/EX-english-20261F/transcript.md` | 54763 | `7f2cdc95cf34a8903493cc5b316cd8ac2185b925b8dd56d62336e0875b876999` |
| `corpus/EX-english-20261M/transcript.md` | 50149 | `33fde64cf038755874eb532f5473ce383e80cf12caa2dc454447d00cff37f6d4` |
| `corpus/EX-history-20241F/transcript.md` | 24518 | `05d8f8cbcd43fa80f4d4828d167c3f2177bb8d57837ce0d13a6a8d6f6b3eb4ed` |
| `corpus/EX-history-20241M/transcript.md` | 23384 | `605a6d061162b558e2bb6e0361defdb665e0ee21e9916d1ac422ad881d7cf83e` |
| `corpus/EX-history-20242F/transcript.md` | 41865 | `bfff9aaf4b4077f0f2f9370df2a587c7a9c972c5963377e90e0434f224a19bfc` |
| `corpus/EX-history-20242M/transcript.md` | 39216 | `f67b1f96d0505b59b9350968aacb61be03c51584b67d97bfb49e1ac4fdf3beab` |
| `corpus/EX-history-20251F/transcript.md` | 29139 | `00548ed4eb43b1a443f79a2ffd40031c5149464b8b665b641ec0c57a520c1e54` |
| `corpus/EX-history-20251M/transcript.md` | 27710 | `027cda44c645f2f600fdf2df7c5c566c5e7aa9f676ae72f5621af228b7d6e6ac` |
| `corpus/EX-history-20252F/transcript.md` | 26277 | `26595f4c36436d5cceaa46d5bf884f7ea997801a0f398782ff55e2e441ec7df3` |
| `corpus/EX-history-20252M/transcript.md` | 25057 | `e0ee96c8403a7e50059129a4ef5cdb944ae1cde04206f0e24383ee978ee7e5c9` |
| `corpus/EX-history-20261F/transcript.md` | 37852 | `065cf1dbc1c5420ee5b1bb4a2f8da48efd4ff06a96feb5faa3d0d549bd264754` |
| `corpus/EX-history-20261M/transcript.md` | 34247 | `19409adaef5259a69f1c0f1c7dccaf7c251e59dd58dc0ff6e4da7bc46ef79701` |
| `corpus/EX-info-20252F/transcript.md` | 10512 | `fe07ad3612ce7054343d48f2e29accd48a68d3fa6b9edcb88528c2ce8fa8035e` |
| `corpus/EX-info-20252M/transcript.md` | 8412 | `bcd760fe017095b0683a9327e77c6597389c557b2a7b975b041704106861cb85` |
| `corpus/EX-korean-20241F/transcript.md` | 72799 | `f8d80427344aa0dc1d50685f7ab0a25d71216266f1f2126e04ff3d9e52a4b853` |
| `corpus/EX-korean-20241M/transcript.md` | 67713 | `8386f99b79d7c2399527d8b1d066c468a35ccbcdc0eb663aa7c7d8cbcc86dc82` |
| `corpus/EX-korean-20242F/transcript.md` | 75745 | `5f2bc589aaeb47d424b9eabf902fae283e81977e113d68b7b3b2e5adab1a4d91` |
| `corpus/EX-korean-20242M/transcript.md` | 65068 | `3b53aff6e2d83c3b5c9f72df746d5d59e2b0d44d034ece074753f5d7bb8ae6f6` |
| `corpus/EX-korean-20251F/transcript.md` | 53701 | `31418f4f31a43d0ce4eae62db1c906811e00b181459e511e024520cbc2c47a44` |
| `corpus/EX-korean-20251M/transcript.md` | 79841 | `11f2d18a4726f9c3adc9a2db954c698ee54847fec38c9193a4c8e277a0019af8` |
| `corpus/EX-korean-20252F/transcript.md` | 82077 | `c543179ce05e34d02b03feac838f263f9ffed83f0d46a8bd2a64962b49002497` |
| `corpus/EX-korean-20252M/transcript.md` | 84171 | `d5d8125181bea6c93de548fc7ae51f10096c6ea5da1a6d52ca3452ff90d96938` |
| `corpus/EX-math1-20241F/transcript.md` | 6679 | `bc7c62c3a58648e3e7ca35119919a31d1052e0bbe5cdc2d748a5dab804b4cfee` |
| `corpus/EX-math1-20241M/transcript.md` | 7400 | `25b5eb75745649547661f85940e055ef99b9d9eaa2235026b90f31a083fa3266` |
| `corpus/EX-math1-20242F/transcript.md` | 11338 | `207128e4d8a10338de6538ce42dd33c096f1bb0556272f3118a4b0de3d17081a` |
| `corpus/EX-math1-20242M/transcript.md` | 13883 | `070d330410de1cd73239d487c544354ba34c69a82a3b6fdf58e5b4135a43c80e` |
| `corpus/EX-math1-20251F/transcript.md` | 8687 | `3f8325628401d6f16e5265c02b62efd2965bcc8abec11026fdc53c04199f2826` |
| `corpus/EX-math1-20251M/transcript.md` | 8022 | `966e3d13c2db6d52ff1298f195ca42d99e1c1de5e772b122f5714f6d78906345` |
| `corpus/EX-math1-20261F/transcript.md` | 17929 | `7c8305b123d80affd2ae516a359180bab4e68861941acdc1f633a39579480d81` |
| `corpus/EX-math1-20261M/transcript.md` | 18573 | `0f950f961b2be17c41de2fd85e0d19d197a73d57eaaf6f8cf4fb0469b08ac159` |
| `corpus/EX-math2-20252F/transcript.md` | 15058 | `580d5655566ae2abe234e46b48c4c71b2eeb40c1a23570ec770b0164aa1dd6ef` |
| `corpus/EX-math2-20252M/transcript.md` | 8336 | `9e2ed478c120c790327eec4e68404bbfbf6e50028f099934b22803d3671744be` |
| `corpus/EX-science-20241F/transcript.md` | 28362 | `faa2c7f9b3601bc6bf78bdee4a935ef4185db2139d2709d8eb3e7f1297a2be9f` |
| `corpus/EX-science-20241M/transcript.md` | 24707 | `d478a9aa95b65ad84a9b9b0b6d0c9096f35efc919141fa7ede4af4a641564735` |
| `corpus/EX-science-20242F/transcript.md` | 39812 | `04c409afe27b732f72310aa5f5b9813ea8eec9e3eb4cbd1ae0c0fcb331d94e11` |
| `corpus/EX-science-20242M/transcript.md` | 29981 | `04be3c40e25a1b21502e08dadadbff01c476d5e70bb21d84dc896e4462c6b3a9` |
| `corpus/EX-science-20251F/transcript.md` | 26331 | `90143add4bb75ad2ef42bac687d0987cc5f205c47312564bbabf5a0708695e40` |
| `corpus/EX-science-20251M/transcript.md` | 25967 | `ddbd9cb5c1d66bc935172ec751f3eece494e4646dbb944471c2e5eadc879dd4a` |
| `corpus/EX-science-20252F/transcript.md` | 25725 | `d2788c7a36262adc622d661cc39aee93b154c79036b073f6b4c053d7fab2c2d7` |
| `corpus/EX-science-20252M/transcript.md` | 31991 | `541d0a5bcc41d144cb58ccddec3fe01f7a102ada3f021282ceafb8a0fa1c01c6` |
| `corpus/EX-science-20261F/transcript.md` | 41349 | `361532951a582237cfd806321f9c07b47c7ae2809dfe069f22a51339cbaa7e8c` |
| `corpus/EX-science-20261M/transcript.md` | 47861 | `313f5ed4f50ccb3fcb020220ae08d297c475243a241f5e6c763d27aade80a85f` |
| `corpus/EX-social-20241F/transcript.md` | 28130 | `5af58b42b2774847bb202ff3196e8ba3b30fb6fd047668ecac0e4d207d1a1593` |
| `corpus/EX-social-20241M/transcript.md` | 31666 | `69e8707f12d24fb51acc307a66bf2b660438e36efc4ef9cc1a3f88e3447fa7d6` |
| `corpus/EX-social-20242F/transcript.md` | 38669 | `49f7d257fd85fa088415896a70c1ed5e2e37a70c9b4f8d50a708ef150d7bf701` |
| `corpus/EX-social-20242M/transcript.md` | 45054 | `3e7fc678538e0ed0b1c1df103dd572e83c4685f6b87c3410fc727d16161bb3a8` |
| `corpus/EX-social-20251F/transcript.md` | 27956 | `39737a4527339c4977e5de8376b3314a3f2b7dcfe917279ff9dbb35c75ed2289` |
| `corpus/EX-social-20251M/transcript.md` | 27376 | `80a915d89664fd7cf58013fafc41308052966194fb04348f4da116930c4c1a89` |
| `corpus/EX-social-20252F/transcript.md` | 25634 | `ce1f7efc73f5f31e69510bddc0e56183eb5c04085d2cd11e8217a372a60838fc` |
| `corpus/EX-social-20252M/transcript.md` | 30293 | `bcd14fefa2642492017741ea94af8cac67fe5fd3ce7d0c3ba9a3101f01a2bcad` |
| `corpus/EX-social-20261F/transcript.md` | 47598 | `67e3c525b27e97d37fab7a4b558b27becca5064865bc8491365f291aff755cac` |
| `corpus/EX-social-20261M/transcript.md` | 36874 | `34868967890b7519abd9ab2fc68038495a5f762ac31789b015d4fcc009648b8d` |
| `analysis/REV_LOG.md` | 244499 | `3271185126ac41917d626905e087c289f41cfd48367e6d03d1f2c7fd145fce6f` |
| `output/260831/rev/260831_04_arbiter_ruling_K1.md` | 39282 | `3dd0ad925ea48a13d723de3560edd01c6d520b3cab960cc5c4920e2df72da2e0` |
| `output/260831/rev/260831_09_arbiter_ruling_m6m7_resign.md` | 34823 | `eda5b387fbabed083cbe607b44d0e520feff920b8161dffaba03ad9f9bab7c31` |
| `.claude/agents/item-quality-auditor.md` | 13305 | `6a0a5f3c1ceb5750da3f1596f2a95ebff723eabdaada15876beb1ba66a20c7d4` |
| `output/260910/260910_01_info_composite_a_questions_review.md` | 19401 | `2017bcaea3eb7c49c65fcbc187596df1a79a5bfb9f2e7664ec2cd01c6c47a88d` |
| `output/260910/260910_02_info_composite_b_questions_review.md` | 20207 | `a4dea5692f3c1a116fb2771ea628f0afaeef01602864de2040e05bd9bb13ccd6` |

## history
- 2026-09-11 — 새 컨텍스트에서 호스트 모델/깊이 확인, 동결 9파일 직접 대조, 요청 세 명령 각각 실행, 원천 60유닛/6계층 및 메모리 최소 수리·결함 주입 검증. Q1·Q3 revise-required, Q2·Q4 경계/절차만 approve. 수리 실행·배포는 blocked. 회신 1개만 신규 작성; 커밋·삭제·리셋 및 제품/기준/공유 원장/WIP 수정 없음.

