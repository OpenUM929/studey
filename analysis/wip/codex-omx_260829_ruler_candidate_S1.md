---
actor: Codex/OMX
task: ruler-candidate-S1
target: output/260829/ruler-candidate/
status: done
updated: 2026-08-29
exclusive_write_owner: Codex/OMX main loop
---

# 260829 ruler candidate S1 WIP

| no | 범위 | state | 산출물 | 비고 |
|---:|---|---|---|---|
| 1 | 동결 입력 13건·정본·개정 이력·write surface 검증 | done | 이 WIP | 13/13 bytes 및 SHA-256 앞 16자 일치; candidate 경로와 WIP는 착수 전 부재 |
| 2 | G1 span 생성기·candidate 수용기준 pilot | done | `gen_expected_ids.candidate.py`, `ACCEPTANCE_SCHEMA.candidate.md` | 결정론 SHA-256 일치; 22행·rule_a 22/22; shipped 대비 의미 차이 1/22 = W-04 44-48→44-49 |
| 3 | G2·G3 candidate 검사기 구현 | done | `check_experiment.candidate.py` | 원본 author 입력 exit 1; `umbrella_rows=2` 및 DIAG-U10/U11 검출; fixed 5..12 검사 없음; warnings는 `len(warnings)` 1곳에서 계산 후 최종 마커 전에 출력 |
| 4 | G4 11종 차등 자기시험 | done | `selftest.candidate.py` | baseline exit 0/failures 0/warnings 0; `detected=11 undetected=0 source_unchanged=True`, exit 0 |
| 5 | G5 generator 최대성 합성 fixture | done | `FIXTURES/` | 동일 `GEN-SHARED`를 singleton 2행으로 분할 시 exit 1, generator equivalence violation 1줄; 원본 참고 확장 16/6/9/1/22/0 |
| 6 | §6-d report·회귀·write-surface 검증 | done | `S1_REPORT.md` | input hash 13/13; report manifest 10/10; AST 3/3; catalog 131 exit 0; mastery 131 warnings 0 exit 0; diff-check exit 0; assurance는 타 소유 WIP 3건을 이름으로 출력하며 의도대로 exit 1 |
| 7 | 사용자 지시로 별도 40문항 authoring 시퀀스 착수 근거 기록 | done | `analysis/wip/codex-omx_260830_math2_novel_40.md` | **bounded parallel branch**: S1 candidate·S1_REPORT·동결 25파일·S2/S3/S4를 수정·승격하거나 현 ruler를 40문항 의미 판정에 소비하지 않는다. 이 WIP의 HOLD는 유지 |

NEXT: HOLD — 다른 신원·fresh-context S2 qualifier가 candidate와 이 report의 full hash를 동결하고 G1~G5를 재현한다. S1 작성자는 qualification·refreeze·measured run을 수행하지 않는다.
