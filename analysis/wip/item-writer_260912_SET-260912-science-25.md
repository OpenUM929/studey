---
set_id: SET-260912-science-25
author: 메인 루프
executor: Codex/OMX
status: blocked
grade: proposal
intended_use: practice
---

# 상산고 1학년 2학기 중간 대비 25제 — 출제 체크포인트

## 사용자 확정 요구
- 2024·2025 과학 2학기 중간의 기존 유형 분석 기반, 총 25문항.
- 숫자·기호·단어 배열만 바꾸는 동형 문제 금지. 비수치 변형축 2개 이상.
- 최고 난도에 DF5 사고력 요구. 문제 작성 → 독립 내용 감사 → 배포본까지 수행.
- 모든 AI Astra. 작성자 자기검산을 독립 감사로 표시하지 않음.
- HWP 재변환, A4·여백·인쇄 규격 점검 제외.

## 현재 확인된 출제 입력 경계
- `analysis/catalog/science.md`는 현재 제목·근거 회차가 통합과학1, 1학기 6회이다.
- `output/260831/260831_01_catalog_update_SC.md`는 미적용이며 신규 유형 ID 미확정이라고 명시한다. 같은 문서 §0-2는 2025-2중간 29문항 중 기존 ID 대응이 ER-05 1건이라고 명시한다.
- `output/260831/260831_01_type_analysis_SC.md` 및 2024·2025 기존 classification 문서는 존재한다. 이를 이유 없이 재변환하거나 전면 재분류하지 않는다.
- CODE_REGISTRY §6(b)에 기존 접두어 연장 정책은 이미 승인되어 있다. 정책 존재와 개별 유형의 승인·적용 완료는 구별한다.
- `.claude/agents/item-writer.md`와 CLAUDE.md 원칙 1에 따른 승인 카탈로그 출제 조건을 아직 충족했다고 주장할 수 없다. 임시 유형을 승인 유형으로 가장하거나 임의 ID를 부여하지 않는다.

## 실적 및 검증
| 슬라이스 | 완료 | 검증 | 상태 |
|---|---|---|---|
| 출제 입력 조건 확인 | 역할 지침·루브릭·기존 유형 분석 및 갱신안 확인 | 위 문서 본문 읽음. 최신 검색에 존재하지 않는 output/260912 경로 경고 발생하여 전역 승인 부재 증명으로 사용하지 않음 | ▲ blocked: 해당 유형의 승인·적용 근거 미확인 |

작성 문항 0/25, 독립 풀이 0/25, 품질 감사 0/25. 배포본 없음.
소유자: 현재 메인 루프 단독. 기존 사용자 변경·원장·카탈로그는 수정하지 않음.
모델 실행 증거 및 현재 잔여 사용 예산 미확인. 새 서브에이전트 발주 없음.

## 2026-09-12 후속 — 작성 후보 생성

사용자가 반복한 수행 지시에 따라 기존 분석을 참조한 **proposal 등급 후보**를 작성했다. 승인 정본 유형 또는 배포본으로 승격한 것이 아니다. 위 0/25는 당시 이력이며 현재 수치는 아래와 같다.

- 문제: `output/260912/260912_01_science_midterm25_questions.md`, 25문항, sha256 `483dbc3d84431afaf2db13c543099172fcaf0989a0584da41411dd43f84c1efe`.
- 답·해설: `output/260912/260912_01_science_midterm25_answers.md`, 25답, sha256 `621e15f1c333e5554d68a90edb13bce3c8fcef642ef1ea1e32158999ebd08e5f`.
- Python 정규식 대조 exit 0: expected=observed=answers=1..25, duplicates=[], missing=[], extra=[], 선택형60+서술형40=100점.
- 현재 독립 검증 0/25. 문제별 신규성 및 T4 목표 충족은 검토 전이다. 특히 원리 설명형의 구조 변화 부족 가능성을 감사 대상으로 남긴다.

### 독립 맹목 풀이 파일럿 발주 행렬

- 목적/단위: 생성 세트 문항 1~8 정확히 8개, 문제 파일 1개에서 해당 부분만 읽는 partial 검증. 기출 전사·분류 검증 아님.
- 입력: 위 문제 파일의 머리말 및 1~8, `.claude/agents/solve-back-verifier.md`, `analysis/catalog/DIFFICULTY_RUBRIC.md`, `docs/ASTRA_EXECUTION_POLICY.md`. 정답·출제자 결론·이 WIP·과거 대화 및 나머지 문항은 금지.
- 근거 밀도/결함: 모든 조건은 문면에 있음. 그림 없음. 임시 분석군 표기와 목표 난도는 승인 증거가 아님.
- 레인: blind-pilot = gpt-6-astra = xhigh(요청; 실제 값은 호스트 반환으로 별도 확인). native architect의 read-only 논리 설계 검토로 실행; 독립 풀이 책임 지침도 소비. 정본 판정 권한 주장 금지.
- 예상 작업: 문항당 정답·핵심 풀이·유일성·모순·잉여 조건·난도 각 1행, 약 8문항/12분. 최대 동시 자식 1.
- 예산: 현재 잔여 세션 예산을 직접 측정할 수 없어 insufficient. AGENTS fallback (2)에 따라 이 한정 파일럿만 발주. 12분 또는 10 tool calls에서 중단하고 이미 푼 문항을 반환. 자동 재발주 없음.
- 쓰기: 자식은 read-only, 영구 파일 쓰기 금지. 반환 원문은 리더가 별도 감사 기록으로 보존. 공유 원장·제품 수정 금지. 독립성은 fork_turns=none과 허용 입력 제한, 파일 시스템 격리 아님.
- 반환 스키마: runtime 모델/깊이 관측과 미확인 구분, 실제 읽은 파일/부분, 입력 해시, expected/observed/duplicates/missing/extra, 8행 풀이표, 결함 ID 목록, 4줄 진행지도+Session.
- 검증/정지점: 리더가 반환 ID 집합=1..8 및 입력 해시 일치 확인 후에만 다음 슬라이스 크기를 결정. 부족/시간 초과 시 확대 금지.

NEXT: 첫 8문항 맹목 풀이 파일럿을 실행하는 동안 리더는 별도 신규성 근거표 작성. 파일럿 반환을 보존·대조하고 결함을 먼저 처리한 뒤 후속 검증을 결정한다. 전수 독립 검증 및 내용 감사 전 배포가능 표기 금지.

## 파일럿 후 수정 및 재검증 체크포인트
- 독립 파일럿: 8/8 유일답; HOLD(3 선택지 우회, 2·4·5·7·8 난도 문제). 4 tool calls 완료. 반환 요약 `output/260912/rev/260912_01_science_blind_pilot.md`에 보존. 원문은 native 반환 메시지.
- 사용자 후속 수행 지시 후 원작성자가 2·3·4·5·7·8 수정. 2·4·5를 T1/2.5점으로 조정, 7·8 새 자료로 구조 변경. 9~12 배점만3.15로 조정하여 선택형60 유지.
- 수정 도중 PowerShell 파이프의 비ASCII 인코딩 손실 발견. author-owned UTF-8 수정 파일을 적용하여 복구; 문제지 ???=0, IDs25 측정. 이 사건을 감추거나 독립 감사로 표시하지 않음.
- 현 문제 hash: cd097a46b0b8da5ba724a0824d0fd07cd1473eb5f4cf6e508ee15d2f404ef17e.
- 재검증 단위1~8(8문항), 동일 read-only 독립 파일럿 컨텍스트 재사용. 정답 미노출 유지. 입력·금지 쓰기·schema는 위 행렬 동일. 관측 파일럿4calls/8items; 남은 서비스 예산 미노출=insufficient, fallback2 재검증1slice만. 최대8calls/10분, 미완료면 부분 반환. model=Astra(앞선 자식 호스트보고), depth=요청xhigh/실측미노출. 작성자와 독립, 새 작성자 답 유입 없음.
NEXT: 수정본1~8 재검증 반환 후 ID/hash와 지적 종료 여부 대조. 통과 이후에만9~16 맹목 풀이로 전진. 리더는 그동안 본문을 동결하고 내용 근거표·검증 기록 정리만 수행.

### 후속 한정 발주 — 8~16 (9문항)
1~7재검증 지적 종료. 8의 자료 의존성만 미종료여서 집계·비교가 필요한 문면으로 재수정했다. 최신 문제 hash892206dcdb2e094a16493d945c1ce973d8757e56d6bc61116bb5d6cc09dc7ccd.
목적: 8 재검증을 먼저 수행하고 종료 확인 시9~16(8개) 독립 풀이. 총 할당9문항.8이 실패하면9~16을 열지 않고 즉시 반환.
나머지 모델/소유권/금지입력/schema는 이전 행렬 동일. 허용 입력범위만8~16으로 제한. 자식모델Astra 호스트보고/깊이미노출, 요청xhigh. 원문prefix hash와 본문전체 hash를 구별하여 기록.
예산: 직전8문항2calls 실측; 현재 서비스 잔여량미노출=insufficient, fallback2 단일slice. 최대10calls/12분. 동시자식1. 결과 출력범위expected8..16; 조기중단시scopepartial 및 미완료IDs명시. 작성자 답지·원장·WIP읽기/쓰기금지.
NEXT: 8 게이트 종료 및9~16 독립 결과를 보존·대조하고 수정. 통과 이후17~25로 진행. 통합본은파생후보이며 수정 종료후재생성.

### 9~16 재작성 및 단일 재검증 발주
독립8지적종료,9~16정답일치이나T3과장/우회로HOLD. 반환요약rev/260912_02_science_blind_middle.md. 원작성자가9~16을자료결합형으로재작성하고답지갱신. 문제hashda838b35564558db236b546e161367aa5407ceeb4ff32d1265484ff7901e20b6.
발주단위9..16정확히8개, 같은독립read-only컨텍스트, 답지/WIP/17..25금지. 모델Astra호스트보고, 요청xhigh/실측깊이미노출. 직전9개3calls실측. 현재잔여예산미노출=insufficient/fallback2, 최대8calls/12분, 동시자식1. 반환각답/풀이/조건/유일성/최단경로난도, expected/observed집합및파일hash. 승인정본/배포판정아님.
NEXT: 9~16 수정본 독립 재검증. 미종료시새작업확대없이해당지적만처리. 리더는동결본문외의신규성기록을현문면에동기화한다.

### 마지막 맹목 슬라이스 발주 — 17~25
9~16재검증8/8주요지적종료, 도구2calls실측, 기록rev/260912_02_science_blind_middle.md. 1~16답지미노출유지.
원작성자는아직미검토17~25중18(집계편향반례),19(혼합비판정),22(가설대조/질량경계)를구조적으로보강하여단순반복을줄였다. 17~25의신규성·목표난도는독립검토전.
할당17..25정확히9문항(선택4,서술5). 입력문제hash557ba2e9f64eb03f74d5f3df25d89511e43c0849a357c26ac1a3c6ab92e35e3d. 허용같은문제머리말/17..25 및루브릭·정책·책임지침. 정답·신규성표·WIP·다른산출물금지. 자식read-only모든쓰기금지.
모델Astra호스트노출보고/요청xhigh/실제깊이미노출. 현남은예산도구미노출=insufficient/fallback2단일slice. 예상9문항/15분, 최대10calls, 동시1. 기준:각독립답·풀이·유일성·조건·실제DF5·서술형의채점가능성; 원작성자해설대조는금지. 4줄진행지도/실제입력hash와expected/observed/duplicates/missing/extra를반환. 시간초과시부분반환.
NEXT: 17~25독립풀이반환·수정·재검증 후 정답파일을별도품질감사컨텍스트로전달. 아직문제와해설의독립대조및N축전수감사미실시.

### 260912 user-directed workflow repair
Preserve all 25 draft items and blind evidence. Final slice summary: output/260912/rev/260912_04_science_blind_final_slice.md. 18/19 Tier overstatement remains; full answer-key and novelty audit pending. Switch from prior NEXT because user explicitly requested instruction audit/removal of micro-check loops. Procedure: docs/ITEM_DELIVERY_WORKFLOW.md; audit: analysis/rev/260912_item_workflow_audit.md. Exclusive owner: root.
NEXT: finish bounded procedure review, then consolidate remaining whole-set content audit and batch corrections; do not restart blind pilot or convert HWP.

