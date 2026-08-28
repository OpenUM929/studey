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
origin_data/<코퍼스ID>/              ← 원본 PDF 등 (영구 보존, 무변형)
corpus/<코퍼스ID>/                   ← 같은 ID의 작업 정제본
  ├─ meta.yml                       ← 자료 등급·회차·렌더 파라미터·신뢰도 (DATA_STANDARD §5.7)
  ├─ transcript.md                  ← 문항 전사본 (type-extractor 산출 — 원문 계수 절대 보존)
  └─ verify_log.tsv                 ← 단계별 검증 원장 (DATA_STANDARD §5.7-A)
corpus/_images/<코퍼스ID>/pNN.png    ← 판독용 페이지 렌더 (meta.yml 파라미터로 재생성 가능 — git 미추적)
```

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
