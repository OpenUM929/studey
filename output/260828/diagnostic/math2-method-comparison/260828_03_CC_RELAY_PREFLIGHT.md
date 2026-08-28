# 260828_03 CC 회람 사전점검 — Opus 페르소나·역할·방법 비교 진단

## 점검 근거

- 회람 형식: `analysis/REV_GUIDE.md` §6-b L299-328
- 외부 실행자 정의: `.claude/agents/type-proposer.md` L1-114
- 실험 동결입력: `INPUT_MANIFEST_260828.tsv` 10행
- Codex 진단: `260828_02_codex_math2_method_trace.md`, `260828_02_codex_math2_diagnostic_analysis.md`

## 보정한 결함

| 이전 260828_02 회람의 빈틈 | 260828_03 보정 |
|---|---|
| 실행자를 단지 “type-proposer 계약을 읽은 Opus”로만 서술 | 상산고 1학년 담당 교사·전문 출제자라는 페르소나, 추출-분석 파이프라인의 제안자라는 역할, 정본 read/cite-only 경계를 명시 |
| 정상 역할 산출물과 이번 진단용 reply-only 예외가 섞일 수 있음 | 정상 역할의 2개 제안문서·verify_log·3단계 검토 진입을 명시하고, 이번에는 방법 비교만을 위한 의도적 예외라고 분리 |
| 업무 항목이 질문 속에 압축됨 | 무결성→문항 배정→5~12 통합/변형축/함정/별표→신규·기존 유형→COMMON_TYPES→로그 초안의 전체 책임을 열거 |
| 회람 규격의 수신자 근거 문장이 약함 | `<executor>`에 정의 파일과 역할 선택 근거를 한 줄로 인용 |

## 발신 전 확인

- [x] §6-b 필수 태그 6개를 한 개의 fenced block에 배치한다.
- [x] 대상·이번 라운드 작성 파일·외부 reply 경로·no-commit·허용 쓰기면을 명시한다.
- [x] 경로/입력 수는 manifest 10개, 문항 수는 22개로 고정한다.
- [x] 외부 Opus가 정본·원장·코퍼스를 수정하지 못하게 한다.
- [x] 이전 `260828_02_CC_OPUS_MATH2_METHOD_COMPARISON_RELAY.md`는 보존하되, 이 `260828_03`이 실행용 회람임을 명시한다.