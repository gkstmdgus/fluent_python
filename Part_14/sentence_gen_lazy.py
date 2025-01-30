import re
import reprlib

RE_WORD = re.compile(r'\w+')

class Sentence:
    """
    기존의 generator(sentence_gen.py)는 self.words에 text의 모든 단어를 list로 저장했다. 
    lazy하게 처리하기 위해서 re.finditer()함수를 사용했다. 해당 함수는 제너레이터를 반환한다. 
    따라서 불필요한 메모리 사용을 줄일수있다. (generator는 next()호출 시 연산을 진행하기 때문) 
    """
    def __init__(self, text):
        self.text = text
    
    def __repr__(self):
        return f"Sentence({reprlib.repr(self.text)})"
    
    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()

    # generator expression 사용 (list comprehension과 비슷)
    # def __iter__(self):
    #     return (match.group() for match in RE_WORD.finditer(self.text))

s = Sentence('"The time has come, " the Warlus said, ')

for word in s:
    print(word)

print(list(s))
