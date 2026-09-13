"""Author self-check only. Finite tests do not certify proofs, novelty or Tier."""
import contextlib
import hashlib
import io
import itertools as it
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
DATA = HERE / '260912_info_ab50_reasoning.json'

def run(code, **initial):
    ns = dict(initial)
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        exec(compile(code, '<authored-item>', 'exec'), ns)
    return out.getvalue().rstrip(), ns

def load_base():
    result = {}
    for letter, number in [('A','01'),('B','02')]:
        p = ROOT / f'output/260910/260910_{number}_info_composite_{letter.lower()}_questions_review.md'
        for chunk in re.split(r'(?=^\*\*\d+\.\*\*)',p.read_text(encoding='utf-8-sig'),flags=re.M)[1:]:
            n = re.match(r'\*\*(\d+)\.\*\* (.+)',chunk)
            result[f'{letter}/{n[1]}'] = {
                'title': n[2], 'code': re.search(r'```python\n(.*?)```',chunk,re.S)[1],
                'tag': re.search(r'^\[IN-.+\]$',chunk,re.M)[0],
                'source':p.relative_to(ROOT).as_posix()}
    return result

def main():
    data = json.loads(DATA.read_text(encoding='utf-8'))
    base = load_base()
    expected = [f'{a}/{n}' for a in 'AB' for n in range(1,26)]
    observed = [x['id'] for x in data['items']]
    assert observed == expected and list(base) == expected
    checks = {}
    def check(id, condition):
        assert id not in checks, id
        assert condition, id
        checks[id] = True
    outputs = {id:run(b['code'])[0] for id,b in base.items()}
    def original(id, replacement=None):
        code = base[id]['code']
        if replacement:
            for old,new in replacement:
                assert old in code, (id,old)
                code = code.replace(old,new)
        return run(code)

    def balance(x):
        for fee in [3,8,2,6]: x=x-fee if x>=fee else x+fee
        return x
    check('A/1',[x for x in range(21) if balance(x)==9]==[12,16])
    def prefix(a, reverse=False):
        a=list(a)
        for i in ([3,2,1] if reverse else [1,2,3]): a[i]+=a[i-1]
        return a
    check('A/2',all((prefix(a)==prefix(a,True))==(a[0]==a[1]==0) for a in it.product(range(-2,3),repeat=4)))
    rotate=run(base['A/3']['code'])[1]['rotate']
    check('A/3',all((rotate(rotate(list(a)))==list(a))==((a[0]%4+a[a[0]%4]%4)%4==0) for a in it.permutations(range(4))))
    check('A/4',all((r[0]!=max(r))==(r[0]<max(r)) for r in it.product(range(-2,3),repeat=3)) and (5<max([5,2,7])) and not 5<2)
    def words(w):
        p=w[1:5]; c1=p[0]==p[-1];c2=p[1]!=p[2]
        return c1,c2,p[1:3] if c1 and c2 else w[:2]
    check('A/5',[words(w) for w in ['AABAAA','AABABA','AAAAAA']]==[(True,True,'BA'),(False,True,'AA'),(True,False,'AA')])
    check('A/6',[c for c in range(21) if original('A/6',[('<= 10',f'<= {c}')])[1]['i']==3]==[12,13])
    f=run(base['A/7']['code'])[1]['f']
    check('A/7',all([n for n in range(1,202) if f(n)==k and f(n+1)>k]==[2*k] for k in range(1,101)))
    check('A/8',original('A/8',[('t = [[3, 2], [4, 1], [2, 5]]','t = [[0]]')])[0]=='[1]' and original('A/8',[('t = [[3, 2], [4, 1], [2, 5]]','t = [[0]]'),('j < i','j <= i')])[0]=='[2]')
    def pairs(a,prune):
        count=0
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if a[j]-a[i]<=4: count+=1
                elif prune: break
        return count
    check('A/9',pairs([1,9,3],False)==2 and pairs([1,9,3],True)==1 and all(pairs(a,False)==pairs(a,True) for a in it.combinations(range(9),4)))
    def dedup(a,skip=False):
        a=list(a);i=1
        while i<len(a):
            if a[i]==a[i-1]:
                del a[i]
                if skip:i+=1
            else:i+=1
        return a
    check('A/10',dedup([1,1,1])==[1] and dedup([1,1,1],True)==[1,1] and all(dedup(a)==dedup(a,True) for n in range(3) for a in it.product(range(2),repeat=n)))
    def row_score(t):
        limit=4;s=0
        for a,b in t:
            if a<limit:s+=b
            limit=a
        return s
    check('A/11',row_score([[2,5],[3,7]])==5 and row_score([[3,7],[2,5]])==12)
    def swaps(p,q,u,v,w):
        a,b=p,q
        for k in [u,v,w]:a,b=b-k,a+k
        return a,b
    check('A/12',all(swaps(p,q,u,v,w)==(q-u+v-w,p+u-v+w) for p,q,u,v,w in it.product(range(-1,2),repeat=5)))
    cut=run(base['A/13']['code'])[1]['cut']
    def last(a):
        a=list(a)
        while len(a)>1:a=cut(a)
        return a[0]
    check('A/13',all(last(a)==max(a) for n in range(1,6) for a in it.product(range(3),repeat=n)))
    check('A/14',outputs['A/14']=='CBC 2' and original('A/14',[('[2, 4, 1]','[1, 4, 2]')])[0]=='BAC 2')
    ns=run(base['A/15']['code'])[1];f,g=ns['f'],ns['g']
    check('A/15',all((g(f(x))==f(g(x)))==(x>5) for x in range(-100,101)))
    check('A/16',outputs['A/16']=='5 7 12' and original('A/16',[('value = t[i][i]\n    t[i][0] = value + t[i][-1]','t[i][0] = t[i][-1]\n    t[i][0] += t[i][i]')])[0]=='6 7 12')
    def counts(a):
        c=[[0,0],[0,0]]
        for x,y in zip(a,a[1:]):c[x][y]+=1
        return c
    check('A/17',all((lambda c:c[0][1]-c[1][0]==a[-1]-a[0])(counts(a)) for n in range(1,9) for a in it.product(range(2),repeat=n)))
    digits=run(base['A/18']['code'])[1]['digits']
    check('A/18',all(digits(n)<n and digits(n)%9==n%9 for n in range(10,10000)) and digits(digits(275))==5)
    def reverse(a,ends):
        a=list(a)
        for l,r in ends:a[l:r+1]=a[l:r+1][::-1]
        return a
    check('A/19',reverse([1,2,3],[(0,1),(1,2)])==[2,3,1] and reverse([1,2,3],[(1,2),(0,1)])==[3,1,2])
    t=[[1,6,3],[4,2,8]]
    def flip(j):
        u=[r[:] for r in t];u[0][j],u[1][j]=u[1][j],u[0][j]
        return [u[1][k]-u[0][k] for k in range(3) if u[0][k]<u[1][k]]
    check('A/20',[j for j in range(3) if flip(j)==[5]]==[0])
    missing=run(base['A/21']['code'])[1]['missing']
    def oracle_missing(a):return next(n for n in range(1,len(a)+2) if n not in a)
    check('A/21',missing([2,1])==1 and all(missing(list(a))==oracle_missing(a) for n in range(6) for a in it.combinations_with_replacement(range(1,6),n)))
    def cancel(a):
        out=[]
        for x in a:
            if out and out[-1]==x:out.pop()
            else:out.append(x)
        return out
    check('A/22',cancel([1,2,2,1])==[] and cancel([1,2,1,2])==[1,2,1,2] and all(len(cancel(a))%2==len(a)%2 for n in range(9) for a in it.product(range(2),repeat=n)))
    def firstlast(m):
        xs=[i for i in range(1,m+1) if i*(i+1)>=10]
        return (xs[0],xs[-1]) if xs else (0,0)
    check('A/23',all((firstlast(m)[0]==firstlast(m)[1])==(m<=3) for m in range(21)))
    def pal(s):
        L=len(s);same=0
        while len(s)>=2:
            same+=s[0]==s[-1];s=s[1:-1]
        return same==L//2
    check('A/24',all(pal(s)==(s==s[::-1]) for n in range(9) for s in it.product('AB',repeat=n)))
    neg=[('t = [[5, 2, 4], [3, 3, 6], [1, 7, 5]]','t = [[-5,-2,-4]]')]
    check('A/25',original('A/25',neg)[0]=='-1 -1' and sum([-5,-2,-4])-max([-5,-2,-4])==-9)

    a=[1,2,3,4]
    for i in range(1,4):a[i]-=a[i-1]
    b=a[:]
    for i in range(3,0,-1):b[i]+=b[i-1]
    check('B/1',a==[1,1,2,2] and prefix(a)==[1,2,4,6] and b==[1,2,3,4])
    def hits(a):
        h=[0]*4
        for i,x in enumerate(a):h[(i+x)%4]+=1
        return h
    check('B/2',hits([1,0,1,0])==[0,2,0,2] and sum(hits(a)==[0,2,0,2] for a in it.product(range(4),repeat=4))==6)
    def maximum(a):
        ans=0
        for x in a:
            if x>4 and x>ans:ans=x
        return ans
    check('B/3',all(maximum(a)==max([0]+[x for x in a if x>4]) for n in range(5) for a in it.product([0,4,7,9],repeat=n)))
    def col(t):return [sum(r[j] for r in t) for j in range(2)]
    check('B/4',col([[2,0],[2,0]])==[4,0] and col([[1,1],[1,1]])==[2,2])
    def letters(s,mode):
        return ''.join(s[i-1] for i in range(len(s)) if (s[i]=='A' if mode==1 else i%2==1 if mode==2 else s[i]=='A' and i%2==1))
    check('B/5',[letters('AABACA',i) for i in [0,1]]==['ABC','AABC'] and [letters('CBBACA',i) for i in [0,2]]==['BC','CBC'])
    def pointers(a,equal=False):
        l,r,s=0,len(a)-1,0
        while l<=r if equal else l<r:s+=a[r]-a[l];l+=1;r-=1
        return s,l,r
    check('B/6',all(pointers(a)[0]==pointers(a,True)[0]==sum(a[len(a)-len(a)//2:])-sum(a[:len(a)//2]) for n in range(6) for a in it.product(range(3),repeat=n)))
    def reserve(req,stock=5):
        acc=[]
        for n in req:
            if n<=stock:stock-=n;acc.append(n)
        return stock,acc
    check('B/7',reserve([4,3])==(1,[4]) and reserve([3,4])==(2,[3]))
    rec=run(base['B/8']['code'])[1]['f']
    check('B/8',all(rec(list(a))==list(a[::2][::-1]) and rec(list(a[1:]))==list(a[1::2][::-1]) for n in range(6) for a in it.product(range(3),repeat=n)))
    combos=[p for p in it.combinations(range(5),3) if ''.join('ABABA'[i] for i in p)=='ABA']
    check('B/9',combos==[(0,1,2),(0,1,4),(0,3,4),(2,3,4)] and original('B/9',[("'AABBAC'","'ABABA'")])[1]['picked']==[0,1,2])
    check('B/10',run(base['B/10']['code'])[1]['pos']==3 and original('B/10',[('a[pos] <= value','a[pos] < value')])[1]['pos']==1)
    check('B/11',original('B/11',[('[[2, 5], [4, 1], [3, 2], [1, 4]]','[[5,1],[1,100]]')])[1]['loads']==[5,100])
    check('B/12',original('B/12',[('[2, 4, 3]','[4,3]'),('[3, 2, 4]','[3,4]')])[1]['count']==1)
    edits=[('[4, 1, 3, 4, 1]','[1,2,3,4,2]')]
    check('B/13',original('B/13',edits)[0]=='1 9' and original('B/13',edits+[('current > best','current >= best')])[0]=='2 9')
    join=run(base['B/14']['code'])[1]['join']
    strings=[''.join(map(chr,range(65,65+n))) for n in range(21)]
    check('B/14',all((join(join(s))==s)==(len(s)<=4) for s in strings))
    def leftmost(a,key):
        left,right,answer=0,len(a)-1,-1
        while left<=right:
            mid=(left+right)//2
            if a[mid]==key:answer=mid;right=mid-1
            elif a[mid]<key:left=mid+1
            else:right=mid-1
        return answer
    check('B/15',all(leftmost(a,k)==(a.index(k) if k in a else -1) for n in range(7) for a in it.combinations_with_replacement(range(4),n) for k in range(-1,5)))
    check('B/16',outputs['B/16']=='13 [9, 8]' and max([4+2+7,4+2+1,4+5+1,4+5+3])==13)
    check('B/17',original('B/17',[('[1, 0, 1, 1, 0]','[1,0]')])[0]=='True [0, 1]' and original('B/17',[('[1, 0, 1, 1, 0]','[0,1]')])[0]=='True [1]')
    def jump(a):
        i=0;visited=[]
        while i<len(a):visited.append(i);i+=a[i]
        return visited
    check('B/18',all(len(jump(a))<=len(a) for n in range(7) for a in it.product(range(1,4),repeat=n)) and len(jump([1]*8))==8 and 0+[0][0]==0)
    code=base['B/19']['code'].replace('    if r == -1:\n        return -1\n','')
    wrong=run(code)[1]['locate']
    check('B/19',all(wrong([3]*n,2)==n-1 for n in range(1,7)))
    def rows(t,reset=True):
        count=0;total=0
        for row in t:
            if reset:count=0
            count+=sum(x%2==0 for x in row)
            total+=count>=2
        return total
    check('B/20',rows([[2,4],[1,3]])==1 and rows([[2,1],[4,3]])==0 and rows([[2,1],[4,3]],False)==1)
    def repair(t):
        t=[r[:] for r in t];fixed=[]
        for i,r in enumerate(t):
            if sum(r[:-1])!=r[-1]:r[-1]=sum(r[:-1]);fixed.append(i)
        return t,fixed
    check('B/21',repair(repair([[2,5,8],[4,1,5],[3,3,5]])[0])[1]==[] and sum([3,5])==8 and sum([2,5])!=8)
    a=[3,8,2,8];b=[]
    for _ in range(2):m=max(a);b.append(m);a=[x for x in a if x!=m]
    check('B/22',a==[2] and b==[8,3] and outputs['B/22']=='[3, 2] [8, 8] 5')
    check('B/23',original('B/23',[('[3, 4, 1, 5, 6]','[3,3,1,1]')])[0]=='0 2' and original('B/23',[('[3, 4, 1, 5, 6]','[1,1,3,3]')])[0]=='2 2')
    def merge(a,b):
        i=j=0;out=[]
        while i<len(a) and j<len(b):
            if a[i]<=b[j]:out.append(a[i]);i+=1
            else:out.append(b[j]);j+=1
        return out+a[i:]+b[j:]
    lists=[list(a) for n in range(4) for a in it.combinations_with_replacement(range(3),n)]
    check('B/24',all(merge(a,b)==sorted(a+b) for a in lists for b in lists))
    check('B/25',original('B/25',[('[[2, 5], [0, 4], [1, 7]]','[[1,2],[2,3],[1,5]]')])[0]=='1 10 [1, 1, 1]')
    assert list(checks)==expected
    result={'author_selfcheck_only':True,'expected':expected,'observed':list(checks),'missing':[],
            'extra':[],'duplicates':[],'checks':checks,'base_outputs':outputs,
            'limits':'Finite checks support examples and formulas; not independent proof, novelty, scope, highest-level or release approval.',
            'data_sha256':hashlib.sha256(DATA.read_bytes()).hexdigest(),'warnings':[],'exit_code':0}
    p=HERE/'260912_info_ab50_selfcheck.json'
    p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('author_selfcheck items=50/50 missing=0 extra=0 duplicate=0 warnings=0 exit=0')

if __name__=='__main__': main()
