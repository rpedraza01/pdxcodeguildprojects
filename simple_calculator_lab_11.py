#simple_calculator_lab_11.py
while True:
    math_operations = {"+", "-", "*", "/"} # This the dictionary of math operations
    print("Let's do some math together.")
    math_operation_input = input("Please enter the math operation you would like to perform. > ") # This asks the user for the type of math they wish to do
    while True:
        # Lines 8 - 13 all have to do with ensuring the user only inputs numbers. An error message returns when a non-number is entered and loops back to asking the user to input a number
        try:
            first_number_input = float(input("What is the your first number? > "))
            second_number_input = float(input("What is your second number? > "))
            break
        except ValueError:
            print("Please enter a number.")
        # Lines 15 - 28 are involved in carrying out the acutal math depending on what operation the user inputs. The if and elifs are executed depending what is called from the math_operations dictionary.
    if math_operation_input == "+":
        output = first_number_input + second_number_input
        # sum_addition = first_number_input + second_number_input
        # print(f"{first_number_input} {math_operation_input} {second_number_input} = {sum_addition}")
    elif math_operation_input == "-":
        output = first_number_input - second_number_input
        # sum_subtraction = first_number_input - second_number_input
        # print(f"{first_number_input} {math_operation_input} {second_number_input} = {sum_subtraction}")
    elif math_operation_input == "*":
        output = first_number_input * second_number_input
        # sum_multiplication = first_number_input * second_number_input
        # print(f"{first_number_input} {math_operation_input} {second_number_input} = {sum_multiplication}")
    elif math_operation_input == "/":
        output = first_number_input / second_number_input
        # sum_division = first_number_input / second_number_input
        # print(f"{first_number_input} {math_operation_input} {second_number_input} = {sum_division}")

    print(f"{first_number_input} {math_operation_input} {second_number_input} = {output}")
    #sum_output = (first_number_input + second_number_input)
    #print(f"{first_number_input} {math_operation_input} {second_number_input} = {sum_output}")
    # Lines 36 - 38 are a simple exit string that gives the user an option to do more math or quit out of the program.
    exit = input("Would you like to do some more math? > ")
    if exit != "yes":
        break
