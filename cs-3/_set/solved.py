import random


class Card:
    def __init__(self, number, color, shape, shading):
        self.number = number
        self.color = color
        self.shading = shading
        self.shape = shape

    def __repr__(self):
        return f"{self.number} {self.shading} {self.color} {self.shape}"


deck = []

for number in [1, 2, 3]:
    for color in ["red", "green", "purple"]:
        for shape in ["oval", "diamond", "s"]:
            for shading in ["striped", "empty", "filled"]:
                deck.append(Card(number, color, shape, shading))


def checkNum(v1, v2, v3):
    same = v1 == v2 and v1 == v3
    diff = v1 != v2 and v1 != v3 and v2 != v3
    return same or diff


random.shuffle(deck)

cards = deck[0:12]

for i, a in enumerate(cards):
    for j, b in enumerate(cards):
        for k, c in enumerate(cards):
            if (
                i < j
                and j < k
                and (
                    checkNum(a.number, b.number, c.number)
                    and checkNum(a.color, b.color, c.color)
                    and checkNum(a.shape, b.shape, c.shape)
                    and checkNum(a.shading, b.shading, c.shading)
                )
            ):
                print(a, b, c)
