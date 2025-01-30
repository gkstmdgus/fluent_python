from random import randint

def d6():
    return randint(1, 6)

# 1번째 인자는 Callable object, 2번째 인자에는 StopIteration이 발동하기 위한 값 (Callable object의 return value)
d6_iter = iter(d6, 1)
# <callable_iterator object at 0x104915f90>
print(d6_iter)

# roll이 1이 나오면 StopIteration 발동
for roll in d6_iter:
    print(roll)