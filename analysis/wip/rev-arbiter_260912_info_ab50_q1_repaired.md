---
title: 정보 A/B50 Q1 수정 후보 독립 재판정 체크포인트
created: 2026-09-12
author: Codex/OMX
responsibility: 독립 재판정
model: gpt-6-astra
reasoning_depth: medium
model_evidence: 현재 대화 사용자 확인; 호스트 검증 아님
status: done
release: blocked
---

## 범위·소유권
- 별도 작성 컨텍스트를 승계하지 않은 독립 재판정. 문항 맹목 풀이는 아니다.
- 책임 정의: `.claude/agents/rev-arbiter.md`, `analysis/REV_GUIDE.md` §5·§6-d, `docs/ASTRA_EXECUTION_POLICY.md`.
- 허용: 06 패키지, 05 manifest 명시 입력, 원천 60유닛 transcript/meta 바이트·메타. 문항 내용/인쇄ID 확정·Q3는 제외.
- 독점 쓰기: 본 WIP와 `output/260912/rev/260912_08_info_ab50_q1_repaired_ruling.md`, REV_LOG 1행. 지정 validation.json 재실행 갱신 허용. 다른 WIP·후보·보호 기준·제품 무수정.
- 자원: 잔여 사용량 수치 미노출. 직접 1묶음만 수행, 발주 없음. 자원 경고 미관측; 경고 발생 시 checkpoint 후 HOLD.

| slice | 완료 증거 | 상태 |
|---|---|---|
| 입력 경계·동결 | manifest 45파일 bytes/SHA256 일치; 04 원천 표 재유도, 60유닛/120파일 개별 hash·locator 일치; directories/sidecar/dispositions 양방향 차집합·중복 0; policy_key=null; 운영 공급 파일 없음 | 완료 |

## 불변 앵커
- manifest, 원천 개별 hash 및 모든 실행 출력은 이번 판정문 §1에 수록한다.
- source_evidence.json SHA256: e804333b3b3bd85e2cb1f39ed151aa8ee042eb017c2e45e140eb6733d02fe551
- repaired_candidate.py SHA256: 12a2f410ec7fcff3b604480dd96c23248e90962a620c1e3bc4350c8e0fd3a4ae
- 원판정04 SHA256: 1ec05434a586f4c372d6409a79de62408f0ff9c3f77e7bbadadf471cc5410c56
- Git 조회에서 사용자 전역 ignore 경로 접근 거부 warning 관측. 기존 변경 보존; 시험 경고0과 혼합하지 않는다.

## 판정 및 반환 체크포인트
- 지정 verify exit0: 303 실패0·기존15·gate0 planted11/undetected0·CLI15/호출부3 기대 일치. baseline exit0은 원결함302/303 재현 성공이다.
- 독립 보강4건(혼합상태·drift 우선·정상 순서변경·분포절 누락) 통과. 첫 JSON 출력 cp1252 인코딩 오류는 ensure_ascii=True로 출력만 보정한 재실행 exit0으로 해결; 제품 결함 아님.
- 판정08: 82009 B / SHA256 fb6254c69361df538639fb0b1cc5fc832f28f7e5e924e6d0332aa161d030a132. Q1/R3 후보 approve, 신규 구속 수정0. Q2 정책키·실제 입력 근거·운영 적용·배포 blocked.
- validation.json: 28109 B / SHA256 3835d24d80ffdd52d42f65859d9d36ed35cb97775a014e62c927563465a355a4.
- 판정문 재현 A 실행: manifest45/원천60/120 mismatch0. 고정 절6·요약3unit·Python 코드블록2 파싱 통과; trailing whitespace0. textpatch self-test exit0 seeded10/undetected0, 의도된 FAIL/WARN 별도 보존.
- 런타임: notepad_write_working 성공. state write 최초 EPERM 뒤 승인된 재실행 성공. 독립 검토 mode inactive, ruling-saved 체크포인트 저장. 수동 compaction 명령 미노출; 수동 compact 수행 주장 없음.
- REV_LOG 행은 기존 prefix 바이트 보존을 확인하여 1행 append. 코드/원천/보호 기준 동결 재확인 후 역할 종료.

NEXT: RETURN-AUTHOR — 작성 세션에서 판정08을 읽고 analysis/wip/solve-back-verifier_260910_info_ab50_newsession.md NEXT를 Q2 정책키·실제 입력 근거 단계로 갱신. 이 독립 세션은 후보 수정·운영 반영 금지.
Next verification: 판정08 §1-A의 manifest45/원천120 hash 대조 및 작성 소유권·충돌 쓰기 확인. 기존 작성 세션 가용성 미확인 시 NEW-CONTINUATION으로 같은 작성 책임 승계.
