# 재개 프롬프트 — 신규 생성 금지

이 작업은 `260907_prompt.md` 이행의 계속이다. 먼저 `AGENTS.md`, `CLAUDE.md`,
`analysis/wip/mainloop_260907_math2_revision_release.md`, `output/_index.md`,
`output/260907/rev/260907_02_math2_implementation_report.md`를 읽는다.

STATUS=COMPLETE면 수정 없이 종료한다. IN_PROGRESS면 완료 목록·현행 파일 hash·소유권·충돌 writer를
확인하고 남은 데이터량을 다시 계산한다. 이미 교체한 3·4·6·7·22·25(1)은 새로 생성하지 않는다.

먼저 `python -X utf8 output/260907/260907_02_math2_verify_artifacts.py`를 실행한다.
불일치 시 파생본을 먼저 덮어쓰지 말고 원인을 확인한다. `package.py`는 의도된 변경의 승인 후에만 재생성한다.
`apply_revision.py` 및 `sync_documents.py`는 이미 적용한 이행 스크립트이므로 재개 명령이 아니다.

NEXT_ACTION: 외부 Opus 감사 결과가 로컬 파일로 도착했는지 확인한다. 없다면
작성자 자기검산이 아직 없는 56문항과 25(2)·(3)을 작은 배치로 보강할 수 있으나 외부 검증을 대행하지 않는다.
원본 신규성·예외·전역 ruler 실패는 해당 외부 판정 없이 완료로 바꾸지 않는다.
감사 회신 뒤에는 승인된 수정만 적용 → 원본/분리본/index/보고서/원장 동기화 → 새 검증 증거를 남긴다.

자동 예약은 구성되지 않았다. quota 중단시 실제 reset 관측 후 1회 resume audit로 이어간다.
외부 승인 대기를 이유로 2시간/5시간마다 Claude Code CLI를 자동 재시도하지 않는다.
