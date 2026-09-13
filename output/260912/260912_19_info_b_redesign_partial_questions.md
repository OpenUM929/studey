---
title: 정보 B형 최상위 사고력 재설계 — 부분 작성 후보
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

# 정보 B형 — 최상위 사고력 재설계 부분 후보

> ⚠️ 범위 미확정 · 미배포 · 현재 4/25문항. 전체 25문항 완성본이 아닙니다.
> 목표는 문항별 최상위+필수 사고력이며 **달성·정식 Tier는 미확정**입니다. 4점이라는 배점을 난도 근거로 쓰지 않습니다.
> 기존 2라운드의 재설계이며 기존 후보·감사·revision4를 보존합니다. 정식 세트ID는 발급하지 않습니다.

기존 슬롯 번호를 유지합니다. 각 문항 4점, 현재 부분 합계 16점이며 전체 목표는 25문항·100점입니다.
문제에 제시된 파이썬3 코드의 실행 의미를 사용합니다. 임의 입력 전수 열거가 아니라 답이 결정되는 과정을 쓰시오.
함수 사용은 학습지 근거이며 올해 공식 시험범위 확정을 의미하지 않습니다.

## 서답형

**7.** 승인과 환급을 함께 고려한 초기 재고 (4점)

```python
def run(stock, jobs):
    accepted = []
    for row in jobs:
        if stock >= row[1]:
            stock -= row[1]
            stock += row[2]
            accepted.append(row[0])
    return [stock, accepted]
```

작업은 E=["E",20,19], B=["B",17,15], C=["C",25,13],
A=["A",9,5], D=["D",8,4]이다. 각 행은 [이름, 승인에 필요한 재고, 승인 직후 환급량]이다.
다섯 작업을 각각 한 번씩 원하는 순서로 넣는다. 거절된 작업에는 환급이 없고 재시도도 없다.
다섯 작업이 모두 승인될 수 있는 가장 작은 0 이상의 정수 초기 재고와,
그 최소 초기 재고에서 모두 승인되는 작업 순서를 모두 구하시오.
최종 재고가 음수가 아니라는 것만으로 승인 가능성을 판단하지 마시오.

[IN-06 + IN-04 + IN-09 · Tier 미확정]

---

**11.** 개선한 배정 규칙이 실패하는 매개변수 (4점)

```python
def assign(x):
    jobs = [[4,7], [6,3], [5,x], [9,4]]
    load = [0,0]
    route = []
    for row in jobs:
        left = max(load[0]+row[0], load[1])
        right = max(load[0], load[1]+row[1])
        if left <= right:
            load[0] += row[0]
            route.append(0)
        else:
            load[1] += row[1]
            route.append(1)
    return [max(load), route]
```

x는 양의 정수이다. 각 작업은 장치 0 또는 장치 1 중 한 곳에서만 처리하며,
한 행의 두 수는 각각 그 장치에 작업을 배정할 때 증가하는 부하다.
다른 장치로 옮기거나 나누지 않는다. assign은 매번 그 작업까지 처리한 뒤의 최대 부하가 작은 쪽을 고른다.
최종 최대 부하를 최소화하는 배정은 중간 단계에서 더 큰 부하를 감수해도 된다.
assign(x)의 결과가 실제로 가능한 최솟값보다 커지는 모든 x와 그때의 차이를 구하시오.
나머지 모든 양의 정수 x에서는 왜 최적임도 설명하시오.

[IN-15 + IN-22 + IN-13 + IN-04 · Tier 미확정]

---

**13.** 겹친 구간 합과 검사값으로 원자료 복원 (4점)

```python
def report(a):
    windows = []
    for i in range(len(a)-2):
        windows.append(sum(a[i:i+3]))
    weighted = 0
    for i in range(len(a)):
        weighted += (i+1)*a[i]
    return [windows, sum(a), weighted % 5]
```

a는 길이 8이고 각 원소가 1 이상 6 이하인 정수 리스트이다.
report(a)는 [[8,10,8,13,11,12],27,3]이었다. 가능한 a를 모두 구하시오.
이어서 맨 마지막 관측값 3을 읽을 수 없었다면 후보가 몇 개인지 구하고,
검사값 하나가 그 후보들을 어떻게 구별하는지 설명하시오.
겹치는 구간을 각각 독립적인 세 원소라고 취급하지 마시오.

[IN-10 + IN-06 + IN-02 + IN-09 · Tier 미확정]

---

**18.** 두 시작점의 방문 요약으로 점프표 복원 (4점)

```python
def walk(a, start):
    i = start
    count = 0
    total = 0
    while i < len(a):
        count += 1
        total += i
        i += a[i]
    return [count, total, i]
```

a는 길이 10이며 1이 다섯 개, 2가 다섯 개 들어 있다.
walk(a,0)=[7,35,10], walk(a,1)=[6,33,10]이다.
두 실행은 같은 a를 읽으며 a를 변경하지 않는다. 가능한 a를 모두 구하시오.
각 실행의 방문 목록을 먼저 구하고, 두 실행이 같은 인덱스를 방문하면 이후에는 같은 경로를 따른다는 점과,
한쪽 실행이 방문하지 않은 칸도 다른 실행에서 쓰일 수 있다는 점을 반영하시오.
total은 점프값의 합이 아니라 방문한 인덱스의 합이다.

[IN-08 + IN-09 + IN-06 · Tier 미확정]
