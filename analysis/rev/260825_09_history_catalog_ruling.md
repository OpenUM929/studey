---
title: "Ruling — history catalog (decision 260825_09 / report 260825_03)"
source: analysis/rev/260825_09_history_catalog_decision.md
created: 260825
author: rev-arbiter (Claude Code, Opus — tier-3)
status: approved (with amendments)
---

# Ruling 09 — history catalog (`analysis/catalog/history.md`)

## Independent verification performed

t2 could only mark H4/H5/H6 PARTIAL ("encoding artifacts"). That diagnosis was wrong —
the extracted files are UTF-8 and read cleanly; what failed was the console codepage, not
the source. **All three are now hard-confirmed by direct reads:**

| finding | arbiter evidence |
|---|---|
| H4 | `2024/중간/한국사.txt` L170-172 — `다음 ㈎, ㈏ 시기 사이에 있었던 사실` with ㈎ 강감찬 상원수 / ㈏ 윤관 9성. **24중간**, not 24기말 |
| H5a | same file L164 — `고려시대 관리 선발 제도의 특징` [2.4점]. **24중간** |
| H5b | same file L179 — `고려 시대의 지방 행정 구역 … ㈎, ㈏` (5도·양계). **24중간** |
| H5c | `2024/기말/한국사.txt` **L40 `[4-5]`** — a explicitly numbered two-item set on ㉠(의정부서사제)/㉡(육조직계제); L44 = item 4 [3.7점], L50 = item 5 [3.8점]. The report's "24기말 Q4~5" is exact |
| H6a | 조광조 appears exactly once in the whole corpus: `2024/기말/한국사.txt` L75. **24기말**, not 2025 |
| H6b | 삼강행실도 is present at 24기말 L56-58 **by description, not by name** (`직제학 설순 … 충신·효자·열녀의 행실을 모아 편찬한 교훈서 … 언해본`). This is why keyword search failed for both tiers |
| H6c | 정효공주 = `2024/중간/한국사.txt` L155-157, a **선택형** item (`다음 중 ㉠의 인물에 관한 내용으로 가장 옳은 것은? [2.4점]`), not 서술형 |
| H7 | whitespace-normalised counts, `2025/기말/한국사.txt`: 강화도조약 1 · 갑신정변 1 · 동학 4 · 을사 5 · 의병 5 · 간도 2 · 흥선 2 · 대원군 3 · 규장각 1 — vs **고구려 0 · 신라 0 · 고려 1**. 25기말 is a modern-history paper |
| H1/H2 | headers: 24중간 `선택형 25, 서술형 4` · 24기말 `선택형 21, 서답형 5` · 25중간 `선택형 25, 서술형 4` · 25기말 `선택형 24, 단답형 6` |

**H1–H7 all stand, none merely partial.**

## Rulings

| question | ruling | evidence | note |
|----------|--------|----------|------|
| Q1 preamble style | **(a) per-round actuals** | four different structures (25/21/25/24 items; 서술형4 vs 단답형5 vs 단답형6) cannot be summarised into one pattern without losing the fact that finals stopped using 서술형 | Same principle as ruling 08/Q1: a compressed pattern sentence is what produced this class of error. Where a value is unmeasured, say unmeasured |
| Q2 E-6 (근대사) creation | **(b) minimal — 3~5 types + frequencies — but with a full item inventory appended** | 25기말 is an entire modern-history paper (24 selected + 6 단답); registering all 24 as types now would over-split (REV_GUIDE §2-b C: 5–12 types, no over-splitting), and history is not in the current 2학기 scope | Register 3~5 types **plus** a raw `## E-6 근거 문항 목록 (미유형화)` list of all 24 items so nothing is discarded (principle 3). Add a 미결 line: "E-6 유형화 완성 — 다음 갱신 주기". Prefix stays `F-` with the 최대번호 연장 rule; **never mint a new `F-nn` outside the existing maximum**, and cite it scoped as `한국사:F-nn` (CODE_REGISTRY §2, F is a dual-owner prefix) |
| Q3 time-range map L7 | **(b) corrected sentence — with a mandatory addition** | per-round counts: 24중간 고려 4·조선 0 / **24기말 고려 11·조선 11** / 25중간 고려 16·조선 9 / 25기말 근대 only | The option (b) sentence as drafted **omits 24기말 entirely**. It must read: "24중간 = 고대 중심 + 고려 도입 · **24기말 = 고려 후기~조선 전기** · 25중간 = 고려 후기~조선 초 · 25기말 = **근대사 단독**." Without 24기말 the map still has a hole |
| preamble 2026 병기 | **rule inherited from ruling 10 / Q1 — option (b), applied identically here** | identical `+ 2026 중간·기말(스캔, 학생본)` line in english.md L3, social.md L3, history.md L3 | Re-label as `참고 자료(미분석): 2026 중간·기말 스캔` — do not delete. See ruling 10 for the reasoning |
| P1 | **approve** (Q1 = (a) form) | headers | |
| P2 | **approve** | headers | wording as proposed: "중간 서술형 4문항(10점×4) / 기말 단답형 5~6문항(3~4점)" |
| P3 | **approve** (Q3 = (b) + 24기말 clause) | counts | |
| P4 | **approve — unconditional** | H4 hard-confirmed (L170-172) | drop the "teacher spot-check" condition t2 attached |
| P5 | **approve — unconditional** | H5a/b/c hard-confirmed (L164 · L179 · L40 `[4-5]`) | item numbers 4·5 for 의정부서사제/육조직계제 are directly printed in the source and may be written as exact numbers |
| P6 | **approve, with an item-number caveat** | H6a/b/c hard-confirmed for **round attribution** | Round attribution (2025 → 24기말) is certain. The **item numbers** "Q6" (삼강행실도) and "Q8" (조광조) are not printed in the extraction — the numbering was stripped. Either pin them first via the 정답_선택형 point-column alignment (the method used in ruling 08), or write the round without a number. Do **not** write an unverified number |
| P7 | **approve** (Q2 = (b) form) | H7 | includes 정조·규장각·세도정치 and the 독도·영토분쟁 axis; E-5 must stop being bounded at "전기" |

## Conditions on application

1. Every corrected frequency records round + item number, or round + "번호 미확정".
2. E-5's ★★★ importance grade currently rests on "2025 기말 핵심" — a false premise.
   Re-derive the star count from 24기말 evidence before writing it back.
3. Add a 금지·주의 line to the swapped types: "회차 귀속은 원문 직접 인용으로 확정할 것 —
   키워드 검색은 사료 제시형에서 실패한다(삼강행실도가 이름 없이 서술로만 제시된 사례)."
   This is the reusable lesson from H6b and belongs in the catalog per REV_GUIDE §7.

## history
- 260825 arbiter ruling. Upgraded H4/H5/H6 from PARTIAL to confirmed by direct source
  reads (the t2 "encoding artifact" diagnosis was a console-codepage artefact, not a file
  problem), so P4/P5 lose their teacher-spot-check condition. Ruled Q1=(a), Q2=(b) with a
  mandatory raw-item inventory, Q3=(b) **plus the missing 24기말 clause**. All 7 checkboxes
  approved; P6 carries an item-number caveat.
