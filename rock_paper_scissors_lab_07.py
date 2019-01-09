#rock_paper_scissors_lab_07.py
import random
def winner(user_choice, computer_choice):
    defeats_dictionary = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if user_choice == computer_choice:
        print(f"Computer chooses {computer_choice}. It's a tie!")
    elif defeats_dictionary[user_choice] == computer_choice:
        print(f"Computer chooses {computer_choice}. Wow, you win!")
    else:
        print(f"Computer chooses {computer_choice}. Sorry, you lose!")
while True:
    print("Let's play a game of ROCK PAPER SCISSORS!")
    users_move = input("Rock, Paper, or Scissors make your choice now > ")
    computers_move = random.choice(["rock", "paper", "scissors"])
#winner is a function and it's passing the arguments of user_choice and computer_choice on to other inputs
    winner(users_move, computers_move)
    exit = input("Would you like to play again? > ")
    if exit != "yes":
        break
