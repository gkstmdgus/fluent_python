# # 리스트 복사
# board = [['_'] * 3 for i in range(3)]
# board[1][2] = 'X'
# print(board)
#
# # same
# board = []
# for i in range(3):
#     row = ['_'] * 3
#     board.append(row)
#
#
# # 잘못된 예
# # 내부 리스트를 곱하면 참조 값이 복사가 됨.
# board = [['_'] * 3] * 3
# board[1][2] = 'X'
# print(board)
#
# # same
# row = ['_'] * 3
# board = []
# for i in range(3):
#     board.append(row)

t = (1,2, [30, 40])
print(id(t))
print(id(t[2]))
try:
    # t[2].extend([50, 60])
    t[2] = [30,50]
except Exception as e:
    print(str(e))
print(t)
print(id(t))
print(id(t[2]))