---
actor: codex-omx
date: 260830
task: math2-novel-40 full authoring sequence test
status: in-progress
exclusive_writer: Codex/OMX main loop
set_id: SET-260830-math2-40
intended_use: practice
parallel_basis: user-directed bounded branch; independent of 260829 ruler candidate S2/S3/S4
---

# WIP — 공통수학2 비수치 신규 40문항 전체 시퀀스 시험

## 목표·정지 조건
- 목표: `analysis/catalog/math2.md`의 SM2-01~33을 근거로 40문항을 만들되, 숫자·좌표·길이·각도·부호·문자명만 바꾼 문항을 0건으로 만든다.
- 산출: `output/260830/260830_01_math2_novel_40.md` + 같은 stem의 `.novelty.tsv` + 작성 part 파일/각 작성자 WIP + 게이트 증거.
- 정지: pilot gate 실패, source/catalog 정당성 때문에 해당 주장에 근거가 없을 때, 배타 write 충돌, 또는 external `solve-back-verifier` 회신 부재 시 `HOLD`/`▲ blocked`로 멈춘다. 외부 회신 전 release 금지.
- 범위: 부교재 기반 `검증(부교재)` 유형의 **연습용(practice)** 세트. 카탈로그의 93문항 원천 추적성이 아직 복구되지 않았으므로 “기출 예측”·“출제 확률 확정” 주장은 하지 않는다.

## 동결 입력
- `analysis/catalog/math2.md` — 유형·비수치 변형 축·단원 6/10/14/10·Tier 4/12/16/8.
- `analysis/catalog/{COMMON_TYPES.md,TYPE_MASTER.md,DIFFICULTY_RUBRIC.md,AUTHORING_GUIDE.md}`.
- `analysis/curriculum_2022.md`, `docs/QUIZ_STANDARD.md`, `docs/DATA_STANDARD.md`.
- 중복 회피용 선행 생성 세트: `output/260822/공통수학2_도형의방정식_모의40.md`, `output/260829/260829_02_math2_comprehensive_25.md`.
- 원본 PDF·유실 transcript는 author에게 제공하지 않는다(정본 카탈로그 소비 원칙).

## staffing matrix (dispatch 전 실측)
| objective/unit | count | evidence density / known defects | schema | exclusive write surface | lane = model = depth | estimate | max concurrency | validation gate | stop/resume |
|---|---:|---|---|---|---|---|---:|---|---|
| ruler/contract implementation | 2 governed docs + validator/tests | core rule existed in item-writer, but non-numeric axis definition·per-item evidence·ID coverage gate absent | prose contract + 8-column TSV + fail-closed CLI | `.claude/agents/item-writer.md`, `analysis/catalog/AUTHORING_GUIDE.md`, `tools/check_novelty_ledger.py`, `tests/test_check_novelty_ledger.py` | coordinator = gpt-5.6-sol = high (configured; observed unavailable) | 1 slice | 1 | unit tests + candidate positive/negative fixtures, warnings=0 | validator qualification before author wave |
| pilot author P1 | 5 items: SM2-05,09,16,24,33; T1/T2/T3/T4 mixed | catalog has ≥5 axes each; original transcript absent; prior generated sets frozen for nearest-prior comparison | part MD + 5-row novelty TSV + self solve-back evidence | `output/260830/parts/P1.*`, `analysis/wip/item-writer_260830_SET-260830-math2-40_P1.md` | item-author = gpt-5.6-sol = medium (configured; observed unavailable) | ≤1 turn | 1 | 5/5 unique IDs, FAIL=0, ≥2 non-numeric axes/item, exact answers | inspect before wave 1 |
| pilot independent review | same 5 items | author reports 5/5 but review/fix separation required; original transcript remains excluded | advisory report, one row/item + set-level findings | `output/260830/rev/P1_ADVISORY_REVIEW.md`, reviewer-own WIP | code-reviewer = gpt-5.6-sol = high (configured; observed unavailable) | 1 turn | 1 | math correctness·condition sufficiency·Tier·novelty claims·format, 5/5 coverage | author fixes only evidence-backed findings, then rerun gates |
| wave authors | I-1=6, I-2=10, I-3=14, I-4=10; pilot items are design probes, final numbering assigned per bundle | 33 catalog types; catalog source trace incomplete; cross-set duplicates possible | exclusive part MD/TSV; no shared set writes | `output/260830/parts/<bundle>.*` + unique writer WIP | item-author lanes = gpt-5.6-sol = medium (configured; observed unavailable) | ≤10 items/lane | 3 | bundle item IDs/count/type/Tier/novelty/solve-back | staged wave; resize on any FAIL |
| wave independent review | W1 bundles 5/9/7 then W2 bundles 5/9 | author evidence can miss semantic novelty, Tier inflation, redundant conditions (P1 empirically found all three) | advisory report with row per item + finding closure | `output/260830/rev/<bundle>_ADVISORY_REVIEW.md` + reviewer-own WIP | code-reviewer lanes = gpt-5.6-sol = high (configured; observed unavailable) | ≤9 items/lane | 3 | exact solve, deletion audit, Tier, semantic novelty, static, CLI | any finding returns only to owning author; no wave advance |
| integration | 40 items | seam/render/tag/answer-table risks | final MD + final TSV | final two files, main-loop single owner | coordinator = gpt-5.6-sol = high | 1 slice | 1 | exact 40 IDs, distributions, parser smoke, novelty FAIL=0, warnings=0 | then external pre-gate only |
| blind solve qualification | 40 items | author self-solve is not independent | report per REV_GUIDE | external reply only | external `solve-back-verifier` = Opus = external | one main session/pilot policy | 1 | 40/40 blind solve, uniqueness, conditions, Tier, middle steps | HOLD until reply exists |

## 고정 분포
- 단원: I-1 6 / I-2 10 / I-3 14 / I-4 10 = 40.
- Tier: T1 4 / T2 12 / T3 16 / T4 8 = 40.
- 형식: 전 문항 서답형; 방정식·범위·개수형 포함; 평면좌표 후반 증명 1문항 허용.
- 필수 유형: SM2-09,13,16,24,28,33. 33개 유형 전부 최소 1회 사용하고 7개 주력 유형을 1회씩 추가하여 40문항을 구성한다.
- 신규성: 문항별 비수치 축 ≥2, `.novelty.tsv` 40/40, `FAIL=0`; scalar/cosmetic substitutions do not count.

## frozen item map (pilot clean pass 후)
| bundle | final item = type/Tier | count | exclusions |
|---|---|---:|---|
| P1 done | 6=SM2-05/T3; 12=SM2-09/T2; 20=SM2-16/T3; 30=SM2-24/T4; 40=SM2-33/T4 | 5 | 다른 bundle은 이 ID·유형 슬롯을 쓰지 않는다 |
| W1-I1 | 1=SM2-01/T1; 2=SM2-02/T2; 3=SM2-03/T2; 4=SM2-04/T2; 5=SM2-06/T2 | 5 | item 6 제외 |
| W1-I2 | 7=SM2-07/T1; 8=SM2-08/T2; 9=SM2-10/T2; 10=SM2-11/T3; 11=SM2-12/T3; 13=SM2-13/T3; 14=SM2-14/T4; 15=SM2-11/T3; 16=SM2-13/T4 | 9 | item 12 제외 |
| W1-I3A | 17=SM2-15/T1; 18=SM2-17/T2; 19=SM2-18/T3; 21=SM2-19/T2; 22=SM2-20/T2; 23=SM2-21/T3; 24=SM2-22/T3 | 7 | items 20,25-30 제외 |
| W2-I3B | 25=SM2-23/T3; 26=SM2-24/T3; 27=SM2-25/T3; 28=SM2-18/T4; 29=SM2-22/T4 | 5 | wave 1 clean pass 전 dispatch 금지 |
| W2-I4 | 31=SM2-26/T1; 32=SM2-27/T2; 33=SM2-28/T2; 34=SM2-29/T3; 35=SM2-30/T3; 36=SM2-31/T3; 37=SM2-32/T3; 38=SM2-28/T4; 39=SM2-33/T4 | 9 | item 40 제외; wave 1 clean pass 전 dispatch 금지 |

합계 gate: IDs 1..40 exact cover; 33유형 전부 ≥1; duplicate slots 7; Tier T1/T2/T3/T4 = 4/12/16/8; 단원 6/10/14/10.

## 슬라이스
| no | 범위 | state | 산출물 | 비고 |
|---:|---|---|---|---|
| 1 | 선행 HOLD·지침·정본 실측 | done | 이 WIP | S2 reply 2파일 미존재; 별도 bounded parallel branch로 한정 |
| 2 | 신규성 계약 보강 | done | item-writer + AUTHORING_GUIDE | 기존 원칙을 비수치 2축 정의·8열 evidence ledger·exact ID coverage로 강화 |
| 3 | novelty validator + tests | done | tools/tests + qualification reports | 1차 A1/A2 → 2차 M1 수리 후 3차 독립 qualification `approve`; hashes 4/4, tests 8/8, CLI 8/8, warnings=0 |
| 4 | P1 pilot 5문항 | done | parts/P1.* + author WIPs | initial author→replacement sequential ownership; R2 final hash `69e5e9da…`/`84d13437…`; self-solve·novelty PASS |
| 4a | P1 independent advisory review | done | review reports + reviewer WIPs | initial 6 findings + R1 condition redundancy 1건을 author가 수정; R2 clean pass 5/5, new findings 0 |
| 4b | P1-R1 resource resume audit·ownership handoff | done | 이 WIP | initial author runtime `/root/math2_pilot_author` usage-limit error, reset 02:26 KST; 08:05 KST 1회 audit에서 review 동결 3파일 hash 일치·충돌 writer 0. 완료 unit=P1 initial+review, 미완료=P1-R1. 새 author는 P1 두 artifact + 새 `_P1_R1` WIP만 소유; 기존 author WIP 불변 |
| 5 | wave 1 authoring | done | W1-I1/W1-I2/W1-I3A parts + unique WIPs | 21/21 authored; exact novelty CLI each PASS warnings=0; shared write 0 |
| 5a | W1-I2 resource resume audit | done | 이 WIP | author final-response usage error/reset 13:04; 13:10 audit에서 MD/TSV/WIP 모두 status=done·NEXT review·gate PASS, 충돌 writer 0. 완결 bounded slice로 채택, retry 없음 |
| 5b | wave 1 independent review | in-progress | 3 review reports + reviewer WIPs | bundle별 `fork_turns=none`, review-only, 원본 수정 금지 |
| 5c | W1-I2 reviewer artifact recovery | in-progress | `W1_I2_ADVISORY_REVIEW.md` + writer WIP | code-reviewer 9/9 review는 4 HIGH를 반환했으나 role read-only로 파일 2건 미생성(`▲ blocked`). 별도 Codex/OMX `rev-writer` 책임 lane이 동결 target을 재검증·문서화하며, reviewer 실행을 파일 생성으로 소급 주장하지 않는다 |
| 6 | wave 2 + integration | pending | final MD/TSV | shared integration sequential |
| 7 | local gates + external relay | pending | gate evidence + [CC 회람] | external reply 전 release 금지 |

NEXT: W1-I1(5)·W1-I2(9)·W1-I3A(7)을 서로 다른 independent reviewer가 21/21 재계산·조건삭제·Tier·semantic novelty·static/CLI 판정한다. finding은 해당 author에게만 반환하며 세 report 모두 clean pass 전 W2 금지.
