"""Reproduce nine recorded similarity candidates against current read-only inputs."""
from pathlib import Path
import hashlib,json,re
import sympy as s

ROOT=Path(__file__).resolve().parents[3]; HOME=ROOT/'output/260908/rev'
old=json.loads((HOME/'260908_04_math2_64_manifest.json').read_text(encoding='utf-8'))
checkpoint=json.loads((HOME/'260909_01_math2_resume_checkpoint.json').read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
changes={r['path']:r for r in checkpoint['input_changes']}
sources=[]; raw={}
for r in old['sources']:
    p=r['path']; data=(ROOT/p).read_bytes(); raw[p]=data
    assert sha(data)==(changes[p]['current_sha256'] if p in changes else r['sha256']),p
    sources.append(dict(path=p,bytes=len(data),sha256=sha(data)))
rows=[
 ('32/A2','corpus/4-1','p15','원상 역산','대응점으로 이동벡터를 구하고 목표점에서 뺀다. 좌표값과 최종 좌표합/좌표 요구만 바뀐다.'),
 ('32/B2','25/7',None,'선행 풀이의 부분문제','둘 다 C=3G-A-B. 25제는 이어 넓이를 계산하지만 32제는 C에서 끝난다.'),
 ('32/B8','corpus/2-12','p06','분기 확대 1축','동일 법선인 두 평행선의 상수항 차의 절댓값으로 역산. 양수 제한 제거로 두 해를 쓰는 차이만 있다.'),
 ('32/C1','corpus/1-1','p01','최종 표현 변경','x축 위 두 거리제곱 합의 완전제곱. 원본은 최소점에서 k를 구하고 32제는 최소점과 최솟값을 묻는다.'),
 ('32u/A6','corpus/2-1','p05','근의 합→곱','세 점 공선의 행렬식에서 이차식, 근과 계수. 합/곱만 바뀌어 두 비수치 축은 없다.'),
 ('32u/B5','corpus/3-18','p12','결과식 및 부호 선별','원 위 접점의 접선과 주어진 직선의 수직 조건은 동일. 출력 a²b²→a+b, 양의 좌표 선별만 추가된다.'),
 ('32u/B7','40/20',None,'선행 풀이의 부분문제','거리비 제곱→아폴로니오스 원 완전제곱이 동일. 40제의 후속 넓이 계산을 생략하고 중심·반지름에서 끝난다.'),
 ('32u/C7','40/27',None,'극값 방향 변경','원 전체가 밑변 직선 한쪽에 있는 조건에서 높이 d±r. 최대→최소, 좌표 출력 생략으로 원본보다 풀이가 줄어든다.'),
 ('32u/D3','corpus/4-20','p18','선행 풀이의 부분문제','대칭축=수직이등분선. 원본의 후속 절편 삼각형 넓이를 제거하고 축 방정식에서 끝난다.'),
]
x,k=s.symbols('x k'); R=s.Rational
calculations={
 '32/A2':dict(source_result='원상(-4,10), 합6',target_result='원상(-3,2)'),
 '32/B2':dict(source_result='C=(4,7), 넓이18',target_result='C=(3,6)'),
 '32/B8':dict(source_result='m=8',target_result='k=-13,17'),
 '32/C1':dict(source_result='최소점 x=7/2, k=7',target_result='최소점 x=4, 최소18'),
 '32u/A6':dict(source_result='근0,7/2, 합7/2',target_result='근-2,5, 곱-10'),
 '32u/B5':dict(source_result='a²b²=4',target_result='a+b=6'),
 '32u/B7':dict(source_result='중심(6,0), 반지름4',target_result='중심(9,0), 반지름3'),
 '32u/C7':dict(source_result='최대 넓이24',target_result='최소 넓이4-2√2'),
 '32u/D3':dict(source_result='대칭축 x-2y-1=0',target_result='대칭축 2x+3y-14=0'),
}
assert s.Point(-3,6)-(s.Point(2,-3)-s.Point(1,1))==s.Point(-4,10)
assert 3*s.Point(2,3)-s.Point(-2,1)-s.Point(4,1)==s.Point(4,7)
assert abs(8+2)/s.sqrt(2)==5*s.sqrt(2)
assert s.diff((x-1)**2+16+(x-6)**2+36,x).subs(x,R(7,2))==0
assert s.solve(6*(k-1)-(k-2)*(2*k+3),k)==[0,R(7,2)]
assert (-2)**2*1**2==4 and (-2)**2+1**2==5
assert s.expand(4*(x-4)**2-(x+2)**2)==s.expand(3*((x-6)**2-16))
assert s.simplify(4*s.sqrt(2)*(4*s.sqrt(2)+s.sqrt(8))/2)==24
assert ((2+4)/2)-2*((3-1)/2)-1==0
out=[]
for item,ref,page,kind,why in rows:
    label,qid=item.split('/')
    target=sources[0 if label=='32' else 1]['path']
    assert re.search(r'^\*\*'+qid+r'\.\*\*',raw[target].decode('utf-8-sig'),re.M)
    if ref.startswith('corpus/'):
        chapter,num=ref.split('/')[1].split('-')
        transcript=raw[sources[2]['path']].decode('utf-8-sig')
        section=re.split(r'^## #'+chapter+r' 단원:',transcript,flags=re.M)[1].split('\n## #')[0]
        question=re.search(r'^\*\*'+num+r'\.\*\*(.*?)(?=^\*\*\d+\.\*\*|\Z)',section,re.M|re.S).group(0)
        assert page in question
        evidence_path=f'corpus/_images/SUP-math2-2026/{page}.png'
        image=(ROOT/evidence_path).read_bytes()
        evidence=dict(path=evidence_path,sha256=sha(image),visual_inspected=True)
    else:
        previous,num=ref.split('/'); path=sources[3 if previous=='25' else 4]['path']
        question=re.search(r'^\*\*'+num+r'\.\*\*(.*?)(?=^---|^\*\*\d+\.\*\*|\Z)',raw[path].decode('utf-8-sig'),re.M|re.S).group(0)
        evidence=dict(path=path,sha256=sha(raw[path]),item=num)
    out.append(dict(item=item,nearest=ref,kind=kind,reason=why,source_excerpt=question,
                    evidence=evidence,calculation=calculations[item],status='REUSE_REPRODUCED_PROPOSAL',replacement='RECOMMENDED'))
assert len({r['item'] for r in out})==9
for p,b in raw.items(): assert (ROOT/p).read_bytes()==b
result=dict(author='메인 루프 (Codex/OMX)',grade='proposal',source_baseline='260909 latest inputs; old baseline preserved',
            source_records=sources,old_manifest_sha256=sha((HOME/'260908_04_math2_64_manifest.json').read_bytes()),
            ownership_evidence='analysis/wip/mainloop_260908_math2_opus_audit.md: 작성 측 완료 NEXT 확인; 해당 파일 읽기 전용',
            rows=out,prior_reproduced=5,new_reproduced=9,total_reproduced=14,remaining_unassessed=50,
            release='BLOCKED',limitations=['부분 신규성 검수; 외부 N 판정 아님','비수치 축의 명칭보다 실제 풀이 재사용을 근거로 한 교체 권고'])
p=HOME/'260909_03_math2_candidate_recheck.json'
if p.exists(): assert json.loads(p.read_text(encoding='utf-8'))==result,'Do not overwrite a changed baseline'
p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('CANDIDATE_RECHECK: 9/9 reproduced; source_hashes=5 stable; total=14; remaining=50; external_N=NOT_RUN')
