# student/ — 학생 데이터 계층 규격 (_README)

> 이 폴더에는 두 종류가 산다. **①원장(TSV)** — 사실의 유일한 저장소(ATTEMPT_LOG·MASTERY·WEAK_LEDGER,
> 스키마는 [`../../docs/DATA_STANDARD.md`](../../docs/DATA_STANDARD.md) §5). **②서술 문서(MD)** — 아래 규격을 따르는
> 사람용 분석 문서(ANL 클래스). 수치가 둘 사이에 어긋나면 **원장이 이긴다**(3층 계획 D3·D8).

## 1. 파일명 (`YYMMDD_NN_` 규칙 적용 — PRD output/260825/260825_01 §5)

| 하위 클래스 | 패턴 | 예 |
|-------------|------|-----|
| 과목 오답분석 | `<YYMMDD>_<subject_code>_wrong_analysis.md` | `261010_math2_wrong_analysis.md` |
| 종합 보고서(과목 횡단) | `<YYMMDD>_cross_summary.md` | `260721_cross_summary.md` |
| 코칭 메모 | `<YYMMDD>_coaching_note.md` | `260721_coaching_note.md` |

- 기존 무날짜 파일명(`wrong_analysis_science.md` 등)은 **레거시 유지** — 외부 인용 15곳 초과라 개명 비용 > 편익(PRD A10 보류).
  신규 작성분부터 본 규격을 쓴다.

## 2. 과목 오답분석 필수 구성 (A15 규격)

```markdown
---
title: "<과목> 오답 분석 — <회차코드>"
created: <YYYY-MM-DD>
author: <작성 주체>
source: "<세트ID 또는 코퍼스ID 나열>"   # 근거 자료 — 조인 가능한 ID만
status: 초안 | 확정
---

# <과목> 오답 분석 — <회차>

## 0. 총평            한 문장. 수식어 금지, 관찰만
## 1. 교차 집계표      유형ID × Tier × DF × mark_code(correct/wrong/blank/unsure)
                      — 원장(ATTEMPT_LOG)에서 집계. 원장 없는 과거 자료는 [추정] 명시 + 신뢰도(상/중/하)
## 2. 취약 축          축 이름(함정코드 E·난이도 DF 연결) + 근거 유형ID 목록
                      + WEAK_LEDGER wk_id 매핑(있으면)
## 3. 처방            축마다: wrong(X)→사다리 T2→T3→T4 / blank(/)→제한시간 완주 훈련
## 4. 후속            다음 세트 출제에 반영할 항목 (item-writer 인용용)
## 이력
```

## 3. 작성 규칙

1. **신뢰도 표기 의무** — 스캔 판독 기반 추정은 `[추정]`+신뢰도를 반드시 남긴다(기존 관행: "신뢰도 중~하").
2. **정정 방식** — 과거 판정이 뒤집히면 본문을 고치고 `## 이력`에 남긴다. 삭제하지 않는다(종합진단_v2의 "이전 리포트 정정" 선례).
3. **수치 이중화 금지** — 원장으로 재현 가능한 집계를 MD에 통째로 복사하지 않는다. 요약 행 + 원장 참조면 충분.
4. **생성 주체** — item-writer(학생 오답 도착 시). 확정(status: 확정)은 사용자(교사) 몫.
