#magic_8_ball_lab_04_v2.py
while True:
    print("Greetings mortal and welcome to the MIGHTY MAGIC EIGHT BALL!")
    question = input("Ask me a question, if you dare. > ")
    import random
    predictions_list = ["Yes", "No", "Maybe so.", "Better luck next time.", "Try again.", "Yes, I can see that happening.", "Fugghetaboutit!", "Zzzzzzt ERROR! Uhhh, I think you broke it.", "For sure dude!", "Nah fam, not this time.", "Fuck it, why not?"]
    answer = random.choice(predictions_list)
    print(answer)
    exit = input("Would you like to ask the MIGHTY MAGIC EIGHT BALL ANOTHER QUESTION? > ")
    if exit != "yes":
        break
