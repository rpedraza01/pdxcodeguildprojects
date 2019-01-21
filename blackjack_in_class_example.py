#blackjack_in_class_example.py
from blackjack_deck_example import Card, Deck
# lines 4 - 9 are print tests to check if the file and class import works
# deck = Deck()
# print(deck)
# deck.shuffle()
# card = deck.draw()
# print(card)
# print(len(deck))

class Hand:
    def __init__(self, card1, card2):
        self.cards = [card1, card2]
        # lines 15 - 19 are equivalent to writing out a big dictionary of every card's value
        face = {key: 10 for key in "JKQ"}
        number = {key: key for key in range(2, 11)}
        self.points = {"A": 1}
        self.points.update(number)
        self.points.update(face)

    def __repr__(self):
        return str(self.cards)


    def score(self):
        # sum up cards in hand
        return sum([self.points[card.rank] for card in self.cards])
        # equivalent to comprehension on line 27
        # total = 0
        # for card in self.cards:
            # total += points[card.rank]
        # return total

    def add(self, card):
        self.cards.append(card) # or self.cards += [card]

# line 38 creates Dealer class and extends the Hand class and has all the same properties as the Hand class
class Dealer(Hand):
    def __init__(self, card1, card2):
        super().__init__(card1, card2)


    def one_face_down(self):
        # prints dealer's hand with first card hidden
        hidden = Card("Hidden", "Hidden")
        return [hidden] + self.cards[1:]
        # for i in range(1, len(self.cards)):
            # print(self.cards[i])


    def visible_score(self):
        hidden_card = self.cards[0] # dealer's first card in their hand is hidden
        print(hidden_card)
        return self.score() - self.points[hidden_card.rank]


class Game:
    def __init__(self, cut_index, num_players = 1): # arguments must go in this order with num_player = 1, the default value going last
        self.deck = Deck()
        self.deck.shuffle()
        self.deck.cut(cut_index)

        # create players
        self.players = []
        for i in range(num_players):
            player = Hand(self.deck.draw(), self.deck.draw())
            self.players.append(player)

        # create dealer
        self.dealer= Dealer(self.deck.draw(), self.deck.draw())


    def play(self):
        print("-"*48)
        print("Dealer's hand.")
        print(self.dealer.one_face_down())
        print("Dealer's score:", self.dealer.visible_score())
        print("-"*48)

        for i, player in enumerate(self.players):
            print("-"*48)
            print(f"Player {i}'s turn")
            print(f"Score: {player.score()}")
            print("-"*48)
            print(player) # displays player's hand
            while player.score() < 21: # loop while player is hitting
                while True:
                    move = input("Hit or stay: ").strip().lower()
                    if move in ["hit", "h", "stay", "s"]:
                        break
                if move.startswith("h"):
                    player.add(self.deck.draw())
                    print(player)
                else:
                    break
            if player.score() > 21:
                print("PLayer is Busted")
            elif player.score() == 21:
                print("Player has Blackjack!")

        # dealer's move
        print("-"*48)
        print("Dealer's turn.")
        print("-"*48)
        dealer_score = self.dealer.score()
        print(self.dealer.one_face_down())
        while self.dealer.score() < 17:
                #dealer hits
                print("Dealer hits!")
                self.dealer.add(self.deck.draw())
                print(self.dealer.one_face_down())
        if dealer_score < 21:
            print("Dealer stays!")
        elif dealer_score == 21:
            print("Dealer has Blackjack!")
        else:
            print("Dealer is Busted!")

        print("-"*48)
        print("Dealer's final hand.")
        print("-"*48)
        print(self.dealer)
        print("Dealer's score:", self.dealer.score())

        for i, player in enumerate(self.players):
            print("-"*48)
            print(f"Player {i}'s hand")
            print(player)
            print(f"Score: {player.score()}")
            print("-"*48)
            if (player.score() > 21) or player.score() <= self.dealer.score() <= 21:
                print(f"Player {i} loses!")
            else:
                print(f"Player {i} wins!")


blackjack = Game(1)
blackjack.play()

# # tests
# deck = Deck()
# # deck.shuffle()
# hand = Hand(deck.draw(), deck.draw())
# print(hand)
# print(hand.score())
# dealer = Dealer(deck.draw(), deck.draw())
# # line 62 is equivalent to lines 64 and 65
# # card1 = deck.draw()
# # card2 = deck.draw()
# print(dealer)
# print(dealer.one_face_down())
# print(dealer.visible_score())
# blackjack = Game(26)
# print(blackjack.deck)
# print(blackjack.players)
# for player in blackjack.players:
#     print(player.score())
# print(blackjack.dealer.one_face_down())
# print(blackjack.dealer.visible_score())
# print(blackjack.dealer)
# print(blackjack.dealer.score())


##################################################################################
##################################################################################


from blackjack_deck_example import Card, Deck
class Hand:
    """
    represents a player's hand in blackjack
    """
    def __init__(self, card1, card2):
        """
        initializes Hand object with two cards
        """
        self.cards = [card1, card2]
        # self.points = {'A': 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 10, 'Q': 10, 'K': 10}
        # equivalent to above
        face = {k: 10 for k in 'JQK'}
        number = {k:k for k in range(2,11)}
        self.points = {'A': 1}
        self.points.update(number)
        self.points.update(face)

    def __repr__(self):
        """
        returns string representation of Hand
        """
        return str(self.cards)

    def score(self):
        """
        returns total of points in hand
        """
        return sum([self.points[card.rank] for card in self.cards])

        # # equivalent to comprehension above
        # total = 0
        # for card in self.cards:
        #   total += self.points[card.rank]
        # return total

    def add(self, card):
        """
        adds card to hand
        """
        self.cards.append(card)


class Dealer(Hand):
    """
    Dealer extends Hand
    """
    def __init__(self, card1, card2):
        super().__init__(card1, card2)

    def one_face_down(self):
        """
        prints dealer's hand with first card hidden
        """ 
        hidden = Card('Hidden', 'Hidden')
        return [hidden] + self.cards[1:]

        # for i in range(1, len(self.cards)):
        #     print(self.cards[i])

    def visible_score(self):
        # self.points = {'A': 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 10, 'Q': 10, 'K': 10}
        hidden_card = self.cards[0]
        return self.score() - self.points[hidden_card.rank]


class Game:
    def __init__(self, cut_index, num_players=1):
        """
        initialize Game object with the following properties:
        :deck: Deck object, shuffled and cut with the cut_index
        :players: list of Hand objects
        :dealer: Dealer object
        """
        # set up deck
        self.deck = Deck()
        self.deck.shuffle()
        self.deck.cut(cut_index)

        # create player hands
        self.players = []
        for i in range(num_players):
            # fill player hand with two cards drawn from the game's deck
            player = Hand(self.deck.draw(), self.deck.draw())
            self.players.append(player)

        # create dealer
        # fill dealer hand with two cards drawn from the game's deck
        self.dealer = Dealer(self.deck.draw(), self.deck.draw())


    def play(self):
        """
        Game logic
        """
        # display player's visible cards and visible score
        print('-'*48)
        print("Dealer's hand")
        print(self.dealer.one_face_down())
        print("Dealer's score:", self.dealer.visible_score())
        print('-'*48)

        # loop through players
        for i, player in enumerate(self.players):
            print('-'*48)
            print(f"Player {i+1}'s turn")
            print(player) # display player's hand
            print(f"Score: {player.score()}")
            print('-'*48)
            while player.score() < 21: # loop while player is hitting and not blackjack or busted
                while True: # input validation
                    move = input('Hit or stay: ').strip().lower()
                    if move in ['hit', 'h', 'stay', 's']:
                        break
                # if the player hits, draw from the deck and add a card to their hand
                if move.startswith('h'):
                    player.add(self.deck.draw())
                    print(player) 
                else: # if the player stays, stop asking for another move
                    break
            if player.score() > 21:
                print('Player busted')
            elif player.score() == 21:
                print('Blackjack!')

        # dealer's move
        print('-'*48)
        print("Dealer's turn")
        print('-'*48)
        print(self.dealer.one_face_down())
        # dealer hits if their score < 17
        while self.dealer.score() < 17:
            print('Dealer hits')
            # draw a card from the deck and add it to the dealer's hand
            self.dealer.add(self.deck.draw())
            print(self.dealer.one_face_down())
        # stay if 17 <= score < 21
        if self.dealer.score() < 21:
            print('Dealer stays!')
        # blackjack
        elif self.dealer.score() == 21:
            print('Blackjack!')
        # busted
        else:
            print('Dealer busted!')

        # reveal dealer's full hand
        print('-'*48)
        print("Dealer's final hand")
        print('-'*48)
        print(self.dealer)
        print("Dealer's score:", self.dealer.score())

        # calculate winner(s)
        for i, player in enumerate(self.players):
            print('-'*48)
            print(f"Player {i+1}'s hand")
            print(player)            
            print(f"Score: {player.score()}")
            print('-'*48)
            # player loses if they busted or if their score is less than the dealer's
            if (player.score() > 21) or player.score() <= self.dealer.score() <= 21:
                print(f'Player {i+1} loses :(')
            else:
                print(f'Player {i+1} wins!')


if __name__ == '__main__':
    print('-'*48)
    print("Welcome to Blackjack!")
    print('-'*48)

    while True: # input validation
        try:
            players = int(input('How many players: '))
            break
        except ValueError:
            pass

    while True: # loop game
        while True: # input validation
            try:
                cut = int(input("Cut the deck: "))
                break
                # if 0 <= cut < 52:
                #     break
                # raise ValueError
            except ValueError:
                print('Enter a number to cut the deck by.')

        # create Game object
        blackjack = Game(cut, players)
        blackjack.play()

        # ask if user wants to play again 
        while True: # input validation
            play_again = input('Do you want to play again: ').strip().lower()
            if play_again in ['y', 'yes', 'n', 'no']:
                break
        if play_again.startswith('n'):
            print('Goodbye!')
            break