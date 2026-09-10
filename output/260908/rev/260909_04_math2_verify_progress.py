"""Structural verification and checkpoint only; never emits release PASS."""
from pathlib import Path
import hashlib,json,re,sys
from collections import Counter
sys.path.insert(0,'tools')
from textpatch import append_row,patch

home=Path('output/260908/rev'); sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected=[]; observed=[]
for label,name in [('32','260909_02_math2_32_selfcheck.json'),('32u','260908_07_math2_32u_selfcheck.json')]:
    result=json.loads((home/name).read_text(encoding='utf-8'))
    source=Path(result['source']['path'])
    assert sha(source)==result['source']['sha256']
    body=source.read_text(encoding='utf-8').split('# 정답 · 해설 · 유형')[0]
    expected += [label+'/'+i for i in re.findall(r'^\*\*([A-D]\d+)\.\*\*',body,re.M)]
    observed += [label+'/'+r['item'] for r in result['rows']]
    assert all(r['result']=='SELF_CHECK_MATCH' for r in result['rows'])
coverage=dict(expected=expected,observed=observed,duplicate=[i for i,n in Counter(observed).items() if n>1],
              missing=sorted(set(expected)-set(observed)),extra=sorted(set(observed)-set(expected)))
assert not coverage['duplicate'] and not coverage['missing'] and not coverage['extra']
candidate=json.loads((home/'260909_03_math2_candidate_recheck.json').read_text(encoding='utf-8'))
for row in candidate['source_records']: assert sha(Path(row['path']))==row['sha256']
reviewed=['32/A1','32/C6','32/C7','32u/B2','32u/D7']+[r['item'] for r in candidate['rows']]
assert len(reviewed)==len(set(reviewed))==14 and set(reviewed)<=set(expected)
remaining=[i for i in expected if i not in reviewed]
report='260909_04_math2_64_progress_review.md'
next_step='미판정50문항 유사성 검수부터 재개한다(목록은260909_04_math2_progress_checkpoint.json). 완료한64개 정답 계산과14개 재사용 근거는 다시 작성하지 않는다. 교체 단계 전에 관련 작성 정본을 읽고 교체 근거를 확정한다.'
artifacts=[home/name for name in ['260909_02_math2_32_selfcheck.py','260909_02_math2_32_selfcheck.json','260909_03_math2_candidate_recheck.py','260909_03_math2_candidate_recheck.json',report]]
state=dict(stage='자체 계산64/64; 유사성14/64; 교체 미착수',owner='Codex/OMX 메인 루프',runtime_identity='/root',
           model_depth='미노출',independent=False,coverage=coverage,similarity_reviewed=reviewed,similarity_pending=remaining,
           sources=candidate['source_records'],artifacts=[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size) for p in artifacts],
           validations=['32 selfcheck exit0 warnings3','32u prior evidence hash stable warnings1','candidate recheck exit0 stable inputs5'],
           blockers=['32u 명명 판정 미결','외부 필수 감사0/64'],release='BLOCKED',next=next_step,
           next_validation='python -X utf8 output/260908/rev/260909_04_math2_verify_progress.py',
           quota='소진 공지 없음; 컨텍스트 체크포인트',exclusive_write='본인 review 증거와 메인루프 WIP; 제품/기준은 읽기 전용')
(home/'260909_04_math2_progress_checkpoint.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
wip=Path('analysis/wip/mainloop_260908_math2_64_revision.md'); text=wip.read_text(encoding='utf-8')
anchor=next(l for l in text.splitlines() if l.startswith('NEXT:'))
note='## 260909 두 번째 슬라이스\n\n64/64 자체 정답 계산 일치(외부0/64). 기존후보9 재현으로 재사용14·미판정50.\n25·40 최신해시는 직전 체크포인트와 동일하고 작성 측 완료 NEXT 확인. 새로운 읽기 전용 입력 기록은260909_03 JSON; 이전 동결 보존.\n정확한 남은ID·해시·소유권·검증은 `output/260908/rev/260909_04_math2_progress_checkpoint.json`. 교체0·정본0.\n\n'
if note not in text: patch(str(wip),[(anchor,note+'NEXT: '+next_step)])
entry=f'- [{report}]({report}): 자체 정답64/64, 재사용14·미판정50; 최신 입력 별도 기록; 교체·최종 승인 미완료.\n'
p=home/'HISTORY.md'; text=p.read_text(encoding='utf-8')
if entry not in text: patch(str(p),[(text,text+'\n'+entry)])
row=f'| 260909 | 4 | Codex/OMX proposal | 두32제 정답·후보 검수 | 자체 정답64/64; 재사용14; 미판정50; 교체0 | {report} | flagged | 미판정50 검수 후 작성자 교체·외부 감사 |'
p=home/'_index.md'
if row not in p.read_text(encoding='utf-8'): append_row(str(p),row)
row=f'| 260909 | [64제 자체 계산·후보 재검수](../output/260908/rev/{report}) | 자체 계산64/64; 재사용14·미판정50; 제품무변경·교체0·외부0/64; 최신 입력 기록 | 검토필요 | output/260908/rev/{report} |'
p=Path('analysis/REV_LOG.md')
if row not in p.read_text(encoding='utf-8'): append_row(str(p),row)
print(json.dumps(coverage,ensure_ascii=False))
print('PROGRESS_VERIFIED: expected=64 observed=64 missing=0 extra=0 duplicate=0; similarity=14 pending=50; release=BLOCKED')
