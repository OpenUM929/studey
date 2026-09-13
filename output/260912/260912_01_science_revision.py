"""Author-owned revision application; not an independent evaluator or gate."""
raise SystemExit('STALE: historical patch; rerunning would revert independently reviewed items. Do not execute.')
from pathlib import Path

root = Path(__file__).parent
p = root / '260912_01_science_midterm25_questions.md'
s = p.read_text(encoding='utf-8')
s = s.replace('I과 II에서 자석과 코일 사이 거리의 시간에 따른 변화는 같으며, 처음 위치 관계도 같다. ', '')
s = s.replace('반응 후 구리 분말이 모두 산화 구리(Ⅱ)가 되었다.', '반응 후 구리 분말 일부가 산화 구리(Ⅱ)가 되었다.')
for n in [2, 4, 5]:
    start = s.index(f'**{n}.**'); end = s.index(f'**{n+1}.**', start)
    b = s[start:end].replace('(2.7점)', '(2.5점)').replace(' · T2 · DF1, DF6]', ' · T1 · DF1]')
    s = s[:start] + b + s[end:]
for n in [9, 10, 11, 12]:
    start = s.index(f'**{n}.**'); end = s.index(f'**{n+1}.**', start)
    s = s[:start] + s[start:end].replace('(3.0점)', '(3.15점)') + s[end:]
start = s.index('**3.**'); end = s.index('**4.**', start)
b = s[start:end].replace('① ㄷ  ', '① ㄱ  ').replace('③ ㄱ, ㄷ  ', '③ ㄴ  ').replace('④ ㄴ, ㄷ  ', '④ ㄱ, ㄷ  ').replace(' · DF1, DF3]', ' · DF1, DF6]')
s = s[:start] + b + s[end:]
start = s.index('**7.**'); end = s.index('**9.**', start)
b = '''**7.** 한 곤충의 유전되는 두 형질 R·S에 대해 살충제 처리 후의 생존과 번식을 조사했다. 처음에는 각 형질이 100마리씩이었고, 자손은 부모와 같은 형질을 갖는다. 자손 수는 다음 세대에 살아남은 자손 수이며, 이동·형질 전환은 없다. 옳은 것만을 고른 것은? (2.7점)

| 형질 | 살충제 처리 후 생존 개체 수 | 생존 개체 한 마리당 자손 수 |
|---|---|---|
| R | 60 | 1 |
| S | 20 | 4 |

ㄱ. 다음 세대에는 R이 S보다 많다.  
ㄴ. 살충제 처리에서 R의 생존 비율은 S의 3배이다.  
ㄷ. 생존 비율이 높다는 사실만으로 다음 세대의 개체 수가 더 많다고 결론 내릴 수 없다.  

① ㄱ  
② ㄴ  
③ ㄱ, ㄷ  
④ ㄴ, ㄷ  
⑤ ㄱ, ㄴ, ㄷ  

[분석군 SC6 · T2 · DF1, DF3]

**8.** 어느 지역의 개발 전후를 완전하게 조사한 결과이다. '계통'은 같은 종 안에서 유전적으로 구별되는 집단을 뜻하며 별개의 종을 뜻하지 않는다. 평가자는 '종 수가 같으면 생물다양성은 모두 보전된 것'이라는 기준을 사용했다. 이 평가에 대한 설명으로 옳은 것만을 고른 것은? (2.7점)

| 항목 | 개발 전 | 개발 후 |
|---|---|---|
| 존재하는 종 | A·B·C | A·B·C |
| 각 종 안에 존재하는 유전적 계통 | 종마다 2계통 | 종마다 기존 1계통만 남음 |
| 존재하는 생태계 종류 | 숲·습지 | 숲 |

ㄱ. 종 수가 그대로여도 각 종의 유전적 다양성은 감소할 수 있으므로 평가 기준은 불충분하다.  
ㄴ. 생태계 종류의 변화를 별도로 평가하면 종 수만으로 놓친 손실을 파악할 수 있다.  
ㄷ. 유전적 계통 감소는 반드시 종 수 감소로 집계해야 한다.  

① ㄱ  
② ㄱ, ㄴ  
③ ㄴ, ㄷ  
④ ㄱ, ㄷ  
⑤ ㄱ, ㄴ, ㄷ  

[분석군 SC7 · T2 · DF1, DF3]

'''
s = s[:start] + b + s[end:]
assert '???' not in s
p.write_text(s, encoding='utf-8')
a = root / '260912_01_science_midterm25_answers.md'
lines = a.read_text(encoding='utf-8').splitlines()
for i, line in enumerate(lines):
    if any(line.startswith(f'| {n} |') for n in [2, 4, 5]):
        lines[i] = line.replace('·T2', '·T1')
    if line.startswith('| 7 |'):
        lines[i] = '| 7 | **④** | 분석군 SC6·T2 | 생존 비율은 R=60/100, S=20/100으로 3배이다. 다음 세대는 R=60×1=60, S=20×4=80으로 R이 적다. 생존과 생존자당 번식 기여를 함께 보아야 하므로 ㄱ만 거짓이다. |'
    if line.startswith('| 8 |'):
        lines[i] = '| 8 | **②** | 분석군 SC7·T2 | A·B·C 세 종은 유지되었지만 각 종의 계통과 생태계 종류는 감소했다. 종 수 하나만으로 서로 다른 수준의 손실을 검출할 수 없다. 종 내 계통 소실을 종 소실로 합산하는 것도 잘못이다. |'
a.write_text('\n'.join(lines) + '\n', encoding='utf-8')
n = root / '260912_01_science_midterm25.novelty.tsv'
lines = n.read_text(encoding='utf-8').splitlines()
for i, line in enumerate(lines):
    if line.startswith('7\t'):
        lines[i] = '7\t분석SC6(정본ID아님)\t유전 형질의 세대 구성은 생존·번식에 의존\t연속 과정 설명에서 서로 다른 생존/번식 지표의 표로\t선택 방향 재진술에서 생존 순위와 자손 수 순위의 역전 검증으로\t두 단계 기여를 곱해 단일 지표로 선택 결과를 단정하는 오류를 검출\tEX-science-20242M 선택14·15; EX-science-20252M 선택12·13/서술3\tREVIEW'
    if line.startswith('8\t'):
        lines[i] = '8\t분석SC7(정본ID아님)\t다양성 수준은 서로 대체 불가\t예시 분류에서 개발 전후의 다수준 변화표로\t이름 연결에서 성과 평가 지표의 검출 실패 판단으로\t종 수는 보존되지만 계통과 생태계는 줄어드는 반례로 평가 기준을 반박\tEX-science-20242M 선택17; EX-science-20252M 선택14·15\tREVIEW'
n.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('AUTHOR_REVISION_APPLIED')
