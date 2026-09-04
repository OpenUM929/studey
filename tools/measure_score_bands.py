"""Regenerate the selective-item score distribution from corpus originals.

Purpose: input for DIFFICULTY_RUBRIC.md §1 band recalibration (K1, two-key).

CLAUDE.md principle 12-b -- the ruler is made by code, not by hand: this script
regenerates the measurement deterministically from corpus/EX-*/transcript.md and
must be re-run rather than its output edited.

CLAUDE.md principle 12-d -- a detector proves its own detection power. Three gates
run before any number is reported:
  GATE 1 truth   : reproduce the six values confirmed by tier-3 ruling 260831_03 §1-2
  GATE 2 dup     : flag units whose selective sequences are byte-identical
  GATE 3 declared: compare extracted item count against the exam's printed declaration
Any GATE 1 miss aborts. GATE 2/3 flags are excluded from the aggregate, never hidden.

Usage:  python tools/measure_score_bands.py            (run from repo root)
Exit 0 only when GATE 1 passes. Output is ASCII-only (principle 9-b).
"""
import re, sys, glob, os
from fractions import Fraction as F

# M2 (260902): the Korean word 점 also means "dot". Two map-legend captions in
# EX-social-20242M -- "(1점=소규모 단위)" and "(1점당 10만명)" -- were counted as item
# scores, pushing that unit to 26 against its printed declaration of 24. A score mark is
# never followed by '=' or '당', so one lookahead separates the two senses of 점.
MARK    = re.compile(r'[\[(]\s*([0-9]+(?:\.[0-9]+)?)\s*점(?!\s*(?:=|당))')
# M3 (260902): HWP text extraction line-breaks a mark into three lines -- "[3.2" / "점"
# / "]" -- so a per-line regex never sees it. EX-science-20252F lost exactly 4 marks this
# way (20 vs declared 24; 66.3 vs 80.0). JOIN re-attaches the number line to its 점 line
# before the body is split; it moves no other text and triggers no state change, because
# neither the 점 line nor the ] line matches TO_SOD/TO_SEL.
JOIN    = re.compile(r'\[\s*([0-9]+(?:\.[0-9]+)?)\s*\n\s*점')
# BF2 (260902, ruling 260831_07 Q2-c): HWP extraction can put a space INSIDE the
# number -- '[3 .8점 ]'. MARK sees no digit-dot-digit and drops the mark silently.
# The class is [^\S\n] (blank but NOT newline), deliberately: with plain \\s*
# this pattern also spans line breaks and silently does JOIN's job, which made the
# GATE 0 line-broken fixture pass even with JOIN deleted (measured 260902). A repair
# that masks another repair destroys that repair's detector.
COMMAFIX= re.compile(r'([\[(][^\S\n]*[0-9])[^\S\n]*,[^\S\n]*([0-9][^\S\n]*점)')
SPACEFIX= re.compile(r'\[[^\S\n]*([0-9]+)[^\S\n]*\.[^\S\n]*([0-9]+)[^\S\n]*점')
# BF2: transcriber annotation lines ('> [판독] ...') re-quote body marks. They are
# commentary, not items, and double-counted one mark in EX-history-20242F.
ANNOT   = re.compile(r'^\s*>')
IDX     = re.compile(r'^-\s*(선택형|서답형|서술형|단답형)\s*\d*\s*[:：]')
IDX_SEL = re.compile(r'^-\s*선택형\s*\d*\s*[:：]')
TO_SOD  = re.compile(r'^\s*(?:#{1,4}\s*|\*{0,2}\s*|\[\s*)(단답형|서술형|서답형)')
TO_SEL  = re.compile(r'^\s*(?:#{1,4}\s*선택형|\*{0,2}\d+\s*\.\s*\S|\d{1,2}\s*$)')
META_BULLET = re.compile(r'^-\s')
DECL_SUM= re.compile(r'선택형 합계\s*([0-9]+(?:\.[0-9]+)?)\s*점')   # F2 (260901)
# BF3 (260902, ruling 260831_07): DECL_SUM only matches '선택형 합계 N점' inside the
# first 60 lines. EX-history-20242F states its own enumeration as '선택형 80.0점(...)'
# at L426 -- invisible to DECL_SUM at ANY window width (measured: 0 matches on the
# whole file). Widening the window alone would be fail-open, so the pattern widens too.
DECL_ANY= re.compile(r'선택형(?:\s*합계)?\s*([0-9]+(?:\.[0-9]+)?)\s*점')
DECL    = re.compile(r'선택형[\s(（]*([0-9]+)[\s)）]*\s*[·,]?\s*(?:문항|단답형|서답형|서술형)')

VALIDATE = {
    # 20252M 6건 -- tier-3 260831_03 §1-2, arbiter가 fresh context에서 독립 재산출
    'EX-korean-20252M':  (29, F(60)),
    'EX-science-20252M': (23, F(60)),
    'EX-social-20252M':  (20, F(60)),
    'EX-english-20252M': (27, F(70)),
    'EX-history-20252M': (20, F(40)),
    'EX-math2-20252M':   (0,  F(0)),
    # BF-K1-6 (260901) -- F계열/2024계열 앵커. 판정문 인용이 아니라, 각 전사본이
    # 스스로 나열한 개별 배점값의 Fraction 정확합에서 유도했다(원칙 12-b).
    # 산출: python -c "sum(Fraction(v) for v in <transcript의 나열식>.split('+'))"
    'EX-science-20242F': (24, F(80)),   # 나열 24값 정확합 80.0 (전사본 선언 78.8은 오기 -- M5)
    'EX-science-20242M': (24, F(60)),   # 나열 24값 정확합 60.0 = 전사본 선언 60.0 일치
    'EX-info-20252F':    (18, F(70)),   # 전사본 선언 "선택형 합계 70점" + 단답 30점 = 100
    'EX-math1-20242M':   (0,  F(0)),    # 수학 계열 선택형 부재 (단답 18문항 합계 60.00 별도 확인)
}
MATH = ('math1', 'math2')   # no OMR selective items at all -- CLAUDE.md:13
# BF-RF-5(b) (260901): these are NOT the current band. DIFFICULTY_RUBRIC.md was re-signed
# on 260901 to a RELATIVE band (r in [0.80, 1.20], §1); the absolute 3.0~4.2 pair was
# DEMOTED to §1-2 as the 80-point-series (mean unit price 3.540) conversion example.
# band() below therefore reports a legacy-scale column kept for comparison only -- never
# cite it as the ruler. The live criterion is R_LO/R_HI further down.
BAND_LO, BAND_HI = F('3.0'), F('4.2')    # legacy absolute example, DIFFICULTY_RUBRIC.md:49


# BF1 (260902, ruling 260831_07 Q2-b): GATE 0 must exercise the SAME pipeline as
# measure(). The old fixture ran MARK.findall() over multi-line text, where \\s*
# spans newlines -- so the line-broken fixture passed even with JOIN deleted and
# proved nothing. prep()/line_marks() are now the single shared path.
def prep(t):
    return JOIN.sub(r'[\1점', SPACEFIX.sub(r'[\1.\2점', COMMAFIX.sub(r'\1.\2', t)))


def line_marks(l):
    return [] if ANNOT.match(l) else MARK.findall(l)


def extract_marks(text):
    out = []
    for l in prep(text).split('\n'):
        out += line_marks(l)
    return out


def measure(path):
    lines = prep(open(path, encoding='utf-8').read()).split('\n')
    subj  = os.path.basename(os.path.dirname(path)).split('-')[1]
    sel, sod = [], []
    # index mode needs a SELECTIVE index. Requiring only IDX let social-2024's
    # "- 단답형1:" summary bullets flip the unit into index mode -> 0 selective.
    if sum(1 for l in lines if IDX_SEL.search(l)) >= 3:
        for l in lines:
            if IDX.search(l):
                (sel if IDX_SEL.search(l) else sod).extend(F(v) for v in MARK.findall(l))
        mode = 'index'
    else:
        st = 'sel'
        for l in lines:
            if META_BULLET.search(l):     # header bullets are metadata, not body
                continue
            if ANNOT.match(l):           # BF2: transcriber annotation, not body
                continue
            if TO_SOD.search(l):   st = 'sod'
            elif TO_SEL.search(l): st = 'sel'
            (sod if st == 'sod' else sel).extend(F(v) for v in line_marks(l))
        mode = 'body'
    decl = dsum = None
    for l in lines[:60]:
        if decl is None:
            m = DECL.search(l)
            if m: decl = int(m.group(1))
        if dsum is None:
            m2 = DECL_SUM.search(l)
            if m2: dsum = F(m2.group(1))
    if subj in MATH:
        sod, sel, decl, dsum, mode = sel + sod, [], 0, None, mode + '+math0'
    return sel, sod, mode, decl, dsum


def band(v): return sum(1 for x in v if BAND_LO <= x <= BAND_HI)


def scan_anysum(path):
    """BF3: 파일 전체에서 '자체 열거 선택형 합계' 선언을 찾는다(창 무제한)."""
    m = DECL_ANY.search(prep(open(path, encoding='utf-8').read()))
    return F(m.group(1)) if m else None


rows = [(os.path.basename(d.rstrip(chr(47)+chr(92))),) + measure(os.path.join(d, 'transcript.md'))
        for d in sorted(glob.glob('corpus/EX-*/'))]
ANYSUM = dict((os.path.basename(d.rstrip(chr(47) + chr(92))),
               scan_anysum(os.path.join(d, 'transcript.md')))
              for d in sorted(glob.glob('corpus/EX-*/')))

# ---- GATE 0 fixture (CLAUDE.md 원칙 12-d) ----
# A detector that has never been shown to fire is an unverified detector. Four defect
# classes are planted here as literals every run -- legend senses of 점 (M2), the
# line-broken mark (M3), the annotation re-quote and the space-inside-number (M6).
# Evaluation goes through extract_marks(), the same path measure() uses; evaluating
# fixtures against multi-line text made the line-broken case undetectable (BF1).
GATE0 = [
    ('legend-equals', '(1점=소규모 단위)',            []),
    ('legend-per',    '점묘법(1점당 10만명)',          []),
    ('plain-bracket', '고른 것은? [2.5 점 ]',          ['2.5']),
    ('plain-paren',   '답하시오.(10점)',               ['10']),
    ('line-broken',   '고른 것은?\n[3.2\n점\n]',       ['3.2']),
    ('annotation-quote', '> [판독] 원본 3번 [3.6점] 재인용',  []),
    ('space-in-number',  '옳은 것은? [3 .8점 ]',              ['3.8']),
    ('comma-decimal',    '적절한 것은?(2,8점)',               ['2.8']),
    ('comma-thousands',  '누적 (1,234점=합계)',               []),
]
print('=== GATE 0 fixture: planted parser defects ===')
g0 = 0
for name, text, want in GATE0:
    got = extract_marks(text)
    if got != want:
        print('[FAIL] fixture %-14s got=%s want=%s' % (name, got, want)); g0 += 1
print('planted=%d undetected=%d' % (len(GATE0), g0))
if g0:
    print('[ABORT] fixture regression -- extraction rules changed meaning'); sys.exit(1)
# GATE 0s: 상태 전이 규칙(TO_SEL)은 extract_marks() 경로 밖이라 따로 심는다.
# HWP 추출이 '10.' 에서 마침표를 떼어 번호만 한 줄에 남기면(EX-english-20251M L145)
# 그 문항의 배점이 직전 서답형 구간에 흡수된다. 거짓 양성 방지 자리를 함께 둔다.
GATE0S = [
    ('numbered-item',   '10. 다음 글의 제목으로', True),
    ('bare-number',     '10',                    True),
    ('bare-number-pad', '  7  ',                 True),
    ('prose-number',    '약 10 명이 참여했다',     False),
    ('sod-header',      '[ 서답형1(서술) ] 쓰시오', False),
    ('three-digit',     '2024',                  False),
]
g0s = 0
for name, line, want in GATE0S:
    if bool(TO_SEL.search(line)) != want:
        print('[FAIL] fixture %-16s TO_SEL=%s want=%s'
              % (name, not want, want)); g0s += 1
print('planted-state=%d undetected=%d' % (len(GATE0S), g0s))
if g0s:
    print('[ABORT] state-transition fixture regression'); sys.exit(1)
print('[GATE 0 PASS] undetected=0')

print('=== GATE 1 truth: reproduce tier-3 confirmed values ===')
undetected = 0
for uid, sel, sod, m, decl, dsum in rows:
    if uid not in VALIDATE: continue
    en, es = VALIDATE[uid]
    ok = (len(sel) == en and sum(sel) == es)
    undetected += 0 if ok else 1
    print('%-20s [%-11s] got n=%-3d sum=%-7s want n=%-3d sum=%-7s %s'
          % (uid, m, len(sel), float(sum(sel)) if sel else 0.0, en, float(es),
             'OK' if ok else 'MISMATCH'))
# F-RF-5 (260901, ruling 260831_05): a gate that reports only `undetected=0` is proved
# in one direction. GATE 2's single firing to date was a FALSE POSITIVE (ruling 260831_04
# U3-a) and it silently dropped 18 items, so the false-alarm side has to be visible too.
# `flagged` = anchors that failed here; each one needs origin adjudication before it may
# be called a corpus defect. `coverage` = how much of the population the truth table covers.
print('checked=%d undetected=%d flagged=%d coverage=%d/%d'
      % (len(VALIDATE), undetected, undetected, len(VALIDATE), len(rows)))
if undetected:
    print('[ABORT] extractor cannot reproduce confirmed values -- results unusable')
    sys.exit(1)
print('[GATE 1 PASS] undetected=0')

print('\n=== GATE 2 dup: identical selective sequences ===')
seen, dup = {}, []
for uid, sel, sod, m, decl, dsum in rows:
    if not sel: continue
    k = tuple(sel)
    if k in seen: dup.append((seen[k], uid, len(sel)))
    else: seen[k] = uid
for a, b, n in dup:
    print('[WARN] identical selective sequence (n=%d): %s == %s' % (n, a, b))
print('duplicates=%d (warning only -- not excluded, see BF-K1-7a)' % len(dup))
print('GATE 2 false-positive rate to date: 1/1 -- EX-info-20252M vs EX-info-20252F are'
      ' different exams that reuse one score-allocation table (ruling 260831_04 U3-a).'
      ' Treat every firing as a candidate, never as a verdict.')

print('\n=== GATE 3 declared: printed declaration vs extraction ===')
mism, sumonly = [], []
for uid, sel, sod, m, decl, dsum in rows:
    if decl is None:
        print('[WARN] %-20s declaration not parsed' % uid); mism.append(uid); continue
    if decl != len(sel):
        print('[WARN] %-20s declared n=%-3d extracted n=%-3d' % (uid, decl, len(sel))); mism.append(uid)
    elif dsum is not None and dsum != sum(sel):        # F2 (260901): declared-sum check
        print('[WARN] %-20s declared sum=%-7s extracted sum=%-7s (declared-sum arithmetic error suspected)'
              % (uid, float(dsum), float(sum(sel)))); mism.append(uid)
        # BF-RF-1 (260901, ruling 260831_05 U8): a sum-only mismatch on a unit whose item
        # COUNT matches and which carries a GATE 1 anchor is a defect in the transcript's
        # one-line summary, not in the verified item data. Warn and fail, but keep the unit
        # in the aggregate -- auto-excluding it silently moved the signed population
        # 462 -> 438 and the signed value 95.2% -> 95.0%.
        if uid in VALIDATE:
            sumonly.append(uid)
print('mismatches=%d' % len(mism))

print('--- GATE 3b sum-axis coverage (BF3) ---')
cov = unc = sax = 0
for uid, sel, sod, m, decl, dsum in rows:
    if m.endswith('+math0'):
        continue
    a = ANYSUM.get(uid)
    if a is None:
        print('[WARN] %-20s self-enumerated selective total not found'
              ' -- sum axis UNCOVERED' % uid); unc += 1; continue
    cov += 1
    if a != sum(sel):
        print('[WARN] %-20s enumerated sum=%-7s extracted sum=%-7s'
              % (uid, float(a), float(sum(sel)))); sax += 1
print('sum-axis coverage=%d/%d uncovered=%d mismatches=%d'
      % (cov, cov + unc, unc, sax))

# BF-K1-7(a) (260901): GATE 2는 경고만 하고 자동 배제하지 않는다.
# 근거 -- tier-3 260831_04 §2 U3-a: 배점 열 일치는 중복의 충분조건이 아니다.
# EX-info-20252M/F는 원본 hwp가 서로 다른 파일이고 본문도 다르다(학교가 배점
# 배분표를 재사용했을 뿐). 오탐률 1/1이었고, 그 오탐이 18문항을 조용히 빼서
# '중간 4.0+ 0건'이라는 거짓 결론을 만들었다. 복원 시 M 233문항/44적합/4.0+ 10건.
EXCL = set(mism) - set(sumonly)
print('\nexcluded from aggregate: %s' % (', '.join(sorted(EXCL)) or 'none'))
if sumonly:
    print('kept in aggregate (sum-only mismatch, count matches, GATE 1 anchor): %s'
          % ', '.join(sorted(sumonly)))

print('\n=== selective-score distribution ===')
print('%-20s %-2s %-6s %4s %5s %8s %11s %9s %5s'
      % ('unit', 'T', 'mode', 'n', 'decl', 'sum', 'range', 'band', '4.0+'))
agg = {}
for uid, sel, sod, m, decl, dsum in rows:
    et = 'M' if uid.endswith('M') else 'F'
    if not sel:
        print('%-20s %-2s %-6s %4d %5s %8s %11s %9s %5s'
              % (uid, et, m, 0, decl, '-', 'no selective', '-', '-')); continue
    fl = ' EXCL' if uid in EXCL else ''
    print('%-20s %-2s %-6s %4d %5s %8s %11s %4d/%-4d %5d%s'
          % (uid, et, m, len(sel), decl, float(sum(sel)),
             '%s~%s' % (float(min(sel)), float(max(sel))), band(sel), len(sel),
             sum(1 for v in sel if v >= 4), fl))
    if uid in EXCL: continue
    a = agg.setdefault(et, [[], []])
    a[0] += sel; a[1].append(sum(sel))

print('\n=== axis test: midterm(M) vs final(F) ===')
print('%-2s %5s %6s %8s %11s %6s %11s' % ('T','units','n','band','pct','4.0+','sel_total_avg'))
for et in ('M', 'F'):
    if et not in agg: continue
    vs, tots = agg[et]
    print('%-2s %5d %6d %8d %10.1f%% %6d %11.1f'
          % (et, len(tots), len(vs), band(vs), 100.0*band(vs)/len(vs),
             sum(1 for v in vs if v >= 4), float(sum(tots))/len(tots)))
print('\nmean unit price:  M=%.2f  F=%.2f'
      % (float(sum(agg['M'][1]))/len(agg['M'][0]), float(sum(agg['F'][1]))/len(agg['F'][0])))


# ---- BF-K1-7(b) (260901): signed relative metric r  --  tier-3 260831_04 §2 U1 ----
# r = item score / (that paper's selective total / selective item count)
# signed band r in [0.80, 1.20]
# Tier: T1 0.800~0.867 · T2 0.867~0.967 · T3 0.967~1.067 · T4 1.067~1.200
R_LO, R_HI = F('0.80'), F('1.20')
# BF-RF-2 (260901): the 4th element is True when the upper bound is CLOSED. T4 must be
# [1.067, 1.200] so that r == 1.200 exactly (4 items: english-20242F 1 · english-20242M 3)
# lands in T4 instead of being counted as "outside band" while sitting inside the band.
TIERS = (('T1', F('0.800'), F('0.867'), False), ('T2', F('0.867'), F('0.967'), False),
         ('T3', F('0.967'), F('1.067'), False), ('T4', F('1.067'), F('1.200'), True))

def tier_of(r):
    """Tier label for a relative score, or None when r falls outside the signed band."""
    for name, lo, hi, closed in TIERS:
        if (lo <= r <= hi) if closed else (lo <= r < hi):
            return name
    return None


runits, rall = [], []
for uid, sel, sod, m, decl, dsum in rows:
    if not sel or uid in EXCL:
        continue
    mean = sum(sel) / len(sel)
    rs = [x / mean for x in sel]
    runits.append((uid, rs))
    rall += rs

print()
print('=== signed relative band  r in [0.80, 1.20] ===')
fit = sum(1 for r in rall if R_LO <= r <= R_HI)
print('ALL   n=%d  fit=%d = %.1f%%  residual=%d' % (len(rall), fit, 100.0*fit/len(rall), len(rall)-fit))

print()
print('--- per stratum ---')
strat = {}
for uid, rs in runits:
    key = ('M' if uid.endswith('M') else 'F') + '-' + uid.split('-')[2][:4]
    strat.setdefault(key, []).extend(rs)
for k in sorted(strat):
    v = strat[k]
    f_ = sum(1 for r in v if R_LO <= r <= R_HI)
    print('%-8s n=%-4d fit=%-4d %6.1f%%' % (k, len(v), f_, 100.0*f_/len(v)))

print()
print('--- per unit (residual > 0 only) ---')
for uid, rs in runits:
    res = len(rs) - sum(1 for r in rs if R_LO <= r <= R_HI)
    if res:
        print('%-20s n=%-4d residual=%d' % (uid, len(rs), res))

print()
print('--- Tier conversion share ---')
for name, lo, hi, closed in TIERS:
    if closed:
        c = sum(1 for r in rall if lo <= r <= hi)
    else:
        c = sum(1 for r in rall if lo <= r < hi)
    print('%-3s [%.3f,%.3f%s %4d  %5.1f%%'
          % (name, float(lo), float(hi), ']' if closed else ')', c, 100.0*c/len(rall)))
out = sum(1 for r in rall if r < F('0.800') or r > F('1.200'))
print('%-3s outside band      %4d  %5.1f%%' % ('--', out, 100.0*out/len(rall)))

# ---- fail-closed exit (CLAUDE.md 원칙 11) ----
# 260901: the tool printed [WARN] for every GATE 3 mismatch and still returned 0.
# tools/check_assurance_contract.py flagged exactly this ("prints [WARN] but has no
# [FAIL] path (fail-open)"). GATE 2 stays warning-only by ruling 260831_04 BF-K1-7(a);
# GATE 3 mismatches were then attributed wholesale to transcription (M2/M3/M5, owner
# type-extractor per ruling 260831_04 F3). 260902 root-cause tracing overturned two of the
# three: M2 and M3 were defects in THIS parser (see MARK/JOIN above), and both units land
# exactly on their printed declaration once the parse rule is corrected. Only M5 --
# EX-science-20242F's summary line declaring 78.8/21.2 where its own enumerated values sum
# to 80.0/20.0 -- is a transcription defect, and it stays with type-extractor.
# A gate must not name an owner it has not proved. The measurement above still prints in full --
# the non-zero exit is the verdict, not a suppression.
# ---- per-item Tier table (U7 slice 2 input) ----
# CLAUDE.md 12-b: the ruler is made by code, not by hand. Downstream actors must NOT
# hand-assign Tier from a printed score; they consume this table. Emitted only on demand
# because it is one line per item.
if '--per-item' in sys.argv:
    print()
    print('=== per-item Tier (signed band, selective items only) ===')
    print('%-20s %4s %8s %9s %6s' % ('unit', 'idx', 'score', 'r', 'tier'))
    sel_by_uid = dict((uid, sel) for uid, sel, sod, m, decl, dsum in rows)
    for uid, rs in runits:
        sel = sel_by_uid[uid]
        mean = sum(sel) / len(sel)
        for i, (v, r) in enumerate(zip(sel, rs), 1):
            t = tier_of(r)
            print('%-20s %4d %8s %9.4f %6s'
                  % (uid, i, float(v), float(r), t if t else 'OUT'))
        print('%-20s mean unit price = %.4f  (selective total %s / n=%d)'
              % (uid, float(mean), float(sum(sel)), len(sel)))
    print('per-item rows = %d' % len(rall))
    print('NOTE: units with zero selective items (math) get no r -- their Tier stays')
    print('      structural per DIFFICULTY_RUBRIC.md, not band-derived.')

print()
if mism:
    print('[FAIL] GATE 3 mismatches=%d -- %s' % (len(mism), ' '.join(sorted(mism))))
    print('       band figures above are usable but the run is NOT a pass. Locate the')
    print('       defect before naming an owner: a count/sum that lands exactly on the')
    print('       printed declaration once a parse rule is corrected is a parser defect')
    print('       (M2/M3, fixed 260902), not a transcription defect. M5 remains one --')
    print('       EX-science-20242F summary 78.8/21.2 vs enumerated 80.0/20.0.')
    sys.exit(1)
print('[OK] GATE 1 undetected=0 / GATE 3 mismatches=0 (GATE 2 warning-only per BF-K1-7a)')
