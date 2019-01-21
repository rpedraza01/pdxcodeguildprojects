#blackjack_deck_example.py
import random
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"Card({self.rank}, {self.suit})"

    def __eq__(self, card):
        return self.rank == card.rank


# tests
# card1 = Card(2, "Spades")
# card2 = Card(2, "Hearts")
# print(card1, "=", card2, card1 == card2)
                         # card1.__eq__(card2) equivalent to the above card1 == card2


class Deck:
    def __init__(self):
        ranks = ["A"] + list(range(2, 11)) + list("JQK")
        suits = ["clubs", "diamonds", "hearts", "spades"]
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        # 
        # lines 29 - 33 is equivalent to the comprehension on line 26
        # self.cards = []
        # for suit in suits:
            # for rank in ranks:
                # card = Card(rank, suit)
                # self.cards.append(card)

    def __repr__(self):
        return str(self.cards)
        # returns string representation of cards property


    def __getitem__(self, i):
        return self.cards[i]
        # returns card at index i. Allows indexing of Deck Object


    def __len__(self):
        return len(self.cards)
        # returns size of cards property. Allows Deck object to be called with len()


    def shuffle(self):
        random.shuffle(self.cards)
        # shuffles cards property in place


    def cut(self, i):
        self.cards = self.cards[i:] + self.cards[:i]
        # cuts deck at index i in place


    def draw(self):
        return self.cards.pop()
        # removes card at the top of the deck and returns it

# tests
# deck = Deck()
# str(deck) #python converts this into deck.__repr__()
# print(deck)
# deck.shuffle()
# print(deck.cards)


# deck[""]