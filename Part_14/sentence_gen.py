import re
import reprlib

RE_WORD = re.compile(r'\w+')

class Sentence:
    """
    yield를 포함하면 genenrator 객체가 생성된다. 
    generator 객체는 반복자이며 next() 함수를 가진다. yield가 끝나면 StopIteration 예외를 발생시킨다.
    generator 반복자를 생성해주므로 이전의 SentenceIterator(sentence_iter.py)는 필요가 없어졌다. 
    """
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
    
    def __repr__(self):
        return f"Sentence({reprlib.repr(self.text)})"
    
    def __iter__(self):
        for word in self.words:
            yield word
        return

s = Sentence('"The time has come, " the Warlus said, ')

for word in s:
    print(word)

print(list(s))