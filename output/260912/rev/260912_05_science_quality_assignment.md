# 과학 25제 전체 내용 감사 발주

목적: 기존 맹목 풀이를 재시작하지 않고 정답·해설·신규성·유형 근거·세트 구성을 한 번에 검토하여 단일 수정 목록을 반환한다.

- 정확한 단위: SET-260912-science-25, ID 1~25 전체. 문제·답지·novelty 3개 대상. 이전 동일 과목 frontmatter 검색 4파일은 모두 현 세트의 통합본·파생본·이전 baseline이다. 다른 과목은 제외. 감사자가 이름/내용 기반 누락 여부도 한 번 확인한다.
- 입력: `output/260912/260912_01_science_midterm25_questions.md`, `_answers.md`, `.novelty.tsv`; `rev/260912_01_science_blind_pilot.md`, `260912_02_science_blind_middle.md`, `260912_04_science_blind_final_slice.md`, `260912_03_science_carry_forward.json`; `output/260902/EX-science-20242M_classification.md`; `output/260831/260831_01_type_analysis_SC.md`, `260831_01_catalog_update_SC.md`; `analysis/catalog/science.md`, `DIFFICULTY_RUBRIC.md`, `TYPE_MASTER.md`, `analysis/curriculum_2022.md`; `.claude/agents/item-quality-auditor.md`, `docs/ITEM_DELIVERY_WORKFLOW.md`, `docs/ASTRA_EXECUTION_POLICY.md`. 허용 자료의 관련 절만 읽는다.
- 제외: HWP/PDF 변환, A4 용지/미관 검사, 유형 재분류·정본 등록, 다른 과목 작업, 전역 시스템 감사. 2025의 placeholder 분류표를 근거로 사용하지 않는다.
- 알려진 결함: 18/19 목표 T4 과장; 실제 T3로 재표기 가능 여부와 배점 영향 검토. 20 경계는 이전 독립 풀이에서 추가 재작성 불필요. 기존 2학기 분석군은 정본 ID가 아니므로 등록 상태를 숨기지 말고, 내용 결함과 등록/기준 공백을 분리한다. 통합본은 stale 후보이며 아직 감사 대상 최종본이 아니다.
- 출력: 각 ID에 정답 대조/핵심 중간 단계/신규성(요구 행동·풀이 구조·비수치 축)/유형·범위/난도/차단 결함 또는 PASS; 세트 내 동형 여부; expected/observed/duplicates/missing/extra; 실제 입력·해시; 우선순위별 단일 수정 목록. 모르는 내용은 미검증으로 표시. 모든 발견을 모은 뒤 반환, 앞 문항 결함 때문에 뒤 문항 검토 중단 금지.
- 소유권: 감사자는 read-only 반환만 소유, 제품·원장·WIP 수정 금지. 리더가 반환을 로컬 보고서로 보존하고 수정 적용. 작성자 자기검산과 독립 감사 분리. 이는 맹목 풀이가 아닌 독립 품질감사다.
- lane=whole-set-quality = gpt-6-astra; 요청 xhigh/실제 깊이 미노출 여부 기록. 네이티브 architect는 위험 검토 실행 역할이며 위 품질감사 책임을 수행; 운영 모델과 입력은 실제 보고한다.
- 측정: 대상 문제 23143 B, 답지 13042 B;25문항, 주요 분석 2개+2024 매핑1개. 예상 25문항 단일 유계 슬라이스. 서비스 잔여 예산 미노출=insufficient, fallback2 1슬라이스만 발주. 최대 동시1; 최대18도구 호출/20분, 자원 경계에서는 완료 ID와 미완료 ID를 보존해 부분 반환. 재귀 위임/자동 재시도 금지.
- 검증: 전25 ID 집합과 반환의 문항별 근거 대조; 범위 밖 등록 문제를 내용 PASS로 감추지 않음. 종료/재개점: 모든 지적을 원작성자가 일괄 반영한 뒤 변경·영향 문항만 재검증. 단순 표기·주관적 난도 경계는 무한 수정 사유가 아니다.
