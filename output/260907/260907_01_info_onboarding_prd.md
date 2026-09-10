---
title: 정보 과목 온보딩 + Python 학습지 2종 정제·분류·출제 운영 PRD
created: 2026-09-07
author: main-loop
status: done
related: analysis/catalog/CODE_REGISTRY.md, docs/DATA_STANDARD.md, analysis/catalog/info.md, corpus/SUP-info-2026-01, corpus/SUP-info-2026-02
---

# 260907_01 — 정보 과목 온보딩 + Python 학습지 2종 처리 PRD

> 사용자 지시(260907): origin_data의 Python 학습지 2종을 표준 명칭으로 정리하고,
> 개념↔실습 매핑을 만들고, 중간고사 유형정리 문서에 실습 문제 유형을 추가하고,
> 개념 근거를 가진 신규 문제를 유형별로 만들고, 전체를 단순변형 감사한다.

## 0. 착수 전 확정 사항 (사용자 승인 260907)

| # | 쟁점 | 확정 | 근거 |
|---|------|------|------|
| D1 | 두 학습지의 코퍼스ID | `SUP` 재사용 + `-NN` 일련번호 슬롯 신설 → `SUP-info-2026-01`(개념 10p) · `SUP-info-2026-02`(실습 5p) | 사용자 선택. DATA_STANDARD §1.3 개정 동반 |
| D2 | 연도 | `2026` (2026학년도 2학기). 회차 자료가 아니므로 `exam_code: null`, 대비 회차는 2026-2M | 사용자 선택 |
| D3 | 유형정리 문서 | 정보 과목 카탈로그가 없으므로 **CODE_REGISTRY §6 온보딩 8항목을 이번 작업에서 실행**해 `analysis/catalog/info.md` 신설. 기존(중간고사) 유형은 `EX-info-20252M`에서, 추가 유형은 실습 학습지에서 | 사용자 선택 |

## 1. 데이터 명세 (실측)

| 항목 | SUP-info-2026-01 | SUP-info-2026-02 |
|------|------------------|------------------|
| 구 폴더명 | `origin_data/Python_2학기_1학년_개념` | `origin_data/Python_2학기_1학년_실습_문제` |
| 페이지 수 | 10 | 5 |
| 원본 파일명 | `4fce8096-7082-48d4-bc88-d2ddd161497c.pdf-00NN.png` | `1f06def2-bd07-4c44-aa44-93b291632fc2.pdf-00NN.png` |
| 픽셀 | 1239x1752 (전 페이지) | 1239x1752 (전 페이지) |
| 추정 dpi | 1239px / 8.27in(A4) = 149.8 → **150** | 동일 |
| p1 표제 (실열람) | 「문제해결과 프로그래밍」 / 반복문(for문) | 「정보 수업 학습지 / 1. 파이썬과 친해지기」 / 변수와 리스트 |
| 자료 등급 | 2차 (수업 학습지) | 2차 (수업 학습지) |

> **관측 주의**: 폴더 라벨과 실제 내용이 일치하지 않는다. "개념" 폴더도 빈칸 채우기 문항을
> 포함하고, "실습_문제" 폴더도 개념 설명을 포함한다. 라벨이 아니라 **전사된 문면**으로 판단한다.

## 2. 단계·게이트·수용기준

| S | 단계 | 주체 | 산출물 | 수용기준 (fail-closed) |
|---|------|------|--------|------------------------|
| S0 | 본 PRD + WIP 개설 | main-loop | 이 파일 · `analysis/wip/mainloop_260907_info_onboarding.md` | 두 파일 존재 |
| S1 | 명명 정책 선행 등록 | main-loop | DATA_STANDARD §1.3 개정 + CODE_REGISTRY 이력 | 개정된 정규식에 `SUP-info-2026-01`이 실제로 매치(파이썬 실행 출력 첨부) |
| S2 | 폴더·파일 개명 + 매핑표 | main-loop | `origin_data/SUP-info-2026-0N/pNN.png` · `corpus/_images/...` · 매핑표 | 디렉터리 불변식 검사 0행 · 개명 전후 파일 수/해시 동일 |
| S3 | 1차 정제 (전사만) | type-extractor | `corpus/SUP-info-2026-0N/{transcript.md,meta.yml,verify_log.tsv}` | 15/15 페이지 전사 · 분류 판단 0건 |
| S4 | 정보 과목 온보딩 8항목 | main-loop | CODE_REGISTRY §1·§3 · DATA_STANDARD §5.8 · catalog/info.md · curriculum_2022 정보 절 · build_catalog_index · md2quiz · index.tsv | `build_catalog_index.py --check` 경고 0줄 + exit 0 |
| S5 | 1차 분류 (기출) | type-proposer | `EX-info-20252M` 25문항 유형 배정 → info.md 초판 | 분모=원본 25, 산출 25 (원칙 11-a) |
| S6 | 1차 분류 (학습지) + 개념↔실습 매핑 | type-proposer | 실습 유형 추가 + 매핑표 | 기존 유형명·정의 중복 신설 0건 |
| S7 | 신규 문제 생성 | item-writer | `output/260907/260907_NN_info_*.md` | 문항마다 근거 개념 페이지 인용 |
| S8 | 맹목 풀이 | solve-back-verifier | 검증 보고 | 전 문항 통과 |
| S9 | 단순변형 감사 (요구사항 6) | item-quality-auditor | 감사·수정 내역 | 원문 나란히 대조 근거 첨부 |

## 3. 리스크

- **R1 범위 가드 부재** — `curriculum_2022.md`에 정보 절이 없다. S4에서 신설하되, 2022 개정
  「정보」성취기준을 이 환경에서 조회할 수 없으면 추측으로 채우지 않고 `blocked`로 남긴다
  (CODE_REGISTRY §6 단서). 그 경우 S7 산출물에 `scope_confirmed: false`를 유지한다.
- **R2 라벨-내용 불일치** — §1 관측 주의 참조.
- **R3 컨텍스트 소진** — 매 단계 종료 시 WIP에 체크포인트를 남기고, 산출물을 파일로 확정한 뒤
  다음 단계로 넘어간다. 세션이 끊기면 WIP의 `NEXT`부터 재개한다.

## 4. 검토 라벨

본 PRD는 `self-check(작성자)` 다 — `rev-writer`/`rev-auditor`를 실제로 호출하지 않았다.
CLAUDE.md 작업 흐름표 「라벨을 실제 배우와 일치시킨다」에 따라 그대로 적는다.
