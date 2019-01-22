#number_to_phrase_lab_15.py
# lines 3 - 5 are dictionaries with keys of an integer and values of strings of the numbers spelled out
tens_dict = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
ones_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
teens_dict = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
# line 7 creates the variable of number_input and asks the user for an integer input
number_input = int(input("What number do you wish to wordify? > "))
# line 9 creates the variable of number_word which is set to an empty list so it can later be modified
number_word = []
# line 11 is the beginning of the while loop
while number_input > 0:
    # checks if the number_input is greater than 99, if so then it runs through the if statement
    if number_input > 99:
        # the variable hundred is created by using float division on number_input to remove the hundreds spot from a 3 digit number
        hundred = number_input // 100
        # the empty list number_word is appeneded with the ones_dict and the variable hundred and the string " hundred"
        number_word.append(ones_dict[hundred] + " hundred")
        # number_input is then modified by % 100 to get any remainder which will then take the number back to the beginning of the loop and proceed to the first elif
        number_input = number_input % 100
    # if number_input is greater than or equal to 20 it runs through the elif statement
    elif number_input >= 20:
        # the variable tens is created by using float division on number_input to remove the tens spot
        tens = number_input // 10
        # the list number_word is then appended with the tens_dict and the variable tens
        number_word.append(tens_dict[tens])
        # number_input is then modified by % 10 get any remainder which will then take the number back to the beginning of the loop and proceed to the next elif
        number_input = number_input % 10
    # checks if number_input is greater than 9
    elif number_input > 9:
        # the list number_word is then appended with teens_dict and number_input
        number_word.append(teens_dict[number_input])
        # the loop breaks if a number meets all of the if/elif statements and there's no remainder by this line
        break
    # checks to see if number_input is greater than 0
    elif number_input > 0:
        # the list number_word is appended with the ones_dict and number_input
        number_word.append(ones_dict[number_input])
        # if all if/elif statements are met then the loop breaks
        break

# prints out the now heavily modified list number_word and joins it with the string " " so that each word is separated by a space and is more readable by the user.
print(" ".join(number_word))