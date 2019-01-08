#random_emoticon_generator_lab_05.py
while True:
    print("Let's see what random emoticon faces we get.")
    import random
    eyes_list = [":", ";", "B", "O"]
    nose_list = ["-", "~", "+", "^"]
    mouths_list = ["(", ")", "@", "P"]
    emoticon_count = 1
    while emoticon_count <= 5:
        random_eyes = random.choice(eyes_list)
        random_nose = random.choice(nose_list)
        random_mouth = random.choice(mouths_list)
        emoticon_face = (f"{random_eyes}{random_nose}{random_mouth}")
        print(emoticon_face)
        emoticon_count += 1
    exit = input("Would you like me to generate another five random emoticon faces? > ")
    if exit != "yes":
        break
