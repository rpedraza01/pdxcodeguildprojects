#make_change_lab_08.py
while True:
    pennies = int(input("Please enter how many pennies you have. > "))
    dollars = pennies // 100
    #pennies = pennies % 100
    #print(f"You have the equivalent of {dollars} dollars in pennies.")
    quarters = pennies // 25
    #pennies = pennies % 25
    #print(f"You have the equivalent of {quarters} quarters in pennies.")
    dimes = pennies // 10
    #pennies = pennies % 10
    #print(f"You have the equivalent of {dimes} dimes in pennies.")
    nickels = pennies // 5
    #pennies = pennies % 5
    #print(f"You have the equivalent of {nickels} nickels in pennies.")
    print(f"You have the equivalent of {dollars} dollars, {quarters} quarters, {dimes} dimes, and {nickels} nickels.")
    #print(f"And you have {pennies} pennies remaining.")
    exit = input("Would you like to calculate how many pennies are in your dollars? > ")
    if exit != 'yes':
        break
    else:
        dollars = float(input("Please enter how many dollars you have. > "))
        dollars = round(dollars, 2)
        pennies = dollars / .01
        pennies = int(pennies)
        print(f"You have {pennies} pennies.")
    exit = input("Would you like to convert more change again? > ")
    if exit != 'yes':
        break
