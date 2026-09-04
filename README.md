# study — 상산고 고1 지필평가 문항 출제 시스템

> 3년치 기출·부교재에서 **문제 유형**을 추출·누적하고, 그 유형으로 **변형 문제**를 만들며,
> 학생 **오답**을 분석해 취약점 보강 문제를 생성한다.
> 운영 지침(페르소나·핵심 원칙·작업 흐름)은 [CLAUDE.md](CLAUDE.md). 이 README는 **데이터·문서의 뼈대 안내서**다.

## 30초 폴더 지도

| 경로 | 무엇이 사는가 | 규칙·정본 문서 |
|------|--------------|----------------|
| `origin_data/` | 도착 원본 자료. 폴더명 = 코퍼스ID(`EX-`기출 ·`NY-`내신집 ·`SUP-`부교재 ·`PA-`수행 ·`CU-`교육과정) + `_inbox/`(신규 도착 대기) + `_archive/`(격리) | [docs/DATA_STANDARD.md](docs/DATA_STANDARD.md) §1.3 |
| `corpus/` | **코퍼스 데이터 하우스** — 유닛 구조는 바로 아래 해부도(원본 생성 답지 `generated_answer.md` 포함, DOC_LOCATION §3-1), 구조 안내는 `corpus/_README.md`, 등록 원장은 `HARVEST_LOG.tsv` | [docs/DATA_STANDARD.md](docs/DATA_STANDARD.md) §5.7·§5.7-A |
| `extracted/` | **레거시 동결**(구 정제 창고). 신규 유입 금지 | [extracted/README.md](extracted/README.md) |
| `raw/` | 보조 증거(2026 공식 정답지 스캔 4건) | [raw/README.md](raw/README.md) |
| `analysis/catalog/` | **유형 카탈로그 = 출제의 정본** + 마스터(A~F 조합 엔진) + 난이도 루브릭(Tier·DF) + 코드 등록부 | [analysis/TYPE_CATALOG.md](analysis/TYPE_CATALOG.md), [catalog/CODE_REGISTRY.md](analysis/catalog/CODE_REGISTRY.md) |
| `analysis/student/` | 학생 오답분석 서술 문서(ANL) | [analysis/student/_README.md](analysis/student/_README.md) |
| `analysis/forecast/` | 회차 출제 유형 예측 보고서 | [analysis/FORECAST_GUIDE.md](analysis/FORECAST_GUIDE.md) |
| `analysis/rev/` | 검토서(정본·시스템 대상). 회차 산출물 대상은 `output/<YYMMDD>/rev/` | [analysis/REV_GUIDE.md](analysis/REV_GUIDE.md) |
| `output/<YYMMDD>/` | 회차 산출물: 문제 세트·계획서·대장. 파일명 `YYMMDD_NN_<영문snake>.md` | DATA_STANDARD §2 |
| `docs/` | 데이터 스키마(DATA_STANDARD)·문제지 양식(QUIZ_STANDARD)·과목 프롬프트 | 각 파일 |
| `student/` *(예정)* | 학생 판단 원장 TSV(ATTEMPT_LOG·MASTERY·WEAK_LEDGER) | 미착수 — output/260825/plan_3layer_architecture.md P1~P3 |
| `tools/` | 변환 스크립트(hwp2md·md2quiz·build_web) | (문서화 예정) |
| `web/` | 문항 웹 뷰어(parser·app) | (문서화 예정) |
| `.claude/agents/` | **Claude Code role definitions ×11**. Opus-only external roles: `type-proposer`, `rev-auditor`, `rev-arbiter`, `solve-back-verifier`, `forecast-writer`, `forecast-arbiter`. Codex/OMX performs every non-Opus role; see `AGENTS.md`. | CLAUDE.md workflow table, analysis/REV_GUIDE.md §3-b |

## 파일 나침반 — 각 파일의 역할 (폴더 지도의 파일 버전)

### 루트
| 파일 | 역할 |
|------|------|
| `CLAUDE.md` | **운영 헌법** — 페르소나·핵심 원칙 8개·작업 흐름표. 모든 세션이 먼저 읽음 |
| `README.md` | **나침반(이 문서)** — 폴더·파일 지도와 코드 체계 안내 |

### docs/ — 형식 표준
| 파일 | 역할 |
|------|------|
| `DATA_STANDARD.md` | **데이터 스키마 총규격** — 모든 ID·enum 코드표·TSV 원장 스키마·meta.yml·파일명 규칙 |
| `QUIZ_STANDARD.md` | 문제지 입력 양식(사용자가 문제를 넣는 틀) |
| `PROMPT_math2.md` | 공통수학2 전용 출제 프롬프트(과목 맥락 주입용) |

### analysis/ — 운영 정본
| 파일 | 역할 |
|------|------|
| `TYPE_CATALOG.md` | 유형 체계 **진입점** — 세 축 설명 + 카탈로그 색인. 여기서 시작 |
| `FORECAST_GUIDE.md` | 회차 예측 절차 — 범위 확정→유형 A~E 등급→사각지대→사후 채점 |
| `curriculum_2022.md` | **범위 가드** — 2022 개정 교육과정 대조(범위 밖 출제 차단) |
| `EXTRACTION_LOG.md` | 자료 등록 원장 — 무슨 자료를 이미 뽑았는가(중복 추출 방지) |
| `REV_GUIDE.md` / `REV_LOG.md` | 검토서 작성 규격 / 검토 반영 이력(append-only) |
| `DOC_LOCATION.md` | 어떤 문서가 어느 폴더에 살아야 하는가 |

### analysis/catalog/ — 출제의 두뇌
| 파일 | 역할 |
|------|------|
| `_README.md` | 항목 형식 기준(템플릿의 수정 기준점) |
| `CODE_REGISTRY.md` | **ID 명칭 등록부** — 접두어 총람출·F충돌 판정·신규 부여 규칙 |
| `TYPE_MASTER.md` | **조합 엔진** — 자극A×발문B×인지C×선지D×함정E×난이도F. 단원 무관 재사용 |
| `DIFFICULTY_RUBRIC.md` | 목표 배점→Tier(T1~4) 레시피 + 활성 특징(DF1~9) + 자기검증 |
| `COMMON_TYPES.md` | 전 과목 관행(C-00~09: 합답형·배점 경향 등) |
| `science/math1/math2/english/english_passage_level/social/history/korean .md` | 과목별 내용 유형 DB(유형ID 항목 나열) — 파일명 = subject_code |

### 그 외
| 파일 | 역할 |
|------|------|
| `corpus/HARVEST_LOG.tsv` | 코퍼스 수확 원장 — 신규 유형·빈도·약점 근거를 유닛 단위로 기록 |
| `corpus/_README.md` | corpus 유닛 구조·검증 사료 3중 축 안내 (해부도 본가) |
| `extracted/INDEX.md` | 구(舊) 자료 색인(레거시 동결 구역의 현위치 안내) |
| `analysis/student/_README.md` | 오답분석 문서(ANL) 작성 규격 |
| `analysis/forecast/README.md` | 예측 보고서 파일명·저장 규칙 |
| `output/260825/260825_01_artifact_management_prd.md` | 산출물 관리 표준 본체(PRD) + 실행 체크박스 대장 |
| `output/260825/260825_02_origin_migration_ledger.md` | 원본 자료 이동 실측 대장 |
| `output/260825/plan_3layer_architecture.md` | 3층 아키텍처 계획(P1~P3 학생 원장 미착수) |
| `tools/*.py`, `web/*` | hwp2md·md2quiz 변환기 / 문항 웹 뷰어 (문서화 예정) |

### 상황별 최단 경로
- **문제를 만들 때**: TYPE_CATALOG → 과목 카탈로그+마스터+루브릭 → QUIZ_STANDARD 양식 → solve-back 게이트(필수) → practice: tier-1 / exam: 3단계 루프(REV_GUIDE §3-b)
- **새 자료가 도착했을 때**: EXTRACTION_LOG 중복 확인 → origin_data/_inbox → 정제(type-extractor) → 제안서(type-proposer) → 검토 루프 → arbiter → 정본 반영
- **검토 의견이 있을 때**: REV_GUIDE three-tier loop — t1 보고 → t2 교차 검증 → t3 결정 → 승인분만 작성 주체가 흔적과 함께 반영
- **회차 예측이 필요할 때**: FORECAST_GUIDE → `forecast-writer` 작성(A~E·사각지대) → 범위 확실도별 차등 검토(확정=t1 `forecast-reviewer` / 미확정=t1⇄t2+분쟁시 `forecast-arbiter`) → 등급표를 세트 배분에 인계



## corpus 유닛 해부도 (자세히: corpus/_README.md)

```
origin_data/<코퍼스ID>/               원본 PDF (영구 보존, 무변형)
corpus/<코퍼스ID>/                    같은 ID의 작업 정제본
  ├─ meta.yml                        등급·회차·렌더 파라미터·신뢰도 (+ answer_key → generated_answer.md)
  ├─ transcript.md                   문항 전사본 (type-extractor 산출)
  ├─ generated_answer.md             원본 생성 답지 1:1 풀이 (DOC_LOCATION §3-1)
  └─ verify_log.tsv                  단계별 검증 원장 — 사유+근거 페이지 인용, append-only
corpus/_images/<코퍼스ID>/pNN.png     판독 이미지 (PDF에서 재생성 가능 — git 미추적)
```

**검증 사료 3중 축**: 원본 → 판독 이미지 → verify_log.tsv. 어떤 주장("유형X=문항12번")이든 이 축으로 소급 검증한다.

## 데이터 흐름

```
도착 origin_data/_inbox → 등록(코퍼스ID 부여) → 정제 corpus/<ID>/(transcript·meta.yml·_images·verify_log)  [Codex/OMX · type-extractor]
  → 제안 output/<YYMMDD>/(유형 배정·카탈로그 갱신안·공통패턴 후보)                                          [Claude Code · type-proposer]
  → 검토 루프 t1 rev-writer ⇄ t2 rev-auditor via _index.md (≤5라운드) → arbiter 승인 → 메인 루프가 정본 반영 [Codex/OMX ⇄ external Claude Code Opus]
  → 예측 forecast/ → 출제 output/(item-writer, intended_use 기록)
  → solve-back 게이트(전 세트 필수) → practice: tier-1 경량 | exam: 전체 루프 → 투입 허가(arbiter 승인+사용자 확인)
  → 응시·채점 → 오답분석 analysis/student/ → 약점 원장 WK-nn(student/, 미착수) → 취약 축 재출제
```

## 회차 예측 흐름 (전용 체인 — 260825)

```
scope 확정(공지 > 과거 분할 패턴, 추정시 ⚠️ 표기) → 유형 A~E 등급·사각지대(E)
  → 보고서 analysis/forecast/<YYMMDD>_<회차코드>-<subject_code>.md        [Claude Code · forecast-writer]
  → 검토 차등: 확정 = t1 forecast-reviewer 1회 | ⚠️미확정 = t1⇄t2(forecast-auditor) ≤5R → 분쟁시 forecast-arbiter
  → 등급표를 item-writer 세트 배분에 인계 → 사후 채점은 같은 파일 말미 append-only (FORECAST_GUIDE §6)
```

## 코드 체계 한눈표 (상세: catalog/CODE_REGISTRY.md)

| 종류 | 형식 | 예 |
|------|------|-----|
| 코퍼스ID | `<자료성격>-<subject_code>-<연도><학기><M/F/Pnn>` | `EX-math2-20262M`, `SUP-math2-2026` |
| 회차코드 | `<YYYY>-<학기><M/F/Pnn>` | `2026-2M` |
| 세트ID | `SET-<subject>-<회차>-<NNN>` | `SET-math2-2026-2M-001` |
| 유형ID | `<접두어>-<번호>` (접두어는 과목·영역별로 등록됨) | `SM2-24`, `BI-02`, `한국사:F-03`(F는 스코프 필수) |
| 인지·함정·자극… | 마스터 A~F축 코드 | `C9`, `E5`, `A10` |
| 난이도 | Tier T1~T4 + 활성 특징 DF1~DF9 | `T3 / DF1·DF4` |
| 약점 | `WK-nn` (원장 표준) | `WK-01` |

## 운영 규칙 요약 (전문은 CLAUDE.md)

- **append-only**: 카테고리 항목·로그 삭제 금지, 폐기는 상태 변경.
- **검증 사료 3중 축**: 원본(origin_data) → 판독 이미지(corpus/_images) → verify_log.tsv(사유·근거 페이지 인용).
- **공통유형 승격**: 과목 카탈로그 반영은 매번, 공통유형 C-nn 신설은 교사 출제 패턴이 2과목↑/2회차↑ 반복될 때만.
- **파일명**: 모든 산출 문서 `YYMMDD_NN_<영문snake>.md`. 정본(living doc)은 한글명 유지.
- **재현성 D/G**: 결정론 계층(폴더·파일명·TSV·meta)=100% 재현, LLM 생성 내용=형식 재현+검증 계약(PRD §6.1).
- **검토 분리(원칙 8)**: 남이 쓴 문서는 직접 고치지 않는다 — 검토서+체크박스 승인 후 반영.
- **Three-tier review**: t1 `rev-writer` ⇄ t2 `rev-auditor` rounds (≤5, duplicate-dispute escalation) → t3 `rev-arbiter` binding ruling. Closure needs user declaration or arbiter approval.
- **Language policy (260825)**: md content is English-first; Korean only in legacy text, proper nouns, and existing filenames.

## 현재 상태 (260825)

- ✅ 완료: 산출물 관리 표준([PRD](output/260825/260825_01_artifact_management_prd.md))·원본 마이그레이션·코드 등록부·데이터 표준 v1.1
- 🚧 진행 전: 학생 원장 TSV 계층(3층 계획 P1~P3) · 검토서 6건 판정(`analysis/rev/260825_01~06`)
