import random

class Card:
    """ A class to describe cards in a pack """
    def __init__(self, number):
        self._card_number = number

    def get_suit(self):
        self._suit = self._card_number // 13
        suits = ['S', 'H', 'D', 'C']
        return suits[self._suit]
    
    def get_value(self):
        self._value = self._card_number % 13
        if self._value == 0:
            return "A"
        elif self._value >= 1 and self._value <= 9:
            return str(self._value + 1)
        elif self._value == 10:
            return "J"
        elif self._value == 11:
            return "Q"
        elif self._value == 12:
            return "K"

    def get_short_name(self):
        """ return card name eg '10D' '8C' 'AH' """
        return self.get_value() + self.get_suit()

    def get_long_name(self):
        names = {
            "A" : "Ace",
            "2" : "Two",
            "3" : "Three",
            "4" : "Four",
            "5" : "Five",
            "6" : "Six",
            "7" : "Seven",
            "8" : "Eight",
            "9" : "Nine",
            "10" : "Ten",
            "J" : "Jack",
            "Q" : "Queen",
            "K" : "King",

            "S" : "Spades",
            "H" : "Hearts",
            "D" : "Diamonds",
            "C" : "Clubs"
        }

        return f"{names[self.get_value()]} of {names[self.get_suit()]}"

    def __eq__(self, other):
        if self.get_value() == other.get_value() and self.get_suit() == other.get_suit():
            return True
        return False

class Deck:
    """ A class to contain a pack of cards with methods for shuffling, adding or removing cards etc. """
    def __init__(self):
        self._card_list = []
        for i in range(52):
            self._card_list.append(Card(i))

    def length(self):
        return len(self._card_list)

    def shuffle_deck(self):
        """ shuffles the cards """
        random.shuffle(self._card_list)

    def take_top_card(self):
        return self._card_list.pop()
    
    def __contains__(self, other):
        for i in self._card_list: 
            if i == other: return True 
        return False

            




deck = Deck()
deck.shuffle_deck()

for _ in range(deck.length()):
    card = deck.take_top_card()
    print(card.get_long_name())