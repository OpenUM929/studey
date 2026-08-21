#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_web.py — web/ 의 외부 에셋(style.css, parser.js, app.js, data.js)을
index.html 에 인라인화해 단일 자급형 파일로 만든다.
결과 index.html 은 외부 참조 없이 더블클릭만으로 동작한다.
(공유용 단일 HTML은 앱 내 '📤 공유 HTML' 버튼으로 런타임 생성.)

사용:  python tools/build_web.py [--web web]
"""
import os, re, argparse


def inline(web_root):
    tpl = os.path.join(web_root, "index.template.html")
    out = os.path.join(web_root, "index.html")
    html = open(tpl, encoding="utf-8").read()

    def read(name):
        return open(os.path.join(web_root, name), encoding="utf-8").read()

    # CSS -> <style>
    html = html.replace('<link rel="stylesheet" href="style.css">',
                        "<style>\n" + read("style.css") + "\n</style>")
    # parser.js -> <script>
    html = html.replace('<script src="parser.js"></script>',
                        "<script>\n" + read("parser.js") + "\n</script>")
    # app.js -> <script>
    html = html.replace('<script src="app.js"></script>',
                        "<script>\n" + read("app.js") + "\n</script>")
    # data.js -> <script id="quiz-data"> (내용 통째 인라인)
    data = read("data.js")
    html = html.replace('<script id="quiz-data" src="data.js"></script>',
                        '<script id="quiz-data">\n' + data + "\n</script>")

    if '<link rel="stylesheet" href="style.css">' in html:
        raise SystemExit("style.css 인라인 실패")
    if 'src="parser.js"' in html or 'src="app.js"' in html or 'src="data.js"' in html:
        raise SystemExit("js 인라인 실패(외부 참조 잔존)")

    open(out, "w", encoding="utf-8").write(html)
    print("OK", out, os.path.getsize(out), "bytes  (외부 참조 0)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--web", default="web")
    args = ap.parse_args()
    inline(args.web)
