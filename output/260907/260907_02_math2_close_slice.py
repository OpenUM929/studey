"""Record bounded implementation evidence; never turn pending review into approval."""
from pathlib import Path
import csv,hashlib,json,re,subprocess,sys
sys.path.insert(0,str(Path('tools').resolve()))
from textpatch import patch,insert_before,append_row
root=Path('output/260907')

# Full set identifier coverage, with untouched novelty judgments explicitly unperformed.
p=Path('output/260829/260829_02_math2_comprehensive_25.md')
t=p.read_text(encoding='utf-8-sig')
notes=json.loads((root/'260907_02_math2_novelty_notes.json').read_text(encoding='utf-8'))
header=['item_id','type_id','invariant','non_numeric_axis_1','non_numeric_axis_2','structural_difference','nearest_prior','verdict']
with p.with_suffix('.novelty.tsv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f,delimiter='\t'); w.writerow(header)
    for n,tag in re.findall(r'^\*\*(\d+)\.\*\*.*?`?\[(SM2-[^\]\n]+)\]',t,re.M|re.S):
        q=notes.get(n)
        w.writerow([n,tag.split()[0],q['invariant'] if q else 'Retained item; novelty not re-evaluated',q['axis1'] if q else '',q['axis2'] if q else '',q['difference'] if q else '',f'output/260907/260907_02_math2_revision_baseline.json#{n}', 'PASS' if q else 'BLOCKED'])

# Preserve dated history, append current implementation rather than rewriting prior audit findings.
audit=Path('output/260907/rev/260907_01_item_quality_audit.md')
block='''## 260908 후속 이행 기록 — Codex/OMX, proposal

- 사용자 `260907_prompt.md` 실행: 25제 3·4·6·7·22·25(1) 교체안과 정답/해설6행·채점기준2곳 반영.
- 40제28·29·30 답란에 기준 표현과 동치 표현 추가. 일반 N축 면제8건과 증명6(1)은 여전히 판정 대기.
- 문제지/답지는 별도 검토용4파일로 보관하고 `output/_index.md`65행은 전부 검토필요로 기록.
- 작성자 계산6단위+동치성3문항, 문서정합65문항/채점13건 통과. **외부 전수 재게이트 미실행**.
- 저장 관리 영구 절차 반영. 전역 assurance gate4건 실패는 미해결; 자·타 작성자WIP는 무변경.
- 세부 이행·검증 범위·미완료·재개: `output/260907/rev/260907_02_math2_implementation_report.md`.
- 이 기록은 기존 검토의 binding 판정·정본 승인·학생 투입 허가가 아니다.

'''
if block.strip() not in audit.read_text(encoding='utf-8'): insert_before(audit,'## history',block)
row='| 260908 | [25제 교체·40제 동치답 이행](../output/260907/rev/260907_02_math2_implementation_report.md) | main-loop(Codex/OMX) proposal: 교체6건·답해설6행·채점2곳·동치답3문항·분리 검토본4개·index65행. 작성자 계산/문서정합과 외부 검증을 구별. 전역 게이트4건 실패 및 외부 전수감사 대기 | 반영 / 검토필요 / 정본0 | output/260829/260829_02_math2_comprehensive_25.md · output/260822/공통수학2_도형의방정식_모의40.md · output/_index.md |'
if row not in Path('analysis/REV_LOG.md').read_text(encoding='utf-8-sig'): append_row('analysis/REV_LOG.md',row)

# Search boundary is explicit: excludes this run's generated evidence/report and runtime state.
needles=['260829_02_math2_comprehensive_25','공통수학2_도형의방정식_모의40']
paths=[]
for directory in ['analysis','output','docs','web']:
    paths.extend(p for p in Path(directory).rglob('*') if p.is_file() and p.suffix in ['.md','.json','.py'])
paths.append(Path('README.md'))
found=[]
for p in sorted(paths):
    if p.as_posix().startswith('output/260907/') or p.as_posix()=='analysis/wip/mainloop_260907_math2_revision_release.md': continue
    try: txt=p.read_text(encoding='utf-8-sig')
    except UnicodeError: continue
    if any(n in txt for n in needles):
        state='historical_print_not_current' if 'output/test2/260830/' in p.as_posix() else 'current_or_historical_reference_preserved'
        found.append({'path':p.as_posix(),'disposition':state,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(root/'260907_02_math2_reference_scan.json').write_text(json.dumps({'boundary':'analysis/output/docs/web .md .json .py plus README; excludes output/260907/** and own WIP; after implementation','count':len(found),'files':found},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

set_path=Path('output/260829/260829_02_math2_comprehensive_25.md')
commands=[['python','-X','utf8','output/260907/260907_02_math2_selfcheck.py'],['python','-X','utf8','output/260907/260907_02_math2_verify_artifacts.py'],['python','-X','utf8','tools/check_assurance_contract.py'],['python','-X','utf8','tools/check_novelty_ledger.py','--set',str(set_path),'--ledger',str(set_path.with_suffix('.novelty.tsv')),'--required-count','25']]
logs=[]
for cmd in commands:
    proc=subprocess.run(cmd,capture_output=True,encoding='utf-8',errors='replace')
    logs.append({'command':cmd,'exit':proc.returncode,'stdout':proc.stdout,'stderr':proc.stderr})
(root/'260907_02_math2_validation_log.json').write_text(json.dumps(logs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert logs[0]['exit']==logs[1]['exit']==0

wip=Path('analysis/wip/mainloop_260907_math2_revision_release.md')
old=wip.read_text(encoding='utf-8-sig')
new=old.replace('20,23,39,40','20,23,38,40').replace('updated: 2026-09-07','updated: 2026-09-08')
new=new[:new.rfind('NEXT:')]+'''## 260908 슬라이스 마감

- STATUS: IN_PROGRESS. author=메인 루프(Codex/OMX). 외부 검증·정본화는 ▲ blocked.
- 완료: 교체6/6(3·4·6·7·22·25(1)), 정답·해설6/6, 채점2/2, 동치답3/3,
  검토용 분리4/4, index65/65(정본0), 저장 지침5파일, 이행 보고·REV_LOG·기존 audit 후속 기록.
- 초기 표는 착수 시점 값이다. 현재 전체/완료/남음은 이 절과 이행 보고 §9를 따른다.
- 외부 재게이트65/65 미실행. 자기계산은 교체6단위+40제3문항뿐이며 나머지56문항과25(2)(3)은 새 계산 미수행.
- novelty.tsv는25행: 교체6건 작성자PASS 주장, 유지19건BLOCKED(미재평가). 신규성 최종 통과 아님.
- 원본동형8건 번호 중 초기39는 오기: audit 전수 행 대조로38로 정정. 39번은 해당 없음.
- ARTIFACT_CHECK_OK: 질문65/답65/채점13/index65, 누락·중복·추가=[], warnings0, exit0.
- 전역 assurance-contract:4failures, exit1. 기존 hold-user WIP 및 ruler 계층 재생성 실패. 보호대상 무변경.
- 재개는 `output/260907/260907_02_math2_resume.md` 사용. 완료 문항 재생성 금지.
- 기준선: `260907_02_math2_revision_baseline.json` sha256=7b45ffe229ce7daa7d5bf8a3de756f58f819a05f926578398056da1c435aea05.
- 현행 hash는 `output/260907/260907_02_math2_manifest.json`; 검증 출력은 validation_log.json.
- quota/reset 미관측, 실제 모델·depth 미노출. 예약 미구성(외부 승인 대기). 자원 고갈로 허위 표기하지 않음.
- 외부 Opus는 사용자 직접 별도 실행; 배타 작성권/변경 충돌 확인 후 회신을 로컬에서 읽는다.

NEXT: 외부 회신 도착 여부 확인 → 없다면 미검산56문항+25(2)(3)의 작성자 자기검산을 한 배치씩 보강 → 외부 전수 solve-back·N/V/A·예외·자 실패 판정 → 승인 수정 후 파생본/index/보고서 동기화. 다음 검증: python -X utf8 output/260907/260907_02_math2_verify_artifacts.py
'''
patch(wip,[(old,new)])

files=[Path(n) for n in ['CLAUDE.md','AGENTS.md','README.md','analysis/DOC_LOCATION.md','analysis/catalog/AUTHORING_GUIDE.md','analysis/REV_LOG.md','output/_index.md',str(wip),'output/260829/260829_02_math2_comprehensive_25.md','output/260829/260829_02_math2_comprehensive_25.novelty.tsv','output/260822/공통수학2_도형의방정식_모의40.md']]
files.extend(p for p in root.rglob('*') if p.is_file() and ('260907_02' in p.name or p.name=='260907_01_item_quality_audit.md') and p.suffix!='.pyc' and not p.name.endswith('_manifest.json'))
manifest={p.as_posix():{'bytes':len(p.read_bytes()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(set(files))}
(root/'260907_02_math2_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'CLOSE_SLICE_OK reference_files={len(found)} manifest_files={len(manifest)} STATUS=IN_PROGRESS')
for log in logs: print('exit',log['exit'],' '.join(log['command']))
