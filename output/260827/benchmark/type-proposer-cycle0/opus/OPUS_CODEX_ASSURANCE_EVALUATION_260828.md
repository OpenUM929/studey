---
artifact_kind: external_opus_codex_assurance_evaluation
status: partially-satisfactory
date: 2026-08-28
executor: external Claude Code Opus
scope: non-canonical advisory capability evaluation
canonical_changes: none
---

# Codex/OMX 보증 능력 — 외부 Opus `type-proposer` 역할 지원 평가

> 한 Opus 메인 세션에서 수행. 서브에이전트·백그라운드·병렬·자동 계속·자동 재시도 없음.
> 정본 카탈로그·원장·코퍼스·WIP·REV_LOG·기존 산출물·매니페스트 미수정, 무커밋. 아래 지정 파일 1건만 작성.

## 0. 범위 선언 — 실행된 것과 계획된 것의 분리

본 평가는 **실제로 실행된 Codex/OMX 단독(solo) 산출물 49건**이 외부 Opus `type-proposer` 역할에 요구되는 작업을 어느 정도 지원하는가를 판단한다. 평가 대상 실행은 **단일 소유자(Sol) 단독 실행**이며, `TEAM_PREFLIGHT_260827.md`가 자체 하드스타트 검사에서 `$TMUX` 공란·tmux 미설치·`.omx/state/team/` 부재를 실측해 `BLOCKED — no actual independent Codex team runtime`으로 선언한 상태에서 나왔다. 따라서 `AGENTS.md` 「Team staffing preflight and model assignment」의 4개 Sol 레인(author / evidence-auditor / adversarial-critic / gatekeeper)과 `.codex/agents/*.toml` 4건은 **문서상 설계이며 실행 증거가 아니다** — 본 평가는 그 설계를 실행된 보증으로 계상하지 않는다. 동결 산출물 49건 중 독립 감사·적대적 비평·게이트키퍼 산출물은 **0건**이다. 본 회신은 Codex/OMX·Sol·단독 실행·장래의 팀 중 어느 것도 외부 Opus의 대체로 선언하지 않으며, 어떤 라운드도 종결하지 않고 어떤 정본 변경도 승인하지 않는다. C1~C8(260827 감사)은 요청서 지시대로 **미반영 상태 그대로** 평가했고, 부록 A의 해시 재실측(49/49 동일)이 그 미반영을 증거로 확정한다.

> 인용 정정 1건: 요청서 증거목록 7번이 지목한 `AGENTS.md` 절 **「Sol-to-Opus substitution evaluation」은 실재하지 않는다**(실측 헤딩 13개 전수 확인). 해당 내용은 「Codex/OMX persona and scope guard」(L37-40)와 「Team-assisted capability evaluation (future, user-authorized only)」(L83-95)에 있다. 본 평가는 이 두 절을 대신 읽었다. → C9.

## 1. 6문항 판정표

| # | 질문 | 판정 | 직접 증거 | 한계 |
|---|---|---|---|---|
| 1 | 증거 규율 (추적성·fail-closed·무창작) | **partially-satisfactory** | 무창작은 확인됨 — 산출물 49건에 신규 유형 ID 주조 0건, 정답 주장 0건, 원장 행 0건, 페이지(pNN) 인용 0건(렌더 부재를 명시하고 행 인용으로 대체). `catalog_diff` 9건은 모두 "no application; decision request only"를 명시. 제어바이트 오염 0건(49/49). 260827 감사에서 대표 단위 인용 범위 29건 중 28건이 원문과 완전 일치. `EX-info-20252M`은 CODE_REGISTRY §1·§3·§6을 행 단위로 인용해 `IN` 미등록으로 fail-closed 했고, `EX-history-20252M`은 `history.md` L131·L136·L180의 실재 미결(E-6 유형화 미완)을 정확히 인용해 HOLD 했다. | 그러나 **자기 보고 수치가 거짓인 사례가 실증**됐다 — 대표 단위 결론의 "Coverage: 29/29"는 선택형 1건 누락 + 복제 행 1건이 상쇄된 결과이고 고유 커버리지는 28/29다(C3). 본 세션 재확인: 해당 문항(transcript L191-205, 선택형 최고배점 `[3.2 점 ]`, 산 수용액과 금속의 산화·환원, 비커 I/II 양이온 수 표)은 science-M 산출물 전체에서 L19x·L20x 인용이 **0건**이다. 단위 완료 요건 1번이 행 수 대조여서 이 결함을 통과시킨다(fail-open, C4). |
| 2 | 분석 완결성 (`type-proposer` 계약 대비) | **unsatisfactory** | 계약(`.claude/agents/type-proposer.md`) 절차 3~8 대비 실측: **변형 축 0건**(`variation ax`·`변형` 언급 0/49 파일), **중요도 별표 0건**(`★` 0/49), **신규 유형 초안 0건**, **COMMON_TYPES 대조 0건**(0/49) — science-M이 관찰한 "ㄱ·ㄴ·ㄷ 3진술 합답형"은 이미 등록된 `C-01`(COMMON_TYPES.md L21)인데 대조 없이 "later check"로 연기됐다. **HARVEST_LOG·EXTRACTION_LOG 초안 0건**, verify_log 행 0건(트랙이 스스로 "prohibited in this track"으로 배제). 통합은 대표 단위에서 27행/25라벨의 1문항 1라벨이라 계약의 "5-12 types"를 충족하지 않는다. | 계약 절차 2가 요구하는 **T1-T4 난이도 등급이 11개 단위 중 5개**(english-M·history-M·science-F·science-M·social-M)에만 존재한다. 계약 규칙 5(한국어 산출)는 **11개 중 3개**(korean-F 40.1%·social-M 39.6%·history-M 34.5%)만 충족하고 나머지 8개는 영문 산문(한글 비율 ≤8.5%)이다. 표 스키마도 단위마다 달라(`item` / `written N` / `선택 N`, 5~6열 혼재) C4가 요구하는 식별자 기반 기계 대사를 현 상태로는 걸 수 없다. **다만 이는 정직성 결함이 아니라 산출물 종별 차이다** — 트랙 스스로 대표 단위 결론에서 "verified evidence-index, not a type proposal fit for review"라고 적었고, 그 자기평가가 본 판정과 일치한다. |
| 3 | 보증 품질 — (a) 실제 단독 실행 / (b) 문서상 팀 설계 | **unsatisfactory** ((a) unsatisfactory · (b) blocked — 증거로 계상 불가) | (a) 단일 소유자가 작성과 자기검증을 겸했고, 유일한 대사 게이트("assigned + held items equals meta.yml items")가 결함을 통과시키는 fail-open임이 실증됐다. 독립 검토·적대적 비평·게이트 판정 산출물은 49건 중 0건. (b) 설계는 실재한다 — `.codex/agents/` 4개 정의, `TEAM_PREFLIGHT`·`PILOT_TASK_MATRIX`의 레인·모델·깊이·배타 출력 경로 표. 그러나 하드스타트 3개 조건이 전부 blocked로 기록돼 **한 번도 실행되지 않았다**. | **계획된 레인·모델·페르소나는 실행 증거가 아니다.** `AGENTS.md` L93은 "A team plan, solo output, or abstention-only baseline **fails preflight**"라고 스스로 규정하므로, 현재 상태는 그 규정의 정의상 **보증 실패**다. 본 평가는 장래 팀이 어떤 품질을 낼지에 대해 아무 판단도 하지 않는다 — 판단할 증거가 없다. |
| 4 | 운영 안전 (정본 보호·역할 경계·한계 보고) | **partially-satisfactory** | 정본 보호 확인 — 260828 재실측에서 동결 입력 33건 `ok=33 mismatch=0 missing=0`, 산출물 49건 `ok=49 mismatch=0 missing=0`. 비가역 조작 없음(ID 미주조·상태 승격 없음·원장 무기입). 역할 경계 보존 — 어떤 문서도 자신을 `type-proposer`라 칭하지 않고, 22개 파일이 "advisory only"를 명시하며, 판정·승인·릴리스를 전부 외부 권한으로 넘겼다. 런타임 한계를 실측 증거(`$TMUX`·`tmux -V`·`omx --version 0.20.5`·`.omx/state/team/` 부재)로 적고 존재하지 않는 팀 산출물을 만들지 않았다. | **거버넌스 충돌 1건이 미해소다.** `AGENTS.md` L93은 preflight가 blocked이면 "do not compare it with Opus ... or send an external benchmark prompt"라고 금지하는데, 트랙은 blocked 상태에서 비교 요청서(`260827_01`)와 블라인드 채점표(`260827_02`)를 실제로 산출·발신했다. 실제 비교 점수는 나오지 않았으므로 피해는 없으나 **사용자 승인 예외를 명시적으로 기록하거나 트랙의 "comparison" 규정을 철회**해야 한다(C10). 또한 회람문 `260827_01`의 제어바이트 오염(0x07×4·0x08·0x09·0x0b)이 **오늘까지 그대로**여서 REV_GUIDE §6-b 자기완결 요건과 CLAUDE.md 원칙 9-b(ASCII 표식)를 계속 위반한다(C1 미반영). |
| 5 | 사용자 만족도 (강한 팀으로 Opus 격차를 보전한다는 요구 대비) | **partially-satisfactory** | 상세는 §2 3행 표. 요약: 315문항·11단위에 걸친 행 단위 증거 색인으로서는 실질 가치가 있고 경계 보존도 명확하지만, **"강한 팀"은 한 번도 구성되지 않았다** — 사용자의 전제(팀으로 격차 보전)는 이번 실행에서 **시험된 바가 없다**. | 만족도는 "무엇으로 쓸 것인가"에 따라 셋으로 갈린다. 하나의 값으로 답하면 오도된다. |
| 6 | 허용 shadow 범위 | **satisfactory** (범위를 §3 표로 한정하는 조건에서) | 트랙이 실제로 잘 수행한 활동군이 존재한다 — 동결·해시·매니페스트 관리(82건 전수 일치), 행 단위 증거 색인(28/29 정확), 미결 정책의 fail-closed 식별(info-M `IN` 미등록, history-M E-6 미완), 한계의 무은폐 보고. 이들은 판단이 아니라 **증거 준비**이며 외부 권한을 침식하지 않는다. | §3 표의 "불가" 행에 속한 활동 — 유형 배정 제안·통합·변형 축·별표·ID 주조·상태 승격·검토 수렴 선언·판정·투입 게이트·벤치마크 채점 — 은 **정책이 명시적으로 바뀌기 전까지 전부 외부 Opus 권한**이며, shadow 실행분은 어떤 경우에도 정식 산출물로 제출되지 않고 사후 대조용으로만 보관된다. |

## 2. 만족도 3행 표

| 용도 | 만족도 | 근거 | 사용 조건 |
|---|---|---|---|
| (a) 자문용 증거 색인 | **partially-satisfactory** | 11단위 315문항에 대해 문항→transcript 행 범위 매핑을 제공하고, 대표 단위 인용 정확도가 28/29다. 증거 공백을 창작으로 메우지 않았다. | **C3·C5 반영 전에는 재사용 금지.** 대표 단위는 문항 1건 누락 + 복제 1건이 남아 있고, 11개 단위 중 10개의 HOLD 근거가 260826에 **이미 종결된** 결정(CODE_REGISTRY §6 (a) 병합 · (b) 연장, 체크박스 `[x]`)을 미결로 서술한다. CODE_REGISTRY를 실제 참조한 단위는 `EX-info-20252M` 1개뿐(4개 파일, 전수 확인). |
| (b) `type-proposer` 산출물 | **unsatisfactory** | 계약이 요구하는 통합·변형 축·별표·신규 항목 초안·COMMON_TYPES 대조·원장 초안이 전부 0건이다(§1 질문 2). | 이 용도로는 사용할 수 없다. 대체 경로는 두 가지 — (i) 외부 Opus가 이 색인을 **입력**으로 받아 유형 분석을 수행하거나, (ii) 트랙이 C7(ii)를 택해 문서 제목·frontmatter를 "evidence index"로 자기규정한다. (ii)가 현 실체에 부합하고 저비용이다. |
| (c) 벤치마크 후보 | **unsatisfactory** | 세 가지 구조적 사유가 그대로다 — 예약 단위 `EX-science-20252M`의 블라인드성이 양측 열람으로 소진됐고, 채점표가 감사 보고서와 유형 분석을 같은 루브릭에 올리며, 결정적 검사(`10 + 10 + 9 = 29`)가 fail-open임이 실증됐다. 더해 **비교 대상인 Opus 측 유형 분석 산출물이 존재하지 않는다**(`RECOVERY_MANIFEST`가 원본 삭제·복구 불가로 기록). | C8 3건 충족 전까지 채점 금지. 교정 가능한 결함이며 영구 결격은 아니다. |

## 3. 허용 Codex/OMX shadow 범위

원칙: **증거를 준비하는 일은 허용, 판단·명명·승인·게이트는 외부 Opus 권한.** shadow 산출물은 별도 경로에 보관하고 정식 산출물로 제출하지 않는다.

| 활동 | Codex shadow 허용? | 이유 | 유지되는 Opus 권한 |
|---|---|---|---|
| 동결·해시·매니페스트 작성 및 재검증 | **허용** | 결정론적 기계 작업이며 판단이 없다. 82건 전수 일치로 능력이 실증됐다. | 무결성 결과의 채택 여부 |
| 문항→transcript 행 범위 증거 색인 | **허용** (유형 라벨 없이) | 전사 인용은 사실 진술이고 28/29 정확도가 실증됐다. `HOLD-XXX` 같은 준-유형 라벨은 붙이지 않는다. | 유형 배정 일체 |
| 식별자 기반 커버리지 대사(C4 규격) | **허용, 권장** | fail-open 게이트의 재발 방지가 shadow의 최우선 가치다. | 게이트 수용기준의 확정 |
| 기존 유형 **후보 검색 결과** 나열 | **허용** (처분 없이) | "이 유형들이 검색됐다"는 조회이고 "이 유형이 맞다"는 판단이다. 후자는 금지. | 중복의미 판정·조건부 매칭 기준 |
| 전사 결함·증거 공백 플래그 | **허용** | EQED 공란·렌더 부재·합답 조합 손실 등은 관측이다. | 결함의 처리 방침 |
| 정책 미결/기결 상태 확인 및 인용 | **허용** | info-M·history-M이 모범 사례다. 단 **11단위 전수에 일관 적용**해야 하며, 1개 단위에만 적용한 것이 F7의 실체다. | 정책 자체의 해석·변경 |
| 회람문·PRD·preflight 기록 작성 | **허용** | 조정자 고유 업무다. 단 §6-b 자기완결·ASCII 요건 준수(C1 재발 금지). | 회람 내용의 승인 |
| 도구·게이트 실행과 로그 첨부 | **허용** | 명령·출력·경고·카운트·exit code 전량 보고를 조건으로 한다. | 통과/미통과 판정 |
| 유형 배정 제안·통합·변형 축·중요도 별표 | **불가** | `type-proposer` 계약의 본체다. 실행 실적 0건이며 계약 요건 미충족이다. | 전부 |
| 신규 유형 ID 주조·접두어 정책 결정 | **불가** | 비가역이다(CLAUDE.md 원칙 9-a, CODE_REGISTRY 운영원칙 ①). | 전부 |
| 상태 승격 `검증(부교재)` → `검증` | **불가** | 별표 축 재산정을 동반하는 정본 판단이다. | 전부 |
| 검토 수렴 선언·tier-2/3 판정 | **불가** | REV_GUIDE §3 rule 2 — 종결권은 tier-3에 있다. | 전부 |
| solve-back 검증·투입 허가 게이트 | **불가** | 외부 전용 역할이다(AGENTS.md 「External-only」). | 전부 |
| 벤치마크 채점·동등성/대체 주장 | **불가** | `AGENTS.md` L93·L95. 사용자가 정책을 명시적으로 바꾸기 전까지. | 전부 |

shadow 실행의 전제 3가지: (i) 산출물은 `output/<YYMMDD>/shadow/` 등 정식 경로 밖에 두고 정식 산출물로 제출하지 않는다 (ii) 각 문서 머리에 "shadow — not a proposal, not compared to Opus"를 명시한다 (iii) 사후 대조는 외부 Opus 산출물이 **먼저 확정된 뒤에만** 수행한다(선행 열람 금지 — 블라인드성 소진 재발 방지).

## 4. 수정 요청 (승인 대상, 신규분만)

> C1~C8(260827 감사)은 **전부 미반영 상태로 유효**하다 — 해시 49/49 동일이 그 증거다. 아래는 이번 평가에서 새로 확인된 항목만 적는다. 원칙 8에 따라 본 평가는 자기가 작성하지 않은 문서를 직접 고치지 않는다.

- [ ] **C9 (요청서 인용 정정)** `260828_01_opus_codex_assurance_evaluation_request.md` 증거목록 7번의 `AGENTS.md` 절 이름 「Sol-to-Opus substitution evaluation」을 실재 헤딩으로 정정한다 — 「Codex/OMX persona and scope guard」(L37-40) + 「Team-assisted capability evaluation (future, user-authorized only)」(L83-95). 수용기준: 정정 후 `grep -n "^## " AGENTS.md` 출력에 인용된 절 이름이 문자 그대로 존재할 것(CLAUDE.md 원칙 9-c-i 준용).
- [ ] **C10 (거버넌스 충돌 해소)** preflight가 `BLOCKED`인 상태에서 비교 요청서·블라인드 채점표를 산출·발신한 것은 `AGENTS.md` L93의 "do not compare it with Opus ... or send an external benchmark prompt"와 충돌한다. **둘 중 하나**를 택해 기록한다 — (i) 사용자 승인 예외를 근거·일자와 함께 `AGENTS.md` 또는 트랙 문서에 명시하거나, (ii) 트랙의 "comparison" 규정을 철회하고 `codex-only/`를 **advisory evidence-index 트랙**으로 재규정한다(C7(ii)와 동시 처리 가능). 수용기준: `260827_01`·`260827_02`·`PILOT_TASK_MATRIX_260827.md`·`codex-only/README.md` 4건에서 "comparison/benchmark" 어휘와 실제 권한 상태가 일치할 것(원칙 10 동반 갱신).
- [ ] **C11 (산출 스키마 통일 — C4의 선행 조건)** 11개 단위의 배정표 스키마가 서로 다르다(문항 라벨 `1` / `written 1` / `선택 1`, 5~6열 혼재, T1-T4 난이도 열은 5개 단위에만 존재, 한국어 산문은 3개 단위만). C4의 식별자 기반 fail-closed 대사는 **단일 스키마 없이는 걸 수 없다**. 수용기준: 문항 식별자 표기 1종 확정 + 전 단위 동일 열 집합 + 스키마 준수를 검사하는 명령과 그 출력(경고 0줄·기대 카운트 병기)을 로그로 첨부.
- [ ] **C12 (COMMON_TYPES 대조 수행 또는 관찰 문장 철회)** 계약 절차 6은 공통 패턴 후보를 **`COMMON_TYPES.md`와 먼저 대조**하도록 요구하나 49건 어디에도 대조 흔적이 없다(언급 0건). science-M 슬라이스 1이 관찰한 "ㄱ·ㄴ·ㄷ 3진술 합답형"은 이미 등록된 **`C-01`**(`COMMON_TYPES.md` L21)이다. **둘 중 하나** — (i) 전 단위에서 C-00~C-07 대조를 수행해 기등록 패턴은 **보강 인용**(어느 문항·어느 행)으로 적거나, (ii) 공통 패턴 관찰 문장을 삭제하고 이 항목을 외부 Opus 범위로 넘긴다.

## 5. 정본 무변경·무커밋 선언

**본 평가는 어떤 정본도 변경하지 않았다.** 카탈로그(`analysis/catalog/*`), 원장(`analysis/REV_LOG.md`·`HARVEST_LOG.md`·`EXTRACTION_LOG.md`·`ATTEMPT_LOG.tsv` 등), 코퍼스(`corpus/*`), WIP(`analysis/wip/*`), 기존 산출물(`output/260827/**`의 기존 파일 전부 — 매니페스트 2건 포함), 도구 코드(`tools/*`), 에이전트 정의(`.claude/agents/*`·`.codex/agents/*`) 어느 것도 **읽기 전용으로만** 접근했다. 커밋·스테이징을 수행하지 않았다. 서브에이전트·백그라운드·병렬·자동 계속·자동 재시도를 사용하지 않았다.

작성한 파일은 **이 한 건뿐**이다: `output/260827/benchmark/type-proposer-cycle0/opus/OPUS_CODEX_ASSURANCE_EVALUATION_260828.md`.

`analysis/REV_LOG.md`에 행을 추가하지 않았다 — 본 회신은 격리된 능력 평가이며 공식 검토 라운드가 아니다. C1~C8은 이번 평가 중 반영하지 않았다.

## 6. 총괄 결론

**`partially-satisfactory — advisory-only, not comparable to Opus role output`**

보충 3줄. (1) 실행된 것은 **단독 실행**이고, 사용자가 요구한 "격차를 보전하는 강한 팀"은 preflight 단계에서 blocked로 멈춰 **한 번도 시험되지 않았다** — 문서상 4개 Sol 레인은 설계이지 증거가 아니다. (2) 실제 산출물은 **검증된 증거 색인**으로서 실질 가치가 있으나(해시 82건 전수 일치, 인용 정확도 28/29, 무창작·경계 보존), `type-proposer` 계약의 분석 층(통합·변형 축·별표·신규 항목 초안·COMMON_TYPES 대조)은 **전부 0건**이므로 역할 산출물로는 대체 불가다. (3) C3(대표 단위 누락·복제)과 C5(이미 종결된 결정을 미결로 서술한 10개 단위)가 미반영인 한 **자문 색인으로서의 재사용도 조건부**이며, 비교·채점은 C8 3건 충족 전까지 별도로 금지된다.

---

## 부록 A — 이번 세션 실측 로그

| # | 검사 | 방법 요지 | 기대 | 실측 | 판정 |
|---|---|---|---|---|---|
| A1 | 동결 입력 무결성 (260828 재실측) | `INPUT_MANIFEST_260827.tsv` 33행의 sha256 + bytes 대조 | 불일치 0 / 부재 0 | `ok=33 mismatch=0 missing=0` | pass |
| A2 | 동결 산출물 무결성 (260828 재실측) | `CODEX_ARTIFACT_MANIFEST_260827.tsv` 49행 대조 | 불일치 0 / 부재 0 | `ok=49 mismatch=0 missing=0` → **C1~C8 미반영 확정** | pass |
| A3 | 회람문 제어바이트 | 대상 `.md` 4건 바이트 스캔 | 오염 0 | `260827_01`: 0x07×4·0x08×1·0x09×1·0x0b×1 **잔존** / `260828_01` 요청서·릴레이·`260827_02`: clean | C1 미반영 / 260828분은 개선 |
| A4 | 누락 문항 재확인 | `corpus/EX-science-20252M/transcript.md` L191-206 직접 열람 + science-M 산출물에서 L19x·L20x 인용 검색 | 인용 존재 | 원문 실재(산 수용액과 금속의 산화·환원, 비커 I/II 양이온 수 표, `[3.2 점 ]`) / 산출물 인용 **0건** | C3 미반영 확정 |
| A5 | 계약 요소 언급 전수 | 49건에서 `변형`·`★`·`HARVEST_LOG`·`EXTRACTION_LOG`·`COMMON_TYPES`·`TYPE_MASTER`·`DIFFICULTY_RUBRIC`·`_README` 검색 | — | 전부 **0파일** / `curriculum_2022` 15파일 / `CODE_REGISTRY` 4파일(전부 info-M) | §1 질문 2 근거 |
| A6 | 난이도 등급 커버리지 | 단위별 `tier`·`Tier`·`난이도` 언급 슬라이스 수 | 11/11 단위 | **5/11 단위**(english-M·history-M·science-F·science-M·social-M) | 계약 절차 2 미충족 |
| A7 | 산출 언어 (계약 규칙 5) | 단위별 한글 문자 비율 측정 | 한국어 산출 | korean-F 40.1% · social-M 39.6% · history-M 34.5% / 나머지 8단위 ≤8.5%(영문 산문) | **3/11 충족** |
| A8 | 경계 선언 | 49건에서 `advisory only` / 무적용·decision-request 문구 검색 | — | `advisory only` 22파일 / 무적용 선언 9파일 | 경계 보존 근거 |
| A9 | 팀 실행 증거 | `codex-team/` 하위 산출물 존재 여부 | 존재 시 팀 실행 | **디렉터리 부재, 산출물 0건** — 감사·비평·게이트 레인 실행 증거 없음 | 질문 3(b) blocked 근거 |

## 부록 B — 본 평가의 명시적 한계

1. **재분석이 아니다.** 본 평가는 능력·프로세스 평가이며, 260827 감사가 문항 단위로 대조한 31문항(전체 315의 약 10%) 위에 기계 검사 9종을 더한 것이다. 나머지 단위의 **유형 배정 타당성은 여전히 미검증**이다.
2. **정답·난이도·페이지를 주장하지 않았다.** 11개 단위 전부 `render_dpi: null`·`_images` 부재이며 `answer_key`는 동결 증거 사슬 밖이다. 이 제약은 Codex 산출물과 본 평가에 **동일하게** 적용된다.
3. **단일 세션·단일 관찰자다.** 본 평가 자체에 대한 독립 교차검토는 없다. tier-1/2/3 판정이 아니며 어떤 라운드도 종결하지 않는다.
4. **장래 팀 성능을 예측하지 않았다.** 질문 3(b)의 `blocked`는 "팀이 못한다"가 아니라 "실행 증거가 0건이라 판단할 수 없다"는 뜻이다.
5. **최근 정본 변경분과 본 트랙의 인과를 분리하지 못했다.** 260827 이후 `analysis/`·`corpus/` 등에서 297개 파일이 갱신됐으나 이는 S1 리파인 웨이브 등 **다른 작업**의 산물이다. 본 트랙의 무침습은 동결 33건 해시 일치(A1)로만 입증되며, 그 밖의 경로에 대해서는 인과를 주장하지 않는다.
