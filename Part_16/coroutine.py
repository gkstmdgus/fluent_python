"""
기본 generator에서 인자를 넘길 수 있는 send() API가 추가되었다. 
호출자로부터 데이터를 받으면서 호출자와 협업하는 프로시저인 코루틴이 된다. 
send() 함수 이외에도 close(), throw()메서드도 추가되었다. 

inspect.getgeneratorstate() 함수로 상태 확인 가능 
GEN_CREATED, GEN_SUSPENDED, GEN_RUNNING, GEN_CLOSED
"""

import inspect
import time

def simple_coroutine():
    print("-> coroutine started")
    x = yield   # send()로 넘어온 인자가 x로 대입된다. 
    time.sleep(3)
    print(f"-> coroutine received: {x}")

# <generator object simple_coroutine at 0x102ecc110>
my_coro = simple_coroutine()

## GEN_CREATED
print(inspect.getgeneratorstate(my_coro))

# generator 실행 
# -> coroutine started
next(my_coro)

## GEN_SUSPENDED
print(inspect.getgeneratorstate(my_coro))

# -> coroutine received: 42 
# raise StopIteration
try:
    my_coro.send(42)
except StopIteration:
    pass

## GET_CLOSED
print(inspect.getgeneratorstate(my_coro))