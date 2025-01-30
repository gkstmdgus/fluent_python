"""
dict와 유사한 자료형의 인터페이스를 정의하기 위해 collections.abc 모듈에서 Mapping <- MutableMapping 추상 베이스 클래스를 제공한다.

해시 테이블을 이용하므로 키 값은 해시가 가능해야 한다!

# hashable?
 수명 주기 동안
  1) 변하지 않는 해시값을 가지고 있고(__hash__() 메서드가 필요!)
  2) 다른 객체와 비교할 수 있으면 (__eq__() 메서드 필요!)
 이 객체를 hashable 이라고 한다. 동일하게 판단되는 객체는 반드시 해시값이 동일해야 한다.

 -> 파이썬이 제공하는 '불변 내장 객체'는 모두 해시 가능 : 튜플은 제외. (해시 불가능한 객체를 참조할 수도 있기 때문)
"""

# dict type 확인하기

my_dict = {}
from collections import abc
isinstance(my_dict, abc.Mapping)
## True


# dictionary 구현하기

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'two': 2, 'one': 1})
a == b == c == d == e
## True


# dict comprehension

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (82, 'South Korea')
]

country_code = {country: code for country, code in DIAL_CODES}
## {86: 'China', 91: 'India', 1: 'United States', 62: 'Indonesia', 82: 'South Korea'}
{code: country.upper() for code, country in country_code.items() if code < 66}
## {1: 'UNITED STATES', 62: 'INDONESIA'}


# 존재하지 않는 키를 setdefault()로 처리하기
## setdefault로 값을 반환 후 

alphabets_dict = {'a': ['A'], 'b': ['B'], 'd': ['D'], 'g': ['G']}
alphabets = 'abcdefg'

for a in alphabets:
    return_value = a.upper()
    if a not in alphabets_dict:
        alphabets_dict[a] = []
        alphabets_dict[a].append(return_value)
print(alphabets_dict)


alphabets_dict = {'a': ['A'], 'b': ['B'], 'd': ['D'], 'g': ['G']}
alphabets = 'abcdefg'

for a in alphabets:
    return_value = a.upper()
    (alphabets_dict.setdefault(a, []).append(return_value))
print(alphabets_dict)

# ??