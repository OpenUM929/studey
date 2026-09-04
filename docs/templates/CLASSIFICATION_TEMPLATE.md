# 1차 분류 표준 산출물 템플릿 — provenance-first (v1.0)

> **용도**: `type-proposer`가 `corpus/<ID>/transcript.md`를 한 문항씩 재독해해 만드는 **1차 분류 제안서**. 승인 전까지 정본 미반영(PROVISIONAL).
> **위치**: `output/<YYMMDD>/<YYMMDD>_<NN>_<corpus-id>_classification.md` + 동반 TSV 2종(`_items.tsv`, `_types.tsv`) — 쌍으로 검증.
> **정본 참조**: `CLAUDE.md` 작업흐름표 · `AGENTS.md` 팀 표 · `DATA_STANDARD §5.7/5.7-A` · `analysis/REV_GUIDE §3/6-b` · `output/260829/ruler-candidate/ACCEPTANCE_SCHEMA.candidate.md` (v1 후보, S2 자격 필요)
> **작성**: Codex/OMX Sol (외부 `type-proposer`(Opus) 회람 전 초안) — 고성능 AI 불필요 단계는 Sol이 이 템플릿을 그대로 채운다.

---

## 왜 이 템플릿이 필요한가 (근인 분석 요약)

**결론: 지침은 맞았고, 파일 골격이 없었다.**

- `CLAUDE.md`·`AGENTS.md`·`type-proposer.md`는 *무엇을* 해야 하는가(8단계 절차, per-item/BLOCKED/≥2 변형축/함정/중요도/ COMMON_TYPES/ HARVEST 초안)를 정확히 정의했다.
- 그러나 **파일 단위 골격**(섹션 순서·표 헤더·플레이스홀더·검증 명령)이 표준 문서로 고정되지 않아, 작성자가 즉흥적으로 생략했다. 그 결과가 `260902` 25개 스텁의 `L?`·빈 통합절이다.
- `260901_03 TRUE`와 `EX-math1-20242M`이 우연히 양쪽 극단(부교재 93문항 완전 귀속 / HWP 22문항 GAP 19)을 커버하며 **올바른 형태를 증명**했으므로, 그 둘을 합쳐 **단일 골격을 동결**하면 Sol이 어느 과목·어느 회차든 동일 품질로 찍어낼 수 있다.

**이 템플릿이 막는 실패:**

| 과거 실패 | 템플릿의 강제 |
|-----------|---------------|
| `L?` 플레이스홀더 — 역추적 불가 | §1의 `증거 = transcript.md:Lxx`를 빈칸 금지로 강제, 동반 `_items.tsv`의 `source_lines`와 교차 검증 |
| 통합절 생략 — 변형축·함정 유실 | §2 `reusable`는 변형축 2개 미기재 시 `fail-closed` |
| GAP을 강제로 SM에 끼워넣기 | §1 `GAP-xxx`는 `CODE_REGISTRY` 신규 접두어 제안으로만 허용, §3에서 disposition 분리 |
| HWP `pNN` 없음 혼동 | §0 `rendered_evidence_status`로 `pNN`/`bindata` 분기 명시, `no pNN`를 속성이지 결함이 아님을 표기 |
| 원장 선반영 | §6은 `draft`만, 승인 전 `HARVEST_LOG.tsv` append 금지 문구 고정 |

---

## 헤더 — 복사해 채우기

```markdown
# {{CORPUS_ID}} 1차 분류 — provenance-first ({{N}}문항, transcript 기반)

> **ID**: {{CORPUS_ID}} | **원천**: `origin_data/{{CORPUS_ID}}/{{원본파일명}}` ({{PDF|HWP}} — `origin_data` 영구 보존)
> **1차 정제**: `corpus/{{CORPUS_ID}}/transcript.md` sha `{{sha256 7자리}}` {{행수}}행 {{N}}문항({{단답|선택형}} {{n}}+{{서술|서답}} {{m}}) + `meta.yml` items:{{N}} confidence:{{high|medium|low}} + `verify_log.tsv` + `_images` {{pNN n장(dpi160) | bindata n건(HWP) — pNN 0장 정상}}
> **방법**: transcript 문면 한 문항씩 재독해 — 카탈로그 빈도 미참조, `{{catalog_ref}}` 정의와 1:1 대조 후 배정. **근원 추적 최우선**: 모든 행은 `transcript.md:줄번호`+`verify_log`로 역추적.
> **카탈로그**: `{{catalog_ref}}` {{유형 접두어}}-01~{{NN}} ({{범위 설명, 예: 2026 중간·기말 기반}}). 범위 불일치 문항은 `GAP → 신규 제안 후보`로 명시(강제 배정 금지).
> **상태**: 제안 문서(PROVISIONAL), 외부 `type-proposer`(Opus) 회람 전. 승인 전까지 HARVEST_LOG/카탈로그 미반영.
> **작성**: Codex/OMX Sol {{YYYY-MM-DD}}
```

**규칙**: `방법` 문장은 이 템플릿 문구를 그대로 유지한다 — 빈도표 참조를 금지하는 가드다.

---

## §0 게이트 — 예상=관측, 중복0, BLOCKED 명시

> 이 표가 `fail-closed`다. 한 칸이라도 비면 `▲ blocked`이며 §1 진입 금지.

| 항목 | 값 | 증거 |
|------|----|------|
| 예상(transcript 동결) | {{N}} | `transcript.md` {{시트·단원별 합계, 예: 단답 18(L62-L126)+서술 4(L138-L153)}} |
| meta.yml items | {{N}} | `corpus/{{CORPUS_ID}}/meta.yml:{{행번호}}` |
| 실측(본 분류) | {{N}} | 아래 §1 표 합계 |
| 중복/결측/초과 | 0 | — |
| BLOCKED(unreadable) | {{0|n}} | {{0이면 "transcript 전 문항 판독 가능" / n이면 §1에서 BLOCKED-n 행으로 명시, verify_log `unreadable` 인용}} |
| 이미지 | {{n}} | {{PDF: `pNN.png` n장 정상 / HWP: `bindata` n건, 표지 로고 등 위치 기록 `transcript.md:Lxx`}} |

> 검증: `Select-String -Pattern "^\*\*[0-9]+\."` 또는 `Select-String -Pattern "^\| [0-9]+"` 전수 계수. 각 행의 `L`은 `transcript.md` 줄번호.

**HWP 분기 추가 문구**(해당 시만):
> `pNN.png` 0장은 HWP 경로의 정상 상태다. 증거는 `transcript.md:줄번호`와 `verify_log.tsv: BIN000x`로 대체하며, `rendered_evidence_status`에 `no pNN (bindata n)`으로 표기한다.

---

## §1 문항별 배정 — transcript 인용 → 판정 (N행, provenance-first)

> `증거` = `transcript.md:줄` + 원천 레코드 근거. `판정`은 카탈로그 정의와 대조 결과, `GAP`은 신규 유형 제안 후보(강제 배정 금지). Tier는 카탈로그 해당 유형의 Tier, GAP은 `TBD` 또는 `T{{n}} 후보`.
> **빈칸 금지**: `L?`, `TBD?`, `근거 없음`은 `▲ blocked`다. 한 줄이라도 비면 동반 TSV 게이트가 실패한다.

| 문항 | transcript 인용(핵심) | 증거 | 유형 판정 | 판정 근거(한 문장) | Tier | GAP/신규 | confidence |
|------|----------------------|------|-----------|-------------------|------|----------|------------|
| 1 | `f(x)=...` 핵심 조건 그대로 | L62 `⟦EQD:...⟧` | **SM-04** 또는 **GAP-FUNC-01** | {{왜 그 유형인지 한 문장}} | T2 | — 또는 신규 제안: ... | high |
| 2 | ... | L64-L68 | ... | ... | ... | ... | ... |
| S1 | ... | L138 | ... | ... | ... | ... | ... |

**작성 규칙:**

- `transcript 인용`은 전사본 문구를 **축소 인용**하되, 핵심 술어·조건·묻는 값을 모두 포함한다(증거 재현성).
- `증거`는 반드시 `L{{시작}}-L{{끝}}` 또는 `L{{단일}}` + `EQED seqno`/`pNN`/`BIN000x` 중 하나를 병기한다.
- `GAP`은 `GAP-{{접두어}}-{{NN}}` 형태이며, `CODE_REGISTRY`에 없는 접두어면 §3에서 신설 제안으로 분리한다.
- `confidence`는 `high|medium|low` 중 하나 — `verify_log.tsv`의 `confidence`와 독립(판정 자신감).
- **Markdown-TSV 비대칭 안내**: §8 `_items.tsv`는 11열이나 위 Markdown 표는 8열이다. `rendered_evidence_status`·`tier_basis`·`observed_trap`·`generator_id` 4열은 Markdown 표에 별도 칸이 없고 **TSV에서만 채운다** — `item_id` 기준 byte-equal 규칙(§1 하단)은 두 산출물에 공통으로 존재하는 열(문항 식별·판정·근거·Tier·GAP·confidence)에만 적용되며, TSV 전용 열은 이 규칙의 예외다. `generator_id`는 기본적으로 `assignment_or_BLOCKED`(유형 판정) 값과 동일하게 채운다 — 배정과 별도로 다른 그룹 키를 쓰려면 §2에서 명시적으로 사유를 남긴다.

**동반 TSV**: `output/<YYMMDD>/<YYMMDD>_<NN>_{{corpus-id}}_classification_items.tsv` — UTF-8 BOM, 11열 고정(§8 스키마). Markdown 표와 TSV는 `item_id` 기준으로 byte-equal이어야 한다.

---

## §2 통합 — 관찰된 변형축·함정 (재사용 증거)

> 각 **재사용 가능 유형**(`reusable`: 동일 `generator_id`로 2문항 이상 관측)마다 transcript에서 직접 관측된 변형축 **2개 이상**과 관찰된 함정을 기재한다. `singleton`은 1문항, `blocked`는 `unreadable` 전용. **통합 없는 나열은 실패다.**

| group_id | member_item_ids | type_disposition | variation_axis_1 | variation_axis_2 | observed_trap | importance_source_axis | common_types_disposition | catalog_disposition | generator_id | row_kind |
|----------|-----------------|------------------|------------------|------------------|---------------|------------------------|--------------------------|---------------------|--------------|----------|
| SM2-02 | #1-1,#1-5,#1-10 | reusable | 목표식 `AP²+BP²` vs `AP+QB`(고정간격) | 매개 `x축 vs 직선 y=-2x+k` | `Pₓ<Qₓ` 방향 무시 | ★★★(부교재 93문항 축) | C-00 해당 없음 | 유지 | SM2-02 | reusable |
| GAP-FUNC-01 | 1 | singleton | — | — | — | TBD | C-00 검토 대상 | 신규 제안 후보 | GAP-FUNC-01 | singleton |
| BLOCKED-01 | 17 | blocked | — | — | — | — | — | — | BLOCKED-01 | blocked |

**규칙 (ACCEPTANCE_SCHEMA §2):**

- `row_kind` = `reusable|singleton|blocked` 중 하나. `blocked`는 `HARVEST` 재사용 분모에서 제외.
- `reusable`는 `variation_axis_1`·`variation_axis_2` **둘 다** 채워야 하며, 빈칸이면 게이트 실패.
- `member_item_ids`는 §1의 문항 번호와 문자 일치해야 하며, 한 문항이 두 row에 중복 소속되면 실패.
- `generator_id`는 위 Markdown 표에 별도 열로 존재한다(§8 TSV 11열과 1:1). 기본값은 `group_id`와 동일하되, `item` 테이블(`_items.tsv`)의 `generator_id`와 반드시 일치해야 한다 — 임의 umbrella row 금지. `group_id`(사람이 읽는 그룹 라벨)와 `generator_id`(조인 키)가 다른 값이어야 하는 경우는 없다고 가정하며, 다르게 쓸 경우 §2 표 하단에 사유를 별도 기재한다.

**동반 TSV**: `output/<YYMMDD>/<YYMMDD>_<NN>_{{corpus-id}}_classification_types.tsv` — 11열 고정(§8 스키마).

---

## §3 카탈로그 disposition — 신규 유형 필요 여부

- {{N}}문항 중 **카탈로그 직접 배정 {{n}}건** + **유사 참조 {{m}}건** + **GAP {{k}}건**. {{범위 일치/불일치 한 문장 판정}}.
- `GAP` {{k}}건은 `CODE_REGISTRY` 신규 접두어 `{{접두어}}-nn` 신설 제안 — `analysis/catalog/COMMON_TYPES.md`와 충돌 검토 후 `type-proposer`(Opus) 회람.
- 유지/폐기/수정 대상 유형: {{해당 시만 기재, 없으면 "해당 없음"}}

---

## §4 COMMON_TYPES disposition

- `analysis/catalog/COMMON_TYPES.md` C-00~09 대조 결과: {{해당/해당 없음, 해당 시 C-nn 병기}}.
- 공통유형 승격은 `2과목↑/2회차↑` 반복 시에만 — 본 분류는 `제안`만 하며 직접 승격 금지.

---

## §5 Provenance — 다른 AI가 근원을 찾는 경로 (최우선)

> 모든 행은 아래 4종으로 역추적 가능. **다른 AI는 아래 순서로 찾으면 된다.**

```
1) ID로 원천 찾기: EXTRACTION_LOG.md #{{NN}} → "origin_data/{{CORPUS_ID}}/{{원본파일명}}"
2) 정제 찾기: corpus/{{CORPUS_ID}}/meta.yml (id, items:{{N}}, transcribed_at:{{ISO8601}}, method:{{method}})
         + corpus/{{CORPUS_ID}}/transcript.md sha{{7자리}} L{{시작}}-L{{끝}} (원문 유지)
         + corpus/{{CORPUS_ID}}/verify_log.tsv (transcribe/unreadable 행, evidence: {{pNN|BIN}})
         + corpus/_images/{{CORPUS_ID}}/{{pNN.png n장 | bindata n건}}
3) 분류 찾기: output/<YYMMDD>/<YYMMDD>_<NN>_{{corpus-id}}_classification.md (본 파일, sha — 생성 시 기록)
         + 동반 TSV 2종: _items.tsv (11열), _types.tsv (11열) — BOM 필수
4) 유형 찾기: {{catalog_ref}} {{접두어}}-01~ + GAP {{k}}건은 CODE_REGISTRY 신규 제안으로 분기
5) 검증: transcript 문항 수({{N}}) == meta items({{N}}) == 분류 행 수({{N}}) == HARVEST_LOG remaining(0) — 불일치 시 ▲ blocked
```

**웹 DAQ 흐름도도 이 체인만으로 그린다** — `origin_data → corpus → output → catalog` 4층, 각 엣지는 `expected==observed`로 굵기 결정. `pNN` 유무는 노드 속성일 뿐 매핑 계산에 쓰지 않는다.

---

## §6 다음 조치 (HARVEST/EXTRACTION 초안 — 승인 전까지 draft)

- **HARVEST_LOG draft** (append 금지, 승인 시에만 append):
  ```
  {{YYMMDD}}	{{CORPUS_ID}}	{{new_types 또는 -}}	{{freq_update 또는 -}}	{{weakness_evidence 또는 -}}	0	{{메모: 예 "1차 분류 PROVISIONAL: N문항 transcript 독립 배정, GAP k건, pNN n장, output/... — 외부 회람 대기"}}
  ```
- **EXTRACTION_LOG draft** `#{{NN}}` 갱신안:
  ```diff
  -| {{NN}} | `{{원본파일명}}` | {{기존}} | 미분류 | {{날짜}} |
  +| {{NN}} | `{{원본파일명}}` | {{수정}} | 분석완료 | {{날짜}} | ... {{N}}문항 transcript 독립 배정 완료(output/...) |
  ```
- **CODE_REGISTRY**: GAP이 있으면 `{{접두어}}-nn` 신설 제안 — `COMMON_TYPES`와 충돌 검토 후 회람.

> 본 파일은 **제안 문서**이며 정본을 직접 수정하지 않는다. 다른 AI가 본 파일을 읽으면 §5 경로로 원천 레코드까지 100% 재현 가능하다.

---

## §7 검증 체크리스트 — 제출 전 self-check (게이트)

- [ ] `transcript.md` 문항 수(N) == `meta.yml` items == §1 행 수 == `HARVEST_LOG remaining:0` — 셋 중 하나라도 불일치 시 `▲ blocked`
- [ ] 모든 행에 `transcript.md:Lxx` 증거가 있고 `L?`가 0건
- [ ] `BLOCKED`는 `verify_log.tsv` `unreadable` 행과 1:1 대응, `generator_id= BLOCKED-`로 표기
- [ ] `reusable` row는 `variation_axis_1`·`2` 둘 다 채움, `singleton`·`blocked`는 `—` 허용
- [ ] 동반 TSV 2종(`_items.tsv` 11열, `_types.tsv` 11열)이 BOM UTF-8이며 Markdown 표와 `item_id` byte-equal
- [ ] `CODE_REGISTRY` 미등록 접두어를 썼다면 §3에 신설 제안으로 분리했는가
- [ ] `scope_confirmed` 미확정이면 `⚠️` 표기를 헤더에 병기했는가(2025-2M 분할 패턴 등)
- [ ] `check_classification.py --check`를 실행했는가 — **현재(S3 동결 전)는 advisory**이므로 결과가 `FAIL`이어도 제출 자체는 가능하나, `warnings`/`failures` 내역을 §6 draft 메모에 그대로 첨부해 회람 검토자가 확인할 수 있게 한다. S3 재동결 이후에는 `PASS`가 제출 필수 조건이 된다(`docs/templates/README.md §3` 참조).

---

## §8 스키마 — 동반 TSV 2종 (기계 소비, BOM 필수)

### `_items.tsv` — 11열 고정 (ACCEPTANCE_SCHEMA §1)

```
item_id	source_lines	rendered_evidence_status	assignment_or_BLOCKED	existing_type_or_decision_request	rationale	tier	tier_basis	observed_trap	confidence	generator_id
{{CORPUS_ID}}-Q01	L62	no pNN (bindata 1) 또는 p01.png	SM-04 또는 BLOCKED	SM-04 또는 GAP-FUNC-01	{{한 문장 근거}}	T2	catalog SM-04 Tier	E5	high	SM-04
```

| 열 | 값 규격 | 예 | 비고 |
|----|---------|-----|------|
| item_id | `{{CORPUS_ID}}-Q{{NN}}` | `EX-math2-20252M-Q01` | §1 문항과 1:1 |
| source_lines | `L{{n}}` 또는 `L{{n}}-L{{m}}` | `L62` | transcript 줄번호 |
| rendered_evidence_status | `pNN.png` 또는 `no pNN (bindata n)` 또는 `unreadable` | `p01.png` | HWP는 bindata |
| assignment_or_BLOCKED | 유형ID 또는 `BLOCKED` | `SM-04` | |
| existing_type_or_decision_request | 유형ID 또는 `GAP-xxx` | `GAP-FUNC-01` | |
| rationale | ASCII 또는 한글 한 문장( TSV는 BOM UTF-8이므로 한글 허용이나, 원장 합류 시 ASCII 변환) | `합성함수 값 계산` | |
| tier | `T1|T2|T3|T4|TBD` | `T2` | GAP은 TBD |
| tier_basis | `catalog {{ID}} Tier` 또는 `TBD` | `catalog SM-04 Tier` | |
| observed_trap | 함정코드 또는 `—` | `E5` | |
| confidence | `high|medium|low` | `high` | |
| generator_id | 유형ID 또는 `BLOCKED-{{n}}` | `SM-04` | §2와 조인 키 |

### `_types.tsv` — 11열 고정 (ACCEPTANCE_SCHEMA §2)

```
group_id	member_item_ids	type_disposition	variation_axis_1	variation_axis_2	observed_trap	importance_source_axis	common_types_disposition	catalog_disposition	generator_id	row_kind
SM2-02	EX-math2-20252M-Q01,EX-math2-20252M-Q05	reusable	목표식 AP²+BP² vs AP+QB	매개 x축 vs 직선	방향 무시	★★★(부교재)	C-00 해당 없음	유지	SM2-02	reusable
```

---

## 확장성 설계 — 과목·회차·이미지·GAP을 흡수하는 방법

| 차원 | 템플릿이 흡수하는 방법 | 예 |
|------|----------------------|-----|
| **과목** | `catalog_ref`를 변수로 — `math1`→`SM`, `math2`→`SM2`, `korean`→`KO`, `english`→`EN`, `science`→`SC` 등 `CODE_REGISTRY` 접두어를 그대로 쓴다. §1 `유형 판정` 열은 어떤 접두어든 수용. | `analysis/catalog/science.md` `SC-07` |
| **회차** | `CORPUS_ID` 패턴 `^[A-Z]{2,4}-[a-z0-9]{2,8}-\d{4}([12][MF]\|P\d{2})?$` — `EX-*`(기출), `SUP-*`(부교재), `NY-*`(내신집) 모두 동일 골격. `exam_code` 미확정 시 헤더에 `⚠️` 병기(260902 2학기 중간처럼). | `EX-korean-20252M`, `SUP-math2-2026` |
| **이미지** | `rendered_evidence_status`로 분기 — PDF는 `pNN.png`, HWP는 `no pNN (bindata n)`. §0 게이트의 `이미지` 행이 두 경로를 모두 설명하므로, 렌더 방식이 바뀌어도 표 구조는 불변. | `EX-math2-20252M: bindata 3건` vs `SUP-math2-2026: p01~p18` |
| **GAP 비율** | 부교재(`SUP`)는 GAP 0, 기출(`EX`)은 GAP 다수 — §1에서 `GAP-xxx`를 강제 배정 금지로 두고 §3·§6에서 신규 제안으로 분리하므로, GAP 0~100% 모두 동일 표로 표현된다. | `EX-math1-20242M: GAP 19/22` |
| **난이도** | `tier`는 카탈로그 Tier를 그대로 인용, GAP은 `TBD`. `DIFFICULTY_RUBRIC` DF 코드는 §1 `observed_trap`과 분리 — DF는 세트 출제 단계에서 부여하므로 1차 분류에서는 `TBD` 허용. | `SM-04: T2`, `GAP-FUNC-01: TBD` |
| **검증** | 동반 TSV 2종이 기계 게이트 — Markdown은 사람이 읽고, TSV는 `check_classification.py`가 `expected==observed==TSV rows`, `L?==0`, `reusable 축 2개`를 자동 검증. 과목이 늘어도 검증 코드는 불변. | `tools/check_classification.py --check` |

---

## 작성 예시 — 두 극단으로 템플릿 검증

- **부교재 완전 귀속 예**: `260901_03 SUP-math2-2026 TRUE` — 93문항 SM2-01~33 전건, GAP 0, `reusable` 6·`singleton` 9(후보 스키마 대비). 이 템플릿의 §0~§6을 모두 채운 **만점 답안**.
- **기출 GAP 다수 예**: `EX-math1-20242M` (260902) — 22문항 중 SM-04 1건 + GAP 19건, `reusable` 0·`singleton` 다수. §2에서 `reusable`가 0이어도 `singleton`으로 정당히 표현되므로 템플릿이 깨지지 않는다.

> 두 예시는 `output/260901/260901_03_SUP-math2-2026_classification_TRUE.md`와 `output/260902/EX-math1-20242M_classification.md`에 원문이 있다 — 이 템플릿으로 재작성해도 정보 손실이 없음을 대조하라.

---

## 이력

- v1.1 — 2026-09-02 Claude(감사) — 내부 불일치 4건 수정: (1) §2 Markdown 표에 `generator_id` 열 누락 → 추가 및 `group_id`와의 관계 명시, (2) §7의 유령 스크립트 `check_assurance_contract.py`(정의된 파일 없음) 제거, (3) §7 `check_classification.py` 게이트가 advisory임을 명확화(README §3과 정합), (4) §1 Markdown-TSV 열 비대칭(8열 vs 11열)을 명시적으로 문서화. Opus 회람 전 정합성 확보 목적. PROVISIONAL 유지.
- v1.0 — 2026-09-02 Codex/OMX Sol — `260901 TRUE` + `EX-math1-20242M` + `ACCEPTANCE_SCHEMA.candidate`를 합쳐 표준 골격 동결. `260902` 25개 스텁의 `L?`·빈 통합절 실패를 재발 방지. 외부 `type-proposer` 회람 전 PROVISIONAL.
