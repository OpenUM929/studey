"""Author calculations, not an external blind-solve or acceptance ruler."""
import json
from pathlib import Path
import sympy as s

results = {}
a,b,t,u,v,x,y,L,r = s.symbols('a b t u v x y L r', real=True)
sol=s.solve([a+3-5,-3+5-b],[a,b]); assert sol=={a:2,b:2}
results['25:3']={'answer':str(sol[a]+sol[b]),'unique':True,'method':'two translation coordinate equations'}
roots=s.solve(t*t-3*t-2,t)
p=[s.Point(z,z*z-2*z) for z in roots]
d2=s.simplify(p[0].distance(p[1])**2); assert d2==34
assert all(s.det(s.Matrix([[0,2,1],[2,4,1],[z,z*z-2*z,1]]))==0 for z in roots)
results['25:4']={'roots':[str(z) for z in roots],'answer':str(d2),'points':2,'method':'explicit roots and determinant, independent of Vieta shortcut'}
T=s.Matrix([[0,-1],[1,0]])
p26=T**2025*s.Matrix([u,v]); p27=T**2026*s.Matrix([u,v])
sol=s.solve([p26[0]+2,p27[0]+5],[u,v]); assert sol=={u:5,v:2}
results['25:6']={'answer':str(sol[u]-sol[v]),'unique':True,'method':'matrix powers 2025 and 2026'}
C=s.Point(3*2-(-2)-4,3*3-1-1)
area=s.Triangle(s.Point(-2,1),s.Point(4,1),C).area; assert area==18
results['25:7']={'C':str(C),'answer':str(area),'method':'centroid inverse and determinant area'}
f1=x*x+y*y-25; f2=(x-4)**2+y*y-25
inter=s.solve([f1,f2],[x,y]); assert set(inter)=={(2,-s.sqrt(21)),(2,s.sqrt(21))}
aa,bb,cc=s.symbols('aa bb cc',real=True)
circle=x*x+y*y+aa*x+bb*y+cc
impossible=s.solve([circle.subs({x:px,y:py}) for px,py in inter+[(2,0)]],[aa,bb,cc]); assert impossible==[]
coeff=s.solve([circle.subs({x:px,y:py}) for px,py in inter+[(0,0)]],[aa,bb,cc]); assert coeff=={aa:-s.Rational(25,2),bb:0,cc:0}
results['25:22']={'part1':'no circle','part2_center':['25/4','0'],'radius':'25/4','unique':True,'method':'general circle coefficients, three point equations'}
heights=s.solve(64+(b+3)**2-100,b); valid=[z for z in heights if z>0]; assert valid==[3]
cross=s.Line(s.Point(0,-3),s.Point(8,valid[0])).intersection(s.Line(s.Point(0,0),s.Point(1,0)))[0]
assert cross==s.Point(4,0)
assert cross.distance(s.Point(0,3))+cross.distance(s.Point(8,3))==10
results['25:25(1)']={'all_height_candidates':[str(z) for z in heights],'valid_height':'3','minimizer':str(cross),'minimum':'10','method':'reflection lower bound plus equality intersection; b>0 removes -9'}
assert s.sqrt(13**2-(7-2)**2)==12
assert s.sqrt(10**2-(2+4)**2)==8
rr=s.solve(17**2-(7+r)**2-8**2,r); rr=[z for z in rr if z>0 and 17>7+z]; assert rr==[8]
assert s.sqrt(17**2-(7-8)**2)==12*s.sqrt(2)
results['40:28']={'canonical':'12','equivalent':'sqrt(144)','equal':True}
results['40:29']={'canonical':'8','equivalent':'sqrt(64)','equal':True}
results['40:30']={'canonical':['8','12*sqrt(2)'],'equivalent':['sqrt(64)','sqrt(288)'],'equal':True}
out=Path('output/260907/260907_02_math2_selfcheck.json')
out.write_text(json.dumps({'grade':'author-self-check-only','calculations':results,'external_blind_solve':'NOT_RUN'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('AUTHOR_CALCULATION_OK replacement_units=6 equivalence_items=3 warnings=0')
for key,value in results.items(): print(key,json.dumps(value,ensure_ascii=False))
