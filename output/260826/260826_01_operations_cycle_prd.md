---
title: "Cycle-0 운영 전체 사이클 테스트 PRD"
created: 2026-08-26
author: main-loop
status: draft v2 — 판정 260826_02(revise-required, BF1~BF9) 반영 완료 · Round-2 재제출물
ruling: analysis/rev/260826_02_ruling.md
data_basis: origin_data 4개 ZIP (260826 09:19 접수)
scope_decisions: 사용자 확정 4건 (§2)
related:
  - output/260825/plan_3layer_architecture.md   # 구축 계획(완료) — 본 PRD는 그 운영 편
  - docs/DATA_STANDARD.md                        # §5.1 ATTEMPT_LOG · §5.8 subject_code
  - analysis/catalog/CODE_REGISTRY.md            # ID 선점 절차
  - analysis/REV_GUIDE.md                        # 검토 루프 규격
  - analysis/FORECAST_GUIDE.md                   # 예측 절차
---

# Cycle-0 — 신규 2학기 기출 전량 투입, 운영 전체 사이클 테스트

## 0. 요약

260826 오전 접수된 ZIP 4개(**2024·2025 2학기 중간+기말 고사원안 원본**)를 유일한 신규 입력으로
삼아, CLAUDE.md 작업 흐름표의 **전 경로를 한 사이클로 연결**해 처음 끝까지 돌린다.
REFINE(전량 변환·대장) → PROPOSE(math2 기출 승격 포함 유형 갱신안 + 정보 과목 신설) →
**묶음 1회** Claude Code 판정 → 반영 → 2026-2M 예측 → 문항 생성(practice) → solve-back 게이트 →
투입 허가 → S01 원장 시뮬레이션. 모든 단계의 산출물과 게이트 결과는 본 PRD §3의 수용기준으로
판정하며, 세션 보고서에 Group Q로 누적 기록한다.

```
S0 접수 ▶ S1 REFINE ▶ S2 PROPOSE ▶ S3 묶음 판정(CC 1회) ▶ S4 반영
        ▶ S5 예측 ▶ S6 생성 ▶ S7 solve-back ▶ S8 투입 허가 ▶ S9 원장 시뮬레이션
```

## 1. 신규 데이터 명세

| ZIP (origin_data/) | 내부 구성 | 특이점 |
|---|---|---|
| `2024_2학기_1학년_중간.zip` | 국어·수학·영어·통합사회·한국사 HWP + **통합과학 PDF** + 정답 PDF 2종(선택형/서답형 분리) | 과학만 PDF |
| `2024_2학기_1학년_기말.zip` | 6과목 HWP + 정답 PDF 2종(〃) | 통합과학 6.2MB |
| `2025_2학기_1학년_중간.zip` | **공통국어2·공통수학2·공통영어2·통합과학2·통합사회2·한국사2 + 정보** HWP + 통합 정답 PDF | **정보 신규**, 과목명 '2' |
| `2025_2학기_1학년_기말.zip` | 〃 7과목 + 통합 정답 PDF | 정보 65KB |

- 총 **25 HWP + 시험지 관련 PDF 1건(24중간 통합과학) + 정답 PDF 6건 = 파일 32건**(zip별
  files=8×4). 대형 파일(영어 6.4MB·과학2 8.9MB·한국사2 5.6~6.6MB)은 이미지 매립 가능성 → S1에서 지문 유실 체크.
- **의의**: ① INDEX.md §5 미확보 "2학기 자료 전반" 해소 ② SM2(도형의 방정식) 최초 실기출
  (`EX-math2-20252M/F`) ③ 정보 과목 자료 최초 유입 ④ 2024 2학기 수학은 당시 공통수학1
  진도(단원은 판독으로 확정, 추정 금지) → `math1.md` 2학기 확장 재료.

## 2. 사용자 확정 결정 (260826)

| # | 결정 |
|---|---|
| D1 | **정보 과목 포함** — 카탈로그 신설(IN 접두어)+교육과정 조사까지 수행 |
| D2 | **REFINE 전량** — 7~8과목 × 4회차 일괄 |
| D3 | **arbiter 묶음 1회** — S2 제안서+S8 세트검토를 하나의 결정요청 패키지로 |
| D4 | **사이클 종점 = S01 원장 시뮬레이션까지** |

## 3. 단계 정의와 게이트

| 단계 | 출력 | 주체 | Gate(수용기준) |
|---|---|---|---|
| **S0 접수·대장** | `origin_data/<zip명 동일 폴더>/` 해제본(zip 보존) · EXTRACTION_LOG 신규 항목 · INDEX.md 2학기 매트릭스 행+§5 체크 | 메인 루프 | 디스크 파일수·바이트 == namelist 집계 |
| **S1 REFINE 전량** | `extracted/<YYYY>-2학기/{중간,기말}/<과목>.txt`(hwp2md.py, 표보존) · PDF 7건(시험지 1+정답 6) PyMuPDF 텍스트/렌더 · **코퍼스 유닛 `corpus/<ID>/` 회차·과목별 생성**(CLAUDE.md REFINE 산출 규격): `transcript.md` + `meta.yml`(DATA_STANDARD §5.7: exam_code·variant·answer_key·render_dpi·render_tool) + 판독 불가 구간 `[unreadable]` 표기 + `verify_log.tsv` 행 + 수식·좌표 실린 페이지는 `corpus/_images/<ID>/pNN.png` 렌더 병행 · 문항수 대조표 | type-extractor | 변환 실패 0 · 머리말 문항수 vs 추출 카운트 ⚠ 목록화(±1 허용) · **판독 수율 임계 — 자료 형식별 2분기(조건 C1 반영, type-extractor 정의 인용)**: ⓐ PDF(7건) = 페이지당 문자수 < 인접 페이지 중앙값×0.4 → 페이지 렌더 대조 의무 · ⓑ **HWP(25건, 3MB 초과 대형파일 8건 전부 해당) = 페이지 개념이 없어 ⓐ 계산 불가** → **문항 수율**(머리말 선언 문항수 대조 ±1) + **이미지 수율**(`hwp2md.py --bindata` 출력 `bindata=<n> imgrefs=<m>`; 본문 `[[BIN....]]` 마커 전건이 전사되거나 `unreadable` 행으로 기록될 것). **`imgrefs > 0` 인데 전사도 `unreadable` 행도 없으면 게이트 FAIL** · 변환기 실행 불가 시 통과가 아니라 `▲ blocked`(원칙 11) |
| **S2 PROPOSE** | `output/260826/` 제안서: ①math2 — SM2-01~33 대조 승격안(**판정 BF6 4조건 내장**: (i) 유형별 기출 **문항단위 근거**(코퍼스ID+문항번호+transcript 행/페이지) (ii) **중요도 별표 재산정·근거축 병기** — 기출은 2025학년도 1개년(2M·2F)뿐이라 기출 근거만으로 ★★★ 불가 (iii) 부교재 근거는 삭제하지 않고 이력·대표 예시에 보존 (iv) 미출제 주석은 "2025-2학기 2회차 미출제"식 **관측 범위 한정**)+신유형(SM2 연장번호) ②타과목 2학기 유형·빈도 갱신안 — **BF2 (a)병합 정책**: 기존 카탈로그에 회차 근거 추가, 2024분 근거는 "(2015 개정)" 병기 ③**정보 신설**(IN-nn 초안 — 반영 시 CODE_REGISTRY §6 온보딩 8항목 전체가 대상임을 명시, curriculum_2022 정보 골격은 웹조사 근거만·미확인 칸 blocked) ④DATA_STANDARD §5.8 `info` 코드 추가안 ⑤CODE_REGISTRY IN 선점(RQ-2 조건부 승인 — BF3 도구 등록·BF5 동반 갱신을 S4에 포함하는 조건) | type-proposer | 제안 전 건에 근거(파일·행) 명시 · 임의 성취기준 기입 0 · **승격안에서 BF6 4조건 누락 시 게이트 FAIL** |
| **S3 묶음 판정** | t1⇄t2 자체검증 → 결정요청 패키지(제안서+S8 세트검토+④⑤ 개정안) → **Claude Code 회람 1회** | rev-writer⇄auditor → rev-arbiter | `*_ruling.md` + REV_LOG tier-3 · write-surface 준수 |
| **S4 반영** | **CODE_REGISTRY §6 「온보딩」 8항목 전부 동시 갱신**: §1 IN 접두어 행 · §3 매핑 행 · DATA_STANDARD §5.8 `info` · `catalog/info.md` 신설 · `curriculum_2022.md` 정보 절 · `build_catalog_index.py`(`SUBJECT_FILES`+`EXPECTED`: IN·info·SM2 변경치) · `md2quiz.py` SUBJECT_MAP · index.tsv 재생성 ＋ math2 승격(SM2 EXPECTED 갱신 포함) · HARVEST_LOG append · INDEX 갱신 | 메인 루프(owner apply) | 치환 count==1 무결성 · `python tools/build_catalog_index.py --check` → **`[OK] index.tsv matches regeneration (<N_after> rows)` 출력 + `[WARN]` 0줄 + exit 0**, 여기서 **`N_after = 131 + ΔIN + ΔSM2`** — `131`은 260826 저장소 실측 현행 행수, `ΔIN`은 S2에서 승인된 `IN-nn` 신설 유형 수, `ΔSM2`는 math2 승격으로 새로 추가되는 SM2 유형 수. **S4 착수 시 `ΔIN`·`ΔSM2`에 S3 판정 확정 정수를 대입해 `<N_after>`를 정수로 확정한 뒤 실행한다** — 기호를 남긴 채로는 게이트가 성립하지 않는다(원칙 9-c-iii · 조건 C3)(fail-closed: 문제 시 `[FAIL] … gate not passed` exit 1) |
| **S5 예측** | `analysis/forecast/` 2026-2M math2 A~E 등급표 — 2025 2학기 기출 단원 구성을 분할 가설의 최강 근거로 사용(근거 회차 열·1개년 관측 명시 — 판정 N2 권고) · **⚠️범위 미확정** 헤더 | forecast-writer → reviewer(t1, 미확정이므로 t1⇄t2 ≤5R 가능) | E(사각지대) 명시 · 근거 회차 링크 |
| **S6 생성** | practice 세트 1본 — 예측 배분 반영, AUTHORING_GUIDE 4단계·서식규칙, **신 QS 프론트매터 계약 적용**(set_id/subject_code/unit/scope_confirmed:false/intended_use:practice) | item-writer | 배분==등급표 · 자기점검 체크리스트 통과 |
| **S7 게이트** | 맹목 풀이 전 문항 — 정답 유일성·조건 충분성·Tier·해설 중간식 | solve-back-verifier | FAIL 0(발견 시 item-writer 수정→재게이트) |
| **S8 투입 허가** | S3 판정 통과+사용자 확인 → tier-1 흔적 반영 → 투입 표기 | 메인 루프 | 미투입→투입 전환 기록 |
| **S9 원장 시뮬레이션** | 가짜 응답 TSV 손작성(mark_code enum · **note=`simulation` ASCII 고정** · **set_id에는 표식 없음** — DATA_STANDARD §5.1 2열 조인키 보호 · main_type은 index.tsv 등재분만) → **샌드박스 강제 실행: `python tools/import_grading.py <sim.tsv> --student-dir student/_sim`**(실원장 경로 지정 시 도구가 거부 — BF4) → MASTERY(샌드박스 내 재생성) → build_report HTML → SHARE_LOG · WEAK_LEDGER 승격 **제안** 1건(교사 판정은 시연으로만) | tools(main loop 구동) | 도구 exit 0 · **실행 전후 `student/S01/*.tsv` sha256 전후 동일(도구의 무손상 증거 출력을 그대로 첨부)** · 비-ASCII 행은 도구가 거부함을 확인(§6) |

## 4. 명명·배치 규칙 (기존 관행 연장)

- 원본: `origin_data/<ZIP과 동일한 폴더명>/…` — 읽기는 변환 시만(원칙).
- 추출물: `extracted/2024-2학기/중간/국어.txt` 식(`extracted/<YYYY>-2학기/{중간,기말}/`) —
  기존 `extracted/<YYYY>/{중간,기말}`(1학기)와 충돌 없음.
- corpus ID: `EX-korean-20242M` … `EX-math2-20252F`, 정보 `EX-info-20252M/F`
  (HARVEST_LOG 기존 `<subject>-<YY><학기><M/F>` 관행).
- 정보 유형 ID: `IN-nn` — CODE_REGISTRY §5 선점 절차 후 부여. subject_code `info`.

## 5. 리스크와 방어

| 리스크 | 방어 |
|---|---|
| math2 기출 수식 소실(좌표식 다수, 1학기 전례) | S1 품질 측정 → 필요시 페이지 PNG 렌더 병행 판독, ⚠ 마킹 유지 |
| 대형 HWP 이미지 매립으로 지문 누락 | ~~페이지당 문자수 급감 감지~~ **HWP엔 페이지가 없어 무동작이었다(조건 C1)**. → `hwp2md.py`가 `[[BIN....]]` 마커를 남기고 `--bindata`로 이미지를 보존하도록 260826 수정 완료. S1 게이트는 `imgrefs` 전건 해소를 요구 |
| hwp5html 환경 의존 | 1학기 때 동일 환경 성공; 실패 시 해당 건만 보류 목록화(전면 중단 없음) |
| 정보 교육과정 임의 기입 | 웹조사 출처 URL만 기입, 미확인 칸은 빈 채로 둠(원칙) |
| 2026-2M 범위 미공지 | 예측 전면 ⚠️미확정 모드 — 확정 시 재채점 절차 FORECAST_GUIDE 따름 |
| 원장 오염 | S9는 **샌드박스 경로 차단**(`--student-dir student/_sim` 외 거부)+실행 전후 sha256 무손상 증거; 표식은 ASCII 한정(note=`simulation`, DATA_STANDARD §6) — set_id 표식 금지(조인키 보호) |

## 6. 원칙 준수

범위 가드(원칙 2) · append-only(3) · 검수 피드백 증록(4) · 정답+해설+유형ID 동반(5) ·
자료 등급 구분 — 부교재-only 유형을 "출제된다"고 서술하지 않음(6) · 미확정 표기(7) ·
검토/수정 분리 — 판정은 CC, 반영은 owner(8) · **비가역 방어(9)** — 코퍼스ID·접두어는
BF2 결정을 CODE_REGISTRY에 선등록한 뒤 부여, 원장 시뮬은 샌드박스만 허용 ·
**동반 갱신(10)** — S4는 CODE_REGISTRY §6 온보딩 8항목을 같은 작업에서 일괄 갱신 ·
**게이트 fail-closed(11)** — exit code 단독 판정 금지, 명령+기대 출력 문자열+경고 0줄+
exitcode 조합으로 판정 · **무커밋**(별도 지시 시에만).

## 7. Ledger 갱신 계획

**S4 반영 목록 = CODE_REGISTRY §6 「신규 과목·신규 학기 온보딩」 8항목 전부** — 같은 작업에서
동시 갱신하며 부분 갱신은 금지다(누락 시 증상은 §6 표 각 행 참조). 이 외 대장:
EXTRACTION_LOG(S0) · INDEX.md(S0/S4) · HARVEST_LOG(S4) · REV_LOG/_index/HISTORY(S3/S8) ·
forecast(S5) · 세트(S6~8) · SHARE_LOG(S9) · 세션 보고서 Group Q(전 단계).

## 8. 최종 Done

S0~S9 게이트 전부 PASS + 묶음 arbiter 승인 + 사용자 투입 확인 + 세션 보고서 Group Q 완결.
커밋은 이후 사용자 지시로 별도 실행.

## 9. 검토 체크박스 (Round-2 판정 결과 — binding_fixes 전건 [x])

- [x] **BF1** — S1이 corpus 유닛(transcript·meta.yml §5.7·`[unreadable]`+verify_log·`_images` pNN.png)을 출력하고, 수율 임계 40%가 판정 가능한 게이트로 명시됐는가
- [x] **BF2** — (a)병합·(b)연장·(c)2015 개정 병기 결정이 CODE_REGISTRY §6에 "S1 이전 기록" 요건(원칙 9-a)을 충족하는 형태로 남아 있는가
- [x] **BF3·BF5** — S4 반영 대상이 §6 온보딩 8항목(도구 등록·curriculum_2022 정보 절 포함)을 전부 덮고, 게이트 문구가 fail-closed 도구 동작(`[OK] … (N rows)`+`[WARN]` 0줄+exit 0)과 일치하는가
- [x] **BF4** — S9이 샌드박스 경로 차단+sha256 무손상 증거 설계이며, set_id 무표식·ASCII 표식 규칙을 지키는가
- [x] **BF6** — S2 승격안에 4조건(문항단위 근거·별표 재산정·부교재 근거 보존·주석 범위한정)이 내장돼 있는가
- [x] **S5 미확정 모드** — Round-1에서 통과 판정(변경 없음 유지, N2 권고 반영해 근거 회차 열 추가)
- [x] **기타** — BF3·BF4의 실행 로그 인용(REV_LOG 「반영 2차」 행)이 N5 재제출 요구를 충족하는가

### 9-b. Round-2 단계 차단 조건 C1~C4 해소 현황 (260826, owner 반영)

| 조건 | 차단 단계 | 근본 원인 층 | 조치 | 상태 |
|------|----------|------------|------|------|
| **C1** HWP에 수율 임계 무동작 + 매립 이미지 소실 | S1 | **지침**(`type-extractor` 정의가 PDF 페이지 전제) + **도구**(`hwp2md.py`) | 도구 3결함 수정(hwp5html 경로 탐색·`[[BIN....]]` 마커·`--bindata` 보존) + `type-extractor` 정의에 HWP 2축(문항수율·이미지수율) 신설 + S1 게이트 2분기 | **해소** — 실측 재현 `bindata=35 imgrefs=38`, 마커 41개·파일 35개 보존 |
| **C2** `§6 (b)`가 실재하지 않는 접두어 `E` 열거·과학 7접두어 누락 | S2 | **지침**(정본 본문의 사본 열거) | 재열거 삭제 → §1 참조로 교체 + 이력 1행 | **해소** |
| **C3** S4 게이트 기대 행수가 기호 `N` | S4 | **지침**(원칙 11이 플레이스홀더를 금지하지 않음) | `N_after = 131 + ΔIN + ΔSM2` 산술식 확정 + 착수 시 정수 대입 의무 명시 | **해소** |
| **C4** 세트ID 예시가 `RE_SET` 불통과 | S6 | **지침**(CLAUDE.md ②가 §1.3 미대조로 예시 창작) | 예시를 `SET-260826-math2-40` + `_I3`(파일명 요소)로 정정, CLAUDE.md·`item-writer` 정의 동시 갱신(원칙 10) | **해소** |

> 재발 방지 — 네 조건 중 셋(C2·C3·C4)이 **정본 본문에 적은 식별자·열거·수치를 레지스트리와
> 대조하지 않은** 같은 원인이었다. CLAUDE.md **원칙 9-c** 를 신설해 회람문에만 걸려 있던 실측
> 의무를 정본 본문까지 확장했다. **서브에이전트 기인 결함은 0건**이다.

# history
- 260826: 초판 — 신규 2학기 기출 4 ZIP 접수에 따른 Cycle-0 PRD. CLAUDE.md 데이터 도착
  게이트(신설)에 따라 Claude Code 검토 라운드를 거친 후 S0 이상 실행.
- 260826: 판정 260826_02(revise-required, BF1~BF9) 반영본(v2) — **BF2 사용자 확정**
  ((a)병합·(b)연장·(c)세대 병기)을 CODE_REGISTRY §6에 선기록, S1=corpus 유닛+수율 임계 40%,
  S2=승격 4조건 내장, S4=§6 온보딩 8항목+fail-closed 게이트 문구, S9=샌드박스 강제+sha256
  증거, §7=온보딩 목록 교체, §6=원칙 9·10·11 추가. 라운드 재개(_index in-round, R2) 후
  Amendment B와 함께 재제출.
- 260826: **Round-2 판정 approve(조건부) 반영** — §9 체크박스 7건 전건 [x], §9-b 신설.
  단계 차단 조건 C1~C4를 owner(메인 루프)가 해소: S1 게이트 HWP 2분기화(C1), S4 게이트
  `N_after = 131 + ΔIN + ΔSM2` 산술식화(C3), §5 리스크 행 정정(C1). 저장소 동반 갱신은
  `tools/hwp2md.py`·`.claude/agents/type-extractor.md`·`.claude/agents/item-writer.md`·
  `analysis/catalog/CODE_REGISTRY.md`·`CLAUDE.md`(원칙 9-c 신설·11 보강). 커밋 없음.
- 260826: **P0 정정([OC 지시] 260826_03)** — §3 S1 게이트 수치 오기 수정(PDF 22→7 · HWP
  24→25; 저장소 전수 재집계 32=HWP 25+PDF 7 대조). `.claude/agents/type-extractor.md` 동일
  수치 동반 갱신(원칙 10). P0-1(info 선행 등록)·P0-2(math1-20242M/F)는 CODE_REGISTRY에,
  P0-4(SUP 폴더 rename)는 corpus/_README 불변식 기록과 함께 반영. 커밋 없음.
