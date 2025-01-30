# 빗변 길이 계산
from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 객체를 문자열로 표현할 때 (print)
    ## __str__()메서드는 str()의 구현체
    ## 둘 중 하나만 구현하려면 __repr__()구현.
    ## 파이썬 인터프리터는 __str__()이 구현되어 있지 않으면 __repr__()를 사용하기 때문. str()도 작동함.
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return "test"

v1 = Vector(2, 4)
v2 = Vector(2, 1)

v = v1 + v2
print(v)

abs_v = abs(v)
print(abs_v)

v_3 = v * 3
print(v_3)

print(str(v_3))
