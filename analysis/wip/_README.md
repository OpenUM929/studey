# analysis/wip/ — 서브에이전트 체크포인트 저장소

> CLAUDE.md 「서브에이전트 공통 실행 규격」 ② (260826) 및 DOC_LOCATION §1 「작업 상태(WIP)」 계층.
> 위치 표준: [`../DOC_LOCATION.md`](../DOC_LOCATION.md) · 실행 규격 본문: 루트 `CLAUDE.md`.

## 규칙

- 파일명: `<actor>_<YYMMDD>_<task>.md` — **에이전트별 배타 소유**. 타 에이전트·검토자가 수정하지 않는다.
- 내용: frontmatter(`actor/task/target/status/in-progress|done|blocked/updated`) +
  슬라이스 표(`no | 범위 | state | 산출물 | 비고`) + 마지막 줄 `NEXT: …`.
- 재개: 소유 에이전트는 시작 시 자기 in-progress WIP의 `NEXT`부터 이어서 한다.
- 정리(삭제): **사용자만**. 에이전트는 done 전환 후 임의 삭제하지 않는다.
- WIP는 산출물·증거가 아니다 — 판정·리포트 인용 금지(완성본만 인용).
