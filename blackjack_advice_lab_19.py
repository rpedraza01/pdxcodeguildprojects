#blackjack_advice_lab_19.py

print("Welcome to the Blackjack Advisor. Let's get you some wins!")
num_card_dict = {1: "A", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10"}
face_card_dict = {10: "J" or "Q" or "K"} #{key: 10 for key in "JKQ"}
card_hand = 0
first_card = int(input("What is your first card? > "))
card_hand += first_card
second_card = int(input("What is your second card? > "))
card_hand += second_card
third_card = int(input("What is your third card? > "))
card_hand += third_card
if card_hand < 17:
	print("I suggest you hit.")
elif 21 > card_hand >= 17:
	print("I advise you stay.")
elif card_hand == 21:
	print("You've got Blackjack! You win!")
elif card_hand > 21:
	print("You've busted. Better luck next time.")