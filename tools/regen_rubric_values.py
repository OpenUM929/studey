#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""자 DIFFICULTY_RUBRIC.md 의 수치를 measure_score_bands.py 출력에서 결정론적으로
재생성하고, 자 본문을 **세 축**으로 대조한다.

  A. 파생값 축   -- 역할별 정규식이 아는 자리 (role_scan)
  B. 도구정체성 축 -- `<bytes> B / <sha16>` 중 **현행** 표식이 붙은 세대 (ident_scan)
  C. 리터럴 잔차 축 -- 이전 세대에서 이동한 리터럴이 자 어딘가에 살아남았는가
                       (residue_scan). 역할 패턴이 모르는 자리를 잡는다.

CLAUDE.md 원칙 12-b -- "자는 손이 아니라 코드가 만든다."
CLAUDE.md 원칙 12-d -- "게이트는 자기 검출력을 증명한다."
CLAUDE.md 원칙 12-c -- 이 도구의 변경은 two-key 대상이다(판정 260831_08 BF-R4).
                       변경 시 원장에 bytes + sha256(16) 사슬 재동결 행을 남긴다.

판정 output/260831/rev/260831_08_arbiter_ruling_resign.md 구속 BF-R1~BF-R4 반영.
읽기 전용 -- 자를 수정하지 않는다.

알려진 경계(정직하게 적는다): C축의 기준선은 **자와 내용이 다른 가장 최근 커밋본**이다.
git 이력이 없으면 C축은 `baseline=none` 으로 비활성이며, 그때 A·B축만으로 판정한다.
"""
import io
import re
import subprocess
import sys
import hashlib

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

RUBRIC = 'analysis/catalog/DIFFICULTY_RUBRIC.md'
TOOL = 'tools/measure_score_bands.py'
NL = chr(10)

# --- BF-R3 허용목록: 이동 리터럴과 글자는 같지만 그 값이 아닌 자리 ---
# 자리(행 + 리터럴)와 사유를 명시한다. 목록에 없는 이동 리터럴이 자에 남아 있으면 실패다.
# 이 목록을 늘리는 것 자체가 12-c two-key 대상이다(BF-R4).
ALLOW = {
    (140, '23'): 'SM2 예시 문항번호 #23 (난이도 값이 아님)',
    (162, '100'): '어구 "100문제 세트" -- 세트 크기',
    (164, '100'): '어구 "100문제로 환산" -- 세트 크기',
    (169, '100'): '표 머리 "100문제 환산" -- 세트 크기',
    (174, '23'): 'T4 100문제 환산 칸 23문 -- 재계산 후에도 불변',
    (177, '100'): '어구 "100문제 요청" -- 세트 크기',
    (182, '100'): '어구 "100문제 세트" -- 세트 크기',
    (185, '20'): '§6-A 진단세트 목표 사다리 10/30/40/20 -- 독립 출처',
    (200, '20'): '예시 문항번호 #20',
    (208, '20'): '목표 분포 T4 20% -- 실측이 아닌 목표치',
}


def sha16(b):
    return hashlib.sha256(b).hexdigest()[:16]


def tool_output():
    p = subprocess.run([sys.executable, TOOL], capture_output=True)
    raw = (p.stdout + p.stderr).decode('utf-8', 'replace')
    return raw.replace(chr(13) + NL, NL).replace(chr(13), NL), p.returncode


def holdout(strata):
    """BF-R2: 계층 4행을 연도로 묶어 fold 별 폐쇄율을 낸다. 측정기 무변경."""
    acc = {}
    for name, n, fit, _ in strata:
        y = name.split('-')[1]
        a = acc.setdefault(y, [0, 0])
        a[0] += int(n)
        a[1] += int(fit)
    return dict((y, ('%.1f' % (100.0 * a[1] / a[0]), a[0], a[1]))
                for y, a in acc.items())


def derive(out):
    """측정기 출력 -> 자가 인용하는 값 전체. 손으로 넣은 상수 0개."""
    v = {}
    m = re.search(r'^ALL\s+n=(\d+)\s+fit=(\d+)\s*=\s*([\d.]+)%\s+residual=(\d+)',
                  out, re.M)
    if not m:
        raise SystemExit('ALL 행 없음 -- 측정기 출력 형식이 바뀌었다.')
    v['n'], v['fit'] = int(m.group(1)), int(m.group(2))
    v['pct'], v['residual'] = m.group(3), int(m.group(4))

    strata = re.findall(r'^([FM]-\d{4})\s+n=(\d+)\s+fit=(\d+)\s+([\d.]+)%', out, re.M)
    if len(strata) != 4:
        raise SystemExit('계층 4행 없음: %r' % (strata,))
    v['strata'] = strata
    v['stratum_min'] = min(strata, key=lambda r: float(r[3]))

    # BF-R2 검산 의무: 연도별 합이 ALL 행과 일치하지 않으면 중단한다.
    v['holdout'] = holdout(strata)
    sn = sum(a[1] for a in v['holdout'].values())
    sf = sum(a[2] for a in v['holdout'].values())
    if (sn, sf) != (v['n'], v['fit']):
        raise SystemExit('연도 합 n=%d fit=%d != ALL n=%d fit=%d -- 중단'
                         % (sn, sf, v['n'], v['fit']))
    v['holdout_min'] = min(v['holdout'].values(), key=lambda r: float(r[0]))[0]

    tiers = re.findall(r'^(T[1-4])\s+\[[\d.,\s]+[)\]]\s+(\d+)\s+([\d.]+)%', out, re.M)
    if len(tiers) != 4:
        raise SystemExit('Tier 4행 없음: %r' % (tiers,))
    v['tier_n'] = {t: int(c) for t, c, _ in tiers}
    v['tier_pct_all'] = {t: p for t, _, p in tiers}

    m = re.search(r'^--\s+outside band\s+(\d+)\s+([\d.]+)%', out, re.M)
    v['outside_n'], v['outside_pct'] = int(m.group(1)), m.group(2)

    dist = re.search(r'=== selective-score distribution ===' + NL + r'(.*?)' + NL * 2,
                     out, re.S)
    rows = [l for l in dist.group(1).split(NL)[1:] if l.strip()]
    v['units_all'] = len(rows)
    v['units_sel'] = sum(1 for l in rows if 'no selective' not in l)

    # 밴드 내 비중 + 100문제 환산(최대잔여법 -- 합 100 보장)
    v['tier_pct_band'] = {}
    frac, base = {}, {}
    for t in ('T1', 'T2', 'T3', 'T4'):
        raw = 100.0 * v['tier_n'][t] / v['fit']
        v['tier_pct_band'][t] = '%.1f' % raw
        base[t] = int(raw)
        frac[t] = raw - int(raw)
    rem = 100 - sum(base.values())
    for t in sorted(frac, key=lambda k: -frac[k])[:rem]:
        base[t] += 1
    v['tier_100'] = base
    return v


def checks(v):
    """(이름, 정규식, 캡처 순서대로의 기대값) -- 캡처마다 개별 대조한다."""
    return [
        ('전수 폐쇄',
         r'전수 폐쇄\s*(\d+)/(\d+)\s*=\s*\*\*([\d.]+)%\*\*',
         [str(v['fit']), str(v['n']), v['pct']]),
        ('ALL 인용',
         r'ALL\s+n=(\d+)\s+fit=(\d+)\s*=\s*([\d.]+)%\s+residual=(\d+)',
         [str(v['n']), str(v['fit']), v['pct'], str(v['residual'])]),
        ('연도 hold-out',
         r'연도 hold-out 최저\s*\*{0,2}([\d.]+)%',
         [v['holdout_min']]),
        ('유닛 수',
         r'(\d+)\s*유닛',
         [str(v['units_sel'])]),
        ('문항 수 라벨',
         r'유닛[^|' + NL + r']{0,12}?(\d+)\s*문항',
         [str(v['n'])]),
        ('밴드 내 모집단',
         r'밴드 내\s*(\d+)',
         [str(v['fit'])]),
        ('전체 기준 모집단',
         r'전체\s*(\d+)\s*기준',
         [str(v['n'])]),
        ('행수 인용',
         r'\((\d+)행\)',
         [str(v['n'])]),
        ('밴드 밖 비중',
         r'\(밴드 밖\)[^|]*\|[^|]*\|[^|]*\|\s*([\d.]+)%\s*\((\d+)문항\)',
         [v['outside_pct'], str(v['outside_n'])]),
        ('문항수 단독 인용',
         r'(\d+)\s*문항 실측',
         [str(v['n'])]),
        ('T1 대비 인용',
         r'\(25% vs ([\d.]+)%\)',
         [v['tier_pct_band']['T1']]),
        ('실측 사다리',
         r'실측 사다리 `([\d.]+) / ([\d.]+) / ([\d.]+) / ([\d.]+)`',
         [v['tier_pct_band']['T1'], v['tier_pct_band']['T2'],
          v['tier_pct_band']['T3'], v['tier_pct_band']['T4']]),
        ('Tier 재현 인용',
         r'T1 (\d+) / T2 (\d+) / T3 (\d+) / T4 (\d+) / outside (\d+)',
         [str(v['tier_n']['T1']), str(v['tier_n']['T2']), str(v['tier_n']['T3']),
          str(v['tier_n']['T4']), str(v['outside_n'])]),
    ]


HOLDOUT_ROLE = '연도 hold-out'

TIER_ROW = re.compile(r'^\|\s*(T[1-4])[^|]*\|\s*\*\*([\d.]+)%\*\*\s*\((\d+)문항\)'
                      r'\s*\|\s*\*\*(\d+)문\*\*\s*\|\s*([\d.]+)%')

# B축: 도구 정체성 인용. 이력 세대는 원칙 3으로 보존되므로 **현행** 표식이 붙은
# 세대만 살아 있는 값과 대조한다.
IDENT = re.compile(r'`(\d+) B / ([0-9a-f]{16})`')
GEN = re.compile(r'^\s*[①-⑨]')


def role_scan(text, v):
    """A축 -- 역할별 개별 대조."""
    lines = text.split(NL)
    bad = []
    for name, pat, want in checks(v):
        rx = re.compile(pat)
        for i, ln in enumerate(lines, 1):
            for m in rx.finditer(ln):
                for g, w in zip(m.groups(), want):
                    if g != w:
                        bad.append((i, name, m.group(0).strip(),
                                    '기대 ' + ' / '.join(want)))
                        break
    for i, ln in enumerate(lines, 1):
        m = TIER_ROW.match(ln)
        if not m:
            continue
        t = m.group(1)
        want = [v['tier_pct_band'][t], str(v['tier_n'][t]),
                str(v['tier_100'][t]), v['tier_pct_all'][t]]
        for g, w, lbl in zip(m.groups()[1:], want,
                             ['밴드내%', '문항수', '100환산', '전체%']):
            if g != w:
                bad.append((i, '%s %s' % (t, lbl), g, '기대 ' + w))
    return sorted(set(bad))


def ident_scan(text, live):
    """B축 -- **현행** 표식이 붙은 세대의 정체성이 살아 있는 도구와 일치하는가.

    live: {(bytes, sha16)} 실행 시점에 계산한 측정기 + 자기 자신(BF-R4).
    """
    lines = text.split(NL)
    bad = []
    cur = None
    for i, ln in enumerate(lines, 1):
        if GEN.match(ln):
            cur = ('**현행**' in ln)
        if cur:
            for m in IDENT.finditer(ln):
                if (m.group(1), m.group(2)) not in live:
                    # bytes 와 sha16 은 각각 하나의 자리다 -- 따로 센다(판정 BF-R1 B "2건").
                    for g, lbl in ((1, 'bytes'), (2, 'sha16')):
                        bad.append((i, '도구정체성(현행) %s' % lbl, m.group(g),
                                    '기대 ' + ' 또는 '.join(
                                        t[g - 1] for t in sorted(live))))
    return sorted(set(bad))


def git_baseline(path):
    """C축 기준선 -- 자와 내용이 다른 가장 최근 커밋본."""
    try:
        r = subprocess.run(['git', 'log', '-20', '--format=%H', '--', path],
                           capture_output=True)
        shas = r.stdout.decode().split()
    except OSError:
        return None, None
    live = open(path, 'rb').read()
    for s in shas:
        b = subprocess.run(['git', 'show', '%s:%s' % (s, path)],
                           capture_output=True).stdout
        if b and b != live:
            return s[:8], b.decode('utf-8')
    return None, None


def moved_literals(base_txt, v):
    """기준선이 인용한 값 중 살아 있는 값과 다른 것 = 이동 리터럴.
    손으로 넣은 상수 0개 -- 기준선에서 기계로 뽑는다."""
    moved = set()
    lines = base_txt.split(NL)
    for name, pat, want in checks(v):
        if name == HOLDOUT_ROLE:   # BF-R2 는 별개 구속 -- BF-R1 작업목록에 섞지 않는다
            continue
        rx = re.compile(pat)
        for ln in lines:
            for m in rx.finditer(ln):
                for g, w in zip(m.groups(), want):
                    if g != w:
                        moved.add((g, name))
    for ln in lines:
        m = TIER_ROW.match(ln)
        if not m:
            continue
        t = m.group(1)
        want = [v['tier_pct_band'][t], str(v['tier_n'][t]),
                str(v['tier_100'][t]), v['tier_pct_all'][t]]
        for g, w, lbl in zip(m.groups()[1:], want,
                             ['밴드내%', '문항수', '100환산', '전체%']):
            if g != w:
                moved.add((g, '%s %s' % (t, lbl)))
    return sorted(moved)


def residue_scan(text, moved):
    """C축 -- 이동 리터럴이 자 어딘가에 살아남았는가. 숫자 경계 가드.
    도구정체성 토큰은 B축 소관이므로 여기서 제외한다(이력 세대는 원칙 3로 보존)."""
    D = '[0-9]'
    lines = text.split(NL)
    lit = {}
    for old, role in moved:                      # 리터럴 단위로 접는다(역할 중복 제거)
        lit.setdefault(old, []).append(role)
    hits, allowed = [], []
    for old in sorted(lit):
        role = ' / '.join(sorted(set(lit[old])))
        rx = re.compile('(?<!' + D + ')(?<!' + D + r'\.)' + re.escape(old)
                        + '(?!' + D + ')(?!\\.' + D + ')')
        for i, ln in enumerate(lines, 1):
            masked = IDENT.sub(lambda m: '`' + '#' * (len(m.group(0)) - 2) + '`', ln)
            for _ in rx.finditer(masked):        # 출현 횟수를 그대로 센다
                (allowed if (i, old) in ALLOW else hits).append((i, old, role))
    return sorted(hits), sorted(allowed)


def gate0(v, live):
    """검출력 증명: 정상 본문 오탐 0 + 심은 결함 전건 검출 (원칙 12-d)."""
    ok = ('| 전수 폐쇄 {fit}/{n} = **{pct}%** | 연도 hold-out 최저 **{ho}%** |' + NL +
          '`ALL n={n} fit={fit} = {pct}% residual={res}`' + NL +
          '모집단: 2학기 기출 {u}유닛 선택형 {n}문항 -- 밴드 내 {fit}' + NL +
          '| 전체 {n} 기준 | ({n}행) |' + NL +
          '| T3 상 | **{t3b}%** ({t3n}문항) | **{t3c}문** | {t3a}% |' + NL
          ).format(fit=v['fit'], n=v['n'], pct=v['pct'], res=v['residual'],
                   u=v['units_sel'], ho=v['holdout_min'],
                   t3b=v['tier_pct_band']['T3'], t3n=v['tier_n']['T3'],
                   t3c=v['tier_100']['T3'], t3a=v['tier_pct_all']['T3'])
    mb, ms = sorted(live)[0]
    ident_ok = ('  ④ 종전 세대 `14731 B / f60455c6fc0d8ca9`.' + NL +
                '  ⑤ **현행** -- `%s B / %s`.' % (mb, ms) + NL)

    base = role_scan(ok, v) + ident_scan(ident_ok, live)
    if base:
        print('  [GATE 0 FAIL] 정상 본문 오탐 %d건: %r' % (len(base), base[:3]))
        return 1

    planted = []

    def A(name, text):
        planted.append((name, lambda: role_scan(text, v)))

    A('전수 폐쇄 분자', ok.replace('%d/' % v['fit'], '%d/' % (v['fit'] - 1), 1))
    A('ALL -- residual만 우연 일치',
      ok.replace('n=%d fit=%d' % (v['n'], v['fit']), 'n=462 fit=440', 1))
    A('유닛 수', ok.replace('%d유닛' % v['units_sel'], '20유닛', 1))
    A('행수 인용', ok.replace('(%d행)' % v['n'], '(462행)', 1))
    A('Tier 100환산', ok.replace('**%d문**' % v['tier_100']['T3'], '**99문**', 1))
    A('Tier 전체%', ok.replace('| %s%% |' % v['tier_pct_all']['T3'], '| 99.9% |', 1))
    A('연도 hold-out(BF-R2)',
      ok.replace('최저 **%s%%**' % v['holdout_min'], '최저 **91.3%**', 1))

    # B축: 현행 세대가 낡은 정체성을 인용
    planted.append(('도구정체성 현행 낡음(BF-R1 B)',
                    lambda: ident_scan(ident_ok.replace(
                        '`%s B / %s`' % (mb, ms),
                        '`14731 B / f60455c6fc0d8ca9`', 1), live)))
    # B축 역방향: 이력 세대(현행 아님)를 고치라고 하면 안 된다 -> 오탐 0 은 base 에서 확인

    # C축: 역할 패턴이 모르는 자리에 이동 리터럴이 살아남은 경우
    resid_base = ('실측 사다리 `5.2 / 32.3 / 39.8 / 22.7`' + NL)
    planted.append(('리터럴 잔차 L184형(BF-R3 fixture 1)',
                    lambda: residue_scan('맨숫자 5.2 가 문장에 남아 있다' + NL,
                                         [('5.2', 'T1 밴드내%')])[0]))
    planted.append(('리터럴 잔차 -- 허용목록 밖 신설 자리',
                    lambda: residue_scan('아무 패턴도 모르는 줄에 462 가 있다' + NL,
                                         [('462', 'n')])[0]))

    # BF-R2 검출력: 계층 행 하나의 fit 을 1 줄이면 최저 fold 가 움직여야 한다
    ymin = min(v['holdout'].items(), key=lambda kv: float(kv[1][0]))[0]
    mut = [(nm, n, str(int(f) - 1) if nm.endswith(ymin) else f, p)
           for nm, n, f, p in v['strata']]
    planted.append(('연도 hold-out 계층 감응(BF-R2 fixture)',
                    lambda: ([] if min(holdout(mut).values(),
                                       key=lambda r: float(r[0]))[0]
                             == v['holdout_min'] else [('mut', 'moved')])))

    und = [n for n, f in planted if not f()]
    print('  planted=%d undetected=%d' % (len(planted), len(und)))
    if und:
        print('  [GATE 0 FAIL] 미검출: %s' % ', '.join(und))
        return 1
    print('  [GATE 0 PASS] undetected=0')
    return 0


def main():
    out, code = tool_output()
    v = derive(out)
    rb = open(RUBRIC, 'rb').read()
    txt = rb.decode('utf-8')
    tool_b = open(TOOL, 'rb').read()
    self_b = open(__file__, 'rb').read()
    live = {(str(len(tool_b)), sha16(tool_b)), (str(len(self_b)), sha16(self_b))}

    print('== 입력 ==')
    print('  %s  exit=%d  bytes=%d sha16=%s'
          % (TOOL, code, len(tool_b), sha16(tool_b)))
    print('  %s  bytes=%d sha16=%s   <- 자기 정체성(BF-R4)'
          % (__file__.replace(chr(92), '/').split('/')[-1], len(self_b),
             sha16(self_b)))
    print('  %s  bytes=%d  sha16=%s' % (RUBRIC, len(rb), sha16(rb)))
    print()
    print('== GATE 0: 검출기 자기 검출력 (원칙 12-d) ==')
    if gate0(v, live):
        print(NL + '검출기가 검출력을 증명하지 못했다 -- 대조 결과를 신뢰하지 않는다.')
        return 2
    print()
    print('== 재생성된 정본 수치 (손으로 넣은 상수 0개) ==')
    print('  전수 폐쇄   %d/%d = %s%%  residual=%d'
          % (v['fit'], v['n'], v['pct'], v['residual']))
    print('  계층 최저   %s%% (%s)' % (v['stratum_min'][3], v['stratum_min'][0]))
    print('  연도 hold-out (BF-R2, 측정기 무변경 -- 계층 4행에서 파생)')
    for y in sorted(v['holdout']):
        p, n, f = v['holdout'][y]
        print('    %s  n=%-4d fit=%-4d %s%%' % (y, n, f, p))
    print('    최저 fold = %s%%' % v['holdout_min'])
    print('  유닛        전체 %d · 선택형 보유 %d' % (v['units_all'], v['units_sel']))
    print('  Tier        전체%    밴드내%   문항  100환산')
    for t in ('T1', 'T2', 'T3', 'T4'):
        print('    %s        %5s    %5s   %4d    %3d문'
              % (t, v['tier_pct_all'][t], v['tier_pct_band'][t],
                 v['tier_n'][t], v['tier_100'][t]))
    print('    밖       %5s            %4d' % (v['outside_pct'], v['outside_n']))
    print('    환산 합계 = %d' % sum(v['tier_100'].values()))
    print()
    print('== 자 본문 대조 (읽기 전용) ==')
    a = role_scan(txt, v)
    b = ident_scan(txt, live)
    print('  -- A축 파생값 --')
    for i, name, frag, want in a:
        print('  :%-4d [%s] %s   ->   %s' % (i, name, frag, want))
    print('  -- B축 도구정체성 --')
    for i, name, frag, want in b:
        print('  :%-4d [%s] %s   ->   %s' % (i, name, frag, want))
    print('  -- C축 리터럴 잔차 --')
    moved = moved_literals(txt, v)
    hits, allowed = residue_scan(txt, moved)
    print('  이동 리터럴 %d종 (자가 인용한 값 중 살아 있는 값과 다른 것 -- 기계 추출)'
          % len(moved))
    for i, old, role in hits:
        print('  :%-4d [잔차] %-18s (%s)' % (i, old, role))
    print('  허용목록 적중 %d건(무변경 대상): %s'
          % (len(allowed), ' '.join('L%d/%s' % (i, o) for i, o, _ in allowed)))
    sha, base_txt = git_baseline(RUBRIC)
    extra = []
    if base_txt is not None:
        gm = [x for x in moved_literals(base_txt, v) if x not in moved]
        eh, _ = residue_scan(txt, gm)
        extra = eh
        print('  교차검사 baseline=%s: 이전 세대 고유 이동 리터럴 %d종 -> 생존 %d건'
              % (sha, len(gm), len(extra)))
        if not gm:
            print('  [NOTE] baseline 이 현행 서명 형식 이전 세대라 교차검사는 사실상'
                  ' 비활성이다 -- 이 실행의 판정 근거는 A·B·C축이다.')
        for i, old, role in extra:
            print('  [WARN] :%-4d 이전 세대 리터럴 생존 %s (%s)' % (i, old, role))
    else:
        print('  교차검사 baseline=none (git 이력 없음)')

    # 건수는 **자리(행+리터럴)** 로 센다. C축(잔차)이 A축의 상위집합이므로 C+B 가 작업목록이고,
    # A축은 그중 역할 패턴이 이미 아는 부분집합이다. residual = 역할 패턴 사각(A가 놓친 자리).
    keys = set((i, o) for i, o, _ in hits) | set((i, f) for i, _, f, _ in b)
    lines_hit = sorted(set(k[0] for k in keys))
    a_lines = set(i for i, _, _, _ in a)
    only_c = [h for h in hits if h[0] not in a_lines]
    print()
    print('  stale=%d lines=%d residual=%d'
          % (len(keys), len(lines_hit), len(only_c)))
    print('  A축(역할) %d건 / B축(정체성) %d건 / C축 잔차 %d건 · 그중 역할 사각 %d건'
          % (len(a), len(b), len(hits), len(only_c)))
    if only_c:
        print('  역할 사각: ' + ' '.join('L%d/%s' % (i, o) for i, o, _ in only_c))
    if lines_hit:
        print('  행: ' + ' '.join('L%d' % x for x in lines_hit))
    ho = [x for x in a if x[1] == HOLDOUT_ROLE]
    print('  D축(BF-R2 연도 hold-out) %d건 -- BF-R1 40건과 별개로 센다' % len(ho))
    return 1 if (keys or a or b) else 0


# [FAIL] path: gate0() returns 1 on planted undetected, prints [GATE 0 FAIL] and exits 2
if __name__ == '__main__':
    sys.exit(main())
