# TYPE_CATALOG — 문제 유형 카탈로그 (인덱스)

> 260714 재편: 기출 자료(상산고 2024·2025·2026 1학년 1학기)가 확보되어
> 과목별 카탈로그 체제로 전환. **정본은 [`catalog/`](catalog/) 폴더의 과목별 파일이다.**
> 형식·운영 규칙은 [`catalog/_README.md`](catalog/_README.md) 참조.

**세 축으로 문제를 준비한다:**
- **내용 축(무엇을)** — 아래 과목별 카탈로그.
- **형식·인지 축(어떻게 묻는가)** — [catalog/TYPE_MASTER.md](catalog/TYPE_MASTER.md) ⭐ *단원 독립.*
- **난이도 축(어느 수준으로)** — [catalog/DIFFICULTY_RUBRIC.md](catalog/DIFFICULTY_RUBRIC.md) ⭐ *목표 배점→특징 레시피+자기검증.*

| 과목 | 정본 파일 | 상태 |
|------|----------|------|
| **출제 유형 마스터(단원 독립)** | [catalog/TYPE_MASTER.md](catalog/TYPE_MASTER.md) | ✅ ⭐ |
| 공통 출제 문법 | [catalog/COMMON_TYPES.md](catalog/COMMON_TYPES.md) | ✅ |
| 통합과학1 | [catalog/science.md](catalog/science.md) | ✅ (24·25·26 전 6회) |
| 공통수학1 | [catalog/math1.md](catalog/math1.md) | ✅ (26 정밀) |
| **공통수학2 (2학기)** | [catalog/math2.md](catalog/math2.md) | ✅ (26 부교재 93문항 / SM2-01~33) |
| 공통영어1 | [catalog/english.md](catalog/english.md) | ✅ (24·25) |
| 통합사회1 | [catalog/social.md](catalog/social.md) | ✅ (24·25) |
| 한국사1 | [catalog/history.md](catalog/history.md) | ✅ (24·25) |
| 공통국어1 | [catalog/korean.md](catalog/korean.md) | ✅ (24·25) |

- **특정 회차 시험 유형 예측(중간/기말 대비)**: [`FORECAST_GUIDE.md`](FORECAST_GUIDE.md) ⭐
  — 기출(1차)과 부교재(2차)를 **합쳐** 회차별 유형 **A~E 등급**을 산정하는 절차.
  회차 범위 확정, 적중률 3지표(반영률·커버율·**사각지대**), 사후 채점 루프를 담는다.
- **생성 실전 운영(파이프라인·모델·저작권·검증)**: [catalog/AUTHORING_GUIDE.md](catalog/AUTHORING_GUIDE.md) ⭐
- **범위 가드(교육과정 대조)**: [`curriculum_2022.md`](curriculum_2022.md) — 공통수학2의 외분 삭제·
  임의 직선 대칭 초과 출제 등 **문제 생성 전 반드시 확인**
- 원본 자료 처리 현황: [`EXTRACTION_LOG.md`](EXTRACTION_LOG.md) (중복 추출 방지 정본)
- 학생(26_1_1) 오답·취약점 분석: [`student/`](student/) 폴더

## 구(舊) 시연 유형의 이관 기록 (append-only 원칙)

초기 시연 유형 M-01~M-04(역학적 시스템, 260713 등록)는 삭제하지 않고
[catalog/science.md](catalog/science.md)의 "시연 유형(기출 미확인)" 절로 이관했다.
기출 분석에서 동일 유형이 확인되면 해당 파일에서 상태를 `검증`으로 올린다.

## 동반 갱신 목록 (CLAUDE.md 원칙 10)
이 문서를 개정하면 **같은 작업에서** 아래를 함께 점검한다. 한쪽만 고치면
"규정은 있는데 아무도 안 지키는" 구멍이 생긴다.

- `CLAUDE.md` 원칙 1(정본 선언) · `AGENTS.md` · `analysis/FORECAST_GUIDE.md` · `analysis/catalog/_README.md` · `tools/build_catalog_index.py`(index.tsv 재생성) · `docs/PROMPT_math2.md` · `README.md`

목록 자체의 존재는 `tools/check_assurance_contract.py`가 검사한다.
근거: 260828 시스템 감사 S3 — 원칙 10이 8개 정본 중 1개에만 구현돼 있었다.
