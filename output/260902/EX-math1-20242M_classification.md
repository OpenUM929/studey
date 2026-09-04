# EX-math1-20242M 1차 분류 — provenance-first (22문항, transcript 기반)

> **ID**: EX-math1-20242M | **원천**: `origin_data/2024_2학기_1학년_중간/2024_2학기_중간_1학년_수학_고사원안.hwp` (HWP, 배포용 문서)
> **1차 정제**: `corpus/EX-math1-20242M/transcript.md` sha `3f27974` 166행 22문항(단답 18+서술 4) + `meta.yml` items:22 confidence:high + `verify_log.tsv` + `_images` 0장(HWP 경로, pNN 없음)
> **방법**: transcript 문면 한 문항씩 재독해 — 카탈로그 빈도 미참조, 카탈로그 정의와 1:1 대조 후 배정. **근원 추적 최우선**: 모든 행은 `transcript.md:줄번호`와 `verify_log`로 역추적 가능.
> **카탈로그**: `analysis/catalog/math1.md` SM-01~18 (2026 중간·기말 기반: 다항식·복소수·이차함수·행렬). 2024-2중간 범위는 **집합·명제·함수** 중심이라 카탈로그에 직접 대응이 없는 문항은 `GAP → 신규 제안 후보`로 명시(강제 배정 금지).
> **상태**: 제안 문서(PROVISIONAL), 외부 `type-proposer`(Opus) 회람 전. 승인 전까지 HARVEST_LOG/카탈로그 미반영.
> **작성**: Codex/OMX Sol 2026-09-02

---

## 0. 게이트 — 예상=관측=22, 중복0, BLOCKED0

| 항목 | 값 | 증거 |
|------|----|------|
| 예상(transcript 동결) | 22 | `transcript.md` 단답 18(L62-L126) + 서술 4(L138-L153) |
| meta.yml items | 22 | `corpus/EX-math1-20242M/meta.yml:7` |
| 실측(본 분류) | 22 | 아래 §1 표 합계 |
| 중복/결측/초과 | 0 | — |
| BLOCKED(unreadable) | 0 | transcript에는 빈 EQED 1개(L90)와 분절 수식 3건이 있으나 판독 가능으로 처리(verify_log 참조) |
| 이미지 | 0 | HWP 경로 정상 — `BIN0001.jpg` 1건은 표지 로고로 `transcript.md:23,54`에 기록 |

> 검증: `Select-String -Pattern "^\*\*[0-9]+\."` 전수 계수, 각 행의 `L`은 `transcript.md` 줄번호.

---

## 1. 문항별 배정 — transcript 인용 → 판정 (22행, provenance-first)

> `증거` = `transcript.md:줄` + 원천 레코드 근거. `판정`은 카탈로그 정의와 대조한 결과, `GAP`은 신규 유형 제안 후보(강제 배정 안 함). Tier는 카탈로그 해당 유형의 Tier, GAP은 `TBD`.

| 문항 | transcript 인용(핵심) | 증거 | 유형 판정 | 판정 근거(한 문장) | Tier | GAP/신규 |
|------|----------------------|------|-----------|-------------------|------|----------|
| 1 | `f(x)=2x+1, g(x)=x^2+3, (g∘f)(1)` | L62 `⟦EQD:f(x)=2x+1,g(x)=x^2+3⟧` | **GAP-FUNC-01** | 일차·이차 합성함수 값 계산 — math1 카탈로그에 함수 합성 유형 없음 | TBD | 신규 제안: 합성함수 값 |
| 2 | `P⊂R^C, P∪Q^C=P, 보기 ㄱr→q ㄴr→~p ㄷ~q→p` | L64-L68 `P subset R^C` | **GAP-LOGIC-01** | 진리집합·포함관계로 명제 참 거짓 판정 — 카탈로그 SM 미포함(집합·명제) | TBD | 신규: 진리집합 연산 |
| 3 | `U={1..8}, A∩B={2,6}, B-A={1,5,7}, B^C 합` | L70 | **GAP-SET-01** | 유한집합 연산으로 여집합 원소 합 — 카탈로그 집합 유형 없음 | TBD | 신규: 집합 연산 |
| 4 | `p:x^2+ax+8≠0, q:x+2≠0, p→q 참` | L72-L74 | **GAP-LOGIC-02** | 함의가 참이 되는 a — 명제 논리 | TBD | 신규: 함의 조건 |
| 5 | `A={1..6}, B={4..10}, X≠∅, (가)∃x∈X∩A, (나)∀x∈X→x∈B` | L76-L78 | **GAP-SET-02** | 조건 만족 부분집합 개수 — 카탈로그 경우의 수(SM-15)와 유사하나 집합 조건이라 신규 | TBD | 신규: 조건부 부분집합 수 |
| 6 | `n(U)=20, n(A)-n(B)=4, n(A-B)=5, n(A∩B)=6, n(A∪B^C)` | L80 | **GAP-SET-03** | 집합 개수 공식 — 카탈로그 없음 | TBD | 신규 |
| 7 | `p:ab<0, q:|a|+|b|>|a+b| 등 보기 3개, 충분조건∧¬필요조건` | L82-L88 | **GAP-LOGIC-03** | 충분·필요조건 판정 — 논리 | TBD | 신규 |
| 8 | `p:x^2-3x-4≠0, q:ax-2a≤2x+3, p가 ~q의 필요조건` | L92 | **GAP-LOGIC-04** | 필요조건으로 a 개수 — 논리+부등식 | TBD | 신규 |
| 9 | `U={x≤13}, p:x는 2 배수, q:|1/2 x -k|≤5, n(P^C∪Q^C)=7` | L94-L97 | **SM-13 유사/GAP** | 절댓값 부등식+집합 개수 — 카탈로그 SM-13(절댓값 부등식)과 축 공유하나 U가 유한집합이라 **GAP-SET-04**로 분류 | T3(참조) | SM-13 확장 후보 |
| 10 | `a>√2, x=a^2+4/a^2, y=a-2/a, x/y 최솟값` | L99 | **SM-04** | 대칭식 변형 `x=(y^2+2)+?` — SM-04 곱셈공식 변형 | T2 | — |
| 11 | `f(x)=x^2+4x, g(x)=f(x+2)+6, h=f^{-1}, (g∘h)(5)` | L101-L103 | **GAP-FUNC-02** | 역함수+합성 — 카탈로그 행렬/다항식 외 | TBD | 신규: 역함수 합성 |
| 12 | `f(x)=-1/3 x+2, f^{-1}(x)=g(2x-1), y=g(x) 축 넓이` | L105 | **GAP-FUNC-03** | 역함수 관계→평행이동→넓이 — 신규 | TBD | 신규 |
| 13 | `f(x)=cases{-1/4 x^2+1(x≥0), 1/4 x^2+1(x<0)}, g(x)=3|x|-8, g(f(x))=g(x) 합` | L107 | **GAP-FUNC-04** | 구간 이차+절댓값 합성 방정식 근 합 — 신규(카탈로그 SM-09 유사하나 구간+절댓값이라 신규) | TBD | 신규 |
| 14 | `f(x)=cases{x^2+x(x≤a), -3x+k(x>a)}, g(x)=2x+5, g∘f 역함수 존재, k 최솟값` | L109 | **GAP-FUNC-05** | 합성함수 전단사 조건으로 k — 신규 | TBD | 신규 |
| 15 | `f=x^2-6x+a, g=cases{-x+2(x≤0),x-2(x>0)}, (g∘f)(x)=4 근 개수 h(a), 0<h<3 정수 a 개수` | L111 | **GAP-FUNC-06** | 구간함수 합성 근 개수 — 신규 | TBD | 신규 |
| 16 | `U={x≤7}, n(A)≥2, A 모든 원소 곱은 8 배수 아님, A 개수` | L113-L116 | **SM-15 유사/GAP** | 부분집합 개수+조건 — SM-15(경우의 수 나열)와 축 공유하나 곱 조건이라 **GAP-CNT-01**로 분류 | T3(참조) | SM-15 확장 후보 |
| 17 | `A={1,2,a}, B={2,b}, X={x+y}, Y={x×y}, n(X∪Y)+n(X∩Y)=10, n(X)=n(Y), a×b<16` | L119-L121 | **GAP-SET-05** | 집합 생성·개수 연립 — 신규 | TBD | 신규 |
| 18 | `X={x≤24}, f:X→X, f(1)=2, f(n^2+k)=3f(n)-k, f(f(m))=m 합` | L123-L126 | **GAP-FUNC-07** | 함수 점화식+역함수 조건 — 신규(2024 고난도) | T4 후보 | 신규 |
| S1 | `n^2 짝수→n 짝수 대우 증명` | L138 | **GAP-LOGIC-05** | 대우법 증명 — 논리 서술형, 카탈로그 SM 없음 | T2 | 신규: 증명 |
| S2 | `X={x|-1≤x≤2}, Y={y|1≤y≤7}, f(x)=ax+b 일대일대응` | L140 | **GAP-FUNC-08** | 일대일대응 선형함수 — 신규 | T2 | 신규 |
| S3 | `U={x≤k}, A-B={1,3}, n(A^C∪B)=6, 합(B)=k, (1)A-B∪(A^C∪B) (2)k (3)A^C∩B^C 합` | L142-L145 | **GAP-SET-06** | 집합 3문항 세트 — 신규 | T3 | 신규 |
| S4 | `X={1..7}, f:X→X, |치역|=6, Σf=34, max-min=5, f(a)=f(b)=n` | L149-L153 | **GAP-FUNC-09** | 함수 치역·합·범위 조건으로 중복값 — 신규 | T4 후보 | 신규 |

**요약**: 22문항 중 **카탈로그 직접 배정 1건(SM-04: 10번) + 유사 참조 2건(9번 SM-13, 16번 SM-15)** , **GAP 19건**. 이는 **2024-2중간 범위가 카탈로그(math1.md, 2026 기반)와 불일치**함을 증명 — 강제 배정 대신 GAP으로 남겨 **CODE_REGISTRY에 신규 접두어(SET/LOGIC/FUNC)**를 제안하는 것이 올바른 provenance다.

---

## 2. Provenance — 다른 AI가 근원을 찾는 경로 (최우선)

모든 행은 아래 4종으로 역추적 가능. **다른 AI는 아래 순서로 찾으면 된다.**

```
1) ID로 원천 찾기: EXTRACTION_LOG.md #40 → "2024_2학기_1학년_중간/2024_2학기_중간_1학년_수학_고사원안.hwp"
2) 정제 찾기: corpus/EX-math1-20242M/meta.yml (id, items:22, transcribed_at:2026-08-26, method:pyhwp 복원, marker 161)
         + corpus/EX-math1-20242M/transcript.md sha3f27974 L62-L153 (원문 유지)
         + corpus/EX-math1-20242M/verify_log.tsv (transcribe 행, evidence: Section0-2 레코드)
3) 분류 찾기: output/260902/EX-math1-20242M_classification.md (본 파일, sha — 생성 시 기록)
4) 유형 찾기: analysis/catalog/math1.md SM-01~18 + GAP 19건은 CODE_REGISTRY 신규 제안으로 분기
5) 검증: transcript 문항 수(22) == meta items(22) == 분류 행 수(22) == HARVEST_LOG remaining(0) — 불일치 시 ▲ blocked
```

**웹 DAQ 흐름도도 이 체인만으로 그린다** — `origin_data → corpus → output → catalog` 4층, 각 엣지는 `expected==observed`로 굵기 결정. 그림(`BIN0001.jpg`) 유무는 노드 속성일 뿐 매핑 계산에 쓰지 않는다.

---

## 3. 다음 조치 (GAP 19건)

- **CODE_REGISTRY**: `SET-nn`(집합), `LOGIC-nn`(명제), `FUNC-nn`(함수 합성/역함수) 접두어 신설 제안 필요 — `analysis/catalog/COMMON_TYPES.md`와 충돌 검토 후 `type-proposer`(Opus) 회람
- **HARVEST_LOG**: 본 분류 승인 전까지 미기재 — 승인 시 `new_types: GAP 19 후보`로 기록
- **재현성**: 수치 재계산(예 10번 `x/y` 최솟값)은 `generated_answer.md`에서 별도 검증, 본 분류는 사실 판정만

> 본 파일은 **제안 문서**이며 정본을 직접 수정하지 않는다. 다른 AI가 본 파일을 읽으면 §2 경로로 원천 레코드까지 100% 재현 가능하다.
