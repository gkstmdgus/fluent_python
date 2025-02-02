"""
대표 제너레이터를 호출자가 초기에 호출하고 대표는 하위 제너레이터를 yield from으로 반환한다. 
그래서 호출자는 하위 제너레이터와 send() 함수를 통해서 데이터를 주고받는다. 대표 제너레이터는 파이프 역할? 
yield from을 사용하면 초기 next(gen)호출, StopIteration 예외처리를 포함하고 있다. 
"""

from collections import namedtuple

Result = namedtuple('Result', 'count average')

data = {
    "girl;kg": [10, 20, 30, 40],
    "boy;cm": [100, 110, 120, 130]
}

# 하위 제너레이터 (subgenerator)
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        if term is None:    # gen.send(None) or next(gen)
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)

# 대표 제너레이터 (delegating generator)
def grouper(results, key):
    while True:
        results[key] = yield from averager()

# 호출자 (caller)
def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            print(f"generating {key}:{value}")
            group.send(value)
        group.send(None)
    return results

print(main(data))
    