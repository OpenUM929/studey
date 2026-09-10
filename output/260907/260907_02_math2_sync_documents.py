"""Synchronize author-owned surfaces; preserve review history and protected rulers."""
from pathlib import Path
import re
import sys
sys.path.insert(0, str(Path('tools').resolve()))
from textpatch import patch, insert_before

p=Path('output/260829/260829_02_math2_comprehensive_25.md')
t=p.read_text(encoding='utf-8-sig')
pairs=[]
def replace_pattern(pattern,new):
    old=re.search(pattern,t,re.M|re.S).group()
    if old!=new: pairs.append((old,new))
replace_pattern(r'^gate_status:.*?\nquality_audit:.*?\n',
'''gate_status: author-self-check-only-260908  # 교체 후 외부 Opus 전수 맹목 풀이 미실행; 종전 PASS는 교체 전 버전의 이력
quality_audit: pending-external-260908  # 6건 교체안 반영; N축 최종 판정 및 exam 투입 승인 미완료
''')
replace_pattern(r'> ⛔ \*\*미투입\.\*\*.*?(?=>\n> \*\*근거)',
'''> ⛔ **미투입·검토필요.** 260908 교체안 6건(3·4·6·7·22·25(1)) 반영.
> 작성자 자기검산은 외부 Opus의 맹목 풀이·품질감사를 대체하지 않는다.
> 교체 전 260907 PASS를 현 버전에 인용하지 않는다. exam 투입에는 기존 검토 루프,
> arbiter 승인과 사용자 확인이 필요하다. 작성자: 메인 루프(Codex/OMX), **proposal**.
''')
replace_pattern(r'### 22번 \[6점\].*?(?=\n### 23번)',
'''### 22번 [6점]
- (1) 두 원의 식을 빼서 공통현 직선 x=2를 구함 … 1점
- (1) A, B, P가 서로 다른 세 공선점임을 확인하고 원이 존재하지 않는다고 설명 … 1점
- (2) x²+y²−25+λ(x−2)=0을 세움 … 1점
- (2) 원점 조건으로 λ=−25/2를 구함 … 1점
- (2) 중심 (25/4,0)을 구함 … 1점
- (2) 반지름 25/4를 구함 … 1점
''')
replace_pattern(r'### 25번 \[7점\].*?(?=\n---)',
'''### 25번 [7점]
- (1) A′(0,−3)을 도입하고 하한 √(64+(b+3)²)의 달성 근거를 설명 … 1점
- (1) 최솟값 10과 b>0으로 b=3을 결정 … 1점
- (1) 등호 조건에서 P(4,0)을 결정 … 1점
- (2) 중심만 이동하고 반지름은 불변임을 명시, (x+1)²+(y−2)²=9 … 2점
- (3) 중점 조건과 수직 조건을 둘 다 세움 … 1점
- (3) Q(−1,3) … 1점
- ⚠️ (3)을 제외하고 운영하는 경우 총점 6점으로 하고 (1) 3점 / (2) 3점으로 배분한다.
''')
replace_pattern(r'— 13번은 260830.*?V-1\)\.',
'''— 13번은 260830 게이트의 Tier 정정(T3→T2) 결과다.
260907 결정 V-1에 따라 중요도 ★★★만을 이유로 Tier를 올리지 않는다.''')
pairs.append(('**SM2-19**(현의 길이)는 260822 40제에 없던 유형으로 이번에 처음 출제했다(9번).',
'**SM2-19**는 이 세트 9번이 현의 길이로, 현재 40제 19번이 넓이 동시 이등분으로 담당한다.'))
if '\n---\n---\n' in t: pairs.append(('\n---\n---\n','\n---\n'))
patch(p,pairs)
insert_before(p,'## 이력', '''## 260908 교체 동반 갱신 기록

- 대상: 3·4·6·7·22·25(1). 본문·정답·해설 6행, 채점기준 22·25번을 갱신했다.
- 유형ID·Tier는 유지했다. 본문 태그 재집계로 커버리지·역검산표·세트 요약의 변경 필요 여부를 검사한다.
- 260907 감사의 승인 대기는 당시 이력이다. 현재 상태는 **교체안 반영 / 외부 재게이트 대기**다.
- 계산 근거와 유형 보존·비수치 변형 근거는 `output/260907/rev/260907_02_math2_implementation_report.md`에 기록한다.

''')

p=Path('output/260822/공통수학2_도형의방정식_모의40.md'); t=p.read_text(encoding='utf-8-sig')
pairs=[]
for n,answer in {28:'정본 답(표현 기준): **12**; 학생 확인용 답: **√144**',29:'정본 답(표현 기준): **8**; 학생 확인용 답: **√64**',30:'정본 답(표현 기준): **(1) r=8 (2) 12√2**; 학생 확인용 답: **(1) r=√64 (2) √288**'}.items():
    old=re.search(rf'^\| {n} \|.*$',t,re.M).group(); new=re.sub(rf'^\| {n} \|.*? \|',f'| {n} | {answer} |',old,count=1); pairs.append((old,new))
patch(p,pairs)
insert_before(p,'## 서답형','''## 260908 원본재현 훈련·답 표현 기록

> ⛔ **검토필요·최종 배포본 아님.** 260907 검산은 이전 판본의 이력이다.
> 28·29·30번은 `analysis/catalog/math2.md` SM2-24 금지·주의의 의도된 3연작을 따른다.
> 답란의 “정본 답”은 기준 **표현**만 뜻하며 세트 출시 승인이나 N축 일반 면제를 뜻하지 않는다.
> 중심거리 13·10·17과 답의 동치성을 작성자 계산으로 확인했다. 식 √144=12, √64=8,
> √288=12√2는 양의 제곱근이며 같은 답으로 인정하는 표기다.
> 원본 동형 8건 및 6번(1) 증명에 대한 추가 N축 면제는 외부 arbiter 판정 전까지 미확정이다.

''')
print('DOCUMENT_SYNC_OK answer_rows=9 grading_sections=2 warnings=0')
