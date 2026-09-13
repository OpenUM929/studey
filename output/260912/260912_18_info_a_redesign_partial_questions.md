---
title: 정보 A형 최상위 사고력 재설계 — 부분 작성 후보
created: 2026-09-12
author: 메인 루프
executor: Codex/OMX
execution_model: gpt-6-astra
execution_effort: medium
grade: proposal
subject_code: info
intended_use: practice
scope_confirmed: false
scope: partial
set_id: null
round: 2
status: 검토필요 — 전수 작성·독립 감사·배포 미완료
---

# 정보 A형 — 최상위 사고력 재설계 부분 후보

> ⚠️ 범위 미확정 · 미배포 · 현재 21/25문항. 전체 25문항 완성본이 아닙니다.
> 목표는 문항별 최상위+필수 사고력이며 **달성·정식 Tier는 미확정**입니다. 4점이라는 배점을 난도 근거로 쓰지 않습니다.
> 기존 2라운드의 재설계이며 기존 후보·감사·revision4를 보존합니다. 정식 세트ID는 발급하지 않습니다.

기존 슬롯 번호를 유지합니다. 각 문항 4점, 현재 부분 합계 84점이며 전체 목표는 25문항·100점입니다.
문제에 제시된 파이썬3 코드의 실행 의미를 사용합니다. 임의 입력 전수 열거가 아니라 답이 결정되는 과정을 쓰시오.
함수 사용은 학습지 근거이며 올해 공식 시험범위 확정을 의미하지 않습니다.

## 서답형

**1.** 뒤집은 수가 섞인 관측값 복원 (4점)

```python
def mix(n):
    original = n
    reverse = 0
    while n > 0:
        reverse = reverse * 10 + n % 10
        n //= 10
    return 2 * original + reverse
```

n은 여섯 자리 양의 정수이다. 여섯 자리 숫자는 모두 1 이상 9 이하이고 서로 다르다.
mix(n)의 반환값은 1211247이다. 가능한 n을 모두 구하시오.
자리별 계산에서 발생하는 올림까지 반영하여 다른 답이 없음을 보이시오.
전체 여섯 자리 수를 대입한 결과 목록만으로 완전성을 주장할 수 없다.

[IN-01 + IN-02 + IN-08 · Tier 미확정]

---

**2.** 순환 갱신이 처음 소멸하는 시점 (4점)

```python
def vanish(a):
    step = 0
    while 1 in a:
        b = []
        for i in range(len(a)):
            b.append((a[i] + a[(i+1) % len(a)]) % 2)
        a = b
        step += 1
    return step
```

입력 a는 길이 16이고 각 원소는 0 또는 1이다. 1은 정확히 여덟 개 들어 있다.
vanish(a)가 8을 반환하는 서로 다른 입력 리스트는 모두 몇 개인가?
회전하여 겹치는 리스트도 인덱스별 값이 다르면 서로 다른 입력으로 센다.
왜 8회째 모두 0이라는 조건만 확인해서는 안 되는지도 설명하시오.
새 리스트 b를 완성한 뒤에 a를 바꾸므로 한 회 안에서는 갱신 전 a만 읽는다.

[IN-07 + IN-09 + IN-11 · Tier 미확정]

---

**3.** 전파 순서가 만드는 세 번째 순회의 종료 (4점)

```python
def spread(edges):
    reached = [1, 0, 0, 0, 0, 0, 0]
    rounds = 0
    while reached[6] == 0:
        for row in edges:
            if reached[row[0]] == 1:
                reached[row[1]] = 1
        rounds += 1
    return rounds
```

edges에는 [0,1], [1,2], [2,3], [3,4], [4,5], [5,6]이 각각 한 번씩 들어 있다.
여섯 행의 순서를 임의로 정한 뒤에는 모든 순회에서 같은 순서를 사용한다.
spread(edges)가 3을 반환하는 서로 다른 행 순서는 모두 몇 개인가?
한 번 갱신한 reached는 같은 순회의 뒤쪽 행에서도 즉시 사용된다.
답을 구할 때 6!개 실행 결과를 나열하지 말고, 행의 위치 관계가 반환값을 결정하는 조건과
그 조건을 만족하는 순서를 빠짐없이 세는 과정을 제시하시오.

[IN-08 + IN-15 + IN-22 · Tier 미확정]

---

**4.** 같은 문자 두 개를 합친 뒤 남을 수 있는 문자열 (4점)

```python
def shrink(choices):
    a = ['A'] * 20
    for i in choices:
        if i < 0 or i + 1 >= len(a):
            return []
        if a[i] != a[i+1]:
            return []
        if a[i] == 'A':
            a[i] = 'B'
        else:
            a[i] = 'A'
        del a[i+1]
    return a
```

choices는 정수 인덱스들을 담은 유한 리스트이며 길이는 자유롭게 정한다.
반환값이 빈 리스트가 아니고, 반환 리스트에서 이웃한 두 문자가 같은 곳도 없어야 한다.
이 조건에서 가능한 반환 리스트를 모두 나타내고, 가장 짧은 것과 가장 긴 것을 구하시오.
가능하다고 주장하는 모든 리스트가 실제 선택 순서로 만들어짐을 설명하고,
최단·최장 반환값 각각을 만드는 choices도 하나씩 제시하시오.
인덱스는 매번 삭제가 끝난 현재 리스트를 기준으로 한다. 길이가 1이면 이웃 조건을 만족한다.

[IN-04 + IN-11 + IN-14 · Tier 미확정]

---

**5.** 평균 이상만 남기는 과정의 가장 작은 최악 입력 (4점)

```python
def rounds(a):
    count = 0
    while len(a) > 1:
        total = sum(a)
        size = len(a)
        b = []
        for x in a:
            if size * x >= total:
                b.append(x)
        a = b
        count += 1
    return count
```

a는 서로 다른 여섯 개의 음이 아닌 정수를 오름차순으로 담은 리스트이고 첫 원소는 0이다.
rounds(a)가 5가 되어야 한다. 이때 a의 마지막 원소의 최솟값과 그 최솟값을 달성하는 a를 모두 구하시오.
실수로 평균을 반올림하지 않고 제시된 정수 비교식 그대로 판정한다.

[IN-08 + IN-11 + IN-13 · Tier 미확정]

---

**6.** 서로 다른 용량의 관측으로 승인 순서 복원 (4점)

```python
def used(a, capacity):
    total = 0
    for x in a:
        if total + x <= capacity:
            total += x
    return total
```

a에는 서로 다른 양의 정수 네 개가 들어 있고 그 합은 16이다. 순서는 알려져 있지 않다.
같은 a를 사용한 관측이 다음과 같다.
| capacity | 1 | 6 | 13 | 15 |
|---|---|---|---|---|
| used(a,capacity) | 0 | 6 | 11 | 14 |
가능한 a를 모두 구하시오. 승인되지 않은 원소를 뒤에서 다시 처리하지 않는다.
각 관측이 입력의 어느 부분을 제한하는지 연결하고, 모든 후보에 대한 완전성을 설명하시오.

[IN-04 + IN-06 + IN-09 · Tier 미확정]

---

**7.** 두 행의 중복을 최소화하는 표 (4점)

```python
def score(a):
    total = 0
    for i in range(4):
        for j in range(i+1, 4):
            same = 0
            for k in range(6):
                if a[i][k] == 1 and a[j][k] == 1:
                    same += 1
            total += same * same
    return total
```

a는 4행 6열의 표이며 모든 원소는 0 또는 1이다.
각 행의 1은 정확히 세 개, 각 열의 1은 정확히 두 개이다.
0번 열과 1번 열은 모두 위에서 아래로 [1,1,0,0]이다.
score(a)의 최솟값을 구하고, 최솟값을 만드는 표의 형태를 빠짐없이 설명한 뒤 그 개수를 구하시오.
행·열 번호는 고정되어 있다. 번호를 바꾸어 서로 다른 표가 되면 별개의 표로 센다.

[IN-07 + IN-15 + IN-22 · Tier 미확정]

---

**8.** 겹친 두 글자 기록을 모두 한 번씩 만드는 문자열 (4점)

```python
def record(s):
    chars = 'ABC'
    a = [[0,0,0], [0,0,0], [0,0,0]]
    for k in range(len(s)-1):
        for i in range(3):
            for j in range(3):
                if s[k] == chars[i] and s[k+1] == chars[j]:
                    a[i][j] += 1
    return a
```

s는 A,B,C로만 이루어진 길이 10의 문자열이고 첫 글자는 A이다.
record(s)가 [[1,1,1],[1,1,1],[1,1,1]]이 되는 서로 다른 문자열 s는 모두 몇 개인가?
각 두 글자는 서로 겹칠 수 있다. 예를 들어 ABA에서는 AB와 BA가 각각 한 번 기록된다.
조건을 만족하는 문자열의 예를 하나 제시하고, 경우의 수 계산에서 불가능한 연결이나 중복을 세지 않았음을 설명하시오.

[IN-14 + IN-15 + IN-22 · Tier 미확정]

---

**9.** 모든 접두 합이 양수인 순환 시작점 (4점)

```python
def starts(a):
    answer = []
    for start in range(len(a)):
        total = 0
        good = True
        for k in range(len(a)):
            total += a[(start+k) % len(a)]
            if total <= 0:
                good = False
        if good:
            answer.append(start)
    return answer
```

a에는 1이 여덟 개, -2가 세 개 들어 있다. 원소의 순서는 자유롭다.
가능한 모든 a에 대하여 len(starts(a))가 가질 수 있는 값을 모두 구하시오.
또한 주어진 a를 한 번 왼쪽부터 읽어 얻은 누적합만으로 starts(a)에 들어갈 인덱스를 정하는 방법을 제시하시오.
열한 시작점 각각에 대해 다시 누적하는 방법은 두 번째 요구의 답이 아니다.
중간 합이 한 번이라도 0이면 그 시작점은 부적합하다.

[IN-06 + IN-07 + IN-09 · Tier 미확정]

---

**10.** 가까운 위치로만 연결된 입력의 최대 교환 (4점)

```python
def arrange(a):
    count = 0
    for i in range(len(a)):
        while a[i] != i + 1:
            j = a[i] - 1
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
            count += 1
    return count
```

a에는 정수 1부터 10까지가 각각 한 번씩 들어 있다.
초기 입력에서 모든 i에 대하여 -2 ≤ a[i] - (i+1) ≤ 2이다.
arrange(a)의 반환값의 최댓값과, 그 최댓값을 만드는 초기 리스트 a를 모두 구하시오.
위 거리 제한은 초기 입력에만 적용한다. 실행 중 리스트는 변경된다.
최댓값의 상한, 그 상한의 실현 가능성, 제시한 것 외에 최적 입력이 없다는 근거를 모두 쓰시오.

[IN-08 + IN-09 + IN-11 · Tier 미확정]

---

**11.** 두 오류 위치를 반드시 구별하는 최소 검사 (4점)

```python
def probe(a, positions):
    count = 0
    for i in positions:
        if a[i] == 1:
            count += 1
    return count
```

a는 길이 6인 0과 1의 리스트이며, 정확히 두 원소가 1이다.
검사자는 a를 직접 읽지 못하고 probe의 반환값만 볼 수 있다. 한 번의 검사에서는
서로 다른 인덱스들을 담은 positions를 자유롭게 정한다. 빈 리스트도 허용한다.
모든 가능한 a에 대해 두 1의 위치를 반드시 알아내려 한다.

(가) 검사 목록들을 처음에 모두 정해 놓는 방식에서 필요한 검사 횟수의 최솟값을 구하고,
그 횟수를 달성하는 실제 positions 목록들과 모든 반환 결과의 해석 방법을 제시하시오.
(나) 앞의 반환값을 본 뒤 다음 positions를 정할 수 있게 하면, 최악의 경우에 필요한
검사 횟수를 (가)보다 줄일 수 있는가? 가능한 모든 입력을 보장하는 근거로 답하시오.
한 입력에서 우연히 빨리 알아내는 횟수가 아니라, 가장 불리한 입력까지 보장하는 횟수를 묻는다.

[IN-04 + IN-06 + IN-09 · Tier 미확정]

---

**12.** 방향을 바꾼 관측은 입력을 더 구별하는가 (4점)

```python
def observe(a, step):
    result = []
    for start in range(len(a)):
        j = start
        top = 0
        count = 0
        for k in range(len(a)):
            if a[j] > top:
                top = a[j]
                count += 1
            j = (j + step) % len(a)
        result.append(count)
    return result
```

a는 1부터 10까지의 정수를 한 번씩 담은 길이 10인 리스트다.
observe(a, 1)의 반환값은 다음과 같다.

`[3, 2, 3, 2, 1, 4, 3, 4, 3, 2]`

(가) 이 관측과 일치하는 서로 다른 a는 모두 몇 개인지 구하시오.
모든 입력을 나열하는 대신 관측이 강제하는 대소관계와 경우를 세는 근거를 제시하시오.
(나) 입력을 더 구별하기 위해 observe(a, 9)도 실행하자는 제안이 나왔다.
이 추가 관측은 (가)의 후보를 실제로 줄일 수 있는가? 가능한 추가 반환값을 모두 제시하고,
그 밖의 반환값이 나올 수 없는 이유를 설명하시오. 두 방향의 코드는 같은 a에서 실행한다.

[IN-04 + IN-06 + IN-09 · Tier 미확정]

---

**13.** 두 누적 기록을 고정한 세 번째 기록의 한계 (4점)

```python
def record(s):
    na = 0
    nb = 0
    ab = 0
    bc = 0
    abc = 0
    for ch in s:
        if ch == 'A':
            na += 1
        elif ch == 'B':
            nb += 1
            ab += na
        else:
            bc += nb
            abc += ab
    return [ab, bc, abc]
```

문자열 s에는 A가 5개, B가 4개, C가 5개 있으며 다른 문자는 없다.
record(s)의 첫째 원소와 둘째 원소는 모두 10이다.

셋째 원소의 최댓값을 구하고, 그 최댓값을 만드는 서로 다른 문자열 s가 모두 몇 개인지 구하시오.
최댓값을 만들 수 있다는 예시뿐 아니라 상한과 최적 문자열을 빠짐없이 세는 근거를 제시하시오.
같은 문자끼리의 교환은 다른 문자열로 세지 않는다.

[IN-04 + IN-06 + IN-14 · Tier 미확정]

---

**14.** 총 교환 수가 같은 입력들의 완료 시간 (4점)

```python
def move(a):
    rounds = 0
    swaps = 0
    while True:
        b = a[:]
        changed = False
        for i in range(len(a)-1):
            if a[i] == 1 and a[i+1] == 0:
                b[i] = 0
                b[i+1] = 1
                swaps += 1
                changed = True
        if not changed:
            return [rounds, swaps]
        a = b
        rounds += 1
```

초기 a는 0 여섯 개와 1 여섯 개로 이루어진 길이 12인 리스트다.
move(a)의 둘째 반환값이 18이라는 사실만 알고 있다.

첫째 반환값의 최솟값과 최댓값을 각각 구하고, 각 값을 만드는 초기 a의 개수를 각각 구하시오.
최솟값을 만드는 입력들의 공통 구성 규칙과, 최댓값을 만드는 입력을 모두 제시하여
경우를 빠뜨리거나 같은 입력을 중복하여 세지 않았음을 설명하시오.
코드에서 한 회의 for문은 a를 읽고 b에 기록한다는 점에 유의하시오.

[IN-08 + IN-09 + IN-06 · Tier 미확정]

---

**15.** 같아지는 순간까지 가장 많이 바뀌는 원형 리스트 (4점)

```python
def settle(a):
    start = a[:]
    rounds = 0
    total = 0
    while True:
        b = a[:]
        changed = 0
        for i in range(16):
            s = a[(i+15)%16] + a[i] + a[(i+1)%16]
            if s >= 2:
                b[i] = 1
            else:
                b[i] = 0
            if b[i] != a[i]:
                changed += 1
        if changed == 0:
            return [rounds, total]
        if b == start:
            return [-1, -1]
        total += changed
        rounds += 1
        a = b
```

초기 a는 0 여덟 개와 1 여덟 개를 담은 길이 16인 리스트다.
인덱스 15와 0도 서로 이웃하며, 한 회에는 이전 a만 읽어 모든 새 값을 동시에 정한다.

(가) [-1,-1]을 반환하는 초기 입력을 모두 구하고, 그 밖의 모든 허용 입력에서는
변화가 멈추어 음수가 아닌 두 값을 반환함을 설명하시오.
(나) 음수가 아닌 값을 반환하는 입력들 중 둘째 반환값의 최댓값과,
그 최댓값을 만드는 초기 리스트의 개수를 구하시오. 최적 입력의 전수 구성 규칙과
그때의 첫째 반환값도 제시하시오. 원형으로 회전한 리스트도 인덱스별 원소가 다르면 서로 다른 입력이다.

[IN-08 + IN-09 + IN-04 · Tier 미확정]

---

**16.** 네 번 이동한 결과로 한 번 이동 규칙을 얼마나 복원할 수 있는가 (4점)

```python
def four(p):
    result = []
    for i in range(12):
        x = i
        for k in range(4):
            x = p[x]
        result.append(x)
    return result
```

p는 0부터 11까지의 정수를 한 번씩 담은 길이 12인 리스트다.
four(p)의 반환값은 다음과 같다.

`[1, 2, 0, 4, 5, 3, 7, 8, 6, 10, 11, 9]`

(가) 이 결과와 일치하는 서로 다른 p는 모두 몇 개인지 구하시오.
경우를 빠뜨리지 않았다는 근거와, 같은 p를 중복하여 세지 않았다는 근거를 제시하시오.
(나) 가능한 p 중 어느 것이 주어져도, 어느 인덱스에서 시작해도,
`x = p[x]`를 정확히 K번 반복하면 시작 인덱스로 돌아오도록 보장하는 양의 정수 K의 최솟값을 구하시오.
모든 p에 대한 보장과 더 작은 K가 불가능한 근거를 구분해 설명하시오.

[IN-09 + IN-11 · Tier 미확정]

---

**17.** 어느 두 칸을 잃어도 유지되는 반환값의 한계 (4점)

```python
def first_gap(a):
    need = 1
    for x in a:
        if x > need:
            return need
        need += x
    return need

def guarantee(a):
    worst = None
    for p in range(len(a)):
        for q in range(p+1, len(a)):
            b = []
            for i in range(len(a)):
                if i != p and i != q:
                    b.append(a[i])
            value = first_gap(b)
            if worst == None or value < worst:
                worst = value
    return worst
```

a는 양의 정수 12개를 비내림차순으로 나열한 리스트이다. 값의 상한과 총합 제한은 없다.
같은 값이 여러 칸에 있어도 서로 다른 칸으로 취급한다. 위 코드에서 None은 아직 값을 저장하지 않았다는 초기 표식이다.

(1) guarantee(a)의 가능한 최댓값을 구하고, 그 값을 만드는 서로 다른 리스트 a를 빠짐없이 나타내시오.
그러한 리스트의 개수도 구하시오. 무한히 큰 값을 허용해도 더 나은 답이 없다는 근거가 필요하다.
(2) guarantee(a)를 계산할 때 언제나 마지막 두 칸만 제외하면 충분하다는 주장은 옳은가?
옳지 않다면 조건을 만족하는 a 하나와, 마지막 두 칸을 제외한 반환값 및 그보다 작은 반환값을 만드는 두 칸을 제시하시오.
프로그램으로 후보들을 모두 나열한 목록은 최적성·완전성의 풀이 근거를 대신할 수 없다.

[IN-04 + IN-06 + IN-09 · Tier 미확정]

---

**18.** 합쳐진 자리별 관측에서 원래 정수의 범위 복원 (4점)

```python
def digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def observe(n):
    total = 0
    p = 1
    for i in range(18):
        total += digits(n+p)
        p *= 10
    return [digits(n), total]
```

n은 십진법으로 정확히 18자리인 양의 정수이며, observe(n)의 반환값은 [81, 1287]이다.
가능한 n의 개수와 그중 가장 작은 n을 구하시오. 두 관측값이 원래 정수의 자릿값 배치를 어떻게
제한하는지 설명하고, 가능한 경우를 빠짐없이 세는 근거를 제시하시오.
개수는 이항계수를 사용한 정확한 정수식으로 제시해도 된다. 컴퓨터로 18자리 정수를 모두
대입한 목록은 풀이 근거를 대신하지 못한다. n+p는 19자리가 되어도 그대로 계산한다.

[IN-01 + IN-08 + IN-06 · Tier 미확정]

---

**19.** 원래 값을 최소로 보관하는 갱신 순서 설계 (4점)

```python
def update(a, order, keep):
    n = len(a)
    saved = [0] * n
    for j in keep:
        saved[j] = a[j]
    for i in order:
        j = (i+1) % n
        k = (i+4) % n
        if j in keep:
            x = saved[j]
        else:
            x = a[j]
        if k in keep:
            y = saved[k]
        else:
            y = a[k]
        a[i] = x+y
    return a
```

입력 a는 양의 정수 12개로 이루어진다. order는 0~11을 각각 한 번씩 나열한 리스트이고,
keep은 0~11 중 일부를 중복 없이 선택한 리스트이다. keep에 들어 있는 값의 순서는 무관하다.
호출 전 a를 u라 할 때, 모든 i에 대해 반환된 a[i]가 u[(i+1)%12]+u[(i+4)%12]이 되게 하려 한다.
order와 keep은 a의 값을 보기 전에 정하며, 어떤 양의 정수 입력에도 같은 선택이 맞아야 한다.
코드는 변경할 수 없다. 보관 비용은 len(keep)으로 센다(나머지 saved 칸의 초기값0은 비용에서 제외).

가능한 최소 보관 비용과, 그 최소 비용을 달성할 수 있는 서로 다른 keep 선택의 수를 구하시오.
같은 keep에 대해 가능한 order가 여러 개여도 keep은 한 번만 센다.
최소 비용을 달성하는 keep과 order 한 쌍도 제시하고, 더 적게 보관할 수 없는 이유 및
세어 낸 각 keep에 적절한 order가 실제로 존재하는 이유를 설명하시오.

[IN-09 + IN-11 + IN-04 · Tier 미확정]

---

**20.** 양방향 누적값을 같게 만드는 최소 입력 (4점)

```python
def measure(a):
    p = 0
    q = 0
    for i in range(len(a)):
        if a[i] == 1:
            p *= 2
        else:
            p += 1
        if a[len(a)-1-i] == 1:
            q *= 2
        else:
            q += 1
    return [p, q]
```

리스트 a는 0 여덟 개와 1 네 개로 이루어진다. 같은 값 0이 세 번 연속 나오는 곳은 없다.
measure(a)의 두 원소가 같아야 한다. 이 조건에서 두 원소의 합의 최솟값과,
그 최솟값을 만드는 a를 모두 구하시오. 최소성뿐 아니라 다른 최적 입력이 없는 근거도 제시하시오.
입력들을 컴퓨터로 모두 나열한 목록은 풀이 근거로 대신할 수 없다.

[IN-06 + IN-04 + IN-09 · Tier 미확정]

---

**22.** 삭제된 실행 기록에서 문자열 복원 (4점)

```python
def inspect(s):
    a = []
    area = 0
    peak = 0
    empty = []
    top = ''
    for i in range(len(s)):
        if len(a) > 0 and a[-1] == s[i]:
            del a[-1]
        else:
            a.append(s[i])
        area += len(a)
        if len(a) > peak:
            peak = len(a)
        if len(a) == 0:
            empty.append(i+1)
        if i == 4:
            top = a[-1]
    return [area, peak, empty, top]
```

s는 A 네 개, B 두 개, C 두 개로 이루어진 길이 8의 문자열이며 첫 글자는 A이다.
실행은 오류 없이 끝났고 반환값은 [14, 3, [8], 'C']였다.
s를 모두 구하시오. a의 길이가 증가·감소하는 실행 경로를 먼저 복원하고,
같은 길이 경로에서도 글자 배치가 달라질 수 있음을 고려하여 빠짐없음을 설명하시오.
empty의 숫자는 인덱스가 아니라 처리한 글자 수이다.

[IN-11 + IN-14 + IN-06 · Tier 미확정]
