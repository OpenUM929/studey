# SUP-info-2026-01 — 전사 (transcript)

> 1차 정제(REFINE) 산출물. **전사만 한다 — 분류 판단은 한 글자도 적지 않는다**(CLAUDE.md 원칙 1).
> 판독 이미지: `corpus/_images/SUP-info-2026-01/pNN.png` · 원본: `origin_data/SUP-info-2026-01/pNN.png`
> 머리글은 전 페이지 공통 「(파이썬 로고) 문제해결과 프로그래밍 / 학번: ____ 이름: ____」이며 이하 반복 표기하지 않는다.

---

## p01 — 반복문(for문)

**정의 상자**
```
for 변수 in range(시작값, 끝값, 증감값) :
    반복 실행 영역
```
- for 반복문은 변수의 값이 시작값부터 (끝값에 도달하기 전)까지 증가 또는 감소하면서 반복하는 횟수가 결정되고, 그 반복 횟수만큼 '반복 실행 영역'을 처리한다. 경우에 따라서 시작값, 증감값은 생략할 수 있다. 시작값이 생략될 경우 0부터 시작한다. 증감값이 생략될 경우 1씩 증가한다.
- 파이썬에서 for 반복문에서 반복 실행하는 영역의 문장을 탭 키 또는 스페이스 키 4개로 들여쓰기해줘야 한다.

**1) for문에서 range( )함수의 사용**

| | 형식1 | 형식2 | 형식3 |
|---|---|---|---|
| 형식 | `for 변수 in range(끝값):` / 반복 실행 영역 | `for 변수 in range(시작값, 끝값):` / 반복 실행 영역 | `for 변수 in range(시작값,끝값,증감값):` / 반복 실행 영역 |
| 설명 | 0부터 '끝값에 도달하기 전'까지의 수를 1씩 증가하면서 반복 실행 영역을 실행한다. | 시작값부터 '끝값에 도달하기 전까지의 수를 1씩 증가하면서 반복 실행 영역을 실행한다. | 시작값부터 '끝값에 도달하기 전'까지의 수를 1씩 증감값만큼 증가하거나 감소하면서 반복 실행 영역을 실행한다. |
| 예 | `for i in range(10):` / `print(i)` | `for i in range(1, 10):` / `print(i)` | `for i in range(1, 10, 2):` / `print(i)` |

| 제목 | 코드 | 실행 결과 |
|---|---|---|
| i 값이 0에서 9까지 변하면서 10번 반복 | `for i in range(10) :` / `    print(i, end = ' ')` | `0 1 2 3 4 5 6 7 8 9` |
| i 값이 1에서 10까지 변하면서 10번 반복 | `for i in range(1, 11) :` / `    print(i, end = ' ')` | `1 2 3 4 5 6 7 8 9 10` |
| i 값이 1부터 시작하여 2씩 증가하면서 범위내에서 반복 | `for i in range(1, 10, 2) :` / `    print(i, end = ' ')` | `1 3 5 7 9` |
| i 값이 1부터 시작하여 5씩 증가하면서 범위내에서 반복 | `for i in range(1, 10, 5) :` / `    print(i, end = ' ')` | `1 6` |

**2) for문을 활용한 프로그램** (빈칸 채우기)

| 1부터 100 까지의 숫자 중 10의 배수만 출력하는 프로그램 | 1부터 10까지의 숫자를 덧셈한 결과를 출력하는 프로그램 |
|---|---|
| `for i in range( ____, ____, ____) :` / `    print(i, end=' ')` | `sum = 0` / `for i in range(1,11):` / `    sum = ______________` / `print('1부터 10까지의 합은', sum, '입니다.')` |

## p02 — 실습 1~3 (빈칸 + 추적표)

**<실습 1>** 1부터 10까지의 숫자 중 3의 배수인 값들의 합을 출력하시오.
```
sum = 0
for i in range(___ ,___ ,____) :
    sum = sum + i
print('최종 합은', sum)
```
우측: 「i와 sum값의 변화」 표 — 열 `i 값` / `sum값`, 빈 행 3개.

**<실습 2>** 1부터 10까지의 숫자 중 5의 배수인 값들의 합을 출력하시오.
```
sum = 0
for i in range(___ ,___ ,____) :
    sum = sum + i
print('최종 합은', sum)
```
우측: 「i와 sum값의 변화」 표 — 열 `i 값` / `sum값`, 빈 행 3개.

**<실습 3>** 1부터 5까지의 숫자를 모두 곱한 값을 출력하시오
```
factorial = 1
for i in range(___ ,___) :
    factorial = factorial * i
print('최종 곱은', factorial)
```
우측: 「i와 factorial값의 변화」 표 — 열 `i 값` / `factorial 값`, 빈 행 5개.

## p03 — 함수

- **함수** : 정의된 기능만을 전담하여 처리하는 독립된 작은 부속 프로그램
  : 각각의 함수는 고유한 이름과 기능을 가짐.
  : 함수의 이름을 호출하는 것만으로 그 함수가 가진 기능을 실행할 수 있음.

| 함수 정의 방법 | 함수 호출 방법 |
|---|---|
| `def 함수명(매개변수) :` / `    명령문1` / `    명령문2` / `    ...` / `    명령문k` / `    return 반환값` | `함수명(인수)` |
| `def f(x) :`  #f(x) = 2x + 1 함수 정의 / `    y = 2*x + 1` / `    return y` | `result = f(3)`  #3을 인수로 사용하여 함수 f를 호출 / `print(result)` |

- 'def 함수명( ):' 을 정의할 때 괄호를 닫지 않거나 문장 끝에 콜론(:)을 빠트리면 오류가 발생한다.
- 매개 변수, 반환값, 인수는 불필요한 경우 생략할 수 있다.
- **인수**: 함수를 호출할 때 넘겨주는 값
- **매개 변수**: 인수를 전달받기 위해 사용하는 변수
- **반환값**: 함수를 처리한 결과를 호출한 쪽으로 되돌려주는 값

**<삼각형의 넓이를 구하는 프로그램:**
```
def triangle(w, h) :          # triangle 함수 정의
    t = (w*h)/2               # 밑변과 높이의 값을 받아서 넓이 계산
    return t                  # 계산 결과를 반환

width = int(input('삼각형의 밑변: '))
height = int(input('삼각형의 높이: '))
area = triangle(width, height)   # triangle() 함수를 호출하고, 매개 변수 전달
print('삼각형의 넓이: ', area)
```

**<위 코드 설명>**

| 항목 | 설명 |
|---|---|
| def | define의 줄임말로, 함수를 만들기 위해 사용하는 파이썬 명령어이다. |
| triangle | 새로 만드는 함수의 이름이다. |
| w, h | 함수가 계산에 사용할 수 있도록 넘겨주는 자료로, **매개 변수**라고 한다. |
| t = (w*h)/2 | 매개 변수로 받은 w와 h를 이용해서 삼각형의 넓이를 구하고, 그 결과를 변수 t에 저장한다. |
| return t | 변수 t에 들어 있는 값을 원래의 위치에 되돌려 주는 것으로, '반환값'이라고 한다. |
| area = triangle(width, height) | triangle( ) 함수를 호출해서 기능을 실행한다. input( )을 통해 사용자로부터 입력받은 width와 height의 값을 triangle( ) 함수에게 매개 변수로 넘겨주고, 계산된 결과를 반환값으로 받아서 변수 area에 저장한다. |

※ 함수의 특징
1. 복잡하고 큰 프로그램을 작은 단위의 여러 부분 프로그램으로 나눌 수 있다. 2. 프로그램을 기능 중심으로 단순하고 이해하기 쉽게 표현할 수 있다. 3. 중복되는 부분을 함수로 만들어 반복 호출함으로써 코드의 불필요한 중복을 최소화할 수 있다. 4. 프로그램의 크기를 줄일 수 있고 오류 발생 시 수정하기가 용이하다. 5. 함수를 재사용함으로써 프로그래밍의 생산성을 높일 수 있다.

## p04 — 함수 호출 사례

**<매개 변수가 없는 함수 호출>**

| | 좌 | 우 |
|---|---|---|
| 코드 | `def hello( ) :`  #함수 정의 / `    print('안녕하세요? 반갑습니다.')` / (빈 줄) / `hello( )`  #함수 호출 | `def hello( ) :`  #함수 정의 / `    print('안녕하세요? 반갑습니다.')` / (빈 줄) / `for i in range(5):` / `    hello( )`  #함수 호출 |
| 실행 결과 | `안녕하세요? 반갑습니다.` | `안녕하세요? 반갑습니다.` 5행 반복 |

**<두 수의 합계 프로그램 & 세 과목 평균을 구하는 프로그램>**

| | 두 수의 합계를 구하는 프로그램 | 세 과목 점수를 입력받아 평균을 구하는 프로그램 |
|---|---|---|
| 코드 | `def sum(a, b) :`  #함수 정의 / `    return a + b` / (빈 줄) / `result = sum(10, 5)`  #함수 호출 / `print('합계: ', result)` | `def avg(k, e, m) :`  #함수 정의 / `    average = (k+e+m)/3` / `    return average` / (빈 줄) / `kor = int(input('국어 점수 입력: '))` / `eng = int(input('영어 점수 입력: '))` / `math = int(input('수학 점수 입력: '))` / `result = avg(kor, eng, math)`  #함수 호출 / `print('평균: ', result)` |
| 실행 결과 | (빈칸) | `국어 점수 입력: 98` / `영어 점수 입력: 90` / `수학 점수 입력: 85` |

**<1부터 n까지의 합 & 1부터 n까지의 곱>**

| | 1부터 n까지의 합 | 1부터 n까지의 곱 |
|---|---|---|
| 코드 | `# n까지의 합 구하기` / `def sum(n) :`  #함수 정의 / `    sum = 0` / `    for i in range(1, n+1):` / `        sum = sum + i` / `    return sum` / (빈 줄) / `a = int(input('1부터 얼마까지의 합을 구할까요?'))` / `result = ____________`  #함수 호출 / `print('1부터', a, '까지의 합은: ', result)` | `# n! 구하기` / `def factorial(n) :`  #함수 정의 / `    fact = 1` / `    for i in range(1, n+1):` / `        fact = fact*i` / `    return fact` / (빈 줄) / `a = int(input('1부터 얼마까지의 곱을 구할까요?'))` / `result = _____________`  #함수 호출 / `print('1부터', a, '까지의 곱은: ', result)` |
| 실행 결과 | `1부터 얼마까지의 합을 구할까요?10` / `1부터 10 까지의 합은:  55` | `1부터 얼마까지의 곱을 구할까요?5` / `1부터 5 까지의 곱은:  120` |

## p05 — 지역변수/전역변수, 재귀함수 도입

> 이 페이지의 표 제목은 p04와 같은 「<1부터 n까지의 합 & 1부터 n까지의 곱>」으로 인쇄돼 있으나 표 내용은 지역변수/전역변수다. **원문 그대로 옮긴다** — 제목-내용 불일치는 원본의 상태다.

| | 지역변수 | 전역변수 |
|---|---|---|
| 설명 | 함수 안에서 만들어지고, 그 함수 안에서만 사용할 수 있는 변수 / (빈 줄) / `def hello():` / `    name = "철수"` / `    print(name)` / (빈 줄) / `hello()` | 전역변수 - 함수 밖에서 만들어진 변수 / 전역변수의 값을 함수 안에서 직접 변경하고 싶다면 global을 사용 / (빈 줄) / `score = 10` / `def change():` / `    global score` / `    score = 20` / (빈 줄) / `change()` / `print(score)` |
| 실행 결과 | (빈칸) | (빈칸) |

**재귀함수 : 어떤 함수 안에서 자기 자신을 부르는 것**

특정 조건이 되면 자신을 호출하지 않고 멈추도록 설계되어야만 함

**<첫 번째 재귀함수 코드>**
```
def fact(n):
 if n<=1 :
      return 1
 return n*fact(n-1)

print(fact(1))
print(fact(5))
```

## p06 — 재귀함수 코드 2~4

**<두 번째 재귀함수 코드>**
```
def abc(n):
    if n == 1:
        return 1
    return n + abc(n - 1)

print(abc(5))
print(abc(10))
```

**재귀 함수의 핵심: "줄여가다가 언젠가는 끝나야 한다"**

**위 코드에서는 n == 1이 종료 조건**

----------------------------------------

**<세 번째 재귀함수 코드>**
```
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

print(fibo(6))
```

----------------------------------------

**<네 번째 재귀함수 코드>**
```
def list_sum(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + list_sum(lst[1:])

print(list_sum([1, 2, 3, 4, 5]))
```

## p07 — Quiz 1~4

> 전 문항 공통 발문: "다음 파이썬 코드를 보고 결과를 써 보세요." / 답란 「결과 : ____」

**Quiz 1**
```
s = 0

for i in range(1, 6):
    if i % 2 == 0:
        s += i

print(s)
```

**Quiz 2**
```
s = 0

for i in range(5):
    for j in range(i):
        s += 1
print(s)
```

**Quiz 3**
```
for i in range(1, 4):
    for j in range(1, 4):
        if i + j == 4:
            print(i, j)
```

**Quiz 4**
```
s = 0
for i in range(1, 6):
    if i % 2 == 0 :
        s += i
    else:
        s -= i
print(s)
```

## p08 — Quiz 5~8 (발문·답란 동일)

**Quiz 5**
```
a = [[1, 2], [3, 4]]

for r in a:
    for x in r:
        if x > 2:
            print(x)
```

**Quiz 6**
```
a = [[10, 20], [30, 40]]
s = 0
for i in range(2):
    for j in range(2):
        if i == j:
            s += a[i][j]
print(s)
```

**Quiz 7**
```
a = [[1, 2], [3, 4]]
for i in range(2):
    for j in range(2):
        if i < j:
            a[i][j] *= 10
print(a)
```

**Quiz 8**
```
def f(x):
    return x * 2

print(f(3) + f(4))
```

## p09 — Quiz 9~11 (발문·답란 동일)

**Quiz 9**
```
def f(x):
    s = 0

    for n in x:
        if n > 10:
            s += n
    return s

print(f([5, 15, 20]))
```

**Quiz 10**
```
a = [[1, 2], [3, 4]]

def f(x):
    s = 0

    for r in x:
        for n in r:
            if n % 2 == 0:
                s += n

    return s

print(f(a))
```

**Quiz 11**
```
def func(n):
    if n <= 0:
        return
    print(n, end="")
    func(n - 1)
    print(n, end="")

func(3)
```

## p10 — Quiz 12~14 (발문·답란 동일)

**Quiz 12**
```
def reverse_str(s):
    if len(s) <= 1:
        return s
    return reverse_str(s[1:]) + s[0]

print(reverse_str("python"))
```

**Quiz 13**
```
def power(a, b):
    if b == 1:
        return a
    return a * power(a, b - 1)

print(power(3, 4))
```

**Quiz 14 (고난이도)**
```
def count_down(n):
    acc = []
    def helper(n):
        if n <= 0:
            return acc
        acc.append(n)
        return helper(n - 1)
    return helper(n)

print(count_down(3))
```
