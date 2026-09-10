"""Own draft authoring and self-computation. Never an external release gate."""
from pathlib import Path
import contextlib, io, json, hashlib, re, csv, ast, html, sys

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'output/260910'
ITEMS = []

def add(group, title, types, code, expected, explanation, axes):
    ITEMS.append(dict(group=group, number=1+sum(x['group']==group for x in ITEMS),
        title=title, types=['IN-'+x for x in types.split()], code=code.strip(),
        expected=expected, explanation=explanation, axes=axes))

add('A','조건에 따라 바뀌는 잔액','04 06 02', '''
balance = 5
for fee in [3, 8, 2, 6]:
    if balance >= fee:
        balance -= fee
    else:
        balance += fee
print(balance)
''', '2', '잔액은 5→2→10→8→2가 된다.', ['고정 조건 대신 직전 잔액에 의존하는 분기','단일 합산 대신 지불과 충전의 교대'])
add('A','수정한 원소를 다시 읽는 누적','09 11 06', '''
a = [2, 5, 1, 4]
for i in range(1, len(a)):
    a[i] = a[i] + a[i-1]
print(a)
''', '[2, 7, 8, 12]', 'i=1에서 7, i=2에서 이미 바뀐 7을 더해 8, i=3에서 8을 더해 12가 된다.', ['이전 원소의 갱신값이 다음 원소로 전달','독립 원소 계산 대신 순차 상태 의존'])
add('A','함수의 반환값이 다음 인수','19 04 01', '''
def step(n):
    if n % 2 == 0:
        return n // 2
    return n + 3
x = 5
print(step(step(x)), step(x + 1))
''', '4 3', 'step(5)=8이므로 step(8)=4이다. 별도의 step(6)은 3이다.', ['호출 결과를 다른 호출의 인수로 사용','중첩 호출과 독립 호출 비교'])
add('A','행별 최댓값의 위치 조건','22 13 09', '''
table = [[3, 8, 2], [9, 1, 4], [5, 2, 7]]
total = 0
for row in table:
    if row[0] != max(row):
        total += max(row) - min(row)
print(total)
''', '11', '첫 행은 8−2=6, 둘째 행은 첫 원소가 최댓값이므로 제외, 셋째 행은 7−2=5를 더한다.', ['원소 조건을 행의 최댓값 위치 조건으로 변경','행을 선별한 뒤 행별 범위를 합산'])
add('A','잘라 낸 문자열로 조건 검사','14 03 04', '''
word = 'ABACBA'
part = word[1:5]
if part[0] == part[-1] and part[1] != part[2]:
    print(part[1:3])
else:
    print(word[:2])
''', 'AC', 'part는 BACB. 양끝 B가 같고 가운데 A와 C는 달라 참 분기에서 AC를 출력한다.', ['슬라이스 결과의 내부 관계가 분기 결정','원문이 아닌 파생 문자열을 다시 슬라이싱'])
add('A','종료 직전까지 담는 상자','08 09 02', '''
size = [4, 3, 5, 2]
used = 0
i = 0
while i < len(size) and used + size[i] <= 10:
    used += size[i]
    i += 1
print(i, used)
''', '2 7', '4와 3까지 담으면 used=7, i=2. 다음 5를 더하면 12여서 반복 몸체에 들어가지 않는다.', ['반복 전 다음 원소의 수용 가능성 검사','종료 인덱스와 누적량을 함께 추적'])
add('A','전역값과 반환값의 다른 역할','20 19 02', '''
score = 10
def local(score):
    score += 4
    return score
def change():
    global score
    score = local(score) // 2
a = local(score)
change()
print(a, score)
''', '14 7', '첫 호출 반환값 a=14는 전역 score를 바꾸지 않는다. change 안에서 local(10)//2를 전역에 대입해 7이 된다.', ['반환값을 보존한 뒤 전역 변경','지역 계산을 전역 갱신식에 결합'])
add('A','재귀에서 남기는 원소','21 10 03', '''
def pick(a):
    if len(a) == 0:
        return 0
    if a[0] > 3:
        return 1 + pick(a[1:])
    return pick(a[1:])
print(pick([2, 6, 3, 5]))
''', '2', '슬라이스로 4→3→2→1→0개가 된다. 6과 5에서만 1을 더하므로 2이다. 최대 호출 깊이는 5이다.', ['재귀 인자가 정수가 아닌 남은 리스트','조건에 맞는 호출에서만 개수 증가'])
add('A','가까운 두 기록의 차이','07 09 06', '''
a = [1, 4, 6, 9]
count = 0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[j] - a[i] <= 4:
            count += 1
print(count)
''', '3', 'i<j인 쌍 중 (1,4), (4,6), (6,9)만 차이가 4 이하이다. 역순 쌍과 자기 자신은 세지 않는다.', ['중복 없는 두 인덱스 조합 순회','배수 조건 대신 두 원소 간 차이로 선별'])
add('A','한 번 삭제한 뒤의 검색','12 11 09', '''
a = [4, 2, 4, 7]
a.remove(a[0])
a.insert(1, a[-1] - a[0])
print(a, sum(a))
''', '[2, 5, 4, 7] 18', 'remove는 첫 4만 지워 [2,4,7]. 현재 끝값 7과 첫값 2의 차이 5를 인덱스1에 삽입한다.', ['삭제 후 상태로 삽입할 값을 계산','삽입 위치와 삽입값을 서로 다른 정보에서 결정'])
add('A','행 사이로 전달되는 기준','22 15 04', '''
t = [[2, 5], [6, 1], [3, 7]]
limit = 4
answer = 0
for row in t:
    if row[0] < limit:
        answer += row[1]
    limit = row[0]
print(answer, limit)
''', '12 3', '첫 행은 2<4여서 5를 더하고 기준2. 둘째 행은 제외 후 기준6. 셋째 행은 3<6여서 7을 더하고 기준3.', ['이전 행의 값이 다음 행 기준','누적 대상과 기준 갱신 원소를 분리'])
add('A','회차마다 달라지는 곱셈','05 06 26', '''
x = 1
trace = []
for i in range(2, 7, 2):
    x = x * i - 1
    trace.append(x)
print(trace, x)
''', '[1, 3, 17] 17', 'i는 2,4,6. 갱신 후 x는 1,3,17이며 trace에는 초기값1을 별도로 넣지 않는다.', ['갱신 결과를 매 회차 저장','단순 곱 대신 곱셈 뒤 보정이 누적'])
add('A','함수가 고른 슬라이스','19 10 13', '''
def cut(a):
    if a[0] < a[-1]:
        return a[1:]
    return a[:-1]
a = [8, 2, 5, 3]
b = cut(a)
print(sum(cut(b)), len(a))
''', '10 4', '첫 호출은 끝을 제외해 b=[8,2,5]. 두 번째도 끝을 제외해 [8,2], 합10. 원본 길이는4이다.', ['양끝 비교로 슬라이스 방향 결정','줄어든 결과에 동일 함수를 재적용'])
add('A','누적값으로 문자를 고르기','14 06 01', '''
text = 'ABCDE'
k = 0
result = ''
for move in [2, 4, 1]:
    k = (k + move) % len(text)
    result += text[k]
print(result, k)
''', 'CBC 2', 'k는 2→1→2. 이에 해당하는 C,B,C를 이어 붙인다. 이동량 자체를 인덱스로 읽지 않는다.', ['누적 이동을 나머지로 순환','수치 상태를 문자열 출력 위치로 변환'])
add('A','두 함수의 적용 순서','19 04 02', '''
def f(x):
    return x + 2
def g(x):
    if x > 5:
        return x - 3
    return x * 2
print(g(f(4)), f(g(4)))
''', '3 10', 'g(f(4))=g(6)=3. f(g(4))=f(8)=10. 호출 순서가 중간값과 분기를 동시에 바꾼다.', ['함수 순서를 교환한 두 경로 비교','중간값이 조건 경계를 넘는 구조'])
add('A','대각선 값을 이용한 행 수정','15 22 11', '''
t = [[2, 1, 3], [4, 5, 2], [7, 1, 6]]
for i in range(3):
    value = t[i][i]
    t[i][0] = value + t[i][-1]
print(t[0][0], t[1][0], t[2][0])
''', '5 7 12', '각 행의 대각선값2,5,6을 먼저 value에 저장하고 끝값3,2,6을 더해 첫 열에 쓴다.', ['행 번호에 따라 참조 열이 변함','읽어 둔 대각선 값으로 다른 열을 갱신'])
add('A','양방향 조건을 이용한 점수','03 04 06', '''
total = 0
for n in [2, 3, 6, 7]:
    if n % 2 == 0 and n % 3 == 0:
        total += 3
    elif n % 2 == 0 or n % 3 == 0:
        total += 1
    else:
        total -= 1
print(total)
''', '4', '2와3은 각1, 6은 첫 가지에서3만 추가, 7은−1이므로 합4. 6에 elif의1까지 더하지 않는다.', ['교집합을 먼저 처리한 조건 분기','배수의 합 대신 조건별 점수 부여'])
add('A','종료 후 다시 만드는 값','08 01 19', '''
def digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s
x = digits(275)
print(x, digits(x))
''', '14 5', '첫 호출은 5+7+2=14를 반환한다. 두 번째는 4+1=5. 반복에서 몫과 나머지는 서로 다른 역할이다.', ['몫으로 입력 축소하며 나머지 누적','축약된 결과를 다시 입력으로 사용'])
add('A','호출 중과 복귀 후의 다른 계산','21 01 19', '''
def f(n):
    if n == 0:
        return 1
    return 2 * f(n-1) + n
print(f(3) - f(1))
''', '16', 'f(0)=1, f(1)=3, f(2)=8, f(3)=19이므로 차16이다. 각 호출은 자기 n을 복귀 계산에 쓴다.', ['호출 복귀 때 이전 결과를 확대','서로 다른 깊이 반환값의 차이'])
add('A','조건에 맞는 열만 모으기','22 15 12', '''
t = [[1, 6, 3], [4, 2, 8]]
out = []
for j in range(3):
    if t[0][j] < t[1][j]:
        out.append(t[1][j] - t[0][j])
print(out)
''', '[3, 5]', '열0은1<4여서3, 열1은6<2가 거짓, 열2는3<8여서5를 넣는다.', ['행 우선 순회 대신 같은 열의 두 행 비교','조건 통과 열의 차이를 새 리스트로 구성'])
add('A','지역 인수와 같은 이름','20 19 04', '''
x = 6
def f(x):
    if x < 5:
        x += 10
    return x - 1
y = f(x - 3)
print(x, y, f(y))
''', '6 12 11', 'f(3)에서 지역 x는13이 되고12반환. 전역x는6. f(12)는 분기 없이11반환.', ['전역과 같은 이름의 매개변수에 가공 인수 전달','지역 반환값을 다음 조건 판정에 재사용'])
add('A','중복 삭제가 바꾸는 합','11 13 06', '''
a = [2, 5, 2, 7, 5]
for value in [2, 5]:
    a.remove(value)
print(a, max(a) - min(a), sum(a))
''', '[2, 7, 5] 5 14', '첫2와 첫5만 각각 삭제하므로 [2,7,5]. 범위는7−2=5, 합은14.', ['중복값에서 한 개씩만 제거','삭제 결과로 범위와 합을 함께 재계산'])
add('A','기준을 넘은 순간의 회차','06 26 04', '''
s = 0
first = 0
for i in range(1, 5):
    s += i * 2
    if s >= 10 and first == 0:
        first = i
print(first, s)
''', '3 20', '누적값2,6,12,20. 처음10이상인 i=3만 first에 기록하며 i=4에서 덮어쓰지 않는다.', ['누적 중 최초 통과 회차를 별도 보존','최초 기록 조건과 최종 누적을 분리'])
add('A','문자열을 줄여 가며 검사','08 14 03', '''
s = 'ABBA'
same = 0
while len(s) >= 2:
    if s[0] == s[-1]:
        same += 1
    s = s[1:-1]
print(same, len(s))
''', '2 0', 'ABBA의 양끝 A, 이어 BB의 양끝 B가 일치. 다음 문자열은 빈 문자열이므로 종료한다.', ['매 회차 양끝을 제거하는 입력 축소','길이에 따른 종료와 문자 관계 판정 결합'])
add('A','두 단계로 고르는 대표 행','22 13 19', '''
def score(row):
    return sum(row) - max(row)
best = -1
who = -1
t = [[5, 2, 4], [3, 3, 6], [1, 7, 5]]
for i in range(len(t)):
    s = score(t[i])
    if s > best:
        best = s
        who = i
print(who, best)
''', '0 6', '행별 점수는6,6,6. 엄격한 >만 갱신하므로 최초 행의 인덱스0과 점수6이 남는다.', ['행 평가함수의 값을 기준으로 순위 결정','동점에서 최초 선택을 유지하는 갱신 규칙'])

add('B','서로 다른 두 갱신을 번갈아 적용','02 06 04', '''
x = 3
for i in range(1, 5):
    if i % 2 == 1:
        x = 2 * x
    else:
        x = x - i
print(x)
''', '4', 'i=1,2,3,4 뒤 x는6,4,8,4이다. 조건은 x의 홀짝이 아니라 회차 i의 홀짝이다.', ['상태값 대신 회차가 갱신식을 선택','증가와 감소가 번갈아 누적'])
add('B','앞에서 고른 값으로 뒤를 수정','11 09 05', '''
a = [3, 1, 4, 2]
for i in range(2):
    a[3-i] = a[i] + a[3-i]
print(a)
''', '[3, 1, 5, 5]', 'i=0이면 a[3]=3+2=5, i=1이면 a[2]=1+4=5. 앞의 두 원소는 바뀌지 않는다.', ['대칭 위치를 한 쌍으로 참조','전체 누적 대신 뒤 절반만 갱신'])
add('B','분기 직전 반환된 값','19 04 06', '''
def first(a):
    for x in a:
        if x > 4:
            return x
    return 0
print(first([2, 7, 9]), first([4, 1]))
''', '7 0', '첫 리스트는7을 만났을 때 즉시 반환하여9를 읽지 않는다. 둘째는 끝까지 조건 불충족이므로0.', ['조건부 조기 반환으로 순회 중단','발견과 미발견의 두 반환 경로'])
add('B','행을 연결하지 않고 열을 합산','22 15 13', '''
t = [[2, 8], [5, 1], [4, 6]]
columns = [0, 0]
for row in t:
    for j in range(2):
        columns[j] += row[j]
print(columns, max(columns))
''', '[11, 15] 15', '각 열에 별도 누적하여 첫열2+5+4=11, 둘째열8+1+6=15. 최댓값은15.', ['하나의 총합 대신 열별 누적 상태','완성한 집계 리스트에서 최댓값 선택'])
add('B','위치에 따른 문자 분류','14 06 03', '''
s = 'CABACA'
out = ''
for i in range(len(s)):
    if s[i] == 'A' and i % 2 == 1:
        out += s[i-1]
print(out)
''', 'CBC', 'A인 위치1,3,5는 모두 홀수. 그 직전 위치0,2,4의 C,B,C를 붙인다.', ['문자값과 위치 조건을 동시에 검사','일치 문자 자체가 아닌 이웃 문자를 출력'])
add('B','움직이는 두 포인터','08 09 02', '''
a = [2, 7, 4, 5]
left = 0
right = 3
s = 0
while left < right:
    s += a[right] - a[left]
    left += 1
    right -= 1
print(s, left, right)
''', '0 2 1', '차는5−2=3, 4−7=−3. 두 포인터가2,1이 되어 교차하면서 종료, 합0.', ['양끝 인덱스가 동시에 이동','종료 여부를 두 위치의 관계로 결정'])
add('B','전역 횟수와 지역 계산값','20 19 06', '''
calls = 0
def twice(x):
    global calls
    calls += 1
    return x * 2
total = 0
for n in [1, 3, 2]:
    total += twice(n)
print(total, calls)
''', '12 3', '반환값2,6,4의 합12와 별도로 전역 호출 수는3이 된다.', ['계산 반환과 호출 횟수 부작용 분리','반복 호출의 두 상태를 동시 집계'])
add('B','재귀가 돌려주는 자리값','21 01 19', '''
def f(n):
    if n == 0:
        return 0
    return 10 * f(n-1) + n
print(f(3))
''', '123', 'f(0)=0, f(1)=1, f(2)=12, f(3)=123. 되돌아오면서 자리값을10배한다.', ['재귀 복귀값에 자리값 부여','현재 인자를 마지막 자리로 합성'])
add('B','두 목록의 일치 횟수','07 09 03', '''
a = [1, 2, 1]
b = [1, 3, 1]
hits = 0
for x in a:
    for y in b:
        if x == y:
            hits += 1
print(hits)
''', '4', 'a의 두1 각각이 b의 두1과 일치하므로2×2=4회. 서로 다른 값의 개수가 아니다.', ['동일 목록의 인덱스 조합 대신 두 목록 곱집합','중복 원소를 별개의 비교 사건으로 계산'])
add('B','삽입 후 삭제할 위치','12 11 10', '''
a = [6, 2, 9]
a.insert(0, a[-1])
del a[2]
print(a[1:], len(a))
''', '[6, 9] 3', '삽입 후[9,6,2,9], 인덱스2인2를 삭제해[9,6,9]. 슬라이스는[6,9], 전체 길이3.', ['삽입으로 이동한 인덱스를 삭제에 사용','전체 상태와 부분 슬라이스를 구분'])
add('B','행별 합의 차례가 달라질 때','22 13 04', '''
t = [[2, 3], [1, 7], [4, 2], [5, 5]]
previous = 0
count = 0
for row in t:
    current = sum(row)
    if current > previous:
        count += 1
    previous = current
print(count)
''', '3', '행합은5,8,6,10. 직전 기준0,5,8,6과 각각 비교하므로 첫째·둘째·넷째가 증가이다.', ['개별 원소 대신 행합을 연속 비교','누적 최댓값이 아니라 직전 행합을 기준으로 유지'])
add('B','중첩 반복의 회차별 기록','07 26 12', '''
trace = []
s = 0
for i in range(1, 4):
    for j in range(i):
        s += i - j
    trace.append(s)
print(trace)
''', '[1, 4, 10]', '바깥 회차별 추가량은1, 2+1=3, 3+2+1=6. s를 초기화하지 않아 기록은1,4,10.', ['안쪽 완료 시점만 기록하는 추적표','회차별 합과 전체 누적을 구별'])
add('B','슬라이스가 바뀌어도 원문은 그대로','10 11 13', '''
a = [4, 8, 2, 6]
b = a[1:3]
b[0] = b[0] - b[1]
a[2] = 10
print(sum(a), sum(b))
''', '28 8', 'b는[8,2]에서[6,2]가 된다. a는[4,8,10,6]이다. 1차원 슬라이스 리스트의 원소 변경은 서로 전달되지 않는다.', ['1차원 슬라이스 사본과 원본의 수정 분리','서로 다른 변경 이후 두 합 비교'])
add('B','문자열 두 조각의 순서 선택','14 19 04', '''
def join(s):
    a = s[:2]
    b = s[2:]
    if len(a) < len(b):
        return b + a
    return a + b
print(join('ABCDE'), join('XYZ'))
''', 'CDEAB XYZ', '첫 호출은 길이2와3이므로 CDE+AB. 둘째는2와1이므로 XY+Z. 입력 길이에 따라 결합 순서가 달라진다.', ['부분 문자열 길이로 연결 순서를 선택','같은 함수에 다른 길이를 주어 분기 비교'])
add('B','서로 다른 반환 경로의 합','19 03 04', '''
def f(a, b):
    if a > b:
        return a - b
    if a == b:
        return a + b
    return b // a
print(f(3, 8) + f(4, 4) + f(9, 2))
''', '17', '각 호출은 작은 경우2, 같은 경우8, 큰 경우7을 반환하므로17. return 이후 아래 분기는 실행하지 않는다.', ['두 인수의 대소 관계로 반환식 결정','세 관계의 결과를 합쳐 하나의 목표값 구성'])
add('B','현재 행이 바꾸는 다음 행','15 22 11', '''
t = [[2, 1], [3, 4], [5, 2]]
for i in range(2):
    t[i+1][0] += t[i][1]
    t[i+1][1] += t[i][0]
print(t[-1])
''', '[11, 6]', '첫 회차에 둘째 행[4,6]. 다음 회차는 갱신된 이 행을 사용해 셋째 행[11,6]을 만든다.', ['수정 대상이 현재 행이 아닌 다음 행','두 열을 교차 연결해 갱신값 전파'])
add('B','하나의 조건만 참인 기록','03 06 04', '''
count = 0
for n in [2, 3, 4, 6, 9]:
    a = n % 2 == 0
    b = n % 3 == 0
    if (a or b) and not (a and b):
        count += 1
print(count)
''', '4', '2,3,4,9는 정확히 한 조건만 참. 6은 둘 다 참이므로 제외한다.', ['둘 중 하나 조건에서 교집합을 제외','중간 불리언 변수를 결합해 배타적 조건 표현'])
add('B','인덱스가 건너뛰는 순회','08 09 02', '''
a = [1, 2, 1, 3, 2]
i = 0
visited = []
while i < len(a):
    visited.append(i)
    i += a[i]
print(visited, i)
''', '[0, 1, 3] 6', '인덱스0에서1칸, 1에서2칸, 3에서3칸 이동해6에서 종료. 이동값과 방문 인덱스를 구별한다.', ['원소값이 다음 이동폭을 결정','방문 위치의 기록과 종료 위치를 따로 출력'])
add('B','문자 사이에 반환값 넣기','21 14 19', '''
def wrap(s):
    if len(s) == 0:
        return '-'
    return s[0] + wrap(s[1:]) + s[0]
print(wrap('AB'))
''', 'AB-BA', '빈 문자열 호출이−를 반환. B호출은B-B, A호출은AB-BA로 감싼다.', ['종료값이 빈 문자열이 아닌 중앙 표식','재귀 결과를 양쪽 문자 사이에 삽입'])
add('B','원소가 아니라 행을 세기','22 06 03', '''
t = [[2, 4, 5], [1, 3, 7], [6, 8, 2]]
rows = 0
for row in t:
    count = 0
    for x in row:
        if x % 2 == 0:
            count += 1
    if count >= 2:
        rows += 1
print(rows)
''', '2', '행별 짝수 수는2,0,3. 둘 이상인 행은 첫째와 셋째이므로2행.', ['원소 개수에서 조건 충족 행 개수로 집계 단위 전환','안쪽 누적은 행마다 초기화'])
add('B','기억하는 기준과 전달하는 인수','20 19 03', '''
limit = 5
def test(x):
    return x > limit
a = test(6)
limit = 8
b = test(6)
print(a, b)
''', 'True False', '함수는 호출 시점의 전역limit를 읽는다. 첫 호출6>5는True, 둘째6>8은False.', ['전역을 읽기만 하는 함수','같은 인수에 대해 호출 사이의 환경 변경'])
add('B','가장 큰 값을 차례로 옮기기','13 12 11', '''
a = [3, 8, 2, 8]
b = []
for i in range(2):
    m = max(a)
    b.append(m)
    a.remove(m)
print(a, b, sum(a))
''', '[3, 2] [8, 8] 5', '한 회차에 최댓값 하나만 이동한다. 첫8 삭제 후에도8이 남아 둘째회차에도8을 이동, a합5.', ['메서드 이름 판별 대신 선택과 이동의 반복','중복 최댓값을 한 번에 하나씩 처리'])
add('B','첫 실패 뒤에도 이어지는 검사','06 26 04', '''
run = 0
best = 0
for n in [3, 4, 1, 5, 6]:
    if n >= 3:
        run += 1
    else:
        run = 0
    if run > best:
        best = run
print(run, best)
''', '2 2', 'run은1,2,0,1,2. 조건 실패에서 현재 연속 횟수만 초기화되고 best는2로 보존된다.', ['전체 횟수 대신 연속 충족 길이 추적','현재 길이와 과거 최대 길이를 분리'])
add('B','리스트의 앞부분만 반환','19 10 08', '''
def prefix(a):
    i = 0
    while i < len(a) and a[i] >= 0:
        i += 1
    return a[:i]
b = prefix([3, 0, 5, -1, 7])
print(b, sum(b))
''', '[3, 0, 5] 8', '인덱스0,1,2는음수가 아니며 i=3의−1에서 중단. a[:3]=[3,0,5], 합8. 뒤의7은 포함하지 않는다.', ['값 필터 전체 수집 대신 최초 실패 전 구간 반환','종료 인덱스를 슬라이스 경계로 사용'])
add('B','좌표 조건과 값 조건의 교집합','22 15 03', '''
t = [[5, 2, 8], [1, 6, 3], [7, 4, 9]]
s = 0
for i in range(3):
    for j in range(3):
        if j > i and t[i][j] % 2 == 0:
            s += t[i][j]
print(s)
''', '10', 'j>i인 칸은(0,1)의2, (0,2)의8, (1,2)의3. 그중 짝수만 더해10이다.', ['순회 영역을 행열 위치 관계로 제한','위치 통과 후 값 조건을 추가 적용'])

# Revision 1: separate author pass after the frozen textual-screen report.
# Earlier definitions above preserve the exact superseded wording and answers.
REVISIONS = {
 'A/7': ('두 관측을 만족하는 입력 찾기','19 03 06', '''
def f(x):
    if x % 2 == 0:
        return x // 2
    return x + 1
answers = []
for n in range(1, 10):
    if f(n) == 4 and f(n+1) > 4:
        answers.append(n)
print(answers)
''','[8]','f(n)=4의 후보는 홀수3과 짝수8이다. n=3이면 f(4)=2로 탈락, n=8이면 f(9)=10으로 통과한다. 따라서 [8]만 남는다.',
 ['함수 출력에서 가능한 입력을 역으로 선별','인접 입력의 두 번째 관측으로 후보를 제거']),
 'A/22': ('서로 지워지는 연속 기록','11 09 06', '''
out = []
for x in [1, 2, 2, 1, 3]:
    if len(out) > 0 and out[len(out)-1] == x:
        del out[len(out)-1]
    else:
        out.append(x)
print(out)
''','[3]','out은 [1]→[1,2]→[1]→[]→[3]이다. 가운데2가 지워진 뒤1도 만나 지워진다. 빈 리스트에서는 and 앞 조건이 거짓이라 뒤 인덱스 접근을 하지 않는다.',
 ['삭제 결과가 다음 입력의 비교 대상을 바꿈','마지막 원소와 새 입력의 일치에 따라 삭제 또는 추가']),
 'B/1': ('역방향 변환 뒤의 복원','11 09 05', '''
a = [2, 5, 9, 14]
for i in range(3, 0, -1):
    a[i] -= a[i-1]
print(a)
for i in range(1, 4):
    a[i] += a[i-1]
print(a)
''','[2, 3, 4, 5]\n[2, 5, 9, 14]','뒤에서부터 빼면 이전 원소가 아직 원값이어서 차이 [2,3,4,5]가 된다. 앞에서부터 더하면 복원된 이전값을 이용해 [2,5,9,14]로 돌아온다.',
 ['차분 변환과 누적 복원을 순서대로 수행','갱신 방향에 따라 원값 또는 갱신값을 읽음']),
 'B/8': ('건너뛴 원소가 돌아오는 순서','21 10 11', '''
def f(a):
    if len(a) == 0:
        return []
    result = f(a[2:])
    result.append(a[0])
    return result
a = [2, 5, 7, 9]
print(f(a), f(a[1:]))
''','[7, 2] [9, 5]','첫 호출은 [2,5,7,9]→[7,9]→[] 순으로 줄고 복귀 때7,2를 추가한다. 두 번째는 [5,7,9]→[9]→[]에서9,5를 추가한다.',
 ['두 칸씩 축소해 위치 집합을 나누어 선택','재귀 복귀 뒤에 추가하여 선택 원소의 순서를 뒤집음']),
 'B/12': ('먼저 배정된 칸은 다시 쓰지 않기','07 11 04', '''
slots = [2, 4, 3]
count = 0
for need in [3, 2, 4]:
    done = False
    for j in range(len(slots)):
        if not done and slots[j] >= need:
            slots[j] = 0
            count += 1
            done = True
print(count, slots)
''','2 [0, 0, 3]','요구3은 처음 적합한 인덱스1에 배정하여0으로 만든다. 요구2는 인덱스0에 배정한다. 요구4는 남은3에 들어가지 못한다. done은 한 요구가 여러 칸을 차지하지 않게 한다.',
 ['이전 배정이 다음 순회의 가용 데이터를 변경','요구별 최초 적합 칸만 선택하는 상태변수 사용']),
 'B/19': ('재귀 검색에서 없는 값의 처리','21 10 04', '''
def locate(a, key):
    if len(a) == 0:
        return -1
    if a[0] == key:
        return 0
    r = locate(a[1:], key)
    if r == -1:
        return -1
    return r + 1
a = [3, 1, 3, 5]
print(locate(a, 5), locate(a, 2))
''','3 -1','5는 [5]에서 상대위치0을 반환하고 복귀할 때1씩 더해 원래 위치3이 된다. 2는 빈 리스트까지 가서−1을 반환하며 이 값에는1을 더하지 않는다. 최대 깊이는5이다.',
 ['부분 리스트의 상대 위치를 복귀 단계에서 원래 위치로 변환','미발견 표식은 위치 보정 없이 전달']),
 'B/25': ('다시 방문하기 직전에 멈추기','15 08 11', '''
t = [[2, 5], [0, 4], [1, 7]]
seen = [0, 0, 0]
pos = 0
total = 0
while seen[pos] == 0:
    seen[pos] = 1
    total += t[pos][1]
    pos = t[pos][0]
print(pos, total, seen)
''','0 16 [1, 1, 1]','방문 순서는0→2→1→0. 각 처음 방문에서 점수5,7,4를 더하여16. 다시0에 도착하면 seen[0]=1이므로 재가산 없이 종료한다.',
 ['첫 열을 다음 행 주소로 해석하는 간접 순회','방문 이력을 변경해 순환 재방문에서 종료'])}
# Separate author phase after rev/260910_03_info_boundary_review.md.
REVISION2 = {
 'A/12': ('두 상태를 넘겨주는 임시 변수','02 06 11', '''
a = 2
b = 5
trace = []
for k in [1, 2, 3]:
    old = a
    a = b - k
    b = old + k
    trace.append(a)
print(a, b, trace)
''', '3 4 [4, 1, 3]',
 '각 회차의 (a,b)는 (4,3)→(1,6)→(3,4)이다. b는 갱신된 a가 아니라 old에 저장한 이전 a로 계산한다. trace는 각 회차의 새 a만 저장한다.',
 ['임시 변수에 보존한 이전 상태와 갱신된 현재 상태 구분','두 변수 사이의 상태 전달을 회차별 기록으로 연결']),
 'B/10': ('같은 값들 뒤에 삽입하기','08 09 11', '''
a = [2, 5, 5, 9]
value = 5
pos = 0
while pos < len(a) and a[pos] <= value:
    pos += 1
a.insert(pos, value)
print(pos, a)
''', '3 [2, 5, 5, 5, 9]',
 '2와 두 개의5는 모두5 이하이므로 pos가0→1→2→3으로 이동한다. a[3]=9에서 종료하고 인덱스3에5를 넣는다. 같은 값의 첫 위치가 아니라 같은 값들 뒤이다.',
 ['삽입 위치를 상수가 아닌 탐색 종료 상태로 결정','중복값을 통과하는 이하 조건과 위치 경계를 함께 처리']),
 'B/13': ('최대 구간이 여러 개일 때','10 13 06 04', '''
a = [4, 1, 3, 4, 1]
best = sum(a[:3])
start = 0
for i in range(1, len(a) - 2):
    current = sum(a[i:i+3])
    if current > best:
        best = current
        start = i
print(start, best)
''', '0 8',
 '길이3인 구간은 시작 위치0,1,2에서 모두 합8이다. 초기 best=8이고 >는 동률에서 거짓이므로 start는0을 유지한다. 리스트 사본을 수정하는 성질은 사용하지 않는다.',
 ['겹치는 고정 길이 구간들의 합을 후보로 비교','최댓값 동률에서 엄격 부등식이 최초 위치를 보존']),
 'B/17': ('입력 사이에도 유지되는 스위치','03 04 06 11', '''
commands = [1, 0, 1, 1, 0]
on = False
lit = []
for i in range(len(commands)):
    if commands[i] == 1:
        on = not on
    if on:
        lit.append(i)
print(on, lit)
''', 'True [0, 1, 3, 4]',
 '처리 후 on은 True,True,False,True,True이다. 0은 끄기 명령이 아니라 상태를 바꾸지 않는 입력이다. 두 번째 if는 첫 번째와 독립이므로 입력0인 위치1과4도 기록된다.',
 ['각 입력을 독립 판정하지 않고 이전 불리언 상태를 반전 또는 유지','상태 갱신 뒤 별도 조건에서 위치 기록'])}
# Author changes authorized by the user's strict non-clone request; review recorded first.
REVISION3 = {
 'A/3': ('첫 원소가 정하는 순환 이동','19 10 01', '''
def rotate(a):
    k = a[0] % len(a)
    return a[k:] + a[:k]
a = [2, 4, 1, 3]
b = rotate(a)
c = rotate(b)
print(b, c)
''', '[1, 3, 2, 4] [3, 2, 4, 1]',
 '첫 이동량은2이므로 b=[1,3,2,4]. 다음 이동량은 원래의2가 아니라 b의 첫 원소1이다. 두 슬라이스를 이어 붙여 길이를 유지하며 c=[3,2,4,1]이 된다.',
 ['데이터 자체에서 이동량을 정해 두 슬라이스를 재결합','재배열된 첫 원소가 다음 변환을 제어']),
 'A/8': ('동점에서도 하나씩 정해지는 순위','07 13 22 03', '''
t = [[3, 2], [4, 1], [2, 5]]
ranks = []
for i in range(len(t)):
    rank = 1
    for j in range(len(t)):
        if sum(t[j]) > sum(t[i]):
            rank += 1
        elif sum(t[j]) == sum(t[i]) and j < i:
            rank += 1
    ranks.append(rank)
print(ranks)
''', '[2, 3, 1]',
 '행합은5,5,7이다. 행0보다 앞서는 것은 행2뿐이므로2위. 행1은 합7인 행2와 동점이면서 번호가 작은 행0 뒤여서3위. 행2는1위이다. 자기 자신은 j<i가 거짓이라 세지 않는다.',
 ['행별 집계값을 모든 다른 행과 비교해 상대 순위를 구성','동점일 때 위치 순서로 우선순위를 결정']),
 'A/10': ('삭제한 자리부터 다시 검사','08 11 09', '''
a = [3, 3, 1, 4, 4, 2]
i = 1
removed = []
while i < len(a):
    if a[i] == a[i-1]:
        removed.append(i)
        del a[i]
    else:
        i += 1
print(a, removed)
''', '[3, 1, 4, 2] [1, 3]',
 'i=1에서 두 번째3을 지우면 [3,1,4,4,2]. i를 늘리지 않고 새 a[1]=1을 재검사한다. 이후 i=3에서 두 번째4를 지우고 새 a[3]=2를 재검사한다. 기록은 원래 인덱스가 아닌 삭제 당시 위치1,3이다.',
 ['리스트 길이와 위치가 변하는 동안 같은 자리를 재검사','삭제 성공 여부에 따라 인덱스 증가를 달리함']),
 'A/19': ('겹치는 구간을 차례로 뒤집기','07 09 11 02', '''
a = [1, 2, 3, 4, 5]
for ends in [[0, 3], [1, 4]]:
    left = ends[0]
    right = ends[1]
    while left < right:
        old = a[left]
        a[left] = a[right]
        a[right] = old
        left += 1
        right -= 1
print(a)
''', '[4, 5, 1, 2, 3]',
 '첫 구간0~3을 뒤집으면 [4,3,2,1,5]. 이 상태에서 구간1~4의 3과5, 2와1을 교환하여 [4,5,1,2,3]. 두 번째 작업은 원본이 아니라 첫 작업 결과를 대상으로 한다.',
 ['임시 변수로 양끝 원소를 교환하며 구간을 축소','겹치는 두 구간의 변경을 순차 적용']),
 'B/7': ('승인된 요청만 잔여량을 변경','20 19 04 06', '''
stock = 7
def reserve(n):
    global stock
    if n > stock:
        return False
    stock -= n
    return True
accepted = []
for n in [4, 5, 2, 1]:
    if reserve(n):
        accepted.append(n)
print(stock, accepted)
''', '0 [4, 2, 1]',
 '4를 승인하면 재고3. 5는 거절되어 재고3을 유지한다. 2와1을 차례로 승인해 재고1,0. 반환된 참/거짓은 accepted에 기록할지를 결정하고 전역 재고는 뒤 요청의 승인 여부를 바꾼다.',
 ['함수의 조기 반환이 전역 상태 갱신을 차단','변경된 자원이 다음 호출의 허용 여부와 기록을 결정']),
 'B/11': ('덜 바쁜 작업대에 배정하기','22 09 11 04', '''
loads = [0, 0]
chosen = []
for job in [[2, 5], [4, 1], [3, 2], [1, 4]]:
    if loads[0] <= loads[1]:
        k = 0
    else:
        k = 1
    loads[k] += job[k]
    chosen.append(k)
print(chosen, loads)
''', '[0, 1, 1, 0] [3, 3]',
 '두 작업대의 누적량이 동률이면0번을 고른다. 배정 후 loads는 [2,0]→[2,1]→[2,3]→[3,3]. 작업대에 따라 같은 작업의 소요량도 job[0] 또는 job[1]로 달라진다.',
 ['직전 행값 대신 두 누적 상태를 비교해 배정 위치 결정','선택한 위치가 더할 자료 열을 결정하고 다음 선택에 피드백']),
 'B/24': ('순서를 유지하며 두 목록 합치기','08 09 11 03', '''
a = [1, 4, 4]
b = [2, 4, 5]
i = 0
j = 0
out = []
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        out.append(a[i])
        i += 1
    else:
        out.append(b[j])
        j += 1
print(out, a[i:], b[j:])
''', '[1, 2, 4, 4] [] [4, 5]',
 '비교로 선택하는 출처는 a,b,a,a이다. 동점4에서는 <= 때문에 a를 먼저 선택한다. i=3이면 한쪽을 다 써 반복이 종료된다. b에 남은4,5는 out에 자동으로 추가되지 않는다.',
 ['독립된 두 인덱스 중 선택한 출처의 인덱스만 전진','동점 우선순위와 한쪽 소진 종료를 결합해 남은 구간 판별'])}
REVISION4 = {
 'A/17': ('두 상태 사이의 이동 횟수','15 11 06 09', '''
states = [0, 1, 1, 0, 1]
counts = [[0, 0], [0, 0]]
for i in range(1, len(states)):
    before = states[i-1]
    after = states[i]
    counts[before][after] += 1
print(counts)
''', '[[0, 2], [1, 1]]',
 '이동은0→1, 1→1, 1→0, 0→1. 행은 출발 상태, 열은 도착 상태이므로 [0][1]만 두 번 증가한다. 각 상태의 단독 등장 횟수가 아니라 이웃한 두 상태의 관계를 센다.',
 ['이웃한 두 값으로 이차원 기록 위치를 결정','같은 상태 재등장과 상태 사이 이동의 빈도를 구분']),
 'A/21': ('처음 빠진 양의 정수','19 04 06 09', '''
def missing(a):
    need = 1
    for x in a:
        if x == need:
            need += 1
        elif x > need:
            return need
    return need
print(missing([1, 1, 2, 4]), missing([1, 2, 2, 3]))
''', '3 4',
 '첫 호출은 need가1→2로 바뀐 뒤 중복1을 건너뛰고2를 만나3이 된다. 다음4가3보다 크므로3을 조기 반환한다. 둘째는 중복2를 건너뛰어 끝까지 검사하고4를 반환한다.',
 ['탐색 목표가 성공할 때마다 다음 값으로 변경','중복 건너뛰기와 빈틈 발견의 조기 반환을 구분']),
 'B/2': ('여러 출발점이 같은 칸에 도착할 때','01 09 11 06', '''
moves = [1, 0, 2, 1]
hits = [0, 0, 0, 0]
for i in range(len(moves)):
    target = (i + moves[i]) % len(moves)
    hits[target] += 1
print(hits)
''', '[2, 2, 0, 0]',
 '각 출발 위치0,1,2,3의 도착 위치는1,1,0,0이다. hits에는 이동량이나 출발 위치가 아니라 도착한 횟수를 누적하므로0번과1번만2가 된다.',
 ['출발 인덱스와 이동량으로 순환 도착 위치 생성','같은 도착 위치로 모이는 여러 출발점의 횟수 집계']),
 'B/9': ('순서를 지키며 필요한 문자 찾기','14 06 11 03', '''
text = 'AABBAC'
pattern = 'ABA'
p = 0
picked = []
for i in range(len(text)):
    if p < len(pattern) and text[i] == pattern[p]:
        picked.append(i)
        p += 1
print(picked, p == len(pattern))
''', '[0, 2, 4] True',
 '첫 A는0에서, 다음 B는2에서, 마지막 A는4에서 고른다. 선택할 때만 p가 증가하며 같은 글자가 반복돼도 다음 필요 문자와 맞지 않으면 건너뛴다. p=3 이후에는 pattern[3]에 접근하지 않는다.',
 ['선택한 문자에 따라 다음에 찾을 문자가 변경','출현 횟수 대신 순서를 지킨 부분수열의 위치를 구성']),
 'B/15': ('가운데 비교로 줄이는 탐색 구간','19 08 09 04', '''
def locate(a, key):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == key:
            return mid
        if a[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1
a = [2, 4, 7, 9, 12]
print(locate(a, 9), locate(a, 8))
''', '3 -1',
 '9 탐색은 mid=2의7 뒤 구간에서 mid=3의9를 찾아3을 반환한다. 8 탐색은 mid=2의7 뒤로 이동한 다음 mid=3의9 앞까지 줄인다. left=3, right=2로 역전되어−1을 반환한다. 재귀 선형 탐색과 달리 비교 결과로 양쪽 중 한 구간 전체를 버린다.',
 ['정렬된 자료의 가운데 비교로 탐색 구간을 선택','발견 반환과 구간 역전으로 인한 미발견 반환을 구분']),
 'B/16': ('아래의 선택 결과를 위로 전달','22 11 13 07', '''
t = [[4], [2, 5], [7, 1, 3]]
for i in range(1, -1, -1):
    for j in range(len(t[i])):
        t[i][j] += max(t[i+1][j], t[i+1][j+1])
print(t[0][0], t[1])
''', '13 [9, 8]',
 '먼저 둘째 행이2+max(7,1)=9, 5+max(1,3)=8로 바뀐다. 첫째 행은 원래 아래값2,5가 아니라 갱신된9,8을 비교하여4+9=13이 된다. 더 큰 바로 아래 원래값5를 고르는 것과 결과가 다르다.',
 ['아래쪽 부분 경로의 집계 결과를 먼저 계산','인접한 두 후보의 최댓값을 위 행 갱신에 사용']),
 'B/21': ('검사 결과에 따라 합계 칸 복구','19 10 13 11 22', '''
def valid(row):
    return sum(row[:-1]) == row[-1]
t = [[2, 5, 8], [4, 1, 5], [3, 3, 5]]
fixed = []
for i in range(len(t)):
    if not valid(t[i]):
        t[i][-1] = sum(t[i][:-1])
        fixed.append(i)
print(fixed, t)
''', '[0, 2] [[2, 5, 7], [4, 1, 5], [3, 3, 6]]',
 '마지막 칸을 제외한 합계는7,5,6이다. 기록된8,5,5와 비교하여0번과2번 행만 불일치한다. 해당 행의 마지막 칸만7과6으로 복구하고 수정한 행 번호를 남긴다.',
 ['자료 칸과 검사용 합계 칸을 슬라이스로 분리','함수의 일관성 검사 결과가 선택적 복구와 수정 이력을 결정'])}
for q in ITEMS:
    ident=f"{q['group']}/{q['number']}"
    if ident in REVISIONS or ident in REVISION2:
        title,types,code,expected,explanation,axes=(REVISION2 if ident in REVISION2 else REVISIONS)[ident]
        q.update(title=title,types=['IN-'+t for t in types.split()],code=code.strip(),
            expected=expected,explanation=explanation,axes=axes)
    if ident in REVISION3:
        title,types,code,expected,explanation,axes=REVISION3[ident]
        q.update(title=title,types=['IN-'+t for t in types.split()],code=code.strip(),
            expected=expected,explanation=explanation,axes=axes)
    if ident in REVISION4:
        title,types,code,expected,explanation,axes=REVISION4[ident]
        q.update(title=title,types=['IN-'+t for t in types.split()],code=code.strip(),
            expected=expected,explanation=explanation,axes=axes)

# The manually reasoned answer is separate from the captured program output.
def selfcheck():
    rows=[]
    for q in ITEMS:
        stream=io.StringIO()
        with contextlib.redirect_stdout(stream):
            exec(compile(q['code'], '<own-draft>', 'exec'), {})
        observed=stream.getvalue().strip()
        rows.append(dict(item=f"{q['group']}/{q['number']}", expected=q['expected'], observed=observed, match=observed==q['expected']))
    return rows

NOTICE = ('⚠️ 범위 미확정 · 검토용 · 미투입 — 작성자 자체 검산본이며 외부 Opus 맹목풀이·품질감사는 미완료입니다. '
    '2025년 1학년 2학기 중간 기출·확인된 학습지 범위의 프로그래밍 복합 연습입니다. '
    '2026년 학교 공식 시험범위 확정본이 아닙니다. 학생 오답 자료가 없어 개인 약점 맞춤은 미반영입니다.')

def stem(group):
    return f"260910_{'01' if group=='A' else '02'}_info_composite_{group.lower()}"

def header(group, kind):
    return (f'---\ntitle: 정보 복합 연습 {group}형 25제 {kind}\ncreated: 2026-09-10\n'
        'author: 메인 루프\nexecutor: Codex/OMX\ngrade: proposal\nsubject_code: info\n'
        'intended_use: practice\nscope_confirmed: false\nset_id: null\n'
        'status: 검토필요\ngate_status: 외부 검증 전 미투입\n'
        'set_id_note: 동일 날짜 동일 과목 동일 문항수 식별 충돌로 정식 ID 미발급\n---\n\n'
        f'# 정보 복합 연습 {group}형 — 25제 {kind}\n\n> {NOTICE}\n\n'
        '자료 구분: 참고자료=교과서 이미지·개념 문서, 문제자료=퀴즈·2025 중간 기출. '
        '이번 초안은 정제된 개념 문서와 승인 IN 카탈로그를 사용했습니다. '
        '새 교과서 이미지 33장 전체 전사·반영은 아직 완료하지 않았습니다.\n\n'
        '구성: 서답·설명형 25문항, 각 4점(총 100점). 공식 기출의 선택형/단답형 비율을 재현한 모의고사가 아닌 복합 연습지입니다. '
        '난이도는 중상 수준을 목표로 한 작성자 잠정 설계이며 최고난도 인증본은 아닙니다. '
        '정식 Tier는 외부 검토 전 미확정입니다. 보안·CCL 등 비프로그래밍은 이 묶음에서 다루지 않습니다.\n\n')

def question(q):
    return (f"**{q['number']}.** {q['title']} (4점)\n\n"
        '다음 파이썬 3 프로그램의 출력 전체를 줄 순서대로 정확히 쓰시오. '
        f"또한 **{q['axes'][0]}**에 해당하는 중간 상태나 분기 근거를 제시하여 결과를 설명하시오.\n\n"
        f"```python\n{q['code']}\n```\n\n"
        f"[{' + '.join(q['types'])} · Tier 미확정 · DF1·DF7]\n\n"
        '출력: ______________________________________________\n\n'
        '과정: ______________________________________________\n\n'
        '____________________________________________________\n\n')

def display_expected(q):
    return q['expected'].replace('\n', ' ⏎ ')

def answer(q):
    return (f"**{q['number']}.** {q['title']}\n\n**정답: `{display_expected(q)}`**\n\n"
        f"해설: {q['explanation']}\n\n복합 연결: {' → '.join(q['axes'])}.\n\n"
        '채점기준(4점): 출력 전체 정확 2점; 해설에 제시된 핵심 중간값·참/거짓 판정·선택 원소 중 '
        '해당하는 근거를 정확히 제시 1점; 그 근거가 최종 출력으로 이어지는 이유 설명 1점. '
        '동치인 풀이를 인정하며 리스트의 불필요한 공백 차이는 감점하지 않습니다. '
        '출력값 일부만 맞으면 출력 점수는 0점이지만 타당한 과정 점수는 독립적으로 인정합니다.\n\n'
        f"근거 유형: {' + '.join(q['types'])}; `analysis/catalog/info.md` 해당 절. "
        '함수·재귀·유효범위는 기출 출제가 아니라 개념 학습지 근거입니다.\n\n')

def printable(group, kind, subset):
    blocks=[]
    for q in subset:
        if kind=='questions':
            blocks.append(f"<section><h2>{q['number']}. {html.escape(q['title'])} <small>(4점)</small></h2>"
        '<p>프로그램의 출력 전체를 줄 순서대로 정확히 쓰고, 다음 관점의 중간 상태 또는 분기 근거를 설명하시오.</p>'
                f"<p><b>{html.escape(q['axes'][0])}</b></p><pre>{html.escape(q['code'])}</pre>"
                '<p>출력: __________________________________________________</p>'
                '<p>과정: __________________________________________________</p>'
                '<p>________________________________________________________</p></section>')
        else:
            blocks.append(f"<section><h2>{q['number']}. {html.escape(q['title'])}</h2>"
                f"<p><b>정답:</b></p><pre>{html.escape(q['expected'])}</pre>"
                f"<p>{html.escape(q['explanation'])}</p>"
                f"<p>복합 연결: {html.escape(' → '.join(q['axes']))}</p>"
                '<p>채점: 출력 전체 2점 + 핵심 중간값·분기 근거 1점 + 최종 결과 연결 설명 1점. '
                '동치 풀이 인정. 리스트 공백 차이 무감점. 부분 출력은 출력 점수 0점, 과정은 별도 채점.</p></section>')
    label='문제지' if kind=='questions' else '답지·해설'
    return ('<!doctype html><html lang="ko"><meta charset="utf-8">'
        f'<title>정보 복합 {group}형 25제 {label} — 검토용</title>'
        '<style>body{font:15px/1.65 "Malgun Gothic",sans-serif;max-width:850px;margin:35px auto;color:#111}'
        'h1{font-size:24px}h2{font-size:18px}small{font-size:13px}pre{font:14px/1.5 Consolas,monospace;'
        'background:#f5f5f5;padding:12px;white-space:pre-wrap}section{break-inside:avoid;margin:30px 0;'
        'border-bottom:1px solid #aaa;padding-bottom:20px}.notice{border:2px solid #a60;padding:12px}'
        '@page{size:A4;margin:15mm}@media print{body{margin:0;font-size:12px}pre{font-size:12px}}</style>'
        f'<h1>정보 복합 {group}형 25제 — {label} (검토용)</h1><p class="notice">{html.escape(NOTICE)}</p>'
        '<p>서답·설명형 25문항 × 4점 = 100점. 정식 세트ID 미발급 초안. '
        '프로그래밍 부분 연습(비프로그래밍 제외). 새 교과서33장 전면 반영 미완료. '
        '최고난도 인증본 아님. 파이썬3 기준, 인덱스는0부터 시작합니다.</p>'
        '<p>이름: ______________　날짜: ______________</p>'+''.join(blocks)+'</html>')

def write_outputs():
    results=selfcheck()
    assert len(results)==50 and all(r['match'] for r in results), results
    screen_path=OUT/'rev/260910_02_info_novelty_text_screen.json'
    screen=json.loads(screen_path.read_text(encoding='utf-8')) if screen_path.exists() else None
    comparisons={r['item']:r for r in screen['rows']} if screen else {}
    revised_nearest={
        'A/7':'output/260910/260910_01_info_composite_a_questions_review.md / A3',
        'A/19':'corpus/SUP-info-2026-01/transcript.md / p06 abc',
        'A/22':'corpus/EX-info-20252M/transcript.md / 선택15',
        'B/1':'output/260910/260910_01_info_composite_a_questions_review.md / A2',
        'B/8':'corpus/SUP-info-2026-01/transcript.md / Quiz14',
        'B/12':'output/260910/260910_01_info_composite_a_questions_review.md / A9',
        'B/19':'corpus/SUP-info-2026-01/transcript.md / p06 list_sum',
        'B/25':'output/260910/260910_02_info_composite_b_questions_review.md / B18',
        'A/12':'output/260910/260910_01_info_composite_a_questions_review.md / A2',
        'B/10':'output/260910/260910_02_info_composite_b_questions_review.md / B12',
        'B/13':'output/260910/260910_02_info_composite_b_questions_review.md / B11',
        'B/17':'output/260910/260910_01_info_composite_a_questions_review.md / A17'}
    OUT.mkdir(parents=True,exist_ok=True)
    revised_nearest.update({
        'A/3':'output/260910/260910_01_info_composite_a_questions_review.md / A13',
        'A/8':'output/260910/260910_01_info_composite_a_questions_review.md / A25',
        'A/10':'output/260910/260910_01_info_composite_a_questions_review.md / A22',
        'A/19':'output/260910/260910_02_info_composite_b_questions_review.md / B6',
        'B/7':'output/260910/260910_01_info_composite_a_questions_review.md / A1',
        'B/11':'output/260910/260910_02_info_composite_b_questions_review.md / B4',
        'B/24':'output/260910/260910_02_info_composite_b_questions_review.md / B6',
    })
    revised_nearest.update({
        'A/17':'output/260910/260910_02_info_composite_b_questions_review.md / B2',
        'A/21':'output/260910/260910_02_info_composite_b_questions_review.md / B3',
        'B/2':'output/260910/260910_01_info_composite_a_questions_review.md / A14',
        'B/9':'output/260910/260910_02_info_composite_b_questions_review.md / B3',
        'B/15':'output/260910/260910_02_info_composite_b_questions_review.md / B19',
        'B/16':'output/260910/260910_01_info_composite_a_questions_review.md / A25',
        'B/21':'output/260910/260910_01_info_composite_a_questions_review.md / A4',
    })
    for group in ['A','B']:
        subset=[q for q in ITEMS if q['group']==group]
        assert [q['number'] for q in subset]==list(range(1,26))
        qs='---\n\n'.join(question(q) for q in subset)
        answers='---\n\n'.join(answer(q) for q in subset)
        table='| no | answer | typeID·Tier | solution(core) / trap |\n|---|---|---|---|\n'
        table+=''.join(f"| {q['number']} | **`{display_expected(q)}`** | {'+'.join(q['types'])}·미확정 | {q['explanation']} |\n" for q in subset)
        table+='\n※ 정답의 ⏎ 표시는 실제 출력의 줄바꿈입니다.\n'
        base=stem(group)
        products={f'{base}_questions_review.md':header(group,'문제지')+qs,
            f'{base}_answers_review.md':header(group,'답지·해설')+'## 정답표\n\n'+table+'\n## 해설\n\n'+answers,
            f'{base}_review.md':header(group,'통합본')+qs+'\n## 정답표\n\n'+table+'\n## 해설\n\n'+answers}
        for kind in ['questions','answers']:
            products[f'{base}_{kind}_review.html']=printable(group,kind,subset)
        for name,data in products.items():
            (OUT/name).write_text(data,encoding='utf-8')
        # Proposal ledger: a pair of design axes is not evidence of corpus-wide novelty.
        with (OUT/f'{base}.novelty.tsv').open('w',encoding='utf-8-sig',newline='') as f:
            writer=csv.writer(f,delimiter='\t')
            writer.writerow(['item_id','type_id','invariant','non_numeric_axis_1','non_numeric_axis_2','structural_difference','nearest_prior','verdict'])
            for q in subset:
                ident=f"{group}/{q['number']}"
                row=comparisons.get(ident)
                nearest=revised_nearest.get(ident) or (row['source']+' / '+row['anchor'] if row else 'UNRESOLVED')
                writer.writerow([ident,'+'.join(q['types']),q['explanation'],*q['axes'],
                    ' → '.join(q['axes']),nearest,'BLOCKED'])
    # Check actual saved problem statements, not just in-memory source entries.
    validation=[]
    catalog=(ROOT/'analysis/catalog/info.md').read_text(encoding='utf-8-sig')
    for group in ['A','B']:
        doc=(OUT/f'{stem(group)}_questions_review.md').read_text(encoding='utf-8')
        ids=re.findall(r'^\*\*(\d+)\.\*\*',doc,re.M)
        assert ids==[str(n) for n in range(1,26)]
        blocks=re.findall(r'```python\n(.*?)\n```',doc,re.S)
        assert len(blocks)==25
        subset=[q for q in ITEMS if q['group']==group]
        for q,code in zip(subset,blocks):
            stream=io.StringIO()
            with contextlib.redirect_stdout(stream):
                exec(compile(code,'<saved-question>','exec'),{})
            assert stream.getvalue().strip()==q['expected']
            assert len(set(q['types']))>=2 and all(f'유형 {t}:' in catalog for t in q['types'])
            validation.append(f"{group}/{q['number']}")
        adoc=(OUT/f'{stem(group)}_answers_review.md').read_text(encoding='utf-8')
        assert re.findall(r'^\| (\d+) \|',adoc,re.M)==ids
        assert re.findall(r'^\*\*정답: `(.*?)`\*\*',adoc,re.M)==[display_expected(q) for q in subset]
        assert '정답:' not in doc and '해설:' not in doc
        for kind in ['questions','answers']:
            h=(OUT/f'{stem(group)}_{kind}_review.html').read_text(encoding='utf-8')
            assert h.count('<section>')==25 and '검토용' in h
    frozen=[]
    input_paths=[Path(__file__),ROOT/'analysis/catalog/info.md',ROOT/'corpus/SUP-info-2026-01/transcript.md']
    if screen:
        input_paths.append(screen_path)
    for path in input_paths:
        b=path.read_bytes(); frozen.append(dict(path=path.relative_to(ROOT).as_posix(),bytes=len(b),sha256=hashlib.sha256(b).hexdigest()))
    artifacts=[]
    for p in sorted(OUT.glob('260910_0[12]_info_composite_*')):
        b=p.read_bytes();artifacts.append(dict(path=p.relative_to(ROOT).as_posix(),bytes=len(b),sha256=hashlib.sha256(b).hexdigest()))
    evidence=dict(author='메인 루프',executor='Codex/OMX',grade='proposal',
        command='python -X utf8 analysis/wip/260910_info_composite_author.py --write',
        expected_ids=[f'{g}/{n}' for g in ['A','B'] for n in range(1,26)],observed_ids=validation,
        missing=[],extra=[],duplicates=[],answer_mismatches=[],
        warnings=['external_review_pending','novelty_review_pending','student_errors_missing','textbook_refinement_pending','set_id_unissued','tier_unconfirmed'],
        release='BLOCKED',results=results,inputs=frozen,artifacts=artifacts,revision1_replacements=sorted(REVISIONS),revision2_replacements=sorted(REVISION2),revision3_replacements=sorted(REVISION3),revision4_replacements=sorted(REVISION4),
        first_pass_corrections=[{'item':'A/1','old':'7','new':'2'},{'item':'A/13','old':'7 4','new':'10 4'},{'item':'A/19','old':'15','new':'16'}])
    (OUT/'260910_03_info_selfcheck.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2),encoding='utf-8')
    print('SELF-CHECK: 50/50 saved questions agree with authored answers; missing=0 extra=0 duplicates=0; split=4 MD + 4 HTML; release=BLOCKED (6 warnings).')

if __name__ == '__main__':
    if '--write' in sys.argv:
        write_outputs()
    else:
        results=selfcheck()
        print(json.dumps(results,ensure_ascii=False,indent=2))
        raise SystemExit(0 if all(r['match'] for r in results) else 1)
