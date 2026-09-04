# docs/templates — 1차 분류 표준 템플릿 안내

> **이 폴더가 왜 생겼는가**: `CLAUDE.md`·`AGENTS.md`·`type-proposer`(8단계)는 *무엇을* 해야 하는지 정확히 정의했지만, *파일 한 장의 골격*이 표준 문서로 고정되지 않아 `260902` 25개 스텁이 `L?` 22건·빈 통합절로 생성됐다. `260901_03 TRUE`(93문항 완전 귀속)와 `EX-math1-20242M`(GAP 19/22) 2개가 같은 골격으로 Sol이 만들 수 있음을 증명한 뒤, 그 둘을 합쳐 **복사-붙여넣기로 찍어내는 골격을 동결**하기 위해 이 폴더를 만들었다.

---

## 1. 위치 — 어디에 무엇이 있는가

| 파일 | 역할 | 상태 |
|------|------|------|
| [`CLASSIFICATION_TEMPLATE.md`](CLASSIFICATION_TEMPLATE.md) | **1차 분류 표준 산출물 템플릿 v1.1** — 헤더/§0 게이트/§1 문항별 배정/§2 통합/§3 catalog disposition/§4 COMMON_TYPES/§5 provenance/§6 HARVEST 초안/§7 체크리스트/§8 스키마 + 확장성 5차원 + 작성 예시 2종 | PROVISIONAL — 외부 `type-proposer`(Opus) 회람 전, S2 자격·S3 동결 필요. v1.1에서 §2 `generator_id` 열 누락 등 내부 불일치 4건 수정(하단 이력 참조) |
| `../../tools/schemas/classification.schema.json` | 동반 TSV 2종(`_items.tsv` 11열 + `_types.tsv` 11열) JSON Schema — 정규식·fail-closed 규칙 기계 집행 | v1.0, 템플릿 §8과 1:1 |
| `../../tools/check_classification.py` | 템플릿 게이트 스텁 — `L?==0`, `expected==observed==TSV rows`, `reusable 축 2개` 등 자동 검증 | candidate-only, S3 동결 전까지 advisory |

**산출물 위치(템플릿이 찍어내는 곳):**

```
output/<YYMMDD>/<YYMMDD>_<NN>_<corpus-id>_classification.md        ← 템플릿을 채워 만드는 Markdown
output/<YYMMDD>/<YYMMDD>_<NN>_<corpus-id>_classification_items.tsv ← 동반 TSV 11열 (BOM)
output/<YYMMDD>/<YYMMDD>_<NN>_<corpus-id>_classification_types.tsv ← 동반 TSV 11열 (BOM)
```

---

## 2. 왜 만들어졌는가 — 근인

| 과거 실패 | 원인 | 템플릿의 강제 |
|-----------|------|---------------|
| `L?` 플레이스홀더 — 역추적 불가 | 증거 형식 미고정 | §1 `증거 = transcript.md:Lxx` 빈칸 금지 + 동반 `_items.tsv` 교차 검증 |
| 통합절 생략 — 변형축·함정 유실 | §2 스키마가 문서로 고정 안 됨 | `reusable`는 변형축 2개 미기재 시 `fail-closed` |
| GAP을 강제로 SM에 끼워넣기 | 신규 제안 경로 미분리 | §1 `GAP-xxx`는 `CODE_REGISTRY` 신설 제안으로만, §3에서 분리 |
| HWP `pNN` 없음 혼동 | PDF/HWP 분기 미명시 | `rendered_evidence_status`로 `pNN`/`bindata` 분기, `no pNN`를 정상으로 표기 |
| 원장 선반영 | draft/provisional 구분 없음 | §6은 `draft`만, 승인 전 `HARVEST_LOG.tsv` append 금지 문구 고정 |

**핵심 통찰:** `260901_02`를 스스로 적발·폐기한 것은 지침이 작동한 증거다. 문제는 지침이 틀려서가 아니라, **지침을 파일 한 장으로 고정해 Sol이 복사-붙여넣기로 찍어낼 수 있게 하지 않은 것**이었다.

---

## 3. 의도와 방향성

### 의도

- **통일**: 과목(`math1`/`math2`/`korean`/`english`/`science`/`social`/`history`/`info`), 회차(`EX`/`SUP`/`NY`), 이미지(`pNN`/`bindata`), GAP 비율(0~100%)이 달라도 **한 장의 표**로 표현되게 한다.
- **분리**: *사실 배정*(§1)은 Sol이 고성능 AI 없이도 할 수 있게 하고, *해석·통합*(§2 변형축 2개)은 Opus의 품질이 드러나게 한다 — 템플릿이 `reusable 축 2개`를 강제해 빈 통합절로 도망치지 못하게 한다.
- **재현**: 어떤 행이든 `transcript.md:Lxx` + `verify_log.tsv` + `corpus/_images`로 100% 역추적 가능하게 한다 — 다른 AI가 읽어도 원천 레코드까지 도달한다.

### 방향성

- **기계 집행**: Markdown은 사람이 읽고, 동반 TSV 2종은 `check_classification.py`가 코드로 검증한다. 과목이 늘어도 검증 코드는 불변이다 — `docs/DATA_STANDARD §0` 2층 원칙(기계 원장=TSV/BOM/ASCII, 사람 문서=MD) 준수.
- **확장 가능**: `catalog_ref` 변수로 과목 확장, `CORPUS_ID` 정규식으로 회차 확장, `rendered_evidence_status` 분기로 이미지 확장, `GAP-xxx` 분리로 신규 유형 확장 — 골격은 바꾸지 않고 값만 바꾼다.
- **점진 동결**: 현재 v1.0은 PROVISIONAL. S2에서 S2 자격 검증 → S3에서 감사 권한+사용자 2nd key로 재동결 → 그때 `check_classification.py`를 fail-closed로 전환한다. 그 전까지는 advisory(경고만)로 운영해 기존 산출물을 깨지 않는다.

---

## 4. 어떻게 쓰는가

```bash
# 1. 템플릿 복사
cp docs/templates/CLASSIFICATION_TEMPLATE.md output/260902/260902_01_EX-math2-20252M_classification.md

# 2. {{플레이스홀더}} 채우기 — 헤더 sha/행수/이미지, §0 게이트, §1 N행(Lxx 필수), §2 통합, §3~§6
# 3. 동반 TSV 2종 생성 (BOM 필수)
# 4. 게이트 검증
python tools/check_classification.py --check output/260902/260902_01_EX-math2-20252M_classification.md
# PASS — warnings 0, failures 0 이어야 제출 가능
```

**검증 예시:**

- `260901_03 TRUE` → `PASS (warnings 2 — 동반 TSV 미생성만)` — 템플릿을 따르면 즉시 PASS
- `EX-math1-20242M` → `PASS` — GAP 19건이어도 PASS, 골격이 깨지지 않음을 증명
- `EX-math2-20252M` 스텁 → `FAIL — L? 22건` — 왜 진입 불가인지 코드로 증명

---

## 5. 고성능 AI 검토 — 회람 패키지

외부 `type-proposer`(Opus) / `rev-auditor`(Opus) 검토를 위해 아래 회람 패키지가 생성됐다. **Codex/OMX는 Opus 결과를 위조하지 않으며**, 회신 파일이 로컬에 생성된 뒤에만 결과를 반영한다(`AGENTS.md` 외부 전용 역할).

| 항목 | 값 |
|------|-----|
| **회람 ID** | `CC-260902-TEMPLATE-classification-v1` |
| **대상** | `docs/templates/CLASSIFICATION_TEMPLATE.md` v1.0 + `tools/schemas/classification.schema.json` + `tools/check_classification.py` |
| **요청 역할** | `rev-auditor`(Opus) — 독립 재검증, `type-proposer`(Opus) — 절차 정합성 — 2-트랙 병렬도 가능 |
| **회람 패키지** | `output/260902/CC_회람_template-classification-v1.md` — §6-b 형식(측정된 경로·개수·범위·요청 판정·회신 경로·write surface·no-commit 제약) |
| **회신 경로** | `output/260902/rev/template-classification-v1_rev-auditor.md` (또는 `analysis/rev/` — `DOC_LOCATION §2`) |
| **사용 방법** | 사용자가 본 패키지를 별도 Claude Code CLI 세션에 전달 → Opus가 회신 파일을 생성 → Codex/OMX가 회신을 읽고 승인분만 반영 |

> **사용자 액션**: Claude Code CLI(Opus)에서 `/review` 또는 해당 role을 호출해 위 회람 패키지를 전달하고, 회신 파일이 생성되면 본 세션에 알려주세요. 회신 전까지 템플릿은 PROVISIONAL을 유지합니다.

---

## 6. 다음 단계

1. `EX-math2-20252M` 22문항을 본 템플릿으로 pilot 재작성 → `check_classification PASS` → Opus 회람
2. pilot PASS 후 나머지 24개 EX 유닛을 동일 템플릿으로 순차 진행(한 번에 25개 fan-out 금지 — staged dispatch)
3. S2 자격·S3 재동결 후 `check_classification.py`를 fail-closed로 전환, `DATA_STANDARD` 동반 갱신 목록에 등재

---

## 이력

- v1.1 — 2026-09-02 Claude(감사) — `CLASSIFICATION_TEMPLATE.md` 자체 감사 수행, 내부 불일치 4건 발견·수정: §2 Markdown 표의 `generator_id` 열 누락(§8 TSV 11열과 불일치), §7의 유령 스크립트 `check_assurance_contract.py` 참조(정의 파일 없음) 제거, §7 게이트가 advisory임을 명확화, §1 Markdown-TSV 열 비대칭 명문화. `type-proposer`(Opus) 회람 전에 반영해 회람 자체가 같은 지점에서 걸리지 않도록 함.
- v1.0 — 2026-09-02 Codex/OMX Sol — `260901 TRUE` + `EX-math1-20242M` + `ACCEPTANCE_SCHEMA.candidate`를 합쳐 표준 골격 동결. `260902` 25개 스텁의 실패를 재발 방지. 외부 회람 전 PROVISIONAL.
