#magic_8_ball_lab_04.py
#print("Welcome to the Mighty Magic Eight Ball!")
while True:
    print("Welcome to the Magic Eight Ball!")
    user_question = input("Please ask the Mighty Magic Eight Ball a question, if you dare. > ")
    import random
    predictions_list = ["Absolutely, yes!", "Never in a million years.", "Sure why not!?", "Sorry, try again.", "Not gonna happen.", "Yeah, I can see that happening.", "Totally dude!", "Fuggedabowdit!!!"]
    answers = random.choice(predictions_list)
    print(answers)
    exit = input("Would you like to ask the Mighty Magic Eight Ball another question? > ")
    if exit != "yes":
        break
