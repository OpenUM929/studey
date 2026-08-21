#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HWP -> text(+tables) via hwp5html. Preserves table/보기 content that hwp5txt drops."""
import sys, os, re, subprocess, tempfile, shutil, warnings
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

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

def convert(hwp_path):
    tmp = tempfile.mkdtemp()
    try:
        subprocess.run(['hwp5html', '--output', tmp, hwp_path],
                       check=True, capture_output=True)
        xhtml = os.path.join(tmp, 'index.xhtml')
        html = open(xhtml, encoding='utf-8').read()
        soup = BeautifulSoup(html, 'lxml')
        out = []
        render(soup.find('body') or soup, out)
        # collapse blank runs
        text = '\n'.join(out)
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    open(dst, 'w', encoding='utf-8').write(convert(src))
    print('OK', dst, os.path.getsize(dst), 'bytes')
