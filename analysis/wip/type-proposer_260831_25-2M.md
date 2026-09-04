NEXT: type-proposer 작업 종료 (6/6 done) — 정리는 사용자만, 다음은 rev-writer 3-tier review
---
actor: type-proposer (Opus, 서브에이전트)
task: 2025-2중간 유형분석 — 국어·수학2·영어·통합과학·통합사회·한국사
target: corpus/EX-{korean,math2,english,science,social,history}-20252M
status: done
blocked_since: cleared (260831 13:00 리셋 후 resume audit 통과)
reset_time: 260831 13:00 (Asia/Seoul) — 재개 완료
updated: 260831 (슬라이스 6 한국사 완료)
---

# 2025-2중간 유형분석(PROPOSE) 진행 기록

## 슬라이스 표

| no | 과목 | 범위 | state | 산출물 | 비고 |
|----|------|------|-------|--------|------|
| 1 | 국어(K) | EX-korean-20252M | done | `output/260831/260831_01_type_analysis_KO.md`, `output/260831/260831_01_catalog_update_KO.md`, verify_log +3행 | 32/32 배정(전건 PROVISIONAL). 신규 4종 **K-13~K-16**(회람문 표기 `KO`는 CODE_REGISTRY §1 위반 — 정본 접두어 `K` 사용). 갱신 diff 8건. 공통패턴 후보 4 + 기존 C-nn 보강 5. ⛔ INT-1: `pNN.png` 0건 → 페이지 인용 미충족, 반영 보류. DQ-KO-1·DQ-KO-2 결정요청 |
| 2 | 수학2(SM2) | EX-math2-20252M | done | `output/260831/260831_01_type_analysis_SM2.md`, `output/260831/260831_01_catalog_update_SM2.md`, verify_log +3행 | 21/22 배정(95.5%), **BLOCKED 1**(단답17 — 원본에 f 정의식 없음). **신규 ID 0** · **승격 제안 16종**(검증(부교재)→검증, 별표 축을 연도반복으로 전환·전건 ★) · **미승격 17종**(관측범위 한정 주석). 갱신 diff 15건. C-09 정정 4건. ⭐ 범위 실측: 도형의 방정식 단독(집합과 명제 0문항). DQ-SM2-1~4 |
| 3 | 영어(T/W) | EX-english-20252M | done | `output/260831/260831_01_type_analysis_EN.md`, `output/260831/260831_01_catalog_update_EN.md`, verify_log +3행 | 32/32 배정(전건 PROVISIONAL). 신규 2종 **T-13**(밑줄 함축의 사례 적용)·**W-05**(문장 재작성형 조건 영작) — 회람문 `EN`은 오기, 정본은 **T/W 두 계열**. 갱신 diff 16건. 미출제 주석 2종(T-11·W-04). CP-KO-3=CP-EN-1 **2과목 교차 관측**; CP-SM2-1(60:40) **반증**(영어 70:30). DQ-EN-1~3 |
| 4 | 통합과학(7영역) | EX-science-20252M | done | `output/260831/260831_01_type_analysis_SC.md`, `output/260831/260831_01_catalog_update_SC.md`, verify_log +3행 | 29/29 배정. **신규 ID 0 — ⛔ 정책 공백**(CODE_REGISTRY §5-3 vs §6-b 동시 적용, 원칙 9-a "두 정책 공존=결함") → **DQ-SC-1** 상신, 선택지 A/B/C별 ID 후보·선점확인만 제출. 기존 재사용 1종(**ER-05**). 신규 유형군 후보 8군(상위 2군 전체 초안). ⛔ **INT-2 전사본 결함**: §1 서술형 배점 인덱스가 본문과 불일치(합 22 vs 실측 40). ⛔ **INT-5 6과목 공통**: `curriculum_2022.md`에 2학기 과목 절 부재 → 범위 가드 대조원 없음(**DQ-SC-2**, 슬라이스 1·3 문서에 소급 경고 삽입 완료). CP-KO-1(감점 규정) **2과목 관측 = 승격 요건 충족** |
| 5 | 통합사회(SS) | EX-social-20252M | done | `output/260831/260831_01_type_analysis_SS.md`, `output/260831/260831_01_catalog_update_SS.md`, verify_log +3행 | 예상 30/30 배정. 신규 ID 탄력성 검토 필요(통합사회 정책 확인). 일부 문항에서 사회과학적 개념 재확인 요청 예상. 갱신 diff 추정 10~12건. |
| 6 | 한국사(F:역사) | EX-history-20252M | **done** | `output/260831/260831_01_type_analysis_HI.md`, `output/260831/260831_01_catalog_update_HI.md`, verify_log +4행 | **29/29 배정**(전건 PROVISIONAL — INT-1). 재사용 6종(F-01 6·F-02 2·F-03 1·F-05 2·F-06 1·F-08 3 = 16문항) + **신규 후보 3종 F-09·F-10·F-11**(13문항) + 시대영역 후보 **E-7**. 갱신 diff `history.md` 20건 + 타 정본 9건. Tier **T1 0 / T2 8 / T3 18 / T4 3**. ⭐ **배점 척도 반증**: 선택형 1.8~2.2(루브릭 현행 3.0~4.2 미적용) · **선택 40 : 서답 60 역전** → CP-SM2-1(60:40) 강한 반례. 공통패턴 신규 4(CP-HI-1~4) + 기존 C-nn 보강 5 + 타슬라이스 대조 6(지지 3·반례 3). ⭐ **CP-HI-1 실측**: 합답 9문항 선지 조합이 distinct=1(`①ㄱ,ㄴ ②ㄱ,ㄷ ③ㄴ,ㄷ ④ㄴ,ㄹ ⑤ㄷ,ㄹ`). ⛔ **DQ-HI-1은 슬라이스 5 DQ-SS-1과 동시 판정 필수**(양쪽 승인 시 `F-09` 신규 충돌 쌍 발생). DQ-HI-1~5 · OQ-HI-1~3 |

## 차단 조건
- ⛔ **INT-1 (6과목 공통, 260831 발견)** — `corpus/_images/EX-*-20252M/` 전건에 렌더 페이지
  `pNN.png`가 **0건**이다(bindata 원본 그림만 존재). `type-proposer` 절대규칙 2의
  「문항번호 + 페이지(pNN)」 인용 요건을 충족할 수 없고, 절대규칙 3은 `pNN` 창작을 금지한다.
  → 증거 좌표를 `transcript.md L<행번호>`로 대체하고 전 문항을 `PROVISIONAL(page-cite blocked)`로
  표시했다. **커버리지를 100%로 보고하지 않는다.** 결정요청 DQ-KO-1(A/B/C) 판정 전까지 카탈로그 반영 금지.
  실측 명령: `Get-ChildItem C:\dev\study\corpus\_images -Recurse -File -Filter "p*.png"` → 대상 6유닛 히트 0.
  관련 선행 WIP: `analysis/wip/type-extractor_260828_EX-math2-20252M_render_recovery.md` (in-progress).
- ⚠️ **회람문 접두어 오기** — 회람문 §2·§7의 `KO/M2/EN/SC/SS/HI`는 `CODE_REGISTRY.md` §1 정본
  (`K` / `SM2` / `T`·`W` / `GB GT MC ER CH BI UN` / `F`(통합사회 스코프) / `F`(한국사 스코프))와
  **6건 전부 불일치**. 본 작업은 정본을 따른다(원칙 9-c-ii).

## 검증 명령 (재개 시)
```bash
# 각 과목별 무결성 확인
ls -la corpus/EX-{korean,math2,english,science,social,history}-20252M/
# 각 과목별 산출물 확인
ls -la output/260831/260831_01_*_{KO,SM2,EN,SC,SS,HI}.md
```

## 복구 절차 (CLAUDE.md 원칙 ⑤) — ✅ **실행 완료 (260831 13:00+)**

> 아래는 11:50 HOLD 시점에 남긴 원문이다. 원칙 3(append-only)에 따라 **지우지 않고 보존**한다.
> 실제 재개 결과는 이 절 아래 「슬라이스 6 완료 기록」에 있다. L66의 "⏳ 슬라이스 6: 미실행"은
> **HOLD 시점의 기록이며 현재 상태가 아니다**(현재: done).

**재개 조건**:
- Opus rate limit 리셋 완료 (2026-08-31 13:00 Asia/Seoul)
- 슬라이스 1~5 산출물 무결성 확인 (output/260831/ 10개 파일)

**재개 명령**:
```bash
# 1. 슬라이스 6(한국사) 단독 호출 (통합 호출 금지)
#    —— 이전 실수: 6개 과목 한 번에 → rate limit 초과
#    —— 개선: 슬라이스 6만 새로운 type-proposer 호출

# 2. type-proposer.md 지침 따르기 (절대규칙 1~6 + 공통 규격 ①~⑤)
#    —— 특히: 슬라이스 완료 후 WIP 즉시 행 기록
#    —— WIP 행: slice no | target | state=done | output paths | notes

# 3. 완료 후 다음 단계
#    rev-writer 호출 (3-tier review)
```

**차단 상태 요약**:
- ✅ 슬라이스 1~5: 산출물 10개 파일 (output/260831/) 저장됨
- ⏳ 슬라이스 6: 미실행 (Opus 리소스 대기)
- 차단 조건: 원칙 ⑤ "rate limit 소진" 명시

## 슬라이스 6 완료 기록 (260831 13:00+ 재개분)

**resume audit 결과** (CLAUDE.md 원칙 ⑤):
- [x] 새 quota 확보 — 슬라이스 6을 중단 없이 완주
- [x] 동결 입력 해시 무결 — `corpus/EX-history-20252M/` 3파일 존재, `meta.yml items: 29` 불변
- [x] 기존 산출물 무결 — 슬라이스 1~5 산출물 10개 파일 존재, **재수행 0건**
- [x] 배타 작성권 — `output/260831/260831_01_*_HI.md` 2건 신규 생성(기존 파일 덮어쓰기 0건),
      `verify_log.tsv` append 전용(기존 4행 불변, +4행), 본 WIP 단독 소유
- [x] 충돌 writer 부재 — 동시간대 `type-proposer` 병렬 인스턴스 없음
- [x] 검증 명령 재실행 — verify_log 8행 전건 8열 유지(아래 명령), 합답 선지 distinct=1 재확인

**차단 조건 처리**: INT-1(pNN 0건)·INT-5(범위 가드 대조원 부재)는 **해소되지 않았다**.
두 조건 모두 산출물 머리말에 ⛔로 명시했고, 전 문항을 `PROVISIONAL(page-cite blocked)`로 표시했으며
**커버리지를 100%로 보고하지 않았다**. 🚧 미표기는 "범위 내"가 아니라 "대조 불가"임을 명문화했다.

**신규 발견(슬라이스 6 고유)**:
- INT-HI-1/2/3 전사본 결함 3건 (번호 소실·서술형2 파편화·배점 표식 선언 34 vs 실측 38) — 수정하지 않고 flag만
- ⭐ **정답지가 존재하는데 미추출**: `EXTRACTION_LOG.md` A11행
  `2025_2학기_1학년_중간/2학기 중간고사 정답 - 1학년.pdf`(7과목 통합, 상태 `미착수`).
  `meta.yml answer_key: null`은 자료 부재가 아니라 **추출 미수행** 때문이다 → **6과목 공통 이익**,
  다음 REFINE 슬라이스로 A11 추출 제안(OQ-HI-2)

## 검증 명령 (슬라이스 6 재현)
```powershell
# 산출물 존재
Get-ChildItem C:\dev\study\output\260831\260831_01_*_HI.md
# verify_log 열 무결성 (기대: 8행 전건 cols=8, 하위 4행 actor=type-proposer)
(Get-Content C:\dev\study\corpus\EX-history-20252M\verify_log.tsv -Encoding UTF8 |
  Where-Object {$_.Trim() -ne ""}) | ForEach-Object { ($_ -split "`t").Count }
# CP-HI-1 재현 (기대: 9행, distinct=1)
(Get-Content C:\dev\study\corpus\EX-history-20252M\transcript.md -Encoding UTF8 |
  Where-Object {$_ -match '^① ㄱ'}) | Sort-Object -Unique
# INT-1 재현 (기대: pNN.png 0건)
Get-ChildItem C:\dev\study\corpus\_images\EX-history-20252M -Recurse -File -Filter "p*.png"
```

## 재개 감사 로그 (260831, 슬라이스 6 재호출 수신분) — append-only

메인 루프가 `260831_04_slice6_resume_briefing.md` 규격의 슬라이스 6 재개 회람문을 다시 보냈다.
**resume audit 결과 슬라이스 6은 이미 `done`이므로 재수행하지 않았다**(공통 실행 규격 ② 재개 규칙:
완료 슬라이스 재수행 금지). 대신 산출물 무결성만 재확인했다.

| 항목 | 기대 | 실측 | 판정 |
|------|------|------|------|
| `output/260831/260831_01_type_analysis_HI.md` | 존재 | 43,881 B | ✅ |
| `output/260831/260831_01_catalog_update_HI.md` | 존재 | 38,777 B | ✅ |
| `verify_log.tsv` 열 무결성 | 8행 전건 8열 | 8행 전건 8열 | ✅ |
| INT-1 재현 (`_images/EX-history-20252M/p*.png`) | 0건 | 0건 (`BIN*.bmp`만) | ✅ 차단 유지 |
| 서술형2 배점 근거 | 전사본 실독 | L303 `[12 점 ]` 축자 존재 | ✅ **역산 아님** |

### ⭐ 신규 실측 — `260831_10_proposer_fix_request.md`(N1) 수치 반증

N1은 CP-SM2-1을 「(강) 총점 6/6 = 100.0 · (중) 60:40 = **4/6**(수학2·국어·과학·사회)」로
재구조화하라고 지시한다. 원칙 9-c(정본 본문 수치는 실측 대조분만)에 따라 **6과목 전량을 직접
재계산**한 결과, **(강)은 성립하나 (중)의 과목 구성이 틀렸다.**

| 과목 | 선택형 | 서답형 | 총점 | 선택:서답 |
|------|--------|--------|------|-----------|
| 국어 | 60.0 (29문항) | 40.0 (서술 3) | **100.0** | 60:40 ✅ |
| 통합과학 | 60.0 (23문항) | 40.0 (서답 6) | **100.0** | 60:40 ✅ |
| 통합사회 | 60.0 (20문항) | 40.0 (서술 5) | **100.0** | 60:40 ✅ |
| 영어 | 70.0 (27문항) | 30.0 (서답 5) | **100.0** | 70:30 |
| 한국사 | 40.0 (20문항) | 60.0 (단답 6 + 서술 3) | **100.0** | 40:60 |
| **수학2** | **0.0 (선택형 0문항)** | **100.0** (단답 60.0 + 서술 40.0) | **100.0** | **0:100** |

1. **수학2를 `60:40 ✓`로 센 것은 축 혼동이다.** 수학2에는 선택형이 **0문항**이고(CLAUDE.md
   페르소나 절 "수학은 1·2학기 기출·부교재 모두 서답형 100%"), 그 60:40은 **단답형:서술형**
   이라는 **다른 축**의 값이다(전사본 L10 `단답형(18)문항, 서술형(4)문항` · L18~20).
   선택형:서답형 축에서 수학2는 **0:100**이며 60:40의 사례가 아니라 **최대 이탈값**이다.
   → 따라서 (중)은 **4/6이 아니라 3/6**(국어·과학·사회)이고, 공교롭게도 CP-SM2-1은
   **자기 이름의 근거 과목이 자기 패턴에 속하지 않는다**.
2. **(강) 총점 100.0은 6/6 성립** — 실측으로 확인했다. 다만 N1의 `100.0`은 "비율"이 아니라
   "만점"이므로 `6/6 과목의 총점이 각각 100.0점`으로 표기해야 오독되지 않는다.
3. **국어 `60.4`는 전사본 헤더의 산술오류** — `EX-korean-20252M/transcript.md` L36이 배점
   29개를 나열하고 "합 60.4점"이라 적었으나, **그 나열값의 실제 합은 60.0**이다(29개 전량 재합산).
   같은 행의 "서술형 합 25점"도 L34·L37의 소문항(7+6+15+6+6)과 맞지 않아 **실측 40**이다.
   → `_HI.md` L393과 `_EN`·`_SM2`의 `국어 60.4:40` 인용은 **전부 `60.0:40.0`으로 정정 필요**.

**조치**: N1을 **지시받은 문안 그대로 반영하지 않았다.** 지시 문안을 그대로 쓰면 실측과
어긋나는 수치를 내 제안서 본문에 넣게 되어 원칙 9-c 및 절대규칙 2를 위반한다. 또한 정정 범위가
`_SM2` 단독이 아니라 `_SM2`·`_EN`·`_HI` 3개 문서에 동시에 걸치므로(국어 60.4 인용) N1의
write surface(`_SM2` 단독)를 넘는다. **결정요청 DQ-N1-R로 상신한다** — 원칙 12-a에 따라
수용기준·판정문안의 타당성은 실행 레인이 단독으로 고칠 사안이 아니다.

## NEXT
**type-proposer 작업 종료 (6/6 슬라이스 done).** 이 WIP는 더 이상 재개 대상이 아니다 — 정리는 사용자만 한다.

**⛔ 선결**: `DQ-N1-R` — CP-SM2-1 재구조화 문안을 위 실측표로 확정한 뒤에야 `_SM2`·`_EN`·`_HI`
3개 문서를 **한 번에** 정정한다. 문서별 개별 수정은 과목 구성이 문서마다 달라지는 불일치를 만든다.

**메인 루프 인계 사항**:
1. 3단계 검토 루프(REV_GUIDE §3-b) 개시 — 대상 12개 파일(`output/260831/260831_01_{type_analysis,catalog_update}_{KO,SM2,EN,SC,SS,HI}.md`)
2. ⛔ **판정 묶음 필수**: **DQ-SS-1 + DQ-HI-1**을 하나의 판정 단위로 — 접두어 `F`의 신규 번호 정책은
   두 과목에 동시에 걸린다(원칙 9-a "두 정책 공존 = 결함")
3. ⛔ **DQ-SC-1**(통합과학 ID 정책 공백)도 같은 성격 — 신규 ID 정책 3건을 함께 판정할 것
4. 6과목 공통 차단 조건 2건(INT-1 렌더 부재 · INT-5 범위 가드 대조원 부재)은 **판정 대상이지
   type-proposer가 해소할 수 있는 것이 아니다**
5. 승격 후보 정리: **CP-KO-1** 4과목 관측(국어·과학·사회·한국사) · **CP-SS-3/CP-HI-3** 2과목 ·
   **CP-KO-3/CP-EN-1** 2과목 지지 + 2과목 반례 · **CP-SM2-1** 반례 2과목(영어 70:30 · 한국사 40:60) → 문안 재작성 필요

**이전 NEXT(달성됨)**: 13:00 리셋 후 슬라이스 6 단독 재호출, 슬라이스 1~5 재수행 금지 — **준수**.

**즉시 실행 명령어**:
```bash
# 슬라이스 6 회람문 파일명
$briefing = "output/260831/260831_04_slice6_resume_briefing.md"

# type-proposer 호출 (회람문 붙여넣기)
# 입력: corpus/EX-history-20252M/
# 출력: output/260831/260831_01_type_analysis_HI.md, 260831_01_catalog_update_HI.md

# 완료 직후: WIP 행 기록
# | 6 | 한국사(F) | EX-history-20252M | done | [경로] | notes |
```

**상태 변경**:
- status: on-hold → (13:00 후) ready-to-resume
- blocked_since: 260831 11:38 → (13:00 후) cleared
- NEXT: slice 6 호출 완료 → rev-writer 호출로 전환
