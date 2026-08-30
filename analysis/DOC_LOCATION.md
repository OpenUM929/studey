# 문서위치 표준 — 자료·정본·산출물·검토 저장 규칙 (260825 확립)

> **배경**: 카탈로그 검토서가 `output/<회차>/rev/`에 들어가는 등 산출물 폴더와 정본 검토가 뒤섞인 사건(260825)을 계기로,
> 모든 문서의 **생성 위치를 사전에 고정**하는 표준이다. 새 문서를 만들기 전 이 표에서 자기 위치를 찾는다.
> 규칙 충돌 시 본 문서 > 관행. 본 문서 개정은 체크박스 승인 절차를 거친다.

## 1. 5계층 분류

| 계층 | 위치 | 담는 것 | 성격 |
|------|------|---------|------|
| **자료** | `origin_data/` · `raw/` · `extracted/` | 원본 PDF/HWP와 그 변환물 | 읽기 전용에 가까움. 분석·출제의 증거 |
| **정본** | `analysis/` | 카탈로그·지침·로그 등 **반복 참조되는 운영 문서** | append-only 원칙 적용. 수정은 승인 후 |
| **산출물** | `output/<YYMMDD>/` | 납품물 — 문제 세트·모의고사 등 **회차 단위 생성물** | 세션마다 새로 만들어지는 결과물 |
| **검토** | 아래 §2 — 산출물 검토와 정본 검토가 **갈라진다** | 검토서(rev) | 수정 불간섭 원칙(원칙 8)의 수송 통로 |
| **작업 상태(WIP)** | `analysis/wip/<actor>_<YYMMDD>_<task>.md` | 서브에이전트 슬라이스 체크포인트 — 타임아웃·컨텍스트 한계 후 재개용 (CLAUDE.md 「서브에이전트 공통 실행 규격」 ②) | 휘발성·배타 소유. done 후 삭제는 사용자만 |

## 2. 검토서(rev) 이원화 — 핵심 규칙

| 검토 대상 | 검토서 위치 | 예시 |
|-----------|------------|------|
| **회차 산출물** (`output/<YYMMDD>/*.md` 문제집) | `output/<YYMMDD>/rev/` | 모의40 문제집 오류 지적(260822 선례) |
| **그 외 전부** — 카탈로그(`analysis/catalog/*`)·지침(`*_지침.md`)·시스템(`web/`·`tools/`)·태그 배관·표준 문서 | `analysis/rev/` | 카탈로그 검산(260825_02~05), 웹 뷰어 결함(260825_01) |

- **판별 한 줄**: *검토 대상 파일이 `output/` 안에 있으면 그 회차 폴더의 rev/, 밖이면 무조건 `analysis/rev/`.*
- 두 홈 모두 동일 규격 적용: [`REV_GUIDE.md`](REV_GUIDE.md) 구조(frontmatter→document→context→findings→questions→proposed_fixes→output_format→이력),
  파일명 `YYMMDD_NN_NAME.md`, **각 홈마다 `HISTORY.md` 진입점**(정적 등록부)과
  **`_index.md` 핸드오프 대장**(라운드 상태 — REV_GUIDE §1 표준 양식, 260825 신설) 유지.
- 순번(NN)은 홈별로 독립 채번한다(output/260825/rev/의 01과 analysis/rev/의 01은 서로 무관).
- 회신(reply)도 같은 홈에 둔다.

## 3. 분석 보고서 위치

| 종류 | 위치 | 비고 |
|------|------|------|
| 회차 출제 유형 예측(A~E 등급표) | `analysis/forecast/` | [`FORECAST_GUIDE.md`](FORECAST_GUIDE.md) §5 규정 — 폴더 신설(260825) |
| 학생 오답·취약점 분석 | `analysis/student/` | 기존 관행 |
| 원본 처리·추출 기록 | `analysis/EXTRACTION_LOG.md` | append-only 정본 |
| 폴더·문서 구조 자체의 규칙 | `analysis/DOC_LOCATION.md` (이 파일) | 개정은 승인제 |

## 4. 명명·참조 규칙

- 검토서 파일명: `YYMMDD_NN_NAME.md` (NAME 영문 스네이크). 보고서도 같은 스타일 권장: `<YYMMDD>_<주제>.md`
- 문서 간 링크는 **이동 후에도 깨지지 않게** 상대경로 기준으로 쓰고, 정본에서 검토서를 인용할 때는
  REV_LOG 링크만 사용한다(직접 경로 하드코딩 금지 — 이동 대응 비용 최소화).
- 검토서 이동 시: 행 삭제 없이 REV_LOG에 **새 행으로 이동 기록**을 추가하고, 기존 행의 링크 href만 갱신한다.

## 5. 마이그레이션 기록 (append-only)

| 날짜 | 대상 | 조치 |
|------|------|------|
| 260825 | `output/260825/rev/260825_01_tag_pipeline_mismatch.md` (웹 시스템 검토) | → `analysis/rev/` 로 이동 |
| 260825 | `output/260825/rev/260825_02~05_catalog_*.md` (카탈로그 검토 4건) | → `analysis/rev/` 로 이동 |
| 260825 | `output/260825/rev/HISTORY.md` | `analysis/rev/HISTORY.md` 로 흡수 통합 후 원본 폴더 소멸 |
| 260825 | `output/260822/rev/*` (모의40 산출물 검토) | **이동하지 않음** — 대상이 output 산출물이라 현위치가 올바름 |

## 이력
- 260825 신설. 계기: 사용자 지적 — 카탈로그 검토서가 output 회차 폴더에 저장됨. 정본·시스템 검토의 홈으로
  `analysis/rev/` 확립, 산출물 검토(`output/<YYMMDD>/rev/`)와 이원화. Shrimp Task Manager MCP 등록으로
  향후 세션 태스크 보드 병행 예정(데이터: `.shrimp/`, gitignore 처리).

## 동반 갱신 목록 (CLAUDE.md 원칙 10)
이 문서를 개정하면 **같은 작업에서** 아래를 함께 점검한다. 한쪽만 고치면
"규정은 있는데 아무도 안 지키는" 구멍이 생긴다.

- `analysis/REV_GUIDE.md` §1(위치·명명) · `.claude/agents/rev-writer.md` · `rev-auditor.md` · `forecast-reviewer.md` · `CLAUDE.md` 원칙 8

목록 자체의 존재는 `tools/check_assurance_contract.py`가 검사한다.
근거: 260828 시스템 감사 S3 — 원칙 10이 8개 정본 중 1개에만 구현돼 있었다.
