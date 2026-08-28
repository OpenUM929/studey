# AGENT_AUDIT_260826 — 서브에이전트 정의 감사·수정 보고서

> **작성**: 260826, Claude Code(Opus) 메인 루프 — 사용자 **특례 승인**으로 검토자가 직접 수정을 수행.
> 평시 규정은 CLAUDE.md 원칙 8(검토·수정 분리)이며, 본 작업은 그 예외다. 따라서 이 문서가
> 검토서·판정서·반영 보고서를 겸하고, 아래 §7의 승인 요청 항목은 **사용자 확인 전까지 미결**이다.
> **대상**: `.claude/agents/*.md` 11개 정의 + 그와 어긋난 정본 3개.

---

## 1. 요약

11개 서브에이전트 정의를 CLAUDE.md·REV_GUIDE·DIFFICULTY_RUBRIC·AUTHORING_GUIDE·catalog/_README·
COMMON_TYPES·DOC_LOCATION·FORECAST_GUIDE·DATA_STANDARD와 1:1 대조했다. 역할 분해·write surface·
라운드 규격의 **설계 자체는 건전**했고, 실제 결함은 두 군데에 몰려 있었다.

1. **정본이 부여한 의무와 도구 권한이 어긋난 곳** — 지침대로 하면 실행이 불가능한 상태(3건).
2. **페르소나가 설계 전제를 배신하는 곳** — 검토 3단계의 값어치는 독립적 판단인데, 11개 중 9개가
   같은 문장("Sangsang High subject teacher and expert exam-item writer")으로 시작해 작성자와
   검토자가 같은 사전확률·같은 맹점을 공유하고 있었다.

| 구분 | 항목 | 처리 |
|------|------|------|
| A 차단급 | A1 도구 권한 누락 3종 · A2 item-writer 셸 부재 | ✅ 반영 |
| B 정합성 | B1 Tier 기준 오기 · B2 COMMON_TYPES 누락 2곳 · B3 보고 주체 불일치 · B4 §1-B 누락 · B5 모델 정책 충돌 · B6 오답 워크플로 무지침 | ✅ 반영 |
| C 설계 | C1 페르소나 동질화 · C2 호출 프롬프트 오염 · C3 환경 분리 주장 · C4 WIP 슬러그 충돌 · C5 위임 트리거 · C8 진행 맵 drift·중계 · C9 산출물 언어 | ✅ 반영 |
| C 설계 | C6 미사용 frontmatter · C7 상수 9중복 | ⏸ 부분 반영 / 사용자 판단 대기 (§6) |

변경 파일: 에이전트 정의 **11개 전부** + 정본 **3개**(`CLAUDE.md`·`analysis/REV_GUIDE.md`·
`analysis/catalog/COMMON_TYPES.md`). 문항·카탈로그·원장·도구 코드는 **일절 건드리지 않았다.**

---

## 2. 사실관계 (측정된 것만)

### 2.1 실행 환경
| 항목 | 실측값 | 확인 방법 |
|------|--------|-----------|
| Claude Code 버전 | **2.1.246** | `claude --version` |
| CLI 실행 파일 | `C:\Users\Administrator\.local\bin\claude` (250,948,768 B) | `which claude` · `ls -la` |
| frontmatter 확장 키 지원 | `disallowedTools`·`effort`·`maxTurns`·`permissionMode`·`isolation` 문자열이 CLI 바이너리의 에이전트 처리 구간에 존재 | `grep -aoE '.{100}"?disallowedTools"?.{160}' claude` — 같은 구간에 `agent() opts.disallowedTools entry ...`, `effort`, `allowed-tools` 등이 함께 등장 |
| 공식 문서 | `https://code.claude.com/docs/en/sub-agents` (구 URL `docs.claude.com/.../sub-agents` 는 301) | WebFetch |

### 2.2 공식 문서에서 확인한 규칙 (변경 근거로 사용)
- frontmatter 필드: `name`·`description`(필수), `tools`·`disallowedTools`·`model`·`permissionMode`·
  `maxTurns`·`skills`·`mcpServers`·`hooks`·`memory`·`background`·`effort`·`isolation`·`color`·`initialPrompt`.
- `model` 값: 별칭(`sonnet`/`opus`/`haiku`/`fable`) · 전체 ID · `inherit` · 생략 시 `inherit`.
  **해석 우선순위**: 환경변수 `CLAUDE_CODE_SUBAGENT_MODEL` → **호출 시 `model` 파라미터** →
  정의의 frontmatter → 메인 대화 모델. (B5 처리의 근거 — 호출부 override가 실재한다.)
- `description`은 **자동 위임 판단의 근거**다. (C5 처리의 근거.)
- `tools` 생략 시 서브에이전트 가용 도구 전부 상속. 본 시스템은 11개 모두 명시하므로 해당 없음.
- 서브에이전트는 기본 3단계까지 중첩 가능하나, 11개 정의 **어느 것도 `Agent`를 갖지 않아** 중첩 불가.
  (현 설계 의도와 일치 — 변경하지 않음.)

### 2.3 감사 대상의 형상
- 정의 11개, 감사 시점 총 **930줄**.
- 줄바꿈 코드가 파일마다 다르다: **CRLF 7개**(item-writer·rev-arbiter·rev-auditor·rev-writer·
  solve-back-verifier·type-extractor·type-proposer), **LF 4개**(forecast-* 4종). 정본 3개는 모두 CRLF.
  → 이 리포에는 **CRLF 프론트매터 파싱 실패 전력**(검토서 260826_01)이 있으므로, 모든 편집에서
  파일별 원래 줄바꿈 코드를 그대로 보존했다.
- **git 추적 상태**: 11개 중 **8개가 untracked(`??`)** — `forecast-*` 4종, `rev-*` 3종, `type-proposer`.
  즉 이 8개는 커밋 이력이 없어 `git diff`로 되돌릴 기준이 없다. **본 작업의 롤백 기준은 §8 해시표뿐이다.**
  (추적 중인 3개: item-writer · solve-back-verifier · type-extractor.)

### 2.4 수정 방법 (재현 가능)
- 모든 편집은 **단일 매치 강제** 스크립트로 수행: 치환 대상 문자열이 파일에서 정확히 1회
  일치하지 않으면 그 파일을 건드리지 않고 즉시 중단(`count != 1 → abort`). 부분 적용 사고를 차단.
- `item-writer.md`만 변경 밀도가 높아 전문(全文) 재작성했고, 나머지는 국소 치환.
- 시뮬레이션·데모 실행 없음. append-only 원장(`ATTEMPT_LOG`·`REV_LOG`·`_index.md`·`verify_log`)에
  **행을 하나도 쓰지 않았다** (CLAUDE.md 원칙 9-b). 정본 3개의 이력 섹션에만 append 했다.

---

## 3. A — 차단급 결함 (지침대로 하면 실행 불가였던 것)

### A1. 정본이 쓰기를 시키는데 도구가 없던 3종 ✅
| 에이전트 | REV_GUIDE §5가 준 write surface | 감사 시점 `tools` | 조치 |
|---|---|---|---|
| `forecast-reviewer` | own reports + `_index` rows + REV_LOG + own WIP | Write 없음 | `Write, Edit` 추가 |
| `forecast-auditor` | own `*_second.md` + `_index` rows + REV_LOG + own WIP | Write 없음 | `Write, Edit` 추가 |
| `solve-back-verifier` | **own WIP only** | Write 없음 | `Write` 추가 |

**사유**: 260826에 WIP 체크포인트 규격이 신설되면서 `rev-*` 3종은 갱신됐지만 이 3종의 `tools:` 줄은
따라오지 않았다. 정본은 "쓰라"고 하고 도구는 없는 상태 = 원칙 10(동반 갱신)이 경고한 그 구멍이
한 번 더 발생한 것이다. 이 상태에서 에이전트가 취할 수 있는 행동은 (a) 규정 위반, (b) 셸
리다이렉션 우회 둘뿐이며, 둘 다 원장 무결성에 나쁘다.

**파생 조치** — `tools` 허용목록은 write surface를 강제하지 못한다. 11개 전부가 셸(PowerShell/Bash)을
갖고 있어 어디든 쓸 수 있기 때문이다. 그래서 **경계를 도구층이 아니라 문서층에 명시**했다:
- 11개 정의 전부에 `**Shell is not a write loophole**` 문장 추가(실측 11/11).
- `REV_GUIDE.md` §5에 **Tool-grant coupling** 주석 + 동반 갱신 목록 신설.
- `CLAUDE.md` 서브에이전트 공통 실행 규격에 **④ write surface는 도구 부여와 함께 정의한다** 신설.

`disallowedTools`로 도구층 차단도 가능하지만 **적용하지 않았다** — 셸이 있는 한 우회 가능해서,
차단됐다는 착각만 만들고 실제 경계는 여전히 문서층이 진다. §6 참조.

### A2. `item-writer`에 계산 수단이 없던 문제 ✅
`tools`에 셸이 없어 authoring rule 4("자기 문항을 풀어 정답 유일성을 확인")를 **눈대중으로만**
수행할 수밖에 없었다. 수학은 서답형 100%이고 math2 목표 분포는 T3 43% / T4 13%
(DIFFICULTY_RUBRIC.md 실측표)다. → `PowerShell, Bash` 추가, rule 4를 "sympy로 실제 계산하는 것"
으로 명문화. 필수 게이트(`solve-back-verifier`)가 1차 실수를 전부 떠안던 구조를 완화한다.

---

## 4. B — 정본과 어긋난 곳

### B1. `solve-back-verifier`의 Tier 판정 기준 오기 ✅ (실질 오작동 위험 1순위)
- 감사 시점 정의: `T1 1–2 / T2 2–3 / **T3 3–5** / **T4 5+** or insight`
- 정본 `DIFFICULTY_RUBRIC.md` §3 표: `T1 1~2 / T2 2~3 / **T3 3** / **T4 4+**`(T4는 DF5 통찰 추가 요구)

→ **정본상 정상인 4단계 T4 문항을 필수 게이트가 "Tier 불일치"로 HOLD**시키고, 4~5단계를 T3로
강등 판정하는 상태였다. 전 세트가 이 게이트를 지나므로 영향 범위가 전면적이다.
조치: 수치 재기술을 **금지**하고 "체크 시점에 `DIFFICULTY_RUBRIC.md` §3 표를 열어 읽으라"로 바꾼 뒤,
현행 값을 참고로 병기. **정본 수치를 에이전트 파일에 복제하는 것 자체가 drift 생성기**이므로
같은 원칙을 `item-writer` rule 3에도 적용했다.

### B2. `COMMON_TYPES.md`가 필독 목록에서 빠져 있던 2곳 ✅
`catalog/_README.md` L3은 생성 정본을 **"과목 카탈로그 + COMMON_TYPES"** 로 규정하는데,
`item-writer`·`type-proposer` 어느 쪽도 이 문서를 읽지 않았다. `type-proposer` 쪽이 더 심각하다 —
**공통 패턴 후보를 제안하는 주체가 기존 C-nn을 모르는 채 제안**하므로 중복 제안을 구조적으로
거를 수 없었다. 조치: 양쪽 필독 목록에 추가 + 제안 절차 6에 "기존 C-nn과 먼저 대조하고,
이미 등록된 패턴은 새 후보가 아니라 **보강 근거**로 보고"를 명시.

### B3. 「공통 패턴 후보」 보고 주체 불일치 ✅ (정본 수정)
`COMMON_TYPES.md` 머리말이 보고 주체를 `type-extractor`로 적고 있었다. 그러나 260825 분업 개편에서
type-extractor는 **전사 전담(판단 금지)** 이 되고 유형 분석·공통 패턴 관측은 `type-proposer`로
이관됐다. 정본만 옛 주체에 멈춰 있던 것. → `type-proposer`로 정정하고 이력에 append.
**260825 이력 행의 서술은 당시 기록이므로 원문 그대로 두었다**(원칙 3 append-only).

### B4. `item-writer`가 AUTHORING_GUIDE **§1-B**를 안 읽던 문제 ✅
필독 목록에 §1-A(서식)만 있었다. §1-B는 실제 재검토 실패에서 역산된 7항 자기점검인데,
그중 **#4(표 헤더 구분행)·#5(정답 볼드 일관)·#6(`DFn · E코드` 후위 표기 — 병합 시 Tier 근거 훼손)·
#7(연속 `---`)은 작성자만 할 수 있는 일**이고 pre-gate는 #2·#3만 커버한다. 즉 **#4~#7은 담당 배우가
없는 상태**였다. → 필독 목록 추가 + authoring rule 7 신설(반환 전 §1-B 일괄 점검, 분할본 이음매까지).

### B5. 모델 정책 충돌 ✅ (자기점검 방식으로 해소)
`AUTHORING_GUIDE.md` §2는 "수학·과학 검증·**T4 킬러**·최종 QA = Opus, 나머지 ~85% = Sonnet"인데
정의는 `model: sonnet` 고정이었다. **`model: inherit`으로 바꾸지 않았다** — 그러면 전량 Opus가 되어
§2의 비용 정책(85% Sonnet)이 반대로 깨진다. 대신 공식 문서에서 확인한 **호출 시 model override**
(우선순위: 호출 파라미터 > frontmatter)를 활용하는 쪽으로 정리했다:
sonnet 기본 유지 + **T4·수학 서답형 묶음을 sonnet으로 받으면 반환 첫 줄에 경고를 띄우도록** 의무화.
> `⚠️ model policy: T4/math bundle authored on sonnet — AUTHORING_GUIDE §2 asks for Opus`

정책이 문서에만 있지 않고 **런타임에 스스로 드러나게** 만든 것이 요점이다.

### B6. 「학생 오답 도착」 워크플로에 지침이 없던 문제 ✅
CLAUDE.md 흐름표는 이 행을 `item-writer`에 배정하는데, 정의에는 취약 축·사다리·원장에 대한 문장이
**하나도 없었다**(지침 없이 호출되는 행). → `## Weakness-remediation ladders` 절 신설:
축 단위 작업 원칙, T2→T3→T4 사다리 구성 규칙, `fail_code`(DATA_STANDARD §4.1-A) 태깅으로 다음
채점 회차에 **축이 움직였는지 측정 가능**하게 만들 것, `intended_use: practice` 기본,
**원장(ATTEMPT_LOG·MASTERY·WEAK_LEDGER)에는 쓰지 않는다**(원칙 9-b, 승격은 교사 판정).
필독 목록에 `analysis/student/*` · DATA_STANDARD §5.1·§5.3·§4.1-A 추가.

---

## 5. C — 설계 결함

### C1. 페르소나 동질화 → 역할별 분화 ✅ (가장 큰 변경)
감사 시점 11개 중 **9개**가 동일 문장으로 시작했다. 3단계 검토의 값어치는 독립적 판단인데,
작성자와 t1·t2·t3가 같은 자아·같은 사전확률·같은 실패 맹점을 공유하면 라운드를 더 도는 것으로
메워지지 않는다(260826 판정에서 t1·t2가 표면 검토에 머물고 tier-3가 차단 결함 4건을 새로 찾은
사건과 같은 계열의 문제다). 참고로 **가장 잘 쓰인 두 정의는 이미 페르소나가 분화돼 있던 쪽**이다
— `type-extractor`("전사자, 판단하지 않는다"), `solve-back-verifier`("처음 보는 학생처럼 푼다").

| 에이전트 | 변경 후 자아 | 심어준 질문 |
|---|---|---|
| `rev-writer` (t1) | **재현 검증자** | "이 안의 모든 수·카운트·인용을 내가 재현할 수 있는가?" |
| `rev-auditor` (t2) | **출제오류 감사관** | "이 문항이 학생 손에서 어떻게 깨지는가?" |
| `rev-arbiter` (t3) | **규정 준수 심판** | "증거가 주장을 지탱하는가, 지배 정본 조항을 만족하는가?" |
| `forecast-reviewer` (t1) | **체크리스트 검사관** | "이 등급·수치·⚠️가 체크리스트를 통과하는가?" |
| `forecast-auditor` (t2) | **증거 감사자** | "전문성만이 지탱하고 인용이 없는 등급은 어디인가?" |
| `forecast-arbiter` (t3) | **규정 준수 심판** | "인용된 증거가 §4 기준에서 이 등급을 지탱하는가?" |

작성 측 3종(`item-writer`·`type-proposer`·`forecast-writer`)은 **교사·출제 전문가 페르소나를 유지**했다
— 그쪽은 전문성이 곧 산출물이므로 분화가 오히려 손해다.

### C2. 호출 프롬프트를 통한 오염 차단 ✅
기존 "독립 먼저" 규칙은 **tier-1 보고서 파일**만 대상이었다. 실제 오염 경로는 메인 루프가 Task
프롬프트·§6-b 회람문에 t1 지적 요약을 넣는 것이고, 그러면 규칙이 무력화되면서 **기록도 남지 않는다.**
→ `rev-auditor`(규칙 2-b)·`forecast-auditor`에 명문화: 호출 메시지가 t1 내용을 실어 왔으면
독립 검증을 먼저 끝내고, **그 사실을 반환 헤더에 적는다**(`⚠️ invocation carried t1 findings`).
파일만 막고 프롬프트가 새면 독립성은 연극이다.

### C3. "환경 분리" 주장 → 검증 가능한 근거로 교체 ✅
`type-extractor`는 "opencode side", `rev-arbiter`는 "Runs OUTSIDE the authoring environment"라고
선언했다. 그러나 **리포에 `.opencode/` 설정이 없고**(확인함), 11개 정의는 전부 `.claude/agents/`에
Claude Code frontmatter로 존재한다. CLAUDE.md 흐름표가 스스로 경고한 *"에이전트 라벨 도용 금지 —
라벨을 실제 배우와 일치시킨다"* 와 같은 종류의 문제다.
→ 독립성의 근거를 **검증 가능한 두 가지**(fresh context + 모든 주장 자가 재검증)로 교체하고,
"어느 클라이언트가 실행했는가"를 보증처럼 인용하지 말라고 못박았다. 역할 분리 자체는 그대로 유효하다.
> ⚠️ **미확인**: 전역 opencode 설정(`~/.config/opencode` 등)은 확인하지 않았다. opencode 쪽 실행이
> 실제로 존재한다면 **그쪽에도 대응 정의 파일이 있어야** 하고 두 벌의 동기화 규칙이 필요하다.
> 그래서 `REV_GUIDE.md` §3·§5의 `[opencode]` 라벨은 **건드리지 않았다** — 운영 사실은 사용자가 안다. §7-③.

### C4. WIP 슬러그 충돌 ✅
`item-writer`는 description상 "unit/type bundle 단위 병렬"인데 WIP 경로는 `<actor>_<YYMMDD>_<task>.md`
였다. 동일 배우 2인이 같은 `<task>`를 쓰면 **서로의 `NEXT`를 덮어써 배타 소유가 깨진다.**
→ CLAUDE.md 규격 ②와 `item-writer` 정의에 슬러그 고유성 의무 명시(세트ID·유형 묶음에서 유도,
`task`/`set` 같은 일반명 금지). 더불어 **t1·t2 동시 실행 금지**를 명문화했다 — 둘 다 같은
`_index.md`·`REV_LOG.md`에 행을 붙이므로 병렬은 원장 손상이다(§5 마지막 줄의 실제 적용).

### C5. 자동 위임 트리거 ✅
`description`은 자동 위임 판단 근거인데 `rev-writer`·`rev-auditor`·`item-writer` 3종에만
"Use when…" 문장이 없었다. → 3종 모두 추가. 반대로 **"use proactively" 계열은 넣지 않았다** —
게이트 순서가 엄격한 파이프라인에서 자동 위임 유도는 pre-gate를 건너뛰게 만든다.

### C8. 진행 맵 drift + 사용자 가시성 ✅
(a) forecast 파이프라인 표기가 정본과 갈려 있었다:
REV_GUIDE `[review: t1 confirmed | t1⇄t2 ≤5R + arbiter on dispute, unconfirmed]` vs
에이전트 4종 `[4 review t1 | t1⇄t2 ≤5R]`. → ASCII 정렬을 깨지 않기 위해 압축 맵은 유지하고,
**분기 주석을 4개 정의에 동일 문구로 삽입**해 의미를 일치시켰다.
(b) 더 중요한 문제: REV_GUIDE §3 rule 5는 "**사용자가** 위치+결과를 한눈에 봐야 한다"고 요구하지만
**서브에이전트의 return 값은 사용자에게 보이지 않는다**(메인 루프만 받는다). 중계 의무가 어디에도
없어서 이 요구는 조용히 실패할 수 있었다. → CLAUDE.md 규격 **③ 진행 맵 중계** 신설:
3부 헤더를 요약 없이 그대로 옮기고 `▲ blocked`·`HOLD`·`⚠️`는 원문 유지.

### C9. 산출물 언어 ✅
정의는 전부 영어, 산출물(문항·검토서·판정서·원장 행)은 한국어인데 **어느 정의도 그것을 적지 않아**
영어 초안이 나올 여지가 열려 있었다. → 11개 전부에 `**Output language**: … Korean` 한 줄 추가
(실측 11/11). 정의가 영어인 것은 토큰 경제상 유지하되, 산출물 언어와 구분됨을 명시.

---

## 6. 반영하지 않은 것과 그 사유

| 항목 | 판단 | 사유 |
|---|---|---|
| **C6 `disallowedTools` 적용** | 미적용 | 11개 전부 셸을 가져 도구층 차단은 우회 가능. "차단됐다"는 착각만 만들고 실제 경계는 문서층이 진다. 문서층(§5 + 정의 + 규격 ④)을 택했다. |
| **C6 `effort` 확대** | **2건만 적용** | `forecast-auditor`(sonnet인데 rev-auditor와 동일 역할 — 체급 비대칭 보정)와 `solve-back-verifier`(필수 게이트의 맹목 풀이)에 `effort: high`. 나머지 확대는 비용·행동을 바꾸므로 사용자 판단 영역. |
| **C6 `maxTurns`** | 미적용 | ≤5라운드 제한의 기술적 담보로 유용하나, 적정값을 실측 없이 정할 수 없다. 잘못 잡으면 정상 라운드가 잘린다. |
| **C7 cohort 9중복** | 유지 | 서브에이전트가 프로젝트 CLAUDE.md를 자동 수신하는지 확인하지 못했다. 정의에서 빼면 정보가 사라질 수 있어 **9곳 문장을 완전히 동일하게 유지**하는 쪽을 택했다 — 학년 승급 시 한 줄로 일괄 갱신 가능:<br>`sed -i 's/grade 1 (2026)/grade 2 (2027)/' .claude/agents/*.md` |
| **REV_GUIDE §3·§5의 `[opencode]` 라벨** | 유지 | C3 참조. 실제 실행 주체는 사용자만 안다. 잘못 지우면 운영 사실을 왜곡한다. |
| **문항·카탈로그·원장·도구 코드** | 무변경 | 감사 범위 밖. append-only 원장에는 행을 하나도 쓰지 않았다(원칙 9-b). |

---

## 7. 사용자 확인 요청 (원칙 8 — 승인 전 미결)

- [ ] **① `effort` 확대 여부** — 현재 `forecast-auditor`·`solve-back-verifier` 2건만. `rev-auditor`·
      `rev-arbiter`·`type-proposer`에도 `effort: high`를 줄 것인가? (판정 품질 ↑ / 비용·시간 ↑)
- [ ] **② `item-writer` 분리 여부** — 현행은 sonnet 고정 + 자기 경고(B5). 대안은
      `item-writer`(T1~T3, sonnet) / `item-writer-hard`(T4·수학, opus) 2종 분리. 분리는 정의가
      하나 늘고 동반 갱신 대상도 늘어난다.
- [ ] **③ opencode 실행 실태 확인** — `type-extractor`가 실제로 opencode에서 도는가?
      돈다면 opencode 쪽 정의 파일이 별도로 필요하고, 두 벌의 동기화 규칙을 CODE_REGISTRY §6
      온보딩 목록에 넣어야 한다. 안 돈다면 REV_GUIDE §3·§5의 `[opencode]` 라벨을 정정해야 한다.
- [ ] **④ untracked 정의 8개 커밋 여부** — `forecast-*` 4종·`rev-*` 3종·`type-proposer`는 커밋
      이력이 없다(§2.3). 지금 커밋해두지 않으면 다음 사고 때 되돌릴 기준이 §8 해시표뿐이다.
- [ ] **⑤ 본 보고서의 검토서 승격 여부** — 특례로 검토·수정을 한 주체가 같으므로, 원칙 8을
      엄격히 지키려면 이 문서를 `analysis/rev/`에 검토서로 등재하고 `REV_LOG.md`에 행을 남겨야 한다.
      **원장 오염을 피하려 지금은 쓰지 않았다** — 승인하시면 등재한다.

---

## 8. 검증 로그 (원칙 11 — 명령과 출력을 그대로)

```
$ claude --version                     → 2.1.246 (Claude Code)
$ python (yaml.safe_load 전 파일)      → 11/11 프론트매터 파싱 성공, name == 파일명 11/11
$ grep -l 'Shell is not a write loophole' .claude/agents/*.md | wc -l   → 11
$ grep -l 'Output language' .claude/agents/*.md | wc -l                 → 11
$ 줄바꿈 코드 재확인                    → CRLF 7 / LF 4 (감사 전과 동일, 변동 0)
$ 편집 스크립트                         → 전 치환 단일 매치(count==1) 통과, 중단 0건
```

**미실행(=통과 아님)**: 실제 서브에이전트 호출 테스트는 하지 않았다. `effort` 키는 CLI 바이너리
문자열과 공식 문서로 지원을 확인했을 뿐 **런타임 검증은 없다.** 다음 호출 때 두 파일
(`forecast-auditor`·`solve-back-verifier`)이 정상 기동하는지 확인하고, 만약 거부되면 그 두 줄만
지우면 된다 — 나머지 변경과 독립적이다.

## 9. 해시 (변경 전 → 변경 후, SHA-256)

| 파일 | 변경 전 | 변경 후 |
|------|---------|---------|
| `.claude/agents/forecast-arbiter.md` | `b52d1c4c…d246` | `d52725cd…4b84` |
| `.claude/agents/forecast-auditor.md` | `840fad1f…2acc` | `70b2d643…03da` |
| `.claude/agents/forecast-reviewer.md` | `c454289a…ee0b` | `22695103…f7cb` |
| `.claude/agents/forecast-writer.md` | `60a8b14d…421d` | `1af997fa…0ee8` |
| `.claude/agents/item-writer.md` | `9bdc2c9b…49f6` | `01a8dfa7…bcf6` |
| `.claude/agents/rev-arbiter.md` | `b0f43249…bc21` | `ceb3a254…bfe5` |
| `.claude/agents/rev-auditor.md` | `02dcbf29…f0da` | `31082ca2…15cc` |
| `.claude/agents/rev-writer.md` | `02ed8fad…2ffb` | `d2e8083e…bd5f` |
| `.claude/agents/solve-back-verifier.md` | `28a02da9…ea6e` | `dac372ca…797f` |
| `.claude/agents/type-extractor.md` | `225403c8…2c0a` | `e20f892d…38c7` |
| `.claude/agents/type-proposer.md` | `85756bcf…c9e0` | `188b3f23…71e2` |
| `CLAUDE.md` | `6ca4c7ce…a085` | `e31a274b…ffe6` |
| `analysis/REV_GUIDE.md` | `a03f7128…badf` | `ee9af3ac…d98e` |
| `analysis/catalog/COMMON_TYPES.md` | `edef1906…25ee` | `dd3541e3…3e05` |

앞 8자리·뒤 4자리 표기. 전체 값은 `sha256sum` 재실행으로 대조 가능하며,
변경 전 값은 본 세션 시작 시점(수정 이전)에 측정한 것이다.

## 이력
- 260826 신설 — 서브에이전트 정의 11종 감사 및 특례 수정. 반영 항목 A1·A2·B1~B6·C1~C5·C8·C9,
  보류 항목 C6(부분)·C7. 정본 3개 동반 갱신(CLAUDE.md 규격 ③④ · REV_GUIDE §5 Tool-grant coupling ·
  COMMON_TYPES 보고 주체 정정).
