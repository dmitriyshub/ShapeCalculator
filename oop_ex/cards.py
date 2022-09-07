import random


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print('{} of {}'.format(self.value, self.suit))


card = Card('Card', 6)
card.show()


class Deck:

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for shape in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for card in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
                self.cards.append(Card(shape, card))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i] , self.cards[r] = self.cards[r] , self.cards[i]

    def draw(self):

        return self.cards.pop()

def main():
    deck = Deck()
    deck.shuffle()
    deck.show()
    print("------")
    card = deck.draw()
    card.show()
    print("------")
    card = deck.draw()
    card.show()
    print("------")
    card = deck.draw()
    card.show()
    print("------")
    card = deck.draw()
    card.show()
    print("------")
    deck.show()

if __name__ == "__main__":
    main()