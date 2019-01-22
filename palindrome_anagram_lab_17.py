#palindrome_anagram_lab_17.py

def check_palindrome(palindrome):
    # palindrome = input("What is the word you wish to check is a palindrome? > ")
    palindrome = palindrome.lower()
    palindrome = palindrome.replace(" ", "")
    palindrome_list = list(palindrome) 
    palindrome_list_reverse = reversed(palindrome_list)
    # palindrome_list.reverse()
    if "".join(palindrome_list) == "".join(palindrome_list_reverse):
        print("That's a palindrome.")
    else:
        print("That's not a palindrome.")


def check_anagram(first_word, second_word):
    # first_word = input("What's your first word? > ")
    # second_word = input("What's your second word? > ")
    first_word = first_word.lower()
    second_word = second_word.lower()
    first_word = first_word.replace(" ", "")
    second_word = second_word.replace(" ", "")
    first_list = list(first_word)
    second_list = list(second_word)
    first_list.sort()
    second_list.sort()
    if first_list == second_list:
        print("That's an anagram.")
    else:
        print("That's not an anagram.")

palindrome = input("What is the word you wish to check is a palindrome? > ")
check_palindrome(palindrome)


first_word = input("What's your first word? > ")
second_word = input("What's your second word? > ")
check_anagram(first_word, second_word)