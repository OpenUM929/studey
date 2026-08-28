---
actor: codex-omx
task: guidance_continuity
target: AGENTS.md, CLAUDE.md, Codex assurance guidance, and assessment Sol role contracts
status: done
updated: 2026-08-28
---

| no | 범위 | state | 산출물 | 비고 |
|---:|---|---|---|---|
| 1 | 기존 지침·정본·활성 WIP 재검토 | done | 본 WIP + 정적 회귀검사 실패 로그 | 사용자 최신 지시가 운영 S2보다 우선하는 로컬 거버넌스 수정. 기존 `codex-omx_260827_cycle0_s2_type_propose_relay.md`의 NEXT는 외부 Opus 11단위 회람이므로 재개 금지; 새 파일럿·단일세션 규칙과 충돌한다. |
| 2 | 컨텍스트/사용량 연속성 계약 회귀검사 | done | `tools/check_assurance_contract.py` | 정책 적용 전 16 failures를 확인했다. |
| 3 | 지침·Sol 역할 계약 보강 | done | `AGENTS.md`, `CLAUDE.md`, assurance 문서 2건, Sol 역할 TOML 4건 | 컨텍스트 60% 경계, 사용량 소진 HOLD, 재개 감사, 외부 Opus 자동재개 금지의 경계를 명문화했다. |
| 4 | 글로벌 지침 버전관리·설치 | done | `docs/GLOBAL_GUIDANCE_CONTINUITY.md`, `tools/sync_global_continuity_guidance.py`, `C:/Users/Administrator/.codex/AGENTS.md` | 글로벌 파일은 Git 저장소 밖이므로 동일 내용을 프로젝트의 정본 fragment+동기화 도구로 추적한다. 설치본 SHA-256 `2ab03e0665f4fe4aabacfa2bfe6192d0b9b6200f7e4a58f8c6eecade595a2389`; 백업 `AGENTS.md.20260828-131644.bak`. |
| 5 | 회귀·런타임 검증 | done | `assurance-contract: PASS (0 failures)`, global sync PASS, TOML 4건 parse PASS, Python compile PASS | `omx doctor`: 18 passed, 0 warnings, 2 failed(process identity, state root/session binding). 실제 팀은 `▲ blocked`. |

NEXT: Git 커밋·push 이후 process identity와 state root/session binding이 정상화된 새 OMX/tmux 세션에서 대표 수학 단위 1건의 actual-team preflight를 재실행한다. 두 runtime gate가 통과하기 전에는 분석 산출물이나 외부 비교 회람을 만들지 않는다.
