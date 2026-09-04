# 개행 코드(CRLF/LF) 정책 및 전수 수정 절차 — v1.0 (260902)

> **이 문서의 독자**: 이 저장소의 개행 문제를 **전수 수정**할 작업자(저성능 AI 포함).
> 판단을 요구하지 않도록 **정확한 규칙·명령·검증 기준**만 적었다. 규칙에 없는 상황을 만나면
> **고치지 말고 §7 보고 양식으로 올린다.**
> **선행 필수**: §2를 읽지 않고 §5를 실행하지 마라. 이 저장소에서 개행은 **고정 속성이 아니다.**

---

## §1 현재 상태 (260902 실측)

```
git config core.autocrlf = true
.gitattributes           = 없음
```

| 구분 | 파일 수 |
|---|---|
| LF 전용 | 362 |
| CRLF 전용 | 272 |
| **MIXED (한 파일에 두 방식 혼재)** | **36** |
| 개행 없음 | 2 |

확장자별 분포(측정): `.md` LF 242 / CRLF 158 / **MIXED 28**, `.tsv` LF 29 / CRLF 23 / **MIXED 5**,
`.txt` CRLF 61 / LF 30, `.py` CRLF 14 / LF 10, `.yml` LF 21 / CRLF 3 / **MIXED 3**,
`.json` LF 26 / CRLF 3, `.html` CRLF 9 / LF 2, `.js` LF 2 / CRLF 1.

**이미 수리된 것 (260902, 이 문서 작성 시점)** — TSV 원장 5종만 LF로 통일:

| 파일 | before | after |
|---|---|---|
| `corpus/HARVEST_LOG.tsv` | `8f2aa46e3906f607` | `028f8195193452ae` |
| `corpus/EX-english-20252M/verify_log.tsv` | `2178cc7a8096354a` | `f61411d17ee12b02` |
| `corpus/EX-math2-20252M/verify_log.tsv` | `b22117449bb59b4f` | `ee88f031bf76d870` |
| `corpus/EX-science-20252M/verify_log.tsv` | `b536b724e321e8d0` | `f6e68ed4db194490` |
| `corpus/EX-social-20252M/verify_log.tsv` | `c21370b90cdd7acb` | `31430ad443511500` |

검증: 행 수 불변, 열 수 분포 불변, `CR=0`. **나머지 31개 MIXED 파일은 미수리** — §5 대상이다.

---

## §2 원인 — 반드시 먼저 이해할 것

**`core.autocrlf=true`는 체크아웃 때 LF→CRLF, 커밋 때 CRLF→LF로 바꾼다.** 그래서:

- **커밋 후 체크아웃된 파일** → 디스크에서 **CRLF**
- **로컬에서 새로 만들거나 덧붙인 내용** → 만든 도구의 기본값(대개 **LF**)

여기에 쓰는 주체가 여럿이다(git 체크아웃·Codex/OMX = CRLF 경향, Python `newline=""`·에디터 = LF).
CRLF 본문에 LF 행이 덧붙으면 그 파일이 **MIXED**가 된다. 36개가 그렇게 생겼다.

> ### ⚠️ 가장 중요한 사실 — 개행은 고정 속성이 아니다
> `autocrlf=true` 아래에서는 **오늘 LF인 파일도 커밋 → 체크아웃을 거치면 CRLF가 된다.**
> 따라서 **「이 파일은 LF였다」는 기억·메모·문서 기재는 시간이 지나면 저절로 거짓이 된다.**
> 파일별 개행을 표로 적어 관리하려는 시도는 전부 실패한다. 하지 마라.
>
> **그리고 `grep`으로 CR을 세지 마라.** `grep -c $'\r' <file>` 은 **CRLF 파일에서 0을 반환한다**
> (grep이 매칭 전에 CR을 떼기 때문). 「LF다」라는 **거짓 통과**가 나온다. 실제 이 저장소에서
> 이 오판이 하루에 3회 재발했다. 판별은 반드시 **바이트 단위**로 한다(§4).

---

## §3 정책 — 지켜야 할 불변식

우선순위 순. 위쪽이 아래쪽을 이긴다.

1. **P1 — 한 파일 안에서 개행은 하나여야 한다 (MIXED 금지).**
   이것이 유일한 강제 불변식이다. CRLF 파일인지 LF 파일인지 자체는 **문제가 아니다.**
2. **P2 — `.tsv` 원장은 LF로 통일한다.**
   MIXED TSV에서는 마지막 필드 끝에 `\r`이 값으로 남아 `actor` 가 `"main-loop\r"` 로 읽힌다.
   비교·집계가 조용히 어긋나므로 데이터 무결성 문제다.
3. **P3 — 그 밖의 파일은 MIXED만 해소하고, 다수파 개행으로 통일한다.**
   CRLF가 많으면 CRLF로, LF가 많으면 LF로. **파일의 기존 성격을 바꾸지 않는다.**
4. **P4 — 편집은 `tools/textpatch.py`로 한다.**
   앵커를 LF로 정규화해 대조하고 원본 개행·BOM으로 되쓰므로 **개행 판별이 불필요**하다.
   손편집·`sed` 직접 치환은 MIXED를 새로 만든다. 금지.
   **주의 — 이 도구는 MIXED 파일 쓰기를 기본 거부한다**(`PatchError`). MIXED 파일을 한 방식으로
   되쓰면 반대 방식이던 **모든 줄이 함께 바뀌어**, 앵커 1곳 편집이 파일 전체 재작성이 되기 때문이다.
   그 정규화를 의도한 경우에만 `allow_mixed=True`를 넘기고 그 diff를 책임진다.
   **그래서 §5의 전수 수정 스크립트는 textpatch가 아니라 바이트 입출력을 직접 쓴다** — 정규화가
   목적인 작업이므로 도구의 거부가 오히려 방해가 된다. 편집과 정규화는 다른 작업이다.
5. **P5 — 개행 정규화는 내용을 바꾸지 않는다.**
   행 수·열 수·필드 값(꼬리 `\r` 제거 제외)이 하나라도 달라지면 **되돌리고 §7로 보고**한다.

> **P1이 근본 해결이 아니라는 점을 알아둘 것.** 디스크 정규화는 `autocrlf=true` 아래에서
> **다음 체크아웃에 되돌아간다.** 항구적 해결은 `.gitattributes` 도입이며 **아직 승인되지 않았다**
> (§8). 그때까지 재발을 실제로 막는 것은 **P4(도구 사용)** 이고, 전수 수정은 현재 손상 제거가 목적이다.

---

## §4 판별 방법 (이것만 쓸 것)

```bash
python -c "import io,sys; d=io.open(sys.argv[1],'rb').read(); c=d.count(b'\r\n'); l=d.count(b'\n')-c; r=d.count(b'\r')-c; print('crlf',c,'lf',l,'cr-only',r,'bom',d[:3]==b'\xef\xbb\xbf')" <파일>
```

- `crlf>0 and lf>0` → **MIXED, 수정 대상**
- `cr-only>0` → 단독 CR. 드물지만 존재하면 §7로 보고(자동 처리하지 마라)
  - **실측 사례**: `analysis/REV_LOG.md` 는 `crlf=0 lf=132 cr-only=2` 다. MIXED가 아니므로
    §5 대상이 **아니고**, 셀 본문 안에 CR 2개가 박혀 있는 상태다. 자동 제거하지 말고 보고만 한다.
- `bom True` → BOM 파일. **BOM은 반드시 보존한다**(일부 TSV가 BOM 필수)

**금지**: `grep -c $'\r'`, `file` 명령, 에디터 표시줄, 「전에 봤을 때 LF였다」는 기억.

---

## §5 전수 수정 절차

### §5-1 대상과 제외

**대상 확장자**: `.md .py .tsv .yml .yaml .json .js .html .txt`

**제외 (건드리지 마라)**:
- `.git/`, `node_modules/`, `__pycache__/`
- 바이너리 전부 — `.png .pdf .hwp .doc .docx .xlsx .zip`
- `origin_data/` **전체** — 원본 자료는 불가침
- `corpus/_images/` — 렌더 산출물
- MIXED가 아닌 파일 — **CRLF 전용·LF 전용 파일은 그대로 둔다** (P3)

### §5-2 실행 (1파일 = 1단위, 체크포인트 필수)

각 파일마다 아래를 **순서대로** 수행한다.

```python
import io, hashlib, collections

def fix(path, is_tsv):
    raw = io.open(path, "rb").read()
    bom = raw.startswith(b"\xef\xbb\xbf")
    body = raw[3:] if bom else raw
    txt = body.decode("utf-8")

    crlf = txt.count("\r\n"); lf = txt.count("\n") - crlf
    if not (crlf and lf):
        return "skip: not mixed"

    before = hashlib.sha256(raw).hexdigest()[:16]
    rows_b = txt.split("\n")

    # 목표 개행: TSV는 무조건 LF(P2), 그 외는 다수파(P3)
    target = "\n" if is_tsv else ("\r\n" if crlf >= lf else "\n")

    flat = txt.replace("\r\n", "\n").replace("\r", "")   # 꼬리 단독 CR 제거
    rows_a = flat.split("\n")

    # --- P5 무손상 검증: 통과 못 하면 쓰지 않는다 ---
    assert len(rows_b) == len(rows_a), "행 수 변동"
    assert [r.rstrip("\r") for r in rows_b] == rows_a, "내용 변동"
    if is_tsv:
        cb = collections.Counter(r.count("\t") for r in rows_b if r.strip())
        ca = collections.Counter(r.count("\t") for r in rows_a if r.strip())
        assert cb == ca, "열 수 분포 변동"

    if not flat.endswith("\n"):
        flat += "\n"                      # 파일 끝 개행 보장 (§6 사고 예방)
    out = flat.replace("\n", target) if target == "\r\n" else flat
    data = (b"\xef\xbb\xbf" if bom else b"") + out.encode("utf-8")
    io.open(path, "wb").write(data)
    return "%s -> %s" % (before, hashlib.sha256(data).hexdigest()[:16])
```

- **`assert`가 하나라도 걸리면 그 파일은 쓰지 말고 §7로 보고한다.** 우회 금지.
- 파일 1개를 끝낼 때마다 WIP에 `경로 · before해시 · after해시 · 행수 · 판정` 한 줄을 남긴다
  (`CLAUDE.md` 규격 ②).

### §5-3 수용기준 (fail-closed, `CLAUDE.md` 원칙 11)

작업 종료 시 아래를 실행하고 **출력을 그대로 첨부**한다.

```bash
python -c "
import io,os
mixed=[]
for root,dirs,files in os.walk('.'):
    dirs[:]=[d for d in dirs if d not in ('.git','node_modules','__pycache__')]
    if 'origin_data' in root or '_images' in root: continue
    for f in files:
        if not f.lower().endswith(('.md','.py','.tsv','.yml','.yaml','.json','.js','.html','.txt')): continue
        p=os.path.join(root,f); d=io.open(p,'rb').read()
        c=d.count(b'\r\n')
        if c and d.count(b'\n')-c: mixed.append(p)
print('MIXED remaining =', len(mixed))
[print(' ',m) for m in mixed]
"
```

**통과 기준**: `MIXED remaining = 0` **이고** 경고 0줄 **이고** exit 0.
`[OK]` 같은 문자열 하나로 통과를 선언하지 마라. **exit code를 파이프 뒤에서 읽지 마라**
(`cmd | grep x; echo $?` 는 grep의 코드다).

추가로 원장 무결성을 확인한다:

```bash
python tools/check_assurance_contract.py     # 신규 FAIL 0건이어야 한다
python tools/build_catalog_index.py --check  # [OK] ... 경고 0줄 · exit 0
```

---

## §6 수리 완료 — 개행과 별개인 실제 손상 1건 (260902 승인·반영)

**같은 계열의 사고이나 내용 수정이므로 이 문서의 §5로 처리하지 마라.**

`corpus/EX-english-20252M/verify_log.tsv` 의 **4행이 15열**이다(정상은 8열). 원인은 개행이 아니라
**파일 끝 개행 없이 append**해서 두 논리 행이 붙은 것이다:

```
... high <TAB> Codex/OMX2026-08-31 <TAB> classify <TAB> ...
                        ^^^^^^^^^^^^^^^^^^ 여기서 갈라져야 한다
```

앞 행의 `actor` 값 `Codex/OMX` 와 뒤 행의 `date` 값 `2026-08-31` 이 붙었다.

**수리 방법(승인 후 실행)**: `Codex/OMX` 와 `2026-08-31` 사이에 개행을 넣어 8열 2행으로 분리.
다른 필드는 손대지 않는다. 분리 후 검증: 해당 파일 전 행이 8열, 행 수 7→8.

- [x] **승인·반영 완료 (260902, 사용자 승인)** — `f61411d17ee12b02` → `9710e9bc775acd29`.
      쓰기 전 무손상 검증 5종 전부 통과: 접합점 유일(1건) · 행 7→8(기대 +1) · 전 행 8열 ·
      개행 외 내용 변동 0(`new.replace("
","") == old.replace("
","")`) ·
      경계 필드 복원 확인(앞 행 `actor=Codex/OMX`, 뒤 행 `date=2026-08-31 step=classify`).
      **다른 필드는 손대지 않았고 행을 추가·삭제하지 않았다** — 붙어 있던 두 논리 행을 원래대로
      되돌린 것이므로 append-only 원칙에 저촉되지 않는다.

**재발 방지는 이미 적용됨**: `tools/textpatch.py` 의 `append_row()` 가 파일 끝 개행을 보장하고
헤더 열 수와 대조한다.

---

## §7 보고 양식 (규칙 밖 상황)

고치지 말고 아래 형식으로 올린다.

```
파일: <경로>
측정: crlf=<n> lf=<n> cr-only=<n> bom=<T/F>
상황: <어느 assert가 걸렸는가 / 어떤 규칙에 해당하지 않는가>
현재 조치: 미수정 (원본 무손상, 해시 <sha256[:16]>)
```

---

## §8 미승인 후속 (실행하지 마라)

- `.gitattributes` 도입(`* text=auto eol=lf` 등) — **항구적 해결이지만 저장소 전체 개행이
  한 번 바뀌고 커밋 diff가 통째로 뜬다.** 사용자 승인 필요.
- pre-commit 훅으로 MIXED 커밋 거부.
- `core.autocrlf` 변경.

---

## 이력
- **260902 v1.0** 신설. 근인: 한 세션에서 CRLF 오판 3회 재발 + 재발방지로 넣은 「편집 전 개행
  확인」 지침이 직후 재범(확인 명령 `grep`이 CRLF에서 0 반환). 규율이 아니라 기계화
  (`tools/textpatch.py`, self-test `seeded=7 undetected=0`)로 전환하고, 현재 손상 분포를
  실측해 전수 수정 절차를 고정했다. TSV 원장 5종은 이 시점에 수리 완료, 나머지 31개 MIXED는 미수리.
