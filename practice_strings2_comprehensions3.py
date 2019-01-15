#practice_strings2_comprehensions3.py

## Strings 2
import random
def missing_char(word):
	missing = []
	for i in range(len(word)):
		left = word[:i] # = "k"
		right = word[i + 1:] # all the letters besides the first letter "tten", removes "i"
		missing.append(left + right)
	return missing
	# return [word[:i] + word[i + 1:] for i in range(len(word))]
	# Line 11 is a comprehension that's equivalent to lines 7 - 10
	# print(missing_char("word:", word))
kitten = missing_char("kitten")
print(missing_char("kitten"))

## Comprehensions 3
def swap_keys_and_values(dictionary):
	return {k: v for (v, k) in dictionary.items()}