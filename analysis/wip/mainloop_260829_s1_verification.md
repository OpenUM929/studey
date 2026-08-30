---
actor: main-loop
task: s1_verification
target: "output/260829/ruler-candidate/ (Codex/OMX S1 산출물) 독립 재현 + S2 회람 작성"
status: done
updated: 260829
---

# WIP — S1 candidate 독립 재현 및 S2 회람 발신

역할: 나는 **검증자 겸 회람 발신 주체**다. candidate 파일과 S1_REPORT.md는 Codex/OMX 소유이므로
원칙 8에 따라 **직접 수정하지 않는다.** 발견 사항은 S2 회람의 unit과 승인 요청 체크박스로만 낸다.

| no | 범위 | state | 산출물 | 비고 |
|----|------|-------|--------|------|
| 1 | candidate 11파일 bytes·SHA-256 독립 산출 | done | — | Codex 신고값과 11/11 일치. 이전 라운드의 `__pycache__/` 잔여물 소멸 확인 |
| 2 | G1 재실행 | done | — | `deterministic=True` `rows=22` `rule_a=22`; 7열 diff vs shipped = W-04 1행(`44 48`→`44 49`) |
| 3 | G2·G3 재실행 | done | — | exit 1 · `umbrella_rows=2 ids=DIAG-U10,DIAG-U11` · `failures=6` · `warnings=2`; `literal_zero_prints=0`; `:452 print(f"warnings={len(warnings)}")`; `5 <=`/`<= 12`/`== 16` grep 0건 |
| 4 | G4 재실행 | done | — | `detected=11 undetected=0 source_unchanged=True` exit 0. 260828 미검출 3종(`report_mojibake`·`ruler_edit`·`schema_ruler_edit`) 전부 검출 |
| 5 | G5 재실행 | done | — | `FAIL: generator equivalence violation: generator_id=GEN-SHARED split across groups=SPLIT-A,SPLIT-B` exit 1 |
| 6 | 동결 입력 재해시 | done | — | **Codex 신고 목록 13건 기준으로는 13/13 일치**였으나 슬라이스 10에서 누락 1건이 드러나 **정정 후 14/14**. `git status` — corpus·output/260828 무수정. `analysis/REV_GUIDE.md`의 ` M`은 내 §6-d 개정분이며 해시는 동결값 `c634a792…`와 동일 |
| 7 | **W-04 분쟁 전수 폐쇄** | done | — | **신규 발견**. 아래 별도 절 |
| 8 | S1_REPORT 결함 3건 식별 | done | — | 아래 별도 절. Codex 소유이므로 승인 요청으로만 제출 |
| 9 | S2 회람 작성·발신 | done | 대화창 `[CC 회람] 260829_03` | Codex 초안은 규격 ① 위반(실행 레인이 자기 자격심사 질문지를 설계)이므로 메인 루프가 재작성 |
| 10 | **§6-d 직접경로 폐쇄 검사** | done | — | **신규 발견 D4**. candidate 코드의 경로 리터럴 전수 추출 결과 `AUTHOR_REPORT_260828.md`가 게이트에 실제 소비되는데 동결 목록에 없었다. 아래 별도 절 |
| 11 | 슬라이스 6·8 정정 반영 | done | 이 WIP | Codex 정정 감사(260829)가 이 WIP의 `13/13` stale 표기를 지적 — 배타 소유자인 내가 반영. 동결 기준은 **정정된 25건 manifest**(기존 14 + candidate 11)이며 이 WIP가 아니다 |

## 슬라이스 7 — W-04 전수 폐쇄 (§6-d closure)

Codex도 나도 종전에는 "W-04 1행이 shipped와 다르다"까지만 적고 **어느 쪽이 옳은지 판정하지
않았다.** shipped 22행 전수를 모집단으로 돌린 결과:

```
reproduce:
python -X utf8 -c "from pathlib import Path;
lines=Path('corpus/EX-math2-20252M/transcript.md').read_text(encoding='utf-8-sig').splitlines();
rows=[l.split(chr(9)) for l in Path('output/260828/diagnostic/math2-method-comparison/codex-team/EXPECTED_ITEM_IDS_260828.tsv').read_text(encoding='utf-8-sig').splitlines()[1:] if l.strip()];
print([(r[0],int(r[5])) for r in rows if lines[int(r[5])-1].strip()!=''], len(rows))"

측정:
  shipped 22행 중 end_line이 공백행인 행 = 20/22
  비공백 예외 2건 = W-04(end=48, '구하시오.') · S-15(end=119, '| ㅁ. f(y-2, x)=0 |')
  S-15의 다음 줄 120 = '## 16.'  -> 후행 공백행이 애초에 없음(구조적 강제, 예외 아님)
  따라서 진짜 예외 = W-04 단독 1/22
  W-04 주변: 44='## 4.' / 45-48=본문 / 49=공백 / 50='# 단답형 문항'
```

판정: **shipped의 정상 관행은 후행 공백행 포함(20/22)이고 W-04만 혼자 잘렸다.**
즉 shipped `EXPECTED_ITEM_IDS_260828.tsv`의 W-04 행은 파서 산출이 아니라 **손수정된 행**이며,
이것이 260828 감사 F9(같은 자 파일 안에 규칙 2종 공존)의 물증이다.
candidate가 이 행을 FAIL로 잡는 것은 결함이 아니라 정확한 동작이다.
이 폐쇄 계산은 `S1_REPORT.md`에도 `260829_01`에도 없었다.

## 슬라이스 8·10 — S1_REPORT.md 결함 4건 (Codex 소유, 승인 요청 대상)

- **D1 (차단)** `S1_REPORT.md:126` `sha256_A=fe10041d1d0fe2a714b13a1805388c7f9e00a97f77552c11ef4a4738daf383af`
  는 PowerShell `Out-File -Encoding utf8` 캡처(BOM·CRLF 포함)의 해시다. 같은 명령의 원시 stdout
  해시는 `b366a066f814d755498f7910cb3f0003cebde63a753bacfc45b4820ffd027a1a`다. §6-d (2)의
  `measured` 열은 리터럴이 `reproduce:` 명령으로 재현될 것을 요구하므로, 캡처 방식에 의존하는
  이 리터럴은 재현 불가다. 도구는 결정론적이며 결함은 **보고서 증거 표기**에 있다.
- **D2** `S1_REPORT.md:226-227` — fixture `missing_id`는 `generator equivalence violation:
  generator_id=DIAG-G08`로, `types_undercount`는 `missing_generators=BLOCKED-S17`로 잡힌다.
  `undetected=0`은 유효하나 **이름이 가리키는 검출기의 생존은 2/11에서 증명되지 않는다**
  (원칙 12-d). §3 follow-up에 누락.
- **D3** `selftest.candidate.py`의 `ruler_edit` fixture는 기대 자를 **같은 생성기로 재생성해**
  대조하므로 "손대지 않았음"만 증명하고 "규칙이 옳음"은 증명하지 못한다. 생성기 자체를 재는
  독립 오라클이 없다 — 슬라이스 7의 20/22 전수 통계가 그 오라클이다.
- **D4 (차단)** §6-d (1) 1번 **직접경로 폐쇄 의무 위반**. `check_experiment.candidate.py:434`와
  `selftest.candidate.py:115`가 `AUTHOR_REPORT_260828.md`를 경로로 지목하고 게이트가 실제로
  읽는데, `S1_REPORT.md` §1.1 동결 표 13건에 없었다. 실측값:
  `output/260828/diagnostic/math2-method-comparison/codex-team/author/AUTHOR_REPORT_260828.md`
  = 16068 B / `291c490d4c498822bf0d2d87003257188f0c9a0abe931d4be3e7a03bfdacd08a` (role: evidence).
  **이것은 260828 F10과 같은 패턴의 재발** — 동결 목록을 피측정 레인이 작성하면 자기 게이트가
  읽는 파일이 목록에서 빠진다. §6-d의 폐쇄 의무가 존재하는 이유가 그대로 실증됐다.
  ```
  reproduce:
  grep -n -oE '"[^"]*(/|\.py|\.md|\.tsv|\.yml)[^"]*"' \
    output/260829/ruler-candidate/check_experiment.candidate.py \
    output/260829/ruler-candidate/selftest.candidate.py
  ```
  Codex 정정 감사(260829)가 위 bytes·SHA-256과 소비 위치 2곳을 독립 재현했다.

## 동결 기준 (정정본)
S2의 기준은 **이 WIP가 아니라 `[CC 회람] 260829_03`의 25건 manifest**다 —
기존 14건(위 13건 + `AUTHOR_REPORT_260828.md`) + candidate 11건.
Codex 정정 감사가 25/25 파일·해시 존재를 확인했고, D1의 원시 stdout 해시
`b366a066f814d755498f7910cb3f0003cebde63a753bacfc45b4820ffd027a1a`도 독립 재현됐다.

## 차단 조건
- candidate 11파일·`S1_REPORT.md` 무수정 (Codex/OMX 배타 소유, 원칙 8).
- 동결 입력 14건 무수정 (원칙 12) — `AUTHOR_REPORT_260828.md` 포함(D4 정정 반영).
- `analysis/wip/codex-omx_260829_ruler_candidate_S1.md` 무수정·무삭제 (규격 ②).
- 커밋·푸시 없음.

## 검증 명령
```
python -X utf8 output/260829/ruler-candidate/gen_expected_ids.candidate.py --emit   # 22행 + header
python -X utf8 output/260829/ruler-candidate/selftest.candidate.py                  # detected=11 undetected=0, exit 0
python -X utf8 output/260829/ruler-candidate/check_experiment.candidate.py --types output/260828/diagnostic/math2-method-comparison/codex-team/author/types.tsv --items output/260828/diagnostic/math2-method-comparison/codex-team/author/items.tsv   # exit 1, umbrella_rows=2
```

NEXT: (완료 — 슬라이스 1~11 전건 done. 다음 라운드는 외부 fresh-context `rev-arbiter`의
S2 qualification 회신 `output/260829/ruler-candidate/S2_QUALIFICATION.md` 수령 시 개시.
그때 기준은 `[CC 회람] 260829_03`의 25건 manifest이며, 회신 전에는 S1 수정·qualification
자가판정·refreeze·S4를 수행하지 않는다.)
