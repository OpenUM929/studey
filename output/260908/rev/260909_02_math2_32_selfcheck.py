"""Non-independent mathematical recomputation; not a release gate."""
from pathlib import Path
import hashlib, json, re
from collections import Counter
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
HOME=ROOT/'output/260908/rev'
SOURCE='output/260830/260830_01_math2_graded_new_forms_32.md'
manifest=json.loads((HOME/'260908_04_math2_64_manifest.json').read_text(encoding='utf-8'))
frozen=next(r for r in manifest['sources'] if r['path']==SOURCE)
raw=(ROOT/SOURCE).read_bytes()
assert hashlib.sha256(raw).hexdigest()==frozen['sha256']
body,answers=raw.decode('utf-8-sig').split('# 정답 · 해설 · 유형',1)
expected=re.findall(r'^\*\*([A-D]\d+)\.\*\*',body,re.M)
answer_rows=dict(re.findall(r'^\| ([A-D]\d+)(?: ⚠️)? \| (.*?) \|',answers,re.M))
x,y,a,b,k,m=s.symbols('x y a b k m',real=True)
R=s.Rational
rows=[]
def eq(u,v):
    if isinstance(u,(list,tuple,s.MatrixBase,s.Point)):
        return len(u)==len(v) and all(eq(c,d) for c,d in zip(u,v))
    return s.simplify(u-v)==0
def check(item,actual,wanted,fragment,proof):
    assert eq(actual,wanted),(item,actual,wanted)
    assert fragment in answer_rows[item],(item,answer_rows[item])
    rows.append(dict(item=item,calculated=str(actual),published_answer=answer_rows[item],
                     result='SELF_CHECK_MATCH',evidence=proof))

check('A1',s.expand(((x-1)**2+(y-1)**2-(x-5)**2-(y-3)**2)/4),2*x+y-8,'2x + y − 8 = 0','거리제곱 차=0; 나눔 상수4는 0 아님.')
check('A2',[-(2-(-1)),-(2-4)],[-3,2],'(−3, 2)','이동량(3,-2)의 역벡터.')
check('A3',s.solve(6*m-4,m)[0],R(2,3),'2 : 3','m/n 비에서 n=1로 두어 6m=4n; 두 값 양수.')
check('A4',[s.det(s.Matrix([[3,4],[9,13]])),4*7-3*12+8],[3,0],'4x − 3y + 8 = 0','행렬식3≠0 비공선. 법선(4,-3)은 AB=(3,4)에 수직이고 C를 지남.')
check('A5',s.solve([a*a-9,b*b-9],[a,b]),[(-3,-3),(-3,3),(3,-3),(3,3)],'4개','두 축까지 거리3을 동시에 만족하는 중심 전부.')
T=s.Matrix([[0,-1],[1,0]])
check('A6',T.inv()*s.Matrix([5,-2]),[-2,-5],'(−2, −5)','x축 대칭 후 y=x 대칭 합성의 역행렬.')
assert s.det(s.Matrix([[4,2],[2,6]]))==20
check('B1',[(s.Point(1,2)+s.Point(7,10))/2,(s.Point(5,4)+s.Point(3,8))/2],[(4,6),(4,6)],'평행사변형이다','대각선 중점 일치. AB와 AD 행렬식20≠0이라 비퇴화.')
check('B2',3*s.Point(2,3)-s.Point(-1,5)-s.Point(4,-2),[3,6],'C(3, 6)','무게중심 방정식에서 세 번째 꼭짓점 유일.')
roots=s.solve(a*(a-1)-6,a)
assert all(s.Matrix([[r,2,-3],[3,r-1,4]]).rank()==2 for r in roots)
check('B3',s.prod(roots),-6,'−6','법선 행렬식0; 두 근 모두 확대행렬 rank2이므로 일치 아님.')
check('B4',[4*2-3*(-1)-11,4*5-3*3-11],[0,0],'4x − 3y − 11 = 0','중심(2,-1)과 외부점(5,3)을 지나는 유일 직선; 원 넓이 이등분.')
check('B5',[20/s.sqrt(3**2+4**2),R(20,25)*3,R(20,25)*4],[4,R(12,5),R(16,5)],'(12/5, 16/5)','원점의 직선상 정사영이 접점; 반지름은 거리.')
check('B6',s.expand((x-1)*(x-5)),s.expand((x-3)**2-4),'(x − 3)² − 4','최고차항1의 이차식이며 서로 다른 두 근1,5로 유일.')
ip=s.solve([x+2*y-3,2*x-y-1],[x,y])
check('B7',[ip[x],ip[y],ip[x]+3*ip[y]-4],[1,1,0],'x + 3y − 4 = 0','교점(1,1); 기울기 -1/3은 주어진 기울기3과 수직.')
check('B8',s.solve((k-2)**2-225,k),[-13,17],'17 또는 k = −13','|k-2|/5=3의 두 실수해; 제곱 후 둘 다 원식 만족.')
check('B9',[-1,2,s.sqrt(1+4-1)],[-1,2,2],'(−1, 2)','원래 중심(1,-2), 원점 대칭, 반지름 불변.')
energy=(x-2)**2+9+(x-6)**2+1
check('C1',s.expand(energy-2*(x-4)**2),18,'18','2(x-4)^2+18이므로 x=4에서 유일 최소18; y=0.')
check('C2',abs(s.solve(2+4*k,k)[0]),R(1,2),'1/2','직선 매개변수 t=-1/2, 길이비 k=|t|; P=(-1/2,0).')
sol=s.solve([b-2-(a-1)/2,2*a+b-14],[a,b])
check('C3',[sol[a],sol[b]],[5,4],'B(5, 4)','중점이 대칭축 위이고 연결선이 축에 수직; A는 축 밖이라 B 유일.')
# 양의 x절편 a이면 a>2, b=3a/(a-2). 제곱식으로 최소를 증명한다.
area=3*a*a/(2*(a-2))
check('C4',s.factor(area-12),3*(a-4)**2/(2*(a-2)),'12','a>2에서 S-12=3(a-4)^2/[2(a-2)]≥0. a=4,b=6에서 달성. AM-GM 없이 가능.')
check('C5',s.expand((x-k)**2+(y+2)**2-(x*x+y*y-2*k*x+4*y+k*k-2*k-5)),2*k+9,'k > −9/2','완전제곱 우변2k+9>0; 등호는 원이 아니라 점.')
poly=s.Poly(s.expand((3-4*m)**2-4*(m*m+1)),m)
check('C6',poly.TC()/poly.LC(),R(5,12),'5/12','12m²-24m+5=0 판별식336>0. x=4는 중심거리4>2로 접선 아님.')
chordx=s.solve(s.expand((x*x+y*y-9)-((x-3)**2+y*y-4)),x)[0]
check('C7',2*s.sqrt(9-chordx**2),8*s.sqrt(2)/3,'8√2/3','공통현 x=7/3; 반현 길이 sqrt(9-49/9).')
check('C8',(s.sqrt(3**2+4**2)+2)**2*(s.sqrt(3**2+4**2)-2)**2,441,'441','외부 고정점 거리 범위[3,7], 두 끝점 모두 중심선상 달성.')
f=s.Function('f'); shifted=f(x-2)
check('C9',shifted.subs(x,-x),f(-x-2),'f(−x − 2)','오른쪽2 평행이동한 그래프를 y축 대칭; 일반 함수로 확인.')
fixed=s.solve([2*x+y-5,x-y+2],[x,y])
check('C10',[(2*fixed[x]+4)/3,(2*fixed[y]+6)/3],[2,4],'(2, 4)','k의 계수와 상수항을 동시에0; 정점(1,3), 내분비1:2.')
distances=s.solve(a*a-8*a+9,a)
assert all(1<d<9 and s.simplify(2*s.sqrt(16-(4-d)**2))==6 for d in distances)
check('D1',sum(distances),8,'8','a>0에서 현x>0, 길이6으로 x=4; 두 근4±√7 모두 교차 조건 만족.')
reflection=s.solve([4+b-2*a,2*(b-4)+a],[a,b])
check('D2',2*reflection[a],R(32,5),'32/5','대칭점(16/5,12/5), 밑변4×높이16/5÷2. 계산은 맞으나 범위 초과 유지.')
A=s.Point(5,-4); B=s.Point(-1,2); P=s.Point(1,0); Q=s.Point(0,1)
check('D3',A.distance(P)+P.distance(Q)+Q.distance(B),6*s.sqrt(2),'6√2','대칭한 경로 길이는 직선거리 이상. A,P,Q,B 순서의 매개변수0,2/3,5/6,1로 등호 달성.')
check('D4',(1+a)**2+(-2+b)**2-(2+1)**2,(a+1)**2+(b-2)**2-9,'(p + 1)² + (q − 2)² = 9','이동 중심(1+p,-2+q), 반지름2 불변; 외접 중심거리3, 역도 성립.')
check('D5',abs(s.det(s.Matrix([[5,0],[1,2]])))/2,5,'5','접선x+2y=5, 수직선y=2x; 꼭짓점 원점,(5,0),(1,2).')
u=13*(3*x-4*y+1); v=5*(5*x+12*y-3)
check('D6',[(u-v)/14,(u+v)/2],[x-8*y+2,32*x+4*y-1],'32x + 4y − 1 = 0','정규화한 두 거리의 ±분기를 모두 풀어 두 이등분선 획득.')
circle=x*x+y*y-4*x-6*y
check('D7',[circle.subs({x:u,y:v}) for u,v in [(0,0),(4,0),(0,6)]],[0,0,0],'중심 **(2, 3)**','세 점 비공선. 직각삼각형 빗변 중점(2,3), 반지름√13; 세 점 모두 통과.')

observed=[r['item'] for r in rows]
coverage=dict(expected=expected,observed=observed,duplicate=[i for i,n in Counter(observed).items() if n>1],
              missing=sorted(set(expected)-set(observed)),extra=sorted(set(observed)-set(expected)))
assert not coverage['duplicate'] and not coverage['missing'] and not coverage['extra']
assert set(answer_rows)==set(expected)
assert (ROOT/SOURCE).read_bytes()==raw
warnings=['D2 계산 일치와 별개로 교육과정 범위 초과 표시 유지',
          'C8 form 대조표는 최대·최소의 합이라고 적지만 발문/답은 제곱값의 곱',
          'C4 기존 AM-GM 선수개념 경고는 제곱식 증명으로 회피 가능하나 원문은 미수정']
result=dict(author='메인 루프 (Codex/OMX)',grade='proposal',independent=False,source=frozen,
            coverage=coverage,rows=rows,warnings=warnings,warning_count=len(warnings),release='BLOCKED',
            limitations=['정답 계산 검산; 전수 신규성/태그/난이도 감사 아님','외부 Opus 검증 아님'])
(HOME/'260909_02_math2_32_selfcheck.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(coverage,ensure_ascii=False))
print('SELF_CHECK: 32 answers=32/32 match; warnings=3; external_verified=0; release=BLOCKED')
