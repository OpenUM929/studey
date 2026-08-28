---
title: "Decision request 260826_02 — Cycle-0 operations PRD gate"
created: 260826
author: main loop (writer=t1, auditor=t2 within session)
type: prd-gate review (CLAUDE.md 데이터 도착 게이트 — 신설 절차 첫 적용)
target: [output/260826/260826_01_operations_cycle_prd.md](../../output/260826/260826_01_operations_cycle_prd.md)
status: waiting:arbiter (Round-2 재제출 — Round-1 판정 revise-required BF1~BF9 반영 완료)
reply_surface: 기존 `analysis/rev/260826_02_ruling.md`에 "## Round 2 decision" 섹션 append (+ REV_LOG 행 1건)
---

# Decision Request — Cycle-0 PRD (신규 2학기 기출 전체 사이클 테스트)

## 1. Context

- 260826 09:19 신규 도착: `origin_data/*.zip` 4개 = **2024·2025 2학기 중간+기말 고사원안 원본**
  (기존 extracted는 전부 1학기 — INDEX.md §5 미확보 항목이 채워지는 자료).
- 사용자가 운영 사이클 개시를 지시하고, 그 실행 근거 문서로 본 PRD를 작성함.
- 동시에 CLAUDE.md 작업 흐름표에 **데이터 도착 게이트 행을 신설**(PRD 작성→CC 검토 라운드→승인 후 실행).
  이 요청은 그 게이트의 첫 회람이다.

## 2. t1 self-review (rev-writer pass) — findings & fixes applied

| ID | Finding | Severity | Action |
|---|---|---|---|
| F1 | §1 inventory totals wrong: claimed "27 HWP + 3 시험지 PDF + 6 정답 PDF"; actual zip census = **25 HWP + 시험지 PDF 1 + 정답 PDF 6 (=32 files)**. Same error leaked into S1 row ("PDF 4건") | factual | owner-fixed in place (§1·S1). No other occurrence remains (grep) |
| F2 | `IN` prefix availability unverified at draft time | procedural | CODE_REGISTRY §1 checked — `IN` unclaimed ⇒ claimable via §5 procedure |
| F3 | PRD §9 checkboxes did not explicitly cover the two standard-amendment items (IN/info) they depend on | completeness | folded into RQ-2 below instead of editing the checklist again |

## 3. t2 independent cross-check (auditor pass)

- Zip recount executed independently (`zipfile` namelist): files=8×4=32,
  hwp 5/6/7/7=**25**, pdf 3/2/1/1=**7** — matches the **corrected** PRD exactly.
- CLAUDE.md gate row integrity: table intact, legacy REFINE row references the gate
  ("데이터 도착 게이트(윗행) 통과 선행"), no-commit state preserved.
- PRD internal links resolve; sibling-doc references (DATA_STANDARD §5.8/§5.1,
  FORECAST_GUIDE, REV_GUIDE, plan_3layer) exist.
- Scope-decision record (§2 D1–D4) matches the user's four answers verbatim.
- Convergence reached in round 1 (≤5R limit unused).

## 4. Ruling requests

| RQ | Question |
|---|---|
| RQ-1 | PRD 전반 승인 여부 — S0~S9 단계 설계·게이트 수용기준·리스크 방어가 CLAUDE.md 원칙 및 각 정본(DATA_STANDARD/REV_GUIDE/FORECAST_GUIDE/CODE_REGISTRY)과 정합하는가. 수정요구가 있으면 항목별로 기술 |
| RQ-2 | 사전 승인(조건부 가능): 정보 과목 신설에 필요한 ① 유형ID 접두어 `IN` 선점(CODE_REGISTRY §1 등록+§5 절차 준용) ② DATA_STANDARD §5.8 subject_code 8번째 코드 `info` 추가. 두 개정안을 S4 반영분으로 미리 허가할 수 있는가 |
| RQ-3 | CLAUDE.md 게이트 행 문언 승인 — 특히 "t1⇄t2 자체검증 후 CC 회람", "승인된 PRD가 그 사이클의 정본", "미승인 상태로 데이터 가공 금지" 세 구절이 원칙 8(검토·수정 분리)과 충돌하지 않는가 |
| RQ-4 | math2 처리 논리 — SM2 카탈로그는 현재 전면 `검증(부교재)`인데, EX-math2-20252M/F 판독으로 유형별 승격(`검증`)을 S2 제안서에서 시도하는 것은 원칙 6(자료 등급)에 부합하는가. 부교재-only 유형이 기출에서 미출제로 확인되면 상태 유지+주석을 요청함 |
| RQ-5 | S9 원장 시뮬레이션의 오염 방지 설명(가짜 응답 TSV에 시뮬 명기)으로 충분한가, 추가 장치가 필요한가 |

### Amendment A (260826, same session — 판정 전 증보)

초기 패키징 이후 같은 세션에서 사용자 지시로 **런타임 프로토콜 2건**이 추가 제정됐다.
본 판정 요청에 편입한다(별도 패키징하지 않음 — D3 묶음 1회 원칙).

| 산출물 | 내용 |
|---|---|
| CLAUDE.md 「서브에이전트 공통 실행 규격」 | ① 회람 발신 의무(§6-b 연결) · **①-b 회람문 작성 태스크**(프롬프트 엔지니어 관점·품질 기준 5개·추측 금지·⚠️미확인 라벨링) · ② 슬라이스 체크포인트 정본 규격(WIP 배타 소유·NEXT 재개·사용자만 정리) |
| analysis/REV_GUIDE.md §6-b | Relay message spec 6필드 + **Authoring stance (mandatory)** + 수신측 반려권(위반 시 추측 실행 금지) |
| analysis/DOC_LOCATION.md §1 | 「작업 상태(WIP)」 제5계층 등록(`analysis/wip/`, 사용자 지시=승인 처리·이력 기록) |
| analysis/wip/_README.md | WIP 저장소 규칙판(배타 소유·재개·판정 인용 금지·삭제는 사용자만) |
| .claude/agents/*.md ×11 | 전원 `Runtime protocol — slice checkpointing` 섹션; 그중 CC 측 4종(type-proposer·rev-arbiter·forecast-writer·forecast-arbiter)만 회람 수신 조항 추가(REV_GUIDE §5 Actors 표 근거) |
| solve-back-verifier 예외 | "무파일" 절대 규칙에 자기 WIP 1개 예외를 명문화(장세트 중단 시 판정 유실 방지; 260824 #38 사례가 보인 리스크) |
| analysis/rev/_index.md | 본 게이트의 t1 행(F1 집계 오기 수정)·t2 행(zip 재집계 일치·R1 수렴) 추가, header submitted |

| RQ | Question |
|---|---|
| RQ-6 | 슬라이스 체크포인트 설계가 원칙 8·REV_GUIDE §5 단일 작성자 규칙과 충돌하지 않는가 — 특히 (a) solve-back-verifier '무파일' 규칙의 자기-WIP 예외 (b) "WIP는 판정·리포트 인용 금지" 규정으로 완성본만 증거 삼는 설계의 적절성 |
| RQ-7 | 회람 규격(§6-b+CLAUDE.md ①-b)이 판정 12류 인용 소소착오의 재발을 막으면서 CC 측 부담은 과도하지 않은가 — 특히 수신측 반려권 문언("공백 지적 후 반려")의 남용 우려 유무 |

## 5. Reply format

`analysis/rev/260826_02_ruling.md` 생성 권장: frontmatter(status/approved-by/date),
RQ별 판정(approve / revise-required(+구체 지시) / reject(+사유)), PRD §9 체크박스 6건의
[ ] 처리, 필요 시 조건 목록. 판정 후 메인 루프(owner)가 승인분만 반영하고 REV_LOG에 흔적을 남긴다.

## 6. Amendment B (260826 — Round-2 재제출, binding_fixes 반영 상태)

Round-1 판정(revise-required, BF1~BF9) 중 **BF7·BF9와 BF3·BF4의 도구 코드분은 Claude Code가
반영 1차(지침층)·2차(코드층)로 완료**했다(REV_LOG 「판정 반영」 행 2건). 아래는 PRD 소유자 몫의
잔여 반영이다.

| BF | 반영 위치 | 증거 |
|---|---|---|
| BF1 | PRD §3 S1 — corpus 유닛 산출(transcript·meta.yml §5.7·`[unreadable]`+verify_log·`_images` pNN.png)+**수율 임계 40%** 게이트(type-extractor 정의 인용) | PRD v2 S1 행 |
| BF2 | CODE_REGISTRY §6 「결정 완료」 — **사용자 확정(260826)**: (a) 병합·기존 subject_code 유지(수학 분리 선례는 "커리큘럼상 별개 과목" 한정 명문화) (b) 접두어 연장(`K-13~`, T/W/E/F 연속) (c) "(2015 개정)" 병기 + 성취기준 미대응 시 비고 처리 + 승격 판정에서 보조 근거 취급 | CODE_REGISTRY §6 + 이력 |
| BF3 | S4 반영 대상에 도구 등록 포함(`SUBJECT_FILES`+`EXPECTED`: IN·info·SM2 변경치, `md2quiz.py` SUBJECT_MAP)+게이트 문구 교체: `[OK] index.tsv matches regeneration (N rows)`+`[WARN]` 0줄+exit 0 | PRD §3 S4 · §7 · §9 |
| BF4 | S9 서술 교체: `python tools/import_grading.py <sim.tsv> --student-dir student/_sim` 강제 · note=`simulation`(ASCII) · set_id 무표식(§5.1 조인키 보호) · sha256 전후 동일 증거 첨부 | PRD §3 S9 · §5 리스크 |
| BF5 | PRD §7을 CODE_REGISTRY §6 온보딩 8항목으로 교체 + S4 목록 확장(curriculum_2022 정보 절·blocked 준용 포함) | PRD §7 · S4 |
| BF6 | S2 승격안 4조건 내장(문항단위 근거 / 별표 재산정·근거축 병기 — 기출 1개년이라 ★★★ 불가 / 부교재 근거 보존 / 주석 범위한정) | PRD §3 S2 |

**BF3·BF4 실행 로그(N5 요구 — REV_LOG 「판정 반영 2차」 행에서 인용)**

```
python tools/build_catalog_index.py --check
→ [OK] index.tsv matches regeneration (131 rows), exit 0   (회귀 없음)
사본 환경 4케이스: 정상 exit0 · 미등록 info.md 투입 exit1 ·
미선언 접두어 SM3 exit1 · 수동 편집 재현 exit1

python tools/import_grading.py sim.tsv                              → [ABORT] … exit 2
python tools/import_grading.py sim.tsv --student-dir student/_sim   → exit 0
  (헤더+2행 기록 · MASTERY 재생성 · student/S01 3파일 sha256 전후 동일:
   c130c71a… / d637117f… / ffae9938…)
python tools/import_grading.py real.tsv --dry-run                   → [DRY] exit 0
python tools/import_grading.py real.tsv --student-dir student/S99   → [ABORT] exit 2
```

**Round-2 회신 방법**: 기존 판정서를 새로 만들지 말고 `analysis/rev/260826_02_ruling.md`
안에 "## Round 2 decision" 섹션을 append(# history 앞)하고 REV_LOG에 행 1건을 추가한다.
PRD v2 §9 체크박스(BF별 6건+S5 통과분) 각각의 [ ] 처리도 함께 요청한다.
