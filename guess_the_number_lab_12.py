#guess_the_number_lab_12.py
import random
print("Let's play Guess The Number.")
while True:
    computer_number = random.randint(1, 10)
    total_guesses = 0
    while True:
        #    print(number)
        #computer_choice =
        user_guess = int(input("Pick a number between 1 and 10. > "))
        total_guesses = total_guesses + 1
        if computer_number == user_guess:
            print(f"You got it, good guess! You guessed {total_guesses} times.")
            break
        elif computer_number != user_guess:
            print("Nope, try again.")
    exit = input("Would you like to play again? > ")
    if exit != "yes":
       break
