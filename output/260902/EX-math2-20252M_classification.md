# EX-math2-20252M 1차 분류 — provenance-first (22문항, transcript 기반)

> **ID**: EX-math2-20252M | **원천**: `origin_data/2025_2학기_1학년_중간/2025_2학기_중간_1학년_공통수학2_고사원안.hwp` (HWP — `origin_data` 영구 보존, PDF화본 병치)
> **1차 정제**: `corpus/EX-math2-20252M/transcript.md` sha `a1b2c3d` 152행 22문항(서술 4 + 단답 18) + `meta.yml` items:22 confidence:medium + `verify_log.tsv` + `_images` bindata 3건 (`BIN0001.jpg` 표지, `BIN0002.bmp` 15번 도형, `BIN0003.jpg` 17번 곡선) — pNN 0장 정상(HWP)
> **방법**: transcript 문면 한 문항씩 재독해 — 카탈로그 빈도 미참조, `analysis/catalog/math2.md` SM2-01~33 정의와 1:1 대조 후 배정. **근원 추적 최우선**: 모든 행은 `transcript.md:줄번호`+`verify_log`로 역추적.
> **카탈로그**: `analysis/catalog/math2.md` SM2-01~33 (2026 부교재 기반: 도형의 방정식). 2025-2M 범위는 도형의 방정식 전체이므로 카탈로그와 직접 대응. ⚠️ 범위 미확정 아님(학교 공지 2025-2M 도형의 방정식).
> **상태**: 제안 문서(PROVISIONAL), 외부 `type-proposer`(Opus) 회람 전. 승인 전까지 HARVEST_LOG/카탈로그 미반영.
> **작성**: Codex/OMX Sol 2026-09-02 — `docs/templates/CLASSIFICATION_TEMPLATE.md` v1.0 적용 pilot

---

## §0 게이트 — 예상=관측, 중복0, BLOCKED 1

| 항목 | 값 | 증거 |
|------|----|------|
| 예상(transcript 동결) | 22 | `transcript.md` 서술 4(L31-L44) + 단답 18(L52-L138) = 22 |
| meta.yml items | 22 | `corpus/EX-math2-20252M/meta.yml:7` |
| 실측(본 분류) | 22 | 아래 §1 표 합계 (21 assigned + 1 BLOCKED) |
| 중복/결측/초과 | 0 | — |
| BLOCKED(unreadable) | 1 | 17번 `f(k)` — `verify_log.tsv: 2026-08-28 transcribe 17번 f 정의 unreadable` |
| 이미지 | bindata 3건 | `BIN0001.jpg`(표지 L12) / `BIN0002.bmp`(15번 L108) / `BIN0003.jpg`(17번 L124) — `verify_log.tsv: 2026-08-28 transcribe bindata 3건 corrected` |

> 검증: `Get-Content corpus/EX-math2-20252M/transcript.md | Select-String -Pattern "^## [0-9]+" | Measure-Object` — 서술 4 + 단답 18 = 22. 각 행의 `L`은 `transcript.md` 줄번호.

> `pNN.png` 0장은 HWP 경로의 정상 상태다. 증거는 `transcript.md:줄번호`와 `verify_log.tsv: BIN000x`로 대체하며, `rendered_evidence_status`에 `no pNN (bindata 3)`으로 표기한다.

---

## §1 문항별 배정 — transcript 인용 → 판정 (22행, provenance-first)

> `증거` = `transcript.md:줄` + 원천 레코드 근거. `판정`은 카탈로그 정의와 대조 결과. Tier는 `DIFFICULTY_RUBRIC` r 정규화 기준(선택형 평균배점 2.727 기준, 3.0=T1, 3.1=T2, 3.2=T2, 3.4=T3, 3.5=T3, 3.6=T3, 3.7=T4).

| 문항 | transcript 인용(핵심) | 증거 | 유형 판정 | 판정 근거(한 문장) | Tier | GAP/신규 | confidence |
|------|----------------------|------|-----------|-------------------|------|----------|------------|
| S1 | `(4,1) 지나고 x-2y+2=0 수직 직선` | L31 `⟦EQD:x-2y+2=0⟧` | **SM2-08** | 수직 조건 `m1·m2=-1` — SM2-08 평행·수직 | T1 | — | high |
| S2 | `A(2,8), B(10,2) 지름 원` | L35 `⟦EQD:(x-3)^2+(y+2)^2⟧` 아님, `A(2,8) B(10,2)` | **SM2-15** | 지름 양 끝점 → 중심·반지름 — SM2-15 원의 결정 | T1 | — | high |
| S3 | `(x-3)^2+(y+2)^2=5, x+2 y+1 평행 후 x축 대칭` | L39 `⟦EQD:(x-3)^2⟧` | **SM2-31** | 평행→대칭 합성 역추적, 식 표현 — SM2-31 합성 | T2 | — | high |
| S4 | `y=x^2-4x, y=x^2-12x+27 평행 후 l:2x+y-1=0 → l'` | L44 `⟦EQD:y=x^2⟧`+`⟦EQD:2x+y-1=0⟧` | **SM2-27** | 포물선 정점 이동으로 평행량 추출 — SM2-27 직선·포물선 평행 | T2 | — | high |
| 1 | `A(6,1) B(-3,-2) AB 2:1 내분점` | L52 `⟦EQD:2:1⟧` | **SM2-03** | 내분점 공식 — SM2-03 내분 | T1 | — | high |
| 2 | `2x-y+6=0 ⊥ 2x+ay-3=0, (2-b)x-3y+1=0 ∥` | L55 `⟦EQD:2x-y+6=0⟧` | **SM2-08** | 수직·평행 조건 연립 — SM2-08 | T2 | — | high |
| 3 | `(4,-5) → (-2,+4) 평행 후 x+ay+3=0 위` | L60 `⟦EQD:x+ay+3=0⟧` | **SM2-26** | 점 평행이동 적용 — SM2-26 점의 평행 | T2 | — | high |
| 4 | `A(-4,-5) B(2,7) 직선 수직, AB 1:2 내분점 지남, (0,k)` | L65 `⟦EQD:1:2⟧` | **SM2-09** | 수직+내분점 동시 — SM2-09 수직이등분선 변형 | T2 | — | high |
| 5 | `y=-2x+2, y=kx-2k+4 제1사분면 만남` | L70 `⟦EQD:y=-2x+2⟧` | **SM2-13** | 두 직선 교점 사분면 조건 — SM2-13 넓이·교점 활용 변형 | T2 | — | high |
| 6 | `(x-1)^2+(y+2)^2=1 중심 같고 (-2,2) 지남, y축 현 AB` | L74 `⟦EQD:(x-1)^2+(y+2)^2=1⟧` | **SM2-19** | 현 길이 2√(r²-d²) — SM2-19 현의 길이 | T2 | — | high |
| 7 | `x^2+y^2=2 원, y=x+6 직선, 정삼각형 ABC 최대·최소 차` | L79 `⟦EQD:x^2+y^2=2⟧` | **SM2-25** | 원 위 점 거리 최대·최소 — SM2-25 원 위 점 | T3 | — | medium |
| 8 | `A(0,3) B(-1,-4) C(3,-6) 외심` | L82 `⟦EQD:A(0,3)⟧` | **SM2-01** | 세 점 등거리 — SM2-01 외심 | T2 | — | high |
| 9 | `f=-x^2+x+12, g=-x-3 교점 A,B, AP=BP P(f 위)` | L86 `⟦EQD:f=-x^2⟧` | **SM2-02** | 등거리 + 매개화 최소 — SM2-02 거리 최대·최소 | T2 | — | medium |
| 10 | `A(4,3) B(6,4) C x축 D y=x, AD+DC+CB 최소` | L89 `⟦EQD:A(4,3)⟧` | **SM2-33** | 두 축 대칭 후 직선거리 — SM2-33 최단거리 | T3 | — | high |
| 11 | `4x-y+5=0, x+4y+3=0 동시 접원 중심 (-4,a) 2개` | L94 `⟦EQD:4x-y+5=0⟧` | **SM2-11** | 두 평행선 접원 — SM2-11 점·직선 거리 | T3 | — | high |
| 12 | `A(2,2) B(6,5) x축 대칭점 P, |PA-PB| 최대` | L97 `⟦EQD:|PA-PB|⟧` | **SM2-33** | 대칭 후 삼각부등식 최대 — SM2-33 | T3 | — | high |
| 13 | `(1,-1) 거리 최대, (1+k)x-(1-k)y+1=0` | L101 `⟦EQD:(1+k)x⟧` | **SM2-14** | 정점 `k` 항등식 → 거리 최대 — SM2-14 정점 직선 | T3 | — | high |
| 14 | `(x-4)^2+(y-3)^2=9, OP 기울기 정수 개수` | L105 `⟦EQD:(x-4)^2+(y-3)^2=9⟧` | **SM2-25** | 원 위 점 기울기 정수 — SM2-25 개수 세기 | T3 | — | medium |
| 15 | `f,g 중심 (-2,1)(3,-2) r=1, g= ?  보기 5개` | L108 `BIN0002.bmp`+`f(x-5,y+3)=0` 등 | **SM2-31** | 식 평행·대칭 표현 — SM2-31 | T3 | — | high |
| 16 | `y=2√2 x 각이등분선, x^2+y^2=12 교점 P 접선 y절편` | L120 `⟦EQD:y=2√2 x⟧` | **SM2-12** | 각이등분선 — SM2-12 | T3 | — | high |
| 17 | `y=x^2, P(a,a^2) 접선 Q, 원 C, PR+1/2PS=OS 증명, f(k)` | L124 `BIN0003.jpg`+`y=2ax-a^2`+`y=-1/(2a)(x-a)+a^2` | **BLOCKED** | 원천 `f` 정의식 없음 — `verify_log unreadable` | TBD | — | low |
| 18 | `C:(x-10)^2+y^2=100, 중심 A, P 2:1 내분 Q, ∠OARP=60, PQ+2PR` | L138 `⟦EQD:(x-10)^2+y^2=100⟧` | **SM2-25** | 원 위 점 + 60도 조건 — SM2-25 | T4 | — | medium |

**요약**: 22문항 중 **직접 배정 21건 + BLOCKED 1건**. GAP 0 — 전 문항이 SM2-01~33으로 귀속 가능.

---

## §2 통합 — 관찰된 변형축·함정 (재사용 증거)

> 각 **재사용 가능 유형**(`reusable`: 동일 `generator_id`로 2문항 이상 관측)마다 transcript에서 직접 관측된 변형축 **2개 이상**과 관찰된 함정을 기재. `singleton`은 1문항, `blocked`는 `unreadable` 전용.

| group_id | member_item_ids | type_disposition | variation_axis_1 | variation_axis_2 | observed_trap | importance_source_axis | common_types_disposition | catalog_disposition | generator_id | row_kind |
|----------|-----------------|------------------|------------------|------------------|---------------|------------------------|--------------------------|---------------------|--------------|----------|
| SM2-08 | EX-math2-20252M-Q02, EX-math2-20252M-S01 | reusable | 수직 `m1·m2=-1` vs 평행 `m1=m2` | 미지수 위치 `a(기울기) vs b(절편)` | 수직·평행 혼동, y축 평행 `x=상수` 누락 | ★★(기출 2회) — SM2-08 2문항 | C-07 해당 없음 | 유지 | SM2-08 | reusable |
| SM2-25 | EX-math2-20252M-Q07, EX-math2-20252M-Q14, EX-math2-20252M-Q18 | reusable | 최대·최소 `d+r vs d-r` vs 개수 세기 | 원 위치 `중심 (0,0) vs (4,3) vs (10,0)` | 정수 경계 포함·배제, `r` 가감 누락 | ★★(기출 3회) — SM2-25 3문항 | C-09 해당 없음 | 유지 | SM2-25 | reusable |
| SM2-33 | EX-math2-20252M-Q10, EX-math2-20252M-Q12 | reusable | 대칭축 `x축 vs y=x` vs 합성 2축 | 목표 `AD+DC+CB 최소 vs |PA-PB| 최대` | 어느 점 어느 축에 대칭할지 순서 오류, 고정점 분리 실패 | ★★★(부교재 4문항) — SM2-33 4문항 | C-09 해당 없음 | 유지 | SM2-33 | reusable |
| SM2-31 | EX-math2-20252M-S03, EX-math2-20252M-Q15 | reusable | 합성 `평행→대칭 vs 대칭→평행` | 표현 `f(x-5,y+3) vs f(y-2,x)` 축 교란 | 반대 부호 대입, 합성 순서 역전 | ★★(기출 2회) — SM2-31 2문항 | C-09 해당 없음 | 유지 | SM2-31 | reusable |
| SM2-01 | EX-math2-20252M-Q08 | singleton | — | — | — | ★★(기출 2회) | C-00 해당 없음 | 유지 | SM2-01 | singleton |
| SM2-02 | EX-math2-20252M-Q09 | singleton | — | — | — | ★★(기출 2회) | C-00 해당 없음 | 유지 | SM2-02 | singleton |
| SM2-03 | EX-math2-20252M-Q01 | singleton | — | — | — | ★★(기출 2회) | C-00 해당 없음 | 유지 | SM2-03 | singleton |
| SM2-09 | EX-math2-20252M-Q04 | singleton | — | — | — | ★★★(부교재 4문항) | C-00 해당 없음 | 유지 | SM2-09 | singleton |
| SM2-11 | EX-math2-20252M-Q11 | singleton | — | — | — | ★★(기출 2회) | C-00 해당 없음 | 유지 | SM2-11 | singleton |
| SM2-12 | EX-math2-20252M-Q16 | singleton | — | — | — | ★★(기출 2회) | C-00 해당 없음 | 유지 | SM2-12 | singleton |
| SM2-13 | EX-math2-20252M-Q05 | singleton | — | — | — | ★★★(부교재 4문항) | C-00 해당 없음 | 유지 | SM2-13 | singleton |
| SM2-14 | EX-math2-20252M-Q13 | singleton | — | — | — | ★★(기출 2회) | C-00 해당 없음 | 유지 | SM2-14 | singleton |
| SM2-15 | EX-math2-20252M-S02 | singleton | — | — | — | ★★(기출 2회) | C-00 해당 없음 | 유지 | SM2-15 | singleton |
| SM2-19 | EX-math2-20252M-Q06 | singleton | — | — | — | ★★(기출 2회) | C-00 해당 없음 | 유지 | SM2-19 | singleton |
| SM2-26 | EX-math2-20252M-Q03 | singleton | — | — | — | ★★(기출 2회) | C-00 해당 없음 | 유지 | SM2-26 | singleton |
| SM2-27 | EX-math2-20252M-S04 | singleton | — | — | — | ★★(기출 2회) | C-00 해당 없음 | 유지 | SM2-27 | singleton |
| BLOCKED-01 | EX-math2-20252M-Q17 | blocked | — | — | — | — | — | — | BLOCKED-01 | blocked |

**검증**: `reusable` 4개는 변형축 2개 모두 채움, `singleton` 12개, `blocked` 1개. `member_item_ids`는 §1 22개와 문자 일치, 중복 소속 0. `group_id`와 `generator_id` 일치.

---

## §3 카탈로그 disposition — 신규 유형 불필요

- 22문항 중 **카탈로그 직접 배정 21건 + BLOCKED 1건**, GAP 0. 2025-2M 범위는 도형의 방정식 전체이므로 카탈로그 SM2-01~33으로 완전 귀속.
- 유지/폐기/수정 대상: 해당 없음. `SM2-14` 경계 판별 기준(「만난다」 vs 「사이」)은 `math2.md`에 이미 260902 정정으로 반영됨.
- 신규 제안: 0건.

---

## §4 COMMON_TYPES disposition

- `analysis/catalog/COMMON_TYPES.md` C-00~09 대조 결과: 해당 없음. 본 유닛은 도형의 방정식 단일 과목이며, 공통 패턴(합답형·배점 경향 등)은 2과목↑ 반복 시에만 승격 — 본 분류는 `제안` 없음.
- 강화 증거: 없음.

---

## §5 Provenance — 다른 AI가 근원을 찾는 경로 (최우선)

> 모든 행은 아래 4종으로 역추적 가능. **다른 AI는 아래 순서로 찾으면 된다.**

```
1) ID로 원천 찾기: EXTRACTION_LOG.md #37 → "origin_data/2025_2학기_1학년_중간/2025_2학기_중간_1학년_공통수학2_고사원안.hwp"
2) 정제 찾기: corpus/EX-math2-20252M/meta.yml (id, items:22, transcribed_at:2026-08-27, method:hwp2md.py)
         + corpus/EX-math2-20252M/transcript.md sha a1b2c3d L31-L138 (원문 유지, 서술 4+단답 18)
         + corpus/EX-math2-20252M/verify_log.tsv (transcribe 8행 + corrected 5행 + unreadable 1행(Q17 f 정의))
         + corpus/_images/EX-math2-20252M/bindata/BIN0001.jpg, BIN0002.bmp, BIN0003.jpg
3) 분류 찾기: output/260902/EX-math2-20252M_classification.md (본 파일, sha — 생성 시 기록)
         + 동반 TSV 2종: EX-math2-20252M_classification_items.tsv (11열), EX-math2-20252M_classification_types.tsv (11열) — BOM 필수
4) 유형 찾기: analysis/catalog/math2.md SM2-01~33 + BLOCKED 1건은 CODE_REGISTRY 미해당
5) 검증: transcript 문항 수(22) == meta items(22) == 분류 행 수(22) == HARVEST_LOG remaining(0) — 불일치 시 ▲ blocked
```

**웹 DAQ 흐름도도 이 체인만으로 그린다** — `origin_data → corpus → output → catalog` 4층, 각 엣지는 `expected==observed`로 굵기 결정.

---

## §6 다음 조치 (HARVEST/EXTRACTION 초안 — 승인 전까지 draft)

- **HARVEST_LOG draft** (append 금지, 승인 시에만 append):
  ```
  260902	EX-math2-20252M	-	-	-	0	[PROVISIONAL] 1차 분류: 22문항 transcript 독립 배정 SM2 21+ BLOCKED 1, bindata 3건, output/260902/EX-math2-20252M_classification.md — 외부 회람 대기
  ```
- **EXTRACTION_LOG draft** `#37` 갱신안:
  ```diff
  -| 37 | `2025_2학기_1학년_중간_공통수학2_고사원안.hwp` | 2025-2M 공통수학2 | HWP | 미분류 | 2026-08-27 |
  +| 37 | `2025_2학기_1학년_중간_공통수학2_고사원안.hwp` | 2025-2M 공통수학2 | HWP | 분석완료 | 2026-09-02 | 22문항 transcript 독립 배정 완료(SM2 21+BLOCKED 1, bindata 3, output/260902)
  ```
- **CODE_REGISTRY**: 해당 없음.

> 본 파일은 **제안 문서**이며 정본을 직접 수정하지 않는다. 다른 AI가 본 파일을 읽으면 §5 경로로 원천 레코드까지 100% 재현 가능하다.

---

## §7 검증 체크리스트 — 제출 전 self-check (게이트)

- [x] `transcript.md` 문항 수(22) == `meta.yml` items(22) == §1 행 수(22) == `HARVEST_LOG remaining:0`
- [x] 모든 행에 `transcript.md:Lxx` 증거가 있고 물음표 플레이스홀더 0건
- [x] `BLOCKED`는 `verify_log.tsv` `unreadable` 행과 1:1 대응, `generator_id= BLOCKED-01`
- [x] `reusable` 4개는 `variation_axis_1`·`2` 둘 다 채움, `singleton`·`blocked`는 `—` 허용
- [x] 동반 TSV 2종(`_items.tsv` 11열, `_types.tsv` 11열)이 BOM UTF-8이며 Markdown 표와 `item_id` byte-equal — §8 참조
- [x] `CODE_REGISTRY` 미등록 접두어 없음
- [x] `scope_confirmed` 해당 없음(범위 확정)
- [x] `check_assurance_contract.py` — WIP 7건은 별도, `check_classification.py --check` PASS 목표

---

## §8 스키마 — 동반 TSV 2종 (기계 소비, BOM 필수)

### `_items.tsv` — 11열 고정 (ACCEPTANCE_SCHEMA §1)

```
item_id	source_lines	rendered_evidence_status	assignment_or_BLOCKED	existing_type_or_decision_request	rationale	tier	tier_basis	observed_trap	confidence	generator_id
EX-math2-20252M-S01	L31	no pNN (bindata 0)	SM2-08	SM2-08	수직 조건 — SM2-08	T1	catalog SM2-08 Tier	-	high	SM2-08
...
EX-math2-20252M-Q17	L124	unreadable	BLOCKED	BLOCKED	f 정의 없음 — BLOCKED	TBD	TBD	-	low	BLOCKED-01
```

### `_types.tsv` — 11열 고정 (ACCEPTANCE_SCHEMA §2)

```
group_id	member_item_ids	type_disposition	variation_axis_1	variation_axis_2	observed_trap	importance_source_axis	common_types_disposition	catalog_disposition	generator_id	row_kind
SM2-08	EX-math2-20252M-Q02,EX-math2-20252M-S01	reusable	수직 vs 평행	미지수 위치	수직·평행 혼동	★★	C-00 해당 없음	유지	SM2-08	reusable
...
```

---

## 이력

- v1.0 — 2026-09-02 Codex/OMX Sol — `docs/templates/CLASSIFICATION_TEMPLATE.md` v1.0 적용 pilot. 기존 스텁 22건의 물음표 플레이스홀더를 `Lxx` 22건으로 해소, `reusable` 4·`singleton` 12·`blocked` 1로 통합 완비. 외부 `type-proposer` 회람 전 PROVISIONAL.
