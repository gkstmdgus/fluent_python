"""
코루틴을 사용하는 예제. 데커레이터를 이용해서 next() 호출을 피할수있다.
yield from을 사용하는 경우, 자체적으로 제너레이터를 가동하므로(next()를 자체적으로 호출함.) 해당 데커레이터는 사용 불가
"""
from functools import wraps
from collections import namedtuple

Result = namedtuple('Result', 'count average')

def coroutine(funcs):
    @wraps(funcs)
    def wrapper(*args, **kwargs):
        coro = funcs(*args, **kwargs)
        next(coro)
        return coro
    return wrapper

@coroutine
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

coro = averager()

# 10
print(coro.send(10))
# 20
print(coro.send(30))
# 15
print(coro.send(5))

try:
    coro.send(None)
    # next(coro)
except StopIteration as e:
    result = e.value
    
# Result(count=3, average=15.0)
print(result)
    