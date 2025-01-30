# list.sort()는 객체 자신을 정렬, sorted(list)는 새로운 배열을 생성해서 반환
fruit = ['grape', 'raspberry', 'apple', 'banana']
sorted(fruit)
## fruit : ['grape', 'raspberry', 'apple', 'banana']
fruit.sort()
## fruit : ['apple', 'banana', 'grape', 'raspberry']

# bisect로 정렬된 시퀀스에 삽입 할 인덱스 알아내기
import bisect
import random

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

## {0:2d} 첫 번째에 있는 값을 2자리 정수로 표현
## {2}{0:<2d} 세 번째 값 출력 + 0번 인덱스의 값 왼쪽 정렬 후 2자리 정수로 표현
ROW_FMT = '{0:2d} @ {1:2d}     {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


print(f"DEMO: {bisect.bisect.__name__}")
print(f"haystack ->  {' '.join('%2d' % n for n in HAYSTACK)}")
demo(bisect.bisect)

print("==========")
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]

print(f"DEMO: {bisect.bisect_left.__name__}")
print(f"haystack ->  {' '.join('%2d' % n for n in HAYSTACK)}")
demo(bisect.bisect_left)

# insort(seq, item) seq를 오름차순으로 유지한 채 item을 seq에 삽입

my_list = []
print("== insort ==")
for i in range(7):
    new_item = random.randrange(14)
    bisect.insort(my_list, new_item)
    print(f'%2d -> {my_list}' % new_item)
