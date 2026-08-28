#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HWP -> text(+tables) via hwp5html. Preserves table/보기 content that hwp5txt drops.

260826 (판정 260826_02 조건 C1) 개정 — 결함 3건 수정:
  (a) `hwp5html`이 PATH에 없으면 FileNotFoundError로 즉사했다. 실측: 이 환경의
      hwp5html.exe는 nt_user scheme 스크립트 폴더에만 있고 PATH에 없다.
      (`python -m hwp5.hwp5html`은 아무것도 하지 않고 exit 0 — fail-open이라 쓰지 않는다.)
  (b) 매립 이미지가 텍스트에서 흔적 없이 사라졌다. 실측: 통합과학 고사원안 1건에
      <img> 38개 / bindata 35개가 있었는데 산출 텍스트의 참조는 0개였다.
      이제 각 이미지 자리에 `[[BIN0001.jpg]]` 마커를 남긴다.
  (c) `shutil.rmtree(tmp)`가 그 이미지 파일들을 삭제했다. `--bindata <dir>`로 보존한다.
사용:
  python tools/hwp2md.py <src.hwp> <dst.txt> [--bindata <dir>]
표준출력 마지막 줄에 `bindata=<n> imgrefs=<m>`를 찍는다 — S1 이미지 수율 게이트의 입력값.
"""
import sys, os, re, subprocess, sysconfig, tempfile, shutil, warnings
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)


def find_hwp5html():
    """PATH -> nt_user scheme -> nt scheme 순으로 실행 파일을 찾는다."""
    exe = shutil.which("hwp5html")
    if exe:
        return exe
    for scheme in ("nt_user", "nt", "posix_user", "posix_prefix"):
        try:
            d = sysconfig.get_path("scripts", scheme)
        except Exception:
            continue
        if not d or not os.path.isdir(d):
            continue
        for name in ("hwp5html.exe", "hwp5html"):
            p = os.path.join(d, name)
            if os.path.exists(p):
                return p
    raise SystemExit(
        "[FAIL] hwp5html not found (PATH nor script dirs). "
        "pip install pyhwp, or add the user scripts dir to PATH. "
        "이 단계는 통과가 아니라 blocked 다."
    )


def cell_text(td):
    return re.sub(r'[ \t]+', ' ', td.get_text(' ', strip=True)).strip()


def render(el, out, depth=0):
    for child in el.children:
        name = getattr(child, 'name', None)
        if name is None:
            continue
        if name == 'table':
            out.append('')
            for tr in child.find_all('tr', recursive=True):
                # only direct-ish cells; nested tables handled by get_text
                cells = [cell_text(td) for td in tr.find_all(['td', 'th'], recursive=False)]
                if not cells:
                    cells = [cell_text(td) for td in tr.find_all(['td', 'th'])]
                if any(cells):
                    out.append('| ' + ' | '.join(cells) + ' |')
            out.append('')
        elif child.find('table'):
            render(child, out, depth+1)
        else:
            t = re.sub(r'[ \t]+', ' ', child.get_text(' ', strip=True)).strip()
            if t:
                out.append(t)


def mark_images(soup):
    """<img>를 `[[파일명]]` 텍스트로 치환해 get_text가 집어가게 한다. 치환 수를 돌려준다."""
    n = 0
    for img in soup.find_all('img'):
        src = img.get('src') or ''
        base = os.path.basename(src) or 'UNKNOWN'
        img.replace_with(' [[%s]] ' % base)
        n += 1
    return n


def convert(hwp_path, bindata_dir=None):
    exe = find_hwp5html()
    tmp = tempfile.mkdtemp()
    try:
        subprocess.run([exe, '--output', tmp, hwp_path], check=True, capture_output=True)
        xhtml = os.path.join(tmp, 'index.xhtml')
        if not os.path.exists(xhtml):
            raise SystemExit("[FAIL] hwp5html produced no index.xhtml for %s" % hwp_path)
        html = open(xhtml, encoding='utf-8').read()
        soup = BeautifulSoup(html, 'lxml')
        imgrefs = mark_images(soup)
        out = []
        render(soup.find('body') or soup, out)
        # collapse blank runs
        text = '\n'.join(out)
        text = re.sub(r'\n{3,}', '\n\n', text)

        src_bin = os.path.join(tmp, 'bindata')
        nbin = 0
        if os.path.isdir(src_bin):
            files = sorted(os.listdir(src_bin))
            nbin = len(files)
            if bindata_dir:
                os.makedirs(bindata_dir, exist_ok=True)
                for f in files:
                    shutil.copy2(os.path.join(src_bin, f), os.path.join(bindata_dir, f))
        if imgrefs and not bindata_dir:
            sys.stderr.write(
                "[WARN] %d embedded image(s) referenced but --bindata not given; "
                "the image files are discarded with the temp dir.\n" % imgrefs)
        return text, nbin, imgrefs
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main(argv):
    args = [a for a in argv[1:]]
    bindata_dir = None
    if '--bindata' in args:
        i = args.index('--bindata')
        try:
            bindata_dir = args[i+1]
        except IndexError:
            raise SystemExit("[FAIL] --bindata needs a directory argument")
        del args[i:i+2]
    if len(args) != 2:
        raise SystemExit(__doc__)
    src, dst = args
    text, nbin, imgrefs = convert(src, bindata_dir)
    open(dst, 'w', encoding='utf-8').write(text)
    print('OK', dst, os.path.getsize(dst), 'bytes')
    print('bindata=%d imgrefs=%d' % (nbin, imgrefs))


if __name__ == '__main__':
    main(sys.argv)
