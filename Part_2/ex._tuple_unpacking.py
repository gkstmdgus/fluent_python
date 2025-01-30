# # tuple unpacking
# quotient ,remainder = divmod(20, 8)
#
# # 초과 항목
# # 0 / 1 / [2, 3, 4]
# a, b, *rest = range(5)
#
# # 반복문에서도 할당 가능
# areas = [
#     ('Tokyo', 'JP', '36.933'),
#     ('Sao Paulo', 'BR', '19.649'),
#     ('Mexico City', 'MX', '20.142')
# ]
#
# for name, cc, pop in areas:
#     print(f"{name} | {cc} | {pop}")
#
# from collections import namedtuple

import numpy

a = numpy.arange(12)

a.shape = 3, 4

print(a)
print(a[2,1])
print(a[:2, 1])
