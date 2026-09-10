"""One bounded authoring wave. Consumes frozen source; never grants a review verdict."""
from pathlib import Path
import hashlib
import json
import re
import sys

sys.path.insert(0, str(Path('tools').resolve()))
from textpatch import patch

BASE = Path('output/260907/260907_02_math2_revision_baseline.json')
TARGET = 'output/260829/260829_02_math2_comprehensive_25.md'
baseline = json.loads(BASE.read_text(encoding='utf-8'))[TARGET]['text']

ITEMS = {
3: '''**3.** 하나의 평행이동에 의하여 점 A(a, 2)는 점 A′(5, 7)로, 점 B(1, −3)은 점 B′(4, b)로 옮겨진다.

이때 a + b의 값을 구하시오. **[3점]**

`[SM2-26 · T1 · DF1]`''',
4: '''**4.** 실수 t에 따라 움직이는 점 P(t, t² − 2t)가 두 점 A(0, 2), B(2, 4)와 한 직선 위에 놓인다.
이 조건을 만족시키는 두 점 P를 P₁, P₂라 하자.

선분 P₁P₂의 길이의 제곱을 구하시오. **[3점]**

`[SM2-07 · T2 · DF1]`''',
6: '''**6.** 점을 x축에 대하여 대칭이동한 다음 직선 y = x에 대하여 대칭이동하는 조작을 T라 하자.
점 P₁에서 시작하여 Pₙ₊₁ = T(Pₙ)으로 점들을 정한다. P₂₀₂₆의 x좌표는 −2이고, P₂₀₂₇의 x좌표는 −5이다.

점 P₁의 x좌표에서 y좌표를 뺀 값을 구하시오. **[3점]**

`[SM2-29 · T2 · DF1·DF9]`''',
7: '''**7.** 삼각형 ABC에서 A(−2, 1), B(4, 1)이고 무게중심은 G(2, 3)이다.

삼각형 ABC의 넓이를 구하시오. **[3점]**

`[SM2-06 · T2 · DF1]`''',
22: '''**22.** 두 원 C₁ : x² + y² = 25, C₂ : (x − 4)² + y² = 25의 서로 다른 두 교점을 A, B라 하자.

**(1)** 세 점 A, B, P(2, 0)를 모두 지나는 원이 존재하는지 판단하고 그 이유를 서술하시오.
**(2)** 두 점 A, B와 원점을 지나는 원의 중심의 좌표와 반지름의 길이를 구하시오. **[6점]**

`[SM2-23 · T3 · DF1·DF2·DF4]`''',
}
NEW25 = '''**(1)** 두 점 A(0, 3), B(8, b)가 있다(b > 0). x축 위를 움직이는 점 P에 대하여 AP + BP의 최솟값이 10이다. b의 값과 이 최솟값을 만드는 점 P의 좌표를 구하시오.'''

ANSWERS = {
3: '| 3 | **4** | SM2-26 · T1 | 평행이동의 x방향 이동량은 B→B′에서 4−1=3, y방향 이동량은 A→A′에서 7−2=5이다. 따라서 a+3=5, −3+5=b에서 a=b=2, a+b=**4**. / 함정: 두 대응을 서로 다른 이동으로 취급하거나 원상 역산의 부호를 뒤집음. |',
4: '| 4 | **34** | SM2-07 · T2 | 직선 AB는 y=x+2. 공선 조건은 t²−2t=t+2, 즉 t²−3t−2=0이다. 두 실근을 α, β라 하면 α+β=3, αβ=−2, (α−β)²=9+8=17>0이므로 서로 다른 두 점이 존재한다. 직선 위에서 두 점의 x좌표 차와 y좌표 차가 같아 P₁P₂²=2(α−β)²=**34**. / 함정: x좌표 차의 제곱 17을 선분 길이의 제곱으로 답함. 공선 관계를 쓰지 않고 두 근을 각각 구하는 우회는 가능하나 불필요하다. |',
6: '| 6 | **3** | SM2-29 · T2 | T(x,y)=(−y,x), T²(x,y)=(−x,−y), T⁴(x,y)=(x,y). P₁=(u,v)이면 2026−1≡1, 2027−1≡2 (mod 4)이므로 P₂₀₂₆=(−v,u), P₂₀₂₇=(−u,−v). −v=−2, −u=−5에서 P₁=(5,2), 요구값은 **3**. / 함정: 주어진 정보는 두 시점의 x좌표이며 한 점의 두 좌표가 아니다. P₁을 기준으로 이동 횟수는 n−1이다. |',
7: '| 7 | **18** | SM2-06 · T2 | C=(c,d)라 하면 (−2+4+c)/3=2, (1+1+d)/3=3이므로 C=(4,7). AB=6이고 C에서 y=1까지 높이는 6이므로 넓이는 6×6/2=**18**. / 검산: G에서 AB까지 높이는 2이므로 △ABG=6, 무게중심의 넓이 삼등분으로 △ABC=18. 함정: △ABG의 넓이 6을 전체 넓이로 답하거나 G를 중점으로 처리함. |',
22: '| 22 | **(1) 존재하지 않는다 (2) 중심 (25/4, 0), 반지름 25/4** | SM2-23 · T3 | 두 원의 식을 빼면 −8x+16=0, 즉 공통현 직선은 x=2. C₁에 대입하면 교점은 (2,±√21)이므로 P(2,0)와 서로 다른 세 점이 일직선이다. 원과 직선의 교점은 최대 두 개이므로 (1)의 원은 없다. (2)는 원족 x²+y²−25+λ(x−2)=0에 원점 대입: −25−2λ=0, λ=−25/2. 따라서 x²+y²−(25/2)x=0, 즉 (x−25/4)²+y²=625/16이다. / 함정: (1)에서 원족의 이차항이 사라지는 직선을 원으로 답함. (2)의 양수 반지름은 25/4이며 제곱 625/16이 아니다. |',
25: '| 25 | **(1) b=3, P(4,0) (2) (x+1)²+(y−2)²=9 (3) (−1,3)** | SM2-33 + SM2-02 + SM2-30 + SM2-32 · T4 | (1) b>0이므로 A, B는 x축의 같은 쪽. A를 대칭시킨 A′=(0,−3)에 대하여 AP+BP=A′P+PB≥A′B=√(64+(b+3)²). 선분 A′B가 x축과 만나므로 하한이 달성된다. √(64+(b+3)²)=10에서 b+3=±6인데 b>0이므로 b=3만 가능하다. A′B가 x축과 만나는 점은 P=(4,0)이고 이때 AP=BP=5, 합=10이다. (2) 중심 (2,−1)을 y=x 대칭 → (−1,2), 반지름 3은 불변. (3) 상을 (p,q)라 하면 중점 조건 (1+q)/2=2(3+p)/2와 수직 조건 q−1=−(p−3)/2를 연립하여 (p,q)=(−1,3). / 함정: (1)의 음의 후보 b=−9는 주어진 조건을 어기며, 최솟값 10만 다시 답하면 b와 P를 누락한 것이다. |',
}

def block(text, n):
    m = re.search(rf'^\*\*{n}\.\*\*.*?(?=\n---)', text, re.M | re.S)
    if not m:
        raise ValueError(f'item missing: {n}')
    return m.group().rstrip()

def apply_wave(ids):
    current = Path(TARGET).read_text(encoding='utf-8-sig')
    pairs = []
    for n in ids:
        old = block(baseline, n)
        if n == 25:
            new = re.sub(r'^\*\*\(1\)\*\*.*$', NEW25, old, count=1, flags=re.M)
            new += '\n> 260907 교체: (1)은 최솟값에서 미지 위치를 역산하고 최소점을 구하는 문항으로 재설계. (2)·(3)은 보존.'
        else:
            new = ITEMS[n] + '\n> 260907 교체: Codex/OMX 작성자 자기검산 완료. 외부 Opus 재게이트 전 제안·미투입.'
        if new in current:
            print(f'SKIP completed item={n}')
            continue
        pairs.append((old, new))
        oldrow = re.search(rf'^\| {n} \|.*$', baseline, re.M).group()
        pairs.append((oldrow, ANSWERS[n]))
    if pairs:
        patch(TARGET, pairs)
    print(f'wave={ids} pairs={len(pairs)}')

if __name__ == '__main__':
    apply_wave([int(n) for n in sys.argv[1:]])
