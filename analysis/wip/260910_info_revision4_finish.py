"""Finalize author-side bookkeeping and verify current draft files."""
from pathlib import Path
import ast
import hashlib
import json
import re
import sys
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.textpatch import patch, append_row, PatchError

def append(path, marker, text):
    p=ROOT/path
    old=p.read_text(encoding='utf-8')
    if marker not in old:
        patch(p,[(old,old.rstrip()+'\n\n'+text+'\n')])

e=json.loads((ROOT/'output/260910/260910_03_info_selfcheck.json').read_text(encoding='utf-8'))
assert len(e['expected_ids'])==50 and e['expected_ids']==e['observed_ids']
assert all(not e[k] for k in ['missing','extra','duplicates','answer_mismatches'])
for row in e['inputs']+e['artifacts']:
    data=(ROOT/row['path']).read_bytes()
    assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256'],row['path']
for group,num in [('a','01'),('b','02')]:
    stem=f'output/260910/260910_{num}_info_composite_{group}'
    q=(ROOT/(stem+'_questions_review.md')).read_text(encoding='utf-8')
    a=(ROOT/(stem+'_answers_review.md')).read_text(encoding='utf-8')
    combined=(ROOT/(stem+'_review.md')).read_text(encoding='utf-8')
    assert len(re.findall(r'^\*\*\d+\.\*\*',q,re.M))==25
    assert '정답:' not in q and '해설:' not in q
    assert len(re.findall(r'^\| \d+ \| \*\*`',a,re.M))==25
    assert q.split('**1.**',1)[1] in combined
    assert a.split('## 정답표',1)[1] in combined
    for kind in ['questions','answers']:
        html=(ROOT/(stem+'_'+kind+'_review.html')).read_text(encoding='utf-8')
        HTMLParser().feed(html)
        assert html.count('<section>')==html.count('</section>')==25
for path in (ROOT/'analysis/wip').glob('260910_info_*.py'):
    ast.parse(path.read_text(encoding='utf-8-sig'))
validation=dict(executor='Codex/OMX',independent=False,revision=4,
    hashes_verified=len(e['inputs']+e['artifacts']),saved_answers=50,
    exact_ids=e['observed_ids'],missing=[],extra=[],duplicates=[],
    split_md=4,html_sections=[25,25,25,25],visual_print_test='not_run',
    warnings=e['warnings'],release='BLOCKED')
(ROOT/'output/260910/rev/260910_09_info_revision4_validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2),encoding='utf-8')

append('output/260910/260910_04_info_creation_report.md','## 10. revision4', '''## 10. revision4 — 잔여 경미 변형 후보7개도 교체한 현재 판본

§9에서 독립 검토 후보로 남겨 둔 **A17·A21·B2·B9·B15·B16·B21도 보수적으로 교체**했다. 사용자의 ‘유사 풀이 배제’ 지시에 따른 저자 수정이며, 판정 권한을 행사한 것이 아니다. 이번 실행의 교체는 총14개이고 두 묶음은 서로 겹치지 않는다. 이전 문항의 코드와 관측은 revision2 archive 및 revision3 comparison JSON에 보존했다.

새 구조는 상태 전이 횟수표·처음 누락된 값 탐색·순환 도착 빈도·부분수열 선택·구간 이분 탐색·삼각형 하단부터 최적값 전달·합계 검사와 선택 복구이다. 정본 유형ID를 새로 발급하지 않았으며 기존 승인 유형들을 결합했다.

현재 비교 기록: [revision4 50문항](rev/260910_08_info_revision4_comparison.md), [원본·산출물 해시 및 코드](rev/260910_08_info_revision4_comparison.json). 앞선 revision3 보고서의 잔여7개는 현재 제품에서 교체됐으므로 그대로 인용하지 않는다. **이번 작성자 비교에서 지적한 교체 후보는 모두 반영했지만, 모든 의미상 유사성이 제거됐다는 독립 판정은 아니다.**

검증: `python -X utf8 analysis/wip/260910_info_composite_author.py --write`, `python -X utf8 analysis/wip/260910_info_revision4_review.py`, `python -X utf8 analysis/wip/260910_info_register_drafts.py`, `python -X utf8 analysis/wip/260910_info_revision4_finish.py`. 저장 코드/작성정답50/50, 입력·제품 해시16/16, ID 누락·초과·중복0, 문제/답 MD4·HTML4 각각25문항, 통합본과 분리본 내용 일치. 자체 스크립트 AST 구문검사 성공. [검증 요약](rev/260910_09_info_revision4_validation.json). 브라우저 인쇄 시각 검사는 미실행이다.

### 현재 직접 열어 볼 파일

| 묶음 | 문제지 | 정답·해설 |
|---|---|---|
| A형25 | [문제 HTML](260910_01_info_composite_a_questions_review.html) | [답 HTML](260910_01_info_composite_a_answers_review.html) |
| B형25 | [문제 HTML](260910_02_info_composite_b_questions_review.html) | [답 HTML](260910_02_info_composite_b_answers_review.html) |

모든 링크는 실제 저장된 revision4를 가리킨다. `output/_index.md` 마지막 revision4 표가 현행이다. 검토필요·미투입을 유지한다.

### 아직 완료할 수 없는 부분

교과서33장 선행 승인·정제가 없어 모든 참고자료 활용은 미완료이며, 비프로그래밍 영역 보완도 남았다. 실제 학생 정보 오답, 정식 세트ID 정책, 외부 감사0/50도 미해소다. 기존 개발자 지침상 외부 Opus 전용 권한을 Astra나 작성자 스스로 대체할 수 없다. 따라서 **사용자 전체 요청은 ▲ blocked**이며, 이 파일들을 ‘전체 자료 활용 최종본’ 또는 ‘독립 감사 완료본’으로 표시하지 않는다.

REV_LOG는 혼합 개행 보호가 걸리면 원장을 정규화하지 않고 다음 추적 초안을 보존한다:

`| 260910 | 정보50 revision4 저자 수정 | Codex/OMX: 유사 구조 후보14개 교체, 자체검산50/50, 외부0/50 | 검토필요 | output/260910/260910_04_info_creation_report.md |`
''')
append('output/260910/rev/HISTORY.md','## 260910 revision4 final author pass',
       '## 260910 revision4 final author pass\n\n추가7개 교체, 이번 총14개. 현행 비교260910_08, 검증260910_09. 50/50 자체검산, 외부0/50. 교과서 및 권한 선행 조건 미해소. 제품 배포BLOCKED.')
append('analysis/wip/mainloop_260908_math2_64_revision.md','### 260910 revision4 checkpoint',
'''### 260910 revision4 checkpoint

owner=/root; executor=Codex/OMX; model/depth unexposed; no native/external lanes. Continued rather than stopping at revision3: A17,A21,B2,B9,B15,B16,B21 replaced, total14 this turn. Current comparison50 exactIDs, normalized current-pair1225 matches0; not semantic audit. Saved answers50/50; source/product hashes16/16; MD4+HTML4 split checks. Report section10 and index revision4 current. Historical revision3 comparison retained; its script refuses use against revision4. No source/student/canonical policy/ruler changes.

NEXT: full-reference requirement is blocked on textbook33 naming policy/approved operating PRD/refinement. Read actual approval artifact before processing; do not invent corpusID or treat the user's request as external arbiter evidence. Then incorporate nonprogramming coverage as appropriate, recompare and independently audit. Missing student errors and setID policy remain. External0/50; cannot activate Astra replacement under developer authority. Math remaining50 review/new hardest50 remain pending, not replaced by info work. First verification: python -X utf8 analysis/wip/260910_info_revision4_review.py and python -X utf8 analysis/wip/260910_info_revision4_finish.py. Hash manifests: output/260910/260910_03_info_selfcheck.json and rev/260910_08_info_revision4_comparison.json. This is a bounded checkpoint, not whole-task completion. No manual compaction performed.
''')
append('output/260910/260910_05_info_opus_review_prompt.md','## revision4 dispatch hold',
       '## revision4 dispatch hold\n\n现행은 revision4(보고서§10). revision3의 잔여7개도 교체됐다. 실제 발주 전 입력 경로/해시·권한·예산 게이트를 다시 구성해야 한다. 이 준비본은 지금 실행하지 않는다. 독립 감사0/50.'.replace('现행','현행'))
index=ROOT/'output/260910/rev/_index.md'
row='| 260910 | 1 | Codex/OMX author-side proposal | info A/B revision4 | 후보14개 저자 교체; 자체검산50/50; 외부0/50 | 260910_08_info_revision4_comparison.md | 검토필요 | 교과서 선행승인·정제 및 외부 감사 |'
if row not in index.read_text(encoding='utf-8'):
    append_row(index,row)
ledger=ROOT/'analysis/REV_LOG.md'
row='| 260910 | 정보50 revision4 저자 수정 | Codex/OMX: 유사 구조 후보14개 교체, 자체검산50/50, 외부0/50 | 검토필요 | output/260910/260910_04_info_creation_report.md |'
if row not in ledger.read_text(encoding='utf-8'):
    try:
        append_row(ledger,row)
    except PatchError as exc:
        print('TRACE-PENDING:',exc)
print(json.dumps(validation,ensure_ascii=False))
