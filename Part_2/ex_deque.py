# # 양방향 큐
# # 양쪽 끝에 추가하거나 제거하는 연산에 특화, 중간에 추가/제거는 불리
from collections import deque

dq = deque(range(10), maxlen=10)
# deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.rotate(3)
# deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
dq.rotate(-4)
# deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)
dq.appendleft(-1)
# deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
dq.extend([11, 22, 33])
# deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)
dq.extendleft([10, 20, 30, 40])
# deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)

