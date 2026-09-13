# NEW-INDEPENDENT — Q1 수정 통합 후보 재판정

아래 블록을 **새로운 깨끗한 Astra 세션**에서 실행한다. 현재 작성 컨텍스트를 감사자로 재표시하지 않는다.
모델/깊이는 실제 호스트 증거 또는 명시적으로 허용된 사용자 확인을 기록하며 미확인은 미확인으로 남긴다.
실행되지 않은 세션/독립 판정을 완료했다고 표시하지 않는다.

```text
작업: 정보 A/B50 Q1 수정 후보의 독립 재판정 1묶음. 작성/수정하지 않는다.
cwd: C:\dev\study
운영: docs/ASTRA_EXECUTION_POLICY.md 및 docs/SESSION_HANDOFF_GUIDE.md 우선. Astra 단독 순차, 서브에이전트 발주/자동 재시도 없음.
책임 정의: analysis/REV_GUIDE.md §5·§6-d, .claude/agents/rev-arbiter.md를 읽되 실행자는 Codex/OMX이며 Claude Code 역할 신분을 주장하지 않는다.
입력: output/260912/rev/260912_06_info_ab50_q1_repaired_review_package.md, 같은 폴더의 260912_05_info_ab50_q1_manifest.json과 그 명시 입력.
먼저 manifest의 bytes/SHA256을 현재 파일과 전부 대조한다. 원천120파일은 source_evidence.json의 개별 hash 및 원천04 스냅숏으로 대조한다. 불일치 시 변경 출처 확인 전 중단한다.
범위: 원천60유닛의 코드/메타/바이트, 회귀303개(상태120/분포180/종료3), 기존15케이스/검출11, CLI15/호출부3. 원천 내용 전사·인쇄ID 확정·A/B 문제 품질·Q3 판정은 제외한다.
허용 읽기: 패키지/manifest의 지침·원판정·원명세·원후보·수정후보·패치·시험·결과, 60유닛 transcript/meta의 동결 확인. 실제 읽은 자료와 해시를 기록한다.
금지: 작성자 자기시험을 독립 증거로 단순 전재, 미확정 적격성/인쇄ID 추정, WARN 면제, 기준 변경, 제품/후보/원판정/작성자WIP/실운영 호출부 수정, 커밋·삭제.
실행: python output/260912/rev/260912_05_info_ab50_q1_verify.py
추가 원결함 재현: python output/260912/rev/260912_05_info_ab50_q1_regression_test.py --baseline --no-save
검증 기대: 수정303 실패0, 기존15 실패0, gate0 planted11/undetected0, 정상 분포 오탐0, CLI15/호출3 기대값 일치, harness 예기치 않은 경고0. 원측정 exit1/WARN40은 실패 증거로 보존한다.
출력: output/260912/rev/260912_08_info_ab50_q1_repaired_ruling.md (존재하면 덮어쓰기 금지), 자신의 새 WIP, 필요 시 REV_LOG append-only. validation.json만 재실행 로그 갱신 허용; 동결 시험결과는 --no-save로 보존한다.
판정 스키마: REV_GUIDE §6-d. Q1 수정 closure, Q2 정책키 미충족, R3 입력/호출 준비를 구분. 실제 입력 미완성과 코드 후보 적합성을 구분하고 정확히 승인 가능한 파일/변경 범위를 적는다. 인쇄ID 전수 커버리지는 null을 성공으로 변환하지 않는다.
예산/중단: 새 세션에서 자원 가용성을 확인하고 직접 1묶음만 수행. 잔여 사용량 미노출이면 수치 추정 금지·발주 금지; 자원 경고 시 증거 체크포인트 저장 후 HOLD. 추가 라운드·재시도·새 선행조건 자동 생성 금지.
정지: 판정문/근거/원장 및 [Codex/OMX 지시] 저장 후 독립 역할만 종료. 후보를 직접 고치거나 배포하지 않는다.
복귀: RETURN-AUTHOR — 이 패키지의 작성 책임, 소유 WIP analysis/wip/solve-back-verifier_260910_info_ab50_newsession.md. 기존 작성 세션 식별자 01a0903f-4294-7412-b42b-f5f8b15b98f9는 이전 인계 기록이며 현 가용성 미확인. 불가하면 NEW-CONTINUATION으로 같은 작성 책임 승계.
복귀 메시지: “output/260912/rev/260912_08_info_ab50_q1_repaired_ruling.md를 읽고 허용 범위와 두 키를 확인해 WIP NEXT에서 재개하라. 승인 없는 정본 반영·배포는 금지한다.”
```

이 문서는 실행 프롬프트이지 발주/독립 실행 증거가 아니다. 작성자 역할의 후보 준비만 완료됐고 전체 배포는 ▲ blocked다.
