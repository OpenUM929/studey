# corpus/ — 코퍼스 데이터 하우스 (유닛 구조 안내, _README)

> **역할**: 원본 자료에서 파생된 모든 작업물의 표준 보관소. 폴더명 = 코퍼스ID
> ([docs/DATA_STANDARD.md](../docs/DATA_STANDARD.md) §1.3). **등록 목록 조회는 [`HARVEST_LOG.tsv`](HARVEST_LOG.tsv)** —
> 전 유닛의 신규 유형·빈도 갱신·약점 근거가 한 행씩 누적되는 단일 원장이다.

> **디렉터리 불변식(260826)**: 폴더명 ≠ 코퍼스ID인 유닛은 규격 위반이다 —
> `Get-ChildItem corpus -Directory | Where-Object { $_.Name -ne '_images' -and $_.Name -notmatch '^[A-Z]{2,4}-[a-z0-9]{2,8}-\d{4}([12][MF]|P\d{2})?$' }`
> 가 0행을 출력해야 한다(`_images`는 예약 디렉터리 제외). 발단: 260825 골격 생성 시 같은 PRD 본문의
> 구경로 지시(`SUP-M2-2026`)가 갱신 없이 그대로 실행돼 폴더명만 v1로 남았다(meta.yml·원장은 v2) —
> 부분 갱신 사고로 CLAUDE.md 원칙 10의 실증 사례. 시정: 260826 `SUP-math2-2026`으로 rename(사용자 승인).

## 유닛 해부도 (origin_data와 1:1)

```
origin_data/<코퍼스ID>/              ← 원본 (PDF/HWP/DOC 등 영구 보존, 무변형 — HWP/DOC는 PDF화본을 함께 보관, §1차 정제 참조)
corpus/<코퍼스ID>/                   ← 같은 ID의 작업 정제본 (1차 정제 게이트 통과 후에만 분류 진입)
  ├─ meta.yml                       ← 자료 등급·회차·렌더 파라미터·신뢰도 (DATA_STANDARD §5.7) — answer_key가 generated_answer.md를 가리킴
  ├─ transcript.md                  ← 문항 전사본 (type-extractor 산출 — 원문 계수 절대 보존, 도표 문항은 _images 링크 포함)
  ├─ generated_answer.md            ← 원본 생성 답지 1:1 풀이 (DOC_LOCATION §3-1, DATA_STANDARD §1.5) — meta.yml:answer_key로 추적
  └─ verify_log.tsv                 ← 단계별 검증 원장 (DATA_STANDARD §5.7-A)
corpus/_images/<코퍼스ID>/pNN.png    ← 판독용 페이지 렌더 (meta.yml 파라미터로 재생성 가능 — git 미추적, HWP/DOC는 PDF화 후 렌더)
```

## 1차 정제 게이트 (260901 신설 — 원본 재열람 방지)

**원칙**: 어떤 분류·유형 배정·사실 검증도 **1차 정제물이 완성되기 전에는 시작하지 않는다**. 원본을 매번 뜯으면 데이터 소모·context 낭비가 반복되므로, 정제물을 정본으로 쓴다.

| 순서 | 입력 → 출력 | 도구·책임 | 산출물 |
|------|-------------|-----------|--------|
| 0 | HWP/DOC 등 비-PDF 원본 → **PDF화** | `tools/hwp2pdf` 등, `type-extractor` 준비 단계 | `origin_data/<ID>/`에 PDF화본 보관(원본과 병치, 무변형 원본 훼손 금지) — HWP 수식 유실 위험은 `verify_log.tsv`에 `unreadable`로 기록 |
| 1 | PDF → 페이지 이미지 | `PyMuPDF` `dpi≥130` (권장 160), `type-extractor` | `corpus/_images/<ID>/pNN.png` |
| 2 | 이미지 → 전사 | `type-extractor` (분류 판단 금지) | `corpus/<ID>/transcript.md` — 도표·그래프 문항은 `![](../_images/<ID>/pNN.png)` 이미지 링크 포함, 계수·좌표 byte-equal |
| 3 | 전사 검증 | `type-extractor` | `verify_log.tsv` transcribe 행 + `meta.yml: transcribed_at/render_dpi/render_tool/confidence` 채움 |

**게이트 조건**: `transcript.md` + `_images/pNN.png` + `verify_log.tsv` transcribe 행 + `meta.yml` 4필드가 모두 채워져야 **1차 분류(PROPOSE) 진입 가능** (`CLAUDE.md` 작업 흐름표 참조). 미충족 시 분류는 `▲ blocked`. 이후 분류·검토·생성은 **원본 PDF 재열람이 아니라 이 정제물**로 수행한다 — 원본은 3중 축 소급 증거로만 사용한다.
> **⚠️ 1차 정제 ≠ 1차 분류 (260901):** 정제는 **전사만**(분류 판단 금지 — 유형ID·변형축·함정 한 글자도 적지 않는다, 산출물은 `corpus/<ID>/`에만), 분류는 **정제물을 다시 읽어 한 문항씩 유형에 배정**하는 작업(산출물은 `output/<YYMMDD>/`에만). 카탈로그 `출제 빈도`를 옮겨 적는 것은 분류가 아니다.

## 검증 사료 3중 축 (260825 신설)

1. **원본 PDF**(`origin_data/`) — 최종 증거, 재판독의 기준점
2. **판독 이미지**(`_images/pNN.png`) — "이 판정이 맞는가"를 눈으로 다시 보는 중간 원화
3. **verify_log.tsv** — 판단의 **사유 + 근거(페이지·위치) 인용**, append-only

→ 어떤 주장("유형 X = 문항 12번")이든 이 3축으로 소급 검증 가능해야 한다.
→ 스키마 상세는 [docs/DATA_STANDARD.md](../docs/DATA_STANDARD.md) §5.7-A. 요약:
`date | step(transcribe·classify·merge·grade·promote) | target | decision | evidence(p07+하단좌측) | reason | confidence | actor`
[판독불가]도 반드시 행으로 남긴다(decision=`unreadable`).

## 이력
- 260826 — **P0-4 시정([OC 지시] 260826_03, 사용자 승인 (a))**: `SUP-M2-2026` →
  `SUP-math2-2026` 디렉터리 rename(원장·meta 무변경 — 이미 v2였음). 원인: 260825 골격
  생성 지시문(L448)이 같은 PRD의 개명 결정(A1)을 따라가지 못한 채 실행됨(부분 갱신).
  디렉터리 불변식+검증 명령을 본문에 명문화. 작성: 메인 루프.
- 260825 신설 — 사용자 지시("분석용 이미지 체계적 관리 + 단계별 사유·판단 근거 기록")에 따라 유닛 구조·검증 축 정의. 작성: 메인 루프.
