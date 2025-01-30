import re
import reprlib

RE_WORD = re.compile(r'\w+')

class Sentence:
    """ yq """
    def __init__(self, text: str):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return f"Sentence({reprlib.repr(self.text)})"

    def __iter__(self):
        return SentenceIterator(self.words)

class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except:
            raise StopIteration()
        self.index += 1
        return word
    
    def __iter__(self):
        return self

s = Sentence('"The time has come, " the Warlus said, ')

for word in s:
    print(word)

print(list(s))