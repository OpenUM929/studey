# [CC 회람] 1차 분류 표준 템플릿 v1.0 — 외부 Opus 검토 요청

> **REV_GUIDE §6-b 형식** — Codex/OMX가 생성, Claude Code CLI(Opus)가 회신. Codex/OMX는 Opus 결과를 위조하지 않으며, 회신 파일이 로컬에 생성된 뒤에만 반영한다.

---

## 1. 회람 식별

| 항목 | 값 |
|------|-----|
| **회람 ID** | `CC-260902-TEMPLATE-classification-v1` |
| **생성일** | 2026-09-02 |
| **생성자** | Codex/OMX Sol (main-loop) |
| **대상 정본** | `CLAUDE.md` 작업흐름표 · `AGENTS.md` 팀 표 · `DATA_STANDARD §5.7/5.7-A` · `REV_GUIDE §3/6-b` |
| **유형** | 산출물 양식(템플릿) — 정본 직접 수정 아님, 제안 문서 |

## 2. 검토 대상 (측정된 경로·해시·개수)

| 파일 | 경로 | sha256 (7자리) | 행수/개수 |
|------|------|---------------|-----------|
| 템플릿 정본 | `docs/templates/CLASSIFICATION_TEMPLATE.md` | `AC65E57` | 231행, 8섹션(헤더+§0~§8) + 확장성 5차원 + 예시 2종 |
| 템플릿 안내 | `docs/templates/README.md` | `36131A9` | 6섹션(위치·근인·의도·사용법·회람·다음단계) |
| 스키마 | `tools/schemas/classification.schema.json` | `ED0B56D` | `_items.tsv` 11열 + `_types.tsv` 11열, JSON Schema draft 2020-12 |
| 게이트 스텁 | `tools/check_classification.py` | `EAC201A` | 5 checks, advisory(S3 동결 전까지) |
| 근거 1 (만점) | `output/260901/260901_03_SUP-math2-2026_classification_TRUE.md` | `5BD44C6`(v3) | 93문항 SM2-01~33 완전 귀속, GAP 0 |
| 근거 2 (GAP) | `output/260902/EX-math1-20242M_classification.md` | `40410F0` | 22문항 SM-04 1 + GAP 19, 템플릿으로 손실 없이 표현 가능 |
| 반례 (스텁) | `output/260902/EX-math2-20252M_classification.md` | — | 22문항 `L?` 22건, FAIL — 템플릿이 막아야 할 실패 |
| 후보 스키마 | `output/260829/ruler-candidate/ACCEPTANCE_SCHEMA.candidate.md` | — | S1 candidate, 87행, S2 자격·S3 동결 필요 |
| 정제물 (PDF) | `corpus/SUP-math2-2026/transcript.md` + `_images/p01~p18.png` | — | 239행 93문항, dpi160 18장 |
| 정제물 (HWP) | `corpus/EX-math2-20252M/transcript.md` + `verify_log.tsv` | — | L31-L145 22문항, bindata 3건, pNN 0장 정상 |

**범위**: 공통수학2(2학기) 도형의 방정식 + 공통수학1(2024-2중간) — 템플릿은 과목 무관(확장성 5차원: 과목·회차·이미지·GAP·검증).

## 3. 요청 역할 및 판정

| 요청 역할 (외부 Opus) | 요청 판정 | 비고 |
|----------------------|-----------|------|
| **`rev-auditor`(Opus) — Tier-2 독립 검증** | `approve / revise-required / reject` — binding 아님, 권고 | `260901_03 TRUE` + `EX-math1-20242M`을 S1 근거로, 템플릿이 `L?`·빈 통합절·GAP 강제배정 등 과거 실패를 재발 방지하는지 독립 검증 |
| **`type-proposer`(Opus) — 절차 정합성** | `approve / revise-required` | 8단계 절차·per-item/BLOCKED/≥2변형축 등 `AGENTS.md` 정의와 템플릿 §0~§8이 1:1인지, 과목 확장 시 깨지지 않는지 |

**병렬 2-트랙 가능**: 두 역할은 서로 다른 Opus 세션에서 독립 수행 가능. 한쪽만 먼저 회신돼도 Codex/OMX는 그 회신을 반영할 수 있다.

## 4. 회신 경로 (Codex/OMX가 읽는 위치)

```
output/260902/rev/template-classification-v1_rev-auditor.md      ← rev-auditor 회신 (우선)
output/260902/rev/template-classification-v1_type-proposer.md    ← type-proposer 회신 (선택)
— 또는 analysis/rev/ (DOC_LOCATION §2에 따라)
```

**회신 파일 필수 포함:**

- `lane = model = reasoning depth` (예: `rev-auditor = Opus = high`)
- `observed_model_depth` (런타임 관측치, TOML 라벨 아님)
- `artifact path` / `exclusive output path` / `completion status`
- `agree / disagree / new-findings` per checklist item (REV_GUIDE §3-b)
- `warnings` / `failures` / `experiment-gate: PASS|FAIL`

## 5. 검증 명령 (Opus가 직접 실행)

```bash
python tools/check_classification.py --check output/260901/260901_03_SUP-math2-2026_classification_TRUE.md
# 기대: PASS (warnings 2 — 동반 TSV 미생성만)

python tools/check_classification.py --check output/260902/EX-math1-20242M_classification.md
# 기대: PASS

python tools/check_classification.py --check output/260902/EX-math2-20252M_classification.md
# 기대: FAIL — L? 22건 (템플릿이 막아야 할 실패가 코드로 증명됨)

python tools/check_assurance_contract.py
# 기대: 템플릿 관련 TEXT_REQUIREMENTS 추가 후 PASS (현재 WIP 6건 FAIL은 별건)
```

## 6. Write Surface 및 제약

| 항목 | 값 |
|------|-----|
| **Opus write surface** | `output/260902/rev/template-classification-v1_*.md`만 — 정본(`docs/templates/CLASSIFICATION_TEMPLATE.md`, `tools/schemas/*.json`, `analysis/catalog/*.md`) 직접 수정 금지 |
| **Codex/OMX write surface** | 회신 승인 후에만 템플릿 수정, `HARVEST_LOG.tsv`/`EXTRACTION_LOG.md`는 승인 전까지 append 금지 |
| **no-commit 제약** | 본 회람은 제안 문서 — 커밋·정본 반영은 사용자 승인 후에만 |
| **병렬 제약** | Opus는 기본 1 메인 세션 + 1 pilot slice, subagent·백그라운드·자동 재시도 금지. 다음 wave는 측정된 이전 결과 + 사용자 per-run 승인 필요 |

## 7. 체크리스트 (Opus가 답해야 할 질문)

- [ ] 템플릿 §0~§8이 `AGENTS.md` Assurance evidence 스키마( per-item or BLOCKED / unique-ID coverage / consolidation ≥2 axes / observed traps / source-axis importance / COMMON_TYPES / catalog disposition / HARVEST draft )를 **빠짐없이** 커버하는가?
- [ ] `L?` 금지·`reusable 축 2개`·`GAP 분리`·`pNN/bindata 분기`가 `260902` 스텁 실패를 코드로 막는가? (`check_classification.py` FAIL로 증명)
- [ ] 과목 확장(`math1→SM`, `science→SC`, `korean→KO` 등)·회차 확장(`EX`/`SUP`/`NY`)·이미지 확장(HWP bindata)·GAP 0~100%에서 **같은 골격**이 깨지지 않는가?
- [ ] 동반 TSV 2종 11열이 `DATA_STANDARD §0` 2층 원칙(기계 TSV/BOM/ASCII vs 사람 MD)과 충돌 없이 `Markdown-TSV byte-equal`로 검증 가능한가?
- [ ] 템플릿이 Sol이 고성능 AI 없이도 §1(사실 배정)을 동일 품질로 찍어내게 하고, §2(통합)에서 Opus 품질이 드러나게 **역할을 분리**하는가?
- [ ] S1 candidate(`ACCEPTANCE_SCHEMA.candidate`)를 S2 자격·S3 동결로 가져가는 경로가 템플릿에 명시돼 있는가? (advisory → fail-closed 전환)

## 8. 사용자 액션

1. 본 파일을 Claude Code CLI(Opus) 세션에 전달한다.
2. Opus가 위 체크리스트에 답하는 회신 파일(`output/260902/rev/template-classification-v1_*.md`)을 생성한다.
3. 사용자가 "회신 생성 완료"를 본 세션에 알리면, Codex/OMX가 회신을 읽고 승인분만 템플릿에 반영한다.

> **주의**: 회신 파일이 로컬에 생성되기 전까지는 어떤 Opus 승인도 추론하지 않는다. `blocked` 상태로 대기한다.

---

## 9. 이력

- 2026-09-02 Codex/OMX Sol — `260901 TRUE` 93문항 + `EX-math1-20242M` GAP 19 + `ACCEPTANCE_SCHEMA.candidate`를 합쳐 v1.0 동결, 외부 회람 패키지 생성.
