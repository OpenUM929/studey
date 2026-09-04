# DAQ 흐름도 — 매핑 전용 설계 검증 (2026-09-02)

> **원칙**: 웹 흐름도(원천→1차정제→1차분류→유형)는 `파일을 새로 만들지 않고` 기존 4층의 **매핑만으로** 그려야 한다.
> 본 문서는 현재 데이터 구조가 그 조건을 만족함을 증거와 함께 검증한다. 실제 `daq_mapping.json` 생성은 본 설계 승인 후에만 수행한다.

---

## 1. 4층 구조와 물리적 증거

| 층 | 경로 | 노드 식별자 | 매핑 키 | 증거 파일 |
|----|------|-------------|---------|-----------|
| 0 원천 | `origin_data/<코퍼스ID>/원본.(pdf/hwp)` | `corpus_id` | 폴더명 = 코퍼스ID | `analysis/EXTRACTION_LOG.md` `#`열 — 원천 파일 → 코퍼스ID |
| 1 1차 정제 | `corpus/<코퍼스ID>/transcript.md` + `meta.yml` + `verify_log.tsv` + `_images/<ID>/pNN.png` | `corpus/<ID>` | `meta.yml: items` = `transcript.md` 문항 수 = `verify_log` transcribe 행 | `corpus/_README.md` 게이트 4종, `corpus/HARVEST_LOG.tsv` `items` |
| 2 1차 분류 | `output/<YYMMDD>/<ID>_classification.md` | `output/...` | `문항번호 → 유형ID(예 SM2-01)` | `corpus/HARVEST_LOG.tsv` `note=output/...(hash)`가 정제→분류 링크 |
| 3 유형 정본 | `analysis/catalog/<subject>.md` | `유형ID` | 분류표의 `SMx-nn` = 카탈로그 `SMx-nn` | `analysis/catalog/CODE_REGISTRY.md` |

### 검증 예시 — SUP-math2-2026 (유일 TRUE)

```
원천: origin_data/SUP-math2-2026/스무년 고1-2.pdf (7109278B, 18쪽, 93문항)
  → 정제: corpus/SUP-math2-2026/transcript.md (239행, **1. 2. ... 15. + 도표 이미지 링크 13건)
         + meta.yml (items:93, transcribed_at:2026-09-01, render_dpi:160, confidence:high, answer_key:generated_answer.md)
         + verify_log.tsv (18행 transcribe)
         + _images/p01.png~p18.png (dpi160)
  → 분류: output/260901/260901_03_SUP-math2-2026_classification_TRUE.md (hash 266F0FE, 93행, SM2-01~33, 중복0)
  → 유형: analysis/catalog/math2.md (SM2-01~33, Tier·변형축·함정)
```

모든 엣지는 `grep -c "^\*\*"`(문항 수)나 `sha256`로 재검증 가능. **그림(`pNN`/`BIN`)은 노드 속성일 뿐 엣지 계산에 불필요** — 웹은 매핑 JSON의 `expected == observed`만으로 흐름선 굵기를 결정한다.

---

## 2. 현재 인벤토리 — 1차 분류 미완 26개

| 그룹 | 코퍼스ID (예) | 문항수 | 정제 게이트 | 분류 |
|------|---------------|-------:|-------------|------|
| 2024-2중간 | EX-math1-20242M/F (22/22), EX-science-20242M/F (29/32) 등 8개 | 214 | `transcript+meta+verify` 전건 PASS | **미완** |
| 2024-2기말 | EX-korean-20242F 등 5개 (이미 214에 포함 — 위는 중간만 예시, 실제 20242 총 13개) | — | PASS | 미완 |
| 2025-2중간 | EX-math2-20252M/F (22/23), EX-english-20252M 등 | 436 | PASS | 미완 |
| SUP | SUP-math2-2026 | 93 | PASS | **TRUE 완료** |

총 **27개 코퍼스 중 26개가 1차 분류 대기**(723문항). 1차 정제는 전건 완료이므로, 매핑만 추가하면 흐름도 완성이다.

---

## 3. 웹 흐름도 매핑 스키마 (생성 전 설계)

```typescript
// 노드
type Node = {
  id: string;          // corpus_id (예: EX-math1-20242M)
  layer: 0|1|2|3;     // 원천|정제|분류|유형
  path: string;        // 파일 경로
  hash?: string;       // sha256 앞 7자
  items: number;       // 문항수
  meta?: { items:number, render_dpi?:number, confidence:string }
}

// 엣지
type Edge = {
  from: string; // corpus_id
  to: string;   // 다음 층 id
  expected: number;
  observed: number;
  missing: number;
  duplicate: number;
  blocked: number;
}

// 전체 매핑 (파일 미생성 — 설계만)
type DAQMapping = {
  generated_at: string;
  corpus_units: Node[];
  type_catalogs: { subject:string, type_ids:string[] }[];
  edges: Edge[]; // 원천→정제, 정제→분류, 분류→유형 3종
}
```

- **원천→정제 엣지**: `EXTRACTION_LOG`의 원천 파일 수 vs `corpus/<ID>/meta.yml:items`
- **정제→분류 엣지**: `transcript.md` 문항 수 vs `output/..._classification.md` 배정 행 수
- **분류→유형 엣지**: 분류표의 `SMx-nn` vs `catalog/<subject>.md` 존재 여부

웹은 이 JSON 하나로 **Sankey/신경망** 흐름도를 그린다 — md 안에 `![pNN]`이 있는지, `[[BIN]]`으로만 표시되는지는 렌더 분기로 처리하고 매핑 계산에는 쓰지 않는다.

---

## 4. 정제 vs 분류 분리 재확인 (260901 정정)

- **1차 정제**: 전사만, `corpus/<ID>/`에만 산출, 유형ID·변형축·함정 절대 금지
- **1차 분류**: 정제물을 한 문항씩 배정, `output/<YYMMDD>/`에만 산출, 카탈로그 빈도 옮겨적기 금지
- 본 설계는 이 분리를 **파일 경로로 강제**한다 — 경로가 다르면 레이어가 다른 것이다.

---

## 5. 다음 단계 (파일 생성 없이)

1. Pilot 2개(EX-math2-20252M/F, EX-math1-20242M 중 1개)로 분류 테이블 포맷 검증
2. 승인 후 wave-1(8개), wave-2(16개) 순차 디스패치 — 각 wave는 `transcript` 기반 per-item 배정, 외부 `type-proposer`(Opus) 회람 패키지까지
3. 승인 후 `output/<YYMMDD>/daq_mapping.json` 생성 — 4층 노드/엣지 실측치로 웹 흐름도 구동

> 본 문서는 **설계 검증 문서**이며, `daq_mapping.json` 자체는 생성하지 않았다.
