"""Read current delivery files; never regenerate questions or historical evidence."""
from pathlib import Path
from collections import Counter
import contextlib
import hashlib
import io
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'output/260910'

def main():
    expected = [f'{g}/{n}' for g in 'AB' for n in range(1, 26)]
    observed, mismatches, artifacts = [], [], []
    for group, number in [('A', '01'), ('B', '02')]:
        prefix = f'260910_{number}_info_composite_{group.lower()}'
        question_path = OUT / (prefix + '_questions_review.md')
        answer_path = OUT / (prefix + '_answers_review.md')
        questions = question_path.read_text(encoding='utf-8-sig')
        answers = answer_path.read_text(encoding='utf-8-sig')
        numbers = re.findall(r'^\*\*(\d+)\.\*\*', questions, re.M)
        observed.extend(f'{group}/{n}' for n in numbers)
        codes = re.findall(r'```python\n(.*?)\n```', questions, re.S)
        keys = re.findall(r'^\*\*정답: `(.*?)`\*\*', answers, re.M)
        assert len(codes) == len(keys) == len(numbers) == 25
        assert re.findall(r'^\| (\d+) \|', answers, re.M) == numbers
        assert '정답:' not in questions and '해설:' not in questions
        for n, code, key in zip(numbers, codes, keys):
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                exec(compile(code, str(question_path), 'exec'), {})
            actual = stream.getvalue().strip().replace('\n', ' ⏎ ')
            if actual != key:
                mismatches.append({'id': f'{group}/{n}', 'actual': actual, 'key': key})
        for kind in ['questions', 'answers']:
            for ext in ['md', 'html']:
                path = OUT / f'{prefix}_{kind}_review.{ext}'
                data = path.read_bytes()
                if ext == 'html':
                    html = data.decode('utf-8-sig')
                    assert html.count('<section>') == html.count('</section>') == 25
                artifacts.append({'path': path.relative_to(ROOT).as_posix(),
                                  'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
    result = {'executor': 'Codex/OMX', 'independent': False,
              'command': 'python -X utf8 analysis/wip/260910_info_delivery_check.py',
              'expected': expected, 'observed': observed,
              'duplicates': [x for x, n in Counter(observed).items() if n > 1],
              'missing': sorted(set(expected) - set(observed)),
              'extra': sorted(set(observed) - set(expected)),
              'answer_mismatches': mismatches, 'artifacts': artifacts,
              'warnings': ['independent_audit_missing', 'textbook_not_integrated',
                           'semantic_novelty_not_certified', 'highest_difficulty_not_certified',
                           'student_error_evidence_missing', 'set_id_unissued',
                           'visual_print_check_not_run'],
              'release': 'BLOCKED'}
    destination = OUT / 'rev/260910_11_info_delivery_check.json'
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return int(any(result[x] for x in ['duplicates', 'missing', 'extra', 'answer_mismatches']))

if __name__ == '__main__':
    raise SystemExit(main())
