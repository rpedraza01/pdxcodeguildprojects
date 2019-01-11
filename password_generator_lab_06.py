#password_generator_lab_06.py
while True:
    print("Welcome to the password generator. Let's get you a new password.")
    import random
    import string
    lowercase_length = int(input("How many lowercase letters would you like in your password? > "))
    lowercase = ""
    for number in range(0, int(lowercase_length)):
        lowercase += random.choice(string.ascii_lowercase)
    uppercase_length = int(input("How many uppercase letters would you like in your password? > "))
    uppercase = ""
    for number in range(0, int(uppercase_length)):
        uppercase += random.choice(string.ascii_uppercase)
    digits_length = int(input("How many digits would you like in your password? > "))
    digits = ""
    for number in range(0, int(digits_length)):
        digits += random.choice(string.digits)
    punctuation_length = int(input("How many punctuations would you like in your password? > "))
    punctuation = ""
    for number in range(0, int(punctuation_length)):
        punctuation += random.choice(string.punctuation)
    #length_total = int(input("How many characters would you like your password to be? > "))
    password_length = lowercase_length + uppercase_length + digits_length + punctuation_length
    password = ""
    #list(lowercase + uppercase + digits + punctuation)
    password_to_list = list(lowercase + uppercase + digits + punctuation)
    # print(password_to_list) to check if previous line works
    random.shuffle(password_to_list)
    #print(password_to_list) to check if previous line works
    list_to_password = "".join(password_to_list)
    print(list_to_password)
    exit = input("Would like to generate another password? > ")
    if exit != "yes":
        break
