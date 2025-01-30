# Generator Expression
## 튜플, 배열 등 리스트 이외의 시퀀스를 생성하기 위한 표현식. 대괄호 대신 괄호를 사용한다.

# tuple 예시
alphabets = 'ABCDEFGHIGKLNMOPQRSTUVWXYZ'
print(tuple(ord(alphabet) for alphabet in alphabets))

# ex_2.4 를 generator expression 으로 작성해보기.
## len(ranks) * len(patterns) 만큼의 list를 만들지 않음.
## for 문을 돌면서 하나씩 yield하기 때문에 list로 저장이 필요하지 않는 경우에는 메모리를 아낄 수 있음.

ranks = list('AKQ')
patterns = ["Spade", "Heart", "Diamond", "Clover"]

for result in ((rank, pattern) for rank in ranks for pattern in patterns):
    print(result)
