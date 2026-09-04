---
actor: 메인 루프
task: bf_apply — 260831_03 판정 구속수정 BF1~BF7 발주·반영
target: output/260831/260831_03_arbiter_ruling.md 구속수정 7건 + K1 two-key
status: in-progress
updated: 260831
---

## 근거

`output/260831/rev/260831_03_arbiter_ruling.md` — verdict `revise-required`, binding_fixes 7.
소유자 배분: type-proposer 4(BF1·BF3·BF4·BF5) · rev-writer 1(BF2) · type-extractor 1(BF7) ·
메인 루프 1(BF6). 별도로 K1(자 재보정)은 **사용자 키 대기** — 발주 대상 아님.

## 선행 감사 (모델 전환 후 오염 확인)

이 세션의 메인 루프는 슬라이스 6~arbiter 발주 구간을 **Haiku 4.5**로 수행했고(`/context` 실측),
그 구간 회람문 3건(260831_11·_12·_13)에서 결함이 적발됐다(경로 오기·사실오류 3건·§6-d 필드 전무·
open unit 3건 미상신). 판정 오염 여부를 Opus 전환 후 직접 검증했다.

| 검증 | 명령 | 기대 | 실측 | 판정 |
|---|---|---|---|---|
| 밴드 적합 전수 | 판정문 §6 python | `N=119 band3.0-4.2=19(16.0%) max=3.3 ge4.0=0` | 동일 | OK |
| MR-a 잔여 | 〃 | `MR-a pop=99 fit=19 residual=80/99` | 동일 | OK |
| MR-b 폐쇄 | 〃 | `MR-b 1.2-3.3 = 119/119` | 동일 | OK |
| 구 밴드 | 〃 | `old 2.2-2.8 = 67/119` | 동일 | OK |
| X2 6개소 실재 | 판정문 §6 bash | OK 6줄 / FAIL 0줄 | OK 6 / FAIL 0 | OK |
| 과목별 분포 | 판정문 §1-2 표 | KO 0/29·SC 2/23·SS 13/20·EN 4/27·HI 0/20·SM2 부재 | 동일 | OK |

**결론**: 판정문의 모든 인용 수치는 arbiter가 fresh context에서 재산출한 값이며 재현된다.
회람문 결함은 판정에 전파되지 않았다(arbiter가 누락 3건을 직권 복원). 판정 유효 — BF 반영 진행.

## 동결 입력 (발주 직전 실측)

| path | bytes | sha256(16) | role |
|---|---:|---|---|
| output/260831/260831_01_type_analysis_EN.md | 30688 | e987a98ad6abeeb1 | output |
| output/260831/260831_01_catalog_update_HI.md | 38777 | 0ba05eb92d9da401 | output |
| output/260831/rev/260831_01_review_SM2.md | 9558 | 99ed49d8f803e39c | evidence |
| output/260831/rev/260831_01_review_KO.md | 9442 | 9d69c9e43cf9270c | evidence |
| corpus/EX-korean-20252M/transcript.md | 83536 | bc455037bad8f196 | source |
| corpus/EX-korean-20252M/meta.yml | 1158 | 8c3286addd588e71 | derived |

## 슬라이스

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | 판정문 정독 + 재현명령 실행 | done | 위 감사표 | 전건 재현 |
| 2 | 대상 행 실측(BF1·BF3·BF4·BF2·BF7) | done | 위 동결표 | 전 행 원문 확인 |
| 3 | type-proposer 발주 (BF1·BF3·BF4·BF5) | done | — | 병렬 |
| 4 | rev-writer 발주 (BF2) | done | — | 병렬 |
| 5 | type-extractor 발주 (BF7) | done | — | 병렬 |
| 6 | BF6 자체 반영 (§6-d 패킷 규격) | done | 아래 §BF6 | 메인 루프 소관 |
| 7 | 3소유자 회신 수합·검증 | done | BF1~BF7 전건 반영 | 반박 3건 접수 — 아래 |
| 8 | K1 사용자 키 상신 | done | 260831 키 부여 | — |
| 9 | K1 정제 측정 | done | tools/measure_score_bands.py · 260831_14 | 게이트 3종 |
| 10 | K1 밴드값 arbiter 서명 요청 (1차) | blocked | - | HOLD - session limit, 11pm reset |
| 11 | resume audit | done | 아래 표 | 재개 조건 충족 |
| 12 | K1 밴드값 arbiter 서명 요청 (재개) | in-progress | 260831_14 패킷 | 슬라이스 2부터 |

## §BF6 — 메인 루프 자체 반영 (판정문 §3 BF6)

**지적**: 260831_13 요청 패킷에 `<frozen_inputs>`·`<actor_grade>`·`<units>`의 `reproduce:`가 전무했고,
tier-2 상신 open 집합 7건 중 3건(N2-c·N5-c·X2)이 판정 단위로 올라가지 않았다. 제목 `X1~X4` ↔
본문 표 `X1~X5` 자기 불일치.

**반영**: 이 WIP의 「동결 입력」 표가 §6-d (1)-1 형식(path|bytes|sha256|role)의 첫 적용이다.
이후 판정 요청 시 아래를 발신 전 점검한다.

- [ ] `<frozen_inputs>` 표 존재 + 본문이 경로로 지목하는 파일 전건 수록(또는 `<excluded>` 사유)
- [ ] `<units>` 각 항에 고유 ID + 질문형 + `verdict enum` + `reproduce:` 1줄
- [ ] `<actor_grade>` 요청 측이 미리 기재
- [ ] `<open_units>` = 직전 라운드 상신 집합 **전건**(부분 상신 금지 — X2 사고)
- [ ] `<out_of_scope>` 명시
- [ ] 제목의 unit 범위 ↔ 본문 표 범위 일치 확인
- [ ] 인용 수치·경로는 발신 직전 실측(원칙 9-c-i·ii)

## 소유자 회신 요약 (260831)

| BF | 소유자 | 결과 |
|---|---|---|
| BF1·BF3·BF4·BF5 | type-proposer | 반영. 병합ID `DQ-RUBRIC-1`, Tier 표식 배너11+절마커34 |
| BF2 | rev-writer | 반영. review_SM2 4개소·review_KO 1개소 |
| BF6 | 메인 루프 | 이 WIP §BF6 |
| BF7 | type-extractor | 반영. 원본 대조로 60.4가 인쇄값 아님 확인 |

## 실행 레인이 제기한 반박 3건 (원칙 12-a — 우회 대신 상신)

1. **[메인 루프 오류 — 확인됨]** rev-writer 지시문에 `_index.md:18` 표 손상을 고지했으나
   **사실무근**. 직접 재측정: 헤더 L5도 18행도 10필드/9파이프로 동일, 손상 없음.
   출처는 판정문 회신 요약의 `REV_LOG` 관련 서술을 내가 파일명을 바꿔 전달한 것.
   실제 손상은 **`analysis/REV_LOG.md` L101·L103·L106** (7필드 규격에 대해 9·8·10필드).
   소유자 각각 다르므로 원칙 8에 따라 미수정 — 후속 항목.
2. **[결정요청 — type-proposer]** BF1/BF3 게이트가 문자 그대로는 불통과(`선택(단답)형`=1·`60.4`=2·
   예외조항=1). 잔여는 전부 **정정 이력·철회 근거 안의 인용**이고 live 표 행은 0건.
   삭제하면 원칙 3(이력 보존)과 충돌 → 게이트를 「live 표 행 0건」으로 정밀화할지 판정 필요.
3. **[측정 정정 — type-proposer]** (a) 판정문의 math2 `18/18`은 인라인 마커로는 16건이며
   나머지 2는 `transcript.md:20` 계수 선언에서 유도 (b) 판정문 §1-6 Tier 수치는 토큰수가
   아니라 **행수**다(5/6 재현, SM2만 59 vs 58). 둘 다 조치에는 영향 없음.

## resume audit (260901, CLAUDE.md 원칙 5)

1차 발주가 `rate_limit HTTP 429 / session limit, resets 11pm (Asia/Seoul)`로 중단됐다.
모델 하향·병렬 재시도·busy-wait 하지 않고 reset 이후 1회만 재개한다.

| 점검 | 결과 |
|---|---|
| 새 quota | reset 시각(11pm) 경과 |
| 판정문 산출물 | `260831_04_*` **미생성** - 깨끗한 재개, 부분 산출물 병합 불필요 |
| 배타 작성권 | arbiter WIP `rev-arbiter_260831_K1_band_signature.md` 존재, 슬라이스 1 done / NEXT=슬라이스 2 |
| 충돌 writer | 없음 (type-proposer·rev-writer·type-extractor 전건 done) |
| 동결 입력 해시 | `measure_score_bands.py` 8c89afe6c6963f81 / `DIFFICULTY_RUBRIC.md` 1533e2930d10fd30 / `260831_03` f9a50f4c561ff8c3 / `260831_14` e718fa0c0bec7b28 - **발주 시점과 전건 동일** |
| 자 무편집 | `DIFFICULTY_RUBRIC.md` 해시 불변으로 확인 |
| 다음 검증 명령 | `python tools/measure_score_bands.py` (기대 GATE1 PASS undetected=0 / dup=1 / mismatch=2) |

불일치 0건 - `blocked` 해제.

NEXT: arbiter 재개(슬라이스 2부터) → 서명 → 반영 → 루프 종결
