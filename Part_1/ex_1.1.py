import collections

# collceiotn.nametuple을 사용하면 메서드를 가지지 않는 일련의 속성으로 구성된 클래스를 만들 수 있다.
Card = collections.namedtuple('Card', ['rank', 'suit'])

beer_card = Card('7', 'diamonds')
print(beer_card)    # Card(rank='7', suit='diamonds', test='tt')
print(type(beer_card))  # <class '__main__.Card'>

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print(len(deck))    # __len__()
print(deck[0])      # __getitem__(0)

from random import choice
print(choice(deck))

# __getitem__()를 구현하면 반복문 구현 가능
for card in deck:
    print(card)

for card in reversed(deck):
    print(card)


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
