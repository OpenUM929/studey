---
title: "결정요청 — PRD S1 렌더 규격 개정 + G2 실행 명령 신설 (Cycle-1)"
created: 2026-09-04
author: main-loop
type: decision-request
target: output/260903/260903_01_cycle1_prd.md  (16,935 B / 94eb2939d806c1a6, 승인본)
ruling_ref: output/260903/rev/260903_03_arbiter_ruling_cycle1_r3.md  (R1b·R3b approve)
---

# 0. 왜 상신하는가

승인된 PRD의 **수용기준 자체를 고쳐야 하는 사유**가 첫 유닛 실행에서 나왔다.
원칙 12-a에 따라 실행 레인은 자기 자를 고치지 않는다. 우회하지 않고 판정을 요청한다.

# 1. 관측 사실 (실측, 판단 아님)

`EX-social-20261M` 정제가 끝났고 **기계 게이트 5축이 전부 통과**했다.

```
pages=8   unit_files=3   typeid_hits=0   present=3 empty=0      (PRD §3 S2 펜스 블록 문면 그대로)
```

**그런데 유닛은 쓸 수 없다.** 인쇄 선언 27문항(선택형 24 + 단답형 3) 대비 전사 확인 20문항이고,
그중 절단 없이 완결된 것은 **9문항**이다. `verify_log.tsv`에 `unreadable` 18행이 명시돼 있다.
PRD §3의 「G1~G5 중 하나라도 어긋나면 ▲ blocked」에 따라 이 유닛은 **blocked**로 판정했다.

## 1-A. 원인은 원본 결락이 아니라 렌더다 (메인 루프 직접 실측)

| 축 | 실측값 | 재현 |
|---|---|---|
| 임베드 스캔 해상도 | **2150 x 3035 px, mode=L → 300 dpi** | `fitz.open(pdf).extract_image(xref)` |
| 정제본 PNG | **1149 x 1622 (dpi 160)** — 선형 53% | `PIL.Image.open(corpus/_images/.../p01.png).size` |
| `page.rotation` | **0** (8쪽 전건) | `[p.rotation for p in fitz.open(pdf)]` |
| 실제 콘텐츠 방향 | **90도 회전** — `rotate(-90, expand=True)`로 정립 | 육안 판독 |
| 지면 구성 | 회전 후 가로 지면 + 전폭 머리말 + **2단** | 육안 판독 |
| 거터 위치 | 가장 흰 열 **1510 / 3035** (중앙 1517) — 완전 백색 열 0개(스큐) | 열별 평균 밝기 |
| 복구 검증 | 네이티브 추출 → `rotate(-90)` → **겹침 180px 2단 분할** 후 p03 양쪽 판독 | 문항 5·7이 도표·`<보기>`·선택지까지 **온전히 읽힘** |

→ 「문항 6·8·16·18·21·23·단답형3 미발견」은 **둘째 단이 판독 불가였던 것**이다.
→ 전사자의 관측(회전·2단·절단)은 정확했다. **내가 `page.rotation=0`만 보고 「회전 아님」이라 한 것이
오판이었고, 이 문서에서 정정한다.**

## 1-B. 게이트가 통과시킨 이유 — G2가 실행 블록에 없다

PRD §3에서 G2(문항 수)는 **산문 절로만** 존재하고 실행 명령이 없다. 기계 블록은 G1·G3·G4·G5만
낸다. 그래서 선언 27 대 전사 20이 기계적으로 걸리지 않고, 사람이 산문을 읽어야만 걸린다.

이것은 원칙 11-a가 경고한 형태다 — **분모를 산출물에서 잡으면 잘려나간 산출물이 만점을 받는다.**
원칙 11-a의 근거 사건(`SUP-math2-2026` 답지 v2가 93문항 중 #3-11에서 멈췄는데 자기 점검과 맹목
풀이 게이트가 둘 다 「오류 0」 보고)과 **동형**이다. 이번에는 전사자가 정직하게 `unreadable` 18행을
남겨서 사람이 알아챘을 뿐, 게이트가 잡은 것이 아니다.

# 2. 판정 요청

## A1 — S1 렌더 규격을 개정하는가?

현행 PRD S1: `corpus/_images/<ID>/pNN.png     PyMuPDF dpi=160, 전 쪽`

제안: **스캔 원본에 한해** 아래로 대체한다(HWP 유래 유닛은 현행 유지).

```python
# 1) 임베드 이미지를 네이티브 해상도로 추출 (재샘플링 없음)
px = doc.extract_image(page.get_images(full=True)[0][0])
# 2) 콘텐츠 회전 정규화 — page.rotation 이 0이어도 콘텐츠는 돌아가 있을 수 있다
im = Image.open(io.BytesIO(px['image'])).rotate(-90, expand=True)
# 3) 2단이면 겹침을 두고 분할 (스큐 때문에 50/50 고정 분할은 내용을 자른다)
w, h = im.size; ov = 180
im.crop((0, 0, w//2+ov, h)).save('.../pNN_L.png')
im.crop((w//2-ov, 0, w, h)).save('.../pNN_R.png')
```

- 회전각·단 수·겹침은 **유닛마다 실측해서 정한다**(고정 상수 아님). 회전 없음·1단이면 그대로 둔다.
- 파일명이 `pNN.png`에서 `pNN_L/R.png`로 늘어나면 **G1 기대표의 분모가 깨진다** — A2와 함께 봐야 한다.
- `meta.yml: render_dpi`에는 네이티브 실효 dpi(이 유닛은 300)를 적는다.

verdict: {approve | revise-required | reject}

## A2 — G1 기대표를 어떻게 하는가? (A1 승인 시에만)

분할하면 `EX-social-20261M`의 PNG는 8장이 아니라 16장이 된다. 선택지:
(가) G1 기대값을 `쪽수 x 단수`로 바꾼다 (나) 분할본을 `corpus/_images/<ID>/split/`에 두고 G1은
`pNN.png` 8장 기준을 유지한다 (다) 다른 안.

verdict: {approve (가) | approve (나) | 다른 안 제시}

## A3 — G2를 실행 명령으로 승격하는가?

제안: 전사자가 `meta.yml`에 이미 적는 `items`(선언 합계)와, transcript에서 센 실제 전사 문항 수를
대조하는 명령을 S2 펜스 블록에 추가한다. 다만 **transcript에서 문항 수를 세는 결정론적 방법을
내가 확정하지 못했다** — 문항 머리 표기가 유닛마다 다를 수 있다. 명령 형태의 확정을 요청한다.

verdict: {approve | revise-required | reject}

## A4 — `EX-social-20261M`의 기존 산출물을 어떻게 하는가?

원칙 3(append-only)과 `type-extractor` 정의의 「Run once and stop / 정정은 NEW `corrected` 행으로」가
걸린다. 선택지: (가) 기존 4종을 남기고 `corrected` 행을 append하며 transcript를 갱신
(나) 유닛을 폐기하고 재생성 (다) 다른 안.

verdict: {approve (가) | approve (나) | 다른 안 제시}

# 3. 범위 밖

- 나머지 9유닛의 정제 — A1~A4 확정 후 순차 진행
- S3 분류 · S5 반영
- 전사 내용의 정오 — 이 문서는 렌더·게이트 규격만 다룬다

# 4. 실행 레인 자기보고

- 이 문서는 **개정안 제시**이고 반영이 아니다. PRD는 `94eb2939d806c1a6` 그대로 무접촉이다.
- 내 오판 1건을 위 1-A에 명시했다(`page.rotation=0` → 「회전 아님」).
- 커밋 없음(HEAD `941af21`).
