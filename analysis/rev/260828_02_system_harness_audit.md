---
title: "하네스 구조 감사 — 지침·서브에이전트 정의·게이트 도구가 실제로 동작하는가"
source: "CLAUDE.md · AGENTS.md · analysis/REV_GUIDE.md · .claude/agents/*.md(11) · tools/*.py(9) · analysis/wip/*(24)"
created: 2026-08-28
author: Claude Code Opus (메인 세션 · 시스템 감사)
status: applied-partial
reviewer: unset
---

# Review 02 — 하네스 구조 감사

> ⚠️ tier-1 라운드가 **아니다**. 사용자 지시로 메인 루프가 직접 수행했다. `_index.md`·`REV_LOG.md`
> 행은 추가하지 않았다 — 그 자체가 발견 S5의 내용이다(§5에 이 배우의 자리가 없다).
> 대상은 산출물이 아니라 **시스템 자신**이다: 규정이 실행 주체에 도달하는가, 게이트가 실제로 막는가.

<document>

## 0. 감사 질문

"우리 시스템이 제대로 동작하는가"를 두 축으로 쪼갰다.

- **도달(reach)** — 정본에 적힌 규정이 그것을 지켜야 할 주체의 정의 안에 실제로 있는가.
- **효력(bite)** — 자동 검사 도구가 위반을 실제로 붙잡고 exit≠0을 내는가.

두 축 모두 **측정으로만** 판정했다. 문서가 "한다"고 적혀 있는 것은 근거로 치지 않았다.

## 1. 발견

### S1 — 계약 검사기가 마커 존재만 본다 (구조적 · 최상위)

`tools/check_assurance_contract.py`는 개정 전까지 **문자열 포함 검사기**였다. 파일 목록을 손으로
고르고 그 안에 특정 문구가 있는지만 확인한다. 실측:

```
$ python tools/check_assurance_contract.py
assurance-contract: PASS (0 failures)     exit=0

$ grep -rl "resume audit" .claude/agents/ | wc -l
0        # 11개 정의 중 0개
```

**260828에 신설된 컨텍스트·쿼터 연속성 규칙(CLAUDE.md ⑤)이 실행 주체 11개 전부에 도달하지
않았는데 계약 게이트는 PASS를 찍었다.** 규칙이 요구한 마커가 AGENTS.md·CLAUDE.md·docs/ 5개
파일에는 있었고, 검사기의 파일 목록이 딱 거기까지였기 때문이다.

이것은 내가 Codex assurance team 감사(`output/260828/rev/260828_01_...`)에서 F3으로 지적한
`check_experiment.py`의 `require_report()`—마커 존재만 확인—**와 완전히 같은 결함 유형이다.**
남의 팀 게이트에서 찾아낸 결함이 우리 저장소의 게이트에도 그대로 있었다.

### S2 — 게이트 도구 2종이 fail-open (원칙 11 위반)

`tools/build_mastery.py:122-124` (개정 전):

```python
    for w in warnings:
        print("[WARN]", w)
    return 0
```

`warnings`의 내용은 `type {t} not in index.tsv` 다. 채점 원장의 유형 ID가 카탈로그 인덱스에
없다는 뜻이고, 이는 인덱스가 낡았거나 채점 TSV에 오타가 있다는 **무결성 결함**이지 참고사항이
아니다. 그런데 exit 0이었다. `tools/import_grading.py:243-248`은 같은 함수를 호출하며 같은
방식으로 warnings를 흘렸고 `rc`에 반영하지 않았다.

원칙 11이 만들어진 계기가 바로 이 패턴(`build_catalog_index.py --check`가 `[WARN]`에도 exit 0)
이었고, **그 도구는 고쳐졌다** — `build_catalog_index.py:217`에 옛 동작을 설명하는 주석이 남아
있다. 그러나 **형제 도구 2종에는 전파되지 않았다.** 원칙 10(동반 갱신)이 규정한 바로 그 사고다.

### S3 — 원칙 10 자신이 1/8 문서에만 구현됨

원칙 10은 "각 정본은 자기 「동반 갱신 목록」을 문서 안에 명시하고, 개정 시 그 목록을 체크한다"고
요구한다. 실측(`grep -c '동반 갱신'`):

| 문서 | 실제 목록 |
|---|---|
| `analysis/REV_GUIDE.md` | **있음** (§5 개정 시 목록) |
| `CLAUDE.md` | 없음 (원칙 10 본문의 자기언급 2회뿐) |
| `AGENTS.md` · `analysis/FORECAST_GUIDE.md` · `analysis/DOC_LOCATION.md` · `analysis/TYPE_CATALOG.md` · `analysis/catalog/CODE_REGISTRY.md` · `analysis/catalog/_README.md` · `docs/DATA_STANDARD.md` | 없음 |

동기화 붕괴를 막으려고 만든 규칙이 정작 자기를 담은 문서에 적용되지 않았다. S1·S2가 이 공백의
직접적 결과다.

### S4 — WIP 원장 규격 이탈 3건

24개 중 3건이 재개 불가능하다.

```
codex-omx_260827_cycle0_s1_restart.md        status='complete'  (열거값 밖)
codex-omx_260827_cycle0_s2_staged_dispatch.md  status 없음 · NEXT 없음
mainloop_260826_cycle0_S0.md                 NEXT 없음
```

규격 ②의 재개 규칙("시작 시 `NEXT`부터 이어서")은 `NEXT`가 없으면 성립하지 않는다.
`codex-omx_260827_cycle0_s2_type_propose_relay.md`는 아직 `in-progress`인 채 방치돼 있다 —
이번 Cycle 0 S2 중단 지점이다.

### S5 — 메인 루프가 실질 검토를 수행할 때 규정상 자리가 없다 (구조적)

REV_GUIDE §5 배우 표에서 main loop의 write surface는 `_index` 헤더 상태·status 필드**뿐**이다.
그런데 260828에 Codex/OMX 쿼터 소진으로 auditor·critic 라인이 멈추자, 사용자 지시로 메인 루프가
38KB 실질 감사와 참조 구현 3종을 작성했다. 이 문서 역시 같은 상태다.

규정대로면 그 작업은 존재할 수 없고, 실제로 일어났으므로 **규정이 현실을 덮지 못한다**.
지금은 `reviewer: unset` + 라벨 미도용으로 정직성만 지키고 있을 뿐, 원장에 흔적이 없다 —
즉 **이 감사는 시스템이 추적하지 못하는 작업이다.**

### S6 — 오탐으로 판명된 것 (기록)

감사 중 두 건을 결함으로 의심했다가 측정으로 기각했다. 남겨 둔다.

- **"슬라이스 규격이 정의에 없다"** — 한글 키워드 `슬라이스`가 11개 정의 중 0개였으나, 실제로는
  영문 `Runtime protocol — slice checkpointing`으로 전부 존재했다. 게다가 형식은 CLAUDE.md를
  **참조**하고 있어 원칙 9-c-ii(사본 열거 금지)를 올바로 따르고 있다.
- **"CLAUDE.md 경로 참조가 깨졌다"** — `REV_LOG.md`·`curriculum_2022.md` 등이 존재하지 않는 것으로
  나왔으나 전부 산문 속 상대 경로 표기였다. 실제 고아 참조 0건.
- **도구 부여 결합(원칙 ④)** — 260826 감사 A1에서 지적된 3종(`forecast-reviewer`·`forecast-auditor`·
  `solve-back-verifier`)은 **현재 모두 Write를 보유**한다. 수정이 반영돼 있었다.

### S7 — 다중 배우 팬아웃이 보증을 만든 적이 없다 (구조적 · 외부 지적 확인)

외부 세션이 "다중 배우 방법에 이득이 없다, 하나씩 돌려라"고 판정했다는 사용자 전언을 받고,
이 저장소의 실측으로 대조했다. **지적은 대체로 옳고, 우리 자료는 그보다 더 강하게 말한다.**

**팬아웃이 만든 것 = 보증의 외형** (전부 실측)

| 산출 | 실측 |
|---|---|
| `codex-team/check_experiment.py:223` | `print(f"warnings=0")` — 플레이스홀더 없는 f-string. 계산이 아니라 상수 |
| 같은 파일 `require_report()` L168-180 | 보고서에 마커 문자열이 있는지만 확인. 내용 검사 아님 |
| `actual-team` 주장 | 실행되지 않은 팀이 실행된 것으로 보고됨 (`260828_05` Purpose 문단) |
| 커버리지 | 중복 행 1건이 결손 문항 1건을 가림 |
| `tools/check_assurance_contract.py` (개정 전) | 손으로 고른 7개 파일의 부분문자열 검사. `PASS (0 failures)`를 찍는 동안 260828 연속성 규칙은 11개 배우 중 **0개**에 도달 |

역할 4개를 나란히 세워도 서로를 검증하지 않았다. 한 코디네이터가 4개의 산출을 모아 보고서를
쓰는 구조였고, 게이트는 그 보고서에 단어가 있는지만 봤다.

**실제로 결함을 잡은 것 = 순차 맹목 재유도**

`opus/OPUS_MATH2_PERSONA_ROLE_METHOD_EVALUATION_260828.md`는 단일 세션·서브에이전트 0·병렬 0으로
실행됐고(§실행 준수 확인), §1~§3을 확정한 **뒤에** 상대 문서를 처음 열었다. 그 순서 하나가
S-05·S-13의 SM2-14(기출 최빈 축, 상대 표에 0회 등장) · 정본 반증 5건 · 전사 결함 4건(I1·I2·I8·I9) ·
범위 미확정의 1차 자료 해소를 만들었다. 동시에 §4-6은 상대 우위 5건을 정직하게 적었다.

**결론**: 독립성은 **순서**로 사는 것이지 **동시성**으로 사는 것이 아니다.
- 쓰기 전에 읽지 않는다 = 독립. 순차로 살 수 있다.
- 같은 코디네이터 밑에서 동시에 돈다 = 비독립. 배우 수를 늘려도 사지 못한다.

따라서 유지할 것은 **동결입력 + 해시 검증 + 맹목 재유도 + 기대 카운트를 가진 fail-closed 게이트**이고,
버릴 것은 **레인 내부 역할 팬아웃 · 병렬 배우 실행 · 일상 작업에 대한 3단계 루프**다.
3단계 루프는 CLAUDE.md 흐름표가 이미 exam 세트로 한정하고 있으므로 규정 개정이 아니라 준수 문제다.

근거: `check_experiment.py:223`·L168-180 실측, `260828_05_guidance_remediation_plan.md` Purpose,
`OPUS_...EVALUATION_260828.md` §4-2·§4-6·§4-8·실행 준수 확인, 본 문서 S1 검증 로그.

## 2. 적용한 수정 (측정 증거 포함)

원칙 11 "도구가 문제를 발견하고도 0을 반환하면 **도구를 고치는 것이 먼저다**"에 따라 도구
결함은 제안이 아니라 수정으로 처리했다.

### A. `tools/check_assurance_contract.py` — 구조 검사 4종 추가

`670aee947164` 7656B. 기존 문자열 표는 그대로 두고 뒤에 붙였다.

1. **연속성 규칙 도달** — `.claude/agents/*.md` 전부가 `HOLD — resource exhausted`·`resume audit`를
   보유하는지.
2. **도구 부여 결합** — REV_GUIDE §5 표를 파싱해 배우별 write surface를 읽고, 해당 정의의
   `tools:` 줄에 Write가 있는지, 공유 원장(`_index`/`REV_LOG`)을 쓰는 배우면 Edit까지 있는지.
   표 행이 8개 미만으로 파싱되면 "표 모양이 바뀌었다"로 실패시킨다(파서 침묵 방지).
3. **WIP 재개 가능성** — `status` 열거값 + `NEXT:` 존재.
4. **fail-open 스캔** — `[WARN]`을 출력하면서 `[FAIL]` 경로가 없는 `tools/*.py`.

### B. `tools/build_mastery.py` · `tools/import_grading.py` — fail-closed 전환

`b20e865a510a` 5761B / `df17a50b8e37` 12463B. warnings를 `[OK]`보다 **먼저** 출력하고(원칙 11의
순서 지적), warnings가 있으면 `[FAIL]` + exit 1. 부수 효과로 `build_mastery.py`의 `warnings=`는
이제 `len(warnings)` 계산값이다 — codex-team `check_experiment.py:223`의 하드코딩 상수와 대비된다.

### C. 연속성 규칙을 11개 정의에 전파

각 정의 말미에 `## Continuity under exhaustion (CLAUDE.md 공통 실행 규격 ⑤, 260828)` 절 추가.
60% 임계, 모델 하향·병렬 재시도·busy-wait 금지, `HOLD — resource exhausted` 중지, 다음 턴
`resume audit` 절차를 담았다.

### D. `analysis/wip/mainloop_260826_cycle0_S0.md`에 `NEXT:` 추가

메인 루프 소유 파일이라 직접 고쳤다. codex-omx 소유 2건은 **손대지 않았다**(배타 소유).

### 검증 — 게이트에 이빨이 생겼음을 실증

```
개정 전:  assurance-contract: PASS (0 failures)              exit=0
개정 직후: assurance-contract: 26 failure(s)                 exit=1
C·D 적용 후: assurance-contract: 3 failure(s)                exit=1
```

남은 3건은 전부 codex-omx 배타 소유 WIP다 — **원칙 8 때문에 내가 고칠 수 없는 항목이고,
게이트가 그것을 정확히 붙잡고 있다.** 이것이 fail-closed가 의도대로 동작하는 모습이다.

회귀 없음:

```
$ python tools/build_catalog_index.py --check
[OK] index.tsv matches regeneration (131 rows)      exit=0
$ python tools/build_mastery.py --check
[OK] MASTERY.tsv matches regeneration (131 rows)
warnings=0                                          exit=0
```

## 3. 승인 요청 (판단이 필요해 수정하지 않은 것)

- [ ] **P-A. S4 잔여 2건 정리** — codex-omx WIP 2건의 `status`/`NEXT` 보정. **사용자 소관으로
      확정**(260828): 사용자가 Codex 작업 재시작을 결정했고, WIP 정리·삭제는 CLAUDE.md 규격 ②상
      사용자 전권이다. 재시작 팀이 새 WIP를 쓰거나 사용자가 이 2건을 정리할 때까지 계약 게이트는
      exit 1을 유지한다 — 이는 결함이 아니라 **의도된 fail-closed 잔류**다.
- [ ] **P-B. `codex-omx_260827_cycle0_s2_type_propose_relay.md` 처분** — `in-progress`로 중단된
      Cycle 0 S2 지점. **P-A와 함께 사용자 소관**(재시작 시 봉인 또는 승계).
- [x] **P-C. S3 — 「동반 갱신 목록」을 나머지 8개 정본에 신설.** (260828 적용) 각 문서의 의존처를
      `grep -rl` 실측으로 확정한 뒤 `CLAUDE.md`·`AGENTS.md`·`FORECAST_GUIDE`·`DOC_LOCATION`·
      `TYPE_CATALOG`·`CODE_REGISTRY`·`catalog/_README`·`DATA_STANDARD` 8종에 절을 추가했다.
      계약 검사기에 5번째 구조 검사(목록 존재, REV_GUIDE §5의 blockquote 형식도 통과)를 함께
      넣어 S3 재발을 차단했다. 구현률 1/8 → 9/9.
- [x] **P-D. S5 — REV_GUIDE §5에 배우 행 신설.** (260828 적용) 표에 대행 행을 추가하고,
      **발동 조건 2요건**(a 담당 배우 실행 불가 관측 · b 사용자 지시)과 **제안 등급 한정**
      (스스로 승인·투입 허가 불가, 담당 배우 복구 시 정규 tier-1 입력으로 재투입)을 본문에
      명시했다. 3단계 루프 우회 통로가 되지 않도록 조건을 좁힌 것이 핵심이다.
- [x] **P-E. `_index.md`·`REV_LOG.md` 기입.** (260828 적용) P-D로 라벨 문제가 해소되어
      `reviewer=main-loop`로 260828_01·260828_02 2행씩 추가했다. REV_LOG에는 시스템 층
      (`analysis/` · `tools/` · `.claude/`) 절을 신설했다 — 종전 절은 전부 `output/` 산출물
      기준이라 시스템 자체 변경을 담을 자리가 없었다.
- [x] **P-F. 메인 루프 WIP** — (260828 적용) 이 감사의 체크포인트를
      `analysis/wip/mainloop_260828_system_harness_audit.md`에 남겼다(슬라이스 14개·차단 조건·
      검증 명령·NEXT). 다만 **규격 ② 본문에 메인 루프를 배우로 추가하는 개정**은 CLAUDE.md
      수정이라 승인 대기로 남긴다 — 아래 P-G.
- [x] **P-G. CLAUDE.md 규격 ②의 적용 대상에 메인 루프 명시.** (260828 적용) "모든 서브에이전트
      **와 메인 루프**"로 확장하고, 메인 루프의 다중 슬라이스 작업(감사·대량 반영·PRD 작성)은
      `analysis/wip/mainloop_<YYMMDD>_<task>.md`에 기록하도록 규정했다.

### 잔여 상태 요약 (260828 종료 시점)

| 항목 | 상태 |
|---|---|
| P-C · P-D · P-E · P-F · P-G | **적용 완료 · 검증됨** |
| P-A · P-B | 사용자 소관 (Codex 재시작) — 계약 게이트 exit 1의 유일한 원인 |

계약 게이트가 exit 1인 것은 **미완이 아니라 설계대로**다. 소유권 때문에 이 세션이 고칠 수 없는
항목을 게이트가 정확히 3건 붙잡고 있고, 그 3건이 무엇인지 이름으로 출력한다.

</document>

## history
- 260828 최초 작성. 발견 S1~S6, 수정 A~D 적용·검증, 승인 요청 P-A~P-F.
- 260829 S7 추가 — 외부 세션의 "다중 배우 무익, 하나씩" 지적을 저장소 실측으로 대조해 확인.
  독립성은 순서로 사는 것이지 동시성으로 사는 것이 아니라는 결론. 정본 개정 없음(관찰 기록).
