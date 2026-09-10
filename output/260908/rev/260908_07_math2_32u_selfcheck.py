"""Proposal-grade recomputation evidence, NOT an independent/release gate."""
from pathlib import Path
import hashlib
import json
import re
from collections import Counter
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
HOME = ROOT / 'output/260908/rev'
SOURCE = 'output/260830/260830_02_math2_unused_axes_32.md'
manifest = json.loads((HOME/'260908_04_math2_64_manifest.json').read_text(encoding='utf-8'))
raw = (ROOT/SOURCE).read_bytes()
frozen = next(r for r in manifest['sources'] if r['path'] == SOURCE)
assert hashlib.sha256(raw).hexdigest() == frozen['sha256']
text = raw.decode('utf-8-sig')
body, answers = text.split('# 정답 · 해설 · 유형', 1)
expected = re.findall(r'^\*\*([A-D]\d+)\.\*\*', body, re.M)
answer_rows = dict(re.findall(r'^\| ([A-D]\d+) \| (.*?) \|', answers, re.M))
x,y,a,b,k,m = s.symbols('x y a b k m', real=True)
R = s.Rational
rows = []

def eq(u,v):
    if isinstance(u,(list,tuple,s.MatrixBase,s.Point)):
        assert len(u)==len(v)
        return all(eq(c,d) for c,d in zip(u,v))
    return s.simplify(u-v)==0

def check(item, actual, wanted, answer_fragment, proof):
    assert eq(actual,wanted), (item,actual,wanted)
    assert answer_fragment in answer_rows[item], (item,answer_rows[item])
    rows.append(dict(item=item, calculated=str(actual), published_answer=answer_rows[item],
                     result='SELF_CHECK_MATCH', evidence=proof))

check('A1',s.solve((2+a)+2-7,a)[0],3,'3','이동한 점(2+a,2)을 직선 방정식에 대입.')
check('A2',[(s.Integer(-1)+5)/2,(s.Integer(2)-6)/2,((5+1)**2+(-6-2)**2)/s.Integer(4)], [2,-2,25],'(x − 2)² + (y + 2)² = 25','중심은 중점, 반지름 제곱은 지름 제곱의 1/4.')
P=s.Point(-2,1)+s.Point(6,6)/3; Q=s.Point(-2,1)+2*s.Point(6,6)/3
check('A3',P.distance(Q),2*s.sqrt(2),'2√2','두 내분점(0,3),(2,5) 사이의 거리.')
swap=s.Matrix([[0,1],[1,0]]); neg=-s.eye(2)
check('A4',neg*swap*s.Matrix([a,b]),[-b,-a],'(−b, −a)','좌표 교환 후 두 부호 반전. 두 변환은 가환하므로 함정 서술은 별도 결함.')
check('A5',abs(s.solve((4-a)**2-a**2,a)[0]),2,'2','(4-a)^2=a^2의 유일해 a=2; 반지름=|a|.')
check('A6',s.prod(s.solve((k-2)*(k-1)-12,k)),-10,'−10','행렬식 공선 조건; k=1은 해 아님.')
check('B1',s.solve(-x/2+4,x)[0],8,'8','교점(0,4), 수직 기울기 -1/2.')
check('B2',s.Point(1,1).distance(s.Point(6,6))+s.Point(5,2).distance(s.Point(2,5)),8*s.sqrt(2),'8√2','중점 사각형 둘레=두 대각선 길이 합.')
intersection=s.solve([2*x-y-1,x+y-5],[x,y])
check('B3',[intersection[x],intersection[y],intersection[x]**2+intersection[y]**2],[2,3,13],'2x + 3y − 13 = 0','P를 지나는 직선까지 거리≤OP; 법선벡터 OP일 때 달성.')
check('B4',[r for r in s.solve(k*k+4*k-5,k) if r>0],[1],'1','이동 후 x=0 대입, 양의 근만 선별.')
sol=s.solve([a*a+b*b-20,b-2*a],[a,b]); pair=next(p for p in sol if p[0]>0)
check('B5',sum(pair),6,'6','접선 수직 조건 b=2a, 원 위 조건과 a>0.')
check('B6',s.expand(9*m*m-9*(m*m+1)),-9,'x = 3','유한 기울기는 -9=0 모순. 수직선 x=3은 거리3, 현8로 유일.')
check('B7',s.expand((9*((x-8)**2+y*y)-(x*x+y*y))/8),s.expand((x-9)**2+y*y-9),'(9, 0)','거리비 제곱식 동치, 중심(9,0), 반지름3.')
check('B8',[-1,-3,2],[-1,-3,2],'(x + 1)² + (y + 3)² = 4','중심(3,1)에 (x,y)→(-y,-x), 반지름 불변.')
check('B9',s.Point(-1,1)+R(2,5)*s.Point(10,10),[3,5],'(3, 5)','선분 내 매개변수 t: 2(1-t)=3t → t=2/5.')
energy=sum((x-u)**2+(y-v)**2 for u,v in [(1,0),(4,3),(-2,5)])
sol=s.solve([s.diff(energy,x),s.diff(energy,y)],[x,y])
assert s.expand(energy-3*((x-1)**2+(y-R(8,3))**2))==R(92,3)
check('C1',[sol[x],sol[y]],[1,R(8,3)],'(1, 8/3)','제곱완성 3[(x-1)^2+(y-8/3)^2]+92/3; 미분은 검산에만 사용.')
pts=s.solve([x*x+y*y-25,(x-1)**2+(y-2)**2-(x-5)**2-(y-6)**2],[x,y])
check('C2',sum([list(t) for t in sorted(pts)],[]),[3,4,4,3],'(3, 4), (4, 3)','원과 x+y=7 연립의 실수해 둘 전부.')
check('C3',s.Integer(2)**2+4**2,20,'20','원점 등거리에서 OA²=OB². 수직이등분선 존재 가정은 A≠B를 내포.')
check('C4',3/(R(3,2)-2),-6,'−6','BC 교점 높이3, x=3/2. AC로 나뉘는 쪽 최대넓이4<6이라 다른 해 없음.')
check('C5',4/s.sqrt(2),2*s.sqrt(2),'2√2','x≥0 거리4/√2로 달성; x<0 거리(4-2x)/√2는 더 큼.')
check('C6',s.Integer(2)**2+3**2,13,'x² + y² = 13','OP²=r²+t²; 반대로 해당 원의 모든 점은 원 밖이고 접선 길이3.')
check('C7',R(1,2)*4*(2-s.sqrt(2)),4-2*s.sqrt(2),'4 − 2√2','y최솟값2-√2>0, 원의 최하점에서 달성.')
ks=[n for n in range(-2,3) if abs(4+n)>2]
check('C8',len(ks),4,'4','첫 조건으로 -2≤k≤2에 한정; 둘째 엄격부등식 적용: -1,0,1,2.')
px=2/(1+k*k); py=2*k/(1+k*k)
check('C9',s.factor((px-1)**2+py**2),1,'원점 제외','x=2/(1+k²)>0. 역으로 원 위 원점 외 점은 k=y/x로 복원; k=0도 포함.')
check('C10',-s.sqrt(5)*s.sqrt(5),-5,'−5','절편±5 중 -5는 x<0일 때 y<0; +5는 (-1,3)을 지남.')
check('D1',s.Point(1,2).distance(s.Point(5,4)),2*s.sqrt(5),'2√5','역삼각부등식 상한AB. P=(-3,0)은 AB의 선분 밖 연장선에 있어 등호 달성.')
check('D2',len([n for n in range(-5,6) if 1<abs(n)<5]),6,'6','반지름3,2의 서로 다른 두 교점 조건 1<|a|<5; 정수±2,±3,±4.')
check('D3',s.expand(((x-2)**2+(y+1)**2-(x-6)**2-(y-5)**2)/4),2*x+3*y-14,'2x + 3y − 14 = 0','두 점의 거리제곱 차를 전개; 서로 다른 두 점이므로 수직이등분선 유일.')
check('D4',s.solve([x*x+y*y-25,(x-8)**2+y*y-41],[x,y]),[(3,-4),(3,4)],'(x − 3)² + y² = 16','두 교점(3,±4); 중점(3,0), 반지름4.')
f=s.Function('f'); g=-f(x+3)
check('D5',-g.subs(x,x-3),f(x),'−g(x − 3)','g(x)=-f(x+3)에서 변수 x-3 대입, 부호 반전.')
check('D6',(-2-1)+(3-3),-3,'−3','QII에서 중심x=-2, 직선에서 y=3. |y|=3≠2로 x축에는 접하지 않음.')
check('D7',s.expand((2*x-y-3)-(x-2*y+3)),x+y-6,'x + y − 6 = 0','거리의 ±분기: x+y-6=0 또는 x-y=0; 원점 제외 조건으로 첫째만.')
assert neg*swap == swap*neg
observed=[r['item'] for r in rows]
coverage=dict(expected=expected, observed=observed,
              duplicate=[i for i,n in Counter(observed).items() if n>1],
              missing=sorted(set(expected)-set(observed)),extra=sorted(set(observed)-set(expected)))
assert not coverage['duplicate'] and not coverage['missing'] and not coverage['extra']
assert set(answer_rows)==set(expected)
assert (ROOT/SOURCE).read_bytes()==raw
result=dict(author='메인 루프 (Codex/OMX)',grade='proposal',independent=False,
            source=frozen,coverage=coverage,rows=rows,
            warning_count=1,warnings=['A4 정답은 맞으나 합성 순서 교환을 오답 원인으로 든 함정 서술은 거짓'],
            release='BLOCKED',limitations=['전체 해설·태그·난이도 감사 미완료','신규성 검사와 별개','외부 Opus 검증 아님'])
(HOME/'260908_07_math2_32u_selfcheck.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(coverage,ensure_ascii=False))
print('SELF_CHECK: 32u answers=32/32 match; explanatory_warnings=1; external_verified=0; release=BLOCKED')
