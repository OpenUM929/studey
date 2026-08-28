---
title: "Ruling — QUIZ_STANDARD revision (decision 260825_12 / report 260825_06)"
source: analysis/rev/260825_12_quiz_standard_decision.md
created: 260825
author: rev-arbiter (Claude Code, Opus — tier-3)
status: approved in part — QS-4 rejected (finding overturned)
---

# Ruling 12 — `docs/QUIZ_STANDARD.md`

## Independent verification performed

QS-1, QS-2, QS-3 re-verified directly against `docs/QUIZ_STANDARD.md` (140 lines),
`docs/DATA_STANDARD.md` §1.3/§5.1/§5.8/§6, and the real paper. All three stand:
the spec's §1 block defines only `[유형ID·Tier]`; its 과목 판별 section names only
영어/통합과학; its §2 schema has 12 fields with no `df`/`aux_types` and no set-level
frontmatter contract.

## QS-4 is factually wrong — overturned

Both tiers asserted "CODE_REGISTRY registers no `T-`/`W-` prefix." The registry does:

> `analysis/catalog/CODE_REGISTRY.md` §1 —
> `| T / W | catalog/english.md | T=독해·문법(Text) 1~12, W=작문(Writing) 1~4 — 한 파일 안 두 계열 | 16 유형 | 동결 |`

and §3 maps `english → T·W`. `T-01` exists at `analysis/catalog/english.md` L17 and
`W-01` at L113. Furthermore the QUIZ_STANDARD example is an **English** paper
(`output/260714/공통영어1_모의문제_25.md`, `"subject": "english"`), so `T-01·T2` and
`W-01·T3` are the *correct, registered* IDs for that example — not placeholders.

CODE_REGISTRY §2 already carries the disambiguation rule for the visual collision the
finding worried about: *"영어 독해 `T-01` vs 난이도 Tier `T2` — 하이픈+2자리 번호면 유형ID,
아니면 티어."*

Replacing them with `SM`/`SM2` IDs, as CB4 proposes, would put **공통수학 type IDs into a
공통영어 example** — a worse document than the one being fixed.

## Rulings

| question | ruling | evidence | note |
|----------|--------|----------|------|
| QS-1 | **approve** | spec §1 vs 모의40 body tags | see ruling 07 finding A1 — the tag standard must also carry the **함정 E-code** slot, which report 06 did not know about. Any §1 rewrite that omits E-codes is incomplete |
| QS-2 | **approve** | spec §1 과목 판별 vs DATA_STANDARD §5.8 (7 codes) | |
| QS-3 | **approve** | spec §2 schema vs DATA_STANDARD §5.1/§5.8/§6 | |
| QS-4 | **reject — finding overturned** | CODE_REGISTRY §1 registers `T`/`W` → english.md; §3 maps english → T·W; english.md L17 `T-01`, L113 `W-01`; §2 already resolves the T-01/T2 collision | the "unregistered prefix" premise is false; both tiers missed §1 of the registry |
| Q4 REV_LOG TSV conversion | **(a) keep MD** | DATA_STANDARD §0 places 검토서(rev/) and 지침 in the human-curated Markdown layer; REV_GUIDE §4 fixes the MD table; no tool currently reads REV_LOG | Concurs with t2. Revisit only when a tool actually needs to aggregate it; conversion would also require REV_GUIDE §4 amendment plus a migration plan for append-only rows and the `## output/YYMMDD` section comments |
| Q5 `scope_confirmed` default false | **uphold** | 모의40 has no frontmatter and declares ⚠️ 범위 미확정 in its own preamble (L4) — default-false reproduces the true state | fail-safe direction; default-true would let an unconfirmed scope pass silently, defeating 원칙 7 |
| CB1 tag standard section | **approve with amendment** | | must define **four** slots — 주유형 · Tier · DF목록 · 함정 E코드 — plus the aux form, and must state the tolerance rule: unknown `·`-separated tail tokens are preserved, never dropped. Use the tested RE from ruling 07 |
| CB2 subject mapping via DATA_STANDARD §5.8 | **approve** | | reference §5.8 rather than restating the table, so the two documents cannot drift |
| CB3 schema + frontmatter contract | **approve** | | add `df[]`, `aux_types[]`, and (per CB1) `traps[]`/`tagExtra[]`; add the set-meta block (`set_id`, `subject_code`, `unit`, `scope_confirmed`, `intended_use`) to the §1 input order and to `sources[]` |
| CB4 replace T-01/W-01 with SM/SM2 | **reject** | QS-4 overturned above | **Instead**: keep `T-01`/`W-01` and add a one-line cross-reference — "예시 ID는 `analysis/catalog/CODE_REGISTRY.md` §1 등록 접두어다(영어 T/W). Tier 코드 `T2`와의 구분법은 §2." That fixes the only real residue (a reader cannot tell the example is registered) at a fraction of the cost |
| CB5 REV_LOG TSV | **out of scope — no action** | Q4 = (a) | stays registered as an exception in DATA_STANDARD §7 |

## Condition on application

CB1 and ruling 07's CB1 target the same standard. Apply the **spec** (this ruling) and the
**parser** (ruling 07) in one change set and verify against the same acceptance criterion:
40 problems / 40 typeId / 40 tier / 6 trap codes / 1 aux from 모의40.

## history
- 260825 arbiter ruling. QS-1~3 approved; **QS-4 overturned** — `T`/`W` are registered
  prefixes (CODE_REGISTRY §1) and `T-01`/`W-01` are the correct IDs for the spec's English
  example, so CB4 is rejected and replaced by a cross-reference line. CB1 approved with the
  함정 E-code slot added (ruling 07 finding A1). Q4 = keep MD, Q5 = uphold default-false.
