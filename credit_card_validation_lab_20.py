#credit_card_validation_lab_20.py

print("Let's validate your credit card.")
def cc_check(user_cc):
	user_cc = input("Please enter your credit card number. > ")
	print(map(int, user_cc.split(",")))
	user_cc[0: -1]
	print(user_cc)
	user_cc_reversed = user_cc.reverse()
