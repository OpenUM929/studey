"""Record the current partial review without rewriting frozen inputs."""
from pathlib import Path
import hashlib
import json
import sys
sys.path.insert(0, 'tools')
from textpatch import patch, append_row

home=Path('output/260908/rev')
manifest_path=home/'260908_04_math2_64_manifest.json'
manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
changes=[]
for row in manifest['sources']+manifest['copies']:
    p=Path(row['path'])
    if sha(p)!=row['sha256']:
        changes.append({'path':row['path'],'old_bytes':row['bytes'],'old_sha256':row['sha256'],
                        'current_bytes':p.stat().st_size,'current_sha256':sha(p)})
assert {c['path'] for c in changes}=={r['path'] for r in manifest['sources'][3:]}, changes
result=json.loads((home/'260908_07_math2_32u_selfcheck.json').read_text(encoding='utf-8'))
assert len(result['rows'])==32 and result['warning_count']==1
report='260909_01_math2_32u_self_review.md'
next_step='변경된25·40 버전/소유권 확인 후 별도 입력 재동결(기존 동결 보존); 남은32제 자체 계산과59문항 유사성 검수를 이어간다. 32u 완료 계산32개는 반복 작성하지 않는다.'
state=dict(stage='자체 검산 부분 완료; 유사성 입력 ▲ blocked',owner='Codex/OMX 메인 루프',
           runtime_identity='/root',model_depth='미노출',independent=False,
           source_manifest=str(manifest_path),manifest_sha256=sha(manifest_path),input_changes=changes,
           completed_units=['32u/'+r['item'] for r in result['rows']],
           artifacts=[dict(path=str(p),sha256=sha(p),bytes=p.stat().st_size) for p in [home/report,home/'260908_07_math2_32u_selfcheck.py',home/'260908_07_math2_32u_selfcheck.json']],
           evidence='32u 32/32 answer match; explanatory_warnings=1; missing/extra/duplicate=[]; exit=0',
           blockers=['25/40 input hash drift','32u ID ruling absent','external audit 0/64'],
           quota='리소스 소진 공지 없음; 컨텍스트 체크포인트',next=next_step,
           next_validation='python -X utf8 output/260908/rev/260908_07_math2_32u_selfcheck.py',
           exclusive_outputs='이 보고서/계산 증거/메인루프 WIP; 원문 세트 및 기준 파일은 읽기 전용')
(home/'260909_01_math2_resume_checkpoint.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
wip=Path('analysis/wip/mainloop_260908_math2_64_revision.md')
old=wip.read_text(encoding='utf-8')
anchor=next(l for l in old.splitlines() if l.startswith('NEXT:'))
note='## 260909 자체 검산 슬라이스\n\n25·40 해시 변경으로 기존 NEXT 대조 분기는 ▲ blocked. 변경되지 않은32u 계산을 독립 의존성의 안전 분기로 먼저 수행했다.\n32/32 정답 일치, A4 함정 설명 오류1건, 원문 무변경. 코드 초기 실패2건은 계산 증거 코드만 고쳐 재실행 exit0.\n상태/해시/소유자/정확한 재개: `output/260908/rev/260909_01_math2_resume_checkpoint.json`.\n외부 검증0/64, 교체0, 정본 등록0. 명명 판정은 여전히 요청서만 확인됨.\n\n'
if note not in old:
    patch(str(wip),[(anchor,note+'NEXT: '+next_step)])
line=f'- [{report}]({report}): 32u 정답 자체검산32/32, 설명 결함1건, 25·40 입력 변경2건. 전체 작업 미완료.\n'
p=home/'HISTORY.md'; old=p.read_text(encoding='utf-8')
if line not in old: patch(str(p),[(old,old+'\n'+line)])
row=f'| 260909 | 3 | Codex/OMX proposal | 32u 자체 검산 | 정답32/32 일치; A4 설명 오류1건; 25/40 입력 변경 | {report} | flagged | 입력 변경 확인; 남은 계산·유사성 검수; 외부 게이트 유지 |'
p=home/'_index.md'
if row not in p.read_text(encoding='utf-8'): append_row(str(p),row)
row=f'| 260909 | [32u 자체 검산](../output/260908/rev/{report}) | Codex/OMX proposal: 정답32/32 일치·설명결함1건; 입력변경2건; 외부0/64·교체0·정본0 | 검토필요 | output/260908/rev/{report} |'
p=Path('analysis/REV_LOG.md')
if row not in p.read_text(encoding='utf-8'): append_row(str(p),row)
print('CHECKPOINT_RECORDED: answer_checks=32; warnings=1; input_drift=2; release=BLOCKED')
