---
actor: any
purpose: 리미트·세션 종료 후 재개 지점 (단일 정본)
set: SET-260908-info-26
updated: 2026-09-08
---

# RESUME — 정보 중간고사 세트 게이트

이 파일이 **유효한 재개 지점의 정본**이다.
`mainloop_260907_info_onboarding.md` 파일 끝의 `NEXT:` 줄은 S4 시절 것이고
260908에 폐기(취소선) 처리했다. 그 줄을 따라 S4를 다시 하지 마라.

## 현재 상태

| 단계 | 상태 | 근거 |
|---|---|---|
| S0~S7 | **완료** | 요구사항 1~5 산출물 존재. `build_catalog_index.py --check` = `[OK] 157 rows` |
| S8 맹목 풀이 | **미실시** | `_gate_state/s8.done` 없음 |
| S9 독립 품질감사 | **미실시** | `_gate_state/s9.done` 없음. S8 통과 전에는 시작 금지 |
| 세트 상태 | `검토필요` | `output/_index.md`. S8·S9 둘 다 PASS 전에는 승격 금지 |

**절대 하지 말 것**: S0~S7 재실행. 산출물이 이미 있고 append-only 이력이 남아 있다.
먼저 아래 «상태 판별»을 실행해 실제로 무엇이 남았는지 확인한 뒤에만 움직인다.

## 상태 판별 (재개 시 첫 명령)

```bash
cd /c/dev/study
ls analysis/wip/_gate_state/*.done 2>/dev/null || echo "게이트 미통과"
python tools/build_catalog_index.py --check
```

## 재개 명령

```bash
cd /c/dev/study
bash analysis/wip/_gate_runner.sh s8      # 먼저
bash analysis/wip/_gate_runner.sh s9      # s8.done 이 생긴 뒤에만 (스크립트가 강제)
```

러너는 **독립 배우**를 띄운다. cwd 를 `C:\dev\study` 로 두어야
`.claude/agents/` 의 `solve-back-verifier`·`item-quality-auditor` 가 등록된다.
`C:\dev\Nconnect` 에서 띄운 세션에는 등록되지 않으므로 그 레인이 열리지 않는다.

작성한 메인 루프가 자기 세트를 검증하면 안 된다 — CLAUDE.md 원칙 12
(피측정자는 자기 자를 소유하지 않는다). 자기 검산은 이미 했고, 그것은 이 게이트를
대신하지 못한다.

## 러너의 안전장치 (리미트 대비)

| 상황 | 동작 |
|---|---|
| 이미 통과한 단계 | `*.done` 확인 후 즉시 skip — 할당량 재소모 없음 |
| 실행 중 재호출 | lock 디렉터리로 거부(exit 2) — 이중 소모 없음 |
| 사용량 리미트로 죽음 | 로그에서 감지, `*.done` **안 만듦**, exit 10 → 다음 시도가 이어받음 |
| S8 미통과 상태의 S9 | 거부(exit 0) — 통과 안 된 세트의 후행 감사에 할당량 안 씀 |
| 보고서에 `VERDICT:` 없음 | 실패 처리, `*.done` 안 만듦 |

즉 **리미트에 걸려 죽어도 진행이 되돌아가지 않는다.** 다음 창에서 같은 명령을
다시 내면 끝난 단계는 건너뛰고 안 끝난 단계부터 이어간다.

## S8 맹목성 보장

`_redact_key.py` 가 세트에서 네 갈래 누설 경로를 제거한다:

1. `# 정답 · 해설 · 유형` 절 전체
2. `[근거: ...]` 태그 27개 (출처 문항을 알려줌)
3. 채점 조건 중 `오답` 을 언급하는 문장 (함정을 미리 알려줌 —
   예: "`b`를 7로 쓴 답은 오답이다" 는 E5 경계 오류 함정을 그대로 노출)
4. `**검증 상태**` 인용구 (작성자 자기 검산 결과)

fail-closed 다. 하나라도 살아남으면 아무것도 쓰지 않고 거부한다.
실측: 552행 · 26문항 보존 · 남은 `정답` 언급 4건은 전부 답 **형식** 제약(순서·부분점수)뿐.

## 통과 후 (S10 승격)

S8·S9 보고서가 **둘 다 `VERDICT: PASS`** 일 때만:

1. `output/_index.md` 26행 상태 `검토필요` → `배포가능`
2. 세트 frontmatter `gate_status`·`quality_audit` 를 실제 실행 결과로 교체
3. WIP S8·S9 행을 `done` 으로, 재개 기록 추가
4. 편집은 전부 `tools/textpatch.py` (원칙 12-b)

`FAIL` 이 하나라도 나오면 승격하지 말고, 지적된 문항을 재설계한 뒤
**S8부터 다시** 돌린다(`*.done` 삭제). 검토와 수정은 분리한다(원칙 8).

## 미해소 발견 (승격과 무관, 별건)

- `tools/build_corpus_unit.py:68` `RE_ID` 가 DATA_STANDARD §1.3보다 좁아
  `SUP-info-2026-01`·`SUP-math2-2026` 을 거부한다. 260907 패턴 개정 이전부터의 불일치.
- `tools/build_catalog_index.py` write 모드 요약이 `per_subj` 를 `subject_code` 가 아닌
  `type_id` 로 집계한다.
- `EX-info-20252F`(기말) 미분류 — `info.md` 에 `scope: partial` 로 명시됨.
