#blackjack_advice_lab_19.py

print("Welcome to the Blackjack Advisor. Let's get you some wins!")
card_dict = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
card_hand = []
first_card = input("What is your first card? > ")
card_hand += first_card
second_card = input("What is your second card? > ")
card_hand += second_card
card_points = card_dict[first_card] + card_dict[second_card]
while card_points < 17:
	print(f"{card_points}, I suggest you hit.")
	card_points += card_dict[input("What is your next card? > ")]
if 21 > card_points >= 17:
	print(f"{card_points}, I advise you stay.")
elif card_points == 21:
	print(f"{card_points}, You've got Blackjack! You win!")
elif card_points > 21:
	print(f"{card_points}, You've busted. Better luck next time.")