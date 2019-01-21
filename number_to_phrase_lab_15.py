#number_to_phrase_lab_15.py
tens_dict = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
ones_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
teens_dict = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

number_input = int(input("What number do you wish to wordify? > "))
number_word = []
while number_input > 0:
	if number_input > 99:
		hundred = number_input // 100
		number_word.append(ones_dict[hundred] + " hundred")
		number_input = number_input % 100
	elif number_input >= 20:
		tens = number_input // 10
		number_word.append(tens_dict[tens])
		number_input = number_input % 10
	elif number_input > 9:
		number_word.append(teens_dict[number_input])
		break
	elif number_input > 0:
		number_word.append(ones_dict[number_input])
		break
	# 	if number_input > 99: 
			
	# 		print(hundred)
	# 	tens = number_input // 10
	# 	# print(tens_dict[tens])
	# 	ones = number_input % 10
	# 	print(tens_dict[tens] + "-" + ones_dict[ones])
	# elif 19 >= number_input > 9:
	# 	print(teens_dict[number_input])
	# elif number_input <= 9:
	# 	print(ones_dict[number_input])

print(" ".join(number_word))