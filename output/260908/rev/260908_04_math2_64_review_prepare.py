"""Non-authoritative inventory and lossless review copies; never a release gate."""
from pathlib import Path
import hashlib
import json
import re
from collections import Counter

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'output/260908'
SOURCES = [
    'output/260830/260830_01_math2_graded_new_forms_32.md',
    'output/260830/260830_02_math2_unused_axes_32.md',
    'corpus/SUP-math2-2026/transcript.md',
    'output/260829/260829_02_math2_comprehensive_25.md',
    'output/260822/공통수학2_도형의방정식_모의40.md',
]

def sha(data):
    return hashlib.sha256(data).hexdigest()

def headings(text):
    return re.findall(r'^\*\*([A-D]?\d+)\.\*\*', text, re.M)

def checked(label, expected, observed):
    duplicate = [x for x, n in Counter(observed).items() if n > 1]
    result = dict(label=label, expected=expected, observed=observed,
                  duplicate=duplicate, missing=sorted(set(expected)-set(observed)),
                  extra=sorted(set(observed)-set(expected)))
    assert not duplicate and not result['missing'] and not result['extra'], result
    return result

def main():
    frozen = {p: (ROOT / p).read_bytes() for p in SOURCES}
    manifest = {'scope': 'structural-only', 'release': 'BLOCKED', 'sources': [], 'copies': [], 'coverage': []}
    for p, data in frozen.items():
        manifest['sources'].append(dict(path=p, bytes=len(data), sha256=sha(data)))
    queue = []
    for pos, p in enumerate(SOURCES[:2]):
        source = frozen[p].decode('utf-8-sig').replace('\r\n', '\n')
        assert source.count('# 정답 · 해설 · 유형') == 1
        body, answers = source.split('# 정답 · 해설 · 유형', 1)
        ids = headings(body)
        expected = [f'{letter}{i}' for letter, n in [('A',6),('B',9),('C',10),('D',7)] for i in range(1,n+1)]
        manifest['coverage'].append(checked(p, expected, ids))
        answer_ids = re.findall(r'^\| ([A-D]\d+)(?: ⚠️)? \|', answers, re.M)
        manifest['coverage'].append(checked(p+' answers', ids, answer_ids))
        label = '32' if pos == 0 else '32u'
        for suffix, payload in [('questions', body), ('answers', '# 정답 · 해설 · 유형'+answers)]:
            relative = f'output/260908/260908_02_math2_{label}_{suffix}_review.md'
            banner = ('# 검토용 사본 — 미투입·정본 아님\n\n'
                      f'> 원통합본: `{p}`\n'
                      '> 원문 구간을 그대로 보존한 대조용 사본이다. 아래 과거 신규성·통과 주장은 재승인되지 않았다.\n'
                      '> 식별자·태그·범위·난이도 표준화 및 외부 정답·품질감사는 미완료다.\n\n')
            full = banner + payload
            target = ROOT / relative
            if target.exists() and target.read_text(encoding='utf-8') != full:
                raise RuntimeError('Conflicting existing copy: '+relative)
            target.write_text(full, encoding='utf-8', newline='\n')
            reread = target.read_text(encoding='utf-8')
            assert reread[len(banner):] == payload
            manifest['copies'].append(dict(path=relative, bytes=target.stat().st_size,
                                          sha256=sha(target.read_bytes()), content_equal=True))
        for item in ids:
            queue.append({'source': p, 'item': item, 'status': 'PENDING', 'release': 'BLOCKED'})
    transcript = frozen[SOURCES[2]].decode('utf-8-sig')
    groups = re.split(r'^## #(\d) 단원:', transcript, flags=re.M)
    corpus_ids = []
    for i in range(1,len(groups),2):
        corpus_ids += [f'{groups[i]}-{x}' for x in headings(groups[i+1])]
    corpus_expected = [f'{c}-{i}' for c,n in [(1,15),(2,23),(3,32),(4,23)] for i in range(1,n+1)]
    manifest['coverage'].append(checked('corpus',corpus_expected,corpus_ids))
    for p,n in zip(SOURCES[3:],[25,40]):
        ids = headings(frozen[p].decode('utf-8-sig'))
        manifest['coverage'].append(checked(p,[str(i) for i in range(1,n+1)],ids))
    confirmed = {('32','A1'): '2-21', ('32','C6'): '3-19', ('32','C7'): '3-10',
                 ('32u','B2'): '1-4', ('32u','D7'): '2-23'}
    for row in queue:
        label = '32' if row['source'] == SOURCES[0] else '32u'
        if (label,row['item']) in confirmed:
            row.update(status='STRUCTURAL_OVERLAP_REPRODUCED', nearest_corpus=confirmed[label,row['item']])
    manifest['review_queue'] = queue
    for p,data in frozen.items():
        assert (ROOT/p).read_bytes() == data, 'Source changed during preparation: '+p
    path = OUT/'rev/260908_04_math2_64_manifest.json'
    path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('STRUCTURAL_COPY_OK: sources=5 unchanged; questions=64 answers=64 copies=4 content_equal=4; warnings=0')
    print('COMPARISON_INPUTS: corpus=93 prior25=25 prior40=40; target=64')
    print('REVIEW_PROGRESS: reproduced_overlap=5 pending=59; mathematical_audit=NOT_RUN; release=BLOCKED')

if __name__ == '__main__':
    main()
