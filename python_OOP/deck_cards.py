

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range (1, 5):
            for card in range (1, 15):
                self.cards.append(Card(suit, card))

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        if (self.suit == 1):
            self.suit = "Spades"
            print self.suit, self.value
        if (self.suit == 2):
            self.suit = "Hearts"
            print self.suit, self.value
        if (self.suit == 3):
            self.suit = "Diamond"
            print self.suit, self.value
        if (self.suit == 4):
            self.suit = "Club"
            print self.suit, self.value

test = Deck()
